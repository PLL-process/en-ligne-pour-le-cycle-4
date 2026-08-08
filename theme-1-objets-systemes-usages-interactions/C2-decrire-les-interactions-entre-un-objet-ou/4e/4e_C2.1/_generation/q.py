# -*- coding: utf-8 -*-
"""Les 30 questions du QCM 4e_C2.1 · C2.2 — Hangzhou, la borne de retrait.

Écrites à la main. Toutes les bonnes réponses sont en position 0 ici : la
répartition sur A/B/C/D est faite ensuite par `_outils/fix_r.js`, de façon
déterministe, à partir d'une graine.

Règle tenue pour chaque distracteur : la réfutation EXPLIQUE pourquoi la réponse
est fausse. Une réfutation courte est un aveu que l'auteur n'a pas cherché ce que
l'élève avait en tête.
"""

IMG_TRAJET = {
    "src": "Images/du_verbatim_a_l_algorigramme.svg",
    "alt": "Quatre représentations d'une même expérience, reliées par des flèches : le langage "
           "naturel, le schéma du parcours en étapes, le graphique des durées et l'algorithme. "
           "Chacune est présentée avec ce qu'elle apporte et ce qu'elle ne sait pas dire.",
}
IMG_EXIG = {
    "src": "Images/six_familles_d_exigences.svg",
    "alt": "Tableau des six familles d'exigences du programme — sécurité, incidences "
           "environnementales, formes et fonctions, ergonomie, qualité, fiabilité — avec la "
           "question que chacune pose et ce qu'elle donne sur la borne de Hangzhou.",
}
IMG_GRAPH = {
    "src": "Images/corrige_temps_par_etape.svg",
    "alt": "Graphique des durées par étape : pour chaque étape, la durée moyenne et la durée "
           "maximale. Choisir a la moyenne la plus haute (40 s) ; déverrouiller a le plus grand "
           "écart (29 s de moyenne, 83 s au maximum) avec 9 reprises sur 30.",
}

Q = []


def q(c, n, question, options, expl, ex, err, refs, ret, img=None):
    """options[0] est toujours la bonne réponse ; refs[0] est vide."""
    assert len(options) == 4 and len(refs) == 4, n
    assert refs[0] == "", n
    for r in refs[1:]:
        assert len(r) > 20, (n, r)
    o = {"c": c, "n": n, "q": question, "o": options, "r": 0,
         "expl": expl, "ex": ex, "err": err, "d": refs, "ret": ret}
    if img:
        o["img"] = img
    Q.append(o)


# ═══════════ 4e_C2.1 — décrire l'expérience de l'utilisateur (15) ═══════════

q("C2.1", "Le trajet imposé", "Décrire l'expérience d'un utilisateur, au programme de 4e, c'est aller…",
  ["du langage naturel vers les schémas, graphiques et algorithmes",
   "des schémas vers le langage naturel",
   "des mesures vers les opinions",
   "du dessin vers la photographie"],
  "Le programme fixe un sens de marche : on part de ce que les gens disent, et on aboutit à des "
  "représentations qui se comparent, se mesurent et s'exécutent.",
  "« Tu tires, ça résiste » (mots) → cinq étapes (schéma) → 83 s (graphique) → un test (algorithme).",
  "S'arrêter au récit, sans jamais le traduire.",
  ["",
   "Le sens inverse ferait perdre l'essentiel : un schéma tout fait empêche d'entendre ce que les gens vivent réellement, et on ne schématise bien que ce qu'on a d'abord écouté.",
   "Une opinion n'est pas un aboutissement : elle est le point de départ. Le trajet va vers des représentations plus partageables, pas vers des avis.",
   "Le mode de reproduction de l'image n'est pas la question : un croquis à la main fait très bien l'affaire au départ, et une photo ne serait pas un aboutissement."],
  "On part des mots, on aboutit aux schémas, graphiques et algorithmes.",
  img=IMG_TRAJET)

q("C2.1", "Le langage naturel", "Partir du « langage naturel », cela veut dire recueillir…",
  ["les mots exacts des usagers, sans les reformuler",
   "un résumé de ce que le professeur a compris",
   "uniquement des chiffres",
   "les réponses à un questionnaire à choix multiples"],
  "Reformuler, c'est déjà interpréter. Les mots exacts gardent ce que l'usager a jugé important — "
  "y compris son hésitation et sa colère.",
  "« Tu ne sais pas si c'est toi ou la borne » dit plus que « l'usager est gêné ».",
  "Résumer le verbatim avant de l'avoir exploité.",
  ["",
   "Un résumé fait par un tiers a déjà écarté ce qui lui semblait secondaire — or c'est souvent là que se trouve le vrai problème.",
   "Les chiffres viennent après, et ils ne disent pas la même chose : une durée ne raconte pas ce que la personne a cru comprendre.",
   "Un QCM impose ses propres catégories : l'usager ne peut y dire que ce que l'auteur avait prévu, et le langage naturel sert précisément à recueillir l'imprévu."],
  "Les mots exacts, avant toute reformulation.")

q("C2.1", "Deux usagers en désaccord", "Wang trouve la liste des vélos décourageante, Ma la trouve pratique. Que fait-on ?",
  ["on écrit les deux : un même objet ne produit pas la même expérience selon qui l'utilise",
   "on tranche en faveur du plus expérimenté",
   "on interroge d'autres usagers jusqu'à obtenir un accord",
   "on écarte les deux, faute d'accord"],
  "Un désaccord entre usagers n'est pas un problème de méthode : c'est un résultat. Il dit que "
  "l'objet convient à certains profils et pas à d'autres.",
  "Ma est livreur, il cherche la batterie ; Wang vient une fois par semaine et ne sait pas quoi regarder.",
  "Vouloir un avis unique là où l'usage est divers.",
  ["",
   "L'expérience de l'usager habitué masque justement les difficultés des autres : c'est le profil le moins représentatif de ceux qui bloquent.",
   "Rien ne garantit qu'un accord existe, et le chercher revient à noyer les profils minoritaires — qui sont souvent ceux qui échouent.",
   "Écarter les témoignages contradictoires reviendrait à ne garder que ce qui est consensuel, c'est-à-dire à perdre tout ce qui distingue les usagers entre eux."],
  "Deux expériences opposées sur le même objet : c'est un résultat.")

q("C2.1", "Ressenti et durée", "Feng dit : « ce n'est pas que ce soit long, c'est de ne pas savoir combien de temps ça va durer ». Ce verbatim montre que…",
  ["le ressenti dépend de l'information reçue autant que de la durée réelle",
   "Feng exagère : trente secondes, ce n'est rien",
   "il faut avant tout raccourcir l'attente",
   "le ressenti n'est pas exploitable en technologie"],
  "Deux attentes de même durée ne se vivent pas pareil selon qu'on en connaît la fin ou non. "
  "C'est une donnée de conception, pas une susceptibilité.",
  "Une barre de progression ne rend rien plus rapide, et rend l'attente supportable.",
  "Croire qu'on ne peut agir que sur la durée.",
  ["",
   "Le jugement sur la personne ne règle rien : ce que dit Feng est vrai pour la plupart des gens, et cela s'observe dans tous les services d'attente.",
   "Raccourcir est une réponse possible, mais coûteuse, et Feng dit précisément que ce n'est pas ce qui le gêne : informer serait plus efficace et moins cher.",
   "Le ressenti est au contraire au cœur du programme de 4e — la formulation du code dit « ressenti et facilité d'usage »."],
  "Attendre en le sachant, ce n'est pas attendre.")

q("C2.1", "La facilité d'usage", "Xu dit : « je fais ça en trente secondes, mais ma mère n'y arrive pas seule ». Ce verbatim apporte que…",
  ["la facilité d'usage dépend de l'expérience de la personne, pas seulement de l'objet",
   "l'objet est trop compliqué pour tout le monde",
   "la mère de Xu manque d'attention",
   "rien d'utile : c'est une opinion personnelle"],
  "Le même objet est facile pour l'habitué et difficile pour le nouveau venu. Concevoir pour "
  "l'habitué, c'est exclure sans le vouloir.",
  "Trente secondes pour Xu, un échec pour sa mère — sur exactement la même borne.",
  "Tester un objet uniquement avec ceux qui le connaissent déjà.",
  ["",
   "Ce serait généraliser à tort : Xu y arrive très bien, et le verbatim dit précisément que l'objet convient à certains et pas à d'autres.",
   "Attribuer l'échec à la personne évite d'examiner l'objet — or c'est l'objet, ici, qu'on est chargé d'améliorer.",
   "Ce verbatim est au contraire l'un des plus utiles de la série : il désigne un profil d'usager que la conception a oublié."],
  "Un objet facile pour l'habitué peut être infranchissable pour un autre.")

q("C2.1", "Le schéma", "Découper le parcours en étapes nommées sert d'abord à…",
  ["ce que tout le monde parle du même endroit du parcours",
   "rendre le parcours plus rapide",
   "supprimer les étapes inutiles",
   "présenter un document propre au professeur"],
  "Sans découpage commun, douze témoignages restent douze histoires. Le schéma leur donne une "
  "adresse commune, et rend les comparaisons possibles.",
  "« C'est trop long » devient « l'étape déverrouiller est trop longue ».",
  "Comparer des récits qui ne parlent pas du même moment.",
  ["",
   "Le découpage ne change rien à la durée : il permet seulement de voir où elle se loge, ce qui est un préalable à toute amélioration.",
   "On ne supprime rien à ce stade : le découpage sert à décrire ce qui existe, pas encore à décider ce qu'il faut changer.",
   "La présentation n'est pas le but ; un schéma mal fait mais partagé sert mieux qu'un beau schéma que personne n'utilise."],
  "Le schéma donne une adresse commune aux témoignages.")

q("C2.1", "Ce que le schéma ne dit pas", "Une fois le parcours découpé en cinq étapes, ce qui manque encore, c'est…",
  ["où part le temps",
   "les mots des usagers",
   "le nom des étapes",
   "rien : le schéma suffit"],
  "Chaque représentation appelle la suivante par ce qui lui manque. Le schéma range, il ne mesure "
  "pas.",
  "On sait qu'il y a une étape « déverrouiller » ; on ignore qu'elle peut durer 83 s.",
  "S'arrêter au schéma en croyant avoir décrit l'expérience.",
  ["",
   "Les mots ont été recueillis à l'étape précédente : ils sont acquis, et c'est même à partir d'eux qu'on a construit le découpage.",
   "Les étapes viennent justement d'être nommées : c'est ce que le schéma apporte, ce n'est pas ce qui lui manque.",
   "Si le schéma suffisait, le programme ne demanderait pas d'aboutir aussi aux graphiques et aux algorithmes."],
  "Le schéma range, il ne mesure pas.",
  img=IMG_TRAJET)

q("C2.1", "Pourquoi le pire cas", "Sur un graphique de durées, tracer le maximum à côté de la moyenne sert à…",
  ["montrer ce que vivent les usagers les plus mal servis, que la moyenne efface",
   "remplir le graphique",
   "vérifier que la moyenne est juste",
   "comparer deux objets différents"],
  "Une moyenne décrit le milieu d'une série, et personne ne vit le milieu. Le maximum dit ce que "
  "subissent ceux qui se plaignent.",
  "Déverrouiller : 29 s de moyenne, 83 s au pire — presque le triple.",
  "Décider à partir des seules moyennes.",
  ["",
   "Un graphique n'a pas à être rempli : chaque élément tracé doit apporter une information, et c'est justement le cas de celui-là.",
   "Le maximum ne vérifie pas la moyenne, il la complète : les deux sont exacts, ils décrivent simplement deux choses différentes.",
   "Comparer deux objets est un autre usage ; ici, les deux barres décrivent le même objet vu sous deux angles."],
  "Personne ne vit la moyenne.")

q("C2.1", "Lire le graphique", "Sur la borne de Hangzhou, l'étape la plus longue en moyenne est…",
  ["« choisir », avec environ 40 secondes",
   "« déverrouiller », avec environ 40 secondes",
   "« identifier », avec environ 40 secondes",
   "« arriver », avec environ 40 secondes"],
  "C'est le résultat qui surprend le plus : l'étape la plus coûteuse en temps n'est pas celle dont "
  "on se plaint.",
  "Choisir 40 s · déverrouiller 29 s · identifier 14 s · partir 13 s · arriver 8 s.",
  "Confondre l'étape la plus longue et l'étape la plus critiquée.",
  ["",
   "Déverrouiller n'est qu'à 29 s de moyenne : c'est son MAXIMUM (83 s) qui est le plus élevé, pas sa moyenne.",
   "Identifier est à 14 s : c'est l'une des étapes les plus rapides, malgré l'hésitation qu'elle provoque chez les nouveaux venus.",
   "Arriver est l'étape la plus courte de toutes, à 8 s en moyenne."],
  "La plus longue est « choisir » — et personne ne s'en plaint.",
  img=IMG_GRAPH)

q("C2.1", "La queue de la moyenne", "L'étape « déverrouiller » monte à 83 s au maximum pour 29 s de moyenne. Pourquoi ?",
  ["parce que 9 retraits sur 30 ont demandé une reprise, ce qui allonge fortement ces cas-là",
   "parce que la moyenne a été mal calculée",
   "parce que les usagers sont lents à cette étape",
   "parce que le chronomètre a été mal utilisé"],
  "Quand une minorité de cas échoue et recommence, la moyenne bouge peu et le maximum explose. "
  "C'est la signature d'un problème de fiabilité.",
  "Vingt-et-un retraits en 25 s, neuf qui doublent ou triplent : la moyenne reste basse.",
  "Croire qu'une moyenne basse signifie qu'il n'y a pas de problème.",
  ["",
   "La moyenne est exacte : c'est justement parce qu'elle est correctement calculée qu'elle masque les cas extrêmes — c'est sa nature, pas une erreur.",
   "La lenteur des usagers ne créerait pas cet écart : elle décalerait toute la série, et pas seulement neuf relevés sur trente.",
   "Une erreur de chronométrage se répartirait au hasard sur les cinq étapes, alors que l'écart se concentre sur une seule et coïncide avec la colonne des reprises."],
  "Une moyenne cache sa queue.")

q("C2.1", "Ressenti contre mesure", "Le graphique des durées, comparé aux verbatims…",
  ["dit ce qui se passe, mais pas ce que les gens ressentent",
   "remplace les verbatims, devenus inutiles",
   "dit la même chose, en plus précis",
   "les contredit, il faut donc choisir"],
  "Les deux se croisent sans se remplacer. C'est même l'intérêt de les avoir tous les deux : "
  "l'écart entre eux est une information.",
  "Le graphique ignore la colère de Chen ; Chen ignore les 41 s de « choisir ».",
  "Croire qu'une mesure rend le témoignage superflu.",
  ["",
   "Sans les verbatims, on corrigerait l'étape la plus longue — « choisir » — dont personne ne se plaint : la mesure seule conduit ici à la mauvaise décision.",
   "Ils ne disent pas la même chose : l'un porte sur des durées, l'autre sur du vécu, et les deux étapes qu'ils désignent ne sont pas les mêmes.",
   "Il n'y a pas de contradiction à trancher : les deux sont vrais, et c'est leur écart qui constitue le résultat le plus utile de l'enquête."],
  "Un ressenti n'est pas une mesure — et l'écart entre les deux informe.")

q("C2.1", "L'algorithme", "Écrire le parcours sous forme d'algorithme apporte ce que le graphique ne donnait pas :",
  ["les cas d'échec deviennent visibles, donc traitables",
   "les durées exactes de chaque étape",
   "le ressenti des usagers",
   "le nombre de personnes interrogées"],
  "Un algorithme force à dire ce qui se passe quand ça rate. Le graphique montrait un pic ; "
  "l'algorithme dit ce que la machine fait pendant ce pic.",
  "« Si l'ancrage ne s'ouvre pas → annoncer la cause, puis proposer de réessayer. »",
  "Ne dessiner que le chemin où tout se passe bien.",
  ["",
   "Les durées venaient de l'étape précédente : un algorithme décrit un enchaînement de décisions, il ne porte pas de chronomètre.",
   "Le ressenti a été recueilli au tout début, et aucun algorithme ne saura l'exprimer : c'est précisément ce qu'il ne sait pas dire.",
   "Le nombre de personnes interrogées relève de la méthode d'enquête, pas de la représentation du fonctionnement."],
  "L'algorithme rend les échecs visibles, donc traitables.")

q("C2.1", "Les formes de l'algorigramme", "Dans un algorigramme, « la carte est-elle reconnue ? » se dessine avec…",
  ["un losange, parce que c'est un test à deux sorties",
   "un rectangle, parce que c'est une action",
   "un ovale, parce que c'est un début",
   "une flèche, parce que c'est un passage"],
  "Chaque forme dit sa nature : ovale pour le début et la fin, rectangle pour une action, losange "
  "pour un test. La forme EST une information.",
  "Toute phrase qui se termine par un point d'interrogation appelle un losange.",
  "Dessiner un test en rectangle, ce qui masque ses deux sorties.",
  ["",
   "Un rectangle représente une action que la machine exécute sans se poser de question ; ici la machine doit décider, et une décision a deux issues.",
   "L'ovale marque une entrée ou une sortie du parcours, pas un point de décision au milieu.",
   "Une flèche relie deux cases : elle ne porte pas de contenu, elle indique seulement l'ordre."],
  "Un test se dessine en losange.")

q("C2.1", "Le test sans sortie", "Un algorigramme dont un test n'a qu'une seule sortie…",
  ["est faux : un test a toujours deux sorties, et le cas « non » doit être traité",
   "est correct si le cas « non » est rare",
   "est correct : on simplifie pour la lisibilité",
   "dépend du logiciel utilisé"],
  "Un test dont une branche ne mène nulle part n'est pas un test : c'est un vœu. La branche "
  "oubliée est exactement celle où l'usager se retrouve bloqué.",
  "Sans sortie d'échec, la reprise boucle : c'est ce que Sun a vécu en recommençant trois fois.",
  "Ne dessiner que la branche « oui ».",
  ["",
   "La rareté ne change rien : ici le cas rare arrive à 9 usagers sur 30, et ce sont eux qui écrivent au service client.",
   "Cette simplification supprime précisément l'information la plus utile ; un algorigramme complet reste lisible si on l'organise bien.",
   "La règle des deux sorties est une règle de représentation, indépendante de l'outil avec lequel on dessine."],
  "Un test a deux sorties, et la sortie « non » mène quelque part.")

q("C2.1", "On n'efface pas les étapes", "Une fois l'algorithme écrit, les verbatims et le schéma…",
  ["restent utiles : chaque représentation garde ce que les autres ne savent pas dire",
   "peuvent être jetés : l'algorithme les résume",
   "doivent être refaits à partir de l'algorithme",
   "ne servaient qu'à occuper la première séance"],
  "Le trajet n'est pas un remplacement successif, c'est un empilement. À la fin, on dispose de "
  "quatre regards complémentaires sur le même objet.",
  "L'algorithme ne dira jamais que Chen doute de lui-même ; le verbatim ne dira jamais 83 s.",
  "Croire que la représentation la plus technique contient toutes les autres.",
  ["",
   "L'algorithme ne contient ni les durées, ni les mots, ni les ressentis : il décrit un enchaînement de décisions, et rien de plus.",
   "Refaire les verbatims à partir de l'algorithme serait inventer des témoignages : le sens de marche ne s'inverse pas.",
   "Les verbatims servent jusqu'à la dernière séance : ce sont eux qui rattachent chaque exigence à une attente d'utilisateur."],
  "Chaque représentation garde ce que les autres ne savent pas dire.")

# ═══════════ 4e_C2.2 — repérer et expliquer les exigences (15) ═══════════

q("C2.2", "Les six familles", "Les familles d'exigences nommées par le programme sont…",
  ["sécurité, incidences environnementales, formes et fonctions, ergonomie, qualité, fiabilité",
   "prix, solidité, couleur, poids, taille, marque",
   "mécanique, électrique, informatique, chimique",
   "conception, fabrication, vente, recyclage"],
  "Six familles, six questions différentes à poser au même objet. Les connaître, c'est disposer "
  "d'une grille qui empêche d'oublier une dimension.",
  "Un même écran relève des formes et fonctions (lisible) et des incidences (consommation).",
  "N'examiner qu'une ou deux familles, et croire l'objet couvert.",
  ["",
   "Ce sont des caractéristiques d'un produit, pas des familles d'exigences : le prix ou le poids traversent plusieurs familles à la fois, ils n'en constituent aucune.",
   "Ce sont des domaines technologiques, c'est-à-dire des MOYENS ; les familles d'exigences désignent au contraire ce qu'on attend de l'objet.",
   "Ce sont des étapes du cycle de vie : elles disent QUAND les exigences produisent leurs effets, pas sur quoi elles portent."],
  "Sécurité, incidences environnementales, formes et fonctions, ergonomie, qualité, fiabilité.",
  img=IMG_EXIG)

q("C2.2", "Ce qu'est une exigence", "Une exigence bien écrite…",
  ["dit ce qui est attendu, se vérifie, et nomme l'attente d'utilisateur à laquelle elle répond",
   "décrit la solution technique à installer",
   "reste large, pour ne pas contraindre le concepteur",
   "se contente de citer une famille du programme"],
  "Trois exigences de forme, et elles tiennent ensemble : sans vérifiabilité, personne ne saura si "
  "elle est tenue ; sans attente nommée, personne ne saura pourquoi elle existe.",
  "« Le déverrouillage doit réussir au moins 98 fois sur 100 » — fiabilité, pour Chen (V01).",
  "Écrire une intention vague qu'aucune mesure ne pourra départager.",
  ["",
   "Décrire la solution ferme le champ des possibles avant même d'avoir cherché : on décide du moyen sans avoir défini le but.",
   "Une exigence volontairement large ne se vérifie pas, donc ne s'oppose à rien : elle laisse le concepteur libre de dire qu'il l'a respectée.",
   "Citer une famille dit dans quel domaine on se place, pas ce qu'on attend : « c'est une question d'ergonomie » n'engage personne."],
  "Attendu, vérifiable, rattaché à une attente.")

q("C2.2", "Exigence ou solution", "« Installer un lecteur de carte plus rapide » n'est pas une exigence parce que…",
  ["c'est déjà une solution : une exigence dit le besoin, pas le moyen",
   "c'est trop cher pour une collectivité",
   "le lecteur n'est pas en cause dans le problème",
   "cela relève de la sécurité, pas de la qualité"],
  "Confondre exigence et solution, c'est décider avant d'avoir cherché — et se priver de toutes "
  "les autres réponses possibles au même besoin.",
  "Exigence : « l'identification doit aboutir en moins de 10 s ». Solution : le lecteur choisi.",
  "Écrire ce qu'on a envie d'acheter à la place de ce qu'il faut obtenir.",
  ["",
   "Le coût n'est pas le critère : une solution gratuite resterait une solution, et le problème est qu'elle ferme le champ des possibles.",
   "Le lecteur est bien concerné par l'étape « identifier » ; ce n'est pas la pertinence technique qui est en cause, c'est la nature de la phrase.",
   "Le classement en famille ne change rien : quelle que soit la famille, une phrase qui nomme un composant à installer reste une solution."],
  "Une exigence dit le besoin ; la solution dira comment.")

q("C2.2", "La fiabilité se chiffre", "« Le déverrouillage doit réussir au moins 98 fois sur 100 » relève de…",
  ["la fiabilité, et cette exigence se vérifie par un comptage",
   "l'ergonomie, car c'est un geste de l'usager",
   "la sécurité, car un blocage est dangereux",
   "la qualité, car il s'agit de bien faire"],
  "La fiabilité répond à une question précise : combien de fois sur cent l'objet échoue-t-il ? "
  "Elle s'écrit donc toujours avec un nombre.",
  "Aujourd'hui : 21 réussites sur 30, soit 70 %. L'écart avec 98 % chiffre le travail à faire.",
  "Écrire « la borne doit être fiable », qui ne se vérifie pas.",
  ["",
   "L'ergonomie porte sur l'adaptation au corps et aux gestes ; ici ce n'est pas le geste qui est en cause, c'est le fait que la machine réussisse ou non.",
   "Un ancrage bloqué est agaçant plus que dangereux ; la sécurité concerne les situations où quelqu'un peut se blesser.",
   "La qualité porte sur le fait que l'objet fasse ce qu'il annonce et informe correctement ; le taux de réussite a sa propre famille."],
  "La fiabilité se compte, donc elle se chiffre.")

q("C2.2", "La qualité informe", "« Pendant une attente, la borne doit afficher le temps restant » relève de…",
  ["la qualité : l'objet doit faire ce qu'il annonce, et informer sur ce qu'il fait",
   "la sécurité",
   "les incidences environnementales",
   "rien du tout : c'est un détail d'affichage"],
  "Informer fait partie du service rendu. Une machine qui travaille sans le dire laisse l'usager "
  "dans l'incertitude, et c'est cette incertitude qui se raconte.",
  "C'est l'exigence qui répond exactement à Feng (V12).",
  "Traiter l'information donnée à l'usager comme un ornement.",
  ["",
   "Aucune blessure n'est en jeu ici : la sécurité concerne les situations où l'intégrité physique est menacée.",
   "Un affichage supplémentaire consomme même un peu plus d'énergie : cette exigence ne relève pas des incidences environnementales.",
   "C'est au contraire l'exigence qui répond au verbatim le plus précis de l'enquête : Feng dit que l'incertitude le gêne plus que la durée."],
  "Informer sur ce qu'on fait, c'est une exigence de qualité.")

q("C2.2", "L'ergonomie", "« Le retrait doit pouvoir se faire d'une seule main » relève de l'ergonomie et répond à…",
  ["Deng, qui a une main prise par son enfant",
   "Ma, le livreur, qui veut aller vite",
   "Guo, le touriste, qui ne lit pas les pictogrammes",
   "personne : c'est une idée de concepteur"],
  "Une exigence d'ergonomie part d'un corps réel dans une situation réelle — pas d'un usager moyen "
  "qui aurait toujours deux mains libres.",
  "« J'ai une main prise. Tout demande deux mains. » (V11)",
  "Concevoir pour un usager idéal, disponible et sans contrainte.",
  ["",
   "Ma se plaint du temps, pas du geste : son verbatim porte sur l'étape « choisir », qu'il trouve d'ailleurs pratique.",
   "Guo bute sur la signalétique, ce qui relève de la lisibilité et non du nombre de mains nécessaires.",
   "Cette exigence vient au contraire directement d'un verbatim, et c'est ce qui lui donne sa légitimité."],
  "L'ergonomie part d'un corps réel, pas d'un usager idéal.")

q("C2.2", "Les incidences environnementales", "« L'écran ne s'allume qu'à l'approche d'un usager » relève de…",
  ["les incidences environnementales : moins d'énergie consommée sur la durée de vie",
   "la fiabilité",
   "la sécurité",
   "l'ergonomie uniquement"],
  "Cette famille regarde ce que l'objet coûte en matière et en énergie, sur toute sa durée de vie "
  "— pas seulement au moment de sa fabrication.",
  "Un écran allumé nuit et jour pendant dix ans, contre un écran qui se réveille au besoin.",
  "Réduire les incidences environnementales au seul recyclage final.",
  ["",
   "La fiabilité porte sur le taux d'échec ; un écran en veille n'échoue pas davantage, il consomme seulement moins.",
   "Aucun risque physique n'est en jeu ; un écran éteint pourrait même poser une question de lisibilité, mais pas de sécurité.",
   "Le confort de lecture est un effet secondaire agréable, mais ce qui motive ce choix, c'est l'énergie économisée sur des années."],
  "La matière et l'énergie, sur toute la durée de vie.",
  img=IMG_EXIG)

q("C2.2", "Formes et fonctions", "« L'écran doit rester lisible sous la pluie et sans se pencher » relève surtout de…",
  ["les formes et fonctions : la forme de l'objet doit servir ce qu'il doit faire",
   "les incidences environnementales",
   "la fiabilité",
   "la sécurité"],
  "Cette famille demande si la forme donnée à l'objet sert réellement sa fonction — ici, un écran "
  "sert à être lu, y compris quand il pleut.",
  "Un écran plat et bas remplit sa fonction par beau temps seulement.",
  "Juger une forme sans se demander à quoi elle sert.",
  ["",
   "Ni la matière ni l'énergie ne sont en cause : incliner un écran ou l'abriter ne change pas sa consommation.",
   "L'écran fonctionne parfaitement sous la pluie : il est illisible, ce qui est un problème de forme et non de panne.",
   "Un écran illisible est gênant, mais il ne met personne en danger ; la sécurité concerne le risque physique."],
  "La forme doit servir la fonction, y compris quand il pleut.")

q("C2.2", "La sécurité", "Sur la borne, une exigence de sécurité serait…",
  ["« l'ancrage doit libérer le vélo sans qu'il bascule sur les pieds de l'usager »",
   "« la borne doit être disponible sept jours sur sept »",
   "« l'écran doit afficher le tarif »",
   "« le vélo doit avoir une selle réglable »"],
  "La sécurité pose une question et une seule : quelqu'un peut-il se blesser ou être mis en "
  "danger ? Si la réponse est non, c'est une autre famille.",
  "Un vélo de 20 kg qui bascule au déverrouillage, c'est un pied écrasé.",
  "Classer en sécurité tout ce qui semble important.",
  ["",
   "La disponibilité relève de la fiabilité du service : une borne indisponible est gênante, elle ne blesse personne.",
   "L'affichage du tarif relève de la qualité de l'information donnée à l'usager avant qu'il s'engage.",
   "Une selle réglable est une exigence d'ergonomie : elle adapte l'objet au corps, sans qu'un danger soit en cause."],
  "Sécurité : quelqu'un peut-il se blesser ?")

q("C2.2", "Deux familles à la fois", "Une exigence peut-elle relever de deux familles ?",
  ["oui : un écran lisible sans se pencher sert les formes et fonctions et l'ergonomie",
   "non : chaque exigence appartient à une seule famille",
   "oui, mais seulement sécurité et fiabilité",
   "non, sauf erreur de rédaction"],
  "Les familles se recoupent souvent. L'exercice consiste alors à dire laquelle domine, et "
  "pourquoi — pas à choisir au hasard.",
  "« Lisible sans se pencher » : c'est la forme de l'objet, et c'est le dos de Wu (V07).",
  "Chercher à tout prix une case unique.",
  ["",
   "Rien n'impose qu'une exigence ne produise qu'un effet : une même contrainte peut servir plusieurs attentes en même temps.",
   "Le recoupement peut concerner n'importe quelle paire : ergonomie et formes, qualité et fiabilité, sécurité et ergonomie.",
   "Servir deux familles est le signe d'une exigence bien trouvée, pas d'une maladresse d'écriture."],
  "Quand deux familles se recoupent, dis laquelle domine.")

q("C2.2", "Remonter à l'attente", "Ce qui rattache une exigence à un utilisateur, dans notre travail, c'est…",
  ["le code du verbatim où cet utilisateur exprime son attente",
   "l'avis du professeur",
   "le nom de la famille d'exigences",
   "le chiffre que contient l'exigence"],
  "Une exigence sans attente nommée flotte : personne ne peut dire pourquoi elle existe, ni la "
  "défendre quand elle coûte cher.",
  "« ...répond à Deng (V11), qui tient son enfant. »",
  "Écrire des exigences plausibles qui ne viennent d'aucun usager.",
  ["",
   "L'avis d'un tiers ne prouve pas qu'un utilisateur a exprimé ce besoin : c'est précisément ce qu'on cherche à éviter en recueillant des verbatims.",
   "La famille dit de quel type d'exigence il s'agit, pas à qui elle profite ; deux exigences de la même famille peuvent servir des usagers opposés.",
   "Un chiffre rend l'exigence vérifiable, ce qui est nécessaire mais ne dit toujours pas pourquoi ce seuil-là et pas un autre."],
  "Une exigence nomme l'attente à laquelle elle répond.")

q("C2.2", "Une exigence sans plainte", "Peut-on écrire une exigence qu'aucun usager n'a réclamée ?",
  ["oui : les usagers ne réclament pas ce qui ne les gêne pas, comme la consommation de l'écran",
   "non : toute exigence doit venir d'un verbatim",
   "oui, mais elle est forcément moins importante",
   "non : ce serait inventer un besoin"],
  "Certaines exigences protègent des tiers, l'environnement ou l'avenir — c'est-à-dire des "
  "intérêts que l'usager du moment ne porte pas.",
  "Personne ne se plaint qu'un écran reste allumé la nuit : ce n'est pas lui qui paie la facture.",
  "Croire que le cahier des charges se déduit entièrement des plaintes.",
  ["",
   "Ce serait réduire la conception aux seules gênes exprimées : la consommation d'énergie ou la recyclabilité ne gênent personne sur le moment.",
   "Elle peut au contraire être décisive : une exigence environnementale engage l'objet sur toute sa durée de vie, bien au-delà d'un désagrément ponctuel.",
   "Inventer un besoin serait écrire une exigence sans raison ; ici la raison existe, elle est simplement portée par d'autres que l'usager immédiat."],
  "Les usagers ne réclament pas ce qui ne les gêne pas.")

q("C2.2", "La plus grosse donnée", "L'étape « choisir » est la plus longue de toutes, et pourtant elle n'appelle aucune exigence urgente. Pourquoi ?",
  ["parce que personne ne s'en plaint, et qu'un usager la trouve même pratique",
   "parce que 40 secondes, ce n'est pas beaucoup",
   "parce qu'on ne peut rien y changer techniquement",
   "parce que le programme ne s'intéresse pas au temps"],
  "C'est le résultat le plus contre-intuitif de l'enquête, et le plus utile : la donnée la plus "
  "grosse n'est pas toujours le problème.",
  "Wang s'en plaint, Ma s'en félicite, et le service client ne reçoit rien à ce sujet.",
  "Traiter d'abord ce qui se voit le plus sur le graphique.",
  ["",
   "Quarante secondes est au contraire la plus longue durée du parcours : c'est bien un temps important, et c'est ce qui rend le résultat surprenant.",
   "On pourrait très bien raccourcir cette étape, par exemple en triant les vélos ; ce n'est pas la faisabilité qui est en cause, c'est l'utilité.",
   "Le temps est au contraire au cœur de la séquence : c'est le croisement du temps et du ressenti qui permet de hiérarchiser."],
  "La donnée la plus grosse n'est pas toujours le problème.")

q("C2.2", "Hiérarchiser", "Pour décider par quoi commencer, la meilleure façon de faire est de…",
  ["croiser ce que disent les usagers avec ce que montrent les mesures",
   "traiter les étapes dans l'ordre du parcours",
   "commencer par l'étape la plus longue",
   "commencer par ce qui coûte le moins cher"],
  "Ni les mots seuls, ni les chiffres seuls ne suffisent : c'est leur croisement qui désigne ce "
  "qui compte vraiment.",
  "Trois verbatims ET un maximum à 83 s : « déverrouiller » se désigne tout seul.",
  "Hiérarchiser à partir d'une seule source d'information.",
  ["",
   "L'ordre du parcours est arbitraire au regard de l'importance : rien ne dit que la première étape soit la plus problématique.",
   "La plus longue est ici « choisir », dont personne ne se plaint : commencer par elle reviendrait à dépenser pour un non-problème.",
   "Le coût est un critère de faisabilité, utile plus tard ; commencer par le moins cher revient à traiter ce qui est facile plutôt que ce qui compte."],
  "On hiérarchise en croisant les mots et les mesures.")

q("C2.2", "Ce que l'exigence engage", "Écrire « le déverrouillage doit réussir 98 fois sur 100 » engage à…",
  ["pouvoir le vérifier plus tard, par un comptage sur des retraits réels",
   "installer immédiatement un nouveau modèle d'ancrage",
   "garantir que plus aucun usager ne se plaindra",
   "rien : une exigence est une intention"],
  "Une exigence chiffrée crée une obligation de vérification. C'est ce qui la distingue d'un "
  "souhait, et c'est aussi ce qui la rend exigeante pour celui qui l'écrit.",
  "Trente retraits observés après travaux, et l'on saura si le seuil est tenu.",
  "Écrire un seuil qu'on n'a aucun moyen de mesurer.",
  ["",
   "L'exigence ne prescrit aucun moyen : changer d'ancrage est une solution possible parmi d'autres, et ce choix vient après.",
   "Aucune exigence ne peut promettre l'absence totale de plaintes ; elle fixe un seuil vérifiable, ce qui est déjà beaucoup.",
   "C'est justement l'inverse : ce qui sépare une exigence d'une intention, c'est qu'on puisse constater si elle est tenue ou non."],
  "Un seuil écrit est un seuil à vérifier.")

assert len(Q) == 30, len(Q)
assert sum(1 for x in Q if x["c"] == "C2.1") == 15, sum(1 for x in Q if x["c"] == "C2.1")
assert sum(1 for x in Q if "img" in x) == 5
