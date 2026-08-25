# Zensets Plugins

Official Zensets plugins for Claude Code, ChatGPT, and Codex.

## Builtgraph

Builtgraph provides evidence-aware AEC research workflows backed by the hosted Builtgraph MCP server. It can:

- build a company ideal client profile and target sectors;
- find and prioritize potential project opportunities;
- research clients, competitors, and their project networks;
- assess attached RFPs using a transparent go/no-go risk rubric;
- identify newly observed and expanding developers; and
- query, score, and visualize Builtgraph project and relationship data.

The current release returns portable narrative, tables, and exportable data. It does not yet ship MCP-rendered interactive components.

## Install in Claude Code (terminal app)

This GitHub marketplace is for **Claude Code**, not the Claude web chat at `claude.ai`. The web
chat does not accept Claude Code's `/plugin` marketplace commands.

In an interactive Claude Code session, add this marketplace and install Builtgraph:

```text
/plugin marketplace add zensets/plugins
/plugin install builtgraph@zensets
```

Run `/reload-plugins` if Claude Code asks you to activate the newly installed plugin. Builtgraph's
skills are available under the `builtgraph` namespace, such as `/builtgraph:get-started`.

## Install in Codex

Register this marketplace:

```bash
codex plugin marketplace add zensets/plugins
```

Then install the plugin:

```bash
codex plugin add builtgraph@zensets
```

Start a new task after installation so Codex loads the plugin's skills and MCP server configuration.

## Repository layout

```text
.claude-plugin/marketplace.json
.agents/plugins/marketplace.json
plugins/builtgraph/
  .claude-plugin/plugin.json
  .codex-plugin/plugin.json
  .mcp.json
  skills/
tests/
```

## Data and decisions

Builtgraph outputs preserve source identifiers, as-of dates, missing values, ambiguous identities, and coverage limits. Opportunity scores prioritize research; they are not calibrated win probabilities. RFP assessments support an accountable human decision and do not replace legal, insurance, financial, safety, or contractual review.
