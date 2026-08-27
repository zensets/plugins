import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "builtgraph"


class ClaudePluginTests(unittest.TestCase):
    def test_marketplace_points_to_builtgraph_plugin(self):
        marketplace = json.loads(
            (ROOT / ".claude-plugin" / "marketplace.json").read_text()
        )
        self.assertEqual(marketplace["name"], "zensets")
        self.assertEqual(marketplace["owner"]["name"], "Zensets")
        self.assertEqual(len(marketplace["plugins"]), 1)
        self.assertEqual(marketplace["plugins"][0]["name"], "builtgraph")
        self.assertEqual(
            marketplace["plugins"][0]["source"], "./plugins/builtgraph"
        )

    def test_claude_manifest_matches_plugin_and_codex_identity(self):
        claude_manifest = json.loads(
            (PLUGIN / ".claude-plugin" / "plugin.json").read_text()
        )
        codex_manifest = json.loads(
            (PLUGIN / ".codex-plugin" / "plugin.json").read_text()
        )
        self.assertEqual(claude_manifest["name"], PLUGIN.name)
        self.assertEqual(claude_manifest["name"], codex_manifest["name"])
        self.assertEqual(claude_manifest["author"]["name"], "Zensets")
        self.assertEqual(
            claude_manifest["repository"], "https://github.com/zensets/plugins"
        )

    def test_shared_skills_and_mcp_config_are_present(self):
        skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 16)

        mcp = json.loads((PLUGIN / ".mcp.json").read_text())
        builtgraph = mcp["mcpServers"]["builtgraph"]
        self.assertEqual(builtgraph["type"], "http")
        self.assertEqual(builtgraph["url"], "https://builtgraph.com/mcp")


if __name__ == "__main__":
    unittest.main()
