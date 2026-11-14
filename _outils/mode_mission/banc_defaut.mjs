// Banc du mode mission « allumé d'emblée » (décision de Pascal du 14/11/2026) — sur chaque séquence du dépôt.
//   node _outils/mode_mission/banc_defaut.mjs [--filtre <texte>]
// Un navigateur d'élève (navigator.webdriver faux) :
//   · arrive en mission à sa première visite, sur toute page dont le mode reconnaît les séances ;
//   · « 📄 Page complète » le ramène à la page qui défile, et la page s'en souvient au rechargement ;
//   · « 🎮 Mode mission » l'y renvoie, et la page s'en souvient aussi ;
//   · une sauvegarde effacée (stockage vidé) le remet en mission ;
//   · imprimé en mission, il sort la même fiche que la page complète (tout ce qui cache est sous @media screen).
// Un robot de test (navigator.webdriver vrai, le défaut de Playwright) ouvre la page complète : c'est ce que les
// autres bancs et les contrôles du dépôt mesurent.
// Sortie 0 si tout passe, 1 sinon. Ne dépend d'aucun réseau.
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const RACINE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const i = process.argv.indexOf('--filtre'); const FILTRE = i > 0 ? process.argv[i + 1] : '';
const pages = [];
(function lire(d) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const c = path.join(d, e.name);
    if (e.isDirectory()) { if (!/^(\.|node_modules|_archive)/.test(e.name)) lire(c); }
    else if (/^sequence.*\.html$/.test(e.name) && /^theme-/.test(path.relative(RACINE, c)) && (!FILTRE || c.includes(FILTRE))) pages.push(c);
  }
})(RACINE);
pages.sort();
if (!pages.length) { console.log('⛔ aucune séquence lue'); process.exit(2); }

const refus = []; let reconnues = 0, telles = [];
const b = await chromium.launch();
const eleve = await b.newContext({ viewport: { width: 390, height: 844 } });
await eleve.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false, configurable: true }); });
const robot = await b.newContext({ viewport: { width: 390, height: 844 } });
const etat = (p) => p.evaluate(() => ({ ms: document.body.classList.contains('ms'), bouton: !!document.getElementById('btnMission') }));
const texteImprime = (p) => p.evaluate(() => {
  const vu = (e) => { for (let x = e; x; x = x.parentElement) { const c = getComputedStyle(x); if (c.display === 'none' || c.visibility === 'hidden') return false; } return true; };
  return [...document.querySelectorAll('h2,h3,legend,label,p,li,td')].filter(vu).map((e) => e.textContent.trim()).join('\n').length;
});

for (const page of pages) {
  const rel = path.relative(RACINE, page), url = pathToFileURL(page).href, faute = (m) => refus.push(rel + ' — ' + m);
  const p = await eleve.newPage(); const err = []; p.on('pageerror', (e) => err.push(e.message));
  await p.goto(url, { waitUntil: 'load' }); await p.evaluate(() => { localStorage.clear(); sessionStorage.clear(); });
  await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(250);
  let e = await etat(p);
  if (!e.bouton) { telles.push(rel); if (e.ms) faute('mission allumée sans bouton pour la quitter'); await p.close(); continue; }
  reconnues++;
  if (!e.ms) faute('première visite d\'un élève : la page ne s\'ouvre pas en mission');
  // imprimée en mission, la fiche est celle de la page complète
  await p.emulateMedia({ media: 'print' }); const enMission = await texteImprime(p); await p.emulateMedia({ media: 'screen' });
  await p.evaluate(() => document.getElementById('msQuitter').click()); await p.waitForTimeout(150);
  await p.emulateMedia({ media: 'print' }); const pleine = await texteImprime(p); await p.emulateMedia({ media: 'screen' });
  if (Math.abs(enMission - pleine) > Math.max(40, pleine * 0.02)) faute(`imprimée en mission, la fiche diffère de la page complète (${enMission} contre ${pleine} caractères)`);
  if ((await etat(p)).ms) faute('« 📄 Page complète » ne quitte pas la mission');
  await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(200);
  if ((await etat(p)).ms) faute('après « 📄 Page complète » et un rechargement, la page revient en mission');
  await p.evaluate(() => document.getElementById('btnMission').click()); await p.waitForTimeout(150); await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(200);
  if (!(await etat(p)).ms) faute('après « 🎮 Mode mission » et un rechargement, la page ne revient pas en mission');
  // « Effacer ma sauvegarde » : la page retire sa propre clé (KEY) puis se recharge. La page avait enregistré quelque chose
  // (sa clé existe) quand l'élève a choisi la page complète ; sa clé disparue, l'élève suivant arrive en mission.
  const cle = await p.evaluate(() => (typeof KEY === 'string' ? KEY : null));
  if (cle) {
    await p.evaluate((k) => { localStorage.setItem(k, '{}'); document.getElementById('msQuitter').click(); }, cle); await p.waitForTimeout(100);
    await p.evaluate((k) => localStorage.removeItem(k), cle); await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(200);
    if (!(await etat(p)).ms) faute('« Effacer ma sauvegarde » (la clé de la page retirée) : la page ne revient pas en mission');
  }
  // un navigateur neuf (stockage vide) : la mission
  await p.evaluate(() => document.getElementById('msQuitter').click()); await p.waitForTimeout(100);
  await p.evaluate(() => localStorage.clear()); await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(200);
  if (!(await etat(p)).ms) faute('stockage vide : la page ne revient pas en mission');
  if (err.length) faute('erreur JS : ' + err[0]);
  await p.close();
  const r = await robot.newPage(); await r.goto(url, { waitUntil: 'load' }); await r.evaluate(() => localStorage.clear());
  await r.reload({ waitUntil: 'load' }); await r.waitForTimeout(200);
  if ((await etat(r)).ms) faute('un robot de test arrive en mission : les bancs ne mesureraient plus la page complète');
  await r.close();
}
await b.close();
console.log(`${pages.length} séquence(s) · ${reconnues} s'ouvrent en mission pour l'élève · ${telles.length} s'ouvrent telles quelles (séances non reconnues)`);
for (const t of telles) console.log('   · telle quelle : ' + t);
if (refus.length) { for (const r of refus) console.log('❌ ' + r); process.exit(1); }
console.log('✅ chaque séquence s\'ouvre en mission pour l\'élève, se quitte et s\'en souvient, revient en mission après une sauvegarde effacée, s\'imprime entière ; un robot de test ouvre la page complète');
