---
name: build-company-icp
description: Build or refresh an AEC firm's ideal client profile using Builtgraph evidence, the firm's portfolio website, and user-provided strategy. Use when a user wants company context, target sectors, ideal owners or developers, market positioning, or a reusable ICP for opportunity research.
---

# Build Company ICP

## Intake

If company identity is not already established, ask for the company name and portfolio website. Also request the user's office or geography, discipline or role, and any sectors they want to enter or avoid when those details would materially change the profile. Do not delay a useful first pass for optional inputs.

Read [references/icp-contract.md](references/icp-contract.md) before producing the profile.
Read [../query-builtgraph/references/live-mcp-playbook.md](../query-builtgraph/references/live-mcp-playbook.md)
before using live graph evidence.

## Workflow

1. Resolve the firm to a stable Builtgraph organization identity; preserve ambiguous matches for review.
2. Use the current MCP schemas to gather observed work, roles, geography, clients, and collaborators.
   Narrow the research to the sectors or roles that affect the profile.
3. Distinguish historical client fit from current observed activity. Compare relevant peers,
   complementary roles, and buyers when target-market context would improve the profile.
4. Review the firm's official portfolio website for missing service, sector, geography, and positioning context. Treat marketing claims as claimed evidence, not completed-project proof.
5. Reconcile conflicts and separate observed, claimed, user-provided, and inferred attributes.
6. Draft a dated ICP with current strengths, target sectors, ideal-client characteristics, exclusions, strategic adjacencies, evidence coverage, and confidence.
7. Offer reusable Markdown or JSON only when the user needs a portable profile.

## Guardrails

- Do not infer market share, profitability, capacity, certifications, office coverage, or project experience from silence.
- Do not turn one project or one website claim into a core sector without labeling weak evidence.
- Keep current demonstrated sectors separate from target sectors.
- Cite Builtgraph record identifiers or source URLs and portfolio pages near the claims they support.
- If live Builtgraph or website coverage is unavailable, produce a partial profile and mark affected fields unknown.
- A project count is observed portfolio depth, not market share; missing years make time-filtered
  results a floor. Do not infer firm capacity or an open opportunity from client activity.

## Presentation

Return a compact company snapshot, an evidence-tagged ICP table, target sectors with rationales, ideal-client criteria, exclusions, strategic adjacencies, and a short list of questions that would most improve the profile. Use badges such as `Observed`, `Claimed`, `User-provided`, and `Inferred` in text; do not imply an interactive widget exists.
