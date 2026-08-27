---
name: research-permits-and-teams
description: Investigate recent NYC construction permits, filing scope, building teams, and contractor evidence through Builtgraph. Use for activity screens, architect-of-record research, contractor histories, filing status, declared cost, or repeat-team analysis.
---

# Research Permits and Teams

Read [../query-builtgraph/references/live-mcp-playbook.md](../query-builtgraph/references/live-mcp-playbook.md)
before live research.

## Workflow

1. Define borough, permit class, lookback window, size measure, role, and decision context.
2. Keep distinct buildings separate from filings and measured records separate from unmeasured ones.
3. Resolve shortlisted buildings and, when evaluating an incumbent, define the target scope,
   current sponsor, triggering capital event, and as-of date.
4. Inspect filing-level details and team evidence. Join each professional to the relevant filing and
   scope rather than treating everyone returned for a building as part of the target project.
5. Distinguish an RA from a PE, the professional who filed from the firm employing them, and both
   from contractors and property-side parties. Preserve unresolved person-to-firm mappings.
6. Preserve filing dates, status, scope text, declared cost, role, license type, and contractor
   quality or attribution warnings.
7. Compare the filing date with the acquisition, financing, sponsor change, or other triggering
   event. Apply the active-architect evidence states from the live MCP playbook.
8. Compare recent activity with historical participation only when it materially changes the
   interpretation.

## Output

Return a bounded activity summary or building-specific filing history with typed IDs, relevant
filings, named roles, dates, scope, available size signals, quality warnings, and coverage. Explain
why shortlisted records merit investigation without calling them available work.

When evaluating an architect, include the active-architect classification, `scope_match`,
`capital_event_alignment`, and the evidence for any RA-to-firm mapping. Do not treat tenant work,
signage, routine facade work, engineering systems, or temporary construction as a whole-building
design commission without exact scope evidence.

Declared filing cost is not contract value or discipline budget. A historical architect or
contractor is not necessarily engaged on a new proposal, and a filing does not prove procurement
status.
