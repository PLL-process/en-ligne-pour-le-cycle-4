/* balayer_questions_qcm.mjs — chaque question de chaque QCM, jouée au téléphone (règles d'or n°343 et n°345, 21/11/2026).
 *
 * D'OÙ VIENT CE CONTRÔLE
 * ----------------------
 * Le 21/11/2026, à la livraison du thème 1, les contrôles des QCM étaient verts. En jouant les 30 questions de chaque
 * QCM modifié à 390 px, la question 15 de `5e_C1.3` sortait de l'écran : ses quatre propositions sont des chemins de
 * fichier (« Hangzhou_velos_groupeXX/01_donnees_brutes/synthese_velos.pdf »), sans espace où couper. La proposition
 * mesurait 574 px sur un écran de 390 : l'élève devait faire défiler la page de côté pour lire la fin du chemin — ce
 * que la question demande justement de lire. Le défaut était sur `main`.
 * Aucun outil ne le voyait : `controle_debordement.py` lit les tableaux dans le source ; le skill `balayage-navigateur`
 * ouvre chaque page mais « ne voit pas ce qui n'apparaît qu'après un clic » ; les bancs des lots jouent quelques
 * questions, pas toutes. Une question se lit seule (n°343) — encore faut-il qu'elle tienne dans l'écran.
 *
 * CE QUE L'OUTIL FAIT
 * -------------------
 * Il ouvre chaque page `qcm_*.html` du gabarit maison dans Chromium, à 390 × 844 px, choisit « Parcours complet », puis
 * affiche les questions une à une par la grille de navigation. Sur chaque question :
 *   B1 ✘ débordement   la page est plus large que l'écran (une proposition, un énoncé ou une image sort à droite) ;
 *   B2 ✘ image         la figure de la question n'est pas décodée (fichier absent, nom mal écrit, SVG invalide) ;
 *   B3 ✘ alt           la figure n'a pas de description, ou moins de 20 caractères (elle doit permettre de répondre) ;
 *   B4 ✘ document      un document de QCM (`Images/doc_…`, n°345) s'affiche à moins de 300 px de large ;
 *   B5 ✘ erreur        une erreur JavaScript, une erreur de console ou une requête ratée pendant le parcours.
 * Sans option, il ne répond à aucune question : il regarde ce que l'élève voit avant de répondre.
 * Avec `--apres`, il donne en plus une réponse fausse à chaque question (dans son navigateur à lui : rien n'est gardé)
 * et mesure B1 sur les trois écrans de l'aide progressive (n°339) : l'indice, le second indice, la correction complète.
 *
 * CE QU'IL NE VOIT PAS, ET LE DIT
 * -------------------------------
 *   · sans `--apres`, ce qui s'affiche après une réponse ; avec, il n'en mesure que la largeur : le texte de l'aide se
 *     juge par `qcm_aides/indices_creux.mjs` et à la lecture ; l'écran d'une réponse JUSTE n'est pas joué ;
 *   · la lisibilité d'un texte dans une image (taille des lettres) : `controle_schemas.mjs`, puis l'œil ;
 *   · les QCM d'un autre gabarit (ateliers à gabarit propre) : dits « non lus », jamais comptés verts ;
 *   · un vrai téléphone : Chromium à 390 px n'est pas Safari sur iPhone.
 *
 * USAGE
 * -----
 *   node _outils/balayer_questions_qcm.mjs [--muet] [--apres] [--largeur 390] [chemin…]
 * Sans chemin : tout le dépôt. Un chemin peut être un dossier (thème, lot) ou une page.
 * Sortie : 0 rien à refuser · 1 au moins une question en écart · 2 aucun QCM lu (en panne, règle d'or n°299).
 */
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL, fileURLToPath } from 'node:url';

const RACINE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const IGNORES = new Set(['.git', 'node_modules', '_archive-anciennes-versions', '_outils', '_exports']);
const args = process.argv.slice(2);
const muet = args.includes('--muet');
const apres = args.includes('--apres');
const iL = args.indexOf('--largeur');
const LARGEUR = iL >= 0 ? parseInt(args[iL + 1], 10) : 390;
const chemins = args.filter((a, i) => !a.startsWith('--') && !(iL >= 0 && i === iL + 1));

function pages(depart) {
  const out = [];
  const st = fs.statSync(depart);
  if (st.isFile()) return /^qcm_.*\.html$/i.test(path.basename(depart)) ? [depart] : [];
  (function marcher(dossier) {
    for (const e of fs.readdirSync(dossier, { withFileTypes: true })) {
      if (IGNORES.has(e.name)) continue;
      const complet = path.join(dossier, e.name);
      if (e.isDirectory()) marcher(complet);
      else if (/^qcm_.*\.html$/i.test(e.name)) out.push(complet);
    }
  })(depart);
  return out;
}

let fichiers = [];
try {
  for (const c of (chemins.length ? chemins : [RACINE])) fichiers.push(...pages(path.resolve(c)));
} catch (e) {
  console.error(`❌ EN PANNE : chemin illisible (${e.message}) — règle d'or n°299.`);
  process.exit(2);
}
fichiers = [...new Set(fichiers)].sort();

let chromium;
try { ({ chromium } = await import('playwright')); } catch (e) {
  console.error('❌ EN PANNE : le paquet `playwright` manque pour Node (non exécuté, règle d\'or n°299).');
  process.exit(2);
}

// Jouée dans la page : null si rien ne dépasse, sinon le texte ou l'image qui va le plus à droite.
// Un texte sans espace déborde de son bloc sans l'élargir : c'est le texte qu'on mesure (Range), pas le bloc.
const DEBORD = () => {
  const W = document.documentElement.clientWidth;
  if (document.documentElement.scrollWidth <= W) return null;
  let pire = null;
  const voir = (droite, texte) => { if (droite > W + 0.5 && (!pire || droite > pire.droite)) pire = { droite: Math.round(droite), texte }; };
  const marche = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const plage = document.createRange();
  for (let n = marche.nextNode(); n; n = marche.nextNode()) {
    if (!n.textContent.trim()) continue;
    plage.selectNodeContents(n);
    const b = plage.getBoundingClientRect();
    if (b.width > 0) voir(b.right, n.textContent.trim().replace(/\s+/g, ' ').slice(0, 60));
  }
  for (const e of document.querySelectorAll('img, svg, table, pre, input, textarea, iframe')) {
    const b = e.getBoundingClientRect();
    if (b.width > 0) voir(b.right, '<' + e.tagName.toLowerCase() + '> ' + (e.getAttribute('alt') || e.getAttribute('src') || '').slice(0, 50));
  }
  return Object.assign(pire || { droite: document.documentElement.scrollWidth, texte: '(élément non identifié)' }, { W });
};

const navigateur = await chromium.launch();
let lus = 0, nonLus = [], questions = 0, illustrees = 0, enEcart = 0, ecransApres = 0;
const refus = [];
for (const fichier of fichiers) {
  const rel = path.relative(RACINE, fichier);
  const page = await navigateur.newPage({ viewport: { width: LARGEUR, height: 844 }, deviceScaleFactor: 1 });
  const erreurs = [];
  page.on('pageerror', e => erreurs.push('JS : ' + e.message.slice(0, 90)));
  page.on('requestfailed', r => erreurs.push('requête ratée : ' + decodeURIComponent(r.url().split('/').pop())));
  page.on('console', m => { if (m.type() === 'error') erreurs.push('console : ' + m.text().slice(0, 90)); });
  let N = 0;
  try {
    await page.goto(pathToFileURL(fichier).href, { waitUntil: 'load' });
    await page.waitForTimeout(250);
    await page.getByRole('button', { name: /Parcours complet/ }).first().click({ timeout: 4000 });
    await page.waitForTimeout(200);
    N = await page.evaluate(() => (typeof QUESTIONS !== 'undefined' && document.querySelector('.option') ? QUESTIONS.length : 0));
  } catch (e) { /* un autre gabarit : dit « non lu » plus bas */ }
  if (!N) { nonLus.push(rel); await page.close(); continue; }
  lus++;
  const ecarts = [];
  for (let n = 1; n <= N; n++) {
    try {
      await page.locator('button', { hasText: new RegExp('^' + n + '$') }).first().click({ timeout: 4000 });
    } catch (e) { ecarts.push(`Q${n} · B5 erreur : la grille de navigation n'a pas de bouton « ${n} »`); continue; }
    await page.waitForTimeout(160);
    const pire = await page.evaluate(DEBORD);
    const img = await page.evaluate(() => {
      const i = document.getElementById('qImg'), fig = document.getElementById('qFigure');
      return (!i || !fig || fig.hidden) ? null : { ok: i.complete && i.naturalWidth > 0, src: i.getAttribute('src') || '',
        alt: (i.getAttribute('alt') || '').trim().length, w: Math.round(i.getBoundingClientRect().width) };
    });
    const r = { pire, img };
    questions++;
    if (r.pire) ecarts.push(`Q${n} · B1 débordement : ${r.pire.droite} px pour un écran de ${r.pire.W} — « ${r.pire.texte} »`);
    if (r.img) {
      illustrees++;
      if (!r.img.ok) ecarts.push(`Q${n} · B2 image non décodée : ${r.img.src}`);
      if (r.img.alt < 20) ecarts.push(`Q${n} · B3 alt absent ou trop court (${r.img.alt} caractère(s)) : ${r.img.src}`);
      if (/\/doc_/.test(r.img.src) && r.img.w < 300 && LARGEUR >= 390) ecarts.push(`Q${n} · B4 document affiché à ${r.img.w} px : ${r.img.src}`);
    }
    if (!apres) continue;
    // une réponse fausse, puis les trois écrans de l'aide progressive (n°339)
    const faux = await page.evaluate(i => { const bonne = QUESTIONS[i].r; return Array.isArray(bonne) ? -1 : (bonne === 0 ? 1 : 0); }, n - 1);
    if (faux < 0) continue;
    try {
      await page.locator('.option').nth(faux).click({ timeout: 4000 });
      await page.locator('#btnValider').click({ timeout: 4000 });
      await page.waitForTimeout(110);
      for (const [ecran, bouton] of [['l\'indice', null], ['le second indice', '#btnIndice2'], ['la correction complète', '#btnVoirCorr']]) {
        if (bouton) {
          const bt = page.locator(bouton);
          if (!(await bt.count()) || !(await bt.isVisible())) continue;
          await bt.click({ timeout: 4000 });
          await page.waitForTimeout(110);
        }
        ecransApres++;
        const d = await page.evaluate(DEBORD);
        if (d) ecarts.push(`Q${n} · B1 débordement après une réponse fausse, sur ${ecran} : ${d.droite} px pour un écran de ${d.W} — « ${d.texte} »`);
      }
    } catch (e) { ecarts.push(`Q${n} · B5 erreur : la réponse fausse n'a pas pu être jouée (${e.message.split('\n')[0].slice(0, 70)})`); }
  }
  for (const e of [...new Set(erreurs)].slice(0, 5)) ecarts.push('B5 ' + e);
  if (ecarts.length) { enEcart++; refus.push([rel, ecarts]); }
  else if (!muet) console.log(`✅ ${rel} · ${N} questions jouées`);
  await page.close();
}
await navigateur.close();

for (const [rel, ecarts] of refus) {
  console.log(`✘ ${rel}`);
  for (const e of ecarts) console.log(`   · ${e}`);
}
// une page non lue se nomme toujours, même avec --muet : ce qui n'est pas lu n'est pas vert (n°299)
for (const rel of nonLus) console.log(`∅ ${rel} · non lu (autre gabarit, ou page sans « Parcours complet »)`);
console.log(`${lus} QCM lu(s) à ${LARGEUR} px · ${questions} questions jouées · ${illustrees} illustrées`
  + (apres ? ` · ${ecransApres} écran(s) d'aide joués après une réponse fausse` : '') + ` · ${enEcart} QCM en écart`
  + (nonLus.length ? ` · ${nonLus.length} page(s) non lue(s)` : ''));
if (!lus) {
  console.error(`❌ EN PANNE : aucun QCM lu (${fichiers.length} page(s) qcm_*.html trouvée(s)) — règle d'or n°299.`);
  process.exit(2);
}
if (enEcart) {
  console.log('✘ une question au moins ne tient pas dans l\'écran du téléphone, ou sa figure ne se lit pas (n°343, n°345)');
  process.exit(1);
}
console.log('✅ chaque question tient dans l\'écran du téléphone, chaque figure est décodée et décrite (n°343, n°345)');
