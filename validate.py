#!/usr/bin/env python3
"""Check the course content before it is built into the image.

Usage:  python validate.py [content-dir]

Prints every problem it finds in plain language and exits 1 if there are any errors,
so a broken lab can never be published. Warnings do not fail the check.
Needs only PyYAML (the rest is the standard library).
"""
import csv
import difflib
import re
import sys
from pathlib import Path

import yaml

ID_RE = re.compile(r"^[\w-]+$")   # ids end up inside saved-answer keys, so keep them simple
LAB_ID_RE = re.compile(r"^[\w.-]+$")   # lab ids only appear in URLs, so dots are fine
TAB_TYPES = {"doc", "table", "form", "steps", "report"}
FIELD_KINDS = {"text", "textarea", "select", "lines"}

LAB_KEYS = {"title", "tabs"}
TAB_KEYS = {"id", "title", "type", "optional", "source", "note", "computed", "hide", "labels",
            "editable", "summary", "scorecard", "heading", "intro", "sections", "sections_from",
            "id_prefix", "hide_examples", "about", "steps"}
ABOUT_KEYS = {"what", "why", "todo"}
SECTION_KEYS = {"title", "help", "fields"}
FIELD_KEYS = {"id", "kind", "label", "example", "rows", "required", "options", "count", "min", "item"}
STEP_KEYS = {"title", "text", "fields", "hints", "answer", "show"}
HINT_KEYS = {"title", "text"}
MATERIAL_KINDS = {"doc", "markdown", "table", "answers"}
TABLE_KEYS = {"id", "source", "note", "computed", "hide", "labels", "editable", "summary", "scorecard",
              "where", "readonly", "tools", "view", "group", "split", "sort"}
TABLE_VIEWS = {"rows", "scorecard"}
REPORT_SECTION_KEYS = {"title", "help", "fields"}


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def error(self, where, msg):
        self.errors.append(f"ERROR   {where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"warning {where}: {msg}")


def suggest(name, choices):
    match = difflib.get_close_matches(str(name), [str(c) for c in choices], n=1)
    return f" (did you mean '{match[0]}'?)" if match else ""


def load_yaml(path, rep, where):
    try:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        mark = getattr(e, "problem_mark", None)
        line = f" near line {mark.line + 1}" if mark else ""
        rep.error(where, f"the YAML is not valid{line}: {getattr(e, 'problem', e)}. "
                         "Check indentation and quotes.")
    except OSError as e:
        rep.error(where, f"cannot read the file ({e.strerror})")
    return None


def check_unknown_keys(d, allowed, where, rep):
    for k in d:
        if k not in allowed:
            rep.error(where, f"unknown setting '{k}'{suggest(k, allowed)}")


def read_csv(path, rep, where):
    try:
        with open(path, encoding="utf-8", newline="") as f:
            rows = list(csv.reader(f))
    except (OSError, UnicodeDecodeError) as e:
        rep.error(where, f"cannot read the CSV file: {e}")
        return None
    if len(rows) < 2:
        rep.error(where, "the CSV needs a header row and at least one data row")
        return None
    header = rows[0]
    if len(set(header)) != len(header):
        dupes = sorted({h for h in header if header.count(h) > 1})
        rep.error(where, f"duplicate column names in the CSV header: {', '.join(dupes)}")
    for n, r in enumerate(rows[1:], start=2):
        if len(r) != len(header):
            rep.error(where, f"CSV line {n} has {len(r)} values but the header has {len(header)} columns")
            break
    return header, [dict(zip(header, r)) for r in rows[1:] if len(r) == len(header)]


def options_ok(options, where, rep):
    """Validate a dropdown option list. Returns the list of values."""
    if not isinstance(options, list) or not options:
        rep.error(where, "options must be a non-empty list")
        return []
    values = []
    for o in options:
        if isinstance(o, dict):
            if "value" not in o or "label" not in o:
                rep.error(where, f"option {o} needs both 'value' and 'label'")
                continue
            values.append(str(o["value"]))
        else:
            values.append(str(o))
    if len(set(values)) != len(values):
        rep.error(where, "two options have the same value")
    return values


def check_table(tab, lab_dir, where, rep):
    src = tab.get("source")
    if not src:
        rep.error(where, "a table tab needs a 'source' CSV file")
        return
    path = lab_dir / src
    if not path.is_file():
        rep.error(where, f"source file '{src}' does not exist in {lab_dir.name}/")
        return
    parsed = read_csv(path, rep, f"{where} ({src})")
    if not parsed:
        return
    header, rows = parsed
    columns = list(header)

    for i, comp in enumerate(tab.get("computed") or []):
        cw = f"{where} > computed[{i}]"
        name = comp.get("name")
        if not name or not ID_RE.match(str(name)):
            rep.error(cw, "needs a 'name' made of letters, numbers, - and _")
            continue
        if name in columns:
            rep.error(cw, f"a column called '{name}' already exists")
        if ("differs" in comp) == ("sum" in comp):
            rep.error(cw, "give exactly one of 'differs' (two columns) or 'sum' (a list of columns)")
            continue
        used = comp.get("differs") or comp.get("sum")
        if "differs" in comp and (not isinstance(used, list) or len(used) != 2):
            rep.error(cw, "'differs' needs exactly two column names")
            continue
        for c in used:
            if c not in header:
                rep.error(cw, f"column '{c}' is not in the CSV{suggest(c, header)}")
            elif "sum" in comp and any(not re.fullmatch(r"-?\d+", r[c] or "0") for r in rows):
                rep.error(cw, f"column '{c}' has non-numeric values, so it cannot be summed")
        columns.append(name)

    for c in tab.get("hide") or []:
        if c not in columns:
            rep.error(f"{where} > hide", f"column '{c}' does not exist{suggest(c, columns)}")
    for c in (tab.get("labels") or {}):
        if c not in columns:
            rep.error(f"{where} > labels", f"column '{c}' does not exist{suggest(c, columns)}")

    editable_values = {}
    for i, e in enumerate(tab.get("editable") or []):
        ew = f"{where} > editable[{i}]"
        col = e.get("column")
        if col not in header:
            rep.error(ew, f"column '{col}' is not in the CSV{suggest(col, header)}")
            continue
        if not ID_RE.match(col):
            rep.error(ew, f"column name '{col}' must use only letters, numbers, - and _ to be editable")
        editable_values[col] = options_ok(e.get("options"), ew, rep)

    summ = tab.get("summary")
    if summ:
        if summ.get("column") not in columns:
            rep.error(f"{where} > summary", f"column '{summ.get('column')}' does not exist{suggest(summ.get('column'), columns)}")
        else:
            bad = [r for r in rows if summ["column"] in r and r[summ["column"]] not in ("0", "1")]
            if bad and summ["column"] in header:
                rep.error(f"{where} > summary", f"column '{summ['column']}' must contain only 0 or 1")

    sc = tab.get("scorecard")
    if sc:
        sw = f"{where} > scorecard"
        if sc.get("baseline_bqs") not in header:
            rep.error(sw, f"baseline_bqs column '{sc.get('baseline_bqs')}' is not in the CSV{suggest(sc.get('baseline_bqs'), header)}")
        elif not any(r[sc["baseline_bqs"]] for r in rows):
            rep.error(sw, f"column '{sc['baseline_bqs']}' has no value in any row")
        if not sc.get("criteria"):
            rep.error(sw, "needs a non-empty 'criteria' list")
        for i, c in enumerate(sc.get("criteria") or []):
            cw = f"{sw} > criteria[{i}]"
            if not c.get("label"):
                rep.error(cw, "needs a 'label'")
            for key in ("current", "baseline"):
                col = c.get(key)
                if col not in columns:
                    rep.error(cw, f"'{key}' column '{col}' does not exist{suggest(col, columns)}")
                    continue
                if key == "current" and col in editable_values:
                    if set(editable_values[col]) - {"0", "1"}:
                        rep.error(cw, f"editable column '{col}' must have option values 1 and 0 to be scored")
                elif any(r.get(col, "") not in ("0", "1", "") for r in rows):
                    rep.error(cw, f"column '{col}' must contain only 0 or 1")


def check_form_fields(sections, prefix, where, rep, seen_ids):
    if not isinstance(sections, list) or not sections:
        rep.error(where, "a form needs a non-empty 'sections' list")
        return
    for si, sec in enumerate(sections):
        sw = f"{where} > sections[{si}]" + (f" ('{sec.get('title')}')" if isinstance(sec, dict) and sec.get("title") else "")
        if not isinstance(sec, dict):
            rep.error(sw, "must be a mapping with a title and fields")
            continue
        check_unknown_keys(sec, SECTION_KEYS, sw, rep)
        if not sec.get("title"):
            rep.error(sw, "needs a 'title'")
        if not sec.get("fields"):
            rep.error(sw, "needs a non-empty 'fields' list")
            continue
        for fi, f in enumerate(sec["fields"]):
            fw = f"{sw} > field '{f.get('id', fi)}'"
            check_unknown_keys(f, FIELD_KEYS, fw, rep)
            fid = f.get("id")
            if not fid or not ID_RE.match(str(fid)):
                rep.error(fw, "needs an 'id' made of letters, numbers, - and _")
                continue
            kind = f.get("kind")
            if kind not in FIELD_KINDS:
                rep.error(fw, f"kind '{kind}' is not one of {', '.join(sorted(FIELD_KINDS))}{suggest(kind, FIELD_KINDS)}")
                continue
            if kind != "lines" and not f.get("label"):
                rep.error(fw, "needs a 'label' (the question the student sees)")
            if kind == "select":
                options_ok(f.get("options"), fw, rep)
            elif "options" in f:
                rep.error(fw, "'options' only applies to kind: select")
            if kind == "textarea" and "rows" in f and not isinstance(f["rows"], int):
                rep.error(fw, "'rows' must be a whole number")
            if kind == "lines":
                count = f.get("count", 3)
                if not isinstance(count, int) or count < 1:
                    rep.error(fw, "'count' must be a whole number of at least 1")
                elif f.get("min", count) > count:
                    rep.error(fw, f"'min' ({f['min']}) cannot be more than 'count' ({count})")
                ids = [f"{prefix}{fid}-{i}" for i in range(1, (count if isinstance(count, int) else 0) + 1)]
            else:
                ids = [f"{prefix}{fid}"]
            for full in ids:
                if full in seen_ids:
                    rep.error(fw, f"the id '{full}' is already used in {seen_ids[full]}. "
                                  "Every field id in a lab must be unique, because that is how saved answers are keyed.")
                else:
                    seen_ids[full] = where


def check_form(tab, tabs_by_id, where, rep, seen_ids):
    sections = tab.get("sections")
    if "sections_from" in tab:
        ref = tabs_by_id.get(tab["sections_from"])
        if ref is None or ref.get("type") != "form" or "sections" not in ref:
            rep.error(where, f"'sections_from' must name another form tab that has its own sections{suggest(tab['sections_from'], [k for k, v in tabs_by_id.items() if v.get('type') == 'form'])}")
            return
        if not tab.get("id_prefix"):
            rep.error(where, "a tab that copies another form's sections needs an 'id_prefix' "
                             "(for example 'b-') so its saved answers do not collide")
            return
        if "sections" in tab:
            rep.error(where, "use either 'sections' or 'sections_from', not both")
        sections = ref["sections"]
    elif "id_prefix" in tab or "hide_examples" in tab:
        rep.error(where, "'id_prefix' and 'hide_examples' only apply with 'sections_from'")
    check_form_fields(sections, tab.get("id_prefix", ""), where, rep, seen_ids)


def check_steps(tab, lab_dir, where, rep, seen_ids, tables, echoes):
    """A tab of numbered steps: each step's box, its answer fields, and the material shown under it."""
    if "about" in tab:
        rep.error(where, "a steps tab has no 'about' box. Put that explanation in the first step instead")
    steps = tab.get("steps")
    if not isinstance(steps, list) or not steps:
        rep.error(where, "a steps tab needs a non-empty 'steps' list")
        return
    for si, step in enumerate(steps):
        sw = f"{where} > step {si + 1}" + (f" ('{step.get('title')}')" if isinstance(step, dict) and step.get("title") else "")
        if not isinstance(step, dict):
            rep.error(sw, "must be a mapping with a title and text")
            continue
        check_unknown_keys(step, STEP_KEYS, sw, rep)
        for key in ("title", "text"):
            if not str(step.get(key) or "").strip():
                rep.error(sw, f"needs a non-empty '{key}'")
        if step.get("fields"):
            check_form_fields([{"title": step.get("title") or "step", "fields": step["fields"]}], "", sw, rep, seen_ids)
        for hi, hint in enumerate(step.get("hints") or []):
            hw = f"{sw} > hints[{hi}]"
            if not isinstance(hint, dict):
                rep.error(hw, "must be a mapping with a 'title' and 'text'")
                continue
            check_unknown_keys(hint, HINT_KEYS, hw, rep)
            for key in ("title", "text"):
                if not str(hint.get(key) or "").strip():
                    rep.error(hw, f"needs a non-empty '{key}'")
        for mi, item in enumerate(step.get("show") or []):
            mw = f"{sw} > show[{mi}]"
            kinds = [k for k in (item if isinstance(item, dict) else {}) if k in MATERIAL_KINDS]
            extra = [k for k in (item if isinstance(item, dict) else {}) if k not in MATERIAL_KINDS]
            if isinstance(item, dict) and len(kinds) == 1 and extra == ["section"] and kinds == ["doc"]:
                pass   # a doc may name one section to show
            elif not isinstance(item, dict) or len(kinds) != 1 or extra:
                rep.error(mw, f"each item must have exactly one of: {', '.join(sorted(MATERIAL_KINDS))}"
                              f"{suggest(next(iter(item), ''), MATERIAL_KINDS) if isinstance(item, dict) and item else ''}")
                continue
            if "doc" in item:
                src = item["doc"]
                if not (lab_dir / str(src)).is_file():
                    rep.error(mw, f"source file '{src}' does not exist in {lab_dir.name}/")
                elif not (lab_dir / src).read_text(encoding="utf-8").strip():
                    rep.error(mw, f"source file '{src}' is empty")
                elif item.get("section"):
                    text = (lab_dir / src).read_text(encoding="utf-8")
                    headings = [re.sub(r"^#+\s+", "", l).strip() for l in text.splitlines() if re.match(r"^#+\s", l)]
                    if item["section"] not in headings:
                        rep.error(mw, f"'{src}' has no heading called '{item['section']}'{suggest(item['section'], headings)}")
            elif "markdown" in item:
                if not str(item["markdown"] or "").strip():
                    rep.error(mw, "'markdown' is empty")
            elif "answers" in item:
                if not isinstance(item["answers"], list) or not item["answers"]:
                    rep.error(mw, "'answers' needs a list of field ids from earlier steps")
                else:
                    echoes.append((mw, item["answers"]))
            else:
                spec = item["table"]
                if not isinstance(spec, dict):
                    rep.error(mw, "'table' must be a mapping with at least a 'source'")
                    continue
                check_unknown_keys(spec, TABLE_KEYS, mw, rep)
                check_table(spec, lab_dir, mw, rep)
                if (lab_dir / str(spec.get("source"))).is_file():
                    parsed = read_csv(lab_dir / spec["source"], Report(), "")
                    cols = (parsed[0] if parsed else []) + [c.get("name") for c in spec.get("computed") or []]
                    for key in ("group", "split", "sort"):
                        if spec.get(key) and spec[key] not in cols:
                            rep.error(mw, f"{key} column '{spec[key]}' does not exist{suggest(spec[key], cols)}")
                    if spec.get("split") and not spec.get("group"):
                        rep.error(mw, "'split' only works together with 'group'")
                view = spec.get("view", "rows")
                if view not in TABLE_VIEWS:
                    rep.error(mw, f"view '{view}' is not one of {', '.join(sorted(TABLE_VIEWS))}{suggest(view, TABLE_VIEWS)}")
                elif view == "scorecard" and not spec.get("scorecard"):
                    rep.error(mw, "view: scorecard needs a 'scorecard' setting to show")
                if spec.get("id") is not None and not ID_RE.match(str(spec["id"])):
                    rep.error(mw, "the table 'id' must use only letters, numbers, - and _")
                tables.append((mw, spec))
                where_ = spec.get("where") or {}
                if where_ and (lab_dir / str(spec.get("source"))).is_file():
                    parsed = read_csv(lab_dir / spec["source"], Report(), "")
                    if parsed:
                        header, rows = parsed
                        for c, vals in where_.items():
                            if c not in header:
                                rep.error(f"{mw} > where", f"column '{c}' is not in the CSV{suggest(c, header)}")
                            elif not isinstance(vals, list):
                                rep.error(f"{mw} > where", f"'{c}' needs a list of values, for example [1, 3]")
                            else:
                                present = {r[c] for r in rows}
                                for v in vals:
                                    if str(v) not in present:
                                        rep.error(f"{mw} > where", f"no row has {c} = {v}")


def check_tables_link_up(tables, rep):
    """Editable tables need their own id; a read-only copy must point at one of them."""
    editable_ids = {}
    for mw, spec in tables:
        if spec.get("editable") and not spec.get("readonly") and spec.get("view", "rows") == "rows":
            tid = spec.get("id")
            if not tid:
                rep.error(mw, "an editable table needs an 'id', because saved answers are keyed by it")
            elif tid in editable_ids and editable_ids[tid][1] != spec.get("source"):
                rep.error(mw, f"the editable table id '{tid}' is already used for a different file in {editable_ids[tid][0]}")
            elif tid not in editable_ids:
                editable_ids[tid] = (mw, spec.get("source"))
    # A table split across steps (same id and file, different rows) is one set of answers.
    for mw, spec in tables:
        if spec.get("readonly") or (spec.get("view") == "scorecard" and spec.get("editable")):
            if spec.get("id") not in editable_ids:
                rep.error(mw, f"a read-only table shows the answers from an editable table, so its 'id' must match one"
                              f"{suggest(spec.get('id'), editable_ids)}")
            if not spec.get("editable"):
                rep.error(mw, "a read-only table or score panel needs the same 'editable' columns as the table it copies")


def check_report(tab, where, rep, step_fields):
    sections = tab.get("sections")
    if "about" in tab:
        rep.error(where, "a report tab has no 'about' box. Use 'intro' instead")
    if not isinstance(sections, list) or not sections:
        rep.error(where, "a report needs a non-empty 'sections' list")
        return
    for si, sec in enumerate(sections):
        sw = f"{where} > sections[{si}]"
        if not isinstance(sec, dict):
            rep.error(sw, "must be a mapping with a title and fields")
            continue
        check_unknown_keys(sec, REPORT_SECTION_KEYS, sw, rep)
        if not sec.get("title"):
            rep.error(sw, "needs a 'title'")
        if not isinstance(sec.get("fields"), list) or not sec["fields"]:
            rep.error(sw, "needs a non-empty 'fields' list of field ids from the steps")
            continue
        for fid in sec["fields"]:
            if fid not in step_fields:
                rep.error(sw, f"field '{fid}' is not an answer box in any step{suggest(fid, step_fields)}")


def check_lab(lab_id, lab_dir, rep):
    where_lab = lab_id
    manifest = load_yaml(lab_dir / "lab.yml", rep, f"{where_lab} > lab.yml")
    if manifest is None:
        if not (lab_dir / "lab.yml").exists():
            rep.error(where_lab, "the folder has no lab.yml")
        return
    if not isinstance(manifest, dict):
        rep.error(where_lab, "lab.yml must be a mapping with 'title' and 'tabs'")
        return
    check_unknown_keys(manifest, LAB_KEYS, where_lab, rep)
    if not manifest.get("title"):
        rep.error(where_lab, "lab.yml needs a 'title'")
    tabs = manifest.get("tabs")
    if not isinstance(tabs, list) or not tabs:
        rep.error(where_lab, "lab.yml needs a non-empty 'tabs' list")
        return

    tabs_by_id, titles, seen_ids, tables, echoes = {}, {}, {}, [], []
    for t in tabs:
        if isinstance(t, dict) and t.get("id"):
            tabs_by_id[t["id"]] = t

    for i, tab in enumerate(tabs):
        if not isinstance(tab, dict):
            rep.error(where_lab, f"tabs[{i}] must be a mapping")
            continue
        tid = tab.get("id", f"#{i + 1}")
        where = f"{where_lab} > tab '{tid}'"
        check_unknown_keys(tab, TAB_KEYS, where, rep)
        if not tab.get("id") or not ID_RE.match(str(tab["id"])):
            rep.error(where, "needs an 'id' made of letters, numbers, - and _")
            continue
        if list(t.get("id") for t in tabs if isinstance(t, dict)).count(tab["id"]) > 1 and tabs_by_id.get(tab["id"]) is not tab:
            rep.error(where, "this tab id is used more than once in the lab")
        about = tab.get("about")
        if tab.get("type") in ("steps", "report"):
            pass   # steps carry their own explanation; checked in check_steps / check_report
        elif not isinstance(about, dict):
            rep.error(where, "needs an 'about' box: a short plain-language note at the top of the tab saying "
                             "'what' this is and 'why' the student is looking at it (optionally 'todo')")
        else:
            check_unknown_keys(about, ABOUT_KEYS, f"{where} > about", rep)
            for key in ("what", "why"):
                if not str(about.get(key) or "").strip():
                    rep.error(f"{where} > about", f"needs a non-empty '{key}'")
        if not tab.get("title"):
            rep.error(where, "needs a 'title' (the name students click)")
        elif tab["title"] in titles:
            rep.error(where, f"has the same title as tab '{titles[tab['title']]}'. Students are told which tab to click by name, so titles must differ.")
        else:
            titles[tab["title"]] = tab["id"]
        ttype = tab.get("type")
        if ttype not in TAB_TYPES:
            rep.error(where, f"type '{ttype}' is not one of {', '.join(sorted(TAB_TYPES))}{suggest(ttype, TAB_TYPES)}")
            continue
        if ttype == "doc":
            src = tab.get("source")
            if not src:
                rep.error(where, "a doc tab needs a 'source' Markdown file")
            elif not (lab_dir / src).is_file():
                rep.error(where, f"source file '{src}' does not exist in {lab_dir.name}/")
            elif not (lab_dir / src).read_text(encoding="utf-8").strip():
                rep.error(where, f"source file '{src}' is empty")
        elif ttype == "table":
            check_table(tab, lab_dir, where, rep)
        elif ttype == "steps":
            check_steps(tab, lab_dir, where, rep, seen_ids, tables, echoes)
        elif ttype == "report":
            pass   # checked once every step field is known
        else:
            check_form(tab, tabs_by_id, where, rep, seen_ids)

    check_tables_link_up(tables, rep)
    step_fields = [fid for fid, w in seen_ids.items() if "> step " in w]
    for mw, ids in echoes:
        for fid in ids:
            if fid not in step_fields:
                rep.error(mw, f"'answers' lists '{fid}', which is not an answer box in any step{suggest(fid, step_fields)}")
    for tab in tabs:
        if isinstance(tab, dict) and tab.get("type") == "report":
            check_report(tab, f"{where_lab} > tab '{tab.get('id')}'", rep, step_fields)

    if not any(t.get("type") in ("form", "steps") and not t.get("optional") for t in tabs if isinstance(t, dict)) \
            and not any(t.get("editable") for t in tabs if isinstance(t, dict)):
        rep.warn(where_lab, "has no required form or editable table, so progress will never show as complete")


def validate(content_dir):
    rep = Report()
    content_dir = Path(content_dir)
    labs_file = content_dir / "labs.yml"
    if not labs_file.is_file():
        rep.error("labs.yml", f"not found in {content_dir}")
        return rep
    data = load_yaml(labs_file, rep, "labs.yml")
    if data is None:
        return rep
    modules = data.get("modules") if isinstance(data, dict) else None
    if not isinstance(modules, list) or not modules:
        rep.error("labs.yml", "needs a non-empty 'modules' list")
        return rep

    seen, registered_dirs = set(), set()
    for m in modules:
        if not m.get("title"):
            rep.error("labs.yml", "a module has no 'title'")
        for lab in m.get("labs") or []:
            lid = lab.get("id")
            if not lid or not LAB_ID_RE.match(str(lid)):
                rep.error("labs.yml", f"the lab titled '{lab.get('title', '?')}' needs an 'id' made of letters, numbers, . - and _")
                continue
            if lid in seen:
                rep.error("labs.yml", f"lab id '{lid}' appears more than once")
            seen.add(lid)
            if not lab.get("title"):
                rep.error("labs.yml", f"lab '{lid}' has no 'title'")
            if "dir" in lab:
                registered_dirs.add(lab["dir"])
                lab_dir = content_dir / lab["dir"]
                if not lab_dir.is_dir():
                    rep.error(f"labs.yml > {lid}", f"folder '{lab['dir']}' does not exist under {content_dir.name}/")
                else:
                    check_lab(lid, lab_dir, rep)

    for d in sorted(p for p in content_dir.iterdir() if p.is_dir()):
        if d.name not in registered_dirs:
            rep.warn(d.name, "this folder is not listed in labs.yml, so students will not see it")
    return rep


def main(argv):
    content = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent / "content"
    rep = validate(content)
    for line in rep.errors + rep.warnings:
        print(line)
    if rep.errors:
        print(f"\nContent check FAILED: {len(rep.errors)} error(s), {len(rep.warnings)} warning(s). "
              "Nothing will be built until these are fixed.")
        return 1
    print(f"Content check passed ({len(rep.warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
