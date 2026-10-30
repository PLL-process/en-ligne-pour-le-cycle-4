# -*- coding: utf-8 -*-
"""Synthèse élève de l'atelier « le besoin » (bête à cornes) — règle d'or n°316 révisée : deux pages A4.

Rendue par syntheses.eleve() : la carte « Ce que je dois retenir », puis, par partie, le titre-question, l'exemple
de l'atelier en deux lignes (en cases quand il compare ou enchaîne), « À retenir », le piège en une ligne ; un seul
lexique à la fin. Les grands schémas restent dans les pages de l'atelier.
"""

H1 = "le besoin, et la bête à cornes qui le montre"
PB = "Avant de choisir un objet, on dit à qui il sert, sur quoi il agit et pourquoi. · 5e · 4e · 3e"
QUESTION = "Comment dire ce dont quelqu'un a besoin, avant de choisir l'objet qui y répond&nbsp;?"

PARTIES = [
    # ── 5e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="5e", emoji="🐂",
        titre="Comment dire le besoin auquel répond un objet&nbsp;?",
        titre_court="Comment dire le besoin&nbsp;?",
        carte="Avec trois questions&nbsp;: à qui l'objet rend-il service, sur quoi agit-il, dans quel but.",
        exemple=(
            "<p>Le vélo-cargo de Léa, dans le schéma que l'on appelle souvent la <b>bête à cornes</b> (le programme dit "
            "«&nbsp;exprimer le besoin&nbsp;»)&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>À qui rend-il service&nbsp;?</b>Léa&nbsp;: c'est elle qui s'en sert.</div>"
            "<div><b>Sur quoi agit-il&nbsp;?</b>Ses deux enfants et ses courses&nbsp;: il les change de place.</div>"
            "<div><b>Dans quel but&nbsp;?</b>Transporter ses enfants et ses courses en ville.</div></div>"),
        retenir="le besoin se dit avec <b>trois questions</b>&nbsp;: <b>à qui</b> l'objet rend-il service, <b>sur "
                "quoi</b> agit-il, <b>dans quel but</b>. La <b>bête à cornes</b> les rassemble et se lit comme une phrase.",
        piege="mettre les enfants dans «&nbsp;à qui&nbsp;?&nbsp;». Ils sont dans le bac, mais c'est Léa que le vélo-cargo "
              "aide&nbsp;: les enfants sont ce sur quoi il agit.",
    ),
    dict(
        niveau="5e", emoji="✍️",
        titre="Comment écrire le but sans donner tout de suite la réponse&nbsp;?",
        titre_court="Comment écrire le but&nbsp;?",
        carte="Avec un verbe à l'infinitif, sans aucune solution&nbsp;: le but dit pourquoi, pas comment.",
        exemple=(
            "<p>La nuit, un lampadaire intelligent s'allume quand un piéton passe sur le parking. Sa bête à cornes&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>Le but ✔</b>«&nbsp;Éclairer la rue du parking la nuit.&nbsp;» Il dit pourquoi.</div>'
            '<div class="ko"><b>Une solution ✘</b>«&nbsp;Allumer une ampoule grâce à un capteur.&nbsp;» Elle dit comment.</div>'
            '<div class="ko"><b>À qui&nbsp;? la mairie ✘</b>Elle paie, mais ce sont les piétons qui marchent là la nuit.</div>'
            "</div>"),
        retenir="le <b>but</b> s'écrit avec un <b>verbe à l'infinitif</b> et ne nomme <b>aucune solution</b>. Il devient "
                "la <b>fonction d'usage</b> de l'objet&nbsp;: ce à quoi il sert.",
        piege="croire que celui qui paie est celui à qui l'objet rend service. La mairie paie le lampadaire&nbsp;; il "
              "rend service aux piétons.",
    ),
    dict(
        niveau="5e", emoji="✅",
        titre="Comment choisir l'objet qui répond au besoin&nbsp;?",
        titre_court="Comment choisir l'objet&nbsp;?",
        carte="Il doit remplir les trois branches à la fois&nbsp;; une seule branche qui échoue suffit à l'écarter.",
        exemple=(
            "<p>Le besoin de Léa&nbsp;: transporter ses enfants et ses courses en ville, <b>sans voiture</b>. Branche par "
            "branche&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>Le vélo-cargo ✔</b>Les trois branches sont remplies.</div>'
            '<div class="ko"><b>La draisienne ✘</b>À qui&nbsp;? À un jeune enfant, pas à Léa.</div>'
            '<div class="ko"><b>La trottinette ✘</b>Sur quoi&nbsp;? Elle ne porte que Léa.</div>'
            '<div class="ko"><b>La voiture ✘</b>Dans quel but&nbsp;? Léa veut s\'en passer.</div></div>'),
        retenir="un objet <b>répond au besoin</b> s'il remplit <b>les trois branches à la fois</b>. <b>Une seule "
                "branche</b> qui échoue suffit à l'<b>écarter</b>.",
        piege="garder la voiture parce qu'elle fait «&nbsp;presque tout&nbsp;». Elle transporte tout, mais le but dit "
              "«&nbsp;sans voiture&nbsp;».",
    ),
    # ── 4e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="4e", emoji="🔄",
        titre="Pourquoi un objet change-t-il au fil du temps&nbsp;?",
        titre_court="Pourquoi un objet change-t-il&nbsp;?",
        carte="Parce que le besoin change&nbsp;; on le montre en comparant les bêtes à cornes d'avant et d'après.",
        exemple=(
            "<p>Au jardin du collège, à Brooklyn, personne ne vient en vacances et l'eau manque pendant la canicule&nbsp;: "
            "l'arrosoir devient un système connecté.</p>"
            '<div class="chaine">'
            "<div><b>Pareil</b>À qui&nbsp;? La gardienne. Sur quoi&nbsp;? Les plantes du jardin.</div>"
            "<div><b>Avant&nbsp;: le but</b>«&nbsp;Arroser les plantes du jardin.&nbsp;»</div>"
            '<div class="ok"><b>Après&nbsp;: le but change</b>«&nbsp;… même en l\'absence de la gardienne, sans '
            "gaspiller l'eau.&nbsp;»</div></div>"),
        retenir="un objet <b>évolue</b> parce que <b>le besoin évolue</b>&nbsp;: façon de vivre, <b>innovation</b>, "
                "<b>développement durable</b>. On le <b>justifie</b> en comparant les bêtes à cornes d'avant et d'après.",
        piege="justifier l'évolution par la mode ou par une panne. Un arrosoir cassé se remplace par un arrosoir.",
    ),
    dict(
        niveau="4e", emoji="⚖️",
        titre="Que faut-il comparer pour choisir entre plusieurs modèles&nbsp;?",
        titre_court="Que comparer pour choisir&nbsp;?",
        carte="Chaque partie du besoin indique une caractéristique à comparer&nbsp;; le reste est écarté.",
        exemple=(
            "<p>Pour choisir le système d'arrosage, chaque partie du besoin dit quoi regarder&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>«&nbsp;En l'absence de la gardienne&nbsp;»</b>L'autonomie, en jours.</div>"
            "<div><b>«&nbsp;Sans gaspiller l'eau&nbsp;»</b>La consommation, en litres par jour.</div>"
            "<div><b>«&nbsp;À qui&nbsp;? la gardienne&nbsp;»</b>La facilité de réglage, en minutes.</div>"
            '<div class="ko"><b>La couleur, la marque ✘</b>Elles ne servent pas le besoin.</div></div>'),
        retenir="pour choisir, <b>chaque partie du besoin</b> indique <b>une caractéristique à comparer</b>. Le programme "
                "ajoute la <b>qualité</b>, l'<b>efficacité énergétique</b>, la <b>durabilité</b> et la "
                "<b>recyclabilité</b>.",
        piege="choisir sur ce qui se voit. Avec une autre couleur, le jardin est arrosé de la même façon.",
    ),
    # ── 3e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="3e", emoji="📋",
        titre="Comment chercher tous les objets qui pourraient répondre au besoin&nbsp;?",
        titre_court="Comment établir la liste&nbsp;?",
        carte="On part d'un but sans solution et on cherche famille par famille, sans juger trop tôt.",
        exemple=(
            "<p>But&nbsp;: «&nbsp;prévenir les habitants de l'arrivée d'un cyclone&nbsp;». Les <b>OST</b> (objets ou "
            "systèmes techniques) possibles&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>Le son</b>Une sirène, un haut-parleur sur une voiture.</div>'
            '<div class="ok"><b>La lumière</b>Un gyrophare, un panneau lumineux.</div>'
            '<div class="ok"><b>Le téléphone</b>Un SMS, une application d\'alerte.</div>'
            '<div class="ko"><b>Pas des OST ✘</b>Les pompiers, «&nbsp;évacuer&nbsp;», le vent.</div></div>'),
        retenir="pour <b>établir une liste d'OST possibles</b>, on part d'un <b>but sans solution</b> et on cherche "
                "<b>famille par famille</b>. Ensuite seulement, on <b>choisit</b> avec des critères.",
        piege="mettre dans la liste une personne (les pompiers) ou une action (évacuer)&nbsp;: ce ne sont pas des OST.",
    ),
    dict(
        niveau="3e", emoji="🔒",
        titre="Que se passe-t-il quand le but nomme déjà une solution&nbsp;?",
        titre_court="Et si le but nomme une solution&nbsp;?",
        carte="Il ferme la liste avant qu'on la fasse&nbsp;: la solution a sa place dans la liste, pas dans le but.",
        exemple=(
            "<p>Une autre équipe a écrit la bête à cornes de l'alerte. Sa liste ne contient qu'une ligne&nbsp;: "
            "«&nbsp;un SMS&nbsp;».</p>"
            '<div class="chaine">'
            '<div class="ko"><b>But&nbsp;: «&nbsp;envoyer un SMS&nbsp;» ✘</b>C\'est une solution&nbsp;: les habitants sans '
            "réseau sont oubliés.</div>"
            '<div class="ko"><b>Sur quoi&nbsp;? «&nbsp;la sécurité&nbsp;» ✘</b>Une idée&nbsp;: l\'objet agit sur les '
            "habitants.</div>"
            '<div class="ok"><b>But corrigé ✔</b>«&nbsp;Prévenir les habitants de l\'arrivée d\'un cyclone.&nbsp;»</div>'
            "</div>"),
        retenir="un but qui <b>nomme une solution</b> <b>ferme la liste</b>. La solution n'est pas mauvaise&nbsp;: <b>sa "
                "place est dans la liste</b>. La case «&nbsp;sur quoi&nbsp;?&nbsp;» nomme <b>une personne ou une "
                "chose</b>, pas une idée.",
        piege="croire que le SMS est un mauvais choix. Il est peut-être bon&nbsp;: il se met dans la liste, à côté des "
              "autres.",
    ),
]

LEXIQUE = [
    ("besoin", "need", "ce qui manque à quelqu'un."),
    ("bête à cornes", "need diagram", "le schéma du besoin, en trois questions."),
    ("usager", "user", "la personne qui se sert de l'objet."),
    ("rendre service", "to help", "aider quelqu'un, lui être utile."),
    ("agir sur", "to act on", "déplacer, toucher ou transformer."),
    ("but", "purpose", "ce pour quoi l'objet existe."),
    ("solution technique", "technical solution", "comment l'objet fait son travail."),
    ("fonction d'usage", "use function", "ce à quoi sert l'objet&nbsp;: le but."),
    ("évolution", "evolution", "un objet nouveau pour un besoin nouveau."),
    ("innovation", "innovation", "une invention entrée dans la vie courante."),
    ("développement durable", "sustainable development", "ne pas gâcher ce qu'il faudra demain."),
    ("canicule", "heat wave", "une longue période de très forte chaleur."),
    ("caractéristique", "characteristic", "ce qui décrit un modèle et se compare."),
    ("autonomie", "running time", "le temps où un système marche seul."),
    ("consommation", "consumption", "ce que le système utilise."),
    ("OST", "technical object or system", "un objet ou système technique."),
    ("établir une liste", "to draw up a list", "chercher toutes les possibilités."),
]
