/* tests_tp_algorigrammes_4e_C6.2.mjs — banc du « TP — Algorigrammes de domotique », rejouable.
 *
 * POURQUOI CE FICHIER
 * -------------------
 * Les PR #832 et #833 (20/11/2026) annonçaient un banc Playwright de 28 puis 29 points pour ce TP ; il n'a jamais
 * été commité (règles d'or n°259 et n°266 : un rapport qui cite un script absent ne prouve rien). Ce banc reprend
 * leurs points et ajoute ceux de la suite de l'audit en 12 axes (21/11/2026) : corrections expliquées, aides à deux
 * niveaux, simulation qui joue les sorties de l'élève, bilan qui montre ses constructions, date du poste, aucun bloc
 * dessiné (n°308), listings en couleurs (n°13), réponses gardées au rechargement (n°15), lien depuis la séquence.
 *
 * Usage, depuis ce dossier :  node tests_tp_algorigrammes_4e_C6.2.mjs
 * Sortie 0 si tout passe, 1 si un point échoue, 2 si le banc n'a rien pu vérifier (n°299).
 */
import path from 'node:path';
import fs from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';

let chromium;
try { ({ chromium } = await import('playwright')); }
catch (e) { console.error('⛔ Playwright introuvable : banc non exécuté (sortie 2).'); process.exit(2); }

const ICI = path.dirname(fileURLToPath(import.meta.url));
const TP = path.join(ICI, 'tp_algorigrammes_domotique.html');
const SEQ = path.join(ICI, 'sequence-jardin-connecte-arrosage-automatique.html');
const URL = pathToFileURL(TP).href;

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d: c ? '' : d });
let b;
try { b = await chromium.launch(); }
catch (e) { console.error('⛔ Chromium ne démarre pas : banc non exécuté (sortie 2). ' + e.message); process.exit(2); }

const essais = (p, item) => p.evaluate(i => state.tries[i] || 0, item);
const statut = (p, item) => p.evaluate(i => state.st[i] || 0, item);
const corrOuverte = (p, item) => p.evaluate(i => [...document.querySelectorAll(`[data-corr="${i}"]`)].every(x => !x.hidden), item);
const vider = async p => { await p.evaluate(() => Object.keys(localStorage).forEach(k => localStorage.removeItem(k))); await p.reload(); await p.waitForTimeout(150); };

/* ════════════════ ORDINATEUR, réseau coupé, horloge de Martinique à 22 h 30 ════════════════ */
{
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 }, timezoneId: 'America/Martinique' });
  const reseau = []; const err = [];
  await ctx.route('**/*', r => { const u = r.request().url(); if (/^https?:/i.test(u)) { reseau.push(u); return r.abort(); } return r.continue(); });
  const p = await ctx.newPage();
  p.on('pageerror', e => err.push(String(e)));
  // 21/11/2026 à 22 h 30 en Martinique = 22/11 à 2 h 30 en temps universel : l'ancienne date UTC donnait le lendemain.
  await p.clock.install({ time: new Date('2026-11-22T02:30:00Z') });
  await p.goto(URL); await p.waitForTimeout(200);
  await vider(p);

  ok('date du jour : celle du poste (21/11 à 22 h 30 en Martinique), pas la date UTC du lendemain',
     await p.inputValue('#studentDate') === '2026-11-21', await p.inputValue('#studentDate'));
  ok('au départ, toutes les corrections sont fermées', await p.evaluate(() => [...document.querySelectorAll('[data-corr]')].every(x => x.hidden)));
  ok('aides : deux niveaux pour les 5 exercices construits, un indice pour chacune des 2 questions, toutes repliées',
     await p.evaluate(() => { const a = [...document.querySelectorAll('details.aide')]; return a.length === 12 && a.every(d => !d.open)
       && a.filter(d => /niveau 1/.test(d.querySelector('summary').textContent)).length === 5 && a.filter(d => /niveau 2/.test(d.querySelector('summary').textContent)).length === 5; }));
  ok('notes d\'auteur retirées (« Précision pédagogique », « Phrase élève », « Pour un débutant »)',
     await p.evaluate(() => !/Précision pédagogique|Phrase élève|Pour un débutant/.test(document.body.innerText)));

  // Phase 0
  await p.click('button[onclick="checkPhase0()"]');
  ok('phase 0 : « Vérifier » sans choix ne compte pas d\'essai', await essais(p, 'p0') === 0);
  for (const [n, v] of [['mEllipse', 'action'], ['mRectangle', 'action'], ['mLosange', 'condition'], ['mPara', 'es']]) await p.check(`input[name=${n}][value=${v}]`);
  await p.click('button[onclick="checkPhase0()"]');
  const ferme1 = !(await corrOuverte(p, 'p0'));
  await p.click('button[onclick="checkPhase0()"]');
  ok('phase 0 : la correction reste fermée après la 1re erreur et s\'ouvre après la 2e', ferme1 && await corrOuverte(p, 'p0'));
  await p.click('[data-corr=p0]');
  await p.check('input[name=mEllipse][value=debut]'); await p.click('button[onclick="checkPhase0()"]');
  ok('phase 0 : réussie après lecture de la correction = statut 1, aucun point', await statut(p, 'p0') === 1 && await p.evaluate(() => state.score === 0));

  // Phase 1
  await p.click('#btnP1');
  await p.click('button[onclick="checkBuild(1)"]');
  ok('phase 1 : construction vide refusée sans compter d\'essai', await essais(p, 'p1') === 0 && /Ajoute des blocs/.test(await p.innerText('#f1')));
  await p.evaluate(() => { addBlock(1, 'debut'); addBlock(1, 'debut'); });
  const doublon = await p.evaluate(() => ({ n: document.querySelectorAll('#zone1 [data-id=debut]').length, gris: document.querySelector('#bank1 button[data-bloc=debut]').disabled }));
  await p.click('#zone1 [data-id=debut] button[aria-label^="Retirer"]');
  const degrise = await p.evaluate(() => !document.querySelector('#bank1 button[data-bloc=debut]').disabled);
  ok('phase 1 : un bloc posé ne s\'ajoute pas deux fois (bouton grisé), et redevient disponible une fois retiré', doublon.n === 1 && doublon.gris && degrise, JSON.stringify(doublon));
  for (const id of ['debut', 'allumer', 'attendre10', 'eteindre', 'fin']) await p.click(`#bank1 button[data-bloc=${id}]`);
  await p.click('button[onclick="checkBuild(1)"]');
  ok('phase 1 : bon ordre réussi avant la correction = 2,5 points', await statut(p, 'p1') === 2 && await p.evaluate(() => state.score === 2.5));

  // Phase 2 + simulation
  await p.click('#btnP2');
  await p.click('button[onclick="simulatePhase2()"]');
  const simSans = await p.innerText('#sim2');
  for (const id of ['debut', 'lireLux', 'testNuit', 'attendre1', 'boucle']) await p.click(`#bank2 button[data-bloc=${id}]`);
  await p.check('input[name=b2oui][value=eteindre]'); await p.check('input[name=b2non][value=allumer]');
  await p.evaluate(() => { const r = document.getElementById('lux'); r.value = 20; r.dispatchEvent(new Event('input')); });
  await p.click('button[onclick="simulatePhase2()"]');
  const simFaux = await p.evaluate(() => ({ t: document.getElementById('sim2').innerText, err: !!document.querySelector('#sim2 .error') }));
  ok('simulation : elle demande d\'abord les sorties, puis joue celles de l\'élève (sorties inversées à 20 lux : « s\'éteint », en erreur)',
     /Choisis d'abord les sorties/.test(simSans) && simFaux.err && /s'éteint/.test(simFaux.t), simSans + ' | ' + simFaux.t);
  await p.click('button[onclick="checkBuild(2)"]');
  ok('phase 2 : tronc juste, sorties fausses → le retour parle des sorties et compte un essai',
     /Relis les sorties/.test(await p.innerText('#f2')) && await essais(p, 'p2') === 1);
  await p.check('input[name=b2oui][value=allumer]'); await p.check('input[name=b2non][value=eteindre]');
  await p.click('button[onclick="simulatePhase2()"]');
  const simNuit = await p.evaluate(() => !!document.querySelector('#sim2 .success') && /allume la lampe/.test(document.getElementById('sim2').innerText));
  await p.evaluate(() => { const r = document.getElementById('lux'); r.value = 120; r.dispatchEvent(new Event('input')); });
  await p.click('button[onclick="simulatePhase2()"]');
  const simJour = await p.evaluate(() => !!document.querySelector('#sim2 .success') && /répond Non/.test(document.getElementById('sim2').innerText));
  ok('simulation : sorties justes → réussite la nuit (20 lux) comme le jour (120 lux) ; curseur de 0 à 200 lux',
     simNuit && simJour && await p.evaluate(() => document.getElementById('lux').max === '200'));
  await p.click('button[onclick="checkBuild(2)"]');
  ok('phase 2 : réussie au 2e essai, avant la correction = points', await statut(p, 'p2') === 2);

  // Phase 3 : les deux ordres de lecture
  await p.click('#btnP3');
  for (const id of ['debut', 'lirePres', 'lireLux', 'testNuit', 'testPres', 'attendre1', 'boucle']) await p.click(`#bank3 button[data-bloc=${id}]`);
  for (const [n, v] of [['b3lumOui', 'test2'], ['b3lumNon', 'eteindre'], ['b3presOui', 'allumer'], ['b3presNon', 'eteindre']]) await p.check(`input[name=${n}][value=${v}]`);
  await p.click('button[onclick="checkBuild(3)"]');
  ok('phase 3 : les deux capteurs peuvent être lus dans l\'ordre inverse', await statut(p, 'p3') === 2);

  // Débogage : listing en couleurs
  ok('débogage : l\'algorithme est en couleurs façon IDE (n°13)', await p.evaluate(() => !!document.querySelector('#phase3 pre.programme .py-kw')));
  await p.check('.bug[value=ou]'); await p.check('.bug[value=sinon]');
  await p.click('button[onclick="checkBugs()"]'); await p.click('button[onclick="checkBugs()"]');

  // Phase 4
  await p.click('#btnP4');
  await p.check('input[name=q0][value="0"]'); await p.click('button[onclick^="checkQcm(0"]');
  ok('question 1 : un seul essai, puis la correction s\'ouvre', await corrOuverte(p, 'q0'));
  await p.check('input[name=q1][value="2"]'); await p.click('button[onclick^="checkQcm(1"]');
  await p.fill('#projectCondition', 'aaaaa'); await p.fill('#projectYes', 'bbbbb'); await p.fill('#projectNo', 'ccccc');
  await p.click('button[onclick="checkProject()"]');
  const refus = await statut(p, 'p4') === 0;
  await p.selectOption('#projectType', 'arrosage');
  await p.fill('#projectCondition', 'humidité du sol < 30 % ET pluie = non ?');
  await p.fill('#projectYes', 'ouvrir l\'électrovanne du potager pendant 30 secondes'); await p.fill('#projectNo', 'laisser l\'électrovanne fermée');
  await p.click('button[onclick="checkProject()"]');
  const proj = await p.evaluate(() => { const s = document.querySelector('#projectAlgo svg'); return { st: state.st.p4, multi: [...s.querySelectorAll('text')].some(t => t.querySelectorAll('tspan').length > 1), dbl: /\?\s*\?/.test(s.textContent) }; });
  ok('mini-projet : « aaaaa » refusé ; une vraie condition validée ; libellé long coupé sur plusieurs lignes ; pas de « ? ? »',
     refus && proj.st === 2 && proj.multi && !proj.dbl, JSON.stringify(proj));

  // Corrections : toutes ouvertes, toutes expliquées, marqueurs uniques, aucun bloc dessiné
  const types = ['bases', 'lineaire', 'condition', 'sequence2tests', 'complexe', 'bug', 'bloc', 'arrosage'];
  const corr = await p.evaluate(ts => ts.map(ty => { showCorrection('corr0', ty); const z = document.getElementById('corr0');
    return { ty, pq: !!z.querySelector('.pourquoi'), pg: !!z.querySelector('.piege'), coul: /couleurs ne sont ici/.test(z.textContent) }; }), types);
  ok('les 8 corrections disent pourquoi et le piège fréquent ; plus aucune ne répète la phrase sur les couleurs',
     corr.every(c => c.pq && c.pg && !c.coul), JSON.stringify(corr.filter(c => !c.pq || !c.pg || c.coul)));
  await p.evaluate(() => { showCorrection('corr1', 'condition'); showCorrection('corr2', 'condition'); showCorrection('corr3', 'sequence2tests'); showCorrection('corr3b', 'complexe'); showCorrection('qcorr0', 'bloc'); showCorrection('qcorr1', 'arrosage'); });
  const marq = await p.evaluate(() => { const ids = [...document.querySelectorAll('marker')].map(m => m.id); const refs = [...document.querySelectorAll('[marker-end]')].map(e => e.getAttribute('marker-end').slice(5, -1));
    return { uniques: new Set(ids).size === ids.length, n: ids.length, orphelins: refs.filter(r => !ids.includes(r)).length }; });
  ok('pointes de flèches : un identifiant par schéma, aucune référence orpheline', marq.uniques && marq.orphelins === 0 && marq.n >= 6, JSON.stringify(marq));
  ok('correction de la phase 3 : deux losanges', await p.evaluate(() => document.querySelectorAll('#corr3 svg polygon[fill="#fb923c"]').length === 2));
  ok('question 1 : aucun bloc dessiné (n°308) ; la décision est montrée en Python coloré',
     await p.evaluate(() => !/si\s*<condition>/.test([...document.querySelectorAll('svg')].map(s => s.textContent).join(' ')) && typeof svgScratch === 'undefined'
       && !!document.querySelector('#qcorr0 pre[data-code-colore=python] .py-kw')));

  // Bilan
  await p.click('#btnP5');
  await p.fill('#studentName', 'Sarah Pierre'); await p.fill('#studentClass', '4e A');
  await p.click('button[onclick="finalReport()"]');
  const bil = await p.evaluate(() => ({ t: document.getElementById('report').innerText, code: document.getElementById('validationCode').textContent.replace('Code de validation : ', '') }));
  ok('bilan : date au format français et trace des constructions (ordre de la phase 1, sorties, mini-projet, essais ratés)',
     /Date : 21\/11\/2026/.test(bil.t) && /Mes constructions et mes réponses/.test(bil.t) && /Début → Allumer lampe → Attendre 10 s → Éteindre lampe → Fin/.test(bil.t)
       && /ouvrir l'électrovanne/.test(bil.t) && /essais ratés/.test(bil.t), bil.t.slice(0, 300));
  await p.click('.verif-code summary');
  await p.fill('#vNom', 'Sarah Pierre'); await p.fill('#vClasse', '4e A'); await p.fill('#vDate', '2026-11-21'); await p.fill('#vCode', bil.code);
  await p.click('button[onclick="verifierCode()"]');
  const vrai = /Code cohérent/.test(await p.innerText('#vRes'));
  await p.fill('#vCode', bil.code.replace(/^[\d,]+/, '20')); await p.click('button[onclick="verifierCode()"]');
  const retouche = /ne correspond pas/.test(await p.innerText('#vRes'));
  ok('code de validation : le vrai est reconnu, une note retouchée est refusée', vrai && retouche, bil.code);

  // Rechargement : tout ce que l'élève a écrit ou coché revient
  await p.reload(); await p.waitForTimeout(200);
  const garde = await p.evaluate(() => ({ nom: document.getElementById('studentName').value, classe: document.getElementById('studentClass').value,
    p0: (document.querySelector('input[name=mEllipse]:checked') || {}).value, bug: [...document.querySelectorAll('.bug:checked')].map(c => c.value).sort().join(','),
    q0: (document.querySelector('input[name=q0]:checked') || {}).value, type: document.getElementById('projectType').value, c: document.getElementById('projectCondition').value,
    z1: document.querySelectorAll('#zone1 .algo-block').length, gris: document.querySelector('#bank1 button[data-bloc=fin]').disabled }));
  ok('rechargement : nom, classe, phase 0, débogage, question 1, mini-projet et constructions sont gardés (n°15)',
     garde.nom === 'Sarah Pierre' && garde.classe === '4e A' && garde.p0 === 'debut' && garde.bug === 'ou,sinon' && garde.q0 === '0'
       && garde.type === 'arrosage' && /pluie/.test(garde.c) && garde.z1 === 5 && garde.gris, JSON.stringify(garde));

  // Effacement complet (n°322)
  await p.click('#btnP5'); await p.click('#btnReset'); await p.click('#btnReset'); await p.waitForTimeout(300);
  // Au rechargement qui suit l'effacement, la page repose un état vierge (phase 0, rien de réussi) : c'est la seule clé
  // qui doit rester, sans nom, sans essai, sans construction.
  const apres = await p.evaluate(() => { const k = Object.keys(localStorage).filter(x => x.startsWith('algoDomotiqueV12')); const s = JSON.parse(localStorage.getItem('algoDomotiqueV12State') || '{}');
    return { k: k.join(','), vierge: !Object.keys(s.st || {}).length && !Object.keys(s.tries || {}).length && !(s.ident || {}).nom && !Object.keys(s.br || {}).length, nom: document.getElementById('studentName').value }; });
  ok('« Effacer toute ma progression » : il ne reste qu\'un état vierge, sans nom, sans essai, sans construction',
     apres.k === 'algoDomotiqueV12State' && apres.vierge && apres.nom === '', JSON.stringify(apres));
  ok('ordinateur : aucune requête réseau, zéro erreur JavaScript', reseau.length === 0 && err.length === 0, reseau.concat(err).slice(0, 3).join(' | '));
  await ctx.close();
}

/* ════════════════ TÉLÉPHONE 390 px ════════════════ */
{
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const p = await ctx.newPage(); const err = []; p.on('pageerror', e => err.push(String(e)));
  await p.goto(URL); await p.waitForTimeout(200);
  const deb = [];
  for (let i = 0; i <= 5; i++) { await p.click(`#btnP${i}`); if (await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1)) deb.push(i); }
  ok('390 px : aucune des six phases ne déborde en largeur', deb.length === 0, 'phases ' + deb.join(', '));
  await p.click('#btnP1'); await p.click('#bank1 button[data-bloc=debut]');
  const cib = await p.evaluate(() => [...document.querySelectorAll('#zone1 .block-actions button')].map(x => { const r = x.getBoundingClientRect(); return Math.min(r.width, r.height); }));
  ok('écran tactile : boutons ↑ ↓ ✕ d\'au moins 44 px', cib.length === 3 && cib.every(v => v >= 44), cib.join(' / '));
  ok('téléphone : zéro erreur JavaScript', err.length === 0, err.join(' | '));
  await ctx.close();
}

/* ════════════════ LA SÉQUENCE MÈNE AU TP ════════════════ */
{
  const s = fs.readFileSync(SEQ, 'utf8');
  ok('la séquence 4e_C6.2 renvoie au TP, à côté de sa définition de l\'algorigramme', /un algorigramme est un dessin[^]*?href="tp_algorigrammes_domotique\.html"/.test(s) && fs.existsSync(TP));
}

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
