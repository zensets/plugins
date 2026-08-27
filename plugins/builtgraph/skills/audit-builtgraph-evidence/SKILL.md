---
name: audit-builtgraph-evidence
description: Audit Builtgraph results for identity, freshness, completeness, pagination, conflicting fields, missing sections, measurement coverage, and attribution quality. Use before relying on a negative, total, comparison, ownership claim, current-status claim, or decision-sensitive export.
---

# Audit Builtgraph Evidence

Read [../query-builtgraph/references/live-mcp-playbook.md](../query-builtgraph/references/live-mcp-playbook.md)
before auditing live results.

## Audit

1. Confirm the subject identity, typed ID, aliases, address or parcel variants, and unresolved
   duplicates or merges.
2. Check freshness, as-of date, source-specific sync limits, and whether a summary is older than its
   detailed records.
3. Compare returned totals with page length; narrow or paginate before making complete-list claims.
4. Inspect the available detail index before interpreting an omitted section or empty result.
5. Keep measured, unmeasured, dated, undated, located, unlocated, resolvable, and unresolved records
   separate.
6. Surface conflicts across properties, sections, relationships, and linked entities. Do not silently
   choose a preferred value without a defensible evidence basis.
7. Preserve source attribution and quality warnings for contractor identity, roles, document-derived
   contacts, ownership, and financing lifecycles.

## Output

Lead with whether the proposed conclusion is supported, partially supported, contradicted, or not
judgeable. Provide the evidence population inspected, material conflicts, coverage and freshness,
claims that remain safe, claims that must be narrowed, and the next verification needed.

Missing evidence is not a negative fact. A bounded count is not a census, an unresolved identity is
not a match, and an apparent current status may remain unknown when later lifecycle evidence is
absent.
