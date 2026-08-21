---
name: query-builtgraph
description: Query, filter, join, summarize, and audit Builtgraph AEC project and relationship data. Use for finding project leads, owners, architects, contractors, subcontractors, awards, bids, and relationship history; answering market questions; exporting evidence-backed lead lists; or checking coverage and provenance in Builtgraph CSV data.
---

# Query Builtgraph

## Workflow

1. Locate the data and read `references/data-contract.md` before writing a query.
2. Inspect headers and distinct values. Never assume role, stage, sector, geography, or date encodings.
3. Translate the request into explicit filters, joins, ranking, and an as-of date.
4. Run `scripts/query_builtgraph.py` for canonical CSV bundles. Use a native database/API query only when the workspace documents it.
5. Return the answer, applied filters, row count, coverage caveats, and source URLs or record IDs.

## Lead rules

- Treat a project as a lead only when its stage, timing, geography, and relevant role create a plausible opportunity.
- Distinguish announced, planned, bidding, awarded, under-construction, completed, cancelled, and unknown stages.
- Do not present an incumbent or historical participant as a current bidder unless current evidence says so.
- Deduplicate organizations by stable ID. Do not merge on name alone when identity is ambiguous.
- Preserve `unknown`, missing, and conflicting values. Never infer values simply to fill a result.
- Apply point-in-time discipline: exclude evidence observed after the requested as-of date.

## Command

```bash
python3 scripts/query_builtgraph.py DATA_DIR \
  --state TX --sector healthcare --stage bidding --as-of 2026-08-20 \
  --output leads.csv
```

Use multiple values with repeated flags. Add `--organization-id` to restrict results to projects connected to a particular organization.

## Output contract

For each lead include project ID, project name, owner, location, stage, relevant dates, estimated value, evidence date, source URL, and why it matched. State whether the result set is complete, filtered, sampled, or partially unavailable.
