import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "carpe_diem.py"


def run(command, cwd):
    return subprocess.run(
        command, cwd=cwd, text=True, capture_output=True, check=False
    )


def run_cli(*args):
    return run([sys.executable, str(CLI), *args], ROOT)


class GitEvidenceTests(unittest.TestCase):
    def make_repo(self, directory):
        repo = Path(directory) / "repo"
        repo.mkdir()
        self.assertEqual(run(["git", "init", "-q"], repo).returncode, 0)
        self.assertEqual(
            run(["git", "config", "user.email", "test@example.com"], repo).returncode,
            0,
        )
        self.assertEqual(
            run(["git", "config", "user.name", "Test User"], repo).returncode, 0
        )
        return repo

    def test_git_evidence_reports_head_and_dirty_state_without_changing_repo(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = self.make_repo(directory)
            tracked = repo / "tracked.txt"
            tracked.write_text("first\n", encoding="utf-8")
            self.assertEqual(run(["git", "add", "tracked.txt"], repo).returncode, 0)
            self.assertEqual(
                run(["git", "commit", "-q", "-m", "first"], repo).returncode, 0
            )
            head = run(["git", "rev-parse", "HEAD"], repo).stdout.strip()
            tracked.write_text("changed\n", encoding="utf-8")
            (repo / "untracked.txt").write_text("new\n", encoding="utf-8")
            before = run(["git", "status", "--porcelain=v1"], repo).stdout

            result = run_cli("evidence", "git", "--root", str(repo), "--json")

            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["head"], head)
            self.assertTrue(payload["dirty"])
            self.assertIn("tracked.txt", payload["changed_paths"])
            self.assertIn("untracked.txt", payload["changed_paths"])
            after = run(["git", "status", "--porcelain=v1"], repo).stdout
            self.assertEqual(after, before)

    def test_git_evidence_compares_current_head_to_recorded_ancestor(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = self.make_repo(directory)
            tracked = repo / "tracked.txt"
            tracked.write_text("first\n", encoding="utf-8")
            run(["git", "add", "tracked.txt"], repo)
            run(["git", "commit", "-q", "-m", "first"], repo)
            first_head = run(["git", "rev-parse", "HEAD"], repo).stdout.strip()
            tracked.write_text("second\n", encoding="utf-8")
            run(["git", "add", "tracked.txt"], repo)
            run(["git", "commit", "-q", "-m", "second"], repo)

            result = run_cli(
                "evidence", "git", "--root", str(repo), "--since", first_head, "--json"
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["history_relationship"], "ancestor")
            self.assertEqual([item["subject"] for item in payload["commits"]], ["second"])
            self.assertEqual(payload["committed_paths"], ["tracked.txt"])


if __name__ == "__main__":
    unittest.main()
