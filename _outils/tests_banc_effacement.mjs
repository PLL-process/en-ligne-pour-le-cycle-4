/* tests_banc_effacement.mjs — le banc de `banc_effacement.mjs`.
 *
 * Sur des pages jetables, il rejoue ce que le banc doit refuser et ce qu'il doit accepter. Les cas refusés sont ceux
 * du 20/11/2026, réduits à l'os :
 *
 *   · une page qui efface sa clé et pas celle d'un exercice voisin (le cahier des charges incrusté du jardin de 4e) ;
 *   · une page dont un menu reste changé après l'effacement, sans qu'aucun texte ne le trahisse (les piqûres de
 *     rappel : un choix dans un menu ne contient pas le témoin) ;
 *   · une page qui efface ses réponses et garde les étoiles du mode mission (près d'une séquence sur deux).
 *
 * Usage : node _outils/tests_banc_effacement.mjs
 * Sortie : 0 si tout passe, 1 sinon, 2 si Playwright manque (le banc ne peut alors rien dire : règle d'or n°299).
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const SCRIPT = path.join(ICI, 'banc_effacement.mjs');
try { await import('playwright'); } catch (e) {
  console.error('❌ EN PANNE : Playwright introuvable, le banc ne peut rien vérifier (règle d\'or n°299).'); process.exit(2);
}

const echecs = []; let controles = 0;
function verifier(titre, condition, detail = '') {
  controles++;
  if (!condition) echecs.push(`${titre}${detail ? `\n     ${String(detail).trim().replace(/\n/g, '\n     ')}` : ''}`);
}

/* Une page d'essai : deux champs et un menu, chacun gardé sous sa clé ; un bouton armé en deux clics, comme sur le
   site, qui retire les clés de `efface` puis recharge. */
const page = ({ efface, mission = false, bouton = true }) => `<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>Essai</title></head><body>
<main><h1>Essai</h1>
<p><label for="a">Ta réponse</label> <input type="text" id="a"></p>
<p><label for="b">L'exercice voisin</label> <textarea id="b"></textarea></p>
<p><label for="m">Ton choix</label> <select id="m"><option value="">—</option><option value="fp">FP</option><option value="fc">FC</option></select></p>
${mission ? '<button type="button" id="btnMission">🎮 Mode mission</button>' : ''}
${bouton ? '<button type="button" id="btnReset">🗑 Effacer ma sauvegarde</button>' : ''}
</main>
<script>
(function(){
  var CLES = { a: "seq_essai", b: "rep_voisin", m: "rep_menu" }, EFFACE = ${JSON.stringify(efface)};
  Object.keys(CLES).forEach(function(id){
    var e = document.getElementById(id), v = null; try { v = localStorage.getItem(CLES[id]); } catch (x) {}
    if (v !== null) e.value = v;
    e.addEventListener("input", function(){ try { localStorage.setItem(CLES[id], e.value); } catch (x) {} });
    e.addEventListener("change", function(){ try { localStorage.setItem(CLES[id], e.value); } catch (x) {} });
  });
  var b = document.getElementById("btnReset"), arme = 0; if (!b) return;
  b.addEventListener("click", function(){
    if (arme && Date.now() - arme < 6000){ EFFACE.forEach(function(k){ try { localStorage.removeItem(k === "MISSION" ? "mission:" + location.pathname.split("/").pop() : k); } catch (x) {} }); location.reload(); return; }
    arme = Date.now(); b.textContent = "Clique encore pour effacer";
  });
})();
</script></body></html>`;

const dossier = fs.mkdtempSync(path.join(os.tmpdir(), 'banc-effacement-'));
const ecrire = (nom, html) => { const d = path.join(dossier, nom); fs.mkdirSync(d); const f = path.join(d, 'page.html'); fs.writeFileSync(f, html); return d; };
const jouer = (...args) => { const r = spawnSync(process.execPath, [SCRIPT, ...args], { encoding: 'utf8' }); return { code: r.status, sortie: (r.stdout || '') + (r.stderr || '') }; };

let r = jouer(ecrire('tout', page({ efface: ['seq_essai', 'rep_voisin', 'rep_menu'] })));
verifier('une page qui efface ses trois clés est acceptée (sortie 0)', r.code === 0, r.sortie);
verifier('… et le banc dit ce qu\'il a posé', /3 réponse\(s\) posée\(s\)/.test(r.sortie) && /1 page\(s\) jouée\(s\)/.test(r.sortie), r.sortie);

r = jouer(ecrire('voisin', page({ efface: ['seq_essai', 'rep_menu'] })));
verifier('une page qui garde la clé de l\'exercice voisin est refusée (sortie 1)', r.code === 1, r.sortie);
verifier('… en nommant la clé gardée et le champ', /rep_voisin/.test(r.sortie) && /le témoin dans le champ #b/.test(r.sortie), r.sortie);

r = jouer(ecrire('menu', page({ efface: ['seq_essai', 'rep_voisin'] })));
verifier('une page dont un menu reste changé est refusée, sans témoin dans le texte (sortie 1)', r.code === 1, r.sortie);
verifier('… en nommant le menu', /menu encore changé : #m/.test(r.sortie) && !/le témoin reste/.test(r.sortie), r.sortie);

r = jouer(ecrire('mission-gardee', page({ efface: ['seq_essai', 'rep_voisin', 'rep_menu'], mission: true })));
verifier('une page qui efface ses réponses et garde les étoiles du mode mission est refusée (sortie 1)', r.code === 1, r.sortie);
verifier('… en nommant la mémoire du mode mission', /le témoin reste dans localStorage « mission:page\.html »/.test(r.sortie), r.sortie);

r = jouer(ecrire('mission-effacee', page({ efface: ['seq_essai', 'rep_voisin', 'rep_menu', 'MISSION'], mission: true })));
verifier('une page qui efface aussi le mode mission est acceptée (sortie 0)', r.code === 0, r.sortie);
verifier('… et le banc dit que la mission a été éprouvée', /mode mission éprouvé sur 1 page/.test(r.sortie), r.sortie);

r = jouer(ecrire('sans-bouton', page({ efface: [], bouton: false })));
verifier('sans bouton d\'effacement, rien n\'est joué : sortie 2, pas 0 (règle d\'or n°299)', r.code === 2, r.sortie);

r = jouer(path.join(dossier, 'nulle-part'));
verifier('un chemin qui n\'existe pas : sortie 2', r.code === 2, r.sortie);

fs.rmSync(dossier, { recursive: true, force: true });
if (echecs.length) { echecs.forEach(e => console.log('❌ ' + e)); console.log(`${controles - echecs.length} / ${controles}`); process.exit(1); }
console.log(`✅ banc_effacement : ${controles} / ${controles} — refuse une clé gardée, un menu resté changé, des étoiles gardées ; accepte une page qui efface tout ; sort à 2 quand il n'a rien joué`);
