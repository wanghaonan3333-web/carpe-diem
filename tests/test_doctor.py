import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "carpe_diem.py"


def run_cli(*args):
    return subprocess.run(
        [sys.executable, str(CLI), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


class DoctorTests(unittest.TestCase):
    def test_doctor_validates_runtime_without_creating_profile(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory) / "missing-profile.json"

            result = run_cli(
                "doctor",
                "--source",
                str(ROOT),
                "--profile",
                str(profile),
                "--json",
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertTrue(payload["valid"])
            self.assertEqual(payload["errors"], [])
            self.assertFalse(profile.exists())
            self.assertIn("profile_missing", [item["code"] for item in payload["warnings"]])

    def test_doctor_reports_corrupted_profile_without_changing_it(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory) / "profile.json"
            original = "{broken"
            profile.write_text(original, encoding="utf-8")

            result = run_cli(
                "doctor",
                "--source",
                str(ROOT),
                "--profile",
                str(profile),
                "--json",
            )

            self.assertEqual(result.returncode, 1)
            payload = json.loads(result.stdout)
            self.assertFalse(payload["valid"])
            self.assertIn("profile_corrupted", [item["code"] for item in payload["errors"]])
            self.assertEqual(profile.read_text(encoding="utf-8"), original)


if __name__ == "__main__":
    unittest.main()
