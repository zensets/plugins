---
name: get-started
description: Orient users to Builtgraph by suggesting useful questions, choosing the right AEC research workflow, and designing reusable intelligence briefs. Use when a user asks what Builtgraph can do, what they can ask, how to get started, or which reports, monitors, or briefs they can set up.
---

# Get Started with Builtgraph

Help the user move from a broad goal to a useful Builtgraph workflow. Treat this as an orientation and routing skill, not a substitute for the specialist research skills.

Read [../query-builtgraph/references/live-mcp-playbook.md](../query-builtgraph/references/live-mcp-playbook.md)
before describing live capabilities. Suggest only questions Builtgraph can investigate with its
current evidence.

## Orient

Infer any context already present. When it would materially improve the recommendation, ask for the user's:

- firm or organization
- AEC role or discipline
- target geography
- decision, account, market, or pursuit they need to support

Do not require a complete profile before offering useful options. Let the user choose `Not sure` and explain what Builtgraph can determine from observed evidence versus what requires their strategy.

Respond with a compact, tailored menu rather than an exhaustive feature inventory. Prefer questions phrased as decisions the user may need to make, such as which opportunities merit investigation, how an owner selects teams, or where a competitor is active.

Balance the menu across the user's context. Useful question families include firm positioning,
active clients, competitors and complementary partners, people and career paths, building teams,
owners and related actors, and planning or environmental activity. Confirm current support from the
MCP rather than publishing a feature inventory or product-gap catalog.

When the user wants a broader capability map, read
[references/question-map.md](references/question-map.md). Use it to explain supported question
families and their evidence boundaries without turning the response into a tool catalog.

## Route

Route the selected goal to the narrowest existing skill:

- firm positioning, target sectors, or ideal clients: `$build-company-icp`
- projects to pursue, investigate, or monitor: `$find-potential-opportunities`
- a client, owner, developer, or prospect: `$research-client`
- competitors, sectors, geographies, or observed client overlap: `$research-competitors`
- emerging or expanding developers: `$find-emerging-developers`
- a building, address, parcel, or development site: `$research-building-and-site`
- ULURP, zoning, certification, or environmental review: `$research-planning-and-ulurp`
- recent permits, filing scope, architects, or contractors: `$research-permits-and-teams`
- a contractor's published projects, permit-observed footprint, or known-list comparison: `$research-contractor-project-history`
- ownership evidence, project LLCs, mortgages, lenders, or collateral: `$trace-ownership-and-financing`
- a person, career path, employer, or repeated team connection: `$research-people-and-career-paths`
- freshness, completeness, conflicts, attribution, or data quality: `$audit-builtgraph-evidence`
- an attached RFP or pursuit decision: `$assess-rfp-go-no-go`
- direct data questions, filtering, joins, coverage, or exports: `$query-builtgraph`
- explainable historical fit or relationship prioritization: `$score-builtgraph-opportunities`
- charts, maps, networks, or pipeline views: `$visualize-builtgraph`

If the request spans several workflows, recommend a sensible sequence and explain what each stage contributes. Do not reproduce the specialist skill's detailed procedure in this skill.

For direct live questions, use plain language that describes the answer the user will receive. For
example: "Which of our past clients have new projects underway?" or "Who owns this building, and
which firms are working on it?"

## Briefs

When the user asks about reports, monitoring, recurring research, or briefs, read [references/brief-catalog.md](references/brief-catalog.md). Recommend only briefs that support the user's stated decision.

For a proposed brief, specify:

- decision supported and intended audience
- scope: firm, accounts, sectors, geographies, stages, and exclusions
- evidence fields and important unknowns
- cadence or triggering event
- comparison window or as-of date
- Builtgraph skill or sequence used to produce it
- delivery format, if the user has stated one

Designing a brief does not schedule it. Only create a recurring task when the user explicitly asks to schedule or automate it, and preserve any approval boundary for outreach or other external actions.

## Evidence Boundaries

Separate `Observed`, `Claimed`, `User-provided`, `Inferred`, and `Unknown` information when those distinctions matter. Describe opportunity results as research prioritization, not win probability. Historical participation does not prove a current bid, preferred-vendor status, an open team role, or a future selection.

State identity, scope, and freshness qualifications when they affect the answer. If Builtgraph
cannot substantiate a request, say so early and offer the closest useful alternative without
presenting it as equivalent Builtgraph evidence.

## Handoff

End orientation with one clear next action. If enough context is available, begin the selected specialist workflow. Otherwise ask the single question most likely to change the recommendation.
