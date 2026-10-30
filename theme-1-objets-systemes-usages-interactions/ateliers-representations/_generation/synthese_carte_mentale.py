# -*- coding: utf-8 -*-
"""Synthèse élève de l'atelier « la carte mentale » (carte heuristique) — règle d'or n°316 révisée : deux pages A4.

Rendue par syntheses.eleve() : la carte « Ce que je dois retenir », puis, par partie, le titre-question, l'exemple
de l'atelier en deux lignes (en cases quand il compare ou enchaîne), « À retenir », le piège en une ligne ; un seul
lexique à la fin. Les cartes mentales dessinées restent dans les pages de l'atelier.
"""

H1 = "la carte mentale, pour ranger ses idées"
PB = "Une idée au centre, des familles autour, quelques mots au bout. · 5e · 4e · 3e"
QUESTION = "Comment ranger ses idées et ses données pour les retrouver, les peser et les défendre&nbsp;?"

PARTIES = [
    # ── 5e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="5e", emoji="🌳",
        titre="Comment ranger les données d'un projet dans une carte mentale&nbsp;?",
        titre_court="Qu'est-ce qu'une carte mentale&nbsp;?",
        carte="Une idée centrale, une branche par famille avec un mot dessus, et au bout, les données en quelques mots.",
        exemple=(
            "<p>Le projet lampadaire de la classe de 5e, dans une <b>carte mentale</b> (on dit aussi <b>carte "
            "heuristique</b>, <i lang=\"en\">mind map</i> en anglais)&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>Au centre&nbsp;: le sujet</b>«&nbsp;Notre projet&nbsp;: le lampadaire&nbsp;»</div>"
            "<div><b>Les branches&nbsp;: un mot par famille</b>Photos, Mesures, Programmes, Croquis…</div>"
            "<div><b>Les feuilles&nbsp;: quelques mots</b>«&nbsp;le capteur de lumière, vu de près&nbsp;»</div>"
            '<div class="ko"><b>La LED ✘</b>Un objet, pas une donnée&nbsp;: on range sa photo.</div></div>'),
        retenir="la carte mentale part d'une <b>idée centrale</b>&nbsp;; chaque <b>branche</b> nomme une <b>famille</b>. "
                "On y range des <b>données</b>&nbsp;: ce qui s'enregistre dans un <b>fichier</b>.",
        piege="ouvrir une branche «&nbsp;Divers&nbsp;». Une idée sans place est une nouvelle famille, ou elle est hors "
              "sujet.",
    ),
    dict(
        niveau="5e", emoji="📁",
        titre="Comment ranger et retrouver les fichiers dans l'ordinateur&nbsp;?",
        titre_court="Comment ranger les fichiers&nbsp;?",
        carte="Comme la carte&nbsp;: le dossier du projet au centre, un dossier par branche, un fichier par feuille.",
        exemple=(
            "<p>La carte donne l'<b>arborescence</b>. Le <b>chemin</b> se lit du plus grand dossier au plus petit&nbsp;:</p>"
            '<div class="chaine etapes">'
            "<div><b>Documents › 5e</b>le dossier de la classe</div>"
            "<div><b>Lampadaire</b>l'idée centrale</div>"
            "<div><b>Mesures</b>une branche</div>"
            "<div><b>releves_mardi.csv</b>une feuille&nbsp;: le fichier</div></div>"),
        retenir="idée centrale → <b>dossier</b> du projet, branche → <b>dossier</b>, feuille → <b>fichier</b>. "
                "L'<b>extension</b> (.jpg, .csv) dit le format&nbsp;; le <b>nom</b> dit de quoi parle le fichier.",
        piege="ranger d'après la seule extension&nbsp;: croquis_boitier_v2.jpg est une image, mais il va dans Croquis.",
    ),
    # ── 4e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="4e", emoji="⚖️",
        titre="Comment peser une évolution technologique avec une carte mentale&nbsp;?",
        titre_court="Comment peser une évolution&nbsp;?",
        carte="Avantages et inconvénients sur deux branches face à face&nbsp;; une phrase vraie mais hors sujet reste "
              "dehors.",
        exemple=(
            "<p>De l'arrosoir à l'arrosage connecté du jardin du collège, au centre de la carte&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>Avantages</b>N\'arrose que si la terre est sèche. Arrose pendant les vacances.</div>'
            '<div class="ok"><b>Inconvénients</b>La pompe consomme de l\'électricité. Tout s\'arrête sans wifi.</div>'
            '<div class="ok"><b>Pour qui&nbsp;?</b>Mme&nbsp;Joseph suit tout sur son téléphone.</div>'
            '<div class="ko"><b>Hors sujet ✘</b>«&nbsp;Les plantes ont besoin d\'eau.&nbsp;» Vrai avant comme après.</div>'
            "</div>"),
        retenir="pour juger une <b>évolution</b>, on range ses <b>avantages</b> et ses <b>inconvénients</b> face à face, "
                "en disant <b>pour qui</b>. Une phrase vraie qui ne dit rien de l'évolution est <b>hors sujet</b>.",
        piege="garder une phrase parce qu'elle est vraie&nbsp;: elle doit parler du changement.",
    ),
    dict(
        niveau="4e", emoji="👓",
        titre="Qu'est-ce qui rend une carte mentale facile à lire&nbsp;?",
        titre_court="Une carte facile à lire&nbsp;?",
        carte="Un sujet au centre, un mot sur chaque branche, des mots-clés, et pas de branche «&nbsp;Divers&nbsp;».",
        exemple=(
            "<p>La carte d'Enzo a de bonnes idées, mais elle se lit mal&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ko"><b>«&nbsp;4e B — mardi&nbsp;» ✘</b>Au centre&nbsp;: le sujet, pas la classe ni la date.</div>'
            '<div class="ko"><b>Une couleur, sans mot ✘</b>Un mot sur chaque branche, la couleur en plus.</div>'
            '<div class="ko"><b>«&nbsp;Divers&nbsp;» ✘</b>Chaque idée dans sa vraie branche.</div>'
            '<div class="ok"><b>Des mots-clés ✔</b>«&nbsp;plus besoin de venir&nbsp;», pas une phrase.</div></div>'),
        retenir="une carte <b>lisible</b> a un <b>sujet au centre</b> et <b>un mot sur chaque branche</b>. Ses feuilles "
                "sont des <b>mots-clés</b>&nbsp;; elle n'a <b>pas de branche «&nbsp;Divers&nbsp;»</b>.",
        piege="prendre l'absence de flèches pour un défaut&nbsp;: une carte mentale range des idées, sans ordre.",
    ),
    # ── 3e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="3e", emoji="🗣️",
        titre="Comment passer de la carte mentale à un argumentaire court&nbsp;?",
        titre_court="De la carte à l'argumentaire&nbsp;?",
        carte="On choisit une branche positive et une négative, on les relie par «&nbsp;cependant&nbsp;», et on conclut.",
        exemple=(
            "<p>«&nbsp;La station d'alerte cyclonique est-elle une bonne chose pour les habitants&nbsp;?&nbsp;» Trois "
            "temps, tirés de la carte&nbsp;:</p>"
            '<div class="chaine etapes">'
            "<div><b>1. Une incidence positive</b>L'alerte arrive plus tôt&nbsp;: on a le temps d'évacuer.</div>"
            "<div><b>2. Cependant, une négative</b>Une fausse alerte ferme les écoles pour rien.</div>"
            "<div><b>3. Une conclusion nuancée</b>Utile, à condition de limiter les fausses alertes.</div></div>"),
        retenir="la carte mentale <b>prépare l'argumentaire</b>. Le texte donne une <b>incidence positive</b>, une "
                "<b>négative</b> après un <b>connecteur d'opposition</b>, puis une <b>conclusion nuancée</b>.",
        piege="décrire le fonctionnement («&nbsp;elle mesure le vent&nbsp;») au lieu d'un effet sur la vie des gens.",
    ),
    dict(
        niveau="3e", emoji="🧭",
        titre="Quand choisir la carte mentale, et quand une autre représentation&nbsp;?",
        titre_court="Carte mentale ou autre chose&nbsp;?",
        carte="La carte mentale organise et fait retenir&nbsp;; pour montrer ce qui circule ou un ordre, on prend autre "
              "chose.",
        exemple=(
            "<p>Le même comportement de la station se dessine de plusieurs façons. Chacune répond à une question&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>Organiser, réviser</b>la carte mentale</div>'
            "<div><b>L'ordre et les tests</b>l'algorigramme</div>"
            "<div><b>Le chemin de l'énergie</b>la chaîne d'énergie</div>"
            "<div><b>Ce qui entoure l'objet</b>le diagramme pieuvre</div></div>"),
        retenir="la carte mentale sert à <b>organiser</b> et à <b>retenir</b>. Pour montrer <b>ce qui circule</b> ou "
                "<b>l'ordre des opérations</b>, on prend une chaîne ou un <b>algorigramme</b>.",
        piege="confondre avec le diagramme pieuvre&nbsp;: lui montre ce qui entoure l'objet, pas des idées rangées.",
    ),
]

LEXIQUE = [
    ("carte mentale", "mind map", "des idées rangées autour d'un sujet."),
    ("idée centrale", "central idea", "le sujet, au milieu."),
    ("branche", "branch", "une famille d'idées, avec son mot."),
    ("feuille", "leaf", "le bout d'une branche&nbsp;: quelques mots."),
    ("mot-clé", "keyword", "quelques mots qui rappellent l'idée."),
    ("recenser", "to list", "faire la liste de tout, sans trier."),
    ("donnée", "data", "ce qui s'enregistre dans un fichier."),
    ("fichier", "file", "ce que l'ordinateur garde sous un nom."),
    ("dossier", "folder", "ce qui range des fichiers."),
    ("arborescence", "file tree", "des dossiers dans des dossiers."),
    ("chemin", "path", "la suite des dossiers jusqu'au fichier."),
    ("extension", "file extension", "les lettres après le point."),
    ("évolution technologique", "technological change", "une nouvelle façon de faire."),
    ("avantage", "advantage", "ce que l'évolution apporte."),
    ("inconvénient", "drawback", "ce qu'elle coûte ou rend fragile."),
    ("incidence sur la société", "impact on society", "un effet sur les gens."),
    ("argumentaire", "argument", "un texte court qui défend un avis."),
    ("connecteur d'opposition", "contrast connector", "mais, cependant."),
    ("algorigramme", "flowchart", "l'ordre des opérations, dessiné."),
]
