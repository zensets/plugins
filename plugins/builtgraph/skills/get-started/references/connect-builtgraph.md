# Connect Builtgraph

Use this reference when a user asks how to install, connect, enable, or set up Builtgraph in Claude,
Claude Desktop, Claude Code, ChatGPT, or Codex.

To book a demo or request access, email [george@zensets.com](mailto:george@zensets.com).

Every host uses the same MCP endpoint:

```text
https://builtgraph.com/mcp
```

## Claude and Claude Desktop

These hosts use a custom MCP connector, not the Claude Code plugin marketplace.

1. Open Claude at [claude.ai](https://claude.ai) or in the Claude Desktop app.
2. Go to **Customize**, then **Connectors**.
3. Choose **Add custom connector**.
4. Name it **Builtgraph** and paste `https://builtgraph.com/mcp`.
5. Click **Add**, then sign in when Claude asks.

In a chat, open **Connectors** from the **+** menu and turn Builtgraph on. Team and Enterprise owners add the connector in **Organization settings** first.

These hosts do not load the seventeen specialist skills from this repository. After connecting MCP, suggest starter questions from [question-map.md](question-map.md).

## Claude Code

Claude Code uses both the MCP server and the plugin marketplace in this repository.

**Add Builtgraph MCP**

```bash
claude mcp add --transport http builtgraph https://builtgraph.com/mcp
```

**Install the plugin marketplace**

```text
/plugin marketplace add zensets/plugins
/plugin install builtgraph@zensets
```

Run `/reload-plugins` if Claude Code asks you to activate the newly installed plugin. Start a new session after setup so Builtgraph MCP and the skills load. Installed skills use the `builtgraph` namespace, such as `/builtgraph:get-started`.

## ChatGPT

ChatGPT Work supports a custom MCP connector or the plugin marketplace in this repository.

**MCP connector only**

1. In ChatGPT, open **Settings** and turn on **Developer mode**.
2. Open **Apps and Connectors**, then create a custom connector.
3. Name it **Builtgraph** and paste `https://builtgraph.com/mcp`.
4. Sign in when ChatGPT asks.

Start a new chat and enable the Builtgraph connector before asking.

**Plugin install (skills + bundled MCP)**

In the ChatGPT desktop app with **Work** or **Codex** mode:

1. Open this repository locally.
2. Restart the ChatGPT desktop app.
3. Open the **Plugins Directory**, choose **Zensets**, and install **Builtgraph**.
4. Start a new chat and enable Builtgraph.

Alternatively, register the marketplace from the CLI:

```bash
codex plugin marketplace add zensets/plugins
codex plugin add builtgraph@zensets
```

## Codex

Codex uses both the MCP server and the plugin marketplace in this repository.

**Add Builtgraph MCP**

Add this to `~/.codex/config.toml`:

```toml
[mcp_servers.builtgraph]
url = "https://builtgraph.com/mcp"
```

**Install the plugin marketplace**

```bash
codex plugin marketplace add zensets/plugins
codex plugin add builtgraph@zensets
```

Start a new Codex task after saving the config and installing the plugin.

## Troubleshooting

- If Builtgraph tools are missing, confirm the MCP connector is enabled in the current chat or task.
- If skills are missing in Claude Code or Codex, confirm the plugin is installed and start a new session.
- If authentication fails, email [george@zensets.com](mailto:george@zensets.com) to book a demo and request access.
- Do not invent alternate MCP URLs or host-specific endpoints. The authoritative endpoint is `https://builtgraph.com/mcp`.
