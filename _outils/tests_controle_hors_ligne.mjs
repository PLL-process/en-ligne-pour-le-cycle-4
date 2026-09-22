/* tests_controle_hors_ligne.mjs — le banc de la règle d'or n°305.
 *
 * Chaque cas est une page fabriquée, rangée seule dans un dossier temporaire,
 * et jugée par le VRAI contrôle (main), méthode navigateur comprise. Le banc
 * dit pour chacun ce qui doit arriver, et le vérifie.
 *
 * Les cinq mutations demandées :
 *   · une police Google Fonts                       → refusée
 *   · un url(https://…) dans un attribut style       → refusé
 *   · un fetch('https://…')                         → refusé
 *   · un <a href="https://…"> de source             → accepté
 *   · une activité vers Vittascience sans 🌐         → refusée
 * Et ce que l'écriture du contrôle a appris :
 *   · la même activité AVEC la mention au début      → acceptée
 *   · la mention posée APRÈS le lien, en fin de bloc  → refusée : « à son début »
 *   · du code Python AFFICHÉ qui contient https://   → accepté : 3e_C1.5 enseigne HTTPS
 *   · une vidéo avec son « Si la vidéo ne s'ouvre pas » → acceptée ; sans repli → refusée
 *   · une adresse CONSTRUITE en JavaScript           → la source ne la voit pas,
 *     le navigateur si : c'est la raison d'être de la méthode b
 *   · un dossier sans page                           → sortie 2, jamais 0
 *   · le script lancé pour de vrai                   → il écrit quelque chose
 *
 * Usage : node _outils/tests_controle_hors_ligne.mjs   Sortie : 0 si tout passe.
 */
import fs from 'fs';
import os from 'os';
import path from 'path';
import { spawnSync } from 'child_process';
import { fileURLToPath } from 'url';
import { main, chargementsDansLaSource } from './controle_hors_ligne.mjs';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const page = (corps, tete = '') => `<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>t</title>${tete}</head><body>${corps}</body></html>`;
const VITTA = '<a class="btn vs-lien" href="https://fr.vittascience.com/python/?mode=mixed">▶ Ouvrir l\'éditeur</a>';
const MENTION = '<p class="activite-en-ligne">🌐 <b>Cette activité demande une connexion Internet.</b></p>';

const CAS = [
  ['une police Google Fonts', 1, page('<p>x</p>', '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter">')],
  ['un url(https://…) dans un attribut style', 1, page('<div style="background:url(https://example.org/fond.png)">x</div>')],
  ['un fetch(\'https://…\')', 1, page('<p>x</p><script>fetch(\'https://example.org/donnees.json\').catch(()=>{})</script>')],
  ['un <a href> de source', 0, page('<p>Source : <a href="https://www.arcep.fr/rapport.pdf">rapport de l\'Arcep</a></p>')],
  ['une activité Vittascience sans 🌐', 1, page(`<section class="card"><h2>Activité 3</h2><p>Consigne.</p>${VITTA}</section>`)],
  ['la même activité avec la mention au début', 0, page(`<section class="card"><h2>Activité 3</h2>${MENTION}<p>Consigne.</p>${VITTA}</section>`)],
  ['la mention posée après le lien', 1, page(`<section class="card"><h2>Activité 3</h2><p>a</p><p>b</p><p>c</p>${VITTA}${MENTION}</section>`)],
  ['du code Python affiché qui contient https://', 0, page('<pre><code>if url.startswith("https://"):\n    requests.get("https://example.org")</code></pre>')],
  ['une vidéo avec son repli', 0, page('<section class="ressource"><h4>Vidéo</h4><a class="ressource-lien" href="https://www.youtube.com/watch?v=x">▶</a><div class="ressource-repli"><p>Si la vidéo ne s\'ouvre pas…</p></div></section>')],
  ['une vidéo sans repli', 1, page('<section class="card"><h2>Regarde</h2><p>…</p><a href="https://www.youtube.com/watch?v=x">▶</a></section>')],
];

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'hors-ligne-'));
let ok = 0, ko = 0;
const dire = (bon, m) => { console.log((bon ? '✅ ' : '❌ ') + m); bon ? ok++ : ko++; };
const silence = async (f) => { const l = console.log, e = console.error; console.log = console.error = () => {}; try { return await f(); } finally { console.log = l; console.error = e; } };

for (const [nom, attendu, html] of CAS) {
  const d = fs.mkdtempSync(path.join(tmp, 'cas-'));
  fs.writeFileSync(path.join(d, 'page.html'), html);
  const rc = await silence(() => main([d]));
  dire(rc === attendu, `${nom} → ${attendu ? 'refusé' : 'accepté'} (sortie ${rc})`);
}

// l'adresse construite : la source seule ne la voit pas, le navigateur si
{
  const html = page('<p>x</p><script>const h = "https:" + "/" + "/example.org"; const i = new Image(); i.src = h + "/logo.png";</script>');
  dire(chargementsDansLaSource(html).length === 0, 'adresse construite en JavaScript : invisible à la lecture de la source (attendu)');
  const d = fs.mkdtempSync(path.join(tmp, 'cas-'));
  fs.writeFileSync(path.join(d, 'page.html'), html);
  dire(await silence(() => main([d])) === 1, 'adresse construite en JavaScript : vue et refusée par le navigateur réseau coupé');
}
// la panne : rien à lire ne sort jamais à 0
{
  const vide = fs.mkdtempSync(path.join(tmp, 'vide-'));
  dire(await silence(() => main([vide])) === 2, 'dossier sans page → sortie 2 (en panne), pas 0');
}
// lancé pour de vrai : la garde de lancement fonctionne, le script parle
{
  const d = fs.mkdtempSync(path.join(tmp, 'cas-'));
  fs.writeFileSync(path.join(d, 'page.html'), CAS[3][2]);
  const r = spawnSync(process.execPath, [path.join(ICI, 'controle_hors_ligne.mjs'), d], { encoding: 'utf8', env: process.env });
  dire(r.status === 0 && /page\(s\) lue\(s\)/.test(r.stdout), `lancé en sous-processus : sortie ${r.status}, ${r.stdout.length} caractères écrits`);
}

fs.rmSync(tmp, { recursive: true, force: true });
console.log(`\n${ok} / ${ok + ko}`);
process.exit(ko ? 1 : 0);
