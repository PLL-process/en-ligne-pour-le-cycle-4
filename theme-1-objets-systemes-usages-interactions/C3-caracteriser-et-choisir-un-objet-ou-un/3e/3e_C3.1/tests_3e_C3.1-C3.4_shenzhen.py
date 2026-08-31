#!/usr/bin/env python3
"""Suite de tests du lot Shenzhen 3e_C3.1 à C3.4.  python3 tests_3e_C3.1-C3.4_shenzhen.py"""
from playwright.sync_api import sync_playwright
import pathlib, sys
SEQ = pathlib.Path("sequence_3e_C3.1-C3.4_shenzhen.html").resolve().as_uri()
QCM = pathlib.Path("qcm_3e_C3.1-C3.4_shenzhen.html").resolve().as_uri()
res = []
def t(n, ok, d=""): res.append((n, bool(ok))); print(("✔" if ok else "✘"), n, d)

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1280,"height":900})
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))

    pg.goto(SEQ); pg.wait_for_timeout(600)
    t("séquence : aucune erreur JS", not errs, str(errs))
    # `pg.content()` sérialise le DOM : chaque SVG en ligne y porte son
    # `xmlns="http://www.w3.org/2000/svg"`, qui est un identifiant d'espace de noms
    # et non une ressource — aucun navigateur ne le demande. Chercher « http:// »
    # dans le HTML rendait donc ce contrôle rouge dès qu'un schéma était dessiné
    # dans la page. On regarde maintenant ce que la page IRAIT CHERCHER : les
    # attributs de chargement, sans les hyperliens, qui eux ont le droit d'être
    # distants (règle d'or n°40, correction du 31/08/2026).
    distantes = pg.eval_on_selector_all(
        "[src], link[href], object[data], iframe[src], use[href]",
        "l=>l.map(e=>e.getAttribute('src')||e.getAttribute('href')||e.getAttribute('data'))"
        ".filter(u=>u && /^(https?:)?\/\//i.test(u))")
    t("séquence : hors ligne, aucune ressource distante (n°40)",
      "fonts.googleapis" not in pg.content() and not distantes, str(distantes))
    t("bandeau de tâches affiché (n°30)", "Séance 1" in pg.inner_text("#tachesBandeau"))
    n_ta = pg.eval_on_selector_all("textarea", "a=>a.length")
    n_et = pg.eval_on_selector_all("details.etayage", "a=>a.length")
    t("chaque zone de rédaction a sa version étayée (n°31)",
      n_ta == n_et == 9, f"{n_ta} zones / {n_et} étayages")
    t("chaque champ porte une étiquette (n°34)",
      pg.evaluate("[...document.querySelectorAll('select,textarea')].every(e=>!e.id||"
                  "document.querySelector(`label[for=\"${e.id}\"]`)||e.getAttribute('aria-label'))"))
    t("chaque figure a une alternative longue",
      pg.evaluate("[...document.querySelectorAll('.fig img')].every(i=>i.alt.length>120)"))
    # billet d'entrée : oriente sans sanctionner
    pg.click('[data-check="0"]'); pg.wait_for_timeout(150)
    t("billet d'entrée : oriente sans note (n°26)",
      "aucune note" in pg.inner_text("#fb0"), pg.inner_text("#fb0")[:60])
    # activité 1 complète
    pg.evaluate("['a1_1','a1_2','a1_3','a1_4','a1_5','a1_6']"
                ".forEach(i=>document.getElementById(i).selectedIndex=1)")
    pg.click('[data-check="1"]'); pg.wait_for_timeout(150)
    t("activité 1 : la liste des trois familles est exigée",
      "TROIS familles" in pg.inner_text("#fb1"), pg.inner_text("#fb1")[-45:])
    pg.fill("#a1_liste", "Solution 1 (passive) : ventilation naturelle traversante. "
                         "Solution 2 (passive) : ombrage du mur ouest. "
                         "Solution 3 (active) : extracteur asservi au thermostat. "
                         "Solution 4 (active) : climatiseur split. "
                         "Solution 5 (organisationnelle) : réduire le nombre de machines.")
    pg.click('[data-check="1"]'); pg.wait_for_timeout(150)
    t("activité 1 : validée une fois la liste écrite", "6 / 6" in pg.inner_text("#fb1"))
    t("progression mise à jour", "1 / 5" in pg.inner_text("#progTxt"))
    # verrou de rédaction : l'activité 2 refuse sans texte
    pg.click("#tab-s2"); pg.wait_for_timeout(150)
    pg.evaluate("['a2_1','a2_2','a2_3','a2_4','a2_5','a2_6']"
                ".forEach(i=>document.getElementById(i).selectedIndex=1)")
    pg.click('[data-check="2"]'); pg.wait_for_timeout(150)
    t("activité 2 : la défense de la grille est exigée",
      "grille" in pg.inner_text("#fb2"), pg.inner_text("#fb2")[-55:])
    pg.fill("#a2_grille", "J'ai retenu le coût sur dix ans, la performance, la consommation "
                          "et la réparabilité. Le coût sur dix ans pèse le plus car le collège "
                          "doit tenir un budget durable. Si le besoin avait été urgent, "
                          "j'aurais privilégié la performance.")
    pg.click('[data-check="2"]'); pg.wait_for_timeout(150)
    t("activité 2 : validée une fois rédigée", "6 / 6" in pg.inner_text("#fb2"))
    # mode essentiel
    pg.click("#btnEssentiel"); pg.wait_for_timeout(150)
    t("mode essentiel masque référentiel et corrections (n°29)",
      not pg.is_visible(".referentiel-card") and not pg.is_visible("details.correction"))
    t("mode essentiel laisse les versions étayées visibles",
      pg.is_visible(".seance-panel.active details.etayage"))
    pg.click("#btnEssentiel")
    # sauvegarde
    pg.reload(); pg.wait_for_timeout(600)
    t("sauvegarde et restauration après rechargement",
      "1 / 5" in pg.inner_text("#progTxt") or "2 / 5" in pg.inner_text("#progTxt"))
    # innerText ignore les panneaux masqués : on interroge le document, pas l'affichage.
    contenu = pg.content()
    t("blocs de la règle n°4 présents",
      "Prêt·e à t'entraîner" in contenu and "Bonus (facultatif" in contenu)
    t("un seul bouton QCM",
      pg.eval_on_selector_all('a.btn.qcm',"a=>a.length")==1)
    t("pas de défilement horizontal à 1280 px",
      pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+1"))
    pg.set_viewport_size({"width":390,"height":844}); pg.wait_for_timeout(300)
    t("pas de défilement horizontal à 390 px",
      pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+2"))
    pg.set_viewport_size({"width":1280,"height":900})

    errs.clear(); pg.goto(QCM); pg.wait_for_timeout(600)
    t("QCM : aucune erreur JS", not errs, str(errs))
    t("QCM : hors ligne (n°40)", "fonts.googleapis" not in pg.content())
    t("QCM : 30 questions", pg.evaluate("QUESTIONS.length")==30)
    t("QCM : 1 illustrée avec alternative longue",
      pg.evaluate("QUESTIONS.filter(q=>q.img).length")==1
      and pg.evaluate("QUESTIONS.filter(q=>q.img).every(q=>q.img.alt.length>80)"))
    rep = pg.evaluate("QUESTIONS.reduce((a,q)=>(a[q.r]=(a[q.r]||0)+1,a),{})")
    t("QCM : bonnes réponses réparties sur A/B/C/D", min(rep.values())>=7, str(rep))
    t("QCM : aucune réfutation en face de la bonne réponse",
      pg.evaluate("QUESTIONS.every(q=>q.d[q.r]==='')"))
    t("QCM : chaque distracteur réfuté",
      pg.evaluate("QUESTIONS.every(q=>q.d.filter((x,i)=>i!==q.r).every(x=>x&&x.length>20))"))
    t("QCM : les quatre codes sont couverts",
      set(pg.evaluate("[...new Set(QUESTIONS.map(q=>q.c))]"))=={"C3.1","C3.2","C3.3","C3.4"})
    t("QCM : les cinq champs de correction sont remplis",
      pg.evaluate("QUESTIONS.every(q=>q.expl&&q.ex&&q.err&&q.ret&&q.n)"))
    b.close()

print(f"\n{sum(1 for _,o in res if o)} / {len(res)} tests passés")
sys.exit(0 if all(o for _,o in res) else 1)
