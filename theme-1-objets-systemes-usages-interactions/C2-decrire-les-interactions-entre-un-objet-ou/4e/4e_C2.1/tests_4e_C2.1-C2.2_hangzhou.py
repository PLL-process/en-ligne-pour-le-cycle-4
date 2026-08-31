#!/usr/bin/env python3
"""Suite de tests du lot Hangzhou 4e_C2.1 · C2.2.

    python3 tests_4e_C2.1-C2.2_hangzhou.py

À lancer depuis le dossier du lot. Les chemins sont relatifs à ce dossier.
"""
from playwright.sync_api import sync_playwright
import csv
import pathlib
import statistics as st
import sys

SEQ = pathlib.Path("sequence_4e_C2_hangzhou_borne.html").resolve().as_uri()
QCM = pathlib.Path("qcm_4e_C2_hangzhou_borne.html").resolve().as_uri()
SYE = pathlib.Path("Synthèses/synthese_eleve_4e_C2.1-C2.2.html").resolve().as_uri()
SYP = pathlib.Path("Synthèses/synthese_professeur_4e_C2.1-C2.2.html").resolve().as_uri()

res = []


def t(n, ok, d=""):
    res.append((n, bool(ok)))
    print(("✔" if ok else "✘"), n, d)


PARCOURS = ("1. arriver — gêne — V04\n2. identifier — hésitation — V02\n"
            "3. choisir — partagé — V03 et V09\n4. déverrouiller — agacement — V01\n"
            "5. partir — soulagement — V06")
PARCOURS_SANS_PREUVE = ("1. arriver — gêne\n2. identifier — hésitation\n3. choisir — partagé\n"
                        "4. déverrouiller — agacement\n5. partir — soulagement")
GRAPH = ("arriver : 8 s en moyenne, 14 s au maximum\nidentifier : 14 s et 27 s\n"
         "choisir : 40 s et 62 s\ndéverrouiller : 29 s et 83 s\npartir : 13 s et 23 s\n"
         "Ce que le graphique montre : choisir est la plus longue en moyenne, mais déverrouiller "
         "a le plus grand écart, à cause des 9 reprises.\n"
         "Ce qu'il ne montre pas : le ressenti des usagers.")
ALGO_SANS_ECHEC = ("DÉBUT\nACTION : la borne ouvre l'ancrage\n"
                   "TEST : l'ancrage s'est-il ouvert ? OUI vers la fin, NON vers l'action\n"
                   "TEST : l'usager tire-t-il ? OUI, NON\nREPRISE : retour à l'action précédente")
ALGO = ("DÉBUT — le vélo est choisi\nACTION : la borne ouvre l'ancrage et affiche le temps restant\n"
        "TEST : l'ancrage s'est-il ouvert ? OUI vers la fin, NON vers l'annonce\n"
        "ACTION : la borne annonce ce qui bloque\n"
        "TEST : est-ce la troisième tentative ? NON reprise vers l'action 2, OUI échec\n"
        "FIN échec : proposer un autre vélo et signaler l'ancrage")
EXIG_UNE_FAMILLE = ("La borne doit déverrouiller 98 fois sur 100. Famille : fiabilité. Chen (V01).\n"
                    "La borne doit tomber en panne moins souvent. Famille : fiabilité. Sun (V05).\n"
                    "Le déverrouillage doit aboutir en 5 s. Famille : fiabilité. Feng (V12).\n"
                    "L'ancrage doit s'ouvrir du premier coup. Famille : fiabilité. Chen (V01).")
EXIG = ("La borne doit déverrouiller au moins 98 fois sur 100. Famille : fiabilité. "
        "Répond à Chen (V01).\n"
        "La borne doit afficher le temps restant. Famille : qualité. Répond à Feng (V12).\n"
        "Le retrait doit se faire d'une seule main. Famille : ergonomie. Répond à Deng (V11).\n"
        "L'écran doit rester lisible sous la pluie. Famille : formes et fonctions. "
        "Répond à Zhao (V04).")

# ─────────────────── les données : ce que la séquence affirme ───────────────────
lignes = list(csv.DictReader(open("donnees_parcours_borne_hangzhou_simulees.csv",
                                  encoding="utf-8"), delimiter=";"))
for l in lignes:
    l["duree_s"] = int(l["duree_s"])


def stat(etape):
    d = [l["duree_s"] for l in lignes if l["etape"] == etape]
    return round(st.mean(d)), max(d)


t("données : 30 retraits × 5 étapes", len(lignes) == 150, str(len(lignes)))
t("données : « choisir » est bien la plus longue en moyenne (40 s)",
  stat("choisir")[0] == 40, str(stat("choisir")))
t("données : « déverrouiller » monte bien à 83 s",
  stat("deverrouiller") == (29, 83), str(stat("deverrouiller")))
t("données : 9 reprises sur 30 à l'étape déverrouiller",
  sum(1 for l in lignes if l["etape"] == "deverrouiller"
      and l["reprise_necessaire"] == "oui") == 9)
verbat = list(csv.DictReader(open("verbatims_usagers_hangzhou_simules.csv",
                                  encoding="utf-8"), delimiter=";"))
t("données : 12 verbatims, les 5 étapes représentées",
  len(verbat) == 12 and len({v["etape_concernee"] for v in verbat}) == 5)

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
    # L'exemption avait été écrite pour « https:// » — et l'espace de noms SVG
    # s'écrit « http:// ». La clause suivante le rattrapait donc, et ce contrôle
    # était rouge dès qu'un schéma était dessiné dans la page. On regarde
    # maintenant ce que la page IRAIT CHERCHER : les attributs de chargement, sans
    # les hyperliens, qui eux ont le droit d'être distants (n°40, corrigé le
    # 31/08/2026).
    distantes = pg.eval_on_selector_all(
        "[src], link[href], object[data], iframe[src], use[href]",
        "l=>l.map(e=>e.getAttribute('src')||e.getAttribute('href')||e.getAttribute('data'))"
        ".filter(u=>u && /^(https?:)?\/\//i.test(u))")
    t("séquence : hors ligne, aucune ressource distante (n°40)",
      "fonts.googleapis" not in contenu and not distantes, str(distantes))
    t("séquence : lien d'accueil valide (n°11)",
      pathlib.Path("../../../../index.html").exists())
    t("bandeau de tâches affiché (n°30)", "Séance 1" in pg.inner_text("#tachesBandeau"))

    n_ta = pg.eval_on_selector_all("textarea", "a=>a.length")
    n_et = pg.eval_on_selector_all("details.etayage", "a=>a.length")
    t("chaque zone de rédaction a sa version étayée (n°31)",
      n_ta == 8 and n_et >= n_ta, f"{n_ta} zones / {n_et} étayages")
    t("chaque champ porte une étiquette (n°34)",
      pg.evaluate("[...document.querySelectorAll('select,textarea')].every(e=>!e.id||"
                  "document.querySelector(`label[for=\"${e.id}\"]`)||e.getAttribute('aria-label'))"))
    t("les trois figures sont chargées, alternative longue (n°1)",
      pg.evaluate("[...document.querySelectorAll('.fig img')].length===3 && "
                  "[...document.querySelectorAll('.fig img')].every(i=>i.alt.length>120)"))
    t("le compteur annonce 4 activités (n°39)", "/ 4 activités" in pg.inner_text("#progTxt"))

    # ── règle n°44 : aucun sigle, aucun bouton nu ──
    t("n°44 : aucun badge ni bouton sans infobulle",
      pg.evaluate("[...document.querySelectorAll('.badges .badge, .toolbar .btn')]"
                  ".filter(e=>!e.title).length") == 0)
    t("n°44 : la légende des badges est lisible sans survol",
      pg.is_visible(".legende-badges"))
    t("n°44 : le mode essentiel est expliqué en clair", pg.is_visible("#aide-essentiel"))

    # billet d'entrée
    pg.click('[data-check="0"]')
    pg.wait_for_timeout(120)
    t("billet d'entrée : oriente sans note (n°26)", "aucune note" in pg.inner_text("#fb0"))
    t("billet d'entrée : ne compte pas dans la progression", "0 / 4" in pg.inner_text("#progTxt"))

    # ── règle n°45 : l'entraînement s'ouvre sur ce qui a été fait ──
    t("n°45 : au départ, le bouton vise le parcours complet",
      pg.get_attribute("#lienQcm", "href") == "qcm_4e_C2_hangzhou_borne.html")

    # activité 1
    pg.evaluate("['a1_1','a1_2','a1_3','a1_4','a1_5','a1_6']"
                ".forEach(i=>document.getElementById(i).selectedIndex=1)")
    pg.click('[data-check="1"]')
    pg.wait_for_timeout(120)
    t("activité 1 : le relevé est exigé", "CINQ étapes" in pg.inner_text("#fb1"))
    pg.fill("#a1_parcours", PARCOURS_SANS_PREUVE)
    pg.click('[data-check="1"]')
    pg.wait_for_timeout(120)
    t("activité 1 : un relevé sans code de verbatim est refusé",
      "CINQ étapes" in pg.inner_text("#fb1"))
    pg.fill("#a1_parcours", PARCOURS)
    pg.click('[data-check="1"]')
    pg.wait_for_timeout(120)
    t("activité 1 : validée avec les cinq étapes et leurs preuves",
      "6 / 6" in pg.inner_text("#fb1"))
    t("n°45 : le bouton vise maintenant 4e_C2.1 seul",
      pg.get_attribute("#lienQcm", "href").endswith("#codes=C2.1"),
      pg.get_attribute("#lienQcm", "href"))
    t("n°45 : le bouton annonce 15 questions", "15 questions" in pg.inner_text("#lienQcm"))

    # activité 2
    pg.click("#tab-s2")
    pg.wait_for_timeout(120)
    pg.evaluate("['a2_1','a2_2','a2_3','a2_4'].forEach(i=>document.getElementById(i).selectedIndex=1)")
    pg.click('[data-check="2"]')
    pg.wait_for_timeout(120)
    t("activité 2 : le graphique et sa lecture sont exigés",
      "deux phrases de lecture" in pg.inner_text("#fb2"))
    pg.fill("#a2_graph", GRAPH)
    pg.click('[data-check="2"]')
    pg.wait_for_timeout(120)
    t("activité 2 : validée une fois le graphique relevé et lu",
      "4 / 4" in pg.inner_text("#fb2"))
    t("n°43 : le corrigé du graphique est présent, replié",
      pg.evaluate("!!document.querySelector('details.correction img[src*=\"corrige\"]')")
      and not pg.evaluate("document.querySelector('details.correction img[src*=\"corrige\"]')"
                          ".closest('details').open"))

    # activité 3
    pg.evaluate("['a3_1','a3_2','a3_3','a3_4'].forEach(i=>document.getElementById(i).selectedIndex=1)")
    pg.click('[data-check="3"]')
    pg.wait_for_timeout(120)
    t("activité 3 : l'algorigramme est exigé", "SORTIE D'ÉCHEC" in pg.inner_text("#fb3"))
    pg.fill("#a3_algo", ALGO_SANS_ECHEC)
    pg.click('[data-check="3"]')
    pg.wait_for_timeout(120)
    t("activité 3 : un algorigramme sans sortie d'échec est refusé",
      "SORTIE D'ÉCHEC" in pg.inner_text("#fb3"))
    pg.fill("#a3_algo", ALGO)
    pg.click('[data-check="3"]')
    pg.wait_for_timeout(120)
    t("activité 3 : validée avec deux tests, une reprise et une sortie d'échec",
      "4 / 4" in pg.inner_text("#fb3"))

    # activité 4
    pg.click("#tab-s3")
    pg.wait_for_timeout(120)
    pg.evaluate("['a4_1','a4_2','a4_3','a4_4','a4_5','a4_6']"
                ".forEach(i=>document.getElementById(i).selectedIndex=1)")
    pg.click('[data-check="4"]')
    pg.wait_for_timeout(120)
    t("activité 4 : les exigences sont exigées", "TROIS familles" in pg.inner_text("#fb4"))
    pg.fill("#a4_exig", EXIG_UNE_FAMILLE)
    pg.click('[data-check="4"]')
    pg.wait_for_timeout(120)
    t("activité 4 : quatre exigences d'une seule famille sont refusées",
      "TROIS familles" in pg.inner_text("#fb4"))
    pg.fill("#a4_exig", EXIG)
    pg.click('[data-check="4"]')
    pg.wait_for_timeout(120)
    t("activité 4 : validée avec trois familles et leurs verbatims",
      "6 / 6" in pg.inner_text("#fb4"))
    t("progression complète", "4 / 4" in pg.inner_text("#progTxt"))
    t("n°45 : les deux compétences faites, retour au parcours complet",
      pg.get_attribute("#lienQcm", "href") == "qcm_4e_C2_hangzhou_borne.html")

    # ── règle n°43 : le Bonus a son corrigé ──
    t("n°43 : le bloc Bonus porte un corrigé",
      pg.evaluate("document.querySelectorAll('.approfondissement details.correction').length") == 1)
    # textContent et non inner_text : un <details> replié n'expose que son summary à
    # inner_text, et le corrigé serait déclaré absent alors qu'il est là (quatrième
    # occurrence de ce piège dans ce dépôt — voir le journal du 24/07).
    corrige_bonus = pg.evaluate(
        "document.querySelector('.approfondissement details.correction').textContent")
    t("n°43 : le corrigé du Bonus traite les trois défis",
      "mots exacts" in corrige_bonus and "chronométrages" in corrige_bonus
      and "exigence" in corrige_bonus,
      f"{len(corrige_bonus)} caractères de corrigé")

    # mode essentiel, hypothèse, sauvegarde
    pg.click("#btnEssentiel")
    pg.wait_for_timeout(120)
    t("mode essentiel : actif et annoncé (n°29)",
      pg.get_attribute("#btnEssentiel", "aria-pressed") == "true")
    pg.click("#btnEssentiel")
    pg.click("#tab-s1")
    pg.fill("#hyp1", "je pense que c'est déverrouiller")
    pg.wait_for_timeout(150)
    pg.click("#tab-s3")
    pg.wait_for_timeout(120)
    t("l'hypothèse de départ est rappelée au bilan",
      "je pense que c'est déverrouiller" in pg.inner_text("#rappelHyp"))
    pg.reload()
    pg.wait_for_timeout(400)
    t("sauvegarde locale restaurée après rechargement",
      pg.input_value("#a4_exig").startswith("La borne doit déverrouiller")
      and "4 / 4" in pg.inner_text("#progTxt"))

    corps = pg.content()
    t("bloc « Prêt·e à t'entraîner » présent (n°4)", "Prêt·e à t'entraîner" in corps)
    t("bloc « Bonus » présent (n°4)", "Bonus (facultatif" in corps)
    t("un seul bouton QCM de séquence (n°4)",
      pg.eval_on_selector_all("a.btn.qcm", "a=>a.length") == 1)

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
    t("QCM : 30 questions, 15 par code",
      info["n"] == 30 and info["c21"] == 15 and info["c22"] == 15, str(info["n"]))
    t("QCM : bonnes réponses réparties A/B/C/D",
      max(info["rep"]) - min(info["rep"]) <= 1, str(info["rep"]))
    t("QCM : 5 questions illustrées", info["imgs"] == 5, str(info["imgs"]))
    t("QCM : chaque distracteur porte une réfutation qui explique",
      info["courtes"] == 0 and info["dvide"], f"{info['courtes']} trop courte(s)")
    t("QCM : explication, exemple, erreur classique et à-retenir partout", info["complets"])

    n = pg.evaluate("QUESTIONS.length")
    for i in range(n):
        r = pg.evaluate(f"QUESTIONS[{i}].r")
        pg.click(f".option >> nth={r}")
        pg.click("#btnValider")
        if i < n - 1:
            pg.click("#btnSuiv")
    pg.click("#btnTerminer")
    pg.wait_for_timeout(300)
    t("QCM : les 30 bonnes réponses sont acceptées",
      pg.evaluate("etat.reponses.filter((x,i)=>x===QUESTIONS[i].r).length") == 30)
    bilan = pg.inner_text("body")
    t("QCM : bilan par compétence affiché", "4e_C2.1" in bilan and "4e_C2.2" in bilan)

    # ── règle n°45 côté QCM : l'arrivée ciblée ──
    for ancre, code in (("#codes=C2.1", "C2.1"), ("#codes=C2.2", "C2.2")):
        ctx = b.new_context()
        p2 = ctx.new_page()
        e2 = []
        p2.on("pageerror", lambda e: e2.append(str(e)))
        p2.goto(QCM + ancre)
        p2.wait_for_timeout(350)
        t(f"n°45 : arrivée sur {ancre} → 15 questions du seul {code}",
          p2.is_visible("#porteeCiblee")
          and p2.evaluate("etat.sousListe.length") == 15
          and p2.evaluate(f"etat.sousListe.every(i=>QUESTIONS[i].c==='{code}')")
          and not e2)
        ctx.close()

    ctx = b.new_context()
    p2 = ctx.new_page()
    p2.goto(QCM)
    p2.wait_for_timeout(300)
    t("n°45 : sans ancre, le QCM s'ouvre normalement sur le parcours complet",
      not p2.is_visible("#porteeCiblee"))
    ctx.close()

    # ───────────────────────────── les synthèses ─────────────────────────────
    for nom, uri, figs in (("élève", SYE, 3), ("professeur", SYP, 0)):
        errs.clear()
        pg.goto(uri)
        pg.wait_for_timeout(300)
        t(f"synthèse {nom} : aucune erreur JS", not errs, str(errs))
        t(f"synthèse {nom} : {figs} figure(s) référencée(s)",
          pg.eval_on_selector_all("object", "a=>a.length") == figs)
        t(f"synthèse {nom} : liens de navigation valides",
          all(pathlib.Path("Synthèses").joinpath(h).exists()
              for h in pg.eval_on_selector_all("a", "a=>a.map(e=>e.getAttribute('href'))")))

    b.close()

ko = [n for n, ok in res if not ok]
print(f"\n{len(res) - len(ko)} / {len(res)} tests passés")
if ko:
    print("Échecs :")
    for n in ko:
        print("  -", n)
sys.exit(1 if ko else 0)
