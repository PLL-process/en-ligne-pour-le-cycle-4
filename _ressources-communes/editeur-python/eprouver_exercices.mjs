/* eprouver_exercices.mjs — un test par exercice outillé de l'éditeur Python, pour les bancs des séquences.
 *
 * Pour chaque exercice : son code de départ s'exécute (par le bouton ▶ de la page, comme un élève) et donne la
 * sortie attendue — ou l'erreur attendue, expliquée, à la bonne ligne ; puis, s'il est donné, un programme
 * corrigé donne la sortie de la correction. Le bloc est remis à son code de départ ensuite.
 *
 *   import { eprouverEditeurs } from "…/_ressources-communes/editeur-python/eprouver_exercices.mjs";
 *   await eprouverEditeurs(page, [
 *     { bloc: "vs1", onglet: "#tab-s2", depart: { sortie: "7\n34\n" } },
 *     { bloc: "vs2", depart: { erreur: "TypeError", ligne: 7 }, corrige: { code: "…", sortie: /Q - 96 St 2 min/ } },
 *   ], ok);
 *   (ok(nom, condition, détail) est la fonction de résultat du banc appelant.)
 */
export async function executerBloc(page, bloc, code, attendre = 20000, arreterApres = 0) {
  const sel = "#" + bloc;
  await page.waitForSelector(sel + ".editeur-py--actif", { timeout: 5000 });
  if (code !== undefined) {
    await page.evaluate(([s, c]) => { const t = document.querySelector(s + " textarea.editeur-py-code"); t.value = c; t.dispatchEvent(new Event("input", { bubbles: true })); }, [sel, code]);
  }
  const n = await page.evaluate(() => {
    if (!window.__finsBanc) { window.__finsBanc = []; document.addEventListener("editeur-py:fin", (e) => window.__finsBanc.push(e.detail)); }
    return window.__finsBanc.length;
  });
  await page.locator(sel).scrollIntoViewIfNeeded();
  await page.click(sel + " .editeur-py-executer");
  if (arreterApres) { await page.waitForTimeout(arreterApres); await page.click(sel + " .editeur-py-arreter").catch(() => {}); }
  await page.waitForFunction((k) => window.__finsBanc.length > k, n, { timeout: attendre });
  return page.evaluate(() => window.__finsBanc[window.__finsBanc.length - 1]);
}

function conforme(r, att) {
  if (!r) return false;
  if (att.erreur) return !!r.erreur && r.erreur.type === att.erreur && (att.ligne === undefined || r.erreur.ligne === att.ligne)
    && (!att.explication || att.explication.test(r.erreur.explication));
  if (r.erreur) return false;
  if (att.arret && r.arret !== att.arret) return false;
  if (!att.arret && r.arret) return false;
  return att.sortie instanceof RegExp ? att.sortie.test(r.sortie) : r.sortie === att.sortie;
}
const dit = (r) => !r ? "rien" : r.erreur ? r.erreur.type + " ligne " + r.erreur.ligne + " · " + r.erreur.explication.slice(0, 70)
  : (r.arret ? "[arrêt " + r.arret + "] " : "") + JSON.stringify(r.sortie).slice(0, 110);

export async function eprouverEditeurs(page, cas, ok) {
  for (const c of cas) {
    if (c.onglet) { await page.click(c.onglet); await page.waitForTimeout(250); }
    const depart = await page.evaluate((s) => { const t = document.querySelector(s + " textarea.editeur-py-code"); return t ? t.defaultValue : null; }, "#" + c.bloc);
    let r = await executerBloc(page, c.bloc, depart, c.attendre, c.arreterApres);
    ok("éditeur Python · " + c.bloc + (c.nom ? " (" + c.nom + ")" : "") + " : le code de départ s'exécute et donne "
       + (c.depart.erreur ? "l'erreur attendue, expliquée (" + c.depart.erreur + (c.depart.ligne ? ", ligne " + c.depart.ligne : "") + ")" : "la sortie attendue"),
       conforme(r, c.depart), dit(r));
    if (c.corrige) {
      r = await executerBloc(page, c.bloc, c.corrige.code, c.attendre, c.corrige.arreterApres || 0);
      ok("éditeur Python · " + c.bloc + " : le programme de la correction donne " + (c.corrige.quoi || "la sortie attendue"), conforme(r, c.corrige), dit(r));
      await page.evaluate(([s, c0]) => { const t = document.querySelector(s + " textarea.editeur-py-code"); t.value = c0; t.dispatchEvent(new Event("input", { bubbles: true })); }, ["#" + c.bloc, depart]);
    }
  }
}

/* Ce que toute page outillée doit tenir : Skulpt absent à l'ouverture, un bloc par exercice, chacun avec son
   champ étiqueté, son lien Vittascience facultatif et sa zone sans JavaScript. */
export async function eprouverPose(page, blocs, ok) {
  const etat = await page.evaluate((B) => ({
    skulpt: !!window.Sk || !!document.querySelector('script[src*="skulpt"]'),
    blocs: B.map((b) => {
      const e = document.getElementById(b);
      if (!e) return { b, ok: false, pourquoi: "absent" };
      const t = e.querySelector("textarea.editeur-py-code"), a = e.querySelector("a.vs-lien"), l = t && document.querySelector('label[for="' + t.id + '"]');
      const pourquoi = !t ? "pas de zone" : !l ? "zone sans étiquette" : !a ? "pas de lien Vittascience" : !/fr\.vittascience\.com\/python\//.test(a.href) ? "lien faux"
        : !e.classList.contains("editeur-py--actif") ? "non monté" : !e.querySelector(".editeur-py-console[aria-live]") ? "console sans aria-live" : "";
      return { b, ok: !pourquoi, pourquoi };
    }),
  }), blocs);
  ok("éditeur Python · Skulpt n'est pas chargé à l'ouverture de la page", !etat.skulpt);
  ok("éditeur Python · " + blocs.length + " éditeur(s) posé(s), chacun étiqueté, avec sa console aria-live et son lien Vittascience facultatif",
     etat.blocs.every((x) => x.ok), etat.blocs.filter((x) => !x.ok).map((x) => x.b + " : " + x.pourquoi).join(" · "));
}
