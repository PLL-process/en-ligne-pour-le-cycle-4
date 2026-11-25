/* controle_page_ouverte.mjs — un contrôle regarde la page ouverte (règle d'or n°361, clé de voûte).
 *
 * LE CONSTAT
 * ----------
 * L'audit en 12 axes du TP « Algorigrammes de domotique » (4e_C6.2, 20/11/2026) a trouvé, dans une page que tous les
 * contrôles disaient verte :
 *   · un bloc « si / alors / sinon » DESSINÉ (contraire à la n°308), que `controle_blocs_dessines.py` ne voyait pas :
 *     le dessin n'existait pas dans le HTML, un script le fabriquait au moment d'ouvrir la correction ;
 *   · la même phrase (« les couleurs ne sont ici qu'une aide visuelle… ») qui fermait les huit corrections, sans rien
 *     expliquer (n°96) — invisible tant qu'aucune correction n'est ouverte ;
 *   · un défaut de contraste dans la légende du code coloré, qui n'apparaît qu'une fois la correction affichée ;
 *   · un algorithme qui défilait à 390 px et cachait « 50 lux », la valeur du seuil.
 * `controle_axe.mjs`, `controle_contraste_liens.mjs` et les contrôles Python lisent la page telle qu'elle se charge, ou
 * son texte source. Ce que l'élève découvre APRÈS un geste (corrections, aides, bilan, onglets suivants, ce qu'un
 * script dessine) leur échappe. La n°49 dit « on teste ce qui est rendu » : il faut aussi tester ce qui est rendu après.
 *
 * LA RÈGLE (clé de voûte)
 * -----------------------
 * Un contrôle regarde la page ouverte, comme l'élève finit par la voir : détails dépliés, corrections et aides
 * affichées, onglets visibles, dessins fabriqués par script compris. Une page qui fabrique ses corrections par script
 * expose `window.__toutOuvrir()` (pilote : le TP 4e_C6.2), que les contrôles appellent avant de mesurer.
 *
 * CE QU'IL MESURE, page ouverte, à 390 px
 * ---------------------------------------
 *   L  un listing qui défile en largeur : ce qui défile est caché (n°364) — `pre`, `.programme`, `.code-box`, et tout
 *      bloc en police à chasse fixe qui garde ses lignes (`div.codebox`, `div.py`, `.terminal`…, depuis le 22/11/2026) ;
 *      (le calque coloré d'un éditeur intégré, posé sur sa zone de saisie, défile avec elle : il n'est pas compté) ;
 *   B  un SVG qui dessine un bloc de programmation (« alors » et « sinon », « répéter… », « quand … cliqué ») : n°308 ;
 *   C  une même phrase (8 mots ou plus) dans 3 corrections ou plus : une correction qui se recopie n'explique pas (n°96) ;
 *      (une ligne d'aide répétée exprès — « 🔍 Touche le schéma pour l'agrandir » — porte `data-repete` et n'est pas lue ;
 *      un intitulé non plus : titre, ou paragraphe tout en gras comme « Question par question — la réponse, et pourquoi
 *      pas les autres », que 4e_C4.7 et 5e_C4.7 posent en tête de chaque correction, 22/11/2026) ;
 *   A  avec --axe : les défauts graves (critical, serious) d'axe-core sur la page ouverte, à 390 px — mêmes règles WCAG
 *      que `controle_axe.mjs` (2.0, 2.1, 2.2 ; A et AA ; `wcag21a` manquait avant le 25/11/2026 : il porte
 *      `label-content-name-mismatch`).
 *
 * Usage :
 *   node _outils/controle_page_ouverte.mjs [chemins…] [--axe] [--strict] [--muet] [--json f]
 *   Sans chemin : les trois thèmes et l'index, hors synthèses professeur, fiches et rapports.
 * L, B ET A REFUSENT (règle n°273 : référence nommée, datée, vide)
 * ----------------------------------------------------------------
 * Le 22/11/2026, sur les 341 pages, L et B sont à 0 (vague n°364 : PR #854, #856, #862). Une page qui fait défiler un
 * listing ou qui dessine un bloc fait sortir à 1, même sans --strict.
 * Le 25/11/2026, avec --axe, A est à 0 sur les 341 pages (zones qui défilent sans clavier : PR #893, #894, #895 ;
 * contraste, étiquettes, attributs, liste : PR #903, #905, #908 ; 64 pages en défaut grave le 22/11 au matin). Un
 * défaut grave d'axe-core, page ouverte à 390 px, fait sortir à 1 lui aussi. `controle_axe.mjs` reste le contrôle de
 * la page à son chargement, à 1 280 px, contre sa référence chiffrée ; celui-ci voit ce qui ne s'affiche qu'au clic
 * (corrections, aides, onglets) et sur un téléphone.
 * C reste une mesure (une phrase répétée peut l'être à bon droit) ; --strict la fait refuser aussi.
 *
 * Sortie : 0 aucun L, B ni A (C mesuré) · 1 au moins un L, un B ou, avec --axe, un A ; ou, avec --strict, au moins un
 *          écart · 2 EN PANNE : Playwright absent, axe-core introuvable avec --axe, aucune page mesurée, ou une page qui
 *          ne s'ouvre pas (n°299).
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const RACINE = path.resolve(ICI, '..');
const IGNORES = new Set(['.git', 'node_modules', '_archive-anciennes-versions', '_outils', '_exports', '_generation', 'captures']);
const PROFESSEUR = /^(synthese_professeur|fiche_|rapport_tests)/i;
const EN_PARALLELE = 4;

const args = process.argv.slice(2);
const AXE = args.includes('--axe'), STRICT = args.includes('--strict'), MUET = args.includes('--muet');
const iJson = args.indexOf('--json'); const JSON_OUT = iJson >= 0 ? args[iJson + 1] : null;
const chemins = args.filter((a, i) => !a.startsWith('--') && args[i - 1] !== '--json');

function pages(depart) {
  if (!fs.statSync(depart).isDirectory()) return [path.resolve(depart)];
  const out = [];
  (function marcher(d) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const c = path.join(d, e.name);
      if (e.isDirectory()) { if (!e.name.startsWith('.') && !IGNORES.has(e.name)) marcher(c); }
      else if (e.name.toLowerCase().endsWith('.html') && !PROFESSEUR.test(e.name)) out.push(c);
    }
  })(depart);
  return out;
}

let liste = [];
if (chemins.length) chemins.forEach(c => liste.push(...pages(path.resolve(c))));
else {
  for (const d of fs.readdirSync(RACINE)) if (d.startsWith('theme-')) liste.push(...pages(path.join(RACINE, d)));
  liste.push(path.join(RACINE, 'index.html'));
}
liste = [...new Set(liste)].sort((a, b) => a.localeCompare(b, 'fr'));

let chromium;
try { ({ chromium } = await import('playwright')); }
catch { console.error('⛔ EN PANNE : Playwright introuvable (n°299).'); process.exit(2); }

let axeSource = null;
if (AXE) {
  try { const { trouverAxe } = await import('./controle_axe.mjs'); const p = trouverAxe(); if (p) axeSource = fs.readFileSync(p, 'utf8'); } catch { /* signalé ci-dessous */ }
  if (!axeSource) { console.error('⛔ EN PANNE : --axe demandé, axe-core introuvable (AXE_CORE=/chemin/vers/axe.min.js).'); process.exit(2); }
}

/* Ouvre tout ce qui s'ouvre, dans la page. */
function ouvrir() {
  try { if (typeof window.__toutOuvrir === 'function') window.__toutOuvrir(); } catch (e) { /* la mesure continue */ }
  const RE = /corr|corrig|solution|aide|indice|reponse|réponse/i;
  document.querySelectorAll('details').forEach(d => { d.open = true; });
  document.querySelectorAll('[hidden]').forEach(el => {
    const cl = typeof el.className === 'string' ? el.className : (el.className && el.className.baseVal) || '';
    const sig = `${el.id} ${cl} ${Object.keys(el.dataset || {}).join(' ')} ${el.getAttribute('role') || ''}`;
    if (RE.test(sig) || el.getAttribute('role') === 'tabpanel') el.hidden = false;
  });
}

/* Mesure L, B, C dans la page ouverte. */
function mesurer() {
  const vis = el => el.getClientRects().length > 0;
  // un calque coloré d'éditeur (caché aux lecteurs d'écran, posé sur une zone de saisie) défile AVEC la saisie : ce n'est
  // pas un listing à lire, il ne compte pas (21/11/2026 : `pre.cl-hl` de 3e_C6.1, `pre.editeur-py-couleurs` de 4e_C6.2)
  const calque = el => el.getAttribute('aria-hidden') === 'true' || !!(el.parentElement && el.parentElement.querySelector(':scope > textarea'));
  // un listing, c'est `pre`, `.programme`, `.code-box`… et tout bloc en police à chasse fixe qui garde ses lignes
  // (`white-space: pre` ou `nowrap`) : `div.codebox`, `div.py`, `div.prog`, `.terminal` (22/11/2026 : neuf listings de
  // ce genre défilaient sans que L les voie, trouvés par axe-core, « scrollable-region-focusable »)
  const mono = el => /mono|courier|consolas|menlo/i.test(getComputedStyle(el).fontFamily);
  const candidats = new Set(document.querySelectorAll('pre, .programme, .code-box'));
  document.querySelectorAll('body div, body p, body td, body li').forEach(el => {
    if (/^(pre|nowrap)$/.test(getComputedStyle(el).whiteSpace) && mono(el)) candidats.add(el);
  });
  const defilants = [...candidats].filter(vis).filter(el => !calque(el) && !el.closest('svg'))
    .filter(el => el.scrollWidth > el.clientWidth + 2);
  const L = defilants.filter(el => !defilants.some(o => o !== el && o.contains(el)))   // le plus extérieur seulement
    .map(el => ({ debut: el.textContent.trim().replace(/\s+/g, ' ').slice(0, 50), px: el.scrollWidth - el.clientWidth }));
  const B = [];
  document.querySelectorAll('svg').forEach(svg => {
    const t = [...svg.querySelectorAll('text')].map(x => x.textContent.trim().toLowerCase());
    if ((t.some(s => /^alors\b/.test(s)) && t.some(s => /^sinon\b/.test(s))) || t.some(s => /^r[ée]p[ée]ter\b/.test(s)) || t.some(s => /^quand .*cliqu/.test(s)))
      B.push(t.slice(0, 6).join(' · ').slice(0, 80));
  });
  const SEL = '[id*="corr" i], [id*="correction" i], [class*="correction" i], [class*="corrige" i], details';
  let boites = [...document.querySelectorAll(SEL)].filter(el => {
    if (el.tagName !== 'DETAILS') return true;
    const s = el.querySelector(':scope > summary'); return s && /correction|corrig|solution/i.test(s.textContent);
  });
  boites = boites.filter(b => !boites.some(o => o !== b && b.contains(o)));  // les plus intérieures seulement
  const compte = new Map();
  boites.forEach(b => {
    const vues = new Set();
    // le texte de la correction, sans son intitulé (« 📖 Correction complète… » se répète à bon droit), ni styles ni scripts
    const c = b.cloneNode(true);
    c.querySelectorAll(':scope > summary, style, script, [data-repete], h1, h2, h3, h4, h5, h6').forEach(x => x.remove());
    // un intitulé tout en gras (« <p><b>Question par question…</b></p> ») se répète à bon droit, comme un titre
    c.querySelectorAll('p').forEach(x => {
      const kids = [...x.childNodes].filter(k => !(k.nodeType === 3 && !k.textContent.trim()));
      if (kids.length === 1 && kids[0].nodeType === 1 && /^(B|STRONG)$/.test(kids[0].tagName)) x.remove();
    });
    c.querySelectorAll('p, li, div, h1, h2, h3, h4, h5, h6, tr, br, pre, svg').forEach(x => x.after('\n'));  // un bloc = une coupure
    (c.textContent || '').split(/(?<=[.!?…])\s+|\n+/).forEach(ph => {
      const n = ph.toLowerCase().replace(/[«»"“”’']/g, ' ').replace(/\s+/g, ' ').trim();
      if (n.split(' ').length >= 8 && !vues.has(n)) { vues.add(n); compte.set(n, (compte.get(n) || 0) + 1); }
    });
  });
  const C = [...compte].filter(([, k]) => k >= 3).map(([ph, k]) => ({ phrase: ph.slice(0, 90), fois: k }));
  return { L, B, C, boites: boites.length };
}

const b = await chromium.launch();
const resultats = []; let pannes = 0;
async function une(fichier) {
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  await ctx.route('**/*', r => (/^https?:/i.test(r.request().url()) ? r.abort() : r.continue()));
  const p = await ctx.newPage();
  const rel = path.relative(RACINE, fichier);
  try {
    await p.goto(pathToFileURL(fichier).href, { waitUntil: 'load', timeout: 20000 });
    await p.waitForTimeout(250);
    await p.evaluate(ouvrir); await p.waitForTimeout(200);
    const m = await p.evaluate(mesurer);
    if (axeSource) {
      await p.evaluate(axeSource);
      m.A = await p.evaluate(async () => (await window.axe.run(document, { runOnly: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] }))
        .violations.filter(v => ['critical', 'serious'].includes(v.impact)).map(v => `${v.id}×${v.nodes.length}`));
    } else m.A = [];
    resultats.push({ rel, ...m });
  } catch (e) { pannes++; resultats.push({ rel, panne: String(e).slice(0, 160) }); }
  await ctx.close();
}
for (let i = 0; i < liste.length; i += EN_PARALLELE) await Promise.all(liste.slice(i, i + EN_PARALLELE).map(une));
await b.close();

const ecarts = resultats.filter(r => !r.panne && (r.L.length || r.B.length || r.C.length || r.A.length));
if (!MUET) {
  for (const r of resultats) {
    if (r.panne) { console.log(`⛔ ${r.rel} — ne s'ouvre pas : ${r.panne}`); continue; }
    r.L.forEach(x => console.log(`L ${r.rel} — listing qui défile de ${x.px} px à 390 px : « ${x.debut} »`));
    r.B.forEach(x => console.log(`B ${r.rel} — un SVG dessine un bloc de programmation : ${x}`));
    r.C.forEach(x => console.log(`C ${r.rel} — même phrase dans ${x.fois} corrections : « ${x.phrase}… »`));
    if (r.A.length) console.log(`A ${r.rel} — axe-core, page ouverte : ${r.A.join(', ')}`);
  }
}
const n = k => resultats.filter(r => !r.panne && r[k] && r[k].length).length;
console.log(`\n${resultats.length - pannes} page(s) ouvertes et mesurées à 390 px · ${pannes} en panne · L ${n('L')} · B ${n('B')} · C ${n('C')}${AXE ? ` · A ${n('A')}` : ''} page(s) concernées`);
if (JSON_OUT) fs.writeFileSync(JSON_OUT, JSON.stringify(resultats, null, 1));
if (!resultats.length || pannes) { console.log('⛔ EN PANNE (n°299)'); process.exit(2); }
const refus = resultats.filter(r => !r.panne && (r.L.length || r.B.length));
const refusA = resultats.filter(r => !r.panne && r.A && r.A.length);
if (refus.length) console.log(`✘ ${refus.length} page(s) font défiler un listing (n°364) ou dessinent un bloc (n°308), page ouverte — référence vide depuis le 22/11/2026 (n°273)`);
if (refusA.length) console.log(`✘ ${refusA.length} page(s) portent un défaut grave d'axe-core, page ouverte à 390 px — référence vide depuis le 25/11/2026 (n°273)`);
if (refus.length || refusA.length) process.exit(1);
if (STRICT && ecarts.length) { console.log('✘ la page ouverte porte des écarts (règle d\'or n°361)'); process.exit(1); }
console.log(ecarts.length ? `ℹ mesure : ${ecarts.length} page(s) à regarder, page ouverte (n°361)` : '✅ rien à signaler, page ouverte');
process.exit(0);
