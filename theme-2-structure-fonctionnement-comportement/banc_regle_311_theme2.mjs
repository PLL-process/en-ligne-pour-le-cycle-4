/* banc_regle_311_theme2.mjs — le relais du thème 2 vers le banc commun de la règle d'or n°311
   (theme-1-…/banc_regle_311.mjs, modèle : le pilote 5e_C3.1).
   Le banc commun lit la mission dans `p.sous` ; le gabarit du thème 2 la porte dans `.subtitle` (p ou div).
   Ce relais vérifie donc d'abord la mission — visible à la séance 1 et à la séance 2, à 1280 et 390 px —, puis passe la main au banc commun.
   À 390 px, il vérifie aussi que la barre d'outils reste compacte à la séance 2 : deux lignes au plus, aucun libellé coupé.
   Page sans hypothèse (4e_C6.2) : l'ouverture n'a aucun champ. Avec `choix: true`, `champ` désigne une liste déroulante
   de la séance 1 ; le banc commun la remplit par selectOption au lieu de fill, et suit sa sauvegarde comme celle d'un champ.

   Usage d'une page : node tests_regle_311_<code>.mjs [--captures <dossier>] */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';
import { lancerBanc311 } from '../theme-1-objets-systemes-usages-interactions/banc_regle_311.mjs';

export async function lancerBanc311Theme2(o) {
  const URL0 = pathToFileURL(path.join(o.dossier, o.page)).href;
  let ko = 0;
  const b = await chromium.launch();
  for (const [nom, w, h] of [['1280', 1280, 900], ['390', 390, 844]]) {
    const p = await (await b.newContext({ viewport: { width: w, height: h } })).newPage();
    await p.goto(URL0);
    const vis = () => p.evaluate(() => { const m = document.querySelector('.subtitle');
      return !!m && m.checkVisibility({ contentVisibilityAuto: true, checkVisibilityCSS: true }) && !m.closest('#ouverture'); });
    const s1 = await vis();
    await p.locator('button.seance-tab').nth(1).click(); await p.waitForTimeout(150);
    const s2 = await vis();
    const c = s1 && s2;
    if (!c) ko++;
    console.log(`${c ? '✅' : '❌'} ${nom} px : mission (.subtitle) visible hors du volet, à la séance 1 et à la séance 2`);
    if (nom === '390') {
      const tb = await p.evaluate(() => { const bs = [...document.querySelector('.toolbar').querySelectorAll('.btn')];
        return { lignes: new Set(bs.map(x => Math.round(x.getBoundingClientRect().top))).size, coupe: bs.some(x => x.scrollWidth > x.clientWidth + 1) }; });
      const ct = tb.lignes <= 2 && !tb.coupe;
      if (!ct) ko++;
      console.log(`${ct ? '✅' : '❌'} 390 px : séance 2, barre d'outils compacte (${tb.lignes} ligne(s)${tb.coupe ? ', libellé coupé' : ''})`);
    }
  }
  await b.close();
  if (ko) { console.log(`\n══ ${o.code} : mission absente ou barre d'outils trop haute — banc commun non lancé ══`); process.exit(1); }
  if (o.choix) {
    console.log(`ℹ ${o.code} : pas de champ dans l'ouverture (pas d'hypothèse) — le banc suit la réponse ${o.champ} de la séance 1.`);
    const b2 = await chromium.launch(); const P = Object.getPrototypeOf(await b2.newPage());
    const fill = P.fill;
    P.fill = function (sel, v, opts) { return sel === o.champ ? this.selectOption(sel, v, opts) : fill.call(this, sel, v, opts); };
    await b2.close();
  }
  await lancerBanc311(o);
}
