import { chromium } from "playwright"; import { pathToFileURL } from "node:url"; import path from "node:path";
const [f, idx] = process.argv.slice(2);
const nav = await chromium.launch(); const ctx = await nav.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage(); await p.goto(pathToFileURL(path.resolve(f)).href); await p.waitForTimeout(400);
await p.locator(".seance-tab").nth(+idx).click(); await p.waitForTimeout(200);
const r = await p.evaluate(() => {
  const pan = [...document.querySelectorAll(".seance-panel")].find((e) => e.offsetParent !== null);
  const out = []; let cur = null;
  const walk = (el) => { for (const c of el.children) {
    if (c.offsetParent === null && getComputedStyle(c).position !== "fixed") continue;
    if (/^H[1-5]$/.test(c.tagName)) { cur = { t: c.tagName + " " + c.innerText.trim().slice(0, 90), mots: 0 }; out.push(cur); continue; }
    if (c.querySelector("h1,h2,h3,h4,h5")) { walk(c); continue; }
    const n = (c.innerText || "").split(/\s+/).filter(Boolean).length; if (cur) cur.mots += n; else out.push({ t: "(avant) " + c.tagName, mots: n });
  } };
  walk(pan); return out;
});
for (const x of r) console.log(String(x.mots).padStart(5), x.t);
await nav.close();
