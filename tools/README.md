# Tools for working on the labs

These are for course authors (and Claude), not students.

| Tool | What it does |
|---|---|
| `tabs_md.py LAB OUT.md` | Writes a Markdown copy of a lab's tabs and steps (e.g. to `~/static/lab-2.1-tabs.md`) so the author can mark up changes. Run from the repo root with `.venv/bin/python`. |
| `labcheck.py LAB [DIR]` | Opens every tab of a lab in a headless browser, prints any JavaScript errors, and optionally screenshots each tab into `DIR`. |
| `shot1.py HASH OUT.png` | Screenshots one page, e.g. `lab-2.1/result`, keeping whatever answers are saved. |
| `setup-browser.sh` | One-time, no-root setup of the headless Chromium the two tools above need (into `./.browser`). `/tmp` on this VM is a small RAM disk that fills up, so run it as `TMPDIR=$PWD/.browser/tmp tools/setup-browser.sh`. |
| `run.sh` | Runs a browser tool with that Chromium: `tools/run.sh tools/labcheck.py lab-2.1` |

The browser tools talk to a **throwaway test server on port 2299** with its own data, so they never touch
real answers on port 2224. Start it with:

```bash
DATA_DIR=/tmp/labtest-data .venv/bin/flask --app server run --host 127.0.0.1 --port 2299 --no-debugger &
```

`labcheck.py` clears that lab's answers on the test server before it runs.

The test server has no auto-reload. Lab content changes show up on the next request, but after a change to
`server.py` restart it. Stop it by its process id (`pgrep -f "port 2299"` lists it); a `pkill -f` on that
pattern also matches the shell running the command and kills it.
