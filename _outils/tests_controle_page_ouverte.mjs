/* tests_controle_page_ouverte.mjs — banc de `controle_page_ouverte.mjs` (règle d'or n°361).
 *
 * Sept pages fabriquées dans un dossier temporaire, chacune pour une frontière :
 *   propre      corrections différentes, listing court → rien ;
 *   crochet     corrections fabriquées par `window.__toutOuvrir()`, avec la même phrase et un bloc dessiné → B et C ;
 *   sans_crochet les mêmes corrections, sans crochet → rien (c'est la limite que le crochet lève) ;
 *   listing     une ligne de code de 120 caractères à 390 px → L ;
 *   codebox     la même ligne dans un `div` en chasse fixe qui garde ses lignes (`white-space:pre`), et un bandeau
 *               `nowrap` en chasse fixe coupé au bord → L (deux) ; le même bloc en `pre-wrap` → rien ;
 *   repete      une ligne d'aide marquée `data-repete` dans chaque correction → rien ;
 *   editeur     le calque coloré d'un éditeur intégré, 150 caractères → rien (il défile avec la saisie) ;
 *   details     trois <details> « Correction » qui répètent une phrase → C ;
 *   intitule    trois corrections qui ouvrent sur le même intitulé tout en gras, et le même titre → rien ;
 *   contraste   une correction repliée écrite en gris clair sur blanc (2,3 : 1) → A, avec --axe seulement ;
 *   titres      un h4 dans une correction repliée, sous un h2 : invisible au chargement, il saute un niveau une fois la
 *               correction ouverte → S (`heading-order`), avec --axe seulement ;
 *   sans_main   une page sans zone principale → S (`landmark-one-main`), avec --axe seulement.
 * Puis les sorties : sans --strict, un L ou un B sort à 1 (référence vide depuis le 22/11/2026) et C seul sort à 0 ;
 * --strict sort à 1 quand il y a un écart, 0 sur la page propre. Avec --axe, un défaut grave sort à 1 (référence vide
 * depuis le 25/11/2026), la page propre à 0 ; un défaut de structure (S) sort à 1 aussi (référence vide depuis le
 * 26/11/2026). Sans axe-core, ces points ne se jouent pas : le banc sort à 2 (n°299).
 * Usage : node _outils/tests_controle_page_ouverte.mjs   · Sortie 0 / 1, 2 si le contrôle est en panne.
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { trouverAxe } from './controle_axe.mjs';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const CONTROLE = path.join(ICI, 'controle_page_ouverte.mjs');
const D = fs.mkdtempSync(path.join(os.tmpdir(), 'page-ouverte-'));
const PHRASE = 'Les couleurs ne sont ici qu\'une aide visuelle et ce sont les formes qui portent le sens.';
const page = (corps, script = '') => `<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>t</title>
<style>body{font:16px sans-serif;margin:16px}pre{white-space:pre;overflow-x:auto}</style></head><body><main><h1>Page d'essai</h1>${corps}</main><script>${script}</script></body></html>`;
const BLOC = '<svg viewBox="0 0 200 80"><rect width="200" height="80" fill="#fb923c"/><text x="5" y="20">si &lt;condition&gt;</text><text x="5" y="45">alors</text><text x="5" y="70">sinon</text></svg>';
const fab = `function fab(){['corr1','qcorr2','corrB'].forEach((id,i)=>{document.getElementById(id).innerHTML='<p>Réponse '+(i+1)+' : étape '+i+'.</p>'+(i===2?'${BLOC.replace(/'/g, "\\'")}':'')+'<p>${PHRASE.replace(/'/g, "\\'")}</p>'})}`;
const pages = {
  propre: page('<details><summary>Correction</summary><p>La lampe s\'allume parce que la luminosité est sous le seuil de cinquante lux annoncé.</p></details><details><summary>Correction</summary><p>Le losange pose une seule question fermée, avec une sortie Oui et une sortie Non.</p></details><details><summary>Correction</summary><p>On lit le capteur avant de poser la question, sinon on teste une valeur inconnue.</p></details><pre>if x &lt; 50:\n    y = 1</pre>'),
  crochet: page('<div id="corr1" hidden></div><div id="qcorr2" hidden></div><div id="corrB" hidden></div>', `${fab};window.__toutOuvrir=fab;`),
  sans_crochet: page('<div id="corr1" hidden></div><div id="qcorr2" hidden></div><div id="corrB" hidden></div>', `${fab};`),
  codebox: page('<div class="codebox" style="font-family:monospace;white-space:pre;overflow-x:auto">' + 'valeur = lire_capteur(A0) * 100 / 1023 + correction_de_temperature(ambiante) - decalage'.padEnd(120, ' ') + '</div>'
    + '<div class="terminal" style="font-family:monospace;white-space:nowrap;overflow:hidden">Protéger ses données • Comprendre les risques • Devenir citoyen numérique éclairé</div>'
    + '<div class="codebox" style="font-family:monospace;white-space:pre-wrap;overflow-wrap:anywhere">' + 'x = 1 ; '.repeat(20) + '</div>'),
  listing: page('<pre>' + 'valeur = lire_capteur(A0) * 100 / 1023 + correction_de_temperature(ambiante) - decalage_du_capteur_mesure * 2'.padEnd(120, ' ') + '</pre>'),
  repete: page(['a', 'b', 'c'].map((x, i) => `<details><summary>Correction</summary><p>Réponse ${i + 1}, propre à cet exercice numéro ${i + 1}.</p><p data-repete>Touche ou clique le schéma pour l'agrandir et voir tous ses détails dessinés.</p></details>`).join('')),
  editeur: page('<div class="saisie"><textarea>' + 'x'.repeat(150) + '</textarea><pre aria-hidden="true">' + 'x'.repeat(150) + '</pre></div>'),
  details: page([1, 2, 3].map(i => `<details><summary>Correction ${i}</summary><p>Réponse ${i}.</p><p>${PHRASE}</p></details>`).join('')),
  contraste: page('<details><summary>Correction</summary><p style="color:#aaaaaa;background:#ffffff">La réponse est écrite trop pâle pour être lue sur un écran au soleil.</p></details>'),
  titres: page('<h2>Activité 1</h2><p>Une consigne.</p><details><summary>Correction</summary><h4>Les deux choix</h4><p>La réponse, et pourquoi.</p></details>'),
  sans_main: `<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>t</title></head><body><h1>Sans zone principale</h1><p>Un texte.</p></body></html>`,
  intitule: page([1, 2, 3].map(i => `<details><summary>Correction ${i}</summary><h4>La correction détaillée de cet exercice, question après question</h4><p><b>Question par question — la réponse, et pourquoi pas les autres</b></p><p>Réponse ${i}, propre à cet exercice.</p></details>`).join('')),
};
for (const [n, h] of Object.entries(pages)) fs.writeFileSync(path.join(D, `${n}.html`), h);

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const jouer = (fichiers, extra = []) => { const j = path.join(D, `r${T.length}.json`);
  const r = spawnSync(process.execPath, [CONTROLE, ...fichiers, '--muet', '--json', j, ...extra], { encoding: 'utf8' });
  return { code: r.status, res: fs.existsSync(j) ? JSON.parse(fs.readFileSync(j, 'utf8')) : [], out: r.stdout + r.stderr }; };

const tout = jouer(Object.keys(pages).map(n => path.join(D, `${n}.html`)));
if (tout.code === 2) { console.error('⛔ le contrôle est en panne :\n' + tout.out); process.exit(2); }
const de = n => tout.res.find(r => r.rel.endsWith(`${n}.html`)) || {};
ok('page propre : rien', !de('propre').L.length && !de('propre').B.length && !de('propre').C.length, JSON.stringify(de('propre')));
ok('crochet : le bloc dessiné par script est vu (B)', de('crochet').B.length === 1, JSON.stringify(de('crochet').B));
ok('crochet : la phrase recopiée dans 3 corrections est vue (C)', de('crochet').C.some(c => c.fois === 3), JSON.stringify(de('crochet').C));
ok('sans crochet : les corrections fabriquées par script restent invisibles (la limite que le crochet lève)', !de('sans_crochet').B.length && !de('sans_crochet').C.length);
ok('listing de 120 caractères à 390 px : il défile (L)', de('listing').L.length === 1 && de('listing').L[0].px > 100, JSON.stringify(de('listing').L));
ok('un bloc en chasse fixe qui garde ses lignes (div.codebox, bandeau nowrap) est vu ; le même en pre-wrap ne l\'est pas (L)', de('codebox').L.length === 2, JSON.stringify(de('codebox').L));
ok('le calque coloré d\'un éditeur (aria-hidden, sur sa zone de saisie) n\'est pas compté comme listing', !de('editeur').L.length, JSON.stringify(de('editeur').L));
ok('une ligne d\'aide marquée data-repete n\'est pas comptée', !de('repete').C.length, JSON.stringify(de('repete').C));
ok('trois <details> « Correction » qui répètent une phrase : vus (C), sans compter leur intitulé', de('details').C.length === 1 && !/correction \d/.test(de('details').C[0].phrase), JSON.stringify(de('details').C));
ok('un intitulé tout en gras ou un titre repris dans chaque correction n\'est pas compté', !de('intitule').C.length, JSON.stringify(de('intitule').C));
ok('sans --strict, un listing qui défile ou un bloc dessiné : sortie 1 (référence vide, n°273)', tout.code === 1, String(tout.code));
ok('sans --strict, un listing seul : sortie 1', jouer([path.join(D, 'listing.html')]).code === 1);
ok('sans --strict, des écarts C seulement : sortie 0 (mesure)', jouer(['propre', 'details', 'repete', 'editeur', 'sans_crochet', 'intitule'].map(n => path.join(D, `${n}.html`))).code === 0);
ok('--strict sur une page à écarts : sortie 1', jouer([path.join(D, 'crochet.html')], ['--strict']).code === 1);
let sansAxe = false;
if (trouverAxe()) {
  const ax = jouer([path.join(D, 'contraste.html')], ['--axe']);
  ok('--axe : un texte trop pâle dans une correction repliée est vu (A) et sort à 1, même sans --strict', ax.code === 1 && (ax.res[0] || {}).A && ax.res[0].A.some(a => a.startsWith('color-contrast')), JSON.stringify([ax.code, (ax.res[0] || {}).A]));
  ok('--axe sur la page propre : sortie 0', jouer([path.join(D, 'propre.html')], ['--axe']).code === 0);
  ok('sans --axe, la même page trop pâle sort à 0 (A n\'est pas mesuré)', jouer([path.join(D, 'contraste.html')]).code === 0);
  const ti = jouer([path.join(D, 'titres.html')], ['--axe']);
  ok('--axe : un h4 dans une correction repliée, sous un h2, est vu page ouverte (S, heading-order) et sort à 1', ti.code === 1 && (ti.res[0] || {}).S && ti.res[0].S.some(s => s.startsWith('heading-order')), JSON.stringify([ti.code, (ti.res[0] || {}).S]));
  const sm = jouer([path.join(D, 'sans_main.html')], ['--axe']);
  ok('--axe : une page sans zone principale est vue (S, landmark-one-main) et sort à 1', sm.code === 1 && (sm.res[0] || {}).S && sm.res[0].S.some(s => s.startsWith('landmark-one-main')), JSON.stringify([sm.code, (sm.res[0] || {}).S]));
  ok('sans --axe, la page aux titres qui sautent sort à 0 (S n\'est pas mesuré)', jouer([path.join(D, 'titres.html')]).code === 0);
} else sansAxe = true;
ok('--strict sur la page propre : sortie 0', jouer([path.join(D, 'propre.html')], ['--strict']).code === 0);

fs.rmSync(D, { recursive: true, force: true });
const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.ok ? '' : ' — ' + t.d}`).join('\n') + `\n${n} / ${T.length}`);
if (sansAxe) { console.log('⛔ axe-core introuvable (AXE_CORE=/chemin/vers/axe.min.js) : 6 points non joués — banc EN PANNE (n°299)'); process.exit(2); }
process.exit(n === T.length ? 0 : 1);
