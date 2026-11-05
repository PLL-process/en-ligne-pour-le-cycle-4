# -*- coding: utf-8 -*-
"""Banc de la piqûre de rappel du cahier des charges (donnees_rappel_cdc.py), dans chaque page qui la porte.

    python3 banc_rappels_cdc.py              # tous les rappels
    python3 banc_rappels_cdc.py bac-4e ...   # quelques-uns (identifiants de donnees_rappel_cdc.RAPPELS)

Dans les données : chaque menu a sa bonne réponse parmi ses options, un retour pour chaque option fausse, et la bonne
réponse n'est pas toujours la première. Dans la page (Chromium, Playwright), pour chaque rappel :
  - à 1280 px : la section, son titre, les mots de référence (FP, FC, critère, niveau, flexibilité F0 à F3), le lien
    vers la leçon de 4e (le fichier existe), aucune affirmation « tu as » ; un menu par case à remplir, nommé
    « ligne — colonne » ; « Vérifier » à vide : chaque case dit « ○ sans réponse » ; chaque option fausse, choisie puis
    vérifiée, écrit son propre retour sous sa case ; juste partout : « Tout est juste » ; la correction cite chaque
    attendu et réfute chaque piège ; après rechargement, chaque menu retrouve son choix ; aucun mot coupé, le tableau
    tient dans son cadre ; à l'impression, le menu disparaît, le choix s'imprime en texte, une case vide donne une ligne ;
  - à 390 px : aucun défilement de côté, chaque ligne en carte, chaque case porte le nom de sa colonne, aucun mot coupé.
La page tout-en-un de 3e_C9.2 et sa page 1 engendrée sont lues toutes les deux.

Code de sortie : 0 tout passe · 1 au moins un échec · 2 rien n'a été vérifié.
"""
import html
import json
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import banc_ateliers  # noqa: E402  (JS_MOTS_COUPES)
import build  # noqa: E402
import donnees_rappel_cdc as rc  # noqa: E402
import moteur  # noqa: E402

RESULTATS = []


def t(nom, ok, detail=""):
    RESULTATS.append((nom, bool(ok)))
    print(("✔ " if ok else "✘ ") + nom + ("" if ok else "  — " + str(detail)[:240]))


def pages(r):
    """Les pages (chemin absolu) qui portent ce rappel."""
    if r.get("atelier"):
        at = __import__("donnees_" + {"exigences-sysml": "exigences"}[r["atelier"][0]])
        return [build.page_niveau(at, r["atelier"][1])]
    p = moteur.DEPOT / r["sequence"]
    out = [p]
    if "3e_C9.2" in r["sequence"]:
        out.append(p.parent / "sequence_3e_C9.2-C8.3_station_1_besoin-et-algorithme.html")
    return out


def norm(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).replace(" ", " ").replace(" ", " ").strip().lower()


def donnees(r):
    nom = "rappel %s (données)" % r["id"]
    manque, total, premier, menus = [], 0, 0, 0
    for L in r["lignes"]:
        for j, c in enumerate(L["cases"]):
            if not isinstance(c, dict):
                continue
            opts = rc.MENUS[c["menu"]] if "menu" in c else c["options"]
            vals = [v for v, _ in opts]
            assert c["bonne"] in vals
            menus += 1
            if "options" in c and vals[0] == c["bonne"]:
                premier += 1
            for v in vals:
                if v != c["bonne"]:
                    total += 1
                    if not c.get("retours", {}).get(v):
                        manque.append("%s/%s=%s" % (L["nom"], rc.COLONNES[j], v))
    t(nom + " : un retour écrit pour chaque option fausse de chaque menu (%d / %d)" % (total - len(manque), total),
      total and not manque, manque[:4])
    a_pieges = sum(1 for L in r["lignes"] for c in L["cases"] if isinstance(c, dict) and "options" in c)
    t(nom + " : la bonne réponse n'est pas toujours la première option (%d menus à pièges sur %d l'ont en tête)"
      % (premier, a_pieges), premier < a_pieges)


JS_OUVRIR = """id => { const el = document.getElementById(id); if (!el) return false;
  const pn = el.closest('[role=tabpanel], .seance-panel, .panneau');
  if (pn && !el.offsetParent) {
    const tab = document.querySelector('[role=tab][data-panel="' + pn.id + '"], [aria-controls="' + pn.id + '"], #tab-' + pn.id);
    if (tab) tab.click();
  }
  el.scrollIntoView({block: 'start'}); return !!el.offsetParent; }"""


def ouvrir(b, chemin, sid, largeur, err, media=None):
    ctx = b.new_context(viewport={"width": largeur, "height": 900})
    pg = ctx.new_page()
    pg.on("pageerror", lambda x: err.append(str(x)))
    pg.goto(chemin.as_uri())
    pg.wait_for_timeout(300)
    vu = pg.evaluate(JS_OUVRIR, sid)
    pg.wait_for_timeout(150)
    return ctx, pg, vu


def page(b, r, chemin):
    sid = "incruste-%s-%s" % (rc.COURT, r["id"])
    uid = "%s_%s" % (rc.COURT, r["id"].replace("-", "_"))
    cle = "rep_%s_%s" % (rc.SLUG, r["id"])
    nom = "rappel %s · %s" % (r["id"], chemin.name)
    if not chemin.exists():
        t(nom + " : la page existe", False, chemin)
        return
    err = []
    ctx, pg, vu = ouvrir(b, chemin, sid, 1280, err)
    pg.evaluate("k => { try { localStorage.removeItem(k); } catch(e){} }", cle)
    pg.reload()
    pg.wait_for_timeout(300)
    vu = pg.evaluate(JS_OUVRIR, sid)
    pg.wait_for_timeout(150)
    t(nom + " : la section est dans la page, et s'affiche une fois sa séance ouverte", vu)
    if not vu:
        ctx.close()
        return
    sel = "#%s .tableau-menus" % sid
    txt = pg.inner_text("#" + sid)
    titre = pg.inner_text("#%s-titre" % sid)
    t(nom + " : le titre « 🔁 Piqûre de rappel : le cahier des charges »",
      norm(titre) == norm("🔁 Piqûre de rappel : le cahier des charges"), titre)
    mots = [m for m in ("fonction principale (fp)", "fonction contrainte (fc)", "critère", "niveau", "flexibilité",
                        "f0 impératif", "f1 peu négociable", "f2 négociable", "f3 très négociable") if m not in norm(txt)]
    t(nom + " : les mots de référence du cahier des charges sont écrits, F0 à F3 compris", not mots, mots)
    lien = pg.evaluate("id => { const a = [...document.getElementById(id).querySelectorAll('p.note a')]"
                       ".find(a => a.getAttribute('href').includes('interacteurs-pieuvre')); return a ? a.getAttribute('href') : ''; }", sid)
    cible = (chemin.parent / lien.split("#")[0]).resolve() if lien else None
    t(nom + " : un lien mène à la leçon de 4e (atelier pieuvre, exercice 6), et le fichier existe",
      lien.endswith("#pv_4e_e6") and cible and cible.exists(), lien)
    t(nom + " : aucune affirmation de ce que l'élève a fait (« tu as… », hors « Tu as réussi si… », le critère)",
      not re.search(r"\btu (as|l'as)\b(?! réussi si)|\bt'a appris\b", norm(txt)), re.findall(r".{20}tu as.{20}", norm(txt))[:2])
    d = json.loads(pg.eval_on_selector("#%s script[type='application/json']" % sid, "e => e.textContent"))["exercices"][uid]
    cases = [c for w in d["widgets"] if w["type"] == "tableau" for c in w["cases"]]
    n_sel = pg.locator(sel + " select").count()
    lus = pg.evaluate("s => [...document.querySelectorAll(s + ' select')].map(x => [x.getAttribute('aria-label') || '', x.options[0].value])", sel)
    t(nom + " : un menu par case à remplir (%d), chacun nommé « ligne — colonne », vide au départ" % len(cases),
      n_sel == len(cases) and all(" — " in a and v == "" for a, v in lus), (n_sel, lus[:2]))
    # ── à vide
    pg.click("#%s button.verifier" % uid)
    pg.wait_for_timeout(80)
    vides = pg.evaluate("s => [...document.querySelectorAll(s + ' td.case-menu')].map(td => td.classList.contains('vide') "
                        "&& td.querySelector('.encoche').textContent.includes('sans réponse'))", sel)
    t(nom + " : « Vérifier » à vide : chaque case dit « ○ sans réponse », et le retour demande de reprendre",
      vides and all(vides) and "🔴" in pg.inner_text("#%s .retour" % uid), vides)
    # ── chaque option fausse écrit son propre retour
    essais, rates, total = pg.evaluate("""([s, defs]) => {
        const t = document.querySelector(s), btn = t.closest('[data-exo]').querySelector('button.verifier');
        const sels = [...t.querySelectorAll('select')];
        const faux = sels.map(x => [...x.options].map(o => o.value).filter(v => v && v !== defs[x.name].bonne));
        let n = 0; const rates = [];
        for (let k = 0; k < Math.max(...faux.map(f => f.length)); k++) {
          sels.forEach((x, i) => { x.value = faux[i][Math.min(k, faux[i].length - 1)]; x.dispatchEvent(new Event('change', {bubbles: true})); });
          btn.click();
          sels.forEach((x, i) => { if (k >= faux[i].length) return; n++;
            const td = x.closest('td'), r = td.querySelector('.retour-case');
            if (!td.classList.contains('faux') || !r.classList.contains('visible') || r.textContent !== '✘ ' + (defs[x.name].retours || {})[x.value])
              rates.push(x.name.split('__').pop() + '=' + x.value); });
        }
        return [n, rates, faux.reduce((a, f) => a + f.length, 0)]; }""", [sel, {c["name"]: c for c in cases}])
    t(nom + " : chaque option fausse, choisie puis vérifiée, écrit son propre retour (✘ et pourquoi) sous sa case (%d essais)"
      % essais, essais == total and total > 0 and not rates, rates[:4])
    # ── juste partout
    for c in cases:
        pg.select_option('#%s select[name="%s"]' % (uid, c["name"]), value=c["bonne"])
    pg.click("#%s button.verifier" % uid)
    pg.wait_for_timeout(80)
    justes = pg.evaluate("s => [...document.querySelectorAll(s + ' td.case-menu')].every(td => td.classList.contains('juste') "
                         "&& !td.querySelector('.retour-case.visible'))", sel)
    t(nom + " : juste partout, « Tout est juste » et chaque case marquée ✔",
      justes and "Tout est juste" in pg.inner_text("#%s .retour" % uid))
    # ── la correction : chaque attendu, chaque piège réfuté
    corr = norm(pg.eval_on_selector("#%s details.correction" % uid, "e => e.innerHTML"))
    oublis = []
    for L in r["lignes"]:
        for j, c in enumerate(L["cases"]):
            if not isinstance(c, dict) or "options" not in c:
                continue
            for v, lib in c["options"]:
                if norm(lib) not in corr:
                    oublis.append("%s : %s" % ("attendu" if v == c["bonne"] else "piège", lib))
                elif v != c["bonne"] and norm(c["retours"][v]).rstrip(".") not in corr:
                    oublis.append("réfutation : " + lib)
        if rc.NOM_FLEX[L["flex"]].lower() not in corr:
            oublis.append("flexibilité " + L["flex"])
    t(nom + " : la correction cite chaque attendu, puis réfute chaque piège avec son retour", not oublis, oublis[:3])
    # ── sauvegarde
    pg.reload()
    try:
        pg.wait_for_function("([n, v]) => { const x = document.getElementsByName(n)[0]; return x && x.value === v; }",
                             arg=[cases[-1]["name"], cases[-1]["bonne"]], timeout=5000)
    except Exception:
        pass
    pg.evaluate(JS_OUVRIR, sid)
    revenus = pg.evaluate("s => [...document.querySelectorAll(s + ' select')].map(x => [x.name, x.value, "
                          "x.parentNode.querySelector('.menu-vu').textContent === x.options[x.selectedIndex].text])", sel)
    bonnes = {c["name"]: c["bonne"] for c in cases}
    etat = pg.evaluate("k => localStorage.getItem(k)", cle) or ""
    t(nom + " : la réponse est sauvegardée, et chaque menu retrouve son choix après rechargement",
      '"reussi": true' in etat.replace('":true', '": true') and all(v == bonnes[n] and ok for n, v, ok in revenus),
      [x for x in revenus if x[1] != bonnes[x[0]]][:2])
    # ── mots coupés, cadre
    coupes, mises, deb = pg.evaluate(banc_ateliers.JS_MOTS_COUPES, sel)
    t(nom + " (1280 px) : aucun mot coupé au milieu (toutes les options, puis les retours), le tableau tient dans son cadre",
      not coupes and deb <= 1, (coupes[:4], deb))
    # ── impression
    premier, second = cases[0]["name"], cases[1]["name"]
    pg.select_option('#%s select[name="%s"]' % (uid, premier), value=cases[0]["bonne"])
    pg.select_option('#%s select[name="%s"]' % (uid, second), value="")
    # la fiche papier des séquences prépare l'impression sur « beforeprint » (elle déplie la séance en cours)
    pg.evaluate("() => window.dispatchEvent(new Event('beforeprint'))")
    pg.emulate_media(media="print")
    pg.wait_for_timeout(150)
    imp = pg.evaluate("""([n1, n2]) => {
        const a = document.getElementsByName(n1)[0], b = document.getElementsByName(n2)[0];
        const va = a.parentNode.querySelector('.menu-vu'), vb = b.parentNode.querySelector('.menu-vu');
        return [getComputedStyle(a).display, va.textContent === a.options[a.selectedIndex].text && va.getBoundingClientRect().height > 0,
                vb.textContent === '' && parseFloat(getComputedStyle(vb).borderBottomWidth) > 0 && vb.getBoundingClientRect().width > 40]; }""",
                      [premier, second])
    pg.emulate_media(media="screen")
    pg.evaluate("() => window.dispatchEvent(new Event('afterprint'))")
    t(nom + " : à l'impression, le menu disparaît, le choix s'imprime en texte, une case vide donne une ligne",
      imp[0] == "none" and imp[1] and imp[2], imp)
    t(nom + " (1280 px) : aucune erreur JavaScript venue du rappel ou du kit",
      not [x for x in err if "TACHES" not in x], err)
    ctx.close()
    # ── 390 px
    err = []
    ctx, pg, vu = ouvrir(b, chemin, sid, 390, err)
    t(nom + " (390 px) : aucun défilement horizontal de la page",
      vu and not pg.evaluate("document.documentElement.scrollWidth > innerWidth"),
      pg.evaluate("document.documentElement.scrollWidth"))
    cartes = pg.evaluate("s => { const t = document.querySelector(s + ' table.cdcf'); return getComputedStyle(t.querySelector('tbody tr')).display === 'block' "
                         "&& getComputedStyle(t.querySelector('thead')).display === 'none' && [...t.querySelectorAll('td')].every(td => "
                         "getComputedStyle(td, '::before').content.replace(/\"/g, '') === td.dataset.col); }", sel)
    t(nom + " (390 px) : chaque ligne devient une carte, chaque case porte le nom de sa colonne", cartes)
    coupes, mises, deb = pg.evaluate(banc_ateliers.JS_MOTS_COUPES, sel)
    t(nom + " (390 px) : aucun mot coupé au milieu, rien ne déborde du cadre", not coupes and deb <= 1, (coupes[:4], deb))
    ctx.close()


def main(ids):
    choisis = [r for r in rc.RAPPELS if not ids or r["id"] in ids]
    if not choisis:
        print("Aucun rappel à vérifier.")
        return 2
    for r in choisis:
        donnees(r)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for r in choisis:
            for chemin in pages(r):
                page(b, r, chemin)
        b.close()
    ok = sum(1 for _, x in RESULTATS if x)
    print("\n%d / %d tests passés" % (ok, len(RESULTATS)))
    echecs = [n for n, x in RESULTATS if not x]
    if echecs:
        print("Échecs :\n  - " + "\n  - ".join(echecs))
    return 0 if not echecs else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
