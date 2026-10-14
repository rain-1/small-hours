// Headless smoke test: load the game, start a new night, screenshot.
//   bun tools/shot.mjs <outdir> [steps...]
import { chromium } from "playwright-core";
const out = process.argv[2] || "/tmp/shots";
const browser = await chromium.launch({ executablePath: "/usr/bin/chromium", args: ["--autoplay-policy=no-user-gesture-required"] });
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
const errors = [];
page.on("console", m => { if (m.type() === "error" || m.type() === "warning") errors.push(m.type() + ": " + m.text()); });
page.on("pageerror", e => errors.push("pageerror: " + e.message));
await page.goto("http://127.0.0.1:8765/index.html");
await page.waitForSelector("#click-to-start:not(.hidden)", { timeout: 15000 });
await page.click("#click-to-start");
await page.waitForTimeout(800);
await page.screenshot({ path: `${out}/01_title.png` });
await page.click("#btn-new");
await page.waitForTimeout(300);
await page.screenshot({ path: `${out}/02_name.png` });
await page.click("#name-ok");
await page.waitForTimeout(1500);
await page.screenshot({ path: `${out}/03_start.png` });
// advance a few lines
for (let i = 0; i < 6; i++) { await page.keyboard.press("Space"); await page.waitForTimeout(150); await page.keyboard.press("Space"); await page.waitForTimeout(250); }
await page.screenshot({ path: `${out}/04_dialogue.png` });
console.log(errors.join("\n") || "no console errors");
await browser.close();
