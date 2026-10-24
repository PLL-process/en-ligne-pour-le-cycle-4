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
         "charge de la batterie et à Remplacer la lampe.")

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
    largeur=1000, acteurs_dans=["gardienne"])

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
