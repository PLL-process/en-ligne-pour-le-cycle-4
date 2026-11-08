#!/usr/bin/env node
/**
 * mesurer_charge.mjs — combien l'élève a-t-il à lire, à l'ouverture de chaque séance ? (08/11/2026)
 *
 * Pascal, le 08/11/2026 : « une révision des 3 thèmes s'impose… depuis longtemps cela me paraissait une charge
 * cognitive ». Les contrôles disent si une page suit les règles ; aucun ne disait combien elle donne à lire. Cet outil
 * ouvre chaque séquence dans Chromium (390 px, la largeur d'un téléphone), clique chaque onglet de séance et compte ce
 * que l'élève VOIT sans rien déplier :
 *   mots     les mots visibles du panneau de la séance (un <details> fermé, un panneau caché ne comptent pas) ;
 *   essentiel les mêmes, mode essentiel allumé (n°29), quand la page l'offre ;
 *   ecrans   la hauteur du panneau en écrans de téléphone (844 px) ;
 *   champs   ce que l'élève doit remplir ou choisir (zones de texte, groupes de boutons, listes, cases) ;
 *   minutes  le temps de lecture seule, à 120 mots par minute (un lecteur de collège qui lit sans aisance).
 * Une séance dure 55 min (décision du 24-25/10/2026) : une séance dont la lecture seule dépasse 10 minutes
 * (1 200 mots visibles) laisse trop peu de temps pour faire. C'est un repère, pas une règle : la sortie vaut 0.
 *
 * Usage :
 *   node _outils/mesurer_charge.mjs                 # toutes les séquences, une ligne par séance
 *   node _outils/mesurer_charge.mjs <page.html>…    # quelques pages
 *   node _outils/mesurer_charge.mjs --json <f>      # écrit aussi les mesures en JSON
 *   node _outils/mesurer_charge.mjs --longs 30 <p>  # cite aussi, séance par séance, chaque bloc visible de plus de
 *                                                   # 30 mots d'un seul tenant (hors corrections repliées) : les
 *                                                   # consignes et annonces à passer en lignes (skill revision-sequence)
 * Sortie 2 si aucune page n'a pu être lue (n°299).
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { chromium } from "playwright";

const DEPOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const SEUIL = 1200, VITESSE = 120;
const argv = process.argv.slice(2);
const iJson = argv.indexOf("--json");
const sortieJson = iJson >= 0 ? argv[iJson + 1] : null;
const iLongs = argv.indexOf("--longs");
const seuilLongs = iLongs >= 0 ? +argv[iLongs + 1] : 0;
const cibles = argv.filter((a, i) => !a.startsWith("--") && !(iJson >= 0 && i === iJson + 1) && !(iLongs >= 0 && i === iLongs + 1));

function toutes() {
  const out = [];
  (function marcher(d) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      if (["node_modules", ".git"].includes(e.name) || e.name.startsWith("_archive")) continue;
      const p = path.join(d, e.name);
      if (e.isDirectory()) marcher(p);
      else if (/^sequence.*\.html$/.test(e.name) && !/station_[1-4]_/.test(e.name) && /[\\/]theme-/.test(p)) out.push(p);
    }
  })(DEPOT);
  return out.sort();
}
const pages = cibles.length ? cibles.map((c) => path.resolve(DEPOT, c)) : toutes();

const nav = await chromium.launch();
const res = [];
for (const f of pages) {
  const ctx = await nav.newContext({ viewport: { width: 390, height: 844 }, hasTouch: true });
  await ctx.route("**/*", (r) => (/^(file|data|blob):/.test(r.request().url()) ? r.continue() : r.abort()));
  const p = await ctx.newPage();
  try { await p.goto(pathToFileURL(f).href, { timeout: 30000 }); await p.waitForTimeout(400); }
  catch (e) { await ctx.close(); continue; }
  const mesure = () => p.evaluate((seuilLongs) => {
    // le panneau AFFICHÉ (un panneau caché par CSS rendrait tout son texte par innerText : il faut le visible)
    const panneau = [...document.querySelectorAll(".seance-panel, [role=tabpanel]")].find((e) => e.offsetParent !== null)
      || document.querySelector("main") || document.body;
    const t = (panneau.innerText || "").replace(/\s+/g, " ").trim();
    const champs = panneau.querySelectorAll("textarea, fieldset.qcm-groupe, select, input[type=checkbox], input[type=text], input[type=number]");
    const visibles = [...champs].filter((c) => c.offsetParent !== null).length;
    // les blocs d'un seul tenant (un paragraphe, un item, une cellule, coupés à leurs retours à la ligne)
    const longs = [];
    if (seuilLongs) {
      for (const el of panneau.querySelectorAll("p, li, dd, td, figcaption, label")) {
        if (el.offsetParent === null || el.querySelector("p, li, div")) continue;
        for (const l of el.innerText.split(/\n+/).map((x) => x.trim()).filter(Boolean)) {
          const n = l.split(/\s+/).length;
          if (n > seuilLongs && !longs.some((x) => x.texte === l)) longs.push({ mots: n, texte: l });
        }
      }
    }
    return { mots: t ? t.split(" ").length : 0, hauteur: panneau.getBoundingClientRect().height, champs: visibles, longs };
  }, seuilLongs);
  const sel = (await p.locator(".seance-tab").count()) ? ".seance-tab" : "[role=tab]";
  const onglets = await p.locator(sel).count();
  const seances = [];
  const n = Math.max(onglets, 1);
  for (let i = 0; i < n; i++) {
    if (onglets) { await p.locator(sel).nth(i).click(); await p.waitForTimeout(150); }
    const m = await mesure();
    let ess = null;
    const bouton = p.locator("#btnEssentiel");
    if (await bouton.count()) {
      await bouton.click(); await p.waitForTimeout(100);
      ess = (await mesure()).mots;
      await bouton.click(); await p.waitForTimeout(100);
    }
    seances.push({ seance: i + 1, mots: m.mots, essentiel: ess, ecrans: +(m.hauteur / 844).toFixed(1), champs: m.champs,
                   minutes: Math.round(m.mots / VITESSE), longs: m.longs });
  }
  await ctx.close();
  res.push({ page: path.relative(DEPOT, f), seances });
}
await nav.close();
if (!res.length) { console.log("✘ aucune page lue : rien n'a été mesuré"); process.exit(2); }
let lourdes = 0, total = 0;
for (const r of res) {
  console.log("── " + r.page);
  for (const s of r.seances) {
    total++;
    const trop = s.mots > SEUIL;
    lourdes += trop;
    console.log(`   ${trop ? "⚠" : "·"} séance ${s.seance} : ${s.mots} mots visibles (${s.minutes} min de lecture)` +
                (s.essentiel != null ? ` · essentiel ${s.essentiel}` : "") + ` · ${s.ecrans} écrans · ${s.champs} champs`);
    for (const l of s.longs || []) console.log(`        ${l.mots} mots d'un seul tenant · « ${l.texte.slice(0, 110)}… »`);
  }
}
console.log(`${res.length} page(s) lues · ${total} séance(s) · ${lourdes} au-delà de ${SEUIL} mots visibles (plus de ${SEUIL / VITESSE} min de lecture seule)`);
if (sortieJson) fs.writeFileSync(sortieJson, JSON.stringify(res, null, 1));
