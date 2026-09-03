# Builtgraph Plugin

Builtgraph packages seventeen AEC and real-estate intelligence skills with the hosted, read-only Builtgraph MCP server at `https://builtgraph.com/mcp`.

The plugin root also ships an [Agent Plugins 1.0](https://agent-plugins.org/specification) portable package (`plugin.json`, `skills/`, `mcp.json`) alongside Claude Code and Codex host manifests.

To book a demo, email [george@zensets.com](mailto:george@zensets.com).

The skills provide public, task-oriented research guidance. Current capabilities and request formats are supplied by the MCP rather than duplicated in the plugin.

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

## Host coverage

| Host | MCP connector | This plugin package |
| --- | --- | --- |
| Agent Plugins 1.0 clients | `mcp.json` | Yes |
| Claude web chat | Custom connector | Not applicable |
| Claude Desktop | Custom connector | Not applicable |
| Claude Code | `claude mcp add --transport http builtgraph https://builtgraph.com/mcp` | Yes |
| ChatGPT Work | Custom connector or plugin marketplace | Yes |
| Codex | `~/.codex/config.toml` entry | Yes |

See the root [README](../../README.md), [docs/HARNESS.md](../../docs/HARNESS.md), or [get-started/references/connect-builtgraph.md](skills/get-started/references/connect-builtgraph.md) for full setup steps on every host.

## ChatGPT Work

In the ChatGPT desktop app:

1. Open this repository locally so `.agents/plugins/marketplace.json` is available.
2. Restart the ChatGPT desktop app.
3. Open the **Plugins Directory**, select **Zensets**, and install **Builtgraph**.
4. Start a new chat and enable Builtgraph.

For MCP-only access without plugin skills, add the custom connector described in the root README.

## Claude Code

To test the Claude Code package directly from the repository root:

```bash
claude --plugin-dir ./plugins/builtgraph
```

Installed skills use the `builtgraph` namespace, such as `/builtgraph:get-started`.

## Codex

Register and install from the repository root:

```bash
codex plugin marketplace add zensets/plugins
codex plugin add builtgraph@zensets
```

Ensure `~/.codex/config.toml` includes the Builtgraph MCP server before starting a new task.
