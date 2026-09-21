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

## How a lab is defined

Each lab is a folder in `content/` with a `lab.yml` listing its **fixed tabs**, in order.
Tab titles are the names the course page tells students to click, so keep them in sync.

| Tab `type` | Source | Student can |
|---|---|---|
| `doc` | a Markdown file | read it |
| `table` | a CSV file | sort, filter, group by / split by; fill `editable` columns with a dropdown |
| `form` | `sections:` in `lab.yml` | type answers (autosaved); `example:` is shown above the field |

Table options: `computed` adds pre-calculated columns (`differs: [a, b]` gives 1 when the
columns differ), `summary` picks the 0/1 column that group-by rates are computed from.
`lines` fields expand into N one-line inputs; `min` sets how many are required.

Register a lab in `content/labs.yml` by giving it a `dir`. Labs without one show as "soon".

**Keep field ids stable.** Saved answers are keyed by lab and field id. Renaming an id in
`lab.yml` orphans any answer a student already saved under the old one.

## Behaviour to know

- Progress (sidebar dot, "N of M answers") counts required form fields and editable table
  cells only.
- "Reset this lab" clears that lab's answers and nothing else. Labs are independent.
- "Save as PDF" renders the open tab, including the student's answers, on the server.
