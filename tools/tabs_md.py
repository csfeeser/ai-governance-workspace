"""Write a Markdown mirror of a steps-format lab: python tabs_md.py lab-1.1 /var/www/static/lab-1.1-tabs.md"""
import csv, sys, yaml
from pathlib import Path
lab_id, dest = sys.argv[1], sys.argv[2]
d = Path("content") / lab_id; lab = yaml.safe_load(open(d / "lab.yml"))
out = [f"# Lab {lab_id.split('-')[1]}: {lab['title']}", "",
       f"_Generated from `content/{lab_id}/lab.yml`. Each tab is a `##` heading, each step a `###` heading. "
       "Answer boxes show their field id in brackets, e.g. `[purpose]`. Material shown under a step is under **Material below the step**._", ""]
def table_md(spec):
    rows = list(csv.DictReader(open(d / spec["source"], encoding="utf-8")))
    where = spec.get("where") or {}
    rows = [r for r in rows if all(r[c] in [str(v) for v in vs] for c, vs in where.items())]
    cols = [c for c in rows[0] if c not in (spec.get("hide") or [])]
    labels = spec.get("labels") or {}
    editable = {e["column"]: e["options"] for e in spec.get("editable") or []}
    lines = ["| " + " | ".join(labels.get(c, c) for c in cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        cells = []
        for c in cols:
            if c in editable:
                cells.append("_(student's choice)_" if spec.get("readonly")
                             else "_drop-down: " + " / ".join(str(o if not isinstance(o, dict) else o["label"]) for o in editable[c]) + "_")
            else:
                cells.append(r[c].replace("|", "\\|"))
        lines.append("| " + " | ".join(cells) + " |")
    note = []
    if spec.get("group"):
        return [f"_(table of `{spec['source']}` opened grouped by {spec['group']}" + (f", split by {spec['split']}" if spec.get("split") else "") + "; shows rows, overrides and rate per group)_"]
    if spec.get("sort"): note.append(f"sorted by {spec['sort']}")
    if spec.get("readonly"): note.append("read-only copy of the table above, showing the student's choices")
    if where: note.append("only rows where " + ", ".join(f"{c} is {vs}" for c, vs in where.items()))
    return (["_(" + "; ".join(note) + ")_", ""] if note else []) + lines
n = 1
for tab in lab["tabs"]:
    out += [f"## Tab: {tab['title']}  (`id: {tab['id']}`)" + ("  _(optional)_" if tab.get("optional") else ""), ""]
    if tab["type"] == "report":
        out += ["_Read-only. Builds itself from the step answers._", "", f"**Heading:** {tab['heading']}", "",
                f"**Intro:** {tab.get('intro', '')}", ""]
        out += [f"- **{sec['title']}**: " + ", ".join(f"`[{f}]`" for f in sec["fields"]) for sec in tab["sections"]] + [""]
        continue
    for s in tab["steps"]:
        out += [f"### Step {n}: {s['title']}", "", s["text"].rstrip(), ""]
        for f in s.get("fields") or []:
            out.append(f"- **Answer box** `[{f['id']}]` ({f['kind']}): {f['label']}")
            out += [f"  - {o}" for o in f.get("options") or []]
        if s.get("fields"): out.append("")
        for h in s.get("hints") or []:
            out += [f"<details><summary>{h['title']}</summary>", "", h["text"].rstrip(), "", "</details>", ""]
        if s.get("answer"):
            out += ["<details><summary>Show the answer</summary>", "", s["answer"].rstrip(), "", "</details>", ""]
        if s.get("show"):
            out += ["**Material below the step:**", ""]
            for m in s["show"]:
                if "doc" in m:
                    body = (d / m["doc"]).read_text(encoding="utf-8").rstrip()
                    label = f"`{m['doc']}`"
                    if m.get("section"):
                        sys.path.insert(0, "."); from server import doc_section
                        body = doc_section(body, m["section"]).rstrip(); label += f", section '{m["section"]}'"
                    out += [f"> _From file {label}:_", ">"] + ["> " + l if l else ">" for l in body.splitlines()] + [""]
                elif "markdown" in m:
                    out += [m["markdown"].rstrip(), ""]
                elif "answers" in m:
                    out += ["_(read-only copy of the student's earlier answers: " + ", ".join(f"`[{a}]`" for a in m["answers"]) + ")_", ""]
                elif m["table"].get("view") == "scorecard":
                    out += ["_(live score box: Current Business Quality Score, Recorded baseline, Change (points), Responses below their own baseline, How each criterion moved)_", ""]
                else:
                    out += table_md(m["table"]) + [""]
        out += ["---", ""]
        n += 1
Path(dest).write_text("\n".join(out), encoding="utf-8")
print("wrote", dest)
