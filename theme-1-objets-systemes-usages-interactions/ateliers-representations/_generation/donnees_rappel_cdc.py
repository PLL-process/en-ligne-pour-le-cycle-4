# -*- coding: utf-8 -*-
"""La piqûre de rappel du cahier des charges : un petit exercice intégré, posé dans chaque séquence de 4e et de 3e qui
se sert d'un cahier des charges, au moment où il revient (demande du professeur du 04/11/2026 : « C'est dans toutes ces
séquences que l'on devrait faire cette piqûre de rappel », « Sous forme d'exercices intégrés aussi »).

Une seule source : ce fichier décrit chaque rappel (son objet, ses lignes) ; `moteur.rappel_cdc` le dessine avec le
widget « tableau » (règle n°317 : le cahier des charges se complète dans le tableau, par menus, avec des pièges et un
retour par option) ; `incrustations.py` le pose dans les séquences (lot `incrustations_lots/rappel_cahier_des_charges.py`)
et `moteur.page_atelier` en tête des ateliers « Le diagramme des exigences » de 4e et de 3e.

Les mots de référence sont ceux de la leçon de 4e (atelier « Le diagramme des interacteurs extérieurs », exercice 6, et
son cours « Le cahier des charges fonctionnel », « Critère, niveau, flexibilité ») : ils font foi.

Un rappel : `id`, `niveau`, `sequence` (chemin depuis la racine du dépôt) et `avant` (la phrase repère, unique), ou
`atelier` (slug, niveau) ; `balise`, `balise_exo` ; `objet` (« la borne de vélos ») ; `pourquoi` (la phrase qui relie le
rappel à la séquence) ; `client` (qui répond « Et si on n'atteint pas tout à fait ce niveau ? ») ; `lignes`, faites par
`ligne()`. Une ligne : cinq cases (Fonction, Désignation, Critère, Niveau, Flexibilité), chacune un menu à pièges ; la
désignation peut être donnée (une chaîne). Chaque option fausse a son retour (✘ et pourquoi), tiré des données de la
ligne ; la correction reprend chaque attendu, puis réfute chaque piège avec le même retour.
"""
import zlib

SLUG = "rappel-cdc"
COURT = "rc"
EMOJI = "🔁"
TITRE = "Piqûre de rappel&nbsp;: le cahier des charges"
CODE = "4e_C2.2"

#: (chemin depuis le dossier des ateliers, ancre, emoji, texte du lien)
LECON = ("interacteurs-pieuvre/atelier_4e_interacteurs-pieuvre.html", "#pv_4e_e6", "🐙",
         "l'atelier de 4e «&nbsp;Le diagramme des interacteurs extérieurs&nbsp;», exercice 6, «&nbsp;Le cahier des charges&nbsp;: "
         "critère, niveau, flexibilité&nbsp;», et son cours")

#: Les mots de référence (leçon de 4e), dans l'ordre des colonnes du tableau.
MOTS_REFERENCE = [
    ("fonction principale (FP)", "elle relie deux interacteurs <b>en passant par l'objet</b>&nbsp;: c'est le service rendu."),
    ("fonction contrainte (FC)", "elle relie l'objet à <b>un seul</b> interacteur&nbsp;: c'est une condition à respecter."),
    ("désignation", "la phrase de la fonction&nbsp;: elle commence par un <b>verbe à l'infinitif</b> («&nbsp;résister à la "
                    "pluie&nbsp;»)."),
    ("critère (on dit aussi critère d'appréciation)", "ce que l'on <b>mesure</b> ou contrôle pour savoir si la fonction est remplie."),
    ("niveau", "la <b>valeur à atteindre</b> pour ce critère (au moins…, au plus…), avec son <b>unité</b>."),
    ("flexibilité", "l'<b>écart que le client accepte</b> autour du niveau&nbsp;: <b>F0</b> impératif · <b>F1</b> peu "
                    "négociable · <b>F2</b> négociable · <b>F3</b> très négociable."),
]

COLONNES = ["Fonction", "Désignation", "Critère", "Niveau", "Flexibilité"]
MENUS = {"fonction": [("fp", "FP"), ("fc", "FC")],
         "flex": [("f0", "F0 — impératif"), ("f1", "F1 — peu négociable"), ("f2", "F2 — négociable"),
                  ("f3", "F3 — très négociable")]}
NOM_FLEX = {"f0": "F0, impératif", "f1": "F1, peu négociable", "f2": "F2, négociable", "f3": "F3, très négociable"}


def _ordre(nom, col, options):
    """Les options d'un menu à pièges, mélangées une fois pour toutes (la bonne n'est pas toujours la première)."""
    k = zlib.crc32(("%s|%s" % (nom, col)).encode("utf-8")) % len(options)
    return options[k:] + options[:k]


def de(objet):
    """« le bac » → « du bac », « la station » → « de la station », « l'arrosage » → « de l'arrosage »."""
    if objet.startswith("le "):
        return "du " + objet[3:]
    if objet.startswith("les "):
        return "des " + objet[4:]
    return "de " + objet


def _sans_html(t):
    import html
    import re
    return html.unescape(re.sub(r"<[^>]+>", "", t))


def ligne(nom, court, fonction, interacteurs, designation, critere, niveau, flex):
    """Une ligne du cahier des charges, ses menus, leurs retours, et ses lignes de correction.

    fonction     "fp" ou "fc" ; interacteurs : le texte entre parenthèses («&nbsp;l'usager → le vélo&nbsp;»)
    designation  une chaîne (case donnée), ou dict(bon=, nom=(texte, le nom, le verbe), sujet=(texte, le sujet),
                 solution=(texte, ce qu'elle dit))
    critere      dict(bon=, pourquoi=, niveau=texte (un niveau pris pour un critère), solution=(texte, ce qu'elle dit),
                 autre=(texte, retour))
    niveau       dict(bon=, sans_unite=(texte, retour), unite=(texte, retour), vague=texte)
    flex         dict(bonne="f0".."f3", cit=paroles du client, ecart=, condition=, securite=bool)
    """
    retours_menus = {}
    # ── Fonction
    if fonction == "fp":
        r_fct = {"fc": "Deux interacteurs, %s, reliés en passant par l'objet : c'est la FP, le service rendu, pas une "
                       "condition." % _sans_html(interacteurs)}
        pourquoi_fct = "deux interacteurs reliés <b>en passant par l'objet</b> → le service rendu → <b>FP</b>"
    else:
        r_fct = {"fp": "Un seul interacteur, %s : c'est une FC, une condition à respecter. La FP relie deux interacteurs "
                       "en passant par l'objet." % _sans_html(interacteurs)}
        pourquoi_fct = "<b>un seul</b> interacteur → une condition à respecter → <b>FC</b>"
    c_fct = dict(menu="fonction", bonne=fonction, apres="(%s)" % interacteurs, retours=r_fct)
    retours_menus["Fonction"] = (fonction.upper(), pourquoi_fct, [("FC" if fonction == "fp" else "FP", list(r_fct.values())[0])])
    # ── Désignation
    if isinstance(designation, str):
        c_des = designation
        des_txt = _sans_html(designation)
    else:
        d = designation
        des_txt = d["bon"]
        r_des = {"nom": "« %s » est un nom : une fonction commence par un verbe à l'infinitif, « %s »." % (d["nom"][1], d["nom"][2]),
                 "sujet": "Cette phrase a un sujet, « %s », et un verbe conjugué : une fonction commence directement par son "
                          "verbe à l'infinitif." % d["sujet"][1],
                 "solution": "C'est une solution, pas une fonction : %s. La fonction dit ce que l'objet doit faire." % d["solution"][1]}
        opts = _ordre(nom, "des", [("bon", d["bon"]), ("nom", d["nom"][0]), ("sujet", d["sujet"][0]), ("solution", d["solution"][0])])
        c_des = dict(options=opts, bonne="bon", retours=r_des)
        retours_menus["Désignation"] = (
            "« %s »" % d["bon"], "elle commence par le verbe à l'infinitif «&nbsp;%s&nbsp;»" % d["bon"].split()[0].lower(),
            [("« %s »" % d[k][0], r_des[k]) for k in ("nom", "sujet", "solution")])
    # ── Critère
    c = critere
    r_cri = {"niveau": "« %s » est un niveau, la valeur à atteindre. Le critère est ce qu'on mesure ; ici : %s."
                       % (c["niveau"], c["bon"][0].lower() + c["bon"][1:]),
             "solution": "« %s » est une solution : %s. Le critère dit ce qu'on mesure, pas avec quoi on y arrive."
                         % (c["solution"][0], c["solution"][1]),
             "autre": c["autre"][1]}
    opts = _ordre(nom, "cri", [("bon", c["bon"]), ("niveau", c["niveau"]), ("solution", c["solution"][0]), ("autre", c["autre"][0])])
    c_cri = dict(options=opts, bonne="bon", retours=r_cri)
    retours_menus["Critère"] = (c["bon"], c["pourquoi"],
                                [("« %s »" % c["niveau"], r_cri["niveau"]), ("« %s »" % c["solution"][0], r_cri["solution"]),
                                 ("« %s »" % c["autre"][0], r_cri["autre"])])
    # ── Niveau
    n = niveau
    r_niv = {"sans_unite": "Un nombre sans unité n'est pas un niveau : %s" % n["sans_unite"][1],
             "unite": n["unite"][1],
             "vague": "« %s » ne se mesure pas : un niveau, c'est un nombre et son unité." % n["vague"]}
    opts = _ordre(nom, "niv", [("bon", n["bon"]), ("sans_unite", n["sans_unite"][0]), ("unite", n["unite"][0]), ("vague", n["vague"])])
    c_niv = dict(options=opts, bonne="bon", retours=r_niv)
    retours_menus["Niveau"] = (n["bon"], "un nombre et l'unité de son critère",
                               [("« %s »" % n["sans_unite"][0], r_niv["sans_unite"]), ("« %s »" % n["unite"][0], r_niv["unite"]),
                                ("« %s »" % n["vague"], r_niv["vague"])])
    # ── Flexibilité
    f = flex
    b, cit, ecart, cond = f["bonne"], f["cit"], f.get("ecart", ""), f.get("condition", "")
    tables = {
        "f0": {"f1": "« %s » : aucun écart, même à une condition. Le niveau est impératif : F0." % cit,
               "f2": "« %s » : aucun écart n'est accepté ; « négociable » voudrait dire un petit écart sans condition." % cit,
               "f3": ("« %s » : la sécurité des personnes ne se négocie pas ; F3 voudrait dire « n'importe quelle valeur me va »."
                      if f.get("securite") else
                      "« %s » : rien n'est négociable ici ; F3 voudrait dire « n'importe quelle valeur me va ».") % cit},
        "f1": {"f0": "Un écart est accepté (%s) : ce n'est pas impératif." % ecart,
               "f2": "L'écart n'est accepté qu'à une condition (%s) : c'est peu négociable, F1." % cond,
               "f3": "Un petit écart, et à une condition (%s) : ce n'est pas « très négociable »." % cond},
        "f2": {"f0": "Un écart est accepté (%s) : ce n'est pas impératif." % ecart,
               "f1": "L'écart est accepté sans condition : c'est négociable, F2, pas « peu négociable »." ,
               "f3": "L'écart accepté est petit (%s) : ce n'est pas « très négociable »." % ecart},
        "f3": {"f0": "Un écart est accepté (%s) : ce n'est pas impératif." % ecart,
               "f1": "L'écart est accepté sans condition : ce n'est pas « peu négociable »." ,
               "f2": "L'écart accepté est large (%s), et sans condition : c'est très négociable, F3." % ecart},
    }
    r_flx = tables[b]
    c_flx = dict(menu="flex", bonne=b, retours=r_flx)
    raison = {"f0": "aucun écart accepté", "f1": "un écart (%s) accepté à une seule condition (%s)" % (ecart, cond),
              "f2": "un petit écart (%s), sans condition" % ecart, "f3": "un écart large (%s), sans condition" % ecart}[b]
    retours_menus["Flexibilité"] = (NOM_FLEX[b], "«&nbsp;%s&nbsp;» → %s" % (cit, raison),
                                    [(NOM_FLEX[k].split(",")[0], v) for k, v in sorted(r_flx.items())])
    return dict(nom=nom, court=court, cit=cit, cases=[c_fct, c_des, c_cri, c_niv, c_flx], interacteurs=interacteurs,
                fonction=fonction, designation=des_txt, critere=c["bon"], niveau=n["bon"], flex=b, corr=retours_menus,
                donnee=isinstance(designation, str))


def _correction(r):
    out = []
    for L in r["lignes"]:
        # 10/11/2026 (révision des trois thèmes, skill texte-clair-et-aere) : une idée par ligne — la ligne du tableau
        # en cinq lignes, chaque piège sur la sienne
        out.append("<b>%s</b> → %s (%s) <br>«&nbsp;%s&nbsp;» <br>critère&nbsp;: %s <br>niveau&nbsp;: %s <br>%s"
                   % (L["nom"], L["fonction"].upper(), L["interacteurs"], L["designation"], L["critere"], L["niveau"],
                      NOM_FLEX[L["flex"]]))
        for col in COLONNES:
            if col not in L["corr"]:
                continue
            bon, pourquoi, pieges = L["corr"][col]
            out.append("<b>%s</b> → %s&nbsp;: %s. <br>Les pièges&nbsp;: <br>%s"
                       % (col, bon, pourquoi, "&nbsp;; <br>".join((t if t.startswith(p) else "%s → %s" % (p, t)).rstrip(".")
                                                        for p, t in pieges) + "."))
    out.append(("conclusion", "Chaque ligne du cahier des charges a sa <b>fonction</b> (FP ou FC), sa <b>désignation</b> (un verbe "
                              "à l'infinitif), son <b>critère</b> (ce qu'on mesure), son <b>niveau</b> (un nombre et son unité) "
                              "et sa <b>flexibilité</b> (l'écart que le client accepte, de F0 impératif à F3 très négociable)."))
    return out


def exercice(r):
    """L'exercice du rappel, dans la forme des exercices des ateliers (moteur.exercice)."""
    lignes = r["lignes"]
    nb = sum(1 for L in lignes for c in L["cases"] if isinstance(c, dict))
    une = len(lignes) == 1
    paroles = "".join("<li><b>%s</b>&nbsp;: «&nbsp;%s&nbsp;»</li>" % (L["court"], L["cit"]) for L in lignes)
    consigne = ["<p><b>Complète %s du cahier des charges %s, directement dans le tableau</b>&nbsp;: chaque case à menu "
                "attend une réponse.</p><ul>" % ("cette ligne" if une else "ces deux lignes", de(r["objet"])),
                "<li><b>Fonction</b>&nbsp;: FP ou FC&nbsp;? Compte les interacteurs écrits dans la case.</li>"]
    if any(not L["donnee"] for L in lignes):
        consigne.append("<li><b>Désignation</b>&nbsp;: la phrase qui commence par un <b>verbe à l'infinitif</b> — ni un nom, ni "
                        "une phrase avec un sujet, ni une solution.</li>")
    consigne.append("<li><b>Critère</b>&nbsp;: ce qu'on mesure — ni la valeur à atteindre, ni une solution.</li>"
                    "<li><b>Niveau</b>&nbsp;: un nombre et l'unité de son critère.</li>"
                    "<li><b>Flexibilité</b>&nbsp;: d'après ce que répond %s, juste au-dessus du tableau.</li></ul>" % r["client"])
    return dict(
        id=r["id"], titre=r["titre"], code=CODE, duree=3 if une else 5,
        objectif="retrouver, sur %s, ce que dit chaque case d'une ligne du cahier des charges&nbsp;: la fonction (FP ou FC), "
                 "sa désignation, son critère, son niveau et sa flexibilité." % r["objet"],
        production="%s du cahier des charges complétée%s (%d cases)." % ("une ligne" if une else "deux lignes", "" if une else "s", nb),
        mots=[("verbe à l'infinitif", "la forme du verbe qu'on trouve dans le dictionnaire, sans conjugaison&nbsp;: résister, "
               "permettre, prendre, être."),
              ("solution technique", "le moyen concret choisi pour remplir une fonction&nbsp;: elle dit <b>avec quoi</b>&nbsp;; la "
               "fonction dit <b>ce que</b> l'objet doit faire."),
              ("interacteur", "un élément extérieur à l'objet, qui agit sur lui ou sur lequel il agit (une personne, la pluie, "
               "un autre objet…).")],
        consigne="".join(consigne),
        critere="les %d cases justes, et tu sais dire pourquoi chaque piège ne va pas." % nb,
        widgets=[dict(type="tableau", name="cdcf",
                      intro="<p><b>Ce que répond %s</b> à la question «&nbsp;Et si on n'atteint pas tout à fait ce "
                            "niveau&nbsp;?&nbsp;»</p><ul class=\"paroles\">%s</ul>" % (r["client"], paroles),
                      legende="Le cahier des charges %s — %s à compléter (entre parenthèses&nbsp;: l'interacteur que la "
                              "fonction concerne)" % (de(r["objet"]), "une ligne" if une else "deux lignes"),
                      colonnes=COLONNES, largeurs=[14, 27, 22, 19, 18], menus=MENUS,
                      lignes=[dict(nom=L["nom"], cases=L["cases"]) for L in lignes])],
        aides=["<p>Remplis le tableau <b>colonne par colonne</b>. Pour chaque case, relis la définition du mot, juste au-dessus, "
               "dans «&nbsp;Les mots du cahier des charges&nbsp;».</p>",
               "<ul><li><b>Fonction</b>&nbsp;: deux interacteurs reliés en passant par l'objet → FP&nbsp;; un seul → FC.</li>"
               "<li><b>Désignation</b>&nbsp;: le premier mot est un verbe à l'infinitif (permettre, résister, être…).</li>"
               "<li><b>Critère</b>&nbsp;: demande-toi «&nbsp;qu'est-ce que je mesurerais&nbsp;?&nbsp;». Une valeur avec «&nbsp;au "
               "moins&nbsp;» ou «&nbsp;au plus&nbsp;» est un niveau, pas un critère.</li>"
               "<li><b>Niveau</b>&nbsp;: un nombre <b>et</b> l'unité du critère&nbsp;: un temps → des secondes ou des "
               "minutes&nbsp;; une température → des degrés Celsius.</li>"
               "<li><b>Flexibilité</b>&nbsp;: aucun écart → F0&nbsp;; un écart à une condition → F1&nbsp;; un petit écart sans "
               "condition → F2&nbsp;; un écart large → F3. Elle ne dit pas l'importance de la fonction.</li></ul>"],
        correction=_correction(r),
        retenir="chaque fonction du cahier des charges (FP ou FC) a une <b>désignation</b> qui commence par un <b>verbe à "
                "l'infinitif</b>, un <b>critère</b> (ce qu'on mesure), un <b>niveau</b> (un nombre et son unité) et une "
                "<b>flexibilité</b> (l'écart que le client accepte, de <b>F0</b> impératif à <b>F3</b> très négociable).",
        piege="prendre le niveau («&nbsp;au moins…&nbsp;») pour le critère, écrire un niveau sans unité, ou choisir la "
              "flexibilité d'après l'importance de la fonction au lieu de l'écart que le client accepte.",
    )


# ─────────────────────────────────────────────────────────────────────────────
# Les rappels, un par page
# ─────────────────────────────────────────────────────────────────────────────
T1 = "theme-1-objets-systemes-usages-interactions/"
T2 = "theme-2-structure-fonctionnement-comportement/"
T3 = "theme-3-creation-conception-realisation-innovations/"
C7 = T3 + "C7-imaginer-concevoir-et-realiser-une-ou-des/"
C8 = T3 + "C8-valider-les-solutions-techniques-par-des/"

RAPPELS = [
    # ── Ateliers « Le diagramme des exigences », en tête du premier onglet
    dict(id="exigences-4e", niveau="4e", atelier=("exigences-sysml", "4e"),
         titre="Deux lignes du cahier des charges du système d'arrosage",
         objet="le système d'arrosage du jardin", client="Mme Joseph, la gardienne du jardin",
         pourquoi="Le diagramme des exigences range, en blocs, les lignes d'un <b>cahier des charges</b>. Avant de le lire, "
                  "trois minutes pour retrouver ce que dit chaque case d'une ligne, sur le système d'arrosage du jardin.",
         lignes=[
             ligne("Ligne 1, le smartphone", "Le compte rendu sur le smartphone", "fc", "le smartphone",
                   dict(bon="Envoyer le compte rendu au smartphone",
                        nom=("Envoi du compte rendu au smartphone", "Envoi", "envoyer"),
                        sujet=("Le smartphone reçoit le compte rendu", "le smartphone"),
                        solution=("Module Wi-Fi dans le boîtier", "le module Wi-Fi est le moyen d'envoyer le message")),
                   dict(bon="Délai entre la fin de l'arrosage et le message, en minutes",
                        pourquoi="on mesure le temps que met le message à arriver",
                        niveau="5 min au plus",
                        solution=("Une box Internet plus rapide", "elle dit avec quoi on irait plus vite"),
                        autre=("Couleur de l'écran du smartphone", "La couleur de l'écran ne dit rien du message : on mesure "
                                                                     "le temps qu'il met à arriver.")),
                   dict(bon="5 min au plus", sans_unite=("5 au plus", "5 quoi ? Des minutes, des messages, des secondes ?"),
                        unite=("5 L au plus", "Le litre mesure un volume d'eau ; le critère est un temps : son unité est la minute (min)."),
                        vague="Rapidement"),
                   dict(bonne="f2", cit="6 ou 7 minutes, ça ira aussi", ecart="une ou deux minutes de plus")),
             ligne("Ligne 2, la gardienne", "La sécurité électrique", "fc", "la gardienne",
                   "Être sans danger pour la gardienne",
                   dict(bon="Tension d'alimentation, en volts", pourquoi="le danger vient du courant électrique : on contrôle "
                                                                        "la tension qui alimente le système",
                        niveau="12 V au plus",
                        solution=("Une batterie de 12 volts", "c'est le moyen choisi pour rester en très basse tension"),
                        autre=("Volume d'eau par jour, en litres", "Le volume d'eau dit si l'on gaspille ; il ne dit rien du "
                                                                   "danger électrique.")),
                   dict(bon="12 V au plus", sans_unite=("12 au plus", "12 quoi ? Des volts, des litres, des minutes ?"),
                        unite=("12 A au plus", "L'ampère (A) mesure une intensité ; le critère est une tension : son unité est "
                                               "le volt (V)."),
                        vague="Sans danger"),
                   dict(bonne="f0", cit="Pas question d'amener le 230 V au jardin", securite=True)),
         ]),
    dict(id="exigences-3e", niveau="3e", atelier=("exigences-sysml", "3e"),
         titre="Deux lignes du cahier des charges de la station d'alerte",
         objet="la station d'alerte cyclonique", client="Mme Augustin, présidente du comité de quartier",
         pourquoi="Évaluer une solution, c'est la comparer aux lignes du <b>cahier des charges</b>. Avant les deux boîtiers, "
                  "cinq minutes pour retrouver ce que dit chaque case d'une ligne, sur deux exigences de la station qui ne "
                  "sont pas dans les exercices.",
         lignes=[
             ligne("Ligne 1, les habitants et le vent", "Le déclenchement de l'alerte", "fp", "les habitants → le vent du cyclone",
                   dict(bon="Prévenir les habitants quand le vent du cyclone forcit",
                        nom=("Prévention des habitants du quartier", "Prévention", "prévenir"),
                        sujet=("La sirène prévient les habitants du quartier", "la sirène"),
                        solution=("Anémomètre relié à une sirène", "l'anémomètre et la sirène sont les moyens de prévenir")),
                   dict(bon="Vitesse moyenne du vent qui déclenche l'alerte, en kilomètres par heure",
                        pourquoi="on mesure la vitesse du vent au moment où l'alerte part",
                        niveau="À partir de 90 km/h",
                        solution=("Un anémomètre à coupelles", "c'est l'instrument qui mesure le vent"),
                        autre=("Direction du vent", "La direction dit d'où vient le vent, pas s'il est assez fort pour être "
                                                    "dangereux.")),
                   dict(bon="90 km/h",
                        sans_unite=("90", "90 quoi ? Des kilomètres par heure, des mètres par seconde ?"),
                        unite=("90 mètres par seconde", "90 mètres par seconde, c'est plus de 300 km/h : l'unité change tout le niveau. Le "
                                         "comité parle en kilomètres par heure."),
                        vague="Quand il y a beaucoup de vent"),
                   dict(bonne="f0", cit="Pas question d'alerter plus tard : à 90 km/h, les tôles commencent à s'envoler",
                        securite=True)),
             ligne("Ligne 2, les voisins", "Les fausses alertes", "fc", "les voisins",
                   "Ne pas réveiller le quartier par erreur",
                   dict(bon="Nombre de fausses alertes par an", pourquoi="on compte les alertes parties sans cyclone",
                        niveau="1 par an au plus",
                        solution=("Un programme qui vérifie deux mesures de suite", "c'est un moyen d'éviter les fausses alertes"),
                        autre=("Distance où l'alerte s'entend, en mètres", "C'est une autre exigence, celle de l'alerte audible ; "
                                                                           "elle ne compte pas les erreurs.")),
                   dict(bon="1 fausse alerte par an au plus",
                        sans_unite=("1 au plus", "1 quoi ? Par an, par jour, par cyclone ?"),
                        unite=("1 min au plus", "La minute mesure une durée ; le critère compte des fausses alertes dans "
                                                "une année."),
                        vague="Pas trop souvent"),
                   dict(bonne="f2", cit="Deux par an, je saurai l'expliquer aux voisins", ecart="une fausse alerte de plus")),
         ]),
    # ── 4e
    dict(id="hangzhou-4e", niveau="4e",
         # révision du 10/11/2026 (la charge de lecture de la séance 3, 2 600 mots) : le rappel ne sert qu'à qui a oublié
         replie="🔁 Piqûre de rappel (5 min)&nbsp;: le cahier des charges, en tableau à menus — ouvre-la si tu ne sais "
                "plus ce qu'est un critère, un niveau, une flexibilité",
         sequence=T1 + "C2-decrire-les-interactions-entre-un-objet-ou/4e/4e_C2.1/sequence_4e_C2_hangzhou_borne.html",
         avant="  <h4>Ton cahier des charges</h4>", balise="h4", balise_exo="h5",
         titre="Deux lignes du cahier des charges de la borne",
         objet="la borne de vélos", client="le service des vélos de la ville",
         pourquoi="Tes quatre exigences vont entrer dans le <b>cahier des charges</b> de la borne. Avant de les écrire, cinq "
                  "minutes pour retrouver ce que dit chaque case d'une ligne, sur deux lignes de cette borne.",
         lignes=[
             ligne("Ligne 1, l'usager et le vélo", "Le déverrouillage", "fp", "l'usager → le vélo",
                   dict(bon="Permettre à l'usager de retirer un vélo",
                        nom=("Retrait d'un vélo par l'usager", "Retrait", "retirer"),
                        sujet=("L'usager retire un vélo à la borne", "l'usager"),
                        solution=("Lecteur de carte et verrou électrique", "le lecteur et le verrou disent avec quoi, pas le "
                                                                           "service rendu")),
                   dict(bon="Nombre de déverrouillages réussis sur 100 essais",
                        pourquoi="on compte les essais qui marchent, sur cent",
                        niveau="Au moins 98 fois sur 100",
                        solution=("Un lecteur de carte plus rapide", "c'est un moyen d'y arriver"),
                        autre=("Couleur de l'écran de la borne", "La couleur de l'écran ne dit pas si le vélo se libère : on "
                                                                 "compte les déverrouillages réussis.")),
                   dict(bon="98 réussites sur 100 au moins",
                        sans_unite=("98 au moins", "98 quoi ? Des réussites sur 100 essais, des secondes ?"),
                        unite=("98 secondes au moins", "La seconde mesure une durée ; le critère compte des réussites sur 100 "
                                                       "essais."),
                        vague="Presque toujours"),
                   dict(bonne="f1", cit="96 sur 100, à la rigueur, si la borne affiche tout de suite pourquoi elle refuse",
                        ecart="96 au lieu de 98", condition="la borne dit pourquoi elle refuse")),
             ligne("Ligne 2, l'usager qui porte un enfant", "Le retrait d'une seule main", "fc", "l'usager qui a une main prise",
                   "Permettre le retrait d'une seule main",
                   dict(bon="Nombre de mains nécessaires pour retirer le vélo",
                        pourquoi="on compte les mains qu'il faut pour sortir le vélo de la borne",
                        niveau="Une seule main",
                        solution=("Une poignée de déverrouillage sur le guidon", "c'est un moyen de libérer le vélo"),
                        autre=("Prix de la location, en yuans", "Le prix ne dit pas si l'on peut faire le geste d'une main.")),
                   dict(bon="1 main au plus",
                        sans_unite=("1 au plus", "1 quoi ? Une main, un essai, une minute ?"),
                        unite=("1 min au plus", "La minute mesure une durée ; le critère compte des mains."),
                        vague="Facilement"),
                   dict(bonne="f0", cit="Une main, pas deux : un parent tient son enfant de l'autre")),
         ]),
    dict(id="arrosage-4e", niveau="4e",
         # révision du 11/11/2026 (la charge de lecture de la séance 3, 1 891 mots) : le rappel ne sert qu'à qui a oublié
         replie="🔁 Piqûre de rappel (3 min)&nbsp;: une ligne du cahier des charges, en tableau à menus — ouvre-la si tu "
                "ne sais plus ce qu'est un critère, un niveau, une flexibilité",
         sequence=T2 + "C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.2/sequence-jardin-connecte-arrosage-automatique.html",
         avant='  <div class="act">\n    <header><span class="num">Activité 7</span>', balise="h3", balise_exo="h4",
         titre="Une ligne du cahier des charges de l'arrosage automatique",
         objet="l'arrosage automatique", client="le professeur responsable du jardin",
         pourquoi="L'activité 7 juge le prototype ligne par ligne du <b>cahier des charges</b>. Avant, trois minutes pour "
                  "retrouver ce que dit chaque case d'une ligne, sur celle de la sécurité.",
         lignes=[
             ligne("Ligne 1, les élèves", "La sécurité électrique", "fc", "les élèves",
                   dict(bon="Fonctionner sans danger pour les élèves",
                        nom=("Sécurité des élèves au jardin", "Sécurité", "fonctionner, être"),
                        sujet=("Le prototype ne met pas les élèves en danger", "le prototype"),
                        solution=("Pile et câble USB au lieu du secteur", "la pile et le câble USB sont les moyens de rester en "
                                                                         "très basse tension")),
                   dict(bon="Tension d'alimentation du prototype, en volts",
                        pourquoi="le danger vient du courant électrique : on contrôle la tension qui alimente le prototype",
                        niveau="5 V au plus",
                        solution=("Un relais entre la carte et la pompe", "c'est un composant du montage"),
                        autre=("Humidité du sol, en pourcentage", "L'humidité dit quand arroser ; elle ne dit rien du danger "
                                                                  "électrique.")),
                   dict(bon="5 V au plus",
                        sans_unite=("5 au plus", "5 quoi ? Des volts, des ampères, des pour cent ?"),
                        unite=("5 A au plus", "L'ampère (A) mesure une intensité ; le critère est une tension : son unité est "
                                              "le volt (V)."),
                        vague="Pas dangereux"),
                   dict(bonne="f0", cit="Jamais le secteur au jardin : la très basse tension prévue, et rien d'autre",
                        securite=True)),
         ]),
    dict(id="jardin-conception-4e", niveau="4e",
         sequence=C7 + "4e/4e_C7.1/sequence_4e_C7_jardin-conception.html",
         avant='<section class="card" id="act2">\n<h2>✏️ Activité 2', balise="h2", balise_exo="h3",
         titre="Deux lignes du cahier des charges du boîtier de la sonde",
         objet="le boîtier de la sonde", client="Mme Ortiz",
         pourquoi="Choisir une solution «&nbsp;avec des critères&nbsp;», c'est partir des lignes du <b>cahier des charges</b> "
                  "que Mme Ortiz a dictées. Avant de choisir, cinq minutes pour retrouver ce que dit chaque case d'une ligne.",
         lignes=[
             ligne("Ligne 1, la pluie", "L'eau", "fc", "la pluie",
                   dict(bon="Protéger l'électronique de la pluie",
                        nom=("Protection de l'électronique contre la pluie", "Protection", "protéger"),
                        sujet=("Le boîtier protège l'électronique de la pluie", "le boîtier"),
                        solution=("Boîte en plastique avec un joint", "la boîte et son joint sont le moyen d'arrêter l'eau")),
                   dict(bon="Indice de protection contre l'eau (IP)",
                        pourquoi="la norme des indices de protection dit à quelle eau un boîtier résiste",
                        niveau="IPX4 au moins",
                        solution=("Un joint en caoutchouc", "c'est un moyen d'arrêter l'eau"),
                        autre=("Couleur du boîtier", "La couleur ne dit rien de l'eau qui entre : ce sont la forme et les joints "
                                                     "qui comptent.")),
                   dict(bon="IPX4 au moins",
                        sans_unite=("4 au moins", "4 quoi ? Le code complet de la norme, IPX4, dit à quelle eau le boîtier "
                                                  "résiste."),
                        unite=("4 cm au moins", "Le centimètre mesure une longueur ; le critère est un indice de protection, "
                                                "écrit IPX4."),
                        vague="Bien étanche"),
                   dict(bonne="f1", cit="IPX3 à la rigueur, si le boîtier reste sous l'auvent du mur sud",
                        ecart="IPX3 au lieu de IPX4", condition="le boîtier reste sous l'auvent")),
             ligne("Ligne 2, Mme Ortiz", "Le changement de pile", "fc", "Mme Ortiz",
                   "Pouvoir s'ouvrir pour changer la pile",
                   dict(bon="Temps pour changer la pile, en minutes",
                        pourquoi="on chronomètre le changement de pile",
                        niveau="5 min au plus",
                        solution=("Un couvercle à vis papillon", "c'est un moyen d'ouvrir vite"),
                        autre=("Nombre de piles dans le boîtier", "Le nombre de piles ne dit pas si le boîtier s'ouvre "
                                                                  "facilement.")),
                   dict(bon="5 min au plus", sans_unite=("5 au plus", "5 quoi ? Des minutes, des vis, des piles ?"),
                        unite=("5 L au plus", "Le litre mesure un volume ; le critère est un temps : son unité est la minute "
                                              "(min)."),
                        vague="Vite"),
                   dict(bonne="f3", cit="Même un quart d'heure : je ne la change qu'une fois par an",
                        ecart="15 minutes au lieu de 5")),
         ]),
    dict(id="bac-4e", niveau="4e",
         sequence=C7 + "4e/4e_C7.3/sequence_4e_C7.3_bac-du-jardin.html",
         avant='<section class="card" id="act0">\n  <h2>📋 Activité 0', balise="h2", balise_exo="h3",
         titre="Deux lignes du cahier des charges du bac",
         objet="le bac de culture", client="l'intendance du collège",
         pourquoi="«&nbsp;Le plus adapté&nbsp;», c'est adapté au <b>cahier des charges</b> des bacs. Avant de le relire ligne par "
                  "ligne, cinq minutes pour retrouver ce que dit chaque case d'une ligne.",
         lignes=[
             ligne("Ligne 1, la terre humide", "La poussée de la terre", "fc", "la terre humide",
                   dict(bon="Résister à la poussée de la terre humide",
                        nom=("Résistance des parois à la terre", "Résistance", "résister"),
                        sujet=("Les parois résistent à la poussée de la terre", "les parois"),
                        solution=("Planches de pin de 3 cm d'épaisseur", "les planches sont le moyen choisi pour tenir")),
                   dict(bon="Résistance en flexion du matériau, en mégapascals (MPa)",
                        pourquoi="on mesure la contrainte que le matériau supporte sans casser quand la paroi plie",
                        niveau="Au moins 20 MPa",
                        solution=("Des équerres en acier aux angles", "c'est un moyen de renforcer le bac"),
                        autre=("Prix du matériau", "Le prix n'est pas une exigence du cahier des charges : on tranche avec lui "
                                                   "une fois les exigences tenues.")),
                   dict(bon="20 MPa au moins",
                        sans_unite=("20 au moins", "20 quoi ? Des mégapascals, des kilogrammes, des euros ?"),
                        unite=("20 kg au moins", "Le kilogramme mesure une masse ; le critère est une résistance, en "
                                                 "mégapascals (MPa)."),
                        vague="Très solide"),
                   dict(bonne="f1", cit="18 MPa à la rigueur, si on ajoute un renfort au milieu du grand côté",
                        ecart="18 MPa au lieu de 20", condition="un renfort au milieu du grand côté")),
             ligne("Ligne 2, le conseil d'administration", "Le recyclage", "fc", "le conseil d'administration",
                   "Pouvoir être recyclé en fin de vie",
                   dict(bon="Part recyclable du matériau, en pourcentage",
                        pourquoi="on mesure la part du matériau qu'une filière sait recycler",
                        niveau="Au moins 40 %",
                        solution=("Une benne de tri au collège", "c'est un moyen de jeter, pas une mesure"),
                        autre=("Masse de la pièce, en kilogrammes", "C'est une autre exigence, celle du bac qu'on déplace ; "
                                                                    "elle ne dit rien du recyclage.")),
                   dict(bon="40 % au moins",
                        sans_unite=("40 au moins", "40 quoi ? Des pour cent, des kilogrammes, des années ?"),
                        unite=("40 kg au moins", "Le kilogramme mesure une masse ; le critère est une part, en pour cent (%)."),
                        vague="Facile à jeter"),
                   dict(bonne="f0", cit="Le collège n'installe pas ce qu'il ne saura pas jeter : c'est voté, pas un point de moins")),
         ]),
    dict(id="jardin-incomplet-4e", niveau="4e",
         sequence=C7 + "4e/4e_C7.5/sequence_4e_C7.5_jardin-incomplet.html",
         avant='<section class="card" id="act0">\n  <h2>🧩 Activité 0', balise="h2", balise_exo="h3",
         titre="Deux lignes du cahier des charges du jardin",
         objet="le prototype d'arrosage", client="le club jardin",
         pourquoi="Pour trouver ce qui manque, on part du <b>cahier des charges</b>, pas du montage. Avant, cinq minutes pour "
                  "retrouver ce que dit chaque case d'une ligne, sur deux lignes du jardin.",
         lignes=[
             ligne("Ligne 1, le club et les plantes", "Le déclenchement", "fp", "le club jardin → les plantes",
                   dict(bon="Arroser les plantes quand la terre est sèche",
                        nom=("Arrosage automatique des plantes", "Arrosage", "arroser"),
                        sujet=("La pompe arrose les plantes quand la terre est sèche", "la pompe"),
                        solution=("Pompe, relais et capteur d'humidité", "ce sont les constituants, pas le service rendu")),
                   dict(bon="Humidité du sol qui déclenche l'arrosage, en pourcentage",
                        pourquoi="on mesure l'humidité de la terre au moment où la pompe part",
                        niveau="Sous 35 %",
                        solution=("Un capteur d'humidité branché sur A0", "c'est le constituant qui mesure"),
                        autre=("Température de l'air, en degrés Celsius", "La température est une autre grandeur : le "
                                                                          "cahier des charges vise l'humidité du sol.")),
                   dict(bon="sous 35 % d'humidité",
                        sans_unite=("sous 35", "35 quoi ? Des pour cent d'humidité, des degrés ?"),
                        unite=("sous 35 °C", "Le degré Celsius mesure une température ; le critère est une humidité, en "
                                             "pour cent (%)."),
                        vague="Quand c'est sec"),
                   dict(bonne="f2", cit="33 ou 37 %, ça ira aussi", ecart="2 points de plus ou de moins")),
             ligne("Ligne 2, la cuve", "La durée d'arrosage", "fc", "la cuve d'eau",
                   "Prendre seulement l'eau nécessaire à chaque arrosage",
                   dict(bon="Durée de chaque arrosage, en secondes",
                        pourquoi="on chronomètre le temps pendant lequel la pompe tourne",
                        niveau="Six secondes",
                        solution=("Un relais qui coupe la pompe", "c'est le constituant qui arrête l'eau"),
                        autre=("Couleur du tuyau", "La couleur ne dit rien de l'eau prise dans la cuve.")),
                   dict(bon="6 s par arrosage",
                        sans_unite=("6 par arrosage", "6 quoi ? Des secondes, des litres ?"),
                        unite=("6 L par arrosage", "Le litre mesure un volume ; le critère est une durée : son unité est la "
                                                   "seconde (s)."),
                        vague="Pas trop longtemps"),
                   dict(bonne="f3", cit="5 ou 10 secondes, peu importe : la cuve est grande", ecart="jusqu'à 10 secondes")),
         ]),
    dict(id="validation-4e", niveau="4e",
         sequence=C8 + "4e/4e_C8.1/sequence_4e_C8_jardin-validation.html",
         avant="<!-- ateliers-representations:debut ex-4e-jardin-validation -->", balise="h3", balise_exo="h4",
         titre="Une ligne du cahier des charges du support",
         objet="le support de capteur", client="Mme Ortiz",
         pourquoi="Valider, c'est comparer chaque résultat à une ligne du <b>cahier des charges</b>. Avant, trois minutes pour "
                  "retrouver ce que dit chaque case d'une ligne, sur celle du gel.",
         lignes=[
             ligne("Ligne 1, le gel de l'hiver", "Le gel", "fc", "le gel de l'hiver",
                   dict(bon="Résister au gel de l'hiver new-yorkais",
                        nom=("Résistance au gel de l'hiver", "Résistance", "résister"),
                        sujet=("L'attache résiste au gel de janvier", "l'attache"),
                        solution=("Attache en acier inoxydable", "l'attache en inox est un moyen de tenir")),
                   dict(bon="Température la plus basse supportée sans fissure, en degrés Celsius",
                        pourquoi="on refroidit l'attache et on regarde jusqu'où elle tient sans se fendre",
                        niveau="Jusqu'à −8 °C",
                        solution=("Une attache en plastique plus épais", "c'est un moyen d'y arriver"),
                        autre=("Nombre de jardinières sur le toit", "Le nombre de jardinières ne dit rien de la tenue au "
                                                                    "froid.")),
                   dict(bon="−8 °C sans fissure",
                        sans_unite=("−8 sans fissure", "−8 quoi ? Des degrés Celsius, des centimètres ?"),
                        unite=("−8 cm sans fissure", "Le centimètre mesure une longueur ; le critère est une température, en "
                                                     "degrés Celsius (°C)."),
                        vague="Par grand froid"),
                   dict(bonne="f0", cit="Pas une fissure à −8 °C : un support fendu lâche la sonde au premier coup de vent")),
         ]),
    # ── 3e
    dict(id="shenzhen-3e", niveau="3e",
         sequence=T1 + "C3-caracteriser-et-choisir-un-objet-ou-un/3e/3e_C3.1/sequence_3e_C3.1-C3.4_shenzhen.html",
         avant="<!-- ateliers-representations:debut ex-3e-shenzhen-c3 -->", balise="h4", balise_exo="h5",
         titre="Une ligne du cahier des charges du local",
         objet="le local des serveurs", client="le constructeur des serveurs",
         pourquoi="Ta grille va peser les solutions d'après le <b>cahier des charges</b> du local. Avant, trois minutes pour "
                  "retrouver ce que dit chaque case d'une ligne, sur celle de la température.",
         lignes=[
             ligne("Ligne 1, les serveurs", "La température du local", "fc", "les serveurs",
                   dict(bon="Garder le local assez frais pour les serveurs",
                        nom=("Refroidissement du local des serveurs", "Refroidissement", "garder, refroidir"),
                        sujet=("Le local reste sous 32 °C l'après-midi", "le local"),
                        solution=("Un climatiseur de 2 kilowatts", "le climatiseur est l'une des solutions à comparer")),
                   dict(bon="Température du local au moment le plus chaud, en degrés Celsius",
                        pourquoi="on relève la température au pic de l'après-midi, le moment le plus défavorable",
                        niveau="32 °C au plus",
                        solution=("Un ventilateur au plafond", "c'est l'une des solutions possibles"),
                        autre=("Coût d'installation, en euros", "Le coût sert à départager les solutions ; il ne dit pas si le "
                                                                "local reste assez frais.")),
                   dict(bon="32 °C au plus",
                        sans_unite=("32 au plus", "32 quoi ? Des degrés Celsius, des kilowattheures ?"),
                        unite=("32 kWh au plus", "Le kilowattheure mesure une énergie ; le critère est une température, en "
                                                 "degrés Celsius (°C)."),
                        vague="Pas trop chaud"),
                   dict(bonne="f0", cit="Au-delà de 32 °C, les machines s'arrêtent d'elles-mêmes : pas un degré de plus")),
         ]),
    dict(id="boitier-3e", niveau="3e",
         sequence=C7 + "3e/3e_C7.3/sequence_3e_C7.3_boitier-de-la-station.html",
         avant='<section class="card">\n  <h2>📐 Activité 0 — L\'épaisseur', balise="h2", balise_exo="h3",
         titre="Deux lignes du cahier des charges du boîtier",
         objet="le boîtier de la station", client="la mairie",
         pourquoi="Toute la séquence se joue sur le <b>cahier des charges</b> du boîtier&nbsp;: le lire, puis décider s'il faut "
                  "en rouvrir une ligne. Avant, cinq minutes pour retrouver ce que dit chaque case d'une ligne, sur deux "
                  "lignes qui ne bougeront pas.",
         lignes=[
             ligne("Ligne 1, le vent du cyclone", "La tenue en tête de mât", "fc", "le vent du cyclone",
                   dict(bon="Tenir en tête de mât par vent de cyclone",
                        nom=("Tenue du boîtier au vent de cyclone", "Tenue", "tenir"),
                        sujet=("Le boîtier tient en haut du mât", "le boîtier"),
                        solution=("Une paroi de 3 mm en PLA", "la paroi est le moyen choisi pour tenir")),
                   dict(bon="Résistance du matériau, en mégapascals (MPa)",
                        pourquoi="on mesure la contrainte que le matériau supporte sans casser",
                        niveau="Au moins 30 MPa",
                        solution=("Quatre vis de fixation en inox", "c'est un moyen de fixer le boîtier"),
                        autre=("Coût du boîtier, en euros", "Le coût départage les matériaux retenus ; il ne dit pas si le "
                                                            "boîtier tient au vent.")),
                   dict(bon="30 MPa au moins",
                        sans_unite=("30 au moins", "30 quoi ? Des mégapascals, des euros, des années ?"),
                        unite=("30 km/h au moins", "Le kilomètre par heure mesure une vitesse ; le critère est une résistance, "
                                                   "en mégapascals (MPa)."),
                        vague="Très résistant"),
                   dict(bonne="f0", cit="Un boîtier qui tombe du mât en plein cyclone, c'est l'alerte qui se tait",
                        securite=True)),
             ligne("Ligne 2, le soleil", "La chaleur dans le boîtier", "fc", "le soleil",
                   "Ne pas cuire l'électronique au soleil",
                   dict(bon="Température dans le boîtier en plein soleil, en degrés Celsius",
                        pourquoi="on mesure la température que l'électronique subit à l'intérieur",
                        niveau="60 °C au plus",
                        solution=("Une peinture blanche", "c'est un moyen de moins chauffer"),
                        autre=("Tenue au soleil, en années", "C'est une autre exigence : le matériau qui vieillit sous les "
                                                              "ultraviolets, pas la chaleur dans la boîte.")),
                   dict(bon="60 °C au plus",
                        sans_unite=("60 au plus", "60 quoi ? Des degrés Celsius, des années ?"),
                        unite=("60 ans au plus", "L'année mesure une durée ; le critère est une température, en degrés Celsius "
                                                 "(°C)."),
                        vague="Pas trop chaud"),
                   dict(bonne="f0", cit="Au-delà de 60 °C, la carte s'arrête : pas un degré de plus")),
         ]),
    dict(id="station-equiper-3e", niveau="3e",
         sequence=C7 + "3e/3e_C7.5/sequence_3e_C7.5_station-a-equiper.html",
         avant='<section class="card">\n  <h2>📋 Activité 0 — Ce que chaque exigence impose', balise="h2", balise_exo="h3",
         titre="Deux lignes du cahier des charges de la commission",
         objet="la station", client="la commission de sécurité",
         pourquoi="C'est le <b>cahier des charges</b> de la commission qui choisit les constituants, pas le catalogue. Avant de "
                  "le traduire, cinq minutes pour retrouver ce que dit chaque case d'une ligne, sur deux de ses exigences.",
         lignes=[
             ligne("Ligne 1, le vent et la cour", "Le déclenchement de l'alerte", "fp", "le vent → les élèves dans la cour",
                   dict(bon="Alerter la cour quand le vent devient dangereux",
                        nom=("Alerte de la cour en cas de vent", "Alerte", "alerter"),
                        sujet=("La station alerte la cour quand le vent souffle", "la station"),
                        solution=("Anémomètre et gyrophare", "ce sont des constituants, pas le service rendu")),
                   dict(bon="Vitesse moyenne du vent qui déclenche l'alerte, en kilomètres par heure",
                        pourquoi="on mesure la vitesse du vent au moment où l'alerte part",
                        niveau="Au-delà de 90 km/h",
                        solution=("Un anémomètre à coupelles", "c'est l'instrument qui mesure le vent"),
                        autre=("Direction du vent", "La direction dit d'où vient le vent, pas s'il est dangereux.")),
                   dict(bon="90 km/h de vent moyen",
                        sans_unite=("90 de vent moyen", "90 quoi ? Des kilomètres par heure, des mètres par seconde ?"),
                        unite=("90 mètres par seconde de vent moyen", "90 mètres par seconde, c'est plus de 300 km/h : l'unité change tout le "
                                                       "niveau. La commission parle en kilomètres par heure."),
                        vague="Quand il y a beaucoup de vent"),
                   dict(bonne="f0", cit="À 90 km/h, on évacue la cour : la commission ne négocie pas", securite=True)),
             ligne("Ligne 2, le réseau électrique coupé", "L'autonomie", "fc", "le réseau électrique coupé",
                   "Fonctionner sans intervention pendant le cyclone",
                   dict(bon="Durée de fonctionnement sans intervention, en heures",
                        pourquoi="on mesure combien de temps la station tient seule",
                        niveau="72 heures au moins",
                        solution=("Une batterie et un panneau solaire", "ce sont des constituants qui tiennent l'énergie"),
                        autre=("Nombre de mesures enregistrées", "C'est l'exigence de l'historique ; elle ne dit pas combien "
                                                                 "de temps la station tient.")),
                   dict(bon="72 h au moins",
                        sans_unite=("72 au moins", "72 quoi ? Des heures, des mesures, des watts ?"),
                        unite=("72 watts au moins", "Le watt mesure une puissance ; le critère est une durée, en heures (h)."),
                        vague="Longtemps"),
                   dict(bonne="f1", cit="60 heures à la rigueur, si la station prévient quand sa batterie faiblit",
                        ecart="60 heures au lieu de 72", condition="la station prévient quand sa batterie faiblit")),
         ]),
    dict(id="produire-boitier-3e", niveau="3e",
         sequence=C7 + "3e/3e_C7.7/sequence_3e_C7.7_produire-le-boitier.html",
         avant='<section class="card">\n  <h2>✏️ Activité 2 — Corriger le dessin', balise="h2", balise_exo="h3",
         titre="Une ligne du cahier des charges du boîtier",
         objet="le boîtier", client="la mairie",
         pourquoi="On corrige le dessin «&nbsp;sans toucher au <b>cahier des charges</b>&nbsp;». Pour savoir ce qu'on n'a pas le "
                  "droit de toucher, trois minutes pour retrouver ce que dit chaque case d'une de ses lignes.",
         lignes=[
             ligne("Ligne 1, le haut du mât", "L'encombrement", "fc", "le support en haut du mât",
                   dict(bon="Tenir dans la place prévue en haut du mât",
                        nom=("Encombrement du boîtier en haut du mât", "Encombrement", "tenir"),
                        sujet=("Le boîtier tient sur le support du mât", "le boîtier"),
                        solution=("Un boîtier imprimé en 3D", "l'impression est le moyen de fabriquer, pas ce que le boîtier "
                                                              "doit faire")),
                   dict(bon="Dimensions extérieures du boîtier, en millimètres",
                        pourquoi="on mesure la longueur, la largeur et la hauteur du boîtier",
                        niveau="200 × 150 × 90 mm au plus",
                        solution=("Une casquette anti-pluie à 45°", "c'est une cote du dessin, un moyen ; elle se corrige"),
                        autre=("Profondeur de la rainure de joint", "C'est une cote du dessin, qui se corrige ; elle ne dit pas "
                                                                     "la place prise en haut du mât.")),
                   dict(bon="200 × 150 × 90 mm au plus",
                        sans_unite=("200 × 150 × 90 au plus", "200 × 150 × 90 quoi ? Des millimètres, des centimètres ?"),
                        unite=("200 × 150 × 90 cm au plus", "En centimètres, le boîtier serait dix fois plus grand dans chaque "
                                                            "sens : l'unité change tout le niveau."),
                        vague="Assez petit"),
                   dict(bonne="f0", cit="Le support en haut du mât est fait pour ces dimensions : pas un millimètre de plus")),
         ]),
    dict(id="mat-simulation-3e", niveau="3e",
         sequence=C8 + "3e/3e_C8.1/sequence_3e_C8.1_mat-de-la-station.html",
         avant='<section class="card" id="act4">\n  <h2>⚖️ Activité 4', balise="h2", balise_exo="h3",
         titre="Une ligne du cahier des charges de la mairie",
         objet="le mât", client="le bureau d'études de la mairie",
         pourquoi="Décider, c'est revenir au <b>cahier des charges</b> de la mairie. Avant, trois minutes pour retrouver ce que "
                  "dit chaque case d'une ligne, sur celle de la flèche en tête.",
         lignes=[
             ligne("Ligne 1, l'anémomètre", "La flèche en tête", "fc", "l'anémomètre en tête du mât",
                   dict(bon="Garder l'anémomètre assez immobile pour mesurer juste",
                        nom=("Rigidité du mât sous le vent", "Rigidité", "garder"),
                        sujet=("Le mât ne plie pas sous le vent", "le mât"),
                        solution=("Un tube d'aluminium de 50 mm", "le tube est l'un des profilés à comparer")),
                   dict(bon="Flèche en tête du mât, en millimètres",
                        pourquoi="on mesure de combien la tête du mât se déplace sous le vent",
                        niveau="40 mm au plus",
                        solution=("Un hauban accroché au toit", "c'est un moyen de raidir le mât"),
                        autre=("Masse du mât, en kilogrammes", "La masse ne dit pas de combien la tête se déplace.")),
                   dict(bon="40 mm au plus",
                        sans_unite=("40 au plus", "40 quoi ? Des millimètres, des newtons ?"),
                        unite=("40 N au plus", "Le newton (N) mesure une force ; le critère est un déplacement, en "
                                               "millimètres (mm)."),
                        vague="Presque pas"),
                   dict(bonne="f0", cit="Au-delà de 40 mm, l'anémomètre ne vise plus juste : aucune marge")),
         ]),
    dict(id="mat-protocole-3e", niveau="3e",
         sequence=C8 + "3e/3e_C8.2/sequence_3e_C8.2_mat-de-la-station.html",
         avant='<section class="card">\n  <h2>✍️ Activité 2 — PROPOSER ton protocole', balise="h2", balise_exo="h3",
         titre="Une ligne du cahier des charges de la mairie",
         objet="le mât", client="le bureau d'études de la mairie",
         pourquoi="Ton protocole va vérifier le <b>cahier des charges</b> de la mairie. Avant de le proposer, trois minutes pour "
                  "retrouver ce que dit chaque case d'une ligne, sur celle de la hauteur.",
         lignes=[
             ligne("Ligne 1, le toit", "La hauteur", "fc", "les turbulences du toit",
                   dict(bon="Placer l'anémomètre au-dessus des turbulences du toit",
                        nom=("Hauteur de l'anémomètre sur le toit", "Hauteur", "placer"),
                        sujet=("L'anémomètre mesure le vent au-dessus du toit", "l'anémomètre"),
                        solution=("Un mât encastré au pied", "c'est la façon de le fixer, un moyen")),
                   dict(bon="Hauteur du mât au-dessus du toit, en mètres",
                        pourquoi="on mesure à quelle hauteur l'anémomètre se trouve",
                        niveau="2 m exactement",
                        solution=("Un tube en aluminium", "c'est une matière possible pour le mât"),
                        autre=("Diamètre du mât, en millimètres", "Le diamètre ne dit pas à quelle hauteur l'anémomètre "
                                                                  "mesure.")),
                   dict(bon="2 m exactement",
                        sans_unite=("2 exactement", "2 quoi ? Des mètres, des kilogrammes ?"),
                        unite=("2 kg exactement", "Le kilogramme mesure une masse ; le critère est une hauteur, en mètres (m)."),
                        vague="Assez haut"),
                   dict(bonne="f0", cit="En dessous de 2 m, l'anémomètre lit les turbulences du toit, pas le vent réel")),
         ]),
    dict(id="station-programmee-3e", niveau="3e",
         sequence=T3 + "C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.2/sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html",
         avant='  <div class="activite" id="act1">', balise="h3", balise_exo="h4",
         titre="Une ligne du cahier des charges de la mairie",
         objet="la station", client="la mairie",
         pourquoi="Le programme décidera d'après le <b>cahier des charges</b> de la mairie. Avant de le relire, trois minutes pour "
                  "retrouver ce que dit chaque case d'une ligne, sur celle du premier seuil.",
         lignes=[
             ligne("Ligne 1, le vent et les habitants", "Le premier seuil", "fp", "le vent → les habitants",
                   dict(bon="Annoncer aux habitants le niveau d'alerte du vent",
                        nom=("Annonce du niveau d'alerte", "Annonce", "annoncer"),
                        sujet=("La station annonce le niveau d'alerte", "la station"),
                        solution=("Un anémomètre relié à la carte", "ce sont des constituants, pas le service rendu")),
                   dict(bon="Vitesse du vent mesurée, en kilomètres par heure",
                        pourquoi="on mesure la vitesse du vent, puis on la compare aux seuils",
                        niveau="À partir de 63 km/h",
                        solution=("Un écran qui affiche le niveau", "c'est un constituant qui affiche"),
                        autre=("Nombre d'appuis sur le bouton", "Le bouton sert à acquitter l'alarme ; il ne dit rien du "
                                                                "vent.")),
                   dict(bon="tempête tropicale à partir de 63 km/h",
                        sans_unite=("tempête tropicale à partir de 63", "63 quoi ? Des kilomètres par heure, des mètres par "
                                                                        "seconde ?"),
                        unite=("tempête tropicale à partir de 63 mètres par seconde", "63 mètres par seconde, c'est plus de 220 km/h : "
                                                                       "l'unité change tout le niveau."),
                        vague="quand le vent forcit"),
                   dict(bonne="f0", cit="Les seuils sont ceux de l'échelle des cyclones : pas un kilomètre par heure d'écart")),
         ]),
]

_ids = [r["id"] for r in RAPPELS]
assert len(_ids) == len(set(_ids)), "identifiants de rappel en double"
