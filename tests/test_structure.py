import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillStructureTests(unittest.TestCase):
    def test_open_source_repository_scaffold_is_complete(self):
        required = (
            "README.md",
            "LICENSE",
            "CONTRIBUTING.md",
            "CODE_OF_CONDUCT.md",
            ".github/ISSUE_TEMPLATE/bug_report.yml",
            ".github/ISSUE_TEMPLATE/feature_request.yml",
            ".github/workflows/ci.yml",
            "docs/internal-testing.md",
        )
        for relative_path in required:
            with self.subTest(resource=relative_path):
                self.assertTrue((ROOT / relative_path).is_file())

        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Apache License", license_text)
        self.assertIn("Version 2.0", license_text)

    def test_readme_offers_english_and_chinese_descriptions(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese_path = ROOT / "README.zh-CN.md"
        self.assertTrue(chinese_path.is_file())
        chinese = chinese_path.read_text(encoding="utf-8")
        self.assertIn("[简体中文](README.zh-CN.md)", english)
        self.assertIn("[English](README.md)", chinese)
        self.assertIn("An open-source Agent Skill", english)
        self.assertIn("开源 Agent Skill", chinese)

    def test_skill_entrypoint_has_discoverable_frontmatter(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        frontmatter = text.split("---", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name: carpe-diem$")
        self.assertRegex(frontmatter, r"(?m)^description: .+项目.+$")
        self.assertNotRegex(frontmatter, r"(?m)^disable-model-invocation:")

    def test_manifest_identifies_versioned_skill_entrypoint(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "carpe-diem")
        self.assertEqual(manifest["version"], "0.1.0")
        self.assertEqual(manifest["schema_version"], 1)
        self.assertIn("SKILL.md", manifest["files"])

    def test_manifest_tracks_every_runtime_resource(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        required = {
            "manifest.json",
            "SKILL.md",
            "adapters/codex/INSTALL.md",
            "adapters/claude-code/INSTALL.md",
            "adapters/cursor/INSTALL.md",
            "adapters/openclaw/INSTALL.md",
            "references/methodology.md",
            "references/state-schema.md",
            "references/safety-boundaries.md",
            "references/stages/discover.md",
            "references/stages/validate.md",
            "references/stages/plan.md",
            "references/stages/track.md",
            "templates/project-plan.md",
            "templates/project-handoff.md",
            "templates/progress-summary.md",
            "scripts/carpe_diem.py",
        }
        self.assertTrue(required.issubset(set(manifest["files"])))

    def test_entrypoint_routes_to_each_stage_reference(self):
        entrypoint = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        stage_paths = [
            "references/stages/discover.md",
            "references/stages/validate.md",
            "references/stages/plan.md",
            "references/stages/track.md",
        ]
        for relative_path in stage_paths:
            with self.subTest(stage=relative_path):
                self.assertIn(relative_path, entrypoint)
                self.assertTrue((ROOT / relative_path).is_file())

    def test_entrypoint_links_shared_state_and_safety_contracts(self):
        entrypoint = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        shared_paths = (
            "references/methodology.md",
            "references/state-schema.md",
            "references/safety-boundaries.md",
            "scripts/carpe_diem.py",
        )
        for relative_path in shared_paths:
            with self.subTest(resource=relative_path):
                self.assertIn(relative_path, entrypoint)
                self.assertTrue((ROOT / relative_path).is_file())

    def test_entrypoint_names_exact_read_only_resume_commands(self):
        entrypoint = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for command in ("state read", "project status", "evidence git"):
            with self.subTest(command=command):
                self.assertIn(command, entrypoint)
        self.assertIn("不要为了发现接口而通读脚本源码", entrypoint)

    def test_plan_stage_links_each_output_template(self):
        plan_stage = (ROOT / "references" / "stages" / "plan.md").read_text(
            encoding="utf-8"
        )
        templates = (
            "templates/project-plan.md",
            "templates/project-handoff.md",
            "templates/progress-summary.md",
        )
        for relative_path in templates:
            with self.subTest(template=relative_path):
                self.assertIn(relative_path, plan_stage)
                self.assertTrue((ROOT / relative_path).is_file())


if __name__ == "__main__":
    unittest.main()
