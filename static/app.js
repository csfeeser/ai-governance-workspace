// AI Governance workspace front end. No build step, no dependencies.
"use strict";

const state = { labs: [], lab: null, tabId: null, answers: {}, saving: 0 };
const pending = new Map();   // key -> timeout id, for debounced saves

// ---------------------------------------------------------------- helpers

function h(tag, attrs, ...children) {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (k === "class") el.className = v;
    else if (k.startsWith("on")) el.addEventListener(k.slice(2), v);
    else if (v !== false && v != null) el.setAttribute(k, v === true ? "" : v);
  }
  for (const c of children.flat()) {
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
    h("p", {}, "Choose a lab from the list on the left. Your course page tells you which lab to open and which tab to use."),
    h("p", {}, "Everything you type is saved automatically.")));
}

// ---------------------------------------------------------------- lab shell

function renderLab() {
  const lab = state.lab, tab = lab.tabs.find(t => t.id === state.tabId);
  const saved = h("span", { class: "saved", id: "saved" });
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
        h("button", { class: "btn", onclick: () => savePdf(tab) }, "Save as PDF")),
      h("div", { id: "panel" }, renderTab(tab))));
}

function renderTab(tab) {
  if (tab.type === "doc") return h("div", { class: "doc" }, docNode(tab.html));
  if (tab.type === "table") return renderTable(tab);
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

function queueSave(key, value) {
  state.answers[key] = value;
  clearTimeout(pending.get(key));
  setSaved("Saving…");
  const labId = state.lab.id;
  pending.set(key, setTimeout(() => doSave(labId, key, value), 500));
}

async function doSave(labId, key, value) {
  pending.delete(key);
  state.saving++;
  try {
    const status = await api(`/api/labs/${labId}/answers`, {
      method: "PUT", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ key, value }),
    });
    if (state.lab && state.lab.id === labId) state.lab.status = status;
    updateStatus(labId, status);
    if (!pending.size) setSaved("✓ Saved", true);
  } catch (e) {
    setSaved("Could not save. Check your connection.");
  } finally { state.saving--; }
}

async function flushSaves() {
  const labId = state.lab && state.lab.id;
  const keys = [...pending.keys()];
  for (const k of keys) { clearTimeout(pending.get(k)); await doSave(labId, k, state.answers[k] || ""); }
}

// ---------------------------------------------------------------- forms

function renderForm(tab) {
  const wrap = h("div", { class: "form" }, h("h1", {}, tab.heading));
  if (tab.intro) wrap.append(h("p", { class: "intro" }, tab.intro));
  for (const sec of tab.sections) {
    wrap.append(h("h2", {}, sec.title));
    if (sec.help) wrap.append(h("p", { class: "help" }, sec.help));
    for (const f of sec.fields) {
      const key = "f:" + f.id, id = "fld-" + f.id;
      const input = f.kind === "textarea"
        ? h("textarea", { id, rows: f.rows || 3 })
        : h("input", { id, type: "text", autocomplete: "off" });
      input.value = state.answers[key] || "";
      input.addEventListener("input", () => queueSave(key, input.value));
      wrap.append(h("div", { class: "field" },
        h("label", { for: id }, f.label, !f.required && h("span", { class: "optional" }, " (optional)")),
        f.example && h("div", { class: "example" }, "Example: " + f.example),
        input));
    }
  }
  return wrap;
}

// ---------------------------------------------------------------- tables

function renderTable(tab) {
  const ui = { sort: null, dir: 1, filters: {}, group: "", split: "" };
  const cols = tab.columns;
  const editable = tab.editable || {};
  const isNum = c => tab.rows.every(r => r[c] !== "" && !isNaN(Number(r[c])));
  const distinct = c => [...new Set(tab.rows.map(r => r[c]))].sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
  const smallSet = c => !(c in editable) && distinct(c).length <= 12 && distinct(c).length > 1 &&
    !(tab.summary && c === tab.summary.column);
  const groupable = cols.filter(smallSet);

  const root = h("div", {});
  if (tab.note) root.append(h("p", { class: "table-note" }, tab.note));
  const tools = h("div", { class: "table-tools" });
  const view = h("div", {});
  const count = h("span", { class: "count" });

  function select(label, onchange, options) {
    const s = h("select", { onchange: e => onchange(e.target.value) },
      h("option", { value: "" }, "None"), options.map(o => h("option", { value: o }, o)));
    return h("label", {}, label, s);
  }

  if (groupable.length && !Object.keys(editable).length) {
    tools.append(
      select("Group by", v => { ui.group = v; draw(); }, groupable),
      select("Split by", v => { ui.split = v; draw(); }, groupable));
  }
  tools.append(h("button", { class: "btn", onclick: () => {
    ui.sort = null; ui.filters = {}; ui.group = ""; ui.split = "";
    tools.querySelectorAll("select").forEach(s => (s.value = ""));
    draw();
  } }, "Clear sort, filters and grouping"), count);
  root.append(tools, view);

  function filtered() {
    return tab.rows.map((r, i) => ({ r, i })).filter(({ r }) =>
      Object.entries(ui.filters).every(([c, v]) => {
        if (!v) return true;
        return smallSet(c) ? r[c] === v : r[c].toLowerCase().includes(v.toLowerCase());
      }));
  }

  function draw() {
    const rows = filtered();
    count.textContent = `Showing ${rows.length} of ${tab.rows.length} rows`;
    view.replaceChildren(ui.group ? groupView(rows) : rowView());
  }

  function rowView() {
    const heads = h("tr", { class: "heads" }, cols.map(c => h("th", {
      title: "Click to sort", onclick: () => {
        if (ui.sort === c) { if (ui.dir === 1) ui.dir = -1; else ui.sort = null; }
        else { ui.sort = c; ui.dir = 1; }
        draw();
      },
    }, c, ui.sort === c && h("span", { class: "arrow" }, ui.dir === 1 ? "▲" : "▼"))));
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
    const table = h("table", { class: "data" }, h("thead", {}, heads, filters), tbody);

    function drawBody() {
      const rs = filtered();
      if (ui.sort) {
        const c = ui.sort, num = isNum(c);
        rs.sort((a, b) => ui.dir * (num ? Number(a.r[c]) - Number(b.r[c]) : a.r[c].localeCompare(b.r[c], undefined, { numeric: true })));
      }
      count.textContent = `Showing ${rs.length} of ${tab.rows.length} rows`;
      tbody.replaceChildren(...rs.map(({ r, i }) => h("tr", {}, cols.map(c => cell(r, i, c)))));
    }
    drawBody();
    return h("div", { class: "tablewrap" }, table);
  }

  function cell(r, i, c) {
    if (c in editable) {
      const key = `t:${tab.id}:${i}:${c}`;
      const s = h("select", {}, h("option", { value: "" }, "Choose…"),
        editable[c].map(o => h("option", { value: o }, o)));
      s.value = state.answers[key] || "";
      const mark = () => s.classList.toggle("unset", !s.value);
      mark();
      s.addEventListener("change", () => { queueSave(key, s.value); mark(); });
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
