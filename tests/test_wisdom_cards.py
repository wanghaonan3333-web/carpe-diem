import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_wisdom_cards.py"
ROUTING_CASES = (
    ROOT / "references" / "wisdom" / "mentors" / "routing-acceptance-cases.json"
)


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_wisdom_cards", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class WisdomCardTests(unittest.TestCase):
    def test_wisdom_library_invariants(self):
        validator = load_validator()
        self.assertEqual(validator.validate(), [])

    def test_routing_uses_a_two_card_context_budget(self):
        zh = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        en = (ROOT / "SKILL.en.md").read_text(encoding="utf-8")
        self.assertIn("每轮最多加载 1 张主卡", zh)
        self.assertIn("at most one primary mentor card", en)
        self.assertIn("不超过两张", (ROOT / "references/wisdom/mentors/README.md").read_text(encoding="utf-8"))

    def test_near_neighbor_routing_decisions(self):
        cases = json.loads(ROUTING_CASES.read_text(encoding="utf-8"))["cases"]
        by_id = {case["id"]: case for case in cases}
        expected_primary = {
            "validate-frame-before-experiment": "validate/test-card.md",
            "validate-choose-experiment": "validate/experiment-design.md",
            "validate-decide-after-experiment": "validate/gonogo-decision.md",
            "scope-before-commit": "cross/say-no-by-default.md",
            "scope-already-growing": "cross/feature-creep.md",
            "rfc-before-decision": "plan/rfc-design.md",
            "adr-after-decision": "plan/adr-rfc-enhance.md",
            "retention-existing-users-leave": "cross/user-retention.md",
            "growth-no-repeatable-loop": "cross/growth-flywheel.md",
        }
        for case_id, primary in expected_primary.items():
            with self.subTest(case_id=case_id):
                self.assertEqual(by_id[case_id]["primary"], primary)

    def test_routing_cases_respect_selection_and_exclusion_boundaries(self):
        cases = json.loads(ROUTING_CASES.read_text(encoding="utf-8"))["cases"]
        mentors = ROUTING_CASES.parent
        for case in cases:
            with self.subTest(case_id=case["id"]):
                selected = {
                    card
                    for card in (case["primary"], case["supporting"])
                    if card is not None
                }
                self.assertLessEqual(len(selected), 2)
                self.assertTrue(selected.isdisjoint(case["must_not_select"]))
                for relative in selected | set(case["must_not_select"]):
                    self.assertTrue((mentors / relative).is_file(), relative)


if __name__ == "__main__":
    unittest.main()
