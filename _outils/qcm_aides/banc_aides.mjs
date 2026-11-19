// banc_aides.mjs — un QCM qui aide avant de corriger, joué au navigateur (règles d'or n°337 et n°339, 17/11/2026).
//
//   node _outils/qcm_aides/banc_aides.mjs <qcm.html> […]     (sans argument : chaque QCM qui porte les aides)
//
// Pour chaque QCM, à 390 px, question par question : une réponse FAUSSE, puis « Valider ». Refus (sortie 1) si :
//   A1  l'indice n'apparaît pas (« 💡 Indice »), ou la bonne réponse est dite (« Bonne réponse ») ou marquée en vert ;
//   A2  « 💡💡 Un indice de plus » ne montre pas la règle à appliquer ;
//   A3  « 📖 Voir la correction complète » ne montre pas la correction (la bonne réponse, en vert) ;
//   A4  une question rangée dans un piège n'affiche pas « Réviser ce piège » sous l'indice ;
//   A5  le bilan ne liste pas les pièges ratés, ou son bouton n'ouvre pas le mode piège (ses seules questions) ;
//   A6  le compte des erreurs par piège ne survit pas au rechargement ;
//   A7  la carte « Avant de commencer » manque, ou une erreur JavaScript survient ;
//   A8  la question 1, fausse puis réussie après « Réessayer », ne donne pas deux notes — « Premier essai » (0) et
//       « Après aides » (1 sur N) — au tableau de bord après rechargement, et dans le résultat (19/11/2026).
// Sortie 0 tout passe · 1 un refus · 2 rien lu (n°299).
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const RACINE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
let pages = process.argv.slice(2).filter(a => !a.startsWith('--')).map(a => path.resolve(a));
if (!pages.length) {
  const voir = d => fs.readdirSync(d, { withFileTypes: true }).flatMap(e => e.name.startsWith('.') || e.name.startsWith('_archive') || e.name === 'node_modules' ? [] :
    e.isDirectory() ? voir(path.join(d, e.name)) : /^qcm.*\.html$/.test(e.name) ? [path.join(d, e.name)] : []);
  pages = fs.readdirSync(RACINE).filter(n => n.startsWith('theme-')).flatMap(t => voir(path.join(RACINE, t)))
    .filter(f => fs.readFileSync(f, 'utf-8').includes('function questionsDuPiege'));
}
if (!pages.length) { console.log('✘ aucun QCM avec les aides : rien n\'a été vérifié'); process.exit(2); }

const b = await chromium.launch();
let refusTotal = 0;
for (const PAGE of pages) {
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 } }); const p = await ctx.newPage();
  const err = []; p.on('pageerror', e => err.push(e.message));
  p.on('dialog', d => d.accept());
  const refus = [];
  await p.goto(pathToFileURL(PAGE).href, { waitUntil: 'load' });
  await p.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
  await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(200);
  if (!(await p.$('#trois-lignes'))) refus.push('A7 pas de carte « Avant de commencer »');
  const pose = await p.evaluate(() => typeof piege === 'function' && typeof questionsDuPiege === 'function');
  if (!pose) {
    console.log(`❌ ${path.relative(RACINE, PAGE)}\n   · A7 les aides et les pièges ne sont pas posés (poser.py)`);
    refusTotal++; await ctx.close(); continue;
  }
  const N = await p.evaluate(() => QUESTIONS.length);
  let dansPiege = 0;
  for (let i = 0; i < N; i++) {
    const info = await p.evaluate(i => { etat.courante = i; choixTemp = null; montrerEcran('q'); rendreTout();
      const Q = QUESTIONS[i]; return { faux: Q.r === 0 ? 1 : 0, f: piege(i) }; }, i);
    await p.locator('#qOptions .option').nth(info.faux).click();
    await p.click('#btnValider');
    const r1 = await p.evaluate(() => ({ t: document.getElementById('corrBloc').innerText, vert: !!document.querySelector('#qOptions .option.bonne') }));
    const ou = `q${i + 1}`;
    if (!r1.t.includes('💡 Indice')) refus.push(`A1 ${ou} : pas d'indice après une réponse fausse`);
    if (r1.t.includes('Bonne réponse') || r1.vert) refus.push(`A1 ${ou} : la bonne réponse se voit pendant l'indice`);
    if (info.f) { dansPiege++; if (!r1.t.includes('Réviser ce piège')) refus.push(`A4 ${ou} : pas de « Réviser ce piège »`); }
    if (await p.$('#btnIndice2')) {
      await p.click('#btnIndice2');
      const t2 = await p.evaluate(() => document.getElementById('corrBloc').innerText);
      if (!t2.includes('La règle à appliquer')) refus.push(`A2 ${ou} : le second indice ne dit pas la règle`);
    } else refus.push(`A2 ${ou} : pas de bouton « Un indice de plus »`);
    await p.click('#btnVoirCorr');
    const r3 = await p.evaluate(() => ({ t: document.getElementById('corrBloc').innerText, vert: !!document.querySelector('#qOptions .option.bonne') }));
    if (!r3.t.includes('Bonne réponse') || !r3.vert) refus.push(`A3 ${ou} : la correction complète ne s'ouvre pas`);
  }
  // le bilan, puis le mode piège
  await p.click('#btnTerminer'); await p.waitForTimeout(150);
  const bil = await p.evaluate(() => ({ t: document.body.innerText.includes('Tes pièges'), n: document.querySelectorAll('#ecranResultat [data-piege]').length }));
  if (dansPiege && (!bil.t || !bil.n)) refus.push('A5 le bilan ne liste pas les pièges ratés');
  if (bil.n) {
    await p.locator('#ecranResultat [data-piege]').first().click(); await p.waitForTimeout(150);
    const m = await p.evaluate(() => { const l = listeActive(), f = etat.sousListe || etat.piege;
      return { mode: etat.mode, ok: l.length >= 3 && l.every(i => piege(i) === piege(l[0])) }; });
    if (m.mode !== 'piege' || !m.ok) refus.push(`A5 le bouton du bilan n'ouvre pas le mode piège (${m.mode})`);
  }
  // le compte des erreurs par piège survit au rechargement
  const avant = await p.evaluate(() => JSON.stringify(etat.erreursPiege || {}));
  await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(200);
  const apres = await p.evaluate(() => JSON.stringify(etat.erreursPiege || {}));
  if (dansPiege && (avant === '{}' || avant !== apres)) refus.push('A6 le compte des erreurs par piège ne survit pas au rechargement');
  // le premier essai : la question 1, fausse au premier essai, réussie après l'aide — deux notes, et elles restent
  const note = k => (Math.round(k / N * 20 * 10) / 10).toFixed(1).replace('.', ',') + ' /20';
  await p.evaluate(() => { montrerEcran('q'); setMode('complet'); etat.courante = 0; choixTemp = null; rendreTout(); });
  if (await p.$('#btnRetenter')) {
    await p.click('#btnRetenter');
    const r = await p.evaluate(() => QUESTIONS[0].r);
    await p.locator('#qOptions .option').nth(r).click();
    await p.click('#btnValider');
    await p.waitForFunction(() => etat.validees[0] === true, null, { timeout: 5000 }).catch(() => {});
    await p.waitForTimeout(300);   /* le navigateur range la sauvegarde avant le rechargement (sous charge, il lui faut ce temps) */
    await p.reload({ waitUntil: 'load' });
    await p.waitForFunction(() => (document.getElementById('dNote')?.textContent || '—').indexOf('—') < 0, null, { timeout: 5000 }).catch(() => {});
    const d = await p.evaluate(() => ({ un: document.getElementById('dNote1')?.textContent, fin: document.getElementById('dNote')?.textContent }));
    if (d.un !== note(0) || d.fin !== note(1)) refus.push(`A8 premier essai ${d.un} / après aides ${d.fin} (attendu ${note(0)} / ${note(1)}), après rechargement`);
    await p.click('#btnTerminer'); await p.waitForTimeout(150);
    const t = await p.evaluate(() => document.getElementById('rEssais')?.innerText || '');
    if (!t.includes('Premier essai') || !t.includes(note(0)) || !t.includes('Après aides') || !t.includes(note(1)))
      refus.push('A8 le résultat ne donne pas les deux notes : ' + JSON.stringify(t.slice(0, 120)));
  } else refus.push('A8 pas de « Réessayer » sur la question 1');
  if (err.length) refus.push('A7 erreur JavaScript : ' + err[0]);
  const nom = path.relative(RACINE, PAGE);
  if (refus.length) { refusTotal++; console.log(`❌ ${nom}`); refus.slice(0, 8).forEach(r => console.log('   · ' + r)); if (refus.length > 8) console.log(`   · … ${refus.length - 8} de plus`); }
  else console.log(`✅ ${nom} — ${N} questions, ${dansPiege} dans un piège, ${bil.n} piège(s) au bilan`);
  await ctx.close();
}
await b.close();
console.log(`${pages.length} QCM joué(s) · ${refusTotal} refusé(s)`);
process.exit(refusTotal ? 1 : 0);
