# -*- coding: utf-8 -*-
"""Les 30 questions du QCM 5e_C2.1 · C2.2 — Shenzhen, la station de vélos.

Écrites à la main. Toutes les bonnes réponses sont en position 0 ici :
la répartition sur A/B/C/D est faite ensuite par `_outils/fix_r.js`,
de façon déterministe, à partir d'une graine.

Règle tenue pour chaque distracteur : la réfutation EXPLIQUE pourquoi la
réponse est fausse. Une réfutation courte (« Aucun rapport. ») est un aveu
que l'auteur n'a pas cherché ce que l'élève avait en tête.
"""

IMG_INT = {
    "src": "Images/interacteurs_de_la_station.svg",
    "alt": "Autour de la station de vélos, trois groupes d'interacteurs : des personnes "
           "(usager, agent de maintenance, riverain), des objets (vélo, borne, trottoir, "
           "réseau, alimentation électrique) et des conditions (pluie, sel marin, "
           "température, vandalisme, règles de la ville).",
}
IMG_CHX = {
    "src": "Images/lire_un_choix_de_conception.svg",
    "alt": "Tableau à quatre colonnes : ce que j'observe, pourquoi pas autrement, "
           "l'interacteur concerné, le domaine de conception, avec quatre exemples pris "
           "sur la station de vélos.",
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


# ═══════════════════════ C2.1 — recenser les interacteurs (15) ═══════════════════════

q("C2.1", "Définition", "Un interacteur d'un objet technique, c'est…",
  ["tout ce qui, à l'extérieur de l'objet, entre en relation avec lui",
   "chacune des pièces qui composent l'objet",
   "la personne qui a conçu l'objet",
   "le lieu où l'objet est installé"],
  "Le mot le dit : ce qui inter-agit. La condition décisive est d'être EXTÉRIEUR à l'objet — "
  "sinon on décrit l'objet lui-même, pas ses relations.",
  "Pour une station de vélos : l'usager, la pluie, le trottoir, le réseau informatique.",
  "Citer une pièce de l'objet (la borne, l'écran) comme si c'était un interacteur.",
  ["",
   "Une pièce est à l'intérieur de l'objet : elle en fait partie. Un interacteur est extérieur, et c'est ce qui le définit.",
   "Le concepteur est en relation avec le projet, pas avec l'objet en service. Ce sont les utilisateurs, la pluie ou le réseau qui agissent sur lui une fois installé.",
   "Le lieu est un seul interacteur parmi d'autres, et il n'en épuise pas la liste : le réseau ou l'usager ne sont pas des lieux."],
  "Un interacteur est toujours EXTÉRIEUR à l'objet.",
  img=IMG_INT)

q("C2.1", "Les trois natures", "Une liste complète d'interacteurs comporte…",
  ["des personnes, d'autres objets, et des conditions ou contraintes",
   "uniquement des personnes qui utilisent l'objet",
   "des objets neufs, des objets usagés et des objets cassés",
   "des interacteurs proches, moyens et lointains"],
  "Trois natures, également légitimes. Aucune n'est plus « technique » que les autres, et c'est "
  "en les passant en revue une par une qu'on cesse d'oublier la moitié de la liste.",
  "Usager (personne), trottoir (objet), sel marin (condition).",
  "S'arrêter à la première nature qui vient — presque toujours les personnes.",
  ["",
   "C'est justement le réflexe qui fait manquer la moitié de la liste : la pluie, le réseau ou le trottoir agissent sur la station sans être des personnes.",
   "L'état d'un objet (neuf, usagé, cassé) ne dit rien de sa relation avec l'objet étudié : un trottoir neuf et un trottoir usé sont tous deux le même interacteur.",
   "La distance n'est pas une nature : le réseau informatique est lointain et pourtant décisif, la couleur du cadre est toute proche et n'est pas un interacteur."],
  "Personnes, objets, conditions : les trois comptent.",
  img=IMG_INT)

q("C2.1", "Ce qui n'en est pas un", "Parmi ces propositions, laquelle n'est PAS un interacteur de la station ?",
  ["la couleur du cadre des vélos",
   "l'agent de maintenance",
   "la pluie",
   "le trottoir sur lequel la station est fixée"],
  "La couleur du cadre est une caractéristique de l'objet lui-même. Elle est dedans, pas dehors : "
  "elle ne peut donc pas être en relation avec lui.",
  "Comparer : la pluie mouille la borne (relation), la couleur du cadre EST le vélo (pas de relation).",
  "Confondre une caractéristique de l'objet avec un interacteur.",
  ["",
   "L'agent de maintenance ouvre le boîtier et sort les vélos bloqués : il agit sur la station, il est donc bien un interacteur.",
   "La pluie mouille les bornes et peut les bloquer — c'est précisément la panne relevée par le service technique. Elle agit sur l'objet.",
   "La station est fixée au trottoir, et la largeur de ce trottoir limite l'espace disponible : le trottoir la porte et la contraint."],
  "Une caractéristique de l'objet n'est pas un interacteur.")

q("C2.1", "Un interacteur non vivant", "La pluie est un interacteur de la station parce que…",
  ["elle agit sur elle : elle mouille les bornes et peut les bloquer",
   "elle est citée dans le relevé du service technique",
   "tout ce qui vient du ciel compte comme interacteur",
   "elle empêche les usagers de venir"],
  "Ce qui fait l'interacteur, c'est l'ACTION exercée sur l'objet ou subie de lui — pas le fait "
  "d'être vivant, ni d'être mentionné quelque part.",
  "L'eau stagne sur le lecteur de carte : la borne cesse de lire les badges.",
  "Croire qu'un interacteur doit être quelqu'un.",
  ["",
   "Être cité dans un document ne crée pas la relation : c'est la relation qui a fait qu'on l'a cité. Sans action sur la station, la pluie n'y figurerait pas.",
   "Le critère n'est pas la provenance mais l'action exercée : le soleil vient du ciel et agit, un satellite aussi vient du ciel et n'agit pas sur cette station.",
   "Ce serait une relation avec les usagers, pas avec la station. Or c'est bien la borne, et non l'usager, qui est bloquée par l'eau."],
  "Un interacteur n'a pas besoin d'être vivant.")

q("C2.1", "Un interacteur invisible", "Le réseau informatique auquel la borne est reliée…",
  ["est un interacteur : sans lui, la borne ne peut ni identifier l'usager ni débloquer un vélo",
   "n'est pas un interacteur, car on ne le voit pas",
   "fait partie de la station elle-même",
   "ne compte que les jours où la connexion est coupée"],
  "Un interacteur peut être immatériel. Le test est toujours le même : si on l'enlève, l'objet "
  "rend-il encore son service ?",
  "Réseau coupé : la borne s'allume toujours, mais plus aucun vélo ne sort.",
  "Ne recenser que ce qu'on peut toucher.",
  ["",
   "La visibilité n'est pas un critère : l'électricité non plus ne se voit pas, et personne ne doute qu'elle soit indispensable à la borne.",
   "Le réseau existe en dehors de la station et sert bien d'autres usages en ville : il n'est pas une pièce de la station, il est ce avec quoi elle dialogue.",
   "Il agit en permanence, y compris quand tout va bien — c'est justement parce qu'il fonctionne que la borne rend son service le reste du temps."],
  "Un interacteur peut être invisible.")

q("C2.1", "Le réflexe coûteux", "Le réflexe qui fait manquer la moitié de la liste, c'est…",
  ["ne citer que des personnes",
   "citer trop d'objets",
   "commencer par la pluie",
   "faire une liste trop longue"],
  "Presque tous les élèves commencent par les humains. Le remède est mécanique : après avoir "
  "listé les personnes, se forcer à chercher deux objets et deux conditions.",
  "Une première liste typique : « l'usager, le technicien, le maire ». Trois personnes, zéro objet, zéro condition.",
  "Rendre une liste où toutes les entrées sont des humains.",
  ["",
   "Il n'y a pas d'excès à craindre de ce côté : les objets sont justement l'une des trois natures attendues, et ils sont plutôt sous-représentés dans les listes d'élèves.",
   "L'ordre est sans importance : commencer par une condition est même un bon moyen d'échapper au réflexe des personnes.",
   "Une liste longue n'est pas un défaut si elle est variée ; le défaut serait une liste longue qui répète dix fois la même nature."],
  "Une liste qui ne contient que des personnes est une liste à moitié faite.")

q("C2.1", "Longueur ou variété", "Une liste de dix interacteurs qui sont tous des personnes…",
  ["est incomplète : il lui manque deux des trois natures",
   "est excellente, car elle est longue",
   "est acceptable si les dix personnes sont différentes",
   "est fausse : dix interacteurs, c'est trop"],
  "Ce qu'on juge, c'est la couverture des trois natures, pas le nombre d'entrées.",
  "Six interacteurs bien répartis valent mieux que dix personnes alignées.",
  "Compter les lignes au lieu de compter les natures.",
  ["",
   "La longueur ne prouve rien sur la couverture : on peut allonger indéfiniment une liste en ajoutant des variantes d'une même nature.",
   "Que les personnes soient différentes entre elles ne change rien : il manquerait toujours les objets et les conditions, c'est-à-dire ce qui alimente, menace et contraint la station.",
   "Il n'existe pas de nombre maximal d'interacteurs ; une station réelle en compte facilement une vingtaine."],
  "On juge une liste à sa couverture, pas à sa longueur.")

q("C2.1", "Ce qui alimente", "Parmi ces interacteurs, lequel ALIMENTE la station ?",
  ["l'alimentation électrique du mobilier urbain",
   "le vandalisme",
   "la largeur du trottoir",
   "le riverain qui passe devant"],
  "Trois questions font sortir les interacteurs oubliés : qu'est-ce qui alimente l'objet, "
  "qu'est-ce qui le menace, qu'est-ce qui le contraint ?",
  "Sans courant, ni écran, ni lecteur, ni verrou électrique.",
  "Oublier l'énergie et le réseau, parce qu'ils ne se voient pas.",
  ["",
   "Le vandalisme menace la station, il ne lui apporte rien : c'est un interacteur, mais de la deuxième question, pas de la première.",
   "La largeur du trottoir contraint l'implantation : elle limite ce qu'on peut installer, sans rien fournir à la station.",
   "Le riverain subit la présence de la station et peut s'en plaindre ; il ne lui fournit ni énergie ni information."],
  "Trois questions à se poser : qu'est-ce qui alimente, menace, contraint ?")

q("C2.1", "Ce qui contraint", "La règle municipale qui impose de laisser 1,40 m de passage sur le trottoir…",
  ["est un interacteur : elle limite l'emprise au sol de la station",
   "n'est pas un interacteur, car une règle n'est pas une chose",
   "concerne la mairie, pas la station",
   "ne compte que si un piéton se plaint"],
  "Une règle agit réellement sur l'objet : elle décide de sa taille et de sa place. Une contrainte "
  "invisible qui change la forme de l'objet est un interacteur de plein droit.",
  "Trottoir de 2 m, passage obligatoire de 1,40 m : il reste 60 cm pour la station.",
  "Ne recenser que des choses matérielles.",
  ["",
   "Ce n'est pas la matérialité qui compte mais l'effet produit : cette règle a modifié la largeur réelle de la station, ce qu'aucune matière n'a fait de plus concret.",
   "La mairie l'écrit, mais c'est la station qui la subit : le concepteur a dû dimensionner son mobilier pour la respecter.",
   "Elle s'applique en permanence, plainte ou pas — c'est même son intérêt : elle protège le passage avant qu'un conflit n'apparaisse."],
  "Une règle qui change la forme de l'objet est un interacteur.")

q("C2.1", "Extérieur ou intérieur", "La batterie interne qui garde l'heure de la borne est…",
  ["un composant de la station, donc pas un interacteur",
   "un interacteur, car elle fournit de l'énergie",
   "un interacteur, car on peut la changer",
   "ni l'un ni l'autre : elle est trop petite pour compter"],
  "Le critère ne change jamais : dedans ou dehors ? La batterie interne est livrée avec la borne, "
  "elle en fait partie. Le réseau électrique de la ville, lui, est dehors.",
  "Batterie interne : composant. Prise d'alimentation de la ville : interacteur.",
  "Croire que tout ce qui fournit de l'énergie est un interacteur.",
  ["",
   "Fournir de l'énergie ne suffit pas : encore faut-il venir de l'extérieur. Le moteur d'une voiture fournit l'énergie et n'est pas un interacteur de la voiture.",
   "Presque toutes les pièces d'un objet sont remplaçables ; la démontabilité ne fait pas passer un composant à l'extérieur.",
   "La taille n'entre jamais dans le critère : une puce minuscule reliée au réseau serait, elle, en relation avec l'extérieur."],
  "Le seul critère : dedans ou dehors ?")

q("C2.1", "Changer de lieu", "Installer la même station en Martinique plutôt qu'à Shenzhen…",
  ["change la liste des interacteurs : certains disparaissent, d'autres apparaissent",
   "ne change rien : c'est le même objet",
   "ne change que le nombre d'usagers",
   "supprime les interacteurs de type condition"],
  "L'objet est le même, mais l'environnement ne l'est pas — et c'est l'environnement qui fait la "
  "liste. C'est pourquoi un objet bien conçu ici peut échouer ailleurs.",
  "En Martinique apparaissent l'air salin, les pluies intenses et le cyclone.",
  "Recopier une liste d'interacteurs d'un lieu à l'autre.",
  ["",
   "L'objet est identique, mais un interacteur n'appartient pas à l'objet : il appartient à la relation, et la relation change avec le lieu.",
   "Ce serait ne voir que la nature « personnes ». Le climat, l'air marin et les règles locales changent tout autant, souvent davantage.",
   "C'est l'inverse : le changement de lieu ajoute des conditions nouvelles, comme le sel marin et le cyclone, qui n'existaient pas là-bas."],
  "Changer de lieu, c'est changer d'interacteurs.")

q("C2.1", "Un interacteur martiniquais", "Le cyclone, pour une station installée à Sainte-Luce, est…",
  ["un interacteur à part entière, différent d'une forte pluie",
   "la même chose qu'une pluie intense",
   "un événement trop rare pour être recensé",
   "un interacteur seulement pour les bâtiments"],
  "Un cyclone ajoute le vent violent et les projectiles : ce n'est pas une pluie en plus fort. Il "
  "impose des réponses techniques propres — arrimer, démonter, protéger.",
  "Une borne qui résiste à l'averse peut être arrachée par une rafale.",
  "Traiter le cyclone comme un cas extrême de pluie.",
  ["",
   "L'eau n'est qu'une partie du phénomène : le vent et les objets qu'il transporte causent des dégâts qu'aucune inclinaison de borne ne prévient.",
   "La rareté n'est pas un critère de recensement : un interacteur rare mais destructeur est justement celui qu'il faut prévoir dès la conception.",
   "Tout mobilier urbain est concerné : abribus, panneaux et stations sont précisément ce que le vent emporte en premier."],
  "Le cyclone n'est pas une pluie forte : c'est un interacteur à part.")

q("C2.1", "Le sel marin", "En bord de mer, l'air salin est un interacteur parce qu'il…",
  ["attaque les métaux de la station et accélère la corrosion",
   "rend l'air plus lourd à respirer pour les usagers",
   "modifie la couleur des vélos avec le temps",
   "n'agit que sur les bateaux"],
  "Le sel agit chimiquement sur les matériaux : il transforme l'objet sans que personne n'y touche. "
  "C'est un interacteur de la nature « condition ».",
  "Une vis en acier ordinaire rouille en quelques mois à 200 m du rivage.",
  "Choisir des matériaux sans regarder où l'objet sera installé.",
  ["",
   "L'effet sur les personnes ne concerne pas la relation avec la station : ce qui compte ici, c'est ce que le sel fait au métal de la borne.",
   "Le ternissement existe, mais il est superficiel ; le vrai problème est la corrosion, qui fait céder des pièces porteuses et des fixations.",
   "Le sel voyage dans l'air jusqu'à plusieurs centaines de mètres à l'intérieur des terres : tout mobilier littoral est concerné."],
  "L'air salin transforme l'objet sans que personne n'y touche.")

q("C2.1", "Le geste de recensement", "Pour ne rien oublier en recensant, la bonne méthode est…",
  ["de tourner autour de l'objet par la pensée et d'interroger chaque nature une par une",
   "de citer ce qui vient spontanément à l'esprit",
   "de recopier la liste d'un objet voisin",
   "de commencer par ce qui coûte le plus cher"],
  "Le recensement est un balayage méthodique, pas un souvenir. Passer les trois natures en revue "
  "évite l'angle mort des personnes.",
  "Au sol, à hauteur de main, au-dessus, sous la terre : à chaque endroit, qui ou quoi ?",
  "Se fier à sa mémoire plutôt qu'à une méthode.",
  ["",
   "Ce qui vient spontanément, ce sont les personnes : c'est exactement la source de l'oubli qu'on cherche à corriger.",
   "Deux objets voisins n'ont pas les mêmes relations : un abribus et une station de vélos partagent le trottoir et la pluie, mais pas le réseau d'identification.",
   "Le coût est un critère d'évaluation, qui vient plus tard ; pendant le recensement, un interacteur gratuit comme la pluie peut être le plus décisif."],
  "Le recensement est un balayage, pas un souvenir.")

q("C2.1", "À quoi ça sert", "Recenser les interacteurs sert d'abord à…",
  ["comprendre pourquoi l'objet a la forme qu'il a, et ce qui peut le mettre en défaut",
   "compter combien de personnes utilisent l'objet",
   "estimer le prix de fabrication de l'objet",
   "décider quelle marque acheter"],
  "La panne de la station de Shenzhen n'était dans aucun appareil : elle était dans une relation "
  "mal anticipée avec la pluie. Recenser, c'est prévoir ces défauts-là.",
  "Bornes bloquées par l'eau : rien n'est cassé, un interacteur a été oublié.",
  "Croire qu'un objet ne tombe en panne que si une pièce casse.",
  ["",
   "Le nombre d'usagers est une donnée de fréquentation ; elle n'explique ni la forme de la borne ni la panne observée.",
   "Le coût de fabrication dépend des matériaux et des procédés, qu'on choisit APRÈS avoir compris à quoi l'objet devra faire face.",
   "Choisir une marque suppose qu'on a déjà défini ce que l'objet doit affronter — c'est justement ce que le recensement établit."],
  "Un objet peut tomber en panne sans qu'aucune pièce ne casse.")

# ═══════════════════════ C2.2 — les choix de conception (15) ═══════════════════════

q("C2.2", "Lire un objet", "Repérer un choix de conception, c'est…",
  ["comprendre quelle décision explique une forme observée",
   "juger si l'objet est beau ou laid",
   "démonter l'objet pour voir l'intérieur",
   "mesurer les dimensions de l'objet"],
  "Chaque détail d'un objet a été décidé par quelqu'un, pour une raison. Lire l'objet, c'est "
  "remonter de la forme à la raison.",
  "La borne est inclinée : quelqu'un a décidé qu'elle ne serait pas plate, et on peut dire pourquoi.",
  "Décrire la forme sans jamais l'expliquer.",
  ["",
   "Le jugement esthétique est une opinion personnelle ; le choix de conception est une décision qu'on peut retrouver et justifier, même si l'objet nous déplaît.",
   "Le démontage renseigne sur la structure interne, mais la plupart des choix se lisent sur la forme extérieure, sans rien ouvrir.",
   "Une mesure donne un nombre ; encore faut-il dire pourquoi ce nombre-là plutôt qu'un autre — et c'est cette explication qui est le choix."],
  "Chaque forme est une décision.",
  img=IMG_CHX)

q("C2.2", "La question qui ouvre", "La question qui permet de repérer un choix de conception est…",
  ["pourquoi pas autrement ?",
   "combien ça coûte ?",
   "qui l'a fabriqué ?",
   "depuis quand ça existe ?"],
  "Tant qu'on n'a pas imaginé l'autre solution possible, on ne voit pas qu'il y a eu décision. "
  "La question fait apparaître l'alternative écartée.",
  "Pourquoi inclinée et pas plate ? Parce que plate, l'eau stagnerait.",
  "Regarder un détail sans se demander ce qu'il aurait pu être à la place.",
  ["",
   "Le prix intervient dans l'arbitrage final, mais il ne fait pas voir l'alternative : deux formes différentes peuvent coûter exactement le même prix.",
   "Le nom du fabricant ne dit rien de la raison d'une forme ; deux fabricants différents peuvent avoir pris la même décision pour la même raison.",
   "L'ancienneté renseigne sur l'histoire de l'objet, pas sur la raison d'un détail : une forme récente peut répondre à une contrainte très ancienne."],
  "« Pourquoi pas autrement ? » fait apparaître la décision.")

q("C2.2", "Trois domaines", "Les trois domaines de choix étudiés cette année sont…",
  ["l'ergonomie, la sécurité et l'esthétique",
   "le prix, la solidité et la couleur",
   "l'électricité, la mécanique et l'informatique",
   "la fabrication, la vente et le recyclage"],
  "Trois domaines, trois questions différentes : l'objet s'adapte-t-il au corps ? protège-t-il ? "
  "s'intègre-t-il au lieu ?",
  "Ancrage à 90 cm : ergonomie. Arêtes arrondies : sécurité.",
  "Ranger tout choix inexpliqué dans « l'esthétique ».",
  ["",
   "Ce sont des critères d'évaluation d'un produit, pas des domaines de conception : la couleur relève de l'esthétique, le prix et la solidité les traversent tous les trois.",
   "Ce sont des familles de technologies, c'est-à-dire des MOYENS ; les trois domaines désignent au contraire les raisons pour lesquelles on emploie ces moyens.",
   "Ce sont des étapes du cycle de vie de l'objet, qui décrivent quand les choix produisent leurs effets, non ce sur quoi ils portent."],
  "Ergonomie, sécurité, esthétique.")

q("C2.2", "L'ergonomie", "L'ergonomie concerne…",
  ["l'adaptation de l'objet au corps et aux gestes de celui qui l'utilise",
   "la protection contre les accidents",
   "l'apparence et l'intégration dans le lieu",
   "la durée de vie de l'objet"],
  "L'ergonomie part du corps humain : hauteurs, efforts, portées, positions. Un objet ergonomique "
  "se manipule sans se contorsionner ni forcer.",
  "L'ancrage à 90 cm est la hauteur où l'on pousse un vélo sans se baisser.",
  "Confondre ergonomie et confort décoratif.",
  ["",
   "C'est la définition de la sécurité. Les deux se rejoignent parfois — un geste plus naturel est aussi moins risqué — mais protéger d'un accident n'est pas s'adapter au corps.",
   "C'est la définition de l'esthétique. Une poignée peut être très élégante et rester épuisante à manœuvrer.",
   "La durée de vie relève de la solidité des matériaux et de l'entretien ; un objet peut durer trente ans et rester pénible à utiliser."],
  "L'ergonomie part du corps et des gestes.")

q("C2.2", "La sécurité", "Les arêtes arrondies de la station relèvent surtout de…",
  ["la sécurité : on se blesse moins en heurtant un angle arrondi",
   "l'ergonomie uniquement",
   "l'économie de matière",
   "la résistance au vent"],
  "Le domaine se lit à ce que le choix ÉVITE. Ici, il évite une blessure : c'est la sécurité.",
  "Un enfant qui court et heurte l'angle d'une borne.",
  "Attribuer à l'esthétique un choix qui évite une blessure.",
  ["",
   "L'arrondi est plus agréable en main, mais ce n'est pas ce qui a motivé la décision : on arrondit d'abord parce qu'un angle vif coupe.",
   "Arrondir un angle ne fait pas gagner de matière de façon significative, et cela demande souvent une opération de fabrication supplémentaire.",
   "L'effet aérodynamique d'un arrondi de quelques millimètres est négligeable sur un mobilier fixe de cette taille."],
  "Le domaine se lit à ce que le choix évite.")

q("C2.2", "Retrouver l'interacteur", "La borne est inclinée vers le bas plutôt que plate. Ce choix répond à…",
  ["la pluie : l'eau s'écoule au lieu de stagner sur le lecteur",
   "l'usager, qui voit mieux l'écran",
   "l'agent de maintenance, qui ouvre plus facilement",
   "l'esthétique : c'est plus joli ainsi"],
  "Derrière chaque choix, on peut nommer l'interacteur visé. Ici, une condition — et c'est "
  "précisément l'interacteur qui a été mal anticipé dans le relevé de panne.",
  "Bornes bloquées par la pluie : l'inclinaison existait, elle était insuffisante.",
  "Chercher un humain derrière chaque choix.",
  ["",
   "La lisibilité est un effet secondaire agréable, mais une inclinaison choisie pour la lecture serait orientée vers le visage, donc vers le haut, pas vers le bas.",
   "L'ouverture du boîtier dépend de la visserie et de l'accès, pas de la pente de la face avant.",
   "L'apparence n'explique pas une pente orientée vers le sol : c'est le sens de l'écoulement de l'eau qui la commande."],
  "Derrière un choix, on peut toujours nommer l'interacteur visé.",
  img=IMG_CHX)

q("C2.2", "Un choix pour la maintenance", "Le boîtier qui s'ouvre avec une vis unique répond à…",
  ["l'agent de maintenance : il intervient vite, sans outillage spécial",
   "l'usager, qui peut réparer lui-même",
   "la pluie, qui entre moins",
   "l'esthétique du boîtier"],
  "L'ergonomie ne concerne pas que l'utilisateur final : celui qui répare a lui aussi un corps, "
  "des gestes et un temps compté.",
  "Vingt minutes pour sortir un vélo : c'était le deuxième symptôme du relevé.",
  "Oublier que la maintenance est un usage à part entière.",
  ["",
   "Le boîtier reste verrouillé pour le public : rendre la réparation accessible à tous ouvrirait la porte au vandalisme et aux erreurs de manipulation.",
   "Une vis unique n'améliore pas l'étanchéité : c'est même le contraire, moins de points de serrage rendent le joint moins régulièrement plaqué.",
   "Le nombre de vis se voit à peine, et une façade sans vis apparente serait plus soignée : l'apparence n'a pas dicté ce choix."],
  "Celui qui répare est un utilisateur, lui aussi.")

q("C2.2", "Deux domaines à la fois", "Un même choix peut-il servir deux domaines à la fois ?",
  ["oui : un angle arrondi est plus sûr et souvent plus agréable à regarder",
   "non : chaque choix répond à un seul domaine",
   "oui, mais seulement l'ergonomie et l'esthétique",
   "non, sauf en cas d'erreur de conception"],
  "Les domaines se recoupent souvent. L'exercice consiste alors à dire lequel DOMINE, et pourquoi.",
  "Une poignée large : plus facile à saisir (ergonomie) et moins blessante (sécurité).",
  "Chercher à tout prix une seule étiquette par choix.",
  ["",
   "Rien n'oblige une forme à ne produire qu'un effet : une même courbe peut simultanément protéger la main, faciliter la prise et plaire à l'œil.",
   "Le recoupement peut concerner n'importe quelle paire : sécurité et esthétique se rejoignent aussi, comme le montre justement l'angle arrondi.",
   "Servir deux domaines est un signe de bonne conception, pas d'erreur : c'est un choix qui rend deux services pour le prix d'un."],
  "Quand deux domaines se recoupent, dis lequel domine.")

q("C2.2", "Le coût d'un choix", "Un boîtier soudé plutôt que vissé…",
  ["résiste mieux au vandalisme mais rend la maintenance beaucoup plus lourde",
   "est un meilleur choix dans tous les cas",
   "ne change rien pour ceux qui l'utilisent",
   "coûte forcément plus cher à fabriquer"],
  "Un choix technique n'est jamais gratuit : il déplace le problème ailleurs. Savoir dire OÙ, "
  "c'est lire un objet.",
  "Soudé : impossible d'ouvrir sans découper. Chaque réparation devient un chantier.",
  "Évaluer un choix sur un seul critère.",
  ["",
   "Aucun choix n'est meilleur sur tous les plans : celui-ci gagne en résistance et perd en réparabilité, ce qui peut condamner l'objet entier à la première panne.",
   "L'agent de maintenance, lui, le sent immédiatement — et l'usager aussi, le jour où la borne reste hors service en attendant une intervention lourde.",
   "Une soudure est souvent MOINS chère à produire qu'un assemblage vissé : ce qu'elle coûte, elle le coûte plus tard, à l'entretien."],
  "Un choix technique déplace le problème ailleurs.")

q("C2.2", "Deux réponses au même problème", "Une autre station abrite ses bornes sous un auvent au lieu de les incliner. Cela montre que…",
  ["un même problème admet plusieurs réponses techniques, chacune avec ses conséquences",
   "l'une des deux stations est forcément une erreur",
   "les deux équipes ne se sont pas concertées",
   "le problème de la pluie n'était pas important"],
  "Auvent et inclinaison répondent au même interacteur : la pluie. Ce sont deux solutions "
  "légitimes, qui ne coûtent pas la même chose aux mêmes endroits.",
  "L'auvent protège mieux mais occupe de la place et prend le vent.",
  "Croire qu'un problème technique a une seule bonne réponse.",
  ["",
   "Les deux réponses traitent le même interacteur ; ce qui les sépare, ce sont leurs conséquences — encombrement d'un côté, protection partielle de l'autre.",
   "La concertation n'est pas en cause : deux équipes parfaitement informées peuvent trancher différemment selon la place disponible et le budget d'entretien.",
   "C'est l'inverse : si deux équipes ont dépensé pour s'en protéger, chacune à sa manière, c'est bien que le problème comptait."],
  "Un même problème admet plusieurs réponses techniques.")

q("C2.2", "Un gain payé ailleurs", "Ancrer les vélos au sol plutôt qu'à 90 cm…",
  ["occupe moins de place mais oblige l'usager à se baisser : un gain d'encombrement payé en ergonomie",
   "est meilleur sur tous les points",
   "est simplement moins sûr",
   "ne change rien pour l'usager"],
  "Nommer le gain ET le prix : c'est ce qui distingue une comparaison d'un avis.",
  "Trottoir étroit : on gagne la place, on la paie sur le dos des usagers.",
  "Ne dire que ce que le choix apporte.",
  ["",
   "Aucun choix n'est meilleur partout : celui-ci gagne en encombrement et perd en confort d'usage, ce qui pèse lourd pour les personnes âgées ou chargées.",
   "La sécurité n'est pas ce qui change ici : un ancrage au sol peut être parfaitement sûr, c'est le geste de l'usager qui devient pénible.",
   "Se baisser à chaque prise et à chaque retour est un changement très concret, répété plusieurs fois par jour."],
  "Nomme le gain ET le prix.")

q("C2.2", "Justifier, pas décrire", "Laquelle de ces phrases explique vraiment un choix de conception ?",
  ["« La borne est inclinée pour que l'eau de pluie s'écoule au lieu de stagner sur le lecteur. »",
   "« La borne est inclinée vers le bas. »",
   "« La borne est inclinée, c'est plus moderne. »",
   "« La borne est inclinée d'environ quinze degrés. »"],
  "Expliquer, c'est relier la forme à un interacteur et à un effet recherché. Sans ce lien, on "
  "décrit — même avec précision.",
  "Comparer : « c'est incliné » (constat) et « incliné POUR que l'eau s'écoule » (explication).",
  "Rendre une description en croyant avoir expliqué.",
  ["",
   "C'est un constat exact et complet, mais il s'arrête à la forme : il ne dit ni à qui ni à quoi cette forme répond.",
   "« Moderne » est une impression d'époque, pas une raison technique : elle n'indique aucun interacteur et ne pourrait pas guider une nouvelle conception.",
   "La mesure ajoute de la précision au constat sans ajouter de raison : quinze degrés plutôt que cinq, il faudrait encore dire pourquoi."],
  "Expliquer, c'est relier la forme à un interacteur.")

q("C2.2", "Le piège du « c'est joli »", "Dire d'un garde-corps arrondi « c'est pour faire joli », c'est…",
  ["passer à côté de la raison principale, qui est d'éviter les blessures",
   "une explication correcte, l'esthétique étant un vrai domaine",
   "une erreur, car l'esthétique n'existe pas en technologie",
   "juste, puisqu'un objet doit d'abord plaire"],
  "L'esthétique est un domaine légitime — mais elle ne doit pas servir de fourre-tout quand on "
  "n'a pas cherché la raison technique.",
  "L'arrondi plaît, et il évite surtout une plaie au front.",
  "Ranger dans « esthétique » tout ce qu'on n'a pas su expliquer.",
  ["",
   "L'esthétique est bien un domaine réel, mais elle n'est pas ici la raison dominante : on arrondit d'abord pour ne pas blesser, l'agrément vient en plus.",
   "L'esthétique est au contraire l'un des trois domaines au programme : l'intégration d'un objet dans un lieu est une vraie question de conception.",
   "Un objet technique doit d'abord rendre son service sans danger ; plaire est un objectif réel, mais il ne passe pas avant l'intégrité des usagers."],
  "L'esthétique est un domaine, pas un fourre-tout.")

q("C2.2", "Transposer", "Pour installer cette station à Sainte-Luce, il faudrait d'abord revoir…",
  ["les matériaux et les traitements de surface, à cause de l'air salin",
   "la couleur des bornes, pour l'accorder au paysage",
   "le nombre de vélos, plus faible qu'en Chine",
   "rien : l'objet a fait ses preuves"],
  "On repart des interacteurs qui changent, et on remonte aux choix qu'ils remettent en cause. "
  "L'ordre compte : d'abord ce qui détruit l'objet, ensuite ce qui l'améliore.",
  "Une visserie en acier ordinaire ne passe pas deux saisons près du rivage.",
  "Transposer un objet sans réexaminer ses interacteurs.",
  ["",
   "La couleur est un ajustement d'intégration, réel mais secondaire : une borne bien assortie qui rouille en six mois reste une borne hors service.",
   "Le dimensionnement de l'offre est une question de service, pas de conception de la borne : il ne change ni les matériaux ni les formes.",
   "Avoir fait ses preuves à Shenzhen ne prouve rien pour Sainte-Luce, précisément parce que les interacteurs — sel, pluies intenses, cyclone — n'y sont pas les mêmes."],
  "On transpose en repartant des interacteurs qui changent.")

q("C2.2", "Ce qu'on fera l'an prochain", "Cette année, en 5e, on repère les choix de conception. En 4e, on apprendra en plus à…",
  ["décrire l'expérience vécue par l'utilisateur de l'objet",
   "recenser les interacteurs, qui n'est pas au programme de 5e",
   "mesurer les dimensions de l'objet avec précision",
   "fabriquer l'objet en atelier"],
  "Repérer un choix visible dans la forme et décrire un vécu ne sont pas la même chose. Cette "
  "année, on lit l'objet ; l'an prochain, on écoutera celui qui s'en sert.",
  "« L'angle est arrondi » (5e) et « l'usager hésite devant la borne » (4e).",
  "Croire qu'on doit déjà raconter ce que ressent l'utilisateur.",
  ["",
   "Le recensement des interacteurs est au contraire le cœur du programme de 5e : c'est exactement ce que fait la première séance de cette séquence.",
   "La mesure précise relève d'une autre compétence, travaillée ailleurs dans le cycle, et non de la description des interactions.",
   "La fabrication concerne la réalisation d'un prototype, qui est un autre moment du programme et ne remplace pas la description de l'expérience utilisateur."],
  "En 5e on lit l'objet ; en 4e on décrira le vécu de l'utilisateur.")

assert len(Q) == 30, len(Q)
assert sum(1 for x in Q if x["c"] == "C2.1") == 15
assert sum(1 for x in Q if "img" in x) == 4
