# -*- coding: utf-8 -*-
"""Synthèse élève de l'atelier « le diagramme des interacteurs extérieurs » (diagramme pieuvre) — règle d'or n°316
révisée : deux pages A4.

Rendue par syntheses.eleve() : la carte « Ce que je dois retenir », puis, par partie, le titre-question, l'exemple
de l'atelier en deux lignes (en cases quand il compare ou enchaîne), « À retenir », le piège en une ligne ; un seul
lexique à la fin. Les grands schémas restent dans les pages de l'atelier.
"""

H1 = "ce qui entoure un objet, et le diagramme pieuvre qui le montre"
PB = "On décrit l'objet de l'extérieur, pendant qu'il sert&nbsp;: ce qui l'entoure, et ce qu'il lui doit. · 5e · 4e"
QUESTION = "Comment repérer tout ce qui entoure un objet, pour savoir ce qu'il doit faire et respecter&nbsp;?"

PARTIES = [
    # ── 5e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="5e", emoji="🐙",
        titre="Qu'est-ce qu'un interacteur extérieur d'un objet&nbsp;?",
        titre_court="Qu'est-ce qu'un interacteur&nbsp;?",
        carte="Ce qui est en dehors de l'objet et en relation avec lui&nbsp;: une personne, une chose, une information, la "
              "nature.",
        exemple=(
            "<p>Le <b>diagramme des interacteurs extérieurs</b>, qu'on appelle aussi <b>diagramme pieuvre</b>, met l'objet "
            "au centre et ses interacteurs autour. Léa monte une côte sous la pluie, avec son vélo-cargo&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>Dehors et en relation ✔</b>Léa, les enfants, la route, la pluie, le téléphone.</div>'
            '<div class="ko"><b>Des pièces ✘</b>La chaîne, la pédale, le bac&nbsp;: elles sont dedans.</div>'
            '<div class="ko"><b>Une action ✘</b>«&nbsp;Aller au marché&nbsp;» est un usage, pas un interacteur.</div>'
            "</div>"),
        retenir="un <b>interacteur extérieur</b> est <b>en dehors</b> de l'objet et <b>en relation</b> avec lui. Le "
                "<b>diagramme pieuvre</b> place l'objet au centre, ses interacteurs autour.",
        piege="oublier le téléphone fixé au guidon. Il n'est pas une pièce du vélo&nbsp;: on l'enlève, et le vélo roule.",
    ),
    dict(
        niveau="5e", emoji="🗂️",
        titre="Dans quelles familles range-t-on les interacteurs&nbsp;?",
        titre_court="Quelles familles&nbsp;?",
        carte="Quatre familles&nbsp;: les usagers, les données, les autres objets, les éléments de l'environnement.",
        exemple=(
            "<p>Les interacteurs du vélo-cargo, famille par famille&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>Les usagers</b>Léa, ses enfants&nbsp;: des personnes.</div>"
            "<div><b>Les données</b>L'itinéraire&nbsp;: on le lit, on ne le touche pas.</div>"
            "<div><b>Les autres objets</b>Le téléphone, les courses&nbsp;: on les touche.</div>"
            "<div><b>L'environnement</b>La route en pente, la pluie&nbsp;: le lieu, la météo.</div></div>"),
        retenir="il y a <b>quatre familles</b>&nbsp;: usagers, données, autres objets, environnement. Une pièce, une "
                "caractéristique ou une règle n'ont <b>pas de bulle</b>.",
        piege="ranger le téléphone et l'itinéraire ensemble&nbsp;: le téléphone est un objet, ce qu'il affiche est une "
              "donnée.",
    ),
    dict(
        niveau="5e", emoji="➰",
        titre="Que disent les traits du diagramme pieuvre&nbsp;?",
        titre_court="Que disent les traits&nbsp;?",
        carte="La FP relie deux interacteurs par l'objet&nbsp;: c'est la corne de la bête à cornes. La FC relie l'objet à "
              "un seul.",
        exemple=(
            "<p>Chaque trait est une fonction, écrite avec un verbe à l'infinitif. Pour le vélo-cargo&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>FP1, fonction principale</b>De Léa aux enfants, en passant par le vélo&nbsp;: «&nbsp;permettre à "
            "Léa de transporter ses enfants&nbsp;».</div>"
            "<div><b>La bête à cornes</b>Sa corne relie «&nbsp;à qui&nbsp;?&nbsp;» (Léa) et «&nbsp;sur quoi&nbsp;?&nbsp;» "
            "(les enfants)&nbsp;: elle devient la FP1.</div>"
            "<div><b>FC1, FC2, fonctions contraintes</b>«&nbsp;Protéger les enfants&nbsp;», «&nbsp;résister à la "
            "pluie&nbsp;»&nbsp;: un seul interacteur.</div></div>"),
        retenir="la <b>FP</b> relie <b>deux</b> interacteurs par l'objet&nbsp;: c'est le <b>service rendu</b>, la corne "
                "de la bête à cornes. La <b>FC</b> relie l'objet à <b>un seul</b>&nbsp;: c'est ce qu'il doit <b>respecter</b>.",
        piege="appeler «&nbsp;fonction principale&nbsp;» un trait qui ne touche qu'un seul interacteur.",
    ),
    dict(
        niveau="5e", emoji="🛡️",
        titre="Pourquoi les concepteurs ont-ils donné cette forme à l'objet&nbsp;?",
        titre_court="Pourquoi cette forme&nbsp;?",
        carte="Chaque choix de conception sert un interacteur, dans un domaine&nbsp;: sécurité, ergonomie ou "
              "développement durable.",
        exemple=(
            "<p>Trois détails du vélo-cargo, et l'interacteur que chacun sert&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>Rebords hauts, ceintures</b>Pour que les enfants ne tombent pas&nbsp;: la sécurité.</div>"
            "<div><b>Huit vitesses</b>Pour monter la pente avec moins d'effort&nbsp;: l'ergonomie.</div>"
            "<div><b>Chaîne sous un carter</b>Contre la pluie, le vélo dure plus longtemps&nbsp;: le développement "
            "durable.</div></div>"),
        retenir="un <b>choix de conception</b> s'explique par <b>l'interacteur qu'il sert</b> et par son domaine&nbsp;: "
                "<b>sécurité</b>, <b>ergonomie</b> ou <b>développement durable</b>.",
        piege="décrire le détail («&nbsp;il y a des ceintures&nbsp;») sans dire pour qui ni contre quoi il a été "
              "choisi.",
    ),
    # ── 4e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="4e", emoji="🌱",
        titre="Comment trouver toutes les contraintes d'un objet, sans en oublier&nbsp;?",
        titre_court="Comment trouver les contraintes&nbsp;?",
        carte="Devant chaque bulle, on cherche la condition qu'elle impose&nbsp;: un interacteur oublié, c'est une "
              "contrainte que personne n'écrira.",
        exemple=(
            "<p>Dans un autre jardin, chaque plainte montre une contrainte oubliée&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ko"><b>Après l\'orage, panne</b>La pluie oubliée&nbsp;: la fiabilité.</div>'
            '<div class="ko"><b>Cuve vide, potager noyé</b>L\'eau oubliée&nbsp;: les incidences environnementales.</div>'
            '<div class="ko"><b>Un tournevis pour régler</b>La gardienne oubliée&nbsp;: l\'ergonomie.</div>'
            '<div class="ko"><b>230 volts sous la pluie</b>Ceux qui le touchent&nbsp;: la sécurité.</div></div>'),
        retenir="devant <b>chaque bulle</b>, on se demande quelle condition l'interacteur impose. Un même interacteur peut "
                "porter la FP et une FC&nbsp;; <b>un interacteur oublié</b>, c'est une contrainte que personne n'écrira.",
        piege="ranger la panne après l'orage en «&nbsp;qualité&nbsp;»&nbsp;: une panne qui arrive avec le temps, c'est la "
              "fiabilité.",
    ),
    dict(
        niveau="4e", emoji="📏",
        titre="Comment rendre une contrainte vérifiable&nbsp;?",
        titre_court="Comment la rendre vérifiable&nbsp;?",
        carte="On lui ajoute un critère (ce qu'on mesure) et un niveau (la valeur à atteindre)&nbsp;: c'est une exigence.",
        exemple=(
            "<p>Au jardin du collège, «&nbsp;prendre seulement l'eau dont les plantes ont besoin&nbsp;» entre dans le "
            "cahier des charges&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>Le critère</b>Ce qu'on mesure&nbsp;: le volume d'eau par jour.</div>"
            "<div><b>Le niveau</b>La valeur à atteindre&nbsp;: 10 litres au plus.</div>"
            "<div><b>D'où vient le niveau</b>D'une norme (IPX4 pour la pluie), d'un label ou du client.</div></div>"),
        retenir="une contrainte devient une <b>exigence</b> avec un <b>critère</b> et un <b>niveau</b>. Le niveau vient "
                "d'une <b>norme</b>, d'un <b>label</b>, d'une certification ou du client.",
        piege="écrire un niveau sans unité, ou un critère qui ne se mesure pas, comme «&nbsp;joli&nbsp;».",
    ),
    dict(
        niveau="4e", emoji="🎚️",
        titre="De combien le niveau peut-il bouger&nbsp;?",
        titre_court="De combien peut-il bouger&nbsp;?",
        carte="La flexibilité dit l'écart que le client accepte&nbsp;: de F0, impératif, à F3, très négociable.",
        exemple=(
            "<p>Ce que la gardienne accepte, niveau par niveau&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>F0, impératif</b>12 volts&nbsp;: «&nbsp;pas question d'autre chose&nbsp;».</div>"
            "<div><b>F1, peu négociable</b>IPX3 au lieu d'IPX4&nbsp;: «&nbsp;seulement sous l'abri&nbsp;».</div>"
            "<div><b>F2, négociable</b>10 litres&nbsp;: «&nbsp;9 ou 11 litres, ça ira&nbsp;».</div>"
            "<div><b>F3, très négociable</b>Régler en 2 minutes&nbsp;: «&nbsp;même 5 minutes, ça ira&nbsp;».</div></div>"),
        retenir="la <b>flexibilité</b> dit <b>l'écart que le client accepte</b> autour du niveau. Elle se note de "
                "<b>F0</b>, impératif, à <b>F3</b>, très négociable.",
        piege="choisir la classe d'après l'importance de la fonction&nbsp;: elle dépend de l'écart que le client accepte.",
    ),
]

LEXIQUE = [
    ("interacteur extérieur", "external interactor", "dehors, et en relation avec l'objet."),
    ("diagramme pieuvre", "interactor diagram", "l'objet au centre, le reste autour."),
    ("usager", "user", "une personne qui se sert de l'objet."),
    ("donnée", "data", "une information, qu'on ne touche pas."),
    ("environnement", "environment", "le lieu, la nature, la météo."),
    ("fonction principale (FP)", "main function", "le service rendu."),
    ("fonction contrainte (FC)", "constraint function", "une condition à respecter."),
    ("choix de conception", "design choice", "une décision du concepteur."),
    ("ergonomie", "ergonomics", "le confort, avec moins d'effort."),
    ("développement durable", "sustainable development", "faire durer, réparer, économiser."),
    ("fiabilité", "reliability", "fonctionner longtemps sans panne."),
    ("incidences environnementales", "environmental impact", "les effets sur la planète."),
    ("exigence", "requirement", "une contrainte qu'on peut vérifier."),
    ("critère", "criterion", "ce qu'on mesure."),
    ("niveau", "level", "la valeur à atteindre."),
    ("flexibilité", "flexibility", "l'écart accepté, de F0 à F3."),
    ("norme", "standard", "une règle commune aux fabricants."),
    ("cahier des charges", "specifications", "ce que le client demande à l'objet."),
]
