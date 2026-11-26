// banc_effacement.mjs — « Effacer, c'est tout effacer » : rejoué dans le navigateur, page par page.
//
// LE CONSTAT (audit externe du jardin connecté de 4e, transmis par Pascal le 20/11/2026)
// ----------------------------------------------------------------------------------
// Une phrase écrite dans le cahier des charges de la séance 4, puis « 🗑 Effacer ma sauvegarde », confirmation,
// rechargement : la phrase était encore là. Le bouton retirait la clé de la séquence ; l'exercice incrusté (kit des
// ateliers) garde son travail sous sa propre clé. Sur un poste partagé, l'élève suivant lit la réponse du précédent.
// Pascal : « ils devraient être généralisés à toutes les séances et QCM ».
//
// Le même geste laissait aussi les étoiles du mode mission sur 27 des 60 séquences : celles dont la clé de sauvegarde
// vit dans une fonction, que le mode mission ne voyait pas. Mesuré sur `main` le 20/11/2026 : 166 pages jouées, 40 qui
// gardaient quelque chose (24 le travail d'un exercice incrusté, 27 les étoiles, 11 les deux) ; aucun des 76 QCM.
//
// La règle d'or n°322 (10/11/2026) demandait qu'une page « sache effacer » ; `controle_sauvegarde_locale.py` le lit
// dans le source (un bouton, un `removeItem`). Lire le source ne dit pas si l'effacement est COMPLET : ce banc le joue.
//
// CE QU'IL FAIT, sur chaque page publiée qui porte un bouton d'effacement (`#btnReset`, `#btnEffacer`, `#btn-effacer`, `#clear`)
//   1. ouvre la page dans un navigateur vide ;
//   2. écrit un TÉMOIN dans chaque champ de texte, coche une proposition par groupe, coche chaque case, change chaque
//      menu — partout, exercices incrustés et éditeur compris — et laisse la page enregistrer ;
//   2 bis. si la page porte le mode mission : pose le témoin dans sa mémoire, comme une étoile gagnée à une visite
//      précédente, puis recharge — l'élève revient, ses réponses et ses étoiles l'attendent ;
//   3. clique sur le bouton d'effacement, confirme (deux clics dans la page), attend le rechargement ;
//   4. REFUSE la page si quelque chose reste : le témoin dans une valeur du navigateur (localStorage, sessionStorage),
//      le témoin dans un champ, une proposition ou une case encore cochée, un menu encore changé.
//
// Ce qu'il ne voit pas : ce que l'élève a écrit depuis une AUTRE page (le QCM du lot a son propre bouton) ; un état
// qui ne passe par aucun champ (un dessin au doigt, un tracé) ; ce qu'un vrai navigateur garde de son côté
// (remplissage automatique des formulaires).
//
//   node _outils/banc_effacement.mjs [--muet] [--a-la-fois=3] [page.html | dossier …]     (sans chemin : les trois thèmes)
// Sortie : 0 rien ne reste · 1 une page garde quelque chose · 2 rien joué (n°299).
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const DEPOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2), MUET = args.includes('--muet');
const chemins = args.filter(a => !a.startsWith('--'));
export const TEMOIN = 'Zq7temoin42';
/* les quatre noms que porte un bouton d'effacement sur le site (les mêmes que `controle_sauvegarde_locale.py`, sans
   « Recommencer » : sur un QCM, il garde le nom de l'élève) */
const BOUTONS = '#btnReset, #btnEffacer, #btn-effacer, #clear';

function pages(racines) {
  const out = [];
  const tour = d => { for (const f of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, f.name);
    if (f.isDirectory()) { if (!/^(_archive|_generation|node_modules|\.)/.test(f.name) && !f.name.startsWith('_archive')) tour(p); }
    else if (f.name.endsWith('.html')) out.push(p);
  } };
  for (const r of racines) { const a = path.resolve(r); if (!fs.existsSync(a)) continue; fs.statSync(a).isDirectory() ? tour(a) : out.push(a); }
  return out.sort().filter(p => /id="(btnReset|btnEffacer|btn-effacer|clear)"/.test(fs.readFileSync(p, 'utf8')));
}

/* dans la page : écrire le témoin partout, et dire ce qu'on a posé (pour le retrouver après le rechargement) */
const POSER = (T) => {
  const dit = (e, t) => e.dispatchEvent(new Event(t, { bubbles: true }));
  const ou = e => e.id ? '#' + CSS.escape(e.id) : null;
  const pose = { textes: [], coches: [], menus: [] };
  document.querySelectorAll('textarea, input[type=text], input:not([type]), input[type=search]').forEach(e => {
    if (e.disabled || e.readOnly) return;
    e.value = T; dit(e, 'input'); dit(e, 'change'); if (ou(e)) pose.textes.push(ou(e));
  });
  const vus = new Set();
  document.querySelectorAll('input[type=radio], input[type=checkbox]').forEach(e => {
    if (e.disabled || e.checked) return;
    if (e.type === 'radio') { if (vus.has(e.name)) return; vus.add(e.name); }
    e.checked = true; dit(e, 'input'); dit(e, 'change'); if (ou(e)) pose.coches.push(ou(e));
  });
  document.querySelectorAll('select').forEach(e => {
    if (e.disabled || e.options.length < 2) return;
    const i = e.selectedIndex === e.options.length - 1 ? 0 : e.options.length - 1;
    e.selectedIndex = i; dit(e, 'input'); dit(e, 'change'); if (ou(e)) pose.menus.push([ou(e), i]);
  });
  return pose;
};
const GARDE = (T) => { const o = [];
  for (const [nom, s] of [['localStorage', localStorage], ['sessionStorage', sessionStorage]])
    for (let i = 0; i < s.length; i++) { const k = s.key(i); if (String(s.getItem(k)).includes(T)) o.push(nom + ' « ' + k + ' »'); }
  return o; };
const RESTE = ([T, pose]) => {
  const reste = [];
  document.querySelectorAll('textarea, input[type=text], input:not([type]), input[type=search]').forEach(e => {
    if (String(e.value).includes(T)) reste.push('le témoin dans le champ ' + (e.id ? '#' + e.id : '<' + e.tagName.toLowerCase() + '>')); });
  for (const s of pose.coches) { const e = document.querySelector(s); if (e && e.checked && !e.defaultChecked) reste.push('encore coché : ' + s); }
  for (const [s, i] of pose.menus) { const e = document.querySelector(s); if (e && e.selectedIndex === i && ![...e.options].some((o, k) => k === i && o.defaultSelected)) reste.push('menu encore changé : ' + s); }
  return reste;
};

export async function jouer(page, fichier) {
  const erreurs = []; page.on('pageerror', e => erreurs.push(e.message)); page.on('dialog', d => d.accept().catch(() => {}));
  await page.goto(pathToFileURL(fichier).href, { waitUntil: 'load' });
  await page.evaluate(() => { localStorage.clear(); sessionStorage.clear(); });
  await page.reload({ waitUntil: 'load' }); await page.waitForTimeout(350);
  const bouton = page.locator(BOUTONS).first();
  if (!(await bouton.count())) return { rien: 'aucun bouton d\'effacement' };
  const pose = await page.evaluate(POSER, TEMOIN);
  await page.waitForTimeout(1100);                                   // les sauvegardes différées (600 ms)
  await page.evaluate(() => { const b = document.getElementById('btnSave'); if (b) b.click(); });
  await page.waitForTimeout(250);
  /* la mémoire du mode mission : le témoin y entre comme une étoile gagnée à une visite précédente, puis l'élève revient.
     Une mission qui ne garde pas le témoin au rechargement (elle se croit déjà effacée) n'est pas éprouvée : on le dit. */
  let mission = 'absente';
  if (await page.evaluate(() => !!document.getElementById('btnMission'))) {
    await page.evaluate((T) => { const c = decodeURIComponent(location.pathname).split('/'), f = c.pop() || 'page', d = c.pop() || '', k = 'mission:' + (d ? d + '/' : '') + f;   // le dossier et la page (26/11/2026)
      let m = null; try { m = JSON.parse(localStorage.getItem(k) || 'null'); } catch (e) {}
      if (!m || m.v !== 1) m = { v: 1, on: false, k: {}, essais: {}, erreurs: {}, etoiles: {}, fait: {}, loin: {} };
      m.etoiles = m.etoiles || {}; m.fait = m.fait || {}; m.etoiles[T] = 3; m.fait[T] = 1; m.vu = true;
      localStorage.setItem(k, JSON.stringify(m)); }, TEMOIN);
    await page.reload({ waitUntil: 'load' }); await page.waitForTimeout(450);
    mission = (await page.evaluate(GARDE, TEMOIN)).some(k => k.includes('« mission:')) ? 'éprouvée' : 'non éprouvée';
  }
  const avant = await page.evaluate(GARDE, TEMOIN);
  const poses = pose.textes.length + pose.coches.length + pose.menus.length;
  /* effacer : un clic, puis un second si la page demande confirmation (deux clics dans la page, n°322) */
  await page.evaluate(() => { window.__avantEffacement = true; });
  const recharge = () => page.evaluate(() => !window.__avantEffacement).catch(() => true);
  for (let i = 0; i < 3 && !(await recharge()); i++) {
    await page.evaluate(sel => { const b = document.querySelector(sel); if (b) b.click(); }, BOUTONS).catch(() => {});
    await page.waitForTimeout(450);
  }
  if (!(await recharge())) {
    /* une page qui efface sans se recharger : on la recharge nous-mêmes, c'est ce que voit l'élève suivant */
    await page.reload({ waitUntil: 'load' });
  }
  await page.waitForLoadState('load').catch(() => {}); await page.waitForTimeout(700);
  const garde = await page.evaluate(GARDE, TEMOIN), reste = await page.evaluate(RESTE, [TEMOIN, pose]);
  return { poses, avant, garde, reste, erreurs, mission };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const liste = pages(chemins.length ? chemins : fs.readdirSync(DEPOT).filter(d => d.startsWith('theme-')).map(d => path.join(DEPOT, d)));
  if (!liste.length) { console.log('✘ aucune page avec un bouton d\'effacement : rien n\'a été joué'); process.exit(2); }
  const b = await chromium.launch();
  let refus = 0, jouees = 0, sansRien = 0, missions = 0, missionsNon = 0;
  /* trois pages à la fois (les attentes sont des minuteries, pas du calcul) ; les lignes sortent dans l'ordre des pages */
  const N = Math.max(1, parseInt((args.find(a => a.startsWith('--a-la-fois=')) || '').split('=')[1] || '3', 10) || 3);
  const resultats = new Array(liste.length); let suivant = 0;
  await Promise.all(Array.from({ length: Math.min(N, liste.length) }, async () => {
    for (;;) {
      const i = suivant++; if (i >= liste.length) return;
      const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }); const page = await ctx.newPage();
      let r; try { r = await jouer(page, liste[i]); } catch (e) { r = { panne: String(e.message || e).split('\n')[0] }; }
      await ctx.close().catch(() => {});
      resultats[i] = r;
    }
  }));
  liste.forEach((f, i) => {
    const r = resultats[i], nom = path.relative(DEPOT, f);
    if (r.panne) { refus++; console.log('❌ ' + nom + '\n     le banc n\'a pas pu jouer la page : ' + r.panne); return; }
    if (r.rien) return;
    jouees++; if (r.mission === 'éprouvée') missions++; else if (r.mission === 'non éprouvée') { missionsNon++; if (!MUET) console.log('·  ' + nom + ' — la mission n\'a pas gardé le témoin au rechargement : son effacement n\'est pas éprouvé ici'); }
    if (!r.poses) { sansRien++; if (!MUET) console.log('·  ' + nom + ' — aucun champ à remplir'); return; }
    const ko = [...r.garde.map(k => 'le témoin reste dans ' + k), ...r.reste];
    if (ko.length) { refus++; console.log('❌ ' + nom + ' — ' + r.poses + ' réponse(s) posée(s), ' + r.avant.length + ' clé(s) écrite(s)'); ko.slice(0, 6).forEach(k => console.log('     ' + k)); if (ko.length > 6) console.log('     … et ' + (ko.length - 6) + ' autre(s)'); }
    else if (!MUET) console.log('✅ ' + nom + ' — ' + r.poses + ' réponse(s) posée(s), ' + r.avant.length + ' clé(s) écrite(s), rien ne reste' + (r.mission === 'éprouvée' ? ' (étoiles du mode mission comprises)' : ''));
  });
  await b.close();
  console.log('══ effacement : ' + jouees + ' page(s) jouée(s) · ' + (jouees - sansRien) + ' avec des réponses · ' + refus + ' qui garde(nt) quelque chose · mode mission éprouvé sur ' + missions + ' page(s)' + (missionsNon ? ', non éprouvé sur ' + missionsNon : '') + ' ══');
  process.exit(refus ? 1 : 0);
}
