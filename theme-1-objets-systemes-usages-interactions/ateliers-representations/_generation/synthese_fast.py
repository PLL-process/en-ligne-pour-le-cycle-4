# -*- coding: utf-8 -*-
"""Synthèse élève de l'atelier « des fonctions aux solutions techniques » (diagramme FAST) — règle d'or n°316
révisée : deux pages A4.

Rendue par syntheses.eleve() : la carte « Ce que je dois retenir », puis, par partie, le titre-question, l'exemple
de l'atelier en deux lignes (en cases quand il compare ou enchaîne), « À retenir », le piège en une ligne ; un seul
lexique à la fin. Les diagrammes FAST complets restent dans les pages de l'atelier.
"""

H1 = "des fonctions aux solutions techniques, avec le diagramme FAST"
PB = "Ce que l'objet doit faire, et ce qui, dans l'objet, le fait. · 5e · 4e · 3e"
QUESTION = "Comment passer de ce à quoi sert un objet aux pièces qui le font marcher&nbsp;?"

PARTIES = [
    # ── 5e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="5e", emoji="🧩",
        titre="Comment le diagramme FAST relie-t-il les fonctions aux solutions&nbsp;?",
        titre_court="Fonction ou solution&nbsp;?",
        carte="La fonction est un verbe, la solution une pièce&nbsp;; «&nbsp;comment&nbsp;?&nbsp;» va à droite, "
              "«&nbsp;pourquoi&nbsp;?&nbsp;» à gauche.",
        exemple=(
            "<p>Le lampadaire de la rue du collège, dans son <b>diagramme FAST</b> (<i lang=\"en\">Function Analysis "
            "System Technique</i>). Vers la droite, on demande «&nbsp;comment&nbsp;?&nbsp;»&nbsp;; vers la gauche, "
            "«&nbsp;pourquoi&nbsp;?&nbsp;».</p>"
            '<div class="chaine">'
            "<div><b>Détecter un passant</b>→ le détecteur de mouvement</div>"
            "<div><b>Produire la lumière</b>→ le bloc de LED</div>"
            "<div><b>Stocker l'énergie pour la nuit</b>→ la batterie, pas le panneau</div>"
            "<div><b>Capter l'énergie du soleil</b>→ le panneau solaire</div></div>"),
        retenir="une <b>fonction technique</b> dit ce que l'objet doit faire&nbsp;: un <b>verbe</b>. Une <b>solution "
                "technique</b> est la pièce qui le fait&nbsp;: un <b>nom</b>. Vers la gauche, chaque <b>«&nbsp;pourquoi&nbsp;?"
                "&nbsp;»</b> ramène à la <b>fonction d'usage</b>.",
        piege="prendre «&nbsp;le capteur&nbsp;» pour une fonction, à cause de «&nbsp;capter&nbsp;»&nbsp;: c'est un nom, "
              "donc une solution.",
    ),
    dict(
        niveau="5e", emoji="🚲",
        titre="Deux principes techniques pour une même fonction&nbsp;: lequel choisir&nbsp;?",
        titre_court="Deux principes&nbsp;: lequel&nbsp;?",
        carte="On compare leurs avantages et leurs inconvénients, puis on choisit celui qui convient à la situation.",
        exemple=(
            "<p>Pour «&nbsp;ralentir la roue&nbsp;» du vélo-cargo de Léa, deux cases reliées par «&nbsp;ou&nbsp;». Les deux "
            "freinent par <b>frottement</b>, pas au même endroit&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>Le frein à patins</b>Il serre la jante, au bord de la roue. Moins cher, il glisse sous la pluie.</div>"
            "<div><b>Le frein à disque</b>Il serre un disque au centre, à l'abri de l'eau. Plus cher.</div>"
            '<div class="ok"><b>Pour Léa ✔ le disque</b>La pluie, deux côtes, les enfants dans le bac.</div></div>'),
        retenir="une même fonction peut avoir plusieurs <b>principes techniques</b>&nbsp;: deux cases reliées par "
                "<b>«&nbsp;ou&nbsp;»</b>. On les <b>compare</b>, puis on choisit selon <b>la situation</b>.",
        piege="croire que deux freins qui frottent se valent&nbsp;: l'endroit du frottement change tout sous la pluie.",
    ),
    # ── 4e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="4e", emoji="🌱",
        titre="Quel constituant fait quoi, et lesquels s'occupent de l'information&nbsp;?",
        titre_court="Qui fait quoi dans l'objet&nbsp;?",
        carte="Chaque constituant réalise une fonction&nbsp;; ceux qui acquièrent, traitent et communiquent forment la "
              "chaîne d'information.",
        exemple=(
            "<p>Dans le FAST de l'arrosage connecté du jardin, chaque <b>constituant</b> est la solution d'une "
            "fonction&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ok"><b>Acquérir</b>Le capteur d\'humidité mesure la terre.</div>'
            '<div class="ok"><b>Traiter</b>La carte programmable décide quand arroser.</div>'
            '<div class="ok"><b>Communiquer</b>Le module Wi-Fi prévient le smartphone.</div>'
            '<div class="ko"><b>Pas d\'information ✘</b>L\'électrovanne, la pompe&nbsp;: elles agissent sur l\'eau.</div>'
            "</div>"),
        retenir="la <b>chaîne d'information</b> réunit les constituants qui <b>acquièrent</b>, <b>traitent</b> et "
                "<b>communiquent</b> une information. Ce qui agit sur le monde est dans la <b>chaîne d'énergie</b>.",
        piege="mettre l'électrovanne dans la chaîne d'information parce qu'elle reçoit un ordre&nbsp;: elle ne traite "
              "rien.",
    ),
    dict(
        niveau="4e", emoji="➕",
        titre="Comment ajouter une nouvelle fonction à un objet&nbsp;?",
        titre_court="Comment ajouter une fonction&nbsp;?",
        carte="On ajoute une branche au FAST&nbsp;: la fonction qui manque, sa solution, et on réutilise ce qui existe.",
        exemple=(
            "<p>Mme&nbsp;Joseph veut être prévenue quand la cuve est presque vide. Aucune branche ne mesure l'eau "
            "qui reste&nbsp;:</p>"
            '<div class="chaine etapes">'
            "<div><b>1. La fonction</b>Mesurer le niveau d'eau de la cuve.</div>"
            "<div><b>2. Sa solution</b>Le capteur de niveau d'eau.</div>"
            "<div><b>3. On réutilise</b>Le module Wi-Fi envoie l'alerte.</div>"
            "<div><b>4. Ce qui change</b>Le programme de la carte.</div></div>"),
        retenir="<b>ajouter une fonction</b>, c'est <b>ajouter une branche</b>&nbsp;: la fonction technique qui manque, "
                "puis sa solution. On <b>réutilise</b> ce qui existe, et le <b>programme</b> change souvent.",
        piege="écrire «&nbsp;un capteur de niveau&nbsp;» comme fonction. La fonction dit quoi faire, la solution avec "
              "quoi.",
    ),
    # ── 3e ─────────────────────────────────────────────────────────────────
    dict(
        niveau="3e", emoji="🔍",
        titre="Comment proposer, puis contrôler, le FAST d'un objet nouveau&nbsp;?",
        titre_court="Comment contrôler un FAST&nbsp;?",
        carte="On propose une ou plusieurs solutions par fonction, puis on vérifie trois points avant de fabriquer.",
        exemple=(
            "<p>Le FAST de la station d'alerte cyclonique, proposé par une équipe, passe le contrôle&nbsp;:</p>"
            '<div class="chaine">'
            '<div class="ko"><b>Un verbe&nbsp;? ✘</b>«&nbsp;Le programme d\'alerte&nbsp;» → «&nbsp;décider du niveau '
            "d'alerte&nbsp;».</div>"
            '<div class="ko"><b>Comment&nbsp;? ✘</b>Pour stocker l\'énergie, pas le panneau&nbsp;: la batterie.</div>'
            '<div class="ko"><b>Pourquoi&nbsp;? ✘</b>«&nbsp;Éclairer la rue&nbsp;» vient d\'un autre objet&nbsp;: on '
            "l'enlève.</div>"
            '<div class="ok"><b>Trois solutions avec «&nbsp;ou&nbsp;» ✔</b>Permis&nbsp;: on choisira ensuite.</div></div>'),
        retenir="avant de fabriquer, on <b>contrôle</b> le FAST&nbsp;: un <b>verbe</b> dans chaque fonction, une solution "
                "qui répond au <b>«&nbsp;comment&nbsp;?&nbsp;»</b>, un <b>«&nbsp;pourquoi&nbsp;?&nbsp;»</b> qui ramène à la "
                "fonction d'usage.",
        piege="prendre pour une erreur plusieurs solutions reliées par «&nbsp;ou&nbsp;»&nbsp;: c'est une alternative, "
              "permise.",
    ),
    dict(
        niveau="3e", emoji="⚖️",
        titre="Comment choisir entre plusieurs solutions, et défendre son choix&nbsp;?",
        titre_court="Comment arbitrer&nbsp;?",
        carte="Un critère impératif élimine, les autres départagent&nbsp;; on argumente, sans cacher la limite.",
        exemple=(
            "<p>Pour diffuser l'alerte, toutes marchent en <b>très basse tension</b>, une exigence impérative. Les autres "
            "critères départagent&nbsp;:</p>"
            '<div class="chaine">'
            "<div><b>La sirène</b>Réveille la nuit, marche sans réseau. N'atteint pas une personne sourde.</div>"
            "<div><b>Le message</b>Atteint une personne sourde. Ne passe plus si le réseau tombe.</div>"
            "<div><b>Le panneau lumineux</b>Atteint une personne sourde. Ne réveille personne.</div>"
            '<div class="ok"><b>Sirène + panneau ✔</b>Ils couvrent tout. Limite&nbsp;: la sirène vide la batterie.</div>'
            "</div>"),
        retenir="pour <b>arbitrer</b>, un critère <b>impératif élimine</b>, les autres <b>départagent</b>. Un "
                "<b>argumentaire</b> dit le choix, parfois une <b>combinaison</b>, ses critères et <b>la limite</b> qui "
                "reste.",
        piege="effacer le critère que toutes remplissent&nbsp;: il reste là pour écarter une solution dangereuse.",
    ),
]

LEXIQUE = [
    ("diagramme FAST", "FAST diagram", "relie le but aux pièces."),
    ("fonction d'usage", "use function", "ce à quoi sert l'objet."),
    ("fonction technique", "technical function", "ce que l'objet doit faire."),
    ("solution technique", "technical solution", "la pièce qui le fait."),
    ("LED", "LED", "diode électroluminescente&nbsp;: une petite lampe."),
    ("principe technique", "technical principle", "le phénomène utilisé, et où."),
    ("frottement", "friction", "deux surfaces qui se freinent."),
    ("frein à disque", "disc brake", "il serre un disque au centre."),
    ("alternative", "alternative", "deux cases reliées par «&nbsp;ou&nbsp;»."),
    ("constituant", "component", "une pièce de l'objet."),
    ("capteur", "sensor", "il prend une information sur le monde."),
    ("carte programmable", "programmable board", "elle suit un programme."),
    ("chaîne d'information", "information chain", "acquérir, traiter, communiquer."),
    ("chaîne d'énergie", "energy chain", "ce qui agit&nbsp;: moteur, vanne."),
    ("électrovanne", "solenoid valve", "un robinet électrique."),
    ("branche", "branch", "une fonction et sa solution."),
    ("critère", "criterion", "ce que l'on regarde pour comparer."),
    ("exigence impérative", "mandatory requirement", "si elle manque, on écarte."),
    ("très basse tension", "extra-low voltage", "sans danger au toucher."),
]
