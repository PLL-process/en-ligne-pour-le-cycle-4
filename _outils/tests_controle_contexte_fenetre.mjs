#!/usr/bin/env node
/**
 * Banc de `controle_contexte_fenetre.mjs` (règle d'or n°375, 28/11/2026). Des pages fabriquées, une par cas :
 *   pres       une question juste sous son rappel du cas → rien à signaler ;
 *   loin       le cas en haut, 1 200 px de texte, puis la question → signalée, au téléphone et au portable zoomé ;
 *   rappel     la même page, avec un `.rappel-cas` juste au-dessus de la question → plus rien ;
 *   seule      la même que « loin », mais la question porte `data-cas="dans-la-question"` → sautée ;
 *   bandeau    un bandeau collant de 300 px : le cas à 300 px de la question sort de la fenêtre du portable zoomé
 *              (576 − 300 = 276 px), pas celle d'une page sans bandeau ;
 *   ident      « Nom », « Classe » : des identifiants, jamais mesurés ;
 *   replie     une question dans un `<details>` fermé : pas mesurée.
 * Et la panne : une page qui n'existe pas fait sortir à 2 (n°299).
 *   node _outils/tests_controle_contexte_fenetre.mjs     # 0 tout passe · 1 un contrôle échoue · 2 en panne
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const OUTIL = path.join(ICI, 'controle_contexte_fenetre.mjs');
try { await import('playwright'); } catch { console.log('⛔ EN PANNE : Playwright introuvable (n°299)'); process.exit(2); }

const page = (corps, tete = '') => `<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>t</title><style>body{font:16px sans-serif;margin:0 16px}${tete}</style></head><body><main><h1>Essai</h1>${corps}</main></body></html>`;
const remplissage = (px) => `<div style="height:${px}px">texte du cas qui continue…</div>`;
const Q = '<label>Que fait le store ?<select><option>—</option><option>Il descend</option></select></label>';
const D = fs.mkdtempSync(path.join(os.tmpdir(), 'contexte-'));
const PAGES = {
  pres: page(`<h2>Le cas</h2><p class="rappel-cas">Le store descend au-dessus de 800 lux.</p>${Q}`),
  loin: page(`<h2>Le cas</h2><p>Le store descend au-dessus de 800 lux.</p>${remplissage(1200)}${Q}`),
  rappel: page(`<h2>Le cas</h2><p>Le store descend au-dessus de 800 lux.</p>${remplissage(1200)}<p class="rappel-cas">📌 Le cas : 800 lux.</p>${Q}`),
  seule: page(`<h2>Le cas</h2><p>Le store descend au-dessus de 800 lux.</p>${remplissage(1200)}<label data-cas="dans-la-question">Que fait le store au-dessus de 800 lux ?<select><option>—</option></select></label>`),
  bandeau: page(`<header style="position:sticky;top:0;height:300px;background:#fff">Bandeau</header><h2>Le cas</h2>${remplissage(250)}${Q}${remplissage(1500)}`),
  sansbandeau: page(`<h2>Le cas</h2>${remplissage(250)}${Q}${remplissage(1500)}`),
  ident: page(`<h2>Identification</h2>${remplissage(1200)}<label>Nom<input type="text"></label><label>Classe<input type="text"></label>`),
  replie: page(`<h2>Le cas</h2>${remplissage(1200)}<details><summary>Aide</summary>${Q}</details>`),
};
for (const [k, v] of Object.entries(PAGES)) fs.writeFileSync(path.join(D, `${k}.html`), v);

function jouer(fichiers) {
  const json = path.join(D, `r${Math.random().toString(36).slice(2)}.json`);
  const r = spawnSync(process.execPath, [OUTIL, ...fichiers, '--json', json], { encoding: 'utf8' });
  const res = fs.existsSync(json) ? JSON.parse(fs.readFileSync(json, 'utf8')) : [];
  return { code: r.status, res, sortie: r.stdout + r.stderr };
}
const hors = (r, fenetre) => { const f = (r.fenetres || []).find((x) => x.nom === fenetre); return f ? f.hors.length : -1; };
const mesurees = (r) => Math.max(0, ...(r.fenetres || []).map((f) => f.questions.length));

let ok = 0, ko = 0;
const verifier = (nom, cond, detail = '') => { if (cond) { ok++; console.log(`✅ ${nom}`); } else { ko++; console.log(`❌ ${nom}${detail ? ' — ' + detail.slice(0, 300) : ''}`); } };

const t = jouer(Object.keys(PAGES).map((k) => path.join(D, `${k}.html`)));
const de = (k) => t.res.find((r) => r.rel.endsWith(`${k}.html`)) || {};
verifier('la mesure sort à 0 (elle ne refuse rien : n°375 en essai)', t.code === 0, t.sortie);
verifier('pres : une question juste sous son rappel n\'est pas signalée', hors(de('pres'), 'téléphone') === 0 && hors(de('pres'), 'portable zoomé') === 0);
verifier('loin : le cas 1 200 px plus haut est signalé, au téléphone et au portable zoomé', hors(de('loin'), 'téléphone') === 1 && hors(de('loin'), 'portable zoomé') === 1, JSON.stringify(de('loin')));
verifier('rappel : un .rappel-cas juste au-dessus suffit', hors(de('rappel'), 'téléphone') === 0 && hors(de('rappel'), 'portable zoomé') === 0, JSON.stringify(de('rappel')));
verifier('seule : data-cas="dans-la-question" saute la question', mesurees(de('seule')) === 0, JSON.stringify(de('seule')));
const fb = (de('bandeau').fenetres || []).find((f) => f.nom === 'portable zoomé') || {};
verifier('bandeau : le bandeau collant est déduit (300 px mesurés)', fb.bandeau >= 290 && fb.bandeau <= 310, JSON.stringify(fb.bandeau));
verifier('bandeau : à 250 px de son cas, la question sort d\'une fenêtre de 276 px', hors(de('bandeau'), 'portable zoomé') === 1, JSON.stringify(fb));
verifier('sans bandeau : la même distance tient dans la fenêtre', hors(de('sansbandeau'), 'portable zoomé') === 0);
verifier('ident : « Nom », « Classe » ne sont pas des questions', mesurees(de('ident')) === 0, JSON.stringify(de('ident')));
verifier('replie : une question dans un <details> fermé n\'est pas mesurée', mesurees(de('replie')) === 0);
const p = jouer([path.join(D, 'nexiste-pas.html')]);
verifier('une page absente : EN PANNE, sortie 2 (n°299)', p.code === 2, p.sortie);

fs.rmSync(D, { recursive: true, force: true });
console.log(ko ? `\n${ok} / ${ok + ko}` : `\n✅ ${ok} / ${ok + ko} — la mesure voit le cas loin de sa question, déduit le bandeau, et respecte rappels et questions qui se suffisent`);
process.exit(ko ? 1 : 0);
