# Company profile and ICP contract

## Required metadata

- `company_name`, stable organization ID when resolved, website, and as-of date
- user's discipline or project role, office or geography, and stated strategy when provided
- coverage state for Builtgraph, portfolio website, and user inputs

## Profile fields

- services and observed project roles
- demonstrated sectors and target sectors
- demonstrated and target geographies
- observed project scale and stage patterns
- recurring owner, developer, design, engineering, contractor, and consultant relationships
- portfolio positioning and differentiators
- strategic adjacencies, exclusions, and weak-fit work

## Evidence labels

- `Observed`: supported by identified Builtgraph records or other project evidence
- `Claimed`: stated by the firm's official website or publication
- `User-provided`: supplied by the user and not independently verified
- `Inferred`: reasoned from evidence; include the rationale and confidence
- `Unknown`: unavailable or conflicting

## Reusable JSON shape

```json
{
  "schema_version": "1.0",
  "as_of": "YYYY-MM-DD",
  "company": {"name": "", "organization_id": null, "website": ""},
  "user_context": {"role": null, "office": null, "strategy": []},
  "demonstrated": {"roles": [], "sectors": [], "geographies": [], "project_scale": {}},
  "targets": {"sectors": [], "geographies": [], "client_characteristics": [], "project_characteristics": []},
  "relationships": [],
  "adjacencies": [],
  "exclusions": [],
  "evidence": [],
  "unknowns": [],
  "coverage": {}
}
```

Keep arrays empty when evidence is absent; do not manufacture placeholder values.
