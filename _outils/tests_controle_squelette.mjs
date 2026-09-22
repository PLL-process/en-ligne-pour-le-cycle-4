/* tests_controle_squelette.mjs — le banc de la règle d'or n°306.
 *
 * Chaque cas est une séquence fabriquée (sequence_banc.html, seule dans un dossier
 * temporaire), jugée par le VRAI contrôle, navigateur compris.
 *
 * Les trois mutations demandées :
 *   · clôture HORS des panneaux (le défaut de 3e_C1.1 avant #418)   → refusée (D1)
 *   · clôture DANS le dernier panneau                               → acceptée
 *   · « Je me positionne » visible à la séance 1                    → refusé (D1)
 * Et ce que l'écriture du contrôle a appris :
 *   · page sans onglets, Bonus → Bilan → QCM                         → acceptée
 *   · page sans onglets, Bilan → QCM → Bonus (n°301 non appliquée)  → refusée (D3)
 *   · un « 💡 Bonus » en h4 au milieu d'un exercice de séance 1     → pas une clôture
 *     (il a trompé audit_cloture_sequence dans 3e_C1.5)
 *   · un dernier onglet « Hors parcours » : la clôture va dans la dernière SÉANCE → acceptée ;
 *     visible dans l'onglet hors parcours → refusée
 *   · un Bonus en h2 posé à même le panneau (book-train)            → reconnu
 *   · le billet d'entrée caché dans le panneau 2                    → refusé (D4)
 *   · la vraie page 3e_C1.1, corrigée en #418                        → acceptée
 *   · un dossier sans séquence → sortie 2 ; lancé en sous-processus → il parle
 * Usage : node _outils/tests_controle_squelette.mjs   Sortie : 0 si tout passe.
 */
import fs from 'fs';
import os from 'os';
import path from 'path';
import { spawnSync } from 'child_process';
import { fileURLToPath } from 'url';
import { main } from './controle_squelette.mjs';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const OUV = `<section class="rappel-spiralaire"><h2>🔄 Avant de commencer : ce que je vérifie</h2></section>
<section class="card"><h2>La situation</h2><p>…</p></section><section class="card"><h2>❓ Problématique</h2><p>…</p></section>
<section class="card"><h2>💭 Ton hypothèse de départ</h2><textarea id="hyp"></textarea></section>
<section class="card"><h2>📚 Le référentiel — je serai capable de…</h2></section>`;
const BILLET = '<section class="card"><h2>🎫 Billet d\'entrée</h2><p>…</p></section>';
const BONUS = '<section class="card"><h2>🎁 Bonus</h2><textarea id="b1"></textarea><details class="correction"><summary>Corrigé du Bonus</summary><p>…</p></details></section>';
const POS = '<fieldset class="qcm-groupe" id="pos1"><legend>3e_C1.1 — repérer une rupture :</legend>'
  + ['🔴 Maîtrise insuffisante', '🟠 Maîtrise fragile', '🟢 Maîtrise satisfaisante', '⭐ Très bonne maîtrise'].map((v, i) => `<label><input type="radio" name="pos1" id="p${i}" value="${v}">${v}</label>`).join('') + '</fieldset>';
const BILAN = `<section class="card"><h2>🏁 Bilan</h2><p>Relis ton hypothèse de départ.</p><h3>🧠 Comment j'ai travaillé</h3><textarea id="m1"></textarea><h3>📍 Je me positionne</h3>${POS}</section>`;
const QCM = '<section class="card"><h2>🧠 Prêt·e à t\'entraîner ?</h2><a class="btn" href="qcm_banc.html">Lancer le QCM</a></section>';
const CLOT = BONUS + BILAN + QCM;
const ACT = (n, x = '') => `<section class="card"><h2>Activité ${n}</h2><p>…</p>${x}</section>`;
const page = (corps, avecOnglets = true, hors = false) => `<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>banc</title>
<style>.seance-panel{display:none}.seance-panel.active{display:block}</style></head><body>${corps}
${avecOnglets ? `<script>document.querySelectorAll('.seance-tab').forEach(b=>b.addEventListener('click',()=>{
document.querySelectorAll('.seance-panel').forEach(p=>p.classList.toggle('active',p.id===b.dataset.panel));}));</script>` : ''}</body></html>`;
const onglets = (n, hors = false) => '<nav>' + Array.from({ length: n }, (_, i) => `<button class="seance-tab" data-panel="s${i + 1}">Séance ${i + 1}</button>`).join('')
  + (hors ? '<button class="seance-tab hors" data-panel="shors">Hors parcours</button>' : '') + '</nav>';
const panneau = (i, x, actif = false) => `<section class="seance-panel${actif ? ' active' : ''}" id="s${i}">${x}</section>`;

const CAS = [
  ['clôture HORS des panneaux (3e_C1.1 avant #418)', 1,
    page(OUV + BILLET + onglets(3) + '<div>' + panneau(1, ACT(1), true) + panneau(2, ACT(2)) + panneau(3, ACT(3)) + '</div>' + CLOT)],
  ['clôture DANS le dernier panneau', 0,
    page(OUV + BILLET + onglets(3) + '<div>' + panneau(1, ACT(1), true) + panneau(2, ACT(2)) + panneau(3, ACT(3) + CLOT) + '</div>')],
  ['« Je me positionne » visible à la séance 1', 1,
    page(OUV + BILLET + onglets(3) + '<div>' + panneau(1, ACT(1, '<h3>📍 Je me positionne</h3>' + POS), true) + panneau(2, ACT(2)) + panneau(3, ACT(3) + BONUS + QCM) + '</div>')],
  ['sans onglets, Bonus → Bilan → QCM', 0, page(OUV + BILLET + ACT(1) + ACT(2) + CLOT, false)],
  ['sans onglets, Bilan → QCM → Bonus', 1, page(OUV + BILLET + ACT(1) + ACT(2) + BILAN + QCM + BONUS, false)],
  ['« 💡 Bonus » en h4 dans un exercice de séance 1', 0,
    page(OUV + BILLET + onglets(2) + '<div>' + panneau(1, ACT(1, '<h4>💡 Bonus — validation tous cas</h4><p>…</p>'), true) + panneau(2, ACT(2) + CLOT) + '</div>')],
  ['dernier onglet « Hors parcours », clôture dans la dernière séance', 0,
    page(OUV + BILLET + onglets(2, true) + '<div>' + panneau(1, ACT(1), true) + panneau(2, ACT(2) + CLOT) + '<section class="seance-panel" id="shors"><h2>Python</h2></section></div>')],
  ['clôture dans l\'onglet « Hors parcours »', 1,
    page(OUV + BILLET + onglets(2, true) + '<div>' + panneau(1, ACT(1), true) + panneau(2, ACT(2)) + '<section class="seance-panel" id="shors"><h2>Python</h2>' + CLOT + '</section></div>')],
  ['Bonus en h2 à même le panneau, après le QCM (book-train)', 1,
    page(OUV + BILLET + onglets(2) + '<div>' + panneau(1, ACT(1), true) + panneau(2, ACT(2) + BILAN + QCM + '<h2>🎁 Bonus</h2><textarea></textarea>') + '</div>')],
  ['billet d\'entrée caché dans le panneau 2', 1,
    page(OUV + onglets(2) + '<div>' + panneau(1, ACT(1), true) + panneau(2, BILLET + ACT(2) + CLOT) + '</div>')],
];

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'squelette-'));
let ok = 0, ko = 0;
const dire = (c, m) => { console.log((c ? '✅ ' : '❌ ') + m); c ? ok++ : ko++; };
const silence = async (f) => { const l = console.log, e = console.error; console.log = console.error = () => {}; try { return await f(); } finally { console.log = l; console.error = e; } };
for (const [nom, attendu, html] of CAS) {
  const d = fs.mkdtempSync(path.join(tmp, 'cas-'));
  fs.writeFileSync(path.join(d, 'sequence_banc.html'), html);
  const rc = await silence(() => main([d]));
  dire(rc === attendu, `${nom} → ${attendu ? 'refusée' : 'acceptée'} (sortie ${rc})`);
}
{
  const vraie = path.join(ICI, '..', 'theme-1-objets-systemes-usages-interactions', 'C1-decrire-les-liens-entre-usages-et-evolutions',
    '3e', '3e_C1.1', 'sequence_3e_C1.1-C1.4_tsinghua_feux.html');
  dire(await silence(() => main([vraie])) === 0, '3e_C1.1, la vraie page corrigée en #418 → acceptée');
}
{
  const vide = fs.mkdtempSync(path.join(tmp, 'vide-'));
  dire(await silence(() => main([vide])) === 2, 'dossier sans séquence → sortie 2 (en panne), jamais 0');
}
{
  const d = fs.mkdtempSync(path.join(tmp, 'cas-'));
  fs.writeFileSync(path.join(d, 'sequence_banc.html'), CAS[1][2]);
  const r = spawnSync(process.execPath, [path.join(ICI, 'controle_squelette.mjs'), d], { encoding: 'utf8', env: process.env });
  dire(r.status === 0 && /séquence\(s\) ouvertes/.test(r.stdout), `lancé en sous-processus : sortie ${r.status}, ${r.stdout.length} caractères écrits`);
}
fs.rmSync(tmp, { recursive: true, force: true });
console.log(`\n${ok} / ${ok + ko}`);
process.exit(ko ? 1 : 0);
