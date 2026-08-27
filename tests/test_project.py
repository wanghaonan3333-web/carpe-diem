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


class ProjectStateTests(unittest.TestCase):
    def test_project_init_creates_only_local_carpe_diem_state(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / "project"
            project.mkdir()

            result = run_cli("project", "init", "--root", str(project), "--json")

            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["status"], "created")
            state_path = project / ".carpe-diem" / "project-state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(state["phase"], "discover")
            self.assertEqual(state["revision"], 1)
            self.assertTrue((project / ".carpe-diem" / "events").is_dir())
            self.assertEqual({path.name for path in project.iterdir()}, {".carpe-diem"})

    def test_project_event_updates_phase_and_keeps_an_immutable_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / "project"
            project.mkdir()
            initialized = run_cli("project", "init", "--root", str(project), "--json")
            self.assertEqual(initialized.returncode, 0, initialized.stderr)

            recorded = run_cli(
                "project",
                "event",
                "--root",
                str(project),
                "--expected-revision",
                "1",
                "--phase",
                "validate",
                "--summary",
                "用户确认项目发现与启动 Skill 方向",
                "--next",
                "调查直接竞品与替代行为",
                "--json",
            )

            self.assertEqual(recorded.returncode, 0, recorded.stderr)
            payload = json.loads(recorded.stdout)
            self.assertEqual(payload["revision"], 2)
            state_path = project / ".carpe-diem" / "project-state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(state["phase"], "validate")
            self.assertEqual(state["next_recommended"], "调查直接竞品与替代行为")
            event_files = list((project / ".carpe-diem" / "events").glob("*.json"))
            self.assertEqual(len(event_files), 1)
            event = json.loads(event_files[0].read_text(encoding="utf-8"))
            self.assertEqual(event["summary"], "用户确认项目发现与启动 Skill 方向")
            self.assertEqual(event["base_revision"], 1)


if __name__ == "__main__":
    unittest.main()
