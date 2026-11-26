// Banc des documents à lire en mode mission — joue chaque synthèse élève, chaque lexique et la carte des
// représentations, écran par écran, dans un navigateur d'élève à 390 px.
//
//   node _outils/mode_mission/banc_lecture.mjs                    → tous les documents à lire du dépôt
//   node _outils/mode_mission/banc_lecture.mjs <page.html> […]    → ces pages-là
//   node _outils/mode_mission/banc_lecture.mjs --detail           → la liste des écrans de chaque page
//
// Né le 25/11/2026 comme banc du « mode lecture » ; le 26/11/2026 (Pascal : « tout doit être en mode mission »), ces
// pages passent au mode mission (`mission.js`, gabarit des documents à lire) et le banc le suit, avec les mêmes refus :
//   L1  une erreur JavaScript ;
//   L2  une page qui ne s'ouvre pas en mode mission pour l'élève ;
//   L3  un écran vide ;
//   L4  un défilement de côté à 390 px ;
//   L5  du texte perdu : ce que montrent les écrans, mis bout à bout, n'est pas ce que montre la page complète ;
//   L6  « Suivant » qui n'avance pas, « Précédent » actif au premier écran, « Suivant » montré au dernier ;
//   L7  un lien de la page vers une ancre d'un autre écran (« ↑ La carte », « voir la partie 3 ») qui n'y mène pas,
//       ou une adresse « page.html#ancre » qui n'ouvre pas l'écran de l'ancre ;
//   L8  « 📄 Page complète » qui ne rend pas la page entière ; une page dont l'élève a choisi la page complète qui
//       s'ouvre quand même en mission ; « 🎮 Mode mission » qui n'y ramène pas ;
//   L9  une fiche papier qui diffère : imprimée en mission, la page sort entière ;
//   L10 autre chose dans le navigateur que le choix d'affichage, sur une page sans bouton d'effacement : sous la clé
//       « mission:<dossier>/<page> », rien que `v` et `on` (règle d'or n°322) ;
//   L11 un robot de test qui arrive en mission : les contrôles ne mesureraient plus la page complète.
// Une page d'un seul écran (un lexique en un seul tableau) est comptée, pas refusée.
//
// Sortie 0 : rien à refuser · 1 : au moins un refus · 2 : aucune page lue (règle d'or n°299). Ne dépend d'aucun réseau.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

let chromium;
try { ({ chromium } = await import('playwright')); } catch (e) { console.log('⛔ Playwright introuvable : rien n\'a été vérifié'); process.exit(2); }

const ICI = path.dirname(fileURLToPath(import.meta.url));
const RACINE = path.resolve(ICI, '..', '..');
const args = process.argv.slice(2), DETAIL = args.includes('--detail');
const donnees = args.filter((a) => !a.startsWith('--'));
const A_LIRE = /^(synthese|lexique|carte_des_representations)/i;
function pages(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.name.startsWith('.') || e.name === 'node_modules' || e.name.startsWith('_archive') || e.name === '_generation') continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) { if (dir === RACINE && !e.name.startsWith('theme-')) continue; pages(p, out); }
    else if (e.name.endsWith('.html') && A_LIRE.test(e.name) && fs.readFileSync(p, 'utf8').includes('<!-- mode-mission v1 : début')) out.push(p);
  }
  return out;
}
const liste = donnees.length ? donnees.map((p) => path.resolve(p)) : pages(RACINE).sort();
if (!liste.length) { console.log('⛔ aucun document à lire en mode mission : rien n\'a été vérifié'); process.exit(2); }

const ELEVE = () => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false, configurable: true }); };
const b = await chromium.launch();
const eleve = await b.newContext({ viewport: { width: 390, height: 844 } });
await eleve.addInitScript(ELEVE);
const robot = await b.newContext({ viewport: { width: 390, height: 844 } });
const cleDe = (F) => 'mission:' + path.basename(path.dirname(F)) + '/' + path.basename(F);
/* « La page s'en souvient au rechargement » ne se joue PAS en rechargeant juste après le clic : Chromium écrit
   `localStorage` en deux temps, et une page rechargée dans les millisecondes qui suivent une écriture ne la retrouve pas
   toujours (mesuré le 25/11/2026 : 3 marques perdues sur 150 rechargements immédiats). Le banc juge les deux moitiés
   séparément : le clic écrit le choix (lu dans la page) ; une page qui TROUVE ce choix à son ouverture s'ouvre complète. */
async function ouvreAvecChoix(url, cle) {
  const c = await b.newContext({ viewport: { width: 390, height: 844 } });
  await c.addInitScript((k) => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false, configurable: true }); try { localStorage.setItem(k, JSON.stringify({ v: 1, on: false })); } catch (e) {} }, cle);
  const q = await c.newPage(); await q.goto(url, { waitUntil: 'load' }); await q.waitForTimeout(150);
  const r = await q.evaluate(() => ({ ms: document.body.classList.contains('ms'), bouton: !!document.getElementById('btnMission') && document.getElementById('btnMission').getClientRects().length > 0 }));
  await c.close(); return r;
}
/* le texte que montre la page, hors de la barre, du pied et du bouton du mode : chaque nœud de texte visible compte sa
   longueur plus un (l'espace qui le sépare du suivant) — une mesure qui s'additionne d'un écran à l'autre */
const TEXTE = (racine) => {
  const vu = (e) => { for (let x = e; x && x.nodeType === 1; x = x.parentElement) { const c = getComputedStyle(x); if (c.display === 'none' || c.visibility === 'hidden') return false; } return true; };
  let n = 0;
  const parcourir = (r) => { const w = document.createTreeWalker(r, NodeFilter.SHOW_TEXT);
    for (let x = w.nextNode(); x; x = w.nextNode()) {
      const p = x.parentElement; if (!p || p.closest('script, style, template, noscript, .ms-seul, .ms-invite, .ms-pied, .ms-tete, .ms-revenir')) continue;
      const t = x.nodeValue.replace(/\s+/g, ' ').trim(); if (t && vu(p)) n += t.length + 1;
    } };
  if (racine === 'ecran') {
    /* l'écran seul : les enfants du conteneur du mode qui ne sont ni l'en-tête de la page, ni son titre, ni sa navigation */
    const P = document.querySelector('.ms-page') || document.body;
    [...P.children].forEach((x) => { if (!x.matches('.ms-seul, .ms-invite, .ms-entete, script, style, h1, nav, header')) parcourir(x); });
  } else parcourir(document.body);
  return n;
};
const ETAT = () => {
  const rail = [...document.querySelectorAll('#msRail [data-k]')], s = document.getElementById('msSuiv'), pr = document.getElementById('msPrec');
  return { ms: document.body.classList.contains('ms'), ici: rail.findIndex((r) => r.classList.contains('ici')), n: rail.length,
    titres: rail.map((r) => (r.getAttribute('aria-label') || '').replace(/^Écran \d+ sur \d+ : /, '').replace(/, vu$/, '')),
    large: document.documentElement.scrollWidth, ou: (document.getElementById('msOu') || {}).textContent || '',
    prec: !!pr && pr.disabled, suivMontre: !!s && !s.hidden };
};
/* ce que l'écran montré porte : du texte, ou une image (hors barre, pied, en-tête de la page) */
const MEDIAS = () => { const P = document.querySelector('.ms-page') || document.body; let m = 0;
  [...P.children].forEach((x) => { if (!x.matches('.ms-seul, .ms-invite, .ms-entete, script, style, h1, nav, header') && x.getClientRects().length) m += [...x.querySelectorAll('img, svg, canvas, table')].filter((y) => y.getClientRects().length).length; });
  return m; };

const refus = []; let lues = 0, seuls = [], ecransTotal = 0;
for (const F of liste) {
  const rel = path.relative(RACINE, F), url = pathToFileURL(F).href, CLE = cleDe(F);
  const faute = (code, m) => refus.push(`${code}  ${rel} — ${m}`);
  const p = await eleve.newPage(); const err = []; p.on('pageerror', (e) => err.push(e.message.slice(0, 140)));
  try {
    await p.goto(url, { waitUntil: 'load' }); await p.evaluate(() => { localStorage.clear(); sessionStorage.clear(); });
    await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(200);
    const e0 = await p.evaluate(ETAT); lues++;
    if (!e0.ms) { faute('L2', 'un élève n\'arrive pas en mode mission'); if (err.length) faute('L1', 'erreur JS : ' + err[0]); await p.close(); continue; }
    ecransTotal += e0.n; if (e0.n < 2) seuls.push(rel);
    if (!e0.prec) faute('L6', '« Précédent » est actif au premier écran');
    if (DETAIL) console.log('   ' + rel + '\n' + e0.titres.map((t, i) => `      ${i + 1}. ${t}`).join('\n'));
    const sansBouton = !(await p.$('#btnReset, #btnEffacer, #btn-effacer, #clear'));
    // la page complète, pour comparer : le texte de tout ce que le mode découpe
    await p.evaluate(() => document.getElementById('msQuitter').click()); await p.waitForTimeout(80);
    const pleine = await p.evaluate(TEXTE);
    const pleinePapier = await (async () => { await p.emulateMedia({ media: 'print' }); const t = await p.evaluate(TEXTE); await p.emulateMedia({ media: 'screen' }); return t; })();
    await p.evaluate(() => document.getElementById('btnMission').click()); await p.waitForTimeout(80);
    if (!(await p.evaluate(ETAT)).ms) faute('L8', '« 🎮 Mode mission » ne ramène pas au mode');
    await p.evaluate(() => document.querySelector('#msRail [data-k="0"]').click()); await p.waitForTimeout(60);
    // chaque écran, par « Suivant »
    let somme = 0;
    for (let j = 0; j < e0.n; j++) {
      const e = await p.evaluate(ETAT), q = { texte: await p.evaluate(TEXTE, 'ecran'), medias: await p.evaluate(MEDIAS) };
      if (e.ici !== j) { faute('L6', `écran ${j + 1} : « Suivant » n'avance pas (écran ${e.ici + 1})`); break; }
      if (!q.texte && !q.medias) faute('L3', `écran ${j + 1} (« ${e0.titres[j]} ») : vide`);
      if (e.large > 392) faute('L4', `écran ${j + 1} (« ${e0.titres[j]} ») : la page défile de côté (${e.large} px)`);
      if (!e.ou.includes(`${j + 1} sur ${e0.n}`)) faute('L6', `écran ${j + 1} : la barre dit « ${e.ou.slice(0, 50)} »`);
      const t = await p.evaluate(TEXTE);
      // la tête de la page (le titre, sa question, sa barre d'outils) : montrée entière au premier écran
      if (j === 0) somme += t; else somme += q.texte;
      if (j === e0.n - 1) { if (e.suivMontre) faute('L6', '« Suivant » est montré au dernier écran'); }
      else { await p.evaluate(() => window.scrollTo(0, document.body.scrollHeight)); await p.click('#msSuiv'); await p.waitForTimeout(60); }
    }
    if (Math.abs(somme - pleine) > Math.max(30, pleine * 0.01)) faute('L5', `les écrans bout à bout font ${somme} caractères, la page complète ${pleine}`);
    // imprimée en mission, la page sort entière
    await p.emulateMedia({ media: 'print' }); const papier = await p.evaluate(TEXTE); await p.emulateMedia({ media: 'screen' });
    if (Math.abs(papier - pleinePapier) > Math.max(30, pleinePapier * 0.01)) faute('L9', `imprimée en mission : ${papier} caractères, contre ${pleinePapier} en page complète`);
    // un lien vers une ancre d'un autre écran y mène (jusqu'à quatre liens par page)
    await p.evaluate(() => document.querySelector('#msRail [data-k="0"]').click()); await p.waitForTimeout(60);
    const liens = await p.evaluate(() => [...document.querySelectorAll('a[href^="#"]')].filter((a) => a.getAttribute('href').length > 1 && a.getClientRects().length)
      .map((a) => a.getAttribute('href')).filter((h, i, t) => t.indexOf(h) === i).filter((h) => { const c = document.getElementById(decodeURIComponent(h.slice(1))); return c && !c.getClientRects().length; }).slice(0, 4));
    for (const h of liens) {
      await p.evaluate(() => document.querySelector('#msRail [data-k="0"]').click()); await p.waitForTimeout(40);
      await p.evaluate((h) => { const a = [...document.querySelectorAll('a[href^="#"]')].find((x) => x.getAttribute('href') === h && x.getClientRects().length); if (a) a.click(); }, h); await p.waitForTimeout(80);
      const vu = await p.evaluate((h) => { const c = document.getElementById(decodeURIComponent(h.slice(1))); return !!c && c.getClientRects().length > 0; }, h);
      if (!vu) faute('L7', `le lien « ${h} » ne mène pas à son écran`);
    }
    // une adresse avec ancre ouvre l'écran de l'ancre (la séquence renvoie au lexique par « #seance-s2 »)
    if (e0.n > 1) {
      const ancre = await p.evaluate(() => { const P = document.querySelector('.ms-page') || document.body; const kids = [...P.querySelectorAll(':scope > *')].filter((x) => !x.matches('.ms-seul, .ms-invite, .ms-entete, script, style, h1, nav'));
        const der = kids[kids.length - 1]; const c = der && (der.id ? der : der.querySelector('[id]')); return c ? c.id : null; });
      if (ancre) {
        const c = await b.newContext({ viewport: { width: 390, height: 844 } }); await c.addInitScript(ELEVE);
        const q = await c.newPage(); await q.goto(url + '#' + encodeURIComponent(ancre), { waitUntil: 'load' }); await q.waitForTimeout(250);
        const ok = await q.evaluate((id) => { const c = document.getElementById(id); return document.body.classList.contains('ms') && !!c && c.getClientRects().length > 0; }, ancre);
        if (!ok) faute('L7', `« …#${ancre} » n'ouvre pas l'écran de cette ancre`);
        await c.close();
      }
    }
    // « Page complète » : tout revient ; le choix est noté — lui seul —, et une page qui le trouve s'ouvre complète
    await p.evaluate(() => document.getElementById('msQuitter').click()); await p.waitForTimeout(80);
    const e9 = await p.evaluate(ETAT), t9 = await p.evaluate(TEXTE);
    if (e9.ms || Math.abs(t9 - pleine) > 5) faute('L8', '« 📄 Page complète » ne rend pas la page entière');
    const memoire = await p.evaluate((k) => ({ cles: Object.keys(localStorage), m: (() => { try { return JSON.parse(localStorage.getItem(k) || 'null'); } catch (e) { return null; } })() }), CLE);
    if (!memoire.m || memoire.m.on !== false) faute('L8', `« 📄 Page complète » n'est pas noté sous « ${CLE} »`);
    if (sansBouton) {
      const autres = memoire.cles.filter((k) => k !== CLE && k !== 'anim-figee');
      const champs = memoire.m ? Object.keys(memoire.m).filter((c) => c !== 'v' && c !== 'on') : [];
      if (autres.length || champs.length) faute('L10', 'le navigateur garde autre chose que le choix d\'affichage : ' + autres.concat(champs.map((c) => CLE + '.' + c)).join(', '));
    }
    const rouverte = await ouvreAvecChoix(url, CLE);
    if (rouverte.ms) faute('L8', 'le choix « Page complète » trouvé à l\'ouverture, la page s\'ouvre quand même en mission');
    else if (!rouverte.bouton) faute('L8', 'ouverte en page complète, la page ne montre pas « 🎮 Mode mission »');
    await p.evaluate(() => localStorage.clear());
    if (err.length) faute('L1', 'erreur JS : ' + err[0]);
  } catch (e) { faute('L1', 'page non jouée : ' + String(e.message || e).slice(0, 160)); }
  await p.close();
  const r = await robot.newPage(); await r.goto(url, { waitUntil: 'load' }); await r.waitForTimeout(150);
  if (await r.evaluate(() => document.body.classList.contains('ms'))) faute('L11', 'un robot de test arrive en mission');
  await r.close();
}
await b.close();
for (const r of refus) console.log('✘ ' + r);
if (DETAIL) for (const s of seuls) console.log('   · un seul écran : ' + s);
console.log(`${lues} document(s) à lire joué(s) · ${ecransTotal} écrans · ${seuls.length} d'un seul écran · ${refus.length} refus`);
if (!lues) process.exit(2);
if (refus.length) process.exit(1);
console.log('✅ chaque document à lire se lit écran par écran en mission, sans rien perdre, se quitte, s\'imprime entier, et ne garde dans le navigateur que le choix d\'affichage');
