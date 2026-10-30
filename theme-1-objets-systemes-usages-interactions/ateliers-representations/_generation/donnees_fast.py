# -*- coding: utf-8 -*-
"""Atelier — Des fonctions aux solutions techniques (diagramme FAST).

Codes servis : 5e_C4.1, 5e_C1.2 (5e) ; 4e_C4.4, 4e_C7.2 (4e) ; 3e_C7.2 (3e).
Objets-fils : le lampadaire intelligent et le vélo-cargo de Léa (5e), le système d'arrosage
connecté du jardin (4e), la station d'alerte cyclonique (3e).

Le verbe change d'un niveau à l'autre, pas la notion :
  5e  LIRE le FAST dans les deux sens, puis le COMPLÉTER ; comparer deux principes pour une fonction ;
  4e  CONSTRUIRE : associer constituants et fonctions (chaîne d'information), ajouter une branche ;
  3e  CONTRÔLER un FAST proposé, puis COMPARER et ARBITRER entre plusieurs solutions.

Le plan de la mission prévoyait six exercices ; la 3e en reçoit deux (un seul exercice de 30 minutes
aurait été indigeste) : « trouver les erreurs d'un FAST » (mécanique « corriger un schéma ») précède
l'arbitrage. Total : sept exercices.
"""
import figures

SLUG = "fast"
COURT = "fa"
EMOJI = "🌳"
TITRE = "Des fonctions aux solutions techniques"
TITRE_COURT = "des fonctions aux solutions techniques (diagramme FAST)"
TITRE_COMPLET = ("Des fonctions aux solutions techniques : le diagramme FAST (Function Analysis System Technique, "
                 "« technique d'analyse fonctionnelle »)")
ETIQUETTE = "🌳 diagramme FAST"
ETIQUETTE_COURTE = "FAST"
MENTION_FICTION = ("Situations imaginées pour les exercices : Léa, Mme Joseph, le jardin du collège, la station d'alerte du "
                   "quartier et le brouillon de l'équipe de 3e sont inventés. Les valeurs de la sirène et de la batterie "
                   "(défi bonus de 3e) sont des ordres de grandeur, pas les caractéristiques d'un appareil réel.")

SIGLE = ("diagramme FAST", "de l'anglais <i lang=\"en\">Function Analysis System Technique</i>, « technique d'analyse "
         "fonctionnelle ». Le schéma part de la fonction d'usage (à gauche), la décompose en fonctions techniques (au milieu) "
         "et associe à chacune la solution technique qui la réalise (à droite).")
MOT_FU = ("fonction d'usage", "ce à quoi sert l'objet, pour la personne qui l'utilise. Elle s'écrit avec un verbe à l'infinitif.")
MOT_FT = ("fonction technique", "une action que l'objet doit réaliser pour rendre son service. Elle commence par un "
          "<b>verbe à l'infinitif</b>&nbsp;: détecter, stocker, mesurer…")
MOT_LED = ("LED", "de l'anglais <i lang=\"en\">light-emitting diode</i>, diode électroluminescente&nbsp;: une petite lampe qui "
           "éclaire beaucoup en consommant peu.")
MOT_ST = ("solution technique", "l'élément de l'objet — une pièce, un composant — qui réalise une fonction technique. C'est un "
          "<b>nom</b>&nbsp;: la batterie, le capteur…")

# ─────────────────────────────────────────────────────────────────────────────
# Les dessins
# ─────────────────────────────────────────────────────────────────────────────
FU_LAMPADAIRE = "Éclairer la rue la nuit quand un piéton passe"
FT_LAMPADAIRE = ["détecter la nuit", "détecter un passant", "décider quand allumer", "produire la lumière",
                 "stocker l'énergie pour la nuit", "capter l'énergie du soleil"]
ST_LAMPADAIRE = ["le capteur de luminosité", "le détecteur de mouvement", "la carte programmable", "le bloc de LED",
                 "la batterie", "le panneau solaire"]
CACHEES = (1, 4, 5)   # les trois solutions à trouver à l'exercice 2


def _branches_lampadaire(cacher=()):
    return [(ft, ["?" if i in cacher else ST_LAMPADAIRE[i]]) for i, ft in enumerate(FT_LAMPADAIRE)]


DESC_LAMPADAIRE = ("Diagramme FAST en trois colonnes. En haut, deux flèches : vers la gauche « Pourquoi ? », vers la droite "
                   "« Comment ? ». À gauche, la fonction d'usage : éclairer la rue la nuit quand un piéton passe. Au milieu, six "
                   "fonctions techniques, de haut en bas : détecter la nuit ; détecter un passant ; décider quand allumer ; "
                   "produire la lumière ; stocker l'énergie pour la nuit ; capter l'énergie du soleil. À droite, la solution de "
                   "chacune, sur la même ligne : ")

LAMPADAIRE_LIRE = figures.fast(
    "fa-lamp", FU_LAMPADAIRE, _branches_lampadaire(CACHEES),
    "Diagramme FAST du lampadaire intelligent, avec trois solutions cachées",
    DESC_LAMPADAIRE + "le capteur de luminosité ; un point d'interrogation ; la carte programmable ; le bloc de LED ; un point "
                      "d'interrogation ; un point d'interrogation.")

LAMPADAIRE_COMPLETER = figures.fast(
    "fa-lamp2", FU_LAMPADAIRE, [(ft, ["" if i in CACHEES else ST_LAMPADAIRE[i]]) for i, ft in enumerate(FT_LAMPADAIRE)],
    "Diagramme FAST du lampadaire intelligent, à compléter",
    DESC_LAMPADAIRE + "le capteur de luminosité ; une case vide ; la carte programmable ; le bloc de LED ; une case vide ; une "
                      "case vide. Les trois cases vides ont un bord en pointillés.",
    vivants={(1, 0): "fa-l1", (4, 0): "fa-l2", (5, 0): "fa-l3"})

LAMPADAIRE_CORRIGE = figures.fast(
    "fa-lamp3", FU_LAMPADAIRE, _branches_lampadaire(),
    "Diagramme FAST du lampadaire intelligent, complet",
    DESC_LAMPADAIRE + "le capteur de luminosité ; le détecteur de mouvement ; la carte programmable ; le bloc de LED ; la "
                      "batterie ; le panneau solaire.")

VELO = figures.fast(
    "fa-velo", "Transporter les enfants et les courses de Léa",
    [("transmettre l'effort de Léa à la roue", ["le pédalier et la chaîne"]),
     ("ralentir la roue", ["frein à patins : frottement sur la jante", "frein à disque : frottement sur un disque"]),
     ("porter les enfants et les courses", ["le bac à rebords hauts"])],
    "Extrait du diagramme FAST du vélo-cargo : deux principes pour ralentir la roue",
    "Diagramme FAST en trois colonnes, avec les flèches « Pourquoi ? » vers la gauche et « Comment ? » vers la droite. "
    "Fonction d'usage : transporter les enfants et les courses de Léa. Trois fonctions techniques. Transmettre l'effort de "
    "Léa à la roue : le pédalier et la chaîne. Ralentir la roue : deux cases reliées par le mot « ou » — frein à patins, "
    "frottement sur la jante, ou frein à disque, frottement sur un disque. Porter les enfants et les courses : le bac à "
    "rebords hauts.")

FU_JARDIN = "Arroser les plantes quand la terre est sèche"
FT_JARDIN = ["mesurer l'humidité du sol", "décider quand arroser", "envoyer l'état au smartphone",
             "laisser passer l'eau ou la bloquer", "faire circuler l'eau jusqu'aux bacs", "stocker l'eau de pluie"]
ST_JARDIN = ["le capteur d'humidité du sol", "la carte programmable", "le module Wi-Fi", "l'électrovanne",
             "la pompe et les tuyaux", "la cuve"]
DESC_JARDIN = ("Diagramme FAST en trois colonnes, avec les flèches « Pourquoi ? » vers la gauche et « Comment ? » vers la "
               "droite. Fonction d'usage : arroser les plantes quand la terre est sèche. Six fonctions techniques, de haut en "
               "bas : mesurer l'humidité du sol ; décider quand arroser ; envoyer l'état au smartphone ; laisser passer l'eau "
               "ou la bloquer ; faire circuler l'eau jusqu'aux bacs ; stocker l'eau de pluie. ")

JARDIN_A_RELIER = figures.fast(
    "fa-jard", FU_JARDIN, [(ft, ["?"]) for ft in FT_JARDIN],
    "Diagramme FAST du système d'arrosage : les fonctions techniques, sans leurs solutions",
    DESC_JARDIN + "Les six cases de solution portent un point d'interrogation.")

JARDIN_CORRIGE = figures.fast(
    "fa-jard2", FU_JARDIN, [(ft, [ST_JARDIN[i]]) for i, ft in enumerate(FT_JARDIN)],
    "Diagramme FAST du système d'arrosage, complet",
    DESC_JARDIN + "Les solutions, dans le même ordre : le capteur d'humidité du sol ; la carte programmable ; le module Wi-Fi ; "
                  "l'électrovanne ; la pompe et les tuyaux ; la cuve.")

NOUVELLE_FT = "mesurer le niveau d'eau de la cuve"
NOUVELLE_ST = "le capteur de niveau d'eau"

JARDIN_AJOUT = figures.fast(
    "fa-jard3", FU_JARDIN, [(ft, [ST_JARDIN[i]]) for i, ft in enumerate(FT_JARDIN)] + [("", [""])],
    "Diagramme FAST du système d'arrosage, avec une nouvelle branche à construire",
    DESC_JARDIN + "Chacune a sa solution : le capteur d'humidité du sol ; la carte programmable ; le module Wi-Fi ; "
                  "l'électrovanne ; la pompe et les tuyaux ; la cuve. Une septième branche, en bas, est vide : sa case de fonction et sa case "
                  "de solution ont un bord en pointillés.",
    vivants={(6, "ft"): "fa-e5-ft", (6, 0): "fa-e5-st"})

JARDIN_AJOUT_CORRIGE = figures.fast(
    "fa-jard4", FU_JARDIN, [(ft, [ST_JARDIN[i]]) for i, ft in enumerate(FT_JARDIN)] + [(NOUVELLE_FT, [NOUVELLE_ST])],
    "Diagramme FAST du système d'arrosage, avec la nouvelle branche",
    DESC_JARDIN + "Chacune a sa solution : le capteur d'humidité du sol ; la carte programmable ; le module Wi-Fi ; "
                  "l'électrovanne ; la pompe et les tuyaux ; la cuve. Une septième branche, la nouvelle, en bas : mesurer le niveau d'eau de "
                  "la cuve, réalisée par le capteur de niveau d'eau.")

FU_STATION = "Prévenir les habitants quand un cyclone approche"
ALERTES = ["la sirène", "un message sur les téléphones", "un panneau lumineux à LED"]
STATION_BRANCHES = [("mesurer la vitesse du vent", ["l'anémomètre"]),
                    ("décider du niveau d'alerte", ["la carte programmable"]),
                    ("diffuser l'alerte aux habitants", ALERTES),
                    ("stocker l'énergie pour la nuit", ["la batterie 12 V"]),
                    ("capter l'énergie du soleil", ["le panneau solaire"])]
DESC_STATION = ("Diagramme FAST en trois colonnes, avec les flèches « Pourquoi ? » vers la gauche et « Comment ? » vers la "
                "droite. Fonction d'usage : prévenir les habitants quand un cyclone approche. ")

STATION_ERREURS = figures.fast(
    "fa-stat", FU_STATION,
    [("mesurer la vitesse du vent", ["l'anémomètre"]),
     ("le programme d'alerte", ["la carte programmable"]),
     ("diffuser l'alerte aux habitants", ALERTES),
     ("stocker l'énergie pour la nuit", ["le panneau solaire"]),
     ("capter l'énergie du soleil", ["le panneau solaire"]),
     ("éclairer la rue la nuit", ["le bloc de LED"])],
    "Le diagramme FAST de la station d'alerte proposé par une équipe, avec trois erreurs",
    DESC_STATION + "Six branches, de haut en bas, chacune avec sa fonction puis sa solution. Branche 1 : mesurer la vitesse du "
                   "vent, l'anémomètre. Branche 2 : le programme d'alerte, la carte programmable. Branche 3 : diffuser l'alerte "
                   "aux habitants, trois solutions reliées par « ou » : la sirène, ou un message sur les téléphones, ou un "
                   "panneau lumineux à LED. Branche 4 : stocker l'énergie pour la nuit, le panneau solaire. Branche 5 : capter "
                   "l'énergie du soleil, le panneau solaire. Branche 6 : éclairer la rue la nuit, le bloc de LED.")

STATION = figures.fast(
    "fa-stat2", FU_STATION, STATION_BRANCHES,
    "Le diagramme FAST de la station d'alerte cyclonique, corrigé",
    DESC_STATION + "Cinq branches, de haut en bas. Mesurer la vitesse du vent : l'anémomètre. Décider du niveau d'alerte : la "
                   "carte programmable. Diffuser l'alerte aux habitants : trois solutions reliées par « ou » — la sirène, ou un "
                   "message sur les téléphones, ou un panneau lumineux à LED. Stocker l'énergie pour la nuit : la batterie 12 V. "
                   "Capter l'énergie du soleil : le panneau solaire.")


def figure_vivante(svg, legende):
    return '<figure class="figure schema-vivant">%s<figcaption>%s</figcaption></figure>' % (svg, legende)


def figure_corrigee(svg, legende):
    return '<figure class="figure">%s<figcaption>%s</figcaption></figure>' % (svg, legende)


# ─────────────────────────────────────────────────────────────────────────────
# 5e
# ─────────────────────────────────────────────────────────────────────────────
E1 = dict(
    id="e1", titre="Lire le FAST du lampadaire", code="5e_C4.1", duree=10,
    objectif="lire un diagramme FAST dans les deux sens&nbsp;: d'une fonction technique vers sa solution («&nbsp;comment&nbsp;?&nbsp;»), "
             "et d'une solution vers sa fonction («&nbsp;pourquoi&nbsp;?&nbsp;»).",
    production="six étiquettes rangées (fonction ou solution) et deux lectures du schéma.",
    mots=[SIGLE, MOT_FU, MOT_FT, MOT_ST,
          MOT_LED,
          ("carte programmable", "une petite carte électronique qui suit un programme&nbsp;: elle reçoit des informations et décide "
           "quoi faire.")],
    documents=[dict(svg=LAMPADAIRE_LIRE, legende="Le diagramme FAST du lampadaire intelligent. Trois solutions sont cachées "
                                                 "(?)&nbsp;: lis leur fonction, la solution viendra ensuite.",
                    description="<p>À gauche, la fonction d'usage&nbsp;: <b>éclairer la rue la nuit quand un piéton passe</b>.</p>"
                                "<p>Au milieu, six fonctions techniques, chacune suivie de sa solution&nbsp;:</p><ul>"
                                "<li>détecter la nuit → le capteur de luminosité&nbsp;;</li>"
                                "<li>détecter un passant → ?&nbsp;;</li>"
                                "<li>décider quand allumer → la carte programmable&nbsp;;</li>"
                                "<li>produire la lumière → le bloc de LED&nbsp;;</li>"
                                "<li>stocker l'énergie pour la nuit → ?&nbsp;;</li>"
                                "<li>capter l'énergie du soleil → ?</li></ul>"
                                "<p>En haut, une flèche vers la gauche dit «&nbsp;Pourquoi&nbsp;?&nbsp;», une flèche vers la droite "
                                "dit «&nbsp;Comment&nbsp;?&nbsp;».</p>")],
    intro="<p>Dans la rue qui monte au collège, à Sainte-Luce, la mairie a posé un <b>lampadaire intelligent</b>&nbsp;: il ne "
          "s'allume que la nuit, et seulement quand quelqu'un passe. Il n'est relié à aucun câble&nbsp;: un panneau solaire et une "
          "batterie lui suffisent, en très basse tension.</p>"
          "<p>Pour comprendre comment il est fait, on dessine son <b>diagramme FAST</b> (de l'anglais <i lang=\"en\">Function "
          "Analysis System Technique</i>, «&nbsp;technique d'analyse fonctionnelle&nbsp;»). On le lit dans deux sens&nbsp;: vers "
          "la <b>droite</b>, on répond à «&nbsp;<b>Comment&nbsp;?</b>&nbsp;»&nbsp;; vers la <b>gauche</b>, à «&nbsp;<b>Pourquoi&nbsp;?</b>&nbsp;».</p>",
    consigne="<p>Une <b>fonction technique</b> dit ce que l'objet doit <b>faire</b>&nbsp;: elle commence par un verbe à l'infinitif "
             "(détecter, stocker…). Une <b>solution technique</b> est l'<b>élément</b> de l'objet qui le fait&nbsp;: c'est un nom "
             "(la batterie…).</p>"
             "<p><b>Range chaque étiquette&nbsp;: fonction technique ou solution technique&nbsp;?</b> Les étiquettes viennent de deux "
             "objets, le lampadaire et le vélo-cargo&nbsp;: c'est la forme des mots qui décide, pas l'objet. Puis <b>lis le schéma</b> une "
             "fois vers la droite et une fois vers la gauche.</p>",
    critere="six étiquettes bien rangées, et deux lectures justes&nbsp;: tu sais dire dans quel sens tu as lu.",
    widgets=[dict(type="classer", name="col",
                  categories=[("ft", "une fonction technique (ce que l'objet doit faire)"),
                              ("st", "une solution technique (l'élément qui le fait)")],
                  items=[("« détecter un passant » (lampadaire)", "ft", "« détecter un passant » commence par un verbe : c'est une action à réaliser."),
                         ("« le bloc de LED » (lampadaire)", "st", "« le bloc de LED » est un nom : c'est un élément qu'on peut toucher."),
                         ("« transmettre l'effort de Léa à la roue » (vélo-cargo)", "ft", "« transmettre » est un verbe à l'infinitif : c'est ce que l'objet doit faire."),
                         ("« la chaîne » (vélo-cargo)", "st", "« la chaîne » est un nom : une pièce du vélo qu'on peut toucher."),
                         ("« capter l'énergie du soleil » (lampadaire)", "ft", "« capter » est un verbe : c'est une fonction, même si tu sais quel objet la réalise."),
                         ("« le capteur de luminosité » (lampadaire)", "st", "« le capteur de luminosité » est un nom : un composant. Attention, « capteur » n'est pas un verbe.")]),
             dict(type="choix", name="comment",
                  legende="Lis vers la droite&nbsp;: <b>comment</b> le lampadaire détecte-t-il la nuit&nbsp;?",
                  options=[("capteur", "Avec le capteur de luminosité."),
                           ("carte", "Avec la carte programmable."),
                           ("led", "Avec le bloc de LED, qui s'allume."),
                           ("horloge", "Avec une horloge réglée sur le coucher du soleil.")],
                  bonne="capteur",
                  retours={"capteur": "Oui : sur la ligne « détecter la nuit », la case de droite dit le capteur de luminosité.",
                           "carte": "La carte programmable est sur la ligne « décider quand allumer » : elle décide, elle ne détecte rien elle-même.",
                           "led": "Le bloc de LED est la réponse à « comment produire la lumière ? » : il éclaire, il ne détecte pas.",
                           "horloge": "Aucune case du schéma ne parle d'horloge : on ne répond qu'avec ce qui est écrit dans le FAST."}),
             dict(type="choix", name="pourquoi",
                  legende="Lis vers la gauche&nbsp;: <b>pourquoi</b> le lampadaire a-t-il un bloc de LED&nbsp;?",
                  options=[("lumiere", "Pour produire la lumière, et donc éclairer la rue quand un piéton passe."),
                           ("nuit", "Pour détecter la nuit, quand le soleil se couche."),
                           ("stocker", "Pour stocker l'énergie du soleil jusqu'au soir."),
                           ("decor", "Pour décorer la rue pendant la journée.")],
                  bonne="lumiere",
                  retours={"lumiere": "Oui : vers la gauche, le bloc de LED mène à « produire la lumière », qui mène à la fonction d'usage.",
                           "nuit": "Détecter la nuit, c'est la ligne du capteur de luminosité, pas celle du bloc de LED.",
                           "stocker": "Stocker l'énergie est la fonction d'une autre solution, cachée pour l'instant : pas celle du bloc de LED.",
                           "decor": "Le lampadaire est éteint le jour : rien, dans le schéma, ne parle de décoration."})],
    aides=["<p>Pour ranger une étiquette, regarde son <b>premier mot</b>&nbsp;: un verbe (détecter, stocker, capter) → une fonction&nbsp;; "
           "un nom précédé de «&nbsp;le&nbsp;» ou «&nbsp;la&nbsp;» → une solution. Pour lire le schéma, pose le doigt sur une case et suis "
           "le trait&nbsp;: vers la droite → «&nbsp;comment&nbsp;?&nbsp;», vers la gauche → «&nbsp;pourquoi&nbsp;?&nbsp;».</p>",
           "<ul><li><b>«&nbsp;capter l'énergie du soleil&nbsp;»</b> → commence par <b>capter</b>, un verbe → <b>fonction</b>.</li>"
           "<li><b>«&nbsp;le capteur de luminosité&nbsp;»</b> → commence par <b>le</b>, puis un nom → <b>solution</b>. «&nbsp;Capteur&nbsp;» "
           "ressemble à «&nbsp;capter&nbsp;», mais c'est l'objet, pas l'action.</li>"
           "<li><b>Comment détecter la nuit&nbsp;?</b> → je pars de la case «&nbsp;détecter la nuit&nbsp;» → je vais à droite → le "
           "capteur de luminosité.</li>"
           "<li><b>Pourquoi un bloc de LED&nbsp;?</b> → je pars de la case «&nbsp;le bloc de LED&nbsp;» → je vais à gauche → produire la "
           "lumière → encore à gauche → éclairer la rue quand un piéton passe.</li></ul>"],
    jumeau=dict(consigne="Le FAST d'une lampe de poche dit&nbsp;: «&nbsp;stocker l'énergie&nbsp;» → «&nbsp;deux piles&nbsp;» et "
                         "«&nbsp;produire la lumière&nbsp;» → «&nbsp;une LED&nbsp;». Pourquoi la lampe a-t-elle deux piles&nbsp;? "
                         "Comment produit-elle la lumière&nbsp;?",
                correction="Pourquoi deux piles&nbsp;? → je lis vers la gauche → <b>pour stocker l'énergie</b> (et donc éclairer sans "
                           "câble). Comment produire la lumière&nbsp;? → je lis vers la droite → <b>avec une LED</b>."),
    correction=[
        "<b>Fonctions</b> (un verbe à l'infinitif)&nbsp;: «&nbsp;détecter un passant&nbsp;», «&nbsp;transmettre l'effort de Léa à la "
        "roue&nbsp;», «&nbsp;capter l'énergie du soleil&nbsp;»",
        "<b>Solutions</b> (un nom, un élément qu'on touche)&nbsp;: «&nbsp;le bloc de LED&nbsp;», «&nbsp;la chaîne&nbsp;», "
        "«&nbsp;le capteur de luminosité&nbsp;»",
        "L'objet ne décide de rien&nbsp;: le lampadaire et le vélo-cargo ont tous deux des fonctions et des solutions.",
        "Le piège&nbsp;: «&nbsp;<b>capteur</b>&nbsp;» ressemble au verbe «&nbsp;capter&nbsp;», mais c'est un objet → solution.",
        "<b>Comment détecter la nuit&nbsp;?</b> → vers la droite → <b>le capteur de luminosité</b>",
        "Pas la carte programmable → elle est sur la ligne «&nbsp;décider quand allumer&nbsp;». Pas le bloc de LED → il produit la "
        "lumière. Pas une horloge → aucune case n'en parle.",
        "<b>Pourquoi un bloc de LED&nbsp;?</b> → vers la gauche → <b>produire la lumière</b> → encore à gauche → éclairer la rue la "
        "nuit quand un piéton passe",
        "Pas détecter la nuit, pas stocker l'énergie → ce sont les lignes d'autres solutions. Pas décorer → le lampadaire est éteint le jour.",
        ("conclusion", "Vers la droite, le FAST répond à «&nbsp;<b>comment&nbsp;?</b>&nbsp;» (quelle solution)&nbsp;; vers la gauche, à "
                       "«&nbsp;<b>pourquoi&nbsp;?</b>&nbsp;» (quelle fonction, et à quoi elle sert)."),
    ],
    retenir="une <b>fonction technique</b> est une action (un verbe à l'infinitif)&nbsp;; une <b>solution technique</b> est l'élément "
            "qui la réalise (un nom). Le FAST se lit «&nbsp;comment&nbsp;?&nbsp;» vers la droite et «&nbsp;pourquoi&nbsp;?&nbsp;» vers la gauche.",
    piege="prendre «&nbsp;le capteur&nbsp;» pour une fonction parce qu'il ressemble au verbe «&nbsp;capter&nbsp;»&nbsp;: c'est un objet, donc une solution.",
)

BANQUE_E2 = ["le détecteur de mouvement", "la batterie", "le panneau solaire", "un interrupteur à bouton"]

E2 = dict(
    id="e2", titre="Compléter les solutions techniques", code="5e_C4.1", duree=10,
    objectif="associer à trois fonctions techniques la solution qui les réalise, et écarter celle qui ne sert pas la fonction d'usage.",
    production="le FAST du lampadaire complété, la raison de l'intrus, et une lecture «&nbsp;pourquoi&nbsp;?&nbsp;».",
    mots=[MOT_ST,
          ("détecteur de mouvement", "un composant qui repère qu'un corps chaud (une personne, un animal) bouge devant lui."),
          ("batterie", "un réservoir d'énergie électrique&nbsp;: elle se charge le jour et rend l'énergie la nuit."),
          ("panneau solaire", "un panneau qui capte la lumière du soleil et la transforme en énergie électrique. Il ne garde rien&nbsp;: "
           "la nuit, il ne donne plus rien."),
          ("intrus", "un mot de la banque qui n'a sa place dans aucune case.")],
    intro="<p>Voici le même diagramme FAST du lampadaire. Les trois solutions cachées sont maintenant des cases en pointillés, "
          "sur les lignes «&nbsp;détecter un passant&nbsp;», «&nbsp;stocker l'énergie pour la nuit&nbsp;» et «&nbsp;capter l'énergie du "
          "soleil&nbsp;». Ce que tu choisis s'écrit dans le schéma.</p>",
    consigne="<p><b>Complète les trois cases</b> avec la banque&nbsp;: <i>le détecteur de mouvement · la batterie · le panneau "
             "solaire · un interrupteur à bouton</i>. La solution d'une case est l'élément qui réalise la fonction technique écrite "
             "sur sa ligne, à gauche. Un mot de la banque est un <b>intrus</b>&nbsp;: <b>dis pourquoi</b> il n'a pas de case. Puis "
             "<b>lis vers la gauche</b> pour la batterie.</p>",
    critere="les trois cases sont justes, tu donnes la bonne raison pour l'intrus, et tu remontes de la batterie jusqu'à la fonction "
            "d'usage.",
    widgets=[dict(type="slots", intro=figure_vivante(LAMPADAIRE_COMPLETER, "Le FAST du lampadaire, à compléter. Tes choix s'écrivent "
                                                                           "dans les cases en pointillés."),
                  slots=[dict(name="s1", cible="fa-l1", legende="La case de la ligne <b>détecter un passant</b>",
                              options=BANQUE_E2, bonnes=["le détecteur de mouvement"],
                              indice="Détecter un passant : quel élément sait qu'une personne bouge devant le lampadaire ?"),
                         dict(name="s2", cible="fa-l2", legende="La case de la ligne <b>stocker l'énergie pour la nuit</b>",
                              options=BANQUE_E2, bonnes=["la batterie"],
                              indice="Stocker l'énergie : quel élément garde l'énergie du jour pour la rendre la nuit ? Le panneau, lui, ne garde rien."),
                         dict(name="s3", cible="fa-l3", legende="La case de la ligne <b>capter l'énergie du soleil</b>",
                              options=BANQUE_E2, bonnes=["le panneau solaire"],
                              indice="Capter l'énergie du soleil : quel élément reçoit la lumière du soleil, le jour ?")]),
             dict(type="choix", name="intrus", legende="Pourquoi «&nbsp;un interrupteur à bouton&nbsp;» n'a-t-il pas de case&nbsp;?",
                  options=[("geste", "Parce qu'il faudrait que le piéton appuie dessus, alors que le lampadaire doit s'allumer tout seul quand il passe."),
                           ("cher", "Parce qu'un interrupteur coûte trop cher pour un lampadaire de rue."),
                           ("electrique", "Parce qu'un interrupteur n'a rien d'électrique."),
                           ("fonction", "Parce qu'un interrupteur est une fonction technique, pas une solution.")],
                  bonne="geste",
                  retours={"geste": "Oui : lis vers la gauche. Un bouton demande un geste ; la fonction d'usage dit « quand un piéton passe », sans geste.",
                           "cher": "Un interrupteur est un composant bon marché : le prix n'est pas la raison.",
                           "electrique": "Un interrupteur ouvre ou ferme un circuit électrique : il est bien électrique, ce n'est pas la raison.",
                           "fonction": "« Un interrupteur » est un nom : c'est bien une solution. Elle ne sert simplement pas cette fonction d'usage."}),
             dict(type="choix", name="batterie",
                  legende="Lis vers la gauche&nbsp;: <b>pourquoi</b> le lampadaire a-t-il une batterie&nbsp;?",
                  options=[("nuit", "Pour stocker l'énergie du jour, et éclairer la nuit quand le panneau ne capte plus rien."),
                           ("capter", "Pour capter l'énergie du soleil pendant la journée, sur le toit du lampadaire."),
                           ("detecter", "Pour détecter la nuit, puisqu'elle se vide quand le soleil se couche."),
                           ("poids", "Pour alourdir le pied du lampadaire et l'empêcher de tomber.")],
                  bonne="nuit",
                  retours={"nuit": "Oui : batterie → stocker l'énergie pour la nuit → éclairer la rue la nuit quand un piéton passe.",
                           "capter": "Capter l'énergie du soleil, c'est la ligne du panneau solaire : la batterie ne reçoit pas la lumière.",
                           "detecter": "Détecter la nuit, c'est la ligne du capteur de luminosité.",
                           "poids": "Aucune ligne du FAST ne parle de stabilité : la batterie y est pour stocker l'énergie."})],
    aides=["<p>Pour chaque case, lis la fonction écrite sur sa ligne, puis demande-toi&nbsp;: <b>quel élément sait faire cela&nbsp;?</b> "
           "Il restera un mot. Pour savoir pourquoi il n'a pas de case, remonte vers la gauche jusqu'à la fonction d'usage.</p>",
           "<p>Détecter un passant → il faut un élément qui sent qu'on bouge → <b>le détecteur de mouvement</b>.<br>"
           "Stocker l'énergie pour la nuit → le panneau ne garde rien → <b>la batterie</b>.<br>"
           "Capter l'énergie du soleil → <b>le panneau solaire</b>.<br>"
           "Reste l'interrupteur à bouton → pourquoi&nbsp;? → pour allumer à la main → mais la fonction d'usage dit «&nbsp;quand un "
           "piéton passe&nbsp;» → pas de case.</p>"],
    jumeau=dict(consigne="Une lampe de vélo rechargeable a deux fonctions techniques&nbsp;: «&nbsp;stocker l'énergie&nbsp;» et "
                         "«&nbsp;produire la lumière&nbsp;». Banque&nbsp;: <i>une LED · une batterie · un panneau solaire</i>. Complète, "
                         "et dis quel mot est l'intrus.",
                correction="Stocker l'énergie → <b>une batterie</b>. Produire la lumière → <b>une LED</b>. Intrus&nbsp;: <b>le panneau "
                           "solaire</b> → cette lampe se recharge avec le câble d'un chargeur, aucune de ses fonctions ne capte le soleil."),
    correction=[
        figure_corrigee(LAMPADAIRE_CORRIGE, "Le FAST du lampadaire, complet."),
        "<b>Détecter un passant</b> → <b>le détecteur de mouvement</b> → il repère qu'une personne bouge",
        "<b>Stocker l'énergie pour la nuit</b> → <b>la batterie</b> → elle se charge le jour et rend l'énergie la nuit",
        "<b>Capter l'énergie du soleil</b> → <b>le panneau solaire</b> → il capte, mais il ne garde rien",
        "Le piège entre ces deux dernières cases&nbsp;: le panneau <b>capte</b>, la batterie <b>stocke</b>. La nuit, le panneau ne donne plus rien.",
        "<b>L'intrus</b>&nbsp;: l'interrupteur à bouton → pourquoi&nbsp;? → allumer à la main → la fonction d'usage dit «&nbsp;quand un "
        "piéton passe&nbsp;», sans geste → aucune ligne ne le demande",
        "Les autres raisons ne tiennent pas&nbsp;: un interrupteur est bon marché, il est électrique, et c'est bien une solution (un nom).",
        "<b>Pourquoi une batterie&nbsp;?</b> → stocker l'énergie pour la nuit → éclairer la rue la nuit quand un piéton passe",
        ("conclusion", "Une solution a sa place dans le FAST si, en lisant vers la gauche («&nbsp;pourquoi&nbsp;?&nbsp;»), on arrive à la "
                       "fonction d'usage."),
    ],
    retenir="chaque fonction technique a sa <b>solution</b>&nbsp;: l'élément qui la réalise. Une solution qui ne ramène pas, par "
            "«&nbsp;pourquoi&nbsp;?&nbsp;», à la fonction d'usage n'a rien à faire dans le FAST.",
    piege="mettre le panneau solaire dans la case «&nbsp;stocker l'énergie&nbsp;»&nbsp;: le panneau <b>capte</b>, c'est la batterie qui <b>stocke</b>.",
)

E3 = dict(
    id="e3", titre="Deux principes pour une même fonction", code="5e_C1.2", duree=14,
    objectif="comparer deux principes techniques qui réalisent la même fonction, puis choisir selon la situation et justifier.",
    production="cinq propriétés rangées, un choix pour le vélo-cargo de Léa, et une phrase de justification.",
    mots=[("principe technique", "la façon physique de réaliser une fonction&nbsp;: quel phénomène, à quel endroit."),
          ("frottement", "deux surfaces qui glissent l'une contre l'autre en se freinant. Le frottement chauffe et use les surfaces."),
          ("jante", "le cercle de métal de la roue, sur lequel est monté le pneu."),
          ("moyeu", "la pièce au centre de la roue, autour de laquelle elle tourne."),
          ("patin", "un bloc de caoutchouc que le frein serre contre la jante."),
          ("disque", "une plaque de métal ronde, fixée au moyeu, qui tourne avec la roue&nbsp;; des plaquettes la serrent pour freiner."),
          ("alternative", "un choix entre deux solutions&nbsp;: dans le FAST, deux cases reliées par «&nbsp;ou&nbsp;».")],
    documents=[dict(svg=VELO, legende="Un extrait du FAST du vélo-cargo&nbsp;: la ligne «&nbsp;ralentir la roue&nbsp;» a deux cases, "
                                      "reliées par «&nbsp;ou&nbsp;».",
                    description="<p>Fonction d'usage&nbsp;: <b>transporter les enfants et les courses de Léa</b>. Trois fonctions "
                                "techniques&nbsp;:</p><ul>"
                                "<li>transmettre l'effort de Léa à la roue → le pédalier et la chaîne&nbsp;;</li>"
                                "<li>ralentir la roue → <b>frein à patins</b> (frottement sur la jante) <b>ou</b> <b>frein à disque</b> "
                                "(frottement sur un disque)&nbsp;;</li>"
                                "<li>porter les enfants et les courses → le bac à rebords hauts.</li></ul>")],
    intro="<p><b>Léa</b> transporte ses deux enfants et ses courses dans le bac de son <b>vélo-cargo</b>. Pour rentrer chez elle, elle descend "
          "deux côtes, souvent sous la pluie. Elle doit changer ses freins, et le vendeur lui propose deux modèles.</p>"
          "<p><b>Deux principes, une fonction.</b> Dans le FAST, «&nbsp;ralentir la roue&nbsp;» a <b>deux</b> cases reliées par «&nbsp;ou&nbsp;»&nbsp;: deux "
          "<b>principes techniques</b> pour la <b>même</b> fonction. Les deux freinent par <b>frottement</b>, mais pas au même "
          "endroit&nbsp;: les patins serrent la <b>jante</b>, au bord de la roue, là où le pneu projette l'eau et la boue&nbsp;; les "
          "plaquettes serrent un <b>disque</b> fixé au <b>moyeu</b>, au centre de la roue, plus à l'abri.</p>",
    consigne="<p>Un <b>principe technique</b>, c'est la façon physique de réaliser une fonction&nbsp;: quel phénomène, à quel endroit. "
             "<b>Range chaque propriété</b>&nbsp;: est-elle vraie pour le frein à patins, pour le frein à disque, ou pour les deux&nbsp;? "
             "Puis <b>choisis</b> le frein du vélo-cargo de Léa et <b>justifie</b> ton choix en une phrase.</p>",
    critere="cinq propriétés bien rangées, le choix qui convient à Léa, et une phrase qui cite la pluie et les côtes (ou la charge).",
    widgets=[dict(type="classer", name="prop",
                  categories=[("patins", "le frein à patins"), ("disque", "le frein à disque"), ("deux", "les deux")],
                  items=[("Il freine presque aussi bien sous la pluie que par temps sec.", "disque",
                          "Sous la pluie : lequel frotte loin de l'eau projetée par le pneu ?"),
                         ("Il use la jante de la roue à chaque freinage.", "patins",
                          "User la jante : lequel frotte directement sur la jante ?"),
                         ("Il coûte plus cher à l'achat et à la réparation.", "disque",
                          "Le prix : lequel demande un disque, des plaquettes et des pièces en plus ?"),
                         ("Il ralentit la roue en frottant sur une pièce qui tourne avec elle.", "deux",
                          "Le frottement : relis l'introduction, les deux freins utilisent-ils le même phénomène ?"),
                         ("Il se règle avec une simple clé, sans outil spécial.", "patins",
                          "Le réglage : lequel est le plus simple, avec ses deux patins visibles ?")]),
             dict(type="choix", name="choix", legende="Quel frein conseilles-tu pour le vélo-cargo de Léa&nbsp;?",
                  options=[("disque", "Le frein à disque."),
                           ("patins", "Le frein à patins."),
                           ("aucun", "Aucun des deux&nbsp;: en descente, il suffit de ne pas pédaler."),
                           ("egal", "N'importe lequel&nbsp;: ils freinent tous les deux par frottement.")],
                  bonne="disque",
                  retours={"disque": "Oui : sous la pluie, dans les côtes, avec deux enfants dans le bac, c'est le freinage par temps humide qui compte le plus.",
                           "patins": "Le frein à patins est moins cher et plus simple, mais il freine moins bien sous la pluie : or Léa descend des côtes sous la pluie.",
                           "aucun": "Dans une descente, le vélo-cargo chargé prend de la vitesse tout seul : il faut une fonction « ralentir la roue ».",
                           "egal": "Même phénomène ne veut pas dire même résultat : l'endroit où l'on frotte change tout sous la pluie."}),
             dict(type="texte", name="justif", lignes=3,
                  exemple="Je choisis le frein à disque parce qu'il freine presque aussi bien sous la pluie, et Léa descend des côtes avec ses enfants.",
                  label="Justifie ton choix en une phrase&nbsp;: dis quel frein, et pourquoi il convient à la situation de Léa.",
                  criteres=[dict(label="ta phrase nomme le frein choisi", motifs=["disque"],
                                 manque="Nomme le frein que tu choisis : lequel freine bien sous la pluie ?"),
                            dict(label="ta phrase parle de la pluie", motifs=["pluie", "pleu", "mouill", "humid", r"\beau\b"],
                                 manque="Parle de la pluie : c'est ce qui départage les deux freins."),
                            dict(label="ta phrase parle des côtes ou de la charge (les enfants, les courses)",
                                 motifs=["cote", "descente", "pente", "descend", "charge", "enfant", "lourd", "poids", "course"],
                                 manque="Parle de la situation de Léa : les côtes à descendre, ou ce qu'elle transporte.")],
                  etayage=["Je choisis le frein à … parce que …",
                           "Sous la pluie, ce frein … ; et comme Léa descend des côtes avec …"])],
    aides=["<p>Pour chaque propriété, demande-toi <b>où</b> chaque frein frotte&nbsp;: sur la jante, au bord de la roue, ou sur un "
           "disque, au centre. Puis lis la situation de Léa&nbsp;: quelle propriété compte le plus pour elle&nbsp;?</p>",
           "<p>Pluie → le pneu projette l'eau sur la jante → les patins glissent → le disque, plus à l'abri, freine mieux → <b>disque</b>.<br>"
           "User la jante → seuls les patins frottent dessus → <b>patins</b>.<br>"
           "Prix et réglage → le frein à patins a moins de pièces → plus simple et moins cher → <b>patins</b> (et le disque coûte plus).<br>"
           "Frottement → les deux → c'est le même phénomène, à deux endroits différents.<br>"
           "Léa → pluie + côtes + enfants dans le bac → le freinage sous la pluie compte plus que le prix → <b>frein à disque</b>.</p>"],
    jumeau=dict(consigne="Pour sécher les mains, les toilettes du collège peuvent avoir un sèche-mains à air chaud ou un distributeur "
                         "d'essuie-mains en papier. Quelle est la fonction&nbsp;? Donne un avantage de chaque principe.",
                correction="Fonction&nbsp;: <b>sécher les mains</b>. Air chaud → le principe est d'évaporer l'eau → aucun déchet, mais il "
                           "consomme de l'électricité. Papier → le principe est d'absorber l'eau → rapide et silencieux, mais il fait des "
                           "déchets. Le choix dépend de la situation (budget, déchets, bruit)."),
    correction=[
        "<b>Sous la pluie</b> → le disque, au centre, est loin de l'eau projetée par le pneu → <b>frein à disque</b>",
        "<b>User la jante</b> → seuls les patins frottent sur la jante → <b>frein à patins</b>",
        "<b>Plus cher</b> → disque, plaquettes et pièces en plus → <b>frein à disque</b>",
        "<b>Frotter sur une pièce qui tourne</b> → la jante pour l'un, le disque pour l'autre → <b>les deux</b>&nbsp;: même phénomène, "
        "endroits différents",
        "<b>Réglage simple</b> → deux patins visibles, une clé suffit → <b>frein à patins</b>",
        "<b>Pour Léa</b> → pluie + côtes + enfants dans le bac → <b>le frein à disque</b>",
        "Pas le frein à patins → moins cher, mais il freine moins bien sous la pluie. Pas «&nbsp;aucun&nbsp;» → un vélo-cargo chargé "
        "accélère seul dans une descente. Pas «&nbsp;n'importe lequel&nbsp;» → même phénomène ne veut pas dire même résultat.",
        "<b>Une phrase attendue&nbsp;:</b> «&nbsp;Je choisis le <b>frein à disque</b>, parce qu'il freine presque aussi bien <b>sous la "
        "pluie</b>, et Léa <b>descend des côtes</b> avec ses enfants.&nbsp;»",
        ("conclusion", "Deux principes pour une même fonction → deux cases reliées par «&nbsp;ou&nbsp;». On ne choisit pas «&nbsp;le "
                       "meilleur&nbsp;» en général&nbsp;: on choisit celui qui convient à <b>la situation</b>."),
    ],
    retenir="une même fonction technique peut être réalisée par plusieurs <b>principes techniques</b>. On les compare par leurs "
            "avantages et leurs inconvénients, puis on choisit selon la situation (ici&nbsp;: la pluie, les côtes, la charge).",
    piege="croire que deux freins qui utilisent le même phénomène (le frottement) se valent&nbsp;: l'endroit où ils frottent change "
          "tout sous la pluie.",
)

# ─────────────────────────────────────────────────────────────────────────────
# 4e
# ─────────────────────────────────────────────────────────────────────────────
CAT_FT_JARDIN = [("humidite", FT_JARDIN[0]), ("decider", FT_JARDIN[1]), ("envoyer", FT_JARDIN[2]),
                 ("vanne", FT_JARDIN[3]), ("circuler", FT_JARDIN[4]), ("stocker", FT_JARDIN[5])]

E4 = dict(
    id="e4", titre="Le FAST du jardin : qui fait quoi ?", code="4e_C4.4", duree=18,
    objectif="associer chaque constituant du système d'arrosage à sa fonction technique, puis repérer ceux qui forment la chaîne "
             "d'information.",
    production="sept constituants reliés à leur fonction, et quatre constituants placés dans la chaîne d'information (ou hors d'elle).",
    mots=[SIGLE, MOT_FT,
          ("constituant", "un élément de l'objet&nbsp;: une pièce, un composant. Dans le FAST, c'est une solution technique."),
          ("chaîne d'information", "les constituants qui s'occupent de l'information&nbsp;: ils l'<b>acquièrent</b>, la <b>traitent</b> "
           "et la <b>communiquent</b>."),
          ("acquérir", "prendre une information sur le monde (une mesure, une présence). C'est le rôle d'un capteur."),
          ("traiter", "comparer, calculer, décider à partir des informations. C'est le rôle de la carte programmable."),
          ("communiquer", "envoyer une information à une personne ou à un autre appareil."),
          ("chaîne d'énergie", "les constituants qui alimentent, stockent, distribuent, convertissent et transmettent l'énergie pour "
           "agir sur le monde."),
          MOT_LED,
          ("électrovanne", "un robinet commandé par un signal électrique&nbsp;: il s'ouvre ou se ferme sur ordre."),
          ("module Wi-Fi", "un composant qui envoie et reçoit des informations sans fil, par ondes radio, comme une box Internet."),
          ("seuil", "la valeur à partir de laquelle on décide d'agir (ici&nbsp;: «&nbsp;terre trop sèche&nbsp;»).")],
    documents=[dict(svg=JARDIN_A_RELIER, legende="Le FAST du système d'arrosage&nbsp;: les fonctions techniques sont là, les solutions "
                                                 "sont à retrouver.",
                    description="<p>Fonction d'usage&nbsp;: <b>arroser les plantes quand la terre est sèche</b>. Six fonctions "
                                "techniques&nbsp;: mesurer l'humidité du sol&nbsp;; décider quand arroser&nbsp;; envoyer l'état au "
                                "smartphone&nbsp;; laisser passer l'eau ou la bloquer&nbsp;; faire circuler l'eau jusqu'aux bacs&nbsp;; "
                                "stocker l'eau de pluie. Chaque case de solution porte un point d'interrogation.</p>")],
    intro="<p>Le jardin partagé du collège a un <b>système d'arrosage connecté</b>. Le club jardin l'a présenté en six phrases. "
          "Chaque phrase cache un couple&nbsp;: <b>un constituant</b> et <b>ce qu'il fait</b>.</p>"
          "<ol><li>«&nbsp;Dans chaque bac, un capteur d'humidité planté dans la terre mesure l'eau qu'elle contient.&nbsp;»</li>"
          "<li>«&nbsp;La carte programmable compare cette mesure au seuil choisi par la gardienne, et décide quand arroser.&nbsp;»</li>"
          "<li>«&nbsp;Le module Wi-Fi envoie l'état du jardin au smartphone de la gardienne.&nbsp;»</li>"
          "<li>«&nbsp;Sur ordre de la carte, l'électrovanne s'ouvre et laisse passer l'eau, ou se ferme et la bloque.&nbsp;»</li>"
          "<li>«&nbsp;La pompe pousse l'eau dans les tuyaux, qui la font circuler jusqu'aux bacs.&nbsp;»</li>"
          "<li>«&nbsp;La cuve recueille l'eau de pluie qui tombe sur le toit du préau.&nbsp;»</li></ol>",
    consigne="<p>Un <b>constituant</b>, c'est un élément de l'objet&nbsp;: dans le diagramme FAST, c'est une <b>solution technique</b>. "
             "<b>Pour chaque constituant, choisis la fonction technique qu'il réalise</b>&nbsp;: tu remplis ainsi les cases «&nbsp;?&nbsp;» "
             "du FAST. Chaque fonction reçoit au moins un constituant&nbsp;; l'une d'elles en reçoit <b>deux</b>.</p>"
             "<p>Puis <b>place quatre constituants dans la chaîne d'information</b>&nbsp;: <b>acquérir</b> (prendre une information), "
             "<b>traiter</b> (comparer, décider) ou <b>communiquer</b> (envoyer l'information) — ou bien <b>hors de cette chaîne</b>, "
             "s'il agit sur l'eau au lieu de s'occuper d'information.</p>",
    critere="onze réponses justes, et tu sais dire pourquoi l'électrovanne n'est pas dans la chaîne d'information.",
    widgets=[dict(type="classer", name="ft", categories=CAT_FT_JARDIN,
                  items=[("Le capteur d'humidité du sol réalise…", "humidite", "Le capteur : relis la phrase 1, que mesure-t-il ?"),
                         ("La carte programmable réalise…", "decider", "La carte : relis la phrase 2, quel est son verbe ?"),
                         ("Le module Wi-Fi réalise…", "envoyer", "Le module Wi-Fi : relis la phrase 3, à qui envoie-t-il ?"),
                         ("L'électrovanne réalise…", "vanne", "L'électrovanne : relis la phrase 4, que fait-elle de l'eau ?"),
                         ("La pompe réalise…", "circuler", "La pompe : relis la phrase 5."),
                         ("Les tuyaux réalisent…", "circuler", "Les tuyaux : relis la phrase 5. Une fonction peut demander deux constituants."),
                         ("La cuve réalise…", "stocker", "La cuve : relis la phrase 6, que garde-t-elle ?")]),
             dict(type="classer", name="chaine",
                  categories=[("acquerir", "chaîne d'information — acquérir"), ("traiter", "chaîne d'information — traiter"),
                              ("communiquer", "chaîne d'information — communiquer"),
                              ("hors", "hors de la chaîne d'information (il agit sur l'eau)")],
                  items=[("Le capteur d'humidité du sol", "acquerir", "Le capteur prend une information sur la terre : quel verbe de la chaîne ?"),
                         ("La carte programmable", "traiter", "La carte compare et décide : quel verbe de la chaîne ?"),
                         ("Le module Wi-Fi", "communiquer", "Le module Wi-Fi envoie l'information à la gardienne : quel verbe ?"),
                         ("L'électrovanne", "hors", "L'électrovanne reçoit un ordre, mais que fait-elle : traiter une information, ou agir sur l'eau ?")])],
    aides=["<p>Dans chaque phrase, cherche le <b>verbe</b> qui suit le constituant&nbsp;: il te donne sa fonction. Pour la chaîne "
           "d'information, demande-toi&nbsp;: ce constituant s'occupe-t-il d'une <b>information</b> (la prendre, la comparer, "
           "l'envoyer), ou agit-il sur l'<b>eau</b>&nbsp;?</p>",
           "<p>Capteur → «&nbsp;mesure l'eau&nbsp;» → mesurer l'humidité du sol → il <b>prend</b> une information → <b>acquérir</b>.<br>"
           "Carte → «&nbsp;compare… décide&nbsp;» → décider quand arroser → <b>traiter</b>.<br>"
           "Module Wi-Fi → «&nbsp;envoie&nbsp;» → envoyer l'état au smartphone → <b>communiquer</b>.<br>"
           "Électrovanne → «&nbsp;laisse passer l'eau&nbsp;» → elle reçoit un ordre, mais elle agit sur l'eau → <b>hors</b> de la chaîne "
           "d'information (elle est dans la chaîne d'énergie&nbsp;: elle distribue).<br>"
           "Pompe <b>et</b> tuyaux → font circuler l'eau (une fonction, deux constituants)&nbsp;; cuve → stocke l'eau de pluie.</p>"],
    jumeau=dict(consigne="Dans le lampadaire intelligent de la rue du collège, quelle fonction technique réalise le <b>détecteur de "
                         "mouvement</b>, et dans quel bloc de la chaîne d'information est-il&nbsp;? Même question pour le <b>bloc de LED</b>.",
                correction="Détecteur de mouvement → <b>détecter un passant</b> → il prend une information → <b>acquérir</b>. Bloc de LED → "
                           "<b>produire la lumière</b> → il agit sur le monde, il ne s'occupe pas d'information → <b>hors</b> de la chaîne "
                           "d'information (chaîne d'énergie&nbsp;: il convertit l'énergie électrique en lumière)."),
    correction=[
        figure_corrigee(JARDIN_CORRIGE, "Le FAST du système d'arrosage, complet."),
        "<b>Capteur d'humidité du sol</b> → phrase 1&nbsp;: «&nbsp;mesure l'eau&nbsp;» → <b>mesurer l'humidité du sol</b> → <b>acquérir</b>",
        "<b>Carte programmable</b> → phrase 2&nbsp;: «&nbsp;compare… décide&nbsp;» → <b>décider quand arroser</b> → <b>traiter</b>",
        "<b>Module Wi-Fi</b> → phrase 3&nbsp;: «&nbsp;envoie&nbsp;» → <b>envoyer l'état au smartphone</b> → <b>communiquer</b>",
        "<b>Électrovanne</b> → phrase 4&nbsp;: «&nbsp;laisse passer l'eau&nbsp;» → <b>laisser passer l'eau ou la bloquer</b> → <b>hors</b> de "
        "la chaîne d'information",
        "Pourquoi hors&nbsp;? → elle reçoit l'ordre de la carte, mais elle ne le traite pas&nbsp;: elle <b>agit</b> sur l'eau → elle "
        "appartient à la chaîne d'énergie (elle distribue)",
        "<b>Pompe et tuyaux</b> → phrase 5 → tous les deux pour <b>faire circuler l'eau jusqu'aux bacs</b>&nbsp;: une fonction peut "
        "demander deux constituants",
        "<b>Cuve</b> → phrase 6 → <b>stocker l'eau de pluie</b>. Ni la pompe, ni les tuyaux, ni la cuve ne s'occupent d'information.",
        ("conclusion", "Le FAST relie chaque constituant à sa fonction. Ceux qui <b>acquièrent</b>, <b>traitent</b> et <b>communiquent</b> "
                       "une information forment la chaîne d'information&nbsp;; ceux qui agissent sur l'eau sont dans la chaîne d'énergie."),
    ],
    retenir="dans le FAST, chaque <b>constituant</b> est la solution d'une fonction technique. La <b>chaîne d'information</b> réunit "
            "ceux qui <b>acquièrent</b> (capteur), <b>traitent</b> (carte programmable) et <b>communiquent</b> (module Wi-Fi) une information.",
    piege="mettre l'électrovanne dans la chaîne d'information parce qu'elle «&nbsp;reçoit un ordre&nbsp;»&nbsp;: elle ne traite rien, elle "
          "agit sur l'eau.",
)

OPTIONS_E5 = [NOUVELLE_ST, "le capteur d'humidité du sol", "une deuxième électrovanne", "un second module Wi-Fi"]

E5 = dict(
    id="e5", titre="Ajouter une fonction au jardin", code="4e_C7.2", duree=15,
    objectif="ajouter au FAST la branche d'une nouvelle fonction&nbsp;: écrire la fonction technique qui manque, lui choisir une "
             "solution, et réutiliser ce qui existe déjà.",
    production="la nouvelle fonction technique écrite dans le FAST, sa solution, et ce qui change dans les branches déjà là.",
    mots=[MOT_FT,
          ("branche", "une ligne du FAST&nbsp;: une fonction technique et sa (ou ses) solution(s)."),
          ("capteur de niveau d'eau", "un capteur placé dans la cuve&nbsp;: un flotteur monte et descend avec l'eau et dit à la carte "
           "combien il en reste."),
          ("réutiliser", "confier une nouvelle fonction à une solution déjà présente, au lieu d'ajouter une pièce."),
          ("programme", "la suite d'instructions que suit la carte programmable&nbsp;: c'est lui qui compare et décide.")],
    intro="<p>Pendant les vacances, la cuve s'est vidée sans que personne le sache, et les plantes ont souffert. La gardienne, "
          "Mme Joseph, demande une <b>nouvelle fonction</b>&nbsp;: <b>«&nbsp;prévenir la gardienne quand la cuve est presque "
          "vide&nbsp;»</b>.</p>"
          "<p>Pour la prévenir, le système doit d'abord <b>savoir</b> combien d'eau reste dans la cuve&nbsp;: aucune branche du FAST ne "
          "le fait encore. La branche du bas est vide&nbsp;: c'est à toi de la construire. Ce que tu écris s'affiche dans le schéma.</p>",
    consigne="<p>Une <b>fonction technique</b> dit ce que le système doit <b>faire</b>, avec un verbe à l'infinitif&nbsp;; la "
             "<b>solution</b> est l'élément qui le fait.</p><ol>"
             "<li><b>Écris la fonction technique qui manque</b> (ce qu'il faut faire, pas l'objet qui le fait).</li>"
             "<li><b>Choisis sa solution technique.</b></li>"
             "<li><b>Trouve</b> la solution déjà présente qui enverra l'alerte, et <b>ce qui doit changer</b> dans une branche déjà là.</li></ol>",
    critere="ta fonction commence par un verbe et parle de l'eau de la cuve, sans nommer d'objet&nbsp;; la solution est juste&nbsp;; tu "
            "réutilises le module Wi-Fi et tu vois que le programme de la carte change.",
    widgets=[dict(type="texte", name="ft", lignes=2, miroir="fa-e5-ft", minCar=10,
                  exemple="mesurer le niveau d'eau de la cuve",
                  label="La fonction technique qui manque (elle s'écrit dans la case en pointillés du FAST)",
                  criteres=[dict(label="elle commence par un verbe à l'infinitif (mesurer, surveiller, détecter…)",
                                 motifs=[r"^\w+(er|ir|re)\b"],
                                 manque="Commence par un verbe à l'infinitif : « mesurer… », « surveiller… », « détecter… »."),
                            dict(label="elle dit sur quoi porte l'action (l'eau de la cuve, son niveau)",
                                 motifs=["niveau", "cuve", r"\beau\b", "reste", "reserve", "quantite", "volume", "remplissage"],
                                 manque="Dis sur quoi porte la fonction : l'eau qui reste dans la cuve.")],
                  interdits=[dict(motifs=["capteur", "flotteur", "module", r"\bcarte\b", "sonde", "electrovanne"],
                                  message="Tu as écrit le nom d'un objet : il ira dans la case de droite. La case de fonction dit seulement ce qu'il faut faire."),
                             dict(motifs=[r"^(prevenir|alerter|avertir|envoyer|informer)\b"],
                                  message="Prévenir la gardienne, c'est la demande de Mme Joseph, et le module Wi-Fi saura envoyer le message. Ce qui manque, c'est ce que le système doit SAVOIR avant de prévenir.")],
                  etayage=["Pour prévenir la gardienne, le système doit d'abord … le … d'eau de la cuve.",
                           "mesurer … / surveiller … / détecter …"]),
             dict(type="slots", intro=figure_vivante(JARDIN_AJOUT, "Le FAST du système d'arrosage, avec la nouvelle branche en bas. "
                                                                   "Ta fonction et ta solution s'y écrivent."),
                  slots=[dict(name="st", cible="fa-e5-st", legende="La solution de la nouvelle branche",
                              options=OPTIONS_E5, bonnes=[NOUVELLE_ST],
                              indice="La solution : quel capteur mesure l'eau DANS la cuve, et non dans la terre ?")]),
             dict(type="choix", name="envoi", legende="Quelle solution, <b>déjà dans le FAST</b>, enverra l'alerte au smartphone&nbsp;?",
                  options=[("wifi", "Le module Wi-Fi&nbsp;: il envoie déjà l'état du jardin au smartphone."),
                           ("carte", "La carte programmable&nbsp;: elle envoie elle-même les messages."),
                           ("vanne", "L'électrovanne&nbsp;: elle se ferme quand la cuve est vide."),
                           ("aucune", "Aucune&nbsp;: il faut ajouter un téléphone au jardin.")],
                  bonne="wifi",
                  retours={"wifi": "Oui : une même solution peut servir deux fonctions. Le module Wi-Fi envoie déjà des messages ; il en enverra un de plus.",
                           "carte": "La carte décidera qu'il faut prévenir, mais elle n'a pas de liaison sans fil : c'est le module Wi-Fi qui envoie.",
                           "vanne": "L'électrovanne agit sur l'eau : elle ne prévient personne.",
                           "aucune": "Le module Wi-Fi sait déjà envoyer au smartphone : inutile d'ajouter un appareil."}),
             dict(type="choix", name="change", legende="Pour que l'alerte parte, que faut-il changer dans une branche <b>déjà là</b>&nbsp;?",
                  options=[("programme", "Le programme de la carte&nbsp;: il doit comparer le niveau d'eau à un seuil et déclencher le message."),
                           ("pompe", "La pompe&nbsp;: elle doit pomper moins fort quand la cuve se vide."),
                           ("rien", "Rien&nbsp;: le capteur de niveau envoie l'alerte tout seul au smartphone."),
                           ("cuve", "La cuve&nbsp;: il faut la remplacer par une cuve plus grande.")],
                  bonne="programme",
                  retours={"programme": "Oui : la carte traite la nouvelle mesure. Son programme reçoit une nouvelle condition : « si le niveau est sous le seuil, alors envoyer un message ».",
                           "pompe": "Pomper moins fort ne prévient personne : la demande est d'alerter la gardienne.",
                           "rien": "Un capteur acquiert une mesure, il ne décide pas et n'envoie rien : il faut la carte et le module Wi-Fi.",
                           "cuve": "Une cuve plus grande se viderait plus tard, mais sans prévenir personne : ce n'est pas la fonction demandée."})],
    aides=["<p>Lis la demande de Mme Joseph et demande-toi&nbsp;: <b>que doit savoir le système</b> pour pouvoir la prévenir&nbsp;? "
           "C'est la fonction qui manque. Puis cherche, dans les branches déjà là, ce qui sait déjà <b>envoyer</b> au smartphone.</p>",
           "<p>Prévenir quand la cuve est presque vide → il faut connaître l'eau qui reste → aucune branche ne la mesure.<br>"
           "→ Fonction&nbsp;: «&nbsp;<b>mesurer le niveau d'eau de la cuve</b>&nbsp;» (un verbe, puis sur quoi il porte).<br>"
           "→ Solution&nbsp;: <b>le capteur de niveau d'eau</b> (le capteur d'humidité mesure la terre, pas la cuve).<br>"
           "→ Envoyer&nbsp;: le <b>module Wi-Fi</b> le fait déjà → on le réutilise.<br>"
           "→ Décider&nbsp;: la carte doit comparer le niveau à un seuil → son <b>programme</b> change.</p>"],
    jumeau=dict(consigne="La mairie veut que le lampadaire intelligent «&nbsp;prévienne les services techniques quand sa batterie est "
                         "presque vide&nbsp;». Quelle fonction technique manque&nbsp;? Le lampadaire sait-il déjà envoyer un message&nbsp;?",
                correction="Il manque «&nbsp;<b>mesurer la charge de la batterie</b>&nbsp;» → une solution qui mesure sa tension. Mais ici, "
                           "aucune branche ne sait envoyer de message&nbsp;: il faut <b>une deuxième branche</b>, «&nbsp;envoyer l'alerte aux "
                           "services techniques&nbsp;», avec un module de communication sans fil. Et le programme de la carte change."),
    correction=[
        figure_corrigee(JARDIN_AJOUT_CORRIGE, "Le FAST du système d'arrosage, avec la nouvelle branche (en bas)."),
        "<b>Ce qui manque</b> → pour prévenir, il faut savoir combien d'eau reste → aucune branche ne le mesure",
        "<b>La fonction</b> → «&nbsp;<b>mesurer le niveau d'eau de la cuve</b>&nbsp;» → un verbe à l'infinitif, puis sur quoi il porte "
        "(«&nbsp;surveiller le niveau de la cuve&nbsp;» convient aussi)",
        "Refusé&nbsp;: «&nbsp;un capteur de niveau&nbsp;» dans la case de fonction → c'est un objet, il va à droite",
        "<b>La solution</b> → <b>le capteur de niveau d'eau</b> → un flotteur suit l'eau de la cuve",
        "Pas le capteur d'humidité du sol → il mesure la terre. Pas une deuxième électrovanne → elle agit sur l'eau, elle ne mesure rien. "
        "Pas un second module Wi-Fi → on n'a pas besoin d'envoyer, mais de mesurer.",
        "<b>Envoyer l'alerte</b> → le <b>module Wi-Fi</b>, déjà là → une solution peut servir deux fonctions",
        "<b>Ce qui change</b> → le <b>programme</b> de la carte&nbsp;: «&nbsp;si le niveau est sous le seuil, alors envoyer un message à "
        "la gardienne&nbsp;»",
        ("conclusion", "Ajouter une fonction, c'est ajouter une <b>branche</b> au FAST&nbsp;: la fonction qui manque, sa solution — et "
                       "réutiliser ce qui existe (le module Wi-Fi, la carte et son programme)."),
    ],
    retenir="pour ajouter une fonction, on écrit d'abord la <b>fonction technique</b> qui manque (un verbe), puis on lui choisit une "
            "<b>solution</b>&nbsp;; on réutilise ce qui existe déjà, et on dit ce qui change ailleurs (souvent le programme).",
    piege="écrire le nom d'un objet («&nbsp;un capteur de niveau&nbsp;») dans la case de fonction&nbsp;: la fonction dit ce qu'il faut "
          "faire, la solution dit avec quoi.",
)

# ─────────────────────────────────────────────────────────────────────────────
# 3e
# ─────────────────────────────────────────────────────────────────────────────
E6 = dict(
    id="e6", titre="Trouver les erreurs d'un FAST", code="3e_C7.2", duree=13,
    objectif="contrôler un FAST proposé par une équipe&nbsp;: chaque case de fonction a un verbe, chaque solution répond à sa "
             "fonction, chaque branche sert la fonction d'usage.",
    production="les trois erreurs repérées et leur correction.",
    mots=[SIGLE,
          ("anémomètre", "un capteur qui mesure la vitesse du vent."),
          MOT_LED,
          ("batterie 12 V", "une batterie de 12 volts&nbsp;: une très basse tension, sans danger au toucher. Elle stocke l'énergie du "
           "panneau solaire pour la nuit."),
          ("alternative", "plusieurs solutions possibles pour une même fonction, reliées par «&nbsp;ou&nbsp;»&nbsp;: on choisira plus tard.")],
    documents=[dict(svg=STATION_ERREURS, legende="Le FAST de la station d'alerte, tel que l'équipe l'a proposé. Il contient trois erreurs.",
                    description="<p>Fonction d'usage&nbsp;: <b>prévenir les habitants quand un cyclone approche</b>. Six branches&nbsp;:</p><ol>"
                                "<li>mesurer la vitesse du vent → l'anémomètre&nbsp;;</li>"
                                "<li>le programme d'alerte → la carte programmable&nbsp;;</li>"
                                "<li>diffuser l'alerte aux habitants → la sirène, ou un message sur les téléphones, ou un panneau lumineux à LED&nbsp;;</li>"
                                "<li>stocker l'énergie pour la nuit → le panneau solaire&nbsp;;</li>"
                                "<li>capter l'énergie du soleil → le panneau solaire&nbsp;;</li>"
                                "<li>éclairer la rue la nuit → le bloc de LED.</li></ol>")],
    intro="<p>Le quartier prépare une <b>station d'alerte cyclonique</b>&nbsp;: elle mesure le vent et prévient les habitants quand un "
          "cyclone approche. Elle fonctionne seule, en très basse tension, avec un panneau solaire et une batterie. Une équipe de 3e "
          "a proposé son <b>diagramme FAST</b> (de l'anglais <i lang=\"en\">Function Analysis System Technique</i>, «&nbsp;technique "
          "d'analyse fonctionnelle&nbsp;»).</p>"
          "<p>Avant de fabriquer quoi que ce soit, on le <b>contrôle</b> avec trois questions&nbsp;: chaque case de fonction commence-t-elle "
          "par un verbe&nbsp;? chaque solution répond-elle au «&nbsp;comment&nbsp;?&nbsp;» de sa fonction&nbsp;? chaque branche "
          "ramène-t-elle, par «&nbsp;pourquoi&nbsp;?&nbsp;», à la fonction d'usage&nbsp;?</p>",
    consigne="<p><b>Coche les trois endroits du FAST qui contiennent une erreur.</b> Puis, pour chacun, <b>choisis la correction</b>. "
             "Attention&nbsp;: une branche qui a plusieurs solutions reliées par «&nbsp;ou&nbsp;» n'est pas forcément une erreur.</p>",
    critere="exactement les trois erreurs cochées, et quatre corrections justes.",
    widgets=[dict(type="cases", name="err", legende="Les endroits du FAST qui contiennent une erreur",
                  options=[("b2", "La case de fonction de la branche 2&nbsp;: «&nbsp;le programme d'alerte&nbsp;»"),
                           ("b1", "La branche 1&nbsp;: «&nbsp;mesurer la vitesse du vent&nbsp;» → l'anémomètre"),
                           ("b4", "La case de solution de la branche 4&nbsp;: «&nbsp;le panneau solaire&nbsp;», en face de «&nbsp;stocker l'énergie pour la nuit&nbsp;»"),
                           ("b5", "La case de solution de la branche 5&nbsp;: «&nbsp;le panneau solaire&nbsp;», en face de «&nbsp;capter l'énergie du soleil&nbsp;»"),
                           ("b3", "La branche 3&nbsp;: trois solutions reliées par «&nbsp;ou&nbsp;»"),
                           ("b6", "La branche 6&nbsp;: «&nbsp;éclairer la rue la nuit&nbsp;» → le bloc de LED")],
                  bonnes=["b2", "b4", "b6"],
                  retours={"b2": "Oui : « le programme d'alerte » est un nom, pas une action. Une case de fonction commence par un verbe.",
                           "b1": "Cette branche est juste : un verbe à l'infinitif, et l'anémomètre mesure bien la vitesse du vent.",
                           "b4": "Oui : le panneau solaire capte l'énergie, il ne la garde pas. La nuit, il ne donne plus rien.",
                           "b5": "Cette case est juste : capter l'énergie du soleil, c'est bien le rôle du panneau solaire.",
                           "b3": "Ce n'est pas une erreur : un FAST peut proposer plusieurs solutions pour une fonction. On choisira ensuite.",
                           "b6": "Oui : pourquoi éclairer la rue ? Ça ne ramène pas à « prévenir les habitants » : cette branche vient d'un autre objet."},
                  indice="Pose les trois questions à chaque branche : un verbe ? une solution qui répond au « comment ? » ? un « pourquoi ? » qui ramène à la fonction d'usage ?"),
             dict(type="classer", name="fix",
                  categories=[("verbe", "écrire un verbe&nbsp;: «&nbsp;décider du niveau d'alerte&nbsp;»"),
                              ("batterie", "remplacer la solution par «&nbsp;la batterie 12 V&nbsp;»"),
                              ("supprimer", "supprimer la branche&nbsp;: elle ne sert pas la fonction d'usage"),
                              ("garder", "garder tel quel&nbsp;: ce n'est pas une erreur")],
                  items=[("Branche 2 — «&nbsp;le programme d'alerte&nbsp;»", "verbe", "Branche 2 : que doit FAIRE la carte avec la vitesse du vent ?"),
                         ("Branche 4 — «&nbsp;le panneau solaire&nbsp;» pour stocker l'énergie", "batterie", "Branche 4 : quel élément garde l'énergie pour la nuit ?"),
                         ("Branche 6 — «&nbsp;éclairer la rue la nuit&nbsp;»", "supprimer", "Branche 6 : pourquoi éclairer la rue ? Est-ce le service de la station ?"),
                         ("Branche 3 — trois solutions reliées par «&nbsp;ou&nbsp;»", "garder", "Branche 3 : un FAST a-t-il le droit de proposer plusieurs solutions ?")])],
    aides=["<p>Passe chaque branche aux trois questions, dans l'ordre&nbsp;: la case de fonction commence-t-elle par un <b>verbe</b>&nbsp;? "
           "La solution répond-elle à «&nbsp;<b>comment&nbsp;?</b>&nbsp;»&nbsp;? En lisant vers la gauche («&nbsp;<b>pourquoi&nbsp;?</b>&nbsp;»), "
           "arrives-tu à «&nbsp;prévenir les habitants&nbsp;»&nbsp;?</p>",
           "<p>Branche 2 → «&nbsp;le programme d'alerte&nbsp;» → c'est un nom → erreur → que fait la carte&nbsp;? elle <b>décide du niveau "
           "d'alerte</b>.<br>"
           "Branche 4 → comment stocker l'énergie pour la nuit&nbsp;? → pas avec le panneau, qui capte → <b>la batterie 12 V</b>.<br>"
           "Branche 6 → pourquoi éclairer la rue&nbsp;? → ça ne prévient personne d'un cyclone → la branche vient du FAST du lampadaire → "
           "<b>on la supprime</b>.<br>"
           "Branche 3 → trois solutions avec «&nbsp;ou&nbsp;» → c'est une alternative, permise → <b>on garde</b>, et on choisira.</p>"],
    jumeau=dict(consigne="Dans le FAST d'un robot aspirateur, une équipe a écrit&nbsp;: «&nbsp;le capteur d'obstacle&nbsp;» → «&nbsp;le "
                         "capteur à ultrasons&nbsp;» et «&nbsp;stocker l'énergie&nbsp;» → «&nbsp;le chargeur&nbsp;». Trouve les deux erreurs.",
                correction="«&nbsp;Le capteur d'obstacle&nbsp;» est un nom dans une case de fonction → il faut un verbe&nbsp;: <b>détecter les "
                           "obstacles</b>. Le chargeur reste à la maison et recharge&nbsp;; ce qui stocke l'énergie dans le robot, c'est <b>la "
                           "batterie</b>."),
    correction=[
        figure_corrigee(STATION, "Le FAST de la station d'alerte, corrigé."),
        "<b>Erreur 1, branche 2</b> → «&nbsp;le programme d'alerte&nbsp;» est un nom → une case de fonction commence par un verbe → "
        "<b>décider du niveau d'alerte</b>",
        "<b>Erreur 2, branche 4</b> → comment stocker l'énergie pour la nuit&nbsp;? → le panneau capte, il ne garde rien → <b>la batterie 12 V</b>",
        "<b>Erreur 3, branche 6</b> → pourquoi éclairer la rue&nbsp;? → cela ne ramène pas à «&nbsp;prévenir les habitants&nbsp;» → la "
        "branche vient d'un autre objet → <b>on la supprime</b>",
        "<b>Pas d'erreur, branche 3</b> → trois solutions reliées par «&nbsp;ou&nbsp;» → une alternative est permise dans un FAST → on garde, "
        "et on choisira (exercice suivant)",
        "<b>Pas d'erreur, branches 1 et 5</b> → un verbe, et une solution qui répond au «&nbsp;comment&nbsp;?&nbsp;». Le panneau solaire "
        "apparaissait deux fois&nbsp;: c'était l'indice que l'une des deux cases était fausse.",
        ("conclusion", "Trois questions contrôlent un FAST&nbsp;: <b>un verbe</b> dans chaque case de fonction, <b>une solution qui répond "
                       "au «&nbsp;comment&nbsp;?&nbsp;»</b>, et <b>un «&nbsp;pourquoi&nbsp;?&nbsp;» qui ramène à la fonction d'usage</b>."),
    ],
    retenir="avant de fabriquer, on contrôle le FAST&nbsp;: une case de fonction commence par un <b>verbe</b>, une solution répond au "
            "«&nbsp;<b>comment&nbsp;?</b>&nbsp;» de sa fonction, et chaque branche ramène, par «&nbsp;<b>pourquoi&nbsp;?</b>&nbsp;», à la fonction d'usage.",
    piege="prendre pour une erreur une branche à plusieurs solutions reliées par «&nbsp;ou&nbsp;»&nbsp;: c'est une alternative, permise, "
          "qu'on tranchera ensuite.",
)

OUI_NON = [("oui", "oui"), ("partie", "en partie"), ("non", "non")]

E7 = dict(
    id="e7", titre="Trois solutions pour alerter : arbitrer", code="3e_C7.2", duree=20,
    objectif="comparer trois solutions d'une même fonction technique selon des critères, distinguer un critère qui élimine d'un "
             "critère qui départage, puis argumenter un choix ou une combinaison.",
    production="un tableau de comparaison complété, la place du critère «&nbsp;très basse tension&nbsp;», et un court argumentaire.",
    mots=[("critère", "ce que l'on regarde pour comparer des solutions (ici&nbsp;: marche-t-elle sans réseau&nbsp;? la nuit&nbsp;?)."),
          ("arbitrer", "choisir entre plusieurs solutions en pesant leurs avantages et leurs inconvénients, et dire pourquoi."),
          ("combinaison", "garder deux solutions à la fois, quand chacune couvre le point faible de l'autre."),
          ("réseau téléphonique", "les antennes qui relient les téléphones portables. Un cyclone peut les abîmer ou les priver "
           "d'électricité."),
          ("très basse tension", "une tension assez faible pour ne pas être dangereuse au toucher (ici, 12 volts). C'est une exigence "
           "impérative de la station&nbsp;: le 230 volts, sous la pluie d'un cyclone, serait un danger mortel."),
          ("exigence impérative", "une exigence dont on ne peut pas s'écarter (flexibilité F0&nbsp;: nulle)&nbsp;: une solution qui ne la "
           "remplit pas est écartée.")],
    documents=[dict(svg=STATION, legende="Le FAST corrigé de la station&nbsp;: la fonction «&nbsp;diffuser l'alerte aux habitants&nbsp;» "
                                         "a trois solutions possibles.",
                    description="<p>Fonction d'usage&nbsp;: <b>prévenir les habitants quand un cyclone approche</b>. Cinq branches&nbsp;: "
                                "mesurer la vitesse du vent → l'anémomètre&nbsp;; décider du niveau d'alerte → la carte programmable&nbsp;; "
                                "<b>diffuser l'alerte aux habitants → la sirène, ou un message sur les téléphones, ou un panneau lumineux à "
                                "LED</b>&nbsp;; stocker l'énergie pour la nuit → la batterie 12 V&nbsp;; capter l'énergie du soleil → le "
                                "panneau solaire.</p>")],
    intro="<p>L'équipe doit maintenant <b>choisir</b> comment diffuser l'alerte. Les trois solutions du FAST, branchées sur la station, "
          "sont toutes alimentées en <b>très basse tension</b> (12 volts) par la batterie et le panneau solaire&nbsp;: une sirène 12 V, un "
          "petit module qui envoie un message sur les téléphones du quartier, un panneau lumineux à LED.</p>"
          '<div class="defile"><table><caption>Le tableau de comparaison, à compléter</caption>'
          "<tr><th>Critère</th><th>La sirène</th><th>Le message sur les téléphones</th><th>Le panneau lumineux</th></tr>"
          "<tr><td>A — Elle marche encore si le réseau téléphonique tombe</td><td>?</td><td>?</td><td>?</td></tr>"
          "<tr><td>B — Elle prévient des habitants qui dorment, la nuit</td><td>?</td><td>?</td><td>?</td></tr>"
          "<tr><td>C — Elle atteint une personne sourde ou malentendante</td><td>?</td><td>?</td><td>?</td></tr>"
          "<tr><td>D — Elle peut être alimentée en très basse tension par la batterie de la station</td><td>oui</td><td>oui</td><td>oui</td></tr>"
          "</table></div>",
    consigne="<p>Un <b>critère</b> est ce que l'on regarde pour comparer. <b>Complète le tableau</b>&nbsp;: pour chaque solution et chaque "
             "critère, oui, en partie ou non. Puis dis à quoi sert le critère D, que toutes les solutions remplissent. Enfin, "
             "<b>argumente</b>&nbsp;: quelle solution — ou quelle <b>combinaison</b> de deux solutions — l'équipe doit-elle fabriquer&nbsp;?</p>",
    critere="neuf cases justes, le bon rôle du critère D, et un argumentaire qui nomme ton choix, s'appuie sur au moins deux critères et "
            "dit une limite.",
    widgets=[dict(type="classer", name="tab", categories=OUI_NON,
                  items=[("A — La sirène, si le réseau téléphonique tombe", "oui", "A, sirène : a-t-elle besoin des antennes de téléphone ?"),
                         ("A — Le message sur les téléphones, si le réseau tombe", "non", "A, message : comment arrive-t-il sur le téléphone ?"),
                         ("A — Le panneau lumineux, si le réseau tombe", "oui", "A, panneau : est-il relié aux antennes de téléphone ?"),
                         ("B — La sirène, pour des habitants qui dorment", "oui", "B, sirène : un son fort réveille-t-il ?"),
                         ("B — Le message, pour des habitants qui dorment", "partie", "B, message : et si le téléphone est en silencieux, ou éteint ?"),
                         ("B — Le panneau lumineux, pour des habitants qui dorment", "non", "B, panneau : qui le regarde quand il dort, volets fermés ?"),
                         ("C — La sirène, pour une personne sourde", "non", "C, sirène : que perçoit une personne qui n'entend pas ?"),
                         ("C — Le message, pour une personne sourde", "oui", "C, message : un texte et une vibration demandent-ils d'entendre ?"),
                         ("C — Le panneau lumineux, pour une personne sourde", "oui", "C, panneau : un texte lumineux demande-t-il d'entendre ?")]),
             dict(type="choix", name="tbt", legende="Le critère D est rempli par les trois solutions. À quoi sert-il quand même&nbsp;?",
                  options=[("elimine", "Il élimine toute solution qui demanderait plus que la très basse tension&nbsp;: c'est une exigence impérative, pas un critère pour départager."),
                           ("inutile", "À rien&nbsp;: un critère que tout le monde remplit peut être effacé du cahier des charges."),
                           ("meilleur", "Il désigne la meilleure solution&nbsp;: celle qui consomme le moins."),
                           ("sirene", "Il montre que la sirène est la seule solution sûre.")],
                  bonne="elimine",
                  retours={"elimine": "Oui : un critère impératif ne départage pas, il écarte. Une sirène sur le 230 volts, sous la pluie d'un cyclone, serait éliminée d'office.",
                           "inutile": "Effacé, le critère ne protégerait plus contre une solution dangereuse proposée plus tard : il reste une exigence.",
                           "meilleur": "Le critère D dit « oui » ou « non », il ne classe pas les consommations : il ne désigne pas de meilleure solution.",
                           "sirene": "Les trois solutions remplissent le critère D : il ne met pas la sirène à part."}),
             dict(type="texte", name="arg", lignes=5,
                  exemple="Je choisis de combiner la sirène et le panneau lumineux, parce que la sirène réveille les habitants la nuit et "
                          "marche même si le réseau tombe, et le panneau prévient les personnes sourdes. Mais la sirène consomme beaucoup "
                          "d'énergie sur la batterie.",
                  label="Ton argumentaire&nbsp;: la solution ou la combinaison que tu choisis, les critères qui la justifient, et une limite qui reste.",
                  criteres=[dict(label="tu nommes ton choix (une solution ou deux)",
                                 motifs=["sirene", "message", "panneau", "telephone", r"\bsms\b"],
                                 manque="Nomme la solution (ou les deux solutions) que tu choisis."),
                            dict(label="tu t'appuies sur un critère du tableau (réseau, nuit, personne sourde)",
                                 motifs=["reseau", "antenne", "nuit", "dor", "reveil", "sourd", "malentend", "entend"],
                                 manque="Appuie-toi sur un critère du tableau : le réseau, la nuit, ou les personnes sourdes."),
                            dict(label="tu relies ton choix à ses raisons (parce que, car, donc…)",
                                 motifs=["parce", r"\bcar\b", "donc", "puisque", "grace", "comme", "ainsi", "pour que"],
                                 manque="Relie ton choix à ses raisons avec « parce que », « car », « donc »…"),
                            dict(label="tu dis une limite ou un point faible qui reste",
                                 motifs=["mais", "cependant", "pourtant", "limite", "inconvenient", "defaut", "faible", "par contre",
                                         "toutefois", "consomm", "sauf"],
                                 manque="Dis une limite qui reste : « mais… », un inconvénient de ton choix.")],
                  etayage=["Je choisis … (ou : je combine … et …), parce que …",
                           "D'après le critère …, cette solution … ; alors que …",
                           "Mais il reste une limite : …"])],
    aides=["<p>Pour chaque case du tableau, demande-toi <b>de quoi la solution a besoin</b> pour atteindre quelqu'un&nbsp;: des antennes de "
           "téléphone&nbsp;? une personne réveillée qui regarde&nbsp;? une personne qui entend&nbsp;? Pour l'argumentaire, cherche la "
           "solution qui a le moins de «&nbsp;non&nbsp;», puis celle qui comble ses «&nbsp;non&nbsp;».</p>",
           "<ul><li><b>A</b> → seul le message passe par les antennes → message&nbsp;: <b>non</b>&nbsp;; sirène et panneau, reliés à la "
           "station&nbsp;: <b>oui</b>.</li>"
           "<li><b>B</b> → un son fort réveille → sirène <b>oui</b>&nbsp;; un téléphone sonne s'il n'est pas en silencieux → message <b>en "
           "partie</b>&nbsp;; personne ne regarde un panneau en dormant → panneau <b>non</b>.</li>"
           "<li><b>C</b> → une personne sourde n'entend pas la sirène → <b>non</b>&nbsp;; elle lit un message ou un panneau → <b>oui</b>.</li>"
           "<li><b>D</b> → oui partout → il ne départage pas, il <b>élimine</b> ce qui demanderait le 230 volts.</li>"
           "<li><b>Argumentaire</b> → aucune solution n'a que des «&nbsp;oui&nbsp;» → la sirène a un seul «&nbsp;non&nbsp;» (C), que le "
           "panneau comble → sirène + panneau couvrent A, B et C → limite&nbsp;: deux appareils sur la même batterie.</li></ul>"],
    jumeau=dict(consigne="Pour la fonction «&nbsp;indiquer qu'une place de parking est libre&nbsp;», on hésite entre un voyant vert "
                         "au-dessus de chaque place et un affichage du nombre de places à l'entrée. Donne un critère qui départage, et un "
                         "critère qui élimine.",
                correction="Un critère qui <b>départage</b>&nbsp;: «&nbsp;l'automobiliste voit la place libre depuis l'allée&nbsp;» → voyant "
                           "<b>oui</b>, affichage <b>non</b> (il donne un nombre, pas l'endroit). Un critère qui <b>élimine</b>&nbsp;: «&nbsp;fonctionne "
                           "en très basse tension&nbsp;» → toute solution qui ne le remplit pas est écartée, quelles que soient ses qualités."),
    correction=[
        "<b>A, réseau tombé</b> → sirène <b>oui</b> (reliée à la station) · message <b>non</b> (il passe par les antennes) · panneau <b>oui</b>",
        "<b>B, la nuit</b> → sirène <b>oui</b> (un son fort réveille) · message <b>en partie</b> (si le téléphone n'est ni en silencieux ni "
        "éteint) · panneau <b>non</b> (personne ne le regarde en dormant)",
        "<b>C, personne sourde</b> → sirène <b>non</b> · message <b>oui</b> (un texte, une vibration) · panneau <b>oui</b> (un texte lumineux)",
        "<b>D, très basse tension</b> → oui partout → il ne départage pas&nbsp;: c'est une <b>exigence impérative</b> (F0) qui <b>élimine</b> "
        "toute solution sur le 230 volts",
        "Les autres réponses pour D ne tiennent pas&nbsp;: on ne l'efface pas (il protège contre une solution dangereuse proposée plus "
        "tard)&nbsp;; il ne classe pas les consommations&nbsp;; il ne met pas la sirène à part.",
        "<b>Lire le tableau</b> → aucune solution n'a trois «&nbsp;oui&nbsp;» → la sirène manque seulement C → le panneau couvre C → "
        "<b>sirène + panneau</b> couvrent A, B et C",
        "<b>Un argumentaire attendu&nbsp;:</b> «&nbsp;Je choisis de <b>combiner la sirène et le panneau lumineux</b>, <b>parce que</b> la sirène "
        "réveille les habitants <b>la nuit</b> et marche même si le <b>réseau</b> tombe, et que le panneau prévient les personnes "
        "<b>sourdes</b>. <b>Mais</b> la sirène consomme beaucoup d'énergie sur la batterie.&nbsp;»",
        "D'autres choix se défendent s'ils sont argumentés&nbsp;: sirène + message (le message touche aussi les habitants loin de la "
        "station, tant que le réseau tient). Un choix sans critère, ou sans limite, ne suffit pas.",
        ("conclusion", "Arbitrer, c'est&nbsp;: <b>écarter</b> ce qui ne remplit pas une exigence impérative, <b>comparer</b> le reste critère "
                       "par critère, puis <b>argumenter</b> un choix — parfois une combinaison — sans cacher sa limite."),
    ],
    retenir="pour choisir entre plusieurs solutions d'une même fonction, on les compare dans un <b>tableau de critères</b>. Un critère "
            "impératif <b>élimine</b>, les autres <b>départagent</b>&nbsp;; une <b>combinaison</b> peut couvrir les points faibles de chacune.",
    piege="chercher «&nbsp;la meilleure solution&nbsp;» dans l'absolu, ou effacer un critère parce que toutes les solutions le "
          "remplissent&nbsp;: un critère impératif reste là pour écarter les solutions dangereuses.",
)

# ─────────────────────────────────────────────────────────────────────────────
# Le cours de chaque niveau
# ─────────────────────────────────────────────────────────────────────────────
COURS = {
    "5e": (
        "<h3>Trois mots pour décrire un objet de l'intérieur</h3><ul>"
        "<li><b>La fonction d'usage</b>&nbsp;: ce à quoi sert l'objet, pour la personne qui l'utilise. Le lampadaire intelligent&nbsp;: "
        "«&nbsp;éclairer la rue la nuit quand un piéton passe&nbsp;».</li>"
        "<li><b>Une fonction technique</b>&nbsp;: une action que l'objet doit réaliser pour rendre ce service. Elle commence par un "
        "<b>verbe à l'infinitif</b>&nbsp;: détecter un passant, stocker l'énergie…</li>"
        "<li><b>Une solution technique</b>&nbsp;: l'élément de l'objet — une pièce, un composant — qui réalise la fonction technique. "
        "C'est un <b>nom</b>&nbsp;: le détecteur de mouvement, la batterie…</li>"
        "<li>Une fonction peut demander <b>plusieurs</b> solutions, et une même solution peut servir <b>deux</b> fonctions.</li></ul>"
        "<h3>Le diagramme FAST&nbsp;: une lecture dans les deux sens</h3><ul>"
        "<li>Le <b>diagramme FAST</b> (de l'anglais <i lang=\"en\">Function Analysis System Technique</i>, «&nbsp;technique d'analyse "
        "fonctionnelle&nbsp;») range ces trois mots en colonnes&nbsp;: la fonction d'usage à gauche, les fonctions techniques au "
        "milieu, les solutions à droite.</li>"
        "<li>Vers la <b>droite</b>, on répond à «&nbsp;<b>Comment&nbsp;?</b>&nbsp;»&nbsp;: comment produire la lumière&nbsp;? → avec un bloc de LED.</li>"
        "<li>Vers la <b>gauche</b>, on répond à «&nbsp;<b>Pourquoi&nbsp;?</b>&nbsp;»&nbsp;: pourquoi un panneau solaire&nbsp;? → pour capter "
        "l'énergie du soleil → pour éclairer sans câble, la nuit.</li>"
        "<li>Une case que «&nbsp;pourquoi&nbsp;?&nbsp;» ne ramène pas à la fonction d'usage n'a rien à faire dans le FAST.</li></ul>"
        "<h3>Une fonction, plusieurs principes</h3><ul>"
        "<li>Un <b>principe technique</b>, c'est la façon physique de réaliser une fonction&nbsp;: quel phénomène, à quel endroit. Pour "
        "«&nbsp;sécher le linge&nbsp;»&nbsp;: l'air chaud d'une machine, ou le soleil et le vent sur un étendoir.</li>"
        "<li>Deux principes pour une même fonction → deux cases reliées par «&nbsp;<b>ou</b>&nbsp;» dans le FAST&nbsp;: c'est une alternative.</li>"
        "<li>Pour choisir, on <b>compare</b> leurs avantages et leurs inconvénients <b>dans la situation</b>&nbsp;: la météo, le lieu, le prix, "
        "la charge…</li></ul>"
        '<div class="defile"><table><caption>Lire un FAST&nbsp;: trois gestes</caption>'
        "<tr><th>Je pars de…</th><th>Je vais…</th><th>Je réponds à…</th></tr>"
        "<tr><td>une fonction technique</td><td>vers la droite</td><td>«&nbsp;Comment&nbsp;?&nbsp;» → la solution</td></tr>"
        "<tr><td>une solution technique</td><td>vers la gauche</td><td>«&nbsp;Pourquoi&nbsp;?&nbsp;» → la fonction, puis la fonction d'usage</td></tr>"
        "<tr><td>deux cases reliées par «&nbsp;ou&nbsp;»</td><td>dans la situation</td><td>«&nbsp;Laquelle choisir&nbsp;?&nbsp;» → on compare</td></tr>"
        "</table></div>"),
    "4e": (
        "<h3>Le FAST, entre le «&nbsp;pourquoi&nbsp;» et le «&nbsp;comment&nbsp;»</h3><ul>"
        "<li>Le diagramme pieuvre et le cahier des charges regardent l'objet <b>du dehors</b>&nbsp;: à quoi il sert, ce qu'il doit "
        "respecter. Le <b>diagramme FAST</b> (de l'anglais <i lang=\"en\">Function Analysis System Technique</i>, «&nbsp;technique "
        "d'analyse fonctionnelle&nbsp;») <b>ouvre</b> l'objet&nbsp;: il part de la fonction d'usage et descend jusqu'à ses constituants.</li>"
        "<li>Chaque <b>constituant</b> est une <b>solution technique</b>&nbsp;; sur sa ligne, à gauche, on lit la <b>fonction technique</b> "
        "qu'il réalise (un verbe à l'infinitif).</li>"
        "<li>Vers la droite&nbsp;: «&nbsp;comment&nbsp;?&nbsp;»&nbsp;; vers la gauche&nbsp;: «&nbsp;pourquoi&nbsp;?&nbsp;».</li></ul>"
        "<h3>La chaîne d'information&nbsp;: trois fonctions</h3><ul>"
        "<li><b>Acquérir</b>&nbsp;: prendre une information sur le monde → un <b>capteur</b> (de luminosité, de présence, de distance…).</li>"
        "<li><b>Traiter</b>&nbsp;: comparer, calculer, décider → la <b>carte programmable</b>, avec son programme.</li>"
        "<li><b>Communiquer</b>&nbsp;: envoyer l'information à une personne ou à un autre appareil → un module sans fil, un afficheur, un voyant.</li>"
        "<li>Ce qui <b>agit</b> sur le monde (un moteur, une lampe, une vanne) est dans la <b>chaîne d'énergie</b>&nbsp;: la carte lui donne "
        "l'ordre, mais il ne traite aucune information.</li></ul>"
        '<div class="defile"><table><caption>Un exemple&nbsp;: la barrière du parking des professeurs</caption>'
        "<tr><th>Constituant</th><th>Fonction technique</th><th>Chaîne</th></tr>"
        "<tr><td>le lecteur de badge</td><td>lire le badge présenté</td><td>information — acquérir</td></tr>"
        "<tr><td>la carte programmable</td><td>décider d'ouvrir ou non</td><td>information — traiter</td></tr>"
        "<tr><td>l'afficheur de l'entrée</td><td>indiquer le nombre de places libres</td><td>information — communiquer</td></tr>"
        "<tr><td>le moteur</td><td>lever la barrière</td><td>énergie — convertir</td></tr>"
        "</table></div>"
        "<h3>Ajouter une fonction&nbsp;: quatre étapes</h3><ol>"
        "<li>Écrire ce que l'objet doit faire en plus.</li>"
        "<li>Chercher la <b>fonction technique qui manque</b>&nbsp;: celle qu'aucune branche ne réalise encore. L'écrire avec un verbe.</li>"
        "<li>Lui associer une <b>solution</b>&nbsp;; <b>réutiliser</b> ce qui existe déjà quand c'est possible.</li>"
        "<li>Relire la nouvelle branche par «&nbsp;pourquoi&nbsp;?&nbsp;», et dire ce qui change ailleurs — souvent le <b>programme</b> de la carte.</li></ol>"),
    "3e": (
        "<h3>Proposer un ensemble de solutions</h3><ul>"
        "<li>Pour un nouvel objet, on part de sa <b>fonction d'usage</b>, on la décompose en <b>fonctions techniques</b>, puis on "
        "<b>propose</b> une ou plusieurs <b>solutions</b> pour chacune&nbsp;: c'est le <b>diagramme FAST</b> (de l'anglais <i lang=\"en\">Function "
        "Analysis System Technique</i>, «&nbsp;technique d'analyse fonctionnelle&nbsp;»).</li>"
        "<li>Une fonction technique peut se décomposer à son tour en fonctions plus fines&nbsp;: le FAST a alors plusieurs niveaux. On "
        "s'arrête quand chaque case peut recevoir une solution.</li>"
        "<li>Quand plusieurs solutions sont possibles, le FAST les montre toutes, reliées par «&nbsp;<b>ou</b>&nbsp;»&nbsp;: le choix vient après.</li></ul>"
        "<h3>Contrôler un FAST&nbsp;: trois questions</h3><ul>"
        "<li>Chaque case de fonction commence-t-elle par un <b>verbe à l'infinitif</b>&nbsp;? «&nbsp;Le moteur&nbsp;» dans une case de "
        "fonction est une erreur&nbsp;: c'est un objet.</li>"
        "<li>Chaque solution répond-elle au «&nbsp;<b>comment&nbsp;?</b>&nbsp;» de sa fonction&nbsp;? Une pile ne «&nbsp;produit pas la "
        "lumière&nbsp;»&nbsp;: elle stocke l'énergie.</li>"
        "<li>Chaque branche ramène-t-elle, par «&nbsp;<b>pourquoi&nbsp;?</b>&nbsp;», à la fonction d'usage&nbsp;? Sinon, elle n'a rien à faire là.</li></ul>"
        "<h3>Arbitrer entre plusieurs solutions</h3><ul>"
        "<li>On les compare dans un <b>tableau</b>&nbsp;: une ligne par critère, une colonne par solution.</li>"
        "<li>Un critère <b>élimine</b> quand c'est une exigence impérative (flexibilité F0)&nbsp;: une solution qui ne la remplit pas est "
        "écartée, quelles que soient ses qualités. La très basse tension en est une.</li>"
        "<li>Un critère <b>départage</b> quand les solutions y répondent différemment.</li>"
        "<li>On peut <b>combiner</b> deux solutions quand chacune couvre le point faible de l'autre.</li>"
        "<li>Un argumentaire dit&nbsp;: <b>ce que je choisis</b>, <b>les critères</b> qui le justifient, et <b>la limite</b> qui reste.</li></ul>"
        "<h3>Ce que le FAST n'est pas</h3><ul>"
        "<li>Il ne reprend pas toutes les fonctions ni toutes les pièces de l'objet&nbsp;: seulement les fonctions étudiées et les "
        "constituants qui les réalisent.</li>"
        "<li>Il ne dessine pas les solutions&nbsp;: il les <b>nomme</b>. Le croquis et le schéma viennent ensuite.</li>"
        "<li>Il ne fait pas partie du cahier des charges&nbsp;: celui-ci dit ce qu'on attend de l'objet&nbsp;; le FAST dit comment on y répond.</li></ul>"),
}

# ─────────────────────────────────────────────────────────────────────────────
# Les trois niveaux
# ─────────────────────────────────────────────────────────────────────────────
NIVEAUX = {
    "5e": dict(
        codes=["5e_C4.1", "5e_C1.2"],
        mission="Ouvrir un objet par la pensée&nbsp;: ce qu'il doit faire, et ce qui le fait — puis comparer deux façons de le faire.",
        avant=[("Je sais dire à quoi sert un objet de tous les jours, en une phrase qui commence par un verbe.",
                "cycle 3 — sciences et technologie", "@synthese#les-mots", "les mots de l'atelier, dans la synthèse (2 minutes)"),
               ("Je sais nommer quelques éléments d'un objet électrique (une pile, une lampe, un interrupteur) et dire à quoi ils servent.",
                "cycle 3 — sciences et technologie", "@synthese#les-mots", "les mots de l'atelier, dans la synthèse (2 minutes)")],
        situation_titre="Le programme et le nom courant",
        situation="<p>Le programme de technologie demande d'<b>associer des solutions techniques à des fonctions techniques</b>, et de "
                  "<b>comparer des principes techniques</b> pour une même fonction. Le schéma qui relie tout cela porte un nom courant&nbsp;: "
                  "le <b>diagramme FAST</b> (de l'anglais <i lang=\"en\">Function Analysis System Technique</i>, «&nbsp;technique "
                  "d'analyse fonctionnelle&nbsp;»).</p>"
                  "<p>Il part de ce à quoi sert l'objet, à gauche, et va jusqu'à ses composants, à droite. Dans cet atelier, tu le lis sur "
                  "le <b>lampadaire intelligent</b> de la rue du collège, puis sur le <b>vélo-cargo</b> de Léa.</p>",
        question="Comment passer de ce qu'un objet doit faire aux éléments qui le font — et choisir entre deux façons de le faire&nbsp;?",
        hypothese_amorces=["Je pense qu'on pourrait écrire d'abord ce que l'objet doit faire, puis…",
                           "Pour savoir à quoi sert une pièce, je me demanderais…",
                           "Pour choisir entre deux freins, je regarderais…"],
        exercices=[E1, E2, E3],
        a_retenir="<ul><li>Une <b>fonction technique</b> est une action que l'objet doit réaliser (un verbe à l'infinitif)&nbsp;; une "
                  "<b>solution technique</b> est l'élément qui la réalise (un nom).</li>"
                  "<li>Le <b>diagramme FAST</b> va de la fonction d'usage aux solutions. Vers la droite, il répond à «&nbsp;<b>comment&nbsp;?</b>&nbsp;»&nbsp;; "
                  "vers la gauche, à «&nbsp;<b>pourquoi&nbsp;?</b>&nbsp;».</li>"
                  "<li>Une solution qui ne ramène pas, par «&nbsp;pourquoi&nbsp;?&nbsp;», à la fonction d'usage n'a rien à faire dans le FAST.</li>"
                  "<li>Une même fonction peut être réalisée par plusieurs <b>principes techniques</b> (deux cases reliées par «&nbsp;ou&nbsp;»)&nbsp;: "
                  "on les compare, puis on choisit selon la situation.</li></ul>",
        bonus=[dict(titre="Le panneau qui voit la nuit",
                    consigne="<p>Dans beaucoup de petites lampes solaires de jardin, il n'y a pas de capteur de luminosité&nbsp;: c'est le "
                             "<b>panneau solaire</b> qui «&nbsp;détecte la nuit&nbsp;». Explique comment c'est possible, et ce que cela change "
                             "dans le FAST.</p>",
                    correction=["Le jour → le panneau reçoit de la lumière → il donne de l'énergie électrique",
                                "La nuit → il ne donne presque plus rien → la carte le remarque → <b>la nuit est détectée</b>",
                                "Dans le FAST → le panneau solaire est la solution de <b>deux</b> fonctions&nbsp;: capter l'énergie du soleil "
                                "<b>et</b> détecter la nuit",
                                ("conclusion", "Une même solution peut servir deux fonctions&nbsp;: une pièce de moins à fabriquer.")]),
                   dict(titre="Trois fonctions d'usage",
                        consigne="<p>Écris la <b>fonction d'usage</b> d'un ventilateur, d'une gourde et d'un cartable, avec un verbe à "
                                 "l'infinitif. Puis donne <b>une</b> fonction technique du ventilateur et sa solution.</p>",
                        correction=["<b>Ventilateur</b> → rafraîchir une personne en déplaçant l'air",
                                    "<b>Gourde</b> → transporter de l'eau pour boire",
                                    "<b>Cartable</b> → transporter ses affaires de classe",
                                    "<b>Une fonction technique du ventilateur</b> → mettre l'air en mouvement → les pales, entraînées par un moteur",
                                    ("conclusion", "La fonction d'usage dit à quoi sert l'objet&nbsp;; les fonctions techniques disent ce qu'il "
                                                   "doit faire pour y arriver.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre une fonction et une solution, ou entre «&nbsp;comment&nbsp;?&nbsp;» et "
                      "«&nbsp;pourquoi&nbsp;?&nbsp;». Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
    "4e": dict(
        codes=["4e_C4.4", "4e_C7.2"],
        mission="Ouvrir le système d'arrosage du jardin&nbsp;: relier chaque constituant à sa fonction, puis lui ajouter une fonction nouvelle.",
        avant=[("Je sais lire un diagramme FAST dans les deux sens&nbsp;: «&nbsp;comment&nbsp;?&nbsp;» vers la droite, «&nbsp;pourquoi&nbsp;?&nbsp;» vers la gauche.",
                "5e_C4.1", "@niveau:5e#fa_5e_e1", "l'atelier de 5e, exercices 1 et 2 (20 minutes)"),
               ("Je sais distinguer une fonction technique (une action, un verbe) d'une solution technique (un élément, un nom).",
                "5e_C4.1", "@niveau:5e#fa_5e_e1", "l'atelier de 5e, exercice 1 (10 minutes)")],
        situation_titre="Le programme et le nom courant",
        situation="<p>Le programme de technologie demande d'<b>identifier les constituants de la chaîne d'information</b> d'un objet réel "
                  "et de les <b>associer à leur fonction</b>, puis de <b>proposer une solution pour ajouter une nouvelle fonction</b>. Le "
                  "schéma qui relie fonctions et constituants porte un nom courant&nbsp;: le <b>diagramme FAST</b> (de l'anglais "
                  "<i lang=\"en\">Function Analysis System Technique</i>, «&nbsp;technique d'analyse fonctionnelle&nbsp;»).</p>"
                  "<p>Dans cet atelier, l'objet est le <b>système d'arrosage connecté</b> du jardin partagé du collège.</p>",
        question="Comment savoir ce que fait chaque constituant d'un système — et où ajouter ce qui lui manque&nbsp;?",
        hypothese_amorces=["Je pense que chaque constituant…", "Pour ajouter une fonction, je commencerais par…",
                           "Je crois qu'une pièce déjà là peut…"],
        exercices=[E4, E5],
        a_retenir="<ul><li>Dans le <b>diagramme FAST</b>, chaque <b>constituant</b> est la solution d'une <b>fonction technique</b>&nbsp;: "
                  "on le lit «&nbsp;comment&nbsp;?&nbsp;» vers la droite, «&nbsp;pourquoi&nbsp;?&nbsp;» vers la gauche.</li>"
                  "<li>La <b>chaîne d'information</b> réunit les constituants qui <b>acquièrent</b> (capteur), <b>traitent</b> (carte "
                  "programmable) et <b>communiquent</b> (module sans fil, afficheur) une information. Ce qui agit sur le monde est dans la "
                  "chaîne d'énergie.</li>"
                  "<li>Ajouter une fonction, c'est ajouter une <b>branche</b>&nbsp;: la fonction technique qui manque, puis sa solution, en "
                  "<b>réutilisant</b> ce qui existe déjà.</li>"
                  "<li>Une nouvelle fonction change souvent le <b>programme</b> de la carte&nbsp;: c'est elle qui décide.</li></ul>",
        bonus=[dict(titre="Goutte-à-goutte ou arroseur",
                    consigne="<p>Pour la fonction «&nbsp;répartir l'eau sur les plantes&nbsp;», le club hésite entre un tuyau "
                             "<b>goutte-à-goutte</b> (l'eau sort au pied de chaque plante) et un <b>arroseur</b> qui projette l'eau en pluie. "
                             "Compare les deux principes, puis choisis pour un jardin qui récupère l'eau de pluie dans une cuve.</p>",
                    correction=["<b>Goutte-à-goutte</b> → l'eau va au pied de la plante → peu d'eau perdue par évaporation au soleil",
                                "<b>Arroseur</b> → l'eau tombe partout, même entre les plantes → plus d'eau perdue, mais un seul appareil",
                                "<b>Pour une cuve d'eau de pluie</b> → l'eau est comptée → <b>le goutte-à-goutte</b>",
                                ("conclusion", "Deux principes pour une fonction&nbsp;: on choisit selon la situation, ici une eau rare.")]),
               dict(titre="Remonter depuis le panneau solaire",
                    consigne="<p>La pompe du jardin est alimentée par un <b>panneau solaire</b>. Ajoute sa branche au FAST&nbsp;: quelle "
                             "fonction technique&nbsp;? Puis remonte («&nbsp;pourquoi&nbsp;?&nbsp;») jusqu'à la fonction d'usage.</p>",
                    correction=["<b>Fonction</b> → capter l'énergie du soleil (pour alimenter la pompe)",
                                "<b>Pourquoi&nbsp;?</b> → pour que la pompe fasse circuler l'eau → pour arroser les plantes quand la terre "
                                "est sèche",
                                ("conclusion", "Toute solution doit pouvoir remonter, par «&nbsp;pourquoi&nbsp;?&nbsp;», jusqu'à la fonction "
                                               "d'usage.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre la chaîne d'information et la chaîne d'énergie, ou entre une fonction et "
                      "une solution. Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
    "3e": dict(
        codes=["3e_C7.2"],
        mission="Proposer, contrôler et choisir les solutions d'un objet nouveau&nbsp;: la station d'alerte cyclonique du quartier.",
        avant=[("Je sais associer chaque constituant d'un objet à sa fonction technique dans un diagramme FAST.",
                "4e_C4.4", "@niveau:4e#fa_4e_e4", "l'atelier de 4e, exercice 1 (18 minutes)"),
               ("Je sais ajouter à un FAST la branche d'une nouvelle fonction&nbsp;: la fonction qui manque, puis sa solution.",
                "4e_C7.2", "@niveau:4e#fa_4e_e5", "l'atelier de 4e, exercice 2 (15 minutes)"),
               ("Je sais comparer deux principes techniques pour une même fonction, selon la situation.",
                "5e_C1.2", "@niveau:5e#fa_5e_e3", "l'atelier de 5e, exercice 3 (14 minutes)")],
        situation_titre="Le programme et le nom courant",
        situation="<p>Le programme de technologie demande de <b>proposer un ensemble de solutions pour produire un nouvel objet</b>. "
                  "Le schéma qui organise ces solutions, fonction par fonction, porte un nom courant&nbsp;: le <b>diagramme FAST</b> (de "
                  "l'anglais <i lang=\"en\">Function Analysis System Technique</i>, «&nbsp;technique d'analyse fonctionnelle&nbsp;»).</p>"
                  "<p>Dans cet atelier, l'objet nouveau est la <b>station d'alerte cyclonique</b> du quartier&nbsp;: elle mesure le vent "
                  "et prévient les habitants, seule, avec un panneau solaire et une batterie.</p>",
        question="Quand plusieurs solutions répondent à la même fonction, comment choisir — et comment le justifier&nbsp;?",
        hypothese_amorces=["Je pense qu'il faut d'abord vérifier que…", "Pour choisir entre plusieurs solutions, je comparerais…",
                           "Je crois qu'on peut aussi garder deux solutions quand…"],
        exercices=[E6, E7],
        a_retenir="<ul><li>Le <b>diagramme FAST</b> d'un objet nouveau propose, pour chaque fonction technique, une ou plusieurs "
                  "<b>solutions</b>&nbsp;; plusieurs solutions possibles sont reliées par «&nbsp;ou&nbsp;».</li>"
                  "<li>On le <b>contrôle</b> avant de fabriquer&nbsp;: un verbe dans chaque case de fonction, une solution qui répond au "
                  "«&nbsp;comment&nbsp;?&nbsp;», une branche qui ramène, par «&nbsp;pourquoi&nbsp;?&nbsp;», à la fonction d'usage.</li>"
                  "<li>Pour <b>arbitrer</b>, on compare les solutions dans un tableau de critères&nbsp;: un critère impératif <b>élimine</b>, "
                  "les autres <b>départagent</b>.</li>"
                  "<li>Un bon argumentaire nomme le choix (parfois une <b>combinaison</b>), les critères qui le justifient, et la limite qui reste.</li></ul>",
        bonus=[dict(titre="Un FAST à deux niveaux",
                    consigne="<p>La fonction «&nbsp;décider du niveau d'alerte&nbsp;» est encore large. Décompose-la en <b>trois</b> fonctions "
                             "plus fines, chacune avec un verbe, que la carte programmable réalisera.</p>",
                    correction=["<b>comparer la vitesse du vent au seuil d'alerte orange</b>",
                                "<b>comparer la vitesse du vent au seuil d'alerte rouge</b>",
                                "<b>choisir le message et le son à diffuser</b>",
                                "Les trois ont la même solution&nbsp;: la carte programmable et son programme.",
                                ("conclusion", "Une fonction technique se décompose à son tour&nbsp;: le FAST a plusieurs niveaux, jusqu'à ce "
                                               "que chaque case reçoive une solution.")]),
               dict(titre="La batterie tiendra-t-elle&nbsp;?",
                    consigne="<p>Une sirène 12 V (volts) consomme environ 2 ampères quand elle sonne. La batterie de la station peut fournir "
                             "environ 20 ampères pendant une heure (on dit 20 ampères-heures). Combien d'heures de sirène, au plus&nbsp;? "
                             "Pourquoi l'équipe prévoit-elle de n'en compter que la moitié&nbsp;?</p>",
                    correction=["20 ampères-heures ÷ 2 ampères → <b>10 heures</b> de sirène, au plus",
                                "La moitié → une batterie qu'on vide entièrement s'abîme, et la carte, l'anémomètre et le panneau "
                                "lumineux consomment aussi → l'équipe compte <b>5 heures</b> environ",
                                ("conclusion", "Arbitrer, c'est aussi vérifier que la solution choisie tient avec l'énergie disponible.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre une erreur et une alternative permise, ou entre un critère qui élimine et "
                      "un critère qui départage. Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
}

# ─────────────────────────────────────────────────────────────────────────────
# Ce que le reste du site lit de cet atelier
# ─────────────────────────────────────────────────────────────────────────────
MODULE = "fast"
NOM_PANNEAU = "diagramme_fast"
PANNEAU_TEXTE = {
    "5e": "Des <b>fonctions techniques</b> aux <b>solutions techniques</b>, avec le <b>diagramme FAST</b>&nbsp;: tu lis celui du "
          "lampadaire intelligent dans les deux sens (comment&nbsp;? pourquoi&nbsp;?), tu le complètes, puis tu compares deux principes "
          "de freinage pour le vélo-cargo de Léa.",
    "4e": "Des <b>fonctions techniques</b> aux <b>solutions techniques</b>, avec le <b>diagramme FAST</b> du système d'arrosage du "
          "jardin&nbsp;: tu relies chaque constituant à sa fonction, tu repères la chaîne d'information, puis tu ajoutes une fonction "
          "nouvelle.",
    "3e": "Des <b>fonctions techniques</b> aux <b>solutions techniques</b>, avec le <b>diagramme FAST</b> de la station d'alerte "
          "cyclonique&nbsp;: tu contrôles le FAST d'une équipe, puis tu compares trois solutions d'alerte et tu argumentes ton choix.",
}
IMAGES = {
    "fast_lampadaire_complet.svg": LAMPADAIRE_CORRIGE,
    "fast_lampadaire_a_completer.svg": LAMPADAIRE_COMPLETER,
    "fast_velo_cargo_freinage.svg": VELO,
    "fast_jardin_arrosage.svg": JARDIN_CORRIGE,
    "fast_jardin_nouvelle_branche.svg": JARDIN_AJOUT_CORRIGE,
    "fast_station_alerte.svg": STATION,
    "fast_station_alerte_erreurs.svg": STATION_ERREURS,
}
VOCAB_EN = [("fonction d'usage", "use function"), ("fonction technique", "technical function"),
            ("solution technique", "technical solution"), ("principe technique", "technical principle"),
            ("diagramme FAST", "FAST diagram (Function Analysis System Technique)"), ("comment ?", "how?"),
            ("pourquoi ?", "why?"), ("constituant", "component"), ("capteur", "sensor"),
            ("chaîne d'information", "information chain"), ("critère", "criterion"), ("frein à disque", "disc brake")]
VERBES = {"5e": "<b>lire</b> le FAST dans les deux sens (comment&nbsp;? pourquoi&nbsp;?), puis le <b>compléter</b>&nbsp;; "
                "<b>comparer</b> deux principes pour une même fonction",
          "4e": "<b>construire</b>&nbsp;: associer chaque constituant à sa fonction (chaîne d'information), puis <b>ajouter</b> une "
                "branche pour une fonction nouvelle",
          "3e": "<b>contrôler</b> un FAST proposé, puis <b>comparer</b> trois solutions d'une même fonction et <b>arbitrer</b> par un "
                "argumentaire"}
CHAINE = ("<p><b>Analyse externe</b>&nbsp;: besoin <i>(bête à cornes)</i> → fonction d'usage → interacteurs <i>(diagramme pieuvre)</i> "
          "→ contraintes et exigences → cahier des charges.<br><b>Charnière</b>&nbsp;: <b>fonction d'usage → fonctions techniques → "
          "solutions techniques <i>(diagramme FAST)</i></b>.<br><b>Analyse interne</b>&nbsp;: constituants → chaîne d'information "
          "(acquérir, traiter, communiquer) et chaîne d'énergie (alimenter, stocker, distribuer, convertir, transmettre).</p>"
          "<p>Cet atelier est la <b>charnière</b> entre le «&nbsp;pourquoi&nbsp;» (l'analyse externe, qui dit à quoi sert l'objet) et le "
          "«&nbsp;comment&nbsp;» (l'analyse interne, qui dit ce qui le fait). Il <b>suit</b> le diagramme pieuvre et le cahier des "
          "charges&nbsp;; il <b>précède</b> les schémas des chaînes d'information et d'énergie, le croquis et la fabrication.</p>")
NOTES_PROF = ("<ul><li>Le programme ne nomme pas le FAST&nbsp;: il dit <i>fonction technique, principe technique, solution technique</i>. "
              "Le titre de l'atelier est donc «&nbsp;Des fonctions aux solutions techniques&nbsp;», et le nom courant, «&nbsp;diagramme "
              "FAST&nbsp;», vient ensuite, avec son sigle développé une fois par niveau (et au lexique).</li>"
              "<li>Lecture enseignée dès la 5e&nbsp;: «&nbsp;comment&nbsp;?&nbsp;» vers la droite, «&nbsp;pourquoi&nbsp;?&nbsp;» vers la "
              "gauche — elle sert ensuite d'outil de contrôle (3e, exercice 1).</li>"
              "<li>Plan&nbsp;: six exercices prévus, sept écrits. La 3e reçoit un exercice de plus («&nbsp;trouver les erreurs d'un "
              "FAST&nbsp;», 13 min) avant l'arbitrage, pour que la page atteigne 30 à 40 minutes sans un exercice unique de 30 minutes.</li>"
              "<li>Inspiration&nbsp;: le cahier «&nbsp;123 Techno&nbsp;» (Bordas, 2021), fiches FAST de 5e, 4e et 3e — mécaniques "
              "reprises, transposées à nos objets et dans nos mots&nbsp;: classer fonction / solution par la grammaire (verbe ou nom)&nbsp;; "
              "FAST tiré d'un texte où chaque phrase cache un couple constituant / fonction (4e)&nbsp;; «&nbsp;corriger le corrigé&nbsp;» "
              "— une case de fonction qui contient un nom (3e)&nbsp;; «&nbsp;ce que le FAST n'est pas&nbsp;» (cours de 3e, QCM). Écarts du "
              "cahier volontairement non repris&nbsp;: FAST sans lecture «&nbsp;pourquoi&nbsp;? / comment&nbsp;?&nbsp;», fonctions sans verbe "
              "d'action («&nbsp;être pliable&nbsp;»). Aucun énoncé, aucune image de l'éditeur n'est repris.</li>"
              "<li>Limite du dessin&nbsp;: le générateur trace un FAST à un seul niveau de fonctions techniques. Le cours de 3e et le "
              "bonus «&nbsp;Un FAST à deux niveaux&nbsp;» disent que le FAST peut en avoir plusieurs, sans pouvoir le dessiner.</li>"
              "<li>Le 5e_C1.2 rejoint la séquence «&nbsp;freinage&nbsp;» de Sainte-Luce&nbsp;: même distinction fonction / principe / "
              "solution, même idée que les freins frottent tous, mais pas au même endroit.</li>"
              "<li>Très basse tension partout&nbsp;: le lampadaire et la station sont alimentés par panneau solaire et batterie 12 V&nbsp;; "
              "le 230 V n'apparaît que comme danger (critère éliminatoire de la 3e).</li>"
              "<li>En 4e et en 3e, l'élève n'a pas forcément fait le niveau précédent&nbsp;: l'ouverture renvoie aux exercices utiles.</li></ul>")
DEUX_NOMS = ("Le programme de technologie parle de <b>fonctions techniques</b>, de <b>principes techniques</b> et de <b>solutions "
             "techniques</b>. Le schéma qui les relie s'appelle couramment le <b>diagramme FAST</b>, de l'anglais <i lang=\"en\">Function "
             "Analysis System Technique</i> («&nbsp;technique d'analyse fonctionnelle&nbsp;»). Il fait le lien entre le «&nbsp;pourquoi&nbsp;» "
             "(à quoi sert l'objet) et le «&nbsp;comment&nbsp;» (ce qui, dans l'objet, le fait).")
QCM_SOUS_TITRE = ("Lire et compléter un diagramme FAST, comparer deux principes (5e) ; associer constituants et fonctions, ajouter une "
                  "fonction (4e) ; proposer, contrôler et choisir des solutions (3e)")
