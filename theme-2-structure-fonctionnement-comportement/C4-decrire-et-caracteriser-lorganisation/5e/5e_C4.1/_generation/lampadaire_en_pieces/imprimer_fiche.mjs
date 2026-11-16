// La fiche A4 du lampadaire, en trois gestes, hors du dépôt puis versée dans le lot :
//   1. `scripts/print.mjs` du kit capture la figure claire (fermée, ouverte, les étapes) et écrit la fiche HTML ;
//   2. ses mots fixés en anglais passent en français (« Parts » → « Les pièces »…) et la licence se dit ;
//   3. Chromium (Playwright) l'imprime en PDF A4, une page, copiée dans ../../lampadaire_fiche_A4.pdf.
// D'abord : node build.mjs --light. Puis : node imprimer_fiche.mjs
import { execFileSync } from "node:child_process";
import { copyFileSync, readFileSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright";

const ICI = dirname(fileURLToPath(import.meta.url));
const KIT = process.env.ANATOMY_DIR || join(homedir(), ".cache", "anatomy-1482e84");
const TRAVAIL = process.env.ANATOMY_TRAVAIL || join(homedir(), ".cache", "anatomy-travail");
const html = join(TRAVAIL, "lampadaire_fiche-drawing-a4.html");

try {
  execFileSync("node", [join(KIT, "scripts", "print.mjs"), join(TRAVAIL, "fiche.mjs"), "--format", "drawing"], {
    stdio: "inherit", env: { ...process.env, CHROME_PATH: process.env.CHROME_PATH || chromium.executablePath() },
  });
} catch (e) {
  // le PDF de print.mjs peut manquer (Chrome en ligne de commande) : la fiche HTML suffit, Playwright imprime
  console.warn("print.mjs n'a pas écrit son PDF ; la fiche HTML est reprise ici.");
}

let t = readFileSync(html, "utf8");
for (const [a, b] of [
  ['lang="en"', 'lang="fr"'], [">Drawing<b>", ">Dessin<b>"], [">Parts<", ">Les pièces<"], [">Specification<", ">Caractéristiques<"],
  [">Not to scale<", ">Pas à l'échelle<"], ["<span>Anatomy</span>", "<span>Kit Anatomy © 2026 Ryan, licence MIT · fiche CC BY-NC-SA 4.0, Pascal Gouacide</span>"],
]) t = t.split(a).join(b);
writeFileSync(html, t);

const b = await chromium.launch();
const p = await (await b.newContext({ viewport: { width: 794, height: 1123 } })).newPage();
await p.goto("file://" + html);
await p.waitForTimeout(500);
await p.emulateMedia({ media: "print" });
const pdf = join(TRAVAIL, "lampadaire_fiche_A4.pdf");
await p.pdf({ path: pdf, format: "A4", printBackground: true, preferCSSPageSize: true });
await b.close();
copyFileSync(pdf, join(ICI, "..", "..", "lampadaire_fiche_A4.pdf"));
console.log("écrit ../../lampadaire_fiche_A4.pdf");
