# -*- coding: utf-8 -*-
"""Atelier — Le diagramme de cas d'utilisation (use case SysML).

Codes servis : 5e_C2.1, 4e_C2.1, 3e_C2.1 (plan du 24/10/2026).
Objets : la station de vélos en libre-service et le lampadaire solaire (5e) ; la borne de la
station et le système d'arrosage du jardin connecté (4e) ; la borne, puis la station d'alerte
cyclonique de Sainte-Luce (3e).

Le verbe change d'un niveau à l'autre, pas la notion :
  5e  RECONNAÎTRE les acteurs parmi les interacteurs, LIRE le diagramme, FAIRE LA LISTE de ses acteurs ;
  4e  PASSER du langage naturel (verbatims) au schéma, COMPLÉTER, REPÉRER ET CORRIGER les erreurs ;
  3e  CHOISIR le mode de représentation selon la question, puis CONSTRUIRE le diagramme d'après un texte.
"""
import figures

SLUG = "cas-utilisation-sysml"
COURT = "cu"
EMOJI = "🧍"
TITRE = "Le diagramme de cas d'utilisation"
TITRE_COURT = "le diagramme de cas d'utilisation (use case)"
TITRE_COMPLET = ("Le diagramme de cas d'utilisation, souvent appelé use case SysML "
                 "(SysML : Systems Modeling Language, le langage de modélisation des systèmes)")
ETIQUETTE = "🧍 use case"
ETIQUETTE_COURTE = "Cas d'utilisation"
MENTION_FICTION = ("Situations imaginées pour les exercices : la station de vélos du front de mer de Sainte-Luce, sa borne, "
                   "les phrases de ses usagers et leurs prénoms, le lampadaire du parking, le diagramme de Noah et la station "
                   "d'alerte cyclonique sont inventés.")

# ─────────────────────────────────────────────────────────────────────────────
# Les dessins (tous écrits par figures.cas_utilisation : la version à compléter et
# la version corrigée sont le même dessin, case pour case)
# ─────────────────────────────────────────────────────────────────────────────
STATION_CAS = [("louer", "Louer un vélo"), ("rendre", "Rendre un vélo"), ("payer", "Payer la location"),
               ("reparer", "Réparer une borne")]
STATION_LIENS = [("usager", "louer"), ("usager", "rendre"), ("usager", "payer"), ("banque", "payer"), ("tech", "reparer")]

FIG_STATION = figures.cas_utilisation(
    "cu-station", "Station de vélos en libre-service",
    acteurs=[("usager", "", "g"), ("tech", "", "g"), ("banque", "", "d")],
    cas=STATION_CAS, liens=STATION_LIENS,
    titre="Diagramme de cas d'utilisation de la station de vélos, trois acteurs à placer",
    desc="Un grand cadre nommé Station de vélos en libre-service. Dedans, quatre ellipses, de haut en bas : Louer un "
         "vélo, Rendre un vélo, Payer la location, Réparer une borne. Hors du cadre, trois bonshommes sans nom. Le "
         "bonhomme du haut, à gauche, est relié par un trait à Louer un vélo, Rendre un vélo et Payer la location. Le "
         "bonhomme du bas, à gauche, est relié à Réparer une borne. Le bonhomme de droite est relié à Payer la location.",
    hauteur=500, vivants={"usager": "cu-a1", "tech": "cu-a2", "banque": "cu-a3"})

FIG_STATION_C = figures.cas_utilisation(
    "cu-station-c", "Station de vélos en libre-service",
    acteurs=[("usager", "l'usager", "g"), ("tech", "le technicien de maintenance", "g"),
             ("banque", "le serveur de paiement", "d")],
    cas=STATION_CAS, liens=STATION_LIENS,
    titre="Diagramme de cas d'utilisation de la station de vélos, corrigé",
    desc="Le cadre Station de vélos en libre-service et ses quatre ellipses. À gauche, en haut, l'usager, relié à Louer "
         "un vélo, Rendre un vélo et Payer la location. À gauche, en bas, le technicien de maintenance, relié à Réparer "
         "une borne. À droite, le serveur de paiement, relié à Payer la location. Ni la pluie ni le vélo n'ont de bonhomme.",
    hauteur=500)

FIG_LAMPADAIRE = figures.cas_utilisation(
    "cu-lampadaire", "Lampadaire solaire du parking",
    acteurs=[("pieton", "le piéton", "g"), ("agent", "l'agent de la mairie", "d"), ("tech", "le technicien", "d")],
    cas=[("voir", "Voir son chemin la nuit"), ("regler", "Régler les heures d'allumage"),
         ("charge", "Suivre la charge de la batterie"), ("lampe", "Remplacer la lampe")],
    liens=[("pieton", "voir"), ("agent", "regler"), ("agent", "charge"), ("tech", "charge"), ("tech", "lampe")],
    titre="Diagramme de cas d'utilisation du lampadaire solaire du parking",
    desc="Un grand cadre nommé Lampadaire solaire du parking. Dedans, quatre ellipses, de haut en bas : Voir son chemin "
         "la nuit, Régler les heures d'allumage, Suivre la charge de la batterie, Remplacer la lampe. À gauche, hors du "
         "cadre, le piéton, relié à Voir son chemin la nuit. À droite, en haut, l'agent de la mairie, relié à Régler les "
         "heures d'allumage et à Suivre la charge de la batterie. À droite, en bas, le technicien, relié à Suivre la "
         "charge de la batterie et à Remplacer la lampe.",
    hauteur=500)

BORNE_ACTEURS = [("usager", "l'usager", "g"), ("tech", "le technicien", "g")]
BORNE_LIENS = [("usager", "louer"), ("usager", "c1"), ("usager", "payer"), ("usager", "c2"), ("tech", "c2"),
               ("tech", "reparer"), ("banque", "payer")]

FIG_BORNE = figures.cas_utilisation(
    "cu-borne", "Borne de la station de vélos",
    acteurs=BORNE_ACTEURS + [("banque", "", "d")],
    cas=[("louer", "Louer un vélo"), ("c1", ""), ("payer", "Payer la location"), ("c2", ""), ("reparer", "Réparer la borne")],
    liens=BORNE_LIENS,
    titre="Diagramme de cas d'utilisation de la borne, deux ellipses et un acteur à compléter",
    desc="Un grand cadre nommé Borne de la station de vélos. Dedans, cinq ellipses, de haut en bas : Louer un vélo ; une "
         "ellipse vide ; Payer la location ; une seconde ellipse vide ; Réparer la borne. À gauche, en haut, l'usager, "
         "relié à Louer un vélo, à la première ellipse vide, à Payer la location et à la seconde ellipse vide. À gauche, "
         "en bas, le technicien, relié à la seconde ellipse vide et à Réparer la borne. À droite, un bonhomme sans nom, "
         "relié à Payer la location.",
    vivants={"c1": "cu-c1", "c2": "cu-c2", "banque": "cu-a4"})

FIG_BORNE_C = figures.cas_utilisation(
    "cu-borne-c", "Borne de la station de vélos",
    acteurs=BORNE_ACTEURS + [("banque", "le serveur de paiement", "d")],
    cas=[("louer", "Louer un vélo"), ("c1", "Rendre un vélo"), ("payer", "Payer la location"), ("c2", "Signaler une panne"),
         ("reparer", "Réparer la borne")],
    liens=BORNE_LIENS,
    titre="Diagramme de cas d'utilisation de la borne, corrigé",
    desc="Le cadre Borne de la station de vélos. Cinq ellipses, de haut en bas : Louer un vélo, Rendre un vélo, Payer la "
         "location, Signaler une panne, Réparer la borne. L'usager, à gauche en haut, est relié aux quatre premières. Le "
         "technicien, à gauche en bas, est relié à Signaler une panne et à Réparer la borne. Le serveur de paiement, à "
         "droite, est relié à Payer la location.")

FIG_ERREURS = figures.cas_utilisation(
    "cu-erreurs", "Système d'arrosage du jardin",
    acteurs=[("gardienne", "la gardienne", "g"), ("pluie", "la pluie", "d"), ("tech", "le technicien", "d")],
    cas=[("prog", "Programmer l'heure d'arrosage"), ("pompe", "La pompe"), ("arrosage", "L'arrosage"),
         ("cuve", "Consulter le niveau de la cuve")],
    liens=[("gardienne", "prog"), ("gardienne", "pompe"), ("gardienne", "cuve"), ("pluie", "arrosage")],
    titre="Le diagramme de cas d'utilisation du système d'arrosage dessiné par Noah, avec des erreurs",
    desc="Un grand cadre nommé Système d'arrosage du jardin. Dedans, quatre ellipses, de haut en bas : Programmer l'heure "
         "d'arrosage, La pompe, L'arrosage, Consulter le niveau de la cuve. Un bonhomme, la gardienne, est dessiné à "
         "l'intérieur du cadre, à gauche des ellipses ; il est relié à Programmer l'heure d'arrosage, à La pompe et à "
         "Consulter le niveau de la cuve. À droite, hors du cadre, deux bonshommes : la pluie, reliée à L'arrosage, et le "
         "technicien, relié à aucune ellipse.",
    largeur=1000, hauteur=520, acteurs_dans=["gardienne"])

CYCLONE_LIENS = [("agent", "declencher"), ("habitant", "recevoir"), ("tech", "tester"), ("meteo", "bulletin")]

FIG_CYCLONE = figures.cas_utilisation(
    "cu-cyclone", "Station d'alerte cyclonique",
    acteurs=[("agent", "", "g"), ("tech", "le technicien", "g"), ("habitant", "", "d"), ("meteo", "", "d")],
    cas=[("declencher", ""), ("recevoir", "Recevoir une alerte"), ("tester", ""), ("bulletin", "Envoyer un bulletin météo")],
    liens=CYCLONE_LIENS,
    titre="Diagramme de cas d'utilisation de la station d'alerte cyclonique, à construire",
    desc="Un grand cadre nommé Station d'alerte cyclonique. Dedans, quatre ellipses, de haut en bas : une ellipse vide ; "
         "Recevoir une alerte ; une seconde ellipse vide ; Envoyer un bulletin météo. À gauche, en haut, un bonhomme "
         "sans nom, relié à la première ellipse vide. À gauche, en bas, le technicien, relié à la seconde ellipse vide. À "
         "droite, en haut, un bonhomme sans nom, relié à Recevoir une alerte. À droite, en bas, un bonhomme sans nom, "
         "relié à Envoyer un bulletin météo.",
    hauteur=500, vivants={"agent": "cu-a5", "habitant": "cu-a6", "meteo": "cu-a7", "declencher": "cu-c3", "tester": "cu-c4"})

FIG_CYCLONE_C = figures.cas_utilisation(
    "cu-cyclone-c", "Station d'alerte cyclonique",
    acteurs=[("agent", "l'agent municipal", "g"), ("tech", "le technicien", "g"), ("habitant", "l'habitant", "d"),
             ("meteo", "le service météo", "d")],
    cas=[("declencher", "Déclencher une alerte"), ("recevoir", "Recevoir une alerte"), ("tester", "Tester la sirène"),
         ("bulletin", "Envoyer un bulletin météo")],
    liens=CYCLONE_LIENS,
    titre="Diagramme de cas d'utilisation de la station d'alerte cyclonique, corrigé",
    desc="Le cadre Station d'alerte cyclonique. Quatre ellipses, de haut en bas : Déclencher une alerte, Recevoir une "
         "alerte, Tester la sirène, Envoyer un bulletin météo. À gauche, l'agent municipal, relié à Déclencher une alerte, "
         "et le technicien, relié à Tester la sirène. À droite, l'habitant, relié à Recevoir une alerte, et le service "
         "météo, relié à Envoyer un bulletin météo. Le vent n'a pas de bonhomme.",
    hauteur=500)

# ─────────────────────────────────────────────────────────────────────────────
# Le cours, niveau par niveau (posé dans l'atelier, la synthèse élève et les séquences)
# ─────────────────────────────────────────────────────────────────────────────
COURS = {
    "5e": "<h3>À quoi sert ce diagramme</h3>"
          "<ul><li>Le <b>diagramme de cas d'utilisation</b> répond à une question&nbsp;: <b>qui se sert du système, et pour "
          "faire quoi&nbsp;?</b></li>"
          "<li>Il regarde le système <b>du dehors</b>&nbsp;: il ne dit ni comment le système marche à l'intérieur, ni dans "
          "quel ordre on agit.</li>"
          "<li>Il vient du langage <b>SysML</b> (<i>Systems Modeling Language</i>, le langage de modélisation des systèmes), "
          "que les ingénieurs utilisent pour décrire un système avec des schémas. Son nom anglais&nbsp;: <b>use case</b>.</li></ul>"
          "<h3>Les quatre éléments du dessin</h3>"
          '<div class="defile"><table><tr><th>On dessine…</th><th>Cela s\'appelle…</th><th>Cela veut dire…</th></tr>'
          "<tr><td>un grand cadre, avec le nom du système en haut</td><td>la <b>frontière du système</b></td>"
          "<td>ce qui est dedans fait partie du système&nbsp;; tout le reste est dehors</td></tr>"
          "<tr><td>un bonhomme, hors du cadre</td><td>un <b>acteur</b></td>"
          "<td>quelqu'un, ou un autre système, qui se sert du système avec un but</td></tr>"
          "<tr><td>une ellipse, dans le cadre</td><td>un <b>cas d'utilisation</b></td>"
          "<td>une action faite avec le système, écrite avec un verbe à l'infinitif&nbsp;: « Louer un vélo »</td></tr>"
          "<tr><td>un trait entre un bonhomme et une ellipse</td><td>une <b>association</b></td>"
          "<td>cet acteur participe à ce cas d'utilisation</td></tr></table></div>"
          "<h3>Qui est un acteur&nbsp;?</h3>"
          "<ul><li>Une <b>personne</b> qui se sert du système&nbsp;: l'usager, le technicien…</li>"
          "<li>Ou un <b>autre système</b> qui échange avec lui&nbsp;: le serveur de paiement d'une banque, un service météo…</li>"
          "<li>Toujours <b>en dehors</b> du système, et toujours <b>avec un but</b>&nbsp;: il demande quelque chose au système, "
          "ou il lui répond.</li></ul>"
          "<h3>Ce qui n'est pas un acteur</h3>"
          "<ul><li>Une <b>pièce</b> du système (l'écran, le cadenas, la batterie)&nbsp;: elle est dedans.</li>"
          "<li>La <b>nature</b> (la pluie, le soleil, le vent)&nbsp;: elle agit sur le système, mais sans but.</li>"
          "<li>Une <b>information</b> (l'itinéraire affiché) ou un <b>objet</b> que le système prête ou transporte (le vélo)&nbsp;: "
          "ils ne demandent rien.</li>"
          "<li>Ceux-là restent des <b>interacteurs</b>&nbsp;: leur place est dans le diagramme des interacteurs extérieurs (le "
          "diagramme pieuvre). Tout acteur est un interacteur&nbsp;; tout interacteur n'est pas un acteur.</li></ul>",
    "4e": "<h3>Du langage naturel au schéma</h3>"
          "<ul><li>On part de ce que racontent les usagers, avec leurs mots&nbsp;: des phrases recopiées telles quelles, des "
          "<b>verbatims</b>, ou un croquis.</li>"
          "<li>Dans chaque phrase, on cherche <b>l'action</b>&nbsp;: que fait la personne avec le système&nbsp;? On l'écrit avec "
          "un <b>verbe à l'infinitif + un complément</b>&nbsp;: « Payer la location ».</li>"
          "<li>Deux phrases peuvent décrire la même action&nbsp;: elles donnent un seul cas d'utilisation. Une phrase qui ne "
          "décrit aucune action (« la borne est jolie ») n'en donne aucun.</li>"
          "<li>Le <b>ressenti</b> (l'agacement, la fatigue, le plaisir) ne se dessine pas dans ce diagramme&nbsp;: on le garde "
          "à côté, pour un tableau, un graphique ou une exigence.</li></ul>"
          "<h3>Bien nommer un cas d'utilisation</h3>"
          '<div class="defile"><table><tr><th>À éviter</th><th>Pourquoi</th><th>À écrire</th></tr>'
          "<tr><td>«&nbsp;L'écran tactile&nbsp;»</td><td>c'est une pièce, pas une action</td><td>«&nbsp;Consulter les vélos disponibles&nbsp;»</td></tr>"
          "<tr><td>«&nbsp;Le paiement&nbsp;»</td><td>il n'y a pas de verbe</td><td>«&nbsp;Payer la location&nbsp;»</td></tr>"
          "<tr><td>«&nbsp;Ouvrir le cadenas&nbsp;»</td><td>c'est ce que fait une pièce, à l'intérieur</td><td>«&nbsp;Louer un vélo&nbsp;»</td></tr>"
          "<tr><td>«&nbsp;C'est trop long&nbsp;»</td><td>c'est un ressenti</td><td>rien dans le diagramme&nbsp;: une exigence, plus tard</td></tr>"
          "</table></div>"
          "<h3>Vérifier un diagramme en cinq questions</h3>"
          "<ul><li>Chaque acteur est-il <b>hors du cadre</b>&nbsp;?</li>"
          "<li>Chaque acteur a-t-il <b>au moins un trait</b>&nbsp;?</li>"
          "<li>Chaque ellipse commence-t-elle par un <b>verbe à l'infinitif</b>&nbsp;?</li>"
          "<li>Aucune ellipse ne nomme-t-elle une <b>pièce</b> du système&nbsp;?</li>"
          "<li>Aucun bonhomme n'est-il <b>la nature</b> ou <b>une donnée</b>&nbsp;?</li></ul>",
    "3e": "<h3>Un mode de représentation pour chaque question</h3>"
          '<div class="defile"><table><tr><th>La question qu\'on se pose</th><th>Le mode qui y répond</th><th>Ce qu\'il ne montre pas</th></tr>'
          "<tr><td>Qui fait quoi avec le système&nbsp;?</td><td>le <b>diagramme de cas d'utilisation</b></td>"
          "<td>l'ordre des actions, les quantités, le ressenti</td></tr>"
          "<tr><td>Dans quel ordre&nbsp;? Que se passe-t-il si…&nbsp;?</td><td>l'<b>algorigramme</b></td>"
          "<td>qui est concerné, ce que l'usager ressent</td></tr>"
          "<tr><td>Que vit l'usager, étape par étape&nbsp;?</td><td>le <b>storyboard</b> (une suite d'images)</td>"
          "<td>les cas d'échec précis, les quantités</td></tr>"
          "<tr><td>Combien&nbsp;? Lequel le plus&nbsp;?</td><td>le <b>graphique</b></td><td>le déroulement, les personnes</td></tr>"
          "<tr><td>Qu'est-ce qui entoure l'objet&nbsp;?</td><td>le <b>diagramme des interacteurs</b> (pieuvre)</td>"
          "<td>ce que chacun fait avec l'objet</td></tr></table></div>"
          "<h3>Construire le diagramme à partir d'un texte</h3>"
          "<ul><li>Souligne les <b>personnes</b> et les <b>autres systèmes</b> qui agissent avec un but&nbsp;: ce sont les "
          "acteurs, dessinés hors du cadre.</li>"
          "<li>Souligne les <b>verbes</b> de ce qu'ils font avec le système&nbsp;: ce sont les cas d'utilisation, dans les "
          "ellipses.</li>"
          "<li>Relie chaque acteur aux cas auxquels il participe&nbsp;; un cas peut avoir deux acteurs.</li>"
          "<li>Écarte la nature, les données et les pièces&nbsp;: elles iront dans le diagramme des interacteurs, les exigences "
          "ou la chaîne d'information.</li></ul>"
          "<h3>Un acteur qui n'est pas une personne</h3>"
          "<ul><li>Un service météo, le serveur d'une banque, un autre ordinateur&nbsp;: ce sont des <b>systèmes</b>, en dehors "
          "du nôtre, qui échangent avec lui <b>avec un but</b>. Ce sont des acteurs.</li>"
          "<li>Dans nos schémas, tous les acteurs sont dessinés en bonhomme. Dans les logiciels qui dessinent en SysML (le "
          "langage de modélisation des systèmes), un acteur qui est un autre système se dessine souvent par un rectangle "
          "marqué «&nbsp;actor&nbsp;»&nbsp;: c'est le même acteur, dessiné autrement.</li></ul>",
}

# ─────────────────────────────────────────────────────────────────────────────
# 5e — RECONNAÎTRE les acteurs (5e_C2.1)
# ─────────────────────────────────────────────────────────────────────────────
BANQUE_E1 = ["l'usager", "le technicien de maintenance", "le serveur de paiement", "la pluie", "le vélo"]

E1 = dict(
    id="e1", titre="Qui sont les acteurs de la station&nbsp;?", code="5e_C2.1", duree=15,
    objectif="reconnaître, parmi ce qui entoure une station de vélos, ceux qui en sont les <b>acteurs</b>, et dire pourquoi "
             "les autres n'en sont pas.",
    production="le classement de sept éléments avec leur raison, trois acteurs placés dans le schéma, et une phrase sur "
               "l'écran tactile.",
    mots=[("acteur", "une personne, ou un autre système, qui se sert du système <b>avec un but</b> et qui reste <b>en dehors</b> "
           "de lui. Il se dessine en bonhomme."),
          ("cas d'utilisation", "une action qu'un acteur fait avec le système, écrite avec un verbe à l'infinitif et un "
           "complément&nbsp;: « Louer un vélo ». Il se dessine dans une ellipse."),
          ("frontière du système", "le grand cadre du diagramme&nbsp;: ce qui est dedans fait partie du système."),
          ("interacteur extérieur", "tout ce qui est en dehors d'un objet et en relation avec lui&nbsp;: personnes, objets, "
           "données, nature. Les acteurs en sont une partie."),
          ("constituant", "une pièce du système lui-même (l'écran, le cadenas). Un constituant est dedans."),
          ("serveur de paiement", "un ordinateur de la banque, loin de la station, qui accepte ou refuse une carte bancaire."),
          ("SysML", "<i>Systems Modeling Language</i>&nbsp;: le langage de modélisation des systèmes, une façon commune de "
           "dessiner les systèmes. Le diagramme de cas d'utilisation en fait partie.")],
    intro="<p>Sur le front de mer de Sainte-Luce, une <b>station de vélos en libre-service</b> (imaginée pour l'exercice) prête "
          "des vélos&nbsp;: on pose sa carte sur la borne, on paie, le cadenas s'ouvre, on part. Le soir, un technicien vient "
          "vérifier les bornes. Pour le paiement, la borne interroge le <b>serveur de paiement</b> de la banque&nbsp;: un "
          "ordinateur, loin de là, qui accepte ou refuse la carte.</p>",
    consigne="<p>Dans un diagramme de cas d'utilisation, un <b>acteur</b> est une personne, ou un autre système, qui se sert "
             "de la station <b>avec un but</b> et qui reste <b>en dehors</b> d'elle. <b>Range chacun des sept éléments</b>&nbsp;: "
             "est-ce un acteur, et sinon, pourquoi&nbsp;? Puis <b>place les trois acteurs</b> dans le schéma (tes choix "
             "s'écrivent sous les bonshommes), et <b>explique</b> en une phrase pourquoi l'écran tactile n'est pas un "
             "acteur.</p>",
    critere="sept classements justes, les trois bonshommes à leur place, et une phrase qui dit que l'écran est une pièce de "
            "la borne, dedans.",
    widgets=[dict(type="classer", name="cl",
                  categories=[("personne", "un acteur&nbsp;: une personne qui se sert de la station, avec un but"),
                              ("systeme", "un acteur&nbsp;: un autre système qui échange avec la station"),
                              ("nature", "pas un acteur&nbsp;: il agit sur la station, mais sans but"),
                              ("donnee", "pas un acteur&nbsp;: c'est une information"),
                              ("objet", "pas un acteur&nbsp;: c'est un objet que la station prête, il ne demande rien"),
                              ("piece", "pas un acteur&nbsp;: c'est une pièce de la station, dedans")],
                  items=[("L'usager qui loue un vélo", "personne",
                          "L'usager : une personne, en dehors de la station, qui veut un vélo."),
                         ("La pluie", "nature", "La pluie mouille la borne, mais veut-elle obtenir quelque chose de la station ?"),
                         ("Le serveur de paiement de la banque", "systeme",
                          "Le serveur de paiement n'est pas une personne, mais il répond à la borne : il accepte ou refuse la carte."),
                         ("L'écran tactile de la borne", "piece", "L'écran tactile : est-il dehors, ou fait-il partie de la borne ?"),
                         ("Le technicien de maintenance", "personne",
                          "Le technicien est une personne ; il vient vérifier et réparer les bornes : c'est un but."),
                         ("Le vélo", "objet", "Le vélo est ce que la station prête : demande-t-il quelque chose à la station ?"),
                         ("L'itinéraire affiché sur l'écran", "donnee", "L'itinéraire se lit, il ne se touche pas : qu'est-ce que c'est ?")]),
             dict(type="slots", intro='<figure class="figure schema-vivant">' + FIG_STATION +
                  "<figcaption>Le diagramme de cas d'utilisation de la station. Tes choix s'écrivent sous les trois bonshommes "
                  "vides (…).</figcaption></figure>",
                  slots=[dict(name="a1", cible="cu-a1",
                              legende="Le bonhomme du haut, à gauche — relié à « Louer un vélo », « Rendre un vélo » et « Payer la location »",
                              options=BANQUE_E1, bonnes=["l'usager"],
                              indice="Le bonhomme du haut, à gauche, loue, rend et paie : une personne qui veut se déplacer."),
                         dict(name="a2", cible="cu-a2", legende="Le bonhomme du bas, à gauche — relié à « Réparer une borne »",
                              options=BANQUE_E1, bonnes=["le technicien de maintenance"],
                              indice="Le bonhomme du bas, à gauche, répare : c'est son métier."),
                         dict(name="a3", cible="cu-a3", legende="Le bonhomme de droite — relié à « Payer la location »",
                              options=BANQUE_E1, bonnes=["le serveur de paiement"],
                              indice="Le paiement a deux acteurs : celui qui paie, et l'ordinateur de la banque qui accepte la carte.")]),
             dict(type="texte", name="ecran", lignes=3,
                  label="Explique en une phrase pourquoi l'écran tactile n'est pas un acteur de la station.",
                  criteres=[dict(label="tu dis que l'écran est une pièce de la borne",
                                 motifs=["piece", "constituant", "partie", "composant", "element de la borne", "morceau"],
                                 manque="Dis ce QU'EST l'écran pour la borne : une pièce de la borne, ou quelqu'un qui s'en sert ?"),
                            dict(label="tu dis qu'il est dans le système, pas en dehors",
                                 motifs=["dedans", "dans la borne", "dans la station", "dans le systeme", "interieur",
                                         "pas en dehors", "pas dehors", "n'est pas exterieur", "dans le cadre"],
                                 manque="Dis OÙ il est : dedans ou dehors ? Un acteur est toujours en dehors du système.")],
                  etayage=["L'écran tactile n'est pas un acteur, car c'est … de la borne.",
                           "Il est … du système, alors qu'un acteur est toujours …"],
                  exemple="L'écran tactile est une pièce de la borne : il est dedans, dans le système, alors qu'un acteur est "
                          "toujours en dehors.")],
    aides=["<p>Pour chaque élément, pose deux questions, dans l'ordre&nbsp;: <b>est-il en dehors de la station&nbsp;?</b> Puis&nbsp;: "
           "<b>se sert-il de la station avec un but</b> — veut-il obtenir quelque chose, ou répond-il à une demande&nbsp;? Pour le "
           "schéma, lis les ellipses reliées à chaque bonhomme&nbsp;: elles disent ce qu'il fait.</p>",
           "<p>L'écran tactile → en dehors&nbsp;? Non, c'est une pièce de la borne → <b>pas un acteur</b>.<br>"
           "La pluie → en dehors&nbsp;? Oui. Avec un but&nbsp;? Non, elle tombe, c'est tout → <b>pas un acteur</b>.<br>"
           "Le serveur de paiement → en dehors&nbsp;? Oui, il est à la banque. Avec un but&nbsp;? Oui&nbsp;: la borne lui demande si "
           "la carte est bonne, il répond → <b>un acteur</b>, sans être une personne.<br>"
           "Dans le schéma&nbsp;: « Réparer une borne » → c'est le métier du technicien.</p>"],
    jumeau=dict(consigne="Un distributeur de billets de banque. Parmi ces quatre éléments, lesquels sont des acteurs&nbsp;: le "
                         "client, le clavier, le serveur de la banque, le soleil qui éclaire l'écran&nbsp;?",
                correction="<b>Le client</b> → une personne, dehors, qui veut des billets → <b>acteur</b>. <b>Le serveur de la "
                           "banque</b> → un autre système, dehors, qui accepte ou refuse le retrait → <b>acteur</b>. <b>Le "
                           "clavier</b> → une pièce du distributeur, dedans → pas un acteur. <b>Le soleil</b> → il agit sans but → "
                           "pas un acteur (un interacteur, dans le diagramme pieuvre)."),
    correction=[
        '<figure class="figure">' + FIG_STATION_C + "<figcaption>Le diagramme corrigé : trois acteurs, hors du cadre.</figcaption></figure>",
        "<b>Ce qu'on cherche&nbsp;:</b> un acteur est <b>en dehors</b> du système <b>et</b> s'en sert <b>avec un but</b> (il "
        "demande, ou il répond).",
        "<b>L'usager</b> → dehors ✔ → veut louer un vélo ✔ → <b>acteur</b> (une personne)",
        "<b>Le technicien de maintenance</b> → dehors ✔ → vient vérifier et réparer ✔ → <b>acteur</b> (une personne)",
        "<b>Le serveur de paiement</b> → dehors, à la banque ✔ → accepte ou refuse la carte ✔ → <b>acteur</b> (un autre système)",
        "<b>La pluie</b> → dehors ✔ → mais sans but ✘ → <b>pas un acteur</b>&nbsp;: un interacteur de l'environnement",
        "<b>L'itinéraire</b> → une information qu'on lit ✘ → <b>pas un acteur</b>&nbsp;: une donnée",
        "<b>Le vélo</b> → ce que la station prête&nbsp;; il ne demande rien ✘ → <b>pas un acteur</b>&nbsp;: un autre objet",
        "<b>L'écran tactile</b> → une pièce de la borne, dedans ✘ → <b>pas un acteur</b>&nbsp;: un constituant",
        "<b>Le schéma</b> → en haut à gauche&nbsp;: <b>l'usager</b> (louer, rendre, payer) → en bas à gauche&nbsp;: <b>le "
        "technicien de maintenance</b> (réparer) → à droite&nbsp;: <b>le serveur de paiement</b> (payer)",
        "<b>Refusés dans le schéma&nbsp;:</b> la pluie et le vélo → aucun but → pas de bonhomme.",
        "<b>Une phrase attendue&nbsp;:</b> « L'écran tactile est une <b>pièce</b> de la borne&nbsp;: il est <b>dedans</b>, alors "
        "qu'un acteur est toujours en dehors. »",
        ("conclusion", "Sur sept éléments, <b>trois</b> sont des acteurs. Tout acteur est un interacteur&nbsp;; tout interacteur "
                       "n'est pas un acteur."),
    ],
    retenir="un <b>acteur</b> est une personne ou un autre système, <b>en dehors</b> du système, qui s'en sert <b>avec un "
            "but</b>. La pluie, une donnée, un objet prêté ou une pièce n'en sont pas.",
    piege="dessiner la pluie en bonhomme parce qu'elle « agit » sur la station&nbsp;: elle agit, mais sans but.",
)

PIECES_LAMPADAIRE = (r"^(la |le |les |l'|un |une |des |son |sa |ses )?(panneaux?|batteries?|lampes?|ampoules?|poteaux?|mats?|"
                     r"capteurs?|detecteurs?|leds?|cables?|piles?|boitiers?)\b")

E2 = dict(
    id="e2", titre="Lire le diagramme du lampadaire, faire la liste de ses acteurs", code="5e_C2.1", duree=15,
    objectif="nommer les quatre éléments d'un diagramme de cas d'utilisation, le lire, et faire la liste des acteurs d'un système.",
    production="quatre éléments nommés, la lecture d'une ellipse, la raison de l'absence du soleil, et la liste des acteurs "
               "du lampadaire.",
    mots=[("frontière du système", "le grand cadre, avec le nom du système en haut&nbsp;: ce qui est dedans fait partie du "
           "système, tout le reste est dehors."),
          ("acteur", "une personne, ou un autre système, en dehors du système, qui s'en sert avec un but&nbsp;; dessiné en bonhomme."),
          ("cas d'utilisation", "une action faite avec le système, dans une ellipse&nbsp;: un verbe à l'infinitif, puis un complément."),
          ("association", "le trait qui relie un acteur à un cas d'utilisation&nbsp;: cet acteur participe à cette action."),
          ("panneau solaire", "la pièce du lampadaire qui transforme la lumière du soleil en énergie électrique, pour charger la batterie.")],
    documents=[dict(svg=FIG_LAMPADAIRE, legende="Le diagramme de cas d'utilisation du lampadaire solaire du parking.",
                    description="<p>Un grand cadre nommé « Lampadaire solaire du parking ». Dedans, quatre ellipses, de haut en "
                                "bas&nbsp;: Voir son chemin la nuit&nbsp;; Régler les heures d'allumage&nbsp;; Suivre la charge "
                                "de la batterie&nbsp;; Remplacer la lampe.</p><p>Hors du cadre, trois bonshommes. À gauche, le "
                                "piéton, relié à Voir son chemin la nuit. À droite, en haut, l'agent de la mairie, relié à Régler "
                                "les heures d'allumage et à Suivre la charge de la batterie. À droite, en bas, le technicien, "
                                "relié à Suivre la charge de la batterie et à Remplacer la lampe.</p>")],
    intro="<p>La mairie a installé des <b>lampadaires solaires</b> sur le parking du collège. Le jour, le soleil recharge "
          "leur batterie grâce à un panneau solaire&nbsp;; la nuit, la lampe éclaire le parking. Un agent de la mairie règle les "
          "heures d'allumage depuis son bureau et suit la charge des batteries&nbsp;; un technicien vient vérifier les "
          "batteries et remplacer les lampes usées.</p>",
    consigne="<p>Un diagramme de cas d'utilisation se dessine avec quatre éléments&nbsp;: la <b>frontière du système</b> (le "
             "cadre), les <b>acteurs</b> (les bonshommes), les <b>cas d'utilisation</b> (les ellipses&nbsp;: ce que l'acteur "
             "fait avec le système) et les <b>associations</b> (les traits). <b>Relie chaque élément dessiné à son nom</b>, "
             "puis <b>lis</b> le diagramme&nbsp;: qui est relié à « Suivre la charge de la batterie »&nbsp;? Dis pourquoi le "
             "soleil n'a pas de bonhomme. Enfin, <b>fais la liste des acteurs</b> du lampadaire.</p>",
    critere="les quatre noms justes, les deux acteurs de la batterie (et eux seuls), la bonne raison pour le soleil, et une "
            "liste de trois acteurs sans intrus.",
    widgets=[dict(type="classer", name="noms",
                  categories=[("frontiere", "la frontière du système"), ("acteur", "un acteur"),
                              ("cas", "un cas d'utilisation"), ("asso", "une association")],
                  items=[("Le grand cadre qui porte en haut le nom « Lampadaire solaire du parking »", "frontiere",
                          "Le grand cadre sépare ce qui fait partie du lampadaire de ce qui est dehors."),
                         ("Chaque bonhomme, hors du cadre", "acteur", "Un bonhomme : quelqu'un qui se sert du lampadaire."),
                         ("Chaque ellipse, dans le cadre", "cas", "Une ellipse contient une action, avec un verbe : « Remplacer la lampe »."),
                         ("Chaque trait entre un bonhomme et une ellipse", "asso",
                          "Un trait relie un acteur à une action à laquelle il participe.")]),
             dict(type="cases", name="batterie",
                  legende="Qui est relié à l'ellipse « Suivre la charge de la batterie »&nbsp;?",
                  options=[("agent", "l'agent de la mairie"), ("tech", "le technicien"), ("pieton", "le piéton"),
                           ("soleil", "le soleil")],
                  bonnes=["agent", "tech"],
                  retours={"agent": "Oui : un trait relie l'agent de la mairie à cette ellipse.",
                           "tech": "Oui : le technicien y est relié aussi. Une ellipse peut avoir deux acteurs.",
                           "pieton": "Le piéton n'a qu'un trait : vers « Voir son chemin la nuit ».",
                           "soleil": "Le soleil n'est pas dessiné : il recharge la batterie, mais sans but. Ce n'est pas un acteur."},
                  indice="Suis les traits qui arrivent à « Suivre la charge de la batterie » : il y en a deux."),
             dict(type="choix", name="soleil",
                  legende="Le soleil recharge la batterie tous les jours. Pourquoi n'a-t-il pas de bonhomme dans le diagramme&nbsp;?",
                  options=[("loin", "Parce qu'il est bien trop loin du parking pour être dessiné."),
                           ("but", "Parce qu'il agit sur le lampadaire sans but&nbsp;: c'est un interacteur, pas un acteur."),
                           ("dedans", "Parce qu'il fait partie du lampadaire, comme le panneau solaire."),
                           ("jour", "Parce que le diagramme ne montre que ce qui se passe la nuit.")],
                  bonne="but",
                  retours={"loin": "La distance ne compte pas : le serveur d'une banque, loin de la station, est un acteur.",
                           "dedans": "Le panneau solaire fait partie du lampadaire ; le soleil, lui, est dehors. Ce n'est pas la raison.",
                           "jour": "Le diagramme ne dit rien du jour ou de la nuit : « Régler les heures d'allumage » se fait de jour.",
                           "but": "Oui : le soleil ne veut rien obtenir du lampadaire. Il reste un interacteur (l'environnement), dans le diagramme pieuvre."}),
             dict(type="liste", name="acteurs", min=3, lignes=5,
                  label="La liste des acteurs du lampadaire (un par ligne)",
                  attendus=[dict(nom="le piéton", motifs=["pieton", "passant", "marcheur", "promeneur", r"\beleve", "usager",
                                                          "personne qui (passe|marche|traverse)"]),
                            dict(nom="l'agent de la mairie", motifs=["agent", "mairie", "municipal", "employe", r"\bmaire\b"]),
                            dict(nom="le technicien", motifs=["technicien", "reparateur", "maintenance", "electricien", "depanneur"])],
                  refuses=[dict(motifs=[r"\bsoleil\b", r"\bnuit\b", r"\bpluie\b", r"\bvent\b", "obscurite", "lumiere du jour"],
                                message="{ligne} agit sur le lampadaire, mais sans but : c'est un interacteur (l'environnement), pas un acteur."),
                           dict(motifs=[PIECES_LAMPADAIRE],
                                message="{ligne} est une pièce du lampadaire : elle est dedans. Un acteur est toujours en dehors."),
                           dict(motifs=[r"^(voir|regler|suivre|remplacer|eclairer|allumer|recharger|changer|reparer)\b"],
                                message="{ligne} est une action : elle s'écrit dans une ellipse, pas sous un bonhomme.")],
                  inconnu="{ligne} : je ne le reconnais pas. Cherche les bonshommes du diagramme — ou écris-le avec un autre mot.",
                  etayage=["Le bonhomme de gauche : …", "Le bonhomme en haut à droite : …", "Le bonhomme en bas à droite : …"],
                  exemple="le piéton\nl'agent de la mairie\nle technicien")],
    aides=["<p>Pour nommer les éléments, regarde leur <b>forme</b>&nbsp;: un cadre, des bonshommes, des ellipses, des traits. "
           "Pour lire le diagramme, <b>suis les traits</b>&nbsp;: chacun part d'un bonhomme et arrive à une ellipse.</p>",
           "<p>Le cadre → il sépare le dedans du dehors → <b>la frontière du système</b>.<br>"
           "Un bonhomme → quelqu'un qui se sert du lampadaire → <b>un acteur</b>.<br>"
           "« Suivre la charge de la batterie » → deux traits y arrivent → l'agent de la mairie <b>et</b> le technicien.<br>"
           "Le soleil → il recharge la batterie, mais il ne veut rien → pas de bonhomme.<br>"
           "La liste des acteurs → recopie le nom écrit sous chaque bonhomme.</p>"],
    jumeau=dict(consigne="Le diagramme de cas d'utilisation d'un four à micro-ondes montre deux bonshommes, « le cuisinier » "
                         "et « le réparateur », et trois ellipses&nbsp;: « Réchauffer un plat », « Programmer une durée », "
                         "« Changer le plateau ». Fais la liste de ses acteurs. Le plat en fait-il partie&nbsp;?",
                correction="Les acteurs&nbsp;: <b>le cuisinier</b> et <b>le réparateur</b>, les deux bonshommes. <b>Le plat</b> "
                           "n'est pas un acteur&nbsp;: il est réchauffé, il ne demande rien au four. On le retrouve dans le "
                           "complément d'un cas&nbsp;: « Réchauffer un plat »."),
    correction=[
        "<b>Le grand cadre</b> → il sépare ce qui est dans le lampadaire de ce qui est dehors → <b>la frontière du système</b>",
        "<b>Chaque bonhomme</b>, hors du cadre → quelqu'un qui se sert du lampadaire avec un but → <b>un acteur</b>",
        "<b>Chaque ellipse</b>, dans le cadre → une action faite avec le lampadaire, avec un verbe à l'infinitif → <b>un cas "
        "d'utilisation</b>",
        "<b>Chaque trait</b> → il relie un acteur à une action à laquelle il participe → <b>une association</b>",
        "<b>« Suivre la charge de la batterie »</b> → deux traits → <b>l'agent de la mairie</b> et <b>le technicien</b> → une "
        "ellipse peut avoir deux acteurs",
        "Le piéton n'y est pas relié&nbsp;: son seul trait va à « Voir son chemin la nuit ». Le soleil n'est pas dessiné du tout.",
        "<b>Le soleil</b> → il recharge la batterie, mais il ne veut rien obtenir → <b>pas un acteur</b>&nbsp;: un interacteur "
        "de l'environnement, à sa place dans le diagramme pieuvre",
        "Les autres raisons ne tiennent pas&nbsp;: la distance ne compte pas (le serveur d'une banque, loin, est un acteur)&nbsp;; "
        "le soleil n'est pas une pièce du lampadaire&nbsp;; le diagramme ne dit rien du jour ou de la nuit.",
        "<b>La liste des acteurs</b> → le piéton → l'agent de la mairie → le technicien",
        "<b>Refusés&nbsp;:</b> le panneau solaire, la batterie, la lampe → des pièces, dedans&nbsp;; le soleil, la nuit → sans "
        "but&nbsp;; « régler les heures » → une action, qui va dans une ellipse.",
        ("conclusion", "Un diagramme de cas d'utilisation se lit en <b>suivant les traits</b>&nbsp;: chaque trait dit <b>qui</b> "
                       "fait <b>quoi</b> avec le système."),
    ],
    retenir="quatre éléments&nbsp;: la <b>frontière du système</b> (le cadre), les <b>acteurs</b> (les bonshommes, dehors), les "
            "<b>cas d'utilisation</b> (les ellipses, dedans) et les <b>associations</b> (les traits qui disent qui fait quoi).",
    piege="lire les ellipses de haut en bas comme une suite d'étapes&nbsp;: le diagramme dit qui fait quoi, pas dans quel ordre.",
)

# ─────────────────────────────────────────────────────────────────────────────
# 4e — PASSER du langage naturel au schéma (4e_C2.1)
# ─────────────────────────────────────────────────────────────────────────────
E3 = dict(
    id="e3", titre="Du verbatim au cas d'utilisation", code="4e_C2.1", duree=10,
    objectif="passer de ce que disent les usagers, avec leurs mots, aux cas d'utilisation de la borne.",
    production="le cas d'utilisation de sept verbatims, et la place du ressenti.",
    mots=[("verbatim", "ce qu'une personne a dit, recopié mot pour mot, sans le résumer."),
          ("langage naturel", "la langue de tous les jours, celle qu'on parle et qu'on écrit, par opposition aux schémas et aux codes."),
          ("cas d'utilisation", "une action qu'un acteur fait avec le système, écrite avec un verbe à l'infinitif et un "
           "complément&nbsp;: « Louer un vélo »."),
          ("ressenti", "ce que l'usager éprouve en se servant du système&nbsp;: agacement, fatigue, doute, plaisir…"),
          ("acteur", "une personne, ou un autre système, en dehors du système, qui s'en sert avec un but&nbsp;; dessiné en bonhomme."),
          ("SysML", "<i>Systems Modeling Language</i>&nbsp;: le langage de modélisation des systèmes, une façon commune de "
           "dessiner les systèmes, dont fait partie le diagramme de cas d'utilisation.")],
    intro="<p>À la station de vélos du front de mer de Sainte-Luce, on a demandé aux usagers de raconter comment ils se "
          "servent de la <b>borne</b>. Leurs phrases, recopiées mot pour mot, s'appellent des <b>verbatims</b>&nbsp;: c'est du "
          "<b>langage naturel</b>, la langue de tous les jours. Le diagramme de cas d'utilisation — souvent appelé use case "
          "SysML (<i>Systems Modeling Language</i>, le langage de modélisation des systèmes) — va en garder l'essentiel&nbsp;: "
          "<b>qui fait quoi</b> avec la borne.</p>",
    consigne="<p>Un <b>cas d'utilisation</b> est une action qu'un acteur fait avec le système, écrite avec un verbe à "
             "l'infinitif et un complément (« Louer un vélo »). <b>Pour chaque verbatim, choisis le cas d'utilisation qu'il "
             "décrit</b> — ou « aucun », si la phrase ne décrit aucune action faite avec la borne. Puis <b>dis</b> où va le "
             "ressenti des usagers.</p>",
    critere="sept réponses justes, et tu sais dire pourquoi l'agacement de Kenza ne se dessine pas dans le diagramme.",
    widgets=[dict(type="classer", name="verb",
                  categories=[("louer", "Louer un vélo"), ("rendre", "Rendre un vélo"), ("payer", "Payer la location"),
                              ("consulter", "Consulter les vélos disponibles"), ("signaler", "Signaler une panne"),
                              ("aucun", "aucun cas&nbsp;: la phrase ne décrit aucune action faite avec la borne")],
                  items=[("Maëva, étudiante&nbsp;: « Je pose ma carte, j'attends le bip, et le cadenas me laisse partir avec le vélo. »",
                          "louer", "Maëva repart avec un vélo : quelle action a-t-elle faite avec la borne ?"),
                         ("Kenza, infirmière&nbsp;: « Je ne trouve jamais où poser ma carte pour prendre un vélo&nbsp;: il y a trois logos sur la borne. »",
                          "louer", "Kenza parle d'une difficulté, mais pendant quelle action ? Elle veut prendre un vélo."),
                         ("Tom, touriste&nbsp;: « Taper le code de ma carte bancaire en plein soleil, c'est long&nbsp;: je ne vois rien sur l'écran. »",
                          "payer", "Tom tape le code de sa carte bancaire : pour faire quoi ?"),
                         ("M. Jean-Baptiste, retraité&nbsp;: « Le soir, je remets le vélo dans un emplacement libre et j'attends que le voyant passe au vert. »",
                          "rendre", "M. Jean-Baptiste remet le vélo à sa place : quelle action ?"),
                         ("Lucas, lycéen&nbsp;: « En arrivant, je regarde sur l'écran de la borne combien il reste de vélos. »",
                          "consulter", "Lucas ne prend rien : il regarde une information sur l'écran."),
                         ("Mme Rosine, habituée&nbsp;: « Le vélo avait un pneu à plat&nbsp;: j'ai appuyé sur le bouton rouge, et la borne l'a mis de côté. »",
                          "signaler", "Mme Rosine prévient la borne qu'un vélo a un problème."),
                         ("Inès, collégienne&nbsp;: « Franchement, le bleu de la borne est joli, il va bien avec la mer. »",
                          "aucun", "Inès donne un avis sur la couleur : fait-elle quelque chose avec la borne ?")]),
             dict(type="choix", name="ressenti",
                  legende="Kenza est agacée, Tom trouve le paiement long. Ce <b>ressenti</b> se dessine-t-il dans le diagramme de "
                          "cas d'utilisation&nbsp;?",
                  options=[("ellipse", "Oui&nbsp;: on ajoute une ellipse « Être agacé », reliée à Kenza."),
                           ("non", "Non&nbsp;: le diagramme dit qui fait quoi&nbsp;; le ressenti se garde à côté, pour une exigence."),
                           ("bonhomme", "Oui&nbsp;: on dessine un bonhomme triste à la place de celui de Kenza."),
                           ("couleur", "Oui&nbsp;: on colorie en rouge les ellipses qui posent un problème.")],
                  bonne="non",
                  retours={"non": "Oui : le diagramme garde l'action (Louer un vélo, Payer la location). Le ressenti se note à côté : il deviendra une exigence (« l'écran reste lisible en plein soleil »).",
                           "ellipse": "« Être agacé » n'est pas une action faite avec la borne : ce n'est pas un cas d'utilisation.",
                           "bonhomme": "Un bonhomme est un acteur, pas une émotion : Kenza reste « l'usager », contente ou non.",
                           "couleur": "Une couleur seule ne se lit pas par tous ; et le diagramme ne montre pas les problèmes : il montre qui fait quoi."})],
    aides=["<p>Dans chaque phrase, cherche le <b>verbe</b> de ce que fait la personne avec la borne&nbsp;: poser sa carte pour "
           "partir, remettre, taper son code, regarder, appuyer pour prévenir… Puis cherche le cas qui dit la même action.</p>",
           "<p>Maëva → pose sa carte et part avec le vélo → <b>Louer un vélo</b>.<br>"
           "Kenza → elle cherche où poser sa carte <b>pour prendre un vélo</b> → sa difficulté est dans <b>Louer un vélo</b>&nbsp;; "
           "son agacement, lui, ne se dessine pas.<br>"
           "Tom → tape le code de sa carte bancaire → <b>Payer la location</b>.<br>"
           "Inès → donne un avis sur la couleur → elle ne fait rien avec la borne → <b>aucun cas</b>.</p>"],
    jumeau=dict(consigne="Deux verbatims de la gardienne du jardin partagé, sur le système d'arrosage&nbsp;: « Le dimanche "
                         "soir, je règle sur mon téléphone l'heure d'arrosage de la semaine. » et « Ce boîtier vert est discret, "
                         "on ne le voit pas derrière les plantes. » Quel cas d'utilisation pour chacun&nbsp;?",
                correction="Le premier → la gardienne règle une heure → <b>Programmer l'heure d'arrosage</b>. Le second → un avis "
                           "sur la couleur et la discrétion → elle ne fait rien avec le système → <b>aucun cas</b>&nbsp;: c'est un "
                           "ressenti, utile plus tard pour une exigence de forme."),
    correction=[
        "<b>Ce qu'on cherche&nbsp;:</b> dans chaque phrase, <b>l'action</b> faite avec la borne, écrite verbe + complément.",
        "<b>Maëva</b> → pose sa carte, part avec le vélo → <b>Louer un vélo</b>",
        "<b>Kenza</b> → cherche où poser sa carte pour prendre un vélo → <b>Louer un vélo</b> (sa difficulté est un ressenti, "
        "pas un autre cas)",
        "<b>Tom</b> → tape le code de sa carte bancaire → <b>Payer la location</b>",
        "<b>M. Jean-Baptiste</b> → remet le vélo dans un emplacement libre → <b>Rendre un vélo</b>",
        "<b>Lucas</b> → regarde combien il reste de vélos → <b>Consulter les vélos disponibles</b>",
        "<b>Mme Rosine</b> → prévient que le vélo a un pneu à plat → <b>Signaler une panne</b>",
        "<b>Inès</b> → donne un avis sur la couleur → aucune action → <b>aucun cas d'utilisation</b>",
        "<b>Le ressenti</b> (l'agacement de Kenza, la gêne de Tom) → ne se dessine pas → il se garde à côté, pour un tableau "
        "des ressentis, un graphique ou une exigence (« l'écran reste lisible en plein soleil »).",
        "Les autres réponses ne tiennent pas&nbsp;: « Être agacé » n'est pas une action&nbsp;; un bonhomme est un acteur, pas une "
        "émotion&nbsp;; une couleur seule ne se lit pas par tous.",
        ("conclusion", "Sept verbatims → <b>cinq</b> cas d'utilisation&nbsp;: deux phrases décrivent la même action, et une n'en "
                       "décrit aucune. Le diagramme garde <b>l'action</b>&nbsp;; le <b>ressenti</b> se garde à côté."),
    ],
    retenir="pour passer d'un verbatim au schéma, on cherche <b>l'action</b> faite avec le système et on l'écrit <b>verbe à "
            "l'infinitif + complément</b>. Le ressenti ne se dessine pas&nbsp;: on le garde pour les exigences.",
    piege="créer un cas d'utilisation par phrase&nbsp;: deux usagers peuvent raconter la même action, et un avis (« c'est "
          "joli ») n'en est pas une.",
)

BANQUE_E4 = ["Rendre un vélo", "Signaler une panne", "le serveur de paiement", "l'écran tactile", "le vélo"]

E4 = dict(
    id="e4", titre="Compléter le diagramme de la borne", code="4e_C2.1", duree=10,
    objectif="compléter un diagramme de cas d'utilisation avec les cas tirés des verbatims, et écarter ce qui n'est ni un "
             "cas ni un acteur.",
    production="deux ellipses et un acteur complétés, et la raison des deux intrus.",
    mots=[("frontière du système", "le grand cadre&nbsp;: ce qui est dedans fait partie du système."),
          ("constituant", "une pièce du système lui-même (l'écran tactile, le cadenas). Un constituant est dedans&nbsp;: ce n'est "
           "ni un acteur, ni une action."),
          ("serveur de paiement", "un ordinateur de la banque, en dehors de la station, qui accepte ou refuse une carte bancaire."),
          ("association", "le trait qui relie un acteur à un cas d'utilisation."),
          ("intrus", "un mot de la banque qui n'a sa place dans aucune case.")],
    intro="<p>Les verbatims des usagers ont donné les cas d'utilisation de la borne. Il reste à les placer dans le schéma. "
          "Deux ellipses et un bonhomme sont encore vides&nbsp;: ils s'affichent avec des points de suspension (…).</p>",
    consigne="<p>Dans ce diagramme, chaque <b>ellipse</b> est un cas d'utilisation (une action, avec un verbe à l'infinitif) "
             "et chaque <b>bonhomme</b> un acteur (une personne ou un autre système, dehors, qui se sert de la borne avec un "
             "but). <b>Complète les deux ellipses vides et le bonhomme vide</b> avec la banque&nbsp;: <i>Rendre un vélo · "
             "Signaler une panne · le serveur de paiement · l'écran tactile · le vélo</i>. Tes choix s'écrivent dans le "
             "schéma. Deux mots de la banque sont des <b>intrus</b>&nbsp;: <b>dis pourquoi</b>.</p>",
    critere="les trois cases justes, et la bonne raison pour l'écran tactile et le vélo.",
    widgets=[dict(type="slots", intro='<figure class="figure schema-vivant">' + FIG_BORNE +
                  "<figcaption>Le diagramme de cas d'utilisation de la borne. Tes choix s'écrivent dans les deux ellipses en "
                  "pointillés et sous le bonhomme de droite.</figcaption></figure>",
                  slots=[dict(name="c1", cible="cu-c1", legende="L'ellipse vide du haut — reliée seulement à l'usager",
                              options=BANQUE_E4, bonnes=["Rendre un vélo"],
                              indice="L'ellipse vide du haut n'est reliée qu'à l'usager : que fait-il seul, quand il a fini sa course ?"),
                         dict(name="c2", cible="cu-c2", legende="L'ellipse vide du bas — reliée à l'usager <b>et</b> au technicien",
                              options=BANQUE_E4, bonnes=["Signaler une panne"],
                              indice="L'ellipse vide du bas est reliée à l'usager ET au technicien : l'usager prévient, le technicien est averti."),
                         dict(name="a4", cible="cu-a4", legende="Le bonhomme vide, à droite — relié à « Payer la location »",
                              options=BANQUE_E4, bonnes=["le serveur de paiement"],
                              indice="Le bonhomme de droite participe au paiement : qui accepte ou refuse la carte ?")]),
             dict(type="choix", name="intrus",
                  legende="L'écran tactile et le vélo restent dans la banque. Pourquoi n'ont-ils de place ni dans une ellipse, ni "
                          "sous un bonhomme&nbsp;?",
                  options=[("dedans", "Parce que tous les deux sont dans le cadre du système, avec les ellipses."),
                           ("inverse", "Parce que le vélo devrait être une ellipse, et l'écran tactile un bonhomme."),
                           ("ok", "L'écran est une pièce de la borne, le vélo un objet prêté&nbsp;: ni action, ni acteur."),
                           ("court", "Parce que leurs noms sont trop courts pour remplir une ellipse.")],
                  bonne="ok",
                  retours={"ok": "Oui : une ellipse attend une action, un bonhomme attend quelqu'un qui se sert de la borne. L'écran est dedans ; le vélo ne demande rien.",
                           "dedans": "L'écran est bien dedans, mais le vélo n'est pas une pièce de la borne : il part avec l'usager. La raison ne vaut pas pour les deux.",
                           "inverse": "Le vélo ne fait aucune action, et l'écran ne se sert pas de la borne : ni l'un ni l'autre ne change de case.",
                           "court": "La longueur ne compte pas : « Louer un vélo » est court aussi. Ce qui compte : une action pour une ellipse, quelqu'un pour un bonhomme."})],
    aides=["<p>Suis les traits&nbsp;: qui est relié à chaque case vide&nbsp;? Une ellipse attend une <b>action</b> (un verbe)&nbsp;; "
           "un bonhomme attend <b>quelqu'un, ou un autre système</b>. Il restera deux mots&nbsp;: demande-toi s'ils sont une "
           "action, ou quelqu'un qui se sert de la borne.</p>",
           "<p>Ellipse du haut → reliée seulement à l'usager → quand il a fini → <b>Rendre un vélo</b>.<br>"
           "Ellipse du bas → l'usager et le technicien → l'usager prévient, le technicien répare → <b>Signaler une panne</b>.<br>"
           "Bonhomme de droite → relié à « Payer la location » → il accepte la carte → <b>le serveur de paiement</b>.<br>"
           "L'écran tactile → une pièce de la borne → ni action, ni acteur.<br>"
           "Le vélo → ce que la borne prête → il ne demande rien.</p>"],
    jumeau=dict(consigne="Le diagramme de cas d'utilisation d'un distributeur de boissons a une ellipse vide reliée au client "
                         "et au serveur de paiement, et un bonhomme vide relié à « Remplir le distributeur ». Banque&nbsp;: "
                         "<i>Payer sa boisson · le livreur · le monnayeur · la canette</i>. Complète, et nomme les intrus.",
                correction="Ellipse → <b>Payer sa boisson</b> (le client et le serveur de paiement y participent). Bonhomme → "
                           "<b>le livreur</b>, qui remplit le distributeur. Intrus&nbsp;: <b>le monnayeur</b> (une pièce du "
                           "distributeur, dedans) et <b>la canette</b> (ce que le distributeur donne&nbsp;; elle ne demande rien)."),
    correction=[
        '<figure class="figure">' + FIG_BORNE_C + "<figcaption>Le diagramme corrigé de la borne.</figcaption></figure>",
        "<b>Ellipse du haut</b> → reliée seulement à l'usager → <b>Rendre un vélo</b> → le verbatim de M. Jean-Baptiste",
        "<b>Ellipse du bas</b> → reliée à l'usager <b>et</b> au technicien → <b>Signaler une panne</b> → le verbatim de Mme "
        "Rosine&nbsp;; le technicien est averti",
        "<b>Bonhomme de droite</b> → relié à « Payer la location » → <b>le serveur de paiement</b> → un autre système, dehors, "
        "qui accepte ou refuse la carte",
        "Inverser les deux ellipses serait faux&nbsp;: « Rendre un vélo » ne concerne pas le technicien.",
        "<b>L'écran tactile</b> → une pièce de la borne, dedans → <b>ni un cas, ni un acteur</b>&nbsp;: on s'en sert pour louer, "
        "payer ou consulter, c'est un moyen, pas une action",
        "<b>Le vélo</b> → ce que la borne prête&nbsp;; il ne demande rien → <b>pas un acteur</b> (un interacteur&nbsp;: un autre objet)",
        "Les autres raisons ne tiennent pas&nbsp;: le vélo n'est pas dans le cadre (il part avec l'usager)&nbsp;; aucun des deux "
        "ne change de case&nbsp;; la longueur d'un nom ne décide de rien.",
        ("conclusion", "Une ellipse attend <b>une action</b>, un bonhomme attend <b>quelqu'un qui se sert du système</b>. Une "
                       "pièce ou un objet prêté n'ont leur place dans aucun des deux."),
    ],
    retenir="une <b>ellipse</b> contient une action (verbe à l'infinitif + complément), un <b>bonhomme</b> quelqu'un ou un autre "
            "système qui se sert du système. Une <b>pièce</b> n'est ni l'un ni l'autre.",
    piege="écrire « l'écran tactile » dans une ellipse parce que l'usager le touche&nbsp;: on s'en sert, mais ce n'est pas une action.",
)

E5 = dict(
    id="e5", titre="Repérer et corriger les erreurs d'un diagramme", code="4e_C2.1", duree=12,
    objectif="vérifier un diagramme de cas d'utilisation avec les règles de construction, repérer ses erreurs et en corriger deux.",
    production="les cinq erreurs cochées, un cas d'utilisation réécrit, et le sort de « La pompe ».",
    mots=[("système d'arrosage connecté", "un système qui arrose les plantes à l'heure choisie et envoie des nouvelles sur un "
           "téléphone."),
          ("cuve", "un grand réservoir&nbsp;; ici, il recueille l'eau de pluie du toit."),
          ("constituant", "une pièce du système (la pompe, le tuyau). Un constituant est dedans&nbsp;: ce n'est pas une action."),
          ("verbe à l'infinitif", "la forme du verbe qui n'est pas conjuguée&nbsp;: arroser, programmer, consulter."),
          ("association", "le trait qui relie un acteur à un cas d'utilisation.")],
    documents=[dict(svg=FIG_ERREURS, legende="Le diagramme de cas d'utilisation du système d'arrosage, dessiné par Noah.",
                    description="<p>Un grand cadre nommé « Système d'arrosage du jardin ». Dedans, quatre ellipses, de haut en "
                                "bas&nbsp;: Programmer l'heure d'arrosage&nbsp;; La pompe&nbsp;; L'arrosage&nbsp;; Consulter le "
                                "niveau de la cuve.</p><p>Un bonhomme, la gardienne, est dessiné <b>à l'intérieur</b> du cadre, "
                                "à gauche des ellipses&nbsp;; il est relié à Programmer l'heure d'arrosage, à La pompe et à "
                                "Consulter le niveau de la cuve. Hors du cadre, à droite, deux bonshommes&nbsp;: la pluie, reliée à "
                                "L'arrosage, et le technicien, relié à aucune ellipse.</p>")],
    intro="<p>Le jardin partagé du collège a un <b>système d'arrosage connecté</b>&nbsp;: la gardienne, Mme Joseph, programme "
          "l'heure d'arrosage et consulte le niveau de la cuve d'eau de pluie sur son téléphone&nbsp;; un technicien vient "
          "l'entretenir. Noah, un élève de 4e, a dessiné son diagramme de cas d'utilisation. Il a fait plusieurs erreurs.</p>",
    consigne="<p>Un diagramme de cas d'utilisation bien construit respecte cinq règles&nbsp;: chaque acteur est <b>hors du "
             "cadre</b>&nbsp;; chaque acteur a <b>au moins un trait</b>&nbsp;; chaque ellipse dit une <b>action</b>, avec un "
             "<b>verbe à l'infinitif</b>&nbsp;; aucune ellipse ne nomme une <b>pièce</b> du système&nbsp;; aucun bonhomme n'est "
             "la <b>nature</b> ou une <b>donnée</b>. <b>Coche les erreurs</b> du diagramme de Noah, puis <b>corrige-en deux</b>.</p>",
    critere="huit lignes justes (cinq erreurs cochées, trois lignes justes laissées), « L'arrosage » réécrit avec un verbe à "
            "l'infinitif et un complément, et le bon sort pour « La pompe ».",
    widgets=[dict(type="cases", name="err", legende="Coche les erreurs du diagramme de Noah",
                  options=[("dedans", "La gardienne est dessinée à l'intérieur du cadre du système."),
                           ("prog", "Une ellipse porte « Programmer l'heure d'arrosage »."),
                           ("pompe", "Une ellipse porte « La pompe »."),
                           ("cadre", "Le cadre porte en haut le nom du système."),
                           ("arrosage", "Une ellipse porte « L'arrosage »."),
                           ("tech", "Le technicien n'est relié à aucune ellipse."),
                           ("cuve", "La gardienne est reliée à « Consulter le niveau de la cuve »."),
                           ("pluie", "La pluie est dessinée en bonhomme.")],
                  bonnes=["dedans", "pompe", "arrosage", "tech", "pluie"],
                  retours={"dedans": "Oui : un acteur est toujours en dehors du système. La gardienne se dessine hors du cadre.",
                           "pompe": "Oui : la pompe est une pièce du système, pas une action.",
                           "arrosage": "Oui : « L'arrosage » n'a pas de verbe ; on ne sait pas qui fait quoi.",
                           "tech": "Oui : un acteur sans trait ne fait rien avec le système. On le relie, ou on l'enlève.",
                           "pluie": "Oui : la pluie agit sans but. Elle a sa place dans le diagramme pieuvre, pas ici.",
                           "prog": "Ce cas est bien écrit : un verbe à l'infinitif, puis un complément.",
                           "cadre": "C'est juste : le nom du système s'écrit en haut du cadre.",
                           "cuve": "Ce trait est juste : la gardienne consulte bien le niveau de la cuve."},
                  indice="Passe les cinq règles une par une : où sont les bonshommes ? ont-ils un trait ? un but ? Les ellipses ont-elles un verbe ?"),
             dict(type="texte", name="corr", lignes=2,
                  label="Réécris « L'arrosage » en vrai cas d'utilisation&nbsp;: un verbe à l'infinitif, puis un complément.",
                  criteres=[dict(label="ta réponse commence par un verbe à l'infinitif",
                                 motifs=[r"^[\s«\"'(]*[a-z]+(er|ir|re|oir)\b"],
                                 manque="Commence par un verbe à l'infinitif : arroser, lancer, programmer…"),
                            dict(label="tu ajoutes un complément (arroser quoi ?)",
                                 motifs=["plante", "jardin", "potager", "legume", "arrosage", "fleur", r"\beau\b", "pelouse",
                                         "massif", "semis", "parcelle", "bac"],
                                 manque="Ajoute un complément : arroser QUOI ?")],
                  etayage=["Un verbe à l'infinitif : …", "puis ce qu'on arrose : les …"],
                  exemple="Arroser les plantes du potager"),
             dict(type="choix", name="pompe", legende="Et « La pompe »&nbsp;: que faut-il en faire&nbsp;?",
                  options=[("bonhomme", "La dessiner en bonhomme hors du cadre, puisqu'elle agit sur l'eau."),
                           ("verbe", "Écrire « Pomper l'eau »&nbsp;: avec un verbe, c'est un vrai cas d'utilisation."),
                           ("retirer", "La retirer&nbsp;: c'est une pièce, sa place est dans la chaîne d'énergie."),
                           ("garder", "La garder telle quelle&nbsp;: c'est la pièce la plus importante du système.")],
                  bonne="retirer",
                  retours={"retirer": "Oui : la pompe est un constituant. Elle apparaîtra quand on décrira comment le système marche (la chaîne d'énergie).",
                           "bonhomme": "La pompe est dans le système, et elle n'a pas de but : ce n'est pas un acteur.",
                           "verbe": "« Pomper l'eau », c'est ce que fait la pièce, à l'intérieur. La gardienne, elle, veut que ses plantes soient arrosées.",
                           "garder": "L'importance d'une pièce ne compte pas : ce diagramme regarde le système du dehors, sans ses pièces."})],
    aides=["<p>Passe les cinq règles une par une sur le dessin&nbsp;: d'abord les bonshommes (où sont-ils&nbsp;? ont-ils un "
           "trait&nbsp;? ont-ils un but&nbsp;?), puis les ellipses (un verbe&nbsp;? une pièce&nbsp;?).</p>",
           "<p>La gardienne → dans le cadre → <b>erreur</b>&nbsp;: un acteur est dehors.<br>"
           "Le technicien → aucun trait → <b>erreur</b>.<br>"
           "La pluie → un bonhomme, mais sans but → <b>erreur</b>.<br>"
           "« La pompe » → une pièce → <b>erreur</b>.<br>"
           "« L'arrosage » → pas de verbe → <b>erreur</b> → on le réécrit&nbsp;: « Arroser les plantes ».<br>"
           "« Programmer l'heure d'arrosage » → un verbe à l'infinitif + un complément → juste.</p>"],
    jumeau=dict(consigne="Dans le diagramme d'un lampadaire, on lit une ellipse « L'allumage » et un bonhomme « la nuit ». "
                         "Quelles erreurs&nbsp;? Corrige l'ellipse.",
                correction="« L'allumage » → pas de verbe → à réécrire, par exemple « Régler les heures d'allumage » (pour "
                           "l'agent de la mairie). « La nuit » → elle agit sans but, ce n'est pas un acteur → on retire le "
                           "bonhomme&nbsp;; la nuit reste un interacteur (l'environnement)."),
    correction=[
        "<b>Erreur 1</b> → la gardienne est dans le cadre → un acteur est toujours <b>en dehors</b> du système → la dessiner "
        "hors du cadre",
        "<b>Erreur 2</b> → « La pompe » dans une ellipse → c'est une <b>pièce</b> du système → la retirer",
        "<b>Erreur 3</b> → « L'arrosage » → <b>pas de verbe</b> → réécrire&nbsp;: « Arroser les plantes » ou « Lancer un arrosage »",
        "<b>Erreur 4</b> → le technicien n'a <b>aucun trait</b> → le relier à un cas (par exemple « Entretenir le système ») ou "
        "le retirer",
        "<b>Erreur 5</b> → la pluie en bonhomme → elle agit <b>sans but</b> → la retirer&nbsp;; elle reste dans le diagramme "
        "pieuvre et dans les exigences (« résister à la pluie »)",
        "<b>Justes, à ne pas cocher&nbsp;:</b> « Programmer l'heure d'arrosage » (verbe + complément)&nbsp;; le nom du système en "
        "haut du cadre&nbsp;; le trait entre la gardienne et « Consulter le niveau de la cuve ».",
        "<b>Une réécriture attendue&nbsp;:</b> « <b>Arroser</b> les plantes du potager » — un verbe à l'infinitif, puis un complément.",
        "<b>La pompe</b> → à retirer&nbsp;: c'est une pièce, qui aura sa place dans la chaîne d'énergie. « Pomper l'eau » serait ce "
        "que fait la pompe à l'intérieur, pas ce que la gardienne fait avec le système&nbsp;; et une pièce n'a ni but ni place "
        "hors du cadre.",
        ("conclusion", "Cinq règles suffisent à vérifier un diagramme&nbsp;: des acteurs <b>dehors</b>, <b>reliés</b>, <b>avec un "
                       "but</b>&nbsp;; des ellipses avec un <b>verbe</b>, jamais une <b>pièce</b>."),
    ],
    retenir="pour vérifier un diagramme de cas d'utilisation&nbsp;: des acteurs <b>hors du cadre</b>, chacun avec <b>un trait</b> "
            "et <b>un but</b>&nbsp;; des ellipses avec un <b>verbe à l'infinitif</b>, jamais une pièce.",
    piege="donner un verbe à une pièce (« Pomper l'eau »)&nbsp;: c'est ce que fait la pièce, dedans, pas ce que l'acteur fait "
          "avec le système.",
)

# ─────────────────────────────────────────────────────────────────────────────
# 3e — CHOISIR le mode, puis CONSTRUIRE (3e_C2.1)
# ─────────────────────────────────────────────────────────────────────────────
E6 = dict(
    id="e6", titre="Choisir le mode de représentation selon la question", code="3e_C2.1", duree=13,
    objectif="choisir, pour chaque question sur l'expérience des usagers, le mode de représentation qui y répond, et dire ce "
             "que le diagramme de cas d'utilisation ne montre pas.",
    production="six questions associées à leur mode, les deux modes de l'ordre des actions, et une justification écrite.",
    mots=[("mode de représentation", "une façon de montrer une information&nbsp;: un diagramme, un algorigramme, une suite "
           "d'images, un graphique…"),
          ("algorigramme", "un schéma d'ovales, de rectangles et de losanges reliés par des flèches, qui montre l'ordre des "
           "actions et les tests (si… alors…)."),
          ("test", "dans un algorigramme, une question à deux réponses, oui ou non&nbsp;: « la carte est-elle acceptée&nbsp;? ». "
           "Il se dessine dans un losange."),
          ("storyboard", "mot anglais du cinéma&nbsp;: une suite d'images, comme une bande dessinée, qui montre ce qui se passe "
           "étape par étape."),
          ("graphique", "des barres, des points ou des courbes qui comparent des quantités d'un coup d'œil."),
          ("diagramme des interacteurs", "le schéma qui place l'objet au centre et, autour, tout ce qui est en relation avec "
           "lui&nbsp;; on l'appelle aussi diagramme pieuvre."),
          ("SysML", "<i>Systems Modeling Language</i>&nbsp;: le langage de modélisation des systèmes, dont fait partie le "
           "diagramme de cas d'utilisation.")],
    intro="<p>La mairie veut améliorer la borne de la station de vélos du front de mer. Avant de dessiner quoi que ce soit, "
          "l'équipe écrit six questions sur l'expérience des usagers. Pour chacune, un <b>mode de représentation</b> répond "
          "mieux que les autres.</p>",
    consigne="<p>Un <b>mode de représentation</b> est une façon de montrer une information&nbsp;: un diagramme, un "
             "algorigramme, une suite d'images, un graphique… <b>Pour chaque question, choisis le mode qui y répond le "
             "mieux</b>&nbsp;: la raison est écrite à côté de chaque mode. Puis <b>coche</b> les deux modes qui montrent dans "
             "quel ordre l'usager agit, et <b>explique</b> pourquoi le diagramme de cas d'utilisation ne suffit pas pour la "
             "question 3.</p>",
    critere="six choix justes, les deux bons modes cochés (et seulement eux), et une explication qui parle de l'ordre et du test.",
    widgets=[dict(type="classer", name="mode",
                  categories=[("cu", "le diagramme de cas d'utilisation — il montre qui fait quoi avec le système"),
                              ("algo", "l'algorigramme — il montre l'ordre des actions et les tests « si… alors… »"),
                              ("story", "le storyboard — une suite d'images qui montre ce que vit l'usager, étape par étape"),
                              ("graph", "le graphique — il compare des quantités d'un coup d'œil"),
                              ("pieuvre", "le diagramme des interacteurs (pieuvre) — il montre tout ce qui entoure l'objet")],
                  items=[("Question 1 — « Qui se sert de la borne, et pour faire quoi&nbsp;: l'usager, le technicien, la banque&nbsp;? »",
                          "cu", "Question 1 : « qui » et « pour faire quoi » : quel diagramme répond exactement à ces deux mots ?"),
                         ("Question 2 — « Combien d'usagers abandonnent avant d'avoir leur vélo, chaque jour de la semaine&nbsp;? »",
                          "graph", "Question 2 : « combien », jour par jour : on compare des quantités."),
                         ("Question 3 — « Si la carte est refusée, la borne la redemande-t-elle, ou rend-elle la main&nbsp;? »",
                          "algo", "Question 3 : « si… » : il y a un test, avec deux suites possibles."),
                         ("Question 4 — « Comment montrer à un touriste qui ne lit pas le français comment louer un vélo&nbsp;? »",
                          "story", "Question 4 : sans lire de texte : il faut des images, étape par étape."),
                         ("Question 5 — « Qu'est-ce qui, autour de la borne, peut l'abîmer&nbsp;: la pluie, le soleil, l'air salé&nbsp;? »",
                          "pieuvre", "Question 5 : « autour de la borne » : tout ce qui l'entoure, même sans but."),
                         ("Question 6 — « Le technicien et l'usager ont-ils une action en commun avec la borne&nbsp;? »",
                          "cu", "Question 6 : des personnes et leurs actions avec la borne : qui fait quoi.")]),
             dict(type="cases", name="ordre",
                  legende="« Dans quel ordre l'usager agit-il pour louer un vélo&nbsp;? » Deux modes y répondent. Lesquels&nbsp;?",
                  options=[("algo", "l'algorigramme"), ("cu", "le diagramme de cas d'utilisation"), ("story", "le storyboard"),
                           ("graph", "le graphique")],
                  bonnes=["algo", "story"],
                  retours={"algo": "Oui : ses flèches donnent l'ordre des actions, et ses losanges les tests.",
                           "story": "Oui : ses images se suivent, étape par étape, comme ce que vit l'usager.",
                           "cu": "Non : ses ellipses ne sont pas rangées dans l'ordre ; il dit qui fait quoi, pas quand.",
                           "graph": "Non : un graphique compare des quantités ; il ne raconte pas un déroulement."},
                  indice="Lequel montre des flèches d'une étape à l'autre ? Lequel montre des images qui se suivent ?"),
             dict(type="texte", name="justif", lignes=3,
                  label="Explique pourquoi le diagramme de cas d'utilisation ne suffit pas pour répondre à la question 3 (la "
                        "carte refusée).",
                  criteres=[dict(label="tu dis ce que ce diagramme ne montre pas (l'ordre, les étapes)",
                                 motifs=["ordre", "etape", "suite", "apres", "avant", "deroulement", "enchainement", "chronolog"],
                                 manque="Dis ce que le diagramme de cas d'utilisation ne montre PAS : l'ordre ? les étapes ?"),
                            dict(label="tu parles du test : ce qui se passe si la carte est refusée",
                                 motifs=["test", "condition", r"\bsi\b", "refus", "echec", "losange", "decision"],
                                 manque="Parle du test : « si la carte est refusée… ». Quel mode montre les tests ?")],
                  etayage=["Le diagramme de cas d'utilisation montre …, mais il ne montre pas …",
                           "Pour la carte refusée, il faut un test : « si … alors … », que seul … montre."],
                  exemple="Le diagramme de cas d'utilisation dit qui fait quoi, mais il ne montre ni l'ordre des étapes ni le "
                          "test « si la carte est refusée » : c'est l'algorigramme qui le montre.")],
    aides=["<p>Dans chaque question, repère le <b>mot qui commande</b>&nbsp;: « qui… pour faire quoi », « combien », « si… », "
           "« sans lire », « autour ». Chacun appelle un mode.</p>",
           "<p>« Qui… pour faire quoi » → <b>diagramme de cas d'utilisation</b>.<br>"
           "« Combien… chaque jour » → <b>graphique</b>.<br>"
           "« Si la carte est refusée » → un test → <b>algorigramme</b>.<br>"
           "« Qui ne lit pas le français » → des images → <b>storyboard</b>.<br>"
           "« Autour de la borne » → <b>diagramme des interacteurs</b>.<br>"
           "Le diagramme de cas d'utilisation montre les actions, mais <b>pas leur ordre</b> ni les tests.</p>"],
    jumeau=dict(consigne="Pour la station d'alerte cyclonique&nbsp;: « Combien d'alertes ont été déclenchées chaque mois de la "
                         "saison&nbsp;? » et « Qui reçoit l'alerte, et qui la déclenche&nbsp;? ». Quel mode pour chaque question&nbsp;?",
                correction="Le nombre d'alertes par mois → des quantités à comparer → <b>un graphique</b>. Qui reçoit, qui "
                           "déclenche → qui fait quoi avec la station → <b>le diagramme de cas d'utilisation</b>."),
    correction=[
        "<b>Question 1</b> → « qui… pour faire quoi » → <b>le diagramme de cas d'utilisation</b>",
        "<b>Question 2</b> → « combien… chaque jour » → <b>le graphique</b> (des barres, une par jour)",
        "<b>Question 3</b> → « si la carte est refusée » → un test et deux suites → <b>l'algorigramme</b>",
        "<b>Question 4</b> → un touriste qui ne lit pas le français → des images → <b>le storyboard</b>",
        "<b>Question 5</b> → tout ce qui entoure la borne, même sans but → <b>le diagramme des interacteurs</b> (pieuvre)",
        "<b>Question 6</b> → une action commune à deux acteurs → <b>le diagramme de cas d'utilisation</b> (une ellipse reliée "
        "à deux bonshommes)",
        "<b>L'ordre des actions</b> → <b>l'algorigramme</b> (flèches et tests) <b>et le storyboard</b> (images qui se suivent)&nbsp;; "
        "ni le diagramme de cas d'utilisation (aucun ordre) ni le graphique (des quantités).",
        "<b>Une justification attendue&nbsp;:</b> « Le diagramme de cas d'utilisation dit <b>qui fait quoi</b>, mais il ne montre "
        "ni <b>l'ordre</b> des étapes ni le <b>test</b> « si la carte est refusée »&nbsp;: c'est l'algorigramme qui le montre. »",
        ("conclusion", "Un mode n'est pas bon en soi&nbsp;: il est bon <b>pour une question</b>. Le diagramme de cas "
                       "d'utilisation répond à « qui fait quoi » — pas à « dans quel ordre », ni à « combien »."),
    ],
    retenir="on choisit un mode d'après <b>la question</b>&nbsp;: qui fait quoi → <b>cas d'utilisation</b>&nbsp;; dans quel "
            "ordre, si… → <b>algorigramme</b>&nbsp;; ce que vit l'usager, en images → <b>storyboard</b>&nbsp;; combien → "
            "<b>graphique</b>&nbsp;; ce qui entoure → <b>diagramme des interacteurs</b>.",
    piege="lire les ellipses d'un diagramme de cas d'utilisation de haut en bas comme une suite d'étapes&nbsp;: il ne montre "
          "aucun ordre.",
)

ACTEURS_E7 = ["l'agent municipal", "l'habitant", "le service météo", "le vent", "l'anémomètre"]
CAS_E7 = ["Déclencher une alerte", "Tester la sirène", "La sirène", "Le cyclone"]

E7 = dict(
    id="e7", titre="Construire le diagramme de la station d'alerte cyclonique", code="3e_C2.1", duree=18,
    objectif="construire, à partir d'un texte, le diagramme de cas d'utilisation d'un système, et justifier qu'un autre "
             "système est un acteur.",
    production="le diagramme complété (trois acteurs, deux cas d'utilisation), une justification écrite, et la place du vent.",
    mots=[("anémomètre", "l'appareil qui mesure la vitesse du vent&nbsp;: ses coupelles tournent d'autant plus vite que le vent "
           "souffle fort."),
          ("gyrophare", "une lampe qui tourne et clignote, pour qu'on la voie de loin."),
          ("service météo", "l'organisme qui observe le temps et prévoit les cyclones&nbsp;; ses ordinateurs envoient des bulletins."),
          ("bulletin météo", "un message qui annonce le temps à venir&nbsp;: la route d'un cyclone, la force du vent attendue."),
          ("agent municipal", "une personne qui travaille pour la commune, à la mairie."),
          ("acteur", "une personne, ou un autre système, en dehors du système, qui s'en sert avec un but&nbsp;; dessiné en bonhomme.")],
    intro="<p>La commune de Sainte-Luce a une <b>station d'alerte cyclonique</b> (imaginée pour l'exercice)&nbsp;: un mât avec un "
          "anémomètre, une sirène et un gyrophare, relié à la mairie. Voici sa description, écrite par la mairie&nbsp;:</p>"
          "<blockquote><p>« Le <b>service météo</b> envoie ses bulletins à la station. Quand un cyclone approche, l'<b>agent "
          "municipal</b> de permanence déclenche l'alerte depuis la mairie. Les <b>habitants</b> reçoivent alors l'alerte&nbsp;: "
          "la sirène sonne, le gyrophare tourne, un message arrive sur leur téléphone. Chaque matin, le <b>technicien</b> teste "
          "la sirène. Pendant la tempête, le vent fait tourner l'anémomètre. »</p></blockquote>",
    consigne="<p>Un <b>acteur</b> est une personne, ou un autre système, hors du cadre, qui se sert de la station avec un "
             "but&nbsp;; un <b>cas d'utilisation</b> est une action faite avec elle, écrite avec un verbe à l'infinitif. "
             "<b>Construis le diagramme de cas d'utilisation de la station</b>&nbsp;: place les trois acteurs et les deux cas "
             "qui manquent (les mots en gras du texte t'aident). Puis <b>explique</b> pourquoi le service météo est un acteur "
             "alors que ce n'est pas une personne, et <b>dis</b> où va le vent.</p>",
    critere="les cinq cases justes, une justification qui dit « autre système », « en dehors » et ce qu'il envoie, et la bonne "
            "place pour le vent.",
    widgets=[dict(type="slots", intro='<figure class="figure schema-vivant">' + FIG_CYCLONE +
                  "<figcaption>Le diagramme de cas d'utilisation de la station, à construire. Tes choix s'écrivent dans les "
                  "ellipses en pointillés et sous les bonshommes vides (…).</figcaption></figure>",
                  slots=[dict(name="a5", cible="cu-a5", legende="Le bonhomme du haut, à gauche — relié à l'ellipse vide du haut",
                              options=ACTEURS_E7, bonnes=["l'agent municipal"],
                              indice="Le bonhomme du haut, à gauche : qui, dans le texte, déclenche l'alerte ?"),
                         dict(name="c3", cible="cu-c3", legende="L'ellipse vide du haut — reliée au bonhomme du haut, à gauche",
                              options=CAS_E7, bonnes=["Déclencher une alerte"],
                              indice="L'ellipse vide du haut : ce que fait l'agent municipal, avec un verbe à l'infinitif."),
                         dict(name="a6", cible="cu-a6", legende="Le bonhomme du haut, à droite — relié à « Recevoir une alerte »",
                              options=ACTEURS_E7, bonnes=["l'habitant"],
                              indice="Le bonhomme du haut, à droite : qui reçoit l'alerte, d'après le texte ?"),
                         dict(name="c4", cible="cu-c4", legende="L'ellipse vide du bas — reliée au technicien",
                              options=CAS_E7, bonnes=["Tester la sirène"],
                              indice="L'ellipse vide du bas : que fait le technicien chaque matin ? « La sirène » seule n'a pas de verbe."),
                         dict(name="a7", cible="cu-a7", legende="Le bonhomme du bas, à droite — relié à « Envoyer un bulletin météo »",
                              options=ACTEURS_E7, bonnes=["le service météo"],
                              indice="Le bonhomme du bas, à droite : qui envoie les bulletins ? Ce n'est pas une personne.")]),
             dict(type="texte", name="meteo", lignes=3,
                  label="Pourquoi le service météo est-il un acteur de la station, alors que ce n'est pas une personne&nbsp;?",
                  criteres=[dict(label="tu dis que c'est un autre système",
                                 motifs=["autre systeme", "un systeme", "est un systeme", "ordinateur", "serveur", "organisme",
                                         "machine", "logiciel"],
                                 manque="Dis ce QU'EST le service météo pour la station : une personne ? un autre système ?"),
                            dict(label="tu dis qu'il est en dehors de la station",
                                 motifs=["dehors", "exterieur", "hors de", "ailleurs", "loin", "pas dans la station", "n'est pas dans"],
                                 manque="Dis OÙ il est : dans la station, ou en dehors ?"),
                            dict(label="tu dis ce qu'il fait avec elle, avec un but (il envoie les bulletins)",
                                 motifs=["envoi", "transmet", "echange", "communique", "informe", "previent", "donne", r"\bbut\b"],
                                 manque="Dis ce qu'il FAIT avec la station : que lui envoie-t-il, et pourquoi ?")],
                  etayage=["Le service météo n'est pas une personne, mais c'est un autre …",
                           "Il est … de la station, et il lui … ses bulletins : il agit avec un but."],
                  exemple="Le service météo est un autre système, en dehors de la station : il lui envoie ses bulletins, avec un "
                          "but. C'est donc un acteur, même si ce n'est pas une personne."),
             dict(type="choix", name="vent", legende="Et le vent, qui fait tourner l'anémomètre&nbsp;: où va-t-il&nbsp;?",
                  options=[("acteur", "Sous un bonhomme&nbsp;: il agit sur la station, donc c'est un acteur."),
                           ("ellipse", "Dans une ellipse « Le vent », puisque la station le mesure."),
                           ("rien", "Nulle part&nbsp;: ce que la station mesure n'intéresse pas le concepteur."),
                           ("pieuvre", "Dans le diagramme pieuvre et les exigences&nbsp;: il agit sans but.")],
                  bonne="pieuvre",
                  retours={"pieuvre": "Oui : le vent est un interacteur (l'environnement). Il entre dans les exigences : « résister au vent d'un cyclone ».",
                           "acteur": "Agir sur la station ne suffit pas : un acteur s'en sert avec un but. Le vent souffle, c'est tout.",
                           "ellipse": "« Le vent » n'a pas de verbe, et ce n'est pas une action faite avec la station.",
                           "rien": "Au contraire : le concepteur doit en tenir compte, dans les exigences (résister au vent, le mesurer)."})],
    aides=["<p>Relis le texte et souligne deux sortes de mots&nbsp;: <b>ceux qui agissent avec un but</b> (des personnes ou des "
           "systèmes) → les acteurs&nbsp;; <b>les verbes de ce qu'ils font avec la station</b> → les cas d'utilisation. Puis suis "
           "les traits du schéma pour savoir quelle case attend quoi.</p>",
           "<p>« L'agent municipal déclenche l'alerte » → un acteur, <b>l'agent municipal</b>, et un cas, <b>Déclencher une "
           "alerte</b> → en haut à gauche.<br>"
           "« Les habitants reçoivent l'alerte » → <b>l'habitant</b>, relié à « Recevoir une alerte ».<br>"
           "« Le technicien teste la sirène » → <b>Tester la sirène</b>.<br>"
           "« Le service météo envoie ses bulletins » → un autre système → <b>le service météo</b>.<br>"
           "Le vent → il fait tourner l'anémomètre, sans but → pas de bonhomme.<br>"
           "L'anémomètre, la sirène → des pièces → ni acteur, ni cas.</p>"],
    jumeau=dict(consigne="« Le portail du collège s'ouvre quand le gardien appuie sur sa télécommande&nbsp;; le soir, le "
                         "logiciel de la vie scolaire commande sa fermeture&nbsp;; un capteur arrête le portail si une voiture est "
                         "dans le passage. » Fais la liste des acteurs et des cas d'utilisation.",
                correction="Acteurs&nbsp;: <b>le gardien</b> (« Ouvrir le portail ») et <b>le logiciel de la vie scolaire</b>, un "
                           "autre système (« Commander la fermeture du soir »). Pas acteurs&nbsp;: <b>le capteur</b> (une pièce du "
                           "portail) et <b>la voiture</b> (un obstacle, sans but&nbsp;: elle donne une exigence de sécurité, "
                           "« s'arrêter devant un obstacle »)."),
    correction=[
        '<figure class="figure">' + FIG_CYCLONE_C + "<figcaption>Le diagramme corrigé de la station d'alerte cyclonique.</figcaption></figure>",
        "<b>En haut à gauche</b> → « l'agent municipal déclenche l'alerte » → <b>l'agent municipal</b>, relié à <b>Déclencher "
        "une alerte</b>",
        "<b>En haut à droite</b> → « les habitants reçoivent l'alerte » → <b>l'habitant</b>, relié à « Recevoir une alerte »",
        "<b>L'ellipse vide du bas</b> → « le technicien teste la sirène » → <b>Tester la sirène</b>",
        "<b>En bas à droite</b> → « le service météo envoie ses bulletins » → <b>le service météo</b>, relié à « Envoyer un "
        "bulletin météo »",
        "<b>Refusés&nbsp;:</b> le vent → il agit sans but&nbsp;; l'anémomètre et « La sirène » → des pièces de la station&nbsp;; "
        "« Le cyclone » → pas de verbe, et c'est un phénomène, pas une action.",
        "<b>Une justification attendue&nbsp;:</b> « Le service météo est un <b>autre système</b>, <b>en dehors</b> de la "
        "station&nbsp;: il lui <b>envoie ses bulletins</b>, avec un but. C'est donc un acteur, même s'il n'est pas une personne. »",
        "<b>Le vent</b> → dans le diagramme des interacteurs et dans les exigences (« résister au vent d'un cyclone ») → il agit "
        "sans but&nbsp;: pas un acteur",
        "Les autres réponses ne tiennent pas&nbsp;: agir sur la station ne suffit pas (il faut un but)&nbsp;; « Le vent » n'a pas "
        "de verbe&nbsp;; le concepteur doit tenir compte du vent, dans les exigences.",
        ("conclusion", "Construire, c'est trier le texte&nbsp;: <b>qui agit avec un but</b> → un bonhomme&nbsp;; <b>ce qu'il "
                       "fait</b> → une ellipse&nbsp;; <b>le reste</b> (la nature, les pièces) → ailleurs."),
    ],
    retenir="un <b>autre système</b> (un service météo, le serveur d'une banque) peut être un acteur&nbsp;: il est dehors et il "
            "échange avec le système avec un but. Le vent, lui, reste un interacteur.",
    piege="dessiner le vent en bonhomme parce que la station le mesure&nbsp;: être mesuré n'est pas se servir du système.",
)

# ─────────────────────────────────────────────────────────────────────────────
# Les trois niveaux
# ─────────────────────────────────────────────────────────────────────────────
NIVEAUX = {
    "5e": dict(
        codes=["5e_C2.1"],
        mission="Reconnaître, parmi tout ce qui entoure un système, ceux qui s'en servent — et pour faire quoi.",
        avant=[("Je sais dire si un élément est une pièce d'un objet, ou s'il est en dehors de lui.",
                "cycle 3 — sciences et technologie", "@synthese#les-mots", "les mots de l'atelier, dans la synthèse (2 minutes)"),
               ("Je sais dire avec un verbe ce que l'on fait avec un objet&nbsp;: rouler, éclairer, ranger.",
                "cycle 3 — sciences et technologie", "@synthese#les-mots", "les mots de l'atelier, dans la synthèse (2 minutes)")],
        situation_titre="Deux noms pour un même schéma",
        situation="<p>Pour décrire un système, on peut se demander <b>qui s'en sert, et pour faire quoi</b>. Le schéma qui "
                  "répond s'appelle le <b>diagramme de cas d'utilisation</b>. Les ingénieurs l'appellent souvent par son nom "
                  "anglais, le <b>use case</b>&nbsp;: il vient du langage <b>SysML</b> (<i>Systems Modeling Language</i>, le "
                  "langage de modélisation des systèmes), une façon commune de dessiner les systèmes.</p>"
                  "<p>Il ressemble un peu au diagramme pieuvre, mais il ne garde que les <b>acteurs</b>&nbsp;: ceux qui se "
                  "servent du système avec un but. Dans cet atelier, le système est une <b>station de vélos en "
                  "libre-service</b>, puis un <b>lampadaire solaire</b>.</p>",
        question="Parmi tout ce qui entoure un système, comment reconnaître ceux qui s'en servent vraiment&nbsp;?",
        hypothese_amorces=["Je pense que ceux qui se servent d'un système sont…", "La pluie, à mon avis, …",
                           "Pour savoir si quelqu'un se sert du système, je regarderais…"],
        exercices=[E1, E2],
        a_retenir="<ul><li>Le <b>diagramme de cas d'utilisation</b> — le <b>use case</b> du langage SysML — dit <b>qui se sert "
                  "du système, et pour faire quoi</b>.</li>"
                  "<li>Il a quatre éléments&nbsp;: la <b>frontière du système</b> (le cadre), les <b>acteurs</b> (les "
                  "bonshommes, dehors), les <b>cas d'utilisation</b> (les ellipses, une action avec un verbe à l'infinitif) et "
                  "les <b>associations</b> (les traits).</li>"
                  "<li>Un <b>acteur</b> est une personne ou un autre système, <b>en dehors</b> du système, qui s'en sert <b>avec "
                  "un but</b>.</li>"
                  "<li>La pluie, le soleil, une donnée, un objet prêté ou une pièce ne sont pas des acteurs&nbsp;: ce sont des "
                  "interacteurs, ou des constituants.</li></ul>",
        bonus=[dict(titre="Le vélo-cargo de Léa",
                    consigne="<p>Léa se sert de son vélo-cargo pour transporter ses enfants et ses courses&nbsp;; un réparateur "
                             "change ses freins chaque année. Écris <b>deux acteurs</b> et <b>un cas d'utilisation</b> pour "
                             "chacun. La pluie est-elle un acteur&nbsp;?</p>",
                    correction=["<b>Léa</b> → « Transporter ses enfants », « Transporter ses courses »",
                                "<b>Le réparateur</b> → « Changer les freins »",
                                "<b>La pluie</b> → elle mouille le vélo-cargo sans but → pas un acteur&nbsp;: un interacteur de "
                                "l'environnement",
                                "<b>Les enfants et les courses</b> → ils sont transportés, ils ne commandent rien au vélo-cargo "
                                "→ pas des acteurs&nbsp;: on les retrouve dans le complément d'un cas",
                                ("conclusion", "Être nommé dans une ellipse n'est pas être un acteur&nbsp;: l'acteur est celui "
                                               "qui agit avec un but.")]),
               dict(titre="La borne de la cantine",
                    consigne="<p>À la cantine, une borne permet à l'élève de réserver son repas&nbsp;; la gestionnaire y "
                             "consulte le nombre de repas réservés&nbsp;; chaque matin, le logiciel de la vie scolaire lui "
                             "envoie la liste des élèves absents. <b>Fais la liste des acteurs</b>. Le plateau en est-il un&nbsp;?</p>",
                    correction=["<b>L'élève</b> → une personne → « Réserver son repas »",
                                "<b>La gestionnaire</b> → une personne → « Consulter le nombre de repas »",
                                "<b>Le logiciel de la vie scolaire</b> → un autre système → « Envoyer la liste des absents »",
                                "<b>Le plateau</b> → un objet, il ne demande rien → pas un acteur",
                                ("conclusion", "Trois acteurs, dont un qui n'est pas une personne.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre un acteur et un interacteur sans but, ou devant un autre système "
                      "qui n'est pas une personne. Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
    "4e": dict(
        codes=["4e_C2.1"],
        mission="Passer de ce que racontent les usagers à un schéma clair&nbsp;: qui fait quoi avec le système.",
        avant=[("Je sais ranger les interacteurs extérieurs d'un objet en quatre familles&nbsp;: usagers, données, autres objets, "
                "éléments de l'environnement.", "5e_C2.1", "@atelier:interacteurs:5e#pv_5e_e2",
                "l'atelier du diagramme pieuvre, 5e, exercice 2 (7 minutes)"),
               ("Je sais reconnaître un acteur&nbsp;: une personne ou un autre système, en dehors du système, qui s'en sert avec "
                "un but.", "5e_C2.1", "@niveau:5e#cu_5e_e1", "l'atelier de 5e, exercice 1 (15 minutes)")],
        situation_titre="Des phrases au schéma",
        situation="<p>En 4e, on décrit l'expérience de l'utilisateur en partant de ses mots&nbsp;: ce qu'il raconte, ce qu'il "
                  "ressent. Pour passer de ces phrases à un schéma, un outil aide beaucoup&nbsp;: le <b>diagramme de cas "
                  "d'utilisation</b>, souvent appelé <b>use case SysML</b> (SysML&nbsp;: <i>Systems Modeling Language</i>, le "
                  "langage de modélisation des systèmes). Il garde de chaque phrase l'<b>action</b>&nbsp;: qui fait quoi avec le "
                  "système.</p>"
                  "<p>Dans cet atelier, le système est la <b>borne d'une station de vélos</b> en libre-service, puis le "
                  "<b>système d'arrosage</b> du jardin partagé du collège.</p>",
        question="Comment passer de ce que disent les usagers à un schéma clair, sans rien perdre et sans rien inventer&nbsp;?",
        hypothese_amorces=["Je pense que dans chaque phrase, il faut chercher…", "Ce que l'usager ressent, à mon avis, …",
                           "Un schéma bien fait, c'est un schéma où…"],
        exercices=[E3, E4, E5],
        a_retenir="<ul><li>Pour passer du <b>langage naturel</b> au schéma, on cherche dans chaque phrase <b>l'action</b> faite "
                  "avec le système et on l'écrit <b>verbe à l'infinitif + complément</b>.</li>"
                  "<li>Le <b>ressenti</b> ne se dessine pas dans le diagramme&nbsp;: on le garde à côté, pour une exigence, un "
                  "tableau ou un graphique.</li>"
                  "<li>Une ellipse contient une <b>action</b>&nbsp;; un bonhomme, <b>quelqu'un ou un autre système</b> qui se sert "
                  "du système. Une pièce n'est ni l'un ni l'autre.</li>"
                  "<li>Pour vérifier un diagramme&nbsp;: des acteurs <b>hors du cadre</b>, chacun avec <b>un trait</b> et <b>un "
                  "but</b>&nbsp;; des ellipses avec un <b>verbe</b>, jamais une pièce.</li></ul>",
        bonus=[dict(titre="Le verbatim qui manque",
                    consigne="<p>Une usagère raconte&nbsp;: « La veille, j'ai réservé un vélo sur l'écran de la borne, pour être "
                             "sûre d'en avoir un le matin. » Faut-il ajouter une ellipse au diagramme de la borne&nbsp;? Un "
                             "bonhomme&nbsp;?</p>",
                    correction=["<b>Une ellipse</b> → oui&nbsp;: « Réserver un vélo », une action qui n'était pas encore dans le "
                                "diagramme",
                                "<b>Un bonhomme</b> → non&nbsp;: c'est l'usager, déjà dessiné&nbsp;; on le relie à la nouvelle ellipse",
                                ("conclusion", "Un nouveau verbatim peut ajouter une action sans ajouter d'acteur.")]),
               dict(titre="Du ressenti à l'exigence",
                    consigne="<p>Tom trouvait l'écran illisible en plein soleil. Écris une <b>exigence</b> qui répond à son "
                             "ressenti, et dis si le diagramme de cas d'utilisation change.</p>",
                    correction=["<b>Exigence</b> → « L'écran de la borne doit rester lisible en plein soleil »",
                                "<b>Pour la vérifier</b> → mesurer le temps qu'il faut pour lire le code, écran au soleil",
                                "<b>Le diagramme</b> → il ne change pas&nbsp;: « Payer la location » reste la même action",
                                ("conclusion", "Le diagramme garde l'action&nbsp;; le ressenti devient une exigence, qui dit ce "
                                               "qu'il faut obtenir.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre une action et un ressenti, ou entre une pièce et un cas "
                      "d'utilisation. Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
    "3e": dict(
        codes=["3e_C2.1"],
        mission="Choisir le mode de représentation qui répond à chaque question, puis construire le diagramme de cas "
                "d'utilisation d'un système.",
        avant=[("Je sais passer de ce que disent les usagers aux cas d'utilisation d'un système.",
                "4e_C2.1", "@niveau:4e#cu_4e_e3", "l'atelier de 4e, exercice 1 (10 minutes)"),
               ("Je sais vérifier un diagramme de cas d'utilisation&nbsp;: acteurs hors du cadre, ellipses avec un verbe.",
                "4e_C2.1", "@niveau:4e#cu_4e_e5", "l'atelier de 4e, exercice 3 (12 minutes)")],
        situation_titre="Un mode pour chaque question",
        situation="<p>Pour décrire l'expérience de l'utilisateur, tu as plusieurs modes de représentation&nbsp;: un "
                  "algorigramme, un graphique, un storyboard, un diagramme… Aucun n'est bon en soi&nbsp;: chacun répond à une "
                  "question. Le <b>diagramme de cas d'utilisation</b> — le <b>use case SysML</b> (SysML&nbsp;: <i>Systems "
                  "Modeling Language</i>, le langage de modélisation des systèmes) — répond à « qui fait quoi avec le "
                  "système&nbsp;? ».</p>"
                  "<p>Dans cet atelier, tu choisis d'abord le mode qui convient à six questions sur une borne de vélos, puis tu "
                  "construis le diagramme de la <b>station d'alerte cyclonique</b> de Sainte-Luce.</p>",
        question="Comment choisir le mode de représentation qui montre le mieux ce que l'on veut dire, et à qui&nbsp;?",
        hypothese_amorces=["Je pense qu'on choisit un mode d'après…", "Le diagramme de cas d'utilisation, à mon avis, ne montre pas…",
                           "Pour construire un diagramme à partir d'un texte, je commencerais par…"],
        exercices=[E6, E7],
        a_retenir="<ul><li>On choisit un mode de représentation d'après <b>la question</b>&nbsp;: qui fait quoi → <b>diagramme "
                  "de cas d'utilisation</b>&nbsp;; dans quel ordre, si… → <b>algorigramme</b>&nbsp;; ce que vit l'usager, en "
                  "images → <b>storyboard</b>&nbsp;; combien → <b>graphique</b>&nbsp;; ce qui entoure → <b>diagramme des "
                  "interacteurs</b>.</li>"
                  "<li>Le diagramme de cas d'utilisation ne montre <b>ni l'ordre, ni les quantités, ni le ressenti</b>.</li>"
                  "<li>Pour le construire à partir d'un texte&nbsp;: <b>qui agit avec un but</b> → un acteur&nbsp;; <b>ce qu'il "
                  "fait</b> → un cas d'utilisation&nbsp;; la nature et les pièces → ailleurs.</li>"
                  "<li>Un <b>autre système</b> (service météo, serveur de paiement) peut être un acteur&nbsp;; le vent, non.</li></ul>",
        bonus=[dict(titre="Deux destinataires, deux modes",
                    consigne="<p>Le maire veut savoir combien de fois la sirène a été testée sans panne ce mois-ci&nbsp;; un "
                             "nouvel habitant veut savoir ce qu'il doit faire quand il reçoit l'alerte. <b>Quel mode pour "
                             "chacun</b>, et pourquoi&nbsp;?</p>",
                    correction=["<b>Le maire</b> → « combien » → <b>un graphique</b>&nbsp;: les tests réussis et en panne, "
                                "semaine par semaine",
                                "<b>Le nouvel habitant</b> → ce qu'il doit faire, étape par étape, sans mode d'emploi → <b>un "
                                "storyboard</b>",
                                ("conclusion", "Même système, deux questions, deux modes&nbsp;: on choisit pour quelqu'un.")]),
               dict(titre="Un acteur de plus",
                    consigne="<p>La station prévient aussi le centre de secours des pompiers&nbsp;: son ordinateur reçoit "
                             "l'alerte en même temps que les habitants. <b>Ajoute ce qu'il faut</b> au diagramme.</p>",
                    correction=["<b>Un acteur</b> → le centre de secours, un autre système, hors du cadre",
                                "<b>Un trait</b> → vers « Recevoir une alerte »&nbsp;: l'ellipse a maintenant deux acteurs",
                                "<b>Pas de nouvelle ellipse</b> → l'action est la même",
                                ("conclusion", "Un acteur de plus ne veut pas dire un cas de plus.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre l'algorigramme et le storyboard, ou devant le service météo. "
                      "Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
}

# ─────────────────────────────────────────────────────────────────────────────
# Ce que le reste du site lit de cet atelier
# ─────────────────────────────────────────────────────────────────────────────
MODULE = "cas_utilisation"
NOM_PANNEAU = "diagramme_cas_utilisation"
PANNEAU_TEXTE = {
    "5e": "Le <b>diagramme de cas d'utilisation</b> — souvent appelé <b>use case</b> — sur une station de vélos et un "
          "lampadaire solaire&nbsp;: tu reconnais les acteurs parmi ce qui entoure le système, tu lis le diagramme et tu fais "
          "la liste de ses acteurs.",
    "4e": "Le <b>diagramme de cas d'utilisation</b> — souvent appelé <b>use case</b> — sur la borne d'une station de vélos et "
          "le système d'arrosage du jardin&nbsp;: tu passes des phrases des usagers aux cas d'utilisation, tu complètes le "
          "diagramme, puis tu repères et corriges ses erreurs.",
    "3e": "Le <b>diagramme de cas d'utilisation</b> — souvent appelé <b>use case</b> — parmi les modes de représentation&nbsp;: "
          "tu choisis le mode qui répond à chaque question, puis tu construis le diagramme de la station d'alerte cyclonique.",
}
IMAGES = {
    "station_velos_cas_utilisation_corrige.svg": FIG_STATION_C,
    "lampadaire_cas_utilisation.svg": FIG_LAMPADAIRE,
    "borne_velos_cas_utilisation_corrige.svg": FIG_BORNE_C,
    "arrosage_cas_utilisation_avec_erreurs.svg": FIG_ERREURS,
    "station_alerte_cas_utilisation_corrige.svg": FIG_CYCLONE_C,
}
ROLES_IMAGES = {
    "station_velos_cas_utilisation_corrige.svg": "corrigé de l'exercice 1 de 5e ; question illustrée du QCM",
    "lampadaire_cas_utilisation.svg": "document de l'exercice 2 de 5e ; schéma de la synthèse (5e) ; question illustrée du QCM",
    "borne_velos_cas_utilisation_corrige.svg": "corrigé de l'exercice 2 de 4e ; schéma de la synthèse (4e) ; question illustrée du QCM",
    "arrosage_cas_utilisation_avec_erreurs.svg": "document de l'exercice 3 de 4e (erreurs à repérer) ; question illustrée du QCM",
    "station_alerte_cas_utilisation_corrige.svg": "corrigé de l'exercice 2 de 3e ; schéma de la synthèse (3e) ; question illustrée du QCM",
}
VOCAB_EN = [("diagramme de cas d'utilisation", "use case diagram"), ("acteur", "actor"), ("cas d'utilisation", "use case"),
            ("frontière du système", "system boundary"), ("association", "association"), ("verbatim", "user quote (verbatim)"),
            ("ressenti", "user feeling"), ("algorigramme", "flowchart"), ("storyboard", "storyboard"),
            ("mode de représentation", "way of representing")]
VERBES = {"5e": "<b>reconnaître</b> les acteurs parmi les interacteurs, <b>lire</b> un diagramme de cas d'utilisation et "
                "<b>faire la liste</b> de ses acteurs (5e_C2.1)",
          "4e": "<b>passer</b> du langage naturel (verbatims d'usagers) au schéma, <b>compléter</b> un diagramme, puis "
                "<b>repérer et corriger</b> ses erreurs (4e_C2.1)",
          "3e": "<b>choisir</b> le mode de représentation selon la question, puis <b>construire</b> le diagramme d'un système à "
                "partir d'un texte (3e_C2.1)"}
CHAINE = ("<p><b>Analyse externe</b>&nbsp;: besoin <i>(bête à cornes)</i> → <b>qui interagit avec le système, et pour faire "
          "quoi</b>&nbsp;: les interacteurs <i>(diagramme des interacteurs, « pieuvre »)</i> et, à côté, <b>les acteurs et leurs "
          "cas d'utilisation <i>(diagramme de cas d'utilisation, use case SysML)</i></b> → contraintes et exigences "
          "<i>(diagramme des exigences)</i> → cahier des charges.</p>"
          "<p>Le diagramme pieuvre fait la liste de <b>tout</b> ce qui entoure l'objet&nbsp;; le diagramme de cas d'utilisation "
          "n'en garde que les <b>acteurs</b> — ceux qui s'en servent avec un but — et dit <b>ce qu'ils font</b> avec le "
          "système. Les deux se lisent ensemble&nbsp;: un interacteur sans but (la pluie, le vent) devient une exigence, pas un "
          "cas d'utilisation.</p>")
NOTES_PROF = ("<ul><li>Plan demandé par Pascal (24/10/2026)&nbsp;: 5e_C2.1 (reconnaître les acteurs), 4e_C2.1 (du langage "
              "naturel au schéma), 3e_C2.1 (choisir le mode, construire). Un exercice a été ajouté en 5e (lire le diagramme du "
              "lampadaire, légender ses éléments, faire la liste de ses acteurs) pour que la page de 5e atteigne 30 minutes&nbsp;: "
              "7 exercices en tout (5e&nbsp;: 2, 4e&nbsp;: 3, 3e&nbsp;: 2).</li>"
              "<li>Définition retenue&nbsp;: un acteur est une personne ou un autre système, extérieur, qui interagit avec le "
              "système dans un cas d'utilisation, avec un but. La pluie, le vent, le soleil, une donnée, un objet prêté ne sont "
              "pas des acteurs&nbsp;: ils restent des interacteurs (diagramme pieuvre) et nourrissent les exigences.</li>"
              "<li>Inspiration&nbsp;: le cahier « 123 Techno » (Bordas 2021, 3e, fiche du diagramme SysML des cas d'utilisation). "
              "Mécaniques reprises, transposées à nos objets&nbsp;: légender les éléments du diagramme (5e, exercice 2)&nbsp;; "
              "extraire acteurs et cas d'un court texte de description (3e, exercice 2)&nbsp;; « lesquels sont des acteurs&nbsp;? » "
              "(5e, exercice 1)&nbsp;; et, du cahier de 5e (fiche croquis, schéma, algorithme), le tableau « pour chaque cas, "
              "choisir le mode de représentation », élargi ici aux modes de 3e (3e, exercice 1). Aucun énoncé, aucune image "
              "ni tournure de l'éditeur n'est repris.</li>"
              "<li>Divergence assumée avec ce cahier&nbsp;: il dessine des phénomènes (pluie, vent, température) et des matières "
              "d'œuvre (pelouse, terrasse) comme acteurs non humains, et formule parfois les cas au passif. Ici, ce sont des "
              "interacteurs, et les cas s'écrivent du point de vue de l'acteur (verbe à l'infinitif + complément). À signaler "
              "aux élèves qui ont le cahier entre les mains.</li>"
              "<li>Tous les acteurs sont dessinés en bonhomme, y compris les autres systèmes (serveur de paiement, service "
              "météo)&nbsp;: le générateur de schémas ne sait pas encore dessiner le rectangle «&nbsp;actor&nbsp;» de SysML. Le "
              "cours de 3e signale cette autre convention.</li>"
              "<li>Pas de relations «&nbsp;include&nbsp;» / «&nbsp;extend&nbsp;» au collège&nbsp;: « Payer la location » est un cas à "
              "part entière, relié à l'usager et au serveur de paiement.</li>"
              "<li>Le diagramme ne montre ni l'ordre ni le ressenti&nbsp;: c'est l'argument central de 4e (le ressenti se garde "
              "à côté, il deviendra une exigence) et de 3e (choisir l'algorigramme, le storyboard ou le graphique quand la "
              "question l'exige).</li>"
              "<li>Les verbatims de 4e sont imaginés, dans l'esprit de ceux de la séquence de Hangzhou (4e_C2.1)&nbsp;; les modes "
              "de 3e reprennent ceux de la séquence de Pékin (3e_C2.1)&nbsp;; le texte de la station d'alerte suit l'objet-fil "
              "de 3e (anémomètre, sirène, gyrophare, technicien qui teste chaque matin).</li></ul>")
DEUX_NOMS = ("Son nom français est le <b>diagramme de cas d'utilisation</b>&nbsp;; le programme de technologie le range parmi "
             "les modes de représentation (la modélisation). Les ingénieurs l'appellent souvent par son nom anglais, <b>use "
             "case</b>, et précisent qu'il vient du langage <b>SysML</b> (<i>Systems Modeling Language</i>, le langage de "
             "modélisation des systèmes)&nbsp;: on dit alors « le use case SysML ». Si tu rencontres l'un des deux noms, c'est "
             "le même schéma.")
QCM_SOUS_TITRE = ("Reconnaître les acteurs d'un système (5e) ; passer des phrases des usagers au diagramme de cas "
                  "d'utilisation, le compléter, le corriger (4e) ; choisir le mode de représentation, construire le "
                  "diagramme (3e)")
