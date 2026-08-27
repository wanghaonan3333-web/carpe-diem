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


class ProfileStateTests(unittest.TestCase):
    def create_proposal(self, profile, directory):
        result = run_cli(
            "state",
            "propose",
            "--profile",
            str(profile),
            "--field",
            "interests",
            "--value",
            "跨 Agent 的本地优先工具",
            "--kind",
            "inferred",
            "--basis",
            "本次项目讨论",
            "--json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        proposal_path = Path(directory) / "proposal.json"
        proposal_path.write_text(result.stdout, encoding="utf-8")
        return proposal_path

    def test_reading_a_missing_profile_returns_new_state_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory) / "me.json"
            result = run_cli("state", "read", "--profile", str(profile), "--json")

            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["status"], "new")
            self.assertEqual(payload["profile"]["handle"], "me")
            self.assertEqual(payload["profile"]["revision"], 0)
            self.assertFalse(profile.exists())

    def test_proposing_an_inference_returns_a_reviewable_diff_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory) / "me.json"
            result = run_cli(
                "state",
                "propose",
                "--profile",
                str(profile),
                "--field",
                "interests",
                "--value",
                "跨 Agent 的本地优先工具",
                "--kind",
                "inferred",
                "--basis",
                "本次项目讨论",
                "--json",
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            proposal = json.loads(result.stdout)
            self.assertEqual(proposal["operation"], "add_profile_fact")
            self.assertEqual(proposal["base_revision"], 0)
            self.assertEqual(proposal["field"], "interests")
            self.assertEqual(proposal["fact"]["confidence"], "candidate")
            self.assertFalse(profile.exists())

    def test_applying_a_reviewed_proposal_persists_a_confirmed_fact(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory) / "profiles" / "me.json"
            proposal = self.create_proposal(profile, directory)

            result = run_cli(
                "state",
                "apply",
                "--profile",
                str(profile),
                "--proposal",
                str(proposal),
                "--json",
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["status"], "applied")
            self.assertEqual(payload["revision"], 1)
            saved = json.loads(profile.read_text(encoding="utf-8"))
            self.assertEqual(saved["interests"][0]["confidence"], "confirmed")
            self.assertIsNotNone(saved["interests"][0]["confirmed_at"])

    def test_stale_proposal_is_rejected_without_overwriting_newer_profile(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory) / "profiles" / "me.json"
            proposal = self.create_proposal(profile, directory)
            first = run_cli(
                "state", "apply", "--profile", str(profile), "--proposal", str(proposal)
            )
            self.assertEqual(first.returncode, 0, first.stderr)

            stale = run_cli(
                "state", "apply", "--profile", str(profile), "--proposal", str(proposal)
            )

            self.assertEqual(stale.returncode, 3)
            self.assertIn("revision conflict", stale.stderr)
            saved = json.loads(profile.read_text(encoding="utf-8"))
            self.assertEqual(saved["revision"], 1)
            self.assertEqual(len(saved["interests"]), 1)

    def test_forgetting_a_confirmed_fact_removes_only_that_fact(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory) / "profiles" / "me.json"
            proposal = self.create_proposal(profile, directory)
            applied = run_cli(
                "state", "apply", "--profile", str(profile), "--proposal", str(proposal)
            )
            self.assertEqual(applied.returncode, 0, applied.stderr)
            saved = json.loads(profile.read_text(encoding="utf-8"))
            fact_id = saved["interests"][0]["id"]

            forgotten = run_cli(
                "state",
                "forget",
                "--profile",
                str(profile),
                "--fact-id",
                fact_id,
                "--expected-revision",
                "1",
                "--json",
            )

            self.assertEqual(forgotten.returncode, 0, forgotten.stderr)
            payload = json.loads(forgotten.stdout)
            self.assertEqual(payload["revision"], 2)
            updated = json.loads(profile.read_text(encoding="utf-8"))
            self.assertEqual(updated["interests"], [])

    def test_correcting_a_fact_requires_a_reviewed_replacement_proposal(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory) / "profiles" / "me.json"
            first_proposal = self.create_proposal(profile, directory)
            applied = run_cli(
                "state", "apply", "--profile", str(profile), "--proposal", str(first_proposal)
            )
            self.assertEqual(applied.returncode, 0, applied.stderr)
            saved = json.loads(profile.read_text(encoding="utf-8"))
            fact_id = saved["interests"][0]["id"]

            proposed = run_cli(
                "state",
                "propose",
                "--profile",
                str(profile),
                "--field",
                "interests",
                "--replace-id",
                fact_id,
                "--value",
                "跨 Agent 的项目引导工具",
                "--kind",
                "explicit",
                "--basis",
                "用户纠正表述",
                "--json",
            )

            self.assertEqual(proposed.returncode, 0, proposed.stderr)
            proposal_payload = json.loads(proposed.stdout)
            self.assertEqual(proposal_payload["operation"], "replace_profile_fact")
            self.assertEqual(proposal_payload["previous_fact"]["id"], fact_id)
            self.assertEqual(
                json.loads(profile.read_text(encoding="utf-8"))["interests"][0]["value"],
                "跨 Agent 的本地优先工具",
            )
            proposal_path = Path(directory) / "replacement.json"
            proposal_path.write_text(proposed.stdout, encoding="utf-8")

            corrected = run_cli(
                "state",
                "apply",
                "--profile",
                str(profile),
                "--proposal",
                str(proposal_path),
                "--json",
            )

            self.assertEqual(corrected.returncode, 0, corrected.stderr)
            updated = json.loads(profile.read_text(encoding="utf-8"))
            self.assertEqual(updated["revision"], 2)
            self.assertEqual(len(updated["interests"]), 1)
            self.assertEqual(updated["interests"][0]["id"], fact_id)
            self.assertEqual(updated["interests"][0]["value"], "跨 Agent 的项目引导工具")

    def test_portable_export_redacts_local_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory) / "me.json"
            raw = {
                "schema_version": 1,
                "handle": "me",
                "revision": 1,
                "updated_at": "2026-08-27T00:00:00Z",
                "strengths": [],
                "interests": [],
                "recurring_frictions": [],
                "constraints": [],
                "project_preferences": [],
                "working_style": [],
                "project_history": [],
                "consents": [
                    {
                        "id": "consent-1",
                        "value": str(Path(directory) / "private-notes"),
                        "kind": "explicit",
                        "confidence": "confirmed",
                        "basis": "用户授权指定目录",
                        "confirmed_at": "2026-08-27T00:00:00Z",
                        "last_used_at": None,
                    }
                ],
            }
            profile.write_text(json.dumps(raw, ensure_ascii=False), encoding="utf-8")

            exported = run_cli("state", "export", "--profile", str(profile), "--json")

            self.assertEqual(exported.returncode, 0, exported.stderr)
            self.assertNotIn(directory, exported.stdout)
            payload = json.loads(exported.stdout)
            self.assertEqual(
                payload["profile"]["consents"][0]["value"], "<redacted-local-path>"
            )

    def test_corrupted_profile_is_reported_without_being_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory) / "me.json"
            original = "{not-json\n"
            profile.write_text(original, encoding="utf-8")

            result = run_cli("state", "read", "--profile", str(profile), "--json")

            self.assertEqual(result.returncode, 4)
            self.assertIn("corrupted", result.stderr)
            self.assertEqual(profile.read_text(encoding="utf-8"), original)


if __name__ == "__main__":
    unittest.main()
