import json
import unittest
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "builtgraph"
BUILTGRAPH_MCP_URL = "https://builtgraph.com/mcp"
PLUGIN_VERSION = "0.1.8"
ICON_PATH = PLUGIN / "assets" / "icon.png"
MIN_ICON_SIZE = 1024


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

    def test_agents_marketplace_points_to_builtgraph_plugin(self):
        marketplace = json.loads(
            (ROOT / ".agents" / "plugins" / "marketplace.json").read_text()
        )
        plugin = marketplace["plugins"][0]
        self.assertEqual(marketplace["name"], "zensets")
        self.assertEqual(plugin["name"], "builtgraph")
        self.assertEqual(plugin["displayName"], "Builtgraph")
        self.assertEqual(plugin["source"]["path"], "./plugins/builtgraph")
        self.assertEqual(plugin["policy"]["installation"], "AVAILABLE")
        self.assertEqual(plugin["policy"]["authentication"], "ON_INSTALL")

    def test_claude_manifest_matches_plugin_and_codex_identity(self):
        claude_manifest = json.loads(
            (PLUGIN / ".claude-plugin" / "plugin.json").read_text()
        )
        codex_manifest = json.loads(
            (PLUGIN / ".codex-plugin" / "plugin.json").read_text()
        )
        self.assertEqual(claude_manifest["name"], PLUGIN.name)
        self.assertEqual(claude_manifest["name"], codex_manifest["name"])
        self.assertEqual(claude_manifest["version"], PLUGIN_VERSION)
        self.assertEqual(codex_manifest["version"], PLUGIN_VERSION)
        self.assertEqual(claude_manifest["author"]["name"], "Zensets")
        self.assertEqual(
            claude_manifest["repository"], "https://github.com/zensets/plugins"
        )

    def test_claude_manifest_declares_skills_and_mcp(self):
        claude_manifest = json.loads(
            (PLUGIN / ".claude-plugin" / "plugin.json").read_text()
        )
        self.assertEqual(claude_manifest["skills"], "./skills/")
        self.assertEqual(claude_manifest["mcpServers"], "./.mcp.json")

    def test_codex_manifest_declares_interface_assets(self):
        codex_manifest = json.loads(
            (PLUGIN / ".codex-plugin" / "plugin.json").read_text()
        )
        interface = codex_manifest["interface"]
        self.assertEqual(interface["composerIcon"], "./assets/icon.png")
        self.assertEqual(interface["logo"], "./assets/icon.png")

    def test_plugin_icon_exists_at_high_resolution(self):
        self.assertTrue(ICON_PATH.is_file(), f"missing icon at {ICON_PATH}")
        if Image is None:
            self.skipTest("Pillow not installed")
        with Image.open(ICON_PATH) as image:
            width, height = image.size
        self.assertGreaterEqual(width, MIN_ICON_SIZE)
        self.assertGreaterEqual(height, MIN_ICON_SIZE)
        self.assertEqual(width, height)

    def test_every_openai_yaml_declares_builtgraph_mcp_dependency(self):
        missing = []
        for path in sorted((PLUGIN / "skills").glob("*/agents/openai.yaml")):
            text = path.read_text()
            if "dependencies:" not in text:
                missing.append(f"{path.parents[1].name}: missing dependencies")
                continue
            if BUILTGRAPH_MCP_URL not in text:
                missing.append(f"{path.parents[1].name}: missing MCP url")
            if "value: builtgraph" not in text:
                missing.append(f"{path.parents[1].name}: missing MCP value")
            if "transport: streamable_http" not in text:
                missing.append(f"{path.parents[1].name}: missing transport")
        self.assertEqual(missing, [])

    def test_connect_guide_covers_all_hosts(self):
        guide = (PLUGIN / "skills" / "get-started" / "references" /
                 "connect-builtgraph.md").read_text()
        for host in (
            "Claude and Claude Desktop",
            "Claude Code",
            "ChatGPT",
            "Codex",
            BUILTGRAPH_MCP_URL,
            "george@zensets.com",
        ):
            self.assertIn(host, guide)

    def test_root_readme_covers_all_hosts(self):
        readme = (ROOT / "README.md").read_text()
        for host in (
            "Claude and Claude Desktop",
            "Claude Code",
            "ChatGPT",
            "Codex",
            BUILTGRAPH_MCP_URL,
            "george@zensets.com",
        ):
            self.assertIn(host, readme)

    def test_harness_guide_documents_marketplaces(self):
        harness = (ROOT / "docs" / "HARNESS.md").read_text()
        for value in (
            ".claude-plugin/marketplace.json",
            ".agents/plugins/marketplace.json",
            "assets/icon.png",
            BUILTGRAPH_MCP_URL,
        ):
            self.assertIn(value, harness)

    def test_get_started_skill_links_connect_guide(self):
        skill = (PLUGIN / "skills" / "get-started" / "SKILL.md").read_text()
        self.assertIn("connect-builtgraph.md", skill)

    def test_plugin_homepage_points_to_zensets(self):
        claude_manifest = json.loads(
            (PLUGIN / ".claude-plugin" / "plugin.json").read_text()
        )
        codex_manifest = json.loads(
            (PLUGIN / ".codex-plugin" / "plugin.json").read_text()
        )
        self.assertEqual(claude_manifest["homepage"], "https://zensets.com")
        self.assertEqual(codex_manifest["homepage"], "https://zensets.com")

    def test_shared_skills_and_mcp_config_are_present(self):
        skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 17)

        mcp = json.loads((PLUGIN / ".mcp.json").read_text())
        builtgraph = mcp["mcpServers"]["builtgraph"]
        self.assertEqual(builtgraph["type"], "http")
        self.assertEqual(builtgraph["url"], BUILTGRAPH_MCP_URL)


if __name__ == "__main__":
    unittest.main()
