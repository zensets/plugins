import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "builtgraph"
TOOL_NAMES = {
    "search_entities", "get_entity", "get_related", "get_portfolio",
    "rank_firms_by_sector", "sector_competition", "get_client_activity",
    "find_buildings", "get_building_team", "find_zoning_activity",
    "get_environmental_seats",
}


class PublicPluginTests(unittest.TestCase):
    def test_distribution_contains_no_executable_scripts(self):
        scripts = sorted(path.relative_to(PLUGIN).as_posix()
                         for path in PLUGIN.rglob("*")
                         if path.is_file() and "scripts" in path.parts)
        self.assertEqual(scripts, [])

    def test_distribution_contains_no_internal_contracts(self):
        forbidden = {"data-contract.md", "scoring-contract.md"}
        found = sorted(path.name for path in PLUGIN.rglob("*") if path.name in forbidden)
        self.assertEqual(found, [])

    def test_public_guidance_does_not_duplicate_tool_catalog(self):
        markdown = "\n".join(path.read_text() for path in PLUGIN.rglob("*.md"))
        exposed = sorted(name for name in TOOL_NAMES if name in markdown)
        self.assertEqual(exposed, [])

    def test_public_guidance_declares_mcp_schema_authority(self):
        guidance = (PLUGIN / "skills" / "query-builtgraph" / "references" /
                    "live-mcp-playbook.md").read_text()
        self.assertIn("authoritative contract", guidance)

    def test_all_specialist_skills_link_public_guidance(self):
        missing = []
        for path in (PLUGIN / "skills").glob("*/SKILL.md"):
            if path.parent.name != "query-builtgraph" and "live-mcp-playbook.md" not in path.read_text():
                missing.append(path.parent.name)
        self.assertEqual(sorted(missing), [])

    def test_active_architect_guidance_requires_scope_and_timing_validation(self):
        guidance = (PLUGIN / "skills" / "query-builtgraph" / "references" /
                    "live-mcp-playbook.md").read_text()
        for value in (
            "Confirmed active architect",
            "Strong active indication",
            "Filing professional only",
            "Historical architect",
            "scope_match",
            "capital_event_alignment",
        ):
            self.assertIn(value, guidance)

        opportunities = (PLUGIN / "skills" / "find-potential-opportunities" /
                         "SKILL.md").read_text()
        permits = (PLUGIN / "skills" / "research-permits-and-teams" /
                   "SKILL.md").read_text()
        self.assertIn("active-architect validation", opportunities)
        self.assertIn("Join each professional to the relevant filing", permits)


if __name__ == "__main__":
    unittest.main()
