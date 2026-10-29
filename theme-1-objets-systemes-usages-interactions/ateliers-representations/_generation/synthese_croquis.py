# -*- coding: utf-8 -*-
"""Synthèse élève de l'atelier « le croquis » (croquis à main levée) — règle d'or n°316 révisée : deux pages A4.

Rendue par syntheses.eleve() : la carte « Ce que je dois retenir », puis, par partie, le titre-question, l'exemple
de l'atelier en deux lignes (en cases quand il compare ou enchaîne), « À retenir », le piège en une ligne ; un seul
lexique à la fin. Les croquis restent dans les pages de l'atelier.
"""

H1 = "le croquis, pour montrer une idée vite et bien"
PB = "Un dessin rapide, sans règle, qui montre l'essentiel. · 4e · 3e"
QUESTION = "Comment montrer une idée ou un usage par un dessin rapide, puis en faire une pièce qu'on peut fabriquer&nbsp;?"

PARTIES = [
    # ── 4e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="4e", emoji="✏️",
        titre="Qu'est-ce qu'un croquis, et à quoi le juge-t-on&nbsp;?",
        titre_court="Qu'est-ce qu'un croquis&nbsp;?",
        carte="Un dessin rapide, sans règle, qui choisit ce qu'il montre&nbsp;; on le juge à ce qu'il fait comprendre.",
        exemple=(
            "<p>On dit souvent <b>croquis à main levée</b>. Inès raconte comment elle sort un vélo de la borne&nbsp;; trois "
            "élèves l'ont dessiné&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>Croquis A ✔</b>La carte, le bip, puis une flèche&nbsp;: Inès tire le vélo vers elle.</div>'
            '<div class="ko"><b>Croquis B ✘</b>La flèche va vers la borne&nbsp;: c\'est son erreur, pousser.</div>'
            '<div class="ko"><b>Croquis C ✘</b>L\'intérieur de la borne&nbsp;: ni Inès, ni son geste.</div></div>'),
        retenir="un <b>croquis</b> est un <b>dessin rapide</b>, sans règle, qui <b>choisit ce qu'il montre</b>. On le juge "
                "à <b>ce qu'il fait comprendre</b>, pas à sa beauté.",
        piege="choisir le croquis le plus technique ou le plus soigné. Pour un usage, il faut la personne et son geste.",
    ),
    dict(
        niveau="4e", emoji="💬",
        titre="Comment passer de ce que raconte un usager à un croquis&nbsp;?",
        titre_court="Du témoignage au croquis&nbsp;?",
        carte="Ce qu'il fait devient une flèche, ce qu'il voit une légende, ce qu'il ressent une bulle.",
        exemple=(
            "<p>Mme&nbsp;Joseph raconte comment elle règle l'heure d'arrosage du jardin. Ce qu'elle dit devient&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>Elle appuie 24 fois sur +</b>Ce qu'elle fait&nbsp;: une flèche de mouvement.</div>"
            "<div><b>L'écran passe à 18:00</b>Ce qu'elle voit&nbsp;: une légende.</div>"
            "<div><b>Sa main en visière</b>Ce qu'elle ressent, la gêne&nbsp;: une bulle.</div>"
            '<div class="ko"><b>L\'intérieur du boîtier ✘</b>Elle ne le voit pas&nbsp;: on ne le dessine pas.</div></div>'),
        retenir="on part <b>des mots de l'usager</b>. Ce qu'il fait devient une <b>flèche de mouvement</b>, ce qu'il "
                "voit une <b>légende</b>, ce qu'il ressent une <b>bulle</b>. Des croquis numérotés forment un "
                "<b>storyboard</b>.",
        piege="dessiner le boîtier seul. Sans la personne ni son geste, on ne voit pas ce que vit la gardienne.",
    ),
    dict(
        niveau="4e", emoji="📏",
        titre="Comment proposer une pièce qu'on pourra fabriquer&nbsp;?",
        titre_court="Proposer une pièce&nbsp;?",
        carte="Par un croquis coté&nbsp;: la forme, les cotes avec leur unité, le matériau, la flèche de montage.",
        exemple=(
            "<p>Pour tenir droit le capteur d'humidité du jardin, on invente un crochet, dessiné en <b>croquis "
            "coté</b>&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>La forme</b>Un crochet qui coiffe le bord du bac, à main levée.</div>"
            "<div><b>Les cotes</b>Une ouverture de 24 mm pour une planche de 22 mm.</div>"
            "<div><b>Le matériau</b>Du PLA, imprimé en 3D&nbsp;: il ne rouille pas.</div>"
            "<div><b>La flèche de montage</b>On enfile le crochet, puis on glisse le capteur.</div></div>"),
        retenir="un <b>croquis coté</b> porte la forme, les <b>cotes avec leur unité</b>, le <b>matériau</b> et la "
                "<b>flèche de montage</b>. Ce sont les cotes, pas le trait, qui donnent les dimensions.",
        piege="oublier l'unité («&nbsp;22&nbsp;»&nbsp;: mm ou cm&nbsp;?), ou croire qu'un croquis coté se trace à la règle.",
    ),
    # ── 3e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="3e", emoji="💡",
        titre="Comment chercher plusieurs solutions avant de choisir&nbsp;?",
        titre_court="Plusieurs solutions&nbsp;?",
        carte="Par des croquis rapides de principes différents, comparés au cahier des charges.",
        exemple=(
            "<p>Fixer la sirène d'alerte sur son poteau, face aux rafales d'un cyclone&nbsp;: trois croquis, trois "
            "principes.</p>"
            '<div class="chaine">'
            '<div class="ok"><b>1. Le collier ✔</b>Serrer autour du poteau.</div>'
            '<div class="ok"><b>2. La platine ✔</b>Poser sur le haut du poteau.</div>'
            '<div class="ok"><b>3. Le bras ✔</b>Accrocher au bout d\'un bras.</div>'
            '<div class="ko"><b>Un collier peint ✘</b>Le même principe&nbsp;: une variante.</div></div>'),
        retenir="on propose <b>plusieurs solutions</b> par des <b>croquis rapides</b>, de <b>principes différents</b>. Puis "
                "on choisit avec le <b>cahier des charges</b>, en disant pourquoi.",
        piege="dessiner trois fois la même solution avec un détail en plus&nbsp;: ce sont des variantes.",
    ),
    dict(
        niveau="3e", emoji="🔩",
        titre="Comment savoir si un croquis coté permet de fabriquer&nbsp;?",
        titre_court="Peut-on fabriquer&nbsp;?",
        carte="Il donne les trois dimensions, leur unité, le matériau et chaque perçage, sur une vue qui le montre.",
        exemple=(
            "<p>Le boîtier de la station doit entrer dans un coffret de 130 × 90 × 70 mm. On compare une à une&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>Longueur ✔</b>120 mm, pour 130 mm de place.</div>'
            '<div class="ok"><b>Hauteur ✔</b>80 mm, pour 90 mm de place.</div>'
            '<div class="ko"><b>Profondeur&nbsp;?</b>Pas de cote&nbsp;: on ne peut pas savoir.</div>'
            '<div class="ko"><b>Il manque aussi</b>Le matériau, et le perçage du câble&nbsp;: diamètre et place.</div></div>'),
        retenir="un <b>croquis coté</b> permet de fabriquer s'il donne <b>les trois dimensions</b> et <b>leur unité</b>. "
                "Il donne aussi le <b>matériau</b> et <b>chaque perçage</b>, sur une <b>vue</b> qui le montre.",
        piege="conclure «&nbsp;ça rentre&nbsp;» en ne comparant que les cotes écrites&nbsp;: une cote qui manque bloque tout.",
    ),
    dict(
        niveau="3e", emoji="🧩",
        titre="Croquis, schéma, graphique, algorithme ou modélisation&nbsp;: lequel choisir&nbsp;?",
        titre_court="Quelle représentation choisir&nbsp;?",
        carte="Le croquis vient d'abord, pour trouver l'idée&nbsp;; les autres la précisent.",
        exemple=(
            "<p>Le <b>schéma</b> montre les liaisons, le <b>graphique</b> une grandeur qui change, l'<b>algorithme</b> "
            "l'ordre des actions. Pour fabriquer, on suit&nbsp;:</p>"
            '<div class="chaine etapes">'
            "<div><b>1. Le croquis</b>L'idée, vite.</div>"
            "<div><b>2. Le croquis coté</b>Les dimensions.</div>"
            "<div><b>3. La modélisation 3D</b>La forme exacte, puis la simulation.</div>"
            "<div><b>4. Le prototype</b>L'essai en vrai.</div></div>"),
        retenir="le <b>croquis</b> est le premier geste. La <b>modélisation 3D</b> donne la forme exacte pour "
                "fabriquer&nbsp;; la <b>simulation</b> fait «&nbsp;fonctionner&nbsp;» ce modèle dans un logiciel.",
        piege="croire qu'une modélisation remplace le croquis&nbsp;: le croquis trouve l'idée, les autres la précisent.",
    ),
]

LEXIQUE = [
    ("croquis", "sketch", "un dessin rapide qui montre l'essentiel."),
    ("à main levée", "freehand", "sans règle ni compas."),
    ("légende", "label", "des mots reliés au dessin par un trait."),
    ("flèche de mouvement", "arrow", "un geste et son sens."),
    ("bulle", "speech bubble", "ce que la personne dit ou ressent."),
    ("ressenti", "user feeling", "ce que l'usager éprouve&nbsp;: gêne, plaisir…"),
    ("storyboard", "storyboard", "une suite de croquis numérotés."),
    ("croquis coté", "dimensioned sketch", "un croquis qui porte des cotes."),
    ("cote", "dimension", "une dimension écrite, avec son unité."),
    ("matériau", "material", "ce dans quoi la pièce est faite."),
    ("flèche de montage", "assembly arrow", "le sens où l'on met la pièce en place."),
    ("principe", "principle", "l'idée qui fait marcher une solution."),
    ("variante", "variant", "la même solution, un détail changé."),
    ("perçage", "hole", "un trou&nbsp;: son diamètre et sa place."),
    ("vue", "view", "le côté d'où l'on dessine la pièce."),
    ("schéma", "diagram", "des symboles normés reliés par des traits."),
    ("algorithme", "algorithm", "des instructions dans l'ordre, avec des «&nbsp;si&nbsp;»."),
    ("modélisation 3D", "3D modelling", "la pièce en volume dans un logiciel."),
    ("prototype", "prototype", "un premier exemplaire, pour essayer."),
]
