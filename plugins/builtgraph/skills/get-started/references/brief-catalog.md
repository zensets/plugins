# Builtgraph Brief Catalog

Use this catalog as a starting point, then adapt scope, cadence, fields, and evidence boundaries to the user's decision. A brief is a reusable research specification until the user explicitly asks to schedule it.

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
- **Include:** Typed nodes and edges, observed roles, time window, source dates, identity uncertainty, and pagination coverage. Co-participation is not proof of a commercial relationship.

## Market Pulse

- **Supports:** Sector and geography planning.
- **Typical scope:** Defined geography, sector, stages, roles, scale, and comparison periods.
- **Cadence:** Monthly or quarterly.
- **Route:** `$query-builtgraph`, with `$visualize-builtgraph` when a chart materially improves comprehension.
- **Include:** Counts and values when available, stage mix, active organizations, change versus the comparison window, missingness, and coverage statement. Do not infer total market size without representative coverage.

## Data Coverage and Freshness Audit

- **Supports:** Deciding whether Builtgraph evidence is adequate for another analysis.
- **Typical scope:** The entities, fields, geography, time window, and relationship types needed by the downstream decision.
- **Cadence:** Before high-stakes analysis or when data sources change.
- **Route:** `$query-builtgraph`.
- **Include:** Row or entity counts, missing fields, unresolved identities, source and effective dates, pagination or sampling limits, conflicts, and downstream implications.
