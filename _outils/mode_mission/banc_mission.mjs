// Banc du mode mission — joue le pilote (le lampadaire de 5e) comme un élève, à 390 px puis à 1 180 px.
//   node _outils/mode_mission/banc_mission.mjs
// Sortie 0 si tout passe, 1 sinon. Ne dépend d'aucun réseau.
import { chromium } from 'playwright';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const PAGE = path.resolve(ICI, '../../theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/5e/5e_C4.1/sequence_5e_C4.1-C4.8_lampadaire_intelligent.html');
let reussis = 0, total = 0;
const ok = (nom, cond, detail = '') => { total++; if (cond) reussis++; console.log((cond ? '✅ ' : '❌ ') + nom + (detail ? ' — ' + detail : '')); };

const b = await chromium.launch();
for (const [nom, vp] of [['390 px', { width: 390, height: 844 }], ['1 180 px', { width: 1180, height: 820 }]]) {
  const ctx = await b.newContext({ viewport: vp }); const p = await ctx.newPage();
  const err = []; p.on('pageerror', e => err.push(e.message));
  await p.goto(pathToFileURL(PAGE).href, { waitUntil: 'load' }); await p.waitForTimeout(400);
  const T = n => `[${nom}] ${n}`;

  const depart = await p.evaluate(() => ({ bouton: !!document.getElementById('btnMission'), ms: document.body.classList.contains('ms'),
    visibles: [...document.querySelectorAll('.ms-seul')].filter(e => e.offsetParent).length, etq: document.querySelectorAll('.ms-etq').length }));
  ok(T('1 · au chargement : le bouton est là, le mode est éteint, la page n\'est pas touchée'), depart.bouton && !depart.ms && depart.visibles === 0 && depart.etq === 0, JSON.stringify(depart));

  await p.click('#btnMission'); await p.waitForTimeout(300);
  const rail = () => p.evaluate(() => [...document.querySelectorAll('#msRail [data-k]')].map(x => x.getAttribute('aria-label').replace(/^Écran \d+ sur \d+ : /, '')));
  const r1 = await rail();
  ok(T('2 · la séance 1 se découpe en écrans : la séance, l\'atelier, le départ, les questions une à une, « je retiens »'),
     r1.length === 11 && /Séance 1/.test(r1[0]) && /^a\) Fonctions/.test(r1[3]) && /^Je retiens/.test(r1[10]), r1.length + ' écrans');
  const c0 = await p.evaluate(() => document.getElementById('msCompte').textContent);
  ok(T('2b · la barre compte les étoiles de la séance (6 questions vérifiables : 18 étoiles), pas celles de toute la séquence'), c0 === '0 / 18', c0);
  const etat = () => p.evaluate(() => ({ ou: document.getElementById('msOu').textContent, compte: document.getElementById('msCompte').textContent,
    retour: [...document.querySelectorAll('.ms-retour')].filter(e => e.offsetParent).map(e => e.textContent).join(' '),
    champs: [...document.querySelectorAll('.seance-panel.active fieldset.qcm-groupe')].filter(e => e.offsetParent).map(e => e.id) }));
  const jusqua = async debut => { for (let i = 0; i < 40; i++) { const e = await etat(); if (e.ou.startsWith(debut)) return e; await p.click('#msSuiv'); await p.waitForTimeout(160); } throw new Error('écran introuvable : ' + debut); };

  await jusqua('a) Fonctions');
  const vu = await p.evaluate(() => ({ etq: [...document.querySelectorAll('.ms-etq')].filter(e => e.offsetParent).length, grilles: [...document.querySelectorAll('#e1_1,#e1_2,.qcm-cles')].filter(e => e.offsetParent).length,
    labs: [...document.querySelectorAll('.ms-lab')].filter(e => e.offsetParent).map(e => e.textContent), large: document.documentElement.scrollWidth > innerWidth,
    cases: [...document.querySelectorAll('.ms-case')].filter(e => e.offsetParent).length, titre: document.querySelector('.ms-reserve-t').textContent }));
  ok(T('3 · la grille de boutons radio se joue en étiquettes : 4 cases, 6 étiquettes dont 2 leurres annoncés, la grille d\'origine cachée, pas de défilement de côté'),
     vu.etq === 1 && vu.grilles === 0 && vu.cases === 4 && vu.labs.length === 6 && /2 en trop/.test(vu.titre) && !vu.large, vu.titre + ' · ' + JSON.stringify(vu.labs));
  const cibles = await p.evaluate(() => Math.min(...[...document.querySelectorAll('.ms-lab,.ms-case,.ms-btn')].filter(e => e.offsetParent).map(e => e.getBoundingClientRect().height)));
  ok(T('4 · étiquettes, cases et boutons de navigation : 44 px de haut au moins'), cibles >= 44, Math.round(cibles) + ' px');

  const poser = async (i, t) => { await p.locator(`.ms-etq:visible .ms-lab:has-text("${t}")`).click(); await p.locator(`.ms-etq:visible .ms-case[data-i="${i}"]`).click(); };
  await poser(0, 'le panneau solaire'); await poser(1, 'le bloc de LED'); await poser(2, 'la batterie');
  // la quatrième au clavier : Entrée sur l'étiquette, Entrée sur la case
  await p.locator('.ms-etq:visible .ms-lab:has-text("la carte électronique")').focus(); await p.keyboard.press('Enter'); await p.locator('.ms-etq:visible .ms-case[data-i="3"]').focus(); await p.keyboard.press('Enter');
  const plein = await p.evaluate(() => ({ titre: document.querySelector('.ms-reserve-t').textContent, restent: [...document.querySelectorAll('.ms-lab')].filter(e => e.offsetParent).map(e => e.textContent) }));
  ok(T('5b · toutes les cases remplies : la réserve le dit, et les deux leurres y restent'), /appuie sur « Vérifier »/.test(plein.titre) && plein.restent.join('|') === 'le capteur de luminosité|le mât', plein.restent.join(' · '));
  const pose = await p.evaluate(() => ['e1_1', 'e1_2', 'e1_3', 'e1_4'].map(i => document.getElementById(i).value));
  ok(T('5 · poser une étiquette (au doigt comme au clavier) coche le bouton radio de la page'),
     pose.join('|') === 'le panneau solaire|le bloc de LED|la batterie|la carte électronique', pose.join(' · '));
  await p.click('#msVerif'); await p.waitForTimeout(250);
  const faux = await p.evaluate(() => ({ justes: document.querySelectorAll('.ms-case.juste').length, faux: document.querySelectorAll('.ms-case.faux').length }));
  await p.waitForTimeout(1000);
  const apres = await p.evaluate(() => ['e1_1', 'e1_2', 'e1_3', 'e1_4'].map(i => document.getElementById(i).value));
  ok(T('6 · vérifier : 2 justes restent en place, 2 fausses retournent dans la réserve, et la page le sait'),
     faux.justes === 2 && faux.faux === 2 && apres[0] && !apres[1] && !apres[2] && apres[3] && /Pas encore/.test((await etat()).retour), JSON.stringify(apres));
  const pq = (await etat()).retour;
  ok(T('6a · chaque erreur est expliquée : la paire fausse est nommée, et ce que la ligne demande est dit — sans donner la réponse'),
     /« le bloc de LED » ne va pas avec « Stocker l'énergie pour la nuit »/.test(pq) && /Stocker, c'est garder/.test(pq) && /Éclairer, c'est produire/.test(pq) && !/la batterie va|→/.test(pq), pq.slice(0, 150));
  const mission = () => p.evaluate(() => JSON.parse(localStorage.getItem(Object.keys(localStorage).find(k => k.startsWith('mission:')))));
  const pret = () => p.waitForSelector('#msVerif:not([aria-disabled])', { timeout: 4000 });
  const bouton = await p.evaluate(() => ({ bloque: document.getElementById('msVerif').getAttribute('aria-disabled'), texte: document.getElementById('msVerif').textContent }));
  await p.click('#msVerif'); const m1 = await mission();
  ok(T('6b · après une erreur, « Vérifier » souffle 2 s (« Relis d\'abord… ») : un appui de plus ne compte pas ; les erreurs se comptent réponse par réponse'),
     bouton.bloque === 'true' && /Relis/.test(bouton.texte) && m1.essais['act1#0.0'] === 1 && m1.erreurs['act1#0.0'] === 2, JSON.stringify([bouton.texte, m1.essais, m1.erreurs]));

  // glisser-déposer : « la batterie » vers la case 2
  const src = await p.locator('.ms-etq:visible .ms-lab:has-text("la batterie")').boundingBox(), dst = await p.locator('.ms-etq:visible .ms-case[data-i="1"]').boundingBox();
  await p.mouse.move(src.x + src.width / 2, src.y + src.height / 2); await p.mouse.down(); await p.mouse.move(src.x + 20, src.y - 20, { steps: 4 }); await p.mouse.move(dst.x + dst.width / 2, dst.y + dst.height / 2, { steps: 8 }); await p.mouse.up(); await p.waitForTimeout(150);
  const glisse = await p.evaluate(() => document.getElementById('e1_2').value);
  if (glisse !== 'la batterie') await poser(1, 'la batterie');
  ok(T('7 · une étiquette se glisse aussi jusqu\'à sa case'), glisse === 'la batterie' || vp.width < 500, glisse || '(case hors de l\'écran à 390 px : posée au toucher)');
  await poser(2, 'le bloc de LED'); await pret(); await p.click('#msVerif'); await p.waitForTimeout(250);
  let e = await etat();
  ok(T('8 · deux erreurs sur quatre étiquettes, puis tout juste : 2 étoiles, et le message valorise l\'erreur corrigée'), /^2 \//.test(e.compte) && /corrigé tes erreurs/.test(e.retour), e.compte);

  await p.click('#msSuiv'); await p.waitForTimeout(200); e = await etat();
  ok(T('9 · écran suivant : une seule question à l\'écran, et le message de l\'écran précédent n\'y traîne pas'), e.champs.join() === 'e1_5' && e.retour.trim() === '', e.champs.join());
  await p.locator('#e1_5 label:has-text("détecteur de mouvement")').click(); await p.click('#msVerif'); await p.waitForTimeout(200); e = await etat();
  ok(T('10 · question à choix juste du premier coup : 3 étoiles'), /^5 \//.test(e.compte) && /premier coup/.test(e.retour), e.compte);

  await p.click('#msSuiv'); await p.waitForTimeout(160);
  const mauvais = p.locator('#e1_m1 .qcm-option', { hasNotText: 'acier galvanisé' });
  await mauvais.nth(0).locator('label').click(); await p.click('#msVerif'); await p.waitForTimeout(150);
  const pq1 = (await etat()).retour;
  const aide0 = await p.evaluate(() => [...document.querySelectorAll('#act1 details.aide1, #act1 details.aide')].some(d => d.open));
  await pret(); await mauvais.nth(1).locator('label').click(); await p.click('#msVerif'); await p.waitForTimeout(150);
  const aide2 = await p.evaluate(() => { const d = document.querySelector('#act1 details.ms-pousse'); return { ouverte: !!d && d.open, vue: !!d && !!d.offsetParent }; });
  e = await etat();
  ok(T('10b · deuxième essai manqué sur le même écran : le coup de pouce de l\'activité s\'ouvre sous le message (pas au premier)'), !aide0 && aide2.ouverte && aide2.vue && /coup de pouce/.test(e.retour), e.retour.slice(0, 90));
  ok(T('10b\' · une mauvaise réponse à choix reçoit son pourquoi (ce matériau, dehors) — sans la bonne réponse'), /pourrit|casse|ramollit/.test(pq1 + e.retour) && !/acier galvanisé/.test(pq1 + e.retour), (pq1 || e.retour).slice(0, 110));
  await pret(); await p.locator('#e1_m1 label:has-text("acier galvanisé")').first().click(); await p.click('#msVerif'); await p.waitForTimeout(160); e = await etat();
  ok(T('10c · deux erreurs sur une question à choix, puis juste : 1 étoile (essayer toutes les réponses ne rapporte pas)'), /^6 \//.test(e.compte), e.compte);
  for (const [id, t] of [['e1_m2', 'polycarbonate'], ['e1_m3', 'aluminium'], ['e1_m4', 'cuivre']]) {
    await p.click('#msSuiv'); await p.waitForTimeout(160); await p.locator(`#${id} label:has-text("${t}")`).first().click(); await p.click('#msVerif'); await p.waitForTimeout(160); }
  await p.click('#msSuiv'); await p.waitForTimeout(200);
  await p.fill('#e1_just', 'Le sel des embruns fait rouiller l’acier nu, le zinc le protège.'); await p.click('#msVerif'); await p.waitForTimeout(250);
  const fin = await p.evaluate(() => ({ fb: document.getElementById('fb1').textContent, vu: !!document.getElementById('fb1').offsetParent, compte: document.getElementById('msCompte').textContent }));
  ok(T('11 · la dernière question de l\'activité lance la vérification de la page : son message s\'affiche (9 / 9)'), /^9 \/ 9/.test(fin.fb) && fin.vu && fin.compte === '15 / 18', fin.fb.slice(0, 60) + ' · ' + fin.compte);

  await p.emulateMedia({ media: 'print' });
  const papier = await p.evaluate(() => ({ pied: !!document.querySelector('.ms-pied').offsetParent, etq: [...document.querySelectorAll('.ms-etq')].filter(x => x.offsetParent).length,
    radios: !!document.getElementById('e1_1').offsetParent, tout: [...document.querySelectorAll('#s1 fieldset.qcm-groupe')].every(x => x.offsetParent) }));
  await p.emulateMedia({ media: 'screen' });
  ok(T('12 · à l\'impression, en plein mode mission : la page entière, ses boutons radio, sans la barre ni les étiquettes'), !papier.pied && papier.etq === 0 && papier.radios && papier.tout, JSON.stringify(papier));

  await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400); e = await etat();
  ok(T('13 · rechargement : le mode, l\'écran et les étoiles reviennent'), await p.evaluate(() => document.body.classList.contains('ms')) && /5 sur 5/.test(e.ou) && e.compte === '15 / 18', e.ou.slice(0, 40));
  await p.evaluate(() => document.querySelector('.seance-tab[data-panel="s3"]').click()); await p.waitForTimeout(250);
  const r3 = await rail();
  ok(T('14 · changer de séance par son onglet : les écrans de la séance 3, le simulateur avec ses questions'), r3.length === 9 && r3.some(x => /simulateur/.test(x)), r3.length + ' écrans');
  await p.evaluate(() => document.querySelector('.seance-tab[data-panel="s6"]').click()); await p.waitForTimeout(250);
  const r6 = await rail(), ib = r6.findIndex(x => /bilan personnel/i.test(x));
  await p.click(`#msRail [data-k="${ib}"]`); await p.waitForTimeout(200);
  const bil = await p.evaluate(() => { const b = [...document.querySelectorAll('.ms-bilan')].find(x => x.offsetParent); return b ? b.textContent : ''; });
  ok(T('14b · au bilan : les étoiles de toute la séquence, et les erreurs corrigées en route (2 étiquettes + 2 choix)'), /15 étoiles sur \d{2,3}/.test(bil) && /corrigé 4 erreurs/.test(bil), bil.slice(0, 110));
  await p.evaluate(() => document.querySelector('.seance-tab[data-panel="s3"]').click()); await p.waitForTimeout(250);
  await p.click('#msQuitter'); await p.waitForTimeout(200);
  const sortie = await p.evaluate(() => ({ ms: document.body.classList.contains('ms'), seuls: [...document.querySelectorAll('.ms-seul')].filter(x => x.offsetParent).length,
    tout: [...document.querySelectorAll('.seance-panel.active fieldset.qcm-groupe, .seance-panel.active .consigne, .seance-panel.active details.correction')].every(x => x.offsetParent), check: !!document.querySelector('.seance-panel.active [data-check]').offsetParent }));
  ok(T('15 · retour à la page complète : tout réapparaît, plus rien de la mission à l\'écran'), !sortie.ms && sortie.seuls === 0 && sortie.tout && sortie.check, JSON.stringify(sortie));
  const avantEff = await p.evaluate(() => Object.keys(JSON.parse(localStorage.getItem(Object.keys(localStorage).find(k => k.startsWith('mission:')))).etoiles).length);
  await p.evaluate(() => { localStorage.removeItem(KEY); }); await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
  const apresEff = await p.evaluate(() => { const m = JSON.parse(localStorage.getItem(Object.keys(localStorage).find(k => k.startsWith('mission:')))); return Object.keys(m.etoiles).length + Object.keys(m.fait).length; });
  ok(T('16 · « Effacer ma sauvegarde » efface aussi les étoiles de la mission (poste partagé)'), avantEff > 0 && apresEff === 0, avantEff + ' → ' + apresEff);
  ok(T('17 · aucune erreur JavaScript'), err.length === 0, err.slice(0, 2).join(' | '));
  await ctx.close();
}
await b.close();
console.log(`══ mode mission : ${reussis} / ${total} tests réussis ══`);
process.exit(reussis === total ? 0 : 1);
