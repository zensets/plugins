#!/usr/bin/env python3
"""Generate a portable SVG relationship network and provenance table."""

import argparse
import csv
import html
import math
from collections import Counter
from pathlib import Path


def read(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_dir", type=Path)
    parser.add_argument("--owner-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--top", type=int, default=15)
    args = parser.parse_args()
    orgs = {r["organization_id"]: r for r in read(args.data_dir / "organizations.csv")}
    rels = read(args.data_dir / "relationships.csv")
    owner_projects = {r["project_id"] for r in rels if r.get("organization_id") == args.owner_id and r.get("role") == "owner"}
    evidence = [r for r in rels if r.get("project_id") in owner_projects and r.get("organization_id") != args.owner_id]
    partners = Counter(r.get("organization_id") for r in evidence).most_common(args.top)
    cx, cy, radius = 450, 280, 205
    nodes, edges = [], []
    owner_name = orgs.get(args.owner_id, {}).get("organization_name", args.owner_id)
    for index, (org_id, count) in enumerate(partners):
        angle = 2 * math.pi * index / max(1, len(partners))
        x, y = cx + radius * math.cos(angle), cy + radius * math.sin(angle)
        name = orgs.get(org_id, {}).get("organization_name", org_id)
        edges.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#9ca3af" stroke-width="{1 + min(count, 8)}"/>')
        nodes.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="18" fill="#14b8a6"/><text x="{x:.1f}" y="{y + 32:.1f}" text-anchor="middle">{html.escape(name)} ({count})</text>')
    table_rows = "".join(f"<tr><td>{html.escape(orgs.get(r.get('organization_id'), {}).get('organization_name', r.get('organization_id', '')))}</td><td>{html.escape(r.get('role', ''))}</td><td>{html.escape(r.get('project_id', ''))}</td><td><a href=\"{html.escape(r.get('source_url', ''), quote=True)}\">source</a></td></tr>" for r in evidence)
    doc = f'''<!doctype html><meta charset="utf-8"><title>{html.escape(owner_name)} relationship network</title>
<style>body{{font:14px system-ui;margin:2rem;color:#172033}}svg{{max-width:100%;border:1px solid #ddd}}text{{font-size:12px}}table{{border-collapse:collapse;width:100%}}td,th{{padding:6px;border-bottom:1px solid #ddd;text-align:left}}</style>
<h1>{html.escape(owner_name)} relationship history</h1><p>Edge width and labels show project co-participation counts; they do not prove preference or future selection.</p>
<svg viewBox="0 0 900 560">{''.join(edges)}<circle cx="{cx}" cy="{cy}" r="30" fill="#1d4ed8"/><text x="{cx}" y="{cy + 48}" text-anchor="middle">{html.escape(owner_name)}</text>{''.join(nodes)}</svg>
<h2>Evidence</h2><table><thead><tr><th>Organization</th><th>Role</th><th>Project</th><th>Source</th></tr></thead><tbody>{table_rows}</tbody></table>'''
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(doc, encoding="utf-8")
    print(f"projects={len(owner_projects)} partners={len(partners)} evidence_rows={len(evidence)} output={args.output}")


if __name__ == "__main__":
    main()
