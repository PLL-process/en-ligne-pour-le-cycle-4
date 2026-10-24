# -*- coding: utf-8 -*-
"""Les 30 questions du QCM de l'atelier « La carte mentale » (carte heuristique).

Toutes les bonnes réponses sont en position 0 ici : la répartition sur A/B/C/D
est faite ensuite par `_outils/fix_r.js`, de façon déterministe.

Répartition : 5e_C1.4 (10) · 4e_C1.2 (10) · 3e_C1.3 (10). Cinq questions illustrées.
"""
from qbanque import Banque

B = Banque()
q = B.q

IMG_PROJET = {"src": "Images/carte_mentale_projet_lampadaire.svg",
              "alt": "Carte mentale : au centre « Notre projet : le lampadaire » ; cinq branches, Photos, Mesures, Programmes, "
                     "Comptes rendus et Croquis, avec deux feuilles chacune."}
IMG_ARBO = {"src": "Images/arborescence_lampadaire.svg",
            "alt": "Arborescence A : Documents contient 5e, qui contient Lampadaire ; dans Lampadaire, les dossiers Photos, "
                   "Mesures, Programmes, Comptes rendus et Croquis ; Photos et Mesures contiennent chacun deux fichiers."}
IMG_FAUTIVE = {"src": "Images/carte_mentale_arrosage_a_corriger.svg",
               "alt": "Carte mentale à corriger : au centre « 4e B — mardi » ; branches Avantages, Inconvénients, Divers, et une "
                      "branche sans aucun mot qui porte la pompe, le capteur d'humidité et la cuve."}
IMG_ARROSAGE = {"src": "Images/carte_mentale_arrosage.svg",
                "alt": "Carte mentale de l'arrosage connecté du jardin : Avantages en haut à droite, Inconvénients en haut à "
                       "gauche, face à face ; en dessous, Ce qui change et Pour qui ?"}
IMG_STATION = {"src": "Images/carte_mentale_station_alerte.svg",
               "alt": "Carte mentale de la station d'alerte cyclonique : branches Sécurité, Coût pour la commune, Ce qu'elle "
                      "mesure, Fausses alertes et Sans téléphone."}

# ═══════════════ 5e_C1.4 — Recenser, classer, représenter, stocker, retrouver des données (10) ═══════════════
C = "5e_C1.4"

q(C, "Ce qu'est une carte mentale",
  "Une carte mentale, c'est…",
  ["un schéma qui range des idées autour d'une idée centrale",
   "un schéma qui suit le chemin de l'énergie dans un objet",
   "un schéma qui donne l'ordre des opérations d'un programme",
   "un plan à l'échelle qui donne les dimensions d'un objet"],
  "Une carte mentale part d'une <b>idée centrale</b>, écrite au milieu ; des <b>branches</b> en partent, chacune avec le nom "
  "d'une famille ; au bout, des <b>feuilles</b> en quelques mots.",
  "Au centre « Notre projet : le lampadaire » ; branches Photos, Mesures, Programmes, Comptes rendus, Croquis.",
  "Croire qu'une carte mentale explique comment un objet fonctionne.",
  ["",
   "Le chemin de l'énergie se montre avec une chaîne d'énergie ; la carte mentale range des idées, sans rien faire circuler.",
   "L'ordre des opérations se montre avec un algorigramme ; une carte mentale n'a ni début, ni fin, ni flèches.",
   "Un plan à l'échelle donne des mesures ; une carte mentale donne des idées rangées par familles."],
  "Carte mentale : une idée centrale, des branches, des feuilles.")

q(C, "Son autre nom",
  "Sous quel autre nom connaît-on aussi la carte mentale ?",
  ["la carte heuristique",
   "le diagramme pieuvre",
   "l'algorigramme",
   "la chaîne d'information"],
  "On dit <b>carte mentale</b> ou <b>carte heuristique</b> (du grec « trouver ») ; en anglais, <i>mind map</i>. Les trois "
  "noms désignent le même schéma.",
  "Un logiciel de « carte heuristique » et un logiciel de « mind map » font la même chose.",
  "Confondre la carte mentale avec un autre schéma qui a aussi un centre.",
  ["",
   "Le diagramme pieuvre a aussi un centre, mais il place un objet au milieu de ses interacteurs, avec des fonctions.",
   "L'algorigramme montre l'ordre des opérations d'un programme, avec des tests : rien à voir avec un rangement d'idées.",
   "La chaîne d'information suit le trajet d'une information dans un objet : acquérir, traiter, communiquer."],
  "Carte mentale = carte heuristique = mind map.")

q(C, "Un objet n'est pas une donnée",
  "Dans le projet lampadaire, lequel n'est pas une donnée ?",
  ["la lampe LED, posée sur la table",
   "la photo du capteur de lumière",
   "le relevé de luminosité de mardi",
   "le programme d'allumage de la LED"],
  "Une <b>donnée</b> est une information que l'on enregistre dans un fichier. La lampe LED est un <b>objet</b> : on peut "
  "enregistrer sa photo, pas la lampe elle-même.",
  "La tablette et la carte programmable sont aussi des objets ; ce qu'elles contiennent, photos et programme, ce sont des données.",
  "Mettre un objet dans une branche de données.",
  ["",
   "Une photo s'enregistre dans un fichier image : c'est bien une donnée.",
   "Des nombres mesurés s'enregistrent dans un tableau : c'est bien une donnée.",
   "Un programme est une suite d'instructions enregistrée dans un fichier : c'est bien une donnée."],
  "Une donnée s'enregistre ; un objet se touche.")

q(C, "La bonne branche",
  "Dans quelle branche de cette carte range-t-on « 900, 450 et 120 lux, jeudi soir » ?",
  ["Mesures",
   "Photos",
   "Programmes",
   "Comptes rendus"],
  "Des nombres avec leur unité, relevés par le capteur : ce sont des <b>mesures</b>.",
  "« luminosité de lundi, en lux » est déjà sur cette branche : la nouvelle feuille la rejoint.",
  "Ranger d'après un mot de la feuille (« soir ») au lieu de sa nature.",
  ["",
   "Une photo est une image ; ici, ce sont des nombres relevés par le capteur.",
   "Un programme donne des instructions (« si… alors… ») ; ces nombres ne commandent rien, ils ont été mesurés.",
   "Un compte rendu raconte la séance en phrases ; une liste de valeurs en lux n'est pas un récit."],
  "Des nombres mesurés, avec leur unité : branche Mesures.",
  img=IMG_PROJET)

q(C, "Ce que porte une branche",
  "Que porte chaque branche d'une carte mentale ?",
  ["un mot qui nomme une famille d'idées",
   "une flèche qui montre ce qui vient après",
   "une phrase complète qui explique l'idée",
   "un numéro qui dit quelle idée compte le plus"],
  "Chaque branche porte un <b>mot</b> : Photos, Mesures, Programmes… Ce mot dit quelle famille d'idées ou de données elle range.",
  "Une branche « Croquis » range tous les dessins faits à la main.",
  "Laisser une branche sans mot, reconnaissable à sa seule couleur.",
  ["",
   "Une carte mentale n'indique pas d'ordre : ses branches partent toutes du centre, sans « avant » ni « après ».",
   "Une phrase complète alourdit la carte : on garde un mot, ou deux ou trois mots-clés.",
   "Une carte mentale ne classe pas les idées par importance : elle les range par familles."],
  "Une branche = un mot = une famille.")

q(C, "De la carte au dossier",
  "Quand on range les fichiers d'un projet comme sa carte mentale, l'idée centrale devient…",
  ["le dossier du projet",
   "un fichier image",
   "le nom de l'ordinateur",
   "l'extension des fichiers"],
  "L'idée centrale devient le <b>dossier du projet</b> (Lampadaire) ; chaque branche, un dossier rangé dedans ; chaque "
  "feuille, un fichier.",
  "Documents › 5e › Lampadaire › Photos › lampadaire_nuit.jpg.",
  "Oublier le dossier du projet et mettre les dossiers des branches directement dans celui de la classe.",
  ["",
   "Un fichier image correspond à une feuille de la branche Photos, pas à l'idée centrale.",
   "Le nom de l'ordinateur ne change pas d'un projet à l'autre ; le dossier du projet, si.",
   "L'extension (.jpg, .csv) dit le format d'un fichier ; elle ne correspond à aucune partie de la carte."],
  "Idée centrale → dossier du projet ; branche → dossier ; feuille → fichier.")

q(C, "Lire une arborescence",
  "Dans cette arborescence, quel dossier contient directement le dossier Lampadaire ?",
  ["5e",
   "Documents",
   "Photos",
   "Mesures"],
  "Lampadaire est rangé <b>dans 5e</b>, qui est lui-même rangé dans Documents. On lit l'arborescence du plus grand dossier "
  "au plus petit.",
  "Pour arriver à releves_mardi.csv : Documents › 5e › Lampadaire › Mesures.",
  "Confondre « contient » et « contient quelque part plus bas ».",
  ["",
   "Documents contient 5e, qui contient Lampadaire : Documents ne le contient pas directement.",
   "Photos est rangé DANS Lampadaire : c'est l'inverse.",
   "Mesures est rangé DANS Lampadaire, à côté de Photos : il ne le contient pas."],
  "Une arborescence se lit du plus grand dossier au plus petit.",
  img=IMG_ARBO)

q(C, "Lire un chemin",
  "Dans « Documents › 5e › Lampadaire › Photos › lampadaire_nuit.jpg », qu'est-ce qui est un fichier ?",
  ["lampadaire_nuit.jpg",
   "le dossier Photos",
   "le dossier Lampadaire",
   "le dossier Documents"],
  "Un chemin se termine par le <b>fichier</b> ; tout ce qui est avant est un dossier. L'extension .jpg le confirme : c'est une image.",
  "Dans Documents › 5e › Lampadaire › Mesures › releves_mardi.csv, le fichier est releves_mardi.csv.",
  "Prendre le dernier dossier pour le fichier.",
  ["",
   "Photos est le dernier dossier du chemin : il contient le fichier, il n'en est pas un.",
   "Lampadaire est le dossier du projet, l'idée centrale de la carte.",
   "Documents est le premier dossier du chemin, celui où tout commence."],
  "Le chemin finit par le fichier.")

q(C, "Ce que dit l'extension",
  "Que dit l'extension .csv à la fin du nom releves_mardi.csv ?",
  ["le format du fichier : un tableau de valeurs",
   "le jour où les mesures ont été relevées",
   "le dossier dans lequel le fichier est rangé",
   "la taille du fichier, comptée en octets"],
  "L'<b>extension</b>, après le point, dit le <b>format</b> : .csv un tableau de valeurs, .jpg une image, .odt un texte.",
  "seance4_compte_rendu.odt : un texte ; lampadaire_pluie.jpg : une image.",
  "Ranger un fichier d'après sa seule extension : un croquis scanné est un .jpg, mais il va dans Croquis.",
  ["",
   "Le jour est dans le nom (« mardi »), avant le point ; l'extension ne le dit pas.",
   "Le dossier se lit dans le chemin, pas dans le nom du fichier.",
   "La taille d'un fichier se lit dans ses propriétés ; l'extension n'en dit rien."],
  "L'extension dit le format du fichier.")

q(C, "Ce qui ne va nulle part",
  "Une idée ne va dans aucune branche de ta carte. Que fais-tu ?",
  ["je crée une branche qui la nomme, ou je l'enlève",
   "je l'ajoute à une branche « Divers » pour le reste",
   "je la mets sur la branche la plus courte, pour équilibrer",
   "je l'écris au centre, juste à côté de l'idée centrale"],
  "Une idée qui ne trouve pas sa place est soit une <b>nouvelle famille</b> (on crée une branche avec un mot), soit <b>hors "
  "sujet</b> (on l'enlève). Une branche « Divers » ne dit rien.",
  "« le jardin créé en 2019 » sur une carte des avantages et inconvénients : hors sujet, on l'enlève.",
  "Créer une branche « Divers » fourre-tout.",
  ["",
   "« Divers » ne nomme aucune famille : on y entasse ce qu'on n'a pas classé, et la carte ne se lit plus.",
   "La longueur des branches ne compte pas : une idée va dans la branche de sa famille, ou nulle part.",
   "Le centre est réservé au sujet de la carte ; y ajouter une idée le brouille."],
  "Pas de branche « Divers ».")

# ═══════════════ 4e_C1.2 — Avantages et inconvénients des évolutions technologiques (10) ═══════════════
C = "4e_C1.2"

q(C, "Un avantage",
  "L'arrosage connecté « n'arrose que si la terre est sèche ». Sur la carte, c'est…",
  ["un avantage : moins d'eau gaspillée",
   "un inconvénient : un capteur de plus",
   "une phrase hors sujet sur la terre",
   "l'ordre dans lequel le système agit"],
  "À l'arrosoir, on arrosait parfois une terre déjà humide. Le capteur évite ce gaspillage : c'est un <b>avantage</b> de "
  "l'évolution.",
  "« Mme Joseph suit tout sur son téléphone » est aussi un avantage : elle sait sans se déplacer.",
  "Voir un inconvénient dans tout ce qui ajoute un composant.",
  ["",
   "Le capteur a un coût, mais la phrase dit ce qu'il apporte : moins d'eau perdue. C'est un avantage.",
   "La phrase parle bien de l'évolution : elle dit ce que le système fait mieux que l'arrosoir.",
   "Une carte mentale ne montre pas d'ordre ; cette phrase dit un bénéfice, pas une étape."],
  "Ce que l'évolution apporte de mieux : un avantage.")

q(C, "Un inconvénient",
  "Lequel est un inconvénient de l'arrosage connecté ?",
  ["la pompe consomme de l'électricité",
   "il arrose même pendant les vacances",
   "Mme Joseph suit l'arrosage à distance",
   "il n'arrose que si la terre est sèche"],
  "L'arrosoir ne consommait pas d'électricité ; la pompe, si. C'est une dépense nouvelle d'énergie : un <b>inconvénient</b>.",
  "« s'arrête si le réseau wifi est coupé » : le système dépend du réseau, un autre inconvénient.",
  "Oublier que toute évolution a un prix.",
  ["",
   "Arroser pendant les vacances, c'est ce que l'arrosoir ne permettait pas : un avantage.",
   "Suivre l'arrosage sans venir est un gain de temps pour la gardienne : un avantage.",
   "Ne pas arroser une terre humide économise l'eau : un avantage."],
  "Ce que l'évolution coûte ou rend fragile : un inconvénient.")

q(C, "Vrai mais hors sujet",
  "Sur la carte « avantages et inconvénients de l'arrosage connecté », quelle phrase est hors sujet ?",
  ["« les tomates aiment le soleil »",
   "« coûte cher à l'achat »",
   "« s'arrête si le wifi est coupé »",
   "« arrose même en vacances »"],
  "C'est vrai, mais c'est vrai avec l'arrosoir comme avec le système : la phrase ne dit rien de l'<b>évolution</b>. Elle est "
  "<b>hors sujet</b>.",
  "« les plantes ont besoin d'eau pour pousser » : vrai, et hors sujet pour la même raison.",
  "Garder une phrase parce qu'elle est vraie.",
  ["",
   "Le prix d'achat est un inconvénient de l'évolution : il a sa place sur la carte.",
   "La dépendance au wifi est un inconvénient de l'évolution : elle a sa place sur la carte.",
   "Arroser pendant les vacances est un avantage de l'évolution : il a sa place sur la carte."],
  "Vrai avant comme après l'évolution : hors sujet.")

q(C, "Face à face",
  "Pourquoi place-t-on les branches Avantages et Inconvénients face à face ?",
  ["pour comparer d'un coup d'œil les deux côtés",
   "parce que les avantages comptent toujours plus",
   "pour montrer dans quel ordre ils se produisent",
   "parce qu'une carte mentale n'a que deux branches"],
  "Face à face, les deux branches se lisent ensemble : on voit tout de suite ce que l'évolution apporte et ce qu'elle coûte.",
  "Sur la carte du jardin, Avantages est en haut à droite, Inconvénients en haut à gauche.",
  "Ne faire qu'une branche, celle des avantages.",
  ["",
   "La carte ne pèse pas les arguments : elle les range. Le débat, ensuite, dira ce qui compte le plus.",
   "Une carte mentale ne montre pas d'ordre : les branches n'ont ni avant ni après.",
   "Cette carte a aussi les branches Ce qui change et Pour qui ? : une carte a autant de branches que de familles."],
  "Avantages et inconvénients face à face, pour comparer.",
  img=IMG_ARROSAGE)

q(C, "Le centre de la carte",
  "Que reproche-t-on au centre de cette carte ?",
  ["il ne dit pas de quoi parle la carte",
   "il est écrit trop gros pour le reste",
   "il n'a pas de couleur qui lui est propre",
   "il devrait être placé en haut de la page"],
  "« 4e B — mardi » dit qui a fait la carte et quand. Le centre doit dire le <b>sujet</b> : « L'arrosage connecté du jardin ».",
  "Pour une carte sur le badge du collège, le centre serait « Des clés au badge ».",
  "Écrire au centre la classe, la date ou le mot « exposé ».",
  ["",
   "La taille du texte n'est pas le problème : c'est ce qu'il dit qui ne va pas.",
   "La couleur du centre importe peu ; ce qui compte, c'est que ses mots disent le sujet.",
   "L'idée centrale se place au milieu : c'est de là que partent toutes les branches."],
  "Au centre : le sujet.",
  img=IMG_FAUTIVE)

q(C, "La branche sans nom",
  "Sur cette carte, une branche n'a aucun mot, seulement une couleur. Pourquoi est-ce un défaut ?",
  ["on ne sait pas quelle famille elle range",
   "elle est plus courte que toutes les autres",
   "sa couleur est trop foncée pour être lue",
   "elle porte trois feuilles au lieu de deux"],
  "Sans mot, la branche ne dit pas sa famille ; et une personne qui distingue mal les couleurs ne peut pas la reconnaître. On "
  "écrit un mot, la couleur en plus : « Le matériel ».",
  "Une branche verte nommée « Inconvénients » se lit, même imprimée en noir et blanc.",
  "Compter sur la couleur seule pour dire la famille.",
  ["",
   "Toutes les branches ont la même longueur ici ; et la longueur ne dit rien de la famille.",
   "La couleur n'est pas en cause : c'est l'absence de mot qui empêche de lire.",
   "Une branche peut porter autant de feuilles qu'il faut : trois feuilles n'ont rien d'anormal."],
  "Un mot sur chaque branche ; la couleur en plus, jamais seule.",
  img=IMG_FAUTIVE)

q(C, "Des mots-clés",
  "Quelle feuille est écrite en mots-clés ?",
  ["« arrosage sans venir au jardin »",
   "« On n'a plus besoin de venir arroser. »",
   "« Je trouve que c'est très pratique. »",
   "« Il faut dire que ça arrose tout seul. »"],
  "Des <b>mots-clés</b> : quelques mots qui suffisent à rappeler l'idée, sans « on », sans « je », sans point final.",
  "« coûte cher à l'achat », « moins d'eau gaspillée » : des feuilles en mots-clés.",
  "Écrire des phrases entières dans les feuilles.",
  ["",
   "C'est une phrase complète, avec « on » et un point : on garde « plus besoin de venir ».",
   "C'est un avis en phrase, et « pratique » ne dit pas en quoi : la feuille doit dire l'idée elle-même.",
   "C'est une phrase qui tourne autour de l'idée : « arrose tout seul » suffit."],
  "Une feuille = quelques mots-clés.")

q(C, "Pas de flèches",
  "Une carte mentale n'a aucune flèche entre ses feuilles. Est-ce un défaut ?",
  ["non : elle range des idées, sans ordre",
   "oui : il faut toujours relier les feuilles",
   "oui : sans flèches, on ne peut pas la lire",
   "non, mais seulement si elle est en couleur"],
  "Une carte mentale <b>range</b> des idées par familles ; elle ne montre ni ce qui circule ni l'ordre des opérations. "
  "L'absence de flèches est donc normale.",
  "Pour montrer dans quel ordre le capteur et la pompe agissent, on dessine un algorigramme.",
  "Prendre l'absence de flèches ou d'ordre pour un défaut.",
  ["",
   "Les flèches servent aux schémas qui montrent un trajet ou un ordre ; la carte mentale n'en a pas besoin.",
   "On la lit du centre vers les feuilles, en suivant les branches : aucune flèche n'est nécessaire.",
   "La couleur n'a rien à voir : avec ou sans couleur, une carte mentale n'a pas de flèches."],
  "Pas de flèches, pas d'ordre : c'est normal.")

q(C, "Pour qui ?",
  "« Mme Joseph suit tout sur son téléphone. » Pour qui est-ce surtout un avantage ?",
  ["pour la gardienne, qui sait sans venir",
   "pour les plantes, qui boivent mieux",
   "pour la pompe, qui s'use moins vite",
   "pour le réseau wifi du collège"],
  "La gardienne sait ce qui se passe au jardin sans se déplacer : l'avantage est pour elle. Une branche « Pour qui ? » évite "
  "de mélanger les points de vue.",
  "Pour les élèves du club, la même évolution peut être un inconvénient : ils viennent moins voir les plantes.",
  "Écrire un avantage sans dire pour qui.",
  ["",
   "Les plantes boivent mieux grâce au capteur d'humidité, pas grâce aux messages sur le téléphone.",
   "Envoyer des messages ne ménage pas la pompe : elle tourne autant.",
   "Le réseau wifi transporte les messages ; il n'en tire aucun avantage."],
  "Un avantage se dit toujours pour quelqu'un.")

q(C, "Une évolution technologique",
  "Dans cet atelier, quelle est l'évolution technologique étudiée ?",
  ["le passage de l'arrosoir à l'arrosage connecté",
   "la croissance des plantes du potager du collège",
   "le changement des saisons au jardin partagé",
   "la création du jardin partagé il y a des années"],
  "Une <b>évolution technologique</b> est le passage d'une façon de faire à une autre, grâce à un objet ou à un programme : "
  "ici, de l'arrosoir au système connecté.",
  "Des clés de la salle de technologie au badge électronique : une autre évolution technologique.",
  "Confondre une évolution technologique avec un changement naturel.",
  ["",
   "La croissance des plantes est un phénomène naturel, pas une évolution d'un objet technique.",
   "Les saisons changent d'elles-mêmes : aucune technique n'y est pour rien.",
   "La création du jardin est un événement passé ; elle ne compare pas deux façons d'arroser."],
  "Évolution technologique : l'ancienne façon de faire, la nouvelle.")

# ═══════════════ 3e_C1.3 — Argumentaire court sur l'incidence d'un OST sur la société (10) ═══════════════
C = "3e_C1.3"

q(C, "Une incidence sur la société",
  "Laquelle est une incidence de la station d'alerte sur la société ?",
  ["les habitants ont le temps de se mettre à l'abri",
   "la station mesure la pression de l'air chaque minute",
   "le capteur de vent est fixé en haut d'un mât métallique",
   "la batterie de la station se recharge grâce au soleil"],
  "Une <b>incidence sur la société</b> est un effet sur la vie des personnes. Avoir le temps de se mettre à l'abri touche "
  "directement les habitants.",
  "Les fausses alertes qui ferment les écoles pour rien : une autre incidence, négative celle-là.",
  "Décrire le fonctionnement de l'objet au lieu de son effet sur les personnes.",
  ["",
   "Mesurer la pression, c'est ce que fait la station : son fonctionnement, pas un effet sur la vie des habitants.",
   "La fixation du capteur est un choix technique ; elle ne dit rien de la vie des habitants.",
   "La recharge au soleil décrit l'énergie de la station ; elle ne dit pas ce qui change pour les personnes."],
  "Incidence sur la société : un effet sur la vie des personnes.")

q(C, "Positive ou négative",
  "« Écoles fermées pour rien, après une fausse alerte. » Quelle incidence ?",
  ["négative : les familles sont dérangées",
   "positive : les élèves sont bien protégés",
   "aucune : c'est le fonctionnement normal",
   "positive : la sirène a bien fonctionné"],
  "Une fausse alerte dérange les familles, et à force, les habitants risquent de ne plus croire la sirène : c'est une "
  "incidence <b>négative</b>.",
  "« personnes âgées isolées » : sans téléphone, elles ne reçoivent pas le message, autre incidence négative.",
  "Voir du positif dans toute alerte, même fausse.",
  ["",
   "Il n'y avait pas de danger : fermer les écoles n'a protégé personne.",
   "Fermer les écoles touche la vie des familles : c'est bien une incidence sur la société, pas un fonctionnement.",
   "Que la sirène marche ne suffit pas : déclenchée pour rien, elle use la confiance des habitants."],
  "Fausse alerte : une incidence négative.")

q(C, "Un connecteur d'opposition",
  "Quel mot introduit une idée contraire dans un argumentaire ?",
  ["cependant",
   "de plus",
   "par exemple",
   "en conclusion"],
  "<b>Cependant</b>, comme <i>mais, pourtant, en revanche, toutefois</i>, annonce une idée opposée à la précédente : c'est un "
  "<b>connecteur d'opposition</b>.",
  "« L'alerte arrive plus tôt. Cependant, la station coûte cher à la commune. »",
  "Enchaîner les deux côtés sans mot qui les oppose.",
  ["",
   "« De plus » ajoute une idée du même côté : il n'oppose rien.",
   "« Par exemple » introduit un exemple qui illustre l'idée précédente.",
   "« En conclusion » annonce la fin du texte et l'avis final."],
  "Opposer : mais, cependant, pourtant, en revanche.")

q(C, "Le plan de l'argumentaire",
  "Dans quel ordre écrit-on un argumentaire court ?",
  ["un effet positif, un effet négatif, une conclusion",
   "la conclusion, puis toutes les idées de la carte",
   "le fonctionnement, puis le prix, puis la conclusion",
   "les feuilles de la carte, dans l'ordre des branches"],
  "Une incidence positive avec un exemple, une incidence négative introduite par un connecteur d'opposition, puis une "
  "<b>conclusion</b> qui donne un avis nuancé.",
  "« Elle prévient plus tôt… Cependant, elle coûte cher… En conclusion, c'est utile si… »",
  "Recopier toute la carte, branche après branche.",
  ["",
   "La conclusion vient à la fin : elle s'appuie sur ce qui a été dit avant.",
   "Le fonctionnement n'est pas une incidence sur la société : il n'a pas sa place au début de l'argumentaire.",
   "Un argumentaire court choisit dans la carte ; il ne la recopie pas, et la carte n'a pas d'ordre à suivre."],
  "Positif, négatif (cependant…), conclusion.")

q(C, "La branche qui ne sert pas",
  "Quelle branche de cette carte ne sert pas à l'argumentaire sur la société ?",
  ["Ce qu'elle mesure",
   "Sécurité",
   "Fausses alertes",
   "Sans téléphone"],
  "« vent, pluie, pression » décrit ce que la station mesure : c'est son <b>fonctionnement</b>, pas un effet sur la vie des "
  "habitants.",
  "Les branches Sécurité et Fausses alertes donnent chacune un côté de l'argumentaire.",
  "Garder une branche technique dans un argumentaire sur la société.",
  ["",
   "Sécurité donne l'incidence positive : l'alerte arrive plus tôt, on évacue à temps.",
   "Fausses alertes donne une incidence négative : on n'y croit plus, les écoles ferment pour rien.",
   "Sans téléphone parle des personnes âgées isolées : une question d'égalité entre habitants."],
  "Le fonctionnement n'est pas une incidence.",
  img=IMG_STATION)

q(C, "Une conclusion nuancée",
  "Laquelle est une conclusion nuancée ?",
  ["« C'est utile, à condition de limiter les fausses alertes. »",
   "« La station est parfaite et n'a aucun défaut, voilà tout. »",
   "« La station mesure le vent et la pluie à chaque minute. »",
   "« Il y a des avantages et il y a aussi des inconvénients. »"],
  "Une conclusion <b>nuancée</b> donne un avis et dit à quelle condition il tient : elle tient compte des deux côtés.",
  "« Les caméras sont utiles, si les images sont vite effacées. »",
  "Conclure sans avis, ou avec un avis qui oublie l'autre côté.",
  ["",
   "Cet avis oublie les incidences négatives que la carte montre : coût, fausses alertes.",
   "Cette phrase décrit le fonctionnement : ce n'est ni un avis ni une conclusion.",
   "C'est vrai, mais ce n'est pas un avis : le lecteur ne sait toujours pas ce que tu penses."],
  "Conclure : un avis, et sa condition.")

q(C, "Le bon outil",
  "Pour quelle tâche la carte mentale est-elle le bon outil ?",
  ["réviser tout un chapitre sur une seule page",
   "suivre le chemin de l'énergie dans la station",
   "donner l'ordre des tests faits par le programme",
   "comparer le prix de deux modèles de station"],
  "La carte mentale <b>organise et fait retenir</b> : résumer un chapitre, rassembler des idées avant un exposé ou un "
  "argumentaire.",
  "Préparer la revue de projet avec toutes les idées de l'équipe : une carte mentale.",
  "Choisir la carte mentale pour tout.",
  ["",
   "Le chemin de l'énergie se suit sur une chaîne d'énergie.",
   "L'ordre des tests se montre avec un algorigramme.",
   "Comparer des valeurs côte à côte se fait dans un tableau."],
  "Organiser, retenir : la carte mentale.")

q(C, "Ce qu'elle cache",
  "Que ne montre pas une carte mentale ?",
  ["dans quel ordre l'objet agit",
   "l'idée centrale du sujet",
   "les familles d'idées",
   "les mots-clés de chaque idée"],
  "Une carte mentale range des idées autour d'un centre ; elle ne dit ni <b>ce qui circule</b> dans l'objet, ni <b>dans quel "
  "ordre</b> il agit.",
  "La carte « L'alerte de la station » dit que la station mesure, décide et prévient, mais pas dans quel ordre.",
  "Lire une carte mentale comme une suite d'étapes.",
  ["",
   "L'idée centrale est au milieu de toute carte mentale : elle la montre toujours.",
   "Les familles d'idées, ce sont les branches : la carte les montre.",
   "Les mots-clés sont écrits dans les feuilles : la carte les montre."],
  "Une carte mentale ne montre pas d'ordre.")

q(C, "Pieuvre ou carte mentale",
  "Un schéma place la station au centre et, autour, les habitants, le vent, la pluie et le réseau. C'est…",
  ["le diagramme des interacteurs extérieurs",
   "une carte mentale pour réviser le cours",
   "une chaîne d'énergie de la station",
   "un algorigramme du programme d'alerte"],
  "L'objet au centre et tout ce qui l'entoure autour : c'est le <b>diagramme des interacteurs extérieurs</b>, souvent appelé "
  "diagramme pieuvre. Il ressemble à une carte mentale, mais il montre des interacteurs, pas des idées rangées par familles.",
  "Le vélo-cargo au centre, Léa, la pluie et la route autour : un diagramme pieuvre.",
  "Appeler « carte mentale » tout schéma qui a un centre.",
  ["",
   "Une carte mentale range des idées par familles ; ici, ce sont les éléments qui entourent l'objet.",
   "Une chaîne d'énergie suit le chemin de l'énergie, de bloc en bloc ; elle n'a pas de centre.",
   "Un algorigramme montre des étapes et des tests reliés par des flèches ; il n'a pas de centre non plus."],
  "Un centre ne suffit pas à faire une carte mentale.")

q(C, "Préparer avec la carte",
  "Pourquoi faire une carte mentale avant d'écrire l'argumentaire ?",
  ["pour voir toutes ses idées et choisir les meilleures",
   "pour ne pas avoir à écrire de vraies phrases ensuite",
   "parce que le texte doit recopier toute la carte",
   "pour montrer comment fonctionne la station d'alerte"],
  "La carte met toutes les idées sous les yeux, rangées par familles : on y <b>choisit</b> une branche positive et une "
  "branche négative avant d'écrire.",
  "Dans la carte de la station, on garde Sécurité et Fausses alertes, et on laisse Ce qu'elle mesure.",
  "Écrire sans avoir fait le tour des idées, et oublier un côté.",
  ["",
   "L'argumentaire s'écrit en phrases, avec des connecteurs : la carte le prépare, elle ne le remplace pas.",
   "Un argumentaire court choisit dans la carte ; recopier toutes les branches donnerait un texte long et sans fil.",
   "La carte mentale ne montre pas le fonctionnement : elle organise des idées."],
  "La carte prépare, le texte choisit.")

Q = B.fin(30, {"5e_C1.4": 10, "4e_C1.2": 10, "3e_C1.3": 10})
