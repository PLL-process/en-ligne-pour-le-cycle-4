# -*- coding: utf-8 -*-
"""Synthèse élève de l'atelier « le diagramme de cas d'utilisation » (use case) — règle d'or n°316 révisée : deux
pages A4.

Rendue par syntheses.eleve() : la carte « Ce que je dois retenir », puis, par partie, le titre-question, l'exemple
de l'atelier en deux lignes (en cases quand il compare ou enchaîne), « À retenir », le piège en une ligne ; un seul
lexique à la fin. Les diagrammes restent dans les pages de l'atelier.
"""

H1 = "le diagramme de cas d'utilisation&nbsp;: qui fait quoi avec le système"
PB = "Qui se sert du système, et pour faire quoi&nbsp;? · 5e · 4e · 3e"
QUESTION = "Comment montrer qui se sert d'un système, et pour faire quoi&nbsp;?"

PARTIES = [
    # ── 5e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="5e", emoji="🧍",
        titre="Qui se sert du système, et pour faire quoi&nbsp;?",
        titre_court="À quoi sert ce diagramme&nbsp;?",
        carte="Il dit qui se sert du système et pour faire quoi, avec un cadre, des bonshommes, des ellipses et des traits.",
        exemple=(
            "<p>Le diagramme de cas d'utilisation, en anglais <b>use case</b> (du langage SysML), a quatre éléments. "
            "Pour le lampadaire solaire du parking&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>Le cadre</b>La frontière du système&nbsp;: le lampadaire est dedans.</div>"
            "<div><b>Le bonhomme, dehors</b>Un acteur&nbsp;: le piéton, l'agent de la mairie, le technicien.</div>"
            "<div><b>L'ellipse, dedans</b>Un cas d'utilisation&nbsp;: «&nbsp;Régler les heures d'allumage&nbsp;».</div>"
            "<div><b>Le trait</b>Une association&nbsp;: l'agent participe à cette action.</div></div>"),
        retenir="le <b>diagramme de cas d'utilisation</b> dit <b>qui se sert du système, et pour faire quoi</b>. Il "
                "regarde le système <b>du dehors</b>&nbsp;: il ne dit ni comment il marche, ni dans quel ordre on agit.",
        piege="lire les ellipses de haut en bas comme une suite d'étapes. Le diagramme dit qui fait quoi, pas l'ordre.",
    ),
    dict(
        niveau="5e", emoji="🙋",
        titre="Qui est un acteur, et qui n'en est pas un&nbsp;?",
        titre_court="Qui est un acteur&nbsp;?",
        carte="Une personne ou un autre système, en dehors du système, qui s'en sert avec un but.",
        exemple=(
            "<p>À la station de vélos du front de mer, on loue un vélo à la borne, et la banque accepte ou refuse la "
            "carte&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>L\'usager ✔</b>Une personne, dehors, qui veut louer un vélo.</div>'
            '<div class="ok"><b>Le serveur de paiement ✔</b>Un autre système, à la banque&nbsp;: il accepte la carte.</div>'
            '<div class="ko"><b>La pluie ✘</b>Elle agit sur la station, mais sans but&nbsp;: un interacteur.</div>'
            '<div class="ko"><b>L\'écran tactile ✘</b>Une pièce de la borne, dedans&nbsp;: un constituant.</div></div>'),
        retenir="un <b>acteur</b> est une <b>personne ou un autre système</b>, <b>en dehors</b> du système, qui s'en sert "
                "<b>avec un but</b>. La nature, une donnée, un objet prêté ou une pièce restent des <b>interacteurs</b> ou "
                "des <b>constituants</b>.",
        piege="dessiner la pluie en bonhomme parce qu'elle «&nbsp;agit&nbsp;» sur la station&nbsp;: elle n'a aucun but.",
    ),
    # ── 4e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="4e", emoji="💬",
        titre="Comment passer de ce que disent les usagers au schéma&nbsp;?",
        titre_court="Des phrases au schéma&nbsp;?",
        carte="Dans chaque phrase, on cherche l'action faite avec le système&nbsp;; le ressenti se garde à côté.",
        exemple=(
            "<p>Les usagers de la borne racontent, avec leurs mots. Leurs phrases recopiées sont des <b>verbatims</b>&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>Maëva ✔</b>«&nbsp;Je pose ma carte et je pars avec le vélo.&nbsp;» → Louer un vélo.</div>'
            '<div class="ok"><b>Kenza ✔</b>«&nbsp;Je ne trouve pas où poser ma carte.&nbsp;» → Louer un vélo, le même.</div>'
            '<div class="ko"><b>Inès ✘</b>«&nbsp;Le bleu de la borne est joli.&nbsp;» → un avis&nbsp;: aucun cas.</div>'
            '<div class="ko"><b>L\'agacement ✘</b>Il ne se dessine pas&nbsp;: on le garde pour une exigence.</div></div>'),
        retenir="dans chaque phrase, on cherche <b>l'action faite avec le système</b>, écrite <b>verbe à l'infinitif + "
                "complément</b>. Le <b>ressenti</b> ne se dessine pas&nbsp;: on le garde à côté.",
        piege="créer un cas par phrase. Deux usagers racontent parfois la même action, et un avis n'en est pas une.",
    ),
    dict(
        niveau="4e", emoji="🔍",
        titre="Comment écrire et vérifier un diagramme&nbsp;?",
        titre_court="Comment le vérifier&nbsp;?",
        carte="Des acteurs dehors, reliés, avec un but&nbsp;; des ellipses avec un verbe, jamais une pièce.",
        exemple=(
            "<p>Noah a dessiné le diagramme de l'arrosage du jardin. Ses erreurs, et leur correction&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ko"><b>La gardienne dans le cadre ✘</b>Un acteur reste dehors.</div>'
            '<div class="ko"><b>«&nbsp;L\'arrosage&nbsp;» ✘</b>Pas de verbe&nbsp;: «&nbsp;Arroser les plantes du '
            "potager&nbsp;».</div>"
            '<div class="ko"><b>«&nbsp;La pompe&nbsp;» ✘</b>Une pièce du système&nbsp;: on la retire.</div>'
            '<div class="ko"><b>La pluie en bonhomme ✘</b>Elle n\'a pas de but&nbsp;: on la retire.</div></div>'),
        retenir="une <b>ellipse</b> contient une <b>action</b>, avec un <b>verbe à l'infinitif</b>, jamais une pièce. Chaque "
                "<b>acteur</b> est <b>hors du cadre</b> et relié par <b>au moins un trait</b> à ce qu'il fait.",
        piege="donner un verbe à une pièce («&nbsp;Pomper l'eau&nbsp;»)&nbsp;: la pompe le fait dedans, pas la gardienne.",
    ),
    # ── 3e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="3e", emoji="🧭",
        titre="Quel mode de représentation choisir pour quelle question&nbsp;?",
        titre_court="Quel mode pour quelle question&nbsp;?",
        carte="On choisit d'après la question&nbsp;; le diagramme de cas d'utilisation répond à «&nbsp;qui fait "
              "quoi&nbsp;».",
        exemple=(
            "<p>La mairie veut améliorer la borne des vélos. À chaque question, son mode de représentation&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>Qui fait quoi&nbsp;?</b>Le diagramme de cas d'utilisation.</div>"
            "<div><b>Et si la carte est refusée&nbsp;?</b>L'algorigramme&nbsp;: l'ordre et les tests.</div>"
            "<div><b>Que vit le touriste&nbsp;?</b>Le storyboard&nbsp;: une suite d'images.</div>"
            "<div><b>Combien d'abandons par jour&nbsp;?</b>Le graphique.</div></div>"),
        retenir="on choisit le <b>mode de représentation</b> d'après <b>la question</b>. Le diagramme de cas "
                "d'utilisation ne montre <b>ni l'ordre, ni les quantités, ni le ressenti</b>. Ce qui entoure l'objet va "
                "dans le <b>diagramme des interacteurs</b>.",
        piege="prendre le diagramme de cas d'utilisation pour «&nbsp;si la carte est refusée&nbsp;»&nbsp;: il n'a aucun test.",
    ),
    dict(
        niveau="3e", emoji="🌀",
        titre="Comment construire le diagramme à partir d'un texte&nbsp;?",
        titre_court="Le construire à partir d'un texte&nbsp;?",
        carte="Qui agit avec un but devient un acteur, ce qu'il fait une ellipse&nbsp;; la nature et les pièces vont "
              "ailleurs.",
        exemple=(
            "<p>Le texte de la mairie sur la station d'alerte cyclonique, souligné, donne&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>L\'agent municipal ✔</b>→ «&nbsp;Déclencher une alerte&nbsp;».</div>'
            '<div class="ok"><b>L\'habitant ✔</b>→ «&nbsp;Recevoir une alerte&nbsp;».</div>'
            '<div class="ok"><b>Le service météo ✔</b>Un autre système → «&nbsp;Envoyer un bulletin météo&nbsp;».</div>'
            '<div class="ko"><b>Le vent, l\'anémomètre ✘</b>La nature et une pièce&nbsp;: ailleurs.</div></div>'),
        retenir="qui agit <b>avec un but</b> devient un <b>acteur</b>, ce qu'il fait un <b>cas d'utilisation</b>. Un "
                "<b>autre système</b> (le service météo, le serveur de paiement) peut être un acteur&nbsp;; le vent, non.",
        piege="dessiner le vent en bonhomme parce que la station le mesure&nbsp;: être mesuré, ce n'est pas s'en servir.",
    ),
]

LEXIQUE = [
    ("diagramme de cas d'utilisation", "use case diagram", "qui se sert du système, et pour faire quoi."),
    ("SysML", "Systems Modeling Language", "un langage commun pour dessiner les systèmes."),
    ("frontière du système", "system boundary", "le cadre&nbsp;: dedans, le système."),
    ("acteur", "actor", "qui se sert du système avec un but, dehors."),
    ("cas d'utilisation", "use case", "une action faite avec le système, dans une ellipse."),
    ("association", "association", "le trait entre un acteur et une ellipse."),
    ("interacteur extérieur", "external interactor", "ce qui entoure l'objet, avec ou sans but."),
    ("constituant", "component", "une pièce du système, dedans."),
    ("serveur de paiement", "payment server", "l'ordinateur de la banque qui accepte la carte."),
    ("verbatim", "user quote", "une phrase recopiée mot pour mot."),
    ("langage naturel", "natural language", "la langue de tous les jours."),
    ("ressenti", "user feeling", "ce que l'usager éprouve&nbsp;: gêne, plaisir…"),
    ("verbe à l'infinitif", "infinitive verb", "le verbe non conjugué&nbsp;: louer, payer."),
    ("mode de représentation", "way of representing", "une façon de montrer une information."),
    ("algorigramme", "flowchart", "l'ordre des actions et les tests, en flèches."),
    ("storyboard", "storyboard", "une suite d'images, comme une bande dessinée."),
    ("graphique", "chart", "des barres ou des courbes qui comparent des quantités."),
]
