/* banc_regle_311_theme3.mjs — le relais du thème 3 vers le banc commun de la règle d'or n°311
   (theme-1-…/banc_regle_311.mjs, modèle : le pilote 5e_C3.1 ; relais jumeau : theme-2-…/banc_regle_311_theme2.mjs).
   Le gabarit des séquences à onglets du thème 3 est celui du thème 2 : la mission est dans `.subtitle`, que le banc commun
   ne lit pas (il la cherche dans `p.sous`). Ce relais vérifie donc d'abord, dans un navigateur à lui :
     · la mission (`.subtitle`) : visible hors du volet à la séance 1 et à la séance 2, à 1280 et 390 px ;
     · « un outil n'est pas du décor » : chaque outil nommé par la page (`outils` : sélecteur de parcours, zones role=status,
       progression, « Où en suis-je ? », banc d'essai…) existe, reste HORS du volet et se voit à la séance 1 comme à la
       séance 2, à 1280 et 390 px ;
     · le sélecteur de parcours et le volet cohabitent : depuis la séance 2, choisir 🅲 range les blocs des autres voies, le
       volet reste replié ; « Tout afficher » remet tout ;
     · à 390 px, la barre d'outils reste compacte à la séance 2 : deux lignes au plus, aucun libellé coupé (et, pour le
       sélecteur de parcours, ses boutons sur deux lignes au plus, sous son intitulé) ;
     · le lien direct vers une ancre d'une séance ≥ 2 : la page finit de se charger, le volet est replié, la cible est à
       l'écran (un dessin <object> de l'ouverture ne se charge pas dans un volet fermé : fermé trop tôt, le volet suspendait
       le « load » de 3e_C9.1 ; il se replie donc au « load ») ;
   puis il passe la main au banc commun du thème 1, sans le modifier.

   Usage d'une page : node tests_regle_311_<code>.mjs [--captures <dossier>] */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';
import { lancerBanc311 } from '../theme-1-objets-systemes-usages-interactions/banc_regle_311.mjs';

/**
 * @param {object} o  les options du banc commun (dossier, page, code, champ, texte, ancreS1, ancreSN, panneauSN…), plus :
 * @param {string[]} o.outils  sélecteurs des outils des séances, qui doivent rester hors du volet « Rappel »
 */
export async function lancerBanc311Theme3(o) {
  const URL0 = pathToFileURL(path.join(o.dossier, o.page)).href;
  let ko = 0;
  const t = (c, m) => { if (!c) ko++; console.log(`${c ? '✅' : '❌'} ${m}`); };
  const b = await chromium.launch();
  for (const [nom, w, h] of [['1280', 1280, 900], ['390', 390, 844]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: h } });
    const p = await ctx.newPage(); const err = [];
    p.on('pageerror', (e) => err.push(String(e).slice(0, 80)));
    p.on('dialog', (d) => d.dismiss().catch(() => {}));
    await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.waitForTimeout(150);
    const lire = () => p.evaluate((outils) => {
      const vis = (e) => !!e && e.checkVisibility({ contentVisibilityAuto: true, checkVisibilityCSS: true });
      const m = document.querySelector('.subtitle');
      return {
        mission: !!m && vis(m) && !m.closest('#ouverture'),
        outils: outils.map((s) => { const e = document.querySelector(s); return { s, ok: !!e && vis(e) && !e.closest('#ouverture') }; }),
      };
    }, o.outils || []);
    const s1 = await lire();
    await p.locator('button.seance-tab').nth(1).click(); await p.waitForTimeout(150);
    const s2 = await lire();
    t(s1.mission && s2.mission, `${nom} px : mission (.subtitle) visible hors du volet, à la séance 1 et à la séance 2`);
    const manquent = (o.outils || []).filter((s, i) => !s1.outils[i].ok || !s2.outils[i].ok);
    t((o.outils || []).length > 0 && manquent.length === 0,
      `${nom} px : un outil n'est pas du décor — ${(o.outils || []).join(', ')} hors du volet, visibles aux séances 1 et 2${manquent.length ? ' — en défaut : ' + manquent.join(', ') : ''}`);
    if (nom === '1280' && await p.locator('.parcours-btn[data-choix="c"]').count()) {
      await p.click('.parcours-btn[data-choix="c"]'); await p.waitForTimeout(150);
      const c = await p.evaluate(() => ({ classe: document.body.classList.contains('parcours-c'), volet: document.getElementById('ouverture').open,
        range: [...document.querySelectorAll('.seance-panel.active [data-parcours]:not([data-parcours~="c"])')].every((e) => getComputedStyle(e).display === 'none') }));
      await p.click('.parcours-btn[data-choix="tous"]'); await p.waitForTimeout(150);
      const tous = await p.evaluate(() => !/parcours-[abc]/.test(document.body.className));
      t(c.classe && c.range && !c.volet && tous, '1280 px : depuis la séance 2, le sélecteur de parcours marche (🅲 range les autres voies), le volet reste replié ; « Tout afficher » remet tout');
    }
    if (nom === '390') {
      const tb = await p.evaluate(() => {
        const lignes = (bs) => new Set(bs.map((x) => Math.round(x.getBoundingClientRect().top))).size;
        const barres = [...document.querySelectorAll('.toolbar')];
        const outils = barres.find((x) => !x.classList.contains('choix-parcours-boutons'));
        const parcours = barres.find((x) => x.classList.contains('choix-parcours-boutons'));
        const tous = barres.flatMap((x) => [...x.querySelectorAll('.btn')]);
        return { outils: lignes([...outils.querySelectorAll('.btn')]), parcours: parcours ? lignes([...parcours.querySelectorAll('.btn')]) : 0,
          coupe: tous.some((x) => x.scrollWidth > x.clientWidth + 1) };
      });
      t(tb.outils <= 2 && tb.parcours <= 2 && !tb.coupe,
        `390 px : séance 2, barre d'outils compacte (${tb.outils} ligne(s)${tb.parcours ? `, parcours : ${tb.parcours} ligne(s) de boutons` : ''}${tb.coupe ? ', libellé coupé' : ''})`);
    }
    t(err.length === 0, `${nom} px : relais sans erreur JS ${err.join(' | ')}`);
    await ctx.close();
  }
  {
    //: le lien direct amène bien la cible à l'écran, une fois le volet replié (il se replie au « load » de la page)
    const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await ctx.newPage();
    await p.goto(URL0 + '#' + o.ancreSN); await p.waitForTimeout(1300);
    const r = await p.evaluate((id) => { const c = document.getElementById(id).getBoundingClientRect(), v = document.getElementById('ouverture');
      return { ecran: c.top < innerHeight && c.bottom > 0 && c.height > 0, replie: !!v && !v.open, charge: document.readyState }; }, o.ancreSN);
    t(r.ecran && r.replie && r.charge === 'complete', `lien direct #${o.ancreSN} : page chargée, volet replié, la cible à l'écran`);
    await ctx.close();
  }
  await b.close();
  if (ko) { console.log(`\n══ ${o.code} : relais du thème 3 en défaut (${ko}) — banc commun non lancé ══`); process.exit(1); }
  await lancerBanc311(o);
}
