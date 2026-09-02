/* tests_controle_impression.mjs — le banc du contrôle d'impression.
 *
 * Il rejoue, sur des pages fabriquées, la seule chose que le contrôle refuse
 * (un texte sombre sur un fond resté sombre) et les quatre choses qu'il ne doit
 * PAS refuser, chacune apprise d'une erreur réelle :
 *
 *   · le texte BLANC sur fond sombre — lisible sur le papier ; le refuser aurait
 *     accusé dix-neuf pages dont l'en-tête se lit très bien (erreur du 02/09) ;
 *   · le texte pâle sur fond clair — une seconde dette, réelle, mais qui demande
 *     une décision de palette et non un correctif mécanique ;
 *   · un élément CACHÉ, ou dont un ANCÊTRE est caché — le bandeau des tâches, que
 *     chaque page masque à l'impression, avait produit vingt faux défauts
 *     (règle d'or n°282) ;
 *   · une page nommée dans TOLEREES avec sa raison.
 *
 * Usage : node _outils/tests_controle_impression.mjs
 * Sortie : 0 si tout passe, 1 sinon.
 */

import fs from 'fs';
import os from 'os';
import path from 'path';
import { main, DEPOT, TOLEREES } from './controle_impression.mjs';

const SOMBRE = '#0a1b3d';

function page(corps, style = '') {
  return `<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>t</title>
<style>body{background:#fff;color:#111}${style}</style></head><body>${corps}</body></html>\n`;
}

function ecrire(racine, nom, contenu) {
  const p = path.join(racine, nom);
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, contenu);
}

/** Joue le contrôle sur un dépôt jetable et rend { code, texte }. */
async function jouer(racine, tolerees = {}) {
  const vrai = console.log;
  let texte = '';
  console.log = (...a) => { texte += a.join(' ') + '\n'; };
  let code;
  try { code = await main(false, racine, tolerees); }
  finally { console.log = vrai; }
  return { code, texte };
}

const echecs = [];
let controles = 0;

async function cas(titre, contenu, doitRefuser, attendu = '', tolerees = {}) {
  controles++;
  const racine = fs.mkdtempSync(path.join(os.tmpdir(), 'ci-'));
  ecrire(racine, 'page.html', contenu);
  const { code, texte } = await jouer(racine, tolerees);
  fs.rmSync(racine, { recursive: true, force: true });
  const dire = m => echecs.push(`${titre} : ${m}\n     ${texte.trim().replace(/\n/g, '\n     ')}`);
  if (doitRefuser && code === 0) dire('acceptée, alors qu’il fallait refuser');
  else if (!doitRefuser && code !== 0) dire('refusée');
  else if (attendu && !texte.includes(attendu)) dire(`message sans « ${attendu} »`);
}

// ══ CE QU'IL DOIT REFUSER ═══════════════════════════════════════════════════
await cas('un texte sombre sur un fond resté sombre',
  page(`<div class="panneau"><p>Le texte que personne ne lira sur le papier.</p></div>`,
       `.panneau{background:${SOMBRE}}`),
  true, 'il disparaît');

// ══ LES QUATRE QU'IL NE DOIT PAS REFUSER ════════════════════════════════════
await cas('un texte BLANC sur fond sombre est lisible : compté, pas refusé',
  page(`<div class="bandeau"><h1>Un titre en blanc sur marine</h1></div>`,
       `.bandeau{background:${SOMBRE};color:#fff}`),
  false, 'blancs sur un fond resté sombre');

await cas('un texte pâle sur fond clair est une dette, pas un refus',
  page(`<p class="sous">Un sous-titre pâle, lisible de justesse.</p>`,
       `.sous{color:#9bbefc}`),
  false, 'sous 4,5 : 1 sur fond clair');

await cas('un élément caché ne s’imprime pas',
  page(`<div class="panneau" style="display:none"><p>Texte d’un bloc masqué.</p></div>`,
       `.panneau{background:${SOMBRE}}`),
  false);

await cas('un élément dont un ANCÊTRE est caché ne s’imprime pas non plus (règle n°282)',
  page(`<div id="bandeau"><ul><li>Une tâche que l’impression ne montre jamais.</li></ul></div>`,
       `#bandeau{background:${SOMBRE};display:none}`),
  false);

await cas('une page nommée dans TOLEREES passe, avec sa raison',
  page(`<div class="panneau"><p>Le texte que personne ne lira sur le papier.</p></div>`,
       `.panneau{background:${SOMBRE}}`),
  false, 'tolérée(s), chacune avec sa raison',
  { 'page.html': 'raison écrite, et ce qui la débloquera' });

// ══ UNE TOLÉRÉE DEVENUE PROPRE EST SIGNALÉE ═════════════════════════════════
{
  controles++;
  const racine = fs.mkdtempSync(path.join(os.tmpdir(), 'ci-'));
  ecrire(racine, 'page.html', page(`<p>Du texte noir sur du blanc, et rien d’autre.</p>`));
  const { texte } = await jouer(racine, { 'page.html': 'raison périmée' });
  fs.rmSync(racine, { recursive: true, force: true });
  if (!texte.includes('peut sortir de TOLEREES'))
    echecs.push('une tolérée redevenue propre n’est pas signalée\n     ' + texte.trim());
}

// ══ LA PAGE PROPRE, ET CE QUI EST ÉCARTÉ ════════════════════════════════════
await cas('une page entièrement noire sur blanc ne déclenche rien',
  page(`<p>Du texte noir sur du blanc, et rien d’autre.</p>`), false, '0 page(s) refusée(s)');

{
  controles++;
  const racine = fs.mkdtempSync(path.join(os.tmpdir(), 'ci-'));
  ecrire(racine, '_archive-anciennes-versions/vieux.html',
    page(`<div class="p"><p>Une version gelée, noir sur noir.</p></div>`, `.p{background:${SOMBRE}}`));
  ecrire(racine, '_outils/gabarit.html',
    page(`<div class="p"><p>Un gabarit d’outillage, noir sur noir.</p></div>`, `.p{background:${SOMBRE}}`));
  ecrire(racine, 'page.html', page(`<p>Du texte noir sur du blanc.</p>`));
  const { code } = await jouer(racine);
  fs.rmSync(racine, { recursive: true, force: true });
  if (code !== 0) echecs.push('l’archive et _outils devraient être écartés, et ne le sont pas');
}

// ══ LE DÉPÔT RÉEL DOIT PASSER ═══════════════════════════════════════════════
{
  controles++;
  const { code, texte } = await jouer(DEPOT, TOLEREES);
  if (code !== 0) echecs.push('le dépôt réel ne passe pas :\n     ' + texte.trim().replace(/\n/g, '\n     '));
}

if (echecs.length) {
  for (const e of echecs) console.log('❌ ' + e);
  console.log(`\n${controles - echecs.length} / ${controles}`);
  process.exit(1);
}
console.log(`✅ ${controles} contrôles — le sombre-sur-sombre est refusé, et rien d’autre ne l’est`);
console.log(`\n${controles} / ${controles}`);
