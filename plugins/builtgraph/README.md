# Builtgraph Plugin

Builtgraph packages seventeen AEC and real-estate intelligence skills with the hosted, read-only Builtgraph MCP server at `https://builtgraph.com/mcp`.

The skills provide public, task-oriented research guidance. Current capabilities and request
formats are supplied by the MCP rather than duplicated in the plugin.

## Workflows

- Guided onboarding, example questions, and reusable intelligence briefs
- Company ICP and target sectors
- Potential opportunity discovery
- Competitor research
- RFP go/no-go assessment
- Client research
- Emerging developer discovery
- Building and development-site research
- Planning, zoning, ULURP, and environmental-review research
- Permit, architect, contractor, and building-team research
- Contractor project-history and permit-observed footprint auditing
- Ownership, project-entity, mortgage, lender, and collateral tracing
- People, career-path, and team-connection research
- Evidence quality, completeness, freshness, and conflict auditing
- Evidence-backed querying
- Opportunity scoring
- Relationship and pipeline visualization

Results can be presented as concise findings, tables, and decision-ready research briefs.

## Claude Code

This directory is a Claude Code plugin as well as a Codex plugin. It is not directly installable
in the Claude web chat at `claude.ai`. To test the Claude Code package directly from the repository
root:

```bash
claude --plugin-dir ./plugins/builtgraph
```

Installed skills use the `builtgraph` namespace, such as `/builtgraph:get-started`.
