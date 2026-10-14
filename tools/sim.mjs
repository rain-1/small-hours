// Random-walk bot over the compiled story: finds runtime errors, unknown speakers,
// stray markup, and measures how much content is reachable.
//   bun tools/sim.mjs [runs]
import { Story } from "inkjs";
import fs from "fs";
const json = fs.readFileSync(new URL("../game/story/story.json", import.meta.url), "utf8");
const SPEAKERS = new Set("lu teo ozzie june mae imogen nkechi hollis rafe dev moth you chorus radio phone sign tv cat pia iris".split(" "));
const knotsSrc = fs.readdirSync(new URL("../game/story/", import.meta.url)).filter(f => f.endsWith(".ink"))
  .map(f => fs.readFileSync(new URL(`../game/story/${f}`, import.meta.url), "utf8")).join("\n");
const knots = [...knotsSrc.matchAll(/^=== (\w+) ===/gm)].map(m => m[1])
  .filter(k => !/^(start|done|finale|finale_confirm|beat_midnight|beat_3am|ozzie_drive|dev_calm_scene|june_noodle_lesson|talk_ozzie_shop|kindness|notice)$/.test(k) && !k.startsWith("enter_"));
const runs = +(process.argv[2] || 200);
const issues = new Map();
const note = (k, m) => issues.set(k, (issues.get(k) || m));
let finals = [], allLines = new Set();
function lists(s, n) { const out = []; for (const [k] of s.variablesState.$(n)) out.push(JSON.parse(k).itemName); return out; }
for (let r = 0; r < runs; r++) {
  const s = new Story(json);
  s.onError = (m, t) => note("ink " + m, m);
  s.variablesState.$("name", "Kit");
  const play = (knot, beg) => {
    s.ChoosePathString(knot);
    for (let guard = 0; guard < 400; guard++) {
      while (s.canContinue) {
        const line = s.Continue().trim();
        for (const t of s.currentTags) if (t.startsWith("end")) return "end";
        if (!line) continue;
        allLines.add(line);
        const m = line.match(/^@(\w+)/);
        if (m && !SPEAKERS.has(m[1])) note("speaker " + m[1], line);
        if (/[{}]|->|~ /.test(line)) note("markup: " + line.slice(0, 80), line);
        for (const t of s.currentTags) if (t.startsWith("end")) return "end";
      }
      if (!s.currentChoices.length) return;
      let cs = s.currentChoices;
      let idx = Math.floor(Math.random() * cs.length);
      const begin = cs.findIndex(c => /Begin the Morning/.test(c.text));
      if (begin >= 0 && !beg) idx = cs.findIndex(c => !/Begin the Morning/.test(c.text));
      if (begin >= 0 && beg) idx = begin;
      const yes = cs.findIndex(c => /Yes\. Let's do it/.test(c.text));
      if (yes >= 0) idx = beg ? yes : cs.length - 1;
      s.ChooseChoiceIndex(Math.max(0, idx));
    }
    note("loop guard " + knot, knot);
  };
  play("start");
  for (let i = 0; i < 1500; i++) {
    const act = s.variablesState.$("act");
    const k = knots[Math.floor(Math.random() * knots.length)];
    // simulate entering shop occasionally (triggers beats)
    if (Math.random() < 0.08) play("enter_shop");
    play(k, false);
  }
  const act = s.variablesState.$("act");
  let res;
  if (act === 3) { s.variablesState.$("here", "roofs"); res = play("talk_mae.mae_act3", true); if (res !== "end") res = play("finale_confirm", true); }
  finals.push({ act, words: lists(s, "words").length, noticed: lists(s, "noticed").length, end: res === "end", tone: s.variablesState.$("reply_tone"), time: s.variablesState.$("time") });
}
const avg = k => (finals.reduce((a, f) => a + f[k], 0) / finals.length).toFixed(1);
console.log(`runs ${runs}: reached act3 ${finals.filter(f => f.act >= 3).length}, ended ${finals.filter(f => f.end).length}, avg words ${avg("words")}, max words ${Math.max(...finals.map(f => f.words))}, avg noticed ${avg("noticed")}, max noticed ${Math.max(...finals.map(f => f.noticed))}`);
console.log("tones:", JSON.stringify(finals.reduce((a, f) => ((a[f.tone] = (a[f.tone] || 0) + 1), a), {})));
console.log(`distinct lines seen: ${allLines.size}`);
for (const [k, m] of issues) console.log("ISSUE", k);
