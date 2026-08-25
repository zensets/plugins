import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASES = json.loads((ROOT / "internal" / "evals" / "answer_quality_cases.json").read_text())
RUBRIC = (ROOT / "internal" / "evals" / "answer_quality_rubric.md").read_text()
PLUGIN = ROOT / "plugins" / "builtgraph"


class AnswerQualityContractTests(unittest.TestCase):
    def test_cases_are_named_and_balanced(self):
        self.assertGreaterEqual(len(CASES), 6)
        self.assertEqual(len(CASES), len({case["id"] for case in CASES}))
        categories = {case["category"] for case in CASES}
        self.assertEqual(categories, {"aec_bd", "real_estate", "boundary"})

    def test_cases_are_reproducible_and_have_acceptance_criteria(self):
        for case in CASES:
            self.assertIn(f'${case["skill"]}', case["prompt"])
            self.assertGreaterEqual(len(case["must_include"]), 3)
            self.assertGreaterEqual(len(case["must_not_claim"]), 2)

    def test_case_skills_exist(self):
        skills = {path.parent.name for path in (PLUGIN / "skills").glob("*/SKILL.md")}
        self.assertEqual(sorted({case["skill"] for case in CASES} - skills), [])

    def test_rubric_covers_usefulness_and_evidence_discipline(self):
        for heading in (
            "Decision relevance", "Specificity", "Traceability", "Interpretation",
            "Evidence discipline", "Next-action quality", "Concision and scanability",
        ):
            self.assertIn(heading, RUBRIC)
        self.assertIn("critical failure", RUBRIC)

    def test_public_playbook_requires_prioritized_answers(self):
        playbook = (PLUGIN / "skills" / "query-builtgraph" / "references" / "live-mcp-playbook.md").read_text()
        self.assertIn("decision-relevant finding", playbook)
        self.assertIn("most useful few results", playbook)
        self.assertIn("Offer an appendix", playbook)
        self.assertIn("procurement status is unknown", playbook)
        self.assertIn("do not repeat the source label", playbook)


if __name__ == "__main__":
    unittest.main()
