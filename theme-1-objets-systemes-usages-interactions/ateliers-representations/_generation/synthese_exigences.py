# -*- coding: utf-8 -*-
"""Synthèse élève de l'atelier « le diagramme des exigences » (diagramme des exigences SysML) — règle d'or n°316
révisée : deux pages A4.

Rendue par syntheses.eleve() : la carte « Ce que je dois retenir », puis, par partie, le titre-question, l'exemple
de l'atelier en deux lignes (en cases quand il compare ou enchaîne), « À retenir », le piège en une ligne ; un seul
lexique à la fin. Les grands schémas restent dans les pages de l'atelier.
"""

H1 = "les exigences, et le diagramme qui les dessine"
PB = "Ce que l'objet doit faire, écrit pour qu'on puisse le vérifier, le tester et choisir. · 4e · 3e"
QUESTION = "Comment écrire ce qu'un système doit faire, puis vérifier qu'il le fait, pour choisir la bonne solution&nbsp;?"

PARTIES = [
    # ── 4e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="4e", emoji="📋",
        titre="Comment lire un diagramme des exigences&nbsp;?",
        titre_court="Comment le lire&nbsp;?",
        carte="Chaque bloc a un nom, un Id et un texte avec critère et niveau. La mère n'est tenue que si toutes ses "
              "filles le sont.",
        exemple=(
            "<p>Le <b>diagramme des exigences</b> (ou diagramme SysML) dessine le cahier des charges en blocs. Celui du "
            "système d'arrosage du jardin&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>«&nbsp;requirement&nbsp;» et le nom</b>Étanchéité. Requirement veut dire exigence.</div>"
            "<div><b>L'Id</b>1.1&nbsp;: la première fille de l'exigence 1. Un numéro, pas un rang.</div>"
            "<div><b>Le texte</b>«&nbsp;IPX4 au moins&nbsp;»&nbsp;: un critère et un niveau.</div>"
            "<div><b>Le lien ⊕</b>La mère 1 contient ses filles 1.1 à 1.4.</div></div>"),
        retenir="un <b>bloc d'exigence</b> a un <b>nom</b>, un <b>Id</b> et un <b>texte</b> (critère et niveau). Avec le "
                "lien <b>⊕</b>, la mère n'est tenue que si <b>toutes</b> ses filles le sont. Chaque exigence a sa "
                "catégorie&nbsp;: sécurité, fiabilité, ergonomie…",
        piege="lire l'Id comme une mesure ou un rang d'importance&nbsp;: il dit seulement la place de l'exigence.",
    ),
    dict(
        niveau="4e", emoji="✍️",
        titre="Comment transformer une ligne du cahier des charges en bloc d'exigence&nbsp;?",
        titre_court="Comment écrire un bloc&nbsp;?",
        carte="La désignation donne le nom, le critère et le niveau donnent le texte. Une exigence dit quoi, jamais comment.",
        exemple=(
            "<p>Suivre l'arrosage sur le smartphone de la gardienne&nbsp;: deux lignes du cahier des charges deviennent "
            "deux blocs.</p>"
            '<div class="chaine">'
            '<div class="ok"><b>2.1 Compte rendu ✔</b>Sur le smartphone, 5 minutes au plus après l\'arrosage.</div>'
            '<div class="ok"><b>2.2 Alerte cuve ✔</b>Une alerte dès qu\'il reste 50 litres dans la cuve.</div>'
            '<div class="ko"><b>«&nbsp;Prévenir assez vite&nbsp;» ✘</b>Aucun nombre&nbsp;: rien à vérifier.</div>'
            '<div class="ko"><b>«&nbsp;Une carte Wi-Fi&nbsp;» ✘</b>Une pièce&nbsp;: c\'est une solution.</div></div>'),
        retenir="la <b>désignation</b> donne le <b>nom</b>&nbsp;; le <b>critère</b> et le <b>niveau</b> donnent le "
                "<b>texte</b>. Une exigence dit <b>ce que</b> le système doit faire, jamais <b>comment</b>.",
        piege="écrire une solution (une carte Wi-Fi, une pompe) dans un bloc «&nbsp;requirement&nbsp;».",
    ),
    dict(
        niveau="4e", emoji="🧪",
        titre="Comment prouver qu'une exigence est respectée&nbsp;?",
        titre_court="Comment le prouver&nbsp;?",
        carte="Par un test qui mesure, relié à l'exigence par la flèche «&nbsp;verify&nbsp;». Un avis n'est pas un test.",
        exemple=(
            "<p>Chaque exigence a son test (l'arroseur pour l'étanchéité, le multimètre pour la tension). Le protocole "
            "du compte rendu&nbsp;:</p>"
            '<div class="chaine etapes">'
            "<div><b>1. Quoi&nbsp;?</b>Le temps jusqu'au message.</div>"
            "<div><b>2. Avec quoi&nbsp;?</b>Un chronomètre.</div>"
            "<div><b>3. Comment&nbsp;?</b>Je le lance dès que l'arrosage s'arrête.</div>"
            "<div><b>4. Quel seuil&nbsp;?</b>5 minutes au plus.</div></div>"),
        retenir="une exigence se prouve par <b>un test qui mesure</b>, relié par la flèche <b>«&nbsp;verify&nbsp;»</b>. "
                "Le <b>protocole</b> dit <b>quoi</b>, <b>avec quoi</b>, <b>comment</b>, et <b>le seuil</b>, avant l'essai.",
        piege="croire qu'un avis («&nbsp;il a l'air solide&nbsp;») est un test&nbsp;: rien n'y est mesuré.",
    ),
    dict(
        niveau="4e", emoji="⚖️",
        titre="Comment décider si le résultat d'un test est assez bon&nbsp;?",
        titre_court="Le résultat est-il assez bon&nbsp;?",
        carte="On compare l'écart à la flexibilité&nbsp;: dans la marge, validée&nbsp;; hors de la marge, non validée.",
        exemple=(
            "<p>Écart = résultat mesuré − niveau demandé. Les résultats du prototype&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>Réglage ✔</b>4 minutes au lieu de 2&nbsp;; en F3, jusqu\'à 5 minutes.</div>'
            '<div class="ko"><b>Sobriété ✘</b>11,5 litres&nbsp;; en F2, la marge s\'arrête à 11 litres.</div>'
            '<div class="ko"><b>Tension ✘</b>24 volts au lieu de 12&nbsp;; en F0, aucun écart.</div></div>'),
        retenir="on <b>valide</b> en comparant <b>l'écart</b> à la <b>flexibilité</b>, de <b>F0</b> (impératif) à "
                "<b>F3</b> (très négociable). Dans la marge&nbsp;: validée. Hors de la marge, même de peu&nbsp;: non "
                "validée.",
        piege="valider un résultat «&nbsp;presque bon&nbsp;»&nbsp;: 11,5 litres sort d'une marge qui s'arrête à 11 litres.",
    ),
    # ── 3e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="3e", emoji="✅",
        titre="Comment évaluer une solution, exigence par exigence&nbsp;?",
        titre_court="Comment évaluer une solution&nbsp;?",
        carte="On compare sa valeur au niveau de chaque exigence&nbsp;; l'égalité satisfait. La flèche «&nbsp;satisfy&nbsp;» "
              "le montre.",
        exemple=(
            "<p>Deux boîtiers pour la station d'alerte cyclonique du quartier, comparés exigence par exigence&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>B, autonomie ✔</b>72 heures pour «&nbsp;72 heures au moins&nbsp;»&nbsp;: l\'égalité '
            "suffit.</div>"
            '<div class="ok"><b>A, coût ✔</b>290 euros pour «&nbsp;300 euros au plus&nbsp;».</div>'
            '<div class="ko"><b>B, étanchéité ✘</b>IP54 pour «&nbsp;IP65 au moins&nbsp;»&nbsp;: 5 est sous 6.</div>'
            '<div class="ko"><b>A, réparabilité ✘</b>5 sur 10 pour «&nbsp;6 sur 10 au moins&nbsp;».</div></div>'),
        retenir="<b>évaluer</b>, c'est comparer la valeur de la solution au niveau de <b>chaque exigence</b>&nbsp;; "
                "<b>l'égalité satisfait</b>. La flèche <b>«&nbsp;satisfy&nbsp;»</b> va de la solution vers l'exigence.",
        piege="croire que «&nbsp;4 sur 5&nbsp;» suffit à choisir&nbsp;: le décompte ne dit pas quelle exigence manque.",
    ),
    dict(
        niveau="3e", emoji="🎚️",
        titre="Comment savoir quel écart le client accepte&nbsp;?",
        titre_court="Quel écart accepte-t-il&nbsp;?",
        carte="On écoute sa réponse&nbsp;: la classe de flexibilité dit l'écart accepté, pas l'importance de l'exigence.",
        exemple=(
            "<p>Mme&nbsp;Augustin, du comité de quartier, répond à «&nbsp;et si on n'atteint pas ce niveau&nbsp;?&nbsp;»&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>F0</b>Étanchéité&nbsp;: «&nbsp;pas question de descendre&nbsp;».</div>"
            "<div><b>F1</b>Autonomie&nbsp;: «&nbsp;60 heures, si elle signale sa batterie faible&nbsp;».</div>"
            "<div><b>F2</b>Réparabilité&nbsp;: «&nbsp;5 sur 10, ça ira&nbsp;».</div>"
            "<div><b>F3</b>Coût&nbsp;: «&nbsp;même 400 euros&nbsp;».</div></div>"),
        retenir="la <b>flexibilité</b> se lit dans <b>la réponse du client</b>. Elle s'écrit avec une <b>classe</b> (F0 à "
                "F3) ou une <b>tolérance chiffrée</b>&nbsp;: «&nbsp;6 sur 10 demandé, 5 sur 10 accepté&nbsp;».",
        piege="donner F0 à ce qui paraît important&nbsp;: le coût compte, et il est pourtant en F3.",
    ),
    dict(
        niveau="3e", emoji="🏁",
        titre="Comment choisir quand aucune solution n'est parfaite&nbsp;?",
        titre_court="Comment arbitrer&nbsp;?",
        carte="On élimine la solution qui manque une exigence F0, on garde celle dont l'écart reste dans la marge, et on "
              "le dit.",
        exemple=(
            "<p>Aucun boîtier ne satisfait les cinq exigences. Le comité arbitre&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ko"><b>B éliminé ✘</b>Il manque l\'étanchéité, en F0&nbsp;: sous un cyclone, la sirène se tait.</div>'
            '<div class="ok"><b>A retenu ✔</b>Il manque la réparabilité, mais 5 sur 10 est accepté (F2).</div>'
            '<div class="ok"><b>L\'amélioration</b>Un couvercle vissé, avec un joint de rechange.</div></div>'),
        retenir="<b>arbitrer</b>, c'est éliminer la solution qui manque une exigence <b>F0</b> et garder celle dont "
                "l'écart reste <b>dans la marge</b>. On dit l'<b>écart accepté</b> et l'<b>amélioration</b> demandée.",
        piege="choisir le moins cher, ou le meilleur «&nbsp;en moyenne&nbsp;», alors qu'il manque une exigence impérative.",
    ),
]

LEXIQUE = [
    ("exigence", "requirement", "ce que le système doit faire, vérifiable."),
    ("diagramme des exigences", "requirement diagram", "les exigences en blocs reliés."),
    ("SysML", "Systems Modeling Language", "un langage de schémas d'ingénieurs."),
    ("identifiant (Id)", "identifier", "le numéro d'une exigence&nbsp;: 1, 1.1…"),
    ("contenance (⊕)", "containment", "la mère contient ses filles."),
    ("critère", "criterion", "ce qu'on mesure."),
    ("niveau", "level", "la valeur à atteindre."),
    ("vérifier («&nbsp;verify&nbsp;»)", "verify", "la flèche du test vers l'exigence."),
    ("cas de test", "test case", "le bloc d'un test."),
    ("protocole de test", "test procedure", "quoi, avec quoi, comment, quel seuil."),
    ("écart", "deviation", "le résultat moins le niveau."),
    ("flexibilité", "flexibility", "l'écart accepté&nbsp;: F0 à F3, ou en chiffres."),
    ("satisfaire («&nbsp;satisfy&nbsp;»)", "satisfy", "la flèche de la solution vers l'exigence."),
    ("indice de protection (IP)", "ingress protection", "la poussière, puis l'eau."),
    ("indice de réparabilité", "repairability index", "une note sur 10."),
    ("arbitrer", "to arbitrate", "choisir en disant ce qu'on perd."),
    ("fiabilité", "reliability", "fonctionner longtemps sans panne."),
]
