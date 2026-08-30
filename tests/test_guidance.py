import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAGES = ("discover", "validate", "plan", "track")
REQUIRED_SECTIONS = (
    "## 一句话本质",
    "## 进入条件",
    "## 主动讲授",
    "## Agent 动作",
    "## 用户决策",
    "## 表达示例",
    "## 成功信号",
    "## 常见误区",
    "## 状态写入",
    "## 下一步路由",
)


class GuidanceContractTests(unittest.TestCase):
    def test_lifecycle_guidance_covers_revalidation_resume_and_new_projects(self):
        plan = (ROOT / "references" / "stages" / "plan.md").read_text(encoding="utf-8")
        track = (ROOT / "references" / "stages" / "track.md").read_text(encoding="utf-8")

        self.assertIn("`phase=validate`", plan)
        self.assertIn("`paused` → `track`", track)
        self.assertIn("新项目根目录", track)
        self.assertIn("不得覆盖旧项目历史", track)

    def test_authorization_guidance_reuses_only_exact_session_scope(self):
        safety = (ROOT / "references" / "safety-boundaries.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("同一会话", safety)
        self.assertIn("完全相同的已授权范围", safety)
        self.assertIn("扩大范围", safety)
        self.assertIn("不得推断为持久授权", safety)

    def test_golden_examples_cover_core_good_and_bad_guidance_patterns(self):
        positive = ROOT / "tests" / "fixtures" / "guidance-positive.md"
        negative = ROOT / "tests" / "fixtures" / "guidance-negative.md"
        self.assertTrue(positive.is_file())
        self.assertTrue(negative.is_file())
        positive_text = positive.read_text(encoding="utf-8")
        negative_text = negative.read_text(encoding="utf-8")
        for marker in ("先给判断", "单一决定", "打断后回主线", "证据化推荐"):
            with self.subTest(marker=marker):
                self.assertIn(marker, positive_text)
        for marker in ("连续盘问", "随机点子列表", "无证据原创声明", "Track 越界开发"):
            with self.subTest(marker=marker):
                self.assertIn(marker, negative_text)

    def test_every_stage_exposes_the_complete_guidance_contract(self):
        for stage in STAGES:
            text = (ROOT / "references" / "stages" / f"{stage}.md").read_text(
                encoding="utf-8"
            )
            with self.subTest(stage=stage):
                positions = [text.find(section) for section in REQUIRED_SECTIONS]
                self.assertNotIn(-1, positions)
                self.assertEqual(positions, sorted(positions))


if __name__ == "__main__":
    unittest.main()
