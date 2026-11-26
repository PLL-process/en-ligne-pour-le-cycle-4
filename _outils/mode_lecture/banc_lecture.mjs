// Banc du mode lecture — joue chaque page qui porte le bloc, partie par partie, dans un navigateur d'élève à 390 px.
//
//   node _outils/mode_lecture/banc_lecture.mjs                    → toutes les pages du dépôt qui portent le bloc
//   node _outils/mode_lecture/banc_lecture.mjs <page.html> […]    → ces pages-là
//   node _outils/mode_lecture/banc_lecture.mjs --detail           → la liste des parties de chaque page
//
// Il REFUSE, page par page :
//   L1  une erreur JavaScript ;
//   L2  une page qui ne s'ouvre pas en mode lecture pour l'élève (alors qu'elle a deux parties au moins) ;
//   L3  une partie vide, ou deux parties montrées ensemble ;
//   L4  un défilement de côté à 390 px ;
//   L5  du texte perdu : ce que montrent les parties, mises bout à bout, n'est pas ce que montre la page complète ;
//   L6  « Suivant » qui n'avance pas, « Précédent » actif à la première partie, « Suivant » actif à la dernière ;
//   L7  un lien de la page vers une ancre d'une autre partie (« ↑ La carte », « voir la partie 3 ») qui n'y mène pas,
//       ou une adresse « page.html#ancre » qui n'ouvre pas la partie de l'ancre ;
//   L8  « 📄 Page complète » qui ne rend pas la page entière ; une page qui trouve la marque « Page complète » à son
//       ouverture et s'ouvre quand même en mode lecture ; « 📖 Mode lecture » qui n'y ramène pas ;
//   L9  une fiche papier qui diffère : imprimée en mode lecture, la page sort entière ;
//   L10 autre chose dans le navigateur que le choix d'affichage : sans choix, le mode n'écrit rien ; « 📄 Page
//       complète » laisse une marque (« lecture:<page> » = 0), « 📖 Mode lecture » la retire ;
//   L11 un robot de test qui arrive en mode lecture : les contrôles ne mesureraient plus la page complète.
// Une page d'une seule partie n'a rien à découper : elle s'ouvre telle quelle, sans bouton. Elle est comptée, pas refusée.
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
function pages(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.name.startsWith('.') || e.name === 'node_modules' || e.name.startsWith('_archive')) continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) { if (dir === RACINE && !e.name.startsWith('theme-')) continue; pages(p, out); }
    else if (e.name.endsWith('.html') && fs.readFileSync(p, 'utf8').includes('<!-- mode-lecture v1 : début')) out.push(p);
  }
  return out;
}
const liste = donnees.length ? donnees.map((p) => path.resolve(p)) : pages(RACINE).sort();
if (!liste.length) { console.log('⛔ aucune page à mode lecture : rien n\'a été vérifié'); process.exit(2); }

const b = await chromium.launch();
const eleve = await b.newContext({ viewport: { width: 390, height: 844 } });
await eleve.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false, configurable: true }); });
const robot = await b.newContext({ viewport: { width: 390, height: 844 } });
/* « La page s'en souvient au rechargement » ne se joue PAS en rechargeant juste après le clic. Chromium écrit
   `localStorage` en deux temps — la page d'abord, le navigateur ensuite — et une page rechargée dans les millisecondes
   qui suivent une écriture ne la retrouve pas toujours (mesuré, machine chargée : 3 marques perdues sur 150
   rechargements immédiats, et autant d'effacements non vus ; un second onglet « témoin » ne suffit pas, il lit parfois
   la même mémoire que la page). Aucun élève ne recharge en 5 ms ; un banc, si, et il refusait une page sur cent, jamais
   la même. Le banc juge donc les deux moitiés séparément, chacune sans course : le clic écrit la marque (lue dans la
   page) ; une page qui TROUVE la marque à son ouverture s'ouvre complète (la marque est posée avant tout script). */
async function ouvreAvecMarque(url, cle) {
  const c = await b.newContext({ viewport: { width: 390, height: 844 } });
  await c.addInitScript((k) => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false, configurable: true }); try { localStorage.setItem(k, '0'); } catch (e) {} }, cle);
  const q = await c.newPage(); await q.goto(url, { waitUntil: 'load' }); await q.waitForTimeout(150);
  const r = await q.evaluate(() => ({ ml: document.body.classList.contains('ml'), bouton: !!document.getElementById('btnLecture') && document.getElementById('btnLecture').getClientRects().length > 0 }));
  await c.close(); return r;
}
/* le texte que montre la page, hors de la barre et du pied du mode */
const TEXTE = () => {
  const vu = (e) => { for (let x = e; x && x.nodeType === 1; x = x.parentElement) { const c = getComputedStyle(x); if (c.display === 'none' || c.visibility === 'hidden') return false; } return true; };
  const o = []; const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let n = w.nextNode(); n; n = w.nextNode()) {
    const p = n.parentElement; if (!p || p.closest('script, style, template, noscript, .ml-seul, .ml-invite')) continue;
    const t = n.nodeValue.replace(/\s+/g, ' ').trim(); if (t && vu(p)) o.push(t);
  }
  return o.join(' ').length;
};
const ETAT = () => {
  const L = document.documentElement._lecture, P = [...document.querySelectorAll('.ml-cache')];
  const montrees = new Set(); let vide = true;
  document.querySelectorAll('[class]').forEach(() => {});
  return { ml: document.body.classList.contains('ml'), ici: L ? L.ici() : -1, n: L ? L.ecrans().length : 0, caches: P.length,
    large: document.documentElement.scrollWidth, ou: (document.getElementById('mlOu') || {}).textContent || '',
    prec: (document.getElementById('mlPrec') || {}).disabled, suiv: (document.getElementById('mlSuiv') || {}).disabled };
};
/* ce que la partie montrée porte : du texte, ou une image */
const PARTIE = () => {
  const ici = document.documentElement._lecture.ici();
  const rail = [...document.querySelectorAll('#mlRail [data-k]')];
  const tete = document.querySelector('.ml-tete');
  // les nœuds de la partie : ceux qui suivent la barre, non cachés, jusqu'au pied
  let texte = 0, medias = 0, n = 0;
  for (let x = tete.nextElementSibling; x; x = x.nextElementSibling) {
    if (x.classList.contains('ml-cache') || x.classList.contains('ml-seul') || /^(SCRIPT|STYLE)$/.test(x.tagName)) continue;
    n++; texte += (x.innerText || '').replace(/\s+/g, ' ').trim().length; medias += x.querySelectorAll('img, svg, canvas, table').length;
  }
  return { ici, marque: rail.findIndex((r) => r.classList.contains('ici')), texte, medias, n };
};

const refus = []; let lues = 0, seules = [], parties = 0;
for (const F of liste) {
  const rel = path.relative(RACINE, F), url = pathToFileURL(F).href;
  const faute = (code, m) => refus.push(`${code}  ${rel} — ${m}`);
  const p = await eleve.newPage(); const err = []; p.on('pageerror', (e) => err.push(e.message.slice(0, 140)));
  try {
    await p.goto(url, { waitUntil: 'load' }); await p.evaluate(() => { localStorage.clear(); sessionStorage.clear(); });
    await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(200);
    const e0 = await p.evaluate(ETAT);
    const MARQUES = () => Object.keys(localStorage).filter((c) => /^lecture:/.test(c)).map((c) => c + '=' + localStorage.getItem(c));
    if ((await p.evaluate(MARQUES)).length) faute('L10', 'le mode écrit dans le navigateur avant tout choix de l\'élève : ' + (await p.evaluate(MARQUES)).join(', '));
    if (e0.n < 2) { seules.push(rel); lues++; if (e0.ml) faute('L2', 'mode lecture allumé sur une page d\'une seule partie'); if (err.length) faute('L1', 'erreur JS : ' + err[0]); await p.close(); continue; }
    lues++; parties += e0.n;
    if (!e0.ml) faute('L2', 'un élève n\'arrive pas en mode lecture');
    if (!e0.prec) faute('L6', '« Précédent » est actif à la première partie');
    const titres = await p.evaluate(() => document.documentElement._lecture.ecrans());
    if (DETAIL) console.log('   ' + rel + '\n' + titres.map((t, i) => `      ${i + 1}. ${t}`).join('\n'));
    // la page complète, pour comparer : le texte de tout ce que le mode découpe
    await p.evaluate(() => document.getElementById('mlQuitter').click()); await p.waitForTimeout(80);
    const pleine = await p.evaluate(TEXTE);
    const pleinePapier = await (async () => { await p.emulateMedia({ media: 'print' }); const t = await p.evaluate(TEXTE); await p.emulateMedia({ media: 'screen' }); return t; })();
    await p.evaluate(() => document.getElementById('btnLecture').click()); await p.waitForTimeout(80);
    if (!(await p.evaluate(ETAT)).ml) faute('L8', '« 📖 Mode lecture » ne ramène pas au mode');
    if ((await p.evaluate(MARQUES)).length) faute('L10', 'revenu en mode lecture, la marque « Page complète » reste : ' + (await p.evaluate(MARQUES)).join(', '));
    // chaque partie, par « Suivant »
    let somme = 0, tete = null;
    for (let j = 0; j < e0.n; j++) {
      const e = await p.evaluate(ETAT), q = await p.evaluate(PARTIE);
      if (e.ici !== j || q.marque !== j) { faute('L6', `partie ${j + 1} : « Suivant » n'avance pas (écran ${e.ici + 1})`); break; }
      if (!q.texte && !q.medias) faute('L3', `partie ${j + 1} (« ${titres[j]} ») : vide`);
      if (e.large > 392) faute('L4', `partie ${j + 1} (« ${titres[j]} ») : la page défile de côté (${e.large} px)`);
      if (!e.ou.includes(`${j + 1} sur ${e0.n}`)) faute('L6', `partie ${j + 1} : la barre dit « ${e.ou.slice(0, 40)} »`);
      const t = await p.evaluate(TEXTE);
      // la tête de la page (le titre, sa question, sa barre d'outils) : montrée entière à la première partie
      if (j === 0) { tete = t - q.texte; somme += t; } else somme += q.texte;
      if (j === e0.n - 1) { if (!e.suiv) faute('L6', '« Suivant » est actif à la dernière partie'); }
      else { await p.evaluate(() => window.scrollTo(0, document.body.scrollHeight)); await p.click('#mlSuiv'); await p.waitForTimeout(60); }
    }
    // rien de perdu : la tête et les parties, bout à bout, font la page (à quelques caractères près : des espaces)
    if (Math.abs(somme - pleine) > Math.max(30, pleine * 0.01)) faute('L5', `les parties bout à bout font ${somme} caractères, la page complète ${pleine}`);
    // imprimée en mode lecture, la page sort entière
    await p.emulateMedia({ media: 'print' }); const papier = await p.evaluate(TEXTE); await p.emulateMedia({ media: 'screen' });
    if (Math.abs(papier - pleinePapier) > Math.max(30, pleinePapier * 0.01)) faute('L9', `imprimée en mode lecture : ${papier} caractères, contre ${pleinePapier} en page complète`);
    // un lien vers une ancre d'une autre partie y mène (jusqu'à quatre liens par page)
    await p.evaluate(() => document.querySelector('#mlRail [data-k="0"]').click()); await p.waitForTimeout(60);
    const liens = await p.evaluate(() => [...document.querySelectorAll('a[href^="#"]')].filter((a) => a.getAttribute('href').length > 1 && a.getClientRects().length)
      .map((a) => a.getAttribute('href')).filter((h, i, t) => t.indexOf(h) === i).filter((h) => { const c = document.getElementById(decodeURIComponent(h.slice(1))); return c && !c.getClientRects().length; }).slice(0, 4));
    for (const h of liens) {
      await p.evaluate(() => document.querySelector('#mlRail [data-k="0"]').click()); await p.waitForTimeout(40);
      await p.evaluate((h) => { const a = [...document.querySelectorAll('a[href^="#"]')].find((x) => x.getAttribute('href') === h && x.getClientRects().length); if (a) a.click(); }, h); await p.waitForTimeout(80);
      const vu = await p.evaluate((h) => { const c = document.getElementById(decodeURIComponent(h.slice(1))); return !!c && c.getClientRects().length > 0; }, h);
      if (!vu) faute('L7', `le lien « ${h} » ne mène pas à sa partie`);
    }
    // une adresse avec ancre ouvre la partie de l'ancre (la séquence renvoie au lexique par « #seance-s2 »)
    const ancre = await p.evaluate(() => { const t = document.querySelector('.ml-tete'); let der = null; for (let x = t.nextElementSibling; x; x = x.nextElementSibling) if (!x.classList.contains('ml-seul') && !/^(SCRIPT|STYLE)$/.test(x.tagName)) der = x;
      const c = der && (der.id ? der : der.querySelector('[id]')); return c ? c.id : null; });
    if (ancre) {
      // dans un navigateur neuf : la marque « Page complète » posée puis retirée plus haut n'y est pour rien
      const c = await b.newContext({ viewport: { width: 390, height: 844 } });
      await c.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false, configurable: true }); });
      const q = await c.newPage(); await q.goto(url + '#' + encodeURIComponent(ancre), { waitUntil: 'load' }); await q.waitForTimeout(250);
      const ok = await q.evaluate((id) => { const c = document.getElementById(id); return document.body.classList.contains('ml') && !!c && c.getClientRects().length > 0; }, ancre);
      if (!ok) faute('L7', `« …#${ancre} » n'ouvre pas la partie de cette ancre`);
      await c.close();
    }
    // « Page complète » : tout revient, la marque est écrite — elle seule —, et une page qui la trouve s'ouvre complète
    await p.evaluate(() => document.getElementById('mlQuitter').click()); await p.waitForTimeout(80);
    const e9 = await p.evaluate(ETAT), t9 = await p.evaluate(TEXTE);
    if (e9.ml || Math.abs(t9 - pleine) > 5) faute('L8', '« 📄 Page complète » ne rend pas la page entière');
    // le choix est noté dans le navigateur — lui seul —, et la page s'en souvient au rechargement
    const nom = decodeURIComponent(path.basename(F)), marques = await p.evaluate(MARQUES);
    if (marques.length !== 1 || marques[0] !== 'lecture:' + nom + '=0') faute('L10', '« 📄 Page complète » : attendu la seule marque « lecture:' + nom + '=0 », lu « ' + marques.join(', ') + ' »');
    const rouverte = await ouvreAvecMarque(url, 'lecture:' + nom);
    if (rouverte.ml) faute('L8', 'la marque « Page complète » trouvée à l\'ouverture, la page s\'ouvre quand même en mode lecture');
    else if (!rouverte.bouton) faute('L8', 'ouverte en page complète, la page ne montre pas « 📖 Mode lecture »');
    await p.evaluate(() => localStorage.clear());
    if (err.length) faute('L1', 'erreur JS : ' + err[0]);
  } catch (e) { faute('L1', 'page non jouée : ' + String(e.message || e).slice(0, 160)); }
  await p.close();
  const r = await robot.newPage(); await r.goto(url, { waitUntil: 'load' }); await r.waitForTimeout(150);
  if (await r.evaluate(() => document.body.classList.contains('ml'))) faute('L11', 'un robot de test arrive en mode lecture');
  await r.close();
}
await b.close();
for (const r of refus) console.log('✘ ' + r);
if (DETAIL) for (const s of seules) console.log('   · une seule partie : ' + s);
console.log(`${lues} page(s) jouée(s) · ${lues - seules.length} en mode lecture, ${parties} parties · ${seules.length} d'une seule partie (ouvertes telles quelles) · ${refus.length} refus`);
if (!lues) process.exit(2);
if (refus.length) process.exit(1);
console.log('✅ chaque page à mode lecture se lit partie par partie, sans rien perdre, se quitte, s\'imprime entière, et ne garde dans le navigateur que le choix d\'affichage');
