/* banc_regle_311_theme2.mjs — le relais du thème 2 vers le banc commun de la règle d'or n°311
   (theme-1-…/banc_regle_311.mjs, modèle : le pilote 5e_C3.1).
   Le banc commun lit la mission dans `p.sous` ; le gabarit du thème 2 la porte dans `.subtitle` (p ou div).
   Ce relais vérifie donc d'abord la mission — visible à la séance 1 et à la séance 2, à 1280 et 390 px —, puis passe la main au banc commun.

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
  }
  await b.close();
  if (ko) { console.log(`\n══ ${o.code} : mission absente — banc commun non lancé ══`); process.exit(1); }
  await lancerBanc311(o);
}
