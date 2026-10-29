/* tests_controle_schemas.mjs — banc de controle_schemas.mjs (règle d'or n°315).
 * Des schémas fabriqués pour l'occasion, chacun avec UN défaut connu (ou aucun) ; le contrôle doit trouver
 * exactement ce défaut-là, et rien sur les schémas propres.
 * Usage : node _outils/tests_controle_schemas.mjs
 */
import fs from 'fs';
import os from 'os';
import path from 'path';
import { execFileSync } from 'child_process';
import { fileURLToPath } from 'url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'schemas-'));
const svg = (corps, h = 300) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 ${h}" font-family="sans-serif" font-size="14">
  <defs><marker id="m" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" viewBox="0 0 10 10"><path d="M0 0L10 5L0 10z"/></marker></defs>
  <rect width="600" height="${h}" fill="#fff"/>${corps}</svg>`;
const cadre = (x, y, w, h, t) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="8" fill="#eef" stroke="#336"/><text x="${x + 12}" y="${y + h / 2 + 5}">${t}</text>`;

const CAS = {
  propre: svg(cadre(20, 40, 160, 60, 'La station') + cadre(300, 40, 160, 60, 'Les usagers')
    + `<path d="M188 70 H 292" stroke="#336" stroke-width="2" fill="none" marker-end="url(#m)"/>`),
  contact: svg(cadre(20, 40, 160, 60, 'La station') + cadre(184, 40, 160, 60, 'Les usagers')),
  chevauchement: svg(cadre(20, 40, 160, 60, 'La station') + cadre(150, 80, 160, 60, 'Les usagers')),
  debordement: svg(cadre(20, 40, 120, 60, 'Un texte bien trop long pour sa boîte')),
  traversee: svg(cadre(20, 120, 140, 60, 'Départ') + cadre(230, 120, 140, 60, 'Obstacle') + cadre(440, 120, 140, 60, 'Arrivée')
    + `<path d="M168 150 H 432" stroke="#336" stroke-width="2" fill="none" marker-end="url(#m)"/>`),
  superposes: svg(`<text x="40" y="60">Premier texte ici</text><text x="46" y="62">Second texte là</text>`),
  tableau: svg(cadre(20, 40, 160, 40, 'Famille') + cadre(180, 40, 160, 40, 'Exemple') + cadre(20, 80, 160, 40, 'Usager') + cadre(180, 80, 160, 40, 'Le cycliste')),
  ecrasee: svg(`<style>text{font-size:13px}</style>` + cadre(20, 40, 260, 60, 'Titre').replace('<text ', '<text font-size="22" ')),
  inclus: svg(`<rect x="20" y="20" width="400" height="200" rx="12" fill="#eef" stroke="#336"/><text x="40" y="50">Le système</text>`
    + cadre(60, 80, 160, 60, 'Un composant')),
};
for (const [n, s] of Object.entries(CAS)) fs.writeFileSync(path.join(tmp, `${n}.svg`), s);
const sortie = path.join(tmp, 'r.json');
try { execFileSync('node', [path.join(ICI, 'controle_schemas.mjs'), tmp, '--json', sortie, '--muet'], { stdio: 'pipe' }); } catch (e) { /* 1 = au moins un ✘ : attendu */ }
const R = Object.fromEntries(JSON.parse(fs.readFileSync(sortie, 'utf8')).map(r => [path.basename(r.schema, '.svg'), r]));
let ok = 0, ko = 0;
const t = (nom, c, d = '') => { if (c) ok++; else { ko++; console.log('  ✘', nom, d); } };
const types = n => R[n].defauts.filter(d => d.g === '✘').map(d => d.type);
t('schéma propre : aucun ✘, aucun ⚠', R.propre.score === 0, JSON.stringify(R.propre.defauts));
t('deux cadres à 4 unités : contact', types('contact').includes('contact'));
t('deux cadres qui se chevauchent : contact', types('chevauchement').includes('contact'));
t('texte plus long que sa boîte : débordement', types('debordement').includes('débordement'));
t('flèche qui passe dans un cadre : traversée', types('traversee').includes('traversée'));
t('flèche qui passe dans un cadre : le départ et l\'arrivée ne comptent pas', types('traversee').length === 2, JSON.stringify(R.traversee.defauts));
t('deux textes l\'un sur l\'autre : superposés', types('superposes').includes('superposés'));
t('cellules d\'un tableau bord contre bord : rien', R.tableau.croix === 0, JSON.stringify(R.tableau.defauts));
t('taille en attribut écrasée par la feuille de style : ⚠ écrasée', R.ecrasee.defauts.some(d => d.type === 'écrasée'));
t('un cadre dans un autre : pas un contact', R.inclus.croix === 0, JSON.stringify(R.inclus.defauts));
fs.rmSync(tmp, { recursive: true, force: true });
console.log(`${ok} / ${ok + ko} tests réussis`);
process.exit(ko ? 1 : 0);
