# -*- coding: utf-8 -*-
"""Les 30 questions du QCM 3e_C2.1 — Pékin, la borne de tickets du métro.

Écrites à la main. Toutes les bonnes réponses sont en position 0 ici : la
répartition sur A/B/C/D est faite ensuite par `_outils/fix_r.js`, de façon
déterministe, à partir d'une graine.

La séquence ne porte qu'un code : les 30 questions sont donc réparties par
THÈME plutôt que par compétence — le chiffre agrégé (8), les six modes et leur
vocabulaire (10), le choix et sa justification (7), l'algorigramme (5).

Règle tenue pour chaque distracteur : la réfutation EXPLIQUE pourquoi la
réponse est fausse.
"""

IMG_MODES = {
    "src": "Images/six_modes_de_representation.svg",
    "alt": "Tableau des six modes de représentation — parcours utilisateur, algorigramme, "
           "graphique, carte d'empathie, storyboard, tableau comparatif — avec pour chacun ce "
           "qu'il montre et son angle mort.",
}
IMG_DEST = {
    "src": "Images/trois_destinataires.svg",
    "alt": "Les trois destinataires du même constat : le technicien, l'élue qui vote le budget, "
           "et l'usager debout dans la station, avec pour chacun ce qu'il peut faire, le temps "
           "dont il dispose et ce qu'il ne supporte pas.",
}
IMG_C3 = {
    "src": "Images/corrige_trois_representations.svg",
    "alt": "Le même constat rendu en algorigramme pour le technicien, en graphique du taux "
           "d'abandon par profil pour l'élue, et en storyboard de trois vignettes pour l'usager.",
}
IMG_C3B = {
    "src": "Images/corrige_trois_autres_modes.svg",
    "alt": "Le même constat rendu en parcours utilisateur avec les abandons par étape, en carte "
           "d'empathie de Mme Liu, et en tableau comparatif de quatre pistes croisées avec le "
           "coût, l'effet et le délai.",
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


C = "C2.1"

# ═══════════ Ce qu'un chiffre agrégé cache (8) ═══════════

q(C, "Un chiffre exact et insuffisant", "« Un usager sur cinq abandonne devant la borne. » Ce chiffre est…",
  ["exact, et pourtant insuffisant pour décider quoi que ce soit",
   "faux : les observations disent autre chose",
   "suffisant : on sait ce qu'il faut corriger",
   "inutilisable : quarante usagers, c'est trop peu"],
  "Un chiffre agrégé additionne des situations très différentes. Il est vrai, et il ne désigne "
  "personne — donc il n'oriente aucune décision.",
  "8 abandons sur 40 : le calcul est juste. Ce qu'il cache, c'est qui sont ces huit.",
  "Prendre un chiffre global pour un diagnostic.",
  ["",
   "Le calcul est parfaitement exact : 8 abandons sur 40 font bien un cinquième. Le problème n'est pas l'arithmétique, c'est ce que l'addition efface.",
   "Savoir que 20 % échouent ne dit ni où, ni pour qui, ni pourquoi : on ne peut rien corriger avec cette seule phrase.",
   "Quarante observations suffisent largement à faire apparaître un écart de 0 % à 50 % entre profils ; ce n'est pas la taille de l'échantillon qui pose problème."],
  "Un chiffre agrégé peut être exact et inutilisable.")

q(C, "Qui abandonne vraiment", "En détaillant par profil, on trouve chez les habitués un taux d'abandon de…",
  ["0 % : aucun des quatorze habitués n'a abandonné",
   "20 %, comme la moyenne générale",
   "11 %, comme les occasionnels",
   "50 %, comme les personnes âgées"],
  "C'est le résultat qui renverse la lecture : l'objet est parfaitement utilisable — quand on le "
  "connaît déjà.",
  "Habitués 0 % · occasionnels 11 % · poussette 25 % · touristes 43 % · personnes âgées 50 %.",
  "Croire que les 20 % se répartissent au hasard.",
  ["",
   "La moyenne générale ne s'applique à aucun profil en particulier : c'est justement ce que le détail révèle.",
   "Les occasionnels sont à 11 %, soit un abandon sur neuf ; les habitués, eux, n'en comptent aucun.",
   "Cinquante pour cent est le taux des personnes âgées, à l'autre extrémité de l'échelle."],
  "Aucun habitué n'abandonne. Ce ne sont jamais les mêmes qui échouent.")

q(C, "La moyenne qui ne décrit personne", "La durée moyenne est de 77 s ; l'habitué met 41 s et la personne âgée 123 s. Cela montre que…",
  ["une moyenne calculée sur un groupe varié peut ne décrire personne",
   "l'un des deux relevés est erroné",
   "la moyenne a été mal calculée",
   "il faudrait arrondir à 80 s"],
  "La moyenne est le milieu d'une série, pas le portrait d'une personne. Sur un groupe hétérogène, "
  "elle tombe souvent dans un creux où personne ne se trouve.",
  "Personne, dans les quarante observations, ne met exactement 77 secondes.",
  "Décrire un usage réel par une moyenne.",
  ["",
   "Les deux relevés sont exacts : ils décrivent deux personnes réelles, très différentes l'une de l'autre.",
   "Le calcul est correct. C'est son interprétation comme portrait d'un usager typique qui est fautive.",
   "Arrondir aggraverait le défaut au lieu de le corriger : le problème n'est pas la précision du nombre mais ce qu'il prétend décrire."],
  "Une moyenne décrit un milieu, pas une personne.")

q(C, "Ce que répond le service technique", "« Nos bornes fonctionnent, aucune n'est en panne. » Cette réponse est…",
  ["vraie, et à côté de la question : on ne parle pas de pannes mais d'usages",
   "fausse : le relevé de maintenance contient trois incidents",
   "la fin de la discussion : s'il n'y a pas de panne, il n'y a pas de problème",
   "une preuve que l'observation des usagers ne sert à rien"],
  "Un objet peut fonctionner parfaitement et échouer à rendre son service. C'est la troisième fois "
  "du cycle que ce constat revient, sur un troisième objet.",
  "Aucune borne en panne, et pourtant une personne âgée sur deux repart sans titre.",
  "Confondre « ça marche » et « ça rend service ».",
  ["",
   "Les trois incidents sont réels mais rares ; même sans eux, la moitié des personnes âgées abandonneraient. Le service technique n'a pas tort sur les faits.",
   "Un objet sans panne qui fait échouer la moitié de ses usagers pose un problème considérable — simplement, ce n'est pas un problème de panne.",
   "C'est l'inverse : seule l'observation des usagers a fait apparaître un problème qu'aucun contrôle technique n'aurait détecté."],
  "Fonctionner et rendre service ne sont pas la même chose.")

q(C, "L'étape qui concentre les abandons", "Sur les cinq étapes, celle qui concentre le plus d'abandons est…",
  ["choisir le titre",
   "approcher la borne",
   "récupérer le titre",
   "choisir la langue"],
  "Quatre des huit abandons s'y produisent : c'est là que l'usager doit comprendre une offre qu'on "
  "ne lui a pas expliquée.",
  "Mme Liu : « trop de boutons, et ils changent de place selon l'écran ».",
  "Chercher la cause à l'étape du paiement, parce qu'elle paraît plus technique.",
  ["",
   "Aucun abandon n'a lieu à l'approche : à ce moment, l'usager n'a encore rencontré aucune difficulté.",
   "Un seul abandon s'y produit, et il concerne une personne qui avait les mains prises — c'est un autre problème.",
   "Un seul abandon a lieu au choix de la langue ; l'étape suivante en concentre quatre fois plus."],
  "C'est au choix du titre que l'offre devient incompréhensible.")

q(C, "Deux fois le même enseignement", "En 4e à Hangzhou, une moyenne de 29 s cachait un maximum de 83 s. Ici, un taux de 20 % cache des taux de 0 % à 50 %. Ces deux constats…",
  ["disent la même chose : un résumé chiffré efface ce qui n'est pas moyen",
   "n'ont aucun rapport : l'un porte sur des durées, l'autre sur des taux",
   "se contredisent",
   "montrent que les statistiques sont trompeuses par nature"],
  "Le rencontrer deux fois, sur deux objets et deux grandeurs différentes, est ce qui transforme "
  "une anecdote en méthode.",
  "Moyenne et pourcentage global : deux résumés, le même angle mort.",
  "Traiter chaque cas comme une curiosité isolée.",
  ["",
   "La grandeur change, le mécanisme est identique : dans les deux cas, un nombre unique remplace une distribution très étalée.",
   "Ils vont exactement dans le même sens ; aucun des deux ne contredit l'autre.",
   "Les statistiques ne sont pas trompeuses en elles-mêmes : c'est leur usage sans le détail qui l'est. Le détail est lui aussi statistique."],
  "Un résumé chiffré efface toujours ce qui n'est pas moyen.")

q(C, "À quoi sert le détail", "Détailler un chiffre global par profil sert d'abord à…",
  ["savoir sur qui agir, et donc quoi corriger",
   "rendre le rapport plus long",
   "vérifier que le chiffre global est juste",
   "montrer qu'on maîtrise le tableur"],
  "Une action se dirige vers quelqu'un. Tant qu'on ignore qui échoue, on ne peut pas décider quoi "
  "changer.",
  "Savoir que ce sont les personnes âgées et les touristes désigne aussitôt la piste : la lisibilité.",
  "Détailler pour détailler, sans en tirer de décision.",
  ["",
   "La longueur n'est pas un objectif : le détail se justifie parce qu'il change la décision, pas parce qu'il remplit une page.",
   "Le chiffre global était déjà juste avant le détail ; ce n'est pas une vérification mais une décomposition.",
   "La compétence technique est un moyen ; ce qui compte est ce que le calcul permet de décider."],
  "On détaille pour savoir sur qui agir.")

q(C, "L'angle mort des concepteurs", "Pourquoi un problème d'usage reste-t-il souvent invisible à ceux qui décident ?",
  ["parce que ceux qui décident sont presque toujours des habitués, et que les habitués réussissent",
   "parce qu'ils ne s'y intéressent pas",
   "parce que les usagers ne se plaignent jamais",
   "parce que les données sont trop difficiles à recueillir"],
  "L'expérience du concepteur est la moins représentative de toutes : il connaît l'objet par cœur. "
  "C'est structurel, pas une question de bonne volonté.",
  "Zéro abandon chez les quatorze habitués — dont font partie les techniciens de la régie.",
  "Tester un objet uniquement avec des gens qui le connaissent.",
  ["",
   "Le désintérêt n'est pas nécessaire pour expliquer l'aveuglement : quelqu'un de très attentif mais habitué ne rencontrera simplement jamais la difficulté.",
   "Certains se plaignent — les huit verbatims en témoignent — mais ceux qui renoncent partent le plus souvent sans rien dire.",
   "Ces données-ci ont été recueillies en observant quarante personnes : c'est long, mais ce n'est pas difficile."],
  "Les habitués réussissent — et ce sont eux qui décident.")

# ═══════════ Les six modes et leur vocabulaire (10) ═══════════

q(C, "Le storyboard", "Un storyboard, c'est…",
  ["une suite de quelques images qui montrent ce qui se passe, étape par étape",
   "un tableau croisant des critères et des solutions",
   "un schéma fait d'ovales, de rectangles et de losanges",
   "une liste de mesures chiffrées"],
  "Le mot vient du cinéma : le film est dessiné avant d'être tourné. En conception, il sert à "
  "montrer un usage à quelqu'un qui n'a ni le temps ni le vocabulaire de lire autre chose.",
  "Trois vignettes affichées près de la borne, presque sans texte.",
  "Confondre storyboard et bande dessinée illustrative : ici chaque image porte une information.",
  ["",
   "C'est la définition du tableau comparatif, qui sert à arbitrer et non à raconter.",
   "Ces formes sont celles de l'algorigramme, qui décrit une logique et non une suite d'images.",
   "Une liste de mesures relève du relevé ou du graphique ; le storyboard ne chiffre rien."],
  "Storyboard : quelques images, une histoire, presque pas de mots.",
  img=IMG_MODES)

q(C, "La carte d'empathie", "Une carte d'empathie se présente sous la forme…",
  ["de quatre cases : ce que la personne dit, fait, voit, ressent",
   "d'une courbe de satisfaction dans le temps",
   "d'une suite d'étapes numérotées",
   "d'un questionnaire à remplir par l'usager"],
  "C'est un outil de concepteur : il oblige à séparer ce qu'on a entendu de ce qu'on a observé, et "
  "à écrire ce que la personne n'a pas dit.",
  "Mme Liu : elle DIT « trop de boutons » ; elle VOIT la file derrière elle — qu'elle n'a pas mentionnée.",
  "Remplir les quatre cases avec la même information reformulée.",
  ["",
   "Une courbe suppose une mesure dans le temps ; la carte d'empathie ne mesure rien, elle range des observations.",
   "Les étapes numérotées sont celles du parcours utilisateur ; la carte d'empathie ne suit pas un déroulement.",
   "Elle n'est pas remplie par l'usager mais par l'observateur, à partir de ce qu'il a entendu et vu."],
  "Carte d'empathie : dit · fait · voit · ressent.")

q(C, "Le parcours utilisateur", "Un parcours utilisateur montre…",
  ["la suite des étapes traversées par la personne, nommées les unes après les autres",
   "la logique interne de la machine, avec ses tests",
   "les quantités comparées entre elles",
   "le ressenti de la personne, case par case"],
  "Son intérêt est de donner une adresse commune : « c'est trop long » devient « l'étape 3 est trop "
  "longue », et douze témoignages deviennent comparables.",
  "Approcher · choisir la langue · choisir le titre · payer · récupérer.",
  "Confondre le parcours de l'usager et le fonctionnement de la machine.",
  ["",
   "La logique interne avec ses tests est l'affaire de l'algorigramme ; le parcours reste du côté de ce que fait la personne.",
   "Comparer des quantités est le rôle du graphique ; le parcours ne porte aucun chiffre par lui-même.",
   "Le ressenti case par case est la carte d'empathie ; le parcours nomme des étapes, pas des émotions."],
  "Parcours utilisateur : les étapes, dans l'ordre où on les vit.")

q(C, "Le tableau comparatif", "Un tableau comparatif est le seul des six modes qui permette…",
  ["d'arbitrer entre plusieurs pistes, en croisant chacune avec plusieurs critères",
   "de montrer un ressenti",
   "de représenter un ordre d'opérations",
   "d'être compris en trois secondes"],
  "Arbitrer suppose de tenir plusieurs options et plusieurs critères en même temps : seule une "
  "grille le permet.",
  "Quatre pistes × trois critères : coût, effet, délai.",
  "L'employer devant quelqu'un qui n'a pas le temps de le lire.",
  ["",
   "Un ressenti se rend par la carte d'empathie ou le storyboard ; un tableau le réduirait à une case, ce qui le détruit.",
   "L'ordre des opérations est l'affaire de l'algorigramme ; un tableau juxtapose, il n'enchaîne pas.",
   "C'est exactement son angle mort : dense et précis, il se lit lentement — un lecteur pressé ne l'ouvrira pas."],
  "Le tableau comparatif est le mode de l'arbitrage.",
  img=IMG_C3B)

q(C, "L'angle mort du graphique", "Le graphique chiffre et hiérarchise. Ce qu'il ne montre pas, c'est…",
  ["le vécu des personnes : pourquoi elles renoncent, ce qu'elles ressentent",
   "les quantités",
   "les comparaisons entre catégories",
   "les écarts entre profils"],
  "Chaque mode a un angle mort, et c'est cet angle mort — pas son point fort — qui décide s'il "
  "convient à un destinataire donné.",
  "50 % chez les personnes âgées : le graphique le dit. Pourquoi ? Il n'en sait rien.",
  "Croire qu'un graphique se suffit à lui-même.",
  ["",
   "Les quantités sont précisément ce qu'un graphique montre le mieux : c'est son point fort, pas son angle mort.",
   "Comparer des catégories est l'usage même du diagramme en barres employé ici.",
   "Les écarts entre profils sautent aux yeux sur ce graphique : c'est ce qui l'a rendu utile pour l'élue."],
  "Le graphique dit combien, jamais pourquoi.")

q(C, "L'angle mort de l'algorigramme", "L'algorigramme rend les cas d'échec traitables. Son angle mort est…",
  ["d'être illisible pour qui n'a pas appris ses formes",
   "de ne pas montrer l'ordre des opérations",
   "d'être imprécis",
   "de ne pas pouvoir représenter d'échec"],
  "Ce n'est pas un défaut du mode, c'est une condition d'emploi : il suppose un lecteur formé. "
  "D'où son destinataire naturel, le technicien.",
  "Un losange ne veut rien dire pour quelqu'un qui n'a jamais vu d'algorigramme.",
  "Le présenter à un décideur non technicien, en pensant faire sérieux.",
  ["",
   "Montrer l'ordre des opérations est justement ce qu'il fait mieux que tous les autres modes.",
   "C'est le plus précis des six : chaque case dit une action ou une décision, sans ambiguïté.",
   "Représenter les échecs est sa raison d'être : c'est la branche « non » de chaque test."],
  "L'algorigramme suppose un lecteur formé.")

q(C, "L'angle mort de la carte d'empathie", "La carte d'empathie restitue le vécu. Son angle mort est…",
  ["qu'elle ne se mesure pas : deux observateurs la rempliront différemment",
   "qu'elle ne dit rien du ressenti",
   "qu'elle est trop longue à lire",
   "qu'elle ne concerne que les personnes âgées"],
  "Ce qu'elle capte — la file d'attente derrière Mme Liu, la gêne d'être vue — n'apparaît dans "
  "aucun chiffre. C'est sa force et sa fragilité en même temps.",
  "Deux élèves observant la même personne n'écriront pas la même case « ressent ».",
  "Lui demander une objectivité qu'elle ne peut pas fournir.",
  ["",
   "Le ressenti est exactement ce qu'elle est faite pour recueillir : c'est l'une de ses quatre cases.",
   "Elle tient sur une page en quatre cases : c'est l'un des modes les plus rapides à parcourir.",
   "Elle s'établit pour n'importe quel usager ; le choix de Mme Liu tient à ce qu'elle représente un profil qui échoue."],
  "La carte d'empathie capte ce qu'aucun chiffre ne dit — et ne se mesure pas.")

q(C, "L'angle mort du storyboard", "Le storyboard se comprend sans mode d'emploi. En revanche…",
  ["il ne tient que très peu d'informations",
   "il demande de savoir lire",
   "il ne fonctionne qu'en couleur",
   "il ne peut pas montrer d'action"],
  "Peu d'informations n'est pas toujours un défaut : pour quelqu'un qui a trois secondes, c'est "
  "exactement ce qu'il faut.",
  "Trois vignettes affichées près de la borne : au-delà, personne ne les regarderait.",
  "Vouloir y faire entrer les chiffres de l'observation.",
  ["",
   "C'est justement son intérêt : il fonctionne sans texte, donc quelle que soit la langue du lecteur.",
   "La couleur aide, mais un storyboard en noir et blanc reste parfaitement lisible.",
   "Montrer une action est précisément sa spécialité : chaque vignette en représente une."],
  "Le storyboard dit peu — et c'est parfois ce qu'il faut.")

q(C, "Deux mots venus du travail", "« Storyboard » et « carte d'empathie » sont des mots…",
  ["venus du monde professionnel, et non du vocabulaire scolaire",
   "inventés pour cette séquence",
   "synonymes l'un de l'autre",
   "réservés aux études d'art"],
  "Les connaître n'est pas anecdotique : ce sont des outils employés dans la conception de "
  "produits et de services, au lycée comme après.",
  "Le storyboard vient du cinéma ; la carte d'empathie, du design de services.",
  "Croire qu'un mot inconnu désigne une notion compliquée.",
  ["",
   "Ils existaient bien avant cette séquence et s'emploient couramment dans les métiers de la conception.",
   "Ils désignent des choses très différentes : l'un raconte une suite d'actions, l'autre range des observations sur une personne.",
   "Ils sont employés en design, en informatique, en marketing et en ingénierie — pas seulement dans les filières artistiques."],
  "Deux outils de métier, pas deux mots d'école.")

q(C, "Aucun n'est meilleur", "Parmi les six modes, lequel est le meilleur ?",
  ["aucun : chacun a été inventé pour un usage, et son angle mort le disqualifie ailleurs",
   "l'algorigramme, parce qu'il est le plus précis",
   "le graphique, parce qu'il est le plus rapide à lire",
   "le storyboard, parce qu'il est compris par tout le monde"],
  "C'est la thèse de la séquence : un mode n'est jamais bon en soi, il est bon pour quelqu'un.",
  "L'algorigramme sauve le technicien et perd l'élue ; le storyboard fait l'inverse.",
  "Classer les modes du meilleur au moins bon.",
  ["",
   "Sa précision est réelle, et elle ne sert à rien devant un lecteur qui n'en connaît pas les symboles.",
   "Il se lit vite, et il ne dit rien du vécu : devant un usager qui doit changer son geste, il est inutile.",
   "Il est compris de tous, et il ne tient presque aucune information : il ne permettrait aucune réparation."],
  "Un mode n'est jamais bon en soi — il est bon pour quelqu'un.",
  img=IMG_MODES)

# ═══════════ Choisir, et justifier (7) ═══════════

q(C, "Ce qui contraint le choix", "Ce qui décide du mode à employer, c'est…",
  ["le destinataire et l'intention : à qui l'on parle, et ce qu'on veut qu'il fasse",
   "le goût de celui qui représente",
   "le temps dont on dispose pour le fabriquer",
   "la matière enseignée"],
  "Sans contrainte, tous les modes se valent et il n'y a rien à justifier. C'est le destinataire "
  "qui rend un choix meilleur qu'un autre.",
  "Trois secondes pour l'usager, quelques minutes pour l'élue, un temps long pour le technicien.",
  "Choisir le mode qu'on préfère, puis fabriquer la justification.",
  ["",
   "Le goût ne se discute pas, donc il ne se justifie pas : une raison qui ne peut être contredite n'est pas une raison.",
   "Le temps de fabrication compte en pratique, mais il ne dit rien de l'utilité de la représentation pour celui qui la reçoit.",
   "Le même geste s'emploie en technologie, en français ou en histoire : c'est une compétence de communication, pas de discipline."],
  "Le destinataire choisit le mode, pas le goût.",
  img=IMG_DEST)

q(C, "Justifier par l'angle mort", "Une bonne justification du choix d'un mode consiste à montrer…",
  ["que son angle mort ne gêne pas ce destinataire-là",
   "qu'il est plus clair que les autres",
   "qu'on sait bien le réaliser",
   "qu'il est utilisé par les professionnels"],
  "Tous les modes ont un point fort : l'invoquer ne désigne personne. Seul l'angle mort discrimine.",
  "« Le graphique ne dit rien du vécu — sans importance ici, elle vote un budget. »",
  "Justifier par le point fort, ce qui vaudrait pour n'importe quel destinataire.",
  ["",
   "« Plus clair » vaudrait pour tout le monde, donc pour personne en particulier : ce n'est pas une justification mais une préférence.",
   "La facilité d'exécution concerne l'auteur, pas le lecteur — or c'est le lecteur qui doit pouvoir agir.",
   "L'usage professionnel ne dit rien du destinataire précis : les professionnels emploient les six, selon les cas."],
  "On justifie un mode par son angle mort, pas par son point fort.")

q(C, "Une justification faible", "« J'ai choisi le graphique parce que c'est plus visuel. » Cette justification est faible parce qu'elle…",
  ["vaudrait pour n'importe quel destinataire, donc elle n'en désigne aucun",
   "est fausse : un graphique n'est pas visuel",
   "est trop courte",
   "emploie un mot d'anglais"],
  "Le test d'une justification : si elle marche pour les trois destinataires, elle n'en justifie "
  "aucun.",
  "Un storyboard aussi est visuel. Et une carte d'empathie. Et un parcours utilisateur.",
  "Se contenter d'une raison vraie mais non discriminante.",
  ["",
   "Un graphique est bel et bien visuel : l'affirmation est exacte, et c'est justement pour cela qu'elle ne prouve rien.",
   "La longueur n'est pas en cause : une justification d'une ligne peut être excellente si elle désigne son destinataire.",
   "Aucun mot d'anglais n'y figure, et cela ne serait pas un défaut."],
  "Une justification qui marche pour tout le monde ne justifie rien.")

q(C, "Le même mode pour deux destinataires", "Peut-on employer le même mode pour deux destinataires différents ?",
  ["oui, mais il faudra sans doute le simplifier ou le compléter pour l'un des deux",
   "non, jamais",
   "oui, sans rien y changer",
   "seulement si les deux ont le même métier"],
  "Le mode et sa mise en œuvre sont deux choses : un même graphique peut servir deux publics s'il "
  "n'est pas légendé de la même façon.",
  "Un graphique pour l'élue tient en une phrase ; le même pour le technicien porterait les effectifs.",
  "Réemployer une représentation telle quelle, pour gagner du temps.",
  ["",
   "Rien ne l'interdit : ce qui change d'un destinataire à l'autre, c'est le niveau de détail et le vocabulaire, pas nécessairement le mode.",
   "Le réemployer sans modification revient à négliger la différence de temps, de vocabulaire et de pouvoir entre les deux.",
   "Deux personnes du même métier peuvent avoir des besoins très différents selon ce qu'elles doivent décider."],
  "Même mode, autre mise en œuvre : c'est possible, et cela se dit.")

q(C, "Ce qu'on laisse de côté", "Dans la défense d'une représentation, le point le plus souvent oublié est…",
  ["ce qu'on a volontairement laissé de côté",
   "le nom du destinataire",
   "le mode retenu",
   "la date de réalisation"],
  "Représenter, c'est choisir ce qu'on montre — donc aussi ce qu'on cache. Savoir dire ce qu'on a "
  "écarté est la preuve qu'on a choisi.",
  "« Je n'ai pas montré la cause des abandons : elle ne la corrigera pas elle-même. »",
  "Mettre tout ce qu'on a, et appeler cela représenter.",
  ["",
   "Le destinataire est presque toujours nommé, parce que la consigne le demande explicitement.",
   "Le mode retenu se voit sur la production elle-même : c'est l'élément le plus difficile à oublier.",
   "La date n'entre pas dans la défense d'une représentation ; elle ne dit rien de sa pertinence."],
  "Ce qu'on écarte prouve qu'on a choisi.")

q(C, "Un mauvais appariement", "Proposer un tableau comparatif à l'usager debout dans la station est un mauvais choix parce que…",
  ["il se lit lentement, et l'usager dispose de trois secondes",
   "un tableau n'est pas une représentation",
   "l'usager ne sait pas lire un tableau",
   "il n'y a rien à comparer"],
  "L'angle mort du mode rencontre exactement la contrainte du destinataire : c'est la définition "
  "d'un mauvais appariement.",
  "Un tableau à douze cases, lu en marchant, ne sera pas lu du tout.",
  "Choisir le mode le plus riche, en pensant bien faire.",
  ["",
   "C'est une représentation à part entière, et l'une des plus utiles — pour un lecteur qui a le temps.",
   "Rien n'indique une difficulté de lecture chez cet usager : c'est le temps qui manque, pas la compétence.",
   "Il y aurait beaucoup à comparer — quatre pistes, trois critères — mais ce n'est pas ce dont l'usager a besoin pour passer le portique."],
  "Un mauvais appariement, c'est un angle mort qui tombe sur une contrainte.")

q(C, "Changer d'avis", "Un élève annonce le graphique, puis produit finalement un storyboard. Cela est…",
  ["acceptable s'il dit qu'il a changé d'avis et pourquoi",
   "une erreur qui doit être sanctionnée",
   "sans importance : seul le résultat compte",
   "impossible : le choix est définitif"],
  "Changer d'avis avec une raison est un geste de concepteur. Ce qui serait fautif, c'est de "
  "changer sans le dire — ou sans savoir pourquoi.",
  "« En le dessinant, j'ai vu que les chiffres ne serviraient pas à un usager pressé. »",
  "Cacher un changement d'avis, de peur qu'il passe pour une erreur.",
  ["",
   "Un changement raisonné est le signe d'une réflexion aboutie, pas d'une faute : c'est ainsi que travaillent les concepteurs.",
   "Le raisonnement compte autant que le résultat : c'est lui qui est évalué dans cette compétence.",
   "Rien ne rend un choix irrévocable, surtout au moment où l'on découvre ce que le mode permet réellement."],
  "Changer d'avis avec une raison est le contraire d'une erreur.")

# ═══════════ L'algorigramme, et l'ordre des opérations (5) ═══════════

q(C, "Le défaut d'ordre", "La borne encaisse le paiement, puis échoue à imprimer faute de papier. Le défaut se situe…",
  ["dans l'ordre des opérations : le test du papier vient après l'encaissement",
   "dans le rouleau de papier, de mauvaise qualité",
   "dans le monnayeur",
   "chez l'usager, qui aurait dû vérifier"],
  "Le test existait déjà : il était simplement au mauvais endroit. Déplacer une case ne coûte rien "
  "en matériel et supprime la pire panne du relevé.",
  "Trois fois en trente jours, un usager a payé et n'a rien reçu.",
  "Corriger l'organe — « changer le rouleau plus souvent » — au lieu de l'ordre.",
  ["",
   "Le rouleau finira toujours par s'épuiser, quelle que soit sa qualité : c'est un consommable, pas une pièce défectueuse.",
   "Le monnayeur fait exactement son travail : il encaisse. Le problème est qu'on le lui a demandé trop tôt.",
   "Un usager n'a aucun moyen de connaître le niveau de papier restant, et ce n'est pas son rôle."],
  "On ne prend jamais l'argent d'un usager avant d'être sûr de pouvoir le servir.",
  img=IMG_C3)

q(C, "Pourquoi l'algorigramme", "Pourquoi ce défaut ne peut-il être montré que par un algorigramme ?",
  ["parce qu'il porte sur l'ordre des opérations, que seul ce mode représente",
   "parce que c'est le mode le plus précis",
   "parce que le technicien préfère les schémas",
   "parce que c'est un exercice du DNB"],
  "Un graphique montrerait la fréquence de la panne, un storyboard son effet sur l'usager. Aucun "
  "des deux ne montre à quel moment le test aurait dû se produire.",
  "Le même incident, sur un graphique : « 3 fois en 30 jours ». Rien sur la cause.",
  "Choisir l'algorigramme par habitude plutôt que par nécessité.",
  ["",
   "La précision seule ne suffit pas : un tableau très précis ne montrerait toujours pas l'enchaînement des opérations.",
   "Les préférences du destinataire ne sont pas un critère ; ce qui compte est que le mode puisse montrer le défaut.",
   "C'est vrai, et sans rapport : l'algorigramme s'impose ici parce que le défaut est un défaut d'ordre."],
  "Un défaut d'ordre ne se voit que sur un algorigramme.")

q(C, "La correction", "Comment corriger l'incident du papier ?",
  ["tester le papier AVANT d'encaisser, et refuser le paiement s'il en manque",
   "changer le rouleau plus souvent",
   "afficher un message d'excuse après l'échec",
   "rembourser automatiquement l'usager"],
  "Déplacer le test en amont supprime la situation, au lieu d'en réparer les conséquences.",
  "La borne se déclare indisponible et alerte la maintenance — sans avoir pris un centime.",
  "Traiter la conséquence plutôt que la cause.",
  ["",
   "Cela réduit la fréquence sans supprimer le cas : le jour où le rouleau s'épuisera quand même, l'usager paiera toujours pour rien.",
   "Un message d'excuse arrive après le prélèvement : l'usager a déjà payé, et l'excuse ne lui rend pas son argent.",
   "Le remboursement automatique répare les dégâts, il ne les évite pas — et il suppose que la borne sache identifier le payeur."],
  "On supprime la situation, on ne répare pas ses conséquences.")

q(C, "La fin en échec", "Quand le papier manque, la borne doit…",
  ["se déclarer indisponible et alerter la maintenance",
   "continuer, et prévenir seulement si l'impression échoue",
   "demander à l'usager s'il veut tenter quand même",
   "ne rien faire de particulier"],
  "Une machine qui se sait incapable de servir doit le dire et prévenir. Sans cette branche, elle "
  "attend le client suivant pour échouer à nouveau.",
  "Trois échecs en trente jours : c'est le nombre de fois où personne n'a été prévenu.",
  "Laisser la branche « non » d'un test sans destination.",
  ["",
   "C'est exactement le comportement actuel, celui qui produit la panne : prévenir après coup ne rend pas le titre.",
   "Reporter la décision sur l'usager lui demande d'arbitrer un risque qu'il ne peut pas évaluer, avec son propre argent.",
   "Ne rien faire garantit que l'incident se reproduira au client suivant, et à tous les autres."],
  "Une borne qui se sait hors service doit le dire et prévenir.")

q(C, "Une pièce refusée", "Le monnayeur refuse les pièces usées. Ce que vit l'usager, c'est…",
  ["la croyance que sa pièce a été refusée par erreur, et il recommence",
   "un abandon immédiat",
   "une panne complète de la borne",
   "rien de particulier : il change de pièce"],
  "Entre la cause technique et le vécu, il y a toujours une interprétation de l'usager — et c'est "
  "elle qui décide de ce qu'il fait ensuite.",
  "Sept fois en trente jours, et à chaque fois plusieurs tentatives.",
  "Décrire un incident par sa cause technique seule.",
  ["",
   "L'abandon n'est pas immédiat : l'usager essaie d'abord plusieurs fois, ce qui allonge son temps et celui de la file.",
   "La borne fonctionne parfaitement : elle applique un critère de reconnaissance, et c'est ce critère qui est trop strict.",
   "Changer de pièce suppose d'avoir compris que la pièce était en cause, ce que rien n'indique à l'usager."],
  "Entre la cause et le vécu, il y a l'interprétation de l'usager.")

assert len(Q) == 30, len(Q)
assert sum(1 for x in Q if "img" in x) == 5
