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


class SkillInstallTests(unittest.TestCase):
    def test_install_plan_rejects_manifest_path_outside_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            (root / "outside.txt").write_text("outside", encoding="utf-8")
            (source / "manifest.json").write_text(
                json.dumps(
                    {
                        "name": "carpe-diem",
                        "version": "0.1.1",
                        "schema_version": 1,
                        "files": ["../outside.txt"],
                    }
                ),
                encoding="utf-8",
            )

            result = run_cli(
                "install",
                "plan",
                "--platform",
                "codex",
                "--source",
                str(source),
                "--target",
                str(root / "target"),
                "--json",
            )

            self.assertEqual(result.returncode, 2)
            self.assertIn("unsafe snapshot path", result.stderr)

    def test_install_plan_rejects_absolute_manifest_path(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            outside = root / "outside.txt"
            outside.write_text("outside", encoding="utf-8")
            (source / "manifest.json").write_text(
                json.dumps(
                    {
                        "name": "carpe-diem",
                        "version": "0.1.1",
                        "schema_version": 1,
                        "files": [str(outside)],
                    }
                ),
                encoding="utf-8",
            )

            result = run_cli(
                "install",
                "plan",
                "--platform",
                "codex",
                "--source",
                str(source),
                "--target",
                str(root / "target"),
                "--json",
            )

            self.assertEqual(result.returncode, 2)
            self.assertIn("unsafe snapshot path", result.stderr)

    def test_install_apply_rejects_tampered_plan_path(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            outside = root / "outside.txt"
            outside.write_text("outside", encoding="utf-8")
            plan_path = root / "install-plan.json"
            plan_path.write_text(
                json.dumps(
                    {
                        "plan_version": 1,
                        "operation": "install",
                        "platform": "codex",
                        "source": str(source),
                        "target": str(root / "target"),
                        "version": "0.1.1",
                        "fingerprint": "not-relevant",
                        "files": ["../outside.txt"],
                    }
                ),
                encoding="utf-8",
            )

            result = run_cli(
                "install", "apply", "--plan", str(plan_path), "--yes", "--json"
            )

            self.assertEqual(result.returncode, 2)
            self.assertIn("unsafe snapshot path", result.stderr)
            self.assertFalse((root / "target").exists())

    def test_detect_reports_platform_roots_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            (home / ".codex" / "skills").mkdir(parents=True)
            (home / ".cursor" / "skills").mkdir(parents=True)

            result = run_cli("install", "detect", "--home", str(home), "--json")

            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            by_name = {item["platform"]: item for item in payload["platforms"]}
            self.assertTrue(by_name["codex"]["root_exists"])
            self.assertTrue(by_name["cursor"]["root_exists"])
            self.assertFalse(by_name["claude-code"]["root_exists"])
            self.assertFalse(by_name["openclaw"]["root_exists"])
            self.assertEqual(
                by_name["codex"]["target"],
                str(home / ".codex" / "skills" / "carpe-diem"),
            )

    def install_snapshot(self, directory):
        target = Path(directory) / "skills" / "carpe-diem"
        planned = run_cli(
            "install",
            "plan",
            "--platform",
            "codex",
            "--source",
            str(ROOT),
            "--target",
            str(target),
            "--json",
        )
        self.assertEqual(planned.returncode, 0, planned.stderr)
        plan_path = Path(directory) / "install-plan.json"
        plan_path.write_text(planned.stdout, encoding="utf-8")
        installed = run_cli(
            "install", "apply", "--plan", str(plan_path), "--yes", "--json"
        )
        self.assertEqual(installed.returncode, 0, installed.stderr)
        return target

    def test_install_requires_plan_and_confirmation_then_verifies_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "skills" / "carpe-diem"
            planned = run_cli(
                "install",
                "plan",
                "--platform",
                "codex",
                "--source",
                str(ROOT),
                "--target",
                str(target),
                "--json",
            )
            self.assertEqual(planned.returncode, 0, planned.stderr)
            plan = json.loads(planned.stdout)
            self.assertEqual(plan["platform"], "codex")
            self.assertIn("SKILL.md", plan["files"])
            self.assertFalse(target.exists())
            plan_path = Path(directory) / "install-plan.json"
            plan_path.write_text(planned.stdout, encoding="utf-8")

            declined = run_cli("install", "apply", "--plan", str(plan_path))
            self.assertEqual(declined.returncode, 2)
            self.assertFalse(target.exists())

            installed = run_cli(
                "install", "apply", "--plan", str(plan_path), "--yes", "--json"
            )
            self.assertEqual(installed.returncode, 0, installed.stderr)
            self.assertTrue((target / "SKILL.md").is_file())
            self.assertTrue((target / ".carpe-diem-install.json").is_file())

            verified = run_cli("install", "verify", "--target", str(target), "--json")
            self.assertEqual(verified.returncode, 0, verified.stderr)
            self.assertTrue(json.loads(verified.stdout)["valid"])

    def test_uninstall_refuses_to_delete_a_locally_modified_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            target = self.install_snapshot(directory)
            skill = target / "SKILL.md"
            skill.write_text(skill.read_text(encoding="utf-8") + "\nlocal change\n", encoding="utf-8")

            result = run_cli(
                "install", "uninstall", "--target", str(target), "--yes", "--json"
            )

            self.assertEqual(result.returncode, 3)
            self.assertTrue(target.is_dir())
            self.assertIn("changed", result.stderr)


if __name__ == "__main__":
    unittest.main()
