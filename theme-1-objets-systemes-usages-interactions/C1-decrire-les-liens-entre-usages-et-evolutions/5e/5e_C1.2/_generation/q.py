# -*- coding: utf-8 -*-
"""Les 30 questions du QCM 5e_C1.2 — Sainte-Luce, quel frein pour les vélos du collège.

Écrites à la main. Toutes les bonnes réponses sont en position 0 ici : la
répartition sur A/B/C/D est faite ensuite par `_outils/fix_r.js`, de façon
déterministe, à partir d'une graine.

La séquence ne porte qu'UN code : les 30 questions sont donc réparties par
THÈME plutôt que par compétence — fonction, principe, solution (8) · ce que
montre la manipulation (7) · lire et comparer des données (8) · choisir selon
un contexte (7).

Règle tenue pour chaque distracteur : la réfutation EXPLIQUE pourquoi la
réponse est fausse — elle ne se contente pas de dire qu'elle l'est.
"""

IMG_PRINCIPES = {
    "src": "Images/corrige_trois_principes_de_freinage.svg",
    "alt": "Les trois principes de freinage — patins serrant la jante, plaquettes serrant un "
           "disque près du moyeu, mâchoires poussant contre un tambour fermé — avec la "
           "distinction entre fonction, principe et solution.",
}
IMG_TABLEAU = {
    "src": "Images/corrige_le_critere_qui_tranche.svg",
    "alt": "Le tableau comparatif des trois solutions sur six critères, avec le meilleur et le "
           "moins bon de chaque colonne, et l'explication du critère qui tranche à Sainte-Luce.",
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


C = "C1.2"

# ═══════════ Fonction, principe, solution (8) ═══════════

q(C, "La fonction technique", "« Arrêter un vélo en mouvement » est…",
  ["une fonction technique : elle dit ce qu'il faut obtenir, sans dire par quel moyen",
   "un principe technique : elle nomme un phénomène physique",
   "une solution technique : elle désigne un frein précis",
   "une contrainte imposée par la mairie"],
  "Une fonction technique s'énonce par un verbe à l'infinitif et un complément. Elle décrit ce "
  "que l'objet doit FAIRE — et elle laisse entièrement ouvert le moyen. C'est ce qui permet à "
  "trois freins différents de la remplir tous les trois.",
  "« Éclairer une salle » est une fonction : la lampe à filament, le tube fluorescent et la diode "
  "la remplissent tous les trois.",
  "Écrire une fonction qui contient déjà sa solution — « freiner avec des patins » — et croire "
  "qu'on a énoncé une fonction alors qu'on a déjà choisi.",
  ["",
   "Aucun phénomène physique n'est nommé : ni frottement, ni magnétisme, ni résistance de l'air. C'est précisément ce qui la distingue d'un principe.",
   "Aucun frein n'est désigné : ni type, ni marque, ni référence. L'énoncé resterait vrai avec n'importe lequel des trois.",
   "Une contrainte impose une condition à respecter ; ici on énonce ce qu'il faut obtenir, ce qui est tout autre chose."],
  "Fonction = ce que l'objet doit FAIRE. Le moyen reste ouvert."),

q(C, "Le piège de « à quoi ça sert »", "« À quoi sert un vélo ? — À se déplacer. » Cette phrase énonce…",
  ["le service rendu à l'usager, ce qu'on appelle la fonction d'usage — pas une fonction technique",
   "une fonction technique du vélo",
   "un principe technique",
   "une solution technique"],
  "C'est la confusion la plus fréquente, et elle a la vie dure. « À quoi ça sert » regarde l'objet "
  "du point de vue de celui qui s'en sert. Une fonction technique regarde ce que l'objet, ou l'une "
  "de ses parties, doit FAIRE pour rendre ce service.",
  "Le vélo SERT à se déplacer. L'une de ses fonctions techniques est d'arrêter le mouvement ; une "
  "autre est de transmettre l'effort des jambes à la roue.",
  "Répondre « à quoi ça sert » quand on demande une fonction technique. Les deux réponses "
  "commencent souvent par un verbe à l'infinitif, ce qui rend le piège difficile à voir.",
  ["",
   "Une fonction technique porte sur ce que fait l'objet ou l'une de ses parties, pas sur le bénéfice qu'en tire l'usager : « arrêter le mouvement » en est une, « se déplacer » n'en est pas une.",
   "Aucun phénomène physique n'est nommé : se déplacer n'est pas un mécanisme, c'est un résultat pour la personne.",
   "Aucun objet concret n'est désigné : ni frein, ni pédalier, ni marque."],
  "« À quoi ça sert » = le service rendu. « Ce que ça doit faire » = la fonction technique."),

q(C, "Le principe", "« Serrer la jante entre deux patins par frottement » est…",
  ["un principe : c'est le phénomène physique employé pour remplir la fonction",
   "une fonction technique",
   "une solution technique",
   "un critère de comparaison"],
  "Le principe répond à la question « par quel phénomène ? ». Ici le phénomène est le frottement, "
  "et l'endroit où on l'applique est la jante. Changer de principe, c'est changer de phénomène ou "
  "d'endroit — pas changer de marque.",
  "Trois principes pour arrêter un vélo : frotter la jante, frotter un disque au moyeu, frotter "
  "l'intérieur d'un tambour.",
  "Confondre le principe avec le matériau : « en caoutchouc » n'est pas un principe.",
  ["",
   "Une fonction ne nomme aucun moyen ; ici le moyen est nommé deux fois, par le phénomène et par l'endroit.",
   "Une solution désigne un objet précis qu'on peut commander sur catalogue ; cet énoncé décrit un mécanisme, pas un article.",
   "Un critère sert à départager (le prix, la masse) ; ici rien n'est comparé, on décrit un fonctionnement."],
  "Principe = par quel phénomène, et à quel endroit.",
  img=IMG_PRINCIPES),

q(C, "La solution", "« Le frein à patins du fournisseur B, référence 2140 » est…",
  ["une solution technique : c'est l'objet concret qu'on achète et qu'on monte",
   "un principe technique",
   "une fonction technique",
   "une exigence du cahier des charges"],
  "La solution est le bout de la chaîne : l'article réel, avec sa référence, son prix et son "
  "fournisseur. Deux solutions différentes peuvent employer exactement le même principe.",
  "Deux marques de freins à patins sont deux solutions distinctes pour un seul et même principe.",
  "Croire qu'on a répondu à la question du principe en donnant une référence de catalogue.",
  ["",
   "Le principe serait « serrer la jante par frottement » ; la référence 2140 n'est qu'une façon particulière de le mettre en œuvre.",
   "Une fonction ne nomme jamais de fournisseur : elle vaut avant même qu'on ait choisi quoi que ce soit.",
   "Une exigence dit ce qu'il faut respecter, pas ce qu'on achète."],
  "Solution = l'objet concret. Plusieurs solutions pour un même principe."),

q(C, "L'ordre des trois", "Dans quel ordre ces trois notions viennent-elles quand on conçoit ?",
  ["fonction, puis principe, puis solution",
   "solution, puis principe, puis fonction",
   "principe, puis fonction, puis solution",
   "l'ordre n'a aucune importance"],
  "On part de ce qu'il faut obtenir, on explore les phénomènes qui pourraient y parvenir, et l'on "
  "choisit enfin un objet. Prendre l'ordre à l'envers — partir de la solution qu'on connaît — "
  "revient à avoir choisi avant d'avoir cherché.",
  "« Arrêter le vélo » → « par frottement sur un disque » → « ce frein-là, référence 2140 ».",
  "Commencer par la solution qu'on a déjà vue quelque part, puis inventer après coup la fonction "
  "qu'elle remplit.",
  ["",
   "Partir de la solution, c'est décider avant de chercher : on ne découvrira jamais les principes qu'on n'avait pas envisagés.",
   "Un principe ne se choisit que si l'on sait déjà ce qu'il doit accomplir : sans fonction, on ne sait pas ce qu'on cherche.",
   "L'ordre est décisif : c'est lui qui laisse ouverte la comparaison entre plusieurs principes, au lieu de la fermer d'avance."],
  "Fonction → principe → solution. Prendre l'ordre à l'envers, c'est avoir déjà choisi."),

q(C, "Pourquoi ne pas nommer le moyen", "Pourquoi une fonction bien écrite ne nomme-t-elle aucun moyen ?",
  ["pour laisser ouverts tous les principes qui pourraient la remplir",
   "pour rester plus courte à écrire",
   "parce que le moyen n'a aucune importance",
   "parce qu'on ne le connaît jamais au départ"],
  "Une fonction est une question posée, pas une réponse. Si elle contient déjà son moyen, il n'y a "
  "plus rien à comparer — et l'on se prive des solutions auxquelles on n'avait pas pensé.",
  "« Arrêter le vélo » laisse place aux trois freins. « Freiner avec des patins » n'en laisse "
  "qu'un, et la comparaison n'a plus lieu d'être.",
  "Écrire une fonction qui contient sa solution, puis s'étonner qu'il n'y ait rien à choisir.",
  ["",
   "La longueur n'entre pas en jeu : une fonction peut être longue et bien écrite, ou courte et déjà refermée sur une solution.",
   "Le moyen a au contraire une importance décisive — c'est lui qui déterminera le prix, la durée de vie et le comportement sous la pluie.",
   "On le connaît souvent très bien : le danger est justement de le faire entrer trop tôt dans l'énoncé."],
  "Une fonction est une question. Si elle contient sa réponse, il n'y a plus rien à comparer."),

q(C, "Le même phénomène, trois fois", "Les trois freins de la séquence emploient…",
  ["le même phénomène — le frottement — mais à des endroits différents",
   "trois phénomènes physiques totalement différents",
   "de l'électronique pour deux d'entre eux",
   "le même principe et la même solution"],
  "C'est ce que la manipulation rend visible : dans les trois cas, deux surfaces glissent l'une "
  "contre l'autre, ralentissent le mouvement et chauffent. Ce qui change est l'ENDROIT — la jante, "
  "un disque au moyeu, l'intérieur d'un tambour — et donc ce qui s'y trouve exposé.",
  "Le patin frotte la jante, exposée à la pluie ; la mâchoire frotte l'intérieur d'un tambour "
  "fermé, où l'eau n'entre pas.",
  "Croire que des objets d'aspect différent reposent forcément sur des phénomènes différents.",
  ["",
   "Le phénomène est identique dans les trois cas : c'est le frottement. Ce sont les surfaces et leur emplacement qui diffèrent.",
   "Aucun des trois freins de la séquence ne comporte d'électronique : ils sont entièrement mécaniques, commandés par un câble.",
   "Le principe diffère bien d'un frein à l'autre par l'endroit du frottement, et la solution diffère aussi."],
  "Même phénomène, trois endroits — et l'endroit décide de tout le reste.",
  img=IMG_PRINCIPES),

q(C, "Ni matériau ni marque", "« En aluminium » proposé comme principe technique est…",
  ["faux : un matériau n'est pas un phénomène, il ne dit pas comment la fonction est remplie",
   "juste, car le matériau détermine le fonctionnement",
   "juste, mais incomplet",
   "un principe seulement si la pièce est métallique"],
  "Un principe décrit une action physique : frotter, aimanter, comprimer, dévier. Un matériau "
  "décrit ce dont la pièce est faite. Les deux sont utiles, ils ne répondent pas à la même "
  "question.",
  "« Serrer un disque par frottement » est un principe. « Disque en acier inoxydable » est un "
  "choix de matériau à l'intérieur de ce principe.",
  "Répondre par ce qu'on voit — la matière, la couleur, la forme — quand on demande comment ça "
  "marche.",
  ["",
   "Le matériau influence les performances, mais il ne dit pas par quel phénomène le vélo s'arrête : un frein en aluminium peut être à patins ou à disque.",
   "Ce n'est pas une réponse incomplète mais une réponse à une autre question : celle de la matière, pas celle du mécanisme.",
   "La nature du matériau n'y change rien : métallique ou non, il ne décrit toujours pas une action physique."],
  "Un principe est une action physique, jamais une matière."),

# ═══════════ Ce que montre la manipulation (7) ═══════════

q(C, "Ce qui se touche", "Sur un frein à patins, les deux pièces qui frottent l'une contre l'autre sont…",
  ["le patin de caoutchouc et la jante, c'est-à-dire le bord métallique de la roue",
   "le patin et le pneu",
   "le câble et le levier",
   "le patin et le moyeu"],
  "Un frottement se fait toujours à DEUX. Le patin est la pièce qui serre ; la jante est la pièce "
  "qui est serrée. Nommer l'une sans l'autre revient à décrire une main qui applaudit toute seule.",
  "Après quelques freinages, c'est la JANTE qui est tiède : c'est bien là que l'énergie s'est "
  "transformée en chaleur.",
  "Ne nommer que la pièce mobile — le patin — et croire qu'on a décrit le frottement.",
  ["",
   "Le pneu n'est pas touché par le patin : s'il l'était, il s'userait en quelques freinages et le freinage serait très mauvais.",
   "Le câble et le levier transmettent l'effort de la main, mais ils ne frottent pas l'un contre l'autre : ils tirent.",
   "Le moyeu est au centre de la roue ; c'est là que frotte un frein à disque ou à tambour, pas un frein à patins."],
  "Un frottement se fait à deux : la pièce qui serre, et celle qui est serrée.",
  img=IMG_PRINCIPES),

q(C, "Où part l'énergie", "Après plusieurs freinages, la jante est tiède. Cela montre que…",
  ["l'énergie du vélo en mouvement s'est transformée en chaleur par frottement",
   "le frein est mal réglé",
   "la jante est de mauvaise qualité",
   "il faisait chaud ce jour-là"],
  "Freiner ne fait pas disparaître l'énergie : cela la transforme. L'énergie du vélo lancé devient "
  "de la chaleur là où les surfaces frottent. C'est vrai des trois principes — et c'est pour cela "
  "que la chaleur devient un problème dans les longues descentes.",
  "Un tambour, parce qu'il est fermé, évacue mal cette chaleur : en fin de longue descente, il "
  "chauffe et freine moins bien.",
  "Chercher une panne là où il y a un phénomène normal et attendu.",
  ["",
   "Un frein bien réglé chauffe exactement de la même façon : la chaleur vient du principe lui-même, pas d'un défaut de réglage.",
   "Une jante de très bonne qualité chauffe tout autant : elle résistera mieux à l'usure, mais l'énergie devra toujours se transformer quelque part.",
   "La température de l'air ne change rien à ce constat : c'est la zone de frottement qui chauffe, et elle seule."],
  "L'énergie ne disparaît pas quand on freine : elle devient de la chaleur."),

q(C, "L'écart au repos", "Levier relâché, il reste environ 2 mm entre le patin et la jante. Cet écart…",
  ["est nécessaire : sans lui, le patin frotterait en permanence et userait la jante",
   "est un défaut de fabrication",
   "sert à laisser passer l'eau de pluie",
   "n'a aucune importance"],
  "Un frein doit pouvoir être RELÂCHÉ. L'écart au repos garantit que rien ne frotte quand on ne "
  "freine pas. Trop grand, le levier arrive en butée avant de serrer ; trop petit, ça frotte en "
  "roulant.",
  "Un frein mal réglé qui frotte en permanence fatigue le cycliste, use les patins et chauffe la "
  "jante sans que personne ne l'ait demandé.",
  "Croire qu'un bon réglage est celui où le patin touche presque toujours la jante.",
  ["",
   "C'est au contraire le résultat d'un réglage volontaire, qu'on refait quand les patins s'usent et que l'écart grandit.",
   "L'eau passe de toute façon : elle est projetée par la roue en marche, et 2 mm ne changent rien à cela.",
   "Son importance est décisive dans les deux sens : trop grand, le frein ne serre plus assez ; trop petit, il freine tout le temps."],
  "Un frein doit aussi savoir ne pas freiner."),

q(C, "Le disque au moyeu", "Sur un frein à disque, la surface qui frotte est placée près du moyeu. La conséquence est que…",
  ["elle est plus haute et plus protégée : elle reçoit moins d'eau et de projections que la jante",
   "elle freine plus doucement",
   "elle ne chauffe pas",
   "elle rend le vélo plus léger"],
  "L'endroit décide de l'exposition. La jante est à la périphérie de la roue, au plus près de la "
  "chaussée et des flaques. Un disque au moyeu se trouve plus haut et plus au centre : l'eau et la "
  "boue l'atteignent beaucoup moins.",
  "C'est ce que confirment les chiffres : sous la pluie, le disque perd 1,0 m par rapport au sol "
  "sec, contre 3,1 m pour les patins.",
  "Croire que la différence de comportement sous la pluie vient de la qualité des pièces, alors "
  "qu'elle vient d'abord de leur emplacement.",
  ["",
   "Un frein à disque freine au contraire plus fort à effort égal, parce que la force s'applique sur un plus petit rayon.",
   "Il chauffe beaucoup, et parfois davantage : la surface est plus petite, donc l'énergie se concentre.",
   "Il alourdit le vélo : 510 g contre 320 g pour les patins, à cause du disque et de son support."],
  "L'endroit du frottement décide de son exposition — et donc de sa tenue sous la pluie.",
  img=IMG_PRINCIPES),

q(C, "Le tambour fermé", "Le frein à tambour résiste le mieux à la corrosion parce que…",
  ["sa surface de frottement est enfermée : le sel et l'eau ne l'atteignent presque pas",
   "il est fabriqué dans un métal plus résistant",
   "il est plus lourd",
   "il est peint"],
  "Encore l'endroit. Les mâchoires poussent contre la paroi INTÉRIEURE d'un tambour clos. Ce qui "
  "est enfermé est protégé — de l'eau, du sel, du sable. C'est un avantage décisif en bord de mer, "
  "et il ne coûte rien de plus.",
  "À Sainte-Luce, à quelques centaines de mètres de la mer, cela vaut 5/5 en corrosion contre 2/5 "
  "pour les patins.",
  "Chercher l'explication dans le matériau alors qu'elle est dans la géométrie.",
  ["",
   "Les trois freins emploient des métaux comparables ; c'est l'exposition qui diffère, pas la nuance d'acier.",
   "La masse ne protège de rien : elle vient de la matière du tambour, elle n'est pas la cause de sa résistance au sel.",
   "La peinture protège les parties visibles, pas la surface de frottement — qui ne peut évidemment pas être peinte, sinon elle ne frotterait plus."],
  "Ce qui est enfermé est protégé. C'est de la géométrie, pas de la chimie."),

q(C, "Le revers du tambour", "L'inconvénient de cette surface enfermée est que…",
  ["la chaleur s'en évacue mal : dans une longue descente, le frein chauffe et perd de son efficacité",
   "elle s'use plus vite",
   "elle est plus chère à fabriquer",
   "elle ne fonctionne pas par temps froid"],
  "Un même choix de conception apporte presque toujours un avantage ET un inconvénient, et ce sont "
  "souvent les deux faces de la même caractéristique. Ici, ce qui protège de l'eau empêche aussi "
  "la chaleur de sortir.",
  "Le relevé d'essai le note : « chauffe en fin de descente » pour le tambour, dans la descente "
  "à 8 %.",
  "Chercher l'inconvénient ailleurs que dans l'avantage. Il est très souvent au même endroit.",
  ["",
   "L'usure est plutôt plus lente, justement parce que la surface est protégée du sable et des projections abrasives.",
   "Le coût d'entretien annoncé, 27 €/an, se situe entre celui des patins et celui du disque : ce n'est pas là que le bât blesse.",
   "Le froid n'a pas d'effet notable sur un frein mécanique de ce type ; c'est la chaleur qui pose problème, pas l'inverse."],
  "Ce qui protège de l'eau retient aussi la chaleur. Le même choix, ses deux faces."),

q(C, "Ce que le schéma ne montrait pas", "Qu'apprend la manipulation sur un vrai vélo, qu'un tableau de chiffres ne dit pas ?",
  ["que la surface qui frotte, sur un frein à patins, est la roue elle-même — celle qui roule dans les flaques",
   "le prix de chaque frein",
   "la distance d'arrêt exacte",
   "la durée de vie des patins"],
  "Les chiffres disent CE QUI se passe ; l'objet dit POURQUOI. Voir de ses yeux que le patin serre "
  "le bord de la roue permet de prévoir sa faiblesse sous la pluie avant d'ouvrir le moindre "
  "tableau — et de comprendre le chiffre au lieu de l'apprendre.",
  "Un élève qui a vu où frotte le patin devine l'écart de 3,1 m sous la pluie ; celui qui n'a vu "
  "que le tableau le retient sans le comprendre.",
  "Croire qu'un tableau bien fait rend l'objet inutile.",
  ["",
   "Le prix figure au contraire dans le tableau, et l'objet ne le donne pas.",
   "La distance d'arrêt est une mesure : elle vient des essais, pas de l'observation à l'arrêt.",
   "La durée de vie ne s'observe pas en une séance : elle demanderait un suivi sur plusieurs mois."],
  "Les chiffres disent ce qui se passe. L'objet dit pourquoi."),

# ═══════════ Lire et comparer des données (8) ═══════════

q(C, "D'où viennent les chiffres", "Sur le parking, les patins ont donné 5,7 puis 5,9 m sur sol sec. La fiche annonce 5,8 m. C'est…",
  ["la moyenne des essais : une fiche technique est un résumé de mesures",
   "une erreur du fournisseur",
   "une valeur inventée pour arrondir",
   "la plus petite des deux mesures"],
  "Une fiche technique n'est pas une parole d'autorité : c'est le résumé de mesures que quelqu'un "
  "a faites. Savoir cela change tout — on peut la vérifier, et on doit demander dans quelles "
  "conditions elle a été établie.",
  "(5,7 + 5,9) ÷ 2 = 5,8. Les quinze essais du parking retombent exactement sur les valeurs de la "
  "fiche.",
  "Prendre une fiche technique pour une vérité qui n'a pas de source.",
  ["",
   "Il n'y a pas d'erreur : la valeur annoncée correspond exactement à la moyenne des mesures.",
   "Elle n'est pas inventée mais calculée, et le calcul est refaisable à partir du fichier des essais.",
   "La plus petite des deux serait 5,7 : ce n'est pas ce qu'annonce la fiche."],
  "Une fiche technique est un résumé de mesures. On peut donc la vérifier."),

q(C, "L'écart, pas la valeur", "Sous la pluie, l'écart avec le sol sec vaut +3,1 m pour les patins et +1,0 m pour le disque. Cet écart dit…",
  ["combien chaque principe perd quand la surface qui frotte est mouillée",
   "que le disque est plus lourd que les patins",
   "que les essais sous la pluie ont été mal faits",
   "que la pluie n'a aucun effet sur le tambour"],
  "Comparer les valeurs absolues ne suffit pas : c'est l'ÉCART entre deux conditions qui révèle la "
  "sensibilité d'un principe. Un frein qui perd peu quand tout se dégrade est un frein sur lequel "
  "on peut compter.",
  "Les patins passent de 5,8 à 8,9 m, le disque de 5,4 à 6,4 m. Le second reste prévisible ; le "
  "premier change de comportement.",
  "Ne regarder que la meilleure valeur, et manquer le fait qu'elle s'effondre dès qu'il pleut.",
  ["",
   "La masse figure dans une autre colonne et n'a aucun rapport avec l'écart entre sec et mouillé.",
   "Les essais ont été faits dans les mêmes conditions pour les trois freins : c'est précisément ce qui rend la comparaison possible.",
   "Le tambour perd lui aussi, mais très peu : +0,8 m. Peu n'est pas rien."],
  "L'écart entre deux conditions en dit plus que la meilleure valeur."),

q(C, "Le plus petit gagne", "Pour la colonne « distance d'arrêt », la meilleure valeur est…",
  ["la plus petite : s'arrêter en 5,4 m vaut mieux qu'en 6,1 m",
   "la plus grande : plus la distance est longue, plus le freinage est progressif",
   "celle du milieu",
   "la même pour les trois, puisqu'ils arrêtent tous le vélo"],
  "Lire un tableau demande de savoir, pour chaque colonne, dans quel sens elle se lit. Pour une "
  "distance d'arrêt, une masse ou un prix, le plus petit est le meilleur. Pour une note de "
  "réparabilité ou de résistance, c'est l'inverse.",
  "Dans la même ligne, 320 g est un bon chiffre et 5/5 aussi — pourtant l'un est le plus petit de "
  "sa colonne et l'autre le plus grand.",
  "Entourer mécaniquement les plus grands nombres de chaque colonne.",
  ["",
   "Une distance d'arrêt plus longue signifie qu'on percute ce qu'on voulait éviter ; la progressivité du freinage est une autre qualité, qui ne se lit pas dans cette colonne.",
   "Rien ne justifie de choisir la valeur médiane : ce n'est ni la meilleure ni la moins bonne, c'est simplement la deuxième.",
   "Ils arrêtent tous le vélo — c'est la fonction, et elle est commune. Les distances, elles, diffèrent nettement."],
  "Dans chaque colonne, il faut savoir dans quel sens on lit."),

q(C, "Une note n'est pas une mesure", "Le critère « réparabilité 5/5 » est…",
  ["une appréciation chiffrée : utile pour comparer, mais elle résume un jugement, pas une mesure",
   "une mesure physique, aussi sûre qu'une distance en mètres",
   "sans valeur, puisque ce n'est pas une mesure",
   "le nombre de pièces détachées disponibles"],
  "Toutes les colonnes d'un tableau n'ont pas la même solidité. 6,4 m se mesure avec un décamètre "
  "et se refait ; 4/5 résulte de l'avis de quelqu'un. On garde ces notes — elles sont utiles — "
  "mais on sait qu'elles se discutent, et on demande qui les a attribuées.",
  "Deux techniciens peuvent noter la même réparabilité 3/5 et 4/5 ; aucun des deux ne mesurera "
  "6,4 m au lieu de 8,9.",
  "Traiter toutes les colonnes comme également sûres parce qu'elles contiennent toutes des "
  "chiffres.",
  ["",
   "Une note résume un jugement : deux personnes peuvent l'attribuer différemment, ce qui n'arrive pas avec une distance mesurée.",
   "Elle a beaucoup de valeur, à condition de savoir ce qu'elle est : la réparabilité compte énormément dans un collège.",
   "Ce serait une donnée intéressante, mais différente : on peut avoir beaucoup de pièces disponibles pour un objet difficile à démonter."],
  "Un chiffre n'est pas forcément une mesure. Certains résument un avis.",
  img=IMG_TABLEAU),

q(C, "Aucune ne gagne partout", "En lisant les six colonnes, on constate que…",
  ["chaque solution est première sur au moins un critère et dernière sur au moins un autre",
   "une solution gagne sur cinq critères sur six",
   "les trois solutions sont équivalentes",
   "le tableau est incomplet, puisqu'il ne désigne pas de vainqueur"],
  "C'est la situation normale, pas l'exception. Si une solution gagnait partout, il n'y aurait "
  "rien à décider et le tableau serait inutile. Un comparatif sert précisément quand les avantages "
  "sont répartis.",
  "Patins : premiers en masse, entretien et réparabilité, derniers sous la pluie et en corrosion. "
  "Disque : premier sur les deux distances, dernier en entretien. Tambour : premier en corrosion, "
  "dernier sur le sec, la masse et la réparabilité.",
  "Chercher la solution qui gagne partout, et conclure que le tableau est mal fait quand on ne la "
  "trouve pas.",
  ["",
   "Aucune n'approche ce score : le maximum est de trois colonnes gagnées, pour les patins.",
   "Elles sont loin d'être équivalentes : 8,9 m contre 6,4 m sous la pluie, c'est deux mètres et demi d'écart.",
   "Un tableau comparatif n'a jamais pour rôle de désigner un vainqueur : il rassemble les faits, la décision vient après."],
  "Un tableau où quelqu'un gagne partout n'apprend rien. C'est la répartition qui rend le choix nécessaire.",
  img=IMG_TABLEAU),

q(C, "Ce que le tableau ne dit pas", "Ce qu'un tableau comparatif ne peut pas donner, c'est…",
  ["l'importance de chaque critère : il donne les faits, pas leur poids",
   "les valeurs de chaque solution",
   "les unités de mesure",
   "le nombre de critères retenus"],
  "Le tableau est un état des lieux. Décider que la corrosion pèse plus que la masse est un choix "
  "humain, qui dépend du lieu, de l'usage et des moyens. Aucune colonne ne contient cette "
  "information — et c'est pour cela qu'un tableau ne décide jamais seul.",
  "Le même tableau, à Sainte-Luce et à Fort-de-France, ne désigne pas la même solution. Pourtant "
  "aucun chiffre n'a changé.",
  "Attendre du tableau qu'il tranche, puis choisir au hasard quand il ne tranche pas.",
  ["",
   "Les valeurs sont exactement ce que le tableau contient : c'est même sa seule fonction.",
   "Les unités figurent en tête de colonne — mètres, grammes, euros par an, notes sur 5.",
   "Le nombre de critères se compte à vue : il y en a six."],
  "Un tableau donne les faits. Il ne donne pas leur importance — cela, c'est nous."),

q(C, "La pente change tout", "Les essais faits dans la descente à 8 % donnent des distances plus longues pour les trois freins. Cela montre que…",
  ["le contexte de la mesure fait partie du résultat : une distance d'arrêt n'a de sens qu'avec ses conditions",
   "les freins étaient usés en fin de série",
   "l'élève a mal chronométré ces trois essais",
   "il ne faut pas tenir compte de ces trois essais"],
  "Une mesure sans ses conditions ne veut rien dire. « 6,4 m » ne signifie quelque chose que si "
  "l'on précise : à quelle vitesse, sur quelle pente, sur quelle chaussée. C'est pourquoi le "
  "fichier d'essai comporte ces colonnes.",
  "En descente, la pesanteur ajoute de l'énergie qu'il faut aussi dissiper : le frein a plus de "
  "travail à fournir pour le même arrêt.",
  "Comparer deux distances d'arrêt mesurées dans des conditions différentes, et croire qu'on "
  "compare les freins.",
  ["",
   "Les trois freins sont affectés de la même façon, y compris ceux testés en premier : ce n'est donc pas une question d'usure.",
   "Le phénomène est cohérent sur les trois solutions, ce qui exclut une erreur de mesure isolée.",
   "Ces trois essais sont au contraire les plus proches de l'usage réel au collège, où il y a justement une descente."],
  "Une mesure ne vaut qu'avec ses conditions. Sinon on ne compare rien."),

q(C, "Comparer, c'est mesurer pareil", "Pour que la comparaison soit valable, il faut que les essais aient été faits…",
  ["dans les mêmes conditions pour les trois freins : même vitesse, même chaussée, même pente",
   "par trois personnes différentes, pour éviter les erreurs",
   "à des dates différentes, pour varier la météo",
   "avec le plus grand nombre d'essais possible, quelles que soient les conditions"],
  "Comparer, c'est faire varier UNE seule chose à la fois. Ici, ce qui varie est le frein ; tout le "
  "reste doit rester identique, sinon on ne sait plus à quoi attribuer la différence observée.",
  "Les quinze essais partent tous de 18 km/h. Si l'un était parti de 25 km/h, sa distance plus "
  "longue n'aurait rien prouvé sur le frein.",
  "Multiplier les essais sans contrôler les conditions, et croire que le nombre compense le "
  "désordre.",
  ["",
   "Changer d'opérateur ajouterait une différence de plus : c'est exactement ce qu'on cherche à éviter pendant la comparaison.",
   "Varier la météo entre les freins rendrait la comparaison impossible : on ne saurait plus si l'écart vient du frein ou du temps qu'il faisait.",
   "Un grand nombre d'essais mal contrôlés donne un résultat précis et faux : on mesure très bien quelque chose dont on ignore ce que c'est."],
  "Comparer, c'est ne faire varier qu'une chose à la fois."),

# ═══════════ Choisir selon un contexte (7) ═══════════

q(C, "Le sel de l'air", "Le collège est à quelques centaines de mètres de la mer. Cela rend décisif le critère…",
  ["de résistance à la corrosion : le sel de l'air attaque les métaux toute l'année",
   "de masse",
   "de coût d'entretien",
   "de réparabilité"],
  "Un critère devient décisif quand le contexte le met en jeu en permanence. En bord de mer, le "
  "sel agit tous les jours, sur tous les vélos, qu'on s'en serve ou non. C'est ce caractère "
  "continu qui lui donne son poids.",
  "Le sel voyage dans l'air sur plusieurs centaines de mètres à l'intérieur des terres : tout "
  "mobilier littoral est concerné.",
  "Traiter tous les critères comme également importants, quel que soit le lieu.",
  ["",
   "La masse compte quand on porte le vélo dans des escaliers ; ici le trajet est extérieur et la question ne se pose pas de la même façon.",
   "Le coût d'entretien importe, mais il ne dépend pas de la proximité de la mer : il est le même partout.",
   "La réparabilité est précieuse, et elle ne change pas non plus selon qu'on est ou non au bord de l'eau."],
  "Un critère devient décisif quand le lieu le met en jeu tous les jours."),

q(C, "La descente et la pluie", "Le trajet comporte une descente et il pleut souvent. Cela rend décisive…",
  ["la distance d'arrêt sous la pluie, et l'écart entre sec et mouillé",
   "la distance d'arrêt sur sol sec uniquement",
   "la masse du frein",
   "la couleur des poignées"],
  "Deux conditions se cumulent ici : la pente ajoute de l'énergie à dissiper, l'eau réduit "
  "l'efficacité du frottement. C'est exactement la situation où un frein sensible à l'humidité "
  "devient dangereux — et elle se produit plusieurs fois par semaine.",
  "Dans la descente à 8 % sous la pluie, les patins demandent 11,4 m, le disque 7,9 m. Trois "
  "mètres et demi d'écart, à l'endroit précis où l'on freine le plus.",
  "Choisir d'après la performance sur sol sec, qui est la condition la plus facile et la moins "
  "représentative.",
  ["",
   "Le sol sec n'est pas la situation critique : c'est celle où tous les freins se valent presque, avec 0,7 m d'écart entre le meilleur et le moins bon.",
   "La masse ne joue aucun rôle dans le comportement sous la pluie ; elle compte pour le transport et la maniabilité.",
   "L'apparence n'est pas un critère technique et ne figure dans aucune colonne du tableau."],
  "On choisit d'après la situation la plus exigeante, pas la plus facile."),

q(C, "Compter n'est pas comparer", "Le frein à patins gagne sur trois critères. Le choisir pour cette raison serait…",
  ["une erreur : compter les colonnes gagnées revient à donner à tous les critères la même importance",
   "juste : trois sur six, c'est la majorité",
   "impossible à trancher sans essai supplémentaire",
   "correct, car ce sont les critères les moins coûteux"],
  "C'est le piège central de tout comparatif. Compter les victoires, c'est décider en silence que "
  "la masse pèse autant que la distance d'arrêt sous la pluie — dans une descente, au bord de la "
  "mer. Ce n'est pas un raisonnement, c'est une abstention déguisée en calcul.",
  "Trois victoires en masse, prix et réparabilité contre deux défaites en pluie et corrosion : le "
  "compte est favorable, le choix serait mauvais.",
  "Transformer une décision en addition, parce que l'addition est plus facile à défendre.",
  ["",
   "La majorité des colonnes n'est pas la majorité de l'importance : une seule colonne peut peser plus que trois autres réunies.",
   "Les essais nécessaires ont déjà été faits ; ce qui manque n'est pas une mesure, c'est une hiérarchie des critères.",
   "Le coût est un critère parmi d'autres, et rien ne justifie de lui donner par avance la première place."],
  "Comparer n'est pas compter. Il faut hiérarchiser, et le dire.",
  img=IMG_TABLEAU),

q(C, "Le même tableau, ailleurs", "Dans un collège de montagne sèche, où l'on répare soi-même…",
  ["le frein à patins deviendrait le meilleur choix : le même tableau, un autre contexte",
   "le classement resterait identique",
   "il faudrait refaire tous les essais",
   "aucun des trois freins ne conviendrait"],
  "C'est la leçon de toute la séquence. Sans embruns et sans pluie fréquente, la corrosion et "
  "l'écart sous la pluie cessent d'être décisifs ; la masse, le prix et la réparabilité passent "
  "devant. Les chiffres n'ont pas bougé d'un millimètre.",
  "À Fort-de-France, en ville et à plat, le raisonnement donne également les patins — pour des "
  "raisons différentes.",
  "Croire qu'une bonne réponse en technologie est vraie partout et pour toujours.",
  ["",
   "Le classement change parce que la hiérarchie des critères change : c'est précisément ce que la séquence cherche à faire comprendre.",
   "Les essais restent valables : ils décrivent le comportement des freins, pas le lieu où on les installe.",
   "Les trois conviendraient techniquement ; la question n'est pas de savoir s'ils fonctionnent, mais lequel convient le mieux à un contexte."],
  "Le même tableau, un autre lieu, un autre gagnant. Et personne ne s'était trompé."),

q(C, "Défendre un choix", "Une défense de choix complète comporte…",
  ["le principe retenu, deux raisons chiffrées, et ce qu'on accepte de perdre",
   "le principe retenu et ses trois avantages",
   "le nom du fournisseur et son prix",
   "l'avis de la majorité de la classe"],
  "Un choix qui ne coûte rien n'est pas un choix : c'est une préférence. Nommer ce qu'on perd "
  "prouve qu'on a comparé, et permet à celui qui lit de vérifier qu'on n'a rien caché.",
  "« Je retiens le disque : 6,4 m sous la pluie contre 8,9, et 4/5 en corrosion. J'accepte 190 g "
  "de plus et 16 € d'entretien annuel supplémentaires. »",
  "N'énumérer que les avantages, ce qui donne un plaidoyer et non une comparaison.",
  ["",
   "Une liste d'avantages ne prouve pas qu'on a comparé : on peut la produire pour n'importe laquelle des trois solutions.",
   "Le fournisseur et le prix sont des informations d'achat ; ils ne disent rien du principe retenu ni des raisons de le retenir.",
   "Un vote ne remplace pas un argument : la majorité peut parfaitement choisir d'après le mauvais critère."],
  "Nommer ce qu'on perd est ce qui distingue un choix d'une préférence."),

q(C, "Deux réponses justes", "Pour Sainte-Luce, le disque et le tambour sont tous deux défendables. Cela signifie que…",
  ["l'exercice n'a pas UNE bonne réponse : il a des réponses bien ou mal défendues",
   "l'énoncé est mal posé",
   "il manque des données pour trancher",
   "les deux freins sont identiques"],
  "Beaucoup de questions techniques n'ont pas de réponse unique. Ce qui se juge alors n'est pas le "
  "résultat mais le raisonnement : les critères retenus, les chiffres cités, et les pertes "
  "assumées.",
  "Le disque gagne sous la pluie, le tambour gagne en corrosion ; les deux sont fondés à Sainte-Luce, "
  "selon qu'on redoute davantage la descente ou le sel.",
  "Chercher « la » bonne réponse et rester bloqué quand il y en a deux.",
  ["",
   "L'énoncé est complet : il donne le lieu, l'usage, six critères et quinze essais. C'est la réalité qui admet deux solutions.",
   "Toutes les données nécessaires sont fournies ; en ajouter ne trancherait pas, car le désaccord porte sur l'importance des critères, pas sur les faits.",
   "Ils sont très différents : 190 g d'écart de masse, un point de corrosion, une réparabilité qui va de 4/5 à 3/5."],
  "Certaines questions n'ont pas une réponse, mais des réponses bien ou mal défendues."),

q(C, "Ce qu'on ne mesure pas", "Aucun des six critères ne parle du bruit du frein. Cela signifie…",
  ["qu'un tableau ne contient que ce qu'on a décidé d'y mettre : il faut aussi regarder ce qui manque",
   "que le bruit n'a aucune importance",
   "que les trois freins font le même bruit",
   "qu'on ne peut pas mesurer un bruit"],
  "Un tableau comparatif porte les traces de celui qui l'a construit. Les colonnes absentes ne "
  "sont pas des critères sans importance : ce sont des critères auxquels personne n'a pensé, ou "
  "qu'on a jugé trop difficiles à mesurer.",
  "Un frein qui grince finit par ne plus être serré à fond : le bruit a des conséquences très "
  "concrètes sur la sécurité.",
  "Prendre le tableau pour la description complète de la réalité.",
  ["",
   "Le bruit compte beaucoup dans l'usage réel, et il influence directement la façon dont on se sert du frein.",
   "Ils font des bruits très différents : un frein à disque mal réglé siffle, un tambour est presque silencieux.",
   "Un bruit se mesure très bien, avec un sonomètre ou une application, à distance et en conditions fixées."],
  "Regarde aussi les colonnes qui ne sont pas là.",
  img=IMG_TABLEAU),
