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



def cocher(pg, ident, texte):
    """Coche la proposition dont la valeur est `texte` (règle d'or n°300).

    Remplace `pg.select_option(...)` : depuis la conversion du 20/09/2026, une
    question à choix est un groupe de boutons radio, pas une liste déroulante.
    On vise la VALEUR — le texte exact de la proposition —, jamais la position,
    et Playwright échoue bruyamment si aucune proposition ne correspond : c'est
    la preuve que la conversion n'a pas décalé un texte.
    """
    pg.locator('#%s input[type=radio][value="%s"]' % (ident, texte)).check()

def t(n, ok, d=""):
    res.append((n, bool(ok)))
    print(("✔" if ok else "✘"), n, d)


# L'exercice inséré (atelier « Le diagramme de cas d'utilisation ») : les bonnes réponses sont lues dans sa
# définition, embarquée dans la page — le banc suit l'exercice si son rédacteur le retouche. Seule la réponse
# écrite est donnée ici (l'exemple juste de la définition).
REMPLIR = """([uid, textes]) => {
  const box = document.getElementById(uid);
  const D = JSON.parse(box.closest('.atelier-incruste').querySelector('script[type="application/json"]').textContent).exercices[uid];
  const coche = (name, val) => { const i = box.querySelector(`input[name="${name}"][value="${val}"]`);
    if (!i) throw new Error('option absente : ' + name + ' = ' + val); i.checked = true; i.dispatchEvent(new Event('change', {bubbles: true})); };
  for (const w of D.widgets) {
    if (w.type === 'choix') coche(w.name, w.bonne);
    else if (w.type === 'cases') box.querySelectorAll(`input[name="${w.name}"]`).forEach(i => { i.checked = w.bonnes.includes(i.value); });
    else if (w.type === 'classer') w.items.forEach(it => coche(it.name, it.bonne));
    else if (w.type === 'slots') w.slots.forEach(s => coche(s.name, s.bonnes[0]));
    else { const z = box.querySelector(`textarea[name="${w.name}"]`); z.value = textes[w.name.split('__')[1]]; z.dispatchEvent(new Event('input', {bubbles: true})); }
  }
}"""


def exercice_insere(pg, uid, nom, textes=None):
    """Vérifié à vide (retour 🔴), puis rempli juste (« Tout est juste »)."""
    pg.click(f"#{uid} button.verifier")
    pg.wait_for_timeout(80)
    t(f"{nom} : à vide, le retour demande de reprendre", "🔴" in pg.inner_text(f"#{uid} .retour"))
    pg.evaluate(REMPLIR, [uid, textes or {}])
    pg.click(f"#{uid} button.verifier")
    pg.wait_for_timeout(80)
    t(f"{nom} : rempli juste, il est réussi", "Tout est juste" in pg.inner_text(f"#{uid} .retour"))


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
    t("séquence : lien d'accueil valide (n°11)", pathlib.Path("../../../../index.html").exists())
    t("bandeau de tâches affiché (n°30)", "Séance 1" in pg.inner_text("#tachesBandeau"))
    # Les exercices insérés (atelier des représentations) apportent leurs propres zones : comptées à part.
    n_ta = pg.eval_on_selector_all("textarea:not(.atelier-incruste textarea)", "a=>a.length")
    n_et = pg.eval_on_selector_all("details.etayage:not(.atelier-incruste details)", "a=>a.length")
    t("chaque zone de rédaction a sa version étayée (n°31)",
      n_ta >= 8 and n_et >= n_ta, f"{n_ta} zones / {n_et} étayages")
    i_ta = pg.eval_on_selector_all(".atelier-incruste textarea", "a=>a.length")
    i_et = pg.eval_on_selector_all(".atelier-incruste details.etayage", "a=>a.length")
    t("exercice inséré : chaque zone de rédaction a sa version étayée (n°31)",
      i_ta >= 1 and i_ta == i_et, f"{i_ta} zones / {i_et} étayages")
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
    # n°298 (15/09/2026) remplace, sur la page élève, la légende des étiquettes (n°44, 3e élément)
    # et la carte de référentiel (n°42) : les deux vivent dans la synthèse professeur.
    sp = pathlib.Path("Synthèses/synthese_professeur_3e_C2.1.html").read_text(encoding="utf-8")
    bloc = sp[sp.find("referentiel-eleve"): sp.find("</div>", sp.find("referentiel-eleve"))]
    t("n°298 : la légende des badges a quitté la page élève pour la synthèse professeur",
      pg.locator(".legende-badges").count() == 0 and 'class="legende-badges"' in bloc)

    # n°42, troisième volet : l'ambiguïté de « choisis » est déclarée — dans le référentiel,
    # désormais lu dans la synthèse professeur (n°298)
    t("n°42 : l'ambiguïté de « choisis » est dite, dans le référentiel de la synthèse professeur",
      pg.locator(".referentiel-card").count() == 0
      and "sans dire" in bloc and "peut faire autrement" in bloc)
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
    pg.evaluate("['a1_1','a1_2','a1_3','a1_4'].forEach(i=>{const g=document.getElementById(i);const r=g.querySelector('input[type=radio]');if(!r)throw new Error('aucune proposition dans '+i);r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}));})")
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
                ".forEach(i=>{const g=document.getElementById(i);const r=g.querySelector('input[type=radio]');if(!r)throw new Error('aucune proposition dans '+i);r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}));})")
    pg.fill("#a2_appar", APPAR)
    pg.click('[data-check="2"]')
    pg.wait_for_timeout(120)
    t("activité 2 : sans le vocabulaire, la validation est refusée",
      "mots qu'on ne connaît pas" in pg.inner_text("#fb2"))
    for i, v in VOC.items():
        cocher(pg, i, v)
    pg.click('[data-check="2"]')
    pg.wait_for_timeout(120)
    t("activité 2 : validée une fois le vocabulaire et les appariements tenus",
      "12 / 12" in pg.inner_text("#fb2"))

    # activité 3 — l'ordre, et le message qui le distingue
    pg.evaluate("['a3_1','a3_2','a3_3','a3_4'].forEach(i=>{const g=document.getElementById(i);const r=g.querySelector('input[type=radio]');if(!r)throw new Error('aucune proposition dans '+i);r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}));})")
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
    pg.evaluate("['a4_1','a4_2','a4_3','a4_4'].forEach(i=>{const g=document.getElementById(i);const r=g.querySelector('input[type=radio]');if(!r)throw new Error('aucune proposition dans '+i);r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}));})")
    pg.fill("#a4_prod", DEFENSE_SANS_ECARTE)
    pg.click('[data-check="4"]')
    pg.wait_for_timeout(120)
    t("activité 4 : une défense sans « ce que j'ai écarté » est refusée, et le message le nomme",
      "n'a rien choisi" in pg.inner_text("#fb4"))
    pg.fill("#a4_prod", DEFENSE)
    pg.click('[data-check="4"]')
    pg.wait_for_timeout(120)
    t("activité 4 : l'exercice « Choisir le mode selon la question » est exigé",
      "Choisir le mode selon la question" in pg.inner_text("#fb4")
      and "3 / 4 activités" in pg.inner_text("#progTxt"), pg.inner_text("#fb4")[-90:])
    # l'exercice inséré en tête de l'activité 4 (atelier « Le diagramme de cas d'utilisation », 3e)
    exercice_insere(pg, "cu_3e_e6", "activité 4 : choisir le mode selon la question",
                    {"justif": "Le diagramme de cas d'utilisation dit qui fait quoi, mais il ne montre ni l'ordre des "
                               "étapes ni le test « si la carte est refusée » : c'est l'algorigramme qui le montre."})
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
    for nom, uri, figs in (("élève", SYE, 0), ("professeur", SYP, 0)):   # n°316 révisée (29/10/2026) : deux pages A4, les grands schémas <object> restent dans la séquence
        errs.clear()
        pg.goto(uri)
        pg.wait_for_timeout(300)
        t(f"synthèse {nom} : aucune erreur JS", not errs, str(errs))
        t(f"synthèse {nom} : {figs} figure(s) référencée(s)",
          pg.eval_on_selector_all("object", "a=>a.length") == figs)
        t(f"synthèse {nom} : liens de navigation valides",
          all(pathlib.Path("Synthèses").joinpath(h.split("#")[0]).exists()
              for h in pg.eval_on_selector_all("a", "a=>a.map(e=>e.getAttribute('href'))")
              if not h.startswith("#")))   # n°316 : la carte renvoie aux parties de la page (#partie-N)
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
