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
    distantes = []; pg.on("request", lambda r: distantes.append(r.url) if r.url.startswith("http") else None)
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
    # (21/11/2026 : le contrôle cherchait encore l'ancienne phrase, « codes de classement internes » ; la page dit
    #  la même chose avec d'autres mots depuis la refonte de l'index.)
    t("la page distingue référence normative et codification interne",
      "Référence normative" in src and "Codification opérationnelle" in src
      and "ils ne viennent pas du programme officiel" in src)
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
    # (21/11/2026 : le contrôle refusait tout lien sortant, dont celui de la licence, règle n°321. Un lien n'est pas
    #  une ressource appelée : on écoute ce que la page charge, et on lit ses balises qui chargent.)
    t("aucune ressource distante appelée", not distantes and "fonts.googleapis" not in src
      and not re.search(r'<(?:script|img|iframe|source|video|audio)\b[^>]*\ssrc="https?://', src)
      and not re.search(r'<link\b[^>]*\shref="https?://', src), str(distantes[:3]))

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
    t("accès rapide : aucun groupe ne déborde à 390 px",
      pg.evaluate("[...document.querySelectorAll('#acces-rapide .rapide-groupe')].every(g=>g.scrollWidth<=g.clientWidth+1)"))
    pg.set_viewport_size({"width": 1280, "height": 900}); pg.wait_for_timeout(200)

    # L'accès rapide (08/11 et 21/11/2026) : chaque lien mène à une page qui existe, et à la séance qu'il annonce ;
    # chaque code de repère mène à sa ligne, qui s'ouvre.
    liens = pg.eval_on_selector_all("#acces-rapide li > a:not(.niv)", "a=>a.map(x=>[x.getAttribute('href'), x.innerText.trim()])")
    t("accès rapide : des liens sont présents", len(liens) >= 10, f"{len(liens)} lien(s)")
    manquants = [h for h, _ in liens if not (RACINE / h.split("#")[0]).is_file()]
    t("accès rapide : chaque lien mène à un fichier qui existe", not manquants, str(manquants[:3]))
    ancres = [(h, n) for h, n in liens if "#" in h]
    rates = []
    for h, n in ancres:
        chemin, ancre = h.split("#", 1)
        q = b.new_page(viewport={"width": 1280, "height": 900})
        q.goto((RACINE / chemin).as_uri() + "#" + ancre); q.wait_for_timeout(900)
        vu = q.evaluate("id=>{const e=document.getElementById(id);return !!e&&e.getClientRects().length>0}", ancre)
        if not vu:
            rates.append(n[:60])
        q.close()
    t("accès rapide : un lien vers une séance ouvre cette séance", ancres and not rates,
      f"{len(ancres)} lien(s) joués" + (f", ratés : {rates}" if rates else ""))
    codes = pg.eval_on_selector_all("#acces-rapide a.niv", "a=>a.map(x=>[x.getAttribute('href'), x.innerText.trim(), x.title])")
    t("accès rapide : un code de repère mène à sa ligne et porte sa formulation",
      codes and all(h == "#" + n and len(ti) > 25 and pg.query_selector(f'[id="{n}"].rep') for h, n, ti in codes),
      f"{len(codes)} code(s)")
    if codes:
        pg.evaluate("document.querySelectorAll('details.comp').forEach(d=>d.open=false)")
        pg.click("#acces-rapide a.niv"); pg.wait_for_timeout(500)
        cible = codes[0][1]
        t("accès rapide : le clic sur un code ouvre sa ligne dans l'index",
          pg.evaluate("id=>{const e=document.getElementById(id);return !!e&&e.getClientRects().length>0}", cible), cible)
    b.close()

print(f"\n{sum(1 for _, o in res if o)} / {len(res)} contrôles passés")
sys.exit(0 if all(o for _, o in res) else 1)
