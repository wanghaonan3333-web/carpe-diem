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


class PlanValidationTests(unittest.TestCase):
    COMPLETE_BODY = """

## 摘要与问题
解决一个明确问题。
## 目标用户与核心场景
面向开发者。
## 价值假设和差异化证据
差异化结论附带来源。
## 目标与非目标
目标和非目标明确。
## 用户体验和功能范围
用户流程和版本范围明确。
## 架构、组件、数据流和接口
模块边界、数据流和接口明确。
## 错误处理、安全和隐私
失败路径和隐私边界明确。
## 测试和验收
通过公开接口验证行为。
## 里程碑、任务和依赖
M1：完成第一个模块。验收标准：公开接口测试通过。
## 风险与降级
缺少网络时明确降级。
## 开源、贡献和发布方式
使用开放许可证并提供贡献流程。
## 关键决策记录
记录已经确认的范围决定。
"""

    def test_incomplete_plan_is_blocked_with_actionable_reasons(self):
        with tempfile.TemporaryDirectory() as directory:
            plan = Path(directory) / "project-plan.md"
            plan.write_text(
                "# 项目实施计划\n\n## 摘要与问题\n\nTODO\n", encoding="utf-8"
            )

            result = run_cli("plan", "validate", "--file", str(plan), "--json")

            self.assertEqual(result.returncode, 1)
            payload = json.loads(result.stdout)
            self.assertFalse(payload["valid"])
            codes = {blocker["code"] for blocker in payload["blockers"]}
            self.assertIn("placeholder", codes)
            self.assertIn("missing_section", codes)

    def test_plan_with_empty_section_and_no_acceptance_criteria_is_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            plan = Path(directory) / "project-plan.md"
            plan.write_text(
                """# 项目实施计划

## 摘要与问题
解决一个明确问题。
## 目标用户与核心场景
面向开发者。
## 价值假设和差异化证据
有来源的证据。
## 目标与非目标
范围明确。
## 用户体验和功能范围
用户流程明确。
## 架构、组件、数据流和接口
模块边界明确。
## 错误处理、安全和隐私
失败路径明确。
## 测试和验收
通过公开接口测试。
## 里程碑、任务和依赖
M1：完成第一个模块。
## 风险与降级
缺少网络时降级。
## 开源、贡献和发布方式
公开发布。
## 关键决策记录

""",
                encoding="utf-8",
            )

            result = run_cli("plan", "validate", "--file", str(plan), "--json")

            self.assertEqual(result.returncode, 1)
            codes = {item["code"] for item in json.loads(result.stdout)["blockers"]}
            self.assertIn("empty_section", codes)
            self.assertIn("missing_acceptance_criteria", codes)

    def test_complete_plan_requires_canonical_title_and_then_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            plan = Path(directory) / "project-plan.md"
            plan.write_text("# 随便的标题\n" + self.COMPLETE_BODY, encoding="utf-8")

            wrong_title = run_cli("plan", "validate", "--file", str(plan), "--json")
            self.assertEqual(wrong_title.returncode, 1)
            codes = {item["code"] for item in json.loads(wrong_title.stdout)["blockers"]}
            self.assertIn("missing_title", codes)

            plan.write_text("# 项目实施计划\n" + self.COMPLETE_BODY, encoding="utf-8")
            complete = run_cli("plan", "validate", "--file", str(plan), "--json")
            self.assertEqual(complete.returncode, 0, complete.stdout + complete.stderr)
            self.assertTrue(json.loads(complete.stdout)["valid"])

    def test_plan_diff_reports_reviewable_changes_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            before = Path(directory) / "project-plan.md"
            after_dir = Path(directory) / "candidate"
            after_dir.mkdir()
            after = after_dir / "project-plan.md"
            before.write_text("# 项目实施计划\n\n旧范围\n", encoding="utf-8")
            after.write_text("# 项目实施计划\n\n新范围\n", encoding="utf-8")

            result = run_cli(
                "plan",
                "diff",
                "--before",
                str(before),
                "--after",
                str(after),
                "--json",
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertTrue(payload["changed"])
            self.assertIn("+新范围", payload["diff"])
            self.assertEqual(before.read_text(encoding="utf-8"), "# 项目实施计划\n\n旧范围\n")


if __name__ == "__main__":
    unittest.main()
