"""Tests for validate.py: the real content must pass, and each kind of mistake must be caught.

Run with:  python -m unittest discover -s tests
"""
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import validate  # noqa: E402


class ValidateContent(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.content = self.tmp / "content"
        shutil.copytree(ROOT / "content", self.content)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def edit(self, rel, old, new):
        p = self.content / rel
        text = p.read_text(encoding="utf-8")
        self.assertIn(old, text, f"test setup: '{old}' not found in {rel}")
        p.write_text(text.replace(old, new, 1), encoding="utf-8")

    def errors(self):
        return "\n".join(validate.validate(self.content).errors)

    def assertCaught(self, *fragments):
        errs = self.errors()
        self.assertTrue(errs, "expected the validator to report an error, but it passed")
        for f in fragments:
            self.assertIn(f, errs)

    def test_real_content_passes(self):
        rep = validate.validate(self.content)
        self.assertEqual(rep.errors, [])
        self.assertEqual(rep.warnings, [])

    def test_bad_yaml_indentation(self):
        self.edit("lab-1.1/lab.yml", "  - id: issues\n    title: Open Issues", "  - id: issues\n   title: Open Issues")
        self.assertCaught("lab-1.1", "YAML is not valid")

    def test_typo_in_setting_name_suggests_fix(self):
        self.edit("lab-1.1/lab.yml", "kind: textarea, rows: 2, label: \"One sentence", "kind: textarea, rows: 2, lable: \"One sentence")
        self.assertCaught("unknown setting 'lable'", "did you mean 'label'")

    def test_missing_source_file(self):
        self.edit("lab-3.1/lab.yml", "source: reviewer-log.csv", "source: reviewer-logs.csv")
        self.assertCaught("lab-3.1", "reviewer-logs.csv", "does not exist")

    def test_computed_column_typo_suggests_fix(self):
        self.edit("lab-3.1/lab.yml", "differs: [ai_decision, human_decision]", "differs: [ai_decison, human_decision]")
        self.assertCaught("ai_decison", "did you mean 'ai_decision'")

    def test_duplicate_field_id_in_a_lab(self):
        self.edit("lab-3.1/lab.yml", "{id: low_rate,", "{id: low_who,")
        self.assertCaught("'low_who' is already used", "unique")

    def test_duplicate_tab_title(self):
        self.edit("lab-3.1/lab.yml", "title: My Findings", "title: Reviewer Log")
        self.assertCaught("same title")

    def test_select_field_without_options(self):
        self.edit("lab-4.1/lab.yml", "{id: i2-urg, kind: select, label: \"Urgency\", options: *urg}", "{id: i2-urg, kind: select, label: \"Urgency\"}")
        self.assertCaught("i2-urg", "options")

    def test_unknown_field_kind(self):
        self.edit("lab-1.1/lab.yml", "{id: tier, kind: text,", "{id: tier, kind: txt,")
        self.assertCaught("kind 'txt'", "did you mean 'text'")

    def test_editable_column_missing_from_csv(self):
        self.edit("lab-1.1/lab.yml", "- column: owner", "- column: ownr")
        self.assertCaught("'ownr' is not in the CSV", "did you mean 'owner'")

    def test_scorecard_column_that_is_not_zero_or_one(self):
        self.edit("lab-2.2/lab.yml", "current: current_score_c1, baseline: baseline_score_c1}\n        - {label: \"c2 Exact figure or entitlement\", current: current_score_c2, baseline: baseline_score_c2}\n        - {label: \"c3 Answers the question asked\", current: current_score_c3, baseline: baseline_score_c3}\n        - {label: \"c4 Human referral where required\", current: current_score_c4, baseline: baseline_score_c4}\n  - id: activitylog",
                  "current: employee_question, baseline: baseline_score_c1}\n        - {label: \"c2 Exact figure or entitlement\", current: current_score_c2, baseline: baseline_score_c2}\n        - {label: \"c3 Answers the question asked\", current: current_score_c3, baseline: baseline_score_c3}\n        - {label: \"c4 Human referral where required\", current: current_score_c4, baseline: baseline_score_c4}\n  - id: activitylog")
        self.assertCaught("employee_question", "only 0 or 1")

    def test_ragged_csv_row(self):
        p = self.content / "lab-1.1" / "open-issues.csv"
        p.write_text(p.read_text(encoding="utf-8") + "9,2026-07-03,too few\n", encoding="utf-8")
        self.assertCaught("CSV line", "columns")

    def test_sections_from_needs_a_prefix(self):
        self.edit("lab-3.2/lab.yml", "    id_prefix: b-\n", "")
        self.assertCaught("id_prefix")

    def test_sections_from_unknown_tab(self):
        self.edit("lab-3.2/lab.yml", "sections_from: answer", "sections_from: anser")
        self.assertCaught("sections_from", "did you mean 'answer'")

    def test_lab_registered_but_folder_missing(self):
        shutil.rmtree(self.content / "lab-5.2")
        self.assertCaught("lab-5.2", "does not exist")

    def test_unregistered_folder_is_only_a_warning(self):
        (self.content / "lab-9.9").mkdir()
        rep = validate.validate(self.content)
        self.assertEqual(rep.errors, [])
        self.assertTrue(any("lab-9.9" in w for w in rep.warnings))

    def test_lines_min_greater_than_count(self):
        self.edit("lab-1.1/lab.yml", "count: 3, min: 2, item: \"Criterion\"", "count: 3, min: 5, item: \"Criterion\"")
        self.assertCaught("'min'")

    def test_command_line_exit_codes(self):
        self.assertEqual(validate.main(["validate.py", str(self.content)]), 0)
        self.edit("lab-3.1/lab.yml", "source: reviewer-log.csv", "source: nope.csv")
        self.assertEqual(validate.main(["validate.py", str(self.content)]), 1)


if __name__ == "__main__":
    unittest.main()
