// Screenshot every scene (with ?debug hotspot overlay) at a chosen game state.
import { chromium } from "playwright-core";
const out = process.argv[2], dbg = process.argv[3] !== "nodebug";
const browser = await chromium.launch({ executablePath: "/usr/bin/chromium" });
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
const errors = [];
page.on("pageerror", e => errors.push("pageerror: " + e.message));
page.on("console", m => { if (m.type() === "error") errors.push(m.text()); });
await page.goto(`http://127.0.0.1:8765/index.html${dbg ? "?debug" : ""}`);
await page.waitForSelector("#click-to-start:not(.hidden)");
await page.click("#click-to-start");
await page.click("#btn-new"); await page.click("#name-ok");
await page.waitForTimeout(1200);
await page.evaluate(() => { const s = __sh.story; s.variablesState.$("act", 4); s.variablesState.$("teo_told", true); s.variablesState.$("hollis_open", true); s.variablesState.$("imogen_choice",""); });
for (const sc of ["shop","street","teo_room","stairs","roofs","roofs_dawn","clinic","hotline","alley","hill_road"]) {
  await page.evaluate(async sc => { document.querySelector("#dialogue").classList.add("hidden"); await __sh.setScene(sc); }, sc);
  await page.waitForTimeout(500);
  await page.screenshot({ path: `${out}/scene_${sc}.png` });
}
console.log(errors.join("\n") || "no errors");
await browser.close();
