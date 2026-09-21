"""AI Governance course workspace.

Serves each lab as a set of fixed tabs (documents, tables, forms). Student answers
are saved to SQLite in DATA_DIR so they survive container restarts when that
directory is a Docker volume.
"""
import csv
import io
import os
import re
import sqlite3
import time
from pathlib import Path

import markdown
import yaml
from flask import Flask, Response, abort, g, jsonify, request, send_from_directory

import pdfgen

BASE = Path(__file__).resolve().parent
CONTENT = BASE / "content"
DATA_DIR = Path(os.environ.get("DATA_DIR", BASE / "data"))

app = Flask(__name__, static_folder=None)


# ---------------------------------------------------------------- persistence

def db():
    if "db" not in g:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        g.db = sqlite3.connect(DATA_DIR / "workspace.db")
        g.db.execute(
            "CREATE TABLE IF NOT EXISTS answers ("
            "lab_id TEXT NOT NULL, key TEXT NOT NULL, value TEXT NOT NULL, "
            "updated_at REAL NOT NULL, PRIMARY KEY (lab_id, key))"
        )
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    conn = g.pop("db", None)
    if conn is not None:
        conn.close()


def saved_answers(lab_id):
    rows = db().execute("SELECT key, value FROM answers WHERE lab_id = ?", (lab_id,))
    return {k: v for k, v in rows}


# -------------------------------------------------------------------- content

def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def lab_index():
    """Return the sidebar structure from labs.yml."""
    return load_yaml(CONTENT / "labs.yml")["modules"]


def find_lab_entry(lab_id):
    for module in lab_index():
        for lab in module["labs"]:
            if lab["id"] == lab_id:
                return lab
    return None


def expand_fields(sections, prefix="", optional=False, examples=True):
    """Turn `lines` fields into N text inputs, apply an id prefix, and mark which are required."""
    out = []
    for sec in sections:
        fields = []
        for f in sec["fields"]:
            if f["kind"] == "lines":
                count = f.get("count", 3)
                required = f.get("min", count)
                for i in range(1, count + 1):
                    fields.append({
                        "id": f"{prefix}{f['id']}-{i}",
                        "kind": "text",
                        "label": f"{f.get('item', 'Item')} {i}",
                        "example": f.get("example") if i == 1 and examples else None,
                        "required": i <= required and not optional,
                    })
            else:
                fields.append({**f, "id": f"{prefix}{f['id']}",
                               "example": f.get("example") if examples else None,
                               "required": f.get("required", True) and not optional})
        out.append({"title": sec["title"], "help": sec.get("help"), "fields": fields})
    return out


def normalize_options(options):
    """Dropdown options may be plain strings or {value, label} pairs."""
    return [o if isinstance(o, dict) else {"value": str(o), "label": str(o)} for o in options]


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def build_table(lab_dir, tab):
    rows = read_csv(lab_dir / tab["source"])
    columns = list(rows[0].keys()) if rows else []
    for comp in tab.get("computed", []):
        for r in rows:
            if "differs" in comp:
                a, b = comp["differs"]
                r[comp["name"]] = "1" if r[a] != r[b] else "0"
            else:
                r[comp["name"]] = str(sum(int(r[c] or 0) for c in comp["sum"]))
        columns.append(comp["name"])
    editable = {e["column"]: normalize_options(e["options"]) for e in tab.get("editable", [])}
    return {
        "columns": columns,
        "rows": rows,
        "editable": editable,
        "hide": tab.get("hide", []),
        "labels": tab.get("labels", {}),
        "summary": tab.get("summary"),
        "scorecard": tab.get("scorecard"),
        "note": tab.get("note"),
    }


def build_tab(lab_dir, tab, raw_tabs):
    base = {"id": tab["id"], "title": tab["title"], "type": tab["type"],
            "optional": bool(tab.get("optional"))}
    if tab["type"] == "doc":
        text = (lab_dir / tab["source"]).read_text(encoding="utf-8")
        html = markdown.markdown(text, extensions=["tables", "sane_lists"])
        return {**base, "html": html, "markdown": text}
    if tab["type"] == "table":
        return {**base, **build_table(lab_dir, tab)}
    if tab["type"] == "form":
        sections = tab.get("sections")
        if "sections_from" in tab:
            sections = next(t for t in raw_tabs if t["id"] == tab["sections_from"])["sections"]
        return {
            **base,
            "heading": tab.get("heading", tab["title"]),
            "intro": tab.get("intro"),
            "sections": expand_fields(sections, tab.get("id_prefix", ""), base["optional"],
                                     not tab.get("hide_examples")),
        }
    abort(500, f"unknown tab type {tab['type']}")


_lab_cache = {}


def _signature(lab_dir):
    """Changes whenever any file in the lab folder (or labs.yml) is edited."""
    files = [CONTENT / "labs.yml", *sorted(lab_dir.iterdir())]
    return tuple((f.name, f.stat().st_mtime_ns) for f in files)


def load_lab(lab_id):
    """Parse a lab, reusing the last parse until a content file changes. Treat the result as read-only."""
    entry = find_lab_entry(lab_id)
    if not entry or "dir" not in entry:
        abort(404)
    lab_dir = CONTENT / entry["dir"]
    sig = _signature(lab_dir)
    cached = _lab_cache.get(lab_id)
    if cached and cached[0] == sig:
        return cached[1]
    manifest = load_yaml(lab_dir / "lab.yml")
    tabs = [build_tab(lab_dir, t, manifest["tabs"]) for t in manifest["tabs"]]
    lab = {"id": lab_id, "title": manifest["title"], "tabs": tabs}
    _lab_cache[lab_id] = (sig, lab)
    return lab


def required_keys(lab):
    """Every answer key that must be non-empty for the lab to count as complete."""
    keys = []
    for tab in lab["tabs"]:
        if tab["type"] == "form":
            for sec in tab["sections"]:
                keys += [f"f:{f['id']}" for f in sec["fields"] if f["required"]]
        elif tab["type"] == "table" and not tab["optional"]:
            for col in tab["editable"]:
                keys += [f"t:{tab['id']}:{i}:{col}" for i in range(len(tab["rows"]))]
    return keys


def status_for(lab_id):
    lab = load_lab(lab_id)
    answers = saved_answers(lab_id)
    req = required_keys(lab)
    done = sum(1 for k in req if answers.get(k, "").strip())
    if req and done == len(req):
        state = "complete"
    elif done:
        state = "in-progress"
    else:
        state = "not-started"
    return {"state": state, "done": done, "total": len(req)}


# ------------------------------------------------------------------------ API

@app.get("/api/labs")
def api_labs():
    modules = []
    for module in lab_index():
        labs = []
        for lab in module["labs"]:
            item = {"id": lab["id"], "title": lab["title"], "available": "dir" in lab}
            if item["available"]:
                item["status"] = status_for(lab["id"])
            labs.append(item)
        modules.append({"title": module["title"], "labs": labs})
    return jsonify(modules)


@app.get("/api/labs/<lab_id>")
def api_lab(lab_id):
    lab = load_lab(lab_id)
    tabs = [{k: v for k, v in tab.items() if k != "markdown"} for tab in lab["tabs"]]
    return jsonify({**lab, "tabs": tabs, "answers": saved_answers(lab_id), "status": status_for(lab_id)})


@app.put("/api/labs/<lab_id>/answers")
def api_save(lab_id):
    load_lab(lab_id)  # 404 for unknown labs
    body = request.get_json(force=True)
    key, value = str(body["key"]), str(body["value"])
    if not re.match(r"^(f:[\w-]+|t:[\w-]+:\d+:[\w-]+)$", key):
        abort(400, "bad key")
    if len(value) > 20000:
        abort(400, "answer too long")
    conn = db()
    if value.strip():
        conn.execute(
            "INSERT INTO answers (lab_id, key, value, updated_at) VALUES (?, ?, ?, ?) "
            "ON CONFLICT(lab_id, key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at",
            (lab_id, key, value, time.time()),
        )
    else:
        conn.execute("DELETE FROM answers WHERE lab_id = ? AND key = ?", (lab_id, key))
    conn.commit()
    return jsonify(status_for(lab_id))


@app.delete("/api/labs/<lab_id>/answers")
def api_reset(lab_id):
    load_lab(lab_id)
    conn = db()
    conn.execute("DELETE FROM answers WHERE lab_id = ?", (lab_id,))
    conn.commit()
    return jsonify(status_for(lab_id))


@app.get("/api/labs/<lab_id>/tabs/<tab_id>/pdf")
def api_pdf(lab_id, tab_id):
    lab = load_lab(lab_id)
    tab = next((t for t in lab["tabs"] if t["id"] == tab_id), None)
    if tab is None:
        abort(404)
    data = pdfgen.render(lab["title"], tab, saved_answers(lab_id))
    filename = f"{lab_id}-{tab_id}.pdf"
    return Response(
        data,
        mimetype="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


# ------------------------------------------------------------------- frontend

@app.get("/")
def index():
    return send_from_directory(BASE / "static", "index.html")


@app.get("/favicon.ico")
def favicon():
    return Response(status=204)


@app.get("/static/<path:name>")
def static_files(name):
    return send_from_directory(BASE / "static", name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 2224)))
