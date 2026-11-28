/* tests_3e_C6.1-C6.3.mjs — « Programmer l'alerte », rejouable.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport de ce lot portait 17 coches et ne citait aucun script : une dette
 * honnête (règle d'or n°259). C'était le lot en tête de la file publiée par
 * `_outils/controle_rapports_tests.py`.
 *
 * CE QUE CETTE SUITE ÉPROUVE EN PROPRE
 * ------------------------------------
 * Ce lot ne vérifie pas des réponses à des menus déroulants : il **exécute le
 * programme que l'élève a écrit** (le petit Python de la page, `banc-python`,
 * source `_outils/banc_python/`). Audit du 21/11/2026 : l'activité 4 cherchait
 * sept motifs dans le TEXTE du programme — un programme juste écrit avec des
 * apostrophes obtenait 5 / 7, un programme faux à 118 obtenait 7 / 7. Depuis le
 * 22/11/2026 (règle d'or n°333, appliquée ; n°373 et n°374, en essai) :
 *
 *   · l'activité 3 lit la VALEUR de `SEUIL_ORANGE` dans le programme exécuté
 *     (60.5 n'est pas 60) et vérifie son effet à 55 et 61 km/h ;
 *   · l'activité 4 exécute le programme sur dix vents et compare le message, la
 *     sirène et le gyrophare au cahier des charges de la version 2 ;
 *   · l'activité 5 sépare « mes prévisions » et « essais de ma version », et un
 *     essai ne vaut que pour la version qu'il a essayée (son empreinte).
 *
 * Les critères de recette de l'audit sont recopiés dans les tests 14 à 17
 * (relire-un-audit-externe, § 2).
 *
 * CE QU'ELLE NE RECOPIE PAS — Y COMPRIS LE PROGRAMME
 * --------------------------------------------------
 * Le programme v2 n'est pas écrit ici : il est **lu dans la correction que la
 * page publie elle-même** (`#act4 details.correction pre`), puis collé dans
 * l'éditeur. Si la correction et le vérificateur divergeaient un jour, cette
 * suite le dirait — ce qu'un programme recopié dans le test ne pourrait pas
 * faire (règle d'or n°268).
 *
 * Les réponses attendues sont extraites des `CHECKS` selon les cinq conventions
 * de ce lot : `att = {…}`, `$("id").value === "…"`, `.indexOf("…") === 0`
 * (préfixe), `num("id") === N`, et la prose jugée par mots-clés — dont la suite
 * ne prétend montrer que l'ouverture aux conditions déclarées.
 *
 * Usage, depuis ce dossier :
 *   node tests_3e_C6.1-C6.3.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

/* Règle d'or n°300 (révision de la séquence, 11/11/2026) : les questions de la page sont des groupes de boutons
   radio (fieldset.qcm-groupe) qui portent leur valeur. selectOption et fill visant un groupe cochent la
   proposition qui porte cette valeur — la leçon de la vague du 20/09 : on vise la VALEUR, jamais la
   position. Rien d'autre du banc ne change. */
function _groupesRadio(page){
  const origIV = page.inputValue.bind(page);
  page.inputValue = async (sel, ...reste) => {
    const groupe = typeof sel === 'string' && await page.evaluate(s => { const e = document.querySelector(s); return !!(e && e.tagName === 'FIELDSET' && e.classList.contains('qcm-groupe')); }, sel);
    return groupe ? page.evaluate(s => document.querySelector(s).value, sel) : origIV(sel, ...reste);
  };
  for (const nom of ['selectOption', 'fill']) {
    const orig = page[nom].bind(page);
    page[nom] = async (sel, val, ...reste) => {
      const groupe = typeof sel === 'string' && await page.evaluate(s => { const e = document.querySelector(s); return !!(e && e.tagName === 'FIELDSET' && e.classList.contains('qcm-groupe')); }, sel);
      if (!groupe) return orig(sel, val, ...reste);
      // comme Playwright sur un <select> : une chaîne vise la valeur OU le libellé ; {index}, {value}, {label} sont acceptés
      const v = (val && typeof val === 'object') ? val : { label: String(val), value: String(val) };
      const ok = await page.evaluate(([s, v]) => {
        const e = document.querySelector(s); const inputs = [...e.querySelectorAll('input[type=radio]')];
        const lib = i => (e.querySelector('label[for="' + i.id + '"]') || {}).textContent?.trim();
        const c = v.index !== undefined ? inputs[v.index]
          : inputs.find(i => i.value === v.value) || inputs.find(i => lib(i) === v.label);
        if (!c) return false;
        c.checked = true; c.dispatchEvent(new Event('change', {bubbles: true})); return true;
      }, [sel, v]);
      if (!ok) throw new Error('aucune proposition \u00ab ' + JSON.stringify(v) + ' \u00bb dans ' + sel);
    };
  }
  return page;
}
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const SEQ = path.join(ICI, 'sequence_3e_C6.1-C6.3_programmer_alerte.html');
const QCM = path.join(ICI, 'qcm_3e_C6.1-C6.3_programmer_alerte.html');

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();

/* ════════════════ CODELAB + SÉQUENCE (25 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = _groupesRadio(await ctx.newPage());
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => { if (!/fonts\.g/.test(r.url())) fail.push(r.url()); });
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

await p.goto(pathToFileURL(SEQ).href, { waitUntil: 'load' });
// Révision du 11/11/2026 : le Bonus et les volets repliés ; le banc les ouvre.
await p.evaluate(() => document.querySelectorAll('details.bonus-replie, details.erreurs-repliees').forEach(d => { d.open = true; }));
await p.waitForTimeout(340);

const texte = (await p.textContent('body')).replace(/\s+/g, ' ');
ok('1 · chargement, titre « Programmer l\'alerte » et les codes 3e_C6.1 / 3e_C6.3',
   /Programmer l['’]alerte/i.test(await p.title())
   && texte.includes('3e_C6.1') && texte.includes('3e_C6.3'));

/* ── CodeLab Techno ──────────────────────────────────────────────────────── */
const v1 = await p.evaluate(() => PROGRAMME_V1);
const lignesV1 = v1.split('\n').length;
ok(`2 · programme d'origine chargé dans l'éditeur, ${lignesV1} lignes annoncées et comptées`,
   (await p.inputValue('#clTa')) === v1
   && (await p.textContent('#clLines')) === lignesV1 + ' lignes',
   await p.textContent('#clLines'));

const teintes = await p.$$eval('#clHl span', l => [...new Set(l.map(e => e.className))]
  .filter(Boolean));
ok(`3 · coloration syntaxique active : ${teintes.length} familles de jetons colorées`,
   // la palette du site (règle d'or n°13, code-colore.js, 05/11/2026) : mots-clés, nombres, variables, commentaires, textes, opérateurs
   ['py-kw', 'py-num', 'py-var', 'py-com', 'py-str', 'py-op'].filter(c => teintes.includes(c)).length >= 5, teintes.join(','));

/* Le surlignage est piloté par les consignes. En séance 1, l'activité lit la version 1 FIGÉE : le bouton surligne
   là (audit du 21/11/2026 : des numéros de ligne qui ne bougent pas). */
await p.click('#act1 [data-hl="6-7"]'); await p.waitForTimeout(100);
ok('3 bis · séance 1 : « surligner les lignes 6-7 » surligne 2 lignes de la version 1 figée, l\'éditeur ne bouge pas',
   (await p.$$('#act1 .programme-fige .pf-l.hl')).length === 2 && (await p.$$('#clHl .cl-line-hl')).length === 0);
/* En séance 2, l'éditeur vient sous la consigne de l'activité qui le fait modifier. */
await p.click('.seance-tab[data-panel="s2"]'); await p.waitForTimeout(120);
await p.evaluate(() => { document.querySelector('#act3 details.fiche-activite').open = true; }); await p.waitForTimeout(60);
const hl = await p.$eval('#act3 [data-hl]', e => e.dataset.hl);
await p.click(`#act3 [data-hl="${hl}"]`); await p.waitForTimeout(120);
const [a1, a2] = hl.split('-').map(Number);
ok(`4 · le bouton « surligner les lignes ${hl} » surligne exactement ${a2 - a1 + 1} ligne(s)`,
   (await p.$$('#clHl .cl-line-hl')).length === a2 - a1 + 1
   && (await p.$$('#clGutter .cl-ln-hl')).length === a2 - a1 + 1,
   String((await p.$$('#clHl .cl-line-hl')).length));
await p.click('#clUnhl'); await p.waitForTimeout(80);
ok('4 bis · le bouton « ne plus surligner » rend le programme à sa lecture normale',
   (await p.$$('#clHl .cl-line-hl')).length === 0);

const tailleAvant = await p.evaluate(() => window.__clFs);
await p.click('#clFontPlus'); await p.waitForTimeout(80);
const tailleApres = await p.evaluate(() => window.__clFs);
ok(`5 · A+ agrandit la police de l'éditeur (${tailleAvant} → ${tailleApres} px, et le style suit)`,
   tailleApres === tailleAvant + 1
   && (await p.$eval('#codelab', e => e.style.getPropertyValue('--cl-fs')))
      === tailleApres + 'px');
await p.click('.seance-tab[data-panel="s1"]'); await p.waitForTimeout(120);

ok('6 · à l\'ouverture, l\'éditeur déclare le programme identique à la version 1 d\'origine, et la version se dit',
   /identique à la version 1 d'origine/.test(await p.textContent('#clDiffInfo'))
   && /version 1 d'origine/.test(await p.textContent('#clVersion')),
   await p.textContent('#clDiffInfo'));

/* ── les attendus, LUS dans la page ─────────────────────────────────────── */
const PLAN = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const src = CHECKS[n].toString();
    const champs = {};
    const objet = src.match(/att\s*=\s*(\{[\s\S]*?\})\s*;/);
    if (objet) for (const [id, v] of Object.entries(eval('(' + objet[1] + ')')))
      champs[id] = { mode: 'exact', v };
    for (const m of src.matchAll(/\$\("([\w.]+)"\)\.value\s*===\s*(['"])((?:\\.|(?!\2).)*)\2/g))
      champs[m[1]] = { mode: 'exact', v: m[3] };
    for (const m of src.matchAll(
        /\$\("([\w.]+)"\)\.value\.indexOf\("((?:\\.|[^"])*)"\)\s*===\s*0/g))
      champs[m[1]] = { mode: 'prefixe', v: m[2] };
    for (const m of src.matchAll(/num\("([\w.]+)"\)\s*===?\s*(-?\d+(?:\.\d+)?)/g))
      champs[m[1]] = { mode: 'nombre', v: m[2] };
    const proses = [...new Set([...src.matchAll(/txt\("([\w.]+)"\)/g)].map(m => m[1]))];
    if (proses.length) {
      const mots = [...src.matchAll(/\.includes\("([^"]+)"\)/g)].map(m => m[1]);
      const longueur = Math.max(0, ...[...src.matchAll(/length\s*>=\s*(\d+)/g)]
        .map(m => Number(m[1])));
      for (const id of proses) champs[id] = { mode: 'prose', mots, longueur };
    }
    out[n] = champs;
  }
  return out;
});
const compte = m => Object.values(PLAN)
  .reduce((s, o) => s + Object.values(o).filter(c => c.mode === m).length, 0);
ok(`7 · attendus extraits des CHECKS : ${compte('exact')} égalités, ${compte('prefixe')} préfixes, `
   + `${compte('nombre')} nombres, ${compte('prose')} rédaction — rien n'est recopié ici`,
   // n°340 (V4) : la justification d'A2 n'est plus jugée par mots-clés — aucune « rédaction » dans les CHECKS
   Object.keys(PLAN).length === 6 && compte('exact') >= 22 && compte('prefixe') >= 4
   && compte('nombre') >= 3 && compte('prose') === 0,
   Object.keys(PLAN).join(','));

const ONGLETS = await p.$$eval('.seance-tab', l => l.map(e => e.dataset.panel));
async function ouvrirPour(id) {
  if (await p.isVisible('#' + id).catch(() => false)) return true;
  for (const panneau of ONGLETS) {
    await p.click(`.seance-tab[data-panel="${panneau}"]`);
    await p.waitForTimeout(90);
    if (await p.isVisible('#' + id).catch(() => false)) return true;
  }
  return false;
}
const rediger = c => {
  let t = 'Réponse rédigée pour le contrôle : ' + c.mots.join(', ') + '.';
  while (t.length < c.longueur + 5) t += ' On le vérifie ensuite point par point.';
  return t;
};
async function remplir(n, seulement = null) {
  for (const [id, c] of Object.entries(PLAN[n])) {
    if (seulement && !seulement.includes(id)) continue;
    if (!(await ouvrirPour(id))) continue;
    const el = await p.$('#' + id); if (!el) continue;
    const balise = await el.evaluate(e => e.tagName);
    if (c.mode === 'prose') { await p.fill('#' + id, rediger(c)); continue; }
    // n°300 (11/11/2026) : une question est un groupe de boutons radio (FIELDSET), rempli par le shim comme une liste
    if (balise !== 'SELECT' && balise !== 'FIELDSET') { await p.fill('#' + id, String(c.v)); continue; }
    if (c.mode === 'prefixe') {
      const exact = await el.evaluate((e, deb) => [...(e.options || e.querySelectorAll('input[type=radio]'))].map(o => o.value)
        .find(v => v && v.startsWith(deb)), c.v);
      if (exact) await p.selectOption('#' + id, exact);
    } else await p.selectOption('#' + id, String(c.v));
  }
}
const valider = async n => {
  await ouvrirPour(Object.keys(PLAN[n])[0] || 'clTa');
  await p.click(`[data-check="${n}"]`); await p.waitForTimeout(110);
};
const retour = n => p.textContent('#fb' + n);
const valide = n => p.evaluate(k => !!window.__valid[k], String(n));
const ecrireCode = async code => {
  await p.$eval('#clTa', (t, v) => {
    t.value = v; t.dispatchEvent(new Event('input', { bubbles: true }));
  }, code);
  await p.waitForTimeout(450);   // la version et la péremption suivent la frappe après 350 ms
};

/* ── billet : un état par question, jamais « rien n'est en place » sur des blancs (audit du 21/11/2026) ── */
await ouvrirPour('btnBillet'); await p.click('#btnBillet'); await p.waitForTimeout(80);
const billetVide = (await p.textContent('#fbBillet')).replace(/\s+/g, ' ');
ok('7 bis · billet sans réponse : « 0 réussie · 0 à revoir · 3 sans réponse », et jamais « rien n\'est en place »',
   /0 réussie · 0 à revoir · 3 sans réponse/.test(billetVide) && !/rien n'est encore en place/.test(billetVide), billetVide.slice(0, 90));

/* ── séance 1 : la version 1 d'origine est figée sous les questions de lecture ── */
const fige = await p.evaluate(() => [...document.querySelectorAll('#act1 .programme-fige, #act2 .programme-fige')].map(z => ({
  n: z.querySelectorAll('.pf-l').length, l6: (z.querySelector('.pf-l[data-n="6"]') || {}).textContent || '' })));
ok('7 ter · activités 1 et 2 : la version 1 d\'origine figée (24 lignes, la ligne 6 lit le vent), au lieu de l\'éditeur',
   fige.length === 2 && fige.every(f => f.n === lignesV1 && /vent_kmh = lire_capteur/.test(f.l6))
   && await p.evaluate(() => !document.querySelector('#act1 .codelab-ici, #act2 .codelab-ici')), JSON.stringify(fige));

/* critère de recette de l'audit : « Les lignes 6 et 21 sont attendues même si un élève insère un commentaire en tête » */
await ecrireCode('# mon commentaire en tête\n' + v1);
await remplir(1); await valider(1);
ok('8 · activité 1 validée 10 / 10 (mesure, paramètre, donnée produite, mesure sans décision, lignes 6 et 21) — même avec un commentaire inséré en tête de CodeLab',
   /10 \/ 10/.test(await retour(1)) && await valide(1), (await retour(1)).slice(0, 60));
await ecrireCode(v1);

await remplir(2); await ouvrirPour('d2_just'); await p.fill('#d2_just', 'Parce que.');
await valider(2);
ok('9 · activité 2 REFUSÉE : « Choix : 3 / 3 corrects » et « Justification : pas encore écrite », deux lignes séparées',
   /Choix : 3 \/ 3 corrects/.test(await retour(2)) && /Justification : pas encore écrite/.test(await retour(2))
   && !(await valide(2)), (await retour(2)).slice(0, 90));
/* critère de recette de l'audit : « Accepter « 118 ne dépasse pas 118 ; il dépasse 90 » » — aucun mot-clé exigé */
await p.fill('#d2_just', '118 ne dépasse pas 118 ; il dépasse 90');
await valider(2);
ok('10 · activité 2 validée avec « 118 ne dépasse pas 118 ; il dépasse 90 » (justification écrite, à relire par le professeur)',
   /Justification : écrite/.test(await retour(2)) && /relire par ton professeur/.test(await retour(2)) && await valide(2),
   (await retour(2)).slice(0, 90));
const trace2 = await p.evaluate(() => { const t = document.querySelector('#act2 .traceur'); return t && !t.hidden ? t.textContent.replace(/\s+/g, ' ') : ''; });
await p.evaluate(() => { const b = [...document.querySelectorAll('#act2 .traceur button')].find(x => /118 km\/h/.test(x.textContent)); b && b.click(); });
await p.waitForTimeout(60);
await p.evaluate(() => { const b = [...document.querySelectorAll('#act2 .traceur button')].find(x => /Tout afficher/.test(x.textContent)); b && b.click(); });
const trace118 = await p.evaluate(() => [...document.querySelectorAll('#act2 .traceur li')].map(l => l.textContent).join(' / '));
ok('10 bis · après « Vérifier », le chemin suivi pas à pas : à 118, « 118 > 118 → faux », puis « 118 > 90 → vrai »',
   trace2.length > 0 && /118 > 118 → faux/.test(trace118) && /118 > 90 → vrai/.test(trace118), trace118.slice(0, 120));

/* ── LE VÉRIFICATEUR EXÉCUTE LE CODE ─────────────────────────────────────── */
const SEUIL = await p.evaluate(() => Number((CHECKS[3].toString().match(/seuil!==(\d+)/) || [])[1]));
await remplir(3); await valider(3);
ok(`11 · activité 3 REFUSÉE : les 2 réponses justes, mais le banc lit SEUIL_ORANGE = 50 dans le programme`,
   /Questions : 2 \/ 2/.test(await retour(3)) && /SEUIL_ORANGE = 50/.test(await retour(3))
   && !(await valide(3)), (await retour(3)).slice(0, 90));
/* critère de recette de l'audit : « La frontière de mot après 60 accepte aussi le début de 60.5 » */
await ecrireCode(v1.replace(/SEUIL_ORANGE\s*=\s*\d+/, 'SEUIL_ORANGE = 60.5'));
await valider(3);
ok('11 bis · SEUIL_ORANGE = 60.5 : refusé, le banc lit la valeur effective (« SEUIL_ORANGE = 60.5 … le club a fixé 60 »)',
   /SEUIL_ORANGE = 60\.5/.test(await retour(3)) && !(await valide(3)), (await retour(3)).slice(0, 90));

await ecrireCode(v1.replace(/SEUIL_ORANGE\s*=\s*\d+/, 'SEUIL_ORANGE = ' + SEUIL));
await p.evaluate(() => { const d = document.querySelector('.cl-diff'); if (d) d.open = true; });
ok('12 · une seule ligne changée : le comparateur annonce 1 ligne ajoutée (+) et 1 retirée (−), pas davantage',
   /^1 ligne ajoutée \(\+\) et 1 ligne retirée/.test(await p.textContent('#clDiffInfo'))
   && /version 1 recalibrée/.test(await p.textContent('#clVersion')),
   (await p.textContent('#clDiffInfo')) + ' · ' + await p.textContent('#clVersion'));

await valider(3);
ok(`13 · activité 3 validée une fois la ligne 2 réellement recalibrée à ${SEUIL} : seuil lu, « Vigilance verte » à 55 km/h`,
   /SEUIL_ORANGE = 60 ✔/.test(await retour(3)) && /Vigilance verte/.test(await retour(3))
   && await valide(3), (await retour(3)).slice(0, 90));

/* ── L'ACTIVITÉ 4 EXÉCUTE LE PROGRAMME SUR DIX VENTS ─────────────────────── */
await valider(4);
const incomplet = await retour(4);
ok('14 · activité 4 REFUSÉE sur la version 1 recalibrée : le premier écart est nommé — 61 km/h, gyrophare actif attendu, arrêté obtenu',
   /Premier écart : 61 km\/h/.test(incomplet) && /gyrophare : actif attendu, arrêté obtenu/.test(incomplet)
   && !(await valide(4)) && await p.evaluate(() => !!document.querySelector('#bancA4 .traceur')), incomplet.slice(0, 120));

/* Le programme v2 n'est pas écrit ici : il est lu dans la correction que la page publie. */
const v2 = (await p.$eval('#act4 details.correction pre', e => e.textContent)).trim() + '\n';
ok(`15 · le programme v2 est lu dans la correction publiée par la page (${v2.split('\n').length} lignes)`,
   v2.length > v1.length * 0.8 && /gyrophare_actif/.test(v2), v2.split('\n').length + ' lignes');

/* critère de recette de l'audit : « Remplacer seulement les guillemets doubles des chaînes par des apostrophes » */
await ecrireCode(v2.replace(/"/g, "'")); await valider(4);
ok('16 · critère de l\'audit : la v2 écrite avec des apostrophes obtient 10 / 10, comme avec des guillemets',
   /10 \/ 10 vents conformes/.test(await retour(4)) && await valide(4), (await retour(4)).slice(0, 80));
/* critère de recette : « Remplacer seulement le test strict du seuil supérieur par un test inclusif » */
await ecrireCode(v2.replace('vent_kmh > SEUIL_OURAGAN', 'vent_kmh >= SEUIL_OURAGAN')); await valider(4);
ok('16 bis · critère de l\'audit : `>=` au seuil ouragan → refusé, « 118 km/h · niveau : rouge attendu, violette obtenu · gyrophare : arrêté attendu, actif obtenu »',
   /118 km\/h · niveau : rouge attendu, violette obtenu · gyrophare : arrêté attendu, actif obtenu/.test(await retour(4)) && !(await valide(4)),
   (await retour(4)).slice(0, 140));
/* « programme non exécutable signalé avec ligne » */
await ecrireCode(v2.replace('if gyrophare_actif:               # ④ nouveau bloc de commande\n    activer_gyrophare()', 'if gyrophare_actif:\nactiver_gyrophare()')); await valider(4);
ok('16 ter · programme non exécutable : « IndentationError » avec sa ligne, et la version le dit',
   /Ligne 29 · IndentationError/.test(await retour(4)) && !(await valide(4)) && /erreur/.test(await p.textContent('#clVersion')),
   (await retour(4)).slice(0, 120));
/* audit Fable du 22/11/2026 : une écriture Python juste que le banc ne connaissait pas (f-string) est lue ;
   une écriture qu'il ne lit pas (liste) est dite « limite du banc », jamais « SyntaxError » (n°340, n°146) */
await ecrireCode(v2.replace('message = "Vigilance " + vigilance', 'message = f"Vigilance {vigilance}"')); await valider(4);
const fstr = await retour(4), fstrOk = await valide(4);
await ecrireCode(v2.replace('vigilance = "verte"        # sorties initialisées « au repos »', 'niveaux = ["verte"]\nvigilance = niveaux[0]')); await valider(4);
const liste = await retour(4);
ok('16 quinquies · une f-string juste obtient 10 / 10 ; une liste (hors du banc) donne « Le banc n\'a pas pu essayer ton programme », « limite du banc », jamais « SyntaxError »',
   /10 \/ 10 vents conformes/.test(fstr) && fstrOk && /Le banc n'a pas pu essayer ton programme/.test(liste) && /limite du banc, pas forcément une erreur/.test(liste) && !/SyntaxError/.test(liste),
   fstr.slice(0, 50) + ' | ' + liste.slice(0, 120));
await ecrireCode(v2); await valider(4);
ok(`16 quater · activité 4 validée 10 / 10 sur la v2 de la correction, et la version se dit « version 2 »`,
   /10 \/ 10 vents conformes/.test(await retour(4)) && await valide(4) && /version 2/.test(await p.textContent('#clVersion')),
   (await retour(4)).slice(0, 60));

/* ── L'ACTIVITÉ 5 : PRÉVOIR, EXÉCUTER, COMPARER — et l'essai périmé ─────── */
/* critère de recette de l'audit : « Avec la v1 restaurée dans l'éditeur, les sept bonnes réponses théoriques donnent
   7/7 et un message de maîtrise » → deux indicateurs, et « à exécuter » tant qu'aucune observation */
await ecrireCode(v1);
await remplir(5); await valider(5);
ok('17 · prévisions et diagnostic justes, rien exécuté : REFUSÉE, « Essais de ma version : à exécuter »',
   /Mes prévisions : 6 \/ 6/.test(await retour(5)) && /Diagnostic de la copie B : 2 \/ 2/.test(await retour(5))
   && /Essais de ma version : à exécuter/.test(await retour(5)) && !(await valide(5)), (await retour(5)).replace(/\n/g, ' / ').slice(0, 160));
await p.click('#banc5Tout'); await p.waitForTimeout(120); await valider(5);
ok('17 bis · la v1 restaurée exécutée : REFUSÉE, « 3 / 10 vents conformes » — la prévision juste ne vaut pas exécution de sa copie',
   /Essais de ma version : 3 \/ 10 vents conformes/.test(await retour(5)) && !(await valide(5)), (await retour(5)).replace(/\n/g, ' / ').slice(0, 160));
await ecrireCode(v2); await valider(5);
ok('17 ter · version modifiée depuis l\'essai : « à rejouer », et le journal marque l\'ancien essai',
   /Essais de ma version : à rejouer/.test(await retour(5)) && !(await valide(5))
   && /à rejouer/.test(await p.textContent('.banc-journal')), (await retour(5)).replace(/\n/g, ' / ').slice(0, 160));
await p.click('#banc5Tout'); await p.waitForTimeout(120); await valider(5);
ok('17 quater · la v2 exécutée sur 10 vents : activité 5 validée, « 10 / 10 … dix cas essayés, pas tous les vents possibles »',
   /10 \/ 10 vents conformes/.test(await retour(5)) && /pas tous les vents possibles/.test(await retour(5)) && await valide(5),
   (await retour(5)).replace(/\n/g, ' / ').slice(0, 160));
const lignesBanc = await p.$$eval('#banc5Table tr', l => l.length - 1);
ok('17 quinquies · le tableau des essais montre 10 vents, la prévision de l\'élève et l\'obtenu de sa version',
   lignesBanc === 10 && /orange · gyrophare seul/.test(await p.textContent('#banc5Table')), String(lignesBanc));
/* l'aller-retour v1 → v2 a périmé les activités 3 et 4 : on les vérifie de nouveau sur la v2 */
await valider(3); await valider(4);

await remplir(6); await valider(6);
ok('18 · activité 6 validée 6 / 6 (transfert : lire un programme qu\'on n\'a pas écrit)',
   /6 \/ 6/.test(await retour(6)) && await valide(6), (await retour(6)).slice(0, 60));

const prog = (await p.textContent('#progTxt')).replace(/\s+/g, ' ').trim();
const [faites, total] = (prog.match(/(\d+)\s*\/\s*(\d+)/) || []).slice(1).map(Number);
ok(`19 · toutes les activités sont validées (${prog})`,
   total > 0 && faites === total, prog);
const coches = await p.$$eval('[id^="done-s"]', l => l.map(e => e.textContent.trim()));
ok(`19 bis · les ${coches.length} onglets de séance portent leur coche`,
   coches.length > 0 && coches.every(c => c === '✔'), coches.join('|'));

/* ── n°346 (21/11/2026) : trois explications écrites, sans propositions, qui ne notent rien ── */
const ecrit = await p.evaluate(() => {
  const z = document.querySelector('#ecritBouee');
  return z && {
    zones: z.querySelectorAll('textarea').length,
    radios: z.querySelectorAll('input[type=radio], select').length,
    etayages: z.querySelectorAll('details.etayage').length,
    correctionFermee: !!z.querySelector('details.correction') && !z.querySelector('details.correction').open,
    copie: (z.querySelector('details.correction').textContent.match(/Sur ta copie, on peut écrire/g) || []).length,
    grille: z.querySelectorAll('.grille-ecrit input[type=checkbox]').length,
  };
});
ok('19 ter · réinvestissement : trois explications écrites, sans proposition, chacune avec sa version étayée, correction repliée avec trois phrases de copie, grille à trois critères (n°346, n°356)',
   ecrit && ecrit.zones === 3 && ecrit.radios === 0 && ecrit.etayages === 3 && ecrit.correctionFermee
   && ecrit.copie === 3 && ecrit.grille === 3, JSON.stringify(ecrit));
const validAvant = await p.evaluate(() => JSON.stringify(window.__valid || {}));
await p.evaluate(() => {
  const f = (id, v) => { const t = document.getElementById(id); t.value = v; t.dispatchEvent(new Event('input', { bubbles: true })); };
  f('eb1', '4.0 > 4 est faux : > est strict, la ligne 5 est sautée, le drapeau reste vert.');
  f('eb3', 'if hauteur_m > SEUIL_HOULE:\n    drapeau = "rouge"\nelif hauteur_m > 2:\n    drapeau = "orange"');
  const c = document.getElementById('ebg2'); c.checked = true; c.dispatchEvent(new Event('change', { bubbles: true }));
});
await p.waitForTimeout(700);
const etat = (await p.textContent('#ebEtat')).replace(/\s+/g, ' ');
ok('19 quater · l\'état compte ce qui est écrit et coché (2 / 3, 1 / 3) sans rien valider ni noter (n°340)',
   /2 \/ 3/.test(etat) && /1 \/ 3/.test(etat) && /aucune note/.test(etat)
   && await p.evaluate(() => JSON.stringify(window.__valid || {})) === validAvant, etat);

await p.evaluate(() => { document.getElementById('boueeEssai').click(); });
const bouee = (await p.textContent('#boueeRes')).replace(/\s+/g, ' ');
ok('19 quinquies · la bouée : les lignes 4 à 7 écrites s\'essaient à 2,0 · 3,0 · 4,0 · 5,0 m, sans note (5,0 m → « Baignade : rouge »)',
   /2,0 m → « Baignade : vert »/.test(bouee) && /3,0 m → « Baignade : orange »/.test(bouee) && /5,0 m → « Baignade : rouge »/.test(bouee)
   && /rien n'est noté/.test(bouee), bouee.slice(0, 140));
await ouvrirPour('hyp1');
await p.fill('#hyp1', 'Il faut connaître ses données.'); await p.fill('#hyp2', 'J\'essaierai 118 et je prévois rouge.');
await p.waitForTimeout(80);
const rappels = await p.evaluate(() => [document.getElementById('hypRappelTxt').textContent, document.getElementById('hypRappelTxt2').textContent]);
ok('19 sexies · bilan : les DEUX hypothèses de départ reviennent, face à deux champs', /ses données/.test(rappels[0]) && /118/.test(rappels[1])
   && await p.evaluate(() => !!document.getElementById('hyp_retour2')), rappels.join(' | '));

/* 19 septies · la reprise des séances 2 et 3 (n°369, en essai) : en tête de séance, de mémoire ; elle ne valide rien */
await p.click('.seance-tab[data-panel="s2"]'); await p.waitForTimeout(120);
const enTete = await p.evaluate(() => { const pan = document.getElementById('s2'); return pan.firstElementChild && pan.firstElementChild.id; });
const repValidAvant = await p.evaluate(() => JSON.stringify(window.__valid || {}));
await p.check('#rp2_1__1'); await p.check('#rp2_2__1');           // deux réponses fausses
await p.click('[data-reprise-verif="S2"]'); await p.waitForTimeout(60);
const rFaux = await p.textContent('#fbRepriseS2');
const lienRappel = await p.$eval('#fbRepriseS2 a', a => a.getAttribute('href')).catch(() => '');
await p.check('#rp2_1__3'); await p.check('#rp2_2__3');           // les bonnes
await p.click('[data-reprise-verif="S2"]'); await p.waitForTimeout(60);
const rJuste = await p.textContent('#fbRepriseS2');
const repValidApres = await p.evaluate(() => JSON.stringify(window.__valid || {}));
await p.click('.seance-tab[data-panel="s3"]'); await p.waitForTimeout(120);
const enTete3 = await p.evaluate(() => { const pan = document.getElementById('s3'); return pan.firstElementChild && pan.firstElementChild.id; });
ok('19 septies · reprise en tête des séances 2 et 3 : une erreur renvoie au rappel, « 2 / 2 retrouvée(s) », et rien n\'est validé',
   enTete === 'repriseS2' && enTete3 === 'repriseS3' && /✘ Pas encore/.test(rFaux) && lienRappel === '#rappel-quatre-mots'
   && /2 \/ 2 retrouvée\(s\) de mémoire/.test(rJuste) && /Elle ne valide rien/.test(rJuste) && repValidAvant === repValidApres,
   [enTete, enTete3, lienRappel, rJuste.slice(0, 80)].join(' | '));

/* ── persistance : le CODE de l'élève doit revenir, pas la version d'origine ── */
/* billet de sortie (règle d'or n°330, 28/11/2026) : seul, sans aide, sur un objet neuf */
{
  const _avant = await p.evaluate(() => (document.querySelector('.seance-panel.active') || {}).id);
  await p.click('.seance-tab[data-panel="s3"]'); await p.waitForTimeout(100);
  const bs = await p.evaluate(() => {
    const s = document.getElementById('billetSortie'); if (!s) return null;
    const corr = s.querySelector('details.correction');
    const bonus = [...document.querySelectorAll('section.card h2')].find(h => /🎁 Bonus/.test(h.textContent));
    return { visible: s.checkVisibility(), zones: s.querySelectorAll('textarea[data-save]').length,
      etayages: s.querySelectorAll('details.etayage').length, boutons: s.querySelectorAll('button').length,
      criteres: (corr.textContent.match(/Critère/g) || []).length, contre: (corr.textContent.match(/✘/g) || []).length,
      avantBonus: !!bonus && s.nextElementSibling === bonus.closest('section'),
      panneau: (s.closest('.seance-panel') || {}).id };
  });
  ok('billet de sortie · il existe, visible à sa séance, juste avant le Bonus', !!bs && bs.visible && bs.panneau === 's3' && bs.avantBonus, JSON.stringify(bs));
  ok('billet de sortie · deux zones gardées, deux versions étayées, deux critères, des contre-exemples, aucun bouton',
     !!bs && bs.zones === 2 && bs.etayages === 2 && bs.criteres === 2 && bs.contre >= 2 && bs.boutons === 0, JSON.stringify(bs));
  await p.fill('#bs_3e_C6_1_1', 'ma réponse au billet');
  await p.waitForTimeout(800);
  if (_avant) { await p.click(`.seance-tab[data-panel="${_avant}"]`); await p.waitForTimeout(80); }
}
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(360);
ok('billet de sortie · la réponse écrite survit au rechargement', (await p.inputValue('#bs_3e_C6_1_1')) === 'ma réponse au billet');
ok('20 · rechargement : le programme v2 de l\'élève est restauré, pas la version d\'origine',
   (await p.inputValue('#clTa')).includes('gyrophare_actif')
   && (await p.inputValue('#clTa')) !== v1,
   (await p.textContent('#clDiffInfo')).slice(0, 60));
ok('20 bis · rechargement : réponses, validations et journal d\'essai restaurés, taille de police comprise',
   (await p.textContent('#progTxt')).trim().length > 0
   && await p.evaluate(() => !!window.__valid[4] && !!window.__valid[5] && window.__banc.journal.length > 0)
   && await p.evaluate(() => window.__clFs) === tailleApres,
   await p.textContent('#progTxt'));
ok('20 ter · rechargement : les explications écrites et la case cochée de la grille reviennent',
   (await p.inputValue('#eb1')).startsWith('4.0 > 4 est faux')
   && await p.isChecked('#ebg2') && !(await p.isChecked('#ebg1')),
   (await p.textContent('#ebEtat')).slice(0, 60));

const corps = (await p.textContent('body')).replace(/\s+/g, ' ');
const svgAlgo = fs.readFileSync(path.join(ICI, 'Images/algorigramme_alerte_graduee.svg'), 'utf8');
const svgPlan = fs.readFileSync(path.join(ICI, 'Images/plan_de_tests_jeux_essai_muet.svg'), 'utf8');
ok('20 quater · documents : l\'algorigramme (spécification de la v2) teste 60, pas 50 ; le plan de tests de la v1 ne commande aucun gyrophare ; aucun « verte/jaune » ; récit fictif, seuil du club',
   /vent_kmh &gt; 60 \?/.test(svgAlgo) && !/&gt; 50/.test(svgAlgo) && /orange · sirène arrêtée/.test(svgPlan) && !/orange \+ gyrophare|sirène \+ gyro/.test(svgPlan)
   && !/verte\/jaune/.test(corps + svgAlgo + svgPlan) && /Simulation scolaire/.test(corps) && /inventés pour l'exercice/.test(corps)
   && !/Météo-France recalibre/.test(corps) && /le club fixe son seuil expérimental/i.test(corps), '');

const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens.filter(h => h && !/^(https?:|mailto:|#|javascript:|data:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok(`21 · les ${liens.length} liens internes existent`, casses.length === 0,
   casses.slice(0, 3).join(' · '));

/* 21 bis · le fichier du Bonus est le programme de la correction de l'activité 4, et il passe le banc */
const bonus = await p.evaluate(() => {
  const a = document.querySelector('a[download="station_alerte_v2_corrige.py"]');
  if (!a) return null;
  const fichier = decodeURIComponent(a.getAttribute('href').replace(/^data:[^,]*,/, ''));
  const code = sansSimulation(fichier);
  const essais = essayerStation(code, 'v2', VENTS_BANC);
  const corr = [...document.querySelectorAll('details.correction pre')].map(x => x.textContent).find(x => /programme d'alerte v2/.test(x)) || '';
  return { entete: fichier.indexOf('# --- Simulation de la maquette') === 0, memeCode: code.trim() === corr.trim(), conformes: essais.filter(e => e.conforme).length, n: essais.length };
});
ok('21 bis · Bonus : le fichier .py donné commence par la simulation, porte le programme de la correction de l\'activité 4, et passe le banc 10 / 10',
   !!bonus && bonus.entete && bonus.memeCode && bonus.conformes === 10 && bonus.n === 10, JSON.stringify(bonus));

const svg = await p.$$eval('img[src$=".svg"], object[data$=".svg"]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('data')));
const svgAbsents = svg.filter(s => !fs.existsSync(path.join(ICI, s)));
// 4 depuis la vague n°331 (15/11/2026) : le schéma des entrées/sorties de l'activité 1 est affiché MUET avec ses
// questions, et complet dans sa correction. 5 depuis sa 2e passe (même jour) : le plan de tests de l'activité 5,
// muet sur la cause du bug et sur les valeurs frontières, avec ses questions ; complet dans sa correction.
ok(`22 · les ${svg.length} SVG référencés existent sur le disque`,
   svg.length === 5 && svgAbsents.length === 0, svgAbsents.join(' · '));

const distantes = await p.$$eval('[src], link[href], object[data], iframe[src]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('href') || e.getAttribute('data'))
        .filter(u => u && /^(https?:)?\/\//i.test(u)));
ok('23 · hors ligne : aucune ressource distante, aucune modale, aucune erreur JS',
   distantes.length === 0 && dlg.length === 0 && fail.length === 0 && err.length === 0,
   (distantes[0] || err[0] || fail[0] || dlg[0] || '').slice(0, 80));
await ctx.close();
}

/* ════════════════ QCM (9 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = _groupesRadio(await ctx.newPage());
const err = []; p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });

await p.goto(pathToFileURL(QCM).href, { waitUntil: 'load' });
await p.waitForTimeout(300);

const Q = await p.evaluate(() => QUESTIONS.map(q => ({
  c: q.c, n: q.n, o: q.o, r: q.r, d: q.d, expl: q.expl, ex: q.ex, err: q.err, ret: q.ret,
  img: q.img ? q.img.src : null })));
const codes = await p.evaluate(() => Object.keys(COMP_LABELS));
const badge = (await p.$eval('.badge.theme', e => e.textContent)).trim();

ok('24 · chargement du QCM, titre « Programmer l\'alerte », taille annoncée exacte',
   /Programmer l['’]alerte/i.test(await p.title()) && badge.includes(String(Q.length))
   && (await p.textContent('#qTot')) === String(Q.length), badge);

const parCode = {};
Q.forEach(q => { parCode[q.c] = (parCode[q.c] || 0) + 1; });
ok(`25 · ${Q.length} questions, ${codes.length} compétences : `
   + codes.map(c => c + ' ' + (parCode[c] || 0)).join(' · '),
   Q.length === 30 && codes.length === 2 && codes.every(c => parCode[c] === 15),
   JSON.stringify(parCode));

const rep = [0, 0, 0, 0]; Q.forEach(q => rep[q.r]++);
ok(`26 · bonnes réponses A/B/C/D = ${rep.join('/')} (écart max 1) et d[r] vide partout`,
   Math.max(...rep) - Math.min(...rep) <= 1 && Q.every(q => q.d[q.r] === ''), rep.join('/'));

const illustrees = Q.filter(q => q.img);
const imgAbsentes = illustrees.filter(q => !fs.existsSync(path.join(ICI, q.img)));
ok(`27 · ${illustrees.length} questions illustrées, fichiers présents sur le disque`,
   illustrees.length === 6 && imgAbsentes.length === 0, imgAbsentes.map(q => q.n).join(' · '));

const incomplets = Q.filter(q => !(q.o.length === 4 && q.d.length === 4 && q.expl && q.ex
                                   && q.err && q.ret));
ok('28 · gabarit maison complet : 4 options, 4 réfutations, explication, exemple, erreur, à retenir',
   incomplets.length === 0, incomplets.map(q => q.n).slice(0, 3).join(' · '));

for (let i = 0; i < Q.length; i++) {
  const r = await p.evaluate(() => QUESTIONS[Number(document.getElementById('qNum')
    .textContent) - 1].r);
  const opts = await p.$$('#qOptions .option');
  await opts[r].click();
  await p.click('#btnValider'); await p.waitForTimeout(30);
  if (i < Q.length - 1) { await p.click('#btnSuiv'); await p.waitForTimeout(30); }
}
await p.click('#btnTerminer'); await p.waitForTimeout(220);
const note = (await p.textContent('#rNote')).trim();
const lignes = await p.$$eval('#tblBilan tbody tr',
  l => l.map(t => t.textContent.replace(/\s+/g, ' ').trim()));
ok(`29 · parcours complet ${Q.length} / ${Q.length} joué → note ${note}, bilan sur `
   + `${lignes.length} compétences`,
   /20,0/.test(note) && (await p.textContent('#rOk')) === String(Q.length)
   && lignes.length === 2 && lignes.every(l => /15 \/ 15/.test(l)),
   note + ' · ' + lignes.join(' | ').slice(0, 70));

/* critère de recette de l'audit : « Afficher « 10/10 réussies dans ce parcours » et « 10/30 travaillées ». Réserver le
   /20 au parcours complet terminé. » — dans un contexte neuf */
{
  const c2 = await b.newContext({ viewport: { width: 390, height: 844 } }); const q = await c2.newPage();
  await q.goto(pathToFileURL(QCM).href, { waitUntil: 'load' }); await q.waitForTimeout(250);
  await q.click('[data-mode="dix"]'); await q.waitForTimeout(80);
  for (let i = 0; i < 10; i++) {
    const r = await q.evaluate(() => QUESTIONS[Number(document.getElementById('qNum').textContent) - 1].r);
    await (await q.$$('#qOptions .option'))[r].click(); await q.click('#btnValider'); await q.waitForTimeout(20);
    if (i < 9) { await q.click('#btnSuiv'); await q.waitForTimeout(20); }
  }
  const reste = (await q.textContent('#dReste')).replace(/\s+/g, ' ');
  await q.click('#btnTerminer'); await q.waitForTimeout(150);
  const rn = (await q.textContent('#rNote')).trim(), re = (await q.textContent('#rEssais')).replace(/\s+/g, ' ');
  ok('29 bis · parcours « 10 questions » réussi : « 10 / 10 réussies » et « 10 / 30 questions travaillées », aucune note sur 20 (pas de 6,7 /20)',
     /10 \/ 10 réussies/.test(rn) && /10 \/ 30 questions travaillées/.test(re) && !/\/20/.test(rn) && /10 \/ 10 réussie/.test(reste)
     && (await q.textContent('#dNote')).trim() === '— /20', rn + ' · ' + re.slice(0, 90));
  await c2.close();
}

const cles = await p.evaluate(() => Object.keys(window.localStorage));
ok('30 · la clé localStorage du QCM est écrite',
   cles.some(k => k.includes('qcm_3e_C6.1-C6.3_programmer')), cles.join(' · '));

const retourSeq = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href'))
  .filter(h => h && /sequence.*\.html$/.test(h)));
ok('31 · le lien de retour vers la séquence existe et pointe sur un fichier réel',
   retourSeq.length > 0
   && retourSeq.every(h => fs.existsSync(path.join(ICI, decodeURIComponent(h)))),
   retourSeq[0] || '');

ok('32 · aucune erreur JS sur le QCM', err.length === 0, err.slice(0, 2).join(' | '));
await ctx.close();
}

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
