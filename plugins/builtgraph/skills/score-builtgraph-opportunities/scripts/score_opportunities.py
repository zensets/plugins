#!/usr/bin/env python3
"""Transparent, point-in-time Builtgraph opportunity prioritization baseline."""

import argparse
import csv
from datetime import date
from pathlib import Path


def read(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def parse_date(value):
    try:
        return date.fromisoformat((value or "")[:10])
    except ValueError:
        return None


def project_date(project):
    for field in ("bid_date", "start_date", "announced_date"):
        parsed = parse_date(project.get(field))
        if parsed:
            return parsed
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_dir", type=Path)
    parser.add_argument("--firm-id", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--as-of", required=True, type=date.fromisoformat)
    parser.add_argument("--project-id", action="append", default=[])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    projects = read(args.data_dir / "projects.csv")
    rels = read(args.data_dir / "relationships.csv")
    by_id = {p["project_id"]: p for p in projects}
    owner_by_project = {r["project_id"]: r["organization_id"] for r in rels if r.get("role") == "owner"}
    firm_rels = [r for r in rels if r.get("organization_id") == args.firm_id]
    candidates = [
        p for p in projects
        if (not args.project_id or p["project_id"] in args.project_id)
        and (not parse_date(p.get("source_date")) or parse_date(p.get("source_date")) <= args.as_of)
    ]
    output = []
    for candidate in candidates:
        decision = min(project_date(candidate) or args.as_of, args.as_of)
        history = []
        temporally_unverified = 0
        for rel in firm_rels:
            prior = by_id.get(rel.get("project_id"))
            if not prior or prior["project_id"] == candidate["project_id"]:
                continue
            effective = parse_date(rel.get("effective_date")) or project_date(prior)
            observed = parse_date(rel.get("source_date")) or parse_date(prior.get("source_date"))
            if not observed:
                temporally_unverified += 1
                continue
            if effective and effective >= decision:
                continue
            if observed and observed > decision:
                continue
            history.append((rel, prior, effective))
        owner = candidate.get("owner_org_id") or owner_by_project.get(candidate["project_id"], "")
        owner_count = sum(owner_by_project.get(p["project_id"]) == owner for _, p, _ in history) if owner else 0
        sector_count = sum(bool(candidate.get("sector")) and p.get("sector") == candidate.get("sector") for _, p, _ in history)
        state_count = sum(bool(candidate.get("state")) and p.get("state") == candidate.get("state") for _, p, _ in history)
        role_count = sum(r.get("role") == args.role for r, _, _ in history)
        dated = [d for _, _, d in history if d]
        recent = bool(dated and (decision - max(dated)).days <= 1096)
        parts = {
            "owner_relationship_points": round(35 * min(owner_count, 5) / 5, 1),
            "sector_fit_points": round(20 * min(sector_count, 10) / 10, 1),
            "geography_fit_points": round(15 * min(state_count, 10) / 10, 1),
            "role_fit_points": round(20 * min(role_count, 10) / 10, 1),
            "recency_points": 10.0 if recent else 0.0,
        }
        score = round(sum(parts.values()), 1)
        output.append({
            "project_id": candidate["project_id"], "project_name": candidate.get("project_name", ""),
            "owner_org_id": owner, "decision_date": decision.isoformat(), "priority_score": score,
            "priority_tier": "high" if score >= 70 else "medium" if score >= 40 else "low",
            "relationship_risk": round(100 - parts["owner_relationship_points"] / 35 * 100, 1),
            "prior_owner_projects": owner_count, "history_rows": len(history),
            "temporally_unverified_rows_excluded": temporally_unverified, **parts,
            "model_version": "observed-market-baseline-v1",
            "calibration_status": "uncalibrated_not_a_win_probability",
        })
    output.sort(key=lambda row: (-row["priority_score"], row["project_id"]))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = list(output[0]) if output else ["project_id"]
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)
    print(f"scored_projects={len(output)} output={args.output} model=observed-market-baseline-v1")


if __name__ == "__main__":
    main()
