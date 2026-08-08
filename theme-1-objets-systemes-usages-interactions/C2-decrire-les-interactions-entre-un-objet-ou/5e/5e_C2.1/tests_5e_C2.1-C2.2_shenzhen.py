#!/usr/bin/env python3
"""Suite de tests du lot Shenzhen 5e_C2.1 · C2.2.

    python3 tests_5e_C2.1-C2.2_shenzhen.py

À lancer depuis le dossier du lot. Les chemins sont relatifs à ce dossier.
"""
from playwright.sync_api import sync_playwright
import pathlib
import sys

SEQ = pathlib.Path("sequence_5e_C2_shenzhen_station_velos.html").resolve().as_uri()
QCM = pathlib.Path("qcm_5e_C2_shenzhen_station_velos.html").resolve().as_uri()
SYE = pathlib.Path("Synthèses/synthese_eleve_5e_C2.1-C2.2.html").resolve().as_uri()
SYP = pathlib.Path("Synthèses/synthese_professeur_5e_C2.1-C2.2.html").resolve().as_uri()

res = []


def t(n, ok, d=""):
    res.append((n, bool(ok)))
    print(("✔" if ok else "✘"), n, d)


# Huit entrées, deux par famille — les quatre familles du programme :
# usagers, données, autres objets, éléments de l'environnement.
LISTE_OK = ("l'usager abonné : il prend et rend un vélo\n"
            "l'agent de maintenance : il répare et débloque\n"
            "l'identifiant de l'abonné (donnée) : sans lui, rien ne se déverrouille\n"
            "l'état « disponible » du vélo (donnée) : il vient du serveur\n"
            "le vélo (autre objet) : il est ancré à la borne\n"
            "le smartphone (autre objet) : il transmet l'identifiant\n"
            "la pluie (environnement) : elle mouille les bornes\n"
            "le trottoir (environnement) : la station y est fixée")

# Huit entrées, mais aucune donnée : la famille qu'on oublie toujours.
LISTE_SANS_DONNEE = ("l'usager abonné\nl'agent de maintenance\nle riverain\nle maire\n"
                     "le vélo\nle smartphone\nla pluie\nle trottoir")

CHOIX_SANS_DD = ("La borne est inclinée : ce choix répond à la pluie, il relève de la sécurité.\n"
                 "L'ancrage est à 90 cm : ce choix répond à l'usager, il relève de l'ergonomie.\n"
                 "Les arêtes sont arrondies : ce choix répond à l'usager, sécurité.\n"
                 "Le boîtier a une vis unique : il répond à l'agent de maintenance, ergonomie.")

CHOIX_OK = ("La borne est inclinée : ce choix répond à la pluie, il relève de la sécurité.\n"
            "L'ancrage est à 90 cm : ce choix répond à l'usager, il relève de l'ergonomie.\n"
            "Les arêtes sont arrondies : ce choix répond à l'usager, il relève de la sécurité.\n"
            "Les pièces se remplacent une par une : cela répond au budget de la ville et à la "
            "matière à produire, cela relève du développement durable.")

TRANSF_OK = ("L'air salin change : il attaque les métaux, il faut revoir les matériaux.\n"
             "La pluie change : elle est bien plus intense, l'inclinaison ne suffit plus.\n"
             "Le cyclone apparaît : il faut pouvoir démonter ou arrimer la station.")

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 900})
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))

    # ───────────────────────────── la séquence ─────────────────────────────
    pg.goto(SEQ)
    pg.wait_for_timeout(500)
    t("séquence : aucune erreur JS", not errs, str(errs))
    contenu = pg.content()
    t("séquence : hors ligne, aucune ressource distante (n°40)",
      "http://" not in contenu and "https://" not in contenu.replace(
          'xmlns="http://www.w3.org/2000/svg"', ""))
    t("séquence : lien d'accueil valide (n°11)",
      pathlib.Path("../../../../index.html").exists())
    t("bandeau de tâches affiché (n°30)",
      "Séance 1" in pg.inner_text("#tachesBandeau"))

    n_ta = pg.eval_on_selector_all("textarea", "a=>a.length")
    n_et = pg.eval_on_selector_all("details.etayage", "a=>a.length")
    t("chaque zone de rédaction a sa version étayée (n°31)",
      n_ta == 7 and n_et >= n_ta, f"{n_ta} zones / {n_et} étayages")

    t("chaque champ porte une étiquette (n°34)",
      pg.evaluate("[...document.querySelectorAll('select,textarea')].every(e=>!e.id||"
                  "document.querySelector(`label[for=\"${e.id}\"]`)||e.getAttribute('aria-label'))"))
    t("chaque figure a une alternative longue (n°1)",
      pg.evaluate("[...document.querySelectorAll('.fig img')].every(i=>i.alt.length>120)"))
    t("les deux figures sont chargées",
      pg.evaluate("[...document.querySelectorAll('.fig img')].length===2"))

    t("le compteur annonce 3 activités (n°39)", "/ 3 activités" in pg.inner_text("#progTxt"))

    # le billet d'entrée oriente, il ne sanctionne pas
    pg.click('[data-check="0"]')
    pg.wait_for_timeout(120)
    t("billet d'entrée : oriente sans note (n°26)",
      "aucune note" in pg.inner_text("#fb0"), pg.inner_text("#fb0")[:55])
    t("billet d'entrée : ne compte pas dans la progression",
      "0 / 3" in pg.inner_text("#progTxt"))

    # activité 1 : le verrou de production
    pg.evaluate("['a1_1','a1_2','a1_3','a1_4','a1_5','a1_6','a1_7']"
                ".forEach(i=>document.getElementById(i).selectedIndex=1)")
    pg.click('[data-check="1"]')
    pg.wait_for_timeout(120)
    t("activité 1 : la liste des quatre familles est exigée",
      "QUATRE familles" in pg.inner_text("#fb1"), pg.inner_text("#fb1")[-50:])
    pg.fill("#a1_liste", LISTE_SANS_DONNEE)
    pg.click('[data-check="1"]')
    pg.wait_for_timeout(120)
    # Le message doit NOMMER la famille manquante : un refus qui n'aide pas
    # l'élève à repartir n'est pas un vérificateur, c'est un mur.
    t("activité 1 : une liste sans données est refusée, et la famille est nommée",
      "DONNÉES" in pg.inner_text("#fb1"), pg.inner_text("#fb1")[-70:])
    pg.fill("#a1_liste", LISTE_OK)
    pg.click('[data-check="1"]')
    pg.wait_for_timeout(120)
    t("activité 1 : validée quand les quatre familles sont couvertes",
      "7 / 7" in pg.inner_text("#fb1"), pg.inner_text("#fb1")[:30])
    t("progression mise à jour", "1 / 3" in pg.inner_text("#progTxt"))

    # activité 2
    pg.click("#tab-s2")
    pg.wait_for_timeout(120)
    pg.evaluate("['a2_1','a2_2','a2_3','a2_4','a2_5','a2_6','a2_7','a2_8']"
                ".forEach(i=>document.getElementById(i).selectedIndex=1)")
    pg.click('[data-check="2"]')
    pg.wait_for_timeout(120)
    t("activité 2 : le relevé écrit est exigé",
      "QUATRE choix" in pg.inner_text("#fb2"), pg.inner_text("#fb2")[-50:])
    pg.fill("#a2_choix", CHOIX_SANS_DD)
    pg.click('[data-check="2"]')
    pg.wait_for_timeout(120)
    t("activité 2 : un relevé sans développement durable est refusé",
      "développement durable" in pg.inner_text("#fb2"))
    pg.fill("#a2_choix", CHOIX_OK)
    pg.click('[data-check="2"]')
    pg.wait_for_timeout(120)
    t("activité 2 : validée une fois le développement durable présent",
      "8 / 8" in pg.inner_text("#fb2"))

    # activité 3 + transfert
    pg.click("#tab-s3")
    pg.wait_for_timeout(120)
    pg.evaluate("['a3_1','a3_2','a3_3','a3_4']"
                ".forEach(i=>document.getElementById(i).selectedIndex=1)")
    pg.click('[data-check="3"]')
    pg.wait_for_timeout(120)
    t("activité 3 : le transfert martiniquais est exigé",
      "TROIS interacteurs" in pg.inner_text("#fb3"), pg.inner_text("#fb3")[-50:])
    pg.fill("#a3_transf", TRANSF_OK)
    pg.click('[data-check="3"]')
    pg.wait_for_timeout(120)
    t("activité 3 : validée une fois le transfert rédigé", "4 / 4" in pg.inner_text("#fb3"))
    t("progression complète", "3 / 3" in pg.inner_text("#progTxt"))

    # mode essentiel (n°29)
    pg.click("#btnEssentiel")
    pg.wait_for_timeout(120)
    t("mode essentiel : actif et annoncé",
      pg.get_attribute("#btnEssentiel", "aria-pressed") == "true")
    pg.click("#btnEssentiel")
    pg.wait_for_timeout(100)

    # rappel de l'hypothèse au bilan
    pg.click("#tab-s1")
    pg.fill("#hyp1", "l'usager, le vélo et la pluie")
    pg.wait_for_timeout(150)
    pg.click("#tab-s3")
    pg.wait_for_timeout(120)
    t("l'hypothèse de départ est rappelée au bilan",
      "l'usager, le vélo et la pluie" in pg.inner_text("#rappelHyp"))

    # sauvegarde / restauration
    pg.reload()
    pg.wait_for_timeout(400)
    t("sauvegarde locale restaurée après rechargement",
      pg.input_value("#a1_liste").startswith("l'usager abonné")
      and "3 / 3" in pg.inner_text("#progTxt"))

    # blocs de la règle n°4
    corps = pg.content()
    t("bloc « Prêt·e à t'entraîner » présent (n°4)", "Prêt·e à t'entraîner" in corps)
    t("bloc « Bonus » présent (n°4)", "Bonus (facultatif" in corps)
    t("un seul bouton QCM dans toute la séquence (n°4)",
      corps.count('href="qcm_5e_C2_shenzhen_station_velos.html"') == 1)

    # ─────────────────────────────── le QCM ───────────────────────────────
    errs.clear()
    pg.goto(QCM)
    pg.wait_for_timeout(400)
    t("QCM : aucune erreur JS", not errs, str(errs))
    info = pg.evaluate("""()=>({
        n: QUESTIONS.length,
        rep: [0,1,2,3].map(k=>QUESTIONS.filter(q=>q.r===k).length),
        dvide: QUESTIONS.every(q=>q.d[q.r]===""),
        courtes: QUESTIONS.flatMap(q=>q.d.filter((x,j)=>j!==q.r&&x.trim().length<=20)).length,
        imgs: QUESTIONS.filter(q=>q.img).length,
        c21: QUESTIONS.filter(q=>q.c==="C2.1").length,
        c22: QUESTIONS.filter(q=>q.c==="C2.2").length,
        complets: QUESTIONS.every(q=>q.expl&&q.ex&&q.err&&q.ret&&q.o.length===4&&q.d.length===4)
    })""")
    t("QCM : 30 questions", info["n"] == 30, str(info["n"]))
    t("QCM : 15 par code", info["c21"] == 15 and info["c22"] == 15,
      f"{info['c21']} / {info['c22']}")
    t("QCM : bonnes réponses réparties sur A/B/C/D", max(info["rep"]) - min(info["rep"]) <= 1,
      str(info["rep"]))
    t("QCM : 5 questions illustrées", info["imgs"] == 5, str(info["imgs"]))
    t("QCM : les trois domaines du code sont ceux du programme",
      pg.evaluate("QUESTIONS.find(q=>q.n==='Trois domaines').o[QUESTIONS.find("
                  "q=>q.n==='Trois domaines').r]")
      == "l'ergonomie, la sécurité et le développement durable")
    t("QCM : chaque distracteur porte une réfutation qui explique",
      info["courtes"] == 0 and info["dvide"], f"{info['courtes']} réfutation(s) trop courte(s)")
    t("QCM : chaque question a explication, exemple, erreur classique et à-retenir",
      info["complets"])

    # parcours complet : toutes les bonnes réponses
    n = pg.evaluate("QUESTIONS.length")
    for i in range(n):
        r = pg.evaluate(f"QUESTIONS[{i}].r")
        pg.click(f".option >> nth={r}")
        pg.click("#btnValider")
        if i < n - 1:
            pg.click("#btnSuiv")
    pg.click("#btnTerminer")
    pg.wait_for_timeout(300)
    bilan = pg.inner_text("body")
    t("QCM : parcours complet, 30 bonnes réponses acceptées",
      pg.evaluate("etat.reponses.filter((x,i)=>x===QUESTIONS[i].r).length") == 30)
    # Règle n°42 : la formulation d'une compétence se recopie. « esthétique » était
    # une substitution de ma main, corrigée dans la séquence en juillet et restée
    # dans le QCM jusqu'au 8 août — le contrôle mécanisé ne regardait que la carte
    # de la séquence. On le vérifie désormais ici aussi.
    libelles = pg.evaluate("Object.values(COMP_LABELS).join(' | ')")
    t("QCM : aucune formulation de compétence ne dit « esthétique »",
      "esthétique" not in libelles, libelles[:80])
    t("QCM : la formulation de C2.2 est celle du référentiel",
      "développement durable" in libelles)
    t("QCM : bilan par compétence affiché",
      "5e_C2.1" in bilan and "5e_C2.2" in bilan)
    pg.reload()
    pg.wait_for_timeout(300)
    t("QCM : sauvegarde restaurée après rechargement",
      pg.evaluate("etat.validees.filter(Boolean).length") == 30)

    # une mauvaise réponse affiche bien la réfutation du distracteur choisi
    pg.evaluate("localStorage.clear()")
    pg.reload()
    pg.wait_for_timeout(300)
    r0 = pg.evaluate("QUESTIONS[0].r")
    faux = (r0 + 1) % 4
    pg.click(f".option >> nth={faux}")
    pg.click("#btnValider")
    pg.wait_for_timeout(200)
    attendu = pg.evaluate(f"QUESTIONS[0].d[{faux}]")
    t("QCM : la réfutation du distracteur choisi est affichée",
      attendu[:40] in pg.inner_text("body"))

    # ───────────────────────────── les synthèses ─────────────────────────────
    for nom, uri, figs in (("élève", SYE, 2), ("professeur", SYP, 0)):
        errs.clear()
        pg.goto(uri)
        pg.wait_for_timeout(300)
        t(f"synthèse {nom} : aucune erreur JS", not errs, str(errs))
        t(f"synthèse {nom} : {figs} figure(s) référencée(s)",
          pg.eval_on_selector_all("object", "a=>a.length") == figs)
        t(f"synthèse {nom} : liens de navigation valides",
          all(pathlib.Path("Synthèses") .joinpath(h).exists()
              for h in pg.eval_on_selector_all("a", "a=>a.map(e=>e.getAttribute('href'))")))

    b.close()

ko = [n for n, ok in res if not ok]
print(f"\n{len(res) - len(ko)} / {len(res)} tests passés")
if ko:
    print("Échecs :")
    for n in ko:
        print("  -", n)
sys.exit(1 if ko else 0)
