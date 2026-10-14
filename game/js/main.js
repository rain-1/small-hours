import { Audio } from "./audio.js";
import { SceneView } from "./scene.js";
import { SPEAKERS, SCENES, MAP_PINS, MAP_FALLBACK, pinHasTask, ORDERS, objective, PEOPLE, WORDS, NOTICED, epilogueCards } from "./data.js";

const $ = s => document.querySelector(s);
const SAVE_KEY = "smallhours.save.v1";
const SETTINGS_KEY = "smallhours.settings.v1";

const audio = new Audio();
const UI_SFX = new Set(["order", "time", "click", "discover", "word", "journal"]);
let portraitSet = null;
const view = new SceneView($("#view"));
let story, storyJson, layout = {}, figuresMeta = {};
let sceneId = null;
let busy = false;         // dialogue / transition running
let overlay = null;       // open overlay id
let settings = { music: 70, sfx: 80, speed: 60 };
let journalTab = "people";
let journalUnseen = false;
let lastLists = { noticed: new Set(), words: new Set() };
let lastOrders = {};
let pendingScene = null;
let ended = false;

// ---------------------------------------------------------------- ink vars
const v = new Proxy({}, {
  get(_, k) {
    if (k === "has") return (list, item) => listItems(list).has(item);
    if (k === "wordCount") return listItems("words").size;
    const val = story.variablesState.$(k);
    if (val && typeof val === "object" && val.Count !== undefined) return val;
    return val;
  },
});
function listItems(name) {
  const l = story.variablesState.$(name);
  const out = new Set();
  if (!l) return out;
  for (const [key] of l) {
    try { out.add(JSON.parse(key).itemName); } catch { out.add(String(key).split(".").pop()); }
  }
  return out;
}
const resolve = (x, ...a) => (typeof x === "function" ? x(v, ...a) : x);

// ---------------------------------------------------------------- scaling
function fit() {
  const k = Math.min(innerWidth / 640, innerHeight / 360);
  const s = k >= 2 ? Math.floor(k * 4) / 4 : k;
  $("#stage").style.transform = `scale(${s})`;
}
addEventListener("resize", fit);
fit();
function toCanvas(e) {
  const r = $("#stage").getBoundingClientRect();
  return { x: (e.clientX - r.left) * 640 / r.width, y: (e.clientY - r.top) * 360 / r.height };
}

// ---------------------------------------------------------------- boot
async function boot() {
  try { Object.assign(settings, JSON.parse(localStorage.getItem(SETTINGS_KEY) || "{}")); } catch {}
  const bar = $("#loading-bar div");
  const step = p => (bar.style.width = `${p}%`);
  const getJSON = (p, d) => fetch(p).then(r => (r.ok ? r.json() : d)).catch(() => d);
  step(10);
  storyJson = await fetch("story/story.json").then(r => r.text());
  step(40);
  layout = await getJSON("data/layout.json", {});
  figuresMeta = await getJSON("art/figures/figures.json", {});
  portraitSet = new Set(await getJSON("art/portraits/index.json", []));
  step(60);
  // warm the image cache
  const imgs = Object.values(SCENES).map(s => `art/${s.bg}.png`).concat(["art/bg_title.png", "art/bg_map.png"]);
  await Promise.all(imgs.map(p => view.img(p)));
  step(100);
  $("#loading").classList.add("hidden");
  $("#click-to-start").classList.remove("hidden");
  $("#click-to-start").addEventListener("click", () => {
    audio.init();
    applySettings();
    audio.preload(["ui/blip.mp3", "ui/click.mp3", "ui/discover.mp3", "ui/word.mp3", "ui/order.mp3", "ui/hover.mp3"]);
    $("#click-to-start").classList.add("hidden");
    showTitle();
  }, { once: true });
  requestAnimationFrame(loop);
}

function newStory() {
  story = new inkjs.Story(storyJson);
  story.onError = (msg) => console.error("ink:", msg);
}

// ---------------------------------------------------------------- title
async function showTitle() {
  ended = false;
  $("#hud").classList.add("hidden");
  $("#dialogue").classList.add("hidden");
  $("#epilogue").classList.add("hidden");
  const bg = await view.img("art/bg_title.png");
  view.scene = { rain: true, ground: 300 };
  view.bg = bg || (await view.img("art/bg_street.png"));
  view.figures = []; view.hotspots = []; view.tint = null;
  sceneId = null;
  $("#title").classList.remove("hidden");
  $("#btn-continue").classList.toggle("hidden", !localStorage.getItem(SAVE_KEY));
  audio.playMusic("title");
  audio.playAmb("amb_rain");
}

$("#btn-new").addEventListener("click", () => {
  audio.ui("click");
  $("#title").classList.add("hidden");
  $("#name-entry").classList.remove("hidden");
  overlay = "name";
  setTimeout(() => { $("#name-input").focus(); $("#name-input").select(); }, 50);
});
$("#name-ok").addEventListener("click", startNew);
$("#name-input").addEventListener("keydown", e => { if (e.key === "Enter") startNew(); e.stopPropagation(); });

async function startNew() {
  const name = ($("#name-input").value || "Kit").trim().slice(0, 14) || "Kit";
  $("#name-entry").classList.add("hidden");
  overlay = null;
  audio.ui("click");
  newStory();
  story.variablesState.$("name", name);
  snapshotLists(true);
  await fadeOut();
  await setScene("shop", { quiet: true });
  $("#hud").classList.remove("hidden");
  await fadeIn();
  await runKnot("start");
  toast("notice", "HOW TO PLAY", "Click people and things. J journal · M map · T Moth");
}

$("#btn-continue").addEventListener("click", async () => {
  audio.ui("click");
  const save = JSON.parse(localStorage.getItem(SAVE_KEY));
  newStory();
  story.state.LoadJson(save.ink);
  snapshotLists(true);
  $("#title").classList.add("hidden");
  await fadeOut();
  await setScene(save.scene || "shop", { quiet: true });
  $("#hud").classList.remove("hidden");
  await fadeIn();
  toast("notice", "WELCOME BACK", `${clockText()} on Halfmoon Street.`);
});

function save() {
  if (!story || ended) return;
  try { localStorage.setItem(SAVE_KEY, JSON.stringify({ ink: story.state.toJson(), scene: sceneId, at: Date.now() })); } catch {}
}

// ---------------------------------------------------------------- scenes
function fadeOut() { $("#fade").classList.add("on"); return wait(450); }
function fadeIn() { $("#fade").classList.remove("on"); return wait(300); }
const wait = ms => new Promise(r => setTimeout(r, ms));

async function setScene(id, { quiet = false } = {}) {
  const sc = SCENES[id];
  if (!sc) { console.warn("no scene", id); return; }
  sceneId = id;
  story.variablesState.$("here", id === "roofs_dawn" ? "roofs" : id);
  await refreshScene();
  if (!quiet || true) {
    if (sc.music) audio.playMusic(sc.music);
    if (sc.amb) audio.playAmb(sc.amb);
  }
  updateTint();
}

async function refreshScene() {
  const sc = SCENES[sceneId];
  const lay = layout[sc.layout || sceneId] || { hotspots: {}, figures: {} };
  const hotspots = [];
  for (const [hid, rect] of Object.entries(lay.hotspots || {})) {
    const lab = sc.labels[hid];
    if (lab === undefined) continue;
    const [label, kind] = Array.isArray(lab) ? [resolve(lab[0]), resolve(lab[1])] : [resolve(lab), "look"];
    hotspots.push({ id: hid, x: rect[0], y: rect[1], w: rect[2], h: rect[3], label, kind, knot: `${sceneId}_${hid}` });
  }
  const figs = (sc.figures(v) || []).filter(Boolean).map(f => {
    const at = (lay.figures || {})[f.at];
    if (!at) return null;
    return { ...f, x: at[0], y: at[1], kind: "talk" };
  }).filter(f => f && !f.hidden);
  // steam emitters from layout
  const scn = { ...sc };
  if (sc.steam && lay.hotspots) {
    const src = sceneId === "shop" ? lay.hotspots.pot : sceneId === "alley" ? lay.hotspots.steam_vent : null;
    if (src) scn.steam = [[src[0] + src[2] / 2, src[1] + 4, sc.steam[0][2]]];
  }
  await view.set(scn, sc.bg, figs, hotspots, lay.occluders ? Object.values(lay.occluders) : null);
}

function updateTint() {
  const sc = SCENES[sceneId] || {};
  const t = story ? v.time : 0;
  if (sceneId === "roofs_dawn" || sceneId === "hill_road") { view.tint = null; return; }
  let tint = null;
  if (t >= 480) tint = "rgba(110,70,140,0.10)";
  else if (t >= 360) tint = "rgba(30,25,90,0.14)";
  else if (t >= 180) tint = "rgba(20,30,80,0.08)";
  if (sc.indoor && tint) tint = tint.replace(/0\.\d+\)$/, "0.05)");
  view.tint = tint;
}

// ---------------------------------------------------------------- story running
function knotExists(name) {
  try { return !!story.KnotContainerWithName(name); } catch { return false; }
}

async function runKnot(name) {
  if (!knotExists(name)) return false;
  busy = true;
  setHover(null);
  pendingScene = null;
  story.ChoosePathString(name);
  await runStory();
  busy = false;
  return true;
}

async function runStory() {
  let shown = false;
  for (;;) {
    while (story.canContinue) {
      const text = story.Continue().trim();
      const tags = story.currentTags || [];
      await handleTags(tags);
      afterStep();
      if (text) {
        if (!shown) { showDialogue(); shown = true; }
        await showLine(text);
      }
    }
    if (story.currentChoices.length) {
      if (!shown) { showDialogue(); shown = true; }
      const idx = await showChoices(story.currentChoices);
      story.ChooseChoiceIndex(idx);
      continue;
    }
    break;
  }
  hideDialogue();
  afterStep();
  if (ended) return;
  // arriving somewhere new during the knot -> run that scene's enter knot
  if (pendingScene) {
    const s = pendingScene;
    pendingScene = null;
    story.ChoosePathString(`enter_${s === "roofs_dawn" ? "roofs" : s}`);
    await runStory();
    return;
  }
  await refreshScene();
  save();
}

async function handleTags(tags) {
  for (const raw of tags) {
    const [k, val] = raw.split(":").map(s => s.trim());
    switch (k) {
      case "go":
        if (val !== sceneId) {
          await fadeOut();
          await setScene(val);
          await fadeIn();
          pendingScene = val;
        }
        break;
      case "sfx": UI_SFX.has(val) ? audio.ui(val, 0.6) : audio.sfx(val); break;
      case "music": audio.playMusic(val, { loop: val !== "dawn" }); break;
      case "amb": audio.playAmb(val); break;
      case "fx":
        if (val === "flicker") view.flicker = 1.8;
        if (val === "flash") view.flash = 1;
        if (val === "dark") { view.flicker = 1.2; setTimeout(() => (view.tint = "rgba(5,4,20,0.45)"), 1200); }
        if (val === "dawn") { view.flash = 1.2; view.tint = null; }
        break;
      case "end": ended = true; setTimeout(runEpilogue, 600); break;
      case "wait": await wait(800); break;
    }
  }
}

// diff ink state → toasts, HUD
function snapshotLists(silent) {
  for (const name of ["noticed", "words"]) lastLists[name] = listItems(name);
  for (const o of ORDERS) lastOrders[o.key] = v[o.key];
  if (!silent) updateHUD();
  updateHUD();
}
function afterStep() {
  if (!story) return;
  const noticed = listItems("noticed"), words = listItems("words");
  for (const n of noticed) if (!lastLists.noticed.has(n)) {
    const [title] = NOTICED[n] || [n];
    toast("notice", "NOTICED", title);
    audio.ui("discover", 0.45);
    journalUnseen = true;
  }
  for (const w of words) if (!lastLists.words.has(w)) {
    const [who] = WORDS[w] || [w];
    toast("word", "A WORD FOR THE MORNING", `from ${who}`);
    audio.ui("word", 0.55);
    journalUnseen = true;
  }
  let newOrder = false;
  for (const o of ORDERS) {
    const val = v[o.key];
    if (val === 1 && lastOrders[o.key] !== 1) newOrder = true;
    if (val === 2 && lastOrders[o.key] === 1) toast("order", "DELIVERED", `${o.who} — ${o.what}`);
    lastOrders[o.key] = val;
  }
  if (newOrder) audio.ui("order", 0.5);
  lastLists = { noticed, words };
  updateHUD();
  updateTint();
}

// ---------------------------------------------------------------- dialogue UI
let advanceResolve = null, typing = false, skipTyping = false;

function showDialogue() { $("#dialogue").classList.remove("hidden"); $("#dialogue").classList.add("dim"); }
function hideDialogue() {
  $("#dialogue").classList.add("hidden");
  $("#portrait").classList.add("hidden");
  $("#choices").innerHTML = "";
}

function parseLine(text) {
  const m = text.match(/^@(\w+)(?::(\w+))?\s*(.*)$/s);
  if (!m) return { who: null, mood: null, text };
  return { who: m[1], mood: m[2] || "neutral", text: m[3] };
}

async function showLine(raw) {
  const { who, mood, text } = parseLine(raw);
  const sp = who ? SPEAKERS[who] || { name: who } : null;
  const lineEl = $("#line"), spEl = $("#speaker"), pEl = $("#portrait"), dlg = $("#dialogue");
  $("#choices").innerHTML = "";
  lineEl.className = "";
  if (!sp) lineEl.classList.add("narration");
  else if (sp.style) lineEl.classList.add(sp.style);
  spEl.textContent = sp ? resolve(sp.name) : "";
  // portrait
  const pid = sp && sp.portrait !== false ? sp.portraitAs || who : null;
  if (pid) {
    const name = portraitSet && !portraitSet.has(`${pid}_${mood}`) ? `${pid}_neutral` : `${pid}_${mood}`;
    pEl.src = `art/portraits/${name}.png`;
    pEl.classList.remove("hidden");
    pEl.classList.toggle("radio", !!sp.radio);
    dlg.classList.add("has-portrait");
  } else {
    pEl.classList.add("hidden");
    dlg.classList.remove("has-portrait");
  }
  await typeText(lineEl, text, sp);
  $("#advance").classList.add("show");
  await new Promise(r => (advanceResolve = r));
  $("#advance").classList.remove("show");
  audio.ui("click", 0.15, 1.3);
}

function typeText(el, html, sp) {
  // split into tokens, keeping <tags> whole
  const tokens = html.match(/<[^>]+>|&[a-z]+;|[\s\S]/g) || [];
  el.innerHTML = "";
  typing = true; skipTyping = false;
  const speed = settings.speed;
  const delay = speed >= 100 ? 0 : 8 + (100 - speed) * 0.45;
  const pitch = sp ? sp.pitch || 1 : 0.9;
  let i = 0, buf = "";
  return new Promise(res => {
    const step = () => {
      if (skipTyping || delay === 0) { el.innerHTML = html; typing = false; return res(); }
      let n = 0;
      while (i < tokens.length && n < 1) {
        const t = tokens[i++];
        buf += t;
        if (!t.startsWith("<")) n++;
      }
      el.innerHTML = buf + (tokens.slice(i).some(t => t.startsWith("</")) ? "" : "");
      const ch = tokens[i - 1] || "";
      if (sp && !sp.silent && /[a-z0-9]/i.test(ch) && i % 2 === 0) audio.blip(pitch);
      if (i >= tokens.length) { el.innerHTML = html; typing = false; return res(); }
      const pause = /[.!?…]/.test(ch) ? delay * 7 : /[,;:—]/.test(ch) ? delay * 3.5 : delay;
      setTimeout(step, pause);
    };
    step();
  });
}

function showChoices(choices) {
  return new Promise(res => {
    const box = $("#choices");
    $("#advance").classList.remove("show");
    // keep the last line visible above choices only if short
    box.innerHTML = "";
    choices.forEach((c, i) => {
      const b = document.createElement("button");
      b.innerHTML = `<span class="num">${i + 1}</span>${c.text}`;
      b.addEventListener("click", e => { e.stopPropagation(); pick(i); });
      b.addEventListener("mouseenter", () => audio.ui("hover", 0.2));
      box.appendChild(b);
    });
    const pick = i => {
      choiceResolve = null;
      audio.ui("click", 0.4);
      box.innerHTML = "";
      res(i);
    };
    choiceResolve = pick;
  });
}
let choiceResolve = null;

$("#box").addEventListener("click", advance);
function advance() {
  if (typing) { skipTyping = true; return; }
  if (advanceResolve) { const r = advanceResolve; advanceResolve = null; r(); }
}

// ---------------------------------------------------------------- HUD
function clockText() {
  const t = story ? v.time : 0;
  const mins = (21 * 60 + t) % (24 * 60);
  let h = Math.floor(mins / 60), m = mins % 60;
  const ampm = h >= 12 && h < 24 ? (h >= 21 ? "PM" : "PM") : "AM";
  const disp = ((h + 11) % 12) + 1;
  return `${disp}:${String(m).padStart(2, "0")} ${h >= 12 ? "PM" : "AM"}`;
}

function updateHUD() {
  if (!story) return;
  const [time, ampm] = clockText().split(" ");
  $("#clock-time").textContent = time;
  $("#clock-ampm").textContent = ampm;
  $("#objective").textContent = objective(v);
  // tickets
  const tk = $("#tickets");
  const active = ORDERS.filter(o => v[o.key] === 1);
  const sig = active.map(o => o.key).join();
  if (tk.dataset.sig !== sig) {
    tk.dataset.sig = sig;
    tk.innerHTML = active.map(o => `<div class="ticket"><b>${o.who}</b>${o.where}</div>`).join("");
  }
  const tape = v.mae_tape === 1;
  if (tape && !tk.querySelector(".tape")) tk.insertAdjacentHTML("beforeend", `<div class="ticket tape"><b>Cassette</b>for Mae</div>`);
  if (!tape && tk.querySelector(".tape")) tk.querySelector(".tape").remove();
  $("#journal-badge").classList.toggle("hidden", !journalUnseen);
  $("#btn-moth").classList.toggle("hidden", v.act === 0 || v.act === 4);
  $("#btn-map").classList.toggle("hidden", v.act === 0 || v.act === 4);
}

function updateCountdown() {
  if (!story) return;
  const left = Math.max(0, 554 - v.time);
  const el = $("#countdown-val");
  if (v.act === 4 && v.time >= 554) { el.textContent = "GOOD MORNING"; return; }
  const s = 59 - (Math.floor(performance.now() / 1000) % 60);
  const h = Math.floor(left / 60), m = left % 60;
  el.textContent = left === 0 ? "0:00:00" : `${h}:${String(Math.max(0, m - 1)).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
}

function toast(kind, k, text) {
  const t = document.createElement("div");
  t.className = `toast ${kind}`;
  t.innerHTML = `<span class="k">${k}</span>${text}`;
  $("#toast-area").appendChild(t);
  setTimeout(() => t.remove(), 4300);
  while ($("#toast-area").children.length > 5) $("#toast-area").firstChild.remove();
}

// ---------------------------------------------------------------- hover/click
function setHover(h) {
  view.hover = h;
  const el = $("#hover-label");
  if (!h) { el.classList.add("hidden"); $("#stage").style.cursor = ""; return; }
  el.textContent = h.label;
  el.className = h.kind === "talk" ? "talk" : h.kind === "go" ? "go" : "";
  el.style.left = `${Math.min(600, Math.max(40, h.x + h.w / 2))}px`;
  el.style.top = `${Math.max(16, h.y)}px`;
  $("#stage").style.cursor = "pointer";
}

$("#stage").addEventListener("mousemove", e => {
  if (busy || overlay || !sceneId || ended) { if (view.hover) setHover(null); return; }
  const { x, y } = toCanvas(e);
  const h = view.hit(x, y);
  if ((h && h.id) !== (view.hover && view.hover.id)) {
    if (h) audio.ui("hover", 0.12);
    setHover(h);
  }
});

$("#view").addEventListener("click", async e => {
  if (busy || overlay || !sceneId || ended) return;
  const { x, y } = toCanvas(e);
  const h = view.hit(x, y);
  if (!h) return;
  audio.ui("click", 0.3);
  setHover(null);
  const knot = h.knot;
  if (!(await runKnot(knot))) {
    busy = true; showDialogue();
    await showLine(h.kind === "go" ? "You can't go that way right now." : `Nothing more to see here.`);
    hideDialogue(); busy = false;
  }
});

addEventListener("keydown", e => {
  if (overlay === "name") return;
  const k = e.key.toLowerCase();
  if (k === " " || k === "enter") {
    if (!$("#dialogue").classList.contains("hidden") && !choiceResolve) { e.preventDefault(); advance(); }
    return;
  }
  if (choiceResolve && /^[1-9]$/.test(k)) {
    const btns = $("#choices").querySelectorAll("button");
    const i = +k - 1;
    if (btns[i]) btns[i].click();
    return;
  }
  if (k === "escape") { overlay ? closeOverlay() : (sceneId && openMenu()); return; }
  if (busy || !sceneId || ended) return;
  if (k === "j") toggleJournal();
  if (k === "m" && v.act >= 1 && v.act < 4) toggleMap();
  if (k === "t" && v.act >= 1 && v.act < 4) talkMoth();
});

// ---------------------------------------------------------------- buttons
$("#btn-moth").addEventListener("click", talkMoth);
$("#btn-map").addEventListener("click", toggleMap);
$("#btn-journal").addEventListener("click", toggleJournal);
$("#btn-menu").addEventListener("click", openMenu);

async function talkMoth() {
  if (busy || overlay) return;
  audio.ui("click", 0.4);
  await runKnot("moth_talk");
}

function closeOverlay() {
  document.querySelectorAll(".overlay").forEach(o => o.classList.add("hidden"));
  if (overlay === "menu") saveSettings();
  overlay = null;
}
document.querySelectorAll(".overlay .close").forEach(b => b.addEventListener("click", () => { audio.ui("click", 0.3); closeOverlay(); }));

// ---- journal
function toggleJournal() {
  if (busy) return;
  if (overlay === "journal") return closeOverlay();
  closeOverlay();
  overlay = "journal";
  journalUnseen = false;
  audio.ui("journal", 0.5);
  renderJournal();
  $("#journal").classList.remove("hidden");
  updateHUD();
}
document.querySelectorAll(".tabs button[data-tab]").forEach(b => b.addEventListener("click", () => {
  journalTab = b.dataset.tab;
  document.querySelectorAll(".tabs button[data-tab]").forEach(x => x.classList.toggle("active", x === b));
  audio.ui("click", 0.3);
  renderJournal();
}));

function renderJournal() {
  const body = $("#journal-body");
  if (journalTab === "people") {
    body.innerHTML = `<div class="people-grid">${PEOPLE.map(p => {
      const known = p.known(v);
      const notes = known ? p.notes.filter(([, c]) => c(v)).map(([t]) => `<li>${t}</li>`).join("") : "";
      const portrait = p.id === "moth" ? "moth_neutral" : `${p.id}_neutral`;
      return `<div class="person ${known ? "" : "unknown"}"><img src="art/portraits/${portrait}.png" style="${known ? "" : "filter:brightness(0)"}"><div><div class="nm">${known ? p.name : "???"}</div><div class="role">${known ? p.role : "Someone on Halfmoon Street"}</div><ul>${notes}</ul></div></div>`;
    }).join("")}</div>`;
  } else if (journalTab === "words") {
    const have = listItems("words");
    const ids = Object.keys(WORDS);
    body.innerHTML = `<h3>Words for the Morning</h3><div class="counter">${have.size} of ${ids.length} gathered — Mae will broadcast three of them, and yours, at 6:13.</div>` +
      ids.map(id => have.has(id)
        ? `<div class="word-card"><span class="who">${WORDS[id][0]}</span>“${WORDS[id][1]}”</div>`
        : `<div class="word-card missing"><span class="who">???</span>Someone hasn't said theirs yet.</div>`).join("");
  } else {
    const have = listItems("noticed");
    const ids = Object.keys(NOTICED);
    const cats = ids.filter(i => i.startsWith("cat_")), kind = ids.filter(i => i.startsWith("k_")), rest = ids.filter(i => !i.startsWith("cat_") && !i.startsWith("k_"));
    const item = id => have.has(id) ? `<div class="notice"><b>${NOTICED[id][0]}</b> — ${NOTICED[id][1]}</div>` : `<div class="notice missing"><b>???</b></div>`;
    const cnt = a => a.filter(i => have.has(i)).length;
    body.innerHTML = `<div class="counter">Noticed ${have.size} of ${ids.length} things on Halfmoon Street.</div>
      <h3>The cat's names (${cnt(cats)}/${cats.length})</h3><div class="notice-list">${cats.map(item).join("")}</div>
      <h3>Unassigned kindnesses (${cnt(kind)}/${kind.length})</h3><div class="notice-list">${kind.map(item).join("")}</div>
      <h3>Everything else (${cnt(rest)}/${rest.length})</h3><div class="notice-list">${rest.map(item).join("")}</div>`;
  }
}

// ---- map
async function toggleMap() {
  if (busy) return;
  if (overlay === "map") return closeOverlay();
  closeOverlay();
  overlay = "map";
  audio.ui("journal", 0.4);
  const map = $("#map");
  map.style.background = `url(art/bg_map.png) center/640px 360px, rgba(7,6,13,.9)`;
  map.style.imageRendering = "pixelated";
  const lay = (layout.map && layout.map.hotspots) || {};
  const here = sceneId === "teo_room" ? "laundromat" : sceneId === "roofs_dawn" ? "roofs" : sceneId;
  $("#map-pins").innerHTML = "";
  for (const p of MAP_PINS) {
    const r = lay[p.id];
    const [x, y] = r ? [r[0] + r[2] / 2, r[1] + r[3] / 2] : MAP_FALLBACK[p.id];
    const open = p.open(v);
    const el = document.createElement("div");
    el.className = `pin ${p.id === here ? "here" : ""} ${open ? "" : "locked"}`;
    el.style.left = `${x}px`; el.style.top = `${y}px`;
    el.innerHTML = `${open ? p.label : "???"}${open && pinHasTask(p.id, v) ? '<span class="dot"></span>' : ""}`;
    el.addEventListener("click", () => travel(p.scene));
    $("#map-pins").appendChild(el);
  }
  map.classList.remove("hidden");
}

async function travel(scene) {
  closeOverlay();
  if (scene === sceneId) return;
  busy = true;
  audio.sfx("scooter", { vol: 0.6 });
  await fadeOut();
  await setScene(scene);
  await fadeIn();
  busy = false;
  await runKnot(`enter_${scene}`);
  save();
}

// ---- menu
function openMenu() {
  if (busy && !$("#dialogue").classList.contains("hidden")) return;
  closeOverlay();
  overlay = "menu";
  $("#vol-music").value = settings.music;
  $("#vol-sfx").value = settings.sfx;
  $("#text-speed").value = settings.speed;
  $("#menu").classList.remove("hidden");
}
function applySettings() { audio.setVolumes({ music: settings.music / 100, sfx: settings.sfx / 100 }); }
function saveSettings() { try { localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings)); } catch {} }
["vol-music", "vol-sfx", "text-speed"].forEach(id => $(`#${id}`).addEventListener("input", e => {
  const key = { "vol-music": "music", "vol-sfx": "sfx", "text-speed": "speed" }[id];
  settings[key] = +e.target.value;
  applySettings();
}));
$("#menu-resume").addEventListener("click", closeOverlay);
$("#menu-title").addEventListener("click", async () => { save(); closeOverlay(); await fadeOut(); await showTitle(); await fadeIn(); });

// ---------------------------------------------------------------- epilogue
async function runEpilogue() {
  try { localStorage.removeItem(SAVE_KEY); } catch {}
  $("#hud").classList.add("hidden");
  hideDialogue();
  await fadeOut();
  view.bg = await view.img("art/bg_roofs_dawn.png");
  view.figures = []; view.hotspots = []; view.tint = "rgba(13,11,26,0.55)";
  view.scene = {};
  audio.playAmb("amb_dawn");
  audio.playMusic("credits", { loop: false });
  const inner = $("#epilogue-inner");
  const cards = epilogueCards(v);
  const noticed = listItems("noticed").size, words = listItems("words").size;
  inner.innerHTML = `<div class="ep-head">SMALL HOURS</div>` + cards.map(c => c.head
    ? `<div class="ep-card"><div class="ep-head" style="font-size:12px;margin:10px 0 6px">${c.head}</div><div class="ep-text">${c.text}</div></div>`
    : `<div class="ep-card"><img src="art/portraits/${c.id === "moth" ? "moth_happy" : c.id + "_smile"}.png"><div class="ep-name">${c.name}</div><div class="ep-text">${c.text}</div></div>`).join("") +
    `<div class="ep-card"><div class="ep-small">You noticed ${noticed} of ${Object.keys(NOTICED).length} things on Halfmoon Street.<br>You gathered ${words} of ${Object.keys(WORDS).length} words for the Morning.<br>${noticed < Object.keys(NOTICED).length ? "There's more to find, another night." : "You noticed everything. Lu would say: show-off."}</div></div>
    <div class="ep-card"><div class="ep-head" style="font-size:12px">THANK YOU FOR STAYING UP</div>
    <div class="ep-small">Written, drawn, scored and built by Claude, for a human who asked for something really, really human.<br><br>Music & sound generated locally with ACE-Step 1.5 and Stable Audio 3 via ComfyUI.<br>Story engine: ink by inkle. Fonts: Pixelify Sans, Atkinson Hyperlegible.</div></div>
    <div class="ep-card" style="margin-top:60px"><button id="ep-done" style="font-family:Pixelify;font-size:10px;padding:5px 16px;background:rgba(13,11,26,.8);border:1px solid #ffb347;color:#ffb347;cursor:pointer">Good morning</button></div>`;
  $("#epilogue").classList.remove("hidden");
  await fadeIn();
  // scroll
  let y = 360;
  const h = inner.scrollHeight;
  let fast = false;
  $("#epilogue").onclick = () => (fast = !fast);
  const tick = () => {
    if ($("#epilogue").classList.contains("hidden")) return;
    y -= fast ? 1.6 : 0.32;
    const minY = 360 - h - 20 + 120;
    if (y < minY) y = minY;
    inner.style.top = `${y}px`;
    requestAnimationFrame(tick);
  };
  tick();
  inner.querySelector("#ep-done").addEventListener("click", async e => {
    e.stopPropagation();
    await fadeOut();
    $("#epilogue").classList.add("hidden");
    await showTitle();
    await fadeIn();
  });
}

// ---------------------------------------------------------------- loop
let last = performance.now();
function loop(now) {
  const dt = Math.min(0.05, (now - last) / 1000);
  last = now;
  view.tick(dt);
  view.draw();
  if (story && !$("#hud").classList.contains("hidden")) updateCountdown();
  requestAnimationFrame(loop);
}

// debug hooks for automated playtesting
view.debug = location.search.includes("debug");
window.__sh = { view, get story() { return story; }, v, runKnot, setScene, get busy() { return busy; }, get scene() { return sceneId; }, advance, listItems, layout: () => layout };

boot();
