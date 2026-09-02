/* controle_impression.mjs — ce que la page devient sur le papier.
 *
 * LE CONSTAT QUI A DONNÉ CE CONTRÔLE
 * ----------------------------------
 * Le 02/09/2026, Pascal a nommé l'imprimante de sa salle : une HP Color LaserJet
 * Pro MFP 3302sdw. Le dépôt promettait depuis toujours que ses pages
 * « s'impriment ». Personne ne l'avait vérifié — parce que personne ne savait sur
 * quoi. Le relevé, fait dans un navigateur en `media: print` :
 *
 *   · 213 pages sur 338 portaient au moins un texte illisible sur papier ;
 *   · 6 830 occurrences de texte SOMBRE sur fond SOMBRE ;
 *   ·  645 textes pâles sur la seule page d'accueil, le pire score du dépôt.
 *
 * La cause tenait en une ligne, répétée partout : `body{background:#fff;color:#111}`
 * et rien de plus. Les panneaux intérieurs gardaient leur fond marine d'écran, et
 * le texte que la règle venait de noircir se posait dessus — #111111 sur #0a1b3d,
 * soit 1,11 : 1. Sur le papier, un rectangle noir ; sur une laser, un rectangle
 * noir ET une cartouche vidée.
 *
 * CE QU'IL FAIT
 * -------------
 * Il ouvre chaque page en `media: print`, et pour chaque texte réellement visible
 * il compare sa couleur au fond qu'il aura vraiment, par le rapport de contraste
 * WCAG. Il REFUSE une seule chose, celle que les PR #338, #339 et #340 ont
 * corrigée et qui ne doit pas revenir : **un texte SOMBRE posé sur un fond
 * SOMBRE**. C'est la combinaison qui fait disparaître le texte, et elle seule.
 *
 * Un fond sombre qui porte du texte BLANC — un bandeau de titre, un pied de page —
 * n'est pas refusé : il se lit très bien sur le papier. Il coûte de l'encre, et
 * c'est une question d'intendance, pas de lisibilité ; ce contrôle la compte à
 * part plutôt que de trancher à la place de Pascal.
 *
 * Il COMPTE, sans refuser, tout texte sous 4,5 : 1 sur fond clair.
 *
 * ET IL FAUT ÊTRE EXACT SUR CE QUE CE COMPTE VEUT DIRE. En livrant les PR #338,
 * #339 et #340, j'ai écrit que ces textes étaient « faibles en niveaux de gris,
 * pas en couleur, et l'imprimante de la salle est une laser couleur ». **C'était
 * faux.** Le rapport que je calcule est le contraste WCAG, qui tient déjà compte
 * de la couleur : un titre à 2,13 : 1 est faible sur n'importe quelle imprimante,
 * et sur l'écran aussi. Il y a donc une seconde dette, réelle, de 3 800 textes —
 * elle demande une décision de palette, page par page, et ce n'est pas la même
 * campagne. Ce contrôle la compte et la nomme ; il ne la refuse pas, parce qu'un
 * contrôle qui refuse ce que personne n'a encore décidé de corriger bloque le
 * dépôt au lieu de le mesurer.
 *
 * POURQUOI IL REGARDE LES ANCÊTRES
 * --------------------------------
 * Le premier relevé trouvait 20 défauts résiduels, exactement deux par séquence.
 * C'était le bandeau des tâches, `#tachesBandeau`, que chaque page masque déjà à
 * l'impression : il ne s'imprime jamais. La mesure vérifiait que l'élément
 * lui-même n'était pas caché, mais pas ses ancêtres (règle d'or n°282).
 *
 * CE QU'IL NE FAIT PAS
 * --------------------
 * Il ne juge pas la mise en page : ni le nombre de feuilles, ni où une page se
 * coupe, ni si un tableau déborde de la largeur A4. Il ne lit pas les images :
 * un schéma illisible en niveaux de gris lui est invisible. Et il ne mesure que
 * l'état de la page AU CHARGEMENT — ce qu'un élève déplie avant d'imprimer lui
 * échappe.
 *
 * Usage :
 *     node _outils/controle_impression.mjs           # rapport complet
 *     node _outils/controle_impression.mjs --muet    # seulement les refus
 * Sortie : 0 si aucune page n'imprime un texte illisible, 1 sinon.
 */

import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
export const DEPOT = path.dirname(ICI);
const ECARTES = ['_archive-anciennes-versions', '_outils'];

/** En dessous, un fond est « sombre » : il a survécu au passage à l'impression. */
const FOND_SOMBRE = 0.12;
/** Seuil WCAG AA. En dessous, le texte est faible — COMPTÉ, jamais refusé : la
 *  décision de palette qui le corrigerait n'a pas encore été prise. */
const SIGNALE = 4.5;

//: Les pages qu'on n'imprime pas, chacune avec sa raison. Cette liste ne doit que
//: RÉTRÉCIR (règle d'or n°273). Vide au 02/09/2026, et c'est un fait mesuré.
export const TOLEREES = {};

export function pages(racine) {
  const out = [];
  (function marcher(d) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      if (e.isDirectory()) { if (!ECARTES.includes(e.name)) marcher(path.join(d, e.name)); }
      else if (e.name.toLowerCase().endsWith('.html')) out.push(path.join(d, e.name));
    }
  })(racine);
  return out.sort();
}

/** Ce que le navigateur voit, page par page. Exporté pour que le banc le rejoue. */
export async function relever(page, url) {
  await page.goto(url, { waitUntil: 'load', timeout: 30000 });
  await page.waitForTimeout(120);
  return page.evaluate(({ FOND_SOMBRE, SIGNALE }) => {
    const parse = s => {
      const m = /rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/.exec(s || '');
      if (!m) return null;
      const a = m[4] === undefined ? 1 : +m[4];
      if (a < 0.15) return null;
      const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
      return 0.2126 * f(+m[1]) + 0.7152 * f(+m[2]) + 0.0722 * f(+m[3]);
    };
    const ratio = (a, b) => { const x = Math.max(a, b), y = Math.min(a, b); return (x + 0.05) / (y + 0.05); };
    const cache = el => {
      let e = el;
      while (e) { const c = getComputedStyle(e); if (c.display === 'none' || c.visibility === 'hidden') return true; e = e.parentElement; }
      return false;
    };
    const refus = [], signales = [], encre = [];
    let lus = 0;
    for (const el of document.querySelectorAll('body *')) {
      if (/^(STYLE|SCRIPT|SVG|PATH|TEXT|OBJECT|IMG|CANVAS|NOSCRIPT)$/.test(el.tagName)) continue;
      const propre = [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join(' ').trim();
      if (propre.length < 3) continue;
      if (cache(el)) continue;                 // règle n°282 : ni lui, ni aucun ancêtre
      const cs = getComputedStyle(el);
      const lc = parse(cs.color); if (lc === null) continue;
      let e = el, lf = null;
      while (e) { const v = parse(getComputedStyle(e).backgroundColor); if (v !== null) { lf = v; break; } e = e.parentElement; }
      if (lf === null) lf = 1;                 // rien de posé : le papier est blanc
      lus++;
      const r = ratio(lc, lf);
      const ligne = { txt: propre.slice(0, 58), tag: el.tagName,
                      cls: String(el.className || '').trim().slice(0, 36), r: +r.toFixed(2) };
      if (lf < FOND_SOMBRE) {
        // Sombre sur sombre : le texte disparaît — c'est LE défaut. Sombre avec du
        // texte blanc : lisible, mais gourmand en encre — compté, pas refusé.
        if (r < SIGNALE) refus.push({ ...ligne, pourquoi: 'texte sombre sur fond sombre — il disparaît' });
        else encre.push(ligne);
      } else if (r < SIGNALE) signales.push(ligne);
    }
    return { lus, refus, signales, encre };
  }, { FOND_SOMBRE, SIGNALE });
}

export async function main(muet = false, racine = DEPOT, tolerees = TOLEREES) {
  const liste = pages(racine);
  const nav = await chromium.launch();
  const ctx = await nav.newContext({ viewport: { width: 794, height: 1123 } });  // A4 à 96 ppp
  const p = await ctx.newPage();
  await p.emulateMedia({ media: 'print' });

  let lus = 0, nSignales = 0, nEncre = 0;
  const fautives = [], tolereesVues = [];
  for (const abs of liste) {
    const rel = path.relative(racine, abs).split(path.sep).join('/');
    let r;
    try { r = await relever(p, 'file://' + abs); }
    catch (e) { fautives.push({ rel, refus: [{ txt: String(e).slice(0, 70), pourquoi: 'page illisible' }] }); continue; }
    lus += r.lus; nSignales += r.signales.length; nEncre += r.encre.length;
    if (!r.refus.length) continue;
    if (rel in tolerees) tolereesVues.push(rel); else fautives.push({ rel, refus: r.refus });
  }
  await nav.close();

  const fantomes = Object.keys(tolerees).filter(t => !tolereesVues.includes(t));
  if (!muet) {
    console.log(`${liste.length} page(s) ouvertes en « media: print » · ${lus} texte(s) lus · `
      + `${fautives.length} page(s) refusée(s)`);
    console.log(`     ${nSignales} texte(s) sous 4,5 : 1 sur fond clair — comptés, jamais refusés.`
      + `\n     Ce sont de VRAIS contrastes faibles, en couleur comme en gris : une seconde`
      + `\n     dette, qui demande une décision de palette et non un correctif mécanique.`);
    console.log(`     ${nEncre} texte(s) blancs sur un fond resté sombre : lisibles sur le papier,`
      + `\n     mais chaque bloc vide la cartouche. Question d'intendance, pas de lisibilité —`
      + `\n     comptée ici, tranchée par Pascal.`);
    if (tolereesVues.length) {
      console.log(`\n${tolereesVues.length} page(s) tolérée(s), chacune avec sa raison écrite :`);
      for (const t of tolereesVues) console.log(`  ${t}\n     ${tolerees[t]}`);
    }
    console.log(`\n     NON LU : la mise en page (nombre de feuilles, coupures, débordement A4) ;`
      + `\n     les images, qu'un schéma soit lisible ou non en niveaux de gris ; et tout ce`
      + `\n     qu'un élève déplie avant d'imprimer — seul l'état au chargement est mesuré.`);
  }

  if (fantomes.length) {
    console.log(`\n⚠ ${fantomes.length} page(s) tolérée(s) s'impriment désormais — leur ligne peut sortir de TOLEREES :`);
    for (const f of fantomes) console.log('  ' + f);
  }

  if (fautives.length) {
    console.log(`\n⛔ ${fautives.length} page(s) portent un texte que le papier ne rendra pas :`);
    for (const f of fautives.slice(0, 12)) {
      console.log(`  ${f.rel} — ${f.refus.length} texte(s)`);
      for (const x of f.refus.slice(0, 3))
        console.log(`     ${String(x.r ?? '—').padStart(5)} : 1  ${x.tag || ''}.${x.cls || ''}  « ${x.txt} »  · ${x.pourquoi}`);
    }
    if (fautives.length > 12) console.log(`  … et ${fautives.length - 12} page(s) de plus`);
    console.log(`\n     Un texte noirci par « body{color:#111} » posé sur un fond resté marine ne`
      + `\n     s'imprime pas : il disparaît, et la laser dépense sa cartouche à le cacher.`);
    return 1;
  }
  console.log(`\n✅ aucune page n'imprime un texte que le papier ne rendra pas`);
  return 0;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  process.exit(await main(process.argv.includes('--muet')));
}
