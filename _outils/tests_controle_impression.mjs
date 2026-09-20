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
 * ET, DEPUIS LE 19/09/2026, CE QUI A MANQUÉ TROIS SEMAINES
 * --------------------------------------------------------
 * Du 02/09 au 19/09, ce contrôle n'a rien contrôlé sous Windows : sa garde de
 * lancement comparait deux CHAÎNES qui ne s'y écrivent jamais pareil, main() ne
 * partait pas, et le script sortait à 0 sans une ligne. Le banc ne l'a pas vu,
 * parce qu'il appelait main() en direct — il ne passait jamais par la garde.
 *
 * Trois familles de cas ferment la porte :
 *
 *   · la GARDE elle-même, interrogée dans les deux sens, y compris sur un nom de
 *     fichier accentué — que l'ancienne comparaison de chaînes ratait sur TOUTES
 *     les plateformes, Linux compris, à cause de l'encodage pour-cent ;
 *   · le script LANCÉ POUR DE VRAI, en sous-processus : s'il n'écrit rien, c'est
 *     exactement le défaut du 02/09, et le banc le refuse ;
 *   · le script PRIVÉ DE SES FICHIERS : sans page à lire, il doit sortir à 2 en
 *     disant qu'il est en panne — jamais à 0 en laissant croire à un dépôt sain.
 *
 * Usage : node _outils/tests_controle_impression.mjs
 * Sortie : 0 si tout passe, 1 sinon.
 */

import fs from 'fs';
import os from 'os';
import path from 'path';
import { spawnSync } from 'child_process';
import { pathToFileURL } from 'url';
import { main, DEPOT, TOLEREES, lanceDirectement } from './controle_impression.mjs';

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
  //: Les deux flux, parce que les messages de panne sortent sur stderr : ils
  //: doivent rester visibles même sous --muet.
  const vraiLog = console.log, vraiErr = console.error;
  let texte = '';
  const capter = (...a) => { texte += a.join(' ') + '\n'; };
  console.log = capter; console.error = capter;
  let code;
  try { code = await main(false, racine, tolerees); }
  finally { console.log = vraiLog; console.error = vraiErr; }
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

// ══ PRIVÉ DE SES FICHIERS, IL EST EN PANNE — PAS VERT ═══════════════════════
//: Le cœur de la correction du 19/09. Un contrôle sans rien à contrôler sortait
//: à 0, comme un succès. Il sort désormais à 2, et il écrit pourquoi.
{
  controles++;
  const racine = fs.mkdtempSync(path.join(os.tmpdir(), 'ci-'));
  ecrire(racine, 'notes.txt', 'un fichier qui n’est pas une page');
  const { code, texte } = await jouer(racine);
  fs.rmSync(racine, { recursive: true, force: true });
  const vu = texte.trim().replace(/\n/g, '\n     ');
  if (code === 0) echecs.push(`aucune page à lire, et le contrôle sort à 0 — c’est le défaut du 02/09\n     ${vu}`);
  else if (code !== 2) echecs.push(`aucune page à lire : sortie ${code}, attendu 2\n     ${vu}`);
  else if (!texte.includes('EN PANNE')) echecs.push(`aucune page à lire : il sort à 2 sans dire qu’il est en panne\n     ${vu}`);
}

{
  controles++;
  const absente = path.join(os.tmpdir(), 'racine-qui-n-existe-pas-' + Date.now());
  const { code, texte } = await jouer(absente);
  const vu = texte.trim().replace(/\n/g, '\n     ');
  if (code === 0) echecs.push(`racine inexistante, et le contrôle sort à 0\n     ${vu}`);
  else if (code !== 2) echecs.push(`racine inexistante : sortie ${code}, attendu 2\n     ${vu}`);
  else if (!texte.includes('EN PANNE')) echecs.push(`racine inexistante : il sort à 2 sans dire qu’il est en panne\n     ${vu}`);
}

// ══ LA GARDE DE LANCEMENT, DANS LES DEUX SENS ═══════════════════════════════
const SCRIPT = path.join(DEPOT, '_outils', 'controle_impression.mjs');
{
  controles++;
  const href = pathToFileURL(SCRIPT).href;
  //: Un nom accentué : l’URL l’encode en pour-cent, le chemin non. L’ancienne
  //: comparaison de chaînes le ratait sur TOUTES les plateformes, Linux compris.
  const accentue = path.join(os.tmpdir(), 'contrôle été.mjs');
  if (pathToFileURL(accentue).href === `file://${accentue}`)
    echecs.push('le cas accentué ne prouve plus rien : l’URL et le chemin coïncident');

  for (const [quoi, obtenu, attendu] of [
    ['lancé par son chemin absolu', lanceDirectement(href, SCRIPT), true],
    ['lancé par un chemin relatif', lanceDirectement(href, path.relative(process.cwd(), SCRIPT)), true],
    ['un nom accentué, encodé en pour-cent dans l’URL',
      lanceDirectement(pathToFileURL(accentue).href, accentue), true],
    ['un AUTRE fichier en argv[1]',
      lanceDirectement(href, path.join(DEPOT, '_outils', 'tests_controle_impression.mjs')), false],
    ['aucun argv[1] — le script est importé', lanceDirectement(href, undefined), false],
  ]) if (obtenu !== attendu) echecs.push(`garde de lancement, ${quoi} : ${obtenu}, attendu ${attendu}`);
}

//: IMPORTÉ, il ne doit rien lancer tout seul. Si la garde se déclenchait à
//: l’import, l’enfant imprimerait le rapport complet en plus de son témoin.
{
  controles++;
  const enfant = spawnSync(process.execPath, ['--input-type=module', '-e',
    `import(${JSON.stringify(pathToFileURL(SCRIPT).href)}).then(() => console.log('IMPORT-SEUL'))`],
    { encoding: 'utf8', timeout: 180000 });
  const sorti = (enfant.stdout || '') + (enfant.stderr || '');
  if (!sorti.includes('IMPORT-SEUL')) echecs.push(`importé, le module n’a pas été chargé :\n     ${sorti.trim()}`);
  else if (sorti.includes('page(s) ouvertes')) echecs.push(`importé, le contrôle est parti tout seul :\n     ${sorti.trim()}`);
}

// ══ LANCÉ POUR DE VRAI, SUR LE DÉPÔT RÉEL ═══════════════════════════════════
//: Ce cas remplace l’appel direct à main() : il passe par la ligne de commande,
//: donc par la garde. Sous l’ancienne garde il sortait à 0 SANS UNE LIGNE — et
//: c’est précisément cela qu’on refuse ici.
let mesure = '';
{
  controles++;
  const lance = spawnSync(process.execPath, [SCRIPT], { encoding: 'utf8', timeout: 600000 });
  const sortie = (lance.stdout || '').trim();
  mesure = sortie.split('\n')[0] || '';
  if (!sortie) echecs.push(`lancé en ligne de commande, le script n’écrit RIEN (sortie ${lance.status})`
    + ` — c’est exactement le défaut du 02/09`);
  else if (lance.status !== 0) echecs.push(`le dépôt réel ne passe pas (sortie ${lance.status}) :\n     `
    + sortie.replace(/\n/g, '\n     '));
  else if (!sortie.includes('page(s) ouvertes')) echecs.push(`lancé en ligne de commande, le rapport manque :\n     `
    + sortie.replace(/\n/g, '\n     '));
}

if (echecs.length) {
  for (const e of echecs) console.log('❌ ' + e);
  console.log(`\n${controles - echecs.length} / ${controles}`);
  process.exit(1);
}
console.log(`✅ ${controles} contrôles — le sombre-sur-sombre est refusé, et rien d’autre ne l’est ;`);
console.log(`   le script lancé en ligne de commande parle, et privé de pages il sort en panne.`);
if (mesure) console.log(`   Dépôt réel : ${mesure}`);
console.log(`\n${controles} / ${controles}`);
