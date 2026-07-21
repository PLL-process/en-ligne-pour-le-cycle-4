# -*- coding: utf-8 -*-
"""
Données sources : compétences Nathan (cahiers 5e / 4e / 3e, éd. 2024)
différenciées par niveau, avec domaines du socle commun.
Chaque tuple = (code_sous_competence, texte, domaines_socle)
"""

# Compétences parentes C1-C9 (identiques sur les 3 cahiers Nathan / conformes BO n°9 du 29/02/2024)
C_PARENT = {
    "C1": ("Décrire les liens entre usages et évolutions technologiques des objets et des systèmes techniques", "D2, D3, D4, D5", 1),
    "C2": ("Décrire les interactions entre un objet ou un système technique, son environnement et les utilisateurs", "D4, D5", 1),
    "C3": ("Caractériser et choisir un objet ou un système technique selon différents critères", "D1.3, D2, D3, D4, D5", 1),
    "C4": ("Décrire et caractériser l’organisation interne d’un objet ou d’un système technique et ses échanges avec son environnement (énergies, données)", "D1.3, D1.4, D2, D4, D5", 2),
    "C5": ("Identifier un dysfonctionnement d’un objet technique et y remédier", "D1.3, D2, D3, D4, D5", 2),
    "C6": ("Comprendre et modifier un programme associé à une fonctionnalité d’un objet ou d’un système technique", "D1.3, D2, D4", 2),
    "C7": ("Imaginer, concevoir et réaliser une ou des solutions en réponse à un besoin, à des exigences (de développement durable, par exemple) ou à la nécessité d’améliorations dans une démarche de créativité", "D2, D3, D4, D5", 3),
    "C8": ("Valider les solutions techniques par des simulations ou par des protocoles de tests", "D1.3, D2, D3, D4, D5", 3),
    "C9": ("Concevoir, écrire, tester et mettre au point un programme", "D1.3, D2, D4", 3),
}

THEME_TITLES = {
    1: "Les objets et les systèmes techniques : leurs usages et leurs interactions à découvrir et à analyser",
    2: "Structure, fonctionnement, comportement : des objets et des systèmes techniques à comprendre",
    3: "Création, conception, réalisation, innovations : des objets à concevoir et à réaliser",
}

# ---------------------------------------------------------------------------
# 5e — Nathan, Cahier d'activités Technologie 5e
# ---------------------------------------------------------------------------
COMP_5E = {
    "C1": [
        ("C1.1", "Collecter, trier et analyser des données.", "D2, D4"),
        ("C1.2", "Comparer des principes techniques pour une même fonction technique.", "D2, D4"),
        ("C1.3", "Décrire le rôle des systèmes d’information dans le partage d’information.", "D2, D5"),
        ("C1.4", "Recenser des données, les identifier, les classer, les représenter, les stocker, les retrouver dans une arborescence.", "D2"),
        ("C1.5", "Identifier des règles permettant de sécuriser un environnement numérique (bases de la cybersécurité) et des règles de respect de la propriété intellectuelle.", "D3"),
        ("C1.6", "Appréhender la responsabilité de chacun dans les dérives (cyberviolence, atteinte à la vie privée, aux données personnelles, usurpation d’identité).", "D3"),
    ],
    "C2": [
        ("C2.1", "Faire la liste des interacteurs extérieurs d’un OST.", "D4"),
        ("C2.2", "Repérer et expliquer les choix de conception dans les domaines de l’ergonomie et de la sécurité ou en lien avec des objectifs de développement durable.", "D4, D5"),
    ],
    "C3": [
        ("C3.1", "Repérer pour un OST les matériaux, les sources et les formes d’énergies, le traitement de l’information.", "D2, D4"),
        ("C3.2", "Identifier les étapes du cycle de vie d’un OST influencées par les choix de matériaux et d’énergie.", "D3, D4, D5"),
        ("C3.3", "Choisir un OST parmi plusieurs propositions en vue de répondre à un besoin.", "D3, D4, D5"),
        ("C3.4", "Mesurer et comparer une performance d’un OST à partir d’un protocole fourni.", "D1.3, D2, D4"),
    ],
    "C4": [
        ("C4.1", "Associer des solutions techniques à une ou des fonctions techniques.", "D2, D4, D5"),
        ("C4.2", "Identifier des constituants de la chaîne d’énergie d’un objet technique (l’organisation de la chaîne d’énergie étant fournie).", "D1.3, D2, D4"),
        ("C4.3", "Indiquer la nature des énergies en entrée et en sortie des constituants de la chaîne d’énergie.", "D1.3, D4"),
        ("C4.4", "Identifier les principaux matériaux constitutifs d’un OST.", "D3, D4, D5"),
        ("C4.5", "Identifier des constituants de la chaîne d’information d’un OST (l’organisation de la chaîne d’information étant fournie).", "D1.3, D2, D4"),
        ("C4.6", "Déterminer des descripteurs permettant de décrire des objets sous forme de données en précisant leurs types et leurs formats.", "D1.3, D2, D4"),
        ("C4.7", "Identifier les composants qui constituent un réseau local (terminaux, commutateurs, liaisons filaires et sans fil (WiFi)) et sa topologie.", "D2, D4"),
        ("C4.8", "Justifier la nécessité d’identifier les terminaux pour communiquer sur un réseau local (activité débranchée et vérification par un outil de simulation).", "D2, D4"),
    ],
    "C5": [
        ("C5.1", "Repérer visuellement une pièce défectueuse.", "D1.3, D2, D4"),
        ("C5.2", "Réaliser une réparation en suivant un protocole fourni.", "D2, D3, D4"),
        ("C5.3", "Découvrir les procédés de réalisation présents dans un atelier de fabrication collaboratif.", "D2, D3, D4, D5"),
    ],
    "C6": [
        ("C6.1", "Identifier les données utilisées et produites par le programme associé à une fonctionnalité d’un OST (à partir d’un programme existant).", "D1.3, D2, D4"),
        ("C6.2", "Comprendre et traduire en un algorithme en langage naturel le programme associé à une fonctionnalité d’un OST.", "D1.3, D4"),
        ("C6.3", "Modifier les paramètres d’un programme et identifier ou évaluer ses effets en termes de fonctionnalité.", "D1.3, D4"),
    ],
    "C7": [
        ("C7.1", "Suivre un processus de conception et de réalisation dans une durée, avec des tâches identifiées.", "D2, D4, D5"),
        ("C7.2", "Fabriquer une solution pour améliorer un OST existant.", "D2, D3, D4"),
        ("C7.3", "Choisir un matériau parmi plusieurs proposés en fonction de leurs caractéristiques.", "D3, D4, D5"),
        ("C7.4", "Choisir une source d’énergie parmi plusieurs proposées et une forme d’énergie possible.", "D3, D4, D5"),
        ("C7.5", "Assembler les constituants fournis pour réaliser un prototype.", "D2, D3, D4"),
        ("C7.6", "Mettre en œuvre les moyens pour réaliser une forme selon une procédure fournie.", "D2, D3, D4"),
    ],
    "C8": [
        ("C8.1", "Utiliser une simulation fournie pour valider la tenue mécanique d’un matériau.", "D1.3, D2, D4"),
        ("C8.2", "Mettre en œuvre un protocole de test fourni pour valider la tenue mécanique d’un matériau.", "D1.3, D2, D3, D4"),
        ("C8.3", "Vérifier le comportement et les performances d’un objet technique en suivant un protocole fourni.", "D1.3, D2, D4, D5"),
    ],
    "C9": [
        ("C9.1", "Analyser un programme simple fourni et tester s’il répond au besoin ou au problème posé.", "D1.3, D2, D4"),
        ("C9.2", "Modifier un programme fourni pour répondre au besoin ou à un problème posé.", "D1.3, D2, D4"),
        ("C9.3", "Réaliser et mettre au point un programme simple commandant un OST.", "D1.3, D2, D4"),
    ],
}

# ---------------------------------------------------------------------------
# 4e — Nathan, Cahier d'activités Technologie 4e
# ---------------------------------------------------------------------------
COMP_4E = {
    "C1": [
        ("C1.1", "Mettre en relation les OST avec leurs usages.", "D4, D5"),
        ("C1.2", "Identifier les avantages et les inconvénients associés aux évolutions technologiques et informatiques.", "D3, D4, D5"),
        ("C1.3", "Justifier l’évolution d’un OST pour répondre à l’évolution des besoins.", "D3, D4, D5"),
        ("C1.4", "Identifier et appliquer les règles pour un usage raisonné des objets communicants et des environnements numériques (propriété intellectuelle, identité numérique, témoins de connexion, géolocalisation).", "D1.3, D2, D3, D4"),
    ],
    "C2": [
        ("C2.1", "Décrire l’expérience de l’utilisateur (ressenti et facilité d’usage) d’un OST en partant du langage naturel (texte, croquis) pour aboutir aux schémas, graphiques, algorithmes.", "D1.3, D4, D5"),
        ("C2.2", "Repérer et expliquer les contraintes, exigences prises en compte (sécurité, incidences environnementales, formes et fonctions, ergonomie, qualité, fiabilité) pour répondre aux attentes des utilisateurs.", "D3, D4, D5"),
    ],
    "C3": [
        ("C3.1", "Identifier les caractéristiques à prendre en compte dans le choix d’un OST en vue de répondre à un besoin.", "D3, D4, D5"),
        ("C3.2", "Comparer qualitativement et/ou quantitativement (incidences environnementales, bilan carbone, efficacité énergétique) plusieurs OST répondant au même besoin et arrêter un choix.", "D1.3, D2, D3, D4, D5"),
        ("C3.3", "Choisir les appareils de mesure à utiliser pour mesurer une performance d’un OST à partir d’un protocole donné.", "D1.3, D2, D4"),
    ],
    "C4": [
        ("C4.1", "Identifier les constituants d’une chaîne d’énergie et les associer à leurs fonctions.", "D2, D4, D5"),
        ("C4.2", "Repérer les transformations d’énergie et les flux d’énergie au sein de l’OST.", "D1.3, D2, D4"),
        ("C4.3", "Mettre en relation la forme d’une pièce avec le procédé de réalisation.", "D3, D4, D5"),
        ("C4.4", "Identifier les constituants de la chaîne d’information d’un objet réel et les associer à leur fonction.", "D1.3, D2, D4"),
        ("C4.5", "Décrire et analyser la transformation des données téléversées ou issues d’un OST.", "D1.3, D2, D4"),
        ("C4.6", "Décrire et analyser la structuration d’une table de données qui permet une exploitation et une interprétation du comportement d’un OST.", "D1.3, D2, D4"),
        ("C4.7", "Paramétrer une adresse IP fixe pour ajouter un objet connecté à un réseau local.", "D2, D4"),
        ("C4.8", "Résoudre des problèmes pour assurer la communication entre les différents terminaux dans un réseau informatique (simulation ou réseau local déconnecté du réseau pédagogique).", "D2, D4"),
        ("C4.9", "Compléter une simulation fournie pour valider le comportement d’un réseau informatique.", "D2, D4"),
    ],
    "C5": [
        ("C5.1", "Proposer un protocole permettant de vérifier l’origine d’un dysfonctionnement.", "D1.3, D2, D4"),
        ("C5.2", "Remplacer une pièce défectueuse sans protocole fourni (la pièce de remplacement étant fournie).", "D2, D3, D4"),
        ("C5.3", "Choisir les procédés de réalisation et les mettre en œuvre.", "D2, D3, D4"),
    ],
    "C6": [
        ("C6.1", "Analyser les données et en déduire des modifications à apporter au programme.", "D1.3, D2, D4"),
        ("C6.2", "Compléter un programme pour répondre à une fonctionnalité d’un OST.", "D1.3, D2, D4"),
        ("C6.3", "Tester et valider, dans un environnement simulé ou réel, une modification du programme.", "D1.3, D2, D4"),
    ],
    "C7": [
        ("C7.1", "Organiser un processus de conception et de réalisation dans une durée, avec des tâches identifiées.", "D2, D4, D5"),
        ("C7.2", "Proposer et fabriquer une solution pour ajouter une nouvelle fonction à un OST (croquis, schéma, graphique, algorithme, modélisation).", "D2, D3, D4"),
        ("C7.3", "Comparer différents matériaux pour choisir le plus adapté.", "D3, D4, D5"),
        ("C7.4", "Comparer différentes sources d’énergie pour choisir la plus adaptée.", "D3, D4, D5"),
        ("C7.5", "Identifier les constituants manquants dans un prototype et le compléter.", "D2, D3, D4"),
        ("C7.6", "Modifier une forme à l’aide d’une modélisation.", "D2, D3, D4"),
        ("C7.7", "Choisir les moyens et produire la forme voulue.", "D2, D3, D4"),
        ("C7.8", "Interfacer un objet technique avec un réseau.", "D2, D3, D4"),
    ],
    "C8": [
        ("C8.1", "Paramétrer une simulation fournie pour valider la tenue mécanique d’un matériau.", "D1.3, D2, D4"),
        ("C8.2", "Proposer un protocole de test pour valider la tenue mécanique d’un matériau.", "D1.3, D2, D3, D4"),
        ("C8.3", "Proposer un protocole de test pour valider le comportement et les performances d’un objet technique.", "D1.3, D2, D3, D4, D5"),
    ],
    "C9": [
        ("C9.1", "Modifier un algorithme permettant de répondre au besoin ou au problème posé.", "D1.3, D2, D4"),
        ("C9.2", "Traduire un algorithme permettant de répondre à un besoin ou à un problème simple en un programme.", "D1.3, D2, D4"),
        ("C9.3", "Réaliser et mettre au point un programme commandant un système réel incluant éventuellement une interaction entre un humain et une machine.", "D1.3, D2, D4"),
    ],
}

# ---------------------------------------------------------------------------
# 3e — Nathan, Cahier d'activités Technologie 3e (édition 2024)
# Domaines du socle proposés par extrapolation cohérente avec les grilles
# 5e/4e ci-dessus (non fournis tels quels dans le cahier Nathan 3e).
# ---------------------------------------------------------------------------
COMP_3E = {
    "C1": [
        ("C1.1", "Identifier les innovations de rupture qui sont attachées à l’évolution d’un OST.", "D3, D4, D5"),
        ("C1.2", "Mettre en relation une découverte scientifique avec ses développements technologiques et leurs effets sur la société.", "D3, D4, D5"),
        ("C1.3", "Exprimer dans un argumentaire court l’incidence d’un OST sur la société.", "D3, D4, D5"),
        ("C1.4", "Exprimer dans un argumentaire court l’incidence des contraintes sociétales sur les OST.", "D3, D4, D5"),
        ("C1.5", "Exprimer dans un argumentaire court le rôle du développement stratégique du numérique au sein de la société et des environnements professionnels (ou des métiers).", "D1.3, D2, D3"),
    ],
    "C2": [
        ("C2.1", "Décrire l’expérience de l’utilisateur d’un OST à l’aide de modes de représentation choisis.", "D1.3, D4, D5"),
    ],
    "C3": [
        ("C3.1", "Établir une liste d’OST possibles en vue de répondre à un besoin.", "D3, D4, D5"),
        ("C3.2", "Choisir un OST et argumenter ce choix en prenant en compte son cycle de vie et les trois piliers du développement durable.", "D3, D4, D5"),
        ("C3.3", "Évaluer les OST selon des exigences ou des critères identifiés (caractéristiques, performances, coût, indice de réparabilité).", "D3, D4, D5"),
        ("C3.4", "Définir et mettre en œuvre un protocole pour mesurer une caractéristique, une performance d’un OST.", "D1.3, D2, D4"),
    ],
    "C4": [
        ("C4.1", "Élaborer, à l’aide d’un schéma bloc, la chaîne d’énergie d’un OST.", "D1.3, D2, D4"),
        ("C4.2", "Justifier le choix d’un matériau et de son procédé de mise en forme au regard des contraintes techniques et environnementales.", "D3, D4, D5"),
        ("C4.3", "Décrire un OST en caractérisant sa chaîne d’information.", "D1.3, D2, D4"),
        ("C4.4", "Associer des grandeurs analogiques issues d’un OST à des données exploitables.", "D1.3, D2, D4"),
        ("C4.5", "Représenter sous forme de données les informations de diverses natures utilisées par un OST.", "D1.3, D2, D4"),
        ("C4.6", "Identifier, selon les cas, leur mise en forme, leur transmission ou leur stockage dans des fichiers (texte, image, nombre) afin de comprendre le fonctionnement de l’OST.", "D1.3, D2, D4"),
        ("C4.7", "Identifier et représenter la circulation d’une information dans le réseau Internet.", "D2, D4"),
        ("C4.8", "Justifier la nécessité d’un protocole de routage pour faire communiquer plusieurs réseaux (activité débranchée, table de routage donnée).", "D2, D4"),
    ],
    "C5": [
        ("C5.1", "Formuler des hypothèses expliquant le dysfonctionnement d’un objet technique.", "D1.3, D2, D4"),
        ("C5.2", "Proposer un protocole de dépannage puis de réparation.", "D1.3, D2, D4"),
        ("C5.3", "Réaliser le dépannage ou la réparation d’un système défectueux.", "D2, D3, D4"),
        ("C5.4", "Réaliser une pièce sur mesure pour réparer un objet technique.", "D2, D3, D4"),
    ],
    "C6": [
        ("C6.1", "Déterminer les données utilisées et produites par un programme associé à une fonctionnalité en vue de le modifier.", "D1.3, D2, D4"),
        ("C6.2", "Programmer un algorithme lié à une nouvelle fonctionnalité.", "D1.3, D2, D4"),
        ("C6.3", "Modifier et tester le programme associé à une nouvelle fonctionnalité d’un OST.", "D1.3, D2, D4"),
    ],
    "C7": [
        ("C7.1", "Élaborer un processus de conception et de réalisation dans une durée, avec des tâches identifiées.", "D2, D4, D5"),
        ("C7.2", "Proposer et fabriquer un ensemble de solutions pour produire un nouvel OST (croquis, schéma, graphique, algorithme, modélisation).", "D2, D3, D4"),
        ("C7.3", "Choisir un matériau constitutif d’un objet et/ou système technique.", "D3, D4, D5"),
        ("C7.4", "Choisir une source d’énergie pour un OST.", "D3, D4, D5"),
        ("C7.5", "Choisir les constituants et assembler un prototype.", "D2, D3, D4"),
        ("C7.6", "Modéliser une forme voulue.", "D2, D3, D4"),
        ("C7.7", "Choisir les moyens et produire la forme voulue.", "D2, D3, D4"),
        ("C7.8", "Interfacer deux objets techniques communicants.", "D2, D3, D4"),
    ],
    "C8": [
        ("C8.1", "Mettre en œuvre une simulation pour valider la tenue mécanique d’un matériau.", "D1.3, D2, D4"),
        ("C8.2", "Proposer un protocole de test pour valider la tenue mécanique d’un matériau.", "D1.3, D2, D3, D4"),
        ("C8.3", "Proposer un protocole de test pour valider le comportement et les performances d’un objet technique.", "D1.3, D2, D3, D4, D5"),
    ],
    "C9": [
        ("C9.1", "Élaborer ou concevoir un algorithme permettant de répondre au besoin visé, puis le traduire en un programme structuré (appel de sous-programmes ou de fonctions), le tester et le mettre au point.", "D1.3, D2, D4"),
        ("C9.2", "Réaliser et mettre au point un programme commandant un système réel incluant une interaction entre un humain et une machine.", "D1.3, D2, D4"),
    ],
}

COMP_BY_LEVEL = {"5e": COMP_5E, "4e": COMP_4E, "3e": COMP_3E}

if __name__ == "__main__":
    for lvl, comp in COMP_BY_LEVEL.items():
        n = sum(len(v) for v in comp.values())
        print(lvl, "->", n, "sous-competences", "sur", len(comp), "familles")
