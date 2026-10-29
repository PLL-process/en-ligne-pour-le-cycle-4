# -*- coding: utf-8 -*-
"""Atelier — Le diagramme des exigences (diagramme des exigences SysML).

Codes servis : 4e_C2.2, 4e_C8.3 (4e) ; 3e_C3.3 (3e). La carte des représentations le
classe « 4e / 3e, facultatif » : pas de 5e.
Objet de 4e : le système d'arrosage connecté du jardin partagé (il prolonge l'exercice 6
de l'atelier des interacteurs : critère, niveau, flexibilité). Objet de 3e : la station
d'alerte cyclonique.

Le verbe change d'un niveau à l'autre, pas la notion :
  4e  LIRE le diagramme, STRUCTURER une ligne du cahier des charges en bloc, RELIER chaque
      exigence au test qui la vérifie («verify») et valider un résultat avec la flexibilité ;
  3e  ÉVALUER deux solutions exigence par exigence («satisfy»), attribuer la flexibilité
      d'après ce que dit le client, puis ARBITRER.
"""
import figures

SLUG = "exigences-sysml"
COURT = "ex"
EMOJI = "📋"
TITRE = "Le diagramme des exigences"
TITRE_COURT = "le diagramme des exigences (diagramme des exigences SysML)"
TITRE_COMPLET = "Le diagramme des exigences, souvent appelé diagramme des exigences SysML"
ETIQUETTE = "📋 diagramme des exigences SysML"
ETIQUETTE_COURTE = "Exigences"
MENTION_FICTION = ("Situations imaginées pour les exercices : Mme Joseph, le jardin du collège et son prototype, les "
                   "résultats de ses tests, le comité de quartier, Mme Augustin, les boîtiers A, B et C, leurs valeurs "
                   "et leurs prix sont inventés. Les codes IP et l'indice de réparabilité, eux, existent vraiment.")

CATEGORIES_PROGRAMME = [("securite", "sécurité"), ("environnement", "incidences environnementales"),
                        ("formes", "formes et fonctions"), ("ergonomie", "ergonomie"), ("qualite", "qualité"),
                        ("fiabilite", "fiabilité")]

# ─────────────────────────────────────────────────────────────────────────────
# Les dessins (générateur commun : figures.exigences)
# ─────────────────────────────────────────────────────────────────────────────
VERT = "#16753a"
ORANGE = "#b35c00"

# 4e — le système d'arrosage : une exigence-mère, quatre filles (largeur des filles : 190).
MERE_ARROSAGE = dict(x=250, y=18, l=320, nom="Arrosage autonome", id="1",
                     texte="Le système doit arroser les plantes du jardin en l'absence de la gardienne.")
FILLES_ARROSAGE = {
    "f1": dict(x=14, y=200, l=190, nom="Étanchéité", id="1.1",
               texte="Le boîtier doit résister aux projections d'eau : IPX4 au moins."),
    "f2": dict(x=216, y=200, l=190, nom="Sobriété", id="1.2",
               texte="Le système doit utiliser au plus 10 L d'eau par jour."),
    "f3": dict(x=418, y=200, l=190, nom="Réglage", id="1.3",
               texte="L'heure d'arrosage doit se changer sans outil, en 2 min au plus."),
    "f4": dict(x=620, y=200, l=190, nom="Sécurité électrique", id="1.4",
               texte="Le système doit être alimenté en très basse tension : 12 V."),
}
CONTIENT_ARROSAGE = [("m", "f1"), ("m", "f2"), ("m", "f3"), ("m", "f4")]


def _blocs_arrosage():
    b = {"m": dict(MERE_ARROSAGE)}
    for k, v in FILLES_ARROSAGE.items():
        b[k] = dict(v)
    return b


DESC_ARROSAGE = ("En haut, au centre, le bloc d'exigence Id 1, nommé Arrosage autonome : le système doit arroser les "
                 "plantes du jardin en l'absence de la gardienne. De son bord inférieur, un petit cercle à croix part "
                 "vers quatre blocs placés en dessous, de gauche à droite : Id 1.1, Étanchéité, le boîtier doit résister "
                 "aux projections d'eau, IPX4 au moins ; Id 1.2, Sobriété, au plus 10 L d'eau par jour ; Id 1.3, Réglage, "
                 "l'heure d'arrosage doit se changer sans outil, en 2 min au plus ; Id 1.4, Sécurité électrique, très "
                 "basse tension, 12 V. Chaque bloc porte en haut le mot requirement.")

EX_ARROSAGE = figures.exigences(
    "ex-arrosage", _blocs_arrosage(),
    "Diagramme des exigences du système d'arrosage du jardin",
    DESC_ARROSAGE, contient=CONTIENT_ARROSAGE, largeur=820, hauteur=340)

# 4e — les mêmes exigences, avec sous chacune le test qui la vérifie (corrigé de l'exercice 3).
TESTS_ARROSAGE = {
    "t3": dict(x=14, y=410, l=190, nom="Essai à l'arroseur", id="T3", stereotype="testCase", couleur=VERT,
               texte="Arroser le boîtier fermé 10 min de tous côtés : aucune goutte dedans."),
    "t1": dict(x=216, y=410, l=190, nom="Relevé du compteur", id="T1", stereotype="testCase", couleur=VERT,
               texte="Relever le compteur d'eau sur 24 h : 10 L au plus."),
    "t4": dict(x=418, y=410, l=190, nom="Réglage chronométré", id="T4", stereotype="testCase", couleur=VERT,
               texte="Chronométrer le réglage, noter les outils : aucun outil, 2 min au plus."),
    "t2": dict(x=620, y=410, l=190, nom="Mesure au multimètre", id="T2", stereotype="testCase", couleur=VERT,
               texte="Mesurer la tension d'alimentation au multimètre : 12 V."),
}


def _blocs_tests():
    b = _blocs_arrosage()
    for k, v in TESTS_ARROSAGE.items():
        b[k] = dict(v)
    return b


EX_ARROSAGE_TESTS = figures.exigences(
    "ex-arrosage-tests", _blocs_tests(),
    "Diagramme des exigences du système d'arrosage, avec le test qui vérifie chaque exigence",
    DESC_ARROSAGE + " Sous chacun des quatre blocs, un bloc vert marqué testCase, relié à lui par une flèche en tirets "
    "nommée verify, qui monte du test vers l'exigence : sous 1.1, T3, essai à l'arroseur, 10 minutes de tous côtés, "
    "aucune goutte dedans ; sous 1.2, T1, relevé du compteur d'eau sur 24 heures, 10 litres au plus ; sous 1.3, T4, "
    "réglage chronométré, aucun outil, 2 minutes au plus ; sous 1.4, T2, mesure de la tension au multimètre, 12 volts.",
    contient=CONTIENT_ARROSAGE,
    relations=[("t3", "f1", "verify"), ("t1", "f2", "verify"), ("t4", "f3", "verify"), ("t2", "f4", "verify")],
    largeur=820, hauteur=548)

# 4e — exercice 2 : deux exigences-mères, deux blocs à remplir (vivants), puis le corrigé.
MERES_SUIVI = {
    "m1": dict(x=20, y=18, l=330, nom="Arrosage autonome", id="1",
               texte="Le système doit arroser les plantes du jardin en l'absence de la gardienne."),
    "m2": dict(x=470, y=18, l=330, nom="Suivi à distance", id="2",
               texte="La gardienne doit pouvoir suivre l'arrosage sur son smartphone, où qu'elle soit."),
}
TEXTE_A = "Le compte rendu doit arriver sur le smartphone 5 min au plus après chaque arrosage."
TEXTE_B = "Une alerte doit partir sur le smartphone dès qu'il reste 50 L dans la cuve."
TEXTE_VAGUE = "Le système doit prévenir la gardienne assez vite quand il le faut."
TEXTE_SOLUTION = "Le boîtier doit contenir une carte Wi-Fi pour envoyer les messages."
NOMS_E2 = ["Compte rendu", "Alerte cuve", "Carte Wi-Fi", "Smartphone"]
TEXTES_E2 = [TEXTE_A, TEXTE_B, TEXTE_VAGUE, TEXTE_SOLUTION]


def _blocs_suivi(corrige):
    b = {k: dict(v) for k, v in MERES_SUIVI.items()}
    if corrige:
        b["a"] = dict(x=110, y=232, l=270, nom="Compte rendu", id="2.1", texte=TEXTE_A)
        b["b"] = dict(x=440, y=232, l=270, nom="Alerte cuve", id="2.2", texte=TEXTE_B)
    else:
        b["a"] = dict(x=110, y=232, l=270, nom="", id="? (bloc A)", texte="",
                      vivants={"nom": "ex-a-nom", "texte": "ex-a-texte"})
        b["b"] = dict(x=440, y=232, l=270, nom="", id="? (bloc B)", texte="",
                      vivants={"nom": "ex-b-nom", "texte": "ex-b-texte"})
    return b


DESC_SUIVI = ("En haut, deux blocs d'exigence côte à côte. À gauche, Id 1, Arrosage autonome : le système doit arroser "
              "les plantes en l'absence de la gardienne. À droite, Id 2, Suivi à distance : la gardienne doit pouvoir "
              "suivre l'arrosage sur son smartphone, où qu'elle soit. ")

EX_SUIVI = figures.exigences(
    "ex-suivi", _blocs_suivi(False),
    "Deux exigences-mères et deux blocs d'exigence à remplir",
    DESC_SUIVI + "En bas, deux blocs encore vides, le bloc A à gauche et le bloc B à droite ; leur Id est un point "
    "d'interrogation. Aucun trait ne les relie encore aux exigences-mères. Tes choix s'écrivent dans leur nom et leur texte.",
    largeur=820, hauteur=372)

EX_SUIVI_C = figures.exigences(
    "ex-suivi-c", _blocs_suivi(True),
    "Diagramme des exigences du suivi à distance, corrigé",
    DESC_SUIVI + "En bas, deux blocs reliés au bloc Id 2 par des traits qui partent de son petit cercle à croix : Id 2.1, "
    "Compte rendu, le compte rendu doit arriver sur le smartphone 5 minutes au plus après chaque arrosage ; Id 2.2, "
    "Alerte cuve, une alerte doit partir sur le smartphone dès qu'il reste 50 litres dans la cuve. Aucun trait ne relie "
    "ces deux blocs au bloc Id 1.",
    contient=[("m2", "a"), ("m2", "b")], largeur=820, hauteur=372)

# 3e — la station d'alerte cyclonique : une exigence-mère, cinq filles (largeur des filles : 154).
MERE_STATION = dict(x=230, y=18, l=360, nom="Alerte cyclonique", id="1",
                    texte="La station doit alerter les habitants du quartier à l'approche d'un cyclone.")
FILLES_STATION = {
    "s1": dict(x=9, y=200, l=154, nom="Étanchéité", id="1.1", texte="Le boîtier doit être IP65 au moins."),
    "s2": dict(x=172, y=200, l=154, nom="Autonomie", id="1.2", texte="La station doit tenir 72 h au moins sur batterie."),
    "s3": dict(x=335, y=200, l=154, nom="Alerte audible", id="1.3", texte="L'alerte doit s'entendre à 100 m au moins."),
    "s4": dict(x=498, y=200, l=154, nom="Réparabilité", id="1.4",
               texte="L'indice de réparabilité doit valoir 6/10 au moins."),
    "s5": dict(x=661, y=200, l=154, nom="Coût", id="1.5", texte="Le boîtier doit coûter 300 € au plus."),
}
CONTIENT_STATION = [("m", k) for k in ("s1", "s2", "s3", "s4", "s5")]


def _blocs_station(solution=None):
    b = {"m": dict(MERE_STATION)}
    for k, v in FILLES_STATION.items():
        b[k] = dict(v)
    if solution:
        b["sol"] = dict(solution)
    return b


DESC_STATION = ("En haut, au centre, le bloc d'exigence Id 1, Alerte cyclonique : la station doit alerter les habitants "
                "du quartier à l'approche d'un cyclone. De son petit cercle à croix partent cinq traits vers cinq blocs, "
                "de gauche à droite : Id 1.1, Étanchéité, le boîtier doit être IP65 au moins ; Id 1.2, Autonomie, la "
                "station doit tenir 72 heures au moins sur batterie ; Id 1.3, Alerte audible, l'alerte doit s'entendre à "
                "100 mètres au moins ; Id 1.4, Réparabilité, l'indice de réparabilité doit valoir 6 sur 10 au moins ; "
                "Id 1.5, Coût, le boîtier doit coûter 300 euros au plus.")

EX_STATION = figures.exigences(
    "ex-station", _blocs_station(),
    "Diagramme des exigences de la station d'alerte cyclonique",
    DESC_STATION, contient=CONTIENT_STATION, largeur=820, hauteur=340)

BOITIER_A = dict(x=285, y=420, l=250, nom="Boîtier A", id="A", stereotype="block", couleur=ORANGE,
                 texte="Déclaré : IP66, 80 h, 110 m, réparabilité 5/10, 290 €.")
BOITIER_B = dict(x=285, y=420, l=250, nom="Boîtier B", id="B", stereotype="block", couleur=ORANGE,
                 texte="Déclaré : IP54, 72 h, 150 m, réparabilité 9/10, 240 €.")

EX_STATION_A = figures.exigences(
    "ex-station-a", _blocs_station(BOITIER_A),
    "Ce que le boîtier A satisfait : les flèches satisfy",
    DESC_STATION + " En bas, au centre, un bloc orange marqué block : le boîtier A, déclaré IP66, 80 heures, 110 mètres, "
    "réparabilité 5 sur 10, 290 euros. Quatre flèches en tirets nommées satisfy montent de lui vers les exigences 1.1, "
    "1.2, 1.3 et 1.5. Aucune flèche ne va vers 1.4, la réparabilité.",
    contient=CONTIENT_STATION,
    relations=[("sol", "s1", "satisfy"), ("sol", "s2", "satisfy"), ("sol", "s3", "satisfy"), ("sol", "s5", "satisfy")],
    largeur=820, hauteur=558)

EX_STATION_B = figures.exigences(
    "ex-station-b", _blocs_station(BOITIER_B),
    "Ce que le boîtier B satisfait : les flèches satisfy",
    DESC_STATION + " En bas, au centre, un bloc orange marqué block : le boîtier B, déclaré IP54, 72 heures, 150 mètres, "
    "réparabilité 9 sur 10, 240 euros. Quatre flèches en tirets nommées satisfy montent de lui vers les exigences 1.2, "
    "1.3, 1.4 et 1.5. Aucune flèche ne va vers 1.1, l'étanchéité.",
    contient=CONTIENT_STATION,
    relations=[("sol", "s2", "satisfy"), ("sol", "s3", "satisfy"), ("sol", "s4", "satisfy"), ("sol", "s5", "satisfy")],
    largeur=820, hauteur=558)

# ─────────────────────────────────────────────────────────────────────────────
# Les tableaux répétés (chaque exercice se suffit à lui-même : il peut être posé seul dans une séquence)
# ─────────────────────────────────────────────────────────────────────────────
TABLE_VALEURS = ('<div class="defile"><table><caption>Les deux boîtiers proposés : valeurs déclarées par leurs fabricants '
                 '(inventées pour l\'exercice)</caption>'
                 '<tr><th>Exigence</th><th>Niveau demandé</th><th>Boîtier A</th><th>Boîtier B</th></tr>'
                 '<tr><td>1.1 Étanchéité — indice de protection</td><td>IP65 au moins</td><td>IP66</td><td>IP54</td></tr>'
                 '<tr><td>1.2 Autonomie sur batterie</td><td>72&nbsp;h au moins</td><td>80&nbsp;h</td><td>72&nbsp;h</td></tr>'
                 '<tr><td>1.3 Distance où l\'alerte s\'entend</td><td>100&nbsp;m au moins</td><td>110&nbsp;m</td><td>150&nbsp;m</td></tr>'
                 '<tr><td>1.4 Indice de réparabilité</td><td>6/10 au moins</td><td>5/10</td><td>9/10</td></tr>'
                 '<tr><td>1.5 Coût du boîtier</td><td>300&nbsp;€ au plus</td><td>290&nbsp;€</td><td>240&nbsp;€</td></tr>'
                 '</table></div>')

# ─────────────────────────────────────────────────────────────────────────────
# 4e
# ─────────────────────────────────────────────────────────────────────────────
MOT_SYSML = ("SysML", "sigle de l'anglais <i>Systems Modeling Language</i>, « langage de modélisation des systèmes »&nbsp;: "
             "une façon normalisée de dessiner un système technique, que les ingénieurs du monde entier lisent de la même "
             "façon. Le diagramme des exigences est l'un de ses schémas.")
MOT_DIAGRAMME = ("diagramme des exigences", "le schéma qui dessine les exigences d'un système dans des blocs, et les liens "
                 "entre elles. On l'appelle souvent diagramme des exigences SysML.")
MOT_EXIGENCE = ("exigence", "ce que le système doit faire ou respecter, écrit pour qu'on puisse le vérifier&nbsp;: avec un "
                "critère et un niveau.")
MOT_REQUIREMENT = ("bloc «&nbsp;requirement&nbsp;»", "le rectangle d'une exigence&nbsp;; <i>requirement</i> est le mot anglais "
                   "pour exigence.")
MOT_ID = ("Id", "abréviation de l'anglais <i>identifier</i>, « identifiant »&nbsp;: le numéro unique d'une exigence (1, 1.1, 1.2…).")
MOT_TEXT = ("Text", "la phrase de l'exigence, écrite dans le bas du bloc&nbsp;; <i>text</i> est le mot anglais pour texte.")
MOT_CONTENANCE = ("contenance (⊕)", "le lien entre une exigence-mère et ses exigences-filles. Le petit cercle à croix ⊕ est "
                  "du côté de la mère&nbsp;: elle contient les filles.")
MOT_CRITERE = ("critère", "ce que l'on mesure ou contrôle pour savoir si l'exigence est respectée (un volume d'eau, une durée…).")
MOT_NIVEAU = ("niveau", "la valeur à atteindre pour ce critère&nbsp;: au moins…, au plus…")

E1 = dict(
    id="e1", titre="Lire le diagramme des exigences du jardin", code="4e_C2.2", duree=10,
    objectif="lire un diagramme des exigences&nbsp;: ce que disent l'Id et le lien ⊕, où sont le critère et le niveau, et "
             "à quelle catégorie du programme appartient chaque exigence.",
    production="deux réponses sur la lecture du diagramme, le tri de quatre morceaux de texte (critère ou niveau) et le "
               "classement de quatre exigences.",
    mots=[MOT_SYSML, MOT_DIAGRAMME, MOT_EXIGENCE, MOT_REQUIREMENT, MOT_ID, MOT_TEXT, MOT_CONTENANCE, MOT_CRITERE, MOT_NIVEAU,
          ("indice de protection (IP)", "un code fixé par une norme internationale, le même chez tous les fabricants&nbsp;; "
           "IPX4 veut dire&nbsp;: résiste aux projections d'eau venant de tous les côtés."),
          ("très basse tension", "une tension électrique assez faible pour ne pas être dangereuse au toucher, comme "
           "12&nbsp;volts (V)&nbsp;; le 230&nbsp;V de la maison, lui, est dangereux."),
          ("fiabilité", "la capacité de l'objet à continuer de fonctionner, sans panne, longtemps et par tous les temps."),
          ("incidences environnementales", "les effets de l'objet sur la planète&nbsp;: eau, énergie, déchets…")],
    documents=[dict(svg=EX_ARROSAGE, legende="Le diagramme des exigences du système d'arrosage du jardin.",
                    description="<p>En haut, l'exigence-mère <b>Id 1 — Arrosage autonome</b>&nbsp;: le système doit arroser "
                                "les plantes du jardin en l'absence de la gardienne.</p>"
                                "<p>Elle contient quatre exigences-filles (le petit cercle à croix est sous elle)&nbsp;:</p><ul>"
                                "<li><b>Id 1.1 — Étanchéité</b>&nbsp;: le boîtier doit résister aux projections d'eau, IPX4 au moins.</li>"
                                "<li><b>Id 1.2 — Sobriété</b>&nbsp;: le système doit utiliser au plus 10&nbsp;L d'eau par jour.</li>"
                                "<li><b>Id 1.3 — Réglage</b>&nbsp;: l'heure d'arrosage doit se changer sans outil, en 2&nbsp;min au plus.</li>"
                                "<li><b>Id 1.4 — Sécurité électrique</b>&nbsp;: le système doit être alimenté en très basse tension, 12&nbsp;V.</li></ul>")],
    intro="<p>Le jardin partagé du collège a un <b>système d'arrosage connecté</b>&nbsp;: il arrose les plantes à l'heure "
          "choisie, avec l'eau d'une cuve, quand la gardienne, Mme Joseph, n'est pas là. Son cahier des charges range ses "
          "exigences dans un tableau. On peut aussi les <b>dessiner</b>&nbsp;: c'est le <b>diagramme des exigences</b>, "
          "qu'on appelle souvent <b>diagramme des exigences SysML</b>. SysML veut dire <i>Systems Modeling Language</i>, "
          "« langage de modélisation des systèmes »&nbsp;: des schémas que les ingénieurs du monde entier lisent de la "
          "même façon.</p>",
    consigne="<p><b>Un bloc d'exigence</b>, c'est chaque rectangle. En haut, le mot «&nbsp;requirement&nbsp;» (exigence, en "
             "anglais) et le <b>nom</b> de l'exigence. Dessous, l'<b>Id</b> — son identifiant, un numéro — puis sa phrase, "
             "le <b>texte</b>. Le trait qui part d'un petit cercle à croix ⊕ est un lien de <b>contenance</b>&nbsp;: "
             "l'exigence-mère, du côté du ⊕, contient les exigences-filles.</p>"
             "<p><b>Le texte</b> d'une exigence porte un <b>critère</b> (ce qu'on mesure) et un <b>niveau</b> (la valeur à "
             "atteindre). Le programme range les exigences en catégories&nbsp;: <b>sécurité</b> (ne blesser personne), "
             "<b>incidences environnementales</b> (les effets sur la planète&nbsp;: eau, énergie, déchets), <b>formes et "
             "fonctions</b>, <b>ergonomie</b> (facile et confortable à utiliser), <b>qualité</b>, <b>fiabilité</b> "
             "(fonctionner sans panne, par tous les temps).</p>"
             "<p><b>Réponds aux deux questions de lecture, trie les quatre morceaux de texte (critère ou niveau), puis "
             "range chaque exigence-fille dans sa catégorie.</b></p>",
    critere="dix réponses justes&nbsp;; tu sais dire pourquoi l'exigence 1 n'est satisfaite que si ses quatre filles le sont.",
    widgets=[dict(type="choix", name="id", legende="Que t'apprend «&nbsp;Id = 1.3&nbsp;», dans le bloc Réglage&nbsp;?",
                  options=[("fille", "C'est la troisième exigence contenue dans l'exigence 1."),
                           ("duree", "Le réglage doit durer 1,3&nbsp;minute au plus."),
                           ("rang", "C'est la troisième exigence la plus importante du jardin."),
                           ("version", "C'est la troisième version de l'exigence, corrigée une fois.")],
                  bonne="fille",
                  retours={"duree": "La durée du réglage est dans le texte (2 min au plus) ; l'Id est un numéro, pas une mesure.",
                           "rang": "L'Id ne classe pas les exigences par importance : 1.3 dit seulement sa place sous l'exigence 1.",
                           "version": "Un Id ne compte pas les corrections : il range l'exigence dans l'arbre.",
                           "fille": "Oui : 1 est l'exigence-mère, et .3 dit que Réglage est sa troisième fille."}),
             dict(type="choix", name="mere", legende="Quand peut-on dire que l'exigence 1, «&nbsp;Arrosage autonome&nbsp;», est satisfaite&nbsp;?",
                  options=[("toutes", "Quand ses quatre exigences-filles sont satisfaites."),
                           ("une", "Dès qu'une de ses exigences-filles est satisfaite."),
                           ("securite", "Quand l'exigence de sécurité est satisfaite&nbsp;: c'est la plus grave."),
                           ("seule", "On la teste seule, sans regarder ses exigences-filles.")],
                  bonne="toutes",
                  retours={"une": "Un boîtier très sobre mais qui prend l'eau n'arroserait pas longtemps : une seule fille ne suffit pas.",
                           "securite": "La sécurité compte beaucoup, mais un système sûr qui gaspille l'eau ne tient pas l'exigence 1.",
                           "seule": "L'exigence 1 n'a ni critère ni niveau à elle : ce sont ses filles qui la précisent.",
                           "toutes": "Oui : la mère contient ses filles. Elle est satisfaite quand toutes ses filles le sont."}),
             dict(type="classer", name="cn",
                  categories=[("critere", "le critère&nbsp;: ce qu'on mesure"), ("niveau", "le niveau&nbsp;: la valeur à atteindre")],
                  items=[("Dans 1.2&nbsp;: «&nbsp;le volume d'eau utilisé par jour&nbsp;»", "critere",
                          "Le volume d'eau : c'est ce qu'on mesure, pas la valeur à atteindre."),
                         ("Dans 1.2&nbsp;: «&nbsp;au plus 10&nbsp;L&nbsp;»", "niveau",
                          "« Au plus 10 L » : un nombre et son unité, c'est la valeur à ne pas dépasser."),
                         ("Dans 1.1&nbsp;: «&nbsp;l'indice de protection contre l'eau&nbsp;»", "critere",
                          "L'indice de protection : c'est ce qu'on contrôle sur le boîtier."),
                         ("Dans 1.1&nbsp;: «&nbsp;IPX4 au moins&nbsp;»", "niveau",
                          "« IPX4 au moins » : c'est la valeur à atteindre, le seuil.")]),
             dict(type="classer", name="cat", categories=CATEGORIES_PROGRAMME,
                  items=[("1.1 Étanchéité — IPX4 au moins", "fiabilite",
                          "1.1 : si l'eau entre, le boîtier tombe en panne. Quelle catégorie parle de fonctionner sans panne, par tous les temps ?"),
                         ("1.2 Sobriété — au plus 10&nbsp;L d'eau par jour", "environnement",
                          "1.2 : il s'agit de ne pas gaspiller l'eau. Quelle catégorie parle des effets sur la planète ?"),
                         ("1.3 Réglage — sans outil, en 2&nbsp;min au plus", "ergonomie",
                          "1.3 : il s'agit d'un geste facile pour la gardienne. Quelle catégorie parle de facilité d'usage ?"),
                         ("1.4 Sécurité électrique — très basse tension, 12&nbsp;V", "securite",
                          "1.4 : il s'agit que personne ne s'électrocute au jardin.")])],
    aides=["<p>Pour l'Id, lis-le de gauche à droite&nbsp;: le premier chiffre est la mère, le chiffre après le point est le "
           "rang de la fille. Pour critère ou niveau, cherche le <b>nombre</b>&nbsp;: là où il y a un nombre et son unité "
           "(ou un seuil comme IPX4), c'est le niveau. Pour les catégories, demande-toi&nbsp;: <b>qu'est-ce qui irait mal</b> "
           "si l'exigence n'était pas tenue&nbsp;?</p>",
           "<p>Id 1.3 → 1 = la mère → .3 = sa troisième fille.<br>"
           "La mère contient ses filles → elle n'est tenue que si <b>toutes</b> ses filles le sont.<br>"
           "«&nbsp;Le volume d'eau par jour&nbsp;» → on le mesure → <b>critère</b>. «&nbsp;Au plus 10&nbsp;L&nbsp;» → un nombre "
           "et son unité → <b>niveau</b>.<br>"
           "1.4 non tenue → quelqu'un peut s'électrocuter → <b>sécurité</b>. 1.2 non tenue → de l'eau gaspillée → "
           "<b>incidences environnementales</b>.</p>"],
    jumeau=dict(consigne="Dans le même diagramme, on ajoute le bloc «&nbsp;Id = 1.5 — Discrétion&nbsp;: la pompe doit faire "
                         "au plus 35&nbsp;dB à 1&nbsp;m, la nuit&nbsp;» (décibels). Qui est sa mère&nbsp;? Quel est son "
                         "critère, quel est son niveau&nbsp;?",
                correction="Sa mère est l'exigence <b>1</b> (Id 1.5 = cinquième fille de 1). Critère&nbsp;: <b>le niveau "
                           "sonore à 1&nbsp;m, la nuit</b> (ce qu'on mesure). Niveau&nbsp;: <b>au plus 35&nbsp;dB</b> (la "
                           "valeur à ne pas dépasser). Catégorie possible&nbsp;: incidences environnementales — le bruit "
                           "est une nuisance pour les voisins."),
    correction=[
        "<b>Id = 1.3</b> → 1 = l'exigence-mère → .3 = sa <b>troisième fille</b>",
        "Les trois autres lectures ne tiennent pas&nbsp;: la durée est dans le texte (2&nbsp;min au plus)&nbsp;; l'Id ne "
        "classe pas par importance&nbsp;; il ne compte pas les versions.",
        "<b>L'exigence 1</b> → elle contient 1.1, 1.2, 1.3 et 1.4 → elle est satisfaite seulement si <b>les quatre</b> "
        "le sont&nbsp;: un boîtier sobre qui prend l'eau, ou sûr qui gaspille, ne tient pas l'arrosage autonome.",
        "<b>«&nbsp;Le volume d'eau utilisé par jour&nbsp;»</b> → ce qu'on mesure → <b>critère</b>&nbsp;; "
        "<b>«&nbsp;au plus 10&nbsp;L&nbsp;»</b> → la valeur à ne pas dépasser → <b>niveau</b>",
        "<b>«&nbsp;L'indice de protection&nbsp;»</b> → ce qu'on contrôle → <b>critère</b>&nbsp;; <b>«&nbsp;IPX4 au "
        "moins&nbsp;»</b> → le seuil → <b>niveau</b>",
        "<b>1.1 Étanchéité</b> → si l'eau entre, le boîtier tombe en panne après une averse → <b>fiabilité</b>",
        "<b>1.2 Sobriété</b> → ne pas gaspiller l'eau de la cuve → <b>incidences environnementales</b>",
        "<b>1.3 Réglage</b> → un geste facile, sans tournevis → <b>ergonomie</b>",
        "<b>1.4 Sécurité électrique</b> → la très basse tension ne blesse pas au toucher, même sous la pluie → <b>sécurité</b>",
        "«&nbsp;Formes et fonctions&nbsp;» et «&nbsp;qualité&nbsp;» sont aussi des catégories du programme&nbsp;: aucune "
        "des quatre exigences n'en relève ici.",
        ("conclusion", "Un bloc se lit en trois temps&nbsp;: <b>son nom</b>, <b>son Id</b> (sa place dans l'arbre), <b>son "
                       "texte</b> (critère + niveau). La mère n'est tenue que si toutes ses filles le sont."),
    ],
    retenir="dans un diagramme des exigences, chaque bloc a un <b>nom</b>, un <b>Id</b> et un <b>texte</b> avec critère et "
            "niveau&nbsp;; le lien ⊕ dit qu'une exigence-mère <b>contient</b> ses filles, et n'est tenue que si toutes le sont.",
    piege="lire l'Id comme une mesure ou un rang d'importance&nbsp;: c'est seulement la place de l'exigence dans l'arbre.",
)

E2 = dict(
    id="e2", titre="Du cahier des charges au bloc d'exigence", code="4e_C2.2", duree=12,
    objectif="transformer une ligne du cahier des charges en bloc d'exigence, et le ranger sous la bonne exigence-mère.",
    production="le nom et le texte de deux blocs, leur exigence-mère avec leur Id, et la raison d'un refus.",
    mots=[MOT_SYSML, MOT_ID, MOT_CONTENANCE,
          ("cahier des charges", "le document qui rassemble ce que le client demande à l'objet&nbsp;: chaque fonction y "
           "reçoit un critère, un niveau et une flexibilité."),
          ("désignation", "dans le cahier des charges, la phrase de la fonction, avec un verbe à l'infinitif."),
          MOT_CRITERE, MOT_NIVEAU,
          ("flexibilité", "l'écart accepté autour du niveau, noté par une classe de F0 (impératif) à F3 (très négociable)."),
          ("solution technique", "la façon concrète de répondre à une exigence&nbsp;: un composant, un matériau, un "
           "programme. Elle dit <b>comment</b>&nbsp;; l'exigence dit <b>ce que</b> le système doit faire."),
          ("cuve", "un grand réservoir&nbsp;; ici, il recueille l'eau de pluie du toit.")],
    intro="<p>Deux lignes s'ajoutent au cahier des charges du système d'arrosage. Elles concernent le smartphone de la "
          "gardienne, Mme Joseph.</p>"
          '<div class="defile"><table><caption>Extrait du cahier des charges du système d\'arrosage</caption>'
          "<tr><th>Fonction</th><th>Désignation</th><th>Critère</th><th>Niveau</th><th>Flexibilité</th></tr>"
          "<tr><td>FC (vers le smartphone)</td><td>Envoyer un compte rendu après chaque arrosage</td>"
          "<td>Temps entre la fin de l'arrosage et l'arrivée du message</td><td>5&nbsp;min au plus</td><td>F2</td></tr>"
          "<tr><td>FC (vers la cuve)</td><td>Prévenir la gardienne quand la cuve est presque vide</td>"
          "<td>Volume d'eau qui reste dans la cuve quand l'alerte part</td><td>50&nbsp;L</td><td>F1</td></tr>"
          "</table></div>"
          "<p>FC veut dire <b>fonction contrainte</b>&nbsp;: une condition que le système doit respecter face à un seul "
          "élément extérieur. Le diagramme ci-dessous a déjà deux exigences-mères, et deux blocs vides, A et B.</p>",
    consigne="<p>Un bloc d'exigence a un <b>nom</b> court et un <b>texte</b>&nbsp;: une phrase qui dit ce que le système doit "
             "faire, avec le <b>critère</b> (ce qu'on mesure) et le <b>niveau</b> (la valeur à atteindre) de la ligne du "
             "cahier des charges.</p>"
             "<p><b>Remplis le bloc A avec la première ligne du tableau et le bloc B avec la seconde</b>&nbsp;: choisis le "
             "nom, puis le texte. Tes choix s'écrivent dans le schéma. <b>Dis ensuite</b> sous quelle exigence-mère ils se "
             "rangent, avec quel Id, et <b>pourquoi</b> un des textes proposés n'a sa place dans aucun bloc.</p>",
    critere="six réponses justes&nbsp;; chaque texte choisi contient un nombre et son unité, et tu sais dire pourquoi la "
            "carte Wi-Fi n'est pas une exigence.",
    widgets=[dict(type="slots", intro='<figure class="figure schema-vivant">' + EX_SUIVI +
                  '<figcaption>Deux exigences-mères, deux blocs à remplir. Tes choix s\'écrivent dans les blocs A et B.</figcaption></figure>',
                  slots=[dict(name="anom", cible="ex-a-nom", legende="Bloc A — son <b>nom</b> (première ligne du tableau)",
                              options=NOMS_E2, bonnes=["Compte rendu"],
                              indice="Bloc A, le nom : un mot court qui résume « envoyer un compte rendu après chaque arrosage »."),
                         dict(name="atexte", cible="ex-a-texte", legende="Bloc A — son <b>texte</b>",
                              options=TEXTES_E2, bonnes=[TEXTE_A],
                              indice="Bloc A, le texte : il faut le critère (le temps) ET le niveau (5 min au plus)."),
                         dict(name="bnom", cible="ex-b-nom", legende="Bloc B — son <b>nom</b> (seconde ligne du tableau)",
                              options=NOMS_E2, bonnes=["Alerte cuve"],
                              indice="Bloc B, le nom : un mot court qui résume « prévenir quand la cuve est presque vide »."),
                         dict(name="btexte", cible="ex-b-texte", legende="Bloc B — son <b>texte</b>",
                              options=TEXTES_E2, bonnes=[TEXTE_B],
                              indice="Bloc B, le texte : il faut le critère (le volume qui reste dans la cuve) ET le niveau (50 L).")]),
             dict(type="choix", name="mere", legende="Sous quelle exigence-mère ranges-tu les blocs A et B, et quel Id leur donnes-tu&nbsp;?",
                  options=[("deux", "Sous l'exigence 2, Suivi à distance&nbsp;: Id 2.1 et 2.2."),
                           ("un", "Sous l'exigence 1, Arrosage autonome&nbsp;: Id 1.5 et 1.6."),
                           ("onze", "Sous l'exigence 1.1, Étanchéité&nbsp;: Id 1.1.1 et 1.1.2."),
                           ("aucune", "Sous aucune&nbsp;: ce sont deux nouvelles mères, Id 3 et 4.")],
                  bonne="deux",
                  retours={"un": "L'eau de la cuve sert à arroser, c'est vrai ; mais ces deux exigences disent comment la gardienne est INFORMÉE : c'est le suivi à distance.",
                           "onze": "L'étanchéité parle de l'eau qui entre dans le boîtier ; un message sur le smartphone ne la précise pas.",
                           "aucune": "L'exigence 2 dit déjà « suivre l'arrosage sur son smartphone » : A et B la précisent, ce sont ses filles.",
                           "deux": "Oui : les deux messages précisent « suivre l'arrosage sur son smartphone ». Ce sont les filles 1 et 2 de l'exigence 2."}),
             dict(type="choix", name="wifi", legende="Pourquoi «&nbsp;contenir une carte Wi-Fi&nbsp;» n'a-t-il sa place dans aucun bloc d'exigence&nbsp;?",
                  options=[("solution", "Parce que c'est une solution&nbsp;: elle dit comment faire, pas ce que le système doit faire."),
                           ("cher", "Parce qu'une carte Wi-Fi coûte trop cher pour un jardin de collège."),
                           ("niveau", "Parce qu'il manque seulement un niveau&nbsp;: «&nbsp;une carte Wi-Fi au moins&nbsp;»."),
                           ("anglais", "Parce que «&nbsp;Wi-Fi&nbsp;» est un mot anglais, interdit dans une exigence.")],
                  bonne="solution",
                  retours={"cher": "Le prix n'est pas la raison : même gratuite, une carte Wi-Fi resterait un COMMENT, pas une exigence.",
                           "niveau": "Ajouter un nombre ne change rien : « une carte au moins » dit toujours comment faire, pas ce qu'on attend.",
                           "anglais": "Le diagramme lui-même emploie des mots anglais (requirement) : la langue n'est pas la raison.",
                           "solution": "Oui : une exigence dit CE QUE le système doit faire. La carte Wi-Fi est un moyen d'y arriver, une solution."})],
    aides=["<p>Pour chaque bloc, lis sa ligne du tableau. Le nom résume la désignation en un ou deux mots. Le texte doit "
           "contenir <b>le critère et le niveau</b>&nbsp;: cherche le texte où tu retrouves le nombre de la ligne et son "
           "unité. Pour la mère, demande-toi&nbsp;: <b>quelle phrase ces deux blocs précisent-ils&nbsp;?</b></p>",
           "<p><b>Les deux blocs.</b> Ligne 1 → «&nbsp;compte rendu&nbsp;» → critère&nbsp;: le temps avant l'arrivée du "
           "message → niveau&nbsp;: 5&nbsp;min au plus → un seul texte contient «&nbsp;5&nbsp;min au plus&nbsp;».<br>"
           "Ligne 2 → «&nbsp;cuve presque vide&nbsp;» → critère&nbsp;: le volume qui reste → niveau&nbsp;: 50&nbsp;L → un "
           "seul texte contient «&nbsp;50&nbsp;L&nbsp;».</p>"
           "<p><b>Les refus.</b> «&nbsp;Assez vite&nbsp;» → pas de nombre → impossible à vérifier → refusé.<br>"
           "«&nbsp;Une carte Wi-Fi&nbsp;» → un composant → c'est <b>comment</b> on fera → une solution, pas une exigence.</p>"
           "<p><b>La mère.</b> A et B parlent du smartphone → ils précisent «&nbsp;Suivi à distance&nbsp;» → Id 2.1 et 2.2.</p>"],
    jumeau=dict(consigne="Une troisième ligne&nbsp;: «&nbsp;Signaler une panne de la pompe — Critère&nbsp;: temps entre la "
                         "panne et l'alerte — Niveau&nbsp;: 10&nbsp;min au plus&nbsp;». Écris le nom, le texte et l'Id de son bloc.",
                correction="Nom&nbsp;: <b>Alerte panne</b>. Texte&nbsp;: «&nbsp;Une alerte doit arriver sur le smartphone "
                           "<b>10&nbsp;min au plus</b> après une panne de la pompe.&nbsp;» Mère&nbsp;: l'exigence 2, Suivi à "
                           "distance → <b>Id 2.3</b>, sa troisième fille."),
    correction=[
        '<figure class="figure">' + EX_SUIVI_C + '<figcaption>Le diagramme corrigé : les blocs 2.1 et 2.2 sont les filles de l\'exigence 2.</figcaption></figure>',
        "<b>Bloc A</b> → nom&nbsp;: <b>Compte rendu</b> → texte&nbsp;: «&nbsp;Le compte rendu doit arriver sur le smartphone "
        "<b>5&nbsp;min au plus</b> après chaque arrosage.&nbsp;» → critère (le temps) + niveau (5&nbsp;min au plus)",
        "<b>Bloc B</b> → nom&nbsp;: <b>Alerte cuve</b> → texte&nbsp;: «&nbsp;Une alerte doit partir sur le smartphone dès qu'il "
        "reste <b>50&nbsp;L</b> dans la cuve.&nbsp;» → critère (le volume qui reste) + niveau (50&nbsp;L)",
        "<b>«&nbsp;Prévenir assez vite quand il le faut&nbsp;»</b> → aucun nombre, aucune unité → personne ne peut dire si "
        "c'est réussi → refusé",
        "<b>«&nbsp;Contenir une carte Wi-Fi&nbsp;»</b> → un composant, donc <b>comment</b> on fera → une <b>solution</b>&nbsp;; "
        "elle viendra plus tard <i>satisfaire</i> l'exigence 2.1, mais elle n'en est pas une",
        "«&nbsp;Carte Wi-Fi&nbsp;» et «&nbsp;Smartphone&nbsp;» ne sont pas des noms d'exigence&nbsp;: l'un est une solution, "
        "l'autre un élément extérieur au système.",
        "<b>La mère</b> → les deux blocs précisent «&nbsp;suivre l'arrosage sur son smartphone&nbsp;» → exigence <b>2</b> → "
        "Id <b>2.1</b> et <b>2.2</b>. L'exigence 1 parle d'arroser, pas d'informer&nbsp;; 1.1 parle de l'eau qui entre "
        "dans le boîtier&nbsp;; et deux nouvelles mères répéteraient l'exigence 2.",
        "<b>La flexibilité</b> (F2, F1) reste dans le tableau du cahier des charges. On peut l'ajouter à la fin du texte, "
        "entre parenthèses&nbsp;: «&nbsp;… 5&nbsp;min au plus après chaque arrosage (F2).&nbsp;»",
        ("conclusion", "Une ligne du cahier des charges devient un bloc&nbsp;: <b>désignation → nom</b>, <b>critère + niveau → "
                       "texte</b>, et une <b>place sous sa mère</b> (son Id). Un composant n'est jamais une exigence."),
    ],
    retenir="pour passer du cahier des charges au diagramme, on garde le <b>critère et le niveau</b> dans le texte du bloc, "
            "et on range le bloc sous l'exigence-mère qu'il précise&nbsp;; une exigence dit <b>ce que</b>, jamais "
            "<b>comment</b>.",
    piege="écrire une solution (une carte Wi-Fi, une pompe 12&nbsp;V, en volts) dans un bloc «&nbsp;requirement&nbsp;»&nbsp;: c'est un "
          "<b>comment</b>, pas une exigence.",
)

TABLE_EXIGENCES_E3 = (
    '<div class="defile"><table><caption>Extrait du cahier des charges : les quatre exigences du diagramme du jardin</caption>'
    "<tr><th>Id</th><th>Exigence</th><th>Niveau</th><th>Flexibilité (classe et marge chiffrée)</th></tr>"
    "<tr><td>1.1</td><td>Étanchéité</td><td>IPX4 au moins&nbsp;: aucune eau dans le boîtier sous des projections</td><td>F1</td></tr>"
    "<tr><td>1.2</td><td>Sobriété</td><td>au plus 10&nbsp;L d'eau par jour</td><td>F2&nbsp;: de 9 à 11&nbsp;L acceptés</td></tr>"
    "<tr><td>1.3</td><td>Réglage</td><td>sans outil, en 2&nbsp;min au plus</td><td>F3&nbsp;: jusqu'à 5&nbsp;min acceptées, toujours sans outil</td></tr>"
    "<tr><td>1.4</td><td>Sécurité électrique</td><td>très basse tension&nbsp;: 12&nbsp;V (volts)</td><td>F0&nbsp;: aucun écart</td></tr>"
    "</table></div>")

TABLE_TESTS_E3 = (
    '<div class="defile"><table><caption>Cinq tests proposés par le club</caption>'
    "<tr><th>Test</th><th>Comment on fait</th></tr>"
    "<tr><td>T1 — Relevé du compteur</td><td>On relève le compteur d'eau du système à 7&nbsp;h, puis le lendemain à 7&nbsp;h, et on fait la différence.</td></tr>"
    "<tr><td>T2 — Mesure au multimètre</td><td>Boîtier en marche, on mesure au multimètre la tension qui l'alimente.</td></tr>"
    "<tr><td>T3 — Essai à l'arroseur</td><td>Boîtier fermé, on l'arrose de tous les côtés pendant 10&nbsp;min, puis on l'ouvre et on cherche des gouttes.</td></tr>"
    "<tr><td>T4 — Réglage chronométré</td><td>Une personne qui découvre le boîtier change l'heure d'arrosage&nbsp;; on la chronomètre et on note les outils qu'elle prend.</td></tr>"
    "<tr><td>T5 — Avis</td><td>On demande à la gardienne si le boîtier lui semble solide.</td></tr>"
    "</table></div>")

E3 = dict(
    id="e3", titre="Relier chaque exigence à son test, puis valider", code="4e_C8.3", duree=15,
    objectif="relier chaque exigence au test qui la vérifie, juger un résultat avec la flexibilité, puis proposer le "
             "protocole de test d'une nouvelle exigence.",
    production="quatre liens exigence → test, quatre verdicts, et un protocole de test écrit.",
    mots=[("protocole de test", "la description précise d'un essai&nbsp;: ce qu'on mesure, avec quel instrument, comment, "
           "et le seuil à atteindre, écrit avant d'essayer."),
          ("«&nbsp;testCase&nbsp;»", "le bloc d'un test, dans un diagramme des exigences&nbsp;; <i>test case</i> veut dire "
           "« cas de test » en anglais."),
          ("«&nbsp;verify&nbsp;»", "« vérifier », en anglais&nbsp;: la flèche en tirets qui va du test vers l'exigence qu'il vérifie."),
          ("multimètre", "un appareil de mesure électrique&nbsp;; en position voltmètre, il mesure une tension en volts (V)."),
          ("écart", "la différence entre le résultat mesuré et le niveau demandé."),
          ("valider", "dire, preuve à l'appui, que le résultat du test respecte l'exigence."),
          ("flexibilité", "l'écart que le client accepte autour du niveau. Classe F0&nbsp;: aucun écart (impératif)&nbsp;; F1&nbsp;: "
           "un petit écart, peu négociable&nbsp;; F2&nbsp;: négociable&nbsp;; F3&nbsp;: très négociable. On peut aussi l'écrire "
           "en chiffres&nbsp;: «&nbsp;de 9 à 11&nbsp;L&nbsp;».")],
    intro="<p>Le club a fabriqué un prototype du système d'arrosage. Avant de l'installer, on <b>vérifie</b> chaque exigence "
          "par un test. Dans le diagramme des exigences, chaque test a son bloc «&nbsp;testCase&nbsp;», relié à l'exigence "
          "par une flèche en tirets «&nbsp;verify&nbsp;»&nbsp;: «&nbsp;ce test vérifie cette exigence&nbsp;».</p>"
          + TABLE_EXIGENCES_E3 + TABLE_TESTS_E3,
    consigne="<p>Un <b>protocole de test</b> dit ce qu'on mesure, avec quel instrument, comment, et le seuil à atteindre. "
             "La <b>flexibilité</b> dit l'écart que le client accepte autour du niveau&nbsp;: un écart dans la marge se "
             "valide, un écart hors de la marge ne se valide pas, et en <b>F0</b> aucun écart n'est accepté.</p>"
             "<p><b>Relie chaque exigence au test qui la vérifie</b> (un des cinq tests ne vérifie rien). <b>Juge</b> ensuite "
             "chaque résultat obtenu sur le prototype. <b>Écris</b> enfin le protocole de test d'une nouvelle exigence.</p>",
    critere="huit réponses justes, et un protocole qui dit ce que tu mesures, avec quel instrument, et le seuil à atteindre.",
    widgets=[dict(type="classer", name="lien",
                  categories=[("t1", "T1 — Relevé du compteur"), ("t2", "T2 — Mesure au multimètre"),
                              ("t3", "T3 — Essai à l'arroseur"), ("t4", "T4 — Réglage chronométré"), ("t5", "T5 — Avis")],
                  items=[("1.1 Étanchéité — IPX4 au moins&nbsp;: quel test la vérifie&nbsp;?", "t3",
                          "1.1 : on cherche à savoir si l'eau entre dans le boîtier. Quel test l'arrose ?"),
                         ("1.2 Sobriété — au plus 10&nbsp;L par jour&nbsp;: quel test&nbsp;?", "t1",
                          "1.2 : on mesure un volume d'eau sur une journée. Quel test le fait ?"),
                         ("1.3 Réglage — sans outil, 2&nbsp;min au plus&nbsp;: quel test&nbsp;?", "t4",
                          "1.3 : on mesure une durée et on regarde les outils. Quel test le fait ?"),
                         ("1.4 Sécurité électrique — 12&nbsp;V&nbsp;: quel test&nbsp;?", "t2",
                          "1.4 : on mesure une tension, en volts. Quel instrument mesure des volts ?")]),
             dict(type="classer", name="verdict",
                  categories=[("atteint", "validée&nbsp;: le résultat atteint le niveau"),
                              ("marge", "validée&nbsp;: l'écart reste dans la marge acceptée"),
                              ("hors", "non validée&nbsp;: l'écart dépasse la marge acceptée"),
                              ("f0", "non validée&nbsp;: flexibilité F0, aucun écart accepté")],
                  items=[("1.1 — résultat de l'essai à l'arroseur&nbsp;: aucune goutte dans le boîtier", "atteint",
                          "1.1 : aucune goutte, c'est exactement ce qui était demandé. Y a-t-il un écart ?"),
                         ("1.2 — résultat du relevé&nbsp;: 11,5&nbsp;L en 24&nbsp;h", "hors",
                          "1.2 : la marge F2 va jusqu'à 11 L. 11,5 L est-il dedans, même de peu ?"),
                         ("1.3 — résultat du réglage chronométré&nbsp;: 4&nbsp;min, sans outil", "marge",
                          "1.3 : 4 min dépasse 2 min, mais la marge F3 va jusqu'à 5 min, sans outil."),
                         ("1.4 — résultat au multimètre&nbsp;: 24&nbsp;V (une alimentation de 24&nbsp;V a été branchée par erreur)", "f0",
                          "1.4 : quelle est la classe de flexibilité de la tension ? Quel écart accepte-t-elle ?")]),
             dict(type="texte", name="proto", lignes=4,
                  label="Nouvelle exigence 2.1&nbsp;: «&nbsp;Le compte rendu doit arriver sur le smartphone 5&nbsp;min au "
                        "plus après chaque arrosage.&nbsp;» Écris son protocole de test.",
                  criteres=[dict(label="tu dis ce que tu mesures (le temps entre la fin de l'arrosage et l'arrivée du message)",
                                 motifs=["temps", "duree", "delai", "combien de (temps|minutes)", "s'ecoule", "attente"],
                                 manque="Dis ce que tu MESURES : une durée, entre quel moment et quel moment ?"),
                            dict(label="tu nommes l'instrument de mesure",
                                 motifs=["chrono", "montre", "minuteur", "horloge", "pendule", "minuterie"],
                                 manque="Nomme l'INSTRUMENT : avec quoi mesure-t-on une durée ?"),
                            dict(label="tu donnes le seuil à atteindre, avec son unité (5 minutes au plus)",
                                 motifs=[r"\b5\s*(min|mn|minutes?)\b", r"cinq\s*minutes", r"\b300\s*(s|sec|secondes?)\b"],
                                 manque="Donne le SEUIL : quelle durée ne faut-il pas dépasser ? Un nombre et son unité.")],
                  etayage=["Je lance un arrosage. Dès qu'il s'arrête, je démarre … et je mesure …",
                           "L'exigence est validée si le message arrive en … au plus."],
                  exemple="Je lance un arrosage. Dès qu'il s'arrête, je démarre un chronomètre et je mesure le temps "
                          "jusqu'à l'arrivée du compte rendu sur le smartphone. L'exigence est validée si le message arrive "
                          "en 5 min au plus.")],
    aides=["<p>Pour relier, cherche dans chaque test <b>ce qu'il mesure</b>&nbsp;: un volume d'eau, une tension, des gouttes, "
           "une durée. Un test qui ne mesure rien ne vérifie rien. Pour juger, calcule l'écart (résultat − niveau), puis "
           "compare-le à la marge de la flexibilité.</p>",
           "<p><b>Relier.</b> 1.1 → de l'eau qui entre&nbsp;? → T3 l'arrose → <b>T3</b>.<br>"
           "1.2 → un volume par jour → T1 relève le compteur → <b>T1</b>.<br>"
           "1.3 → une durée et des outils → <b>T4</b>.<br>"
           "1.4 → des volts → le multimètre → <b>T2</b>. T5 ne mesure rien&nbsp;: c'est un avis.</p>"
           "<p><b>Juger.</b> 1.2&nbsp;: 11,5&nbsp;L → écart +1,5&nbsp;L → la marge s'arrête à 11&nbsp;L → <b>hors de la "
           "marge</b>, même de peu.<br>"
           "1.4&nbsp;: 24&nbsp;V au lieu de 12&nbsp;V → F0 → <b>aucun écart accepté</b>.</p>"
           "<p><b>Le protocole.</b> <b>Ce que je mesure</b> (une durée) → <b>avec quoi</b> (un chronomètre) → <b>le "
           "seuil</b> (5&nbsp;min au plus).</p>"],
    jumeau=dict(consigne="Exigence 2.2&nbsp;: «&nbsp;Une alerte doit partir sur le smartphone dès qu'il reste 50&nbsp;L dans la "
                         "cuve.&nbsp;» Écris son protocole de test.",
                correction="Je vide la cuve peu à peu en lisant ses <b>graduations</b> (ou une jauge)&nbsp;; je note le "
                           "<b>volume qui reste</b> au moment où l'alerte arrive. L'exigence est validée si l'alerte part "
                           "quand il reste <b>50&nbsp;L</b> (à la marge près que fixe sa flexibilité)."),
    correction=[
        '<figure class="figure">' + EX_ARROSAGE_TESTS + '<figcaption>Chaque exigence et le test qui la vérifie : une flèche « verify » monte du test vers l\'exigence.</figcaption></figure>',
        "<b>1.1 Étanchéité</b> → on veut savoir si l'eau entre → <b>T3, essai à l'arroseur</b>&nbsp;: 10&nbsp;min de "
        "projections de tous côtés, comme le demande IPX4",
        "<b>1.2 Sobriété</b> → un volume d'eau sur une journée → <b>T1, relevé du compteur</b> (à 7&nbsp;h, puis le lendemain à 7&nbsp;h)",
        "<b>1.3 Réglage</b> → une durée et des outils → <b>T4, réglage chronométré</b>, par une personne qui découvre le boîtier",
        "<b>1.4 Sécurité électrique</b> → une tension en volts → <b>T2, mesure au multimètre</b>",
        "<b>T5, l'avis de la gardienne</b> → rien n'est mesuré, aucun seuil → ce n'est pas un test&nbsp;: il ne vérifie aucune exigence",
        "<b>1.1</b> → aucune goutte → écart nul → <b>validée</b>&nbsp;: le résultat atteint le niveau",
        "<b>1.2</b> → 11,5&nbsp;L − 10&nbsp;L = écart de +1,5&nbsp;L → la marge F2 s'arrête à 11&nbsp;L → <b>non validée</b>, "
        "même si c'est presque → réglage possible&nbsp;: raccourcir la durée d'arrosage, puis refaire le test",
        "<b>1.3</b> → 4&nbsp;min − 2&nbsp;min = +2&nbsp;min → la marge F3 va jusqu'à 5&nbsp;min, sans outil → <b>validée</b> dans la marge",
        "<b>1.4</b> → 24&nbsp;V au lieu de 12&nbsp;V → flexibilité <b>F0</b> → aucun écart accepté → <b>non validée</b>. "
        "24&nbsp;V reste une très basse tension, sans danger au toucher&nbsp;: ce n'est pas la question. Le niveau est "
        "impératif, et la pompe prévue pour 12&nbsp;V pourrait griller → réglage&nbsp;: brancher l'alimentation de 12&nbsp;V prévue.",
        "<b>Un protocole attendu pour 2.1&nbsp;:</b> «&nbsp;Je lance un arrosage. Dès qu'il s'arrête, je démarre un "
        "<b>chronomètre</b> et je mesure <b>le temps</b> jusqu'à l'arrivée du compte rendu sur le smartphone. L'exigence est "
        "validée si le message arrive en <b>5&nbsp;min au plus</b>.&nbsp;» On peut le refaire sur plusieurs arrosages&nbsp;: "
        "un seul essai peut tomber sur un bon jour.",
        ("conclusion", "Une exigence se vérifie par un test qui <b>mesure</b> (lien «&nbsp;verify&nbsp;»). On la valide en "
                       "comparant l'<b>écart</b> à la <b>flexibilité</b>&nbsp;: dans la marge → validée&nbsp;; hors de la "
                       "marge, même de peu → non validée&nbsp;; en F0 → aucun écart."),
    ],
    retenir="un <b>protocole de test</b> dit ce qu'on mesure, avec quel instrument, comment, et le seuil à atteindre&nbsp;; "
            "le résultat se juge en comparant l'<b>écart</b> à la <b>flexibilité</b> — en F0, aucun écart ne se valide.",
    piege="valider un résultat «&nbsp;presque bon&nbsp;» (11,5&nbsp;L pour une marge qui s'arrête à 11&nbsp;L), ou croire "
          "qu'un avis («&nbsp;il a l'air solide&nbsp;») est un test.",
)

# ─────────────────────────────────────────────────────────────────────────────
# 3e
# ─────────────────────────────────────────────────────────────────────────────
MOT_SATISFY = ("«&nbsp;satisfy&nbsp;»", "« satisfaire », en anglais&nbsp;: la flèche en tirets qui va d'une solution (un bloc "
               "«&nbsp;block&nbsp;») vers l'exigence qu'elle satisfait.")
MOT_IP = ("indice de protection (IP)", "un code fixé par une norme internationale&nbsp;: le premier chiffre dit la "
          "protection contre la poussière (6&nbsp;: étanche à la poussière), le second contre l'eau (4&nbsp;: projections, "
          "5&nbsp;: jets d'eau, 6&nbsp;: jets puissants). Plus le chiffre est grand, mieux le boîtier est protégé.")
MOT_REPARABILITE = ("indice de réparabilité", "une note sur 10, affichée en France sur certains appareils, qui dit s'il est "
                    "facile de les réparer&nbsp;: notice, démontage, pièces détachées et leur prix.")
MOT_DECLARE = ("valeur déclarée", "une valeur annoncée par le fabricant, pas encore mesurée par nous&nbsp;; un test pourra la vérifier.")
MOT_CLASSES = ("classe de flexibilité", "un code de F0 à F3 qui dit si le niveau se négocie&nbsp;: F0, flexibilité nulle "
               "(impératif)&nbsp;; F1, faible (peu négociable)&nbsp;; F2, moyenne (négociable)&nbsp;; F3, forte (très négociable).")

E4 = dict(
    id="e4", titre="Évaluer deux boîtiers, exigence par exigence", code="3e_C3.3", duree=13,
    objectif="comparer, exigence par exigence, les valeurs déclarées de deux boîtiers aux niveaux du diagramme des exigences.",
    production="dix verdicts «&nbsp;satisfaite / non satisfaite&nbsp;» et une conclusion sur ce qu'on peut en dire.",
    mots=[MOT_SYSML, MOT_DIAGRAMME, MOT_ID, MOT_CONTENANCE, MOT_SATISFY, MOT_IP, MOT_REPARABILITE, MOT_DECLARE,
          ("autonomie", "le temps pendant lequel la station fonctionne sur sa batterie, sans le courant du réseau électrique.")],
    documents=[dict(svg=EX_STATION, legende="Le diagramme des exigences de la station d'alerte cyclonique.",
                    description="<p>En haut, l'exigence-mère <b>Id 1 — Alerte cyclonique</b>&nbsp;: la station doit alerter "
                                "les habitants du quartier à l'approche d'un cyclone. Elle contient cinq exigences-filles&nbsp;:</p><ul>"
                                "<li><b>1.1 Étanchéité</b>&nbsp;: le boîtier doit être IP65 au moins.</li>"
                                "<li><b>1.2 Autonomie</b>&nbsp;: la station doit tenir 72&nbsp;h au moins sur batterie.</li>"
                                "<li><b>1.3 Alerte audible</b>&nbsp;: l'alerte doit s'entendre à 100&nbsp;m au moins.</li>"
                                "<li><b>1.4 Réparabilité</b>&nbsp;: l'indice de réparabilité doit valoir 6/10 au moins.</li>"
                                "<li><b>1.5 Coût</b>&nbsp;: le boîtier doit coûter 300&nbsp;€ au plus.</li></ul>")],
    intro="<p>Le comité de quartier veut installer une <b>station d'alerte cyclonique</b>&nbsp;: elle mesure le vent, la pluie "
          "et la pression, et fait sonner une sirène pour prévenir les habitants, même quand le courant et Internet sont "
          "coupés. Ses exigences sont dessinées dans un <b>diagramme des exigences</b> — on dit souvent <b>diagramme des "
          "exigences SysML</b>, du nom de ce langage de schémas (<i>Systems Modeling Language</i>, « langage de modélisation "
          "des systèmes »). Deux fabricants proposent un boîtier.</p>" + TABLE_VALEURS,
    consigne="<p>Une solution <b>satisfait</b> une exigence quand sa valeur atteint le niveau&nbsp;: «&nbsp;au moins&nbsp;» "
             "veut dire cette valeur <b>ou plus</b>, «&nbsp;au plus&nbsp;» cette valeur <b>ou moins</b>&nbsp;; l'égalité "
             "suffit. Pour l'indice de protection IP, chacun des deux chiffres (poussière, puis eau) doit être au moins égal. "
             "Dans le diagramme, on le montre par une flèche «&nbsp;satisfy&nbsp;» (satisfaire), de la solution vers "
             "l'exigence.</p>"
             "<p><b>Pour chaque exigence, dis si le boîtier A la satisfait, puis si le boîtier B la satisfait.</b> Dis enfin "
             "ce qu'on peut conclure du décompte.</p>",
    critere="onze réponses justes&nbsp;; tu sais expliquer pourquoi IP66 satisfait «&nbsp;IP65 au moins&nbsp;» et pourquoi "
            "72&nbsp;h satisfait «&nbsp;72&nbsp;h au moins&nbsp;».",
    widgets=[dict(type="classer", name="a",
                  categories=[("oui", "satisfaite"), ("non", "non satisfaite")],
                  items=[("Boîtier A — 1.1 Étanchéité&nbsp;: IP66 pour «&nbsp;IP65 au moins&nbsp;»", "oui",
                          "A, 1.1 : compare chiffre par chiffre. 6 pour la poussière, 6 pour l'eau : est-ce au moins 6 et 5 ?"),
                         ("Boîtier A — 1.2 Autonomie&nbsp;: 80&nbsp;h pour «&nbsp;72&nbsp;h au moins&nbsp;»", "oui",
                          "A, 1.2 : 80 h, est-ce 72 h ou plus ?"),
                         ("Boîtier A — 1.3 Alerte audible&nbsp;: 110&nbsp;m pour «&nbsp;100&nbsp;m au moins&nbsp;»", "oui",
                          "A, 1.3 : 110 m, est-ce 100 m ou plus ?"),
                         ("Boîtier A — 1.4 Réparabilité&nbsp;: 5/10 pour «&nbsp;6/10 au moins&nbsp;»", "non",
                          "A, 1.4 : 5, est-ce 6 ou plus ?"),
                         ("Boîtier A — 1.5 Coût&nbsp;: 290&nbsp;€ pour «&nbsp;300&nbsp;€ au plus&nbsp;»", "oui",
                          "A, 1.5 : « au plus » : 290 €, est-ce 300 € ou moins ?")]),
             dict(type="classer", name="b",
                  categories=[("oui", "satisfaite"), ("non", "non satisfaite")],
                  items=[("Boîtier B — 1.1 Étanchéité&nbsp;: IP54 pour «&nbsp;IP65 au moins&nbsp;»", "non",
                          "B, 1.1 : 5 pour la poussière (6 demandé), 4 pour l'eau (5 demandé)."),
                         ("Boîtier B — 1.2 Autonomie&nbsp;: 72&nbsp;h pour «&nbsp;72&nbsp;h au moins&nbsp;»", "oui",
                          "B, 1.2 : « au moins 72 h » : 72 h exactement, est-ce assez ? L'égalité suffit."),
                         ("Boîtier B — 1.3 Alerte audible&nbsp;: 150&nbsp;m pour «&nbsp;100&nbsp;m au moins&nbsp;»", "oui",
                          "B, 1.3 : 150 m, est-ce 100 m ou plus ?"),
                         ("Boîtier B — 1.4 Réparabilité&nbsp;: 9/10 pour «&nbsp;6/10 au moins&nbsp;»", "oui",
                          "B, 1.4 : 9, est-ce 6 ou plus ?"),
                         ("Boîtier B — 1.5 Coût&nbsp;: 240&nbsp;€ pour «&nbsp;300&nbsp;€ au plus&nbsp;»", "oui",
                          "B, 1.5 : « au plus » : 240 €, est-ce 300 € ou moins ?")]),
             dict(type="choix", name="bilan", legende="Chaque boîtier satisfait quatre exigences sur cinq. Que peut-on en conclure&nbsp;?",
                  options=[("rien", "Rien encore&nbsp;: il faut voir quelle exigence manque à chacun, et si cet écart est acceptable."),
                           ("egal", "Qu'ils se valent&nbsp;: on prend le moins cher, le boîtier B."),
                           ("aucun", "Qu'aucun ne convient&nbsp;: il faut chercher un troisième boîtier."),
                           ("depasse", "Qu'il faut prendre celui qui dépasse le plus souvent les niveaux demandés.")],
                  bonne="rien",
                  retours={"egal": "Quatre sur cinq ne dit pas LAQUELLE manque : une exigence manquée n'en vaut pas une autre.",
                           "aucun": "Peut-être pas : si le client accepte un petit écart sur l'exigence manquée, un boîtier peut rester possible.",
                           "depasse": "Dépasser un niveau ne rattrape pas une exigence manquée : 150 m au lieu de 100 m n'empêche pas l'eau d'entrer.",
                           "rien": "Oui : le décompte ne suffit pas. Il faut savoir quelle exigence manque, et ce que le client accepte."})],
    aides=["<p>Pour chaque ligne, repère d'abord le mot du niveau&nbsp;: <b>au moins</b> (il faut cette valeur ou plus) ou "
           "<b>au plus</b> (cette valeur ou moins). Compare ensuite les deux nombres. Pour l'IP, compare chiffre par chiffre.</p>",
           "<p>A, 1.1 → IP<b>6</b><b>6</b> pour IP<b>6</b><b>5</b> → 6 ≥ 6 et 6 ≥ 5 → <b>satisfaite</b>.<br>"
           "B, 1.1 → IP<b>5</b><b>4</b> → 5 &lt; 6 et 4 &lt; 5 → <b>non satisfaite</b>.<br>"
           "B, 1.2 → 72&nbsp;h pour «&nbsp;72&nbsp;h au moins&nbsp;» → égalité → <b>satisfaite</b>.<br>"
           "A, 1.5 → «&nbsp;300&nbsp;€ au plus&nbsp;» → 290 ≤ 300 → <b>satisfaite</b>.<br>"
           "Puis → A manque 1.4, B manque 1.1 → ce ne sont pas les mêmes exigences → le décompte ne départage pas.</p>"],
    jumeau=dict(consigne="Un boîtier C est déclaré IP67, 60&nbsp;h, 120&nbsp;m, réparabilité 7/10, 330&nbsp;€. Quelles "
                         "exigences satisfait-il&nbsp;?",
                correction="1.1&nbsp;: IP67 → 6 ≥ 6 et 7 ≥ 5 → <b>satisfaite</b>. 1.2&nbsp;: 60&nbsp;h &lt; 72&nbsp;h → <b>non "
                           "satisfaite</b>. 1.3&nbsp;: 120&nbsp;m ≥ 100&nbsp;m → <b>satisfaite</b>. 1.4&nbsp;: 7 ≥ 6 → "
                           "<b>satisfaite</b>. 1.5&nbsp;: 330&nbsp;€ &gt; 300&nbsp;€ → <b>non satisfaite</b> (au plus). "
                           "Trois sur cinq."),
    correction=[
        '<figure class="figure">' + EX_STATION_A + '<figcaption>Le boîtier A : quatre flèches « satisfy » ; aucune vers 1.4, la réparabilité.</figcaption></figure>',
        "<b>A, 1.1</b> → IP66 pour IP65 au moins → poussière 6 ≥ 6, eau 6 ≥ 5 → <b>satisfaite</b> (IP66 résiste même à des jets plus puissants)",
        "<b>A, 1.2</b> → 80&nbsp;h ≥ 72&nbsp;h → <b>satisfaite</b>",
        "<b>A, 1.3</b> → 110&nbsp;m ≥ 100&nbsp;m → <b>satisfaite</b>",
        "<b>A, 1.4</b> → 5/10 &lt; 6/10 → <b>non satisfaite</b>",
        "<b>A, 1.5</b> → «&nbsp;au plus&nbsp;» → 290&nbsp;€ ≤ 300&nbsp;€ → <b>satisfaite</b>",
        '<figure class="figure">' + EX_STATION_B + '<figcaption>Le boîtier B : quatre flèches « satisfy » ; aucune vers 1.1, l\'étanchéité.</figcaption></figure>',
        "<b>B, 1.1</b> → IP54 → poussière 5 &lt; 6, eau 4 &lt; 5 → <b>non satisfaite</b>&nbsp;: IP54 résiste aux "
        "projections, pas aux jets d'eau",
        "<b>B, 1.2</b> → 72&nbsp;h pour «&nbsp;72&nbsp;h au moins&nbsp;» → l'égalité suffit → <b>satisfaite</b>",
        "<b>B, 1.3</b> → 150&nbsp;m ≥ 100&nbsp;m → <b>satisfaite</b>&nbsp;; <b>B, 1.4</b> → 9/10 ≥ 6/10 → <b>satisfaite</b>&nbsp;; "
        "<b>B, 1.5</b> → 240&nbsp;€ ≤ 300&nbsp;€ → <b>satisfaite</b>",
        "<b>Le décompte</b> → 4 sur 5 chacun → mais A manque la <b>réparabilité</b>, B manque l'<b>étanchéité</b> → on "
        "ne peut pas encore choisir. Prendre le moins cher, chercher un troisième boîtier ou compter les niveaux "
        "dépassés ne répond pas à la vraie question&nbsp;: <b>quel écart le client accepte-t-il&nbsp;?</b>",
        ("conclusion", "On évalue <b>exigence par exigence</b> (au moins → cette valeur ou plus&nbsp;; au plus → cette valeur "
                       "ou moins&nbsp;; l'égalité suffit). Chaque exigence satisfaite reçoit une flèche «&nbsp;satisfy&nbsp;». "
                       "Le décompte seul ne départage pas deux solutions."),
    ],
    retenir="évaluer une solution, c'est comparer sa valeur au niveau de <b>chaque</b> exigence&nbsp;; «&nbsp;satisfy&nbsp;» "
            "relie la solution à chaque exigence qu'elle satisfait, et le décompte seul ne suffit pas à choisir.",
    piege="lire «&nbsp;au plus 300&nbsp;€&nbsp;» comme «&nbsp;au moins&nbsp;», ou refuser 72&nbsp;h pour «&nbsp;72&nbsp;h au "
          "moins&nbsp;»&nbsp;: l'égalité satisfait.",
)

E5 = dict(
    id="e5", titre="Ce que le client accepte : la flexibilité", code="3e_C3.3", duree=8,
    objectif="attribuer une classe de flexibilité (F0 à F3) à chaque exigence, d'après l'écart que le client accepte.",
    production="cinq classes de flexibilité, et la même marge écrite en chiffres.",
    mots=[("flexibilité", "l'écart que le client accepte autour du niveau, sans refuser l'objet."), MOT_CLASSES,
          ("tolérance chiffrée", "l'autre façon d'écrire la flexibilité&nbsp;: avec des nombres («&nbsp;de 9 à 11&nbsp;L&nbsp;», "
           "«&nbsp;± 1&nbsp;L&nbsp;», «&nbsp;au moins&nbsp;», «&nbsp;au plus&nbsp;»)."),
          ("comité de quartier", "l'association des habitants qui commande la station&nbsp;: c'est le client.")],
    intro="<p>Le cahier des charges de la station porte, pour chaque exigence, une <b>flexibilité</b>&nbsp;: l'écart que le "
          "client accepte autour du niveau. Mme Augustin, présidente du comité de quartier, a répondu à la question «&nbsp;Et "
          "si on n'atteint pas tout à fait ce niveau&nbsp;?&nbsp;»&nbsp;:</p><ul>"
          "<li><b>1.1 Étanchéité, IP65 au moins</b> — «&nbsp;Pas question de descendre&nbsp;: pendant un cyclone, si l'eau "
          "entre, plus d'alerte.&nbsp;»</li>"
          "<li><b>1.2 Autonomie, 72&nbsp;h au moins</b> — «&nbsp;60&nbsp;heures, à la rigueur, si la station m'envoie un "
          "message quand sa batterie faiblit.&nbsp;»</li>"
          "<li><b>1.3 Alerte audible, 100&nbsp;m au moins</b> — «&nbsp;La dernière maison du quartier est à 100&nbsp;m&nbsp;: "
          "pas un mètre de moins.&nbsp;»</li>"
          "<li><b>1.4 Réparabilité, 6/10 au moins</b> — «&nbsp;5 sur 10, ça ira aussi.&nbsp;»</li>"
          "<li><b>1.5 Coût, 300&nbsp;€ au plus</b> — «&nbsp;Même 400&nbsp;€, on trouvera l'argent.&nbsp;»</li></ul>",
    consigne="<p>La flexibilité se note par une <b>classe</b>&nbsp;: <b>F0</b>, flexibilité nulle — aucun écart, le niveau "
             "est impératif&nbsp;; <b>F1</b>, faible — un écart accepté seulement à une condition précise&nbsp;; <b>F2</b>, "
             "moyenne — un petit écart accepté sans condition&nbsp;; <b>F3</b>, forte — un écart large accepté. On peut "
             "aussi l'écrire en chiffres, comme une <b>tolérance</b>.</p>"
             "<p><b>Range chaque réponse de Mme Augustin dans sa classe</b>, puis <b>choisis</b> la bonne écriture chiffrée "
             "de la marge de l'exigence 1.4.</p>",
    critere="six réponses justes&nbsp;; tu sais dire que la classe dépend de l'écart que le client accepte, pas de "
            "l'importance de l'exigence.",
    widgets=[dict(type="classer", name="flex",
                  categories=[("f0", "F0 — flexibilité nulle&nbsp;: impératif"), ("f1", "F1 — faible&nbsp;: peu négociable"),
                              ("f2", "F2 — moyenne&nbsp;: négociable"), ("f3", "F3 — forte&nbsp;: très négociable")],
                  items=[("1.1 Étanchéité — «&nbsp;Pas question de descendre…&nbsp;»", "f0",
                          "1.1 : « pas question » : quel écart est accepté ?"),
                         ("1.2 Autonomie — «&nbsp;60 heures, à la rigueur, si la station m'envoie un message…&nbsp;»", "f1",
                          "1.2 : un écart est accepté, mais seulement à une condition : laquelle des classes le dit ?"),
                         ("1.3 Alerte audible — «&nbsp;… pas un mètre de moins.&nbsp;»", "f0",
                          "1.3 : « pas un mètre de moins » : quel écart est accepté ?"),
                         ("1.4 Réparabilité — «&nbsp;5 sur 10, ça ira aussi.&nbsp;»", "f2",
                          "1.4 : un petit écart (un point), accepté sans condition."),
                         ("1.5 Coût — «&nbsp;Même 400&nbsp;€, on trouvera l'argent.&nbsp;»", "f3",
                          "1.5 : 100 € de plus, sans condition : l'écart accepté est-il petit ou large ?")]),
             dict(type="choix", name="chiffre", legende="La marge de l'exigence 1.4 (6/10 au moins, classe F2), écrite en chiffres&nbsp;:",
                  options=[("bon", "6/10 demandé&nbsp;; 5/10 accepté."),
                           ("pm", "6/10 ± 5, donc de 1/10 à 11/10."),
                           ("plus", "6/10 au plus&nbsp;; 7/10 refusé."),
                           ("exact", "6/10 exactement&nbsp;; rien d'autre.")],
                  bonne="bon",
                  retours={"pm": "± 5 accepterait 1/10 : bien plus large que « 5 sur 10, ça ira aussi ». Et une note sur 10 ne monte pas à 11.",
                           "plus": "« Au plus » inverse le sens : une meilleure réparabilité (7/10) n'a aucune raison d'être refusée.",
                           "exact": "« Exactement » serait une flexibilité nulle, F0 : or Mme Augustin accepte 5/10.",
                           "bon": "Oui : la classe F2 dit « négociable », la tolérance chiffrée dit de combien : 5/10 au plus bas."})],
    aides=["<p>Pour chaque réponse, pose deux questions&nbsp;: <b>accepte-t-elle un écart&nbsp;?</b> Si oui, <b>à une "
           "condition</b>, ou <b>sans condition&nbsp;?</b> Et cet écart est-il <b>petit</b> ou <b>large</b>&nbsp;?</p>",
           "<p>Aucun écart («&nbsp;pas question&nbsp;», «&nbsp;pas un mètre de moins&nbsp;») → <b>F0</b>.<br>"
           "Un écart, mais à une condition («&nbsp;si la station m'envoie un message&nbsp;») → <b>F1</b>.<br>"
           "Un petit écart sans condition («&nbsp;5 sur 10, ça ira&nbsp;») → <b>F2</b>.<br>"
           "Un écart large sans condition (100&nbsp;€ de plus) → <b>F3</b>.<br>"
           "En chiffres, 1.4 → niveau 6/10, plus bas accepté 5/10 → «&nbsp;6/10 demandé, 5/10 accepté&nbsp;».</p>"],
    jumeau=dict(consigne="Une sixième exigence&nbsp;: «&nbsp;Le message radio doit partir 30&nbsp;s au plus après le "
                         "déclenchement&nbsp;». Mme Augustin&nbsp;: «&nbsp;Une minute, si le vent coupe la radio, je peux le "
                         "comprendre — mais seulement dans ce cas-là.&nbsp;» Quelle classe&nbsp;?",
                correction="Un écart est accepté (1&nbsp;min au lieu de 30&nbsp;s), mais <b>à une seule condition</b> (le vent "
                           "qui coupe la radio) → <b>F1</b>, peu négociable."),
    correction=[
        "<b>1.1 Étanchéité</b> → «&nbsp;pas question de descendre&nbsp;» → aucun écart → <b>F0</b>",
        "<b>1.2 Autonomie</b> → 60&nbsp;h acceptées, mais <b>à une condition</b> (le message de batterie faible) → <b>F1</b>",
        "<b>1.3 Alerte audible</b> → «&nbsp;pas un mètre de moins&nbsp;» → aucun écart → <b>F0</b>",
        "<b>1.4 Réparabilité</b> → 5/10 au lieu de 6/10, sans condition → petit écart → <b>F2</b>",
        "<b>1.5 Coût</b> → 400&nbsp;€ au lieu de 300&nbsp;€, sans condition → écart large → <b>F3</b>",
        "<b>En chiffres, 1.4</b> → «&nbsp;6/10 demandé&nbsp;; 5/10 accepté&nbsp;». «&nbsp;± 5&nbsp;» accepterait 1/10&nbsp;; "
        "«&nbsp;au plus&nbsp;» refuserait une meilleure note&nbsp;; «&nbsp;exactement&nbsp;» serait du F0.",
        "Le piège&nbsp;: croire que la classe dit l'<b>importance</b>. Le comité n'est pas riche, et pourtant le coût est en "
        "F3&nbsp;; la réparabilité compte pour faire durer la station, et elle est en F2. La classe dit seulement "
        "<b>l'écart accepté</b>.",
        ("conclusion", "La flexibilité s'écrit de deux façons&nbsp;: une <b>classe</b> (F0 impératif → F3 très négociable) "
                       "ou une <b>tolérance chiffrée</b> (de combien on peut s'écarter). Elle vient de ce que dit le client."),
    ],
    retenir="la <b>classe de flexibilité</b> se lit dans la réponse du client&nbsp;: aucun écart → F0&nbsp;; un écart à une "
            "condition → F1&nbsp;; un petit écart → F2&nbsp;; un écart large → F3. La <b>tolérance chiffrée</b> dit de combien.",
    piege="donner F0 à ce qui paraît important et F3 au reste, au lieu d'écouter l'écart que le client accepte.",
)

TABLE_ARBITRAGE = (
    '<div class="defile"><table><caption>Ce que l\'on sait des deux boîtiers</caption>'
    "<tr><th>Exigence</th><th>Niveau</th><th>Flexibilité</th><th>Boîtier A</th><th>Boîtier B</th></tr>"
    "<tr><td>1.1 Étanchéité</td><td>IP65 au moins</td><td>F0&nbsp;: aucun écart</td><td>IP66 — satisfaite</td><td>IP54 — non satisfaite</td></tr>"
    "<tr><td>1.2 Autonomie</td><td>72&nbsp;h au moins</td><td>F1&nbsp;: 60&nbsp;h si alerte de batterie faible</td><td>80&nbsp;h — satisfaite</td><td>72&nbsp;h — satisfaite</td></tr>"
    "<tr><td>1.3 Alerte audible</td><td>100&nbsp;m au moins</td><td>F0&nbsp;: aucun écart</td><td>110&nbsp;m — satisfaite</td><td>150&nbsp;m — satisfaite</td></tr>"
    "<tr><td>1.4 Réparabilité</td><td>6/10 au moins</td><td>F2&nbsp;: 5/10 accepté</td><td>5/10 — non satisfaite</td><td>9/10 — satisfaite</td></tr>"
    "<tr><td>1.5 Coût</td><td>300&nbsp;€ au plus</td><td>F3&nbsp;: jusqu'à 400&nbsp;€</td><td>290&nbsp;€ — satisfaite</td><td>240&nbsp;€ — satisfaite</td></tr>"
    "</table></div>")

E6 = dict(
    id="e6", titre="Arbitrer : choisir un boîtier et le justifier", code="3e_C3.3", duree=12,
    objectif="choisir entre deux solutions qui ne satisfont pas tout, avec les flexibilités, et justifier ce choix par écrit.",
    production="un choix, une amélioration à demander, et une justification écrite.",
    mots=[("arbitrer", "décider entre plusieurs solutions imparfaites, en disant ce qu'on accepte de perdre et pourquoi."),
          MOT_CLASSES, MOT_REPARABILITE,
          ("condition", "ce que l'on exige en échange d'un écart accepté (une pièce de rechange, une garantie…)."),
          ("amélioration", "un changement demandé au fabricant pour que sa solution tienne mieux l'exigence.")],
    intro="<p>Aucun boîtier ne satisfait les cinq exigences. Le comité de quartier doit pourtant en choisir un avant la "
          "saison des cyclones.</p>" + TABLE_ARBITRAGE,
    consigne="<p><b>Arbitrer</b>, c'est choisir entre des solutions imparfaites en disant ce qu'on accepte de perdre. Regarde "
             "d'abord la <b>flexibilité</b> de chaque exigence non satisfaite&nbsp;: un écart sur une exigence <b>F0</b> "
             "n'est jamais accepté&nbsp;; un écart qui reste dans la marge peut l'être, à condition de le dire.</p>"
             "<p><b>Choisis un boîtier, choisis l'amélioration à demander à son fabricant, puis justifie ton choix</b> en "
             "trois idées&nbsp;: l'exigence qui décide et pourquoi elle compte pour la sécurité des habitants&nbsp;; "
             "l'exigence que ton boîtier ne satisfait pas&nbsp;; une amélioration ou une condition.</p>",
    critere="les deux choix justes, et une justification qui nomme l'exigence décisive, l'exigence non satisfaite et une "
            "amélioration ou une condition.",
    widgets=[dict(type="choix", name="choix", legende="Quel boîtier le comité doit-il retenir&nbsp;?",
                  options=[("a", "Le boîtier A&nbsp;: son seul écart, la réparabilité à 5/10, reste dans la marge F2."),
                           ("b", "Le boîtier B&nbsp;: plus réparable, plus puissant et moins cher que A."),
                           ("aucun", "Aucun&nbsp;: chacun manque une exigence, il faut tout recommencer."),
                           ("egal", "N'importe lequel&nbsp;: ils satisfont tous deux quatre exigences sur cinq.")],
                  bonne="a",
                  retours={"b": "B est meilleur sur trois points, mais il manque l'étanchéité, en F0 : pendant un cyclone, l'eau entrerait et la sirène se tairait.",
                           "aucun": "L'écart de A (5/10 au lieu de 6/10) est exactement celui que Mme Augustin accepte : A reste possible.",
                           "egal": "Les deux écarts ne pèsent pas pareil : l'un est en F0 (aucun écart), l'autre en F2 (5/10 accepté).",
                           "a": "Oui : B est éliminé par une exigence F0 ; l'écart de A reste dans la marge acceptée."}),
             dict(type="choix", name="amelio", legende="Quelle amélioration demander au fabricant du boîtier A&nbsp;?",
                  options=[("vis", "Fixer le couvercle par des vis, avec un joint vendu en pièce détachée, au lieu de le coller."),
                           ("trous", "Percer des trous d'aération pour que l'électronique chauffe moins."),
                           ("prix", "Baisser son prix à 240&nbsp;€, comme le boîtier B."),
                           ("sirene", "Ajouter une seconde sirène pour qu'on l'entende à 150&nbsp;m.")],
                  bonne="vis",
                  retours={"trous": "Des trous laisseraient entrer l'eau : le boîtier perdrait son IP66, l'exigence F0.",
                           "prix": "Le coût est déjà satisfait (290 € pour 300 € au plus) : baisser le prix ne règle pas l'écart de A.",
                           "sirene": "L'alerte est déjà satisfaite (110 m pour 100 m) : une sirène de plus ne rend pas le boîtier réparable.",
                           "vis": "Oui : un couvercle vissé et un joint de rechange le rendent réparable, sans toucher à son étanchéité."}),
             dict(type="texte", name="justif", lignes=5,
                  label="Justifie ton choix en trois idées&nbsp;: l'exigence qui décide et pourquoi elle compte pour les "
                        "habitants, l'exigence que ton boîtier ne satisfait pas, une amélioration ou une condition.",
                  criteres=[dict(label="tu nommes l'exigence qui décide : l'étanchéité (IP65 au moins)",
                                 motifs=["etanch", r"\bip\s?6\d", r"\bip\s?54", r"\b1\.1\b", r"l'eau", "pluie", "jets? d'eau"],
                                 manque="Nomme l'exigence qui DÉCIDE : celle qu'un des boîtiers ne tient pas et qui n'accepte aucun écart."),
                            dict(label="tu dis pourquoi elle compte pour la sécurité des habitants",
                                 motifs=["habitant", "securite", "cyclone", "sirene", "prevenir", "previen", "danger", "proteg", "population"],
                                 manque="Dis pourquoi cette exigence compte pour les HABITANTS : que se passerait-il pendant un cyclone ?"),
                            dict(label="tu reconnais l'exigence que ton boîtier ne satisfait pas (la réparabilité, 5/10)",
                                 motifs=["repar", r"5\s*/\s*10", r"5 sur 10", r"\b1\.4\b"],
                                 manque="Reconnais l'écart de ton boîtier : quelle exigence ne satisfait-il pas ?"),
                            dict(label="tu proposes une amélioration ou une condition",
                                 motifs=["condition", "amelior", r"\bvis\b", "visse", "rechange", "fabricant", "demand",
                                         "exige", "garantie", "negoci", "remplac", "colle", "joint", "detache"],
                                 manque="Propose une AMÉLIORATION ou une CONDITION : que demandes-tu au fabricant, ou en échange de l'écart ?")],
                  interdits=[dict(motifs=[r"(choisi|retien|retenu|prend|garde|opte)\w*\s+(pour\s+)?(le\s+)?boitier\s+b\b",
                                          r"\bje (choisis|prends|retiens) (le )?b\b"],
                                  message="Le boîtier B ne tient pas l'étanchéité, et le comité n'accepte aucun écart sur elle (F0) : il ne peut pas être retenu.")],
                  etayage=["Je retiens le boîtier … . L'exigence qui décide est … , parce que pendant un cyclone …",
                           "Le boîtier que je retiens ne satisfait pas … ( … au lieu de … ), mais le comité accepte … .",
                           "Je demande au fabricant de … , pour que … ."],
                  exemple="Je retiens le boîtier A. L'exigence qui décide est l'étanchéité, IP65 au moins, en F0 : pendant "
                          "un cyclone, si l'eau entre, la sirène se tait et les habitants ne sont plus prévenus. Le boîtier A "
                          "ne satisfait pas la réparabilité (5/10 au lieu de 6/10), mais le comité accepte 5/10. Je demande "
                          "au fabricant de fixer le couvercle par des vis au lieu de le coller.")],
    aides=["<p>Commence par les exigences <b>non satisfaites</b>&nbsp;: il y en a une par boîtier. Pour chacune, lis sa "
           "<b>flexibilité</b>. Un écart sur une exigence F0 élimine le boîtier. Un écart dans la marge le laisse possible.</p>",
           "<p>B → manque 1.1, l'étanchéité → <b>F0</b> → aucun écart accepté → <b>éliminé</b>, même s'il est meilleur ailleurs.<br>"
           "A → manque 1.4 (5/10 au lieu de 6/10) → <b>F2</b>, 5/10 accepté → l'écart est dans la marge → <b>A reste possible</b>.<br>"
           "Amélioration → elle doit réduire l'écart de A <b>sans</b> abîmer une autre exigence → un couvercle vissé, pas des trous.<br>"
           "Justification → étanchéité + cyclone + habitants → réparabilité 5/10 → vis, joint, pièces de rechange.</p>"],
    jumeau=dict(consigne="Un boîtier C est déclaré IP67, 60&nbsp;h sans alerte de batterie faible, 120&nbsp;m, 7/10, "
                         "330&nbsp;€. Peut-il être retenu, avec les flexibilités du comité&nbsp;? À quelle condition&nbsp;?",
                correction="1.5&nbsp;: 330&nbsp;€ → dans la marge F3 (jusqu'à 400&nbsp;€) → acceptable. 1.2&nbsp;: 60&nbsp;h → "
                           "F1, accepté <b>seulement</b> si la station envoie un message de batterie faible → C n'en a pas. "
                           "<b>Il peut être retenu à une condition</b>&nbsp;: que le fabricant ajoute ce message. Sans lui, "
                           "l'écart sort de la marge et C est refusé."),
    correction=[
        "<b>B</b> → manque 1.1, l'étanchéité (IP54) → flexibilité <b>F0</b> → aucun écart accepté → <b>éliminé</b>. Plus "
        "réparable, plus puissant, moins cher&nbsp;: rien de cela ne rattrape l'eau qui entre pendant un cyclone.",
        "<b>A</b> → manque 1.4, la réparabilité (5/10 au lieu de 6/10) → flexibilité <b>F2</b>, 5/10 accepté → l'écart reste "
        "dans la marge → <b>A est retenu</b>, en le disant.",
        "«&nbsp;Aucun&nbsp;» ne tient pas&nbsp;: l'écart de A est exactement celui que le comité accepte. «&nbsp;N'importe "
        "lequel&nbsp;» ne tient pas&nbsp;: un écart en F0 et un écart en F2 ne pèsent pas pareil.",
        "<b>L'amélioration</b> → un couvercle <b>vissé</b> avec un joint de rechange → la réparabilité monte, l'étanchéité "
        "reste. Des trous d'aération casseraient l'IP66&nbsp;; baisser le prix ou ajouter une sirène ne touche pas à l'écart.",
        "<b>Une justification attendue&nbsp;:</b> «&nbsp;Je retiens le boîtier A. L'exigence qui décide est "
        "<b>l'étanchéité</b> (IP65 au moins, F0)&nbsp;: pendant un cyclone, si l'eau entre, la sirène se tait et "
        "<b>les habitants</b> ne sont plus prévenus. Le boîtier A ne satisfait pas <b>la réparabilité</b> (5/10 au lieu de "
        "6/10), mais le comité accepte 5/10. Je demande au fabricant de fixer le couvercle par <b>des vis</b> au lieu de le "
        "coller.&nbsp;»",
        "<b>Dans le diagramme</b> → A garde ses quatre flèches «&nbsp;satisfy&nbsp;»&nbsp;; pour 1.4, l'écart accepté s'écrit "
        "noir sur blanc (on note «&nbsp;5/10 accepté par le comité&nbsp;») — un écart accepté se dit, il ne se cache pas.",
        ("conclusion", "Arbitrer&nbsp;: <b>éliminer</b> la solution qui manque une exigence F0, <b>garder</b> celle dont l'écart "
                       "reste dans la marge, puis <b>dire</b> l'écart accepté et l'amélioration demandée."),
    ],
    retenir="pour arbitrer, on ne compte pas les exigences satisfaites&nbsp;: on regarde la <b>flexibilité</b> de celles qui "
            "manquent. Un écart en <b>F0</b> élimine&nbsp;; un écart dans la marge se négocie, et se dit.",
    piege="choisir la solution la moins chère ou la plus performante «&nbsp;en moyenne&nbsp;», alors qu'elle manque une "
          "exigence impérative (F0).",
)

# ─────────────────────────────────────────────────────────────────────────────
# Le cours (encadré « 📘 Le cours », synthèse élève, blocs insérés dans les séquences)
# ─────────────────────────────────────────────────────────────────────────────
TABLE_LIENS = ('<div class="defile"><table><tr><th>Lien</th><th>Comment il se dessine</th><th>Ce qu\'il dit</th></tr>'
               "<tr><td>contenance</td><td>un trait, avec un petit cercle à croix ⊕ du côté de la mère</td>"
               "<td>l'exigence-mère contient ses filles&nbsp;; elle n'est tenue que si toutes ses filles le sont</td></tr>"
               "<tr><td>«&nbsp;verify&nbsp;»</td><td>une flèche en tirets, du test («&nbsp;testCase&nbsp;») vers l'exigence</td>"
               "<td>ce test vérifie cette exigence</td></tr>"
               "<tr><td>«&nbsp;satisfy&nbsp;»</td><td>une flèche en tirets, de la solution («&nbsp;block&nbsp;») vers l'exigence</td>"
               "<td>cette solution satisfait cette exigence</td></tr></table></div>")

TABLE_FLEX = ('<div class="defile"><table><tr><th>Classe</th><th>Flexibilité</th><th>Ce que dit le client</th>'
              "<th>Exemple au jardin</th></tr>"
              "<tr><td>F0</td><td>nulle&nbsp;: impératif</td><td>«&nbsp;Pas question.&nbsp;»</td><td>12&nbsp;V (volts), rien d'autre</td></tr>"
              "<tr><td>F1</td><td>faible&nbsp;: peu négociable</td><td>«&nbsp;À la rigueur, si…&nbsp;» (un écart, à une condition)</td>"
              "<td>IPX3 seulement sous l'abri, preuve à l'appui</td></tr>"
              "<tr><td>F2</td><td>moyenne&nbsp;: négociable</td><td>«&nbsp;Un peu plus, un peu moins, ça ira.&nbsp;»</td>"
              "<td>de 9 à 11&nbsp;L par jour</td></tr>"
              "<tr><td>F3</td><td>forte&nbsp;: très négociable</td><td>«&nbsp;Même bien plus, ça m'ira.&nbsp;»</td>"
              "<td>réglage en 5&nbsp;min au lieu de 2</td></tr></table></div>")

COURS = {
    "4e": "<h3>À quoi sert le diagramme des exigences</h3><ul>"
          "<li>Le <b>cahier des charges</b> range les exigences dans un tableau. Le <b>diagramme des exigences</b> les dessine "
          "dans des blocs reliés&nbsp;: on voit d'un coup d'œil quelle exigence en contient d'autres, et quel test vérifie "
          "quoi.</li>"
          "<li>On l'appelle souvent <b>diagramme des exigences SysML</b>. SysML&nbsp;: <i>Systems Modeling Language</i>, "
          "« langage de modélisation des systèmes » — des schémas que les ingénieurs du monde entier lisent de la même "
          "façon.</li></ul>"
          "<h3>Un bloc d'exigence</h3><ul>"
          "<li>En haut, «&nbsp;requirement&nbsp;» (exigence, en anglais) et le <b>nom</b>, court&nbsp;: «&nbsp;Sobriété&nbsp;».</li>"
          "<li><b>Id</b>, l'identifiant&nbsp;: 1 est une exigence-mère&nbsp;; 1.1, 1.2… sont ses filles.</li>"
          "<li><b>Text</b>, la phrase&nbsp;: elle porte un <b>critère</b> (ce qu'on mesure) et un <b>niveau</b> (la valeur à "
          "atteindre) — «&nbsp;au plus 10&nbsp;L d'eau par jour&nbsp;».</li>"
          "<li>Une exigence dit <b>ce que</b> le système doit faire, jamais <b>comment</b>&nbsp;: «&nbsp;contenir une carte "
          "Wi-Fi&nbsp;» est une solution, pas une exigence.</li></ul>"
          "<h3>Les liens</h3>" + TABLE_LIENS +
          "<h3>Chaque exigence a sa catégorie</h3><ul>"
          "<li>Le programme en cite six&nbsp;: <b>sécurité</b> (12&nbsp;volts, très basse tension), <b>incidences "
          "environnementales</b> (10&nbsp;L d'eau par jour au plus), <b>ergonomie</b> (réglage sans outil), <b>fiabilité</b> "
          "(IPX4&nbsp;: fonctionner sous la pluie), <b>formes et fonctions</b>, <b>qualité</b>.</li></ul>"
          "<h3>Proposer un protocole de test</h3><ul>"
          "<li>Un protocole dit <b>ce qu'on mesure</b>, <b>avec quel instrument</b>, <b>comment</b> (conditions, durée) et le "
          "<b>seuil</b> à atteindre, écrit <b>avant</b> l'essai.</li>"
          "<li>Un avis («&nbsp;il a l'air solide&nbsp;») n'est pas un test&nbsp;: rien n'y est mesuré.</li>"
          "<li><b>Écart</b> = résultat mesuré − niveau demandé.</li></ul>"
          "<h3>Valider avec la flexibilité</h3><ul>"
          "<li>Le cahier des charges donne à chaque exigence sa <b>flexibilité</b>&nbsp;: l'écart que le client accepte. Elle "
          "s'écrit de deux façons&nbsp;: une <b>classe</b>, de F0 à F3, ou une <b>tolérance chiffrée</b> («&nbsp;de 9 à "
          "11&nbsp;L&nbsp;», «&nbsp;± 1&nbsp;L&nbsp;»).</li></ul>" + TABLE_FLEX +
          "<ul><li>Écart dans la marge → exigence <b>validée</b>. Écart hors de la marge, même de peu → <b>non validée</b>. "
          "En <b>F0</b>, aucun écart n'est validé.</li>"
          "<li>Dans un bloc, on peut ajouter la classe à la fin du texte, entre parenthèses&nbsp;: «&nbsp;au plus 10&nbsp;L "
          "d'eau par jour (F2)&nbsp;».</li></ul>",
    "3e": "<h3>Lire un diagramme des exigences</h3><ul>"
          "<li>Le <b>diagramme des exigences</b> — souvent appelé <b>diagramme des exigences SysML</b>, de <i>Systems Modeling "
          "Language</i>, « langage de modélisation des systèmes » — dessine le cahier des charges en blocs reliés.</li>"
          "<li>Chaque bloc «&nbsp;requirement&nbsp;» a un <b>nom</b>, un <b>Id</b> (1, 1.1, 1.2…) et un <b>texte</b> avec "
          "<b>critère</b> et <b>niveau</b>&nbsp;: «&nbsp;72&nbsp;h au moins sur batterie&nbsp;».</li>"
          "<li>Le lien ⊕ (contenance)&nbsp;: l'exigence-mère contient ses filles, et n'est tenue que si toutes le sont.</li></ul>"
          "<h3>Évaluer une solution, exigence par exigence</h3><ul>"
          "<li>On compare la valeur de la solution — mesurée, ou <b>déclarée</b> par le fabricant — au niveau de chaque "
          "exigence.</li>"
          "<li>«&nbsp;Au moins 72&nbsp;h&nbsp;»&nbsp;: 72&nbsp;h ou plus. «&nbsp;Au plus 300&nbsp;€&nbsp;»&nbsp;: 300&nbsp;€ ou "
          "moins. <b>L'égalité satisfait.</b></li>"
          "<li>Indice de protection IP&nbsp;: deux chiffres, la poussière puis l'eau&nbsp;; chacun doit être au moins égal. "
          "IP66 satisfait «&nbsp;IP65 au moins&nbsp;», IP54 non.</li>"
          "<li>Les critères du programme&nbsp;: les <b>caractéristiques</b>, les <b>performances</b>, le <b>coût</b> et "
          "l'<b>indice de réparabilité</b> (une note sur 10, affichée en France sur certains appareils).</li></ul>"
          "<h3>Les liens «&nbsp;satisfy&nbsp;» et «&nbsp;verify&nbsp;»</h3>" + TABLE_LIENS +
          "<ul><li>Une valeur <b>déclarée</b> se croit sur parole jusqu'au test&nbsp;: c'est le test, relié par «&nbsp;verify&nbsp;», "
          "qui la prouve.</li></ul>"
          "<h3>La flexibilité&nbsp;: l'écart que le client accepte</h3><ul>"
          "<li>Une <b>classe</b>&nbsp;: <b>F0</b> nulle (impératif)&nbsp;; <b>F1</b> faible (un écart, à une condition)&nbsp;; "
          "<b>F2</b> moyenne (un petit écart, sans condition)&nbsp;; <b>F3</b> forte (un écart large).</li>"
          "<li>Ou une <b>tolérance chiffrée</b>&nbsp;: «&nbsp;6/10 demandé, 5/10 accepté&nbsp;», «&nbsp;jusqu'à 400&nbsp;€&nbsp;».</li>"
          "<li>La classe se lit dans la réponse du client&nbsp;; elle ne dit pas l'importance de l'exigence.</li></ul>"
          "<h3>Arbitrer</h3><ul>"
          "<li>Compter les exigences satisfaites ne suffit pas&nbsp;: «&nbsp;4 sur 5&nbsp;» ne dit pas laquelle manque.</li>"
          "<li>Une solution qui manque une exigence <b>F0</b> est éliminée.</li>"
          "<li>Si l'écart reste dans la marge, la solution reste possible — à condition de le dire.</li>"
          "<li>On justifie par l'exigence qui décide, l'écart accepté, et l'<b>amélioration</b> ou la <b>condition</b> "
          "demandée.</li></ul>",
}

# ─────────────────────────────────────────────────────────────────────────────
# Les deux niveaux
# ─────────────────────────────────────────────────────────────────────────────
NIVEAUX = {
    "4e": dict(
        codes=["4e_C2.2", "4e_C8.3"],
        mission="Dessiner les exigences d'un système, les ranger, et relier chacune au test qui la vérifie.",
        avant=[("Je sais écrire une contrainte avec un critère et un niveau, et lui donner une classe de flexibilité (F0 à F3).",
                "4e_C2.2", "@atelier:interacteurs:4e#pv_4e_e6",
                "l'atelier « diagramme des interacteurs extérieurs », exercice sur le cahier des charges (15 minutes)"),
               ("Je sais ranger une contrainte dans sa catégorie&nbsp;: sécurité, incidences environnementales, ergonomie, fiabilité…",
                "4e_C2.2", "@atelier:interacteurs:4e#pv_4e_e7",
                "l'atelier « diagramme des interacteurs extérieurs », exercice sur les contraintes oubliées (12 minutes)")],
        situation_titre="Deux noms pour un même schéma",
        situation="<p><b>Les mots du programme</b>&nbsp;: contraintes, exigences, cahier des charges. Quand on dessine "
                  "les exigences d'un système dans des blocs reliés entre eux, on obtient le <b>diagramme des "
                  "exigences</b>. Les ingénieurs l'appellent <b>diagramme des exigences SysML</b>&nbsp;: SysML veut dire "
                  "<i>Systems Modeling Language</i>, « langage de modélisation des systèmes », un ensemble de schémas qui "
                  "se lisent de la même façon dans le monde entier.</p>"
                  "<p><b>Dans cet atelier</b>, le système est le <b>système d'arrosage connecté</b> du jardin partagé du collège. Ses "
                  "exigences sont déjà dans un tableau&nbsp;: tu vas les voir en schéma, en ajouter, puis les "
                  "<b>vérifier</b> par des tests.</p>",
        question="Comment montrer d'un coup d'œil toutes les exigences d'un système — et comment prouver que chacune est "
                 "tenue&nbsp;?",
        hypothese_amorces=["Je pense qu'on pourrait dessiner chaque exigence dans…", "Pour prouver qu'une exigence est tenue, il faudrait…",
                           "Une exigence bien écrite contient…"],
        exercices=[E1, E2, E3],
        a_retenir="<ul><li>Le <b>diagramme des exigences</b> — souvent appelé <b>diagramme des exigences SysML</b> — dessine "
                  "chaque exigence dans un bloc&nbsp;: un <b>nom</b>, un <b>Id</b>, un <b>texte</b> avec critère et niveau.</li>"
                  "<li>Le lien ⊕ dit qu'une exigence-mère <b>contient</b> ses filles&nbsp;; elle n'est tenue que si toutes "
                  "le sont. Une exigence dit <b>ce que</b> le système doit faire, jamais <b>comment</b>.</li>"
                  "<li>Chaque exigence se vérifie par un <b>test</b> qui mesure&nbsp;: la flèche «&nbsp;verify&nbsp;» va du test "
                  "vers l'exigence. Un protocole dit ce qu'on mesure, avec quoi, comment, et le seuil à atteindre.</li>"
                  "<li>On valide en comparant l'<b>écart</b> à la <b>flexibilité</b>&nbsp;: dans la marge → validée&nbsp;; "
                  "hors de la marge → non validée&nbsp;; en <b>F0</b>, aucun écart.</li></ul>",
        bonus=[dict(titre="La pompe qui réveille la voisine",
                    consigne="<p>La nuit, la pompe du système réveille la voisine. Écris le <b>bloc d'exigence</b> qui manque "
                             "(nom, Id, texte avec critère et niveau), sa <b>catégorie</b>, et le <b>test</b> qui la vérifiera.</p>",
                    correction=["<b>Nom</b> → Discrétion → <b>Id</b> → 1.5, cinquième fille de l'exigence 1",
                                "<b>Texte</b> → «&nbsp;La pompe doit faire au plus 35&nbsp;dB à 1&nbsp;m, entre 22&nbsp;h "
                                "et 7&nbsp;h.&nbsp;» (décibels) → critère&nbsp;: le niveau sonore&nbsp;; niveau&nbsp;: 35&nbsp;dB au plus",
                                "<b>Catégorie</b> → incidences environnementales&nbsp;: le bruit est une nuisance pour les voisins",
                                "<b>Test</b> → un sonomètre (l'appareil qui mesure le bruit) à 1&nbsp;m de la pompe, pendant un "
                                "arrosage de nuit&nbsp;; seuil&nbsp;: 35&nbsp;dB au plus",
                                ("conclusion", "Une plainte nouvelle, c'est souvent une exigence oubliée&nbsp;: on l'ajoute au "
                                               "diagramme, avec son test.")]),
               dict(titre="Le diagramme qui se trompe",
                    consigne="<p>Un élève a dessiné une flèche «&nbsp;verify&nbsp;» qui part de l'exigence 1.2 et va vers le "
                             "test T1. Il a aussi écrit «&nbsp;pompe 12&nbsp;V&nbsp;» (volts) dans un bloc «&nbsp;requirement&nbsp;». "
                             "Trouve les deux erreurs et corrige-les.</p>",
                    correction=["<b>Erreur 1</b> → la flèche «&nbsp;verify&nbsp;» va <b>du test vers l'exigence</b>&nbsp;: de T1 "
                                "vers 1.2, pas l'inverse",
                                "<b>Erreur 2</b> → «&nbsp;pompe 12&nbsp;V&nbsp;» est une <b>solution</b> (un composant)&nbsp;: elle "
                                "ne va pas dans un bloc d'exigence. Elle irait dans un bloc «&nbsp;block&nbsp;», relié à "
                                "l'exigence 1.4 par une flèche «&nbsp;satisfy&nbsp;»",
                                ("conclusion", "Exigence&nbsp;: ce que. Solution&nbsp;: comment. Test&nbsp;: la preuve.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre un critère et un niveau, entre une exigence et une solution, "
                      "ou pour valider un résultat «&nbsp;presque bon&nbsp;». Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
    "3e": dict(
        codes=["3e_C3.3"],
        mission="Évaluer deux solutions avec un diagramme des exigences, puis choisir — et dire ce qu'on accepte.",
        avant=[("Je sais lire un bloc d'exigence&nbsp;: son nom, son Id, son texte avec critère et niveau, et le lien ⊕.",
                "4e_C2.2", "@niveau:4e#ex_4e_e1", "l'atelier de 4e, exercice de lecture du diagramme (10 minutes)"),
               ("Je sais relier une exigence au test qui la vérifie, et juger un résultat avec la flexibilité.",
                "4e_C8.3", "@niveau:4e#ex_4e_e3", "l'atelier de 4e, exercice sur les tests (15 minutes)")],
        situation_titre="Deux noms pour un même schéma",
        situation="<p><b>Évaluer des objets</b> selon des exigences ou des critères — caractéristiques, performances, "
                  "coût, indice de réparabilité&nbsp;: c'est ce que demande le programme de technologie. Pour avoir toutes "
                  "les exigences sous les yeux, on les dessine dans un <b>diagramme des exigences</b>, que les ingénieurs "
                  "appellent <b>diagramme des exigences SysML</b> — SysML veut dire <i>Systems Modeling Language</i>, "
                  "« langage de modélisation des systèmes ».</p>"
                  "<p><b>Dans cet atelier</b>, le système est la <b>station d'alerte cyclonique</b> du quartier. Deux boîtiers "
                  "sont proposés&nbsp;; aucun n'est parfait.</p>",
        question="Quand aucune solution ne satisfait toutes les exigences, comment choisir — et comment le justifier&nbsp;?",
        hypothese_amorces=["Je pense qu'on choisit la solution qui…", "Pour départager deux solutions, je regarderais…",
                           "Une exigence non satisfaite, c'est grave quand…"],
        exercices=[E4, E5, E6],
        a_retenir="<ul><li>Évaluer, c'est comparer la valeur d'une solution au niveau de <b>chaque</b> exigence&nbsp;: "
                  "«&nbsp;au moins&nbsp;» → cette valeur ou plus&nbsp;; «&nbsp;au plus&nbsp;» → cette valeur ou moins&nbsp;; "
                  "l'égalité satisfait.</li>"
                  "<li>La flèche «&nbsp;satisfy&nbsp;» relie une solution à chaque exigence qu'elle satisfait&nbsp;; la flèche "
                  "«&nbsp;verify&nbsp;» relie une exigence au test qui la prouve.</li>"
                  "<li>La <b>flexibilité</b> dit l'écart que le client accepte&nbsp;: une classe (F0 impératif → F3 très "
                  "négociable) ou une tolérance chiffrée.</li>"
                  "<li>Arbitrer&nbsp;: éliminer la solution qui manque une exigence <b>F0</b>, garder celle dont l'écart reste "
                  "dans la marge, et <b>dire</b> l'écart accepté et l'amélioration demandée.</li></ul>",
        bonus=[dict(titre="Le boîtier C",
                    consigne="<p>Un troisième boîtier arrive&nbsp;: IP67, 60&nbsp;h <b>avec</b> message de batterie faible, "
                             "120&nbsp;m, réparabilité 7/10, 330&nbsp;€. Avec les flexibilités du comité, peut-il battre le "
                             "boîtier A&nbsp;? Justifie.</p>",
                    correction=["<b>1.1</b> → IP67 → satisfaite&nbsp;; <b>1.3</b> → 120&nbsp;m → satisfaite&nbsp;; <b>1.4</b> → "
                                "7/10 → satisfaite",
                                "<b>1.2</b> → 60&nbsp;h → F1, accepté avec le message de batterie faible → C l'a → dans la marge",
                                "<b>1.5</b> → 330&nbsp;€ → F3, jusqu'à 400&nbsp;€ → dans la marge",
                                "<b>Bilan</b> → C a deux écarts acceptés (autonomie, coût), A un seul (réparabilité). C est plus "
                                "réparable et plus étanche&nbsp;; A tient plus longtemps sur batterie et coûte moins. Les deux "
                                "sont possibles&nbsp;: le choix se discute avec le comité — par exemple, une station qui tient "
                                "80&nbsp;h plutôt que 60&nbsp;h pendant un long cyclone.",
                                ("conclusion", "Quand deux solutions restent possibles, l'arbitrage se dit avec le client&nbsp;: "
                                               "on lui présente les écarts de chacune.")]),
               dict(titre="L'indice de réparabilité en magasin",
                    consigne="<p>En France, certains appareils (téléphones, ordinateurs portables, lave-linge…) affichent un "
                             "indice de réparabilité sur 10. Cite <b>trois</b> choses qui rendent un appareil plus facile à "
                             "réparer, et dis pourquoi c'est une exigence de développement durable.</p>",
                    correction=["<b>Une notice de réparation</b> disponible, pour savoir comment faire",
                                "<b>Un démontage simple</b>, avec des outils courants&nbsp;: des vis plutôt que de la colle",
                                "<b>Des pièces détachées</b> disponibles, à un prix raisonnable",
                                "<b>Pourquoi</b> → un appareil réparé dure plus longtemps&nbsp;: moins d'objets fabriqués et "
                                "jetés, moins de matières premières et de déchets",
                                ("conclusion", "Un critère de choix peut servir la planète autant que le porte-monnaie.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre «&nbsp;au moins&nbsp;» et «&nbsp;au plus&nbsp;», entre F1 et F2, "
                      "ou pour écarter un boîtier pourtant meilleur sur plusieurs points. Qu'est-ce que tu dois encore revoir, "
                      "et comment&nbsp;?",
    ),
}

# ─────────────────────────────────────────────────────────────────────────────
# Ce que le reste du site lit de cet atelier
# ─────────────────────────────────────────────────────────────────────────────
MODULE = "exigences"
NOM_PANNEAU = "diagramme_des_exigences"
PANNEAU_TEXTE = {
    "4e": "Le <b>diagramme des exigences</b> — souvent appelé <b>diagramme des exigences SysML</b> — sur le système "
          "d'arrosage du jardin&nbsp;: tu lis ses blocs, tu transformes une ligne du cahier des charges en bloc d'exigence, "
          "puis tu relies chaque exigence au test qui la vérifie et tu juges ses résultats avec la flexibilité.",
    "3e": "Le <b>diagramme des exigences</b> — souvent appelé <b>diagramme des exigences SysML</b> — sur la station d'alerte "
          "cyclonique&nbsp;: tu évalues deux boîtiers exigence par exigence, tu attribues la flexibilité d'après ce que dit "
          "le client, puis tu choisis et tu justifies.",
}
IMAGES = {
    "exigences_arrosage.svg": EX_ARROSAGE,
    "exigences_arrosage_tests_verify.svg": EX_ARROSAGE_TESTS,
    "exigences_suivi_a_distance.svg": EX_SUIVI_C,
    "exigences_station.svg": EX_STATION,
    "exigences_station_boitier_a.svg": EX_STATION_A,
    "exigences_station_boitier_b.svg": EX_STATION_B,
}
ROLES_IMAGES = {
    "exigences_arrosage.svg": "lire un diagramme des exigences (4e, exercice de lecture et QCM)",
    "exigences_arrosage_tests_verify.svg": "relier chaque exigence à son test, flèches « verify » (4e, corrigé et QCM)",
    "exigences_suivi_a_distance.svg": "ranger deux blocs sous leur exigence-mère (4e, corrigé et QCM)",
    "exigences_station.svg": "évaluer deux boîtiers (3e, exercice et QCM)",
    "exigences_station_boitier_a.svg": "ce que le boîtier A satisfait, flèches « satisfy » (3e, corrigé et QCM)",
    "exigences_station_boitier_b.svg": "ce que le boîtier B satisfait, flèches « satisfy » (3e, corrigé)",
}
VOCAB_EN = [("exigence", "requirement"), ("diagramme des exigences", "requirement diagram"),
            ("identifiant (Id)", "identifier (Id)"), ("contenance", "containment"), ("vérifier", "verify"),
            ("satisfaire", "satisfy"), ("cas de test", "test case"), ("protocole de test", "test procedure"),
            ("critère", "criterion"), ("niveau", "level"), ("flexibilité", "flexibility"), ("écart", "deviation"),
            ("indice de réparabilité", "repairability index"), ("indice de protection", "ingress protection rating")]
VERBES = {"5e": "pas d'exercice de ce diagramme&nbsp;: la carte des représentations le classe en 4e / 3e, facultatif. En 5e, "
                "on <b>reconnaît</b> le cahier des charges et ses contraintes, sans les dessiner en blocs.",
          "4e": "<b>lire</b> un diagramme des exigences, <b>structurer</b> une ligne du cahier des charges en bloc d'exigence, "
                "<b>relier</b> chaque exigence au test qui la vérifie («&nbsp;verify&nbsp;»), <b>proposer</b> un protocole et "
                "<b>valider</b> un résultat avec la flexibilité",
          "3e": "<b>évaluer</b> deux solutions exigence par exigence («&nbsp;satisfy&nbsp;»), <b>attribuer</b> la flexibilité "
                "d'après ce que dit le client, puis <b>arbitrer</b> et justifier"}
CHAINE = ("<p><b>Analyse externe</b>&nbsp;: besoin <i>(bête à cornes)</i> → interacteurs <i>(diagramme pieuvre)</i> → "
          "<b>contraintes et exigences → cahier des charges <i>(diagramme des exigences SysML)</i></b>.</p>"
          "<p>Puis <b>boucle de validation</b>, en conception&nbsp;: une solution satisfait une exigence (lien «&nbsp;satisfy&nbsp;»), "
          "un test la vérifie (lien «&nbsp;verify&nbsp;»), et le résultat se compare au niveau et à la flexibilité — c'est ce "
          "que le programme appelle comparer les résultats obtenus aux exigences issues du cahier des charges.</p>"
          "<p>Cet atelier <b>suit</b> l'atelier du diagramme des interacteurs (4e_C2.2&nbsp;: critère, niveau, flexibilité) et "
          "<b>prolonge</b> son cahier des charges du jardin. Il <b>prépare</b> la validation en conception (4e_C8.3) et le "
          "choix argumenté d'une solution en 3e (3e_C3.3).</p>")
NOTES_PROF = ("<ul><li>Plan de l'atelier, au 24/10/2026&nbsp;: <b>six exercices</b> au lieu des cinq prévus. Ajout de l'exercice "
              "«&nbsp;Ce que le client accepte&nbsp;: la flexibilité&nbsp;» (3e_C3.3), demandé par Pascal&nbsp;: la phrase du "
              "client → la classe F0–F3, sur la station d'alerte cyclonique. L'exercice des tests (4e_C8.3) reçoit en plus un "
              "tableau de résultats à juger avec la flexibilité (un écart dans la marge F1/F2/F3 se valide, en F0 jamais).</li>"
              "<li>La flexibilité de 4e reprend mot pour mot celle de l'exercice 6 de l'atelier des interacteurs (12&nbsp;V F0, "
              "IPX4 F1, 10&nbsp;L F2, réglage F3)&nbsp;: même jardin, mêmes classes. En 3e, l'élève attribue lui-même les classes, "
              "puis s'en sert pour arbitrer.</li>"
              "<li>Convention de l'atelier&nbsp;: le texte d'un bloc porte toujours un critère et un niveau&nbsp;; la flexibilité "
              "reste dans le tableau du cahier des charges, et peut s'ajouter au texte entre parenthèses («&nbsp;(F2)&nbsp;»). "
              "SysML ne prévoit pas de champ «&nbsp;flexibilité&nbsp;» : c'est un usage scolaire, dit comme tel.</li>"
              "<li>Vocabulaire SysML retenu, et lui seul&nbsp;: «&nbsp;requirement&nbsp;», Id, Text, contenance (⊕), "
              "«&nbsp;verify&nbsp;» (testCase → exigence), «&nbsp;satisfy&nbsp;» (block → exigence). Pas de «&nbsp;refine&nbsp;», "
              "«&nbsp;deriveReqt&nbsp;» ni «&nbsp;trace&nbsp;» au collège.</li>"
              "<li>Inspiration (jamais recopiée)&nbsp;: cahier « 123 Techno » (Bordas 2021) — 3e DIC fiche 5 (gabarit d'exigences à "
              "légender, titre ou texte donné), 3e DIC fiche 4 (paires critère ↔ niveau, critère retrouvé par l'unité), "
              "4e MSOST fiche 26 et 5e MSOST fiche 27 (extrait de cahier des charges + résultats de tests → écart → validé ou "
              "non, piège du minimum). Écarts de l'éditeur corrigés ici&nbsp;: exigences sans Id ni niveau chiffré, pas de "
              "«&nbsp;verify&nbsp;»/«&nbsp;satisfy&nbsp;», F0–F3 jamais définies, test qui exige «&nbsp;écart = 0&nbsp;» malgré une "
              "tolérance.</li>"
              "<li>Faits réels, et leurs sources&nbsp;: codes IP — norme internationale CEI 60529 (NF EN 60529)&nbsp;; IPX4 = "
              "projections d'eau de toutes directions, essai de 10&nbsp;min&nbsp;; indice de réparabilité — loi n°2020-105 du "
              "10 février 2020 (dite AGEC), affichage obligatoire depuis le 1er janvier 2021 pour certaines familles "
              "d'appareils&nbsp;; très basse tension&nbsp;: 12&nbsp;V. Toutes les valeurs des boîtiers, des tests et les prix sont "
              "fictifs, et déclarés comme tels.</li>"
              "<li>La carte des représentations classe ce diagramme «&nbsp;4e / 3e, facultatif&nbsp;»&nbsp;: aucune page de 5e. "
              "L'élève de 3e n'a pas forcément fait la 4e&nbsp;: le cours de 3e reprend la lecture d'un bloc, et l'ouverture "
              "renvoie aux exercices de 4e.</li></ul>")
DEUX_NOMS = ("Le programme de technologie parle d'<b>exigences</b> et de <b>cahier des charges</b>. Le schéma qui dessine ces "
             "exigences dans des blocs reliés s'appelle le <b>diagramme des exigences</b>&nbsp;; les ingénieurs l'appellent "
             "<b>diagramme des exigences SysML</b> (en anglais, <i>requirement diagram</i>). SysML veut dire <i>Systems "
             "Modeling Language</i>, « langage de modélisation des systèmes ». Si tu rencontres l'un des deux noms, tu sauras "
             "que c'est le même schéma.")
QCM_SOUS_TITRE = ("Lire un diagramme des exigences, passer du cahier des charges au bloc, relier une exigence à son test et "
                  "valider avec la flexibilité (4e) ; évaluer deux solutions et arbitrer (3e)")
