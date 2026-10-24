# -*- coding: utf-8 -*-
"""Banc de tests des ateliers des représentations (Playwright / Chromium).

    python3 banc_ateliers.py                 # tous les ateliers construits, leurs QCM, synthèses et les cahiers
    python3 banc_ateliers.py interacteurs    # un ou plusieurs modules (--json fichier : résultats écrits)

Pour chaque page de niveau, à 390 px :
  - aucune erreur JavaScript, aucun défilement horizontal ;
  - un onglet par exercice, plus la clôture ;
  - chaque exercice : « Vérifier » à vide donne un retour 🔴 ; rempli juste (réponses tirées des définitions de la
    page, `exemple` des widgets texte/liste lu dans le module de données), il donne « Tout est juste » ;
  - la sauvegarde locale revient après un rechargement.
Puis le QCM (30 questions), les deux synthèses et les cahiers de niveau : chargement sans erreur, sans débordement.

Code de sortie : 0 tout passe · 1 au moins un échec · 2 rien n'a été vérifié (règle d'or n°299).
"""
import importlib
import json
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import build  # noqa: E402

RESULTATS = []


def t(nom, ok, detail=""):
    RESULTATS.append((nom, bool(ok)))
    print(("✔ " if ok else "✘ ") + nom + ("" if ok else "  — " + str(detail)[:220]))


def defs_page(pg):
    brut = pg.eval_on_selector("#donnees-page", "e => e.textContent")
    return json.loads(brut)["exercices"]


def exemples(at, niv):
    """{nom complet du widget : exemple} pour les widgets texte et liste du niveau."""
    ex = {}
    for e in at.NIVEAUX[niv]["exercices"]:
        uid = "%s_%s_%s" % (at.COURT, niv, e["id"])
        for w in e["widgets"]:
            if w.get("exemple"):
                ex["%s__%s" % (uid, w["name"])] = w["exemple"]
    return ex


def remplir(pg, uid, d, exs):
    """Remplit juste l'exercice uid ; rend la liste des widgets qu'il n'a pas su remplir."""
    rate = []
    sel = "#%s " % uid
    for w in d["widgets"]:
        ty = w["type"]
        if ty == "choix":
            pg.check(sel + 'input[name="%s"][value="%s"]' % (w["name"], w["bonne"]))
        elif ty == "cases":
            for val in w["toutes"]:
                loc = pg.locator(sel + 'input[name="%s"][value="%s"]' % (w["name"], val))
                (loc.check if val in w["bonnes"] else loc.uncheck)()
        elif ty == "classer":
            for it in w["items"]:
                pg.check(sel + 'input[name="%s"][value="%s"]' % (it["name"], it["bonne"]))
        elif ty == "slots":
            for s in w["slots"]:
                pg.check(sel + 'input[name="%s"][value="%s"]' % (s["name"], s["bonnes"][0]))
        elif ty == "liste":
            texte = exs.get(w["name"]) or "\n".join(a["nom"] for a in w["attendus"])
            pg.fill("#" + w["name"], texte)
        elif ty == "texte":
            if w["name"] in exs:
                pg.fill("#" + w["name"], exs[w["name"]])
            else:
                rate.append(w["name"])
        elif ty == "croquis":
            pg.fill("#%s_desc" % w["name"], "Au centre de mon croquis, on voit l'objet en entier ; les légendes nomment chaque "
                                              "partie, et une flèche rouge montre le geste demandé.")
            for i in range(len(w["checklist"])):
                pg.check(sel + "#%s_check-%d" % (w["name"], i))
        else:
            rate.append(w.get("name", ty))
    return rate


def page_niveau(b, at, niv):
    chemin = build.page_niveau(at, niv)
    nom = "%s %s" % (at.SLUG, niv)
    ctx = b.new_context(viewport={"width": 390, "height": 900})
    pg = ctx.new_page()
    err = []
    pg.on("pageerror", lambda e: err.append(str(e)))
    pg.on("console", lambda m: err.append("console: " + m.text) if m.type == "error" else None)
    pg.goto(chemin.as_uri())
    pg.wait_for_timeout(250)
    t(nom + " : aucune erreur JavaScript au chargement", not err, err)
    t(nom + " : aucun défilement horizontal à 390 px", not pg.evaluate("document.documentElement.scrollWidth > innerWidth"))
    defs = defs_page(pg)
    exos = at.NIVEAUX[niv]["exercices"]
    onglets = pg.locator('[role="tab"]').count()
    t(nom + " : un onglet par exercice, plus la clôture (%d)" % (len(exos) + 1), onglets == len(exos) + 1, onglets)
    exs = exemples(at, niv)
    for i, e in enumerate(exos):
        uid = "%s_%s_%s" % (at.COURT, niv, e["id"])
        pg.locator('[role="tab"]').nth(i).click()
        pg.wait_for_timeout(60)
        pg.click("#%s button.verifier" % uid)
        r0 = pg.inner_text("#%s .retour" % uid)
        t(nom + " · %s : « Vérifier » à vide donne un retour à reprendre" % e["id"], "🔴" in r0, r0[:120])
        rate = remplir(pg, uid, defs[uid], exs)
        pg.click("#%s button.verifier" % uid)
        pg.wait_for_timeout(60)
        r1 = pg.inner_text("#%s .retour" % uid)
        t(nom + " · %s : rempli juste, « Tout est juste »%s" % (e["id"], " (sans exemple : %s)" % rate if rate else ""),
          "Tout est juste" in r1 and not rate, r1[:160])
    # sauvegarde : le premier exercice revient après rechargement
    pg.reload()
    pg.wait_for_timeout(250)
    uid0 = "%s_%s_%s" % (at.COURT, niv, exos[0]["id"])
    etat = pg.evaluate("k => localStorage.getItem(k)", "rep_%s_%s_%s" % (at.SLUG, niv, exos[0]["id"]))
    t(nom + " : la sauvegarde locale du premier exercice existe", bool(etat))
    reussi = False
    try:
        reussi = bool(json.loads(etat or "{}").get("reussi"))
    except ValueError:
        pass
    t(nom + " : le premier exercice est noté réussi après rechargement", reussi, (etat or "")[:120])
    t(nom + " : aucune erreur JavaScript pendant le parcours", not err, err)
    ctx.close()


def page_simple(b, chemin, nom, attendu_q=None):
    if not chemin.exists():
        t(nom + " : la page existe", False, chemin)
        return
    for largeur in (390, 1280):
        ctx = b.new_context(viewport={"width": largeur, "height": 900})
        pg = ctx.new_page()
        err = []
        pg.on("pageerror", lambda e: err.append(str(e)))
        pg.goto(chemin.as_uri())
        pg.wait_for_timeout(250)
        t("%s (%d px) : aucune erreur JavaScript" % (nom, largeur), not err, err)
        t("%s (%d px) : aucun défilement horizontal" % (nom, largeur),
          not pg.evaluate("document.documentElement.scrollWidth > innerWidth"))
        if attendu_q and largeur == 390:
            n = pg.evaluate("typeof QUESTIONS !== 'undefined' ? QUESTIONS.length : -1")
            t("%s : %d questions" % (nom, attendu_q), n == attendu_q, n)
        ctx.close()


def main(modules, cahiers=False, sortie_json=None):
    construits = []
    for m in modules:
        try:
            at = importlib.import_module("donnees_" + m)
        except ModuleNotFoundError:
            continue
        if all(build.page_niveau(at, niv).exists() for niv in at.NIVEAUX):
            construits.append(at)
    if not construits:
        print("Aucun atelier construit à vérifier.")
        return 2
    with sync_playwright() as p:
        b = p.chromium.launch()
        for at in construits:
            for niv in at.NIVEAUX:
                page_niveau(b, at, niv)
            page_simple(b, build.qcm(at), at.SLUG + " QCM", attendu_q=30)
            page_simple(b, build.synthese_eleve(at), at.SLUG + " synthèse élève")
            page_simple(b, build.synthese_prof(at), at.SLUG + " synthèse professeur")
        if cahiers:
            for niv in ("5e", "4e", "3e"):
                if build.cahier(niv).exists():
                    page_simple(b, build.cahier(niv), "cahier " + niv)
        b.close()
    ok = sum(1 for _, r in RESULTATS if r)
    print("\n%d / %d tests passés" % (ok, len(RESULTATS)))
    echecs = [n for n, r in RESULTATS if not r]
    if echecs:
        print("Échecs :\n  - " + "\n  - ".join(echecs))
    if sortie_json:
        pathlib.Path(sortie_json).write_text(json.dumps([{"test": n, "ok": r} for n, r in RESULTATS],
                                                        ensure_ascii=False, indent=1), encoding="utf-8")
    return 0 if not echecs else 1


if __name__ == "__main__":
    args = sys.argv[1:]
    sortie = None
    if "--json" in args:
        i = args.index("--json")
        sortie = args[i + 1]
        del args[i:i + 2]
    # sans module nommé : tous les ateliers, et les cahiers de niveau
    sys.exit(main(args or build.MODULES, cahiers=not args, sortie_json=sortie))
