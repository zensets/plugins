---
name: research-competitors
description: Research AEC competitors' observed projects, sectors, geographies, roles, clients, collaborators, and current activity using Builtgraph evidence. Use for competitor briefs, overlap analysis, incumbent research, or understanding where another firm appears active.
---

# Research Competitors

## Workflow

1. Identify the user's firm, relevant project role, named competitors, market, and as-of date. If no competitors are named, discover candidates by demonstrated overlap and label the selection method.
2. Resolve every organization to a stable identity and keep unresolved same-name firms separate.
3. Query projects and relationships with the Builtgraph MCP server or `$query-builtgraph`.
4. Separate announced or planned work, evidenced pursuits, awards, under-construction projects, completed work, and unknown stages.
5. Compare sector, geography, scale, owner, role, collaborator, and recent-activity overlap. Use `$visualize-builtgraph` when a network or pipeline view materially helps.

## Guardrails

- A firm working in the same market is not necessarily a direct competitor. Label direct overlap only when role and opportunity context support it.
- Do not infer that a firm bid, lost, won, or remains engaged from a project mention alone.
- Do not describe historical partners as current team members without current evidence.
- State coverage limitations before interpreting apparent gaps as strategy.

## Output

Return a competitor snapshot, current and historical project table, owner and collaborator patterns, overlap matrix, differentiated strengths or gaps supported by evidence, and monitoring signals. Attach an as-of date and sources to every time-sensitive section.
