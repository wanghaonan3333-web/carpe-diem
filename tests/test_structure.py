import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillStructureTests(unittest.TestCase):
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
            "SKILL.md",
            "references/methodology.md",
            "references/state-schema.md",
            "references/safety-boundaries.md",
            "references/stages/discover.md",
            "references/stages/validate.md",
            "references/stages/plan.md",
            "references/stages/track.md",
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


if __name__ == "__main__":
    unittest.main()
