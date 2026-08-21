---
name: find-potential-opportunities
description: Find and prioritize AEC project opportunities against a firm's explicit ideal client profile. Use when a user wants matched leads, projects to pursue or monitor, a strategic pipeline, or explanations of why current Builtgraph opportunities fit their company.
---

# Find Potential Opportunities

## Workflow

1. Load a dated ICP produced by `$build-company-icp`, or summarize the minimum firm, role, sector, geography, scale, and exclusion criteria from the conversation. Ask for missing criteria only when they would materially alter the search.
2. Define the as-of date and eligible project stages. Use `$query-builtgraph` or the Builtgraph MCP server to build the candidate set.
3. Use `$score-builtgraph-opportunities` when historical relationship scoring is warranted. Keep ICP fit, relationship evidence, timing, and data confidence as separate dimensions.
4. Remove projects that violate explicit exclusions. Preserve cold starts and missing values rather than assigning neutral evidence.
5. Classify results as `Pursue now`, `Investigate`, `Monitor`, or `Low fit`; do not call these win probabilities.

## Ranking dimensions

- sector, geography, project scale, role, delivery model, and stage fit
- owner and project-team history
- incumbent concentration and competitive context
- timing and evidence freshness
- strategic adjacency and cold-start status
- coverage quality and unresolved identity matches

## Output

Lead with a filterable-in-prose opportunity table containing project, owner, location, stage, relevant dates, value when known, fit tier, fit reasons, risks, unknowns, evidence date, and source. Follow with recommended next research actions and a coverage statement. Offer CSV or JSON export when useful; do not imply a native interactive component is available.

Treat the result as research prioritization, not an automated pursuit decision.
