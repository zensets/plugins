---
name: visualize-builtgraph
description: Create evidence-aware visualizations from live Builtgraph results, including bounded networks, portfolios, activity timelines, comparisons, and geographic views. Use when a visual materially clarifies an AEC or real-estate decision.
---

# Visualize Builtgraph

Read [../query-builtgraph/references/live-mcp-playbook.md](../query-builtgraph/references/live-mcp-playbook.md)
and [references/chart-selection.md](references/chart-selection.md).

## Workflow

1. Define the decision, audience, comparison, and as-of date.
2. Gather the smallest relevant live result using the current MCP schemas. Preserve identifiers,
   relationship labels, scope, freshness, and completeness metadata in a source table.
3. Choose the simplest view that makes the important relationship easier to understand. Aggregate
   only when the aggregation remains traceable to the returned evidence.
4. Verify labels, counts, filters, legends, and empty states against the source table.
5. State whether the view is complete, bounded, sampled, or partially unavailable.

## Integrity rules

- Encode unknown as unknown, not zero.
- Do not turn frequency into relationship strength, causation, bid intent, or future selection.
- Keep unresolved identities separate.
- Prefer a small legible subgraph to a dense partial network.
- Do not imply geographic precision when coordinates are unavailable or completeness when the MCP
  reports truncation.
