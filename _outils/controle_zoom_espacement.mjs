/**
 * controle_zoom_espacement.mjs — une page se lit à 200 % et avec des lettres espacées (règle d'or n°370, en essai).
 *
 * LE CONSTAT (audit du 22/11/2026, PR #867)
 * Le dépôt mesure la page à 390 px (débordement, n°364), le contraste des liens, les champs à 16 px ; il n'a jamais
 * mesuré les deux réglages qu'utilisent les élèves dyslexiques et malvoyants : le zoom du navigateur (WCAG 2.2, 1.4.4)
 * et l'espacement du texte (1.4.12 : hauteur de ligne 1,5 × la taille ; paragraphes 2 × ; lettres 0,12 em ;
 * mots 0,16 em). `balayage-navigateur` l'a toujours écrit « non exécuté ». Idée tirée de la veille du 22/11
 * (`masuP9/a11y-specialist-skills`, MIT), réécrite de zéro : aucun paquet tiers n'est lancé.
 *
 * CE QU'IL MESURE (sans effet de bord : aucun clic, aucune saisie)
 *   Z1  zoom 200 % : fenêtre de 640 px de large (1 280 px à 200 %), aucun défilement horizontal de la page ;
 *   E1  espacement 1.4.12 injecté : aucun texte ne se coupe — un élément à `overflow:hidden` (ou `clip`) dont le
 *       contenu dépasse (`scrollHeight > clientHeight + 2` ou `scrollWidth > clientWidth + 2`) et qui porte du texte ;
 *   C1  cibles : boutons, liens hors du texte courant, cases et boutons radio visibles de moins de 24 × 24 px
 *       (2.5.8), hors liens placés dans une phrase (exception de la norme) — compté, jamais refusé.
 * Ce qu'il ne voit pas : la lecture au lecteur d'écran, le clavier pas à pas, une page qui ne s'ouvre qu'après un clic.
 *
 * STATUT : MESURE (règle en essai, n°147). Sortie 0 quand la mesure est faite ; avec --strict, 1 dès qu'une page a
 * un Z1 ou un E1 ; 2 EN PANNE si Playwright manque ou si aucune page n'a été lue (n°299).
 * Usage : node _outils/controle_zoom_espacement.mjs [chemins…] [--strict] [--muet] [--max N]
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const RACINE = path.resolve(ICI, '..');
const IGNORES = new Set(['.git', 'node_modules', '_archive-anciennes-versions', '_outils', '_exports']);
const ESPACEMENT = `*:not(svg):not(svg *){line-height:1.5!important;letter-spacing:.12em!important;word-spacing:.16em!important}
p{margin-bottom:2em!important}`;

const args = process.argv.slice(2);
const strict = args.includes('--strict');
const muet = args.includes('--muet');
const iMax = args.indexOf('--max');
const max = iMax >= 0 ? parseInt(args[iMax + 1], 10) : Infinity;
const departs = args.filter((a, i) => !a.startsWith('--') && !(iMax >= 0 && i === iMax + 1));

function pages(depart) {
  const st = fs.statSync(depart);
  if (st.isFile()) return depart.endsWith('.html') ? [depart] : [];
  const out = [];
  for (const e of fs.readdirSync(depart, { withFileTypes: true })) {
    if (IGNORES.has(e.name) || e.name.startsWith('.')) continue;
    const p = path.join(depart, e.name);
    if (e.isDirectory()) out.push(...pages(p));
    else if (/^(sequence|qcm|atelier|tp_|synthese|lexique).*\.html$/.test(e.name)) out.push(p);
  }
  return out.sort();
}

let chromium;
try { ({ chromium } = await import('playwright')); }
catch { console.log('⛔ EN PANNE : Playwright introuvable (n°299).'); process.exit(2); }

const liste = (departs.length ? departs : [RACINE]).flatMap(d => pages(path.resolve(d))).slice(0, max);
if (!liste.length) { console.log('⛔ EN PANNE : aucune page lue (n°299).'); process.exit(2); }

const navigateur = await chromium.launch();
const resultats = [];
for (const fichier of liste) {
  const ctx = await navigateur.newContext({ viewport: { width: 640, height: 900 }, reducedMotion: 'reduce' });
  const page = await ctx.newPage();
  try {
    await page.goto(pathToFileURL(fichier).href, { waitUntil: 'load', timeout: 30000 });
    await page.addStyleTag({ content: ESPACEMENT });
    await page.waitForTimeout(150);
    const r = await page.evaluate(() => {
      const doc = document.documentElement;
      const z1 = doc.scrollWidth > window.innerWidth + 2;
      const coupes = [];
      for (const el of document.querySelectorAll('body *')) {
        const cs = getComputedStyle(el);
        if (cs.display === 'none' || cs.visibility === 'hidden') continue;
        if (el.closest('details:not([open])') || el.closest('svg') || el.closest('[aria-hidden="true"]')) continue;  // un calque d'éditeur (aria-hidden) défile avec sa zone de saisie (n°364)
        const cache = /hidden|clip/.test(cs.overflowX + cs.overflowY);
        if (!cache || !(el.innerText || '').trim()) continue;
        if (el.scrollHeight > el.clientHeight + 2 || el.scrollWidth > el.clientWidth + 2) {
          if (el.clientHeight === 0 && el.clientWidth === 0) continue;
          coupes.push((el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/)[0] : '')).slice(0, 40));
        }
      }
      let petites = 0;
      for (const el of document.querySelectorAll('button, a, input[type=checkbox], input[type=radio], [role=button], [role=tab]')) {
        const b = el.getBoundingClientRect();
        if (!b.width || !b.height) continue;
        if (el.tagName === 'A' && el.closest('p, li, td, dd')) continue;
        if (b.width < 24 || b.height < 24) petites++;
      }
      return { z1, coupes: [...new Set(coupes)].slice(0, 5), nCoupes: coupes.length, petites };
    });
    resultats.push({ fichier: path.relative(RACINE, fichier), ...r });
  } catch (e) {
    resultats.push({ fichier: path.relative(RACINE, fichier), erreur: String(e.message || e).slice(0, 80) });
  }
  await ctx.close();
}
await navigateur.close();

const lues = resultats.filter(r => !r.erreur);
if (!lues.length) { console.log('⛔ EN PANNE : aucune page n\'a pu être ouverte (n°299).'); process.exit(2); }
const z = lues.filter(r => r.z1), e = lues.filter(r => r.nCoupes), c = lues.filter(r => r.petites);
if (!muet) {
  for (const r of resultats) {
    if (r.erreur) { console.log(`⚠ ${r.fichier} — non ouverte : ${r.erreur}`); continue; }
    if (!r.z1 && !r.nCoupes) continue;
    console.log(`${r.fichier}`);
    if (r.z1) console.log('   · Z1 à 200 % (640 px), la page défile de côté');
    if (r.nCoupes) console.log(`   · E1 lettres espacées : ${r.nCoupes} texte(s) coupé(s) — ${r.coupes.join(', ')}`);
  }
}
console.log(`${lues.length} page(s) ouvertes à 200 % avec l'espacement du texte WCAG 1.4.12 · ${z.length} défilent de côté · `
  + `${e.length} coupent du texte · ${c.length} ont au moins une cible sous 24 × 24 px (compté, non refusé)`);
console.log('ℹ Non vu : lecteur d\'écran, clavier pas à pas, ce qui ne s\'ouvre qu\'après un clic.');
if (strict && (z.length || e.length)) {
  console.log('✘ une page se lit à 200 % et avec des lettres espacées — règle d\'or n°370 (--strict)');
  process.exit(1);
}
console.log(z.length || e.length ? '📏 mesure (règle n°370 en essai) : rien n\'est refusé sans --strict'
  : '✅ chaque page se lit à 200 % et avec des lettres espacées');
process.exit(0);
