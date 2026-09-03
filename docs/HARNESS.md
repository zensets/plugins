# Harness guide

This repository ships one Builtgraph plugin package for multiple agent hosts. Use this guide when authoring, testing, or distributing the plugin.

To book a demo or request access, email [george@zensets.com](mailto:george@zensets.com).

## Shared contract

Every host uses the same MCP endpoint:

```text
https://builtgraph.com/mcp
```

The plugin root is `plugins/builtgraph/`. It bundles:

- seventeen skills under `skills/*/SKILL.md`
- hosted MCP config in `.mcp.json`
- host manifests in `.claude-plugin/` and `.codex-plugin/`
- a 1024×1024 marketplace icon at `assets/icon.png` (sourced from `assets/logo.svg`, the Zensets mark)

## Host matrix

| Host | Marketplace file | Manifest | Skills | Bundled MCP |
| --- | --- | --- | --- | --- |
| Claude Code | `.claude-plugin/marketplace.json` | `.claude-plugin/plugin.json` | Yes | Yes |
| Codex CLI / desktop Codex | `.agents/plugins/marketplace.json` or CLI add | `.codex-plugin/plugin.json` | Yes | Yes |
| ChatGPT Work (desktop) | `.agents/plugins/marketplace.json` | `.codex-plugin/plugin.json` | Yes | Yes |
| Claude web / Desktop | None | None | No | Connector only |
| ChatGPT MCP-only path | None | None | No | Connector only |

## Claude Code

**Install**

```bash
claude mcp add --transport http builtgraph https://builtgraph.com/mcp
```

```text
/plugin marketplace add zensets/plugins
/plugin install builtgraph@zensets
```

**Local test**

```bash
claude --plugin-dir ./plugins/builtgraph
```

**Skill namespace:** `/builtgraph:<skill-name>`

**Required files**

- `plugins/builtgraph/.claude-plugin/plugin.json` with `skills` and `mcpServers`
- `plugins/builtgraph/.mcp.json`
- `.claude-plugin/marketplace.json`

## Codex

**Install**

```toml
# ~/.codex/config.toml
[mcp_servers.builtgraph]
url = "https://builtgraph.com/mcp"
```

```bash
codex plugin marketplace add zensets/plugins
codex plugin add builtgraph@zensets
```

**Skill invocation:** `$<skill-name>`

**Required files**

- `plugins/builtgraph/.codex-plugin/plugin.json` with `interface`, `skills`, and `mcpServers`
- `plugins/builtgraph/assets/icon.png`
- `plugins/builtgraph/skills/*/agents/openai.yaml` with Builtgraph MCP `dependencies.tools`

## ChatGPT Work

ChatGPT desktop can load repo marketplaces from `.agents/plugins/marketplace.json`. ChatGPT web Work can use the same plugin when installed through a registered marketplace or workspace publishing flow.

**Plugin install (desktop)**

1. Open this repository locally.
2. Restart the ChatGPT desktop app.
3. Plugins Directory → **Zensets** → install **Builtgraph**.
4. Start a new chat and enable Builtgraph.

**MCP connector only**

Use Settings → Developer mode → Apps and Connectors → custom connector → `https://builtgraph.com/mcp`.

## Claude web and Claude Desktop

These hosts do not install plugin skills from this repository. Add Builtgraph as a custom connector and enable it per chat. Use starter questions from `plugins/builtgraph/skills/get-started/references/question-map.md`.

## Authoring checklist

When changing the plugin:

1. Keep Claude and Codex manifest versions in sync.
2. Update skill workflows in `skills/*/SKILL.md`.
3. Keep `agents/openai.yaml` MCP dependencies aligned with `.mcp.json`.
4. Preserve the 1024×1024 `assets/icon.png` sourced from the official Zensets mark in `assets/logo.svg`.
5. Run `python3 -m unittest discover -s tests -v`.

## Repository layout

```text
.claude-plugin/marketplace.json
.agents/plugins/marketplace.json
plugins/builtgraph/
  .claude-plugin/plugin.json
  .codex-plugin/plugin.json
  .mcp.json
  assets/icon.png
  assets/logo.svg
  skills/
docs/HARNESS.md
tests/
```
