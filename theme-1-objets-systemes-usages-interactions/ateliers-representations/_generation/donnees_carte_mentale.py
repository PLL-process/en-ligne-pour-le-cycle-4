# -*- coding: utf-8 -*-
"""Atelier — La carte mentale (carte heuristique, « mind map »).

Codes servis : 5e_C1.4, 4e_C1.2, 3e_C1.3. Le programme ne nomme pas la carte mentale :
il demande d'« exprimer et structurer sa pensée en mobilisant le langage naturel et des
outils de représentation » et, en 5e, de classer des données et de les retrouver dans une
arborescence.

Message clé : la carte mentale est un outil de SYNTHÈSE et d'organisation des idées, pas une
description technique — elle ne montre ni ce qui circule, ni l'ordre des opérations.

Le verbe change d'un niveau à l'autre, pas la notion :
  5e  CLASSER des données (et passer de la carte à l'arborescence de dossiers) ;
  4e  ORGANISER des arguments (avantages, inconvénients) et corriger une carte mal faite ;
  3e  ARGUMENTER à partir de la carte, et CHOISIR la carte mentale quand c'est elle qui convient.
"""
import figures

SLUG = "carte-mentale"
COURT = "cm"
EMOJI = "🗺️"
TITRE = "La carte mentale"
TITRE_COURT = "la carte mentale (carte heuristique)"
TITRE_COMPLET = "La carte mentale, aussi appelée carte heuristique (mind map en anglais)"
ETIQUETTE = "🗺️ carte mentale"
ETIQUETTE_COURTE = "Carte mentale"
MENTION_FICTION = ("Situations imaginées pour les exercices : les fichiers de la 5e B, le jardin du collège et Mme Joseph, "
                   "la station d'alerte de la commune et ses chiffres sont inventés.")

e = figures.e

# ─────────────────────────────────────────────────────────────────────────────
# Les dessins
# ─────────────────────────────────────────────────────────────────────────────
# 5e — le projet lampadaire : cinq branches, une feuille d'exemple et une case à remplir chacune.
DONNEES_E1 = ["le capteur de lumière, vu de près",
              "820, 640, 310 et 95 lux, mardi soir",
              "si moins de 200 lux, allumer la LED",
              "ce qu'on a fait et conclu, séance 2",
              "le boîtier dessiné à main levée",
              "la lampe LED, posée sur la table"]

BRANCHES_PROJET = [("Photos", "le lampadaire allumé, la nuit", DONNEES_E1[0]),
                   ("Mesures", "luminosité de lundi, en lux", DONNEES_E1[1]),
                   ("Programmes", "allumage automatique, version 1", DONNEES_E1[2]),
                   ("Comptes rendus", "compte rendu de la séance 1", DONNEES_E1[3]),
                   ("Croquis", "le mât et son support, avec cotes", DONNEES_E1[4])]

DESC_PROJET = ("Carte mentale. Au centre, une ellipse : « Notre projet : le lampadaire ». Cinq branches en partent, chacune "
               "avec un nom et une couleur. À droite : Photos, Mesures, Programmes. À gauche : Comptes rendus, Croquis. ")

CM_PROJET_A_REMPLIR = figures.carte_mentale(
    "cm-projet", "Notre projet : le lampadaire", [(b, [f, ""]) for b, f, _ in BRANCHES_PROJET],
    "Carte mentale des données du projet lampadaire, à compléter",
    DESC_PROJET + "Chaque branche porte deux feuilles. La première est écrite : Photos, « le lampadaire allumé, la nuit » ; "
    "Mesures, « luminosité de lundi, en lux » ; Programmes, « allumage automatique, version 1 » ; Comptes rendus, « compte rendu "
    "de la séance 1 » ; Croquis, « le mât et son support, avec cotes ». La seconde feuille de chaque branche est vide, en "
    "pointillés : c'est là que s'écrivent tes choix.",
    vivants={(i, 1): "cm-p%d" % (i + 1) for i in range(5)})


def _projet(ident, titre):
    return figures.carte_mentale(
        ident, "Notre projet : le lampadaire", [(b, [f, g]) for b, f, g in BRANCHES_PROJET], titre,
        DESC_PROJET + "Photos : « le lampadaire allumé, la nuit » et « le capteur de lumière, vu de près ». Mesures : « luminosité "
        "de lundi, en lux » et « 820, 640, 310 et 95 lux, mardi soir ». Programmes : « allumage automatique, version 1 » et « si "
        "moins de 200 lux, allumer la LED ». Comptes rendus : « compte rendu de la séance 1 » et « ce qu'on a fait et conclu, "
        "séance 2 ». Croquis : « le mât et son support, avec cotes » et « le boîtier dessiné à main levée ».")


CM_PROJET_CORRIGE = _projet("cm-projet-c", "Carte mentale des données du projet lampadaire, complétée")
CM_PROJET_E2 = _projet("cm-projet-2", "Carte mentale des données du projet lampadaire")


def arborescence(ident, lettre, lignes, titre, desc, largeur=400):
    """Un dossier de l'ordinateur, vu comme dans l'explorateur : lignes = [(profondeur, nom, 'd'|'f')].
    Un dossier et un fichier ont deux formes d'icône différentes (jamais la couleur seule), et une légende."""
    pas, x0, y0 = 30, 22, 66
    hauteur = y0 + len(lignes) * pas + 46
    corps = ['<circle cx="34" cy="26" r="15" fill="#1f5fbf"/>',
             figures.texte(34, 26, lettre, taille=16, gras=True, couleur="#ffffff", car=3),
             figures.texte(60, 26, "Arborescence " + lettre, taille=16, gras=True, ancre="start", car=40, lignes_max=1)]
    pos = []
    for k, (prof, nom, genre) in enumerate(lignes):
        x, y = x0 + prof * 26, y0 + k * pas
        pos.append((x, y, prof))
        # le trait qui part du dossier parent
        for kp in range(k - 1, -1, -1):
            if pos[kp][2] == prof - 1:
                xp, yp = pos[kp][0], pos[kp][1]
                corps.append('<path d="M%.1f,%.1f V%.1f H%.1f" fill="none" stroke="%s" stroke-width="1.6"/>'
                             % (xp + 10, yp + 10, y, x - 3, figures.GRIS))
                break
    for (x, y, prof), (_, nom, genre) in zip(pos, lignes):
        if genre == "d":
            corps.append('<path d="M%.1f,%.1f h8 l3,3 h11 v15 h-22 z" fill="#fff1df" stroke="#b35c00" stroke-width="1.6"/>'
                         % (x, y - 9))
        else:
            corps.append('<path d="M%.1f,%.1f h11 l5,5 v15 h-16 z M%.1f,%.1f v5 h5" fill="#ffffff" stroke="%s" stroke-width="1.5"/>'
                         % (x + 3, y - 10, x + 14, y - 10, figures.GRIS))
        corps.append(figures.texte(x + 30, y, nom, taille=14.5, gras=(genre == "d"), ancre="start", car=40, lignes_max=1))
    yl = y0 + len(lignes) * pas + 12
    corps.append('<path d="M22,%.1f h8 l3,3 h11 v15 h-22 z" fill="#fff1df" stroke="#b35c00" stroke-width="1.6"/>' % (yl - 9))
    corps.append(figures.texte(52, yl, "un dossier", taille=13, couleur=figures.GRIS, ancre="start", car=20, italique=True))
    corps.append('<path d="M173,%.1f h11 l5,5 v15 h-16 z M184,%.1f v5 h5" fill="#ffffff" stroke="%s" stroke-width="1.5"/>'
                 % (yl - 10, yl - 10, figures.GRIS))
    corps.append(figures.texte(200, yl, "un fichier", taille=13, couleur=figures.GRIS, ancre="start", car=20, italique=True))
    return figures.svg(largeur, hauteur, titre, desc, "".join(corps), ident=ident)


BRANCHES_DOSSIERS = ["Programmes", "Comptes rendus", "Croquis"]
ARBO_A = arborescence(
    "cm-arbo-a", "A",
    [(0, "Documents", "d"), (1, "5eB", "d"), (2, "Lampadaire", "d"), (3, "Photos", "d"),
     (4, "lampadaire_nuit.jpg", "f"), (4, "capteur_de_pres.jpg", "f"), (3, "Mesures", "d"),
     (4, "releves_lundi.csv", "f"), (4, "releves_mardi.csv", "f")] + [(3, b, "d") for b in BRANCHES_DOSSIERS],
    "Arborescence A : Documents, 5eB, Lampadaire, puis un dossier par branche",
    "Arborescence A. Le dossier Documents contient le dossier 5eB, qui contient le dossier Lampadaire. Dans Lampadaire, "
    "cinq dossiers : Photos (avec les fichiers lampadaire_nuit.jpg et capteur_de_pres.jpg), Mesures (avec releves_lundi.csv "
    "et releves_mardi.csv), Programmes, Comptes rendus et Croquis. Une icône de chemise désigne un dossier, une icône de "
    "page un fichier.")
ARBO_B = arborescence(
    "cm-arbo-b", "B",
    [(0, "Documents", "d"), (1, "lampadaire_nuit.jpg", "f"), (1, "releves_mardi.csv", "f"),
     (1, "seance1_compte_rendu.odt", "f"), (1, "capteur_de_pres.jpg", "f"), (1, "croquis_mat.jpg", "f"),
     (1, "releves_lundi.csv", "f")],
    "Arborescence B : tous les fichiers directement dans Documents",
    "Arborescence B. Le dossier Documents contient directement six fichiers, mélangés : lampadaire_nuit.jpg, "
    "releves_mardi.csv, seance1_compte_rendu.odt, capteur_de_pres.jpg, croquis_mat.jpg, releves_lundi.csv. Aucun autre dossier.")
ARBO_C = arborescence(
    "cm-arbo-c", "C",
    [(0, "Documents", "d"), (1, "5eB", "d"), (2, "Photos", "d"),
     (3, "lampadaire_nuit.jpg", "f"), (3, "capteur_de_pres.jpg", "f"), (2, "Mesures", "d"),
     (3, "releves_lundi.csv", "f"), (3, "releves_mardi.csv", "f")] + [(2, b, "d") for b in BRANCHES_DOSSIERS],
    "Arborescence C : Documents, 5eB, puis les dossiers des branches directement",
    "Arborescence C. Le dossier Documents contient le dossier 5eB. Dans 5eB, directement, cinq dossiers : Photos (avec "
    "lampadaire_nuit.jpg et capteur_de_pres.jpg), Mesures (avec releves_lundi.csv et releves_mardi.csv), Programmes, "
    "Comptes rendus et Croquis. Il n'y a pas de dossier Lampadaire.")

# 4e — l'arrosage connecté du jardin partagé
OPTIONS_E3 = ["n'arrose que si la terre est sèche",
              "Mme Joseph suit tout sur son téléphone",
              "la pompe a besoin d'électricité",
              "s'arrête si le réseau wifi est coupé",
              "les plantes ont besoin d'eau pour pousser",
              "le jardin est derrière la cantine"]

DESC_ARROSAGE = ("Carte mentale. Au centre : « L'arrosage connecté du jardin ». Quatre branches. À droite, en haut : Avantages ; "
                 "en dessous : Ce qui change, avec « avant : l'arrosoir, à la main » et « maintenant : capteur et pompe ». À "
                 "gauche, en haut : Inconvénients ; en dessous : Pour qui ?, avec « la gardienne, Mme Joseph », « les élèves du "
                 "club jardin » et « les plantes du potager ». ")


def _arrosage(ident, titre, desc, av, inc, vivants=None):
    return figures.carte_mentale(
        ident, "L'arrosage connecté du jardin",
        [("Avantages", av), ("Ce qui change", ["avant : l'arrosoir, à la main", "maintenant : capteur et pompe"]),
         ("Inconvénients", inc), ("Pour qui ?", ["la gardienne, Mme Joseph", "les élèves du club jardin", "les plantes du potager"])],
        titre, DESC_ARROSAGE + desc, vivants=vivants)


CM_ARROSAGE_A_COMPLETER = _arrosage(
    "cm-arrosage", "Carte mentale de l'arrosage connecté du jardin, à compléter",
    "Avantages : « arrose même pendant les vacances », puis deux feuilles vides en pointillés. Inconvénients : « coûte cher "
    "à l'achat », puis trois feuilles vides en pointillés ; la dernière attend ta propre idée.",
    ["arrose même pendant les vacances", "", ""], ["coûte cher à l'achat", "", "", ""],
    vivants={(0, 1): "cm-a1", (0, 2): "cm-a2", (2, 1): "cm-i1", (2, 2): "cm-i2", (2, 3): "cm-ix"})

CM_ARROSAGE_CORRIGE = _arrosage(
    "cm-arrosage-c", "Carte mentale de l'arrosage connecté du jardin, complétée",
    "Avantages : « arrose même pendant les vacances », « n'arrose que si la terre est sèche », « Mme Joseph suit tout sur son "
    "téléphone ». Inconvénients : « coûte cher à l'achat », « la pompe a besoin d'électricité », « s'arrête si le réseau "
    "wifi est coupé », « les capteurs s'usent, à changer ».",
    ["arrose même pendant les vacances", OPTIONS_E3[0], OPTIONS_E3[1]],
    ["coûte cher à l'achat", OPTIONS_E3[2], OPTIONS_E3[3], "les capteurs s'usent, à changer"])

CM_FAUTIVE = figures.carte_mentale(
    "cm-fautive", "4e B — mardi",
    [("Avantages", ["moins d'eau gaspillée", "On n'a plus besoin de venir arroser."]),
     ("Inconvénients", ["coûte cher à l'achat", "arrose même pendant les vacances"]),
     ("Divers", ["le réseau wifi", "la facture d'électricité", "le jardin créé en 2019"]),
     (" ", ["la pompe", "le capteur d'humidité", "la cuve d'eau de pluie"])],
    "Carte mentale de l'arrosage connecté, faite par un élève : à corriger",
    "Carte mentale à corriger. Au centre : « 4e B — mardi ». Quatre branches. À droite, Avantages : « moins d'eau gaspillée » "
    "et « On n'a plus besoin de venir arroser. ». En dessous, Inconvénients : « coûte cher à l'achat » et « arrose même "
    "pendant les vacances ». À gauche, en haut, Divers : « le réseau wifi », « la facture d'électricité », « le jardin créé "
    "en 2019 ». En dessous, une branche sans aucun mot, reconnaissable seulement à sa couleur : « la pompe », « le capteur "
    "d'humidité », « la cuve d'eau de pluie ».")

CM_FAUTIVE_CORRIGEE = figures.carte_mentale(
    "cm-fautive-c", "L'arrosage connecté du jardin",
    [("Avantages", ["moins d'eau gaspillée", "plus besoin de venir", "arrose pendant les vacances"]),
     ("Inconvénients", ["coûte cher à l'achat", "la facture d'électricité"]),
     ("Le matériel", ["la pompe", "le capteur d'humidité", "la cuve d'eau de pluie", "le réseau wifi"])],
    "La même carte mentale, corrigée",
    "Carte mentale corrigée. Au centre : « L'arrosage connecté du jardin ». Trois branches. Avantages : « moins d'eau "
    "gaspillée », « plus besoin de venir », « arrose pendant les vacances ». Inconvénients : « coûte cher à l'achat », « la "
    "facture d'électricité ». Le matériel : « la pompe », « le capteur d'humidité », « la cuve d'eau de pluie », « le réseau "
    "wifi ». La branche Divers a disparu, et « le jardin créé en 2019 » a été retiré : il est hors sujet.")

# 3e — la station d'alerte cyclonique et la société
CM_STATION = figures.carte_mentale(
    "cm-station", "La station d'alerte cyclonique",
    [("Sécurité", ["l'alerte arrive plus tôt", "évacuer les quartiers bas", "rentrer les bateaux à temps"]),
     ("Coût pour la commune", ["achat et pose", "entretien chaque année"]),
     ("Ce qu'elle mesure", ["vent, pluie, pression"]),
     ("Fausses alertes", ["on n'y croit plus", "écoles fermées pour rien"]),
     ("Sans téléphone", ["personnes âgées isolées", "une sirène en plus des messages"])],
    "Carte mentale : la station d'alerte cyclonique et la société",
    "Carte mentale. Au centre : « La station d'alerte cyclonique ». Cinq branches. À droite : Sécurité (« l'alerte arrive "
    "plus tôt », « évacuer les quartiers bas », « rentrer les bateaux à temps ») ; Coût pour la commune (« achat et pose », "
    "« entretien chaque année ») ; Ce qu'elle mesure (« vent, pluie, pression »). À gauche : Fausses alertes (« on n'y croit "
    "plus », « écoles fermées pour rien ») ; Sans téléphone (« personnes âgées isolées », « une sirène en plus des messages »).")

def algorigramme_alerte(ident):
    """Le comportement de la station, en algorigramme : début, lecture, test, action, attente, boucle."""
    E, G = figures.ENCRE, figures.GRIS
    pt = "url(#%s-pt)" % ident
    c = [figures.fleche_def(ident + "-pt")]

    def boite(cx, cy, l, h, txt, rx=4, car=26):
        c.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="%d" fill="#eef4ff" stroke="#1f5fbf" stroke-width="2.4"/>'
                 % (cx - l / 2, cy - h / 2, l, h, rx))
        c.append(figures.texte(cx, cy, txt, taille=14, gras=True, car=car, lignes_max=2))

    def fl(d):
        c.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.2" marker-end="%s"/>' % (d, E, pt))

    # Début (rectangle aux coins arrondis)
    c.append('<rect x="140" y="20" width="120" height="40" rx="20" fill="#ffffff" stroke="%s" stroke-width="2.4"/>' % E)
    c.append(figures.texte(200, 40, "Début", taille=14.5, gras=True, car=10))
    fl("M200,60 V96")
    boite(200, 120, 230, 48, "Lire la vitesse du vent")
    fl("M200,144 V168")
    # Le test (losange)
    c.append('<path d="M200,170 L312,225 L200,280 L88,225 z" fill="#fff8e6" stroke="#a06a00" stroke-width="2.4"/>')
    c.append(figures.texte(200, 225, "Vent plus fort que 90 km/h ?", taille=13.5, gras=True, car=16, lignes_max=2))
    fl("M200,280 V310")
    c.append(figures.texte(222, 296, "Oui", taille=13, gras=True, couleur="#16753a", car=4))
    boite(200, 340, 250, 56, "Déclencher la sirène et envoyer le message", car=24)
    fl("M312,225 H348")
    c.append(figures.texte(330, 210, "Non", taille=13, gras=True, couleur="#b3261e", car=4))
    boite(430, 225, 160, 48, "Attendre 1 minute", car=18)
    # Les deux retours vers la lecture
    fl("M200,368 V398 H40 V78 H192")
    fl("M430,201 V78 H208")
    return figures.svg(520, 420, "Le comportement de la station d'alerte, en algorigramme",
                       "Algorigramme. Début, puis « Lire la vitesse du vent », puis un losange : « Vent plus fort que 90 km/h ? ». "
                       "Si oui : « Déclencher la sirène et envoyer le message », puis une flèche qui remonte avant « Lire la vitesse "
                       "du vent ». Si non : « Attendre 1 minute », puis une flèche qui remonte au même endroit. La lecture "
                       "recommence donc sans fin.", "".join(c), ident=ident)


ALGO_ALERTE = algorigramme_alerte("cm-algo")
CM_ALERTE = figures.carte_mentale(
    "cm-alerte", "L'alerte de la station",
    [("Ce qu'elle mesure", ["la vitesse du vent"]), ("Son seuil", ["90 km/h"]),
     ("Comment elle prévient", ["la sirène", "un message sur les téléphones"]),
     ("Entre deux mesures", ["1 minute d'attente"])],
    "Le comportement de la station d'alerte, en carte mentale",
    "Carte mentale. Au centre : « L'alerte de la station ». Quatre branches. Ce qu'elle mesure : « la vitesse du vent ». Son "
    "seuil : « 90 km/h ». Comment elle prévient : « la sirène », « un message sur les téléphones ». Entre deux mesures : « 1 "
    "minute d'attente ». Aucune flèche, aucun ordre.")

# ─────────────────────────────────────────────────────────────────────────────
# 5e — CLASSER des données
# ─────────────────────────────────────────────────────────────────────────────
NOMS_BRANCHES = [b for b, _, _ in BRANCHES_PROJET]
INDICES_E1 = ["Branche Photos : une image prise avec la tablette.",
              "Branche Mesures : des nombres relevés par le capteur, avec leur unité.",
              "Branche Programmes : une instruction que la carte programmable exécute.",
              "Branche Comptes rendus : un texte qui raconte la séance.",
              "Branche Croquis : un dessin fait à la main."]

E1 = dict(
    id="e1", titre="Ranger les données du projet dans une carte mentale", code="5e_C1.4", duree=15,
    objectif="recenser les données d'un projet, puis les <b>classer</b> dans les branches d'une carte mentale.",
    production="la liste des données du projet, et la carte mentale du projet complétée.",
    mots=[("carte mentale", "un schéma qui part d'une <b>idée centrale</b> et range les idées sur des <b>branches</b>. On dit "
           "aussi <b>carte heuristique</b>, et <i lang=\"en\">mind map</i> en anglais."),
          ("idée centrale", "le sujet de la carte, écrit au milieu (ici, le projet lampadaire)."),
          ("branche", "un trait qui part du centre et porte un <b>mot</b> : il regroupe les idées d'une même famille."),
          ("feuille", "une idée ou une donnée, au bout d'une branche, écrite en quelques mots."),
          ("donnée", "une information que l'on peut enregistrer dans un fichier : une image, des nombres, un texte, un programme…"),
          ("recenser", "faire la liste complète de ce que l'on a, sans rien oublier."),
          ("lux", "l'unité de la luminosité : environ 100 000 lux en plein soleil, moins de 10 lux la nuit dans une rue sombre."),
          ("LED", "une petite lampe qui consomme peu d'électricité (de l'anglais <i lang=\"en\">light-emitting diode</i>, "
           "diode électroluminescente).")],
    intro="<p>La 5e B construit un <b>lampadaire intelligent</b> pour une rue de Sainte-Luce&nbsp;: la nuit tombe, le capteur "
          "mesure la lumière, et la LED s'allume toute seule. Après trois séances, l'équipe a beaucoup de choses sur sa table "
          "et sur sa tablette. Pour ne rien perdre, elle les range dans une <b>carte mentale</b>&nbsp;: au centre, le projet&nbsp;; "
          "sur chaque branche, une famille de données.</p>",
    consigne="<p>Une <b>donnée</b>, c'est une information que l'on peut enregistrer dans un fichier&nbsp;: une photo, des "
             "nombres, un texte, un programme. <b>D'abord, recense les données</b>&nbsp;: coche ce qui en est une. <b>Puis "
             "range-les</b> dans la carte mentale&nbsp;: chaque branche a déjà une feuille d'exemple et une feuille vide, en "
             "pointillés. Choisis ce qui va dans chaque feuille vide&nbsp;; ton choix s'écrit dans la carte. Une étiquette de "
             "la liste n'a sa place dans aucune branche.</p>",
    critere="tu coches les cinq données et seulement elles, et chaque feuille vide reçoit la donnée de sa famille.",
    widgets=[dict(type="cases", name="donnees",
                  legende="Sur la table de l'équipe, qu'est-ce qui est une <b>donnée</b>, c'est-à-dire une information que l'on "
                          "peut enregistrer dans un fichier&nbsp;?",
                  options=[("photo", "la photo du capteur de lumière, prise de près"),
                           ("carte", "la carte programmable du lampadaire"),
                           ("releves", "les nombres relevés par le capteur, mardi soir"),
                           ("led", "la lampe LED"),
                           ("programme", "le programme qui allume la LED"),
                           ("tablette", "la tablette qui a pris les photos"),
                           ("cr", "le compte rendu de la séance 2"),
                           ("croquis", "le croquis du boîtier, passé au scanner")],
                  bonnes=["photo", "releves", "programme", "cr", "croquis"],
                  retours={"carte": "La carte programmable se touche : c'est un objet. Le programme qu'elle contient, lui, est une donnée.",
                           "led": "La LED est un objet : on ne l'enregistre pas dans un fichier. Sa photo, oui.",
                           "tablette": "La tablette est un objet : elle fabrique et garde des données, mais elle n'en est pas une.",
                           "photo": "Oui : une photo s'enregistre dans un fichier image.",
                           "releves": "Oui : des nombres mesurés s'enregistrent dans un tableau.",
                           "programme": "Oui : un programme est une suite d'instructions, enregistrée dans un fichier.",
                           "cr": "Oui : un compte rendu est un texte, enregistré dans un fichier.",
                           "croquis": "Oui : une fois scanné, le croquis devient un fichier image."},
                  indice="Pour chaque ligne, demande-toi : peut-on l'enregistrer dans un fichier, ou est-ce une chose que l'on touche ?"),
             dict(type="slots", intro='<figure class="figure schema-vivant">' + CM_PROJET_A_REMPLIR +
                  '<figcaption>La carte mentale du projet. Tes choix s\'écrivent dans les feuilles en pointillés.</figcaption></figure>',
                  slots=[dict(name="p%d" % (i + 1), cible="cm-p%d" % (i + 1),
                              legende="Branche « %s » — la feuille vide" % NOMS_BRANCHES[i],
                              options=DONNEES_E1, bonnes=[DONNEES_E1[i]], indice=INDICES_E1[i]) for i in range(5)])],
    aides=["<p>Commence par la question « <b>peut-on l'enregistrer dans un fichier&nbsp;?</b> ». Puis, pour chaque donnée, "
           "demande-toi <b>de quelle nature</b> elle est&nbsp;: une image, des nombres, une instruction, un texte, un dessin. "
           "Chaque nature a sa branche.</p>",
           "<p>« La lampe LED » → on la touche → un objet, pas une donnée → aucune branche.<br>"
           "« 820, 640, 310 et 95 lux » → des nombres avec leur unité → <b>Mesures</b>.<br>"
           "« si moins de 200 lux, allumer la LED » → une instruction que la carte exécute → <b>Programmes</b>.<br>"
           "« ce qu'on a fait et conclu » → un texte qui raconte → <b>Comptes rendus</b>.<br>"
           "« dessiné à main levée » → un dessin → <b>Croquis</b>&nbsp;; « vu de près », pris avec la tablette → <b>Photos</b>.</p>"],
    jumeau=dict(consigne="Pour un exposé sur le vélo-cargo, Inès a&nbsp;: une vidéo d'essai dans une côte, le vélo-cargo "
                         "lui-même, un tableau des temps de trajet, et son plan d'exposé. Quelles sont les données, et quelle "
                         "branche donnerais-tu à chacune&nbsp;?",
                correction="Trois données&nbsp;: la <b>vidéo</b> (branche Vidéos ou Images), le <b>tableau des temps</b> (branche "
                           "Mesures), le <b>plan d'exposé</b> (branche Textes). Le vélo-cargo lui-même est un <b>objet</b>&nbsp;: "
                           "il n'a pas de feuille, seulement sa photo pourrait en avoir une."),
    correction=[
        "<b>Ce qu'on cherche d'abord&nbsp;:</b> ce qui s'enregistre dans un fichier.",
        "<b>La photo du capteur</b> → un fichier image ✔ → donnée",
        "<b>Les nombres relevés</b> → un tableau de mesures ✔ → donnée",
        "<b>Le programme</b> → une suite d'instructions enregistrée ✔ → donnée",
        "<b>Le compte rendu</b> → un texte ✔ → donnée",
        "<b>Le croquis scanné</b> → un fichier image ✔ → donnée",
        "<b>La carte programmable, la LED, la tablette</b> → on les touche → des <b>objets</b>, pas des données. On peut "
        "enregistrer leur photo, pas l'objet lui-même.",
        '<figure class="figure">' + CM_PROJET_CORRIGE + '<figcaption>La carte mentale du projet, complétée.</figcaption></figure>',
        "<b>Photos</b> → « le capteur de lumière, vu de près » → une image",
        "<b>Mesures</b> → « 820, 640, 310 et 95 lux, mardi soir » → des nombres avec leur unité",
        "<b>Programmes</b> → « si moins de 200 lux, allumer la LED » → une instruction",
        "<b>Comptes rendus</b> → « ce qu'on a fait et conclu, séance 2 » → un texte",
        "<b>Croquis</b> → « le boîtier dessiné à main levée » → un dessin",
        "<b>L'intrus</b> → « la lampe LED, posée sur la table » → un objet → aucune branche",
        ("conclusion", "On <b>recense</b> (qu'est-ce qui est une donnée&nbsp;?), puis on <b>classe</b> (de quelle nature&nbsp;?) : "
                       "une branche par famille, avec un mot sur chaque branche."),
    ],
    retenir="une carte mentale part d'une <b>idée centrale</b>&nbsp;; chaque <b>branche</b> porte le nom d'une famille, et chaque "
            "<b>feuille</b> une idée ou une donnée, en quelques mots.",
    piege="ranger un objet (la LED, la tablette) comme une donnée&nbsp;: dans un fichier, on enregistre sa photo, pas l'objet.",
)

E2 = dict(
    id="e2", titre="De la carte mentale aux dossiers de l'ordinateur", code="5e_C1.4", duree=15,
    objectif="passer de la carte mentale à une <b>arborescence</b> de dossiers, puis <b>stocker</b> et <b>retrouver</b> un fichier.",
    production="le choix de la bonne arborescence, le rangement de quatre nouveaux fichiers, et le chemin complet d'un fichier.",
    mots=[("dossier", "une « chemise » de l'ordinateur : il contient des fichiers, ou d'autres dossiers."),
          ("fichier", "une donnée enregistrée, avec un nom : une photo, un tableau, un texte…"),
          ("arborescence", "la façon dont les dossiers sont rangés les uns dans les autres, comme les branches d'un arbre."),
          ("chemin", "la suite des dossiers à ouvrir pour arriver à un fichier, du plus grand au plus petit : "
           "Documents › 5eB › Lampadaire › Mesures › releves_mardi.csv."),
          ("extension", "les lettres après le point, à la fin du nom d'un fichier : elles disent son format. "
           "<b>.jpg</b> : une image&nbsp;; <b>.csv</b> : un tableau de valeurs&nbsp;; <b>.odt</b> : un texte."),
          ("stocker", "enregistrer un fichier à un endroit précis, pour le garder.")],
    documents=[dict(svg=CM_PROJET_E2, legende="La carte mentale du projet (exercice 1).",
                    description="<p>Au centre&nbsp;: « Notre projet&nbsp;: le lampadaire ». Cinq branches&nbsp;: Photos, Mesures, "
                                "Programmes, Comptes rendus, Croquis, avec deux feuilles chacune.</p>"),
               dict(svg=ARBO_A, legende="Arborescence A.",
                    description="<p>Documents › 5eB › Lampadaire, puis cinq dossiers&nbsp;: Photos (lampadaire_nuit.jpg, "
                                "capteur_de_pres.jpg), Mesures (releves_lundi.csv, releves_mardi.csv), Programmes, Comptes "
                                "rendus, Croquis.</p>"),
               dict(svg=ARBO_B, legende="Arborescence B.",
                    description="<p>Documents contient directement six fichiers mélangés&nbsp;: deux photos, deux tableaux de "
                                "relevés, un compte rendu, un croquis. Aucun autre dossier.</p>"),
               dict(svg=ARBO_C, legende="Arborescence C.",
                    description="<p>Documents › 5eB, puis directement cinq dossiers&nbsp;: Photos, Mesures, Programmes, Comptes "
                                "rendus, Croquis. Il n'y a pas de dossier Lampadaire.</p>")],
    intro="<p>La carte mentale range les idées. Sur l'ordinateur, on range les fichiers de la même façon&nbsp;: l'<b>idée "
          "centrale</b> devient le <b>dossier du projet</b>, chaque <b>branche</b> devient un <b>dossier</b> rangé dedans, et "
          "chaque <b>feuille</b> devient un <b>fichier</b>. En classe, on enregistre toujours dans <b>Documents</b>, puis dans "
          "le <b>dossier au nom de la classe</b>&nbsp;: <b>5eB</b>.</p>",
    consigne="<p>Une <b>arborescence</b>, c'est la façon dont les dossiers sont rangés les uns dans les autres. <b>Choisis "
             "l'arborescence qui correspond à la carte mentale</b> et à la règle de la classe. Puis <b>range</b> quatre nouveaux "
             "fichiers&nbsp;: les lettres après le point, l'<b>extension</b>, disent le format (.jpg une image, .csv un tableau "
             "de valeurs, .odt un texte), mais c'est le nom qui dit de quoi parle le fichier. Enfin, <b>écris le chemin</b> "
             "complet du fichier releves_mardi.csv&nbsp;: la suite des dossiers à ouvrir, du plus grand au plus petit.</p>",
    critere="la bonne arborescence, quatre fichiers bien rangés, et un chemin qui passe, dans l'ordre, par 5eB, Lampadaire et "
            "Mesures jusqu'au fichier.",
    widgets=[dict(type="choix", name="arbo",
                  legende="Quelle arborescence range les fichiers comme la carte mentale, et comme le demande la classe&nbsp;?",
                  options=[("a", "L'arborescence A."),
                           ("b", "L'arborescence B&nbsp;: tous les fichiers sont visibles d'un seul coup."),
                           ("c", "L'arborescence C&nbsp;: un dossier par branche, juste dans 5eB."),
                           ("toutes", "Les trois se valent&nbsp;: l'ordinateur retrouve un fichier de toute façon.")],
                  bonne="a",
                  retours={"a": "Oui : Documents › 5eB, puis le dossier du projet (l'idée centrale), puis un dossier par branche.",
                           "b": "Dans B, rien n'est rangé : la carte avait cinq branches, il n'y a ici aucun dossier. Avec trente fichiers, on ne s'y retrouve plus.",
                           "c": "Dans C, il manque le dossier du projet, l'idée centrale. Au prochain projet, les photos du vélo-cargo se mélangeront à celles du lampadaire.",
                           "toutes": "La recherche de l'ordinateur aide, mais seulement si l'on connaît le nom exact du fichier. Un rangement clair, lui, se retrouve sans chercher."},
                  indice="Compare chaque arborescence à la carte : où est l'idée centrale ? où sont les branches ?"),
             dict(type="classer", name="ranger",
                  categories=[("photos", "Photos"), ("mesures", "Mesures"), ("programmes", "Programmes"),
                              ("cr", "Comptes rendus"), ("croquis", "Croquis")],
                  items=[("lampadaire_pluie.jpg", "photos", "lampadaire_pluie.jpg : .jpg veut dire une image, et le nom parle du lampadaire sous la pluie."),
                         ("releves_jeudi.csv", "mesures", "releves_jeudi.csv : .csv veut dire un tableau de valeurs relevées."),
                         ("seance4_compte_rendu.odt", "cr", "seance4_compte_rendu.odt : .odt veut dire un texte, et le nom dit ce que c'est."),
                         ("croquis_boitier_v2.jpg", "croquis", "croquis_boitier_v2.jpg : c'est bien une image (.jpg), mais le nom dit ce qu'elle montre : un croquis.")]),
             dict(type="texte", name="chemin", lignes=2, minCar=10,
                  label="Écris le chemin complet du fichier releves_mardi.csv, en séparant les dossiers par « › » (ou par « / »).",
                  criteres=[dict(label="ton chemin passe par le dossier de la classe (5eB)", motifs=[r"5\s?e\s?b"],
                                 manque="Il manque le dossier de la classe : dans Documents, on ouvre d'abord 5eB."),
                            dict(label="il passe par le dossier du projet (Lampadaire)", motifs=["lampadaire"],
                                 manque="Il manque le dossier du projet : l'idée centrale de la carte, Lampadaire."),
                            dict(label="il passe par la bonne branche (Mesures)", motifs=["mesure"],
                                 manque="Il manque la bonne branche : un tableau de relevés va dans le dossier Mesures."),
                            dict(label="les dossiers sont dans l'ordre, du plus grand au plus petit", motifs=[r"5\s?e\s?b.*lampadaire.*mesure"],
                                 manque="Remets les dossiers dans l'ordre où on les ouvre : 5eB, puis Lampadaire, puis Mesures."),
                            dict(label="le chemin finit par le nom du fichier", motifs=[r"mesures?\W.*releves?.?mardi"],
                                 manque="Termine le chemin par le nom du fichier : releves_mardi.csv.")],
                  etayage=["Documents › … › … › … › releves_mardi.csv",
                           "J'ouvre Documents, puis le dossier de ma classe, puis le dossier du projet, puis la branche…"],
                  exemple="Documents › 5eB › Lampadaire › Mesures › releves_mardi.csv")],
    aides=["<p>Pose la carte mentale à côté des arborescences. Cherche où est passée l'<b>idée centrale</b> (le projet), puis "
           "les <b>branches</b> (les dossiers). Pour ranger un fichier, lis d'abord son <b>nom</b>&nbsp;: il dit de quoi parle le "
           "fichier&nbsp;; l'extension dit seulement son format.</p>",
           "<p>Carte → dossiers&nbsp;: idée centrale → <b>Lampadaire</b>&nbsp;; branches → <b>Photos, Mesures…</b>&nbsp;; feuilles → "
           "fichiers.<br>Règle de la classe → tout commence par <b>Documents › 5eB</b>.<br>"
           "A → Documents › 5eB › Lampadaire › branches → ✔.<br>"
           "croquis_boitier_v2.jpg → .jpg, une image… mais le nom dit « croquis » → dossier <b>Croquis</b>.<br>"
           "Chemin → on écrit chaque dossier ouvert, dans l'ordre&nbsp;: Documents › 5eB › Lampadaire › Mesures › puis le fichier.</p>"],
    jumeau=dict(consigne="La 5e A range son projet « Vélo-cargo » de la même façon. Écris le chemin de la photo velo_cote.jpg.",
                correction="<b>Documents › 5eA › Vélo-cargo › Photos › velo_cote.jpg</b>&nbsp;: d'abord le dossier de la classe, "
                           "puis celui du projet (l'idée centrale), puis la branche Photos, et enfin le fichier."),
    correction=[
        "<b>L'idée centrale</b> « Notre projet&nbsp;: le lampadaire » → devient le dossier <b>Lampadaire</b>",
        "<b>Les cinq branches</b> → deviennent cinq dossiers dans Lampadaire&nbsp;: Photos, Mesures, Programmes, Comptes rendus, Croquis",
        "<b>Les feuilles</b> → deviennent les fichiers, chacun dans le dossier de sa branche",
        "<b>A</b> → Documents › 5eB › Lampadaire › un dossier par branche → ✔ c'est la carte, rangée comme le veut la classe",
        "<b>B</b> → aucun dossier, tout est mélangé → ✘ les branches de la carte ont disparu",
        "<b>C</b> → pas de dossier Lampadaire → ✘ l'idée centrale manque&nbsp;; au projet suivant, tout se mélange",
        "« Les trois se valent » → ✘ la recherche de l'ordinateur ne marche que si l'on connaît le nom exact du fichier",
        "<b>lampadaire_pluie.jpg</b> → une image du lampadaire → <b>Photos</b>",
        "<b>releves_jeudi.csv</b> → un tableau de valeurs relevées → <b>Mesures</b>",
        "<b>seance4_compte_rendu.odt</b> → un texte → <b>Comptes rendus</b>",
        "<b>croquis_boitier_v2.jpg</b> → une image (.jpg), mais c'est un dessin du boîtier → <b>Croquis</b>&nbsp;: on range "
        "d'après ce que montre le fichier, pas d'après son extension seule",
        "<b>Le chemin attendu&nbsp;:</b> Documents › 5eB › Lampadaire › Mesures › releves_mardi.csv",
        ("conclusion", "Une carte mentale bien faite donne l'arborescence&nbsp;: <b>idée centrale → dossier du projet</b>, "
                       "<b>branches → dossiers</b>, <b>feuilles → fichiers</b>. Le chemin se lit du plus grand dossier au plus petit."),
    ],
    retenir="on range ses fichiers comme une carte mentale&nbsp;: le dossier du projet au centre, un dossier par branche&nbsp;; le "
            "<b>chemin</b> d'un fichier se lit du plus grand dossier au plus petit, et l'<b>extension</b> (.jpg, .csv, .odt) dit son format.",
    piege="ranger un fichier d'après sa seule extension&nbsp;: un croquis scanné est une image .jpg, et il va pourtant dans Croquis.",
)

# ─────────────────────────────────────────────────────────────────────────────
# 4e — ORGANISER des arguments
# ─────────────────────────────────────────────────────────────────────────────
E3 = dict(
    id="e3", titre="Les avantages et les inconvénients de l'arrosage connecté", code="4e_C1.2", duree=15,
    objectif="organiser, sur une carte mentale, les <b>avantages</b> et les <b>inconvénients</b> d'une évolution technologique.",
    production="la carte mentale de l'arrosage connecté complétée, la raison d'un hors-sujet, et une feuille écrite par toi.",
    mots=[("évolution technologique", "le passage d'une ancienne façon de faire à une nouvelle, grâce à un objet ou à un "
           "programme (ici&nbsp;: de l'arrosoir à l'arrosage connecté)."),
          ("avantage", "ce que l'évolution apporte de mieux, à quelqu'un ou à quelque chose."),
          ("inconvénient", "ce que l'évolution coûte, fait perdre ou rend fragile."),
          ("hors sujet", "une phrase qui peut être vraie, mais qui ne répond pas à la question posée."),
          ("connecté", "relié à un réseau (ici le wifi du collège) pour envoyer ou recevoir des informations."),
          ("capteur d'humidité", "un composant planté dans la terre, qui mesure si elle est sèche ou mouillée.")],
    intro="<p>Avant, au jardin partagé du collège, les élèves du club arrosaient à l'<b>arrosoir</b>. Depuis la rentrée, un "
          "<b>système d'arrosage connecté</b> s'en charge&nbsp;: un capteur d'humidité mesure la terre, une pompe prend l'eau "
          "de la cuve, et la gardienne, Mme Joseph, reçoit des nouvelles sur son téléphone. Le club prépare une carte mentale "
          "pour en débattre.</p>",
    consigne="<p>Un <b>avantage</b>, c'est ce que l'évolution apporte de mieux&nbsp;; un <b>inconvénient</b>, ce qu'elle coûte "
             "ou fait perdre. <b>Complète les feuilles vides</b> des branches Avantages et Inconvénients avec les étiquettes de "
             "la liste&nbsp;: tes choix s'écrivent dans la carte. Deux étiquettes sont <b>hors sujet</b>&nbsp;: elles restent "
             "dehors, et tu dis <b>pourquoi</b>. Enfin, <b>écris ta propre feuille</b>&nbsp;: un autre inconvénient, en "
             "quelques mots.</p>",
    critere="deux avantages et deux inconvénients bien placés, la bonne raison pour le hors-sujet, et une feuille courte qui "
            "dit ce que le système coûte ou fait perdre.",
    widgets=[dict(type="slots", intro='<figure class="figure schema-vivant">' + CM_ARROSAGE_A_COMPLETER +
                  '<figcaption>La carte mentale du club jardin. Tes choix s\'écrivent dans les feuilles en pointillés.</figcaption></figure>',
                  slots=[dict(name="a1", cible="cm-a1", legende="Branche « Avantages » — première feuille vide",
                              options=OPTIONS_E3, bonnes=OPTIONS_E3[0:2], groupe="av",
                              indice="Branche Avantages : choisis ce que le système fait de mieux que l'arrosoir (et pas deux fois la même étiquette)."),
                         dict(name="a2", cible="cm-a2", legende="Branche « Avantages » — seconde feuille vide",
                              options=OPTIONS_E3, bonnes=[OPTIONS_E3[1], OPTIONS_E3[0]], groupe="av",
                              indice="Branche Avantages : choisis ce que le système fait de mieux que l'arrosoir (et pas deux fois la même étiquette)."),
                         dict(name="i1", cible="cm-i1", legende="Branche « Inconvénients » — première feuille vide",
                              options=OPTIONS_E3, bonnes=OPTIONS_E3[2:4], groupe="inc",
                              indice="Branche Inconvénients : choisis ce que le système coûte ou rend fragile (et pas deux fois la même étiquette)."),
                         dict(name="i2", cible="cm-i2", legende="Branche « Inconvénients » — deuxième feuille vide",
                              options=OPTIONS_E3, bonnes=[OPTIONS_E3[3], OPTIONS_E3[2]], groupe="inc",
                              indice="Branche Inconvénients : choisis ce que le système coûte ou rend fragile (et pas deux fois la même étiquette).")]),
             dict(type="choix", name="hors",
                  legende="Pourquoi « les plantes ont besoin d'eau pour pousser » n'a-t-il pas de feuille&nbsp;?",
                  options=[("faux", "Parce que c'est faux&nbsp;: les plantes du jardin se passent d'eau."),
                           ("hors", "Parce que c'est vrai, mais cela ne dit rien de ce que l'arrosage connecté change."),
                           ("long", "Parce que la phrase est trop longue pour tenir dans une feuille."),
                           ("plantes", "Parce que les plantes sont déjà dans la branche « Pour qui&nbsp;? ».")],
                  bonne="hors",
                  retours={"faux": "C'est vrai, au contraire : les plantes ont besoin d'eau. Le problème est ailleurs.",
                           "long": "Elle tiendrait en deux lignes. Ce n'est pas sa longueur qui l'écarte, c'est son sujet.",
                           "plantes": "Les plantes ont bien leur feuille dans « Pour qui ? ». Mais cette phrase-là ne dit ni un avantage ni un inconvénient.",
                           "hors": "Oui : c'est vrai avec l'arrosoir comme avec le système. Ce n'est donc ni un avantage ni un inconvénient de l'évolution."},
                  indice="Demande-toi si cette phrase était déjà vraie au temps de l'arrosoir."),
             dict(type="texte", name="mafeuille", lignes=2, minCar=6, miroir="cm-ix",
                  label="Ta feuille, dans la dernière case des Inconvénients&nbsp;: un autre inconvénient, en quelques mots.",
                  criteres=[dict(label="ta feuille est courte&nbsp;: quelques mots, pas plus de deux lignes de la carte",
                                 motifs=[r"^.{3,44}$"],
                                 manque="Ta feuille est trop longue : garde trois ou quatre mots-clés, comme les autres feuilles."),
                            dict(label="elle dit ce que le système coûte, fait perdre ou rend fragile",
                                 motifs=[r"cher|cout|prix|argent|euro|pay|factur|electri|energi|batterie|pile|panne|bug|cass|"
                                         r"internet|connexion|pirat|donnee|depend|entretien|entreten|repar|capteur|dechet|recycl|"
                                         r"plastique|bruit|uses?\b|usure|oubli|perd|mise a jour|complique|vol[eé]?\b|vandal|"
                                         r"moins (de |d.)?(eleves|visite|passage|observ)|plus personne|ne viennent plus|"
                                         r"ne voi|regard"],
                                 manque="Dis ce que le système coûte, fait perdre ou rend fragile : l'argent, l'énergie, les pannes, la présence des élèves…")],
                  interdits=[dict(motifs=[r"wifi", r"pompe (a besoin|consomme)", r"cher a l.achat"],
                                  message="Cette idée est déjà sur la carte : trouve un autre inconvénient.")],
                  etayage=["Il faut … (changer, réparer, payer) …", "Les élèves … (venir, regarder) …"],
                  exemple="les capteurs s'usent, à changer")],
    aides=["<p>Pour chaque étiquette, pose la question&nbsp;: « <b>est-ce que l'arrosage connecté change quelque chose, en "
           "mieux ou en moins bien&nbsp;?</b> » En mieux → Avantages. En moins bien → Inconvénients. Rien ne change → hors "
           "sujet.</p>",
           "<p>« n'arrose que si la terre est sèche » → moins d'eau perdue qu'à l'arrosoir → <b>avantage</b>.<br>"
           "« Mme Joseph suit tout sur son téléphone » → elle sait ce qui se passe sans venir → <b>avantage</b>.<br>"
           "« la pompe a besoin d'électricité » → l'arrosoir n'en avait pas besoin → <b>inconvénient</b>.<br>"
           "« s'arrête si le réseau wifi est coupé » → le système devient fragile → <b>inconvénient</b>.<br>"
           "« les plantes ont besoin d'eau » → vrai avant comme après → <b>hors sujet</b>.</p>"],
    jumeau=dict(consigne="Le collège remplace les clés de la salle de technologie par un badge électronique. Donne un avantage, "
                         "un inconvénient, et une phrase vraie mais hors sujet.",
                correction="Avantage&nbsp;: <b>un badge perdu se désactive</b> (plus besoin de changer la serrure). Inconvénient&nbsp;: "
                           "<b>la porte ne s'ouvre plus en cas de panne de courant</b>. Hors sujet&nbsp;: « la salle de technologie est "
                           "au premier étage » — vrai, mais rien à voir avec l'évolution."),
    correction=[
        '<figure class="figure">' + CM_ARROSAGE_CORRIGE + '<figcaption>La carte mentale complétée (la dernière feuille est un exemple de réponse).</figcaption></figure>',
        "<b>« n'arrose que si la terre est sèche »</b> → moins d'eau gaspillée qu'à l'arrosoir → <b>Avantages</b>",
        "<b>« Mme Joseph suit tout sur son téléphone »</b> → elle sait sans se déplacer → <b>Avantages</b>",
        "<b>« la pompe a besoin d'électricité »</b> → une dépense d'énergie nouvelle → <b>Inconvénients</b>",
        "<b>« s'arrête si le réseau wifi est coupé »</b> → le système dépend du réseau → <b>Inconvénients</b>",
        "<b>« les plantes ont besoin d'eau pour pousser »</b> → vrai, mais vrai aussi à l'arrosoir → <b>hors sujet</b>",
        "<b>« le jardin est derrière la cantine »</b> → vrai, mais sans rapport avec l'évolution → <b>hors sujet</b>",
        "Les autres raisons ne tiennent pas&nbsp;: la phrase n'est pas fausse, elle tiendrait dans une feuille, et les plantes "
        "ont déjà leur place dans « Pour qui&nbsp;? » sans que cela dise un avantage ou un inconvénient.",
        "<b>Ta feuille</b> → par exemple « les capteurs s'usent, à changer », « des déchets électroniques », « les élèves "
        "viennent moins au jardin », « une panne passe inaperçue »",
        ("conclusion", "Une carte mentale <b>organise</b> les arguments&nbsp;: les avantages et les inconvénients face à face, et "
                       "<b>rien</b> de hors sujet, même si c'est vrai."),
    ],
    retenir="pour juger une évolution technologique, on range ses <b>avantages</b> et ses <b>inconvénients</b> sur deux branches "
            "face à face&nbsp;; une phrase vraie qui ne parle pas de l'évolution est <b>hors sujet</b> et reste dehors.",
    piege="garder une phrase parce qu'elle est vraie&nbsp;: « les plantes ont besoin d'eau » est vrai, mais ne dit rien de "
          "l'évolution.",
)

E4 = dict(
    id="e4", titre="Corriger une carte mentale mal faite", code="4e_C1.2", duree=15,
    objectif="repérer les défauts d'une carte mentale d'arguments, puis les corriger.",
    production="la liste des défauts, le tri de la branche « Divers », et une feuille réécrite en mots-clés.",
    mots=[("mot-clé", "un mot, ou un petit groupe de mots, qui suffit à rappeler toute une idée."),
          ("fourre-tout", "un endroit où l'on met tout ce qu'on ne sait pas ranger. Sur une carte, la branche « Divers »."),
          ("défaut", "ce qui empêche la carte d'être lue ou comprise.")],
    documents=[dict(svg=CM_FAUTIVE, legende="La carte mentale d'Enzo, sur l'arrosage connecté du jardin.",
                    description="<p>Au centre&nbsp;: « 4e B — mardi ». Branche Avantages&nbsp;: « moins d'eau gaspillée », « On n'a "
                                "plus besoin de venir arroser. ». Branche Inconvénients&nbsp;: « coûte cher à l'achat », « arrose "
                                "même pendant les vacances ». Branche Divers&nbsp;: « le réseau wifi », « la facture d'électricité », "
                                "« le jardin créé en 2019 ». Une quatrième branche n'a pas de nom, seulement une couleur&nbsp;: « la "
                                "pompe », « le capteur d'humidité », « la cuve d'eau de pluie ».</p>")],
    intro="<p>Enzo a fait sa carte mentale de l'arrosage connecté du jardin. Elle contient de bonnes idées, mais elle est "
          "difficile à lire, et une idée est à la mauvaise place.</p>",
    consigne="<p>Une carte mentale se lit d'un coup d'œil si son <b>idée centrale</b> dit le sujet, si chaque <b>branche</b> "
             "porte un mot qui dit sa famille, et si chaque feuille est faite de <b>mots-clés</b> (quelques mots, pas une "
             "phrase). <b>Coche les défauts</b> de la carte d'Enzo — attention, certaines propositions décrivent des choses "
             "normales. Puis <b>trie la branche « Divers »</b>, et <b>réécris en mots-clés</b> la feuille qui est une phrase.</p>",
    critere="les cinq défauts cochés et seulement eux, les trois feuilles de « Divers » bien triées, et une feuille courte "
            "qui garde l'idée.",
    widgets=[dict(type="cases", name="defauts", legende="Qu'est-ce qui ne va pas dans la carte d'Enzo&nbsp;?",
                  options=[("centre", "L'idée centrale ne dit pas de quoi parle la carte."),
                           ("fleches", "Aucune flèche ne relie les feuilles entre elles."),
                           ("phrase", "Une feuille est une phrase entière, pas des mots-clés."),
                           ("divers", "La branche « Divers » mélange des idées sans rapport."),
                           ("couleurs", "Chaque branche a sa propre couleur."),
                           ("range", "Un avantage est rangé dans les inconvénients."),
                           ("ordre", "On ne voit pas dans quel ordre le capteur et la pompe fonctionnent."),
                           ("nom", "Une branche n'a pas de nom&nbsp;: seule sa couleur la distingue.")],
                  bonnes=["centre", "phrase", "divers", "range", "nom"],
                  retours={"centre": "Oui : « 4e B — mardi » dit qui et quand, pas le sujet.",
                           "phrase": "Oui : « On n'a plus besoin de venir arroser. » est une phrase ; trois mots suffisent.",
                           "divers": "Oui : « Divers » ne dit rien ; chaque idée doit aller dans sa vraie branche.",
                           "range": "Oui : arroser pendant les vacances est un avantage, pas un inconvénient.",
                           "nom": "Oui : sans mot, la branche ne dit pas sa famille, et ceux qui voient mal les couleurs ne la distinguent pas.",
                           "fleches": "C'est normal : une carte mentale range des idées, elle ne montre pas ce qui circule d'une feuille à l'autre.",
                           "couleurs": "C'est normal, et même utile : une couleur aide à lire, à condition qu'un mot l'accompagne.",
                           "ordre": "C'est normal : l'ordre des opérations se montre avec un algorigramme, pas avec une carte mentale."},
                  indice="Pour chaque proposition, demande-toi : est-ce que cela empêche de lire ou de comprendre la carte ? Une carte mentale n'a pas à montrer un ordre ni ce qui circule."),
             dict(type="classer", name="divers",
                  categories=[("av", "la branche Avantages"), ("inc", "la branche Inconvénients"),
                              ("mat", "la branche sans nom, une fois nommée « Le matériel »"),
                              ("enlever", "nulle part&nbsp;: c'est hors sujet, on l'enlève")],
                  items=[("« le réseau wifi »", "mat", "Le réseau wifi : est-ce un avantage, un inconvénient, ou une chose dont le système a besoin pour fonctionner ?"),
                         ("« la facture d'électricité »", "inc", "La facture d'électricité : c'est ce que la pompe coûte chaque mois."),
                         ("« le jardin créé en 2019 »", "enlever", "Le jardin créé en 2019 : cela dit-il quelque chose de l'arrosage connecté ?")]),
             dict(type="texte", name="motscles", lignes=2, minCar=4,
                  label="Réécris en mots-clés la feuille « On n'a plus besoin de venir arroser. »",
                  criteres=[dict(label="ta feuille est courte&nbsp;: cinq mots au plus", motifs=[r"^\S+(\s\S+){0,4}$"],
                                 manque="C'est encore trop long : garde l'essentiel, en cinq mots au plus."),
                            dict(label="elle garde l'idée&nbsp;: plus besoin de venir au jardin",
                                 motifs=[r"venir|deplac|presence|present|passer|absent|sans (nous|personne|la gardienne|eleve)|"
                                         r"automati|tout seul|seul|a distance|plus besoin|vacances"],
                                 manque="Garde l'idée de départ : le système arrose sans que personne ait à venir."),
                            dict(label="ce n'est plus une phrase&nbsp;: ni « on », ni point final", motifs=[r"^(?!on\b)(?!.*\.$)"],
                                 manque="Enlève « on » et le point final : une feuille n'est pas une phrase.")],
                  etayage=["plus besoin de …", "arrosage sans …"],
                  exemple="plus besoin de venir")],
    aides=["<p>Lis la carte comme quelqu'un qui ne connaît pas le sujet&nbsp;: le centre te dit-il de quoi on parle&nbsp;? "
           "chaque branche te dit-elle sa famille&nbsp;? chaque feuille est-elle à sa place&nbsp;? Une carte mentale n'a pas "
           "à montrer un ordre ni des flèches&nbsp;: ce ne sont pas des défauts.</p>",
           "<p>Centre « 4e B — mardi » → la classe et le jour, pas le sujet → <b>défaut</b>.<br>"
           "« On n'a plus besoin… » → une phrase avec un point → <b>défaut</b> → « plus besoin de venir ».<br>"
           "« Divers » → un fourre-tout → <b>défaut</b> → le wifi va avec le matériel, la facture dans les inconvénients, "
           "2019 dehors.<br>"
           "« arrose pendant les vacances », dans les inconvénients → <b>défaut</b>.<br>"
           "Branche sans mot → <b>défaut</b>.<br>"
           "Pas de flèches, pas d'ordre, des couleurs → <b>normal</b>.</p>"],
    jumeau=dict(consigne="Une carte mentale sur le téléphone au collège a pour centre « Exposé », une branche « Autres », et la "
                         "feuille « Je pense que le téléphone distrait beaucoup en classe. ». Corrige ces trois défauts.",
                correction="Centre → « <b>Le téléphone au collège</b> » (le sujet). Branche « Autres » → <b>répartir</b> ses feuilles dans "
                           "les vraies branches, ou les enlever. Feuille → « <b>distrait en classe</b> » (des mots-clés, sans « je pense »)."),
    correction=[
        '<figure class="figure">' + CM_FAUTIVE_CORRIGEE + '<figcaption>La carte d\'Enzo, corrigée.</figcaption></figure>',
        "<b>Défaut 1</b> → le centre « 4e B — mardi » → il dit qui et quand, pas le sujet → « L'arrosage connecté du jardin »",
        "<b>Défaut 2</b> → « On n'a plus besoin de venir arroser. » → une phrase → « plus besoin de venir »",
        "<b>Défaut 3</b> → la branche « Divers » → un fourre-tout → chaque feuille va dans sa vraie branche, ou sort",
        "<b>Défaut 4</b> → « arrose même pendant les vacances » dans les inconvénients → c'est un <b>avantage</b> → on le déplace",
        "<b>Défaut 5</b> → une branche sans mot → on ne sait pas sa famille → on écrit « Le matériel »",
        "<b>Pas des défauts</b> → l'absence de flèches et d'ordre (une carte mentale ne montre ni ce qui circule ni l'ordre "
        "des opérations) et les couleurs (utiles, puisqu'un mot les accompagne)",
        "<b>« le réseau wifi »</b> → le système en a besoin pour envoyer ses messages → <b>Le matériel</b>",
        "<b>« la facture d'électricité »</b> → ce que la pompe coûte → <b>Inconvénients</b>",
        "<b>« le jardin créé en 2019 »</b> → ne dit rien de l'arrosage connecté → <b>on l'enlève</b>",
        "<b>Feuille réécrite, par exemple&nbsp;:</b> « plus besoin de venir », « arrosage à distance », « sans venir au jardin »",
        ("conclusion", "Une carte lisible&nbsp;: un <b>sujet</b> au centre, un <b>mot</b> sur chaque branche, des <b>mots-clés</b> "
                       "dans les feuilles, <b>chaque idée à sa place</b> — et pas de branche « Divers »."),
    ],
    retenir="une carte mentale lisible a un <b>sujet</b> au centre, un <b>mot</b> sur chaque branche (la couleur en plus, jamais "
            "seule), des <b>mots-clés</b> dans les feuilles, et pas de branche « Divers ».",
    piege="prendre pour un défaut l'absence de flèches ou d'ordre&nbsp;: une carte mentale ne montre ni ce qui circule ni "
          "l'ordre des opérations, et ce n'est pas son rôle.",
)

# ─────────────────────────────────────────────────────────────────────────────
# 3e — ARGUMENTER à partir de la carte
# ─────────────────────────────────────────────────────────────────────────────
E5 = dict(
    id="e5", titre="De la carte mentale à l'argumentaire court", code="3e_C1.3", duree=18,
    objectif="trier les feuilles d'une carte mentale, puis s'en servir pour écrire un <b>argumentaire court</b> sur "
             "l'incidence d'un objet sur la société.",
    production="six feuilles triées, puis un argumentaire de 5 à 8 lignes.",
    mots=[("incidence sur la société", "l'effet d'un objet sur la vie des personnes&nbsp;: leur sécurité, leur argent, leur "
           "confiance, l'égalité entre elles…"),
          ("argumentaire court", "un texte de quelques lignes qui défend un avis en donnant des raisons, des exemples, et une "
           "conclusion."),
          ("connecteur d'opposition", "un mot qui annonce une idée contraire&nbsp;: <i>mais, cependant, pourtant, en revanche, "
           "toutefois</i>."),
          ("fausse alerte", "une alerte donnée alors que le danger n'arrive pas."),
          ("station d'alerte cyclonique", "un ensemble de capteurs (vent, pluie, pression de l'air) relié à une sirène et à un "
           "service de messages, qui prévient la population quand un cyclone approche."),
          ("pression", "ici, la pression de l'air&nbsp;: quand elle baisse vite, une tempête approche.")],
    documents=[dict(svg=CM_STATION, legende="La carte mentale préparée par la classe sur la station d'alerte de la commune.",
                    description="<p>Au centre&nbsp;: « La station d'alerte cyclonique ». Sécurité&nbsp;: l'alerte arrive plus tôt, "
                                "évacuer les quartiers bas, rentrer les bateaux à temps. Coût pour la commune&nbsp;: achat et pose, "
                                "entretien chaque année. Ce qu'elle mesure&nbsp;: vent, pluie, pression. Fausses alertes&nbsp;: on n'y "
                                "croit plus, écoles fermées pour rien. Sans téléphone&nbsp;: personnes âgées isolées, une sirène en "
                                "plus des messages.</p>")],
    intro="<p>La commune installe une <b>station d'alerte cyclonique</b>&nbsp;: dès que le vent forcit et que la pression de "
          "l'air chute, elle déclenche une sirène et envoie un message sur les téléphones. La classe a préparé une carte mentale "
          "pour répondre à la question du conseil municipal des jeunes&nbsp;: « <b>Cette station est-elle une bonne chose pour "
          "les habitants&nbsp;?</b> »</p>",
    consigne="<p>Une <b>incidence sur la société</b>, c'est un effet de l'objet sur la vie des personnes. <b>Trie d'abord six "
             "feuilles de la carte</b>&nbsp;: incidence positive, incidence négative, ou ni l'une ni l'autre (une feuille qui "
             "décrit le fonctionnement de la station). Puis <b>écris un argumentaire court</b> de 5 à 8 lignes, à partir de la "
             "carte&nbsp;: une incidence positive, une incidence négative introduite par un <b>connecteur d'opposition</b> "
             "(mais, cependant, pourtant…), et une <b>conclusion</b>.</p>",
    critere="six feuilles bien triées, et un argumentaire qui donne une incidence positive, une négative, un connecteur "
            "d'opposition et une conclusion.",
    widgets=[dict(type="classer", name="tri",
                  categories=[("pos", "une incidence positive pour la société"), ("neg", "une incidence négative pour la société"),
                              ("tech", "ni l'une ni l'autre&nbsp;: c'est le fonctionnement de la station")],
                  items=[("« l'alerte arrive plus tôt »", "pos", "« l'alerte arrive plus tôt » : qu'est-ce que cela change pour les habitants ?"),
                         ("« écoles fermées pour rien »", "neg", "« écoles fermées pour rien » : qui en subit les effets, et pourquoi ?"),
                         ("« achat et pose »", "neg", "« achat et pose » : qui paie, avec quel argent ?"),
                         ("« personnes âgées isolées »", "neg", "« personnes âgées isolées » : reçoivent-elles le message sur un téléphone ?"),
                         ("« une sirène en plus des messages »", "pos", "« une sirène en plus des messages » : qui entend une sirène sans avoir de téléphone ?"),
                         ("« vent, pluie, pression »", "tech", "« vent, pluie, pression » : est-ce un effet sur la vie des personnes, ou ce que la station mesure ?")]),
             dict(type="texte", name="argumentaire", lignes=8, minCar=220,
                  vide="Ton argumentaire est encore trop court : il faut 5 à 8 lignes, soit quatre ou cinq phrases.",
                  label="Mon argumentaire court (5 à 8 lignes)&nbsp;: la station d'alerte est-elle une bonne chose pour les habitants&nbsp;?",
                  criteres=[dict(label="tu donnes une incidence positive (la sécurité, le temps gagné, la sirène…)",
                                 motifs=[r"plus tot|a temps|proteg|securi|sauv|evacu|a l.abri|bateau|sirene|prevenu|previent|prevenir|vies?\b|bless"],
                                 manque="Donne une incidence positive, prise sur la carte : la sécurité, le temps gagné pour se mettre à l'abri…"),
                            dict(label="tu donnes une incidence négative (le coût, les fausses alertes, les personnes sans téléphone…)",
                                 motifs=[r"cout|cher|prix|argent|impot|budget|entretien|fausses? alertes?|n.y croi|confiance|"
                                         r"ecoles? fermees?|pour rien|isole|agee|sans telephone|pas de telephone|exclu|oubli"],
                                 manque="Donne une incidence négative, prise sur la carte : le coût pour la commune, les fausses alertes, les personnes sans téléphone…"),
                            dict(label="tu l'introduis par un connecteur d'opposition (mais, cependant, pourtant, en revanche…)",
                                 motifs=[r"\bmais\b|cependant|pourtant|en revanche|toutefois|neanmoins|par contre|alors que|meme si|malgre"],
                                 manque="Relie tes deux idées par un connecteur d'opposition : mais, cependant, pourtant, en revanche, toutefois."),
                            dict(label="tu termines par une conclusion (donc, en conclusion, finalement…)",
                                 motifs=[r"en conclusion|pour conclure|finalement|au final|en somme|c.est pourquoi|\bdonc\b|\bainsi\b|en resume|pour finir"],
                                 manque="Termine par une conclusion qui donne ton avis : « En conclusion… », « Finalement… », « C'est pourquoi… ».")],
                  etayage=["La station d'alerte protège les habitants, car… Par exemple, …",
                           "Cependant, elle a aussi des inconvénients : …",
                           "En conclusion, je pense que… à condition de…"],
                  exemple="La station d'alerte cyclonique est utile aux habitants, car l'alerte arrive plus tôt : on a le temps "
                          "d'évacuer les quartiers bas et de rentrer les bateaux. La sirène prévient aussi ceux qui n'ont pas de "
                          "téléphone. Cependant, elle coûte cher à la commune, à l'achat puis à l'entretien, et une fausse alerte "
                          "ferme les écoles pour rien : on risque de ne plus y croire. En conclusion, je pense que c'est une "
                          "bonne chose, à condition de limiter les fausses alertes.")],
    aides=["<p>Pour trier, demande-toi&nbsp;: « <b>est-ce un effet sur la vie des personnes&nbsp;?</b> » Si oui, est-il bon ou "
           "mauvais pour elles&nbsp;? Si non, c'est du fonctionnement. Pour écrire, prends <b>une branche positive</b> et "
           "<b>une branche négative</b> de la carte&nbsp;: ce sont tes deux paragraphes.</p>",
           "<p>« l'alerte arrive plus tôt » → les habitants ont le temps de se mettre à l'abri → <b>positive</b>.<br>"
           "« achat et pose » → c'est l'argent des habitants qui paie → <b>négative</b>.<br>"
           "« vent, pluie, pression » → ce que la station mesure → <b>fonctionnement</b>, pas une incidence.<br>"
           "Le plan de l'argumentaire&nbsp;: incidence positive + exemple → <b>Cependant</b>, incidence négative + exemple → "
           "<b>En conclusion</b>, ton avis, nuancé.</p>"],
    jumeau=dict(consigne="Écris l'ossature (trois phrases) d'un argumentaire sur les caméras de surveillance du parking du "
                         "collège&nbsp;: une incidence positive, une négative avec un connecteur d'opposition, une conclusion.",
                correction="« Les caméras <b>dissuadent les vols</b> de vélos sur le parking. <b>Pourtant</b>, elles filment aussi "
                           "les élèves et le personnel, qui n'ont pas choisi d'être <b>observés</b>. <b>En conclusion</b>, elles sont "
                           "utiles si les images sont peu gardées et vues seulement en cas de vol. »"),
    correction=[
        "<b>« l'alerte arrive plus tôt »</b> → les habitants ont le temps de se protéger → <b>positive</b>",
        "<b>« une sirène en plus des messages »</b> → même ceux qui n'ont pas de téléphone sont prévenus → <b>positive</b>",
        "<b>« écoles fermées pour rien »</b> → une fausse alerte dérange les familles → <b>négative</b>",
        "<b>« achat et pose »</b> → c'est l'argent de la commune, donc des habitants → <b>négative</b>",
        "<b>« personnes âgées isolées »</b> → sans téléphone, elles ne reçoivent pas le message → <b>négative</b>",
        "<b>« vent, pluie, pression »</b> → ce que la station mesure → <b>ni l'une ni l'autre</b>&nbsp;: c'est le fonctionnement, "
        "pas un effet sur la vie des personnes",
        "<b>Un argumentaire attendu&nbsp;:</b> « La station d'alerte cyclonique est utile aux habitants, car <b>l'alerte arrive "
        "plus tôt</b>&nbsp;: on a le temps d'évacuer les quartiers bas et de rentrer les bateaux. La sirène prévient aussi ceux "
        "qui n'ont pas de téléphone. <b>Cependant</b>, elle <b>coûte cher</b> à la commune, et une <b>fausse alerte</b> ferme les "
        "écoles pour rien&nbsp;: on risque de ne plus y croire. <b>En conclusion</b>, c'est une bonne chose, à condition de "
        "limiter les fausses alertes. »",
        "Chaque idée du texte vient d'une <b>branche</b> de la carte&nbsp;: Sécurité, Sans téléphone, Coût, Fausses alertes. La "
        "branche « Ce qu'elle mesure » ne sert pas&nbsp;: elle décrit l'objet, elle ne dit pas son effet sur la société.",
        ("conclusion", "La carte mentale <b>prépare</b> l'argumentaire&nbsp;: on y choisit une branche positive, une branche "
                       "négative, on les relie par un connecteur d'opposition, et on conclut."),
    ],
    retenir="un argumentaire court se prépare avec une carte mentale&nbsp;: une incidence positive, une incidence négative "
            "introduite par un <b>connecteur d'opposition</b>, puis une <b>conclusion</b> qui donne un avis nuancé.",
    piege="décrire le fonctionnement de l'objet (« elle mesure le vent ») au lieu de son incidence sur la vie des personnes.",
)

E6 = dict(
    id="e6", titre="Carte mentale ou autre représentation ?", code="3e_C1.3", duree=18,
    objectif="voir ce qu'une carte mentale montre et cache, puis la choisir quand il faut organiser ou retenir — et une autre "
             "représentation quand il faut montrer comment l'objet fonctionne.",
    production="quatre représentations identifiées, six questions reliées à leur représentation, et une phrase qui justifie "
               "un choix.",
    mots=[("représentation", "un schéma, un tableau ou un texte qui montre une idée d'une certaine façon."),
          ("algorithme", "la suite des opérations d'un programme, écrite en lignes, avec ses tests (si… alors… sinon…)."),
          ("algorigramme", "le même algorithme dessiné&nbsp;: des rectangles pour les actions, un losange pour chaque test, des "
           "flèches pour l'ordre."),
          ("seuil", "la valeur à partir de laquelle on déclenche quelque chose (ici, 90 km/h de vent)."),
          ("chaîne d'énergie", "le schéma qui montre le chemin de l'énergie dans un objet, et ses transformations."),
          ("diagramme des interacteurs extérieurs", "le schéma, souvent appelé diagramme pieuvre, qui place l'objet au centre "
           "et tout ce qui l'entoure autour."),
          ("autonomie", "le temps pendant lequel la station fonctionne sans recharge.")],
    intro="<p>Voici <b>le même comportement</b> de la station d'alerte, décrit de quatre façons.</p>"
          '<div class="critere"><p><b>①</b> La station lit la vitesse du vent. Si le vent est plus fort que 90&nbsp;km/h, elle '
          "déclenche la sirène et envoie un message sur les téléphones&nbsp;; sinon, elle attend une minute. Puis elle "
          "recommence, sans fin.</p></div>"
          '<div class="critere"><p><b>②</b><br>Répéter sans fin&nbsp;:<br>&nbsp;&nbsp;lire la vitesse du vent<br>'
          "&nbsp;&nbsp;si vent &gt; 90&nbsp;km/h alors déclencher la sirène et envoyer le message<br>"
          "&nbsp;&nbsp;sinon attendre 1 minute</p></div>"
          '<p><b>③</b></p><figure class="figure">' + ALGO_ALERTE + "<figcaption>Représentation ③.</figcaption></figure>"
          '<details class="description"><summary>📝 Ce que montre le schéma, en mots</summary><p>Début, puis « Lire la vitesse '
          "du vent », puis un losange « Vent plus fort que 90 km/h&nbsp;? ». Oui&nbsp;: « Déclencher la sirène et envoyer le "
          "message ». Non&nbsp;: « Attendre 1 minute ». Dans les deux cas, une flèche remonte avant la lecture du vent.</p></details>"
          '<p><b>④</b></p><figure class="figure">' + CM_ALERTE + "<figcaption>Représentation ④.</figcaption></figure>"
          '<details class="description"><summary>📝 Ce que montre le schéma, en mots</summary><p>Au centre&nbsp;: « L\'alerte de '
          "la station ». Ce qu'elle mesure&nbsp;: la vitesse du vent. Son seuil&nbsp;: 90 km/h. Comment elle prévient&nbsp;: la "
          "sirène, un message sur les téléphones. Entre deux mesures&nbsp;: 1 minute d'attente. Ni flèche, ni ordre.</p></details>"
          "<p>Pour son exposé, l'équipe se pose ensuite six questions. Pour chacune, une représentation convient mieux que les "
          "autres.</p>",
    consigne="<p><b>Dis ce qu'est chacune des quatre représentations</b>&nbsp;: un texte, un <b>algorithme</b> (les opérations "
             "écrites en lignes), un <b>algorigramme</b> (les mêmes opérations dessinées, avec un losange pour le test) ou une "
             "carte mentale. <b>Dis laquelle ne montre pas l'ordre.</b> Puis <b>relie chaque question</b> à la représentation qui "
             "y répond le mieux&nbsp;: la carte mentale, la chaîne d'énergie (le chemin de l'énergie), l'algorigramme, le "
             "diagramme des interacteurs extérieurs (ce qui entoure l'objet) ou le tableau (des valeurs à comparer). Enfin, "
             "<b>explique</b> pourquoi la carte mentale ne convient pas pour la question 2.</p>",
    critere="les quatre représentations reconnues, la bonne réponse sur l'ordre, six questions bien reliées, et une phrase "
            "qui dit ce que la carte mentale ne montre pas et ce qu'il faut à la place.",
    widgets=[dict(type="classer", name="quatre",
                  categories=[("texte", "un texte"), ("algo", "un algorithme"), ("gramme", "un algorigramme"),
                              ("carte", "une carte mentale")],
                  items=[("Représentation ①", "texte", "① : des phrases, à lire d'un bout à l'autre."),
                         ("Représentation ②", "algo", "② : les opérations écrites ligne à ligne, avec « si… alors… sinon »."),
                         ("Représentation ③", "gramme", "③ : des formes reliées par des flèches, et un losange pour le test."),
                         ("Représentation ④", "carte", "④ : un centre et des branches, sans flèches.")]),
             dict(type="choix", name="ordre",
                  legende="Avec laquelle ne peut-on pas savoir si la station lit le vent <b>avant</b> ou <b>après</b> avoir déclenché "
                          "la sirène&nbsp;?",
                  options=[("4", "la représentation ④"), ("1", "la représentation ①"), ("2", "la représentation ②"),
                           ("3", "la représentation ③")],
                  bonne="4",
                  retours={"4": "Oui : la carte mentale range les idées par familles, sans ordre. On sait ce que fait la station, pas dans quel ordre.",
                           "1": "Le texte donne l'ordre avec ses mots : « lit… si… sinon… puis elle recommence ».",
                           "2": "L'algorithme donne l'ordre ligne après ligne : on lit le vent d'abord, on teste ensuite.",
                           "3": "L'algorigramme donne l'ordre avec ses flèches : la lecture du vent est avant le losange."},
                  indice="Cherche la représentation qui n'a ni « puis », ni lignes successives, ni flèches."),
             dict(type="classer", name="choix",
                  categories=[("carte", "la carte mentale"), ("energie", "la chaîne d'énergie"), ("algo", "l'algorigramme"),
                              ("pieuvre", "le diagramme des interacteurs extérieurs (diagramme pieuvre)"), ("tableau", "un tableau")],
                  items=[("1 — Rassembler toutes nos idées sur la station, avant de préparer l'exposé", "carte",
                          "Question 1 : rassembler et organiser des idées."),
                         ("2 — Montrer comment l'énergie du soleil arrive jusqu'à la sirène", "energie",
                          "Question 2 : il faut suivre le chemin de l'énergie."),
                         ("3 — Montrer dans quel ordre le programme lit le vent, le compare au seuil, puis déclenche l'alerte", "algo",
                          "Question 3 : il faut montrer l'ordre des opérations et un test."),
                         ("4 — Montrer tout ce qui entoure la station&nbsp;: les habitants, le vent, la pluie, le réseau téléphonique", "pieuvre",
                          "Question 4 : il faut placer l'objet au centre et ce qui l'entoure autour."),
                         ("5 — Comparer deux modèles de station&nbsp;: prix, autonomie, portée de la sirène", "tableau",
                          "Question 5 : il faut comparer des valeurs, ligne à ligne."),
                         ("6 — Réviser tout le chapitre sur une seule page, la veille de l'évaluation", "carte",
                          "Question 6 : il faut résumer et retenir.")]),
             dict(type="texte", name="pourquoi", lignes=3, minCar=30,
                  label="Explique pourquoi la carte mentale ne convient pas pour la question 2.",
                  criteres=[dict(label="tu dis ce que la carte mentale ne montre pas (le chemin, ce qui circule, l'ordre…)",
                                 motifs=[r"chemin|circul|parcour|trajet|ordre|etape|transform|passe|suit|fleche|flux|de .{2,30} jusqu|transmet"],
                                 manque="Dis ce que la carte mentale ne montre pas : le chemin de l'énergie, ce qui circule, l'ordre des étapes."),
                            dict(label="tu nommes la représentation qui convient (la chaîne d'énergie)",
                                 motifs=[r"chaine d.energie|chaine de l.energie|chaine energ"],
                                 manque="Nomme la représentation qui convient pour la question 2 : la chaîne d'énergie.")],
                  etayage=["La carte mentale range des idées autour d'un centre, mais elle ne montre pas…",
                           "Pour la question 2, il faut plutôt… parce que…"],
                  exemple="La carte mentale range des idées autour d'un centre, mais elle ne montre pas le chemin de l'énergie "
                          "du panneau solaire à la sirène : il faut une chaîne d'énergie.")],
    aides=["<p>Pour les quatre représentations, regarde leur <b>forme</b>&nbsp;: des phrases, des lignes avec « si… alors », "
           "des formes reliées par des flèches, ou un centre avec des branches. Pour chaque question, cherche le <b>verbe</b>&nbsp;: "
           "rassembler, réviser → organiser des idées&nbsp;; montrer comment l'énergie arrive → un chemin&nbsp;; dans quel ordre → "
           "des étapes et des tests&nbsp;; ce qui entoure → l'objet au centre&nbsp;; comparer des valeurs → des lignes et des "
           "colonnes.</p>",
           "<p>Les quatre formes&nbsp;:</p><ul><li>① des phrases → <b>texte</b>&nbsp;;</li>"
           "<li>② des lignes « si… alors… sinon » → <b>algorithme</b>&nbsp;;</li>"
           "<li>③ un losange et des flèches → <b>algorigramme</b>&nbsp;;</li>"
           "<li>④ un centre et des branches → <b>carte mentale</b>.</li></ul>"
           "<p>L'ordre&nbsp;: les trois premières disent « d'abord… ensuite… »&nbsp;; la carte mentale n'a ni flèche ni ligne "
           "→ <b>pas d'ordre</b>.</p>"
           "<p>Questions 1 et 6 → organiser, retenir → <b>carte mentale</b>.<br>"
           "Question 2 → le soleil, le panneau, la batterie, la sirène&nbsp;: un chemin de l'énergie → <b>chaîne d'énergie</b>.<br>"
           "Question 3 → lire, comparer, déclencher&nbsp;: un ordre et un test → <b>algorigramme</b>.<br>"
           "Question 4 → la station au centre, ce qui l'entoure autour → <b>diagramme des interacteurs</b>.<br>"
           "Question 5 → trois valeurs pour deux modèles → <b>tableau</b>.</p>"],
    jumeau=dict(consigne="Pour le lampadaire intelligent&nbsp;: « montrer ce que fait le programme quand la lumière baisse » et "
                         "« préparer la revue de projet avec toutes nos idées ». Quelle représentation pour chacune&nbsp;?",
                correction="« Ce que fait le programme quand la lumière baisse » → un ordre et un test → <b>l'algorigramme</b>. "
                           "« Toutes nos idées pour la revue de projet » → organiser → <b>la carte mentale</b>."),
    correction=[
        "<b>①</b> → des phrases → <b>un texte</b>",
        "<b>②</b> → les opérations ligne à ligne, avec « si… alors… sinon » → <b>un algorithme</b>",
        "<b>③</b> → des formes, des flèches, un losange pour le test → <b>un algorigramme</b>",
        "<b>④</b> → un centre, des branches, aucune flèche → <b>une carte mentale</b>",
        "<b>L'ordre</b> → ①, ② et ③ le donnent (« puis », les lignes, les flèches)&nbsp;; <b>④ ne le donne pas</b>&nbsp;: elle dit "
        "tout ce que fait la station, rangé par familles, mais pas dans quel ordre",
        "<b>1 — Rassembler nos idées</b> → organiser → <b>carte mentale</b>",
        "<b>2 — L'énergie du soleil jusqu'à la sirène</b> → un chemin, des transformations → <b>chaîne d'énergie</b>",
        "<b>3 — L'ordre du programme</b> → des étapes et un test (le vent dépasse-t-il le seuil&nbsp;?) → <b>algorigramme</b>",
        "<b>4 — Ce qui entoure la station</b> → l'objet au centre, ses interacteurs autour → <b>diagramme des interacteurs "
        "extérieurs</b> (diagramme pieuvre)",
        "<b>5 — Comparer deux modèles</b> → des valeurs côte à côte → <b>tableau</b>",
        "<b>6 — Réviser sur une page</b> → résumer, retenir → <b>carte mentale</b>",
        "Le piège de la question 4&nbsp;: le diagramme pieuvre ressemble à une carte mentale (un centre, des traits). Mais il "
        "montre des <b>interacteurs</b>, avec des fonctions, pas des idées rangées par familles.",
        "<b>Une explication attendue&nbsp;:</b> « La carte mentale range des idées autour d'un centre, mais elle ne montre pas le "
        "<b>chemin de l'énergie</b> du panneau solaire à la sirène&nbsp;: il faut une <b>chaîne d'énergie</b>. »",
        ("conclusion", "La carte mentale sert à <b>organiser et retenir</b>&nbsp;; pour montrer <b>comment ça marche</b> — ce qui "
                       "circule, dans quel ordre — on choisit une autre représentation."),
    ],
    retenir="la carte mentale <b>organise et fait retenir</b>&nbsp;; elle ne montre ni ce qui circule (chaîne d'énergie ou "
            "d'information), ni l'ordre des opérations (algorigramme).",
    piege="choisir la carte mentale pour tout&nbsp;: elle range des idées, elle n'explique pas comment l'objet fonctionne.",
)

# ─────────────────────────────────────────────────────────────────────────────
# Le cours, niveau par niveau
# ─────────────────────────────────────────────────────────────────────────────
COURS = {
    "5e": "<h3>Ce qu'est une carte mentale</h3><ul>"
          "<li>Un schéma qui part d'une <b>idée centrale</b>, écrite au milieu de la feuille&nbsp;: le sujet.</li>"
          "<li>Des <b>branches</b> partent du centre. Chacune porte un <b>mot</b> qui nomme une famille d'idées.</li>"
          "<li>Au bout des branches, les <b>feuilles</b>&nbsp;: une idée ou une donnée chacune, en quelques mots.</li>"
          "<li>On l'appelle aussi <b>carte heuristique</b>, et <i lang=\"en\">mind map</i> en anglais.</li></ul>"
          "<h3>La construire en cinq gestes</h3><ul>"
          "<li><b>Écrire le sujet</b> au centre.</li>"
          "<li><b>Recenser</b>&nbsp;: faire la liste de tout ce que l'on a, sans trier.</li>"
          "<li><b>Chercher les familles</b>&nbsp;: une branche par famille, avec un mot dessus.</li>"
          "<li><b>Ranger</b> chaque idée sur sa branche, en mots-clés.</li>"
          "<li><b>Relire</b>&nbsp;: ce qui ne va sur aucune branche est hors sujet, on l'enlève — pas de branche « Divers ».</li></ul>"
          "<h3>Les données d'un projet</h3><ul>"
          "<li>Une <b>donnée</b> est une information que l'on peut enregistrer dans un fichier&nbsp;: une image, des nombres, "
          "un texte, un programme, un dessin scanné.</li>"
          "<li>Un <b>objet</b> (la LED, la tablette, la carte programmable) n'est pas une donnée&nbsp;: on enregistre sa photo, "
          "pas l'objet.</li></ul>"
          "<h3>De la carte aux dossiers</h3>"
          '<div class="defile"><table><tr><th>Sur la carte mentale</th><th>Sur l\'ordinateur</th><th>Exemple</th></tr>'
          "<tr><td>l'idée centrale</td><td>le dossier du projet</td><td>Lampadaire</td></tr>"
          "<tr><td>une branche</td><td>un dossier rangé dedans</td><td>Mesures</td></tr>"
          "<tr><td>une feuille</td><td>un fichier</td><td>releves_mardi.csv</td></tr></table></div>"
          "<ul><li>En classe, tout commence par <b>Documents</b>, puis le <b>dossier de la classe</b>&nbsp;: "
          "Documents › 5eB › Lampadaire › Mesures › releves_mardi.csv. Cette suite s'appelle le <b>chemin</b> du fichier.</li>"
          "<li>L'<b>extension</b>, après le point, dit le format&nbsp;: <b>.jpg</b> une image, <b>.csv</b> un tableau de "
          "valeurs, <b>.odt</b> un texte. Le <b>nom</b> dit de quoi parle le fichier&nbsp;: sans espace ni accent, avec un "
          "numéro de séance ou de version.</li></ul>"
          "<h3>Ce qu'elle ne montre pas</h3><ul>"
          "<li>Ni ce qui circule dans un objet, ni l'ordre de ce qu'il fait&nbsp;: elle <b>range</b> des idées, elle ne "
          "décrit pas un fonctionnement.</li></ul>",
    "4e": "<h3>Organiser des arguments sur une évolution</h3><ul>"
          "<li>Au centre&nbsp;: l'<b>évolution</b> étudiée (de l'arrosoir à l'arrosage connecté).</li>"
          "<li>Deux branches face à face&nbsp;: <b>Avantages</b> et <b>Inconvénients</b>. D'autres branches peuvent dire "
          "<b>ce qui change</b> et <b>pour qui</b>.</li>"
          "<li>Un même fait peut être un avantage pour l'un et un inconvénient pour l'autre&nbsp;: on écrit pour qui.</li></ul>"
          "<h3>Avantage, inconvénient ou hors sujet&nbsp;?</h3><ul>"
          "<li><b>Avantage</b>&nbsp;: ce que l'évolution apporte de mieux (de l'eau économisée, du temps gagné…).</li>"
          "<li><b>Inconvénient</b>&nbsp;: ce qu'elle coûte ou rend fragile (l'argent, l'énergie, les pannes, la dépendance au "
          "réseau, les déchets…).</li>"
          "<li><b>Hors sujet</b>&nbsp;: une phrase vraie avant comme après l'évolution. Elle reste dehors.</li></ul>"
          "<h3>Une carte lisible</h3>"
          '<div class="defile"><table><tr><th>À faire</th><th>À éviter</th></tr>'
          "<tr><td>le sujet au centre</td><td>un titre vague (la classe, la date)</td></tr>"
          "<tr><td>un mot sur chaque branche, la couleur en plus</td><td>une branche reconnue à sa seule couleur</td></tr>"
          "<tr><td>des mots-clés dans les feuilles</td><td>des phrases entières</td></tr>"
          "<tr><td>une branche par famille</td><td>une branche « Divers » fourre-tout</td></tr>"
          "<tr><td>chaque idée dans sa branche</td><td>un avantage rangé dans les inconvénients</td></tr></table></div>"
          "<h3>Ce qu'elle ne montre pas</h3><ul>"
          "<li>Pas de flèches, pas d'ordre&nbsp;: ce n'est pas un défaut. Pour montrer ce qui circule ou dans quel ordre, on "
          "prend une chaîne d'énergie, une chaîne d'information ou un algorigramme.</li>"
          "<li>Elle ne fait pas partie du cahier des charges&nbsp;: elle aide à <b>préparer</b> et à <b>débattre</b>, elle "
          "n'exige rien de l'objet.</li></ul>",
    "3e":"<h3>De la carte à l'argumentaire</h3><ul>"
          "<li>La carte mentale <b>prépare</b> le texte&nbsp;: chaque branche est une idée possible.</li>"
          "<li>On choisit une branche <b>positive</b> et une branche <b>négative</b>, avec un exemple chacune.</li>"
          "<li>Un <b>argumentaire court</b> (5 à 8 lignes)&nbsp;: incidence positive et exemple → connecteur d'opposition, "
          "incidence négative et exemple → conclusion qui donne un avis nuancé.</li></ul>"
          "<h3>Les mots qui relient</h3>"
          '<div class="defile"><table><tr><th>Pour…</th><th>On écrit</th></tr>'
          "<tr><td>ajouter une idée</td><td>de plus, aussi, en outre</td></tr>"
          "<tr><td>opposer</td><td>mais, cependant, pourtant, en revanche, toutefois</td></tr>"
          "<tr><td>donner un exemple</td><td>par exemple, ainsi</td></tr>"
          "<tr><td>conclure</td><td>en conclusion, finalement, c'est pourquoi, donc</td></tr></table></div>"
          "<h3>Une incidence sur la société</h3><ul>"
          "<li>C'est un effet sur la vie des personnes&nbsp;: leur sécurité, leur argent, leur confiance, l'égalité entre "
          "celles qui ont un téléphone et celles qui n'en ont pas.</li>"
          "<li>Ce que l'objet mesure ou comment il marche n'est <b>pas</b> une incidence&nbsp;: c'est son fonctionnement.</li></ul>"
          "<h3>Choisir sa représentation</h3>"
          '<div class="defile"><table><tr><th>Pour…</th><th>On choisit</th></tr>'
          "<tr><td>organiser des idées, réviser, préparer un exposé</td><td>la carte mentale</td></tr>"
          "<tr><td>suivre le chemin de l'énergie</td><td>la chaîne d'énergie</td></tr>"
          "<tr><td>suivre le chemin de l'information</td><td>la chaîne d'information</td></tr>"
          "<tr><td>montrer l'ordre des opérations et les tests</td><td>l'algorigramme</td></tr>"
          "<tr><td>montrer ce qui entoure l'objet</td><td>le diagramme des interacteurs extérieurs (pieuvre)</td></tr>"
          "<tr><td>comparer des valeurs</td><td>un tableau</td></tr></table></div>",
}

# ─────────────────────────────────────────────────────────────────────────────
# Les trois niveaux
# ─────────────────────────────────────────────────────────────────────────────
NIVEAUX = {
    "5e": dict(
        codes=["5e_C1.4"],
        mission="Ranger les données d'un projet dans une carte mentale, puis dans les dossiers de l'ordinateur, pour les retrouver.",
        avant=[("Je sais ranger des mots ou des objets par familles, et dire ce qui les rassemble.",
                "cycle 3 — français et sciences", "@synthese#les-mots", "les mots de l'atelier, dans la synthèse (2 minutes)"),
               ("Je sais enregistrer un fichier dans un dossier, sur un ordinateur ou une tablette.",
                "cycle 3 — sciences et technologie", "@synthese#les-mots", "les mots de l'atelier, dans la synthèse (2 minutes)")],
        situation_titre="Une carte pour ne rien perdre",
        situation="<p>Un projet produit beaucoup de <b>données</b>&nbsp;: des photos, des mesures, des programmes, des comptes "
                  "rendus, des croquis. Au bout de trois séances, si rien n'est rangé, on ne retrouve plus rien. Pour "
                  "organiser tout cela, on dessine une <b>carte mentale</b>&nbsp;: le projet au centre, une branche par famille "
                  "de données. Le programme de technologie ne lui donne pas de nom&nbsp;; on l'appelle <b>carte mentale</b>, ou "
                  "<b>carte heuristique</b>.</p>"
                  "<p>Dans cet atelier, le projet est le <b>lampadaire intelligent</b> de la 5e B, pour une rue de Sainte-Luce.</p>",
        question="Comment ranger les données d'un projet pour les retrouver en quelques secondes, même trois mois plus tard&nbsp;?",
        hypothese_amorces=["Je pense qu'il faudrait d'abord…", "Pour retrouver un fichier, je rangerais…",
                           "Je crois qu'on peut regrouper les données par…"],
        exercices=[E1, E2],
        a_retenir="<ul><li>La <b>carte mentale</b> — ou <b>carte heuristique</b> — part d'une <b>idée centrale</b>&nbsp;; chaque "
                  "<b>branche</b> porte le nom d'une famille, chaque <b>feuille</b> une idée ou une donnée, en quelques mots.</li>"
                  "<li>Une <b>donnée</b> s'enregistre dans un fichier&nbsp;; un objet, non&nbsp;: on enregistre sa photo.</li>"
                  "<li>La carte donne l'<b>arborescence</b>&nbsp;: le dossier du projet au centre, un dossier par branche, un fichier "
                  "par feuille. Le <b>chemin</b> se lit du plus grand dossier au plus petit&nbsp;: Documents › 5eB › Lampadaire › "
                  "Mesures › releves_mardi.csv.</li>"
                  "<li>La carte mentale <b>range</b> des idées&nbsp;: elle ne montre ni ce qui circule ni l'ordre des opérations.</li></ul>",
        bonus=[dict(titre="La carte de ton cartable",
                    consigne="<p>Dessine sur ton cahier la carte mentale de ton cartable&nbsp;: au centre, « Mon cartable »&nbsp;; "
                             "<b>quatre branches</b> au moins, avec un mot chacune. Puis dis quel objet tu as eu du mal à ranger, "
                             "et pourquoi.</p>",
                    correction=["<b>Centre</b> → « Mon cartable »",
                                "<b>Des branches possibles</b> → Cahiers, Livres, Trousse, Affaires de sport, Goûter",
                                "<b>Feuilles</b> → en mots-clés&nbsp;: « cahier de techno », « règle 30 cm », « gourde »",
                                "<b>Un objet difficile</b> → la calculatrice&nbsp;: Trousse ou Maths&nbsp;? Les deux branches "
                                "se défendent&nbsp;: l'important est de choisir une famille et de s'y tenir.",
                                ("conclusion", "Classer, c'est choisir <b>une</b> famille pour chaque chose, et nommer chaque branche.")]),
                   dict(titre="Le bon nom de fichier",
                        consigne="<p>Trois noms pour la même photo&nbsp;: <b>IMG_2041.jpg</b>, <b>photo trucs final final.jpg</b>, "
                                 "<b>lampadaire_pluie_seance3.jpg</b>. Lequel choisis-tu, et pourquoi les deux autres posent-ils "
                                 "problème&nbsp;?</p>",
                        correction=["<b>lampadaire_pluie_seance3.jpg</b> → il dit ce que montre la photo et quand elle a été prise",
                                    "<b>IMG_2041.jpg</b> → le nom donné par la tablette&nbsp;: il ne dit rien du contenu",
                                    "<b>photo trucs final final.jpg</b> → vague, avec des espaces, et « final » ne dit pas quelle "
                                    "version",
                                    ("conclusion", "Un bon nom de fichier se lit comme une feuille de carte mentale&nbsp;: quelques "
                                                   "mots-clés qui disent le contenu.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre un objet et une donnée, ou entre deux branches pour un même "
                      "fichier. Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
    "4e": dict(
        codes=["4e_C1.2"],
        mission="Organiser sur une carte mentale les avantages et les inconvénients d'une évolution technologique, puis "
                "corriger une carte mal faite.",
        avant=[("Je sais ranger des idées dans les branches d'une carte mentale, autour d'une idée centrale.",
                "5e_C1.4", "@niveau:5e#cm_5e_e1", "l'atelier de 5e, exercice 1 (15 minutes)"),
               ("Je sais qu'une branche porte un mot qui nomme sa famille, et qu'une feuille s'écrit en quelques mots.",
                "5e_C1.4", "@niveau:5e#cm_5e_e1", "l'atelier de 5e, exercice 1 (15 minutes)")],
        situation_titre="Une évolution a toujours deux côtés",
        situation="<p>Quand un objet change — de l'arrosoir à l'arrosage connecté, de la clé au badge —, il apporte des "
                  "<b>avantages</b> et il a un <b>prix</b>&nbsp;: de l'argent, de l'énergie, des pannes nouvelles. Pour en "
                  "débattre sans rien oublier, on <b>organise</b> les arguments sur une <b>carte mentale</b>, qu'on appelle "
                  "aussi <b>carte heuristique</b>&nbsp;: l'évolution au centre, les avantages d'un côté, les inconvénients de "
                  "l'autre.</p>"
                  "<p>Dans cet atelier, l'évolution est le <b>système d'arrosage connecté</b> du jardin partagé du collège.</p>",
        question="Comment organiser les avantages et les inconvénients d'une évolution technologique pour en débattre "
                 "honnêtement&nbsp;?",
        hypothese_amorces=["Je pense qu'il faut séparer…", "Pour ne rien oublier, je regarderais…",
                           "Je crois qu'une phrase vraie peut quand même…"],
        exercices=[E3, E4],
        a_retenir="<ul><li>Pour juger une <b>évolution technologique</b>, on range sur une carte mentale ses <b>avantages</b> et "
                  "ses <b>inconvénients</b>, sur deux branches face à face.</li>"
                  "<li>Une phrase vraie qui ne dit rien de l'évolution est <b>hors sujet</b>&nbsp;: elle reste dehors.</li>"
                  "<li>Une carte lisible a un <b>sujet</b> au centre, un <b>mot</b> sur chaque branche (la couleur en plus, jamais "
                  "seule), des <b>mots-clés</b> dans les feuilles, et pas de branche « Divers ».</li>"
                  "<li>Elle n'a ni flèches ni ordre&nbsp;: elle organise des idées, elle ne montre pas comment l'objet "
                  "fonctionne.</li></ul>",
        bonus=[dict(titre="Le badge de la salle de technologie",
                    consigne="<p>Le collège remplace les clés de la salle de technologie par un badge. Dessine la carte mentale "
                             "de cette évolution&nbsp;: au centre l'évolution, <b>deux avantages</b> et <b>deux "
                             "inconvénients</b>, en mots-clés.</p>",
                    correction=["<b>Centre</b> → « Des clés au badge »",
                                "<b>Avantages</b> → « badge perdu désactivé », « on sait qui est entré »",
                                "<b>Inconvénients</b> → « bloqué si panne de courant », « des données sur les entrées »",
                                ("conclusion", "« On sait qui est entré » est un avantage pour le collège, mais aussi une donnée "
                                               "personnelle à protéger&nbsp;: un même fait peut aller des deux côtés.")]),
                   dict(titre="Pour qui est-ce un avantage ?",
                        consigne="<p>« Mme Joseph suit tout sur son téléphone. » Pour qui est-ce un avantage, et pour qui "
                                 "pourrait-ce être un inconvénient&nbsp;?</p>",
                        correction=["<b>Avantage</b> → pour Mme Joseph&nbsp;: elle sait ce qui se passe sans venir",
                                    "<b>Inconvénient possible</b> → pour les élèves du club&nbsp;: on a moins besoin d'eux, ils "
                                    "viennent moins voir les plantes",
                                    "<b>Inconvénient possible</b> → pour Mme Joseph aussi&nbsp;: des messages même pendant ses "
                                    "vacances",
                                    ("conclusion", "Sur la carte, on peut ajouter une branche « Pour qui&nbsp;? » pour ne pas "
                                                   "mélanger les points de vue.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre un avantage et un hors-sujet, ou entre un défaut et une chose "
                      "normale dans une carte. Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
    "3e": dict(
        codes=["3e_C1.3"],
        mission="Se servir d'une carte mentale pour écrire un argumentaire court sur l'incidence d'un objet sur la société, et "
                "savoir quand choisir une autre représentation.",
        avant=[("Je sais ranger des arguments en avantages et en inconvénients sur une carte mentale.",
                "4e_C1.2", "@niveau:4e#cm_4e_e3", "l'atelier de 4e, exercice 1 (15 minutes)"),
               ("Je sais reconnaître une phrase hors sujet, même quand elle est vraie.",
                "4e_C1.2", "@niveau:4e#cm_4e_e3", "l'atelier de 4e, exercice 1 (15 minutes)")],
        situation_titre="Une carte pour penser, un texte pour convaincre",
        situation="<p>Avant d'écrire un argumentaire, on rassemble ses idées. La <b>carte mentale</b> — ou <b>carte "
                  "heuristique</b> — permet de les voir toutes d'un coup, rangées par familles, et de <b>choisir</b> celles "
                  "que l'on gardera. Le texte vient ensuite&nbsp;: une idée par branche choisie, reliées par des mots qui "
                  "opposent et qui concluent.</p>"
                  "<p>Dans cet atelier, l'objet est la <b>station d'alerte cyclonique</b> de la commune.</p>",
        question="Comment passer d'une carte mentale à un argumentaire court et nuancé — et quand faut-il une autre "
                 "représentation&nbsp;?",
        hypothese_amorces=["Je pense qu'une carte mentale aide à…", "Pour écrire un argumentaire, je commencerais par…",
                           "Je crois que la carte mentale ne peut pas montrer…"],
        exercices=[E5, E6],
        a_retenir="<ul><li>La carte mentale <b>prépare</b> un argumentaire&nbsp;: on y choisit une branche positive et une branche "
                  "négative.</li>"
                  "<li>Un <b>argumentaire court</b>&nbsp;: une incidence positive, une incidence négative introduite par un "
                  "<b>connecteur d'opposition</b>, puis une <b>conclusion</b> qui donne un avis nuancé.</li>"
                  "<li>Une <b>incidence sur la société</b> est un effet sur la vie des personnes&nbsp;; ce que l'objet mesure est "
                  "son fonctionnement.</li>"
                  "<li>La carte mentale <b>organise et fait retenir</b>&nbsp;; pour montrer ce qui circule ou l'ordre des "
                  "opérations, on choisit une chaîne d'énergie, une chaîne d'information ou un algorigramme.</li></ul>",
        bonus=[dict(titre="La branche qui manque",
                    consigne="<p>La carte de la station n'a pas de branche « Environnement ». Propose-la, avec <b>deux "
                             "feuilles</b>, et dis si chacune est une incidence positive ou négative.</p>",
                    correction=["<b>Branche</b> → « Environnement »",
                                "<b>« panneau solaire »</b> → la station ne consomme pas d'électricité du réseau → plutôt positive",
                                "<b>« batterie à recycler »</b> → un déchet à traiter dans quelques années → négative",
                                ("conclusion", "Une nouvelle branche, c'est un nouvel angle&nbsp;: on l'ajoute à la carte avant "
                                               "d'écrire, pas après.")]),
                   dict(titre="Le contre-argumentaire",
                        consigne="<p>Un camarade écrit&nbsp;: « La station est inutile, car il y a déjà la radio. » Réponds-lui en "
                                 "deux phrases, avec un connecteur d'opposition et une idée de la carte.</p>",
                        correction=["« La radio prévient, <b>mais</b> il faut l'allumer au bon moment&nbsp;: la sirène, elle, "
                                    "réveille tout le quartier, même la nuit. »",
                                    "« <b>Pourtant</b>, la station prévient plus tôt&nbsp;: les pêcheurs ont le temps de rentrer "
                                    "les bateaux. »",
                                    ("conclusion", "Répondre à un argument, c'est en reconnaître la part juste, puis l'opposer à une "
                                                   "idée précise.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre une incidence et un fonctionnement, ou entre la carte mentale et "
                      "le diagramme pieuvre. Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
}

# ─────────────────────────────────────────────────────────────────────────────
# Ce que le reste du site lit de cet atelier
# ─────────────────────────────────────────────────────────────────────────────
MODULE = "carte_mentale"
NOM_PANNEAU = "carte_mentale"
PANNEAU_TEXTE = {
    "5e": "La <b>carte mentale</b> — on dit aussi <b>carte heuristique</b> — sur le projet lampadaire&nbsp;: tu recenses les "
          "données du projet, tu les ranges dans les branches de la carte, puis tu passes de la carte aux dossiers de "
          "l'ordinateur pour les stocker et les retrouver.",
    "4e": "La <b>carte mentale</b> — on dit aussi <b>carte heuristique</b> — sur l'arrosage connecté du jardin&nbsp;: tu "
          "organises les avantages et les inconvénients de cette évolution, puis tu corriges une carte mal faite.",
    "3e": "La <b>carte mentale</b> — on dit aussi <b>carte heuristique</b> — sur la station d'alerte cyclonique&nbsp;: tu tries "
          "ses feuilles, tu écris un argumentaire court sur son incidence sur la société, puis tu choisis quand une autre "
          "représentation convient mieux.",
}
IMAGES = {
    "carte_mentale_projet_lampadaire.svg": CM_PROJET_CORRIGE,
    "arborescence_lampadaire.svg": ARBO_A,
    "carte_mentale_arrosage_a_corriger.svg": CM_FAUTIVE,
    "carte_mentale_arrosage.svg": CM_ARROSAGE_CORRIGE,
    "carte_mentale_station_alerte.svg": CM_STATION,
}
SCHEMAS_SYNTHESE = {"5e": CM_PROJET_CORRIGE, "4e": CM_ARROSAGE_CORRIGE, "3e": CM_STATION}
VOCAB_EN = [("carte mentale", "mind map"), ("idée centrale", "central idea"), ("branche", "branch"),
            ("mot-clé", "keyword"), ("dossier", "folder"), ("fichier", "file"), ("arborescence", "file tree (directory tree)"),
            ("chemin", "path"), ("avantage", "advantage"), ("inconvénient", "drawback"),
            ("argumentaire", "argument (short essay)")]
VERBES = {"5e": "<b>recenser</b> et <b>classer</b> les données d'un projet dans une carte mentale, puis les <b>stocker</b> et les "
                "<b>retrouver</b> dans une arborescence de dossiers",
          "4e": "<b>organiser</b> les avantages et les inconvénients d'une évolution technologique, et <b>corriger</b> une carte "
                "mal construite",
          "3e": "<b>argumenter</b> à partir de la carte (argumentaire court, incidence sur la société), et <b>choisir</b> la carte "
                "mentale seulement quand il s'agit d'organiser ou de retenir"}
CHAINE = ("<p><b>Hors de la chaîne d'analyse.</b> La carte mentale n'est pas un maillon de l'analyse externe (besoin → "
          "interacteurs → exigences) ni de l'analyse interne (FAST, chaînes d'énergie et d'information)&nbsp;: c'est un outil "
          "de <b>synthèse et d'organisation</b>, utilisable à toutes les étapes — pour <b>recenser</b> (les données d'un projet, "
          "5e), pour <b>résumer</b> (un chapitre, une revue de projet), pour <b>préparer un argumentaire</b> (4e, 3e).</p>"
          "<p>Elle ne montre ni ce qui circule ni l'ordre des opérations&nbsp;: l'exercice 6 (3e) fait choisir entre elle et "
          "les représentations techniques.</p>")
NOTES_PROF = ("<ul><li>Le programme 2024 ne nomme pas la carte mentale&nbsp;: il demande d'« exprimer et structurer sa pensée en "
              "mobilisant le langage naturel et des outils de représentation » (thème 1) et, en 5e, de « recenser des données, "
              "les identifier, les classer, les représenter, les stocker, les retrouver dans une arborescence ». La carte mentale "
              "sert ces gestes&nbsp;; elle n'est jamais un objectif évalué pour elle-même.</li>"
              "<li>Codes servis&nbsp;: 5e_C1.4 (classer, arborescence), 4e_C1.2 (avantages et inconvénients d'une évolution), "
              "3e_C1.3 (argumentaire court). Chaque niveau a son objet-fil&nbsp;: le lampadaire intelligent, l'arrosage connecté "
              "du jardin, la station d'alerte cyclonique.</li>"
              "<li>Exercice 2 (5e)&nbsp;: la règle de rangement est celle de la classe — Documents, puis un dossier au nom de la "
              "classe. Adapter « 5eB » au nom réel de la classe si besoin.</li>"
              "<li>Source d'inspiration, jamais recopiée&nbsp;: le cahier « 123 Techno » (Bordas 2021). On en retient la place "
              "de la carte mentale parmi les outils de présentation (organiser des idées, synthèse de cours), les exercices « "
              "choisir la représentation adaptée à une situation », et la mécanique « problème / solution » sur un document mal "
              "fait (transposée en exercice 4). Écart assumé&nbsp;: le cahier de 5e range la carte mentale parmi les « outils de "
              "description d'un fonctionnement »&nbsp;; ici, elle est réservée à l'organisation des idées, et l'exercice 6 le fait "
              "dire à l'élève.</li>"
              "<li>Les cases à remplir des cartes vivantes (exercices 1 et 3) se choisissent dans une liste (une feuille = un "
              "choix)&nbsp;; la dernière feuille de l'exercice 3 s'écrit au clavier et apparaît dans la carte.</li>"
              "<li>En 4e et en 3e, l'élève n'a pas forcément fait le niveau précédent&nbsp;: l'ouverture renvoie aux exercices "
              "à rattraper.</li></ul>")
DEUX_NOMS = ("Le programme de technologie ne donne pas de nom à ce schéma&nbsp;: il demande d'exprimer et de structurer sa pensée "
             "avec des outils de représentation, et de classer des données. On l'appelle <b>carte mentale</b>, ou <b>carte "
             "heuristique</b> (du grec <i>heuriskein</i>, « trouver »)&nbsp;; en anglais, <i lang=\"en\">mind map</i>. Si tu "
             "rencontres l'un de ces noms, tu sauras que c'est le même schéma&nbsp;: une idée centrale, des branches, des feuilles.")
QCM_SOUS_TITRE = ("Recenser et classer des données dans une carte mentale, passer à l'arborescence de dossiers (5e) ; organiser "
                  "avantages et inconvénients, corriger une carte (4e) ; argumenter à partir d'une carte et choisir sa "
                  "représentation (3e)")
