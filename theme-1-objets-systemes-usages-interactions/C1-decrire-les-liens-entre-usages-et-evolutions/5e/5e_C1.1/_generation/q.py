# -*- coding: utf-8 -*-
"""Les 30 questions du QCM 5e_C1.1 à C1.6 — Chengdu, le collège qui mesure son air.

Écrites à la main. Toutes les bonnes réponses sont en position 0 ici : la
répartition sur A/B/C/D est faite ensuite par `_outils/fix_r.js`, de façon
déterministe, à partir d'une graine.

Six codes, six blocs — C1.1 (6) · C1.2 (5) · C1.3 (5) · C1.4 (5) · C1.5 (5) ·
C1.6 (4). C'est cette répartition que le filtre par compétence du gabarit rend
utilisable, et c'est elle que la séquence appelle par `#codes=` (règle n°45).

Règle tenue pour chaque distracteur : la réfutation EXPLIQUE pourquoi la
réponse est fausse — elle ne se contente pas de dire qu'elle l'est.
"""

IMG_PRINCIPES = {
    "src": "Images/trois_principes_de_mesure.svg",
    "alt": "Trois principes pour une même fonction — diffusion optique, gravimétrie, "
           "atténuation bêta — avec pour chacun son temps de réponse, son incertitude, "
           "son prix, sa consommation et ce qu'il exige d'entretien.",
}
IMG_ARBO = {
    "src": "Images/corrige_arborescence.svg",
    "alt": "À gauche quatorze entrées mal nommées, à droite la même chose rangée en un "
           "dossier racine et quatre sous-dossiers, avec les quatre règles de nommage.",
}
IMG_SI = {
    "src": "Images/corrige_systeme_information.svg",
    "alt": "Le système d'information en quatre étages — source, stockage, traitement, "
           "diffusion — avec pour chacun qui a le droit de faire quoi.",
}
IMG_DESIGNE = {
    "src": "Images/la_donnee_qui_designe.svg",
    "alt": "Le même fait vrai publié de trois façons : avec le nom de l'agent, sans dire "
           "la cause, ou en nommant l'horaire du nettoyage et non la personne.",
}

Q = []


def q(c, n, question, options, expl, ex, err, refs, ret, img=None):
    assert len(options) == 4 and len(refs) == 4, n
    assert refs[0] == "", n
    for r in refs[1:]:
        assert len(r) > 20, (n, r)
    o = {"c": c, "n": n, "q": question, "o": options, "r": 0,
         "expl": expl, "ex": ex, "err": err, "d": refs, "ret": ret}
    if img:
        o["img"] = img
    Q.append(o)


# ═══════════ C1.1 — Collecter, trier et analyser des données (6) ═══════════

q("C1.1", "Une donnée n'est pas une information",
  "Le capteur écrit « 26,4 » dans le fichier. Ce nombre est…",
  ["une donnée : brute, elle ne dit rien tant qu'on ne l'a pas mise en rapport avec autre chose",
   "une information : elle renseigne sur la qualité de l'air",
   "une connaissance : elle s'ajoute à ce que la classe sait déjà",
   "une mesure fausse tant qu'on ne l'a pas vérifiée"],
  "Une donnée est un fait brut enregistré. Elle devient une information quand on la "
  "compare, qu'on la situe, qu'on la relie : « 26,4 aujourd'hui, contre 67 les mardis » "
  "informe ; « 26,4 » tout seul n'informe personne.",
  "Le même nombre, 26,4, ne dit rien d'utile s'il s'agit d'une température en degrés, "
  "d'un prix en euros ou d'une concentration de poussières.",
  "L'erreur classique est de croire qu'une donnée « parle d'elle-même ». Elle ne parle "
  "que quand quelqu'un la met en rapport avec une autre.",
  ["",
   "Le nombre ne renseigne sur rien tant qu'on ne sait ni son unité, ni à quoi le comparer : "
   "c'est précisément ce travail de mise en rapport qui manque encore.",
   "Une connaissance est ce qui reste quand on a compris ; ici, personne n'a encore rien "
   "compris — on n'a qu'un nombre écrit dans un fichier.",
   "Rien ne permet de la dire fausse : le doute sur une valeur est une question différente "
   "de celle de savoir si un nombre brut est déjà une information."],
  "Donnée brute → information (mise en rapport) → connaissance (ce qui reste)."),

q("C1.1", "La valeur impossible",
  "Dans les relevés, mercredi 11 h porte la valeur −4,2 µg/m³. Que faut-il en conclure ?",
  ["c'est une valeur impossible : une concentration ne peut pas être négative, il y a un défaut de mesure",
   "l'air était exceptionnellement pur ce jour-là",
   "il faut la remplacer par 0, qui est la plus proche valeur possible",
   "il faut la garder telle quelle : on ne modifie jamais des mesures"],
  "Une masse de poussières par mètre cube est une quantité de matière : elle vaut zéro "
  "au minimum. Une valeur négative ne décrit aucun état du monde — elle décrit une panne, "
  "une dérive de l'électronique ou une erreur d'enregistrement.",
  "Un pèse-personne qui afficherait −3 kg ne dirait pas que vous êtes très léger : il "
  "dirait qu'il est déréglé.",
  "L'erreur classique est de discuter la valeur (« est-elle plausible ? ») au lieu de "
  "reconnaître qu'elle est hors du domaine possible de la grandeur mesurée.",
  ["",
   "Un air très pur donnerait une valeur faible mais positive, proche de zéro : la pureté "
   "n'a pas de sens en dessous de zéro, puisqu'il n'y a pas moins que pas de poussière.",
   "Remplacer par 0 revient à inventer une mesure : on écrirait dans le fichier un chiffre "
   "que le capteur n'a jamais produit, et plus rien ne signalerait le défaut.",
   "Ne rien toucher est juste pour le fichier d'origine, mais la valeur doit être écartée "
   "du CALCUL et signalée : garder n'est pas la même chose que compter."],
  "Une valeur hors du domaine physique possible n'est pas une mesure : c'est un signal de panne."),

q("C1.1", "Le capteur bloqué",
  "Vendredi, de 9 h à 14 h, le fichier porte six fois exactement 23,7. C'est le signe…",
  ["d'un capteur bloqué : une vraie mesure varie toujours un peu d'une heure à l'autre",
   "d'un air parfaitement stable pendant cinq heures",
   "d'une erreur de recopie faite par un élève",
   "de rien du tout : une valeur peut se répéter"],
  "Une grandeur physique mesurée fluctue toujours, ne serait-ce que du bruit de mesure. "
  "Une suite de valeurs rigoureusement identiques, à la décimale près, est presque "
  "toujours le signe que l'appareil a cessé d'échantillonner et répète sa dernière valeur.",
  "Une montre qui affiche 14 h 03 pendant une heure n'indique pas que le temps s'est "
  "arrêté : elle indique qu'elle est arrêtée.",
  "L'erreur classique est de chercher l'anomalie dans les valeurs extrêmes seulement. "
  "Ici, la valeur est parfaitement plausible : c'est sa RÉPÉTITION qui est impossible.",
  ["",
   "Un air stable donnerait des valeurs proches, 23,5 puis 23,9 puis 24,1 — jamais six "
   "fois la même décimale : c'est cette identité parfaite qui est invraisemblable.",
   "Les valeurs sont écrites automatiquement par le capteur, sans intervention humaine : "
   "il n'y a pas eu de recopie à laquelle attribuer l'erreur.",
   "Une valeur peut en effet se répéter deux fois par hasard ; six fois de suite à la "
   "décimale près, la probabilité devient si faible qu'on cherche une cause matérielle."],
  "Une mesure qui ne bouge plus du tout ne mesure plus : elle se répète."),

q("C1.1", "La donnée manquante",
  "Lundi 14 h, aucune ligne n'a été enregistrée. La bonne conduite est…",
  ["de le signaler et de calculer sans elle : on n'invente jamais une mesure absente",
   "de recopier la valeur de 13 h, la plus proche",
   "d'écrire 0 pour que la colonne soit complète",
   "d'écarter toute la journée du lundi"],
  "Une donnée manquante est une information en soi : elle dit que quelque chose s'est "
  "passé. On la signale, on calcule sur les valeurs réellement obtenues, et on indique "
  "combien il en manquait. Le tableur sait faire : MOYENNE ignore les cellules vides.",
  "Dans un relevé de notes, un élève absent n'a pas 0 : il n'a pas de note. Les deux ne "
  "produisent pas la même moyenne, et ne disent pas la même chose.",
  "L'erreur classique est de vouloir « boucher le trou » pour faire propre. Une case "
  "remplie par une valeur inventée est pire qu'une case vide : elle ne se voit plus.",
  ["",
   "Recopier 13 h revient à affirmer que rien n'a changé en une heure — c'est une "
   "invention, et elle sera comptée comme une vraie mesure dans la moyenne.",
   "Écrire 0 fait entrer dans le calcul une valeur très basse qui n'a jamais été mesurée : "
   "la moyenne s'en trouve tirée vers le bas, faussement.",
   "Écarter les douze autres heures du lundi, toutes valides, ferait perdre bien plus "
   "d'information que le trou lui-même : on jette du vrai pour un manque."],
  "Une case vide se signale et se compte comme manquante. Elle ne se remplit pas."),

q("C1.1", "Ce que coûte une donnée sale",
  "Moyenne calculée sur les 90 relevés : 27,4 µg/m³. Moyenne après écart des quatre "
  "anomalies : 25,2. Que montre cet écart de 2,2 ?",
  ["que quelques valeurs fausses suffisent à déplacer un résultat, et donc qu'il faut nettoyer avant de calculer",
   "que la différence est faible, donc qu'on pouvait se dispenser du nettoyage",
   "que la moyenne est un mauvais indicateur",
   "que le capteur doit être remplacé"],
  "Quatre valeurs sur quatre-vingt-dix — moins de 5 % des lignes — déplacent la moyenne "
  "de près de 9 %. C'est l'effet d'une valeur aberrante : 251 au lieu de 25,1 pèse à elle "
  "seule autant que dix relevés normaux.",
  "Une seule note de 200 sur 20 saisie par erreur suffit à faire croire qu'une classe "
  "entière a réussi.",
  "L'erreur classique est de juger l'écart « petit » en valeur absolue. C'est sa cause "
  "qui compte : il ne vient pas des mesures, il vient des erreurs.",
  ["",
   "2,2 µg/m³ sur 25 représente près de 9 % : c'est loin d'être négligeable, et surtout "
   "cet écart n'est dû à aucun phénomène réel, seulement à des défauts.",
   "La moyenne n'est pas en cause : elle a fait exactement ce qu'on lui demandait, sur "
   "des données qu'on ne lui avait pas nettoyées.",
   "Un capteur qui a produit 86 mesures correctes sur 90 fonctionne ; ce sont les quatre "
   "restantes qu'il faut traiter, pas l'appareil qu'il faut jeter."],
  "On nettoie AVANT de calculer. Sinon on calcule juste sur des données fausses."),

q("C1.1", "Écarter n'est pas effacer",
  "Une fois les quatre anomalies repérées, que fait-on du fichier d'origine ?",
  ["on les écarte du calcul mais on les garde dans le fichier, avec une note qui dit pourquoi",
   "on les efface définitivement pour ne plus les voir",
   "on les corrige en devinant la valeur qu'elles auraient dû avoir",
   "on garde le fichier tel quel et on ne calcule rien"],
  "Le fichier d'origine est une trace : il dit ce que le capteur a réellement produit. "
  "On travaille sur une copie, on y écarte les valeurs défectueuses, et on note l'écart "
  "et sa raison. N'importe qui peut alors refaire le chemin et vérifier.",
  "Un relevé de notes raturé sans explication devient invérifiable ; annoté « copie non "
  "rendue, absence justifiée », il reste vérifiable des années après.",
  "L'erreur classique est de confondre « données propres » et « données jolies ». Des "
  "données propres sont des données dont on peut expliquer chaque écart.",
  ["",
   "Effacer supprime la preuve que le capteur a mal fonctionné : personne ne pourra plus "
   "vérifier le nettoyage, ni s'apercevoir que la panne se répète.",
   "Deviner produit un chiffre que personne n'a mesuré, et qui sera ensuite traité comme "
   "s'il l'avait été : c'est le contraire du travail sur données.",
   "Ne rien calculer laisse la question du départ sans réponse, alors que 86 relevés sur "
   "90 sont parfaitement exploitables."],
  "On écarte du calcul, on garde dans le fichier, et on écrit pourquoi."),

# ═══════════ C1.2 — Comparer des principes techniques (5) ═══════════

q("C1.2", "Fonction ou principe",
  "« Mesurer la concentration de poussières dans l'air. » Cet énoncé est…",
  ["une fonction technique : il dit ce qu'il faut obtenir, sans dire par quel moyen",
   "un principe technique : il décrit le phénomène physique employé",
   "une solution technique : il désigne un appareil précis",
   "un critère de choix : il permet de départager deux appareils"],
  "Une fonction technique s'énonce par un verbe à l'infinitif et un complément, et elle "
  "n'impose aucun moyen. C'est justement ce qui permet à plusieurs principes différents "
  "de la remplir tous les trois.",
  "« Fermer une ouverture » est une fonction ; le verrou, l'aimant et le loquet sont trois "
  "solutions qui la remplissent.",
  "L'erreur classique est de croire qu'une fonction bien écrite désigne un appareil. Si "
  "elle en désigne un, c'est qu'elle est mal écrite : elle a déjà choisi.",
  ["",
   "Aucun phénomène physique n'est nommé dans cet énoncé : ni lumière, ni pesée, ni "
   "rayonnement — c'est précisément ce qui le distingue d'un principe.",
   "Aucun appareil n'est désigné : ni marque, ni modèle, ni technologie ; l'énoncé "
   "resterait vrai avec n'importe lequel des trois principes du dossier.",
   "Un critère sert à comparer (le prix, le délai, la précision) ; ici rien n'est comparé, "
   "on énonce seulement ce qu'il faut obtenir."],
  "Fonction = ce qu'il faut faire. Principe = par quel phénomène. Solution = avec quoi.",
  IMG_PRINCIPES),

q("C1.2", "Trois principes, une seule fonction",
  "Diffusion optique, gravimétrie, atténuation bêta : trois appareils différents pour la "
  "même fonction. Qu'est-ce que cela montre ?",
  ["qu'une fonction n'impose pas sa solution : il y a toujours plusieurs chemins pour y parvenir",
   "que deux des trois principes sont inutiles",
   "que les concepteurs ne se sont pas concertés",
   "que la fonction a été mal définie au départ"],
  "C'est la leçon centrale de la comparaison des principes : entre le besoin et l'objet, "
  "il y a un espace de choix. Comparer les principes, c'est explorer cet espace avant de "
  "s'y engager.",
  "Pour la fonction « éclairer une pièce », l'incandescence, la fluorescence et la diode "
  "électroluminescente sont trois principes tous valides, aux qualités différentes.",
  "L'erreur classique est de chercher « le bon » principe dans l'absolu. Aucun ne l'est : "
  "chacun l'est pour un usage, un budget et une contrainte donnés.",
  ["",
   "Chacun des trois est employé dans le monde réel pour des besoins différents : la "
   "gravimétrie sert de référence réglementaire, l'optique équipe les stations mobiles.",
   "Ils ne visent pas le même usage : ce sont des réponses différentes à des contraintes "
   "différentes, pas des tentatives concurrentes de la même réponse.",
   "C'est le contraire : une fonction bien définie n'impose justement pas de solution, "
   "et laisse donc apparaître plusieurs principes possibles."],
  "Une même fonction, plusieurs principes. C'est cet écart qui rend un choix nécessaire.",
  IMG_PRINCIPES),

q("C1.2", "Le délai comme critère",
  "La gravimétrie donne un seul résultat par 24 h. Pour un collège qui veut décider chaque "
  "matin s'il ouvre les fenêtres, cela signifie…",
  ["qu'aucune alerte n'est possible le matin : on ne saurait jamais que la veille",
   "que l'appareil est en panne une journée sur deux",
   "que la mesure obtenue est moins précise",
   "que c'est de toute façon le meilleur choix, puisque le plus précis"],
  "Un critère ne se juge pas dans l'absolu mais par rapport à l'usage. Ici l'usage est "
  "une décision quotidienne prise le matin : un résultat qui arrive avec un jour de retard "
  "ne peut pas la servir, quelle que soit sa qualité.",
  "Une météo parfaitement exacte publiée le lendemain soir ne fait sortir personne avec "
  "un parapluie.",
  "L'erreur classique est de classer les principes par précision seule. La précision est "
  "un critère parmi d'autres — et le délai peut peser plus lourd qu'elle.",
  ["",
   "L'appareil fonctionne parfaitement : c'est son principe même, la pesée d'un filtre "
   "chargé pendant vingt-quatre heures, qui impose ce délai.",
   "C'est l'inverse : la gravimétrie est le plus précis des trois, avec ± 2 % — c'est sa "
   "précision qui coûte du temps, puisqu'il faut accumuler de la matière.",
   "Le meilleur choix dépend de l'usage : pour établir une référence annuelle, oui ; pour "
   "décider d'ouvrir une fenêtre ce matin, non."],
  "Un critère se juge par rapport à l'usage, jamais dans l'absolu."),

q("C1.2", "Une contrainte qui élimine",
  "L'atténuation bêta emploie une source radioactive scellée. Pour un collège, cela…",
  ["l'élimine : une source scellée relève d'un contrôle réglementaire qu'un collège ne peut pas assurer",
   "n'a aucune importance, puisque la source est scellée",
   "impose seulement de former un professeur",
   "l'empêche de mesurer les particules fines"],
  "Certains critères ne se pondèrent pas : ils éliminent. Un principe hors de portée "
  "réglementaire ou juridique sort de la comparaison, même s'il gagne sur tous les autres "
  "points. On appelle cela une contrainte éliminatoire.",
  "Une voiture parfaite mais non homologuée ne se compare pas aux autres : elle ne peut "
  "pas rouler.",
  "L'erreur classique est de tout mettre dans un tableau de notes et de faire une somme. "
  "Certaines lignes ne s'additionnent pas : elles barrent.",
  ["",
   "Le fait qu'elle soit scellée rend l'appareil sûr à l'usage, mais ne supprime ni le "
   "suivi réglementaire, ni la traçabilité, ni la reprise en fin de vie.",
   "La difficulté n'est pas une question de compétence individuelle : elle est "
   "administrative et juridique, et ne se règle pas par une formation.",
   "L'atténuation bêta mesure très bien les particules fines — c'est même un principe de "
   "référence dans les stations officielles."],
  "Certains critères éliminent au lieu de peser. Il faut les regarder en premier."),

q("C1.2", "Ce qu'on accepte de perdre",
  "La classe retient la diffusion optique. Que perd-elle en la choisissant ?",
  ["de la précision — ± 10 % au lieu de ± 2 % — et la possibilité d'entretenir l'optique elle-même",
   "rien : c'est le principe le moins cher et le plus rapide",
   "la possibilité de mesurer les particules fines",
   "la possibilité de comparer ses résultats d'un jour à l'autre"],
  "Choisir, c'est renoncer. Le rôle d'une comparaison de principes n'est pas de désigner "
  "un gagnant sans défaut : c'est de savoir, en s'engageant, ce que l'on abandonne — et "
  "de vérifier que cela ne gêne pas l'usage visé.",
  "En prenant le vélo plutôt que le bus, on gagne en liberté d'horaire et on perd l'abri "
  "en cas de pluie. Le choix reste bon ; il n'est pas gratuit.",
  "L'erreur classique est de défendre son choix en n'énumérant que ses avantages. Une "
  "défense qui ne nomme aucune perte n'a rien choisi : elle a préféré.",
  ["",
   "Le prix et la rapidité sont ses avantages, et ils sont réels — mais un choix qui ne "
   "coûterait rien ne serait pas un choix, seulement une évidence.",
   "La diffusion optique mesure bien les particules fines : c'est sa précision qui est "
   "moindre, pas sa capacité à les détecter.",
   "Les comparaisons d'un jour à l'autre restent possibles et même fiables, puisque le "
   "biais de l'appareil est le même chaque jour."],
  "Une défense sérieuse dit ce qu'on gagne ET ce qu'on accepte de perdre.",
  IMG_PRINCIPES),

# ═══════════ C1.3 — Le rôle des systèmes d'information (5) ═══════════

q("C1.3", "Ce qu'est un système d'information",
  "Un système d'information, c'est…",
  ["l'ensemble des personnes, des outils et des règles qui font circuler l'information",
   "un ordinateur puissant",
   "un logiciel de gestion",
   "le réseau internet"],
  "Le mot « système » compte autant que le mot « information ». Il y a des machines, mais "
  "aussi des gens, des habitudes et des règles : qui dépose quoi, où, quand, et qui a le "
  "droit de le lire. Retirez les règles, il ne reste qu'un tas d'appareils.",
  "Au collège, la vie scolaire, le logiciel de notes, le cahier de texte et la règle "
  "« les notes se saisissent avant le conseil » forment ensemble un système d'information.",
  "L'erreur classique est de réduire un système d'information à sa partie visible, la "
  "machine. La partie qui tombe en panne le plus souvent est l'autre.",
  ["",
   "La puissance de la machine ne change rien à la circulation de l'information : un "
   "système d'information peut fonctionner sur du papier.",
   "Un logiciel n'est qu'un des outils du système : il ne contient ni les personnes qui "
   "l'alimentent, ni les règles qui disent qui peut y écrire.",
   "Internet n'est qu'un moyen de transport parmi d'autres ; un système d'information "
   "peut exister entièrement à l'intérieur d'un établissement."],
  "Des personnes, des outils, des règles. Les trois, ou ce n'en est pas un.",
  IMG_SI),

q("C1.3", "Où la donnée devient information",
  "Dans la chaîne du capteur à l'ENT, à quel étage la donnée devient-elle une information ?",
  ["au traitement : c'est là qu'on trie, qu'on écarte et qu'on calcule",
   "à la source, dès que le capteur mesure",
   "au stockage, quand la valeur est enregistrée",
   "à la diffusion, quand le graphique est publié"],
  "Le traitement est l'étage où quelqu'un décide : quelles valeurs on garde, ce qu'on "
  "calcule, ce qu'on compare. C'est donc l'étage où l'on peut le plus se tromper, et "
  "celui qu'il faut pouvoir refaire.",
  "Un thermomètre produit des nombres ; c'est la moyenne mensuelle comparée à celle des "
  "dix dernières années qui informe sur un réchauffement.",
  "L'erreur classique est de placer la transformation à la diffusion, parce que c'est là "
  "que ça devient visible. Visible n'est pas la même chose que transformé.",
  ["",
   "Le capteur produit des données brutes et n'en juge aucune : il ne compare rien, il "
   "ne calcule rien, il ne trie rien.",
   "Le stockage conserve sans juger : la valeur qui y entre en ressort identique, "
   "juste ou fausse.",
   "La diffusion rend l'information visible par d'autres, mais elle ne la fabrique pas : "
   "à cet étage, les choix ont déjà été faits."],
  "La donnée devient information là où quelqu'un choisit ce qu'on en garde.",
  IMG_SI),

q("C1.3", "Travailler sur une copie",
  "Pourquoi la classe travaille-t-elle sur une copie du fichier de relevés ?",
  ["pour que l'original reste intact et qu'on puisse toujours revenir en arrière",
   "pour aller plus vite",
   "pour économiser de la place sur le serveur",
   "parce que l'original est protégé par un mot de passe"],
  "L'original est la trace de ce que le capteur a produit. Tant qu'il existe, toute "
  "erreur de traitement est réparable : on repart de zéro. Le jour où il est écrasé, "
  "plus aucune vérification n'est possible.",
  "On photocopie un document ancien avant de l'annoter, précisément pour pouvoir se "
  "tromper sans conséquence.",
  "L'erreur classique est de considérer la copie comme une précaution facultative « au "
  "cas où ». C'est en réalité ce qui rend le travail vérifiable.",
  ["",
   "Travailler sur une copie ne fait rien gagner en vitesse : c'est même une opération "
   "de plus.",
   "Une copie occupe de la place supplémentaire, pas moins : l'argument est exactement "
   "à l'envers.",
   "Un mot de passe n'est pas ce qui est en jeu : même avec tous les droits, on "
   "travaillerait sur une copie."],
  "L'original ne se modifie pas. C'est lui qui permet de réparer les erreurs."),

q("C1.3", "Une erreur qui remonte tous les étages",
  "Une valeur fausse enregistrée à la source…",
  ["se propage à tous les étages tant que personne ne l'écarte",
   "est corrigée automatiquement par le tableur",
   "disparaît au moment du stockage",
   "n'a d'effet qu'au moment de la diffusion"],
  "Aucun étage ne nettoie tout seul. Une valeur fausse est stockée telle quelle, entre "
  "dans les calculs, puis dans le graphique, puis dans la décision. Elle ne s'arrête que "
  "là où quelqu'un a décidé de la chercher.",
  "Une adresse mal saisie à l'inscription se retrouve sur les bulletins, les convocations "
  "et les courriers, jusqu'à ce que quelqu'un la corrige à la source.",
  "L'erreur classique est de supposer qu'un logiciel « vérifie ». Il vérifie ce qu'on lui "
  "a demandé de vérifier, et rien d'autre (règle n°47).",
  ["",
   "Le tableur calcule ce qu'on lui demande sur ce qu'on lui donne : il n'a aucun moyen "
   "de savoir qu'une valeur est physiquement impossible.",
   "Le stockage conserve, il ne juge pas : la valeur fausse y est rangée exactement comme "
   "les autres.",
   "Elle a produit son effet bien avant : dans les moyennes, donc dans le graphique, donc "
   "dans la décision prise à partir du graphique."],
  "Une erreur ne s'arrête qu'où quelqu'un la cherche."),

q("C1.3", "Écrire qui a le droit de faire quoi",
  "À quoi sert d'écrire, pour chaque étage, qui a le droit d'y écrire ?",
  ["à savoir qui peut modifier quoi, et donc où chercher quand quelque chose a changé",
   "à empêcher les élèves de travailler sur les données",
   "à respecter une obligation administrative",
   "à accélérer le fonctionnement du système"],
  "Les droits ne servent pas seulement à empêcher : ils servent à comprendre. Quand une "
  "valeur a changé, la liste des personnes autorisées est la première chose qui réduit "
  "la recherche — c'est la question par laquelle commence toute enquête.",
  "Si seuls deux comptes pouvaient écrire dans un fichier, on ne fouille pas trente "
  "hypothèses : on en regarde deux.",
  "L'erreur classique est de voir les droits comme une contrainte imposée d'en haut. Ils "
  "sont d'abord un outil de diagnostic.",
  ["",
   "La classe travaille pleinement — dans une copie : les droits organisent le travail, "
   "ils ne l'interdisent pas.",
   "L'obligation existe, mais elle n'explique pas l'utilité : on écrirait ces droits même "
   "si aucun texte ne l'exigeait.",
   "Les droits n'ont aucun effet sur la vitesse du système : ils portent sur qui fait "
   "quoi, pas sur la performance des machines."],
  "Savoir qui peut écrire, c'est savoir où chercher quand quelque chose a changé.",
  IMG_SI),

# ═══════════ C1.4 — Recenser, classer, stocker, retrouver (5) ═══════════

q("C1.4", "Un nom dit ce que c'est",
  "Le fichier « capteur mardi PIC ATTENTION.csv » est mal nommé parce qu'il…",
  ["dit ce qu'on en pense, et non ce que le fichier contient",
   "est trop court",
   "ne contient pas de chiffre",
   "est écrit en français"],
  "Un nom de fichier est une adresse, pas un commentaire. « PIC ATTENTION » est une "
  "interprétation, valable un jour et fausse le suivant ; « releves-air-2026-s10 » reste "
  "exact et retrouvable dans deux ans.",
  "Nommer une photo « super soirée » ne permet de la retrouver que si l'on se souvient "
  "l'avoir trouvée super. « 2026-04-02-remise-des-prix » ne demande rien à la mémoire.",
  "L'erreur classique est de nommer au moment où l'on est le plus intéressé par le "
  "contenu — donc de nommer son émotion plutôt que le contenu.",
  ["",
   "Il est au contraire assez long : c'est son contenu qui pose problème, pas sa taille.",
   "Un nom sans chiffre peut être excellent ; ce qui manque ici n'est pas un chiffre "
   "mais une description de ce que le fichier contient.",
   "La langue n'est pas en cause : on peut parfaitement nommer un fichier en français, "
   "à condition de dire ce qu'il contient."],
  "Un nom dit CE QUE C'EST, jamais ce qu'on en pense.",
  IMG_ARBO),

q("C1.4", "La date qui met de l'ordre",
  "Pourquoi écrire les dates sous la forme 2026-04-02 plutôt que 02-04-2026 ?",
  ["parce qu'ainsi le tri alphabétique donne l'ordre chronologique",
   "parce que c'est la façon anglaise de noter les dates",
   "parce que c'est plus court à taper",
   "parce que les ordinateurs refusent l'autre format"],
  "En commençant par l'unité la plus grande, on obtient une propriété précieuse : ranger "
  "les noms par ordre alphabétique range les fichiers par ordre de date. Aucun logiciel "
  "particulier n'est nécessaire.",
  "Trié alphabétiquement, 2025-12-31 vient avant 2026-01-01 ; avec 31-12-2025 et "
  "01-01-2026, le tri place janvier avant décembre.",
  "L'erreur classique est de croire que c'est une convention arbitraire. C'est un choix "
  "qui produit un effet mécanique et vérifiable.",
  ["",
   "L'ordre anglais est mois-jour-année, différent de celui-ci : la ressemblance est "
   "trompeuse, et cet ordre-là ne trie pas correctement non plus.",
   "Les deux écritures comptent exactement le même nombre de caractères : la longueur "
   "n'est pas l'argument.",
   "Les ordinateurs acceptent n'importe quel format dans un nom de fichier ; c'est le "
   "résultat du tri qui change, pas l'autorisation."],
  "AAAA-MM-JJ : le tri alphabétique devient un tri chronologique."),

q("C1.4", "Le doublon",
  "« finalV2 (copie).csv » est identique, octet pour octet, à « finalV2.csv ». Que faire ?",
  ["le supprimer : deux fichiers identiques créent un doute, pas une sécurité",
   "le garder, on ne sait jamais",
   "le renommer finalV3",
   "le déplacer dans un dossier « à ranger »"],
  "Une sauvegarde est une copie rangée AILLEURS, datée, et dont on sait qu'elle en est "
  "une. Un doublon posé à côté de l'original n'est pas une sauvegarde : c'est une source "
  "d'hésitation, et le jour où l'un des deux évolue, plus personne ne sait lequel fait foi.",
  "Deux exemplaires d'un même formulaire sur un bureau font perdre du temps à chaque "
  "fois qu'on cherche « le bon ».",
  "L'erreur classique est de confondre redondance et sécurité. La redondance ne protège "
  "que si l'on sait laquelle des copies est la référence.",
  ["",
   "« On ne sait jamais » est précisément le problème : garder sans savoir pourquoi "
   "produit un dossier où l'on ne sait plus quel fichier fait foi.",
   "Le renommer en finalV3 laisse croire à une version plus récente alors que le contenu "
   "est identique : cela aggrave la confusion au lieu de la lever.",
   "Le déplacer sans le supprimer ne fait que repousser le doute dans un autre dossier, "
   "où il resurgira plus tard, encore plus difficile à trancher."],
  "Une seule version conservée : la bonne. Les sauvegardes vont ailleurs, et sont datées.",
  IMG_ARBO),

q("C1.4", "Ni espaces, ni accents",
  "Pourquoi éviter les espaces, les accents et les majuscules dans un nom de fichier ?",
  ["pour qu'un nom survive au passage d'un ordinateur, d'un site ou d'un système à un autre",
   "pour taper plus vite",
   "parce que c'est interdit",
   "pour économiser de la place"],
  "Les systèmes ne traitent pas ces caractères de la même façon : un accent peut se "
  "transformer en suite illisible, une majuscule être ignorée ici et distinguée là, un "
  "espace couper une adresse en deux. Un nom sobre traverse tout sans se déformer.",
  "« relevé été.csv » déposé sur un serveur peut revenir en « relev%C3%A9%20t%C3%A9.csv ».",
  "L'erreur classique est de juger d'après son propre ordinateur, où tout fonctionne. Le "
  "problème n'apparaît qu'au moment du transfert — c'est-à-dire trop tard.",
  ["",
   "Le gain de frappe est dérisoire et n'aurait jamais justifié une règle suivie "
   "partout dans le monde professionnel.",
   "Rien ne l'interdit : le système accepte ces caractères, et c'est bien ce qui rend "
   "le piège dangereux.",
   "Un caractère accentué occupe un ou deux octets : à l'échelle d'un fichier, c'est "
   "totalement négligeable."],
  "Un nom doit survivre au voyage. Sobre, il voyage ; décoré, il se casse."),

q("C1.4", "Un dossier qui ne dit rien",
  "Un dossier nommé « Nouveau dossier/ » pose problème parce qu'il…",
  ["ne dit rien de ce qu'il contient : son nom n'aide personne à chercher",
   "est vide",
   "a été créé par erreur",
   "ne peut pas être renommé"],
  "Une arborescence sert à retrouver sans ouvrir. Chaque niveau doit réduire la "
  "recherche : « 1-releves », « 2-analyses », « 3-documents ». Un nom qui ne réduit rien "
  "oblige à ouvrir — et l'arborescence ne sert plus à rien.",
  "Dans une bibliothèque, un rayon étiqueté « livres » n'aide personne ; « romans "
  "policiers » aide.",
  "L'erreur classique est de remettre le nommage à plus tard, au moment où l'on crée le "
  "dossier. Plus tard, on ne sait plus ce qu'on y avait mis.",
  ["",
   "Il contient au contraire trois fichiers : c'est bien son NOM, et non son contenu, "
   "qui est en cause.",
   "Il a été créé volontairement, pour y ranger quelque chose ; c'est l'étape du nommage "
   "qui a été sautée, pas la création qui était une erreur.",
   "Renommer un dossier est toujours possible et prend deux secondes — c'est justement "
   "ce qu'il faut faire."],
  "Chaque niveau d'une arborescence doit réduire la recherche. Sinon il l'allonge.",
  IMG_ARBO),

# ═══════════ C1.5 — Sécuriser, et respecter la propriété intellectuelle (5) ═══════════

q("C1.5", "La première question après un incident",
  "Une valeur du fichier partagé a été modifiée, personne ne sait par qui. Par quoi "
  "commence-t-on ?",
  ["par regarder qui avait le droit d'écrire dans ce fichier",
   "par interroger toute la classe",
   "par supprimer le fichier",
   "par changer le mot de passe de l'ENT"],
  "La liste des personnes autorisées transforme une question ouverte en question fermée. "
  "C'est la raison profonde pour laquelle on écrit les droits AVANT l'incident : sans "
  "eux, l'enquête n'a pas de point de départ.",
  "Une salle dont trois personnes seulement ont la clé se cherche autrement qu'une salle "
  "toujours ouverte.",
  "L'erreur classique est de commencer par une action spectaculaire — changer les mots de "
  "passe, tout verrouiller — avant d'avoir compris ce qui s'est passé.",
  ["",
   "Interroger trente personnes sans avoir réduit la liste revient à chercher au hasard, "
   "et met en cause des élèves qui n'avaient même pas accès au fichier.",
   "Supprimer le fichier détruit la trace de la modification : on perd la seule pièce qui "
   "permettait de comprendre.",
   "Changer le mot de passe peut être utile ensuite, mais fait d'abord perdre la "
   "possibilité de savoir qui s'était connecté, et avec quels droits."],
  "Avant de chercher qui, on regarde qui POUVAIT. C'est pour cela qu'on écrit les droits."),

q("C1.5", "Le droit minimal",
  "Quelle règle aurait le mieux évité cet incident ?",
  ["donner à chacun le droit minimal dont il a besoin : lire ne demande pas d'écrire",
   "mettre un mot de passe plus long",
   "interdire l'accès à l'ENT aux élèves",
   "sauvegarder le fichier plus souvent"],
  "C'est le principe du moindre privilège : chacun reçoit exactement ce que sa tâche "
  "exige, pas davantage. Une classe qui doit consulter des relevés a besoin de les lire ; "
  "le droit d'écrire, qu'elle n'utilise pas, ne fait qu'ouvrir une possibilité d'erreur.",
  "On confie la clé de la salle de sport au professeur d'EPS, pas un passe qui ouvre "
  "aussi le secrétariat.",
  "L'erreur classique est d'accorder largement « pour éviter les blocages ». Chaque droit "
  "inutile est une occasion d'accident, y compris involontaire.",
  ["",
   "Un mot de passe plus long protège contre quelqu'un d'extérieur ; il ne change rien "
   "quand la personne était autorisée et n'aurait pas dû l'être.",
   "Interdire l'ENT supprime l'usage plutôt que le risque : la classe ne pourrait plus "
   "travailler du tout.",
   "Sauvegarder aide à réparer après coup, mais n'empêche pas la modification — et il "
   "faut encore s'apercevoir qu'elle a eu lieu."],
  "Le moindre privilège : exactement les droits nécessaires, pas un de plus."),

q("C1.5", "À quoi sert une version datée",
  "Garder une copie datée du fichier chaque soir permet…",
  ["de comparer, donc de savoir ce qui a changé et de revenir en arrière",
   "d'empêcher toute modification",
   "d'identifier à coup sûr le coupable",
   "de rendre le fichier illisible pour les autres"],
  "Une suite de versions datées est une mémoire. Elle ne protège de rien par elle-même, "
  "mais elle rend visible : sans point de comparaison, on ne sait même pas qu'une valeur "
  "a changé.",
  "Deux photographies d'une même salle à un mois d'intervalle montrent tout de suite ce "
  "qui a bougé ; une seule photo ne montre rien.",
  "L'erreur classique est d'attendre d'une sauvegarde qu'elle protège. Elle répare et "
  "elle révèle : ce n'est pas la même fonction qu'un droit d'accès.",
  ["",
   "Une copie n'empêche personne de modifier le fichier courant : elle permet seulement "
   "de retrouver l'état d'avant.",
   "La comparaison dit ce qui a changé et quand, pas par qui : c'est la journalisation "
   "des accès qui répond à cette question.",
   "Une copie datée est un fichier ordinaire, lisible comme les autres : rien n'y est "
   "chiffré ni masqué."],
  "Une version datée ne protège pas : elle permet de comparer, donc de réparer."),

q("C1.5", "La notice trouvée sur internet",
  "La notice du capteur, en anglais, vient du site du fabricant. La republier sur l'ENT…",
  ["demande de vérifier la licence, et de citer la source dans tous les cas",
   "est libre : elle est déjà sur internet",
   "est interdite en toutes circonstances",
   "ne pose de question que si elle est payante"],
  "Être accessible n'est pas être libre de droits. Un document publié reste protégé par "
  "le droit d'auteur ; le republier suppose une autorisation, ou une licence qui la "
  "donne. Et la source se cite toujours, même quand la republication est permise.",
  "Un article de presse est lisible en ligne ; le recopier entier sur un autre site est "
  "une contrefaçon, même sans en tirer d'argent.",
  "L'erreur classique est de confondre « accessible », « gratuit » et « libre ». Ce sont "
  "trois choses différentes.",
  ["",
   "La mise en ligne ne vaut pas renoncement aux droits : l'auteur conserve les siens, "
   "que l'accès soit gratuit ou non.",
   "Beaucoup de notices sont republiables, sous licence ouverte ou avec l'accord du "
   "fabricant : l'interdiction générale est fausse.",
   "Le prix n'a rien à voir : un document gratuit peut être strictement protégé, un "
   "document payant peut être sous licence ouverte."],
  "Accessible ≠ libre. On vérifie la licence, et on cite la source dans tous les cas."),

q("C1.5", "Le mot de passe partagé",
  "Un mot de passe unique, partagé par toute la classe…",
  ["ne protège plus rien et empêche de savoir qui a fait quoi",
   "est acceptable s'il est assez long",
   "est plus sûr qu'un mot de passe par élève",
   "est obligatoire pour travailler en classe"],
  "Un mot de passe remplit deux fonctions : empêcher l'accès des autres, et rattacher "
  "chaque action à quelqu'un. Partagé, il perd les deux — il circule bien au-delà de la "
  "classe, et toutes les actions se ressemblent.",
  "Un cahier signé « la classe » n'engage personne et ne prouve rien.",
  "L'erreur classique est de juger un mot de passe à sa solidité seule. Un mot de passe "
  "de trente caractères connu de trente personnes ne vaut rien.",
  ["",
   "La longueur protège contre une attaque par essais successifs ; elle ne change rien "
   "au fait que trente personnes le connaissent.",
   "C'est l'inverse : des identifiants distincts permettent de retirer un accès "
   "individuellement et de rattacher chaque action à son auteur.",
   "Rien ne l'impose ; les environnements scolaires fournissent au contraire un compte "
   "personnel à chaque élève, précisément pour cette raison."],
  "Un mot de passe partagé ne protège plus et ne prouve plus rien."),

# ═══════════ C1.6 — La responsabilité de chacun (4) ═══════════

q("C1.6", "Exacte et inacceptable",
  "Publier « le pic vient du passage de M. ___, agent d'entretien », avec sa photo. "
  "Cette publication est…",
  ["exacte et inacceptable : une mesure d'air devient une accusation contre une personne identifiable",
   "fausse, donc à écarter",
   "acceptable, puisque c'est vrai",
   "acceptable si l'agent a été prévenu"],
  "C'est le cœur de la question : la vérité d'un fait ne suffit pas à autoriser sa "
  "publication. Il faut aussi se demander qui il désigne, devant qui, et avec quel effet "
  "sur cette personne.",
  "Dire publiquement d'un élève, en le nommant, qu'il est arrivé en retard onze fois est "
  "exact — et ne se publie pas sur le site du collège.",
  "L'erreur classique est de traiter « est-ce vrai ? » comme la seule question. C'est la "
  "première ; elle n'est pas la dernière.",
  ["",
   "Elle n'est pas fausse : le pic correspond bien au passage de la balayeuse, et c'est "
   "précisément ce qui rend le cas difficile.",
   "La vérité d'un fait n'a jamais suffi à en autoriser la diffusion sur une personne "
   "identifiable : la question du préjudice reste entière.",
   "Un accord ne rétablit pas l'équilibre quand il est demandé par une institution à un "
   "agent, et il ne protège pas des lecteurs extérieurs au collège."],
  "La question n'est pas seulement « est-ce vrai ? » mais « qui cela désigne, et pour quel effet ? »",
  IMG_DESIGNE),

q("C1.6", "Acceptable et inutile",
  "Publier seulement « la concentration monte les mardis et jeudis à 7 h », sans dire "
  "pourquoi. Cette publication est…",
  ["acceptable et inutile : personne ne peut agir sans savoir d'où vient le pic",
   "la meilleure des trois, puisqu'elle ne met personne en cause",
   "malhonnête, puisqu'elle cache la cause",
   "identique à la troisième publication"],
  "Protéger quelqu'un en supprimant toute information utile n'est pas une solution : "
  "c'est un renoncement. Le travail consiste à trouver la formulation qui protège ET "
  "permet d'agir — pas à choisir entre les deux.",
  "Signaler qu'un couloir est glissant certains matins, sans dire quand ni pourquoi, ne "
  "fait rien changer.",
  "L'erreur classique est de croire qu'on a bien fait dès qu'on n'a nui à personne. Un "
  "travail qui ne sert à rien n'est pas pour autant réussi.",
  ["",
   "Elle ne met personne en cause, c'est vrai, mais elle laisse le problème entier : "
   "aucune décision ne peut en découler.",
   "Elle ne cache rien de trompeur : elle dit un fait exact, simplement incomplet. La "
   "malhonnêteté supposerait une intention de tromper.",
   "La troisième nomme la cause — le nettoyage mécanique — et propose une action ; "
   "celle-ci ne fait ni l'un ni l'autre."],
  "Protéger en supprimant toute utilité n'est pas une solution : c'est un abandon.",
  IMG_DESIGNE),

q("C1.6", "Désigner sans nommer",
  "Écrire « la personne qui passe la balayeuse le mardi », sans donner de nom…",
  ["la désigne quand même : dans un collège, une seule personne correspond à cette description",
   "protège suffisamment son identité",
   "rend l'information anonyme",
   "ne relève pas des données personnelles"],
  "Une donnée est personnelle dès qu'elle permet d'identifier quelqu'un, directement ou "
  "indirectement. Le croisement de quelques détails — un métier, un jour, un lieu — suffit "
  "souvent : dans un établissement, un seul agent correspond.",
  "« L'élève de 5eB qui joue du tuba » ne comporte aucun nom et désigne pourtant une "
  "personne précise pour tous ceux qui la connaissent.",
  "L'erreur classique est de croire qu'on a anonymisé parce qu'on a retiré le nom. "
  "L'anonymat se juge sur ce que le lecteur peut reconstituer.",
  ["",
   "La protection est illusoire pour les lecteurs du collège, qui sont justement les "
   "premiers concernés et savent qui fait ce travail.",
   "L'anonymat suppose que personne ne puisse remonter à la personne ; ici, tout le "
   "monde le peut sans effort.",
   "C'est bien une donnée personnelle, puisqu'elle permet une identification indirecte — "
   "et le droit le dit explicitement."],
  "Une donnée est personnelle dès qu'elle permet d'identifier, même indirectement.",
  IMG_DESIGNE),

q("C1.6", "Ce qui distingue la bonne publication",
  "Publier « le pic correspond au nettoyage mécanique de la cour ; peut-on le décaler "
  "avant l'arrivée des élèves ? ». Ce qui distingue cette version des deux autres :",
  ["elle désigne une organisation — l'horaire du nettoyage — et non une personne",
   "elle est plus courte",
   "elle ne donne aucun chiffre",
   "elle évite de dire toute la vérité"],
  "Elle dit le même fait, complètement, et le rattache à ce qui peut être changé : un "
  "horaire, une organisation. Une décision devient possible, et personne n'est mis en "
  "cause. C'est ce déplacement — de la personne vers l'organisation — qui fait tout.",
  "« Le portail se bloque quand deux cars arrivent en même temps » ouvre une solution ; "
  "« M. ___ ouvre mal le portail » n'en ouvre aucune.",
  "L'erreur classique est de croire qu'il fallait choisir entre dire la vérité et "
  "protéger quelqu'un. La troisième voie existe presque toujours — encore faut-il la chercher.",
  ["",
   "Sa longueur n'a aucune importance : elle est même plus longue que la deuxième, et "
   "c'est la première qui est la plus brève.",
   "Elle s'appuie au contraire sur les chiffres mesurés — c'est ce qui lui donne sa "
   "force et rend la proposition crédible.",
   "Elle dit exactement la même vérité que les deux autres : ce qu'elle change, c'est "
   "ce qu'elle désigne, pas ce qu'elle affirme."],
  "On n'a pas le choix des faits. On a le choix de ce qu'on en publie — et de qui cela désigne.",
  IMG_DESIGNE),
