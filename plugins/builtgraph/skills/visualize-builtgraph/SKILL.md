---
name: visualize-builtgraph
description: Create evidence-aware visualizations from Builtgraph AEC data, including owner-partner networks, project pipelines, geographic lead maps, relationship concentration charts, and opportunity scorecards. Use when users ask to chart, map, visualize, compare, or explore Builtgraph projects and organization relationships.
---

# Visualize Builtgraph

## Workflow

1. Define the decision the visualization supports and the as-of date.
2. Inspect data fields, units, missingness, row counts, and source coverage.
3. Choose the smallest useful view using `references/chart-selection.md`.
4. Aggregate before rendering; preserve a drill-down table with project and source identifiers.
5. Run `scripts/relationship_graph.py` for a portable owner/partner network HTML file.
6. Verify labels, counts, totals, filters, legends, and empty states against source rows.

## Integrity rules

- Encode unknown values as unknown, not zero.
- Do not turn relationship frequency into relationship strength without labeling the proxy.
- Do not imply causation, bid intent, or future selection from historical co-participation.
- Keep organizations with similar names separate unless stable IDs establish identity.
- Show the selected time window and whether the data represents projects, relationships, awards, bids, or mentions.
- Avoid network hairballs: filter, facet, or rank to the decision-relevant subgraph.

## Command

```bash
python3 scripts/relationship_graph.py DATA_DIR --owner-id owner-123 --output owner-network.html
```

The HTML is dependency-free and embeds a provenance table beneath the graph.
