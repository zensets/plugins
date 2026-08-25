# Builtgraph Brief Catalog

Use this catalog as a starting point, then adapt scope, cadence, fields, and evidence boundaries to the user's decision. A brief is a reusable research specification until the user explicitly asks to schedule it.

Every live brief follows the research and evidence boundaries in
[the live MCP playbook](../../query-builtgraph/references/live-mcp-playbook.md). A cadence describes
the proposed research rhythm; it does not create a monitor.

## Opportunity Pipeline Brief

- **Supports:** Business-development and pursuit prioritization.
- **Typical scope:** Eligible project stages, target sectors, geographies, scale, role, and exclusions from a dated company ICP.
- **Cadence:** Weekly or when relevant project evidence changes.
- **Route:** `$build-company-icp` when needed, then `$find-potential-opportunities`; use `$score-builtgraph-opportunities` only when historical relationship evidence is useful.
- **Include:** Project, owner, location, stage, relevant dates, value when known, fit tier, fit reasons, risks, unknowns, evidence date, and source.

## Owner or Developer Activity Watch

- **Supports:** Account planning and early project discovery.
- **Typical scope:** Named owners, developers, owner families, portfolios, addresses, filings, projects, and observed team relationships.
- **Cadence:** Weekly, monthly, or ahead of an account review.
- **Route:** `$research-client`, with `$query-builtgraph` for bounded filtering or export.
- **Include:** Newly observed activity, changed records, team participants by role, unresolved aliases, evidence dates, and source identifiers.

## Emerging Developer Watchlist

- **Supports:** Discovery of newly observed or rapidly expanding developers.
- **Typical scope:** Geography, lookback window, activity threshold, project type, and exclusions.
- **Cadence:** Monthly or quarterly.
- **Route:** `$find-emerging-developers`.
- **Include:** Observed activity change, portfolio context, identity confidence, evidence coverage, and why each firm merits investigation. Do not call a bounded result a citywide ranking unless coverage supports that claim.

## Client Intelligence Brief

- **Supports:** Meeting preparation, account strategy, and relationship development.
- **Typical scope:** One client, owner, developer, or prospect plus relevant affiliates and portfolio.
- **Cadence:** Before meetings or monthly for strategic accounts.
- **Route:** `$research-client`.
- **Include:** Organization identity, recent observed activity, sectors, geographies, project teams, recurring collaborators, relationship history, open questions, freshness, and sources.

## Competitor Activity Brief

- **Supports:** Positioning, market selection, and pursuit context.
- **Typical scope:** Named competitors, roles, sectors, geographies, clients, project stages, and time window.
- **Cadence:** Monthly, quarterly, or before a strategy review.
- **Route:** `$research-competitors`.
- **Include:** Observed projects and roles, client overlap, sector and geography patterns, evidence gaps, and identity caveats. Do not infer bids, losses, market share, or competitive intent from silence.

## RFP and Pursuit Review

- **Supports:** Go/no-go discussion and diligence planning.
- **Typical scope:** An attached RFP, the pursuing firm's dated ICP, and relevant client or team history.
- **Cadence:** When an RFP arrives and at material pursuit milestones.
- **Route:** `$assess-rfp-go-no-go`, optionally preceded by `$build-company-icp` or `$research-client`.
- **Include:** Requirements, fit, relationship evidence, delivery and commercial risks, conflicts, unknowns, clarification questions, and evidence-backed recommendation. Keep the final decision with the user.

## Relationship and Incumbent Map

- **Supports:** Account mapping and team-strategy discussion.
- **Typical scope:** An owner, project, sector, geography, and explicit relationship types.
- **Cadence:** Before a pursuit or account review; refresh when evidence changes.
- **Route:** `$query-builtgraph`, then `$visualize-builtgraph`; use `$score-builtgraph-opportunities` for explainable historical concentration or affinity measures.
- **Include:** Identified actors and relationships, observed roles, time window, source dates, and identity uncertainty. Co-participation is not proof of a commercial relationship.

## Market Pulse

- **Supports:** Sector and geography planning.
- **Typical scope:** Defined geography, sector, stages, roles, scale, and comparison periods.
- **Cadence:** Monthly or quarterly.
- **Route:** `$query-builtgraph`, selecting current MCP capabilities according to the market question;
  add `$visualize-builtgraph` only when a chart materially improves comprehension.
- **Include:** Supported counts, active organizations, comparison window, missingness, and coverage.
  Include values or stage mix only when the selected live surface returns them. Do not infer total
  market size without representative coverage.

## Building and Team Watch

- **Supports:** Account discovery, project-team research, and preparation for work at a known site.
- **Typical scope:** Named addresses or a bounded borough/permit-type/recency building set.
- **Route:** `$query-builtgraph` to resolve the place, inspect relevant activity and teams, and
  follow only decision-relevant relationships.
- **Include:** Building IDs, observed filings, owners where resolved, people and firms by recorded
  role, lookback window, relationship completeness, identity caveats, and worthwhile follow-ups.

## Zoning and Environmental Movement Brief

- **Supports:** Early advisory, environmental, design, and development intelligence.
- **Typical scope:** Borough, milestone, lookback window, and relevant specialist disciplines.
- **Route:** `$query-builtgraph` to identify relevant planning movement, inspect environmental
  context, and research selected applicants or specialists.
- **Include:** Application IDs, milestones, dates, applicants and related actors, environmental
  obligation state, named participants, missing participant evidence, and coverage. A missing
  participant is an evidence gap, not an open or available role.

## People and Career Map

- **Supports:** Relationship-path research and meeting preparation.
- **Typical scope:** Named people, organizations, role context, and as-of date.
- **Route:** `$query-builtgraph` to resolve the person, then perform a bounded,
  completeness-checked affiliation and project investigation.
- **Include:** Resolved identity, aliases, observed affiliations and projects, source IDs, and
  ambiguous matches. An observed affiliation is not current employment
  unless time-specific evidence establishes it.

## Data Coverage and Freshness Audit

- **Supports:** Deciding whether Builtgraph evidence is adequate for another analysis.
- **Typical scope:** The entities, fields, geography, time window, and relationship types needed by the downstream decision.
- **Cadence:** Before high-stakes analysis or when data sources change.
- **Route:** `$query-builtgraph`.
- **Include:** Relevant record counts, missing fields, unresolved identities, source and effective
  dates, material scope limits, conflicts, and downstream implications.
