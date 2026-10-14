// Compile game/story/*.ink (in manifest order) to game/story/story.json.
//   bun tools/build_ink.mjs
import { Compiler } from "inkjs/full";
import fs from "fs";
import path from "path";

const dir = path.join(import.meta.dir, "..", "game", "story");
const order = fs.readFileSync(path.join(dir, "manifest.txt"), "utf8").split("\n").map(s => s.trim()).filter(Boolean);
const src = order.map(f => `// ==== ${f} ====\n` + fs.readFileSync(path.join(dir, f), "utf8")).join("\n\n");
const errors = [], warnings = [];
const compiler = new Compiler(src, {
  errorHandler: (msg, type) => (type === 2 ? errors : warnings).push(msg),
});
let story;
try { story = compiler.Compile(); } catch (e) { errors.push(String(e)); }
// map concatenated line numbers back to files
const starts = []; let line = 1;
for (const f of order) { starts.push([line, f]); line += fs.readFileSync(path.join(dir, f), "utf8").split("\n").length + 2; }
const where = msg => msg.replace(/line (\d+)/, (m, n) => {
  n = +n; let cur = starts[0];
  for (const s of starts) if (s[0] <= n) cur = s;
  return `${cur[1]}:${n - cur[0]}`;
});
warnings.forEach(w => console.log("WARN", where(w), "<<", w));
errors.forEach(e => console.log("ERROR", where(e), "<<", e));
if (errors.length || !story) process.exit(1);
fs.writeFileSync(path.join(dir, "story.json"), story.ToJson());
console.log(`ok: ${order.length} files, ${src.split(/\s+/).length} words -> story.json`);
