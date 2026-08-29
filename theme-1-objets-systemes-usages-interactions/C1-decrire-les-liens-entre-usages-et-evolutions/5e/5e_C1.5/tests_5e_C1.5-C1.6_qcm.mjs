import { chromium } from 'playwright';
const f = process.argv[2], c1 = process.argv[3], c2 = process.argv[4], seq = process.argv[5];
// combien de questions chaque code doit porter — 20/10 par défaut, 15/15 pour un lot à deux codes
const n1 = parseInt(process.argv[6] || '20', 10), n2 = parseInt(process.argv[7] || '10', 10);
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

const banque = await p.evaluate(() => QUESTIONS.map(q => ({
  c: q.c, n: q.n, r: q.r, no: q.o.length, nd: q.d.filter(x => x).length,
  vide: q.d[q.r] === '', img: !!q.img,
  champs: ['q', 'expl', 'ex', 'err', 'ret'].every(k => (q[k] || '').trim().length > 0),
})));
ok('30 questions', banque.length === 30, String(banque.length));
ok('4 options par question', banque.every(q => q.no === 4));
ok('3 réfutations par question', banque.every(q => q.nd === 3));
ok('la bonne réponse n’a pas de réfutation', banque.every(q => q.vide));
ok('tous les champs du gabarit remplis', banque.every(q => q.champs));
ok('aucune image héritée du lot voisin', banque.every(q => !q.img));
ok('30 notions distinctes', new Set(banque.map(q => q.n)).size === 30,
   String(new Set(banque.map(q => q.n)).size));

const parCode = {};
banque.forEach(q => parCode[q.c] = (parCode[q.c] || 0) + 1);
ok(n1 + ' questions sur ' + c1, parCode[c1] === n1, JSON.stringify(parCode));
ok(n2 + ' questions sur ' + c2, parCode[c2] === n2, JSON.stringify(parCode));
ok('les deux codes dépassent le seuil de 5 questions',
   Object.values(parCode).every(v => v >= 5) && Object.keys(parCode).length === 2);

const rep = [0, 0, 0, 0]; banque.forEach(q => rep[q.r]++);
ok('bonnes réponses réparties sur les 4 positions', rep.every(v => v >= 7), rep.join('/'));

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
ok('aucune bonne réponse détachée par sa longueur', biais.detachees === 0, String(biais.detachees));
ok('écart moyen de longueur sous 5 caractères', Math.abs(biais.moyen) < 5, biais.moyen.toFixed(1));

const r0 = await p.evaluate(() => QUESTIONS[0].r);
await p.locator('#qOptions button').nth(r0).click();
await p.click('#btnValider'); await p.waitForTimeout(150);
ok('une bonne réponse est déclarée correcte', (await p.textContent('#corrBloc')).includes('Correct'));
ok('la correction déplie les trois réfutations',
   (await p.$$eval('#corrBloc .dist-liste li', n => n.length)) === 3);
ok('la correction porte un « À retenir »', (await p.textContent('#corrBloc')).includes('À retenir'));

await p.click('#btnSuiv');
const r1 = await p.evaluate(() => QUESTIONS[1].r);
await p.locator('#qOptions button').nth((r1 + 1) % 4).click();
await p.click('#btnValider'); await p.waitForTimeout(150);
ok('une mauvaise réponse est déclarée incorrecte', (await p.textContent('#corrBloc')).includes('Incorrect'));

// ── règle n°188 : les deux confirmations en deux temps ────────────────────
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

await p.evaluate(() => document.querySelector('[data-mode="marquees"]').click());
await p.waitForTimeout(150);
ok('le mode « marquées » vide n’ouvre aucune boîte modale', dlg.length === 0, dlg.join(' | '));
ok('il affiche un bandeau à la place', (await p.textContent('#savedNote')).includes('marquée'),
   await p.textContent('#savedNote'));
await p.evaluate(() => document.querySelector('[data-mode="complet"]').click());

await p.evaluate(() => { etat.reponses = QUESTIONS.map(q => q.r);
  etat.validees = QUESTIONS.map(() => true); rendreTout(); save(); });
await p.waitForTimeout(150);
ok('30 bonnes réponses donnent 100 %', (await p.textContent('#dScore')).includes('100'),
   await p.textContent('#dScore'));
ok('la note affichée est 20/20', (await p.textContent('#dNote')).includes('20'),
   await p.textContent('#dNote'));
ok('le lien vers la séquence pointe le bon fichier',
   (await p.getAttribute('#navharm a:nth-child(2)', 'href')) === seq,
   await p.getAttribute('#navharm a:nth-child(2)', 'href'));
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
ok('la progression survit au rechargement', (await p.textContent('#dRep')) === '30',
   await p.textContent('#dRep'));
ok('aucune boîte modale sur tout le parcours', dlg.length === 0, dlg.join(' | '));

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close(); process.exit(n === T.length ? 0 : 1);
