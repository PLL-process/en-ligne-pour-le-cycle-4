/* tests_controle_page_ouverte.mjs — banc de `controle_page_ouverte.mjs` (règle d'or n°346).
 *
 * Six pages fabriquées dans un dossier temporaire, chacune pour une frontière :
 *   propre      corrections différentes, listing court → rien ;
 *   crochet     corrections fabriquées par `window.__toutOuvrir()`, avec la même phrase et un bloc dessiné → B et C ;
 *   sans_crochet les mêmes corrections, sans crochet → rien (c'est la limite que le crochet lève) ;
 *   listing     une ligne de code de 120 caractères à 390 px → L ;
 *   repete      une ligne d'aide marquée `data-repete` dans chaque correction → rien ;
 *   details     trois <details> « Correction » qui répètent une phrase → C.
 * Puis : --strict sort à 1 quand il y a un écart, 0 sur la page propre.
 * Usage : node _outils/tests_controle_page_ouverte.mjs   · Sortie 0 / 1, 2 si le contrôle est en panne.
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const CONTROLE = path.join(ICI, 'controle_page_ouverte.mjs');
const D = fs.mkdtempSync(path.join(os.tmpdir(), 'page-ouverte-'));
const PHRASE = 'Les couleurs ne sont ici qu\'une aide visuelle et ce sont les formes qui portent le sens.';
const page = (corps, script = '') => `<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>t</title>
<style>body{font:16px sans-serif;margin:16px}pre{white-space:pre;overflow-x:auto}</style></head><body>${corps}<script>${script}</script></body></html>`;
const BLOC = '<svg viewBox="0 0 200 80"><rect width="200" height="80" fill="#fb923c"/><text x="5" y="20">si &lt;condition&gt;</text><text x="5" y="45">alors</text><text x="5" y="70">sinon</text></svg>';
const fab = `function fab(){['corr1','qcorr2','corrB'].forEach((id,i)=>{document.getElementById(id).innerHTML='<p>Réponse '+(i+1)+' : étape '+i+'.</p>'+(i===2?'${BLOC.replace(/'/g, "\\'")}':'')+'<p>${PHRASE.replace(/'/g, "\\'")}</p>'})}`;
const pages = {
  propre: page('<details><summary>Correction</summary><p>La lampe s\'allume parce que la luminosité est sous le seuil de cinquante lux annoncé.</p></details><details><summary>Correction</summary><p>Le losange pose une seule question fermée, avec une sortie Oui et une sortie Non.</p></details><details><summary>Correction</summary><p>On lit le capteur avant de poser la question, sinon on teste une valeur inconnue.</p></details><pre>if x &lt; 50:\n    y = 1</pre>'),
  crochet: page('<div id="corr1" hidden></div><div id="qcorr2" hidden></div><div id="corrB" hidden></div>', `${fab};window.__toutOuvrir=fab;`),
  sans_crochet: page('<div id="corr1" hidden></div><div id="qcorr2" hidden></div><div id="corrB" hidden></div>', `${fab};`),
  listing: page('<pre>' + 'valeur = lire_capteur(A0) * 100 / 1023 + correction_de_temperature(ambiante) - decalage_du_capteur_mesure * 2'.padEnd(120, ' ') + '</pre>'),
  repete: page(['a', 'b', 'c'].map((x, i) => `<details><summary>Correction</summary><p>Réponse ${i + 1}, propre à cet exercice numéro ${i + 1}.</p><p data-repete>Touche ou clique le schéma pour l'agrandir et voir tous ses détails dessinés.</p></details>`).join('')),
  details: page([1, 2, 3].map(i => `<details><summary>Correction ${i}</summary><p>Réponse ${i}.</p><p>${PHRASE}</p></details>`).join('')),
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
ok('une ligne d\'aide marquée data-repete n\'est pas comptée', !de('repete').C.length, JSON.stringify(de('repete').C));
ok('trois <details> « Correction » qui répètent une phrase : vus (C), sans compter leur intitulé', de('details').C.length === 1 && !/correction \d/.test(de('details').C[0].phrase), JSON.stringify(de('details').C));
ok('mesure sans --strict : sortie 0', tout.code === 0, String(tout.code));
ok('--strict sur une page à écarts : sortie 1', jouer([path.join(D, 'crochet.html')], ['--strict']).code === 1);
ok('--strict sur la page propre : sortie 0', jouer([path.join(D, 'propre.html')], ['--strict']).code === 0);

fs.rmSync(D, { recursive: true, force: true });
const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.ok ? '' : ' — ' + t.d}`).join('\n') + `\n${n} / ${T.length}`);
process.exit(n === T.length ? 0 : 1);
