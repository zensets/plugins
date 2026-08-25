---
name: find-potential-opportunities
description: Find and prioritize AEC project opportunities against a firm's explicit ideal client profile. Use when a user wants matched leads, projects to pursue or monitor, a strategic pipeline, or explanations of why current Builtgraph opportunities fit their company.
---

# Find Potential Opportunities

Read [../query-builtgraph/references/live-mcp-playbook.md](../query-builtgraph/references/live-mcp-playbook.md)
before building a live candidate set.

## Workflow

1. Load a dated ICP produced by `$build-company-icp`, or summarize the minimum firm, role, sector, geography, scale, and exclusion criteria from the conversation. Ask for missing criteria only when they would materially alter the search.
2. Define the as-of date and eligibility criteria. Use the current MCP schemas to build candidates
   from supported activity, planning, building, project, or entity evidence.
3. Enrich only shortlisted candidates with relevant team, relationship, firm-fit, owner-activity,
   or environmental context.
4. Use `$score-builtgraph-opportunities` when the candidate evidence supports a meaningful
   comparison. Keep ICP fit, relationship evidence, timing, and confidence separate.
5. Remove candidates that violate explicit exclusions. Preserve cold starts and missing values.
6. Classify supported candidates as `Investigate`, `Monitor`, or `Low fit`. Use `Pursue now` only
   when explicit current opportunity and role evidence supports that urgency.

Never call a missing or unnamed team participant an open, available, or unassigned role. State
that Builtgraph does not name a participant and that procurement status remains unknown. Translate
any returned availability-style field into that wording rather than quoting its label.

## Ranking dimensions

- sector, geography, project scale, role, delivery model, and stage fit
- owner and project-team history
- incumbent concentration and competitive context
- timing and evidence freshness
- strategic adjacency and cold-start status
- coverage quality and unresolved identity matches

## Output

Lead with the strongest few candidates and explain why each merits action. Include the returned
record, owner when resolved, location, observed activity and dates, fit tier, reasons, risks,
unknowns, evidence date, and record ID. Include stage or value only when the evidence supplies it.
Follow with focused research actions and a scope statement; offer deeper detail only when useful.

Treat the result as research prioritization, not an automated pursuit decision.
