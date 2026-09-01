---
name: research-contractor-project-history
description: Build an evidence-audited history of a contractor's projects and permit-linked buildings over a requested period. Use for customer project histories, contractor footprint research, and comparisons between known project lists, published portfolios, and permit-observed activity.
---

# Research Contractor Project History

Read [../query-builtgraph/references/live-mcp-playbook.md](../query-builtgraph/references/live-mcp-playbook.md)
before live research.

Investigate the work history of one or more contractors using both curated project credits and permit-linked building evidence.

Use the current Builtgraph MCP descriptions as the authoritative contract for available tools, fields, limits, and evidence semantics.

## Define the request

Establish:

- Contractor or customer names
- Geography
- Requested time window
- Relevant contractor roles
- Whether the user wants published projects, permit-observed work, or both
- Whether a known-project or platform-deployment list is available
- As-of date

Use the user's supplied roster when available. If a roster must be assembled from public sources, preserve its provenance and distinguish:

- Officially identified customer
- Case-study participant
- Testimonial or logo placement
- Partner or integration
- Inferred relationship
- Unknown current status

Do not treat a public reference cohort as a complete customer roster.

## Resolve contractor identity

Resolve identity before counting or comparing work.

1. Search the contractor's brand name, legal name, former names, abbreviations, and common variants.
2. Inspect every plausible organization face rather than accepting the first fuzzy match.
3. Preserve each typed Builtgraph ID until the evidence supports a merge or selection.
4. Inspect available identity evidence, including:
   - Current and former names
   - New York Department of State entity
   - Entity status
   - NYC DOB license number and status
   - Licensed qualifiers
   - Roles
   - First- and last-seen dates
5. Compare legal names and aliases with the name used by the user or source roster.
6. Report unresolved duplicate or affiliated entities separately.

A shared or similar name does not establish identity. A former-name match may support identity when it is consistent with legal-entity, license, qualifier, address, and activity evidence.

## Use both work-history lanes

Always consider these as distinct evidence populations.

### Published portfolio

Curated projects credited to the contractor through company, architect, engineer, award, or project-profile sources.

Use this lane to understand:

- Named projects
- Sectors
- Geographies
- Clients
- Collaborators
- Project scale
- Published contractor roles
- Construction years where available

A published portfolio is selective. It is not a complete work history.

### Permit-observed activity

Buildings where source filings identify the contractor in a specific role.

Use this lane to identify:

- Alterations
- Tenant improvements
- Interior construction
- Mechanical or structural modifications
- Public-facility work
- Scaffolding or site-safety roles
- Other work that may not appear in a curated portfolio

Do not combine published projects and permit-observed buildings into one unexplained count.

## Walk from contractors to buildings

For each resolved contractor:

1. Inspect the organization record's available sections.
2. Read organization-level counts, work profile, trade profile, and building relationships where available.
3. Follow relationships into buildings for the requested contractor roles.
4. Compare:
   - Organization-level building count
   - Relationship total
   - Returned relationship rows
   - `top_buildings` length
   - Building-level contractor summaries
5. Inspect additional organization faces when expected coverage appears unexpectedly small.
6. Retain the building's typed ID, address, borough, BIN, BBL, and address variants.

Do not rely solely on a building's bounded `top_contractors` section. A contractor may be connected to a building but omitted from that short ranking.

Do not treat `top_buildings` as a complete list unless its length equals the relevant organization-level total or the MCP explicitly says it is complete.

## Apply the time window correctly

Filter permit-observed work using the contractor's activity date at the building.

Do not substitute:

- The building's latest filing date
- Another contractor's filing date
- The building's construction year
- A curated project's completion year
- The date the source page was published

Calculate an exact cutoff date when the user requests a rolling period such as "the last three years."

Keep these populations separate:

- Contractor activity inside the window
- Contractor activity before the window
- Undated contractor relationships
- Buildings with recent activity by other parties only

For published projects, explain whether the available date represents completion, start, announcement, or another milestone. If the date meaning is unknown, label it unknown.

## Inspect the underlying filings

For each qualifying permit-linked building, inspect the contractor-linked filings needed to substantiate the result.

Capture when available:

- Building name
- Primary address and address variants
- Borough
- BIN and BBL
- Contractor name as filed
- Contractor typed ID
- Contractor role
- License or qualifier
- Permit or filing number
- Filed date
- Permit type
- Status
- Work description
- Estimated or declared cost
- First observed contractor activity
- Latest observed contractor activity
- Number of contractor-linked filings
- Named owner
- Named architect or applicant
- Other relevant trade contractors

Describe declared permit costs as values stated on filings, not contract value or total project cost.

A building-level recent-filings section may be limited to the building's most recent filings across all parties. If the contractor's older filing falls outside that slice, retain the organization-level attribution and state that the detailed scope was not returned.

## Preserve roles precisely

Distinguish:

- General contractor
- Construction manager
- Scaffolding contractor
- Site-safety role
- Permit responsible party
- Owner
- Applicant
- Architect
- Engineer
- Other collaborator

Do not convert `collaborated_on` into a more specific role unless another field supports that role.

Do not describe a contractor as the general contractor for a building when the evidence only identifies scaffolding, safety, ownership, or another role.

## Compare known and observed records

When the user supplies a known-project or platform-deployment list:

1. Normalize company names, project names, addresses, boroughs, BINs, BBLs, and aliases.
2. Match exact identifiers before using name similarity.
3. Preserve uncertain matches for review.
4. Classify each record as:
   - `Known record`
   - `Additional permit-observed work`
   - `Possible match requiring review`
   - `Known record not found in Builtgraph`
5. Keep published portfolio matches separate from permit-only matches.
6. Explain the coverage and date boundaries of both datasets.

Absence from a supplied list does not establish non-deployment, non-participation, or lack of awareness. Report platform usage as unknown unless directly evidenced.

## Audit completeness and conflicts

Before making a total, negative, or comparative claim:

1. Compare totals with returned page lengths.
2. Check for truncated relationships and ranked subsections.
3. Inspect `sections_available` before treating omitted details as absent.
4. Separate dated, undated, located, unlocated, resolved, and unresolved records.
5. Compare summary fields with detailed rows.
6. Surface inconsistent first-seen, last-seen, permit-count, or role values.
7. Check whether duplicate organization faces divide the contractor's work.
8. Preserve contractor-quality or attribution warnings.
9. Check freshness and the source-specific as-of date.
10. Narrow any conclusion that the available interface cannot support completely.

When organization-level and building-level summaries conflict, do not silently select one. Explain the conflict and prefer the source-specific detailed record only when its provenance and scope justify doing so.

## Evidence labels

Use these labels when the distinction affects the conclusion:

- `Observed`: Returned by Builtgraph from a named source record or relationship
- `Claimed`: Published by a company, customer, or project source
- `User-provided`: Supplied by the user without independent confirmation
- `Inferred`: A reasoned connection not directly stated by a source
- `Unknown`: Not established by the available evidence

A public company portfolio is a claim of participation. A permit filing is an observation tied to a filing, role, and date. Neither automatically proves the complete commercial arrangement.

## Output

Lead with whether the requested conclusion is:

- Supported
- Partially supported
- Contradicted
- Not judgeable

For each contractor, provide:

### Identity

- Display name
- Legal or former names
- Typed Builtgraph IDs
- License and entity evidence
- Remaining identity uncertainty

### Published projects

- Project
- Location
- Sector
- Published role
- Client
- Relevant date
- Source basis

### Permit-observed buildings

- Building and address
- Borough
- Contractor role
- First and latest observed activity
- Filing count
- Recent filing scope
- Permit status and number where useful
- Relevant attribution or coverage caveat

### Comparison

When a known list exists:

- Known records matched
- Additional permit-observed records
- Possible matches
- Known records not found

### Coverage

State:

- Requested time window and exact cutoff
- Geography
- Resolved and unresolved contractors
- Published-project coverage
- Permit-linked building coverage
- Pagination or ranking limits
- Missing dates or filing details
- As-of date and freshness

## Safe conclusion patterns

Prefer:

> Builtgraph observed Swinerton Builders as general contractor on 17 NYC buildings during the requested three-year window. These permit-linked records supplement its published portfolio.

> Builtgraph connects the contractor to 20 NYC buildings overall, of which 17 have contractor activity inside the requested window, two fall before the cutoff, and one requires date review.

> The organization-level record attributes the contractor to this building, but the contractor's filing falls outside the building's bounded recent-filings section, so the detailed scope was not returned.

Avoid:

> These are all of the contractor's projects.

> The contractor did not work anywhere else.

> The software was not deployed on these projects.

> No contractor has been selected.

> The contractor currently owns or controls the project.

Missing evidence, truncation, or absence from another dataset does not establish any of those claims.
