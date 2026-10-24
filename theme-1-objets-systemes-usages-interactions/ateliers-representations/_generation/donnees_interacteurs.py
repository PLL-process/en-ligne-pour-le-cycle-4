# -*- coding: utf-8 -*-
"""Atelier — Le diagramme des interacteurs extérieurs (diagramme pieuvre).

Codes servis : 5e_C2.1, 5e_C2.2, 4e_C2.2 (choix de Pascal, 13/10/2026 : pas de
pieuvre en 4e_C2.1 ni en 3e). Objet de 5e : le vélo-cargo (choix de Pascal,
13/10/2026) ; objet de 4e : le système d'arrosage du jardin connecté.

Le verbe change d'un niveau à l'autre, pas la notion :
  5e  LISTER, CLASSER, COMPLÉTER le diagramme ; EXPLIQUER un choix par un interacteur ;
  4e  DISTINGUER le service rendu des contraintes, puis les ÉCRIRE pour qu'on puisse les vérifier.
"""
import figures
import dessins

SLUG = "interacteurs-pieuvre"
COURT = "pv"
EMOJI = "🐙"
TITRE = "Le diagramme des interacteurs extérieurs"
TITRE_COURT = "le diagramme des interacteurs extérieurs (diagramme pieuvre)"
TITRE_COMPLET = "Le diagramme des interacteurs extérieurs, souvent appelé diagramme pieuvre"
ETIQUETTE = "🐙 diagramme pieuvre"
MENTION_FICTION = ("Situations imaginées pour les exercices : Léa, ses enfants, Mme Joseph et le jardin "
                   "du collège sont inventés ; les plaintes de l'exercice 7 aussi.")

FAMILLES = [("usager", "un usager"), ("donnee", "une donnée"), ("objet", "un autre objet"),
            ("environnement", "un élément de l'environnement")]

# ─────────────────────────────────────────────────────────────────────────────
# Les dessins
# ─────────────────────────────────────────────────────────────────────────────
SCENE = dessins.velo_cargo(
    "pv-scene", "Léa et son vélo-cargo, dans une côte, sous la pluie",
    "Dessin. Une femme pédale sur un vélo-cargo qui monte une route en pente. Dans le bac, devant elle, "
    "deux enfants et un sac de courses. Il pleut. Un téléphone est fixé au guidon ; son écran montre un "
    "tracé. Aucun élément n'est nommé.")

SCENE_REPERES = dessins.velo_cargo(
    "pv-choix", "Trois détails du vélo-cargo, repérés A, B et C",
    "Le même dessin, avec trois repères. A montre le rebord du bac, où sont assis les enfants. "
    "B montre la petite commande de vitesses, sur la poignée du guidon. C montre la coque grise qui enferme la chaîne, "
    "entre la roue arrière et le pédalier.",
    reperes=[("A", 560, 140, 470, 274), ("B", 230, 140, 352, 234), ("C", 150, 300, 280, 378)])

# Léa en haut, entre ses enfants (①, en haut à gauche) et les courses (②, en haut à droite) : les deux interacteurs de
# chaque FP sont voisins sur le cercle, et chaque FP se lit comme un U qui plonge dans l'objet (la corne de la bête à
# cornes). Les FC se numérotent à partir des enfants (FC1, au bout de la FP1), dans le sens inverse des aiguilles.
BULLES_E3 = [dict(nom="Léa", famille="neutre"),
             dict(nom="", famille="vide", vivant="pv-b2", vide="② un autre objet ?", prefixe="②"),
             dict(nom="le téléphone", famille="neutre"),
             dict(nom="l'itinéraire", famille="neutre"),
             dict(nom="", famille="vide", vivant="pv-b3", vide="③ un élément de l'environnement ?", prefixe="③"),
             dict(nom="la pluie", famille="neutre"),
             dict(nom="", famille="vide", vivant="pv-b1", vide="① un usager ?", prefixe="①")]

FONCTIONS_VELO = dict(liens_fp=[(0, 6, "FP1"), (0, 1, "FP2")], liens_fc=[(6, "FC1"), (5, "FC2"), (4, "FC3"), (2, "FC4"), (3, "FC5")])

PIEUVRE_A_COMPLETER = figures.pieuvre(
    "pv-pieuvre", "Le vélo-cargo", BULLES_E3,
    "Diagramme des interacteurs extérieurs du vélo-cargo, à compléter",
    "Au centre, le vélo-cargo. Sept bulles autour. Quatre sont remplies : Léa, le téléphone, la pluie, "
    "l'itinéraire. Trois sont vides et annoncent seulement la famille attendue : bulle 1, un usager ; "
    "bulle 2, un autre objet ; bulle 3, un élément de l'environnement. Deux courbes partent de Léa et passent "
    "par le vélo-cargo : FP1 arrive à la bulle 1, FP2 à la bulle 2. Cinq traits droits relient le "
    "vélo-cargo à un seul élément : FC1 à la bulle 1, FC2 à la pluie, FC3 à la bulle 3, FC4 au téléphone, "
    "FC5 à l'itinéraire.",
    **FONCTIONS_VELO)

BULLES_CORRIGE = [dict(nom="Léa", famille="usager"), dict(nom="② les courses", famille="objet"),
                  dict(nom="le téléphone", famille="objet"), dict(nom="l'itinéraire", famille="donnee"),
                  dict(nom="③ la route en pente", famille="environnement"), dict(nom="la pluie", famille="environnement"),
                  dict(nom="① les enfants", famille="usager")]

PIEUVRE_CORRIGE = figures.pieuvre(
    "pv-pieuvre-c", "Le vélo-cargo", BULLES_CORRIGE,
    "Diagramme des interacteurs extérieurs du vélo-cargo, corrigé",
    "Au centre, le vélo-cargo. Sept bulles, chacune avec sa famille écrite dessous. Léa : un usager. "
    "Bulle 1, les enfants : un usager. Le téléphone : un autre objet. Bulle 2, les courses : un autre "
    "objet. La pluie : l'environnement. Bulle 3, la route en pente : l'environnement. L'itinéraire : "
    "une donnée. Les fonctions FP1 et FP2 passent par le vélo-cargo, de Léa aux enfants et aux courses ; "
    "FC1 à FC5 le relient aux enfants, à la pluie, à la route en pente, au téléphone et à l'itinéraire.",
    montrer_famille=True, **FONCTIONS_VELO)

# La gardienne (en haut à gauche) et les plantes (en haut à droite) sont voisines : la FP plonge en U dans le système.
BULLES_JARDIN = [dict(nom="les plantes", famille="environnement"), dict(nom="la cuve d'eau de pluie", famille="objet"),
                 dict(nom="la pluie et le soleil", famille="environnement"), dict(nom="le smartphone", famille="objet"),
                 dict(nom="l'heure d'arrosage choisie", famille="donnee"), dict(nom="la gardienne", famille="usager")]

PIEUVRE_JARDIN = figures.pieuvre(
    "pv-jardin", "Le système d'arrosage", BULLES_JARDIN,
    "Diagramme des interacteurs extérieurs du système d'arrosage du jardin, avec six traits numérotés",
    "Au centre, le système d'arrosage. Six bulles autour : la gardienne, les plantes, la cuve d'eau de "
    "pluie, la pluie et le soleil, le smartphone, l'heure d'arrosage choisie. Le trait 1 est une courbe "
    "qui part de la gardienne, passe par le système et arrive aux plantes. Les traits 2 à 6 sont "
    "droits et relient le système à un seul interacteur : 2 à la pluie et au soleil, 3 à la cuve, 4 au "
    "smartphone, 5 à la gardienne, 6 à l'heure d'arrosage choisie.",
    liens_fp=[(5, 0, "1")], liens_fc=[(2, "2"), (1, "3"), (3, "4"), (5, "5"), (4, "6")], montrer_famille=True,
    largeur=820, hauteur=520, rotation=30)

FONCTIONS_JARDIN = [("FP1", "permettre à la gardienne d'arroser les plantes sans être là"),
                    ("FC1", "résister à la pluie et au soleil"),
                    ("FC2", "prendre dans la cuve seulement l'eau dont les plantes ont besoin"),
                    ("FC3", "envoyer l'état de l'arrosage au smartphone"),
                    ("FC4", "être facile à régler par la gardienne"),
                    ("FC5", "respecter l'heure d'arrosage choisie")]

PIEUVRE_JARDIN_CORRIGE = figures.pieuvre(
    "pv-jardin-c", "Le système d'arrosage", BULLES_JARDIN,
    "Diagramme pieuvre du système d'arrosage, corrigé : FP1 et FC1 à FC5",
    "Le même diagramme, avec le nom de chaque fonction. FP1 est la courbe qui part de la gardienne, entre dans le "
    "système d'arrosage et arrive aux plantes. FC1 relie le système à la pluie et au soleil, FC2 à la cuve, FC3 au "
    "smartphone, FC4 à la gardienne, FC5 à l'heure d'arrosage choisie. La gardienne porte donc deux fonctions : la FP1 "
    "et la FC4.",
    liens_fp=[(5, 0, "FP1")], liens_fc=[(2, "FC1"), (1, "FC2"), (3, "FC3"), (5, "FC4"), (4, "FC5")], montrer_famille=True,
    largeur=820, hauteur=520, rotation=30)

BETE_VERS_PIEUVRE = figures.bete_vers_pieuvre(
    "pv-bp", "Léa", "ses enfants", "le vélo-cargo", "transporter ses enfants en ville",
    "permettre à Léa de transporter ses enfants", "protéger les enfants pendant le trajet",
    "De la bête à cornes au diagramme pieuvre",
    "À gauche, la bête à cornes du vélo-cargo : repère 1, à qui rend-il service ? Léa ; repère 2, sur quoi agit-il ? ses "
    "enfants ; la corne bleue relie les deux en passant sous le vélo-cargo ; repère 3, dans quel but ? transporter ses "
    "enfants en ville. Une flèche marquée « devient » mène à droite, au diagramme pieuvre : la bulle Léa (repère 1) et la "
    "bulle ses enfants (repère 2) sont en haut ; la courbe bleue FP1 part de Léa, descend passer par le vélo-cargo et "
    "remonte aux enfants, comme la corne. Un trait rouge FC1 relie le vélo-cargo aux enfants. En dessous, repère 3 : FP1, "
    "permettre à Léa de transporter ses enfants ; FC1, protéger les enfants pendant le trajet. Légende : le repère 1 est "
    "la bulle d'où part la FP1, le repère 2 la bulle où elle arrive, le repère 3 la phrase de la FP1.")

# ─────────────────────────────────────────────────────────────────────────────
# 5e
# ─────────────────────────────────────────────────────────────────────────────
PIECES = (r"^(la |le |les |l'|une? |des |mon |ma |son |sa )?(pedales?|chaines?|selles?|guidons?|roues?|pneus?|"
          r"freins?|bac|caisse|cadre|moteur|batterie|garde.?boue|phares?|sonnette|porte.?bagages?|"
          r"sieges?|ceintures?|harnais|vitesses?|derailleur|rayons?|fourche)\b")

E1 = dict(
    id="e1", titre="Lister ce qui entoure le vélo-cargo", code="5e_C2.1", duree=8,
    objectif="repérer, dans une scène, tout ce qui est <b>en dehors</b> du vélo-cargo et en relation avec lui.",
    production="une liste de cinq interacteurs extérieurs, un par ligne.",
    mots=[("interacteur extérieur", "une personne, une chose, une information ou un élément de la nature qui est "
           "<b>en dehors</b> de l'objet et <b>en relation</b> avec lui : il le touche, il agit sur lui, ou l'objet agit sur lui."),
          ("constituant", "une pièce de l'objet lui-même (la pédale, la chaîne, le bac…). Un constituant est <b>dedans</b>."),
          ("usage", "ce que l'on fait avec l'objet (aller au marché). Un usage est une action, pas un interacteur.")],
    documents=[dict(svg=SCENE, legende="La scène : Léa monte une côte en vélo-cargo, sous la pluie.",
                    description="<p>Léa pédale sur son vélo-cargo. La route monte. Dans le bac, devant elle, il y a ses deux "
                                "enfants et un sac de courses. Il pleut. Son téléphone, fixé au guidon, lui montre le chemin.</p>")],
    intro="<p>Léa transporte ses deux enfants et ses courses en vélo-cargo — un vélo avec un grand bac devant. "
          "La route monte. Il pleut. Son téléphone, fixé au guidon, lui montre le chemin.</p>",
    consigne="<p><b>Écris cinq interacteurs extérieurs du vélo-cargo, un par ligne.</b> Un interacteur extérieur, c'est "
             "une personne, une chose, une information ou un élément de la nature qui est <b>en dehors</b> du vélo-cargo "
             "et <b>en relation</b> avec lui.</p>",
    critere="ta liste a cinq lignes ; chacune nomme quelque chose qui est en dehors du vélo-cargo ; aucune ne nomme une pièce "
            "du vélo ou une action.",
    widgets=[dict(type="liste", name="liste", min=5, lignes=7,
                  label="Mes cinq interacteurs extérieurs (un par ligne)",
                  attendus=[
                      dict(nom="Léa", motifs=[r"\blea\b", "cycliste", "conductrice", "maman", r"\bmere\b", "dame", "femme", "utilisatrice", "pilote"]),
                      dict(nom="les enfants", motifs=["enfant", r"\bfils\b", r"\bfille", "petits?\\b", "bebe", "passager", "gamin"]),
                      dict(nom="les courses", motifs=["course", r"\bsac", "provision", "marchandise", "colis", "paquet", "commission", "poireau", "baguette", "legume"]),
                      dict(nom="l'itinéraire", motifs=["itineraire", "chemin", "trajet", r"\bcarte\b", r"\bplan\b", "direction", "parcours", "route a suivre", "gps"]),
                      dict(nom="la route en pente", motifs=["route", "pente", r"\bcote\b", "montee", "chaussee", r"\bsol\b", r"\brue\b", "goudron", "bitume"]),
                      dict(nom="la pluie", motifs=["pluie", "pleut", r"\beau\b", "averse", "mouill", "humid", "orage", "meteo", "nuage"]),
                      dict(nom="le téléphone", motifs=["telephone", "portable", "smartphone", "mobile", "ecran"]),
                  ],
                  refuses=[
                      dict(motifs=[PIECES], message="{ligne} est une pièce du vélo-cargo : elle est À L'INTÉRIEUR de l'objet. Un interacteur est toujours en dehors."),
                      dict(motifs=[r"^(aller|transporter|faire|rouler|monter|porter|livrer|emmener|pedaler)\b"],
                           message="{ligne} dit ce que Léa FAIT avec le vélo-cargo : c'est un usage. Un interacteur est quelqu'un ou quelque chose, pas une action."),
                  ],
                  inconnu="{ligne} : je ne le reconnais pas. Vérifie qu'il est bien dans la scène et en dehors du vélo-cargo — ou écris-le avec un autre mot.",
                  etayage=["Une personne que l'on voit : …", "Une chose que le vélo-cargo transporte : …",
                           "Ce qui vient du ciel : …", "Ce sur quoi roulent les roues : …",
                           "Un objet fixé au guidon, mais qui n'est pas une pièce du vélo : …",
                           "Ce que l'écran de cet objet montre à Léa : …"])],
    aides=["<p>Fais trois tours de la scène. Premier tour : les <b>personnes</b>. Deuxième tour : les <b>choses</b> qui touchent "
           "le vélo-cargo ou qu'il transporte. Troisième tour : ce qui vient du <b>ciel</b> ou du <b>sol</b>. Puis cherche "
           "quelque chose qu'on ne peut pas toucher, mais qu'on <b>lit</b> sur un écran.</p>",
           "<p>Pour chaque élément de la scène, pose deux questions&nbsp;:</p>"
           "<ol><li>Est-il <b>en dehors</b> du vélo-cargo&nbsp;?</li><li>Est-il <b>en relation</b> avec lui&nbsp;?</li></ol>"
           "<p>La pluie&nbsp;: en dehors → oui. En relation → oui, elle mouille le bac, Léa et le téléphone. "
           "<b>C'est un interacteur.</b><br>La pédale&nbsp;: en dehors → non, c'est une pièce du vélo. "
           "<b>Ce n'est pas un interacteur.</b></p>"],
    jumeau=dict(consigne="Un parasol est planté dans le sable d'une plage, au soleil ; une famille pique-nique dessous. "
                         "Écris trois de ses interacteurs extérieurs.",
                correction="Par exemple&nbsp;: <b>le sable</b> (il tient le pied), <b>le soleil</b> (le parasol fait de l'ombre "
                           "contre lui), <b>le vent</b> (il pousse la toile), <b>la famille</b> (elle s'abrite dessous). "
                           "La toile et le mât sont des pièces du parasol&nbsp;: ce ne sont pas des interacteurs."),
    correction=[
        "<b>Ce qu'on cherche&nbsp;:</b> ce qui est <b>en dehors</b> du vélo-cargo <b>et</b> en relation avec lui.",
        "<b>Léa</b> → en dehors ✔ → elle pédale et dirige ✔ → interacteur",
        "<b>Les enfants</b> → en dehors ✔ → le bac les porte ✔ → interacteur",
        "<b>Les courses</b> → en dehors ✔ → le bac les porte ✔ → interacteur",
        "<b>La route en pente</b> → en dehors ✔ → les roues roulent dessus et la pente demande plus d'effort ✔ → interacteur",
        "<b>La pluie</b> → en dehors ✔ → elle mouille le vélo, Léa et le téléphone ✔ → interacteur",
        "<b>Le téléphone</b> → fixé au guidon, mais <b>pas une pièce</b> du vélo&nbsp;: on l'enlève et le vélo roule toujours ✔ → interacteur",
        "<b>L'itinéraire</b> → l'information affichée par le téléphone, que Léa lit pour diriger le vélo ✔ → interacteur",
        "<b>Refusés&nbsp;:</b> la pédale, la chaîne, la selle, le guidon, les roues, le bac → ce sont des <b>constituants</b>, dedans. "
        "« Aller au marché » → c'est un <b>usage</b>, une action.",
        ("conclusion", "La scène montre <b>sept</b> interacteurs extérieurs&nbsp;; <b>cinq</b> suffisaient."),
    ],
    retenir="un interacteur extérieur est toujours <b>en dehors</b> de l'objet, et ce n'est pas forcément une personne&nbsp;: "
            "une chose, une information ou la météo en sont aussi.",
    piege="citer des pièces de l'objet (la pédale, la chaîne)&nbsp;: elles sont <b>dedans</b>, pas autour.",
)

E2 = dict(
    id="e2", titre="Classer les interacteurs, écarter les fausses bulles", code="5e_C2.1", duree=9,
    objectif="ranger chaque interacteur dans l'une des quatre familles du programme, et reconnaître ce qui n'est pas un interacteur.",
    production="le classement de quatre interacteurs du vélo-cargo, et les fausses bulles d'un diagramme écartées.",
    mots=[("usager", "une personne qui se sert de l'objet, ou que l'objet sert (Léa, ses enfants)."),
          ("donnée", "une information&nbsp;: on la lit, on l'entend ou on la mesure, mais on ne peut pas la toucher."),
          ("autre objet", "une chose que l'on peut toucher et qui n'est pas une pièce de notre objet."),
          ("élément de l'environnement", "ce qui vient du lieu ou de la nature&nbsp;: le sol, l'air, la pluie, le soleil, la pente…"),
          ("caractéristique", "ce qui décrit l'objet lui-même&nbsp;: sa masse, sa taille, sa couleur. Elle est DANS l'objet, pas autour.")],
    consigne="<p>Le programme de technologie range les interacteurs extérieurs en <b>quatre familles</b>&nbsp;: les <b>usagers</b> "
             "(des personnes), les <b>données</b> (des informations, qu'on ne touche pas), les <b>autres objets</b> (des choses "
             "qu'on peut toucher) et les <b>éléments de l'environnement</b> (le lieu, la nature, la météo).</p>"
             "<p><b>Range chacun de ces quatre interacteurs du vélo-cargo dans sa famille.</b> Puis regarde le brouillon d'un "
             "camarade&nbsp;: il a mis six bulles autour du vélo-cargo. <b>Coche celles qui n'ont pas leur place</b> dans le "
             "diagramme, parce que ce ne sont pas des interacteurs extérieurs.</p>",
    critere="les quatre lignes sont justes, les trois fausses bulles sont cochées, et tu sais dire pourquoi le téléphone et "
            "l'itinéraire ne sont pas de la même famille.",
    widgets=[dict(type="classer", name="cl", categories=FAMILLES,
                  items=[("Léa", "usager", "Léa est une personne qui se sert du vélo-cargo."),
                         ("Le téléphone fixé au guidon", "objet", "Le téléphone, on peut le toucher et le décrocher : c'est une chose, pas une information."),
                         ("L'itinéraire affiché sur l'écran", "donnee", "L'itinéraire, on ne peut pas le toucher : c'est une information que l'on lit."),
                         ("La pluie", "environnement", "La pluie vient du ciel : elle fait partie de la météo, donc de l'environnement.")]),
             dict(type="cases", name="fausses",
                  legende="Le brouillon du camarade&nbsp;: quelles bulles n'ont <b>pas</b> leur place autour du vélo-cargo&nbsp;?",
                  options=[("masse", "la masse du vélo-cargo"),
                           ("loi", "la loi qui oblige les vélos à avoir un éclairage"),
                           ("beaute", "la beauté du vélo-cargo"),
                           ("pietons", "les piétons sur le trottoir"),
                           ("soleil", "le soleil"),
                           ("cadenas", "le cadenas de Léa")],
                  bonnes=["masse", "loi", "beaute"],
                  retours={"masse": "La masse décrit le vélo-cargo lui-même : c'est une caractéristique, DANS l'objet. Elle servira plus tard de critère.",
                           "loi": "Une loi ne touche pas le vélo-cargo : elle s'impose à ceux qui le fabriquent. C'est une exigence, pas une bulle.",
                           "beaute": "La beauté est une qualité qu'on attend de l'objet, pas quelqu'un ou quelque chose autour de lui.",
                           "pietons": "Les piétons sont des personnes autour du vélo-cargo, qu'il doit éviter : ce sont bien des interacteurs.",
                           "soleil": "Le soleil chauffe et éblouit : c'est un élément de l'environnement, il a sa bulle.",
                           "cadenas": "Le cadenas est une chose qu'on touche et qui n'est pas une pièce du vélo : un autre objet, il a sa bulle."})],
    aides=["<p>Pour chaque ligne, pose-toi les questions dans cet ordre&nbsp;: est-ce une <b>personne</b>&nbsp;? une <b>chose qu'on "
           "peut toucher</b>&nbsp;? une <b>information</b>&nbsp;? quelque chose qui vient <b>du lieu ou de la nature</b>&nbsp;?</p>",
           "<p>Le test qui départage le plus souvent&nbsp;: <b>peut-on le toucher&nbsp;?</b></p>"
           "<p>Le téléphone → oui, on le touche → <b>un autre objet</b>.<br>"
           "L'itinéraire → non, on le lit sur l'écran → <b>une donnée</b>.<br>"
           "Ils vont ensemble, mais ce ne sont pas la même chose&nbsp;: l'un affiche, l'autre est affiché.</p>"
           "<p>Pour le brouillon, une seule question&nbsp;: <b>est-ce quelqu'un ou quelque chose, en dehors du vélo-cargo&nbsp;?</b> "
           "Une masse, une beauté, une loi&nbsp;: ni quelqu'un, ni quelque chose autour de lui.</p>"],
    jumeau=dict(consigne="Classe ces quatre interacteurs d'une barrière de parking&nbsp;: le gardien&nbsp;; le code d'accès "
                         "tapé au clavier&nbsp;; la voiture&nbsp;; le vent.",
                correction="Le gardien → <b>un usager</b>. Le code d'accès → <b>une donnée</b> (on ne la touche pas, on la tape). "
                           "La voiture → <b>un autre objet</b>. Le vent → <b>un élément de l'environnement</b>."),
    correction=[
        "<b>Léa</b> → une personne qui pédale et dirige → <b>un usager</b>",
        "<b>Le téléphone</b> → une chose qu'on touche et qu'on peut décrocher du guidon → <b>un autre objet</b>",
        "<b>L'itinéraire</b> → une information qu'on lit sur l'écran, qu'on ne touche pas → <b>une donnée</b>",
        "<b>La pluie</b> → elle vient du ciel → <b>un élément de l'environnement</b>",
        "<b>Fausses bulles</b> → la masse (une caractéristique du vélo-cargo, dedans) · la loi sur l'éclairage (une règle&nbsp;: "
        "une exigence pour le fabricant) · la beauté (une qualité attendue)",
        "<b>Vraies bulles</b> → les piétons (des personnes autour) · le soleil (l'environnement) · le cadenas (un autre objet)",
        ("conclusion", "Le piège est entre le téléphone et l'itinéraire&nbsp;: le téléphone est un <b>objet</b>, ce qu'il affiche est "
                       "une <b>donnée</b>. Ils sont liés, mais pas de la même famille."),
    ],
    retenir="quatre familles d'interacteurs&nbsp;: <b>usagers, données, autres objets, éléments de l'environnement</b>. Une liste "
            "qui ne contient que des personnes est une liste à moitié faite.",
    piege="mettre l'appareil et l'information qu'il affiche dans la même famille, ou donner une bulle à une caractéristique "
          "de l'objet (sa masse, sa beauté) ou à une loi.",
)

E3 = dict(
    id="e3", titre="Compléter le diagramme pieuvre et ses fonctions", code="5e_C2.1", duree=11,
    objectif="compléter un diagramme des interacteurs extérieurs, écarter ce qui n'en est pas, et lire ses fonctions.",
    production="le diagramme pieuvre du vélo-cargo complété, la raison des deux intrus, et deux fonctions retrouvées.",
    mots=[("diagramme des interacteurs extérieurs", "le schéma qui place l'objet au centre et, autour, chaque interacteur "
           "extérieur. C'est le nom du programme de technologie."),
          ("diagramme pieuvre", "l'autre nom, très employé, du même schéma&nbsp;: l'objet est la tête, les traits sont les tentacules."),
          ("fonction principale (FP)", "le service rendu par l'objet&nbsp;: un trait qui relie <b>deux</b> éléments extérieurs "
           "<b>en passant par</b> l'objet."),
          ("fonction contrainte (FC)", "on dit aussi fonction complémentaire&nbsp;: ce que l'objet doit respecter pour s'adapter "
           "à <b>un</b> élément extérieur. Le trait va de l'objet à cet élément, et à lui seul."),
          ("intrus", "un mot qui n'a pas sa place dans la liste.")],
    intro="<p>Ce schéma s'appelle le <b>diagramme des interacteurs extérieurs</b>&nbsp;; on l'appelle aussi le "
          "<b>diagramme pieuvre</b>. Le vélo-cargo est au centre. Quatre bulles sont déjà remplies. Les trois bulles en "
          "pointillés sont vides&nbsp;: chacune annonce seulement la <b>famille</b> attendue.</p>"
          "<p>Chaque trait porte un nom. <b>FP</b> veut dire <b>fonction principale</b>&nbsp;: la courbe part d'un élément, "
          "<b>passe par le vélo-cargo</b> et arrive à un autre élément — c'est le service rendu. <b>FC</b> veut dire "
          "<b>fonction contrainte</b>&nbsp;: le trait relie le vélo-cargo à <b>un seul</b> élément — c'est ce que le vélo-cargo "
          "doit respecter. Une fonction s'écrit avec un verbe à l'infinitif&nbsp;:</p>"
          "<ul><li><b>FP1</b>&nbsp;: permettre à Léa de transporter ses enfants.</li>"
          "<li><b>FP2</b>&nbsp;: permettre à Léa de transporter ses courses.</li>"
          "<li><b>FC1</b>&nbsp;: protéger les enfants pendant le trajet.</li>"
          "<li><b>FC2</b>&nbsp;: résister à la pluie.</li>"
          "<li><b>FC3</b>&nbsp;: … (à retrouver)</li>"
          "<li><b>FC4</b>&nbsp;: tenir le téléphone de Léa sans qu'il tombe.</li>"
          "<li><b>FC5</b>&nbsp;: … (à retrouver)</li></ul>",
    consigne="<p><b>Complète les trois bulles vides</b> avec les mots de la banque&nbsp;: <i>les enfants · les courses · "
             "la route en pente · la pédale · la chaîne</i>. Tes choix s'écrivent dans le schéma. Deux mots de la banque "
             "sont des <b>intrus</b>&nbsp;: <b>dis pourquoi</b> ils n'ont pas de bulle. Puis <b>explique</b> pourquoi FP1 passe "
             "par le vélo-cargo, <b>retrouve</b> les phrases de FC3 et de FC5, et <b>relie</b> la bête à cornes du vélo-cargo "
             "à son diagramme pieuvre.</p>",
    critere="chaque bulle porte un interacteur de la famille annoncée, tu donnes la bonne raison pour les intrus, et tu "
            "retrouves FC3 et FC5.",
    widgets=[dict(type="slots", intro='<figure class="figure schema-vivant">' + PIEUVRE_A_COMPLETER +
                  '<figcaption>Le diagramme pieuvre du vélo-cargo, avec ses fonctions. Tes choix s\'écrivent dans les bulles en pointillés.</figcaption></figure>',
                  slots=[dict(name="b1", cible="pv-b1", legende="Bulle ① — elle attend <b>un usager</b>",
                              options=["les enfants", "les courses", "la route en pente", "la pédale", "la chaîne"], bonnes=["les enfants"],
                              indice="Bulle ① : il faut une personne que le vélo-cargo sert."),
                         dict(name="b2", cible="pv-b2", legende="Bulle ② — elle attend <b>un autre objet</b>",
                              options=["les enfants", "les courses", "la route en pente", "la pédale", "la chaîne"], bonnes=["les courses"],
                              indice="Bulle ② : il faut une chose qu'on touche et qui n'est pas une pièce du vélo."),
                         dict(name="b3", cible="pv-b3", legende="Bulle ③ — elle attend <b>un élément de l'environnement</b>",
                              options=["les enfants", "les courses", "la route en pente", "la pédale", "la chaîne"], bonnes=["la route en pente"],
                              indice="Bulle ③ : il faut quelque chose qui vient du lieu, là où roule le vélo.")]),
             dict(type="choix", name="intrus", legende="Pourquoi la pédale et la chaîne n'ont-elles pas de bulle&nbsp;?",
                  options=[("bouger", "Parce qu'elles bougent tout le temps."),
                           ("pieces", "Parce que ce sont des pièces du vélo-cargo&nbsp;: elles ne sont pas en dehors de l'objet."),
                           ("personnes", "Parce que ce ne sont pas des personnes."),
                           ("petites", "Parce qu'elles sont trop petites pour compter.")],
                  bonne="pieces",
                  retours={"bouger": "Les enfants bougent aussi, et ils ont une bulle : bouger ou non ne décide de rien.",
                           "personnes": "La pluie et la route ne sont pas des personnes non plus, et ce sont des interacteurs.",
                           "petites": "La taille ne décide de rien : seule compte la question « dedans ou dehors ? ».",
                           "pieces": "Oui : un interacteur est toujours extérieur. Une pièce de l'objet est dedans."}),
             dict(type="choix", name="fp", legende="Pourquoi le trait FP1 passe-t-il par le vélo-cargo&nbsp;?",
                  options=[("lea", "Parce que Léa est plus importante que les autres éléments."),
                           ("service", "Parce qu'il relie Léa et ses enfants grâce au vélo-cargo&nbsp;: c'est le service rendu."),
                           ("long", "Parce que FP1 est le trait le plus long du schéma."),
                           ("dedans", "Parce que les enfants sont à l'intérieur du vélo-cargo.")],
                  bonne="service",
                  retours={"lea": "Léa a aussi une place dans le schéma, mais l'importance d'une personne ne décide pas de la forme du trait.",
                           "long": "La longueur d'un trait ne veut rien dire : c'est le nombre d'éléments qu'il relie qui compte.",
                           "dedans": "Les enfants sont assis dans le bac, mais ce ne sont pas des pièces du vélo-cargo : ils restent des éléments extérieurs.",
                           "service": "Oui : une fonction principale relie deux éléments extérieurs en passant par l'objet. C'est ce que l'objet fait POUR eux."}),
             dict(type="classer", name="fc",
                  categories=[("fp", "permettre à Léa de transporter ses enfants"),
                              ("pente", "monter les pentes sans trop d'effort"),
                              ("lire", "laisser lire l'itinéraire à Léa sans lâcher le guidon"),
                              ("pluie", "résister à la pluie")],
                  items=[("FC3 — le trait vers la route en pente&nbsp;: quelle phrase&nbsp;?", "pente", "FC3 va vers la route en pente : que doit faire le vélo-cargo face à une côte ?"),
                         ("FC5 — le trait vers l'itinéraire&nbsp;: quelle phrase&nbsp;?", "lire", "FC5 va vers l'itinéraire, une information que Léa doit pouvoir lire en roulant.")]),
             dict(type="classer", name="bete",
                  intro="<p>La bête à cornes du vélo-cargo dit&nbsp;: <b>à qui</b>&nbsp;? Léa · <b>sur quoi</b>&nbsp;? ses enfants · "
                        "<b>dans quel but</b>&nbsp;? les transporter en ville. Où chaque partie se retrouve-t-elle dans le diagramme pieuvre&nbsp;?</p>",
                  categories=[("depart", "la bulle d'où part la FP1"), ("arrivee", "la bulle où arrive la FP1"),
                              ("phrase", "la phrase de la FP1"), ("centre", "l'objet au centre, par où passe la FP1")],
                  items=[("« À qui ? » — Léa", "depart", "La FP1 part de la personne à qui l'objet rend service."),
                         ("« Sur quoi ? » — ses enfants", "arrivee", "La FP1 arrive à ce sur quoi l'objet agit."),
                         ("« Dans quel but ? » — les transporter", "phrase", "Le but devient la phrase : permettre à Léa de les transporter."),
                         ("Le vélo-cargo", "centre", "Le produit est au milieu dans les deux schémas : la FP1 passe par lui.")])],
    aides=["<p>Lis d'abord la famille annoncée dans chaque bulle vide, puis cherche dans la banque le mot qui lui correspond. "
           "Il restera deux mots&nbsp;: demande-toi s'ils sont dedans ou dehors. Pour les fonctions, regarde vers quelle bulle "
           "va chaque trait.</p>",
           "<p>Bulle ① → une personne → parmi les mots, une seule désigne des personnes.<br>"
           "Bulle ② → une chose qu'on touche, transportée par le vélo.<br>"
           "Bulle ③ → ce sur quoi roulent les roues.<br>"
           "Restent la pédale et la chaîne → on les trouve <b>dans</b> le vélo-cargo → pas de bulle.<br>"
           "FP1 → touche <b>deux</b> éléments (Léa, les enfants) → c'est le service rendu.<br>"
           "FC3 → va vers la route en pente → sa phrase commence par un verbe à l'infinitif&nbsp;: «&nbsp;monter les pentes…&nbsp;».</p>"],
    jumeau=dict(consigne="Le diagramme pieuvre d'un parapluie&nbsp;: un trait part de la personne, passe par le parapluie et "
                         "arrive à la pluie&nbsp;; un autre relie seulement le parapluie au vent. Lequel est une FP, lequel une FC&nbsp;?",
                correction="Le trait personne → parapluie → pluie relie <b>deux</b> éléments en passant par l'objet&nbsp;: c'est la "
                           "<b>FP</b> (protéger la personne de la pluie). Le trait parapluie → vent ne touche qu'<b>un</b> élément&nbsp;: "
                           "c'est une <b>FC</b> (résister au vent)."),
    correction=[
        '<figure class="figure">' + PIEUVRE_CORRIGE + '<figcaption>Le diagramme corrigé : chaque bulle porte sa famille, chaque trait sa fonction.</figcaption></figure>',
        "<b>Bulle ①</b>, un usager → <b>les enfants</b> → le vélo-cargo les transporte",
        "<b>Bulle ②</b>, un autre objet → <b>les courses</b> → une chose qu'on touche, que le bac porte",
        "<b>Bulle ③</b>, un élément de l'environnement → <b>la route en pente</b> → les roues roulent dessus",
        "<b>Les intrus</b> → la pédale et la chaîne → ce sont des <b>pièces du vélo-cargo</b>, dedans",
        "Les trois autres raisons ne tiennent pas&nbsp;: les enfants bougent aussi et ont une bulle&nbsp;; la pluie n'est pas une "
        "personne et a une bulle&nbsp;; la taille ne décide de rien.",
        "<b>FP1</b> → relie <b>deux</b> éléments, Léa et ses enfants, <b>en passant par</b> le vélo-cargo → le service rendu",
        "<b>FP1 et la bête à cornes</b> → Léa, c'est «&nbsp;à qui&nbsp;?&nbsp;» (la bulle de départ) ; les enfants, «&nbsp;sur "
        "quoi&nbsp;?&nbsp;» (la bulle d'arrivée) ; transporter, «&nbsp;dans quel but&nbsp;?&nbsp;» (la phrase) ; le vélo-cargo, au "
        "centre des deux schémas → la FP1 dit la <b>fonction d'usage</b>, c'est la corne de la bête à cornes",
        '<figure class="figure">' + BETE_VERS_PIEUVRE + '<figcaption>La corne devient la FP1.</figcaption></figure>',
        "<b>FC1</b> → au bout de FP1, les enfants imposent aussi une contrainte → «&nbsp;protéger les enfants pendant le trajet&nbsp;» "
        "(c'est souvent le cas&nbsp;: ce sur quoi l'objet agit lui impose une condition)",
        "<b>FC3</b> → le vélo-cargo et la route en pente → « monter les pentes sans trop d'effort »",
        "<b>FC5</b> → le vélo-cargo et l'itinéraire → « laisser lire l'itinéraire à Léa sans lâcher le guidon »",
        ("conclusion", "Une bulle&nbsp;: <b>dedans ou dehors&nbsp;?</b> Un trait&nbsp;: <b>deux éléments par l'objet</b> (FP) ou "
                       "<b>un seul</b> (FC)."),
    ],
    retenir="le <b>diagramme pieuvre</b> met l'objet au centre. Une <b>fonction principale</b> (FP) relie deux éléments "
            "extérieurs en passant par l'objet&nbsp;; une <b>fonction contrainte</b> (FC) relie l'objet à un seul élément. "
            "Chaque fonction s'écrit avec un verbe à l'infinitif.",
    piege="donner une bulle à une pièce de l'objet, ou appeler « fonction principale » un trait qui ne touche qu'un élément.",
)

E4 = dict(
    id="e4", titre="Relier une forme à un interacteur", code="5e_C2.2", duree=12,
    objectif="expliquer un choix de conception par l'interacteur qu'il sert et par son domaine.",
    production="trois choix reliés à leur interacteur et à leur domaine, et une explication écrite.",
    mots=[("choix de conception", "une décision prise par ceux qui ont dessiné l'objet&nbsp;: une forme, un matériau, une pièce ajoutée."),
          ("sécurité", "éviter qu'une personne se blesse."),
          ("ergonomie", "rendre l'objet confortable et facile à utiliser, avec moins d'effort."),
          ("développement durable", "préserver la planète&nbsp;: faire durer l'objet, réparer plutôt que jeter, économiser l'énergie et les matériaux."),
          ("carter", "un capot qui enferme une pièce pour la protéger (ici, la chaîne).")],
    documents=[dict(svg=SCENE_REPERES, legende="Trois détails du vélo-cargo, repérés A, B et C.",
                    description="<ul><li><b>A</b> — le bac a des rebords hauts, et chaque enfant a une ceinture.</li>"
                                "<li><b>B</b> — une commande de huit vitesses, sur le guidon.</li>"
                                "<li><b>C</b> — la chaîne est enfermée dans un carter, et les pièces sont traitées contre la rouille.</li></ul>")],
    intro="<ul><li><b>A</b> — le bac a des <b>rebords hauts</b>, et chaque enfant a une <b>ceinture</b>.</li>"
          "<li><b>B</b> — une commande de <b>huit vitesses</b>, sur le guidon.</li>"
          "<li><b>C</b> — la chaîne est enfermée dans un <b>carter</b>, et les pièces sont traitées <b>contre la rouille</b>.</li></ul>",
    consigne="<p>Chaque détail est un <b>choix de conception</b>&nbsp;: les concepteurs l'ont décidé pour s'adapter à un "
             "interacteur. <b>Pour A, B et C, choisis l'interacteur qu'il sert, puis le domaine</b>&nbsp;: la <b>sécurité</b> "
             "(ne pas se blesser), l'<b>ergonomie</b> (le confort, moins d'effort) ou le <b>développement durable</b> (faire "
             "durer l'objet, moins de pièces à fabriquer et à jeter). Puis <b>explique</b> le choix A en une phrase.</p>",
    critere="six réponses justes, et une phrase qui dit pour qui est le choix A et ce qu'il évite.",
    widgets=[dict(type="classer", name="int",
                  categories=[("enfants", "les enfants"), ("route", "la route en pente"), ("pluie", "la pluie"), ("itineraire", "l'itinéraire")],
                  items=[("A — les rebords hauts et les ceintures servent…", "enfants", "A : regarde qui est assis dans le bac."),
                         ("B — les huit vitesses servent à s'adapter à…", "route", "B : on change de vitesse quand l'effort change, en montée par exemple."),
                         ("C — le carter et le traitement contre la rouille protègent de…", "pluie", "C : la rouille vient de l'eau.")]),
             dict(type="classer", name="dom",
                  categories=[("securite", "la sécurité"), ("ergonomie", "l'ergonomie"), ("dd", "le développement durable")],
                  items=[("A — rebords hauts et ceintures : quel domaine ?", "securite", "A : que se passerait-il sans rebords ni ceintures, dans un virage ?"),
                         ("B — huit vitesses : quel domaine ?", "ergonomie", "B : les vitesses rendent la montée moins fatigante."),
                         ("C — carter et traitement contre la rouille : quel domaine ?", "dd", "C : un vélo qui ne rouille pas dure plus longtemps : moins de pièces à fabriquer et à jeter.")]),
             dict(type="texte", name="pourquoi", exemple="Les rebords hauts et les ceintures empêchent les enfants de tomber du bac quand le vélo tourne : c'est un choix de sécurité.", lignes=3,
                  label="Explique en une phrase pourquoi le bac a des rebords hauts et des ceintures (choix A).",
                  criteres=[dict(label="ta phrase dit pour qui est ce choix (les enfants)", motifs=["enfant", "passager", "petits?\\b"],
                                 manque="Dis pour QUI est ce choix : qui est assis dans le bac ?"),
                            dict(label="ta phrase dit ce que le choix évite ou protège (une chute, une blessure)",
                                 motifs=["tomb", "chut", "bless", "proteg", "secur", "danger", "ejecte", "glisse", "accident", "retien", "tien"],
                                 manque="Dis ce que les rebords et les ceintures ÉVITENT : que pourrait-il arriver aux enfants sans eux ?")],
                  etayage=["Le bac a des rebords hauts et des ceintures pour que les enfants…",
                           "Sans ces rebords, dans un virage, les enfants pourraient…"])],
    aides=["<p>Pour chaque détail, demande-toi d'abord <b>contre quoi</b> ou <b>pour qui</b> il est là. Le domaine vient ensuite&nbsp;: "
           "se blesser → sécurité&nbsp;; se fatiguer → ergonomie&nbsp;; jeter, réparer, faire durer → développement durable.</p>",
           "<p>A → les enfants sont assis dans le bac → sans rebords ni ceintures, ils peuvent tomber → <b>sécurité</b>.<br>"
           "B → en montée, il faut plus de force → les vitesses diminuent l'effort → <b>ergonomie</b>.<br>"
           "C → l'eau fait rouiller la chaîne → protégée, elle dure plus longtemps → <b>développement durable</b>.</p>"],
    jumeau=dict(consigne="Une poussette a un frein au pied et une capote. Pour chacun, donne l'interacteur et le domaine.",
                correction="Le frein → la pente du trottoir (la poussette ne doit pas partir seule) → <b>sécurité</b>. La capote → le "
                           "soleil et la pluie (le bébé reste à l'abri) → <b>ergonomie</b>, le confort du bébé."),
    correction=[
        "<b>A</b> → sert <b>les enfants</b> → sans rebords ni ceintures, ils pourraient tomber du bac → <b>sécurité</b>",
        "<b>B</b> → sert à s'adapter à <b>la route en pente</b> → les vitesses rendent la montée moins fatigante → <b>ergonomie</b>",
        "<b>C</b> → protège de <b>la pluie</b> → une chaîne qui ne rouille pas dure plus longtemps&nbsp;: moins de pièces à fabriquer "
        "et à jeter → <b>développement durable</b>",
        "<b>Une phrase attendue pour A&nbsp;:</b> « Le bac a des rebords hauts et des ceintures pour que <b>les enfants</b> ne "
        "<b>tombent</b> pas dans un virage ou un freinage. »",
        ("conclusion", "Chaque forme répond à « <b>pour qui, contre quoi&nbsp;?</b> ». La réponse est presque toujours dans la "
                       "liste des interacteurs."),
    ],
    retenir="pour expliquer un choix de conception, on cherche l'<b>interacteur</b> qu'il sert, puis son <b>domaine</b>&nbsp;: "
            "sécurité, ergonomie ou développement durable.",
    piege="décrire le détail (« il y a des ceintures ») au lieu de l'expliquer (« pour que les enfants ne tombent pas »).",
)

# ─────────────────────────────────────────────────────────────────────────────
# 4e
# ─────────────────────────────────────────────────────────────────────────────
E5 = dict(
    id="e5", titre="Le service rendu et les contraintes", code="4e_C2.2", duree=10,
    objectif="distinguer, dans un diagramme pieuvre, le service rendu (FP) des contraintes (FC).",
    production="le type de chacun des six traits, et la phrase de trois contraintes.",
    mots=[("fonction principale (FP)", "le service que l'objet rend&nbsp;: elle relie <b>deux</b> interacteurs en passant par l'objet."),
          ("fonction contrainte (FC)", "une condition que l'objet doit respecter pour s'adapter à <b>un</b> interacteur."),
          ("cuve", "un grand réservoir&nbsp;; ici, il recueille l'eau de pluie du toit.")],
    documents=[dict(svg=PIEUVRE_JARDIN, legende="Le diagramme pieuvre du système d'arrosage, avec six traits numérotés.",
                    description="<p>Au centre, le système d'arrosage. Six interacteurs autour&nbsp;: la gardienne (un usager), les "
                                "plantes (l'environnement), la cuve d'eau de pluie (un autre objet), la pluie et le soleil "
                                "(l'environnement), le smartphone (un autre objet), l'heure d'arrosage choisie (une donnée).</p>"
                                "<p>Le trait 1 est une courbe qui part de la gardienne, passe par le système et arrive aux plantes. "
                                "Les traits 2 à 6 sont droits et relient le système à un seul interacteur&nbsp;: 2 à la pluie et au soleil, "
                                "3 à la cuve, 4 au smartphone, 5 à la gardienne, 6 à l'heure d'arrosage choisie.</p>")],
    intro="<p>Le jardin partagé du collège s'équipe d'un <b>système d'arrosage connecté</b>&nbsp;: il arrose les plantes à "
          "l'heure choisie, avec l'eau d'une cuve qui recueille la pluie, et envoie des nouvelles sur le smartphone de la "
          "gardienne, Mme Joseph. Voici son diagramme des interacteurs extérieurs — son <b>diagramme pieuvre</b>.</p>",
    consigne="<p>Dans un diagramme pieuvre, on trace deux sortes de traits. Une <b>fonction principale</b> (FP) relie "
             "<b>deux</b> interacteurs en passant par l'objet&nbsp;: c'est le <b>service rendu</b>. Une <b>fonction contrainte</b> "
             "(FC) relie l'objet à <b>un seul</b> interacteur&nbsp;: c'est une <b>condition</b> que l'objet doit respecter. "
             "Chaque fonction, FP ou FC, s'écrit avec une phrase qui commence par un <b>verbe à l'infinitif</b>&nbsp;: "
             "«&nbsp;permettre…&nbsp;», «&nbsp;résister…&nbsp;».</p>"
             "<p><b>Un même interacteur peut porter la FP et une FC.</b> C'est souvent le cas de l'usager&nbsp;: la FP dit le "
             "service qu'il reçoit, la FC dit ce que l'objet doit respecter pour lui (être facile à régler, par exemple). "
             "Ici, deux traits touchent la gardienne.</p>"
             "<p><b>Dis pour chaque trait s'il est une FP ou une FC, puis choisis la phrase des traits 2, 3 et 4.</b></p>",
    critere="neuf réponses justes ; tu sais dire pourquoi le trait 1 passe par deux interacteurs.",
    widgets=[dict(type="classer", name="type", categories=[("fp", "une fonction principale (FP) : le service rendu"),
                                                             ("fc", "une fonction contrainte (FC) : une condition à respecter")],
                  items=[("Trait 1 (de la gardienne aux plantes, en passant par le système)", "fp", "Le trait 1 touche DEUX interacteurs."),
                         ("Trait 2 (la pluie et le soleil)", "fc", "Le trait 2 ne touche qu'un interacteur."),
                         ("Trait 3 (la cuve d'eau de pluie)", "fc", "Le trait 3 ne touche qu'un interacteur."),
                         ("Trait 4 (le smartphone)", "fc", "Le trait 4 ne touche qu'un interacteur."),
                         ("Trait 5 (la gardienne)", "fc", "Le trait 5 ne touche qu'un interacteur : la gardienne y est seule."),
                         ("Trait 6 (l'heure d'arrosage choisie)", "fc", "Le trait 6 ne touche qu'un interacteur : une donnée.")]),
             dict(type="classer", name="phrase",
                  categories=[("meteo", "Résister à la pluie et au soleil."),
                              ("cuve", "Prendre dans la cuve seulement l'eau dont les plantes ont besoin."),
                              ("tel", "Envoyer l'état de l'arrosage au smartphone."),
                              ("fp", "Permettre à la gardienne d'arroser les plantes sans être là.")],
                  items=[("Trait 2 — vers la pluie et le soleil : quelle phrase&nbsp;?", "meteo", "Le trait 2 va vers la pluie et le soleil."),
                         ("Trait 3 — vers la cuve : quelle phrase&nbsp;?", "cuve", "Le trait 3 va vers la cuve."),
                         ("Trait 4 — vers le smartphone : quelle phrase&nbsp;?", "tel", "Le trait 4 va vers le smartphone.")])],
    aides=["<p>Compte les interacteurs que chaque trait touche. Deux → FP. Un seul → FC. Pour la phrase, regarde vers quelle bulle "
           "va le trait.</p>",
           "<p>Trait 1 → gardienne + plantes → <b>deux</b> → FP → c'est le service&nbsp;: arroser à la place de la gardienne.<br>"
           "Traits 2 à 6 → un seul interacteur chacun → FC → ce sont des conditions.<br>"
           "La phrase « permettre à la gardienne d'arroser… » est celle du trait 1&nbsp;: elle ne va avec aucun des traits 2, 3, 4.</p>"],
    jumeau=dict(consigne="Pour une borne de recharge de trottinettes, le trait A relie l'usager à la trottinette en passant par la "
                         "borne&nbsp;; le trait B relie la borne au réseau électrique. A et B sont-ils des FP ou des FC&nbsp;?",
                correction="A touche deux interacteurs (l'usager, la trottinette) → <b>FP</b>&nbsp;: recharger la trottinette de "
                           "l'usager. B touche un seul interacteur → <b>FC</b>&nbsp;: se brancher sur le réseau électrique."),
    correction=[
        "<b>Trait 1</b> → touche la gardienne <b>et</b> les plantes → <b>FP</b> → « permettre à la gardienne d'arroser les plantes sans être là »",
        "<b>Trait 2</b> → un seul interacteur, la météo → <b>FC</b> → « résister à la pluie et au soleil »",
        "<b>Trait 3</b> → un seul interacteur, la cuve → <b>FC</b> → « prendre seulement l'eau dont les plantes ont besoin »",
        "<b>Trait 4</b> → un seul interacteur, le smartphone → <b>FC</b> → « envoyer l'état de l'arrosage au smartphone »",
        "<b>Trait 5</b> → un seul interacteur, la gardienne → <b>FC</b> → « être facile à régler par la gardienne »&nbsp;: la gardienne "
        "porte la FP <b>et</b> une FC — c'est normal, un même interacteur peut porter les deux.",
        "<b>Trait 6</b> → un seul interacteur, l'heure choisie (une donnée) → <b>FC</b> → « respecter l'heure d'arrosage choisie »",
        "<b>Le diagramme corrigé</b>, chaque fonction nommée et écrite avec un verbe à l'infinitif&nbsp;:"
        '<figure class="figure">' + PIEUVRE_JARDIN_CORRIGE + "<figcaption>Le diagramme pieuvre du système d'arrosage, corrigé&nbsp;: "
        "FP1, puis FC1 à FC5.</figcaption></figure>"
        "<ul>" + "".join("<li><b>%s</b>&nbsp;: %s.</li>" % f for f in FONCTIONS_JARDIN) + "</ul>",
        ("conclusion", "<b>Deux interacteurs</b> reliés par l'objet → le service rendu (FP). <b>Un seul</b> → une condition à respecter (FC). "
                       "Chaque fonction commence par un verbe à l'infinitif."),
    ],
    retenir="la <b>fonction principale</b> (FP) relie deux interacteurs en passant par l'objet&nbsp;: c'est le service rendu. "
            "Une <b>fonction contrainte</b> (FC) relie l'objet à un seul interacteur&nbsp;: c'est une condition.",
    piege="croire qu'un interacteur ne peut avoir qu'un trait&nbsp;: la gardienne est dans la FP et dans une FC. Autre piège&nbsp;: "
          "écrire «&nbsp;le système doit…&nbsp;» au lieu de commencer la fonction par son verbe à l'infinitif.",
)

E6 = dict(
    id="e6", titre="Le cahier des charges : critère, niveau, flexibilité", code="4e_C2.2", duree=15,
    objectif="donner à une contrainte un critère, un niveau et une flexibilité, et dire d'où vient ce niveau.",
    production="trois critères choisis, l'origine d'un niveau, quatre classes de flexibilité, et une exigence écrite avec "
               "critère et niveau.",
    mots=[("critère", "ce que l'on mesure ou contrôle pour savoir si la contrainte est respectée."),
          ("niveau", "la valeur à atteindre pour ce critère (au moins…, au plus…)."),
          ("norme", "un texte officiel qui fixe la même règle pour tous les fabricants, dans tout un pays ou dans le monde."),
          ("indice de protection (IP)", "un code fixé par une norme internationale&nbsp;; le chiffre après IPX dit à quelle eau "
           "l'appareil résiste (IPX4&nbsp;: projections d'eau de tous côtés)."),
          ("cahier des charges fonctionnel (CdCF)", "le document qui rassemble ce que le client demande à l'objet&nbsp;: "
           "chaque fonction y reçoit un critère, un niveau et une flexibilité."),
          ("flexibilité", "la marge acceptée autour du niveau&nbsp;: de combien on peut s'en écarter sans que le client refuse l'objet."),
          ("classe de flexibilité", "un code de F0 à F3 qui dit si le niveau se négocie&nbsp;: F0, pas du tout (impératif)&nbsp;; "
           "F1, un peu&nbsp;; F2, assez&nbsp;; F3, beaucoup."),
          ("label", "une étiquette officielle qui garantit une qualité (économie d'eau, d'énergie…).")],
    intro="<p>« Résister à la pluie »&nbsp;: c'est une bonne contrainte, mais <b>qui décide</b> si c'est réussi&nbsp;? Pour qu'on "
          "puisse la vérifier, on lui ajoute un <b>critère</b> (ce qu'on mesure ou contrôle) et un <b>niveau</b> (la valeur à "
          "atteindre). On obtient une <b>exigence</b>.</p>"
          "<p>Le <b>cahier des charges fonctionnel</b> (CdCF) range ces exigences dans un tableau. La dernière colonne, la "
          "<b>flexibilité</b>, dit de combien on peut s'écarter du niveau. On la note par une <b>classe</b>&nbsp;:</p>"
          "<ul><li><b>F0</b>&nbsp;: flexibilité nulle — le niveau est impératif&nbsp;;</li>"
          "<li><b>F1</b>&nbsp;: flexibilité faible — le niveau est peu négociable&nbsp;;</li>"
          "<li><b>F2</b>&nbsp;: flexibilité moyenne — le niveau est négociable&nbsp;;</li>"
          "<li><b>F3</b>&nbsp;: flexibilité forte — le niveau est très négociable.</li></ul>"
          '<div class="defile"><table><caption>Extrait du cahier des charges du système d\'arrosage (entre parenthèses&nbsp;: '
          "l'interacteur que la fonction concerne)</caption>"
          "<tr><th>Fonction</th><th>Désignation</th><th>Critère</th><th>Niveau</th><th>Flexibilité</th></tr>"
          "<tr><td>FP (la gardienne → les plantes)</td><td>Permettre à la gardienne d'arroser les plantes sans être là</td>"
          "<td>Jours d'arrosage sans la gardienne</td><td>7 jours sur 7, vacances comprises</td><td>F0&nbsp;: aucun jour oublié</td></tr>"
          "<tr><td>FC (la pluie et le soleil)</td><td>Résister à la pluie et au soleil</td><td>Indice de protection</td><td>IPX4 au moins</td>"
          "<td>à trouver</td></tr>"
          "<tr><td>FC (la cuve)</td><td>Prendre seulement l'eau dont les plantes ont besoin</td><td>Volume d'eau par jour</td>"
          "<td>10&nbsp;L</td><td>à trouver</td></tr>"
          "<tr><td>FC (le smartphone)</td><td>Envoyer l'état de l'arrosage au smartphone</td><td>à écrire (dernière question)</td>"
          "<td>à écrire</td><td>—</td></tr>"
          "<tr><td>FC (la gardienne)</td><td>Être sans danger pour la gardienne</td><td>Tension d'alimentation</td><td>12&nbsp;V</td>"
          "<td>à trouver</td></tr>"
          "<tr><td>FC (la gardienne)</td><td>Être facile à régler par la gardienne</td><td>Temps pour changer l'heure d'arrosage</td><td>2&nbsp;min au plus</td>"
          "<td>à trouver</td></tr>"
          "</table></div>"
          "<p>La gardienne a deux lignes&nbsp;: un même interacteur peut imposer plusieurs contraintes.</p>",
    consigne="<p><b>Pour chaque contrainte, choisis le critère qui permet de la vérifier.</b> Puis dis d'où vient le niveau "
             "« IPX4 ». <b>Classe</b> ensuite chaque réponse de la gardienne dans sa classe de flexibilité (F0 à F3), et "
             "<b>écris l'exigence complète</b> de la contrainte du smartphone.</p>",
    critere="trois critères justes, la bonne origine pour IPX4, quatre classes de flexibilité justes, et une exigence qui "
            "contient un nombre et son unité.",
    widgets=[dict(type="classer", name="crit",
                  categories=[("ip", "l'indice de protection contre l'eau (IP)"), ("litres", "le volume d'eau utilisé par jour, en litres"),
                              ("temps", "le temps pour changer l'heure d'arrosage, en minutes"), ("couleur", "la couleur du boîtier")],
                  items=[("« Résister à la pluie et au soleil »", "ip", "Résister à la pluie : ce qu'on contrôle, c'est l'eau qui peut entrer."),
                         ("« Prendre seulement l'eau dont les plantes ont besoin »", "litres", "Ne pas gaspiller : ce qu'on mesure, c'est une quantité d'eau."),
                         ("« Être facile à régler par la gardienne »", "temps", "Facile : ce qu'on mesure, c'est le temps que prend le réglage.")]),
             dict(type="choix", name="ipx4", legende="Le niveau « IPX4 au moins » vient…",
                  options=[("gardienne", "…de l'avis de la gardienne, qui préfère cette valeur."),
                           ("norme", "…d'une norme&nbsp;: un texte officiel qui fixe les mêmes codes IP pour tous les fabricants."),
                           ("label", "…d'un label d'économie d'eau."),
                           ("couleur", "…de la couleur du boîtier, plus ou moins étanche.")],
                  bonne="norme",
                  retours={"gardienne": "La gardienne peut DEMANDER un niveau dans son cahier des charges, mais le code IPX4 lui-même, ce qu'il veut dire et comment on le teste, sont fixés par une norme.",
                           "label": "Un label garantit une qualité (économiser l'eau, par exemple) ; il ne définit pas les codes de résistance à l'eau.",
                           "couleur": "La couleur ne dit rien de l'étanchéité : ce sont les joints et la forme du boîtier qui comptent.",
                           "norme": "Oui : les codes IP sont fixés par une norme internationale. IPX4 veut dire : résiste aux projections d'eau de tous côtés."}),
             dict(type="classer", name="flex",
                  categories=[("f0", "F0 — flexibilité nulle&nbsp;: le niveau est impératif"),
                              ("f1", "F1 — flexibilité faible&nbsp;: peu négociable"),
                              ("f2", "F2 — flexibilité moyenne&nbsp;: négociable"),
                              ("f3", "F3 — flexibilité forte&nbsp;: très négociable")],
                  items=[("Sans danger, 12&nbsp;V. La gardienne&nbsp;: « Pas question d'amener le 230&nbsp;V au jardin. »", "f0",
                          "« Pas question » : aucun écart n'est accepté, et le 230 V est un danger."),
                         ("Résister à la pluie, IPX4. La gardienne&nbsp;: « IPX3 sous l'abri, à la rigueur, si on me prouve que la pluie n'y entre pas. »", "f1",
                          "Un écart est possible, mais seulement à une condition précise : c'est peu négociable."),
                         ("L'eau nécessaire, 10&nbsp;L par jour. La gardienne&nbsp;: « 9 ou 11 litres, ça ira aussi. »", "f2",
                          "Un écart d'un litre est accepté sans condition : c'est négociable."),
                         ("Se régler en 2&nbsp;min au plus. La gardienne&nbsp;: « Même 5 minutes, ça m'ira&nbsp;: je ne le fais qu'une fois par mois. »", "f3",
                          "Un écart très large est accepté, sans condition : c'est très négociable.")]),
             dict(type="texte", name="exig", exemple="Le système doit envoyer l'état de l'arrosage au smartphone au moins 1 fois par jour.", lignes=3,
                  label="Écris l'exigence complète de la contrainte « envoyer l'état de l'arrosage au smartphone » : avec un critère et un niveau.",
                  criteres=[dict(label="ton exigence parle bien du smartphone ou du message envoyé",
                                 motifs=["smartphone", "telephone", "portable", "message", "notification", "envoi", "envoy"],
                                 manque="Ton exigence doit parler de ce qu'on envoie au smartphone."),
                            dict(label="elle contient un nombre (le niveau)", motifs=[r"\d"],
                                 manque="Il manque le NIVEAU : un nombre (au moins…, au plus…, en moins de…)."),
                            dict(label="le nombre a son unité (secondes, minutes, fois par jour…)",
                                 motifs=[r"\d\s*(s\b|sec|min|h\b|heure|jour|fois|%|messages?|minutes?)"],
                                 manque="Un nombre sans unité n'est pas un niveau : écris « minutes », « fois par jour »…")],
                  etayage=["Le système doit envoyer … au smartphone au moins … fois par …",
                           "Le message doit arriver sur le smartphone en moins de … (unité) après …"])],
    aides=["<p>Pour trouver le critère, demande-toi&nbsp;: <b>qu'est-ce que je mesurerais ou compterais</b> pour savoir si c'est "
           "réussi&nbsp;? Une couleur ne se mesure pas pour ces contraintes-là.</p>",
           "<p>Exigence = contrainte + critère + niveau.<br>"
           "« Résister à la pluie » → critère&nbsp;: l'indice de protection → niveau&nbsp;: IPX4 au moins.<br>"
           "« Envoyer l'état au smartphone » → critère&nbsp;: le nombre de messages, ou le temps avant qu'il arrive → niveau&nbsp;: "
           "un nombre avec son unité.<br>"
           "Flexibilité → écoute ce que la gardienne accepte&nbsp;: aucun écart → F0&nbsp;; un écart à une condition → F1&nbsp;; "
           "un petit écart sans condition → F2&nbsp;; tout lui va → F3.</p>"],
    jumeau=dict(consigne="« La pompe ne doit pas gêner les voisins. » Donne un critère et un niveau.",
                correction="Critère&nbsp;: le <b>niveau sonore</b>, en décibels (dB), mesuré à un mètre. Niveau&nbsp;: <b>au plus 35&nbsp;dB</b> "
                           "la nuit. (Autre réponse juste&nbsp;: critère « heures de fonctionnement », niveau « jamais entre 22&nbsp;h et 7&nbsp;h ».)"),
    correction=[
        "<b>« Résister à la pluie et au soleil »</b> → critère&nbsp;: <b>l'indice de protection (IP)</b> → niveau&nbsp;: IPX4 au moins",
        "<b>« Prendre seulement l'eau nécessaire »</b> → critère&nbsp;: <b>le volume d'eau par jour</b> → niveau&nbsp;: par exemple au plus 10&nbsp;L, "
        "fixé dans le cahier des charges du jardin",
        "<b>« Être facile à régler par la gardienne »</b> → critère&nbsp;: <b>le temps pour changer l'heure</b> → niveau&nbsp;: 2&nbsp;min au plus",
        "La couleur du boîtier ne vérifie aucune des trois contraintes.",
        "<b>IPX4</b> → vient d'une <b>norme</b> internationale&nbsp;: elle fixe les codes IP pour tous les fabricants.",
        "<b>12&nbsp;V</b> → « pas question » d'autre chose → aucun écart → <b>F0</b> (le 230&nbsp;V serait un danger mortel au jardin)",
        "<b>IPX4</b> → IPX3 accepté à une seule condition (sous l'abri, preuve à l'appui) → <b>F1</b>",
        "<b>10&nbsp;L par jour</b> → 9 ou 11&nbsp;L acceptés sans condition → <b>F2</b>",
        "<b>Réglage en 2&nbsp;min</b> → même 5&nbsp;min acceptées, sans condition → écart très large → <b>F3</b>",
        "Le piège&nbsp;: croire que la flexibilité dépend de l'importance de la fonction. Elle dépend de ce que le client "
        "<b>accepte</b> comme écart&nbsp;: la gardienne tient beaucoup à ses plantes, et pourtant le volume d'eau est en F2.",
        "<b>Une exigence attendue&nbsp;:</b> « Le système doit envoyer l'état de l'arrosage au smartphone <b>au moins 1 fois par jour</b>. » "
        "ou « …le message doit arriver <b>en moins de 5 minutes</b> après l'arrosage. »",
        ("conclusion", "Exigence = <b>contrainte + critère + niveau</b>, et la <b>flexibilité</b> dit de combien le niveau peut "
                       "bouger (F0 impératif → F3 très négociable). Le niveau vient d'une norme, d'un cahier des charges, d'un "
                       "label ou d'une certification."),
    ],
    retenir="dans le cahier des charges, chaque fonction reçoit un <b>critère</b> (ce qu'on mesure), un <b>niveau</b> (la valeur à "
            "atteindre) et une <b>flexibilité</b> (l'écart accepté), notée de <b>F0</b> (impératif) à <b>F3</b> (très négociable)&nbsp;; "
            "le niveau vient d'une <b>norme</b>, d'un <b>cahier des charges</b>, d'un <b>label</b> ou d'une <b>certification</b>.",
    piege="écrire un niveau sans unité (« au moins 1 »), un critère qui ne se mesure pas (« bien », « joli »), ou choisir la "
          "flexibilité d'après l'importance de la fonction au lieu de l'écart que le client accepte.",
)

E7 = dict(
    id="e7", titre="Ce que le concepteur a oublié", code="4e_C2.2", duree=12,
    objectif="repérer, dans une plainte d'usager, la contrainte qui a été oubliée, et l'expliquer avec le diagramme.",
    production="quatre plaintes rangées dans leur catégorie, et une explication écrite.",
    mots=[("concepteur", "la personne ou l'équipe qui a imaginé et dessiné l'objet."),
          ("fiabilité", "la capacité de l'objet à continuer de fonctionner, sans panne, longtemps."),
          ("incidences environnementales", "les effets de l'objet sur la planète&nbsp;: eau, énergie, déchets…"),
          ("très basse tension", "une tension électrique assez faible pour ne pas être dangereuse au toucher (par exemple 12 volts). "
           "Le 230 volts de la maison, lui, est dangereux.")],
    intro="<p>Un autre système d'arrosage, moins cher, a été installé dans un autre jardin. Voici quatre plaintes "
          "(imaginées pour l'exercice)&nbsp;:</p><ol>"
          "<li>« Après l'orage, l'écran du boîtier s'est éteint pour de bon. »</li>"
          "<li>« Pendant les vacances, la cuve s'est vidée en deux jours et le potager a été noyé. »</li>"
          "<li>« Pour changer l'heure d'arrosage, il faut dévisser le capot avec un tournevis. »</li>"
          "<li>« Le boîtier est branché directement sur le 230 volts, au fond du jardin, sous la pluie. »</li></ol>",
    consigne="<p>Le programme range les contraintes en catégories&nbsp;: <b>sécurité</b>, <b>incidences environnementales</b>, "
             "<b>formes et fonctions</b>, <b>ergonomie</b>, <b>qualité</b>, <b>fiabilité</b>. <b>Range chaque plainte dans la "
             "catégorie de la contrainte oubliée</b>, puis <b>explique</b> la plainte 1 avec le diagramme pieuvre.</p>",
    critere="quatre catégories justes, et une explication qui nomme l'interacteur oublié et la contrainte qui manquait.",
    widgets=[dict(type="classer", name="cat",
                  categories=[("securite", "sécurité"), ("environnement", "incidences environnementales"), ("formes", "formes et fonctions"),
                              ("ergonomie", "ergonomie"), ("qualite", "qualité"), ("fiabilite", "fiabilité")],
                  items=[("Plainte 1 — l'écran s'est éteint après l'orage", "fiabilite", "Plainte 1 : l'objet a cessé de fonctionner. Quelle catégorie parle de tenir dans le temps, sans panne ?"),
                         ("Plainte 2 — la cuve vidée, le potager noyé", "environnement", "Plainte 2 : de l'eau gaspillée. Quelle catégorie parle des effets sur la planète ?"),
                         ("Plainte 3 — un tournevis pour changer l'heure", "ergonomie", "Plainte 3 : l'objet est difficile à utiliser. Quelle catégorie parle de facilité d'usage ?"),
                         ("Plainte 4 — branché sur le 230 volts sous la pluie", "securite", "Plainte 4 : quelqu'un pourrait s'électrocuter.")]),
             dict(type="texte", name="expl", exemple='Le concepteur a oublié la pluie dans le diagramme pieuvre : il manquait la bulle et le trait de la contrainte « résister à la pluie » (étanche, IPX4).', lignes=4,
                  label="Explique la plainte 1 : quel interacteur le concepteur a-t-il oublié, et quelle contrainte aurait-il dû écrire ?",
                  criteres=[dict(label="tu nommes l'interacteur oublié (la pluie, l'orage, la météo)",
                                 motifs=["pluie", "orage", "meteo", r"\beau\b", "intemperie", "averse"],
                                 manque="Nomme l'interacteur oublié : qu'est-ce qui a frappé le boîtier pendant l'orage ?"),
                            dict(label="tu écris la contrainte qui manquait (résister, être étanche…)",
                                 motifs=["resist", "etanch", r"\bip\b", "ipx", "protege", "proteg", "abri", "supporter"],
                                 manque="Écris la contrainte : « le système doit … »."),
                            dict(label="tu relies l'oubli au diagramme (une bulle, un trait, un interacteur)",
                                 motifs=["bulle", "trait", "interacteur", "diagramme", "pieuvre", r"\bfc\b", "oubli"],
                                 manque="Relie ton explication au diagramme : quelle bulle, quel trait manquait ?")],
                  etayage=["Le concepteur a oublié l'interacteur … : il n'a pas tracé le trait vers …",
                           "Il aurait dû écrire la contrainte « le système doit … », avec le niveau …"])],
    aides=["<p>Pour chaque plainte, demande-toi&nbsp;: <b>qui ou quoi</b> a causé le problème — c'est l'interacteur oublié. Puis&nbsp;: "
           "<b>qu'est-ce qui a été abîmé ou gêné</b>&nbsp;? une personne en danger → sécurité&nbsp;; de l'eau perdue → environnement&nbsp;; "
           "un geste pénible → ergonomie&nbsp;; une panne → fiabilité.</p>",
           "<p>Plainte 1 → l'orage → la pluie et le soleil → personne n'a tracé le trait « résister à la pluie » → l'objet tombe en "
           "panne → <b>fiabilité</b>.<br>Plainte 4 → le 230 volts sous la pluie → danger de mort → <b>sécurité</b>&nbsp;: un tel "
           "système doit fonctionner en <b>très basse tension</b>.</p>"],
    jumeau=dict(consigne="« Les lettres de l'écran sont si petites que la gardienne ne peut pas les lire sans lunettes. » "
                         "Quelle catégorie&nbsp;? Quel interacteur&nbsp;?",
                correction="L'interacteur est <b>la gardienne</b> (un usager)&nbsp;; la contrainte oubliée est « être lisible facilement » → "
                           "catégorie <b>ergonomie</b>. Critère possible&nbsp;: hauteur des lettres&nbsp;; niveau&nbsp;: au moins 5&nbsp;mm."),
    correction=[
        "<b>Plainte 1</b> → la pluie de l'orage → contrainte oubliée&nbsp;: résister à la pluie (IPX4 au moins) → <b>fiabilité</b>",
        "<b>Plainte 2</b> → la cuve et les plantes → contrainte oubliée&nbsp;: ne prendre que l'eau nécessaire → <b>incidences environnementales</b>",
        "<b>Plainte 3</b> → la gardienne → contrainte oubliée&nbsp;: se régler sans outil → <b>ergonomie</b>",
        "<b>Plainte 4</b> → toute personne qui touche le boîtier → contrainte oubliée&nbsp;: fonctionner en très basse tension → <b>sécurité</b>",
        "<b>Une explication attendue pour la plainte 1&nbsp;:</b> « Le concepteur a oublié <b>la pluie</b> dans son diagramme pieuvre&nbsp;: "
        "il n'a pas tracé de <b>fonction contrainte</b> vers elle. Il aurait dû écrire « le système doit <b>résister à la pluie</b> », "
        "avec le niveau IPX4 au moins. »",
        ("conclusion", "Un interacteur oublié dans le diagramme, c'est une contrainte que personne n'écrira — et une plainte plus tard."),
    ],
    retenir="le diagramme pieuvre sert à <b>ne rien oublier</b>&nbsp;: chaque interacteur pose la question « quelle contrainte "
            "nous impose-t-il&nbsp;? ».",
    piege="ranger la plainte 1 en « qualité » parce que l'objet est « de mauvaise qualité »&nbsp;: la panne qui arrive avec le temps "
          "relève de la <b>fiabilité</b>.",
)

# ─────────────────────────────────────────────────────────────────────────────
# Les deux niveaux
# ─────────────────────────────────────────────────────────────────────────────
NIVEAUX = {
    "5e": dict(
        codes=["5e_C2.1", "5e_C2.2"],
        mission="Dessiner tout ce qui entoure un objet, puis voir que chacune de ses formes répond à l'un d'eux.",
        avant=[("Je sais dire si un élément est une pièce d'un objet, ou s'il est en dehors de lui.",
                "cycle 3 — sciences et technologie", "@synthese#les-mots", "les mots de l'atelier, dans la synthèse (2 minutes)"),
               ("Je sais distinguer un objet, que l'on peut toucher, d'une information, que l'on peut seulement lire ou entendre.",
                "cycle 3 — sciences et technologie", "@synthese#les-mots", "les mots de l'atelier, dans la synthèse (2 minutes)")],
        situation_titre="Deux noms pour un même schéma",
        situation="<p>Pour décrire un objet, on commence souvent par regarder <b>ce qui l'entoure</b>&nbsp;: les personnes qui s'en "
                  "servent, les choses qui le touchent, les informations qu'il échange, la météo et le lieu. Le schéma qui "
                  "rassemble tout cela s'appelle, dans le programme de technologie, le <b>diagramme des interacteurs extérieurs</b>. "
                  "Beaucoup de livres et de professeurs l'appellent aussi le <b>diagramme pieuvre</b>&nbsp;: l'objet au centre, et "
                  "autour, comme des tentacules, tout ce qui est en relation avec lui.</p>"
                  "<p>Dans cet atelier, l'objet est un <b>vélo-cargo</b>&nbsp;: un vélo avec un grand bac devant, pour transporter "
                  "des enfants ou des courses.</p>",
        question="Comment montrer, d'un seul coup d'œil, tout ce qui entoure un objet et agit sur lui — sans rien oublier&nbsp;?",
        hypothese_amorces=["Je pense qu'on pourrait dessiner l'objet… et autour…", "Pour ne rien oublier, je regarderais…",
                           "Je crois qu'il faut séparer les personnes et…"],
        exercices=[E1, E2, E3, E4],
        a_retenir="<ul><li>Le <b>diagramme des interacteurs extérieurs</b> — le <b>diagramme pieuvre</b> — met l'objet au centre "
                  "et relie à lui, par un trait, tout ce qui est en relation avec lui.</li>"
                  "<li>Un interacteur est toujours <b>en dehors</b> de l'objet. Il appartient à l'une des quatre familles&nbsp;: "
                  "<b>usagers, données, autres objets, éléments de l'environnement</b>.</li>"
                  "<li>Une <b>fonction principale</b> (FP) relie deux éléments extérieurs en passant par l'objet&nbsp;: c'est le "
                  "service rendu. Une <b>fonction contrainte</b> (FC) relie l'objet à un seul élément&nbsp;: c'est ce qu'il doit "
                  "respecter.</li>"
                  "<li>Un choix de conception s'explique par l'interacteur qu'il sert et par son domaine&nbsp;: <b>sécurité, "
                  "ergonomie, développement durable</b>.</li></ul>",
        bonus=[dict(titre="Le vélo-cargo à la plage",
                    consigne="<p>Léa part sur la route du bord de mer, entre le sable et l'air salé. Cite <b>deux nouveaux "
                             "interacteurs</b>, leur famille, et <b>un choix de conception</b> qu'ils pourraient expliquer.</p>",
                    correction=["<b>Le sable</b> → un élément de l'environnement → des pneus plus larges, qui s'enfoncent moins",
                                "<b>L'air salé</b> (le sel de la mer) → un élément de l'environnement → des pièces traitées contre "
                                "la rouille, qui durent plus longtemps → développement durable",
                                "<b>Le soleil fort</b> → un élément de l'environnement → une selle et un bac qui ne chauffent pas trop",
                                ("conclusion", "Changer de lieu, c'est changer d'interacteurs — donc de choix de conception.")]),
               dict(titre="La trottinette en quatre familles",
                    consigne="<p>Écris <b>quatre</b> interacteurs extérieurs d'une trottinette électrique, <b>un par famille</b>.</p>",
                    correction=["<b>Un usager</b> → la personne qui roule",
                                "<b>Une donnée</b> → la vitesse ou le niveau de la batterie affichés sur l'écran",
                                "<b>Un autre objet</b> → le chargeur, un casque, une voiture",
                                "<b>Un élément de l'environnement</b> → le trottoir, la pluie, la pente",
                                ("conclusion", "Le guidon, les roues et la batterie sont des pièces de la trottinette&nbsp;: pas des interacteurs.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre un objet et une donnée, ou entre une pièce et un interacteur. "
                      "Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
    "4e": dict(
        codes=["4e_C2.2"],
        mission="Passer du dessin des interacteurs à des contraintes écrites, que l'on peut vérifier.",
        avant=[("Je sais faire la liste des interacteurs extérieurs d'un objet et les ranger en quatre familles.",
                "5e_C2.1", "@niveau:5e#pv_5e_e1", "l'atelier de 5e, exercices 1 à 3 (20 minutes)"),
               ("Je sais expliquer un choix de conception par l'interacteur qu'il sert (sécurité, ergonomie, développement durable).",
                "5e_C2.2", "@niveau:5e#pv_5e_e4", "l'atelier de 5e, exercice 4 (12 minutes)")],
        situation_titre="Deux noms pour un même schéma",
        situation="<p>Le schéma qui place un objet au centre et, autour, tout ce qui est en relation avec lui s'appelle, dans le "
                  "programme de technologie, le <b>diagramme des interacteurs extérieurs</b>. On l'appelle aussi le "
                  "<b>diagramme pieuvre</b>. En 4e, on s'en sert pour <b>trouver les contraintes</b>&nbsp;: chaque interacteur "
                  "impose à l'objet une condition à respecter.</p>"
                  "<p>Dans cet atelier, l'objet est le <b>système d'arrosage connecté</b> du jardin partagé du collège.</p>",
        question="Comment passer du dessin des interacteurs à une liste de contraintes que l'on peut vérifier&nbsp;?",
        hypothese_amorces=["Je pense que chaque interacteur…", "Pour vérifier une contrainte, il faudrait…",
                           "Une contrainte bien écrite contient…"],
        exercices=[E5, E6, E7],
        a_retenir="<ul><li>La <b>fonction principale</b> (FP) relie deux interacteurs en passant par l'objet&nbsp;: c'est le service "
                  "rendu. Une <b>fonction contrainte</b> (FC) relie l'objet à un seul interacteur&nbsp;: c'est une condition.</li>"
                  "<li>Une contrainte devient une <b>exigence</b> vérifiable avec un <b>critère</b> (ce qu'on mesure) et un "
                  "<b>niveau</b> (la valeur à atteindre).</li>"
                  "<li>Le <b>cahier des charges fonctionnel</b> range les fonctions dans un tableau&nbsp;: fonction, désignation, "
                  "critère, niveau, <b>flexibilité</b>. La flexibilité dit l'écart accepté autour du niveau&nbsp;: <b>F0</b> "
                  "impératif, <b>F1</b> peu négociable, <b>F2</b> négociable, <b>F3</b> très négociable.</li>"
                  "<li>Le niveau vient d'une <b>norme</b>, d'un <b>cahier des charges</b>, d'un <b>label</b> ou d'une "
                  "<b>certification</b>. Un interacteur oublié, c'est une contrainte que personne n'écrira.</li></ul>",
        bonus=[dict(titre="La pompe qui réveille la voisine",
                    consigne="<p>La nuit, la pompe du système fait du bruit et réveille la voisine. Ajoute un interacteur au "
                             "diagramme, écris la contrainte, puis l'exigence avec un critère et un niveau.</p>",
                    correction=["<b>Interacteur</b> → la voisine, une personne de l'environnement du jardin",
                                "<b>Contrainte</b> → une fonction contrainte, verbe à l'infinitif&nbsp;: « ne pas gêner la voisine par son bruit »",
                                "<b>Critère</b> → le niveau sonore, en décibels (dB), mesuré à un mètre de la pompe",
                                "<b>Niveau</b> → au plus 35&nbsp;dB la nuit (ou&nbsp;: aucun arrosage entre 22&nbsp;h et 7&nbsp;h)",
                                ("conclusion", "Une personne qui n'utilise pas l'objet peut quand même lui imposer une contrainte.")]),
               dict(titre="Lire un emballage",
                    consigne="<p>Sur l'emballage d'un appareil de jardin ou d'une lampe d'extérieur, on trouve souvent un code "
                             "comme <b>IP44</b> ou <b>IPX4</b>. Explique ce que garantit le second chiffre, et pourquoi ce code est "
                             "le même chez tous les fabricants.</p>",
                    correction=["<b>Le second chiffre</b> → la résistance à l'eau (4&nbsp;: projections d'eau de tous côtés)",
                                "<b>Le premier chiffre</b> → la résistance à la poussière et aux objets (X&nbsp;: non testé)",
                                "<b>Le même partout</b> → parce que ces codes sont fixés par une <b>norme</b> internationale",
                                ("conclusion", "Une norme permet de comparer deux appareils sans les ouvrir.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre FP et FC, ou entre un critère et un niveau. Qu'est-ce que tu dois "
                      "encore revoir, et comment&nbsp;?",
    ),
}

# ─────────────────────────────────────────────────────────────────────────────
# Ce que le reste du site lit de cet atelier
# ─────────────────────────────────────────────────────────────────────────────
MODULE = "interacteurs"
NOM_PANNEAU = "diagramme_pieuvre"
PANNEAU_TEXTE = {
    "5e": "Le <b>diagramme des interacteurs extérieurs</b> — souvent appelé <b>diagramme pieuvre</b> — sur un vélo-cargo&nbsp;: "
          "tu listes ce qui l'entoure, tu le ranges en quatre familles, tu complètes le schéma, puis tu relies trois de ses "
          "formes à l'interacteur qu'elles servent.",
    "4e": "Le <b>diagramme des interacteurs extérieurs</b> — souvent appelé <b>diagramme pieuvre</b> — sur le système "
          "d'arrosage du jardin&nbsp;: tu distingues le service rendu des contraintes, tu écris des contraintes qu'on peut "
          "vérifier, puis tu retrouves celles qu'un concepteur a oubliées.",
}
IMAGES = {
    "velo_cargo_la_scene.svg": SCENE,
    "velo_cargo_trois_choix.svg": SCENE_REPERES,
    "pieuvre_velo_cargo_a_completer.svg": PIEUVRE_A_COMPLETER,
    "pieuvre_velo_cargo_corrige.svg": PIEUVRE_CORRIGE,
    "pieuvre_jardin_arrosage.svg": PIEUVRE_JARDIN,
}
SCHEMAS_SYNTHESE = {"5e": PIEUVRE_CORRIGE, "4e": PIEUVRE_JARDIN}

COURS = {
    "5e": (
        "<h3>À quoi sert ce diagramme</h3>"
        "<ul><li>Le <b>diagramme des interacteurs extérieurs</b> — le <b>diagramme pieuvre</b> — décrit un objet <b>de "
        "l'extérieur</b>, pendant qu'il sert&nbsp;: l'objet au centre, dans une <b>ellipse</b>, et autour, une ellipse (une "
        "«&nbsp;bulle&nbsp;») pour chaque interacteur.</li>"
        "<li>Un <b>interacteur extérieur</b> remplit deux conditions à la fois&nbsp;: il est <b>en dehors</b> de l'objet, et il "
        "est <b>en relation</b> avec lui (il le touche, agit sur lui, ou subit son action).</li></ul>"
        "<h3>Les quatre familles d'interacteurs</h3>"
        "<ul><li><b>Les usagers</b>&nbsp;: les personnes qui se servent de l'objet ou que l'objet sert (Léa, ses enfants).</li>"
        "<li><b>Les données</b>&nbsp;: les informations, qu'on lit ou qu'on mesure sans pouvoir les toucher (l'itinéraire).</li>"
        "<li><b>Les autres objets</b>&nbsp;: les choses qu'on touche et qui ne sont pas des pièces de l'objet (le téléphone, les courses).</li>"
        "<li><b>Les éléments de l'environnement</b>&nbsp;: le lieu, la nature, la météo (la route, la pluie, le soleil).</li></ul>"
        "<h3>Ce qui n'a pas de bulle</h3>"
        "<ul><li>Une <b>pièce de l'objet</b> (la chaîne, la pédale)&nbsp;: elle est dedans.</li>"
        "<li>Une <b>caractéristique de l'objet</b> (sa masse, sa couleur, sa beauté)&nbsp;: elle décrit l'objet, elle n'est pas autour de lui.</li>"
        "<li>Une <b>règle</b>, une loi, une norme&nbsp;: elle ne touche pas l'objet&nbsp;; elle s'impose à ceux qui le conçoivent. "
        "C'est une <b>exigence</b>.</li></ul>"
        "<h3>Les traits sont des fonctions</h3>"
        "<ul><li>La <b>fonction principale</b> (FP)&nbsp;: une courbe qui part d'un interacteur, <b>passe par l'objet</b> — on la "
        "voit entrer dans son ellipse — et arrive à un autre interacteur. C'est le <b>service rendu</b>&nbsp;: «&nbsp;permettre à "
        "Léa de transporter ses enfants&nbsp;».</li>"
        "<li>La <b>fonction contrainte</b> (FC) — on dit aussi fonction complémentaire&nbsp;: un trait droit entre l'objet et "
        "<b>un seul</b> interacteur. C'est ce que l'objet <b>doit respecter</b>&nbsp;: «&nbsp;résister à la pluie&nbsp;».</li>"
        "<li>Chaque fonction, FP ou FC, commence par un <b>verbe à l'infinitif</b> (permettre, résister, protéger…), et se "
        "numérote&nbsp;: FP1, FP2… FC1, FC2…</li>"
        "<li>Un même interacteur peut avoir plusieurs traits&nbsp;: Léa est dans FP1 et dans FP2. Il peut aussi porter "
        "<b>une FP et une FC</b>&nbsp;: les enfants sont au bout de la FP1, et la FC1 les relie aussi au vélo-cargo.</li></ul>"
        "<h3>La fonction principale, c'est la bête à cornes dans le diagramme</h3>"
        "<ul><li>La FP1 part de l'élément «&nbsp;<b>à qui</b> l'objet rend-il service&nbsp;?&nbsp;» (Léa), passe par l'objet, et "
        "arrive à l'élément «&nbsp;<b>sur quoi</b> agit-il&nbsp;?&nbsp;» (ses enfants).</li>"
        "<li>Sa phrase dit «&nbsp;<b>dans quel but</b>&nbsp;?&nbsp;»&nbsp;: «&nbsp;permettre à Léa de transporter ses enfants&nbsp;». "
        "La FP1 décrit donc la <b>fonction d'usage</b> de l'objet.</li>"
        "<li>Très souvent, l'élément au bout de la FP1 impose <b>aussi</b> une contrainte, qu'on numérote FC1&nbsp;: les enfants "
        "demandent d'être protégés pendant le trajet. C'est fréquent, ce n'est pas une règle.</li></ul>"
        '<figure class="figure">' + BETE_VERS_PIEUVRE + '<figcaption>La même liaison, deux fois&nbsp;: la corne de la bête à '
        'cornes devient la fonction principale FP1. Les repères ①②③ se répondent d\'un schéma à l\'autre.</figcaption></figure>' 
        "<h3>Construire le diagramme, pas à pas</h3>"
        "<ol><li>Imaginer l'objet en train de servir, du départ à l'arrivée.</li>"
        "<li>Faire la liste de ce qui l'entoure, famille par famille&nbsp;: une liste de personnes seulement est à moitié faite.</li>"
        "<li>Écarter les pièces, les caractéristiques et les règles.</li>"
        "<li>Tracer la ou les fonctions principales (la bête à cornes les donne), puis une fonction contrainte par condition "
        "à respecter, en commençant par l'élément au bout de la FP1.</li></ol>"
    ),
    "4e": (
        "<h3>Du diagramme pieuvre aux contraintes</h3>"
        "<ul><li>La <b>fonction principale</b> (FP) relie deux interacteurs <b>en passant par l'objet</b>&nbsp;: c'est le service rendu.</li>"
        "<li>Chaque <b>fonction contrainte</b> (FC) relie l'objet à <b>un seul</b> interacteur&nbsp;: c'est une condition à respecter. "
        "Devant chaque bulle, on se demande&nbsp;: «&nbsp;quelle condition cet interacteur impose-t-il à l'objet&nbsp;?&nbsp;»</li>"
        "<li>Chaque fonction commence par un <b>verbe à l'infinitif</b>&nbsp;: «&nbsp;permettre à la gardienne d'arroser…&nbsp;», "
        "«&nbsp;résister à la pluie…&nbsp;» — et non «&nbsp;le système doit…&nbsp;», qui est la forme d'une <b>exigence</b>.</li>"
        "<li>Un même interacteur peut imposer plusieurs contraintes, et porter <b>à la fois la FP et une FC</b>&nbsp;: la "
        "gardienne reçoit le service (FP1) et impose une condition (FC4&nbsp;: être facile à régler par elle). Un interacteur "
        "oublié, c'est une contrainte que personne n'écrira.</li></ul>"
        "<h3>Le cahier des charges fonctionnel</h3>"
        "<ul><li>Le <b>cahier des charges fonctionnel</b> (CdCF) met par écrit ce que le client attend de l'objet, <b>avant</b> de "
        "chercher des solutions. Il rassemble l'expression du besoin, le diagramme pieuvre et le tableau des fonctions.</li>"
        "<li>Le tableau a cinq colonnes&nbsp;: <b>Fonction</b> (FP1, FC1…) · <b>Désignation</b> (la phrase, verbe à l'infinitif) · "
        "<b>Critère</b> · <b>Niveau</b> · <b>Flexibilité</b>.</li></ul>"
        "<h3>Critère, niveau, flexibilité</h3>"
        "<ul><li>Le <b>critère</b> est ce que l'on observe ou mesure pour savoir si la fonction est remplie&nbsp;: un volume d'eau, "
        "une durée, un indice de protection. Il a souvent une <b>unité</b>.</li>"
        "<li>Le <b>niveau</b> est la valeur à atteindre&nbsp;: «&nbsp;10&nbsp;L par jour&nbsp;», «&nbsp;IPX4 au moins&nbsp;», "
        "«&nbsp;en moins de 2&nbsp;min&nbsp;». Il peut aussi être une qualité&nbsp;: «&nbsp;couleur&nbsp;: vert&nbsp;».</li>"
        "<li>La <b>flexibilité</b> dit l'écart que le client accepte autour du niveau. Elle s'écrit soit comme une marge chiffrée "
        "(«&nbsp;± 1&nbsp;L&nbsp;», «&nbsp;au plus&nbsp;», «&nbsp;au moins&nbsp;»), soit par une classe&nbsp;:</li></ul>"
        '<div class="defile"><table><tr><th>Classe</th><th>Flexibilité</th><th>Le niveau est…</th><th>Ce que dit le client</th></tr>'
        "<tr><td>F0</td><td>nulle</td><td>impératif</td><td>«&nbsp;Pas question d'autre chose.&nbsp;»</td></tr>"
        "<tr><td>F1</td><td>faible</td><td>peu négociable</td><td>«&nbsp;À la rigueur, mais seulement si…&nbsp;»</td></tr>"
        "<tr><td>F2</td><td>moyenne</td><td>négociable</td><td>«&nbsp;Un peu plus ou un peu moins, ça ira.&nbsp;»</td></tr>"
        "<tr><td>F3</td><td>forte</td><td>très négociable</td><td>«&nbsp;N'importe quelle valeur me va.&nbsp;»</td></tr></table></div>"
        "<h3>D'où vient le niveau</h3>"
        "<ul><li>D'une <b>norme</b> (un texte officiel, le même pour tous les fabricants&nbsp;: les codes IP), d'un <b>label</b> (une "
        "qualité garantie&nbsp;: l'économie d'eau), d'une <b>certification</b>, ou de la demande du client écrite dans le cahier des charges.</li></ul>"
        "<h3>Les erreurs à éviter</h3>"
        "<ul><li>Écrire une <b>solution</b> à la place d'un critère&nbsp;: «&nbsp;une électrovanne&nbsp;» n'est pas un critère, "
        "«&nbsp;le volume d'eau par jour&nbsp;» en est un.</li>"
        "<li>Écrire un niveau <b>sans unité</b>, ou un critère qui ne se mesure pas («&nbsp;bien&nbsp;», «&nbsp;joli&nbsp;»).</li>"
        "<li>Choisir la flexibilité d'après l'<b>importance</b> de la fonction&nbsp;: elle dépend de l'<b>écart accepté</b> par le client.</li>"
        "<li>Mettre une norme dans une bulle du diagramme&nbsp;: c'est une exigence, qui fixe un niveau.</li></ul>"
    ),
}

VOCAB_EN = [("interacteur", "interactor (external element)"), ("usager", "user"), ("donnée", "data"),
            ("environnement", "environment"), ("contrainte", "constraint"), ("exigence", "requirement"),
            ("critère", "criterion"), ("niveau", "level"), ("norme", "standard"), ("cahier des charges", "specifications")]
VERBES = {"5e": "<b>lister, classer, compléter</b> le diagramme et <b>lire</b> ses fonctions (FP, FC), puis <b>expliquer</b> un "
                "choix de conception par un interacteur",
          "4e": "<b>distinguer</b> service rendu et contraintes, puis <b>formuler</b> une contrainte avec critère et niveau",
          "3e": "pas d'exercice de ce diagramme&nbsp;: en 3e, le programme demande de <b>choisir</b> ses modes de représentation "
                "pour décrire l'expérience de l'utilisateur (3e_C2.1). Le diagramme pieuvre y est un choix possible, parmi d'autres."}
CHAINE = ("<p><b>Analyse externe</b>&nbsp;: besoin <i>(bête à cornes)</i> → fonction d'usage → <b>interacteurs <i>(diagramme "
          "des interacteurs, « pieuvre »)</i></b> → contraintes et exigences → cahier des charges.</p>"
          "<p>Cet atelier est le deuxième maillon. Il <b>suit</b> la formulation du besoin et <b>précède</b> le tableau des "
          "contraintes et exigences (4e_C2.1, Hangzhou) et le diagramme des exigences.</p>")
NOTES_PROF = ("<ul><li>Le cours (encadré « 📘 Le cours ») et deux mécaniques — écarter les fausses bulles (exercice 2), "
              "le tableau du cahier des charges avec la flexibilité (exercice 6) — s'inspirent du cahier « 123 Techno » "
              "(Bordas 2021) utilisé par Pascal, sans rien en reprendre&nbsp;: objets, mots et schémas sont ceux du site. "
              "Écarts assumés avec ce cahier&nbsp;: aucune caractéristique (masse, esthétique) ni « législation » en bulle&nbsp;; "
              "FC lue « fonction contrainte » (on signale « fonction complémentaire »)&nbsp;; classes F0–F3 définies et travaillées.</li>"
              "<li>Choix de Pascal (13/10/2026)&nbsp;: le diagramme pieuvre en 5e_C2.1, 5e_C2.2 et 4e_C2.2 seulement.</li>"
              "<li>Demande de Pascal (24/10/2026)&nbsp;: le diagramme montre ses fonctions dès la 5e — la fonction principale (FP) "
              "passe par l'objet entre deux éléments, chaque fonction contrainte (FC) relie l'objet à un seul élément — et le cahier "
              "des charges de 4e porte la flexibilité, par classes F0 à F3. En 5e, l'élève LIT et complète les fonctions&nbsp;; "
              "en 4e, il les FORMULE avec critère, niveau et flexibilité.</li>"
              "<li>Le programme ne nomme ni « pieuvre » ni « fonction contrainte »&nbsp;: il dit <i>interacteurs, contraintes, "
              "exigences, cahier des charges</i>. Le diagramme est donc toujours nommé deux fois&nbsp;: d'abord par le mot du "
              "programme, puis par son nom courant.</li>"
              "<li>Les quatre familles d'interacteurs sont celles du programme, mot pour mot&nbsp;: usagers, données, autres objets, "
              "éléments de l'environnement. Une norme ou une règle de la ville n'est pas un interacteur&nbsp;: c'est une exigence.</li>"
              "<li>En 4e, l'élève n'a pas forcément fait l'atelier de 5e&nbsp;: l'ouverture renvoie aux exercices de 5e pour "
              "rattraper en vingt minutes.</li></ul>")
DEUX_NOMS = ("Dans le programme de technologie, ce schéma s'appelle le <b>diagramme des interacteurs extérieurs</b>. Dans "
             "beaucoup de livres et de classes, on l'appelle aussi le <b>diagramme pieuvre</b>&nbsp;: l'objet est la tête, les "
             "traits vers ses interacteurs sont les tentacules. Si tu rencontres l'un des deux noms, tu sauras que c'est le même "
             "schéma.")
ETIQUETTE_COURTE = "Interacteurs"
QCM_SOUS_TITRE = ("Lister et classer les interacteurs extérieurs, compléter le diagramme pieuvre, expliquer un choix de "
                  "conception (5e) ; distinguer service rendu et contraintes, écrire une exigence avec critère et niveau (4e)")
