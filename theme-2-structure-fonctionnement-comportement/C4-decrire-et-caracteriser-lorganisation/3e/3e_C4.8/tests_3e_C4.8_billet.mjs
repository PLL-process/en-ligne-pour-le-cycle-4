/* Banc du billet de sortie de 3e_C4.8 (règle d'or n°330, 28/11/2026).
 * node tests_3e_C4.8_billet.mjs — sortie 0 si tout passe, 1 sinon. */
import { chromium } from 'playwright';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
const ICI = path.dirname(new URL(import.meta.url).pathname);
const URL0 = pathToFileURL(path.join(ICI, 'sequence_3e_C4.7-C4.8_pont_numerique_packet_tracer.html')).href;
const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 390, height: 900 } });
const err = []; p.on('pageerror', (e) => err.push(e.message)); p.on('dialog', (d) => d.dismiss().catch(() => {}));
await p.goto(URL0, { waitUntil: 'load' }); await p.evaluate(() => localStorage.clear()); await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(300);
await p.click('.seance-tab[data-panel="seance3"]'); await p.waitForTimeout(120);
const bs = await p.evaluate(() => {
  const s = document.getElementById('billetSortie'); if (!s) return null;
  const corr = s.querySelector('details.correction');
  const bonus = [...document.querySelectorAll('section.card h2')].find(h => /🎁 Bonus/.test(h.textContent));
  return { visible: s.checkVisibility(), zones: s.querySelectorAll('textarea[data-save]').length,
    etayages: s.querySelectorAll('details.etayage').length, boutons: s.querySelectorAll('button').length,
    criteres: (corr.textContent.match(/Critère/g) || []).length, contre: (corr.textContent.match(/✘/g) || []).length,
    avantBonus: !!bonus && s.nextElementSibling === bonus.closest('section'),
    panneau: (s.closest('.seance-panel') || {}).id, large: s.scrollWidth <= 390 };
});
ok('billet de sortie · il existe, visible à la séance 3, juste avant le Bonus', !!bs && bs.visible && bs.panneau === 'seance3' && bs.avantBonus, JSON.stringify(bs));
ok('billet de sortie · deux zones gardées, deux versions étayées, deux critères, des contre-exemples, aucun bouton',
   !!bs && bs.zones === 2 && bs.etayages === 2 && bs.criteres === 2 && bs.contre >= 2 && bs.boutons === 0, JSON.stringify(bs));
ok('billet de sortie · tient dans l\'écran du téléphone (390 px)', !!bs && bs.large);
await p.fill('#bs_3e_C4_8_1', 'ma réponse au billet'); await p.waitForTimeout(800);
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
ok('billet de sortie · la réponse écrite survit au rechargement', (await p.inputValue('#bs_3e_C4_8_1')) === 'ma réponse au billet');
ok('aucune erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
await b.close();
console.log(T.map((x) => `${x.ok ? '✅' : '❌'} ${x.n}${x.d ? ' — ' + x.d : ''}`).join('\n'));
const n0 = T.filter((x) => x.ok).length;
console.log(`${n0} / ${T.length}`);
process.exit(n0 === T.length ? 0 : 1);
