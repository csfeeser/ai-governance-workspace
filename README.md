# AI Governance Workspace

Web app that gives students of the AI Governance course (`ai-governance-0H5`) their
evidence, tables, and answer forms in the browser. Nothing is downloaded, opened locally,
or saved by hand. Students open it from `Web Ports` -> `aux1` (port 2224).

## Run it

On the lab VM (Docker required), one command:

```bash
docker run -d --name governance --restart unless-stopped \
  -p 2224:2224 -v governance-data:/data \
  ghcr.io/csfeeser/ai-governance-workspace:latest
```

`-p 2224:2224` publishes the app on all of the VM's addresses. Then open
`http://<vm-address>:2224`, or use `Web Ports` -> `aux1` in the LMS.

Student answers are saved to SQLite on the `governance-data` volume, so they survive a
crash, a `docker restart`, or removing and recreating the container.

## Update to the newest version

Every push to `main` rebuilds and publishes `:latest` (after the tests in
`.github/workflows/build.yml` pass). To pick it up, keeping student work:

```bash
docker pull ghcr.io/csfeeser/ai-governance-workspace:latest
docker rm -f governance
docker run -d --name governance --restart unless-stopped \
  -p 2224:2224 -v governance-data:/data \
  ghcr.io/csfeeser/ai-governance-workspace:latest
```

A specific build is also published as `:<commit-sha>` if you need to pin one.

## Other commands

| Goal | Command |
|---|---|
| See logs | `docker logs governance` |
| Stop / start | `docker stop governance` / `docker start governance` |
| Wipe **all** student progress | `docker rm -f governance && docker volume rm governance-data` |
| Back up answers | `docker cp governance:/data/workspace.db .` |

## Develop locally

```bash
pip install -r requirements.txt
python server.py            # http://localhost:2224, data in ./data
```

Or build the image: `docker build -t ai-governance-workspace .`

## Editing labs

Nearly everything is plain text in `content/`. To change a lab, edit its files, check them,
and push. No code changes are needed for wording, data, questions or tab order.

```bash
python validate.py                 # checks every lab; prints plain-language problems
python -m unittest discover -s tests   # tests the checker itself
```

**The check runs in CI before anything is built.** If `validate.py` finds an error, the
workflow stops and no image is built or published. It catches bad YAML indentation, misspelled
settings (with a "did you mean ...?" hint), missing files, columns that do not exist, duplicate
field ids or tab names, dropdowns with no options, and ragged CSV rows. Warnings (for example a
folder that is not listed in `labs.yml`) do not stop the build.

To preview edits on a machine without rebuilding, mount the folder over the built-in copy. The
server re-reads changed files on the next page load:

```bash
docker run --rm -p 2224:2224 -v "$(pwd)/content:/app/content" ai-governance-workspace
```

### How a lab is defined

Each lab is a folder in `content/` with a `lab.yml` listing its **fixed tabs**, in order. Tab
titles are the names the course page tells students to click, so keep them in sync. Register
a lab in `content/labs.yml` by giving it a `dir`. Labs without one show as "soon".

| Tab `type` | Source | Student can |
|---|---|---|
| `doc` | a Markdown file | read it |
| `table` | a CSV file | sort, filter, group by / split by; fill `editable` columns with a dropdown |
| `form` | `sections:` in `lab.yml` | type or choose answers (autosaved) |
| `steps` | `steps:` in `lab.yml` | follow numbered steps, each with its own answer boxes and the material under it |
| `report` | `sections:` naming step field ids | read a page built from their step answers (read-only; this is the PDF they save) |

**Steps tabs (every lab uses them).** Students work through the tabs left to right and each
tab top to bottom, never going back. Every instruction is a numbered step in an orange box; step numbers
run across the whole lab. The material a step needs goes right under it in `show:`, even if an earlier
step already showed it.

```yaml
- id: basics
  title: PolicyPal Basics
  type: steps
  steps:
    - title: Find PolicyPal's risk tier          # the step heading
      text: |                                    # Markdown instructions
        Find the risk tier in the row below.
      fields:                                    # answer boxes, same format as form fields
        - {id: tier, kind: text, label: "Risk tier"}
      hints:                                     # optional, each opens on click
        - {title: "Hint: where to look", text: "The **Assigned risk tier** row."}
      answer: "`Medium`"                         # optional "Show the answer"
      show:                                      # material under the step, in order
        - doc: intake-record.md                  # a Markdown file
        - markdown: "| a | b |\n|---|---|\n| 1 | 2 |"   # or inline Markdown
        - table:                                 # or a CSV table (same settings as a table tab)
            source: open-issues.csv
            where: {"#": [1, 3]}                 # optional: only these rows
            tools: false                         # optional: hide sort/filter/group controls
```

More things a step can show under it:

| `show:` item | What it shows |
|---|---|
| `doc: file.md` plus `section: "Heading text"` | only that section of the file (up to the next heading of the same level) |
| `answers: [field-id, ...]` | the student's earlier answers, read-only, updating live, so no step needs a trip back to an earlier tab |
| `table:` with `group:`, `split:`, `sort:` | the table opened already grouped, split or sorted; the menus still work |
| `table:` with `view: scorecard` | only the live Business Quality Score panel for that table |

One editable table can be split across steps (for example the first five rows, then the rest): give each
part the same `id` and `source` and a different `where:`. Their answers are one set.

A steps tab with `optional: true` (challenge tabs) is left out of the progress count. It can follow the
report tab; the report then links on to it.

An editable table needs an `id` (answers are keyed by it). To show the student's choices again in a later
step, repeat the table with the same `id` and `readonly: true`. A `report` tab lists field ids from the
steps; a missing answer says which step to go back to.

**Form fields** (`kind:`): `text`, `textarea`, `select` (needs `options:`), and `lines` (expands
into `count` one-line inputs, `min` of them required). `example:` shows a grey example above the
field. `required: false` makes a field optional.

**Table options:**

| Setting | What it does |
|---|---|
| `computed` | Adds a calculated column: `differs: [a, b]` gives 1 when two columns differ, `sum: [a, b, c]` adds numeric columns. |
| `summary` | Names the 0/1 column that Group by rates are calculated from. |
| `hide` / `labels` | Hide columns, or rename headers for display. |
| `editable` | Columns students fill in with a dropdown. Options are strings, or `{value, label}` pairs. |
| `scorecard` | Shows a live Business Quality Score panel from per-criterion 0/1 columns (see Labs 2.1 and 2.2). |

**Every tab needs an `about` box.** It is the blue box at the top of the tab, in plain words, for a
student who has no idea what they are looking at. `what` says what the document is, `why` says why they
are looking at it, and `todo` (optional) says what to do there. The check refuses to build a tab without
`what` and `why`, so a new tab cannot ship unexplained. Write it as if for someone who has never seen
the subject: short sentences, no jargon, and explain any term you have to use.

```yaml
- id: intake
  title: Intake Record
  about:
    what: "A fact sheet about PolicyPal, the AI assistant you have just been put in charge of."
    why: "You cannot look after something until you know the basics about it."
    todo: "Read it from top to bottom."
  type: doc
  source: intake-record.md
```

**Optional tabs and reused forms:** `optional: true` keeps a tab out of the progress count (used
for Bronze challenges). `sections_from: <tab id>` copies another form's questions, with
`id_prefix:` keeping the saved answers separate and `hide_examples: true` dropping the examples.

**Keep field ids stable.** Saved answers are keyed by lab and field id. Renaming an id in
`lab.yml` orphans any answer a student already saved under the old one.

Anything not listed here (a new calculation, a new kind of field) is a change to `server.py`
or `static/app.js`, not a content edit.

## Behaviour to know

- Progress (sidebar dot, "N of M answers") counts required form fields and editable table
  cells only.
- "Reset this lab" clears that lab's answers and nothing else. Labs are independent.
- "Save as PDF" renders the open tab, including the student's answers, on the server.
