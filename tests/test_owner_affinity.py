import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "plugins/builtgraph/skills/score-builtgraph-opportunities/scripts/analyze_owner_affinity.py"
FIXTURE = ROOT / "tests/fixtures/basic"
SPEC = importlib.util.spec_from_file_location("owner_affinity", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class OwnerAffinityTests(unittest.TestCase):
    def test_known_selected_firm_leads_owner_history(self):
        result = MODULE.analyze(FIXTURE, "owner1", "firm1", "architect", date(2026, 8, 21))
        self.assertEqual(result["candidate_owner_selections"], 2)
        self.assertEqual(result["top_incumbent_id"], "firm1")
        self.assertEqual(result["assessment"], "observed_incumbent_or_leader")
        self.assertFalse(result["cold_start"])
        self.assertEqual(result["calibration_status"], "not_a_calibrated_win_probability")

    def test_other_role_is_not_mislabeled_as_architect(self):
        result = MODULE.analyze(FIXTURE, "owner1", "gc1", "architect", date(2026, 8, 21))
        self.assertEqual(result["candidate_owner_selections"], 0)
        self.assertTrue(result["cold_start"])

    def test_point_in_time_excludes_future_selection(self):
        result = MODULE.analyze(FIXTURE, "owner1", "firm1", "architect", date(2022, 1, 1))
        self.assertEqual(result["candidate_owner_selections"], 1)
        self.assertGreater(result["excluded_future_rows"], 0)

    def test_cli_writes_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "affinity.json"
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), str(FIXTURE), "--owner-id", "owner1",
                 "--firm-id", "firm1", "--role", "architect", "--as-of", "2026-08-21",
                 "--output", str(output)],
                check=True, capture_output=True, text=True,
            )
            self.assertIn("winner-only-owner-affinity-v1", completed.stdout)
            self.assertEqual(json.loads(output.read_text())["candidate_owner_selections"], 2)


if __name__ == "__main__":
    unittest.main()
