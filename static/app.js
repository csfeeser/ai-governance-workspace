// AI Governance workspace front end. No build step, no dependencies.
"use strict";

const state = { labs: [], lab: null, tabId: null, answers: {}, saving: 0, queued: 0 };
const pending = new Map();   // key -> timeout id, for debounced saves
const bound = new Map();     // answer key -> functions that redraw every place that answer is shown
let saveChain = Promise.resolve();   // saves go out one at a time so they cannot arrive out of order

// ---------------------------------------------------------------- helpers

function h(tag, attrs, ...children) {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (k === "class") el.className = v;
    else if (k.startsWith("on")) el.addEventListener(k.slice(2), v);
    else if (v !== false && v != null) el.setAttribute(k, v === true ? "" : v);
  }
  for (const c of children.flat(Infinity)) {
    if (c == null || c === false) continue;
    el.append(c.nodeType ? c : document.createTextNode(c));
  }
  return el;
}

async function api(path, opts) {
  const r = await fetch(path, opts);
  if (!r.ok) throw new Error(`${r.status} ${path}`);
  return r.json();
}

const DOT = { "complete": "●", "in-progress": "◐", "not-started": "○" };

// ---------------------------------------------------------------- sidebar

async function loadSidebar() {
  state.labs = await api("/api/labs");
  renderSidebar();
}

function renderSidebar() {
  const nav = document.getElementById("sidebar");
  nav.replaceChildren(h("div", { class: "brand" }, "AI Governance Workspace"));
  for (const mod of state.labs) {
    nav.append(h("div", { class: "module" }, mod.title));
    for (const lab of mod.labs) {
      const st = lab.status ? lab.status.state : "not-started";
      const active = state.lab && state.lab.id === lab.id;
      nav.append(h("button", {
        class: "lab" + (active ? " active" : ""), disabled: !lab.available,
        onclick: () => go(lab.id),
      },
        h("span", { class: "dot " + st, title: st.replace("-", " ") }, DOT[st]),
        h("span", {}, lab.title),
        !lab.available && h("span", { class: "soon" }, "soon")));
    }
  }
}

function updateStatus(labId, status) {
  for (const mod of state.labs) for (const lab of mod.labs) if (lab.id === labId) lab.status = status;
  renderSidebar();
  const p = document.getElementById("progress");
  if (p && state.lab && state.lab.id === labId) p.textContent = progressText(status);
}

function progressText(s) {
  return s.total ? `${s.done} of ${s.total} answers filled in` : "";
}

// ---------------------------------------------------------------- routing

function go(labId, tabId) {
  location.hash = `#/${labId}` + (tabId ? `/${tabId}` : "");
}

async function route() {
  const [, labId, tabId] = location.hash.split("/");
  if (!labId) { showWelcome(); return; }
  await flushSaves();
  if (!state.lab || state.lab.id !== labId) {
    try {
      state.lab = await api(`/api/labs/${labId}`);
    } catch (e) { showWelcome(); return; }
    state.answers = state.lab.answers;
  }
  const tab = state.lab.tabs.find(t => t.id === tabId) || state.lab.tabs[0];
  state.tabId = tab.id;
  renderLab();
  renderSidebar();
}

function showWelcome() {
  state.lab = null;
  renderSidebar();
  document.getElementById("main").replaceChildren(h("div", { id: "welcome" },
    h("h1", {}, "AI Governance Workspace"),
    h("p", {}, "Choose the lab your instructor names from the list on the left. Then work through its tabs from left to right, doing each numbered step in order."),
    h("p", {}, "Everything you type is saved automatically.")));
}

// ---------------------------------------------------------------- lab shell

function renderLab() {
  const lab = state.lab, tab = lab.tabs.find(t => t.id === state.tabId);
  const saved = h("span", { class: "saved", id: "saved" });
  bound.clear();
  const next = lab.tabs[lab.tabs.indexOf(tab) + 1];
  const main = document.getElementById("main");
  main.replaceChildren(
    h("div", { class: "lab-header" },
      h("h1", {}, lab.title),
      h("span", { class: "progress", id: "progress" }, progressText(lab.status)),
      h("button", { class: "btn subtle", onclick: resetLab }, "Reset this lab")),
    h("div", { class: "tabs", role: "tablist" },
      lab.tabs.map(t => h("button", {
        class: "tab" + (t.id === tab.id ? " active" : ""), role: "tab",
        onclick: () => go(lab.id, t.id),
      }, t.title))),
    h("div", { id: "panelwrap", style: "display:flex;flex-direction:column;flex:1;min-height:0" },
      h("div", { class: "tabbar-tools" }, saved, h("span", { class: "spacer" }),
        tab.type !== "steps" && h("button", { class: "btn", onclick: () => savePdf(tab) }, "Save as PDF")),
      h("div", { id: "panel" }, aboutBox(tab.about), renderTab(tab),
        tab.type === "steps" && next && h("div", { class: "next-tab" },
          h("span", {}, "Finished every step on this tab?"),
          h("button", { class: "btn primary", onclick: () => { go(lab.id, next.id); document.getElementById("panel").scrollTop = 0; } },
            `Go to the next tab: ${next.title} \u2192`)))));
}

// The plain-language box at the top of every tab: what this is, why it is here, what to do.
function aboutBox(a) {
  if (!a) return null;
  const row = (label, text) => text && h("p", {}, h("strong", {}, label + " "), text);
  return h("details", { class: "about", open: true },
    h("summary", { class: "about-title" }, "About this tab (click here to hide or show this box)"),
    row("What this is:", a.what),
    row("Why you are looking at it:", a.why),
    row("What to do here:", a.todo));
}

function renderTab(tab) {
  if (tab.type === "doc") return h("div", { class: "doc" }, docNode(tab.html));
  if (tab.type === "table") return renderTable(tab);
  if (tab.type === "steps") return renderSteps(tab);
  if (tab.type === "report") return renderReport(tab);
  return renderForm(tab);
}

function docNode(html) {
  const d = document.createElement("div");
  d.innerHTML = html;   // trusted: rendered server-side from course content
  return d;
}

async function resetLab() {
  if (!confirm("Reset this lab? This clears everything you have entered in it and cannot be undone.")) return;
  await flushSaves();
  const status = await api(`/api/labs/${state.lab.id}/answers`, { method: "DELETE" });
  state.answers = {};
  state.lab.status = status;
  updateStatus(state.lab.id, status);
  renderLab();
}

async function savePdf(tab) {
  await flushSaves();
  const a = h("a", { href: `/api/labs/${state.lab.id}/tabs/${tab.id}/pdf`, download: "" });
  document.body.append(a); a.click(); a.remove();
}

// ---------------------------------------------------------------- saving

function setSaved(text, ok) {
  const el = document.getElementById("saved");
  if (el) { el.textContent = text; el.className = "saved" + (ok ? " ok" : ""); }
}

function queueSave(key, value, from) {
  state.answers[key] = value;
  for (const fn of bound.get(key) || []) if (fn !== from) fn(value);
  clearTimeout(pending.get(key));
  setSaved("Saving…");
  const labId = state.lab.id;
  pending.set(key, setTimeout(() => doSave(labId, key, value), 500));
}

function doSave(labId, key, value) {
  pending.delete(key);
  state.queued++;
  saveChain = saveChain.then(() => sendSave(labId, key, value));
  return saveChain;
}

async function sendSave(labId, key, value) {
  state.saving++;
  try {
    const status = await api(`/api/labs/${labId}/answers`, {
      method: "PUT", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ key, value }),
    });
    if (state.lab && state.lab.id === labId) state.lab.status = status;
    updateStatus(labId, status);
    if (!pending.size && state.queued === 1) setSaved("✓ Saved", true);
  } catch (e) {
    setSaved("Could not save. Check your connection.");
  } finally { state.saving--; state.queued--; }
}

async function flushSaves() {
  const labId = state.lab && state.lab.id;
  const keys = [...pending.keys()];
  for (const k of keys) { clearTimeout(pending.get(k)); doSave(labId, k, state.answers[k] || ""); }
  await saveChain;
}

// ---------------------------------------------------------------- forms

function renderForm(tab) {
  const wrap = h("div", { class: "form" }, h("h1", {}, tab.heading));
  if (tab.intro) wrap.append(h("p", { class: "intro" }, tab.intro));
  for (const sec of tab.sections) {
    wrap.append(h("h2", {}, sec.title));
    if (sec.help) wrap.append(h("p", { class: "help" }, sec.help));
    for (const f of sec.fields) wrap.append(renderField(f));
  }
  return wrap;
}

// Remember a way to redraw this element when the same answer changes somewhere else on the page.
function bind(key, fn) {
  if (!bound.has(key)) bound.set(key, []);
  bound.get(key).push(fn);
  return fn;
}

function renderField(f) {
  const key = "f:" + f.id, id = "fld-" + f.id;
  let input;
  if (f.kind === "select") {
    input = h("select", { id }, h("option", { value: "" }, "Choose\u2026"),
      f.options.map(o => h("option", { value: o }, o)));
  } else if (f.kind === "textarea") {
    input = h("textarea", { id, rows: f.rows || 3 });
  } else {
    input = h("input", { id, type: "text", autocomplete: "off" });
  }
  input.value = state.answers[key] || "";
  const redraw = bind(key, v => { input.value = v; });
  input.addEventListener(f.kind === "select" ? "change" : "input", () => queueSave(key, input.value, redraw));
  return h("div", { class: "field" },
    h("label", { for: id }, f.label, !f.required && h("span", { class: "optional" }, " (optional)")),
    f.example && h("div", { class: "example" }, "Example: " + f.example),
    input);
}

// ---------------------------------------------------------------- steps

// A tab made of numbered steps. Each step is a coloured box holding the instructions and any
// answer boxes, followed by the material the student needs for that step.
function renderSteps(tab) {
  return h("div", { class: "steps" }, tab.steps.map(s => [
    h("section", { class: "step", id: `step-${s.number}` },
      h("div", { class: "step-label" }, `Step ${s.number}`),
      h("h2", { class: "step-title" }, s.title),
      h("div", { class: "step-text" }, docNode(s.html)),
      s.fields.map(renderField),
      s.hints.map(x => h("details", { class: "hint" }, h("summary", {}, x.title), docNode(x.html))),
      s.answer && h("details", { class: "hint answer" }, h("summary", {}, "Show the answer"), docNode(s.answer))),
    s.show.map(m => h("div", { class: "material" },
      m.kind === "doc" ? h("div", { class: "doc" }, docNode(m.html)) : renderTable(m))),
  ]));
}

// A read-only page that gathers the answers typed into the step boxes on the other tabs.
function renderReport(tab) {
  const wrap = h("div", { class: "form report" },
    h("p", { class: "report-note" }, "This page fills itself in from your answers on the other tabs. You cannot type here. To change an answer, change it in its step."),
    h("h1", {}, tab.heading));
  if (tab.intro) wrap.append(h("p", { class: "intro" }, tab.intro));
  for (const sec of tab.sections) {
    wrap.append(h("h2", {}, sec.title));
    if (sec.help) wrap.append(h("p", { class: "help" }, sec.help));
    for (const f of sec.fields) {
      const v = (state.answers["f:" + f.id] || "").trim();
      wrap.append(h("div", { class: "field" },
        h("div", { class: "report-label" }, f.label),
        v ? h("div", { class: "report-value" }, v)
          : h("div", { class: "report-value empty" }, `Not answered yet. Answer it in Step ${f.step}.`)));
    }
  }
  return wrap;
}

// ---------------------------------------------------------------- tables

function renderTable(tab) {
  // Just the live score panel, for steps that read the result of marking done in an earlier step.
  if (tab.view === "scorecard") return makeScorecard(tab, { open: true, sticky: false }).el;
  const ui = { sort: null, dir: 1, filters: {}, group: "", split: "" };
  const cols = tab.columns.filter(c => !(tab.hide || []).includes(c));
  const label = c => (tab.labels || {})[c] || c;
  const editable = tab.editable || {};
  const isNum = c => tab.rows.every(r => r[c] !== "" && !isNaN(Number(r[c])));
  const distinct = c => [...new Set(tab.rows.map(r => r[c]))].sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
  const smallSet = c => !(c in editable) && distinct(c).length <= 12 && distinct(c).length > 1 &&
    !(tab.summary && c === tab.summary.column);
  const groupable = cols.filter(smallSet);

  const base = (tab.show_rows || tab.rows.map((_, i) => i)).map(i => ({ r: tab.rows[i], i }));
  const tools_on = tab.tools !== false;
  const root = h("div", {});
  if (tab.note) root.append(h("p", { class: "table-note" }, tab.note));
  const card = tab.scorecard ? makeScorecard(tab) : null;
  if (card) root.append(card.el);
  const tools = h("div", { class: "table-tools" });
  const view = h("div", {});
  const count = h("span", { class: "count" });

  function select(label, onchange, options) {
    const s = h("select", { onchange: e => onchange(e.target.value) },
      h("option", { value: "" }, "None"), options.map(o => h("option", { value: o }, o)));
    return h("label", {}, label, s);
  }

  if (tools_on && groupable.length && !Object.keys(editable).length) {
    tools.append(
      select("Group by", v => { ui.group = v; draw(); }, groupable),
      select("Split by", v => { ui.split = v; draw(); }, groupable));
  }
  if (tools_on && !Object.keys(editable).length) {
    tools.append(h("button", { class: "btn", onclick: () => {
      ui.sort = null; ui.filters = {}; ui.group = ""; ui.split = "";
      tools.querySelectorAll("select").forEach(s => (s.value = ""));
      draw();
    } }, "Clear sort, filters and grouping"));
  }
  if (tools_on) tools.append(count);
  root.append(tools, view);

  function filtered() {
    return base.filter(({ r }) =>
      Object.entries(ui.filters).every(([c, v]) => {
        if (!v) return true;
        return smallSet(c) ? r[c] === v : r[c].toLowerCase().includes(v.toLowerCase());
      }));
  }

  function draw() {
    const rows = filtered();
    count.textContent = `Showing ${rows.length} of ${base.length} rows`;
    view.replaceChildren(ui.group ? groupView(rows) : rowView());
  }

  function rowView() {
    const heads = h("tr", { class: "heads" }, cols.map(c => h("th", {
      title: "Click to sort", onclick: () => {
        if (ui.sort === c) { if (ui.dir === 1) ui.dir = -1; else ui.sort = null; }
        else { ui.sort = c; ui.dir = 1; }
        draw();
      },
    }, label(c), ui.sort === c && h("span", { class: "arrow" }, ui.dir === 1 ? "▲" : "▼"))));
    const hasFilters = tools_on && !Object.keys(editable).length;
    const filters = h("tr", { class: "filters" }, cols.map(c => {
      if (c in editable) return h("th", {});
      let el;
      if (smallSet(c)) {
        el = h("select", { onchange: e => { ui.filters[c] = e.target.value; draw(); } },
          h("option", { value: "" }, "All"), distinct(c).map(v => h("option", { value: v }, v)));
      } else {
        el = h("input", { type: "search", placeholder: "Filter", oninput: e => { ui.filters[c] = e.target.value; drawBody(); } });
      }
      el.value = ui.filters[c] || "";
      return h("th", {}, el);
    }));
    const tbody = h("tbody", {});
    const table = h("table", { class: "data" }, h("thead", {}, heads, hasFilters && filters), tbody);

    function drawBody() {
      const rs = filtered();
      if (ui.sort) {
        const c = ui.sort, num = isNum(c);
        rs.sort((a, b) => ui.dir * (num ? Number(a.r[c]) - Number(b.r[c]) : a.r[c].localeCompare(b.r[c], undefined, { numeric: true })));
      }
      count.textContent = `Showing ${rs.length} of ${base.length} rows`;
      tbody.replaceChildren(...rs.map(({ r, i }) => h("tr", {}, cols.map(c => cell(r, i, c)))));
    }
    drawBody();
    return h("div", { class: "tablewrap" + (card ? " with-card" : "") }, table);
  }

  function cell(r, i, c) {
    if (c in editable) {
      const key = `t:${tab.id}:${i}:${c}`;
      if (tab.readonly) {
        const td = h("td", {});
        const show = v => {
          const o = editable[c].find(o => o.value === v);
          td.textContent = v ? (o ? o.label : v) : "(not chosen yet)";
          td.classList.toggle("unset-text", !v);
        };
        show(state.answers[key] || "");
        bind(key, show);
        return td;
      }
      const s = h("select", {}, h("option", { value: "" }, "Choose…"),
        editable[c].map(o => h("option", { value: o.value }, o.label)));
      s.value = state.answers[key] || "";
      const mark = () => s.classList.toggle("unset", !s.value);
      mark();
      const redraw = bind(key, v => { s.value = v; mark(); });
      s.addEventListener("change", () => { queueSave(key, s.value, redraw); mark(); if (card) card.update(); });
      return h("td", {}, s);
    }
    return h("td", { class: isNum(c) ? "num" : "" }, r[c]);
  }

  function groupView(rows) {
    const g = ui.group, sp = ui.split && ui.split !== ui.group ? ui.split : "";
    const sum = tab.summary;
    const groups = [...new Set(rows.map(x => x.r[g]))].sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
    const splits = sp ? [...new Set(rows.map(x => x.r[sp]))].sort((a, b) => a.localeCompare(b, undefined, { numeric: true })) : [];
    const fmt = list => {
      const n = list.length;
      if (!sum) return String(n);
      const k = list.reduce((t, x) => t + Number(x.r[sum.column]), 0);
      return n ? `${k}/${n} (${Math.round(100 * k / n)}%)` : "–";
    };
    const head = sp
      ? [g + " \\ " + sp, ...splits, "All"]
      : sum ? [g, "Rows", sum.label, "Rate"] : [g, "Rows"];
    const body = groups.map(v => {
      const list = rows.filter(x => x.r[g] === v);
      if (sp) return [v, ...splits.map(s => fmt(list.filter(x => x.r[sp] === s))), fmt(list)];
      if (!sum) return [v, String(list.length)];
      const k = list.reduce((t, x) => t + Number(x.r[sum.column]), 0);
      return [v, String(list.length), String(k), `${Math.round(100 * k / list.length)}%`];
    });
    let total;
    if (sp) total = ["All", ...splits.map(s => fmt(rows.filter(x => x.r[sp] === s))), fmt(rows)];
    else if (!sum) total = ["All", String(rows.length)];
    else {
      const k = rows.reduce((t, x) => t + Number(x.r[sum.column]), 0);
      total = ["All", String(rows.length), String(k), rows.length ? `${Math.round(100 * k / rows.length)}%` : "–"];
    }
    return h("div", { class: "tablewrap" }, h("table", { class: "data" },
      h("thead", {}, h("tr", { class: "heads" }, head.map(x => h("th", { style: "cursor:default" }, x)))),
      h("tbody", {}, body.map(r => h("tr", {}, r.map((x, j) => h("td", { class: j ? "num" : "" }, x)))),
        h("tr", { class: "total" }, total.map((x, j) => h("td", { class: j ? "num" : "" }, x))))));
  }

  draw();
  return root;
}

// ---------------------------------------------------------------- scorecard

// Live Business Quality Score panel. Current scores come from the row data, or from the
// student's dropdown answers when that column is editable.
function makeScorecard(tab, opts = {}) {
  const sc = tab.scorecard, editable = tab.editable || {};
  const marking = Object.keys(editable).length && !opts.open;
  const el = h("div", { class: "scorecard" + (marking && opts.sticky !== false ? " sticky" : "") });
  const cur = (i, col) => {
    const v = col in editable ? state.answers[`t:${tab.id}:${i}:${col}`] : tab.rows[i][col];
    return v === "1" ? 1 : v === "0" ? 0 : null;
  };
  const baselineBqs = Number((tab.rows.map(r => r[sc.baseline_bqs]).find(v => v !== "")) || NaN);

  function update() {
    const n = tab.rows.length, k = sc.criteria.length, total = n * k;
    let scored = 0, passed = 0, below = 0;
    const perCrit = sc.criteria.map(() => ({ now: 0, base: 0, scored: 0 }));
    tab.rows.forEach((r, i) => {
      let rowScored = 0, rowNow = 0, rowBase = 0;
      sc.criteria.forEach((c, j) => {
        const v = cur(i, c.current);
        const b = Number(r[c.baseline]) || 0;
        perCrit[j].base += b;
        rowBase += b;
        if (v !== null) { scored++; rowScored++; passed += v; rowNow += v; perCrit[j].now += v; perCrit[j].scored++; }
      });
      if (rowScored === k && rowNow < rowBase) below++;
    });
    const done = scored === total;
    const bqs = done ? Math.round(100 * passed / total) : null;
    const change = done && !isNaN(baselineBqs) ? bqs - baselineBqs : null;
    const stat = (name, value, hint) => h("div", { class: "stat" },
      h("div", { class: "stat-name" }, name), h("div", { class: "stat-value" }, value),
      hint && h("div", { class: "stat-hint" }, hint));
    el.replaceChildren(
      h("div", { class: "stats" },
        stat("Current Business Quality Score", done ? String(bqs) : "\u2013",
          done ? null : `Score every response to see it (${scored} of ${total} checks scored)`),
        stat("Recorded baseline", isNaN(baselineBqs) ? "\u2013" : String(baselineBqs)),
        stat("Change (points)", change === null ? "\u2013" : (change > 0 ? "+" : "") + change),
        stat("Responses below their own baseline", done ? `${below} of ${n}` : "\u2013")),
      h("details", { class: "crit-details", open: !marking },
        h("summary", {}, "How each criterion moved"),
      h("table", { class: "data crit" },
        h("thead", {}, h("tr", { class: "heads" },
          ["Criterion", "Passing now", "Passing at baseline", "Change"].map(x => h("th", { style: "cursor:default" }, x)))),
        h("tbody", {}, sc.criteria.map((c, j) => {
          const p = perCrit[j], d = p.now - p.base, ready = p.scored === n;
          return h("tr", {}, h("td", {}, c.label),
            h("td", { class: "num" }, ready ? `${p.now} of ${n}` : "\u2013"),
            h("td", { class: "num" }, `${p.base} of ${n}`),
            h("td", { class: "num" }, ready ? (d > 0 ? "+" : "") + d : "\u2013"));
        })))));
  }
  update();
  return { el, update };
}

// ---------------------------------------------------------------- start

window.addEventListener("hashchange", route);
window.addEventListener("beforeunload", () => {
  // Best-effort flush of edits still waiting on the 500 ms debounce.
  for (const [k, t] of pending) {
    clearTimeout(t);
    fetch(`/api/labs/${state.lab.id}/answers`, { method: "PUT", keepalive: true,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ key: k, value: state.answers[k] || "" }) });
  }
});
(async () => { await loadSidebar(); await route(); })();
