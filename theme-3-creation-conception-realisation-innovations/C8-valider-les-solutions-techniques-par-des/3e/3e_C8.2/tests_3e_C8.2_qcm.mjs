import { chromium } from 'playwright';
const f = process.argv[2];
const b = await chromium.launch();
const p = await b.newPage();
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => fail.push(r.url()));
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });
const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
await p.goto('file://' + f, { waitUntil: 'load' }); await p.waitForTimeout(500);

ok('charge sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
ok('aucune requête échouée', fail.length === 0, fail.slice(0, 2).join(' | '));

// ── la banque ──────────────────────────────────────────────────────────────
const banque = await p.evaluate(() => QUESTIONS.map(q => ({
  c: q.c, n: q.n, r: q.r, no: q.o.length, nd: q.d.filter(x => x).length,
  vide: q.d[q.r] === '', img: !!q.img,
  champs: ['q', 'expl', 'ex', 'err', 'ret'].every(k => (q[k] || '').trim().length > 0),
})));
ok('30 questions', banque.length === 30, String(banque.length));
ok('4 options par question', banque.every(q => q.no === 4));
ok('3 réfutations par question', banque.every(q => q.nd === 3));
ok('la bonne réponse n’a pas de réfutation', banque.every(q => q.vide));
ok('tous les champs du gabarit sont remplis', banque.every(q => q.champs));
ok('aucune image héritée du lot voisin', banque.every(q => !q.img));
const notions = new Set(banque.map(q => q.n));
ok('30 notions distinctes', notions.size === 30, String(notions.size));

const parCode = {};
banque.forEach(q => parCode[q.c] = (parCode[q.c] || 0) + 1);
ok('20 questions sur 3e_C8.2', parCode['3e_C8.2'] === 20, JSON.stringify(parCode));
ok('10 questions sur 3e_C3.4', parCode['3e_C3.4'] === 10, JSON.stringify(parCode));
ok('les deux codes dépassent le seuil de 5 questions évaluables',
   Object.values(parCode).every(v => v >= 5));

const rep = [0, 0, 0, 0]; banque.forEach(q => rep[q.r]++);
ok('bonnes réponses réparties sur les 4 positions', rep.every(v => v >= 7),
   rep.join('/'));

// ── longueur : la bonne réponse ne doit pas se voir ────────────────────────
const biais = await p.evaluate(() => {
  let detachees = 0, somme = 0;
  QUESTIONS.forEach(q => {
    const L = q.o.map(o => o.length), b = L[q.r];
    const a = L.filter((_, i) => i !== q.r);
    if (b > Math.max(...a) + 8 || b < Math.min(...a) - 8) detachees++;
    somme += b - a.reduce((s, x) => s + x, 0) / 3;
  });
  return { detachees, moyen: somme / QUESTIONS.length };
});
ok('aucune bonne réponse détachée par sa longueur', biais.detachees === 0,
   String(biais.detachees));
ok('écart moyen de longueur sous 5 caractères', Math.abs(biais.moyen) < 5,
   biais.moyen.toFixed(1));

// ── parcours réel : une bonne réponse, une mauvaise ────────────────────────
const r0 = await p.evaluate(() => QUESTIONS[0].r);
await p.locator('#qOptions button').nth(r0).click();
await p.click('#btnValider');
await p.waitForTimeout(200);
ok('une bonne réponse est déclarée correcte',
   (await p.textContent('#corrBloc')).includes('Correct'),
   (await p.textContent('#corrBloc')).slice(0, 40));
ok('la correction déplie les trois réfutations',
   (await p.$$eval('#corrBloc .dist-liste li', n => n.length)) === 3);
ok('la correction porte un « À retenir »',
   (await p.textContent('#corrBloc')).includes('À retenir'));

await p.click('#btnSuiv');
const r1 = await p.evaluate(() => QUESTIONS[1].r);
await p.locator('#qOptions button').nth((r1 + 1) % 4).click();
await p.click('#btnValider');
await p.waitForTimeout(200);
ok('une mauvaise réponse est déclarée incorrecte',
   (await p.textContent('#corrBloc')).includes('Incorrect'),
   (await p.textContent('#corrBloc')).slice(0, 40));

// ── règle n°188 : les deux confirmations en deux temps ────────────────────
// Ajoutés le 29/08. Le test précédent affirmait « aucune boîte modale » sans
// jamais emprunter les deux chemins qui en ouvraient une.
await p.evaluate(() => { etat.reponses = QUESTIONS.map(() => null);
  etat.validees = QUESTIONS.map(() => false); etat.courante = 0; rendreTout(); });
await p.click('#btnValider'); await p.waitForTimeout(120);
ok('valider sans réponse n’ouvre aucune boîte modale', dlg.length === 0, dlg.join(' | '));
ok('valider sans réponse annonce et ne valide pas encore',
   (await p.textContent('#savedNote')).includes('non répondue')
   && !(await p.evaluate(() => etat.validees[0])),
   await p.textContent('#savedNote'));
await p.click('#btnValider'); await p.waitForTimeout(120);
ok('le second clic valide bien', await p.evaluate(() => etat.validees[0]));

await p.evaluate(() => { etat.reponses = QUESTIONS.map(q => q.r);
  etat.validees = QUESTIONS.map(() => true); rendreTout(); save(); });
await p.evaluate(() => document.getElementById('btnTerminer').click());
await p.waitForTimeout(150);
await p.evaluate(() => document.getElementById('btnRecommencer').click());
await p.waitForTimeout(120);
ok('« recommencer » n’ouvre aucune boîte modale', dlg.length === 0, dlg.join(' | '));
ok('« recommencer » demande confirmation sans rien effacer',
   (await p.evaluate(() => etat.validees.filter(Boolean).length)) === 30,
   String(await p.evaluate(() => etat.validees.filter(Boolean).length)));
await p.evaluate(() => document.getElementById('btnRecommencer').click());
await p.waitForTimeout(150);
ok('le second clic remet bien à zéro',
   (await p.evaluate(() => etat.validees.filter(Boolean).length)) === 0,
   String(await p.evaluate(() => etat.validees.filter(Boolean).length)));

// ── les modes du moteur ne bloquent plus la page ───────────────────────────
await p.evaluate(() => document.querySelector('[data-mode="marquees"]').click());
await p.waitForTimeout(150);
ok('le mode « marquées » vide n’ouvre aucune boîte modale', dlg.length === 0,
   dlg.join(' | '));
ok('il affiche un bandeau à la place',
   (await p.textContent('#savedNote')).includes('marquée'),
   await p.textContent('#savedNote'));
await p.evaluate(() => document.querySelector('[data-mode="complet"]').click());

// ── les 30 questions en bonne réponse : score plein ────────────────────────
await p.evaluate(() => {
  etat.reponses = QUESTIONS.map(q => q.r);
  etat.validees = QUESTIONS.map(() => true);
  rendreTout(); save();
});
await p.waitForTimeout(200);
ok('30 bonnes réponses donnent 100 %', (await p.textContent('#dScore')).includes('100'),
   await p.textContent('#dScore'));
ok('la note affichée est 20/20', (await p.textContent('#dNote')).includes('20'),
   await p.textContent('#dNote'));

// ── navigation et persistance ──────────────────────────────────────────────
ok('le lien vers la séquence pointe le bon fichier',
   (await p.getAttribute('#navharm a:nth-child(2)', 'href')) === 'sequence_3e_C8.2_mat-de-la-station.html',
   await p.getAttribute('#navharm a:nth-child(2)', 'href'));
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
ok('la progression survit au rechargement',
   (await p.textContent('#dRep')) === '30', await p.textContent('#dRep'));
ok('aucune boîte modale sur tout le parcours', dlg.length === 0, dlg.join(' | '));

const r = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${r} / ${T.length}`);
await b.close(); process.exit(r === T.length ? 0 : 1);
