# Zensets Plugins

Official Zensets plugins and workflow guidance for Builtgraph across Claude, Claude Code, ChatGPT, and Codex.

To book a demo, email [george@zensets.com](mailto:george@zensets.com).

For harness-specific authoring and install details, see [docs/HARNESS.md](docs/HARNESS.md).

## Builtgraph

Builtgraph provides evidence-aware AEC research workflows backed by the hosted Builtgraph MCP server. It can:

- build a company ideal client profile and target sectors;
- find and prioritize potential project opportunities;
- research clients, competitors, and their project networks;
- assess attached RFPs using a transparent go/no-go risk rubric;
- identify newly observed and expanding developers; and
- query, score, and visualize Builtgraph project and relationship data.

Every host uses the same MCP endpoint:

```text
https://builtgraph.com/mcp
```

To book a demo or request access, email [george@zensets.com](mailto:george@zensets.com).

The current release returns portable narrative, tables, and exportable data. It does not yet ship MCP-rendered interactive components.

## Connect Builtgraph MCP

### Claude and Claude Desktop

Add Builtgraph MCP as a custom connector in Claude web chat or the Claude Desktop app.

1. Open Claude at [claude.ai](https://claude.ai) or in the Claude Desktop app.
2. Go to **Customize**, then **Connectors**.
3. Choose **Add custom connector**.
4. Name it **Builtgraph** and paste `https://builtgraph.com/mcp`.
5. Click **Add**, then sign in when Claude asks.

In a chat, open **Connectors** from the **+** menu and turn Builtgraph on. Team and Enterprise owners add the connector in **Organization settings** first.

### Claude Code

Connect the MCP server, then install this marketplace for the Builtgraph research skills.

**Step 1 — add Builtgraph MCP**

```bash
claude mcp add --transport http builtgraph https://builtgraph.com/mcp
```

**Step 2 — install the plugin marketplace**

In an interactive Claude Code session:

```text
/plugin marketplace add zensets/plugins
/plugin install builtgraph@zensets
```

Run `/reload-plugins` if Claude Code asks you to activate the newly installed plugin. Builtgraph skills are available under the `builtgraph` namespace, such as `/builtgraph:get-started`.

Start a new Claude Code session after you add the server so Builtgraph MCP loads.

### ChatGPT

ChatGPT Work supports both a custom MCP connector and the plugin marketplace in this repository.

**Option A — MCP connector only**

On a paid ChatGPT plan:

1. In ChatGPT, open **Settings** and turn on **Developer mode**.
2. Open **Apps and Connectors**, then create a custom connector.
3. Name it **Builtgraph** and paste `https://builtgraph.com/mcp`.
4. Sign in when ChatGPT asks.

Start a new chat and enable the Builtgraph connector before you ask.

**Option B — install the Builtgraph plugin (skills + bundled MCP)**

In the ChatGPT desktop app with **Work** or **Codex** mode:

1. Clone or open this repository locally.
2. Confirm `.agents/plugins/marketplace.json` points at `./plugins/builtgraph`.
3. Restart the ChatGPT desktop app.
4. Open the **Plugins Directory**, choose the **Zensets** marketplace, and install **Builtgraph**.
5. Start a new chat and enable Builtgraph.

For CLI-based marketplace registration from another machine:

```bash
codex plugin marketplace add zensets/plugins
codex plugin add builtgraph@zensets
```

To book a demo or request access, email [george@zensets.com](mailto:george@zensets.com).

### Codex

Connect the MCP server, then install this marketplace for the Builtgraph research skills.

**Step 1 — add Builtgraph MCP**

Add this to `~/.codex/config.toml`:

```toml
[mcp_servers.builtgraph]
url = "https://builtgraph.com/mcp"
```

**Step 2 — install the plugin marketplace**

```bash
codex plugin marketplace add zensets/plugins
codex plugin add builtgraph@zensets
```

Start a new Codex task after you save the config and install the plugin so Codex loads Builtgraph MCP and the research skills.

## What each host gets

| Host | MCP connector | Plugin skills from this repo |
| --- | --- | --- |
| Claude web chat | Yes | No — use MCP plus starter questions from the get-started skill |
| Claude Desktop | Yes | No — use MCP plus starter questions from the get-started skill |
| Claude Code | Yes | Yes — seventeen specialist research skills |
| ChatGPT Work | Yes | Yes — install from `.agents/plugins/marketplace.json` or MCP connector only |
| Codex | Yes | Yes — seventeen specialist research skills |

## Repository layout

```text
.claude-plugin/marketplace.json
.agents/plugins/marketplace.json
plugins/builtgraph/
  plugin.json
  mcp.json
  .claude-plugin/plugin.json
  .codex-plugin/plugin.json
  .mcp.json
  assets/icon.png
  assets/logo.svg
  skills/
docs/HARNESS.md
tests/
```

## Data and decisions

Builtgraph outputs preserve source identifiers, as-of dates, missing values, ambiguous identities, and coverage limits. Opportunity scores prioritize research; they are not calibrated win probabilities. RFP assessments support an accountable human decision and do not replace legal, insurance, financial, safety, or contractual review.
