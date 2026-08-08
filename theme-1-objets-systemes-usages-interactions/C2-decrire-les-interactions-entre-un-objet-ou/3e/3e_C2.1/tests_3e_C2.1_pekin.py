#!/usr/bin/env python3
"""Suite de tests du lot Pékin 3e_C2.1.

    python3 tests_3e_C2.1_pekin.py

À lancer depuis le dossier du lot. Les chemins sont relatifs à ce dossier.
"""
from playwright.sync_api import sync_playwright
import csv
import glob
import pathlib
import statistics as st
import sys

SEQ = pathlib.Path("sequence_3e_C2_pekin_borne.html").resolve().as_uri()
QCM = pathlib.Path("qcm_3e_C2_pekin_borne.html").resolve().as_uri()
SYE = pathlib.Path("Synthèses/synthese_eleve_3e_C2.1.html").resolve().as_uri()
SYP = pathlib.Path("Synthèses/synthese_professeur_3e_C2.1.html").resolve().as_uri()

res = []


def t(n, ok, d=""):
    res.append((n, bool(ok)))
    print(("✔" if ok else "✘"), n, d)


LECTURE = ("habitués : 0 % (0 sur 14)\noccasionnels : 11 %\navec poussette : 25 %\n"
           "touristes : 43 %\npersonnes âgées : 50 %\n"
           "Le chiffre global cachait qu'aucun habitué n'abandonne, alors qu'une personne âgée "
           "sur deux renonce.")
LECTURE_SANS_EXTREMES = ("habitués : 5 %\noccasionnels : 11 %\navec poussette : 25 %\n"
                         "touristes : 43 %\npersonnes âgées : 30 %\n"
                         "Le chiffre global cachait que ça dépend beaucoup des profils observés.")
VOC = {"a2_v1": "un storyboard", "a2_v2": "une carte d'empathie", "a2_v3": "un algorigramme",
       "a2_v4": "un parcours utilisateur", "a2_v5": "un tableau comparatif", "a2_v6": "un graphique"}
APPAR = ("Pour le technicien, l'algorigramme : il rend les cas d'échec traitables. Son angle mort, "
         "être illisible pour un non-technicien, ne le gêne pas.\n"
         "Pour l'élue, le graphique : il chiffre en un coup d'oeil. Son angle mort, ne rien dire "
         "du vécu, ne la gêne pas car elle vote un budget.\n"
         "Pour l'usager, le storyboard : il se comprend sans mode d'emploi. Son angle mort, tenir "
         "peu de choses, ne le gêne pas, il a trois secondes.")
ALGO_ORDRE_INVERSE = ("DÉBUT\nACTION : la borne encaisse le paiement\n"
                      "TEST : le paiement a-t-il abouti ? NON : restituer\n"
                      "TEST : reste-t-il plus de 8 % de papier ? NON : indisponible, alerter la "
                      "maintenance, FIN échec\nACTION : imprimer le titre\nFIN réussite")
ALGO = ("DÉBUT — l'usager a choisi son titre\n"
        "TEST : reste-t-il plus de 8 % de papier ? NON : afficher indisponible, alerter la "
        "maintenance, FIN échec\nACTION : la borne encaisse le paiement\n"
        "TEST : le paiement a-t-il abouti ? NON : restituer\nACTION : imprimer le titre\n"
        "FIN réussite : l'usager prend son titre")
DEFENSE_SANS_ECARTE = ("J'ai produit pour l'élue. J'ai choisi le graphique parce qu'il chiffre "
                       "vite et qu'elle vote un budget en quelques minutes seulement, ce qui lui "
                       "permet de décider sans lire une longue explication technique.")
DEFENSE = DEFENSE_SANS_ECARTE + ("\nJ'ai laissé de côté la cause des abandons : elle ne la "
                                 "corrigera pas elle-même.")

# ─────────────── les données : ce que la séquence et les corrigés affirment ───────────────
obs = list(csv.DictReader(open("observations_borne_pekin_simulees.csv", encoding="utf-8"),
                          delimiter=";"))
for o in obs:
    o["duree_totale_s"] = int(o["duree_totale_s"])


def taux(profil):
    sub = [o for o in obs if o["profil"] == profil]
    return round(sum(1 for o in sub if o["abandon"] == "oui") / len(sub) * 100)


t("données : 40 observations", len(obs) == 40, str(len(obs)))
t("données : 8 abandons, soit 20 % — « un sur cinq »",
  sum(1 for o in obs if o["abandon"] == "oui") == 8)
t("données : aucun habitué n'abandonne (0 %)", taux("habitue") == 0, str(taux("habitue")))
t("données : touristes 43 %, personnes âgées 50 %",
  taux("touriste") == 43 and taux("personne_agee") == 50,
  f"{taux('touriste')} / {taux('personne_agee')}")
t("données : durée moyenne 77 s, habitué 41 s, personne âgée 123 s",
  round(st.mean([o["duree_totale_s"] for o in obs])) == 77
  and round(st.mean([o["duree_totale_s"] for o in obs if o["profil"] == "habitue"])) == 41
  and round(st.mean([o["duree_totale_s"] for o in obs if o["profil"] == "personne_agee"])) == 123)
verb = list(csv.DictReader(open("verbatims_usagers_pekin_simules.csv", encoding="utf-8"),
                           delimiter=";"))
inc = list(csv.DictReader(open("incidents_maintenance_pekin_simules.csv", encoding="utf-8"),
                          delimiter=";"))
t("données : 8 verbatims et 3 incidents", len(verb) == 8 and len(inc) == 3)

# ── règle n°43 précisée : les SIX modes ont chacun leur corrigé ──
corriges = " ".join(open(f, encoding="utf-8").read().lower()
                    for f in glob.glob("Images/corrige_*.svg"))
manquants = [m for m in ("parcours", "algorigramme", "graphique", "empathie",
                         "storyboard", "tableau comparatif") if m not in corriges]
t("n°43 : les six modes offerts ont tous leur corrigé", not manquants, str(manquants))

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
    t("séquence : lien d'accueil valide (n°11)", pathlib.Path("../../../../index.html").exists())
    t("bandeau de tâches affiché (n°30)", "Séance 1" in pg.inner_text("#tachesBandeau"))
    n_ta = pg.eval_on_selector_all("textarea", "a=>a.length")
    n_et = pg.eval_on_selector_all("details.etayage", "a=>a.length")
    t("chaque zone de rédaction a sa version étayée (n°31)",
      n_ta == 8 and n_et >= n_ta, f"{n_ta} zones / {n_et} étayages")
    t("chaque champ porte une étiquette (n°34)",
      pg.evaluate("[...document.querySelectorAll('select,textarea')].every(e=>!e.id||"
                  "document.querySelector(`label[for=\"${e.id}\"]`)||e.getAttribute('aria-label'))"))
    t("les figures sont chargées, alternative longue (n°1)",
      pg.evaluate("[...document.querySelectorAll('.fig img')].every(i=>i.alt.length>120)"))
    t("le compteur annonce 4 activités (n°39)", "/ 4 activités" in pg.inner_text("#progTxt"))

    # n°44
    t("n°44 : aucun badge ni bouton sans infobulle",
      pg.evaluate("[...document.querySelectorAll('.badges .badge, .toolbar .btn')]"
                  ".filter(e=>!e.title).length") == 0)
    t("n°44 : la légende des badges est lisible sans survol", pg.is_visible(".legende-badges"))

    # n°42, troisième volet : l'ambiguïté de « choisis » est déclarée à l'élève
    t("n°42 : l'ambiguïté de « choisis » est dite à l'élève",
      "sans dire" in pg.inner_text(".referentiel-card")
      and "peut faire autrement" in pg.inner_text(".referentiel-card"))
    t("la marche du C2 sur trois niveaux est écrite à l'élève",
      "Shenzhen" in contenu and "Hangzhou" in contenu and "compétence C2" in contenu)

    pg.click('[data-check="0"]')
    pg.wait_for_timeout(120)
    t("billet d'entrée : oriente sans note (n°26)", "aucune note" in pg.inner_text("#fb0"))

    # n°45, version mono-code
    t("n°45 : au départ, le bouton propose le parcours court",
      "10 questions" in pg.inner_text("#lienQcm")
      and pg.get_attribute("#lienQcm", "href").endswith("#depart=court"))

    # activité 1
    pg.evaluate("['a1_1','a1_2','a1_3','a1_4'].forEach(i=>document.getElementById(i).selectedIndex=1)")
    pg.click('[data-check="1"]')
    pg.wait_for_timeout(120)
    t("activité 1 : la lecture par profil est exigée", "CINQ profils" in pg.inner_text("#fb1"))
    pg.fill("#a1_lecture", LECTURE_SANS_EXTREMES)
    pg.click('[data-check="1"]')
    pg.wait_for_timeout(120)
    t("activité 1 : une lecture qui ne nomme pas les extrêmes est refusée",
      "CINQ profils" in pg.inner_text("#fb1"))
    pg.fill("#a1_lecture", LECTURE)
    pg.click('[data-check="1"]')
    pg.wait_for_timeout(120)
    t("activité 1 : validée avec les cinq taux et les deux extrêmes",
      "4 / 4" in pg.inner_text("#fb1"))

    # activité 2 — le vocabulaire d'abord
    pg.click("#tab-s2")
    pg.wait_for_timeout(120)
    pg.evaluate("['a2_1','a2_2','a2_3','a2_4','a2_5','a2_6']"
                ".forEach(i=>document.getElementById(i).selectedIndex=1)")
    pg.fill("#a2_appar", APPAR)
    pg.click('[data-check="2"]')
    pg.wait_for_timeout(120)
    t("activité 2 : sans le vocabulaire, la validation est refusée",
      "mots qu'on ne connaît pas" in pg.inner_text("#fb2"))
    for i, v in VOC.items():
        pg.select_option("#" + i, label=v)
    pg.click('[data-check="2"]')
    pg.wait_for_timeout(120)
    t("activité 2 : validée une fois le vocabulaire et les appariements tenus",
      "12 / 12" in pg.inner_text("#fb2"))

    # activité 3 — l'ordre, et le message qui le distingue
    pg.evaluate("['a3_1','a3_2','a3_3','a3_4'].forEach(i=>document.getElementById(i).selectedIndex=1)")
    pg.fill("#a3_algo", ALGO_ORDRE_INVERSE)
    pg.click('[data-check="3"]')
    pg.wait_for_timeout(120)
    t("activité 3 : quand SEUL l'ordre est faux, le message le dit précisément",
      "sauf l'essentiel" in pg.inner_text("#fb3"), pg.inner_text("#fb3")[-60:])
    pg.fill("#a3_algo", ALGO)
    pg.click('[data-check="3"]')
    pg.wait_for_timeout(120)
    t("activité 3 : validée quand le test du papier précède l'encaissement",
      "4 / 4" in pg.inner_text("#fb3"))

    # activité 4 — la défense, et le troisième point
    pg.click("#tab-s3")
    pg.wait_for_timeout(120)
    pg.evaluate("['a4_1','a4_2','a4_3','a4_4'].forEach(i=>document.getElementById(i).selectedIndex=1)")
    pg.fill("#a4_prod", DEFENSE_SANS_ECARTE)
    pg.click('[data-check="4"]')
    pg.wait_for_timeout(120)
    t("activité 4 : une défense sans « ce que j'ai écarté » est refusée, et le message le nomme",
      "n'a rien choisi" in pg.inner_text("#fb4"))
    pg.fill("#a4_prod", DEFENSE)
    pg.click('[data-check="4"]')
    pg.wait_for_timeout(120)
    t("activité 4 : validée avec les trois points", "4 / 4" in pg.inner_text("#fb4"))
    t("progression complète", "4 / 4 activités" in pg.inner_text("#progTxt"))
    t("n°45 : la séquence terminée, le bouton ouvre le parcours complet",
      pg.get_attribute("#lienQcm", "href") == "qcm_3e_C2_pekin_borne.html")

    # n°43 : les corrigés sont là, et repliés
    t("n°43 : les deux planches de corrigé sont dans des blocs repliés",
      pg.evaluate("[...document.querySelectorAll('details.correction img[src*=\"corrige\"]')]"
                  ".every(i=>!i.closest('details').open)")
      and pg.evaluate("document.querySelectorAll('details.correction img[src*=\"corrige\"]').length") >= 3)
    corrige_bonus = pg.evaluate(
        "document.querySelector('.approfondissement details.correction').textContent")
    t("n°43 : le Bonus a son corrigé, et il traite les trois défis",
      "portail" in corrige_bonus and "storyboard" in corrige_bonus
      and "cas d'échec" in corrige_bonus, f"{len(corrige_bonus)} caractères")

    pg.reload()
    pg.wait_for_timeout(400)
    t("sauvegarde locale restaurée après rechargement",
      pg.input_value("#a4_prod").startswith("J'ai produit pour l'élue")
      and "4 / 4 activités" in pg.inner_text("#progTxt"))
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
        complets: QUESTIONS.every(q=>q.expl&&q.ex&&q.err&&q.ret&&q.o.length===4&&q.d.length===4)
    })""")
    t("QCM : 30 questions", info["n"] == 30, str(info["n"]))
    t("QCM : bonnes réponses réparties A/B/C/D",
      max(info["rep"]) - min(info["rep"]) <= 1, str(info["rep"]))
    t("QCM : 5 questions illustrées", info["imgs"] == 5, str(info["imgs"]))
    t("QCM : chaque distracteur porte une réfutation qui explique",
      info["courtes"] == 0 and info["dvide"], f"{info['courtes']} trop courte(s)")
    t("QCM : explication, exemple, erreur classique et à-retenir partout", info["complets"])
    t("QCM : la question « lequel est le meilleur » a pour réponse « aucun »",
      pg.evaluate("(()=>{const q=QUESTIONS.find(q=>q.n==='Aucun n\\'est meilleur');"
                  "return q && q.o[q.r].startsWith('aucun');})()"))

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
    t("QCM : bilan par compétence affiché", "3e_C2.1" in pg.inner_text("body"))

    for ancre, attendu, lab in (("#depart=court", 10, "parcours court"), ("", None, "sans ancre")):
        ctx = b.new_context()
        p2 = ctx.new_page()
        e2 = []
        p2.on("pageerror", lambda e: e2.append(str(e)))
        p2.goto(QCM + ancre)
        p2.wait_for_timeout(350)
        sl = p2.evaluate("etat.sousListe ? etat.sousListe.length : null")
        t(f"n°45 : arrivée « {lab} » → {attendu if attendu else 'parcours complet'}",
          sl == attendu and p2.is_visible("#porteeCiblee") == bool(attendu) and not e2, str(sl))
        ctx.close()

    # ───────────────────────────── les synthèses ─────────────────────────────
    for nom, uri, figs in (("élève", SYE, 2), ("professeur", SYP, 0)):
        errs.clear()
        pg.goto(uri)
        pg.wait_for_timeout(300)
        t(f"synthèse {nom} : aucune erreur JS", not errs, str(errs))
        t(f"synthèse {nom} : {figs} figure(s) référencée(s)",
          pg.eval_on_selector_all("object", "a=>a.length") == figs)
        t(f"synthèse {nom} : liens de navigation valides",
          all(pathlib.Path("Synthèses").joinpath(h).exists()
              for h in pg.eval_on_selector_all("a", "a=>a.map(e=>e.getAttribute('href'))")))
    t("synthèse professeur : les deux variantes d'usage y sont écrites",
      "Variante A" in pg.content() and "Variante B" in pg.content())

    b.close()

ko = [n for n, ok in res if not ok]
print(f"\n{len(res) - len(ko)} / {len(res)} tests passés")
if ko:
    print("Échecs :")
    for n in ko:
        print("  -", n)
sys.exit(1 if ko else 0)
