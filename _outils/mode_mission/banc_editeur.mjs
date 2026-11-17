/* banc_editeur.mjs — en mode mission, l'éditeur Python intégré se voit là où l'élève en a besoin (17/11/2026).
 *
 * Le constat (Pascal, 17/11/2026, sur 3e_C9.1, séance 2, activité 3) : « on dit que l'éditeur Python est intégré à
 * l'activité, mais je ne le vois pas ». En mode mission, l'annonce « l'éditeur Python est intégré à l'activité »
 * s'affichait sur les écrans de prédiction, avant l'éditeur ; et l'éditeur, montré avec la première question qui le
 * lit, disparaissait aux questions suivantes, qui lisent pourtant la console.
 *
 * Ce banc joue chaque page qui porte un éditeur (`.editeur-py`), en mode mission, écran par écran, et refuse :
 *   E1  un écran qui montre l'annonce de l'éditeur intégré (`.activite-en-ligne` d'une activité qui porte un éditeur)
 *       sans montrer l'éditeur ;
 *   E2  un écran de question qui suit, dans la même activité (avant son écran « Je retiens »), un écran où l'éditeur
 *       s'est montré, et qui ne le montre plus.
 * Les écrans de prédiction, AVANT l'éditeur, ne le montrent pas : c'est voulu (on prédit avant d'essayer).
 *
 * Usage : node _outils/mode_mission/banc_editeur.mjs [page.html …]   (sans page : toutes les séquences du dépôt)
 * Sortie : 0 rien à refuser · 1 au moins un refus · 2 rien n'a pu être lu (aucune page, ou Playwright absent).
 */
import { pathToFileURL } from 'node:url';
import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join, resolve } from 'node:path';

let chromium;
try { ({ chromium } = await import('playwright')); } catch (e) { console.log('✘ Playwright introuvable : rien n\'a été vérifié'); process.exit(2); }

const racine = resolve(new URL('../..', import.meta.url).pathname);
function toutes(d, o = []) {
  for (const n of readdirSync(d)) {
    if (n.startsWith('_archive') || n === 'node_modules' || n.startsWith('.') || n.startsWith('captures_')) continue;
    const p = join(d, n); const s = statSync(p);
    if (s.isDirectory()) toutes(p, o);
    else if (/^sequence_.*\.html$/.test(n)) { const t = readFileSync(p, 'utf8'); if (t.includes('class="editeur-py') && t.includes('mode-mission v1')) o.push(p); }
  }
  return o;
}
const pages = process.argv.slice(2).length ? process.argv.slice(2).map(p => resolve(p)) : toutes(racine).sort();
if (!pages.length) { console.log('✘ aucune page avec éditeur et mode mission : rien n\'a été vérifié'); process.exit(2); }

const b = await chromium.launch();
let refus = 0, ecransLus = 0;
for (const f of pages) {
  const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
  await p.goto(pathToFileURL(f).href); await p.waitForTimeout(400);
  const bouton = await p.$('#btnMission');
  if (!bouton) { console.log(`  ✘ ${f.replace(racine + '/', '')} : pas de bouton du mode mission`); refus++; await p.close(); continue; }
  await bouton.click(); await p.waitForTimeout(300);
  const fautes = [];
  let vuDansActivite = false, seance = '';
  for (let i = 0; i < 400; i++) {
    const e = await p.evaluate(() => {
      const vis = n => { const r = n.getBoundingClientRect(); return n.offsetParent !== null && r.width > 0 && r.height > 0; };
      const ou = (document.getElementById('msOu') || {}).textContent || '';
      const ed = [...document.querySelectorAll('.editeur-py')].some(vis);
      const annonce = [...document.querySelectorAll('.activite-en-ligne')].some(a => vis(a) && a.closest('.activite, .act, .card, .carte, section') && a.closest('.activite, .act, .card, .carte, section').querySelector('.editeur-py'));
      const question = [...document.querySelectorAll('fieldset.qcm-groupe, textarea, select[id]')].some(q => vis(q) && !q.closest('.editeur-py') && !q.closest('.identite'));
      return { ou, ed, annonce, question };
    });
    ecransLus++;
    const s = (e.ou.match(/Séance \d+/) || [''])[0];
    if (s !== seance) { seance = s; vuDansActivite = false; }
    if (/^Je retiens/.test(e.ou)) vuDansActivite = false;
    if (e.annonce && !e.ed) fautes.push(`E1 annonce sans éditeur · ${e.ou.slice(0, 80)}`);
    /* un écran de question d'une activité : « … · 2 sur 5 », « À toi de jouer », « b) … », « Avant de vérifier » */
    const enActivite = /· \d+ sur \d+|Avant de vérifier|^À toi de jouer|^[a-z]\) /.test(e.ou);
    if (vuDansActivite && enActivite && e.question && !e.ed) fautes.push(`E2 éditeur disparu · ${e.ou.slice(0, 80)}`);
    if (e.ed) vuDansActivite = true;
    else if (!enActivite) vuDansActivite = false;   // une carte, un bilan, le départ d'une autre activité : l'activité est close
    const suiv = await p.$('#msSuiv'); if (!suiv || !(await suiv.isVisible())) break;
    await suiv.click().catch(() => {}); await p.waitForTimeout(100);
    if ((await p.evaluate(() => (document.getElementById('msOu') || {}).textContent || '')) === e.ou) break;
  }
  const nom = f.replace(racine + '/', '').split('/').pop();
  if (fautes.length) { refus += fautes.length; console.log(`  ✘ ${nom}`); fautes.slice(0, 8).forEach(x => console.log('      · ' + x)); }
  else console.log(`  ✅ ${nom}`);
  await p.close();
}
await b.close();
console.log(`${pages.length} page(s) jouées · ${ecransLus} écran(s) · ${refus ? '✘ ' + refus + ' refus' : '✅ l\'éditeur se voit partout où on l\'annonce et où on le lit'}`);
process.exit(refus ? 1 : 0);
