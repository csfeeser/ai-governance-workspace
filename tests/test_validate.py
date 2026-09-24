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


LEGACY_LAB = """title: Legacy lab
tabs:
  - id: notes
    title: Notes
    about:
      what: "Some notes."
      why: "To test the old format."
    type: doc
    source: notes.md
  - id: answer
    title: My Answer
    about:
      what: "A form."
      why: "To test forms."
    type: form
    sections:
      - title: "One"
        fields:
          - {id: high, kind: text, label: "High"}
          - {id: low, kind: text, label: "Low"}
          - {id: pick, kind: select, label: "Pick", options: [a, b]}
  - id: bronze
    title: Bronze
    about:
      what: "A copy."
      why: "To test sections_from."
    type: form
    optional: true
    sections_from: answer
    id_prefix: b-
"""


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

    def add_legacy_lab(self):
        """A small lab in the older doc/table/form format, so those tab types stay tested
        after every real lab has moved to steps."""
        d = self.content / "lab-legacy"
        d.mkdir()
        (d / "notes.md").write_text("# Notes\n\nSome notes.\n", encoding="utf-8")
        (d / "lab.yml").write_text(LEGACY_LAB, encoding="utf-8")
        labs = self.content / "labs.yml"
        labs.write_text(labs.read_text(encoding="utf-8") +
                        '  - title: "Legacy"\n    labs:\n      - {id: lab-legacy, dir: lab-legacy, title: "Legacy"}\n',
                        encoding="utf-8")
        self.assertEqual(validate.validate(self.content).errors, [], "the legacy fixture itself must pass")

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
        self.add_legacy_lab()
        self.edit("lab-legacy/lab.yml", "{id: high,", "{id: low,")
        self.assertCaught("'low' is already used", "unique")

    def test_duplicate_tab_title(self):
        self.edit("lab-3.1/lab.yml", "title: High Outlier", "title: Low Outlier")
        self.assertCaught("same title")

    def test_select_field_without_options(self):
        self.add_legacy_lab()
        self.edit("lab-legacy/lab.yml", ', options: [a, b]}', '}')
        self.assertCaught("pick", "options")

    def test_unknown_field_kind(self):
        self.edit("lab-1.1/lab.yml", "{id: tier, kind: text,", "{id: tier, kind: txt,")
        self.assertCaught("kind 'txt'", "did you mean 'text'")

    def test_editable_column_missing_from_csv(self):
        self.edit("lab-1.1/lab.yml", "- column: owner", "- column: ownr")
        self.assertCaught("'ownr' is not in the CSV", "did you mean 'owner'")

    def test_scorecard_column_that_is_not_zero_or_one(self):
        self.edit("lab-2.2/lab.yml", '- {label: "c1 Current, named source", current: current_score_c1,',
                  '- {label: "c1 Current, named source", current: employee_question,')
        self.assertCaught("employee_question", "only 0 or 1")

    def test_ragged_csv_row(self):
        p = self.content / "lab-1.1" / "open-issues.csv"
        p.write_text(p.read_text(encoding="utf-8") + "9,2026-07-03,too few\n", encoding="utf-8")
        self.assertCaught("CSV line", "columns")

    def test_sections_from_needs_a_prefix(self):
        self.add_legacy_lab()
        self.edit("lab-legacy/lab.yml", "    id_prefix: b-\n", "")
        self.assertCaught("id_prefix")

    def test_sections_from_unknown_tab(self):
        self.add_legacy_lab()
        self.edit("lab-legacy/lab.yml", "sections_from: answer", "sections_from: anser")
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
        self.edit("lab-1.1/lab.yml", "{id: tier, kind: text, label: \"Risk tier\"}", "{id: tier, kind: lines, count: 3, min: 5, item: \"Tier\"}")
        self.assertCaught("'min'")

    def test_tab_without_an_about_box(self):
        self.add_legacy_lab()
        self.edit("lab-legacy/lab.yml", "    about:\n      what: \"Some notes.\"", "    nope:\n      what: \"Some notes.\"")
        self.assertCaught("lab-legacy", "about")

    def test_about_box_with_empty_why(self):
        self.add_legacy_lab()
        self.edit("lab-legacy/lab.yml", 'why: "To test forms."', 'why: ""')
        self.assertCaught("lab-legacy", "'why'")

    def test_step_without_text(self):
        self.edit("lab-1.1/lab.yml", "      - title: Find PolicyPal's risk tier and review requirements\n        text: |", "      - title: Find PolicyPal's risk tier and review requirements\n        txt: |")
        self.assertCaught("Find PolicyPal's risk tier", "'text'")

    def test_step_material_file_missing(self):
        self.edit("lab-1.1/lab.yml", "- doc: review-cadence.md", "- doc: review-cadance.md")
        self.assertCaught("review-cadance.md", "does not exist")

    def test_step_material_unknown_kind(self):
        self.edit("lab-1.1/lab.yml", "- doc: review-cadence.md", "- docs: review-cadence.md")
        self.assertCaught("exactly one of", "did you mean 'doc'")

    def test_step_table_row_filter_matches_nothing(self):
        self.edit("lab-1.1/lab.yml", 'where: {"#": [3, 7]}', 'where: {"#": [3, 70]}')
        self.assertCaught("no row has # = 70")

    def test_readonly_table_must_copy_an_editable_one(self):
        self.edit("lab-1.1/lab.yml", "              id: issues\n              source: open-issues.csv\n              readonly: true",
                  "              id: isues\n              source: open-issues.csv\n              readonly: true")
        self.assertCaught("read-only table", "did you mean 'issues'")

    def test_report_field_that_no_step_asks_for(self):
        self.edit("lab-1.1/lab.yml", "fields: [tolerance]}", "fields: [tolerence]}")
        self.assertCaught("'tolerence' is not an answer box", "did you mean 'tolerance'")

    def test_step_field_ids_must_be_unique(self):
        self.edit("lab-1.1/lab.yml", "{id: just2, kind: textarea", "{id: just1, kind: textarea")
        self.assertCaught("'just1' is already used")

    def test_step_doc_section_that_does_not_exist(self):
        self.edit("lab-2.1/lab.yml", 'section: "8. Quality alarm level"', 'section: "8. Quality alarm"')
        self.assertCaught("no heading called '8. Quality alarm'", "did you mean '8. Quality alarm level'")

    def test_score_panel_needs_a_scorecard(self):
        self.edit("lab-2.1/lab.yml", "              view: scorecard\n", "              view: scorcard\n")
        self.assertCaught("view 'scorcard'", "did you mean 'scorecard'")

    def test_step_table_group_column_that_does_not_exist(self):
        self.edit("lab-3.1/lab.yml", "group: reviewer, split: case_type}", "group: reviewr, split: case_type}")
        self.assertCaught("group column 'reviewr'", "did you mean 'reviewer'")

    def test_echoed_answer_that_no_step_asks_for(self):
        self.edit("lab-2.2/lab.yml", "- answers: [tr_conclusion]", "- answers: [tr_conclusoin]")
        self.assertCaught("'tr_conclusoin', which is not an answer box", "did you mean 'tr_conclusion'")

    def test_command_line_exit_codes(self):
        self.assertEqual(validate.main(["validate.py", str(self.content)]), 0)
        self.edit("lab-3.1/lab.yml", "source: reviewer-log.csv", "source: nope.csv")
        self.assertEqual(validate.main(["validate.py", str(self.content)]), 1)


if __name__ == "__main__":
    unittest.main()
