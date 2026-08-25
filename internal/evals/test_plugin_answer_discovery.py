import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PLUGIN = ROOT / "plugins" / "builtgraph"
PLAYBOOK = PLUGIN / "skills" / "query-builtgraph" / "references" / "live-mcp-playbook.md"
QUESTIONS = json.loads((ROOT / "internal" / "evals" / "golden_questions.json").read_text())

TOOLS = {
    "search_entities", "get_entity", "get_related", "get_portfolio",
    "rank_firms_by_sector", "sector_competition", "get_client_activity",
    "find_buildings", "get_building_team", "find_zoning_activity",
    "get_environmental_seats",
}


class PluginAnswerDiscoveryTests(unittest.TestCase):
    def test_balanced_golden_corpus_has_thirty_unique_questions(self):
        self.assertEqual(len(QUESTIONS), 30)
        self.assertEqual(len({row["id"] for row in QUESTIONS}), 30)
        counts = {category: sum(q["category"] == category for q in QUESTIONS)
                  for category in {q["category"] for q in QUESTIONS}}
        self.assertGreaterEqual(counts.get("aec_bd", 0), 10)
        self.assertGreaterEqual(counts.get("real_estate", 0), 10)
        self.assertGreaterEqual(counts.get("boundary", 0), 8)

    def test_every_live_tool_has_a_golden_question(self):
        covered = {tool for row in QUESTIONS for tool in row["tools"]}
        self.assertEqual(sorted(TOOLS - covered), [])

    def test_golden_questions_reference_existing_skills(self):
        skill_names = {path.parent.name for path in (PLUGIN / "skills").glob("*/SKILL.md")}
        missing = sorted({row["skill"] for row in QUESTIONS} - skill_names)
        self.assertEqual(missing, [])

    def test_specialist_skills_link_live_contract(self):
        missing = []
        for path in (PLUGIN / "skills").glob("*/SKILL.md"):
            if path.parent.name != "query-builtgraph" and "live-mcp-playbook.md" not in path.read_text():
                missing.append(path.parent.name)
        self.assertEqual(sorted(missing), [])

    def test_query_skill_uses_live_schema_as_authority(self):
        text = (PLUGIN / "skills" / "query-builtgraph" / "SKILL.md").read_text()
        self.assertIn("authoritative contract", text)
        self.assertNotIn("Offline CSV fallback", text)

    def test_every_ui_prompt_names_its_skill(self):
        missing = []
        for path in (PLUGIN / "skills").glob("*/agents/openai.yaml"):
            if f"${path.parents[1].name}" not in path.read_text():
                missing.append(path.parents[1].name)
        self.assertEqual(sorted(missing), [])


if __name__ == "__main__":
    unittest.main()
