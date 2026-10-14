// Scripted end-to-end playthrough in headless Chromium with an auto-advancer.
import { chromium } from "playwright-core";
const out = process.argv[2];
const browser = await chromium.launch({ executablePath: "/usr/bin/chromium", args: ["--autoplay-policy=no-user-gesture-required"] });
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
const errors = [];
page.on("pageerror", e => errors.push("pageerror: " + e.message));
page.on("console", m => { if (m.type() === "error") errors.push(m.text()); });
page.on("response", r => { if (r.status() >= 400) errors.push(`${r.status()} ${r.url()}`); });
await page.goto("http://127.0.0.1:8765/index.html");
await page.waitForSelector("#click-to-start:not(.hidden)");
await page.click("#click-to-start");
await page.click("#btn-new"); await page.fill("#name-input", "Rin"); await page.click("#name-ok");
// auto-advance: always pick the LAST choice unless told otherwise via window.__pick
await page.evaluate(() => {
  window.__pick = null;
  setInterval(() => {
    const btns = document.querySelectorAll("#choices button");
    if (btns.length) {
      let i = btns.length - 1;
      if (window.__pick) { const j = [...btns].findIndex(b => b.textContent.includes(window.__pick)); if (j >= 0) i = j; else i = 0; }
      else i = 0;
      btns[i].click();
    } else if (!document.querySelector("#dialogue").classList.contains("hidden")) __sh.advance();
  }, 30);
});
const idle = () => page.waitForFunction(() => !__sh.busy, null, { timeout: 120000, polling: 100 });
const knot = async (k, pick = null) => { await idle(); await page.evaluate(([k, p]) => { window.__pick = p; return __sh.runKnot(k); }, [k, pick]); await idle(); };
const go = async sc => { await idle(); await page.evaluate(sc => __sh.setScene(sc), sc); };
const shot = async n => { await page.waitForTimeout(300); await page.screenshot({ path: `${out}/p_${n}.png` }); };
await page.waitForFunction(() => __sh.story && __sh.v.act >= 1 && !__sh.busy, null, { timeout: 120000, polling: 200 });
await shot("01_after_prologue");
// Act 1
await go("street"); await knot("street_car"); await knot("street_cat"); await knot("street_kiosk");
await go("teo_room"); await knot("talk_teo"); await knot("teo_room_monitors");
await go("clinic"); await knot("talk_nkechi"); await knot("clinic_baby_photos");
await go("hotline"); await knot("talk_hollis");
await shot("02_hotline");
await go("shop"); await knot("enter_shop");
await shot("03_midnight");
const act = await page.evaluate(() => __sh.v.act); console.log("act after midnight", act);
// Act 2
await go("stairs"); await knot("talk_imogen"); await knot("stairs_lamp");
await go("roofs"); await knot("talk_mae"); await knot("talk_june"); await knot("roofs_seed_library");
await go("alley"); await knot("talk_rafe"); await knot("alley_crates");
await go("clinic"); await knot("talk_nkechi");
console.log("act after act2", await page.evaluate(() => __sh.v.act));
await shot("04_3am");
// Act 3
await go("roofs"); await knot("talk_june");
await go("teo_room"); await knot("talk_teo", "Tell him what June");
await go("shop"); await knot("talk_lu"); await knot("talk_lu", "lantern");
await go("roofs"); await knot("talk_mae");
await go("street"); await knot("street_car", "Get in");
await go("alley"); await knot("talk_rafe", "why the drones");
await go("stairs"); await knot("talk_imogen", "roof");
await go("hotline"); await knot("talk_hollis", "watch the phones"); await knot("talk_hollis", "Morning");
await go("clinic"); await knot("talk_dev"); await knot("talk_nkechi");
console.log("words", await page.evaluate(() => [...__sh.listItems("words")].join(",")));
await shot("05_before_finale");
await go("roofs");
await page.evaluate(() => { window.__pick = "Begin the Morning"; __sh.runKnot("talk_mae"); });
await page.waitForTimeout(1500);
await page.evaluate(() => { window.__pick = "Yes"; });
await page.waitForTimeout(4000);
await page.evaluate(() => { window.__pick = null; });
await shot("06_finale");
await page.waitForFunction(() => !document.querySelector("#epilogue").classList.contains("hidden"), null, { timeout: 180000 });
await shot("07_epilogue");
await page.waitForTimeout(15000);
await shot("08_epilogue_scroll");
console.log(errors.join("\n") || "no errors");
await browser.close();
