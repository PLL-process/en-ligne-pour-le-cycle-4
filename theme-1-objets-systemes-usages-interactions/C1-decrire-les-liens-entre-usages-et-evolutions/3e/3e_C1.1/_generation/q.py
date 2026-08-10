# -*- coding: utf-8 -*-
"""Les 30 questions du QCM 3e_C1.1 à C1.4 — Tsinghua, robots, drones et IA face aux feux.

Répartition : C1.1 (8) · C1.2 (7) · C1.3 (8) · C1.4 (7). Sept illustrées.

Toutes les bonnes réponses sont en position 0 ici ; fix_r.js les répartit ensuite
sur A/B/C/D de façon déterministe.

Les chiffres sont ceux du fichier public du lot — ministère de l'Intérieur,
JRC/EFFIS, ADEME, PNUE. Les questions qui touchent aux données du PNUE portent la
même discipline que la séquence (règle n°68) : on y compare des indicateurs et
des méthodes de mesure, jamais des souffrances.
"""

IMG_REGIMES = {
    "src": "Images/corrige_trois_regimes_de_surveillance.svg",
    "alt": "Les trois régimes de surveillance des feux — vigie humaine, satellite, détection "
           "multi-indices — avec ce que chacun permet, ce qu'il ne permet pas, et le métier qu'il "
           "suppose.",
}
IMG_HERSCHEL = {
    "src": "Images/corrige_de_la_decouverte_a_l_usage.svg",
    "alt": "Frise de la découverte de l'infrarouge par Herschel en 1800 jusqu'au drone thermique "
           "d'aujourd'hui, en passant par la fabrication de détecteurs puis leur diffusion.",
}
IMG_ZONES = {
    "src": "Images/corrige_ce_qui_ne_se_convertit_pas.svg",
    "alt": "Trois zones : ce qui se convertit grâce à une unité commune, ce qui ne se convertit "
           "pas faute d'unité et de nature communes, et ce qui ne se compare jamais.",
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


# ═══════════ C1.1 — Les innovations de rupture (8) ═══════════

q("C1.1", "Amélioration ou rupture", "Une tour de guet plus haute, avec de meilleures jumelles, est…",
  ["une amélioration : on fait mieux la même chose, avec le même savoir-faire",
   "une innovation de rupture",
   "un changement sans effet",
   "une régression"],
  "Une amélioration se reconnaît à ce qu'elle ne change ni la nature de l'usage, ni le métier de "
  "celui qui l'exerce. Le guetteur voit plus loin ; il regarde toujours, et son savoir-faire vaut "
  "toujours.",
  "Des jumelles à fort grossissement font gagner quelques kilomètres. Elles ne font pas voir la "
  "nuit.",
  "Confondre l'ampleur du gain avec la nature du changement. Un gain considérable peut n'être "
  "qu'une amélioration.",
  ["",
   "Rien de nouveau ne devient possible : on voit plus loin, on ne voit pas autre chose ni autrement.",
   "L'effet est réel — la portée augmente — mais il ne change pas la nature de la surveillance.",
   "Rien ne se dégrade : la tour plus haute fait strictement mieux que la précédente."],
  "Une amélioration fait mieux la même chose. Le métier ne change pas.",
  img=IMG_REGIMES),

q("C1.1", "Le signe de la rupture", "Le signe le plus sûr qu'un changement est une rupture, c'est que…",
  ["le métier change : le savoir-faire d'avant ne suffit plus",
   "le prix baisse",
   "l'objet devient plus petit",
   "les journaux en parlent"],
  "C'est le critère le plus fiable, parce qu'il est observable. Quand une rupture a lieu, les "
  "compétences qui faisaient la valeur d'un professionnel cessent de suffire — et de nouvelles "
  "compétences deviennent nécessaires.",
  "Guetteur, analyste d'images, exploitant de système : trois savoir-faire sans rapport entre eux, "
  "pour une seule et même mission.",
  "Chercher la rupture dans l'objet. Elle se voit mieux dans les gens qui l'emploient.",
  ["",
   "Beaucoup d'améliorations font baisser le prix sans rien changer d'autre, et certaines ruptures coûtent d'abord bien plus cher.",
   "La miniaturisation est un progrès technique fréquent, qui accompagne aussi bien les améliorations que les ruptures.",
   "La couverture médiatique dit ce qui est nouveau, pas ce qui est structurellement différent."],
  "Regarde le métier. S'il change, c'est une rupture.",
  img=IMG_REGIMES),

q("C1.1", "Pourquoi le satellite rompt", "Le passage à l'observation satellitaire est une rupture parce qu'elle…",
  ["rend possible ce qui ne l'était pas du tout : voir la nuit, et sur un continent entier",
   "coûte moins cher qu'une tour de guet",
   "est plus récente",
   "emploie de l'électronique"],
  "Aucune tour, aussi haute soit-elle, ne permet de surveiller un continent ni de voir dans "
  "l'obscurité. Ce n'est pas un regard humain amélioré : c'est une autre façon de savoir, fondée "
  "sur un autre phénomène physique.",
  "Une anomalie thermique se repère la nuit, quand un guetteur ne verrait rien du tout.",
  "Justifier une rupture par la nouveauté ou par le prix, au lieu de dire ce qui devient possible.",
  ["",
   "Un satellite coûte infiniment plus cher qu'une tour : ce n'est certainement pas par là qu'il s'impose.",
   "La date n'explique rien : une technologie récente peut n'apporter qu'une amélioration marginale.",
   "L'électronique est présente dans quantité d'améliorations sans rupture — une paire de jumelles à stabilisation électronique reste des jumelles."],
  "Une rupture se justifie par ce qu'elle rend possible, jamais par sa date."),

q("C1.1", "Ce qu'une rupture ne fait pas", "Une innovation de rupture fait-elle disparaître ce qui la précède ?",
  ["pas toujours : des tours de guet fonctionnent encore, parce qu'un œil humain lève un doute qu'aucun capteur ne lève",
   "oui, toujours et immédiatement",
   "oui, après quelques années",
   "non, jamais"],
  "C'est l'erreur la plus fréquente sur cette notion. Une rupture ouvre une possibilité nouvelle ; "
  "elle ne rend pas forcément inutile ce qui existait. Les régimes coexistent souvent, chacun "
  "couvrant ce que l'autre ne couvre pas.",
  "Un satellite signale une anomalie thermique ; il ne dit pas si c'est un feu, un toit brûlant ou "
  "un feu de camp autorisé. Quelqu'un doit encore aller voir.",
  "Croire que le nouveau remplace mécaniquement l'ancien, et cesser d'étudier ce qui subsiste.",
  ["",
   "La disparition immédiate est rare : les moyens anciens continuent souvent de servir là où les nouveaux échouent.",
   "Le délai n'est pas la question : certains moyens anciens ne disparaissent jamais, parce qu'ils font quelque chose d'irremplaçable.",
   "Certaines ruptures font bien disparaître ce qui précède — la photographie argentique en est un exemple. Ce n'est simplement pas une règle."],
  "Une rupture ouvre. Elle ne referme pas forcément.",
  img=IMG_REGIMES),

q("C1.1", "Trois métiers", "Guetteur, analyste d'images, exploitant de système sont…",
  ["trois savoir-faire sans rapport, pour une même mission — c'est ce qui signale deux ruptures",
   "trois noms pour le même métier",
   "trois niveaux hiérarchiques",
   "trois façons de dire « surveillant »"],
  "Un guetteur sait rester attentif des heures. Un analyste sait lire une donnée et distinguer un "
  "signal d'un artefact. Un exploitant sait faire tenir un réseau, gérer une énergie et trier des "
  "alertes. On ne passe pas de l'un à l'autre par la formation continue.",
  "La mission est constante depuis toujours&nbsp;: repérer un départ de feu au plus tôt. Tout le "
  "reste a changé deux fois.",
  "Croire qu'un même mot — « surveillance » — désigne un même travail à travers les époques.",
  ["",
   "Les trois n'exigent ni les mêmes gestes, ni les mêmes connaissances, ni les mêmes outils.",
   "Aucune hiérarchie n'est en jeu : ce sont des métiers différents, pas des échelons.",
   "Le mot commun cache justement la différence, et c'est ce que la séquence cherche à faire voir."],
  "Quand trois savoir-faire sans rapport se succèdent pour une même mission, il y a eu des ruptures."),

q("C1.1", "Une amélioration déguisée", "Un réseau de capteurs deux fois plus dense, sur le même principe, est…",
  ["une amélioration : plus de points de mesure, même façon de détecter, même métier",
   "une rupture, car il y a deux fois plus de capteurs",
   "une rupture, car la couverture change",
   "un retour en arrière"],
  "Doubler la densité améliore la couverture et réduit les angles morts. Mais on détecte de la "
  "même façon, on exploite le même système, et l'on n'a rien rendu possible qui ne l'était pas.",
  "Deux fois plus de capteurs, c'est deux fois plus de maintenance — et exactement le même travail.",
  "Prendre une différence de quantité pour une différence de nature.",
  ["",
   "Le nombre ne fait pas la rupture : cent capteurs identiques détectent comme un seul, en plus d'endroits.",
   "La couverture s'améliore, mais rien de nouveau ne devient possible : ce sont les mêmes grandeurs, mesurées de la même façon.",
   "Rien ne recule : la détection est strictement meilleure qu'avant."],
  "Plus, ce n'est pas autrement. La quantité ne fait pas la rupture."),

q("C1.1", "Rupture et coexistence", "Aujourd'hui, la surveillance des feux emploie…",
  ["les trois régimes à la fois, chacun couvrant ce que les autres ne couvrent pas",
   "seulement le régime le plus récent",
   "seulement les satellites",
   "seulement des capteurs au sol"],
  "Le satellite voit large mais grossier et par intermittence ; les capteurs voient fin mais "
  "localement ; l'humain lève les doutes. Un système réel combine, parce qu'aucun régime n'est "
  "complet à lui seul.",
  "Un satellite signale une zone, un capteur confirme localement, un opérateur décide d'engager "
  "les moyens.",
  "Raisonner comme si l'histoire des techniques était une file où chacun chasse le précédent.",
  ["",
   "Le plus récent a ses angles morts — portée limitée, réseau à entretenir — que les autres comblent.",
   "Le satellite seul manquerait tous les départs survenant entre deux passages, et serait aveugle sous les nuages.",
   "Des capteurs seuls ne couvriraient jamais les surfaces concernées : il en faudrait un nombre irréaliste."],
  "Les régimes coexistent. Chacun couvre le trou de l'autre.",
  img=IMG_REGIMES),

q("C1.1", "Ce qui prouve une rupture", "Pour établir qu'un changement est une rupture, il faut montrer…",
  ["ce qui devient possible et ne l'était pas du tout, et quel savoir-faire cesse de suffire",
   "que la technologie employée est nouvelle",
   "que les performances ont augmenté",
   "que l'objet a changé d'apparence"],
  "C'est une démonstration en deux temps, et les deux sont nécessaires. La possibilité nouvelle "
  "évite de confondre avec un simple gain ; le savoir-faire caduc évite de qualifier de rupture "
  "tout ce qui est spectaculaire.",
  "Voir la nuit sur un continent (possibilité nouvelle) + le guetteur ne sait pas lire une image "
  "satellitaire (savoir-faire caduc) = rupture établie.",
  "S'arrêter au premier temps de la démonstration, et appeler rupture toute nouveauté frappante.",
  ["",
   "La nouveauté de la technologie ne dit rien de la nature du changement qu'elle produit.",
   "Une hausse de performance, même forte, reste une amélioration si l'usage et le métier demeurent.",
   "L'apparence ne prouve rien : deux objets très différents peuvent faire exactement la même chose."],
  "Deux preuves à fournir : ce qui devient possible, et ce qui devient caduc."),

# ═══════════ C1.2 — De la découverte scientifique à ses effets (7) ═══════════

q("C1.2", "Ce que Herschel cherchait", "En 1800, William Herschel place des thermomètres sous chaque couleur d'un spectre. Il cherchait…",
  ["quelle couleur chauffe le plus — il ne cherchait pas l'infrarouge",
   "un moyen de détecter les incendies",
   "à fabriquer une caméra",
   "à mesurer la température du Soleil"],
  "C'est une découverte faite en cherchant autre chose. Le thermomètre placé juste au-delà du "
  "rouge, là où l'œil ne voit plus rien, monte davantage que tous les autres : il existe donc un "
  "rayonnement invisible. Personne n'avait posé cette question.",
  "Beaucoup de découvertes majeures viennent d'une mesure faite « pour voir », et d'un résultat "
  "qu'on n'attendait pas.",
  "Raconter l'histoire des sciences à l'envers, comme si l'on avait cherché ce qu'on a trouvé.",
  ["",
   "Les feux de forêt n'étaient pas son sujet, et aucun instrument de détection n'existait alors.",
   "La photographie elle-même n'existait pas encore : une caméra était hors de portée de l'époque.",
   "La température du Soleil est une tout autre question, et elle demande d'autres méthodes."],
  "Une découverte se fait souvent en cherchant autre chose.",
  img=IMG_HERSCHEL),

q("C1.2", "Le délai", "Plus de deux siècles séparent la découverte de l'infrarouge du drone thermique. Ce délai montre que…",
  ["une découverte devient une technique quand une capacité de fabrication ET un besoin la rencontrent",
   "les scientifiques d'autrefois travaillaient lentement",
   "la découverte était inutile",
   "l'usage aurait pu venir tout de suite"],
  "Trois conditions doivent se réunir : savoir que le phénomène existe, savoir fabriquer un "
  "détecteur, et avoir une raison de le faire. Tant qu'il en manque une, la découverte reste sans "
  "usage — et cela n'a rien d'anormal.",
  "Le laser a été qualifié à sa naissance de « solution cherchant un problème ». Il équipe "
  "aujourd'hui les lecteurs, la chirurgie et les télécommunications.",
  "Juger une découverte à sa vitesse d'application, et croire qu'une science utile est une science "
  "rapidement rentable.",
  ["",
   "La lenteur n'est pas en cause : ce sont les moyens de fabrication qui manquaient, pas l'intelligence.",
   "Elle a été extraordinairement féconde — mais des décennies plus tard, ce qui est la règle.",
   "Aucun matériau ni procédé de 1800 ne permettait de fabriquer un détecteur infrarouge exploitable."],
  "Découverte + capacité de fabrication + besoin. Il en manque un, et rien ne se passe.",
  img=IMG_HERSCHEL),

q("C1.2", "L'ordre des étapes", "L'enchaînement observé est…",
  ["découverte scientifique → capacité technique → diffusion → usages nouveaux",
   "besoin → découverte → usage",
   "usage → découverte → technique",
   "il n'y a pas d'ordre"],
  "La découverte vient d'abord et ne vise rien de précis. La capacité de fabrication la rend "
  "exploitable. La baisse des coûts la répand. Et c'est alors seulement que des usages apparaissent "
  "— souvent bien loin de ce que le découvreur imaginait.",
  "Infrarouge (1800) → détecteurs (XXᵉ) → capteurs bon marché (années 2000) → thermomètre sans "
  "contact, caméra thermique, drone de détection.",
  "Croire que toute technique naît d'un besoin exprimé. Beaucoup naissent d'une possibilité "
  "découverte.",
  ["",
   "Ce chemin existe aussi — la recherche appliquée — mais ce n'est pas celui de l'infrarouge : personne n'avait exprimé ce besoin en 1800.",
   "Un usage ne peut pas précéder la découverte du phénomène sur lequel il repose.",
   "L'ordre est très net ici, et il est daté : 1800, XXᵉ siècle, années 2000, aujourd'hui."],
  "Découverte, capacité, diffusion, usages. Dans cet ordre.",
  img=IMG_HERSCHEL),

q("C1.2", "L'effet sur la société", "Un capteur infrarouge devenu bon marché a pour effet…",
  ["de faire entrer une mesure jusque-là réservée aux laboratoires dans des objets ordinaires",
   "de rendre les laboratoires inutiles",
   "de faire baisser la température des objets",
   "de remplacer les thermomètres classiques partout"],
  "C'est l'effet le plus profond de la diffusion : ce n'est pas seulement moins cher, c'est ailleurs "
  "et pour d'autres gens. Un thermomètre sans contact chez un particulier, c'était impensable au "
  "siècle dernier.",
  "Un thermomètre frontal, un détecteur de présence, une caméra thermique de bricolage : trois "
  "objets courants qui reposent sur la découverte de 1800.",
  "Réduire la diffusion d'une technologie à une question de prix. C'est d'abord une question "
  "d'accès.",
  ["",
   "Les laboratoires continuent d'employer des instruments bien plus précis, pour d'autres questions.",
   "Un capteur mesure une température, il ne la modifie pas.",
   "Les thermomètres à contact restent plus précis pour beaucoup d'usages, en particulier médicaux."],
  "La diffusion change qui peut mesurer, pas seulement combien cela coûte."),

q("C1.2", "Ce qu'une découverte ne garantit pas", "Découvrir un phénomène garantit-il un usage utile ?",
  ["non : il faut encore savoir le fabriquer à un coût acceptable, et qu'un besoin existe",
   "oui, tôt ou tard, tout se transforme en application",
   "oui, si la découverte est importante",
   "non, une découverte ne sert jamais directement"],
  "Beaucoup de phénomènes connus n'ont aucun usage courant, faute de moyen de fabrication ou de "
  "raison de le faire. L'histoire retient les découvertes appliquées ; elle oublie les autres, ce "
  "qui donne l'illusion d'une transformation automatique.",
  "L'infrarouge a attendu un siècle et demi avant de servir à quoi que ce soit du quotidien.",
  "Confondre ce dont on entend parler avec ce qui existe. Les découvertes sans application ne font "
  "pas de titres.",
  ["",
   "Rien ne garantit qu'une application apparaisse : certaines découvertes anciennes n'en ont toujours aucune.",
   "L'importance scientifique et l'utilité pratique sont deux choses distinctes, souvent sans rapport.",
   "Certaines découvertes trouvent un usage très vite, quand la capacité de fabrication existe déjà."],
  "Découvrir ne suffit pas. Il faut pouvoir fabriquer, et avoir une raison de le faire."),

q("C1.2", "Mettre en relation", "Mettre en relation une découverte avec ses effets sur la société, c'est…",
  ["montrer le chemin complet : le phénomène, la capacité de fabrication, la diffusion, puis ce qui change pour les gens",
   "citer la date de la découverte",
   "nommer le scientifique",
   "décrire l'appareil actuel"],
  "C'est le geste du code 3e_C1.2, et il est exigeant : il demande de tenir ensemble une histoire "
  "des sciences, une histoire des techniques et une observation sociale. Sauter un maillon rend "
  "l'enchaînement incompréhensible.",
  "Sans l'étape « on sait fabriquer un détecteur », le passage de Herschel au drone paraît "
  "miraculeux.",
  "S'arrêter aux deux bouts — la découverte et l'objet d'aujourd'hui — en laissant le milieu vide.",
  ["",
   "Une date situe, elle n'explique pas : elle ne dit rien de ce qui a permis le passage à l'usage.",
   "Le nom du découvreur appartient à l'histoire des sciences ; il ne décrit aucun effet social.",
   "L'appareil actuel est le point d'arrivée : le décrire ne montre pas le chemin qui y mène."],
  "Le phénomène, la fabrication, la diffusion, les effets. Quatre maillons, aucun facultatif.",
  img=IMG_HERSCHEL),

q("C1.2", "Un effet non prévu", "Que le drone thermique serve aussi à repérer des fuites de chaleur dans les bâtiments montre que…",
  ["une même capacité technique trouve des usages que personne n'avait prévus",
   "les drones sont mal conçus",
   "la détection de feux était un mauvais objectif",
   "les deux usages sont identiques"],
  "Une capacité technique se diffuse latéralement : dès qu'elle existe, d'autres métiers s'en "
  "emparent pour leurs propres questions. C'est ainsi qu'une technologie née dans un domaine "
  "transforme des domaines voisins.",
  "Voir une déperdition de chaleur par le toit d'une maison n'a rien à voir avec les feux de "
  "forêt — et repose exactement sur la même mesure.",
  "Croire qu'une technique reste dans le domaine pour lequel on l'a développée.",
  ["",
   "Rien n'est mal conçu : c'est au contraire le signe d'une capacité générale, donc robuste.",
   "L'objectif initial reste pertinent ; il a simplement ouvert davantage qu'on ne pensait.",
   "Les deux usages emploient la même mesure et répondent à des questions entièrement différentes."],
  "Une capacité technique déborde toujours le besoin qui l'a fait naître."),

# ═══════════ C1.3 — L'incidence d'un OST sur la société (8) ═══════════

q("C1.3", "Le sens de l'incidence", "« Le drone réduit l'exposition des pompiers » est une incidence…",
  ["de l'objet technique SUR la société : l'objet change quelque chose pour des gens",
   "de la société sur l'objet technique",
   "purement technique, sans effet social",
   "sans rapport avec le sujet"],
  "Repérer le sens est le premier geste. Ici, l'objet existe et sa mise en service modifie le "
  "travail, le risque et l'organisation de personnes réelles. La flèche va de l'objet vers la "
  "société.",
  "Avant : on entre dans la zone pour savoir. Après : on sait avant d'entrer. Le métier de pompier "
  "n'est plus tout à fait le même.",
  "Traiter toute phrase sur la technique et la société comme si le sens allait de soi.",
  ["",
   "L'inverse serait : une règle, un budget ou une attente collective qui contraint la conception du drone.",
   "Réduire l'exposition d'êtres humains à un danger est un effet social majeur, pas un détail technique.",
   "C'est au contraire le cœur du code 3e_C1.3 : l'incidence d'un objet technique sur la société."],
  "Demande-toi toujours : qui agit sur qui ? L'objet sur la société, ou l'inverse ?"),

q("C1.3", "Un argumentaire solide", "Un argumentaire court est solide quand…",
  ["chaque affirmation s'appuie sur un fait vérifiable, et qu'il dit ce qu'il laisse de côté",
   "il contient beaucoup d'arguments",
   "il emploie un vocabulaire technique",
   "il se termine par une phrase forte"],
  "Un argumentaire n'est pas un plaidoyer. Ce qui le rend solide, c'est qu'on puisse le vérifier — "
  "donc le contester. Et nommer soi-même ses angles morts est ce qui distingue un raisonnement "
  "d'une publicité.",
  "« Le délai d'alerte diminue » se vérifie. « C'est une technologie d'avenir » ne se vérifie pas.",
  "Multiplier les arguments pour compenser leur faiblesse. Trois arguments vérifiables valent "
  "mieux que dix affirmations.",
  ["",
   "Le nombre ne fait rien à l'affaire : dix arguments invérifiables ne prouvent pas davantage qu'un seul.",
   "Le vocabulaire technique peut même masquer l'absence de preuve derrière une apparence de rigueur.",
   "Une belle formule finale n'ajoute aucune preuve ; elle ajoute de la conviction, ce qui est autre chose."],
  "Vérifiable, et honnête sur ce qu'il ignore. C'est tout."),

q("C1.3", "Les deux faces", "Un argumentaire qui n'énumère que des bénéfices…",
  ["ne prouve rien : on pourrait l'écrire à l'identique pour n'importe quelle solution",
   "est convaincant, puisqu'il est positif",
   "est correct si les bénéfices sont réels",
   "est le format attendu en technologie"],
  "Un raisonnement se reconnaît à ce qu'il aurait pu conclure autrement. S'il ne mentionne aucun "
  "coût, aucun risque, aucune perte, c'est qu'il n'a pas comparé — il a défendu une solution "
  "choisie d'avance.",
  "Fausses alertes à trier, réseau à entretenir, images qui n'existaient pas : trois coûts réels "
  "d'une détection automatisée.",
  "Croire qu'un exposé technique doit être positif pour être professionnel. C'est l'inverse.",
  ["",
   "La conviction n'est pas la preuve : un texte uniquement positif se lit comme un argumentaire commercial.",
   "Des bénéfices réels ne suffisent pas si les coûts, également réels, sont passés sous silence.",
   "Le format attendu, en 3e comme ailleurs, comporte les deux faces — c'est même le sens du mot « peser »."],
  "Un raisonnement qui ne pouvait que conclure ainsi n'est pas un raisonnement."),

q("C1.3", "Un métier qui se transforme", "Que le guetteur devienne exploitant de système est une incidence…",
  ["sociale : elle change des emplois, des formations et des compétences",
   "purement technique",
   "négligeable, puisque le nombre d'emplois est le même",
   "seulement économique"],
  "Les effets sur le travail sont parmi les plus profonds, et les plus lents. Un métier qui se "
  "transforme, ce sont des personnes à former, des recrutements différents, et parfois des "
  "compétences qui perdent leur valeur.",
  "Savoir rester attentif huit heures durant ne se convertit pas en savoir entretenir un réseau de "
  "capteurs.",
  "Compter les emplois sans regarder ce qu'ils demandent. Le nombre peut rester stable pendant que "
  "tout change.",
  ["",
   "Un changement de métier est social avant d'être technique : il concerne des personnes, pas des objets.",
   "Un effectif constant peut cacher un remplacement complet des compétences requises — c'est même fréquent.",
   "L'effet économique existe, mais il ne résume pas ce que vivent les personnes concernées."],
  "Un métier qui change est l'un des effets les plus profonds d'une technique."),

q("C1.3", "Ce qui n'est pas pris en compte", "Terminer un argumentaire par ce qu'il ne prend pas en compte…",
  ["le renforce : cela montre qu'on connaît les limites de son propre raisonnement",
   "l'affaiblit, puisqu'on avoue une lacune",
   "est facultatif",
   "sert seulement à faire plus long"],
  "Un lecteur averti cherchera de toute façon les angles morts. Les nommer d'avance prouve qu'on "
  "les a vus, et déplace la discussion vers ce qui compte vraiment.",
  "« Je ne prends pas en compte le coût réel ni ce qui se passe quand le réseau tombe » : le "
  "lecteur sait désormais où porte l'argument, et où il ne porte pas.",
  "Confondre l'aveu d'une limite avec l'aveu d'une faute.",
  ["",
   "Une lacune reconnue est une lacune maîtrisée ; c'est la lacune cachée qui décrédibilise un texte quand on la découvre.",
   "C'est au contraire ce qui distingue un argumentaire de 3e d'un argumentaire de 5e.",
   "Cette phrase est souvent la plus courte du texte, et la plus utile."],
  "Nommer ses angles morts prouve qu'on les a vus."),

q("C1.3", "Une affirmation vérifiable", "Laquelle de ces phrases s'appuie sur un fait vérifiable ?",
  ["« Au 24 juillet 2026, plus de 50 000 ha avaient brûlé en France depuis le 1ᵉʳ janvier. »",
   "« Les robots sont l'avenir de la lutte contre les feux. »",
   "« Tout le monde sait que la technologie progresse. »",
   "« Il faut absolument équiper tous les massifs. »"],
  "Elle donne une date, un territoire, une grandeur et une unité — et l'on peut remonter à la "
  "source, le ministère de l'Intérieur. Quelqu'un peut la confirmer ou la corriger.",
  "Chaque élément de la phrase peut être contesté séparément : la date, le chiffre, le périmètre.",
  "Prendre pour un fait une affirmation générale à laquelle on adhère.",
  ["",
   "« L'avenir » n'est pas vérifiable aujourd'hui : c'est une prédiction, pas un fait.",
   "« Tout le monde sait » ne désigne aucune source, et ne peut donc être ni vérifié ni contesté.",
   "« Il faut absolument » exprime une volonté, pas une observation."],
  "Un fait vérifiable a une source, une date, un périmètre et une unité."),

q("C1.3", "L'effet sur les habitants", "Une alerte précoce publiée à destination des habitants change…",
  ["ce qu'ils peuvent faire : se préparer, évacuer plus tôt, protéger des biens",
   "rien, puisque ce sont les secours qui interviennent",
   "seulement leur inquiétude",
   "uniquement l'organisation interne des pompiers"],
  "Une information ne vaut que par les décisions qu'elle rend possibles. Prévenir plus tôt ne "
  "change pas le feu ; cela change le temps dont disposent les personnes pour agir.",
  "Une heure d'avance sur un ordre d'évacuation, ce sont des trajets faits sans précipitation et "
  "des routes moins encombrées.",
  "Croire qu'une information destinée au public n'a d'effet que psychologique.",
  ["",
   "Les habitants agissent aussi : ils se déplacent, protègent, signalent, et leurs décisions comptent.",
   "L'inquiétude existe, mais elle n'est pas le seul effet — et une information précise inquiète souvent moins qu'une rumeur.",
   "L'organisation des secours change également, mais la question portait sur les habitants."],
  "Une information vaut par les décisions qu'elle rend possibles."),

q("C1.3", "Ce que l'argumentaire doit relier", "Un argumentaire de 3e sur l'incidence d'un OST doit relier…",
  ["une caractéristique de l'objet à un changement concret pour des personnes identifiées",
   "l'objet à sa technologie",
   "l'objet à son prix",
   "l'objet à son fabricant"],
  "C'est le lien à ne jamais lâcher : d'un côté ce que l'objet fait, de l'autre ce que cela change "
  "pour quelqu'un. Sans le second terme, on décrit une machine ; sans le premier, on énonce une "
  "opinion.",
  "« Le drone voit sous la fumée » (objet) → « les pompiers entrent dans une zone déjà reconnue » "
  "(personnes).",
  "Décrire longuement la technologie, puis conclure par une phrase générale sur la société, sans "
  "rien relier entre les deux.",
  ["",
   "La technologie décrit l'objet à lui-même : elle ne dit pas encore ce que cela change pour quelqu'un.",
   "Le prix est une donnée économique, qui ne devient sociale que si l'on dit qui le paie et ce qu'il renonce à faire.",
   "Le fabricant relève de l'industrie, pas de l'incidence sur la société."],
  "Une caractéristique de l'objet, un changement pour des personnes. Le lien est tout."),

# ═══════════ C1.4 — L'incidence des contraintes sociétales sur les OST (7) ═══════════

q("C1.4", "L'autre sens", "« La réglementation de l'espace aérien limite le vol des drones » est une incidence…",
  ["de la société SUR l'objet technique : une règle collective contraint sa conception et son usage",
   "de l'objet technique sur la société",
   "d'ordre uniquement technique",
   "négligeable"],
  "C'est le sens inverse du précédent, et c'est le code 3e_C1.4. Une décision collective — une loi, "
  "une norme, un budget, une attente — oblige les concepteurs à faire autrement. L'objet porte la "
  "trace de la société qui l'accueille.",
  "Un drone conçu pour un pays où le vol au-dessus des habitations est interdit n'aura pas le même "
  "mode de fonctionnement qu'ailleurs.",
  "Ne voir qu'un seul sens, et croire que la technique s'impose à la société sans réciproque.",
  ["",
   "Ce serait l'inverse : le drone changeant quelque chose pour les gens. Ici, ce sont les gens qui changent le drone.",
   "Une réglementation est une décision collective, donc sociale, même si ses effets sont techniques.",
   "Elle décide de ce qui est constructible et utilisable : c'est tout sauf négligeable."],
  "La société contraint l'objet autant que l'objet change la société.",
  img=IMG_ZONES),

q("C1.4", "Trois natures de contraintes", "Un bon argumentaire sur les contraintes sociétales en cite de natures différentes, par exemple…",
  ["une règle, un moyen, et une attente collective",
   "trois règles différentes",
   "trois contraintes techniques",
   "trois inconvénients de l'objet"],
  "Une contrainte sociétale peut être juridique (une norme), matérielle (un budget public, du "
  "personnel), ou culturelle (ce que les gens acceptent). Les trois pèsent, et elles ne se "
  "négocient pas de la même façon.",
  "Espace aérien (règle) · budget d'une commune (moyen) · refus d'être filmé (attente).",
  "Citer trois fois la même nature de contrainte, et croire qu'on a couvert le sujet.",
  ["",
   "Trois règles restent une seule nature de contrainte : on manque les moyens et les attentes.",
   "Une contrainte technique vient de la physique ou du matériel, pas de la société.",
   "Un inconvénient décrit l'objet ; une contrainte sociétale décrit ce que la société lui impose."],
  "Une règle, un moyen, une attente. Trois natures, trois façons de contraindre."),

q("C1.4", "Ce qu'une contrainte change", "Nommer une contrainte sans dire ce qu'elle change dans l'objet…",
  ["ne prouve rien : c'est l'effet sur la conception qui fait l'argument",
   "suffit, la contrainte parle d'elle-même",
   "est la méthode attendue",
   "vaut mieux qu'un exemple"],
  "Une liste de contraintes est un inventaire. L'argumentaire commence quand on dit : à cause de "
  "celle-ci, l'objet a telle caractéristique qu'il n'aurait pas eue autrement.",
  "« La protection des données » ne dit rien. « La protection des données oblige à limiter la "
  "résolution et la durée de conservation des images » dit tout.",
  "Recopier la liste des contraintes du cours en pensant avoir répondu à la question.",
  ["",
   "Une contrainte citée seule laisse le lecteur deviner l'effet, et il devinera peut-être autre chose.",
   "La méthode attendue est précisément l'inverse : contrainte, puis effet concret sur l'objet.",
   "Un exemple concret est justement ce qui manque à une contrainte nommée toute seule."],
  "Contrainte → effet sur l'objet. Sans le second terme, ce n'est pas un argument.",
  img=IMG_ZONES),

q("C1.4", "Une contrainte de vie privée", "Une caméra tournée vers la forêt filme aussi les chemins. La contrainte qui en découle oblige à…",
  ["décider de la résolution, de la durée de conservation et de qui peut consulter les images",
   "renoncer à toute caméra",
   "prévenir les promeneurs par un panneau, et rien de plus",
   "filmer en noir et blanc"],
  "Une contrainte de protection des données se traduit en décisions de conception mesurables. On "
  "peut concevoir un système qui détecte une chaleur anormale sans permettre d'identifier "
  "quiconque — c'est un choix technique, pris pour une raison sociale.",
  "Une image thermique de faible résolution suffit à repérer un départ de feu, et ne permet de "
  "reconnaître personne.",
  "Traiter la vie privée comme une formalité juridique posée après coup, au lieu d'une exigence de "
  "conception.",
  ["",
   "Renoncer à l'outil n'est pas la seule issue : la question est de le concevoir autrement, pas de l'abandonner.",
   "Informer est nécessaire et insuffisant : cela ne change rien à ce que le système enregistre et conserve.",
   "La couleur n'a aucun rapport avec l'identification : on reconnaît très bien quelqu'un sur une image en noir et blanc."],
  "Une exigence sociale devient une caractéristique technique. C'est cela, concevoir."),

q("C1.4", "Le budget d'une commune", "Un budget public limité oblige surtout à…",
  ["choisir une solution entretenable avec les moyens locaux, ce qui écarte des matériels performants mais irréparables sur place",
   "acheter le moins cher",
   "renoncer au projet",
   "demander une subvention"],
  "Le coût d'achat n'est qu'une partie du problème. Une commune doit aussi pouvoir faire vivre le "
  "système : réparer, remplacer, former quelqu'un. Un matériel excellent mais dont personne ne sait "
  "s'occuper localement devient inutile en un an.",
  "Un capteur bon marché mais réparable par les services techniques tient plus longtemps qu'un "
  "matériel de pointe dont le fabricant est à l'autre bout du monde.",
  "Réduire une contrainte de moyens au prix d'achat, en oubliant le coût de possession.",
  ["",
   "Le moins cher à l'achat est souvent le plus cher à l'usage, s'il tombe en panne et n'est pas réparable.",
   "Renoncer est une issue possible, mais la contrainte oblige d'abord à concevoir autrement.",
   "Une subvention change le montant disponible ; elle ne change pas la question de l'entretien."],
  "Une contrainte de moyens porte sur la durée, pas seulement sur l'achat."),

q("C1.4", "Contrainte ou obstacle", "Les contraintes sociétales sont…",
  ["une partie du cahier des charges, au même titre que la portée ou l'autonomie",
   "des obstacles qui empêchent de bien concevoir",
   "des questions juridiques sans rapport avec la technique",
   "des préoccupations qui viennent après la conception"],
  "Une contrainte n'empêche pas de concevoir : elle définit ce qu'il faut concevoir. Un objet qui "
  "ignorerait les règles, les moyens et les attentes ne serait pas plus libre — il serait "
  "inutilisable.",
  "Un drone qui vole magnifiquement mais qu'aucune autorisation ne permet d'employer n'a aucune "
  "valeur.",
  "Traiter les contraintes sociétales comme des tracasseries ajoutées à la fin, alors qu'elles "
  "orientent les choix dès le début.",
  ["",
   "Elles orientent la conception au lieu de l'empêcher : c'est exactement le rôle d'un cahier des charges.",
   "Elles se traduisent en caractéristiques techniques mesurables — résolution, durée de conservation, mode dégradé.",
   "Les prendre en compte après coup oblige à refaire ; c'est là qu'elles deviennent réellement coûteuses."],
  "Une contrainte ne bloque pas la conception. Elle la définit."),

q("C1.4", "Les deux sens ensemble", "Un argumentaire complet de 3e sur un système technique…",
  ["traite les deux sens : ce que l'objet change pour la société, et ce que la société oblige l'objet à changer",
   "traite le sens le plus important des deux",
   "traite le sens de l'objet vers la société, qui est le seul au programme",
   "n'a pas à choisir : les deux reviennent au même"],
  "Les deux codes — 3e_C1.3 et 3e_C1.4 — décrivent la même relation vue des deux côtés. Les tenir "
  "ensemble, c'est comprendre qu'une technique et une société se façonnent mutuellement, et non "
  "que l'une subit l'autre.",
  "Le drone réduit l'exposition des pompiers (objet → société) ; la réglementation aérienne "
  "l'oblige à prévoir un mode dégradé (société → objet).",
  "Traiter un seul sens et croire le sujet épuisé.",
  ["",
   "Aucun des deux n'est plus important : ce sont deux compétences distinctes du référentiel, toutes deux exigibles.",
   "Les deux figurent au programme de 3e, sous les codes C1.3 et C1.4.",
   "Ils ne reviennent pas au même : dans l'un l'objet agit, dans l'autre il subit — et les faits à citer sont différents."],
  "L'objet change la société ; la société change l'objet. Les deux, toujours.",
  img=IMG_ZONES),
