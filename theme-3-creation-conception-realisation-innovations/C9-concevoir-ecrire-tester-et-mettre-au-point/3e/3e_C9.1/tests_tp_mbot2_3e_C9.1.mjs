// tests_tp_mbot2_3e_C9.1.mjs — le banc du TP « Programmer le robot mBot2 en Python » (refonte des 26 et 27/11/2026).
//
//   node tests_tp_mbot2_3e_C9.1.mjs            (depuis le dossier du lot, ou avec son chemin)
//
// Il rejoue, dans Chromium, chaque constat de la relecture du 26/11/2026 — pour qu'aucun ne revienne :
//   · une étiquette se déplace au doigt, à la souris et au clavier (avant : à la souris seulement) ;
//   · « while true: » est refusé, « while True: » accepté ; les espaces et le type de guillemets ne comptent pas
//     (avant : « while true: » était la réponse enregistrée, et « for x in [2, 4, 6]: » était refusé) ;
//   · une correction ouverte avant la réussite coûte les points ; une réponse changée retire la réussite ;
//   · les points : 55 pour un sans-faute, 0 pour une page vide ; une vérification à vide n'est pas un essai ;
//   · tout se retrouve après un rechargement, et « Effacer » (deux clics) n'en laisse rien ;
//   · le robot simulé exécute le programme construit, et ne prête aucun de ses noms au programme de l'élève ;
//   · chaque exemple de code d'une consigne, et chaque ligne attendue, est du Python que Python accepte ;
//   · B1 à B20 (27/11/2026) : la page EXÉCUTE le programme avec la ligne de l'élève — chaque ligne du corrigé fait
//     afficher ce que la consigne annonce ; une autre écriture qui fait le même travail est acceptée ; une ligne
//     qui ne convient qu'aux nombres du programme montré est refusée au second essai ; sans moteur Python, la page
//     le dit et ne compte pas l'essai ;
//   · 390 px sans défilement de côté, aucune erreur JavaScript, une fiche imprimée de deux pages au plus.
// Sortie : 0 tout passe · 1 un point échoue · 2 le banc n'a rien pu jouer (règle d'or n°299).
import { chromium } from 'playwright';
import { spawnSync } from 'node:child_process';
import path from 'node:path';
import fs from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const PAGE = path.join(ICI, 'tp_mbot2_python.html');
if (!fs.existsSync(PAGE)) { console.log('⛔ EN PANNE : page introuvable — ' + PAGE); process.exit(2); }
const URL_PAGE = pathToFileURL(PAGE).href;

let passes = 0, echecs = 0;
const point = (nom, ok, vu) => { if (ok) passes++; else echecs++; console.log((ok ? '  ✔ ' : '  ✘ ') + nom + (ok || vu === undefined ? '' : '\n      vu : ' + String(vu).slice(0, 300))); };
const SOLUTIONS = { 1: ['m1t1', 'm1t3', 'm1t2', 'm1t4'], 2: ['m2t1', 'm2t2', 'm2t3', 'm2t4'], 3: ['m3t1', 'm3t2', 'm3t3', 'm3t4'], 4: ['m4t1', 'm4t2', 'm4t3', 'm4t4'], 5: ['m5t1', 'm5t2', 'm5t3'], 6: ['m6t1', 'm6t2'] };
const A7 = ['a7t1', 'a7t2', 'a7t3', 'a7t4', 'a7t5', 'a7t6', 'a7t7', 'a7t8', 'a7t9', 'a7t10'];
const LIGNES = { b1: 'while True:', b2: 'time.sleep(0.05)', b3: 'for i in range(5):', b4: 'break', b5: 'continue', b6: 'for i in range(10):', b7: 'for i in range(1, 6):', b8: 'while d >= 15:', b9: "while not cyberpi.controller.is_press('a'):", b10: 'print(i)', b11: 's = 0', b12: 's = s + i', b13: 'for x in [2, 4, 6]:', b14: 'for c in "ABC":', b15: 'while d is None:', b16: "while not (cyberpi.controller.is_press('a') or cyberpi.controller.is_press('b')):", b17: 'for i in [3, 2, 1]:', b18: 'for i in range(0, 9, 2):', b19: 'for i, v in enumerate(sons):', b20: 'for _ in range(3):' };

let nav;
try { nav = await chromium.launch(); } catch (e) { console.log('⛔ EN PANNE : Chromium ne démarre pas — ' + e.message); process.exit(2); }
const ouvrir = async (opts = {}) => {
  const ctx = await nav.newContext({ viewport: { width: 1280, height: 900 }, ...opts }); const p = await ctx.newPage();
  const erreurs = []; p.on('pageerror', e => erreurs.push(e.message)); p.on('console', m => { if (m.type() === 'error') erreurs.push(m.text()); });
  await p.goto(URL_PAGE, { waitUntil: 'load' }); await p.waitForTimeout(500);
  return { ctx, p, erreurs };
};
const ordre = (p, z) => p.evaluate(z => [...document.querySelectorAll('#prog' + z + ' .token')].map(t => t.id), z);
const retour = (p, cle) => p.innerText('#fb-' + cle);
// une ligne B qui n'est pas celle du corrigé est jugée en exécutant le programme : on attend le verdict
const verifier = async (p, cle) => { await p.click('[data-verifier="' + cle + '"]'); if (/^b\d+$/.test(cle)) await p.waitForFunction(c => !/exécute le programme/.test(document.getElementById('fb-' + c).textContent), cle, { timeout: 40000 }); };
const poserTout = async (p, ids) => { for (const id of ids) await p.click('#' + id); };

try {
  // ───────────── 1. la page, telle qu'elle se charge ─────────────
  console.log('1. La page');
  let { ctx, p, erreurs } = await ouvrir();
  point('20 lignes de boucle, 35 exercices, 55 points', await p.locator('section.q-boucle').count() === 20 && await p.evaluate(() => ITEMS.length) === 35 && await p.innerText('#total') === '55');
  point('aucune réserve ne s’ouvre dans l’ordre de la solution', await p.evaluate(S => Object.keys(S).every(z => [...document.querySelectorAll('#bank' + z + ' .token')].map(t => t.id).join() !== S[z].join()), SOLUTIONS));
  point('chaque étiquette est un bouton atteignable au clavier', await p.evaluate(() => [...document.querySelectorAll('.token')].every(t => t.tagName === 'BUTTON' && t.tabIndex >= 0)));
  point('chaque exercice a ses deux aides, puis sa correction', await p.evaluate(() => ITEMS.every(it => { const c = document.querySelector('details.correction[data-item="' + it.cle + '"]'); const s = c && c.closest('section'); return !!s && !!s.querySelector('details.aide1') && !!s.querySelector('details.aide2') && (s.querySelector('details.aide1').compareDocumentPosition(c) & 4) === 4; })));

  // ───────────── 2. les étiquettes : souris, clavier ─────────────
  console.log('2. Les étiquettes');
  await p.locator('#m1').scrollIntoViewIfNeeded();
  const glisser = async (src, dst, dy = 0) => { const s = await p.locator(src).boundingBox(), d = await p.locator(dst).boundingBox(); await p.mouse.move(s.x + 10, s.y + 10); await p.mouse.down(); await p.mouse.move(s.x + 40, s.y + 30, { steps: 3 }); await p.mouse.move(d.x + d.width / 2, d.y + d.height / 2 + dy, { steps: 6 }); await p.mouse.up(); await p.waitForTimeout(60); };
  await glisser('#m1t2', '#prog1'); await glisser('#m1t1', '#prog1', -40);
  point('glisser à la souris, et s’insérer devant une étiquette', (await ordre(p, 1)).join() === 'm1t1,m1t2', await ordre(p, 1));
  await p.click('#m1t3'); await p.click('#m1t4');
  point('toucher ajoute à la suite', (await ordre(p, 1)).join() === 'm1t1,m1t2,m1t3,m1t4', await ordre(p, 1));
  await verifier(p, 'qd1');
  point('A1 dans un mauvais ordre : refusé, et le retour compte les lignes en place', /Pas encore/.test(await retour(p, 'qd1')) && /2 lignes sur 4/.test(await retour(p, 'qd1')), await retour(p, 'qd1'));
  await p.focus('#m1t3'); await p.keyboard.press('ArrowUp');
  point('au clavier, ↑ monte l’étiquette d’une ligne', (await ordre(p, 1)).join() === SOLUTIONS[1].join(), await ordre(p, 1));
  await verifier(p, 'qd1');
  point('A1 juste au 2e essai : 2 points sur 2', /Juste/.test(await retour(p, 'qd1')) && await p.innerText('#score') === '2', await retour(p, 'qd1'));
  point('après la réussite, la correction s’ouvre', await p.evaluate(() => document.querySelector('details.correction[data-item="qd1"]').open));
  await p.click('#m1t4');
  point('une réponse changée retire la réussite', await p.innerText('#score') === '0' && /changé/.test(await retour(p, 'qd1')), await retour(p, 'qd1'));
  await p.click('#m6t1'); await p.click('#m6t3'); await verifier(p, 'qd6');
  point('A6 : l’étiquette en trop (tourner à droite) est refusée', /Pas encore/.test(await retour(p, 'qd6')), await retour(p, 'qd6'));
  await p.click('#m2 details.correction > summary'); await poserTout(p, SOLUTIONS[2]); await verifier(p, 'qd2');
  point('correction ouverte avant la réussite : 0 point, et c’est dit', /0 point/.test(await retour(p, 'qd2')) && await p.evaluate(() => E.items.qd2.pts) === 0, await retour(p, 'qd2'));
  await verifier(p, 'q4');
  point('vérifier à vide n’est pas un essai', await p.evaluate(() => !E.items.q4), await retour(p, 'q4'));
  point('aucune erreur JavaScript', erreurs.length === 0, erreurs.join(' | '));
  await ctx.close();

  // ───────────── 3. les lignes de Python ─────────────
  console.log('3. Les lignes de Python écrites par l’élève');
  ({ ctx, p, erreurs } = await ouvrir());
  // [exercice, ligne, attendu, ce que le retour doit dire (facultatif)]
  const cas = [
    // la ligne du corrigé, aux espaces et aux guillemets près
    ['b1', 'while True:', true], ['b1', 'while True :', true], ['b13', 'for x in [2, 4, 6]:', true], ['b13', 'for x in [2,4,6]:', true], ['b11', 's=0', true], ['b12', 's += i', true],
    ['b3', 'for k in range(5):', true], ['b9', 'while not cyberpi.controller.is_press("a"):', true], ['b2', 'time.sleep(.05)', true], ['b14', "for c in 'ABC':", true], ['b18', 'for i in range(0, 10, 2):', true],
    // une autre écriture, qui fait le même travail : acceptée, et la page le dit
    ['b1', 'while 1:', true, /même travail/], ['b3', 'for k in range(1, 6):', true, /même travail/], ['b8', 'while d > 14:', true, /même travail/], ['b12', 's = i + s', true],
    ['b9', "while cyberpi.controller.is_press('a') == False:", true, /même travail/], ['b15', 'while not d:', true, /même travail/], ['b18', 'for i in [0, 2, 4, 6, 8]:', true, /même travail/],
    ['b16', 'while not cyberpi.controller.is_press("a") and not cyberpi.controller.is_press("b"):', true, /même travail/],
    // une ligne fausse : refusée, et le retour montre ce que fait le programme avec elle
    ['b1', 'while true:', false, /majuscules/], ['b3', 'for for in range(5):', false, /Python arrête/], ['b3', 'for i in range(4):', false, /Bip\nBip\nBip\nBip\n[^B]/], ['b3', 'while True:', false, /ne s’arrête plus/],
    ['b4', 'continue', false, /4\n5\nfin/], ['b5', 'break', false, /2\nfin/], ['b6', 'for i in range(9):', false, /7\n8\n/], ['b6', 'for k in range(10):', false, /se sert de i/],
    ['b9', 'while not cyberpi.controller.is_press(a):', false, /Python arrête/], ['b9', 'while not cyberpi.controller.is_press("b"):', false, /Cas 1 sur 2/], ['b2', 'time.sleep(50)', false, /pause de 50 s/], ['b2', 'sleep(0.05)', false, /sleep/],
    ['b20', 'for i in range(3)', false, /deux-points/], ['b14', "for lettre in 'ABC':", false, /se sert de c/], ['b10', 'print("i")', false, /i\ni\ni/], ['b18', 'for i in range(0, 8, 2):', false, /4\n6\n[^8]/], ['b15', 'while d is none:', false, /majuscules/],
    ['b12', 's = i', false, /Somme : 4/], ['b17', 'for i in range(3):', false, /0\n1\n2\nDépart/], ['b19', 'for i, v in sons:', false, /Python arrête/], ['b16', 'while not cyberpi.controller.is_press("a"):', false, /Cas 2 sur 3[\s\S]*pousse le bouton B \(ton programme attend une autre touche\)/],
    // une ligne qui ne convient qu'aux nombres du programme montré : refusée au second essai
    ['b1', 'while tours < 5:', false, /Cas 2 sur 2/], ['b1', 'for i in range(5):', false, /Cas 2 sur 2/], ['b8', 'for d in [18, 17, 16, 15]:', false, /Cas 2 sur 2/], ['b12', 's = 10', false, /Cas 2 sur 2/], ['b15', 'while essais < 3:', false, /Cas 2 sur 2/]];
  for (const [cle, v, attendu, dit] of cas) { await p.fill('#' + cle, v); await verifier(p, cle); const r = await retour(p, cle); point('« ' + v + ' » ' + (attendu ? 'accepté' : 'refusé') + (dit ? ' — ' + dit.source.replace(/\\n/g, ' ') : ''), /Juste/.test(r) === attendu && (!dit || dit.test(r)), r); }
  // le corrigé de chaque exercice, joué à chaque essai : le programme affiche ce que la consigne annonce
  const joues = await p.evaluate(async () => { const ko = []; let n = 0; for (const it of blanksData) { const essais = essaisDe(it); for (let k = 0; k < essais.length; k++) for (const a of it.a) { n++; const r = await jouerLigne(it, essais[k], enClair(it, a)); if (r.erreur || r.arret || (!it.robot && sortieNette(r) !== essais[k].affiche) || (it.robot && !essais[k].faut)) ko.push(it.id + ' essai ' + (k + 1) + ' « ' + a + ' » → ' + JSON.stringify(sortieNette(r)).slice(0, 80)); } } return { n, ko }; });
  point(joues.n + ' lignes du corrigé jouées : chaque programme affiche ce que sa consigne annonce', joues.ko.length === 0 && joues.n >= 30, joues.ko.join(' | '));
  point('chaque exercice montre son programme troué, ce qu’il doit afficher ou faire, et « À savoir »', await p.evaluate(() => [...document.querySelectorAll('section.q-boucle')].every(s => /______/.test(s.querySelector('.ligne-doc pre').textContent) && !!s.querySelector('.ligne-doc .console-lue, .ligne-doc .ligne-essais, .ligne-doc .ligne-faut-robot') && !!s.querySelector('.savoir'))));
  point('un exemple de code peut se couper après « ( » (téléphone), et son texte ne change pas', await p.evaluate(() => { const pre = document.querySelector('#carte-b16 .savoir pre'); return pre.querySelectorAll('wbr').length >= 3 && pre.textContent.includes('cyberpi.controller.is_press("left")'); }));
  point('aucune consigne ne contient la ligne attendue', await p.evaluate(() => blanksData.every(it => { const s = document.getElementById('carte-' + it.id), vu = [...s.children].filter(e => e.tagName !== 'DETAILS').map(e => e.textContent).join('\n').replace(/\s+/g, ''); return it.a.every(a => a.length < 9 || !vu.includes(enClair(it, a).replace(/\s+/g, '').replace(/'/g, '"'))); })));
  // sans moteur Python : la page le dit, et l'essai n'est pas compté
  const essaisAvant = await p.evaluate(() => (E.items.b7 || { essais: 0 }).essais);
  await p.evaluate(() => { window.__moteur = window.EditeurPython; window.EditeurPython = undefined; });
  await p.fill('#b7', 'for i in [1, 2, 3, 4, 5]:'); await verifier(p, 'b7');
  point('sans moteur Python, une autre écriture n’est ni validée ni comptée comme une erreur', /n’a pas pu exécuter/.test(await retour(p, 'b7')) && /pas compté/.test(await retour(p, 'b7')) && await p.evaluate(() => (E.items.b7 || { essais: 0 }).essais) === essaisAvant, await retour(p, 'b7'));
  await p.fill('#b7', 'for i in range(1, 6):'); await verifier(p, 'b7');
  point('… et la ligne du corrigé reste reconnue', /Juste/.test(await retour(p, 'b7')), await retour(p, 'b7'));
  await p.evaluate(() => { window.EditeurPython = window.__moteur; });
  await p.fill('#b1', 'while true:'); await verifier(p, 'b1');
  point('« true » sans majuscule : le retour dit de regarder les majuscules', /majuscules/.test(await retour(p, 'b1')), await retour(p, 'b1'));
  // chaque exemple de code et chaque ligne attendue, donnés à Python
  const listings = await p.evaluate(() => [...document.querySelectorAll('section.q-boucle')].flatMap(s => [...s.querySelectorAll('pre')].map(x => ({ ou: s.id + (x.closest('details') ? ' (' + x.closest('details').className + ')' : ' (consigne)'), code: x.textContent }))));
  const attendues = await p.evaluate(() => blanksData.flatMap(it => it.a.map(a => ({ ou: it.id + ' (ligne attendue)', code: a.replace('@', it.nom || 'i') }))));
  const aJuger = listings.filter(l => !/…|\.\.\.|____|Indice :/.test(l.code)).concat(attendues);
  const py = spawnSync('python3', ['-c', 'import ast, json, sys, textwrap\nko = []\nfor l in json.load(sys.stdin):\n    c = textwrap.dedent(l["code"].strip("\\n")).rstrip()\n    if c.endswith(":"): c += "\\n    pass"\n    if c in ("break", "continue"): c = "while True:\\n    " + c\n    try: ast.parse(c)\n    except SyntaxError as e: ko.append(l["ou"] + " : " + e.msg + " — " + l["code"].strip()[:60])\nprint(json.dumps(ko))'], { input: JSON.stringify(aJuger), encoding: 'utf8' });
  if (py.status !== 0) { console.log('  ⚠ python3 introuvable : les listings ne sont pas jugés par Python (' + (py.stderr || '').trim().split('\n').pop() + ')'); }
  else { const ko = JSON.parse(py.stdout); point(aJuger.length + ' exemples et lignes attendues : Python les accepte tous', ko.length === 0 && aJuger.length >= 40, ko.join(' | ') || aJuger.length + ' lus'); }
  await ctx.close();

  // ───────────── 4. les points ─────────────
  console.log('4. Les points');
  ({ ctx, p, erreurs } = await ouvrir());
  point('page vide : 0 sur 55, 0,0 sur 20, 35 exercices pas encore faits', await p.innerText('#score') === '0' && await p.innerText('#note20') === '0,0' && await p.innerText('#nbRestants') === '35');
  for (const z of Object.keys(SOLUTIONS)) { await poserTout(p, SOLUTIONS[z]); await verifier(p, 'qd' + z); }
  await poserTout(p, A7); await verifier(p, 'A7');
  for (const [cle, v] of Object.entries(LIGNES)) { await p.fill('#' + cle, v); await verifier(p, cle); }
  await p.fill('#q2a', '#FFFF00'); await verifier(p, 'q2a'); await p.fill('#q2b', '00ffff'); await verifier(p, 'q2b'); await p.fill('#q2c', '#FF00FF'); await verifier(p, 'q2c');
  await p.check('input[name="q1"][value="b"]'); await verifier(p, 'q1'); await p.check('input[name="q3"][value="a"]'); await verifier(p, 'q3');
  await p.fill('#q4', '2'); await verifier(p, 'q4'); await p.fill('#q5a', '50'); await p.fill('#q5b', '1'); await verifier(p, 'q5');
  for (const v of ['A', 'B', 'C']) await p.check('input[name="q9"][value="' + v + '"]'); await verifier(p, 'q9');
  point('sans-faute au premier essai : 55 sur 55, 20,0 sur 20', await p.innerText('#score') === '55' && await p.innerText('#note20') === '20,0' && await p.innerText('#nbReussis') === '35', await p.innerText('#identite'));
  // une question à choix se devine : tous les points, la moitié, puis rien — comptés sur une page neuve
  { const neuve = await ouvrir(), q = neuve.p;
    await q.check('input[name="q1"][value="a"]'); await verifier(q, 'q1'); await q.check('input[name="q1"][value="b"]'); await verifier(q, 'q1');
    point('question à choix juste au 2e essai : la moitié des points', await q.evaluate(() => E.items.q1.pts) === 1, await retour(q, 'q1'));
    await q.check('input[name="q1"][value="c"]'); await verifier(q, 'q1'); await q.check('input[name="q1"][value="b"]'); await verifier(q, 'q1');
    point('… et rien à partir du 3e', await q.evaluate(() => E.items.q1.pts) === 0, await retour(q, 'q1'));
    await q.check('input[name="q3"][value="a"]'); await verifier(q, 'q3');
    point('… tous les points au 1er essai', await q.evaluate(() => E.items.q3.pts) === 2, await retour(q, 'q3'));
    await neuve.ctx.close(); }
  // A7 : 15 et 50 échangés
  await p.click('[data-vider="A7"]'); await poserTout(p, ['a7t1', 'a7t4', 'a7t3', 'a7t2', 'a7t5', 'a7t6', 'a7t7', 'a7t8', 'a7t9', 'a7t10']); await verifier(p, 'A7');
  point('A7 : la distance d’alerte et la vitesse échangées sont refusées, trou par trou', /8 trous sur 10/.test(await retour(p, 'A7')), await retour(p, 'A7'));

  // ───────────── 5. garder, retrouver, effacer ─────────────
  console.log('5. La sauvegarde');
  await p.fill('#nom', 'Dupont'); await p.fill('#flou', 'les boucles while'); await p.check('#reel1'); await p.check('input[name="position"][value="3"]'); await p.waitForTimeout(500);
  const avant = await p.innerText('#score'); await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(700);
  point('après un rechargement : nom, points, programmes, lignes, cases', await p.inputValue('#nom') === 'Dupont' && await p.innerText('#score') === avant && (await ordre(p, 3)).join() === SOLUTIONS[3].join() && await p.inputValue('#b13') === LIGNES.b13 && await p.isChecked('#reel1') && await p.isChecked('input[name="position"][value="3"]') && await p.inputValue('#flou') === 'les boucles while', await p.innerText('#score'));
  await p.emulateMedia({ media: 'print' });
  point('la fiche imprimée porte le nom, les points et les programmes', await p.evaluate(() => { const t = document.getElementById('trace'); return getComputedStyle(t).display !== 'none' && /Dupont/.test(t.textContent) && /sur 55/.test(t.textContent) && /import cyberpi/.test(t.textContent) && getComputedStyle(document.querySelector('main')).display === 'none'; }));
  const pdf = await p.pdf({ format: 'A4' }); const pages = (pdf.toString('latin1').match(/\/Type\s*\/Page[^s]/g) || []).length;
  point('la fiche imprimée tient en deux pages au plus (' + pages + ')', pages >= 1 && pages <= 2, pages);
  await p.emulateMedia({ media: 'screen' });
  await p.click('#btnEffacer'); await p.waitForTimeout(100);
  point('un seul clic sur « Effacer » n’efface rien', await p.inputValue('#nom') === 'Dupont');
  await p.click('#btnEffacer'); await p.waitForLoadState('load'); await p.waitForTimeout(700);
  point('le second clic efface tout : nom, points, programmes, clé du navigateur', await p.inputValue('#nom') === '' && await p.innerText('#score') === '0' && (await ordre(p, 3)).length === 0 && await p.evaluate(() => localStorage.getItem(KEY)) === null);
  point('aucune erreur JavaScript', erreurs.length === 0, erreurs.join(' | '));
  await ctx.close();

  // ───────────── 6. le robot simulé ─────────────
  console.log('6. Le robot simulé');
  ({ ctx, p, erreurs } = await ouvrir());
  const sim = (code) => p.evaluate(code => window.EditeurPython.executer(code, { simulation: document.getElementById('robot-simule').textContent.replace(/^\s*\n/, ''), limiteActive: 4000, limiteTotale: 12000 }), code);
  await poserTout(p, SOLUTIONS[1]); await p.click('[data-simuler="1"]'); await p.waitForSelector('#sim-1 .sim-journal', { timeout: 30000 });
  point('A1 sur le robot simulé : l’écran montre Y, puis XZ', (await p.innerText('#sim-1 .ecran-robot')) === 'Y\nXZ', await p.innerText('#sim-1'));
  let r = await sim('import cyberpi, time\ncyberpi.led.on(255,20,30,"all")\ntime.sleep(1)\ncyberpi.led.off()');
  point('A2 : allumer, attendre 1 s (comptée, pas attendue), éteindre', !r.erreur && /lumières allumées : rouge 255, vert 20, bleu 30/.test(r.sortie) && /\[1\.0 s\] 💡 lumières éteintes/.test(r.sortie), r.sortie);
  r = await sim("import cyberpi, time\nwhile not cyberpi.controller.is_press('up'):\n    time.sleep(0.05)\ncyberpi.mbot2.forward(speed=40, run_time=1)");
  point('A3 : la manette est poussée pendant l’essai, puis le robot avance', !r.erreur && /pousse la manette vers le haut/.test(r.sortie) && /avance pendant 1 s, vitesse 40 tr\/min/.test(r.sortie), r.sortie);
  r = await sim(await p.evaluate(() => A7_MODELE.map(l => '    '.repeat(l[0]) + l[1] + (l[2] === null ? '' : document.getElementById(A7_ATTENDU[l[2]]).getAttribute('data-code'))).join('\n')));
  point('A7 : lumières vertes, obstacle, rire, recul, virage — puis l’essai se termine seul', !r.erreur && !r.arret && /vert 255/.test(r.sortie) && /son « laugh »/.test(r.sortie) && /tourne de 135° vers la droite/.test(r.sortie) && /fin de l'essai simulé/.test(r.sortie), (r.erreur && r.erreur.message) || r.sortie.slice(-300));
  r = await sim('cyberpi.console.print("X")');
  point('sans « import cyberpi », Python dit que le nom est inconnu (le robot simulé ne prête pas ses noms)', !!r.erreur && r.erreur.type === 'NameError', r.erreur && r.erreur.message);
  r = await sim('import cyberpi\ncyberpi.mbot2.fly(speed=100)');
  point('une commande qui n’existe pas arrête le programme, comme sur le robot', !!r.erreur && r.erreur.type === 'AttributeError' && /mbot2/.test(r.erreur.message), r.erreur && r.erreur.message);
  r = await sim('import cyberpi\ncyberpi.mbot2.forward(speed="40", run_time=1)');
  point('une vitesse écrite en texte : TypeError (le défi 1 du Bonus)', !!r.erreur && r.erreur.type === 'TypeError', r.erreur && r.erreur.message);
  await p.locator('#bac-a-sable').scrollIntoViewIfNeeded(); await p.locator('#vsRobot button', { hasText: 'Exécuter' }).first().click(); await p.waitForTimeout(2500);
  point('la console du bac à sable se lit sans code interne (ni « ⏎ », ni « DEL »)', !/⏎|DEL/.test(await p.innerText('#vsRobot')), (await p.innerText('#vsRobot')).slice(-200));
  point('le bac à sable exécute son programme de départ', /lumières allumées : rouge 0, vert 0, bleu 255/.test(await p.innerText('#vsRobot')), (await p.innerText('#vsRobot')).slice(-200));
  // envoyer au vrai robot : l'éditeur ouvert sur le programme de l'élève, copier, Vittascience
  await p.click('[data-editer="2"]');
  point('« Ouvrir mon programme » sur un programme vide : la page le dit, et n’ouvre rien', /vide/.test(await p.innerText('#note-robot-2')) && !(await p.$('#py_2')));
  await poserTout(p, SOLUTIONS[2]); await p.click('[data-editer="2"]'); await p.waitForTimeout(300);
  point('… sur un programme posé : l’éditeur s’ouvre sous l’activité, avec ce programme', await p.evaluate(() => !!document.querySelector('#m2 #vs2.editeur-py--actif')) && await p.inputValue('#py_2') === await p.evaluate(() => codeDe(2)), await p.inputValue('#py_2'));
  await p.fill('#py_2', 'import cyberpi\ncyberpi.led.on(1, 2, 3, "all")'); await p.waitForTimeout(800);
  await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(700); await p.click('[data-editer="2"]'); await p.waitForTimeout(300);
  point('… rouvert après un rechargement : il reprend le programme modifié', /led\.on\(1, 2, 3/.test(await p.inputValue('#py_2')), await p.inputValue('#py_2'));
  await p.click('[data-copier="A7"]');
  point('« Copier » sur le programme A7 troué : la page dit qu’il reste des trous', /trous/.test(await p.innerText('#note-robot-A7')), await p.innerText('#note-robot-A7'));
  point('sous chaque activité A1 à A7 : ouvrir dans l’éditeur, copier, et le lien Vittascience mBot2', await p.evaluate(() => ['1','2','3','4','5','6','A7'].every(z => { const b = document.querySelector('.vers-robot[data-zone="' + z + '"]'); return b && b.querySelector('[data-editer]') && b.querySelector('[data-copier]') && /vittascience\.com\/cyberpi/.test(b.querySelector('a').href) && b.querySelector('a').target === '_blank'; })));
  await p.locator('#vsBonus button', { hasText: 'Exécuter' }).first().click(); await p.waitForTimeout(2500);
  point('le Bonus a son éditeur, branché sur le robot simulé', /avance pendant 1 s, vitesse 40 tr\/min/.test(await p.innerText('#vsBonus')), (await p.innerText('#vsBonus')).slice(-200));
  point('aucune erreur JavaScript', erreurs.length === 0, erreurs.join(' | '));
  await ctx.close();

  // ───────────── 7. le téléphone ─────────────
  console.log('7. Sur un téléphone (390 px, tactile)');
  ({ ctx, p, erreurs } = await ouvrir({ viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true }));
  point('rien ne défile de côté', await p.evaluate(() => document.documentElement.scrollWidth) <= 390, await p.evaluate(() => document.documentElement.scrollWidth));
  await p.locator('#m5t1').scrollIntoViewIfNeeded(); for (const id of SOLUTIONS[5]) await p.tap('#' + id);
  point('au doigt, toucher place les étiquettes', (await ordre(p, 5)).join() === SOLUTIONS[5].join(), await ordre(p, 5));
  await p.locator('#m4t2').scrollIntoViewIfNeeded(); await p.waitForTimeout(150);
  const pose = await p.evaluate(() => { const j = document.getElementById('m4t2'), z = document.getElementById('prog4'), a = j.getBoundingClientRect(), d = z.getBoundingClientRect(); const ev = (t, x, y) => new PointerEvent(t, { bubbles: true, cancelable: true, pointerId: 7, pointerType: 'touch', isPrimary: true, clientX: x, clientY: y, button: 0 }); j.dispatchEvent(ev('pointerdown', a.left + 8, a.top + 8)); document.dispatchEvent(ev('pointermove', a.left + 20, a.top + 40)); document.dispatchEvent(ev('pointermove', d.left + 30, d.top + 20)); document.dispatchEvent(ev('pointerup', d.left + 30, d.top + 20)); return [...z.querySelectorAll('.token')].map(t => t.id).join(); });
  point('au doigt, glisser dépose l’étiquette', pose === 'm4t2', pose);
  point('une étiquette ne laisse pas la page défiler sous le doigt (touch-action)', await p.evaluate(() => getComputedStyle(document.querySelector('button.token')).touchAction) === 'none');
  await p.fill('#b6', 'for i in range(9):'); await verifier(p, 'b6');
  point('B6 faux, au téléphone : « il affiche » et « il doit afficher » côte à côte, sans déborder', await p.evaluate(() => { const c = document.querySelectorAll('#fb-b6 .ligne-compare > div'); return c.length === 2 && Math.abs(c[0].getBoundingClientRect().top - c[1].getBoundingClientRect().top) < 2 && document.documentElement.scrollWidth <= 390; }));
  point('A7 : une longue ligne peut se couper après « ( » ou « , », et son texte ne change pas', await p.evaluate(() => { const l = [...document.querySelectorAll('.a7-ligne [data-code-colore]')].find(e => /backward/.test(e.textContent)); return !!l && l.querySelectorAll('wbr').length >= 2 && l.textContent === 'cyberpi.mbot2.backward(speed=VITESSE, run_time=0.4)'; }));
  await poserTout(p, []); for (const id of A7) await p.tap('#' + id); await p.tap('[data-verifier="A7"]');
  point('A7 au doigt : dix étiquettes touchées dans l’ordre des trous', /Juste/.test(await retour(p, 'A7')), await retour(p, 'A7'));
  point('aucune erreur JavaScript', erreurs.length === 0, erreurs.join(' | '));
  await ctx.close();
} catch (e) {
  console.log('⛔ EN PANNE : le banc s’est arrêté — ' + (e && e.message)); await nav.close(); process.exit(2);
}
await nav.close();
if (passes + echecs === 0) { console.log('⛔ EN PANNE : aucun point joué'); process.exit(2); }
console.log('\n' + (echecs ? '❌ ' : '✅ ') + passes + ' / ' + (passes + echecs) + ' points — TP mBot2 (3e_C9.1, 3e_C9.2)');
process.exit(echecs ? 1 : 0);
