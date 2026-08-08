#!/usr/bin/env python3
"""Contrôles de l'index — règles d'or n°35 à n°41 (audit externe du 08/08/2026).

    python3 _outils/tests_index.py        # depuis la racine du dépôt
"""
import pathlib, re, sys
from playwright.sync_api import sync_playwright

RACINE = pathlib.Path(__file__).resolve().parent.parent
res = []


def t(nom, ok, det=""):
    res.append((nom, bool(ok)))
    print(("✔" if ok else "✘"), nom, det)


with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 900})
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto((RACINE / "index.html").as_uri()); pg.wait_for_timeout(600)
    src = pg.content()
    t("aucune erreur JavaScript", not errs, str(errs))

    # n°35 — un code n'apparaît jamais seul, et rien n'est tronqué
    pg.evaluate("document.querySelectorAll('details.comp').forEach(d=>d.open=true)")
    pg.wait_for_timeout(300)
    reperes = pg.eval_on_selector_all(".rep", "a=>a.map(x=>x.id)")
    t("les 114 repères sont présents", len(reperes) == 114, f"{len(reperes)} trouvés")
    t("chaque repère porte une formulation non vide",
      pg.evaluate("[...document.querySelectorAll('.rep')].every(r=>{"
                  "const f=r.querySelector('.form');return f && f.innerText.trim().length>25;})"))
    t("aucune formulation tronquée par des points de suspension",
      pg.evaluate("[...document.querySelectorAll('.rep .form, .comp>summary>span:nth-child(2)')]"
                  ".every(e=>!e.innerText.trim().endsWith('…'))"))
    t("chaque repère affiche ses domaines du socle",
      pg.evaluate("[...document.querySelectorAll('.rep')].every(r=>"
                  "(r.querySelector('.meta')||{}).innerText?.startsWith('Socle'))"))
    t("chaque repère affiche son statut de couverture",
      pg.evaluate("[...document.querySelectorAll('.rep')].every(r=>r.querySelector('.statut'))"))

    # n°36 — la codification interne est nommée comme telle
    t("la page distingue référence normative et codification interne",
      "Référence normative" in src and "codes de classement internes" in src
      and "ne figurent pas comme tels au BO" in src)
    t("la page n'affirme plus que les codes de repère viennent du BO",
      "C1-C9 du BO" not in src)

    # n°37 / n°39 — ressources pédagogiques d'un côté, gouvernance de l'autre
    t("aucun fichier de gouvernance dans la liste pédagogique",
      pg.evaluate("""[...document.querySelectorAll('.rep ul a')].every(a=>
        !/manifest|rapport_tests|SOURCES_MEDIAS|matrice_couverture|README\\.md|tests_.*\\.py/i
          .test(a.getAttribute('href')))"""))
    t("les fichiers de gouvernance restent accessibles, repliés",
      pg.eval_on_selector_all(".rep details.maint", "a=>a.length") > 0)
    t("les ressources portent un nom pédagogique, pas un nom de fichier",
      pg.evaluate("[...document.querySelectorAll('.rep ul a')].every(a=>"
                  "!/\\.(html|md|csv|json|py|pkt|drawio|xlsx)$/.test(a.innerText.trim()))"))
    t("l'étiquette du compteur dit ce qui est compté",
      "ressource(s) pédagogique(s)" in src)

    # n°40 — hors ligne d'abord
    t("aucune ressource distante appelée", "fonts.googleapis" not in src
      and not re.search(r'(src|href)="https?://(?!pll-process)', src))

    # n°41 — l'index tenu au niveau des séquences
    t("structure sémantique (header, nav ou main, footer)",
      pg.eval_on_selector_all("main", "a=>a.length") == 1
      and pg.eval_on_selector_all("footer", "a=>a.length") >= 1)
    t("lien d'évitement vers le contenu", pg.eval_on_selector_all("a.skip", "a=>a.length") == 1)
    t("focus clavier stylé", "focus-visible" in src)
    t("les liens ne reposent pas sur la seule couleur",
      pg.evaluate("getComputedStyle(document.querySelector('.rep a')).textDecorationLine")
      .startswith("underline"))
    t("meta description renseignée",
      len(pg.eval_on_selector("meta[name=description]", "e=>e.content") or "") > 80)
    t("pas de défilement horizontal à 1280 px",
      pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+1"))
    pg.set_viewport_size({"width": 390, "height": 844}); pg.wait_for_timeout(300)
    t("pas de défilement horizontal à 390 px",
      pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+2"))
    b.close()

print(f"\n{sum(1 for _, o in res if o)} / {len(res)} contrôles passés")
sys.exit(0 if all(o for _, o in res) else 1)
