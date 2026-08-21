#!/usr/bin/env python3
"""Filter a canonical Builtgraph CSV bundle without third-party dependencies."""

import argparse
import csv
import sys
from datetime import date
from pathlib import Path


def rows(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        yield from csv.DictReader(handle)


def normalized(items):
    return {item.strip().casefold() for item in items if item.strip()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_dir", type=Path)
    parser.add_argument("--state", action="append", default=[])
    parser.add_argument("--sector", action="append", default=[])
    parser.add_argument("--stage", action="append", default=[])
    parser.add_argument("--organization-id", action="append", default=[])
    parser.add_argument("--as-of", type=date.fromisoformat)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    projects_path = args.data_dir / "projects.csv"
    relationships_path = args.data_dir / "relationships.csv"
    if not projects_path.exists():
        parser.error(f"missing {projects_path}")
    related = None
    if args.organization_id:
        if not relationships_path.exists():
            parser.error("--organization-id requires relationships.csv")
        related = {r["project_id"] for r in rows(relationships_path) if r.get("organization_id") in set(args.organization_id)}
    filters = {"state": normalized(args.state), "sector": normalized(args.sector), "stage": normalized(args.stage)}
    result = []
    for row in rows(projects_path):
        if any(wanted and row.get(field, "").strip().casefold() not in wanted for field, wanted in filters.items()):
            continue
        if related is not None and row.get("project_id") not in related:
            continue
        source_date = row.get("source_date", "").strip()
        if args.as_of and source_date:
            try:
                if date.fromisoformat(source_date[:10]) > args.as_of:
                    continue
            except ValueError:
                row["temporal_warning"] = "invalid_source_date"
        elif args.as_of:
            row["temporal_warning"] = "missing_source_date"
        result.append(row)
    fieldnames = list(result[0]) if result else []
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
    handle = args.output.open("w", newline="", encoding="utf-8") if args.output else sys.stdout
    try:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        if fieldnames:
            writer.writeheader()
            writer.writerows(result)
    finally:
        if args.output:
            handle.close()
    print(f"matched_rows={len(result)}", file=sys.stderr)


if __name__ == "__main__":
    main()
