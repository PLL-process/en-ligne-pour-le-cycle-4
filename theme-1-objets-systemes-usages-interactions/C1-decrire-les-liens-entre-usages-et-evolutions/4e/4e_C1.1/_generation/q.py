# -*- coding: utf-8 -*-
"""Les 30 questions du QCM 4e_C1.1 à C1.3 — Tsinghua, détecter les feux.

Toutes les bonnes réponses sont en position 0 ici : la répartition sur A/B/C/D
est faite ensuite par `_outils/fix_r.js`, de façon déterministe.

Répartition : C1.1 (12) · C1.2 (9) · C1.3 (9).

Les chiffres cités sont ceux du fichier de données du lot, qui sont **publics et
sourcés** — ministère de l'Intérieur, JRC/EFFIS, ADEME Impact CO₂. C'est le seul
QCM du dépôt dans ce cas, et les questions s'appuient dessus sans les arrondir
autrement que ne le fait la séquence.
"""

IMG_EQUIV = {
    "src": "Images/corrige_equivalences_et_perimetres.svg",
    "alt": "Les quatre équivalences calculées à partir de 1,98 MtCO₂, avec pour chacune son "
           "unité exacte — kilomètre de véhicule ou passager-kilomètre — et sa question critique.",
}
IMG_CHAINE = {
    "src": "Images/corrige_du_nombre_a_l_exigence.svg",
    "alt": "La chaîne du raisonnement en cinq étapes, de la donnée publique à l'exigence "
           "vérifiable, avec l'incertitude que chaque étape ajoute et qu'aucune ne retire.",
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


# ═══════════ C1.1 — Mettre en relation les OST avec leurs usages (12) ═══════════

q("C1.1", "Par où l'on commence", "Une équipe qui doit concevoir un système de détection de feux commence par…",
  ["comprendre le besoin : ce que les secours attendent réellement, et dans quelles conditions",
   "choisir un capteur adapté",
   "choisir un microcontrôleur",
   "estimer le prix du système"],
  "Un système technique n'existe pas parce qu'un composant est disponible. Il existe pour répondre "
  "à un besoin identifié dans une situation d'usage. Commencer par le composant, c'est répondre "
  "avant d'avoir écouté la question.",
  "La séquence entière se déroule sans qu'aucun capteur ne soit choisi : ce sera le travail du "
  "Thème 2.",
  "Partir du matériel qu'on connaît déjà, et construire le besoin autour.",
  ["",
   "Choisir un capteur suppose de savoir quelle grandeur mesurer, avec quelle précision et dans quel délai — trois choses qu'on ignore encore.",
   "Le microcontrôleur traite des données qu'on n'a pas encore décidé de produire : le choisir maintenant serait arbitraire.",
   "Le prix se calcule sur une solution ; il n'y a rien à chiffrer tant qu'on ne sait pas ce que le système doit faire."],
  "Un système existe pour un besoin, pas parce qu'un composant existe."),

q("C1.1", "Trois grandeurs, zéro addition", "« 50 000 ha », « 32 feux » et « 50 % » ne s'additionnent pas parce que…",
  ["ce sont trois grandeurs de natures différentes : une surface cumulée, un état instantané, une proportion",
   "les nombres sont trop éloignés les uns des autres",
   "elles viennent de trois sources différentes",
   "le tableur refuserait l'opération"],
  "Additionner suppose la même unité ET le même sens. Ici les trois manquent aux deux conditions. "
  "L'addition produirait un nombre parfaitement calculé et parfaitement dépourvu de signification.",
  "50 000 + 32 + 50 = 50 082. Ce nombre existe, et il ne désigne rien au monde.",
  "Se fier au fait que le calcul « marche ». Une machine calcule ce qu'on lui demande sans savoir "
  "ce que les nombres veulent dire.",
  ["",
   "L'écart entre les valeurs n'a aucune importance : on additionne très bien 3 et 3 000 s'ils désignent la même chose.",
   "Des chiffres de sources différentes s'additionnent parfaitement s'ils mesurent la même grandeur de la même façon.",
   "C'est précisément le danger : le tableur acceptera l'opération sans broncher et affichera un résultat."],
  "On n'additionne que ce qui a la même unité ET le même sens."),

q("C1.1", "Un cumul", "« 50 000 ha brûlés depuis le 1ᵉʳ janvier » est…",
  ["un cumul, annoncé comme un minimum : la surface réelle est au moins celle-là",
   "la surface qui brûle chaque jour",
   "la surface totale des forêts françaises",
   "une estimation calculée par un modèle"],
  "Un cumul ne fait que grandir au fil de l'année. Et le statut « minimum annoncé » signale que le "
  "comptage n'est pas terminé : la valeur définitive sera supérieure, sans qu'on sache de combien.",
  "Le même indicateur, mesuré en octobre, aura nécessairement augmenté — sans qu'aucun feu "
  "nouveau n'ait besoin d'être plus grand.",
  "Lire un cumul comme un instantané, et croire que le chiffre décrit une situation présente.",
  ["",
   "Une surface journalière varierait chaque jour et redescendrait ; un cumul, jamais.",
   "La forêt française couvre plusieurs millions d'hectares : 50 000 en est une fraction très faible.",
   "Cette valeur est un comptage d'observations, non le résultat d'un modèle — la colonne « statut » le précise."],
  "Un cumul grandit toute l'année et ne redescend jamais."),

q("C1.1", "Un état instantané", "« 32 feux en cours » est…",
  ["un état instantané : le nombre à un moment donné, qui aura changé le lendemain",
   "le nombre de feux de l'année",
   "une moyenne journalière",
   "une prévision pour la semaine"],
  "Un état instantané est une photographie. Il peut monter, redescendre, revenir au même chiffre "
  "pour des feux entièrement différents. Le comparer d'un jour à l'autre a du sens ; le cumuler "
  "n'en a aucun.",
  "Trente-deux feux le 24 juillet et trente-deux le 25 ne font pas soixante-quatre feux : ce sont "
  "peut-être les mêmes.",
  "Additionner des états instantanés successifs, et compter plusieurs fois le même phénomène.",
  ["",
   "Le nombre annuel serait bien plus élevé et n'aurait pas la même signification : il compterait chaque départ, éteint ou non.",
   "Une moyenne suppose un calcul sur plusieurs jours ; ici la valeur est relevée à un instant.",
   "Rien n'est prédit : la donnée décrit ce qui est observé au moment de l'annonce."],
  "Un état instantané se compare, il ne se cumule pas."),

q("C1.1", "Une proportion", "« 50 % des départs de feu sont liés à une imprudence » n'a de sens que si l'on sait…",
  ["de quel ensemble c'est la part : ici, l'ensemble des départs de feu en France",
   "combien de feux cela représente exactement",
   "quelle est la surface concernée",
   "quel jour la mesure a été faite"],
  "Un pourcentage est une part. Sans son ensemble de référence, il flotte : 50 % de quoi, sur "
  "quel territoire, sur quelle période ? C'est cet ensemble qui donne au chiffre sa portée — et "
  "qui interdit de l'additionner à des hectares.",
  "« 50 % des départs » et « 50 % des surfaces brûlées » seraient deux affirmations très "
  "différentes, et la seconde serait bien plus grave.",
  "Retenir le pourcentage et oublier son ensemble, ce qui arrive dès qu'on le recopie sans sa phrase.",
  ["",
   "Le nombre absolu serait une information supplémentaire utile, mais la proportion garde son sens sans lui, pourvu qu'on sache de quoi elle est la part.",
   "La surface est une autre grandeur : elle ne dit rien de la part des départs dus à une imprudence.",
   "La date situe la donnée, mais ne dit toujours pas de quel ensemble le pourcentage est la part."],
  "Un pourcentage sans son ensemble de référence ne veut rien dire."),

q("C1.1", "À quoi sert la colonne « statut »", "Dans le fichier, la colonne `statut` porte « minimum_annonce », « instantane », « estimation_modelee ». Elle sert à…",
  ["dire de quelle NATURE est chaque chiffre — c'est elle qui empêche les additions absurdes",
   "indiquer la date de la mesure",
   "classer les lignes par ordre d'importance",
   "signaler les erreurs du fichier"],
  "C'est la colonne la plus précieuse du fichier, et celle qu'on regarde le moins. Elle transporte "
  "ce qu'un nombre seul ne peut pas dire : comment il a été obtenu, et donc ce qu'on a le droit "
  "d'en faire.",
  "Deux nombres dans la même colonne « valeur » — 50 000 et 20 — n'autorisent pas les mêmes "
  "opérations, et seule la colonne « statut » permet de le savoir.",
  "Supprimer les colonnes « qui ne contiennent pas de chiffres » pour alléger le tableau.",
  ["",
   "La date figure dans sa propre colonne ; le statut ne dit pas quand, il dit comment.",
   "Aucun ordre d'importance n'est établi : les trois statuts sont également légitimes, ils décrivent des choses différentes.",
   "Aucune des lignes n'est erronée : le statut décrit une méthode d'obtention, pas un défaut."],
  "La colonne « statut » dit ce qu'on a le droit de faire avec le nombre."),

q("C1.1", "Pourquoi citer la source", "La colonne `source` est indispensable parce que…",
  ["un chiffre sans source ne peut être ni vérifié ni discuté",
   "cela fait plus sérieux",
   "c'est obligatoire dans un fichier CSV",
   "cela permet de trier les lignes plus facilement"],
  "Citer la source, ce n'est pas une politesse académique : c'est ce qui rend un chiffre "
  "contestable. Un nombre qu'on ne peut pas remonter jusqu'à son producteur ne peut être ni "
  "confirmé ni réfuté — il ne peut qu'être cru.",
  "« 504 002 ha en 2023 » vient du JRC/EFFIS, service de la Commission européenne : n'importe qui "
  "peut aller vérifier, et constater les mises à jour.",
  "Recopier un chiffre trouvé en ligne sans noter d'où il vient. Une semaine plus tard, personne "
  "ne peut plus le retrouver.",
  ["",
   "L'apparence n'entre pas en jeu : un fichier peut paraître très sérieux et ne contenir que des chiffres invérifiables.",
   "Le format CSV n'impose aucune colonne : c'est une convention de travail, pas une règle technique.",
   "Le tri se ferait tout aussi bien sur n'importe quelle autre colonne."],
  "Un chiffre sans source ne se discute pas. Il se croit ou il se rejette."),

q("C1.1", "Ce qu'un seuil seul produit", "Un système qui déclencherait l'alerte au-dessus de 40 °C, dans une cour où l'écart ombre/soleil dépasse 10 °C…",
  ["se déclencherait tous les jours d'été, sans le moindre feu",
   "ne se déclencherait jamais",
   "fonctionnerait correctement",
   "ne fonctionnerait que la nuit"],
  "C'est la raison pour laquelle la séquence commence par une mesure dans la cour. Un capteur "
  "unique confond la cause qu'on cherche avec toutes celles qui produisent le même effet — et le "
  "soleil sur du bitume produit exactement le même effet qu'un début d'incendie sur un thermomètre.",
  "Relevé réel dans une cour : 29,4 °C à l'ombre, 41,8 °C au soleil, au même instant.",
  "Fixer un seuil à partir de la valeur qu'atteint un feu, sans regarder ce que la vie ordinaire "
  "atteint déjà.",
  ["",
   "Il se déclencherait au contraire très souvent : 41,8 °C au soleil dépasse largement le seuil.",
   "Il ferait exactement ce qu'on lui a demandé — et c'est le problème : ce qu'on lui a demandé est mal posé.",
   "La nuit est justement le moment où il ne se déclencherait pas, faute de soleil."],
  "Un capteur unique ne distingue pas la cause qu'on cherche des autres qui font le même effet."),

q("C1.1", "Croiser les indices", "Pour limiter les fausses alertes, la solution est de…",
  ["croiser plusieurs indices indépendants avant de confirmer",
   "augmenter le seuil de température",
   "vérifier moins souvent",
   "installer davantage de capteurs du même type"],
  "Deux indices indépendants se trompent rarement ensemble. La température seule monte au soleil ; "
  "les particules seules montent quand une voiture passe ; les deux ensemble, au même endroit, au "
  "même moment, sont beaucoup plus difficiles à expliquer autrement que par un feu.",
  "Température ET particules de fumée ET absence de pluie : trois conditions dont la rencontre "
  "fortuite est rare.",
  "Croire qu'un capteur plus précis résout le problème. Le défaut n'est pas la précision, c'est "
  "l'ambiguïté.",
  ["",
   "Un seuil plus haut réduit les fausses alertes et fait manquer les vrais départs : on déplace l'erreur, on ne la supprime pas.",
   "Vérifier moins souvent revient à détecter plus tard, ce qui est exactement l'inverse du besoin.",
   "Multiplier les capteurs identiques multiplie aussi les fausses alertes : ils se trompent tous de la même façon, pour la même raison."],
  "Deux indices indépendants se trompent rarement ensemble."),

q("C1.1", "L'absence de donnée", "« Aucune alerte reçue » prouve qu'il n'y a pas de feu ?",
  ["non : un capteur en panne, déchargé ou hors de portée ne transmet rien non plus",
   "oui, si le système fonctionne",
   "oui, la nuit seulement",
   "cela ne concerne pas la conception du système"],
  "Le silence a deux causes possibles, et elles sont indiscernables de loin : rien à signaler, ou "
  "plus personne pour signaler. Un système sérieux distingue les deux — en envoyant régulièrement "
  "un signe de vie même lorsqu'il n'a rien à dire.",
  "Un capteur qui émet « je vais bien » toutes les heures permet de savoir, au bout de deux "
  "heures de silence, qu'il faut aller voir.",
  "Interpréter l'absence de signal comme une bonne nouvelle.",
  ["",
   "C'est précisément ce qu'on ne peut pas savoir à distance : un système en panne ressemble en tout point à un système qui n'a rien à signaler.",
   "L'heure ne change rien : une batterie se vide de jour comme de nuit.",
   "C'est au contraire une exigence de conception majeure : elle décide de la façon dont le système doit se signaler."],
  "Le silence d'un capteur n'est pas une preuve. C'est une question."),

q("C1.1", "Du besoin à l'information", "« Détecter tôt » exige d'abord de savoir…",
  ["quelles grandeurs mesurer, et à quelle fréquence",
   "quel microcontrôleur employer",
   "combien coûtera le système",
   "qui financera le projet"],
  "Entre un besoin exprimé en français — « détecter tôt » — et un objet technique, il y a une "
  "étape : dire quelles informations sont nécessaires. C'est elle qui commande tout le reste, y "
  "compris le choix des composants du Thème 2.",
  "« Détecter tôt » → température, fumée, image, vent → « quelle fréquence de mesure ? » → et "
  "seulement ensuite, quel capteur.",
  "Sauter l'étape de l'information et passer directement du besoin au matériel.",
  ["",
   "Le microcontrôleur traite des informations : le choisir avant de savoir lesquelles est prématuré.",
   "Le coût dépend des choix techniques, qui dépendent eux-mêmes des informations nécessaires.",
   "Le financement est une question réelle, mais elle ne dit rien de ce que le système doit mesurer."],
  "Entre le besoin et l'objet, il y a l'information nécessaire."),

q("C1.1", "Ce que la séquence ne fait pas", "À la fin de cette séquence, on n'a toujours pas…",
  ["choisi le moindre composant — c'est le travail du Thème 2",
   "compris le besoin",
   "écrit d'exigences",
   "regardé de données"],
  "C'est volontaire, et c'est la marque d'une bonne analyse externe : on sait ce que le système "
  "doit faire et comment on le vérifiera, sans avoir décidé avec quoi. L'espace des solutions "
  "reste entier.",
  "Cinq exigences vérifiables sont écrites, et pas un seul capteur n'est nommé.",
  "Vouloir « finir » en choisissant un composant, et fermer ainsi la comparaison avant de l'avoir "
  "faite.",
  ["",
   "Le besoin est au contraire l'objet même de la séquence, et il est établi dès la première séance.",
   "Cinq exigences vérifiables sont rédigées en séance 4 : c'est la production principale du lot.",
   "Les données publiques sont lues, triées et exploitées pendant trois séances."],
  "Savoir ce qu'il faut obtenir sans avoir choisi avec quoi : c'est cela, l'analyse externe.",
  img=IMG_CHAINE),

# ═══════════ C1.2 — Avantages et inconvénients des évolutions (9) ═══════════

q("C1.2", "Un proxy", "Le ratio 20 000 000 ÷ 504 002 ≈ 39,68 tCO₂/ha est…",
  ["un proxy : une valeur empruntée à un autre contexte, faute de mieux",
   "une mesure faite en France en 2026",
   "une valeur officielle applicable partout",
   "une constante physique"],
  "Un proxy est un remplaçant assumé. On n'a pas la valeur qu'il faudrait, on en prend une "
  "voisine, et l'on dit qu'on l'a fait. C'est parfaitement légitime — à condition que la dernière "
  "partie ne soit pas oubliée.",
  "Le ratio vient de l'Union européenne en 2023 ; on l'applique à la France en 2026. Deux "
  "territoires, deux années, d'autres végétations.",
  "Employer un proxy et n'en parler à personne. Le résultat devient alors une affirmation.",
  ["",
   "Aucune mesure de ce type n'a été faite en France en 2026 : c'est justement pour cela qu'on emprunte.",
   "Aucune valeur officielle n'autorise à transposer un ratio d'un territoire à un autre sans précaution.",
   "Une constante physique ne dépend ni de l'année ni du lieu ; celle-ci dépend des deux."],
  "Un proxy est légitime. Un proxy tu, ne l'est plus."),

q("C1.2", "L'ordre de grandeur", "Appliqué à 50 000 ha, ce ratio donne environ…",
  ["1,98 million de tonnes de CO₂",
   "39,68 millions de tonnes",
   "504 002 tonnes",
   "20 millions de tonnes"],
  "50 000 × 39,68 ≈ 1 984 000, soit près de deux millions de tonnes. L'intérêt de ce calcul n'est "
  "pas le chiffre exact : c'est de savoir si l'on parle de milliers ou de millions.",
  "Se tromper d'un facteur mille sur un ordre de grandeur change complètement la conversation "
  "qu'on peut avoir avec un décideur.",
  "Recopier un des nombres de l'énoncé au lieu de faire l'opération.",
  ["",
   "39,68 millions serait le résultat d'une multiplication par un million, non par 50 000.",
   "504 002 est la surface européenne brûlée en 2023, exprimée en hectares : ce n'est pas un résultat.",
   "20 millions de tonnes est l'estimation européenne de départ, celle qu'on a utilisée pour bâtir le ratio."],
  "Une estimation sert d'abord à connaître l'ordre de grandeur."),

q("C1.2", "Ce que l'estimation ignore", "Cette estimation ne tient pas compte…",
  ["du type de végétation, de l'humidité, de la sévérité du feu et de la biomasse réellement consumée",
   "de rien : le calcul est complet",
   "uniquement de la date",
   "uniquement du nombre de feux"],
  "Un hectare de garrigue et un hectare de forêt dense ne libèrent pas la même quantité de "
  "carbone, à surface égale. Le ratio moyen écrase toutes ces différences — c'est ce qui le rend "
  "utilisable, et c'est ce qui le rend approximatif.",
  "Un feu de sous-bois qui court vite consume peu de biomasse ; un feu de cimes en consume "
  "énormément. La surface brûlée est pourtant la même.",
  "Présenter une estimation comme si le calcul avait tout pris en compte.",
  ["",
   "Le calcul est arithmétiquement juste et physiquement très incomplet : les deux choses sont compatibles.",
   "La date est un facteur parmi d'autres, et pas le plus important ici.",
   "Le nombre de feux n'entre pas dans le calcul, qui ne porte que sur des surfaces."],
  "Un ratio moyen écrase les différences. C'est son utilité et sa limite."),

q("C1.2", "Une estimation présentée comme une mesure", "Écrire « les feux français ont émis 1,98 MtCO₂ en 2026 » serait…",
  ["malhonnête : c'est un ordre de grandeur emprunté à un autre territoire et une autre année",
   "acceptable, puisque le calcul est juste",
   "acceptable si l'on cite la source",
   "sans importance, c'est un exercice"],
  "La phrase est fausse non par son chiffre mais par son statut : elle affirme au lieu d'estimer. "
  "Et un chiffre voyage toujours seul — détaché de sa page, il devient une donnée que d'autres "
  "citeront.",
  "Le même nombre écrit « estimation par proxy européen 2023, non officielle » est parfaitement "
  "honnête.",
  "Retirer l'avertissement au moment de faire un joli graphique ou une diapositive.",
  ["",
   "Un calcul juste sur des hypothèses empruntées ne produit pas une mesure : il produit une estimation, et la nuance est tout le sujet.",
   "Citer la source du ratio ne suffit pas : il faut dire que le ratio vient d'ailleurs et qu'on l'a transposé.",
   "L'exercice apprend précisément à ne pas faire cela ; s'en dispenser dans un exercice, c'est apprendre l'inverse."],
  "Une estimation sans avertissement devient une affirmation. C'est là qu'elle devient fausse."),

q("C1.2", "Véhicule ou passager", "Comparer directement 0,142 kgCO₂e/km (voiture) et 0,00293 kgCO₂e/passager-km (TGV)…",
  ["est un piège : l'un compte un véhicule, l'autre une personne — les périmètres diffèrent",
   "est correct, ce sont deux moyens de transport",
   "est correct si l'on arrondit",
   "est impossible à calculer"],
  "Le facteur voiture porte sur un véhicule, quel que soit le nombre de personnes à bord. Le "
  "facteur TGV porte sur une personne. Les mettre côte à côte sans le dire fait apparaître un "
  "rapport de un à cinquante qui n'existe pas sous cette forme.",
  "Une voiture avec quatre passagers émet, par personne, quatre fois moins que la même voiture "
  "avec un seul conducteur — et le facteur ne le dit pas.",
  "Aligner des facteurs d'émission dans un tableau sans recopier leurs unités.",
  ["",
   "Le fait que ce soient deux transports ne suffit pas : encore faut-il compter la même chose des deux côtés.",
   "L'arrondi ne corrige pas une différence d'unité : il la rend seulement moins visible.",
   "Le calcul est très facile — c'est son interprétation qui est piégée."],
  "Recopie toujours l'unité du facteur. C'est elle qui dit ce qu'on compte.",
  img=IMG_EQUIV),

q("C1.2", "Le mot du titre", "Le titre du graphique doit contenir…",
  ["« équivalences » — et surtout pas « mêmes impacts »",
   "« mêmes impacts »",
   "« comparaison exacte »",
   "« pollution »"],
  "Une équivalence porte sur une seule grandeur : la quantité de CO₂. Elle ne dit rien de la "
  "durée, des effets locaux, de la réversibilité, ni de ce qui brûle avec la forêt. Le titre doit "
  "donc annoncer ce qu'il compare, et rien de plus.",
  "Un feu détruit aussi un écosystème, des habitations parfois, et il relâche son carbone en "
  "quelques heures. Un trajet en voiture ne fait rien de tout cela.",
  "Choisir un titre qui en dit plus que le calcul — c'est ainsi qu'on trompe sans mentir.",
  ["",
   "« Mêmes impacts » affirme une identité que le calcul ne démontre pas : seule la quantité de CO₂ a été comparée.",
   "« Comparaison exacte » laisse croire à une précision que des facteurs moyens ne permettent pas.",
   "« Pollution » désigne un ensemble beaucoup plus large que les émissions de CO₂, et introduit une confusion supplémentaire."],
  "Un titre ne doit jamais promettre plus que ce que le calcul a établi.",
  img=IMG_EQUIV),

q("C1.2", "Ce qu'une équivalence dit", "« Autant que 14 milliards de km en voiture » signifie…",
  ["que les quantités de CO₂ sont du même ordre — pas que les deux phénomènes se ressemblent",
   "que les feux et la voiture ont le même effet sur l'environnement",
   "qu'il faudrait interdire la voiture",
   "que les feux ne sont pas si graves"],
  "Une équivalence est un traducteur d'échelle. Elle sert à rendre une mégatonne imaginable par "
  "quelqu'un qui n'en a aucune représentation. Elle ne dit rien de la nature des phénomènes "
  "comparés.",
  "On pourrait dire aussi bien « autant que 399 millions de repas avec du bœuf » : ni le repas ni "
  "la voiture ne ressemblent à un feu de forêt.",
  "Passer de « même quantité de CO₂ » à « même chose », en une phrase.",
  ["",
   "Les effets diffèrent profondément : durée, destruction d'habitats, fumées, réversibilité. Seule la quantité de CO₂ est comparable.",
   "Aucune décision politique ne découle mécaniquement d'une équivalence : elle informe, elle ne tranche pas.",
   "L'équivalence ne minimise rien ; elle donne une échelle, et 14 milliards de kilomètres est un chiffre considérable."],
  "Une équivalence traduit une échelle. Elle ne rend pas les choses semblables."),

q("C1.2", "L'équivalence retournée", "On peut décrire 1,98 MtCO₂ comme « 399 millions de repas » ou comme « environ 0,5 % des émissions annuelles françaises ». Ces deux phrases…",
  ["sont exactes toutes les deux, et n'orientent pas du tout la même conclusion",
   "ne peuvent pas être exactes en même temps",
   "disent la même chose",
   "sont fausses toutes les deux"],
  "Le choix du terme de comparaison fait la moitié du travail d'argumentation, avant même qu'on "
  "ait discuté. C'est pourquoi lire une équivalence, c'est toujours demander : pourquoi celle-là "
  "plutôt qu'une autre ?",
  "Le même chiffre paraît colossal ramené à des repas, et minuscule ramené au total national.",
  "Choisir l'équivalence qui va dans le sens de ce qu'on veut démontrer, et la présenter comme "
  "neutre.",
  ["",
   "Elles peuvent parfaitement l'être : ce sont deux divisions différentes du même nombre, toutes deux correctes.",
   "Elles disent la même quantité et produisent des impressions opposées — c'est exactement le problème.",
   "Les deux calculs sont justes ; c'est leur usage rhétorique qui demande de la vigilance."],
  "Une équivalence n'est jamais neutre. Demande toujours : pourquoi celle-là ?"),

q("C1.2", "Les deux faces", "La détection automatisée des feux apporte…",
  ["des avantages ET des inconvénients, qu'il faut nommer tous les deux",
   "uniquement des avantages, sinon on ne l'adopterait pas",
   "uniquement des inconvénients",
   "ni l'un ni l'autre : c'est un outil neutre"],
  "C'est le cœur du code C1.2. Toute évolution technique se paie : ici, un gain de temps contre "
  "des fausses alertes, un coût, une consommation d'énergie, et des caméras qui regardent aussi "
  "ce qui n'est pas la forêt.",
  "Un système qui alerte en dix minutes au lieu de deux heures sauve des hectares — et filme, "
  "peut-être, des promeneurs.",
  "N'énumérer que les bénéfices, parce que c'est ce qu'on attend d'un exposé technique.",
  ["",
   "On adopte souvent des techniques dont les inconvénients sont réels et jugés acceptables : les nommer ne les condamne pas.",
   "Les avantages sont considérables : la détection précoce est le principal levier contre les grands feux.",
   "Aucune technique n'est neutre : elle change ce qu'on peut faire, donc ce qu'on fait, donc ce qu'on surveille."],
  "Toute évolution technique se paie. Nommer le prix n'est pas la condamner."),

# ═══════════ C1.3 — Justifier l'évolution d'un OST (9) ═══════════

q("C1.3", "Une exigence vérifiable", "Une exigence vérifiable se reconnaît à ce qu'elle…",
  ["peut être contrôlée par une mesure ou un test qui répond par oui ou par non",
   "est écrite en termes techniques",
   "contient toujours un nombre",
   "désigne le composant à utiliser"],
  "Le test est simple : « comment je vérifie ? ». Si l'on ne sait pas répondre, ce n'est pas une "
  "exigence, c'est un souhait. Un critère par oui ou non suffit parfaitement — le chiffre n'est "
  "pas obligatoire.",
  "« Le système doit permettre à un opérateur d'annuler une alerte » se vérifie sans aucun "
  "chiffre : on essaie, et l'on voit.",
  "Écrire des intentions — « le système doit être fiable » — qu'aucun essai ne peut trancher.",
  ["",
   "Le vocabulaire technique ne rend rien vérifiable : on peut écrire une phrase très technique et totalement incontrôlable.",
   "Beaucoup d'exigences excellentes n'ont pas de nombre : ce qui compte est l'existence d'un test, pas la présence d'un chiffre.",
   "Désigner un composant, c'est écrire une solution : l'exigence dit ce qu'il faut obtenir, pas avec quoi."],
  "Une exigence se reconnaît à ce qu'on sait comment la vérifier."),

q("C1.3", "Exigence ou solution", "« Installer une caméra thermique » est…",
  ["une solution, pas une exigence : elle désigne déjà le moyen",
   "une exigence vérifiable",
   "une contrainte réglementaire",
   "un besoin"],
  "Écrire la solution dans le cahier des charges ferme la comparaison avant qu'elle ait lieu. "
  "L'exigence correspondante serait : « le système doit détecter une élévation anormale de "
  "température à 200 m » — et là, plusieurs solutions redeviennent possibles.",
  "La même exigence peut être remplie par une caméra thermique, un réseau de capteurs au sol ou "
  "un satellite. Nommer la caméra élimine les deux autres sans les avoir examinées.",
  "Écrire les solutions qu'on a en tête à la place des exigences, parce qu'elles sont plus "
  "faciles à formuler.",
  ["",
   "Elle est vérifiable — on voit bien si la caméra est installée — mais elle ne dit pas ce que le système doit obtenir, seulement ce qu'on doit acheter.",
   "Aucune réglementation n'impose de caméra thermique : c'est un choix technique, pas une obligation.",
   "Un besoin s'exprime du point de vue de l'usage — « détecter tôt » — et non par un matériel."],
  "L'exigence dit ce qu'il faut obtenir. La solution dit avec quoi. Ne les échange pas."),

q("C1.3", "L'ordre des étapes", "L'ordre correct est…",
  ["besoin → information nécessaire → contrainte → exigence vérifiable → (Thème 2) solution",
   "solution → exigence → besoin",
   "exigence → besoin → information",
   "l'ordre n'a pas d'importance"],
  "Chaque étape restreint la suivante sans la déterminer. C'est ce qui laisse un espace de "
  "conception : plusieurs solutions peuvent satisfaire les mêmes exigences, et c'est là qu'on "
  "pourra comparer.",
  "« Détecter tôt » → température et fumée → délai maximal → « signaler en moins de 10 min » → "
  "et seulement ensuite, avec quoi.",
  "Commencer par la solution qu'on connaît, puis rédiger des exigences taillées pour elle.",
  ["",
   "Partir de la solution revient à écrire un cahier des charges sur mesure pour un produit déjà choisi : plus rien n'est comparé.",
   "Une exigence ne peut pas précéder le besoin dont elle découle : on ne saurait pas ce qu'on exige, ni pourquoi.",
   "L'ordre est décisif : c'est lui qui garde ouvert l'espace des solutions jusqu'au moment de choisir."],
  "Chaque étape restreint la suivante sans la choisir. C'est là qu'est la conception.",
  img=IMG_CHAINE),

q("C1.3", "Justifier une évolution", "Justifier l'évolution d'un système de détection, c'est dire…",
  ["de quel besoin nouveau ou mal satisfait elle procède",
   "quelle technologie récente elle emploie",
   "combien elle a coûté",
   "en quelle année elle est apparue"],
  "C'est exactement le code 4e_C1.3. Une évolution ne se justifie pas par sa nouveauté mais par "
  "le besoin qu'elle sert mieux que la version précédente. Sinon on décrit un changement, on ne "
  "l'explique pas.",
  "On est passé du guet humain en tour de surveillance à la détection automatique parce que la "
  "surveillance continue de milliers d'hectares dépasse ce qu'une personne peut tenir.",
  "Confondre « c'est plus moderne » avec « c'est justifié ».",
  ["",
   "La technologie employée décrit le moyen, pas la raison : une technologie récente peut répondre à un besoin inexistant.",
   "Le coût est une conséquence du choix, pas sa justification.",
   "La date situe l'évolution sans expliquer pourquoi elle a eu lieu."],
  "Une évolution se justifie par un besoin, jamais par sa nouveauté."),

q("C1.3", "Le garde-fou humain", "Pourquoi le système ne doit-il pas décider seul de déclencher les secours ?",
  ["parce qu'une alerte automatique doit pouvoir être vérifiée par un opérateur avant d'engager des moyens réels",
   "parce que les machines sont toujours moins fiables que les humains",
   "parce que c'est interdit par la loi",
   "parce que cela coûterait moins cher"],
  "Une alerte engage des camions, des équipages et parfois des vies. La décision d'engager reste "
  "humaine — non parce que la machine serait mauvaise, mais parce que la responsabilité, elle, ne "
  "s'automatise pas.",
  "Le système propose, l'opérateur dispose : c'est une exigence de conception, à écrire au même "
  "titre que le délai de détection.",
  "Traiter la validation humaine comme une politesse ajoutée à la fin, au lieu d'une exigence à "
  "part entière.",
  ["",
   "Ce n'est pas une question de fiabilité comparée : sur la détection de motifs, une machine peut être meilleure qu'un humain fatigué.",
   "Aucune interdiction générale n'existe ; c'est un choix de conception, qu'il faut justifier et non subir.",
   "Le coût n'est pas l'argument : une vérification humaine coûte plutôt davantage."],
  "Le système propose. Un humain décide. Et cela s'écrit dans les exigences."),

q("C1.3", "Une exigence bien formée", "Laquelle de ces phrases est une exigence vérifiable ?",
  ["« Le système doit transmettre une alerte horodatée en moins de 30 secondes après confirmation par deux indices indépendants. »",
   "« Le système doit être performant et moderne. »",
   "« Le système doit utiliser une liaison LoRa. »",
   "« Le système doit plaire aux pompiers. »"],
  "Elle dit ce qu'il faut obtenir, avec un délai mesurable et une condition contrôlable, et elle "
  "ne nomme aucun composant. On peut la vérifier par un essai, et plusieurs solutions techniques "
  "peuvent la satisfaire.",
  "Un chronomètre et deux capteurs suffisent à dire si elle est tenue ou non.",
  "Confondre longueur et précision : une phrase longue n'est pas forcément vérifiable.",
  ["",
   "« Performant » et « moderne » ne se mesurent pas : aucun essai ne peut dire si l'exigence est tenue.",
   "LoRa est une technologie précise : cette phrase est une solution déguisée en exigence.",
   "« Plaire » ne se contrôle pas ; on pourrait en revanche exiger qu'un utilisateur réussisse une tâche donnée en moins d'un temps donné."],
  "Un délai mesurable, une condition contrôlable, aucun composant nommé."),

q("C1.3", "Ce qui prépare le Thème 2", "Les exigences écrites en séance 4 servent ensuite à…",
  ["choisir et comparer des solutions techniques, puis à valider celle qui sera retenue",
   "commander le matériel",
   "rédiger le rapport de stage",
   "rien : l'exercice s'arrête là"],
  "Le cahier des charges n'est pas un devoir qu'on rend : c'est le référentiel qui servira à "
  "trancher entre les solutions, puis à vérifier que celle qu'on a construite fait bien ce qu'on "
  "attendait. C'est la boucle de l'analyse technique.",
  "« Signaler en moins de 10 minutes » permettra d'éliminer une solution qui met une heure — sans "
  "avoir à discuter des goûts de chacun.",
  "Traiter le cahier des charges comme une formalité administrative de début de projet.",
  ["",
   "On ne commande rien tant qu'on n'a pas comparé les solutions possibles, ce qui est le travail du Thème 2.",
   "Le rapport documente le travail ; il n'est pas ce à quoi servent les exigences.",
   "C'est au contraire le point de départ de tout le reste du cycle."],
  "Les exigences serviront deux fois : pour choisir, puis pour valider.",
  img=IMG_CHAINE),

q("C1.3", "L'incertitude se transmet", "Dans la chaîne donnée → proxy → estimation → équivalence → exigence, chaque étape…",
  ["ajoute une incertitude, et aucune ne la retire",
   "corrige l'incertitude de la précédente",
   "n'ajoute rien tant que le calcul est juste",
   "supprime l'incertitude au moment de l'arrondi"],
  "L'incertitude ne se dissipe pas en avançant : elle s'accumule. C'est pourquoi la dernière "
  "ligne — l'exigence — doit porter la mémoire de tout ce qui l'a précédée. Une exigence écrite "
  "sans savoir d'où viennent les chiffres est indéfendable.",
  "Le minimum annoncé, puis le proxy d'un autre pays, puis le ratio moyen, puis le choix de "
  "l'équivalence : quatre approximations empilées avant la première exigence.",
  "Croire qu'un calcul exact sur des données approximatives produit un résultat exact.",
  ["",
   "Aucune étape ne corrige la précédente : elles s'appuient dessus, donc elles en héritent.",
   "La justesse du calcul et la fiabilité des données sont deux questions distinctes : on peut calculer parfaitement sur du sable.",
   "Arrondir ne réduit pas l'incertitude : cela la rend seulement moins visible."],
  "L'incertitude s'accumule. La dernière ligne doit la porter.",
  img=IMG_CHAINE),

q("C1.3", "Ce qu'on transmet au Thème 2", "Ce que cette séquence transmet au Thème 2, c'est…",
  ["des questions ouvertes — comment acquérir, traiter, communiquer, alimenter — et des exigences à respecter",
   "une liste de composants à acheter",
   "un programme informatique",
   "un schéma électrique"],
  "L'analyse externe s'arrête au seuil du « comment ». Elle transmet des questions bien posées, "
  "et des exigences qui serviront à juger les réponses. C'est précisément ce qui rend le Thème 2 "
  "intéressant : il reste quelque chose à chercher.",
  "« Comment acquérir la température ? » est une question du Thème 2 ; « le système doit détecter "
  "en moins de 10 minutes » est l'exigence qui permettra de juger la réponse.",
  "Vouloir tout résoudre dans la première séquence, et n'avoir plus rien à étudier ensuite.",
  ["",
   "Aucun composant n'est choisi : ce serait répondre aux questions avant de les avoir posées.",
   "Il n'y a pas encore de programme, puisqu'on ne sait ni quelles grandeurs seront acquises ni comment elles seront traitées.",
   "Un schéma électrique suppose des composants choisis : c'est plusieurs étapes plus loin."],
  "On transmet des questions bien posées et des exigences pour juger les réponses."),
