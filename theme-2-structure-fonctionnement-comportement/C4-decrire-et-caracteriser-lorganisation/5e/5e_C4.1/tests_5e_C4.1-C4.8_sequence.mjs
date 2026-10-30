/* tests_5e_C4.1-C4.8_sequence.mjs — les seize coches de la séquence, rejouées.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport du lot annonçait « Séquence (16 tests) », seize lignes, seize
 * coches vertes — et citait un script `tests_lot05.js` **jamais commité**. Le
 * QCM a reçu sa suite le 31/08/2026 ; la séquence est restée avec sa liste de
 * bonnes intentions (règle d'or n°259).
 *
 * Ce fichier conduit la séquence POUR DE VRAI : il remplit les huit activités,
 * manœuvre le simulateur, provoque un passage devant le détecteur, et lit ce
 * que la page répond.
 *
 * SIX SÉANCES DEPUIS LE 24/10/2026
 * --------------------------------
 * La séance 5 annonçait 25 + 25 + 25 = 75 min pour 55. Le réinvestissement (la
 * sonnette, clé 7) et la clôture passent en séance 6, avec l'activité 7 « Le FAST
 * du lampadaire, complet » (clé 8 : l'exercice 2 de l'atelier FAST, inséré). Les
 * clés des activités déjà validées ne changent pas : une sauvegarde faite avec la
 * version à cinq séances se relit (contrôles 31 à 35).
 *
 * IL NE RECOPIE PAS LES BONNES RÉPONSES. Elles sont extraites des fonctions
 * `CHECKS` de la page elle-même : un test qui recopie ce qu'il doit vérifier
 * cesse de le vérifier, et se désynchronise en silence le jour où la séquence
 * change une option.
 *
 * CE QU'IL A TROUVÉ EN NAISSANT
 * -----------------------------
 * `window.__exp` valait `{"jour":"eteint"}` **au chargement de la page** :
 * `majLampe()` était appelé à l'initialisation et enregistrait l'état affiché
 * comme une expérience observée. Le verrou de l'activité 3 en exige trois
 * (jour, nuit, nuit+passage) : il s'ouvrait donc d'un tiers tout seul, avant
 * que l'élève ait touché le curseur. C'est exactement ce que la règle d'or
 * n°226 interdit, et le tableau écrit à la main affirmait le contraire.
 *
 * Usage, depuis ce dossier :
 *   node tests_5e_C4.1-C4.8_sequence.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import fs from 'node:fs';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const PAGE = path.join(ICI, 'sequence_5e_C4.1-C4.8_lampadaire_intelligent.html');

const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => { if (!/fonts\.g/.test(r.url())) fail.push(r.url()); });
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });

await p.goto('file://' + PAGE, { waitUntil: 'load' });
await p.waitForTimeout(350);

ok('1 · charge sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
ok('2 · aucune requête locale échouée', fail.length === 0, fail.slice(0, 2).join(' | '));

/* ── règle d'or n°226 : aucun verrou ouvert avant le premier geste ───────── */
const expDepart = await p.evaluate(() => window.__exp || {});
ok('3 · aucune expérience enregistrée au chargement (règle n°226)',
   Object.keys(expDepart).length === 0, JSON.stringify(expDepart));
ok('4 · aucune activité validée au chargement',
   Object.keys(await p.evaluate(() => window.__valid || {})).length === 0);

/* ── les réponses attendues, LUES dans la page ───────────────────────────── */
const ATT = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const m = CHECKS[n].toString().match(/att\s*=\s*(\{[\s\S]*?\})\s*;/);
    out[n] = m ? eval('(' + m[1] + ')') : {};
  }
  return out;
});
const totalChamps = Object.values(ATT).reduce((s, o) => s + Object.keys(o).length, 0);
ok('5 · les bonnes réponses sont extraites de la page, pas recopiées ici',
   Object.keys(ATT).length === 8 && totalChamps >= 45,
   `${Object.keys(ATT).length} activités · ${totalChamps} champs`);

/* Les activités vivent dans six onglets de séance, et un onglet inactif est
   masqué : il faut l'ouvrir comme un élève le ferait. La répartition est celle
   de `majProgress()` dans la page — s5 porte les clés 5 et 6, s6 les clés 8
   (activité 7, le FAST) et 7 (la sonnette). */
const SEANCE = { 1: 's1', 2: 's2', 3: 's3', 4: 's4', 5: 's5', 6: 's5', 7: 's6', 8: 's6' };
async function ouvrirSeance(n) {
  await p.click(`.seance-tab[data-panel="${SEANCE[n]}"]`);
  await p.waitForTimeout(120);
}

/** Renseigne les champs d'une activité avec ce que la page attend. */
async function remplir(n) {
  await ouvrirSeance(n);
  for (const [id, v] of Object.entries(ATT[n])) {
    const balise = await p.$eval('#' + id, e => e.tagName);
    if (balise === 'SELECT') await p.selectOption('#' + id, v);
    else await p.fill('#' + id, v);
  }
}
const valider = async n => { await p.click(`[data-check="${n}"]`); await p.waitForTimeout(90); };
const retour = n => p.textContent('#fb' + n);

/** L'exercice d'atelier incrusté en tête de l'activité 1 (diagramme FAST) : ses bonnes
    réponses sont LUES dans la définition JSON de sa section, comme celles des CHECKS. */
async function remplirIncruste(uid) {
  await p.evaluate(uid => {
    const sec = document.getElementById(uid).closest('.atelier-incruste');
    const D = JSON.parse(sec.querySelector('script[type="application/json"]').textContent).exercices[uid];
    const coche = (name, v) => [...document.getElementsByName(name)].find(r => r.value === v).click();
    for (const w of D.widgets) {
      if (w.type === 'choix') coche(w.name, w.bonne);
      else if (w.type === 'classer') w.items.forEach(it => coche(it.name, it.bonne));
      else if (w.type === 'slots') w.slots.forEach(s => coche(s.name, s.bonnes[0]));
      else if (w.type === 'cases') w.bonnes.forEach(v => coche(w.name, v));
    }
  }, uid);
}

/* ── activité 1 : associations + matériaux + justification ───────────────── */
await remplir(1);
await valider(1);
ok('6 · act. 1 refusée tant que la justification ne parle pas du sel marin',
   !/Excellent|Bravo|Très bien/.test(await retour(1)), (await retour(1)).slice(0, 80));
await p.fill('#e1_just', "Près de la mer, les embruns apportent du sel : l'acier rouille vite.");
await valider(1);
ok('6 bis · act. 1 refusée tant que l\'exercice du diagramme FAST inséré n\'est pas réussi',
   /diagramme FAST/.test(await retour(1)) && !(await p.evaluate(() => !!window.__valid[1])),
   (await retour(1)).slice(0, 120));
await p.click('#fa_5e_e1 button.verifier');
await p.waitForTimeout(80);
ok('6 ter · l\'exercice FAST inséré se vérifie à vide (retour à reprendre)',
   (await p.textContent('#fa_5e_e1 .retour')).includes('🔴'),
   (await p.textContent('#fa_5e_e1 .retour')).slice(0, 70));
await remplirIncruste('fa_5e_e1');
await p.click('#fa_5e_e1 button.verifier');
await p.waitForTimeout(80);
ok('6 quater · l\'exercice FAST inséré, rempli juste, est réussi',
   (await p.textContent('#fa_5e_e1 .retour')).includes('Tout est juste'),
   (await p.textContent('#fa_5e_e1 .retour')).slice(0, 70));
await valider(1);
ok('7 · act. 1 validée avec les 9 réponses, la justification et l\'exercice FAST',
   /9 \/ 9/.test(await retour(1)) && await p.evaluate(() => !!window.__valid[1]),
   (await retour(1)).slice(0, 70));

/* ── activité 2 : chaîne d'énergie, ordre et natures ─────────────────────── */
await remplir(2);
await valider(2);
ok('8 · act. 2 refusée sans la chaîne fléchée au cahier',
   !/9 \/ 9 réponses correctes. (Excellent|Bravo|Très bien)/.test(await retour(2)),
   (await retour(2)).slice(0, 80));
await p.fill('#e2_cahier', 'lumineuse → électrique → chimique → électrique → lumineuse');
await valider(2);
ok('9 · act. 2 validée (9/9) une fois la chaîne écrite', /9 \/ 9/.test(await retour(2)),
   (await retour(2)).slice(0, 70));

/* ── activité 3 : LE VERROU EXPÉRIENTIEL ─────────────────────────────────── */
await remplir(3);
await valider(3);
ok('10 · act. 3 REFUSÉE tant que les trois expériences ne sont pas faites',
   /Fais VRAIMENT les expériences/.test(await retour(3)), (await retour(3)).slice(0, 90));

/** Manœuvre le simulateur comme un élève : curseur, puis bouton de passage. */
async function regler(lum) {
  await p.evaluate(v => {
    const s = document.getElementById('simJour');
    s.value = String(v);
    s.dispatchEvent(new Event('input', { bubbles: true }));
  }, lum);
  await p.waitForTimeout(60);
}
await regler(80);
ok('11 · jour (80 lux) : la LED est éteinte',
   (await p.textContent('#simLedTxt')).includes('éteint'), await p.textContent('#simLedTxt'));
await regler(10);
ok('12 · nuit (10 lux) sans passage : veille',
   (await p.textContent('#simLedTxt')).includes('veille'), await p.textContent('#simLedTxt'));
await p.click('#btnPassage');
await p.waitForTimeout(80);
ok('13 · nuit + passage : pleine puissance',
   (await p.textContent('#simLedTxt')).includes('PLEINE PUISSANCE'),
   await p.textContent('#simLedTxt'));

const exp = await p.evaluate(() => window.__exp);
ok('14 · les trois situations sont tracées, et seulement par le geste',
   ['jour', 'nuit', 'nuit+passage'].every(k => k in exp), JSON.stringify(exp));

await valider(3);
ok('15 · act. 3 validée (10/10) une fois les expériences réellement faites',
   /10 \/ 10/.test(await retour(3)), (await retour(3)).slice(0, 70));

/* ── activités 4 à 7 ─────────────────────────────────────────────────────── */
await remplir(4);
await p.fill('#e4_6', '2');
await valider(4);
ok('16 · act. 4 descripteurs et lecture de la table validée (7/7)',
   /7 \/ 7/.test(await retour(4)), (await retour(4)).slice(0, 70));

await remplir(5);
await valider(5);
ok('17 · act. 5 réseau local validée (6/6)', /6 \/ 6/.test(await retour(5)),
   (await retour(5)).slice(0, 70));

await remplir(6);
await valider(6);
ok('18 · act. 6 refusée tant que la justification n\'explique pas le conflit',
   /justification/.test(await retour(6)), (await retour(6)).slice(0, 90));
await p.fill('#e6_just',
  'Deux machines de même nom : le réseau ne sait plus à qui livrer, un nom doit être unique.');
await valider(6);
ok('19 · act. 6 jeu du courrier validée (5/5)', /5 \/ 5/.test(await retour(6)),
   (await retour(6)).slice(0, 70));

await remplir(7);
await valider(7);
ok('20 · act. 7 réinvestissement sonnette connectée validée (6/6)',
   /6 \/ 6/.test(await retour(7)), (await retour(7)).slice(0, 70));

/* ── séance 6, activité 7 (clé 8) : l'exercice 2 de l'atelier FAST, inséré ── */
await ouvrirSeance(8);
await valider(8);
ok('20 bis · activité 7 (FAST) refusée tant que l\'exercice inséré n\'est pas réussi',
   /Tout est juste/.test(await retour(8)) && !(await p.evaluate(() => !!window.__valid[8])),
   (await retour(8)).slice(0, 110));
await p.click('#fa_5e_e2 button.verifier');
await p.waitForTimeout(80);
ok('20 ter · l\'exercice FAST e2 inséré se vérifie à vide (retour à reprendre)',
   (await p.textContent('#fa_5e_e2 .retour')).includes('🔴'),
   (await p.textContent('#fa_5e_e2 .retour')).slice(0, 70));
await remplirIncruste('fa_5e_e2');
await p.click('#fa_5e_e2 button.verifier');
await p.waitForTimeout(80);
ok('20 quater · l\'exercice FAST e2, rempli juste, est réussi',
   (await p.textContent('#fa_5e_e2 .retour')).includes('Tout est juste'),
   (await p.textContent('#fa_5e_e2 .retour')).slice(0, 70));
const caseSchema = await p.evaluate(() => [...document.querySelectorAll('#fa_5e_e2 [data-miroir], #fa-lamp2 text')]
  .map(e => e.textContent).join(' | '));
ok('20 quinquies · les choix s\'écrivent dans le schéma vivant (batterie, panneau, détecteur)',
   /batterie/.test(caseSchema) && /panneau solaire/.test(caseSchema) && /détecteur de mouvement/.test(caseSchema),
   caseSchema.slice(0, 120));
await valider(8);
ok('20 sexies · activité 7 (FAST) validée une fois l\'exercice réussi',
   /5 \/ 5/.test(await retour(8)) && await p.evaluate(() => !!window.__valid[8]),
   (await retour(8)).slice(0, 70));
const sauvee = await p.evaluate(() => JSON.parse(localStorage.getItem('seq_5e_C4.1-C4.8_lampadaire') || '{}'));
const capte = [...Object.keys(sauvee.inputs || {}), ...Object.keys(sauvee.radios || {})].filter(k => /^fa_5e_/.test(k));
ok('20 septies · la sauvegarde de la page ne capte pas les champs des exercices insérés (ils ont leur clé)',
   capte.length === 0, capte.slice(0, 4).join(' · '));

/* ── progression, hypothèse, persistance ─────────────────────────────────── */
ok('21 · progression 8 / 8 activités validées',
   (await p.textContent('#progTxt')).includes('8 / 8'), await p.textContent('#progTxt'));
const coches = await p.$$eval('[id^="done-s"]', l => l.map(e => e.textContent.trim()));
ok('22 · les six séances portent leur coche', coches.length === 6 && coches.every(c => c === '✔'),
   coches.join('|'));

/* Règle d'or n°311 : dès la séance 2, l'hypothèse est repliée dans le volet
   « Rappel » ; l'élève l'écrit à la séance 1, on y retourne comme lui. */
await ouvrirSeance(1);
await p.fill('#hyp1', 'Je pense que le lampadaire s\'allume seulement quand il fait nuit.');
await p.waitForTimeout(120);
ok('23 · l\'hypothèse est rappelée dès la saisie',
   (await p.textContent('#hypRappelTxt')).includes('nuit'),
   await p.textContent('#hypRappelTxt'));

await p.reload({ waitUntil: 'load' });
await p.waitForTimeout(350);
ok('24 · les réponses survivent au rechargement',
   (await p.inputValue('#e5_1')) === ATT[5].e5_1, await p.inputValue('#e5_1'));
ok('25 · les validations survivent au rechargement',
   (await p.textContent('#progTxt')).includes('8 / 8'), await p.textContent('#progTxt'));
ok('26 · les traces d\'expériences survivent au rechargement',
   await p.evaluate(() => ['jour', 'nuit', 'nuit+passage'].every(k => k in (window.__exp || {}))));
const cochesFast = await p.$$eval('#fa_5e_e1 input[type=radio]:checked', l => l.length);
ok('26 bis · l\'exercice FAST inséré retrouve ses 8 réponses au rechargement (sa propre sauvegarde)',
   cochesFast === 8, cochesFast + ' cases cochées');
const cochesFast2 = await p.$$eval('#fa_5e_e2 input[type=radio]:checked', l => l.length);
ok('26 ter · l\'exercice FAST e2 (séance 6) retrouve ses 5 réponses au rechargement',
   cochesFast2 === 5, cochesFast2 + ' cases cochées');

/* ── liens locaux et hygiène ─────────────────────────────────────────────── */
const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens
  .filter(h => h && !/^(https?:|mailto:|#|javascript:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok('27 · aucun lien local cassé', casses.length === 0, casses.slice(0, 3).join(' · '));

const ids = await p.evaluate(() => [...document.querySelectorAll('[id]')].map(e => e.id));
ok('28 · aucun identifiant HTML en double', ids.length === new Set(ids).size);
ok('29 · aucune boîte modale sur tout le parcours', dlg.length === 0, dlg.join(' | '));
ok('30 · aucune erreur JS après l\'ensemble des interactions', err.length === 0,
   err.slice(0, 2).join(' | '));

/* ── six séances : le temps, la navigation, la clôture ───────────────────── */
const decoupe = await p.evaluate(() => {
  const ong = [...document.querySelectorAll('.seance-tab')].map(o => o.dataset.panel);
  const minutes = ong.map(id => [...document.querySelectorAll('#' + id + ' .activite > header .duree')]
    .reduce((s, d) => s + parseInt(d.textContent.replace(/\D+/g, ''), 10), 0));
  const bandeau = (document.querySelector('.badge.duree') || {}).textContent || '';
  return { ong, minutes, bandeau };
});
ok('31 · six onglets, et le bandeau dit « 6 séances de 55 min »',
   decoupe.ong.join() === 's1,s2,s3,s4,s5,s6' && /6 séances de 55 min/.test(decoupe.bandeau),
   decoupe.ong.join() + ' · ' + decoupe.bandeau);
ok('32 · chaque séance annonce 55 min d\'activités au plus (s5 : 50, s6 : 35)',
   decoupe.minutes.every(m => m > 0 && m <= 55) && decoupe.minutes[4] === 50 && decoupe.minutes[5] === 35,
   decoupe.minutes.join(' / '));
await ouvrirSeance(5);
await p.click('#s5 .vers-seance[data-vers="s6"]');
await p.waitForTimeout(150);
const apresBouton = await p.evaluate(() => ({ actif: document.querySelector('.seance-panel.active').id,
  volet: document.getElementById('ouverture').classList.contains('volet'),
  taches: document.getElementById('tachesBandeau').textContent }));
ok('33 · le bouton de fin de séance 5 ouvre la séance 6 (volet « Rappel » replié, tâches de la séance 6)',
   apresBouton.actif === 's6' && apresBouton.volet && /Séance 6/.test(apresBouton.taches) && /FAST/.test(apresBouton.taches),
   JSON.stringify(apresBouton).slice(0, 140));
const cloture = await p.evaluate(() => {
  const ou = t => [...document.querySelectorAll('.seance-panel')].filter(pn => [...pn.querySelectorAll('h2')].some(h => h.textContent.includes(t))).map(pn => pn.id).join();
  return { bonus: ou('Bonus'), bilan: ou('Mon bilan'), qcm: ou('Prêt·e'), synth: ou('Synthèse de la séquence'), sonnette: document.getElementById('act7').closest('.seance-panel').id };
});
ok('34 · la sonnette, la synthèse, le Bonus, le bilan et le QCM sont en séance 6, et seulement là',
   Object.values(cloture).every(v => v === 's6'), JSON.stringify(cloture));

/* Une sauvegarde faite avec la version à cinq séances (activités 1 à 7 validées) se relit. */
await p.evaluate(() => {
  localStorage.removeItem('rep_fast_5e_e2');
  localStorage.setItem('seq_5e_C4.1-C4.8_lampadaire', JSON.stringify({
    inputs: { e5_1: 'terminaux', e7_1: 'la sonnerie (haut-parleur) de la vie scolaire', hyp1: 'Ancienne hypothèse.' },
    radios: { confiance: '3' }, valid: { 1: true, 2: true, 3: true, 4: true, 5: true, 6: true, 7: true },
    exp: { jour: 'eteint', nuit: 'veille', 'nuit+passage': 'fort' } }));
});
const errAvant = err.length;
await p.reload({ waitUntil: 'load' });
await p.waitForTimeout(350);
const reprise = await p.evaluate(() => ({ prog: document.getElementById('progTxt').textContent,
  s5: document.getElementById('done-s5').textContent.trim(), s6: document.getElementById('done-s6').textContent.trim(),
  e7: document.getElementById('e7_1').value, hyp: document.getElementById('hyp1').value }));
ok('35 · une sauvegarde de la version à cinq séances se relit : 7 / 8, séance 5 cochée, séance 6 à finir',
   err.length === errAvant && reprise.prog.includes('7 / 8') && reprise.s5 === '✔' && reprise.s6 === '' &&
   reprise.e7.startsWith('la sonnerie') && reprise.hyp === 'Ancienne hypothèse.', JSON.stringify(reprise));

/* ── clôture : le Bonus a un champ et un corrigé complet par défi ; le bilan a son positionnement ── */
await ouvrirSeance(7);
const bonus = await p.evaluate(() => {
  const sec = [...document.querySelectorAll('#s6 section.card')].find(s => /Bonus/.test(s.querySelector('h2')?.textContent || ''));
  return [...sec.querySelectorAll('.bonus-defi')].map(d => {
    const c = d.querySelector('details.correction');
    const champ = d.querySelector('textarea[id]');
    return { id: d.id, champ: champ ? champ.id : null,
      etaye: !!(champ && champ.nextElementSibling && champ.nextElementSibling.matches('details.etayage')),
      replie: !!c && !c.open, resume: c ? c.querySelector('summary').textContent : '',
      erreurs: !!c && /Erreurs classiques/.test(c.textContent), pourquoi: !!c && /Pourquoi/.test(c.textContent),
      texte: c ? c.textContent : '' };
  });
});
ok('36 · Bonus : trois défis, chacun avec son champ, sa version étayée et un corrigé replié (réponse, pourquoi, erreurs classiques)',
   bonus.length === 3 && bonus.every(b => b.champ && b.etaye && b.replie && /Corrigé/.test(b.resume) && b.erreurs && b.pourquoi),
   bonus.map(b => `${b.id}:${b.champ}/${b.etaye}/${b.replie}/${b.erreurs}/${b.pourquoi}`).join(' · '));
const [maq, mai, fil] = bonus.map(b => b.texte);
ok('37 · les corrigés disent ce qu\'il faut observer : 4 états de la LED, une chaîne exemple fléchée, le ping et le doublon d\'adresse dans Filius',
   /éteinte[\s\S]*en veille[\s\S]*pleine puissance[\s\S]*éteinte/.test(maq)
   && /ALIMENTER[\s\S]*DISTRIBUER[\s\S]*CONVERTIR/.test(mai) && /TRANSMETTRE est absent/.test(mai)
   && /ping 192\.168\.0\.7/.test(fil) && /même adresse/.test(fil) && /Afficher les échanges de données/.test(fil),
   [maq.length, mai.length, fil.length].join(' / ') + ' caractères');
await p.fill('#bonusFilius', 'Essai : PC-TECHNO-01 en 192.168.0.1.');
const pos = await p.evaluate(() => [...document.querySelectorAll('#s6 fieldset.positionnement')].map(f => ({
  code: (f.querySelector('legend')?.textContent || '').slice(0, 7),
  radios: f.querySelectorAll('input[type=radio]').length,
  noms: new Set([...f.querySelectorAll('input[type=radio]')].map(r => r.name)).size,
  etiquetes: [...f.querySelectorAll('input[type=radio]')].every(r => !!document.querySelector(`label[for="${r.id}"]`)) })));
const codes = ['5e_C4.1', '5e_C4.2', '5e_C4.3', '5e_C4.4', '5e_C4.5', '5e_C4.6', '5e_C4.7', '5e_C4.8'];
ok('38 · bilan : « Je me positionne », un groupe de quatre boutons radio par code (les huit), chacun étiqueté',
   pos.length === 8 && pos.every((g, i) => g.code === codes[i] && g.radios === 4 && g.noms === 1 && g.etiquetes),
   pos.map(g => `${g.code}:${g.radios}`).join(' '));
for (const [i, c] of ['c41', 'c42', 'c43', 'c44', 'c45', 'c46', 'c47', 'c48'].entries())
  await p.check(`#pos_${c}_${(i % 4) + 1}`);
await p.waitForTimeout(800);
await p.reload({ waitUntil: 'load' });
await p.waitForTimeout(350);
const posApres = await p.evaluate(() => ['c41', 'c42', 'c43', 'c44', 'c45', 'c46', 'c47', 'c48']
  .map(c => (document.querySelector(`input[name="pos_${c}"]:checked`) || {}).value || '-'));
ok('39 · le positionnement et les champs du Bonus survivent au rechargement',
   posApres.join() === 'insuffisante,fragile,satisfaisante,tres-bonne,insuffisante,fragile,satisfaisante,tres-bonne'
   && (await p.inputValue('#bonusFilius')).startsWith('Essai'), posApres.join(' '));
/* ── séance 2 : les deux chaînes animées, pas à pas (30/10/2026) ─────────────
   L'animation remplace le schéma fixe à l'écran ; le schéma fixe reste dans un volet replié (agrandir), et s'imprime.
   « Suivant » n'est pas bloqué à la prédiction (le banc commun du lecteur doit pouvoir parcourir toutes les étapes) ;
   c'est « Regarder » qui s'y arrête, et choisir une réponse mène à l'étape 5 avec son retour. */
await ouvrirSeance(2);
const SEL = '#chaines-lampadaire-pas-a-pas';
const cpt = () => p.$eval(`${SEL} [data-lpp="compte"]`, e => e.textContent.trim());
const anim = await p.evaluate(sel => {
  const b = document.querySelector(sel), s2 = document.getElementById('s2'), vol = document.getElementById('chlFixe');
  const voix = [];
  for (let k = 1; k <= 9; k++) voix.push('Audio/chaines_lampadaire_etape' + k);
  return { dansS2: !!b && s2.contains(b), avantAct2: !!b && !!(b.compareDocumentPosition(document.getElementById('act2')) & Node.DOCUMENT_POSITION_FOLLOWING),
    dispo: document.getElementById('chlDessin').getAttribute('data-dispo'), blocs: document.querySelectorAll('#chlDessin .chx-bloc').length,
    volet: !!vol && !vol.classList.contains('ouvert') && document.getElementById('chlFixeCorps').getBoundingClientRect().height === 0
      && !!vol.querySelector('object[data="Images/chaines_energie_information_lampadaire.svg"]'),
    objetHorsVolet: [...document.querySelectorAll('object[data="Images/chaines_energie_information_lampadaire.svg"]')].filter(o => !o.closest('#chlFixe')).length,
    large: document.documentElement.scrollWidth > innerWidth + 1, voix: b.getAttribute('data-lpp-voix') };
}, SEL);
const voixManquantes = [];
for (let k = 1; k <= 9; k++) for (const e of ['.ogg', '.mp3'])
  if (!fs.existsSync(path.join(ICI, 'Audio', 'chaines_lampadaire_etape' + k + e))) voixManquantes.push(k + e);
ok('41 · séance 2 : les deux chaînes animées, avant l\'activité 2, « Étape 1 / 9 », huit blocs ; à 390 px, en colonne, sans défilement de côté ; le schéma fixe dans un volet replié ; neuf prises de voix',
   anim.dansS2 && anim.avantAct2 && (await cpt()) === 'Étape 1 / 9' && anim.blocs === 8 && anim.dispo === 'etroit' && !anim.large
   && anim.volet && anim.objetHorsVolet === 0 && voixManquantes.length === 0,
   JSON.stringify(anim) + (voixManquantes.length ? ' · voix absentes : ' + voixManquantes.join(' ') : ''));
for (let k = 1; k < 4; k++) { await p.click(`${SEL} [data-lpp="suiv"]`); await p.waitForTimeout(80); }
const etape4 = await p.evaluate(() => ({ pred: !document.getElementById('chlPrediction').hidden,
  choix: document.querySelectorAll('#chlPrediction [data-choix]').length,
  question: getComputedStyle(document.querySelector('#chlDessin [data-id="question"]')).display !== 'none' }));
await p.click('#chlPrediction [data-choix="veille"]');
await p.waitForTimeout(120);
const apresVeille = { compte: await cpt(), retour: await p.evaluate(() => { const r = document.getElementById('chlRetour'); return r.hidden ? '' : r.className + ' | ' + r.textContent; }) };
await p.click(`${SEL} [data-lpp="prec"]`); await p.waitForTimeout(80);
await p.click('#chlPrediction [data-choix="pleine"]'); await p.waitForTimeout(120);
const apresPleine = await p.evaluate(() => document.getElementById('chlRetour').className);
ok('42 · étape 4 : la prédiction propose trois réponses ; en choisir une mène à l\'étape 5, avec son retour (la veille : « sans passage » ; pleine puissance : juste)',
   etape4.pred && etape4.choix === 3 && etape4.question && apresVeille.compte === 'Étape 5 / 9'
   && /faux/.test(apresVeille.retour) && /sans/.test(apresVeille.retour) && /juste/.test(apresPleine),
   JSON.stringify({ etape4, apresVeille, apresPleine }).slice(0, 220));
/* « Regarder » depuis l'étape 3 : la voix de l'étape 3, puis celle de l'étape 4… et le déroulé attend la réponse. */
await p.click(`${SEL} [data-lpp="zero"]`); await p.waitForTimeout(80);
for (let k = 1; k < 3; k++) { await p.click(`${SEL} [data-lpp="suiv"]`); await p.waitForTimeout(80); }
await p.click(`${SEL} [data-lpp="regarder"]`);
let attendu = '';
for (let t = 0; t < 60 && !attendu; t++) {
  await p.waitForTimeout(500);
  const e = await p.evaluate(sel => ({ c: document.querySelector(sel + ' [data-lpp="compte"]').textContent.trim(),
    b: document.querySelector(sel + ' [data-lpp="regarder"]').textContent.trim(), f: document.activeElement && document.activeElement.getAttribute('data-choix') }), SEL);
  if (e.c === 'Étape 4 / 9' && /Regarder/.test(e.b) && e.f) attendu = JSON.stringify(e);
  if (e.c === 'Étape 5 / 9') { attendu = 'PASSÉ : ' + JSON.stringify(e); break; }
}
await p.waitForTimeout(1500);
const toujours = await cpt();
await p.click('#chlPrediction [data-choix="pleine"]'); await p.waitForTimeout(200);
const reprend = { compte: await cpt(), bouton: await p.$eval(`${SEL} [data-lpp="regarder"]`, e => e.textContent.trim()) };
await p.click(`${SEL} [data-lpp="regarder"]`);           // pause
ok('43 · « Regarder » s\'arrête à l\'étape 4 tant que l\'élève n\'a pas répondu, met le premier choix sous le doigt, puis reprend à l\'étape 5',
   attendu && !attendu.startsWith('PASSÉ') && toujours === 'Étape 4 / 9' && reprend.compte === 'Étape 5 / 9' && /Pause/.test(reprend.bouton),
   (attendu || 'jamais arrêté à l\'étape 4') + ' · ' + JSON.stringify(reprend));
for (let k = 5; k < 9; k++) { await p.click(`${SEL} [data-lpp="suiv"]`); await p.waitForTimeout(80); }
const fin = await p.evaluate(() => {
  const t = document.getElementById('chlTache'), a = document.getElementById('chlVersAct2');
  return { tache: !t.hidden, cible: a.getAttribute('href') };
});
await p.click('#chlFixeBouton'); await p.waitForTimeout(80);
fin.ouvert = await p.evaluate(() => document.getElementById('chlFixeCorps').getBoundingClientRect().height > 100);
await p.click('#chlFixeBouton'); await p.waitForTimeout(80);
await p.evaluate(() => window.dispatchEvent(new Event('beforeprint')));   // comme une vraie impression : la fiche papier marque la séance
await p.emulateMedia({ media: 'print' });
fin.imprime = await p.evaluate(() => ({ schema: document.getElementById('chlFixeCorps').getBoundingClientRect().height > 100,
  anim: getComputedStyle(document.getElementById('chaines-lampadaire-pas-a-pas')).display === 'none' }));
await p.emulateMedia({ media: 'screen' });
await p.evaluate(() => window.dispatchEvent(new Event('afterprint')));
ok('44 · étape 9 « À toi » : le bouton mène à l\'activité 2 ; le schéma fixe s\'ouvre à la demande ; à l\'impression, le schéma fixe, pas l\'animation',
   (await cpt()) === 'Étape 9 / 9' && fin.tache && fin.cible === '#act2' && fin.ouvert && fin.imprime.schema && fin.imprime.anim, JSON.stringify(fin));
ok('40 · aucune erreur JS jusqu\'à la fin', err.length === 0, err.slice(0, 2).join(' | '));

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
