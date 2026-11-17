// Banc de la barre d'étapes (le « chenillard ») et du retour en mission — toutes les pages qui portent le mode mission.
// Défauts relevés par Pascal le 16/11/2026 sur 4e_C9.1, cherchés ici dans les trois thèmes :
//   B1 · revenir en arrière éteint des écrans déjà passés (ils se rallument quand on avance de nouveau) ;
//   B2 · un écran où l'on écrit, sans rien à vérifier ici, ne s'allume jamais, même écrit et dépassé ;
//   B3 · sorti du mode et la page défilée, aucun bouton visible ne permet d'y revenir.
// La barre ne doit jamais dire si une réponse est juste : le banc ne répond à aucune question à choix.
//
//   node _outils/mode_mission/banc_barre.mjs                      → les pages du dépôt
//   node _outils/mode_mission/banc_barre.mjs --racine <dossier>   → une autre copie du site (main, pour comparer)
//   node _outils/mode_mission/banc_barre.mjs --json <fichier>     → le détail, page par page
//   node _outils/mode_mission/banc_barre.mjs --filtre 4e_C9.1      → les pages dont le chemin contient ce texte
// Sortie 0 : aucun défaut ; 1 : au moins un ; 2 : rien n'a pu être lu (n°299).
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const opt = (n) => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : null; };
const RACINE = path.resolve(opt('--racine') || path.join(ICI, '..', '..'));
const JSON_OUT = opt('--json'), FILTRE = opt('--filtre');

function pages(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.name.startsWith('.') || e.name === 'node_modules' || e.name.startsWith('_archive')) continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) { if (dir === RACINE && !e.name.startsWith('theme-')) continue; pages(p, out); }
    else if (e.name.endsWith('.html') && fs.readFileSync(p, 'utf8').includes('<!-- mode-mission v1 : début')) out.push(p);
  }
  return out;
}
const liste = pages(RACINE).sort().filter((f) => !FILTRE || f.includes(FILTRE));
if (!liste.length) { console.log('⛔ aucune page à mode mission sous ' + RACINE); process.exit(2); }

const RAIL = `[...document.querySelectorAll('#msRail [data-k]')].map(b => b.classList.contains('fait') ? 'F' : b.classList.contains('repondu') ? 'r' : '.')`;
const b = await chromium.launch();
const res = [];
for (const F of liste) {
  const rel = path.relative(RACINE, F);
  const r = { page: rel, ecrans: 0, b1: [], b2: [], b3: false, erreurs: [] };
  const ctx = await b.newContext({ viewport: { width: 1280, height: 860 } }); const p = await ctx.newPage();
  p.on('pageerror', (e) => r.erreurs.push(e.message.slice(0, 120)));
  try {
    await p.goto(pathToFileURL(F).href, { waitUntil: 'load' }); await p.waitForTimeout(400);
    if (!(await p.$('#btnMission'))) { r.lu = false; r.pourquoi = 'pas de bouton du mode mission (gabarit non reconnu)'; res.push(r); await ctx.close(); continue; }
    await p.click('#btnMission'); await p.waitForTimeout(250);
    const L = (await p.evaluate(RAIL)).length; r.ecrans = L;
    // la séance 1 parcourue écran par écran : sur un écran à écrire sans vérification, on écrit ; on ne répond à rien d'autre
    const ecrits = [];
    for (let j = 0; j < L - 1 && j < 40; j++) {
      const e = await p.evaluate(() => {
        const s = document.documentElement._mission.ecran(), v = document.getElementById('msVerif');
        return { t: s && s.t, verif: v && !v.hidden };
      });
      if (e.t === 'partie' && !e.verif) {
        const n = await p.evaluate(() => {
          const vu = (x) => x.offsetParent && !x.closest('.ms-cache');
          // un écran qui porte aussi une question à choix ne compte pas : le banc ne répond à aucune question à choix
          if ([...document.querySelectorAll('select, input[type=radio]')].some(vu)) return 0;
          let n = 0;
          for (const x of document.querySelectorAll('textarea, input[type=text], input:not([type])')) {
            if (!x.offsetParent || x.disabled || x.readOnly || x.closest('.ms-cache')) continue;
            x.value = 'essai du banc'; x.dispatchEvent(new Event('input', { bubbles: true })); n++;
          }
          return n;
        });
        if (n) ecrits.push(j);
      }
      const suiv = await p.$('#msSuiv:not([hidden])'); if (!suiv) break;
      await p.click('#msSuiv'); await p.waitForTimeout(90);
      if ((await p.evaluate(RAIL)).length !== L) break;          // passé à la séance suivante : on s'arrête
    }
    const k = await p.evaluate(() => [...document.querySelectorAll('#msRail [data-k]')].findIndex(x => x.classList.contains('ici')));
    const avant = await p.evaluate(RAIL);
    r.b2 = ecrits.filter((j) => j < k && avant[j] !== 'F');            // écrit et dépassé, mais éteint
    if (L >= 3 && k >= 2) {
      await p.click('#msRail [data-k="1"]'); await p.waitForTimeout(120);
      const apres = await p.evaluate(RAIL);
      r.b1 = avant.map((x, j) => (j >= 2 && x === 'F' && apres[j] !== 'F') ? j : -1).filter((j) => j >= 0);
      // ce qui était éteint avant le retour, mais déjà dépassé, compte aussi : un écran sans question dépassé s'allume
      r.passesEteints = avant.slice(0, k).filter((x) => x === '.').length;
    }
    // sortir, défiler loin du bouton du haut, chercher un bouton visible pour revenir
    await p.click('#msQuitter'); await p.waitForTimeout(200);
    await p.evaluate(() => window.scrollTo(0, document.body.scrollHeight * 0.6)); await p.waitForTimeout(350);
    const vis = await p.evaluate(() => {
      const dansVue = (x) => { if (!x || !x.offsetParent && getComputedStyle(x).position !== 'fixed') return false; const q = x.getBoundingClientRect(); return q.width > 0 && q.bottom > 0 && q.top < innerHeight && getComputedStyle(x).display !== 'none' && getComputedStyle(x).visibility !== 'hidden'; };
      return { haut: dansVue(document.getElementById('btnMission')), flottant: dansVue(document.getElementById('msRevenir')) };
    });
    r.b3 = !vis.haut && !vis.flottant;
    if (vis.flottant) { await p.click('#msRevenir'); await p.waitForTimeout(250); r.revenu = await p.evaluate(() => document.body.classList.contains('ms')); }
    r.lu = true;
  } catch (e) { r.lu = false; r.pourquoi = String(e.message || e).slice(0, 160); }
  res.push(r); await ctx.close();
  const d = [r.b1.length ? 'B1 ' + r.b1.length : '', r.b2.length ? 'B2 ' + r.b2.length : '', r.b3 ? 'B3' : '', r.erreurs.length ? 'JS ' + r.erreurs.length : ''].filter(Boolean).join(' · ');
  console.log((!r.lu ? '⛔ ' : d ? '✘ ' : '✓ ') + rel.replace(/^theme-\d-[^/]+\/[^/]+\//, '') + (r.lu ? ' — ' + r.ecrans + ' écrans' + (d ? ' — ' + d : '') : ' — non lue : ' + r.pourquoi));
}
await b.close();
if (JSON_OUT) fs.writeFileSync(JSON_OUT, JSON.stringify(res, null, 1));
const lues = res.filter((r) => r.lu), nb = (f) => lues.filter(f).length;
console.log(`\n${lues.length} / ${res.length} page(s) jouées · B1 (retour en arrière éteint) ${nb((r) => r.b1.length)} · B2 (écrit jamais allumé) ${nb((r) => r.b2.length)} · B3 (pas de bouton pour revenir) ${nb((r) => r.b3)} · erreurs JS ${nb((r) => r.erreurs.length)}`);
if (!lues.length) process.exit(2);
process.exit(lues.some((r) => r.b1.length || r.b2.length || r.b3 || r.erreurs.length) ? 1 : 0);
