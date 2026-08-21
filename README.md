# Zensets Plugins

Official Zensets plugins for ChatGPT and Codex.

## Builtgraph

Builtgraph provides evidence-aware AEC research workflows backed by the hosted Builtgraph MCP server. It can:

- build a company ideal client profile and target sectors;
- find and prioritize potential project opportunities;
- research clients, competitors, and their project networks;
- assess attached RFPs using a transparent go/no-go risk rubric;
- identify newly observed and expanding developers; and
- query, score, and visualize Builtgraph project and relationship data.

The current release returns portable narrative, tables, and exportable data. It does not yet ship MCP-rendered interactive components.

## Install

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
.agents/plugins/marketplace.json
plugins/builtgraph/
  .codex-plugin/plugin.json
  .mcp.json
  skills/
tests/
```

## Data and decisions

Builtgraph outputs preserve source identifiers, as-of dates, missing values, ambiguous identities, and coverage limits. Opportunity scores prioritize research; they are not calibrated win probabilities. RFP assessments support an accountable human decision and do not replace legal, insurance, financial, safety, or contractual review.
