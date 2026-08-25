#!/usr/bin/env python3
"""Winner-only owner/firm affinity analysis for canonical Builtgraph CSV bundles."""

import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ROLE_ALIASES = {
    "architect": {"architect", "design_architect", "architect_of_record", "designed_by"},
    "general_contractor": {"general_contractor", "gc", "construction_manager", "cm_at_risk"},
    "engineer": {
        "engineer", "structural_engineer", "mep_engineer", "civil_engineer",
        "mechanical_engineer", "electrical_engineer", "plumbing_engineer",
    },
    "subcontractor": {
        "subcontractor", "trade_contractor", "electrical_contractor",
        "plumbing_contractor", "fire_suppression_contractor", "specialty_contractor",
    },
}


def read_csv(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def parse_date(value):
    try:
        return date.fromisoformat((value or "")[:10])
    except ValueError:
        return None


def project_date(project):
    for field in ("award_date", "bid_date", "start_date", "announced_date"):
        parsed = parse_date(project.get(field))
        if parsed:
            return parsed
    return None


def role_set(role):
    canonical = role.strip().casefold()
    return ROLE_ALIASES.get(canonical, {canonical})


def recency_weight(event_date, as_of, half_life_years):
    if not event_date:
        return 1.0
    age_years = max(0.0, (as_of - event_date).days / 365.25)
    return math.exp(-math.log(2) * age_years / half_life_years)


def normalized_entropy(weights):
    positive = [value for value in weights if value > 0]
    if len(positive) <= 1:
        return 0.0
    total = sum(positive)
    entropy = -sum((value / total) * math.log(value / total) for value in positive)
    return entropy / math.log(len(positive))


def confidence_label(owner_projects, dated_share):
    if owner_projects >= 10 and dated_share >= 0.8:
        return "high"
    if owner_projects >= 4 and dated_share >= 0.5:
        return "medium"
    return "low"


def analyze(data_dir, owner_id, firm_id, role, as_of, half_life_years=5.0,
            prior_strength=2.0, sector=None, state=None):
    organizations = read_csv(data_dir / "organizations.csv")
    projects = read_csv(data_dir / "projects.csv")
    relationships = read_csv(data_dir / "relationships.csv")
    org_names = {row["organization_id"]: row.get("organization_name", row["organization_id"])
                 for row in organizations}
    if owner_id not in org_names:
        raise ValueError(f"unknown owner organization_id: {owner_id}")
    if firm_id not in org_names:
        raise ValueError(f"unknown candidate organization_id: {firm_id}")

    project_by_id = {row["project_id"]: row for row in projects}
    owners_by_project = defaultdict(set)
    selected_by_project = defaultdict(set)
    accepted_roles = role_set(role)
    excluded_future = 0
    excluded_missing_source = 0

    for rel in relationships:
        project = project_by_id.get(rel.get("project_id"))
        if not project:
            continue
        observed = parse_date(rel.get("source_date")) or parse_date(project.get("source_date"))
        if not observed:
            excluded_missing_source += 1
            continue
        if observed > as_of:
            excluded_future += 1
            continue
        effective = parse_date(rel.get("effective_date")) or project_date(project)
        if effective and effective > as_of:
            excluded_future += 1
            continue
        normalized_role = (rel.get("role") or "").strip().casefold()
        if normalized_role == "owner":
            owners_by_project[project["project_id"]].add(rel.get("organization_id"))
        if normalized_role in accepted_roles:
            selected_by_project[project["project_id"]].add(rel.get("organization_id"))

    # owner_org_id is an accepted canonical fallback when an explicit owner edge is absent.
    for project in projects:
        observed = parse_date(project.get("source_date"))
        if observed and observed <= as_of and project.get("owner_org_id"):
            owners_by_project[project["project_id"]].add(project["owner_org_id"])

    global_weights = Counter()
    owner_weights = Counter()
    owner_raw = Counter()
    owner_context_weights = Counter()
    owner_project_ids = []
    owner_dated = 0
    owner_last_selected = {}

    for project_id, firms in selected_by_project.items():
        project = project_by_id[project_id]
        event_date = project_date(project) or parse_date(project.get("source_date"))
        weight = recency_weight(event_date, as_of, half_life_years)
        for selected_firm in firms:
            global_weights[selected_firm] += weight
        if owner_id not in owners_by_project.get(project_id, set()):
            continue
        owner_project_ids.append(project_id)
        if event_date:
            owner_dated += 1
        context_match = (not sector or project.get("sector", "").casefold() == sector.casefold()) and (
            not state or project.get("state", "").casefold() == state.casefold())
        for selected_firm in firms:
            owner_weights[selected_firm] += weight
            owner_raw[selected_firm] += 1
            if context_match:
                owner_context_weights[selected_firm] += weight
            if event_date and (selected_firm not in owner_last_selected or event_date > owner_last_selected[selected_firm]):
                owner_last_selected[selected_firm] = event_date

    owner_total = sum(owner_weights.values())
    global_total = sum(global_weights.values())
    global_share = global_weights[firm_id] / global_total if global_total else 0.0
    smoothed_affinity = (owner_weights[firm_id] + prior_strength * global_share) / (
        owner_total + prior_strength) if owner_total or global_total else 0.0
    historical_share = owner_weights[firm_id] / owner_total if owner_total else 0.0
    context_total = sum(owner_context_weights.values())
    context_share = owner_context_weights[firm_id] / context_total if context_total else None

    sorted_incumbents = sorted(owner_weights.items(), key=lambda item: (-item[1], item[0]))
    top_firm_id, top_weight = sorted_incumbents[0] if sorted_incumbents else (None, 0.0)
    shares = [value / owner_total for value in owner_weights.values()] if owner_total else []
    hhi = sum(value * value for value in shares)
    entropy = normalized_entropy(owner_weights.values())
    openness = entropy * 100
    dated_share = owner_dated / len(owner_project_ids) if owner_project_ids else 0.0
    confidence = confidence_label(len(set(owner_project_ids)), dated_share)
    cold_start = owner_raw[firm_id] == 0

    if not owner_project_ids:
        assessment = "insufficient_owner_role_history"
    elif cold_start and hhi >= 0.5:
        assessment = "high_entry_risk"
    elif cold_start:
        assessment = "cold_start_owner_appears_open"
    elif top_firm_id == firm_id:
        assessment = "observed_incumbent_or_leader"
    else:
        assessment = "observed_relationship_not_leading"

    return {
        "owner_id": owner_id,
        "owner_name": org_names[owner_id],
        "candidate_firm_id": firm_id,
        "candidate_firm_name": org_names[firm_id],
        "role": role,
        "as_of": as_of.isoformat(),
        "sector_filter": sector,
        "state_filter": state,
        "model_version": "winner-only-owner-affinity-v1",
        "calibration_status": "not_a_calibrated_win_probability",
        "assessment": assessment,
        "evidence_confidence": confidence,
        "owner_role_projects": len(set(owner_project_ids)),
        "owner_distinct_selected_firms": len(owner_weights),
        "candidate_owner_selections": owner_raw[firm_id],
        "candidate_recency_weighted_selections": round(owner_weights[firm_id], 6),
        "candidate_historical_selection_share": round(historical_share, 6),
        "candidate_smoothed_affinity": round(smoothed_affinity, 6),
        "candidate_context_selection_share": None if context_share is None else round(context_share, 6),
        "candidate_global_role_share": round(global_share, 6),
        "candidate_last_selected": owner_last_selected.get(firm_id).isoformat() if owner_last_selected.get(firm_id) else None,
        "cold_start": cold_start,
        "top_incumbent_id": top_firm_id,
        "top_incumbent_name": org_names.get(top_firm_id) if top_firm_id else None,
        "top_incumbent_share": round(top_weight / owner_total, 6) if owner_total else 0.0,
        "owner_selection_hhi": round(hhi, 6),
        "owner_selection_entropy": round(entropy, 6),
        "owner_openness_index": round(openness, 1),
        "dated_history_share": round(dated_share, 6),
        "excluded_future_rows": excluded_future,
        "excluded_missing_source_date_rows": excluded_missing_source,
        "observed_incumbents": [
            {
                "organization_id": selected_firm,
                "organization_name": org_names.get(selected_firm, selected_firm),
                "selections": owner_raw[selected_firm],
                "weighted_share": round(weight / owner_total, 6) if owner_total else 0.0,
                "last_selected": owner_last_selected.get(selected_firm).isoformat()
                if owner_last_selected.get(selected_firm) else None,
            }
            for selected_firm, weight in sorted_incumbents
        ],
        "limitations": [
            "Only observed selected firms are known; unobserved firms are not treated as losers.",
            "Smoothed affinity estimates historical selection share, not proposal win probability.",
            "Results depend on organization identity resolution, role normalization, and source-date coverage.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data_dir", type=Path)
    parser.add_argument("--owner-id", required=True)
    parser.add_argument("--firm-id", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--as-of", required=True, type=date.fromisoformat)
    parser.add_argument("--sector")
    parser.add_argument("--state")
    parser.add_argument("--half-life-years", type=float, default=5.0)
    parser.add_argument("--prior-strength", type=float, default=2.0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.half_life_years <= 0:
        parser.error("--half-life-years must be positive")
    if args.prior_strength < 0:
        parser.error("--prior-strength cannot be negative")
    try:
        result = analyze(
            args.data_dir, args.owner_id, args.firm_id, args.role, args.as_of,
            args.half_life_years, args.prior_strength, args.sector, args.state,
        )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))
    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
        print(f"output={args.output} model={result['model_version']}")
    else:
        print(payload)


if __name__ == "__main__":
    main()
