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
