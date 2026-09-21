/* tests_controle_contraste_liens.mjs — le banc de la règle d'or n°303.
 *
 * Il rejoue, sur des pages fabriquées, les deux choses que le contrôle doit
 * refuser et celles qu'il ne doit pas refuser. Chaque cas vient d'un défaut
 * réel du dépôt, pas d'une idée :
 *
 *   · le BLEU PAR DÉFAUT sur fond sombre — `rgb(0,0,238)` sur `rgb(16,41,79)`,
 *     1,54:1 : c'est le lien de l'atelier « double authentification » du Bonus
 *     de `4e_C1.4`, resté invisible sans qu'un seul contrôle le dise ;
 *   · une page qui colore `a` SANS colorer `a:visited` — 141 pages du dépôt le
 *     faisaient, et le lien y redevenait violet au premier clic ;
 *   · un BOUTON dont la couleur est écrasée UNE FOIS CLIQUÉ — le défaut de la
 *     première version de la règle : `a,a:visited{…}` pèse (0,1,1) et
 *     `.button{color:#fff}` (0,1,0), donc la règle de lien l'emportait après le
 *     clic et le texte du bouton prenait la couleur des liens sur le fond du
 *     bouton. 7,27:1 devenait 1,15:1, sans qu'un contrôle n'en dise rien ;
 *   · le PAPIER — un bleu clair lisible à l'écran tombe à 1,6:1 sur blanc.
 *
 * ET CE QU'IL NE DOIT PAS REFUSER, chacun appris d'un faux coupable :
 *
 *   · un fond TRANSLUCIDE posé sur un fond sombre : s'arrêter au premier
 *     `background-color` non nul donnait 1,16:1 là où le vrai rapport dépasse
 *     7 — cinq séquences accusées à tort ;
 *   · un lien de NAVIGATION, qui a son propre gabarit ;
 *   · un bouton-lien dont la TRANSITION n'est pas finie : mesuré pendant le
 *     changement de média, un `.btn` rendait une couleur intermédiaire et
 *     paraissait fautif alors qu'il ne l'était pas ;
 *   · un lien ORDINAIRE, qui doit garder sa couleur après le clic : sans ce
 *     cas, on pourrait « réparer » le bouton en cassant tous les autres liens.
 *
 * Usage : node _outils/tests_controle_contraste_liens.mjs
 * Sortie : 0 si tout passe, 1 sinon.
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'child_process';
import { fileURLToPath } from 'node:url';
import { main, lanceDirectement, SEUIL } from './controle_contraste_liens.mjs';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const SCRIPT = path.join(ICI, 'controle_contraste_liens.mjs');

const SOMBRE = '#10294f';   // le fond des sections de `4e_C1.4`
const CLAIR = '#f9fbff';

/* La page d'essai porte ce que TOUTES les pages du dépôt portent, et rien de
   plus : un fond sombre à l'écran, et le bloc d'impression qui le blanchit.
   Sans cette seconde ligne la fixture mentirait — elle garderait sur le papier
   un fond marine que plus aucune page du dépôt n'a, et cinq cas justes
   ressortiraient fautifs. */
const page = (corps, style = '') => `<!DOCTYPE html><html lang="fr"><head>
<meta charset="utf-8"><title>Essai</title><style>
body{background:${SOMBRE};color:#e7eefc}
@media print{body{background:#fff;color:#111}}
${style}
</style></head><body>${corps}</body></html>`;

/** Joue le contrôle sur un dépôt jetable et rend { code, texte }. */
async function jouer(racine) {
  const vraiLog = console.log, vraiErr = console.error;
  let texte = '';
  const capter = (...a) => { texte += a.join(' ') + '\n'; };
  console.log = capter; console.error = capter;
  let code;
  try { code = await main(false, racine); }
  finally { console.log = vraiLog; console.error = vraiErr; }
  return { code, texte };
}

const echecs = [];
let controles = 0;

async function cas(titre, contenu, doitRefuser, attendu = '') {
  controles++;
  const racine = fs.mkdtempSync(path.join(os.tmpdir(), 'ccl-'));
  fs.writeFileSync(path.join(racine, 'page.html'), contenu, 'utf8');
  const { code, texte } = await jouer(racine);
  fs.rmSync(racine, { recursive: true, force: true });
  const dire = (m) => echecs.push(`${titre} : ${m}\n     ${texte.trim().replace(/\n/g, '\n     ')}`);
  if (doitRefuser && code === 0) dire('acceptée, alors qu\'il fallait refuser');
  else if (!doitRefuser && code !== 0) dire('refusée');
  else if (attendu && !texte.includes(attendu)) dire(`message sans « ${attendu} »`);
}

/* la correction telle que le dépôt la porte : couleur d'écran, `a:visited`,
   couleur d'impression. C'est elle qu'on mute, cas par cas. */
const CORRIGE = 'a,a:visited{color:#9ecbff}\n'
  + '@media print{a,a:visited{color:#00309e!important}\n'
  + 'a.btn,a.button,a.bouton{color:#00309e!important;background:#fff!important;'
  + 'border:1px solid #00309e!important}}';

// ══ CE QU'IL DOIT REFUSER ═══════════════════════════════════════════════════
await cas('le bleu par défaut du navigateur sur un fond sombre',
  page('<p>Ouvre <a href="x.html">l\'atelier double authentification</a>.</p>'),
  true, 'bleu par défaut');

await cas('MUTATION — un lien corrigé, mais sans `a:visited`',
  page('<p>Ouvre <a href="x.html">l\'atelier</a>.</p>',
       'a{color:#9ecbff}\n@media print{a{color:#00309e!important}}'),
  true, 'a:visited');

await cas('MUTATION — un lien lisible à l\'écran, mais pas sur le papier',
  page('<p>Ouvre <a href="x.html">l\'atelier</a>.</p>',
       'a,a:visited{color:#9ecbff}'),
  true, 'SUR LE PAPIER');

await cas('MUTATION — une couleur d\'écran recopiée d\'une autre page',
  // #9ecbff donne 10,06 sur un fond et 2,9 sur celui-ci : la couleur se vérifie
  // contre LE fond de CETTE page, jamais contre celui de la voisine.
  page('<div class="pale"><p>Ouvre <a href="x.html">l\'atelier</a>.</p></div>',
       `.pale{background:#7ba7d8}\n${CORRIGE}`),
  true);

// ══ CE QU'IL NE DOIT PAS REFUSER ════════════════════════════════════════════
await cas('un lien corrigé : couleur d\'écran, `a:visited`, couleur de papier',
  page('<p>Ouvre <a href="x.html">l\'atelier</a>.</p>', CORRIGE),
  false, 'se lit sur son fond réel');

await cas('un voile TRANSLUCIDE ne remplace pas le fond qu\'il couvre',
  // le faux coupable des cinq séquences `station_*` : rgba(…,0.06) pris pour
  // le fond donnait 1,16:1 au lieu de plus de 7.
  page('<div class="voile"><p>Ouvre <a href="x.html">l\'atelier</a>.</p></div>',
       `.voile{background:rgba(155,190,252,0.06)}\n${CORRIGE}`),
  false);

await cas('un lien de NAVIGATION n\'est pas jugé ici',
  page('<nav><a href="i.html">Accueil</a></nav>'
     + `<p>Ouvre <a href="x.html">l'atelier</a>.</p>`, CORRIGE),
  false);

await cas('un bouton-lien dont la transition n\'est pas finie n\'est pas fautif',
  page('<p><a class="btn" href="q.html">Ouvrir le QCM</a></p>',
       `.btn{background:#205ea8;color:#fff;transition:color 4s,background 4s}\n${CORRIGE}`),
  false);

// ══ L'ÉTAT VISITÉ — ce que #412 croyait immesurable ═════════════════════════
await cas('MUTATION — un bouton coloré par sa classe, écrasé une fois CLIQUÉ',
  // Le défaut de #412, mesuré par Pascal : `a,a:visited{color:…}` pèse (0,1,1),
  // `.button{color:#fff}` pèse (0,1,0). Avant le clic, la classe gagne ; après,
  // la règle de lien gagne, et le texte du bouton prend la couleur des liens
  // SUR LE FOND DU BOUTON. 7,27:1 devient 1,15:1, sans qu'un seul contrôle
  // n'en dise rien.
  page('<p><a class="button" href="d.csv">Télécharger le CSV original</a></p>',
       ['.button{background:#155e75;color:#fff;padding:6px 10px;border-radius:8px}',
        'a,a:visited{color:#1d4e89}',
        '@media print{a,a:visited{color:#00309e!important}}'].join('\n')),
  true, 'UNE FOIS CLIQUÉS');

await cas('le même bouton, protégé par `:where(:visited)`',
  // `:where()` remet la spécificité à zéro : `a:where(:visited)` pèse (0,0,1),
  // donc `.button` (0,1,0) l'emporte, cliqué ou non.
  page('<p><a class="button" href="d.csv">Télécharger le CSV original</a></p>',
       ['.button{background:#155e75;color:#fff;padding:6px 10px;border-radius:8px}',
        'a,a:where(:visited){color:#9ecbff}',
        '@media print{a,a:visited{color:#00309e!important}',
        'a.btn,a.button,a.bouton{color:#00309e!important;background:#fff!important;'
        + 'border:1px solid #00309e!important}}'].join('\n')),
  false);

await cas('un lien ordinaire garde bien sa couleur une fois cliqué',
  // `:where()` ne doit pas faire DISPARAÎTRE la règle : le lien sans classe
  // reste lisible après le clic. Sans ce cas, on pourrait « corriger » le
  // bouton en cassant tous les autres liens sans le voir.
  page('<p>Ouvre <a href="x.html">l\'atelier</a>.</p>', CORRIGE),
  false);

// ══ LA PANNE, ET LA GARDE DE LANCEMENT ══════════════════════════════════════
controles++;
{
  const vide = fs.mkdtempSync(path.join(os.tmpdir(), 'ccl-vide-'));
  const { code } = await jouer(vide);
  fs.rmSync(vide, { recursive: true, force: true });
  if (code !== 2) echecs.push(`un dépôt sans page doit sortir EN PANNE (2), pas ${code}`);
}

controles++;
if (!lanceDirectement(new URL('file:///C:/Users/PHASEL%7E1/x/controle_contraste_liens.mjs').href,
                      'C:\\Users\\PHASEL~1\\x\\controle_contraste_liens.mjs')) {
  echecs.push('la garde de lancement doit reconnaître le même chemin sous Windows');
}
controles++;
if (lanceDirectement(import.meta.url, path.join(ICI, 'autre_script.mjs'))) {
  echecs.push('la garde de lancement ne doit pas partir pour un autre script');
}

controles++;
{
  // importé, il ne doit RIEN faire tout seul (règle d'or n°299)
  const r = spawnSync(process.execPath, ['--input-type=module', '-e',
    `import ${JSON.stringify('file://' + SCRIPT.replace(/\\/g, '/'))};`],
    { encoding: 'utf8', timeout: 120000 });
  if ((r.stdout || '').trim()) echecs.push('importé, le contrôle écrit alors qu\'il ne doit rien faire');
}

controles++;
if (SEUIL !== 4.5) echecs.push(`le seuil doit être 4,5:1 (WCAG AA), pas ${SEUIL}`);

// ══ VERDICT ════════════════════════════════════════════════════════════════
if (echecs.length) {
  console.log('');
  for (const e of echecs) console.log('❌ ' + e);
  console.log(`\n${controles - echecs.length} / ${controles}`);
  process.exit(1);
}
console.log(`✅ ${controles} contrôles — refusés : le bleu par défaut, l'absence de `
  + '`a:visited`, le papier, et le bouton dont la couleur est écrasée UNE FOIS');
console.log('   CLIQUÉ ; acceptés : le voile translucide, la navigation, la transition');
console.log('   en cours, et le lien ordinaire qui garde sa couleur après le clic');
console.log(`\n${controles} / ${controles}`);
process.exit(0);
