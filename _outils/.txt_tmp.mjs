import { chromium } from "playwright"; import { pathToFileURL } from "node:url"; import path from "node:path";
const [f, idx, sel] = process.argv.slice(2);
const nav = await chromium.launch(); const ctx = await nav.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage(); await p.goto(pathToFileURL(path.resolve(f)).href); await p.waitForTimeout(400);
await p.locator(".seance-tab").nth(+idx).click(); await p.waitForTimeout(200);
console.log(await p.locator(sel).first().innerText());
await nav.close();
