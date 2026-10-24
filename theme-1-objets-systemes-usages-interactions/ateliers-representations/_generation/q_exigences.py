# -*- coding: utf-8 -*-
"""Les 30 questions du QCM de l'atelier « diagramme des exigences » (diagramme des exigences SysML).

Toutes les bonnes réponses sont en position 0 ici : la répartition sur A/B/C/D
est faite ensuite par `_outils/fix_r.js`, de façon déterministe.

Répartition : 4e_C2.2 (12) · 4e_C8.3 (8) · 3e_C3.3 (10). Cinq questions illustrées.
La flexibilité (classes F0–F3, tolérance chiffrée) porte cinq questions.
"""
from qbanque import Banque

B = Banque()
q = B.q

IMG_ARROSAGE = {"src": "Images/exigences_arrosage.svg",
                "alt": "Diagramme des exigences du système d'arrosage : en haut l'exigence 1, Arrosage autonome ; reliées à "
                       "elle par un petit cercle à croix, quatre exigences-filles : 1.1 Étanchéité (IPX4 au moins), "
                       "1.2 Sobriété (au plus 10 L par jour), 1.3 Réglage (sans outil, 2 min au plus), 1.4 Sécurité "
                       "électrique (très basse tension, 12 V)."}
IMG_TESTS = {"src": "Images/exigences_arrosage_tests_verify.svg",
             "alt": "Le même diagramme du système d'arrosage, avec sous chaque exigence un bloc testCase relié par une "
                    "flèche en tirets « verify » qui monte du test vers l'exigence : T3 vers 1.1, T1 vers 1.2, T4 vers "
                    "1.3, T2 vers 1.4."}
IMG_SUIVI = {"src": "Images/exigences_suivi_a_distance.svg",
             "alt": "Deux exigences-mères : 1, Arrosage autonome, et 2, Suivi à distance. Sous l'exigence 2, reliées par "
                    "son petit cercle à croix, deux filles : 2.1 Compte rendu (5 min au plus après chaque arrosage) et "
                    "2.2 Alerte cuve (dès qu'il reste 50 L)."}
IMG_STATION = {"src": "Images/exigences_station.svg",
               "alt": "Diagramme des exigences de la station d'alerte cyclonique : l'exigence 1, Alerte cyclonique, contient "
                      "1.1 Étanchéité (IP65 au moins), 1.2 Autonomie (72 h au moins sur batterie), 1.3 Alerte audible "
                      "(100 m au moins), 1.4 Réparabilité (6/10 au moins), 1.5 Coût (300 € au plus)."}
IMG_STATION_A = {"src": "Images/exigences_station_boitier_a.svg",
                 "alt": "Le diagramme de la station avec, en bas, le bloc « Boîtier A » (IP66, 80 h, 110 m, réparabilité "
                        "5/10, 290 €) ; quatre flèches « satisfy » montent de lui vers 1.1, 1.2, 1.3 et 1.5 ; aucune vers 1.4."}

# ═══════════════ 4e_C2.2 — Repérer et expliquer les contraintes, exigences (12) ═══════════════
C = "4e_C2.2"

q(C, "Les deux noms du schéma",
  "Le diagramme des exigences est souvent appelé…",
  ["le diagramme des exigences SysML",
   "le diagramme pieuvre des contraintes",
   "le diagramme de Gantt des exigences",
   "le diagramme FAST du cahier des charges"],
  "Les ingénieurs l'appellent <b>diagramme des exigences SysML</b>, du nom du langage de schémas SysML. Les deux noms "
  "désignent le même schéma : des blocs d'exigence reliés entre eux.",
  "Dans un logiciel d'ingénierie, le menu « requirement diagram » ouvre ce schéma.",
  "Confondre les représentations entre elles parce qu'elles ont toutes un surnom.",
  ["",
   "Le diagramme pieuvre montre les interacteurs autour de l'objet ; il ne contient ni Id ni niveau chiffré.",
   "Le diagramme de Gantt place des tâches dans le temps : il organise un projet, il ne range pas des exigences.",
   "Le FAST va des fonctions techniques aux solutions, le « comment » : il ne fait pas partie du cahier des charges."],
  "Diagramme des exigences = diagramme des exigences SysML.")

q(C, "Ce que veut dire SysML",
  "SysML (Systems Modeling Language) désigne…",
  ["un langage de schémas pour modéliser les systèmes",
   "un logiciel qui simule le fonctionnement des machines",
   "une norme qui fixe la tension des appareils électriques",
   "une liste officielle des systèmes autorisés en France"],
  "SysML veut dire « langage de modélisation des systèmes » : un ensemble de schémas normalisés, lus de la même façon "
  "par les ingénieurs du monde entier. Le diagramme des exigences en fait partie.",
  "Le diagramme des cas d'utilisation est un autre schéma du même langage SysML.",
  "Prendre SysML pour un logiciel ou pour une loi.",
  ["",
   "Un logiciel peut dessiner du SysML, mais SysML lui-même est une façon d'écrire des schémas, pas un programme.",
   "Les tensions sont fixées par d'autres textes ; SysML ne fixe aucune valeur, il dessine les exigences.",
   "SysML n'autorise ni n'interdit rien : c'est un langage, utilisé dans le monde entier, pas une liste française."],
  "SysML : un langage de schémas.")

q(C, "Lire un Id",
  "Sur ce diagramme, que dit « Id = 1.2 » dans le bloc Sobriété ?",
  ["Sobriété est la deuxième fille de l'exigence 1.",
   "Le système utilise 1,2 litre d'eau par jour.",
   "Sobriété est la deuxième exigence la plus grave.",
   "L'exigence Sobriété a été corrigée deux fois."],
  "L'<b>Id</b> (identifiant) range l'exigence dans l'arbre : 1 est la mère, .2 dit que Sobriété est sa deuxième fille.",
  "Id 2.1 : la première fille de l'exigence 2.",
  "Lire l'Id comme une mesure ou un rang d'importance.",
  ["",
   "Le volume d'eau est dans le texte du bloc (au plus 10 L) ; l'Id est un numéro, pas une mesure.",
   "L'Id ne classe pas les exigences par gravité : il dit seulement leur place sous la mère.",
   "Un Id ne compte pas les corrections : il range l'exigence dans l'arbre."],
  "Id : la place de l'exigence dans l'arbre.",
  img=IMG_ARROSAGE)

q(C, "Le petit cercle à croix",
  "Dans un diagramme des exigences, le petit cercle à croix ⊕ au bout d'un trait indique…",
  ["le côté de l'exigence-mère, qui contient l'autre",
   "une exigence qu'il faut vérifier en tout premier lieu",
   "le test qui vérifie l'exigence placée au-dessus",
   "une exigence que rien ne satisfait encore"],
  "C'est le lien de <b>contenance</b> : le ⊕ est du côté de l'exigence-mère, qui contient ses exigences-filles.",
  "Le ⊕ sous « Arrosage autonome » : elle contient Étanchéité, Sobriété, Réglage et Sécurité électrique.",
  "Prendre le ⊕ pour un ordre de priorité ou pour un test.",
  ["",
   "Le ⊕ ne donne aucun ordre de vérification : il dit seulement qui contient qui.",
   "Un test se dessine dans un bloc « testCase », relié par une flèche en tirets « verify », pas par un ⊕.",
   "Le ⊕ ne dit rien des solutions : la flèche « satisfy » relie une solution à l'exigence qu'elle satisfait."],
  "⊕ : du côté de la mère.")

q(C, "Une mère et ses filles",
  "L'exigence 1 contient 1.1 à 1.4. Le prototype tient 1.1, 1.2 et 1.4, mais pas 1.3. L'exigence 1 est…",
  ["non tenue : il lui faut toutes ses filles",
   "tenue : trois filles sur quatre suffisent",
   "tenue : 1.3 ne parle que du confort de la gardienne",
   "impossible à juger sans son propre test"],
  "Une exigence-mère est précisée par ses filles : elle n'est tenue que si <b>toutes</b> ses filles le sont.",
  "Un boîtier sobre et sûr, mais qu'on ne peut régler qu'avec un tournevis, ne tient pas l'arrosage autonome.",
  "Croire qu'une majorité de filles suffit.",
  ["",
   "Trois sur quatre laisse une exigence manquée : la gardienne ne pourrait pas régler l'heure sans outil.",
   "1.3 relève de l'ergonomie, et c'est une exigence comme les autres : elle compte.",
   "La mère n'a ni critère ni niveau à elle : on la juge par ses filles, sans test propre."],
  "La mère n'est tenue que si toutes ses filles le sont.")

q(C, "Critère ou niveau",
  "Dans « le boîtier doit résister aux projections d'eau : IPX4 au moins », que désigne « IPX4 au moins » ?",
  ["le niveau : la valeur à atteindre",
   "le critère : ce que l'on mesure",
   "la flexibilité : l'écart que l'on accepte",
   "la solution : le boîtier choisi"],
  "Le <b>critère</b> est ce qu'on contrôle (l'indice de protection contre l'eau) ; le <b>niveau</b> est la valeur à "
  "atteindre (IPX4 au moins).",
  "« Au plus 10 L » est le niveau ; « le volume d'eau par jour » est le critère.",
  "Inverser critère et niveau.",
  ["",
   "Le critère, c'est l'indice de protection lui-même ; « IPX4 au moins » est la valeur à atteindre.",
   "La flexibilité est une autre colonne du cahier des charges (F0 à F3) ; elle dit l'écart accepté autour du niveau.",
   "Le texte d'une exigence ne nomme pas de boîtier : il dit ce qu'on attend, pas la solution."],
  "Critère : ce qu'on mesure. Niveau : la valeur à atteindre.")

q(C, "Retrouver le critère par l'unité",
  "Un bloc d'exigence se termine par « … au plus 35 dB à 1 m ». Quel est son critère ?",
  ["le niveau sonore, mesuré à 1 m",
   "la tension qui alimente la pompe",
   "la durée de marche de la pompe",
   "le volume d'eau pompé par jour"],
  "L'unité du niveau trahit le critère : le décibel (dB) mesure le <b>bruit</b>. Le critère est donc le niveau sonore, "
  "mesuré à 1 m.",
  "12 V → une tension ; 10 L → un volume ; 2 min → une durée.",
  "Chercher le critère sans regarder l'unité.",
  ["",
   "Une tension se mesure en volts (V), pas en décibels.",
   "Une durée se mesure en secondes ou en minutes, pas en décibels.",
   "Un volume se mesure en litres (L), pas en décibels."],
  "L'unité du niveau dit le critère.")

q(C, "Ce que, pas comment",
  "Laquelle de ces phrases peut être le texte d'un bloc d'exigence ?",
  ["« Le système doit utiliser au plus 10 L d'eau par jour. »",
   "« Le système doit avoir une électrovanne de grande marque. »",
   "« Le système doit être vraiment très économe en eau. »",
   "« Le système doit plaire à la gardienne et aux élèves. »"],
  "Une exigence dit <b>ce que</b> le système doit faire, avec un critère (le volume d'eau par jour) et un niveau "
  "(au plus 10 L) : on peut la vérifier.",
  "« L'alerte doit partir dès qu'il reste 50 L dans la cuve » : critère et niveau, aucune solution.",
  "Écrire une solution, ou une phrase sans niveau.",
  ["",
   "Une électrovanne est une solution : elle dit COMMENT faire. Elle satisfera peut-être l'exigence, elle n'en est pas une.",
   "« Vraiment très économe » n'a ni nombre ni unité : personne ne peut dire si c'est réussi.",
   "Plaire est un avis, qui change d'une personne à l'autre : aucun test ne peut le trancher."],
  "Une exigence : ce que, avec critère et niveau.")

q(C, "La catégorie de la sobriété",
  "« Le système doit utiliser au plus 10 L d'eau par jour. » Dans quelle catégorie du programme range-t-on cette exigence ?",
  ["les incidences environnementales",
   "l'ergonomie et le confort d'usage",
   "la fiabilité dans le temps",
   "la qualité de fabrication"],
  "Ne pas gaspiller l'eau de la cuve, c'est limiter les effets du système sur la planète : <b>incidences "
  "environnementales</b>.",
  "Économiser l'énergie ou réduire les déchets relève aussi des incidences environnementales.",
  "Ranger dans l'ergonomie tout ce qui « rend service ».",
  ["",
   "L'ergonomie rend le système facile à utiliser ; le volume d'eau ne change rien au geste de la gardienne.",
   "La fiabilité parle des pannes ; 10 L par jour ne dit rien de la durée de vie du système.",
   "La qualité de fabrication parle de la finition ; ici, il s'agit de l'eau consommée."],
  "Ne pas gaspiller : incidences environnementales.")

q(C, "L'étanchéité, quelle catégorie ?",
  "Sans l'exigence « résister aux projections d'eau », l'écran du boîtier s'éteint après une averse. Quelle catégorie ?",
  ["la fiabilité : pas de panne sous la pluie",
   "la qualité : un boîtier joliment fini",
   "l'ergonomie : un écran facile à lire",
   "la sécurité : personne ne se blesse"],
  "Un boîtier qui prend l'eau tombe en panne : continuer à fonctionner, par tous les temps, c'est la <b>fiabilité</b>.",
  "Une lampe de jardin qui s'éteint au premier orage manque de fiabilité.",
  "Ranger toute histoire d'eau et d'électricité dans la sécurité.",
  ["",
   "La finition ne protège pas de l'eau : ce sont les joints et la forme du boîtier qui comptent.",
   "L'écran peut être très lisible et s'éteindre quand même à la première averse.",
   "Le boîtier fonctionne en très basse tension, 12 V : l'eau le fait tomber en panne, elle ne le rend pas dangereux."],
  "Fonctionner sans panne, par tous les temps : fiabilité.")

q(C, "Sous la bonne mère",
  "Sur ce diagramme, pourquoi « Alerte cuve » est-elle une fille de l'exigence 2, et non de l'exigence 1 ?",
  ["Elle précise comment la gardienne suit l'arrosage de loin.",
   "La cuve est un composant que le système doit contenir.",
   "L'exigence 2 est la plus récente des deux exigences-mères.",
   "Chaque exigence-mère doit avoir exactement deux filles."],
  "Une exigence-fille <b>précise</b> sa mère. L'alerte part sur le smartphone : elle précise « suivre l'arrosage sur son "
  "smartphone », l'exigence 2.",
  "« Compte rendu », un message après chaque arrosage, précise aussi l'exigence 2.",
  "Ranger une exigence d'après un mot qui revient (l'eau) plutôt que d'après ce qu'elle précise.",
  ["",
   "La cuve est un élément du jardin, pas une exigence ; et ce qui est rangé ici, c'est l'alerte, pas la cuve.",
   "L'ordre d'écriture ne décide de rien : seule compte la phrase que la fille précise.",
   "Une mère peut avoir une, deux ou dix filles : l'exigence 1 en a quatre."],
  "Une fille précise sa mère.",
  img=IMG_SUIVI)

q(C, "Une norme, où la mettre ?",
  "Une norme internationale fixe ce que veut dire « IPX4 ». Où cette exigence apparaît-elle ?",
  ["dans un bloc d'exigence, avec le niveau IPX4",
   "dans une bulle du diagramme pieuvre du jardin",
   "dans un bloc testCase, à la place de l'essai",
   "dans le diagramme de Gantt du projet du club"],
  "Une norme ne touche pas l'objet : elle s'impose à ceux qui le conçoivent. Elle donne une <b>exigence</b>, écrite dans un "
  "bloc avec son niveau.",
  "Bloc 1.1, Étanchéité : « résister aux projections d'eau : IPX4 au moins ».",
  "Mettre une norme dans une bulle d'interacteur.",
  ["",
   "Les bulles de la pieuvre sont des interacteurs (usagers, données, objets, environnement) ; une norme n'en est pas un.",
   "Le bloc testCase décrit l'essai qui vérifie l'exigence ; la norme, elle, fixe le niveau à atteindre.",
   "Le Gantt place des tâches dans le temps ; il ne contient pas les exigences de l'objet."],
  "Une norme donne une exigence, jamais une bulle.")

# ═══════════════ 4e_C8.3 — Proposer un protocole de test (8) ═══════════════
C = "4e_C8.3"

q(C, "Le sens de « verify »",
  "Sur ce diagramme, une flèche « verify » monte du test T1 vers l'exigence 1.2. Elle veut dire…",
  ["le test T1 vérifie l'exigence 1.2",
   "l'exigence 1.2 vérifie le test T1",
   "le test T1 satisfait l'exigence 1.2",
   "le test T1 se fait avant l'exigence 1.2"],
  "« Verify » veut dire vérifier : la flèche va <b>du test vers l'exigence</b> qu'il vérifie.",
  "T2, la mesure au multimètre, vérifie 1.4, la très basse tension.",
  "Lire la flèche à l'envers, ou confondre « verify » et « satisfy ».",
  ["",
   "Une exigence ne vérifie rien : c'est le test qui mesure et qui prouve.",
   "« Satisfy » relie une solution (un boîtier, un composant) à l'exigence ; un test, lui, la vérifie.",
   "La flèche ne dit aucun ordre dans le temps : elle dit quel test prouve quelle exigence."],
  "« Verify » : du test vers l'exigence.",
  img=IMG_TESTS)

q(C, "Ce qui manque au protocole",
  "« On arrose le boîtier pendant 10 minutes, puis on regarde. » Que manque-t-il à ce protocole ?",
  ["le seuil à atteindre : aucune goutte dedans",
   "le prix de l'arroseur utilisé pour l'essai",
   "le nom de l'élève qui tient l'arroseur",
   "l'heure de la journée où l'on arrose"],
  "Un protocole dit ce qu'on mesure, avec quoi, comment, et le <b>seuil</b> à atteindre. Sans seuil, « on regarde » ne "
  "permet pas de conclure.",
  "« … puis on ouvre le boîtier : validé s'il n'y a aucune goutte à l'intérieur. »",
  "Oublier le résultat attendu.",
  ["",
   "Le prix de l'arroseur ne change rien au résultat : il ne dit pas quand l'exigence est tenue.",
   "Qui arrose ne change pas ce qu'on doit observer ; le seuil, lui, manque.",
   "L'heure ne joue pas sur l'étanchéité ; ce qui manque, c'est ce qu'on doit trouver dans le boîtier."],
  "Un protocole sans seuil ne conclut rien.")

q(C, "Le bon instrument",
  "Pour vérifier l'exigence « très basse tension : 12 V », quel instrument faut-il ?",
  ["un multimètre en position voltmètre",
   "un compteur d'eau gradué en litres",
   "un chronomètre réglé en secondes",
   "un thermomètre à affichage numérique"],
  "Une tension se mesure en volts (V), avec un <b>multimètre</b> réglé en voltmètre. À 12 V, la mesure est sans danger.",
  "Un compteur d'eau vérifie « au plus 10 L par jour » ; un chronomètre, « 2 min au plus ».",
  "Choisir l'instrument d'une autre exigence du même diagramme.",
  ["",
   "Le compteur d'eau mesure un volume ; il vérifie la sobriété, pas la tension.",
   "Le chronomètre mesure une durée ; il vérifie le réglage, pas la tension.",
   "Le thermomètre mesure une température ; aucune exigence du diagramme n'en parle."],
  "Volts : multimètre.")

q(C, "Un avis n'est pas un test",
  "« On demande à la gardienne si le boîtier lui semble étanche. » Est-ce un protocole de test ?",
  ["Non : rien n'est mesuré, aucun seuil n'est fixé.",
   "Oui : la gardienne connaît bien son jardin.",
   "Oui, s'il est posé à plusieurs personnes.",
   "Non : seul un ingénieur peut tester un boîtier."],
  "Un test <b>mesure</b> et compare à un seuil. Un avis, même sincère, ne prouve pas que l'eau n'entre pas.",
  "Arroser 10 min de tous côtés, puis chercher des gouttes : là, on mesure.",
  "Confondre impression et mesure.",
  ["",
   "Bien connaître le jardin ne permet pas de voir l'eau qui entre dans un boîtier fermé.",
   "Dix avis restent dix avis : sans mesure ni seuil, on ne conclut toujours rien.",
   "Un élève peut tester, s'il suit un protocole : ce qui compte, c'est la mesure, pas le métier."],
  "Un test mesure ; un avis non.")

q(C, "Le seuil d'abord",
  "Pourquoi écrit-on le seuil à atteindre AVANT de faire l'essai ?",
  ["pour ne pas l'adapter au résultat obtenu",
   "pour gagner du temps pendant l'essai",
   "parce que l'instrument de mesure l'exige",
   "pour pouvoir sauter l'essai si on est pressé"],
  "Écrit avant, le seuil est une promesse : on compare le résultat à ce qu'on attendait, sans être tenté de dire « c'est "
  "bon quand même ».",
  "« Validé si le message arrive en 5 min au plus » : écrit avant d'appuyer sur le chronomètre.",
  "Fixer le seuil après coup, d'après ce qu'on a mesuré.",
  ["",
   "Le temps de l'essai reste le même ; ce que l'on gagne, c'est un jugement honnête.",
   "Un instrument mesure, il n'exige rien : c'est la méthode qui demande le seuil avant.",
   "Le seuil ne remplace jamais l'essai : sans mesure, il n'y a rien à comparer."],
  "Le seuil s'écrit avant l'essai.")

q(C, "Dans la marge",
  "Niveau : au plus 10 L d'eau par jour, flexibilité F2 (de 9 à 11 L acceptés). Le test mesure 10,8 L. L'exigence est…",
  ["validée : l'écart reste dans la marge",
   "non validée : 10,8 L dépasse 10 L",
   "non validée : F2 n'accepte aucun écart",
   "à refaire : le compteur est sûrement faux"],
  "L'écart vaut +0,8 L ; la flexibilité F2 accepte jusqu'à 11 L. L'écart reste <b>dans la marge</b> : l'exigence est validée.",
  "11,5 L, en revanche, dépasserait la marge : non validée, même si c'est presque.",
  "Refuser tout écart, quelle que soit la flexibilité.",
  ["",
   "10,8 L dépasse le niveau, c'est vrai ; mais la flexibilité dit justement que le client accepte jusqu'à 11 L.",
   "« Aucun écart », c'est F0 ; F2 est une flexibilité moyenne, négociable.",
   "Rien n'indique une erreur de mesure : 10,8 L est un résultat plausible, à juger avec la marge."],
  "Écart dans la marge : validée.")

q(C, "Presque, en F0",
  "Exigence : « la pompe démarre 30 s au plus après l'heure choisie », flexibilité F0. Le chronomètre indique 31 s. L'exigence est…",
  ["non validée : en F0, aucun écart n'est accepté",
   "validée : une seconde de trop, c'est presque rien",
   "validée : le chronomètre a pu se tromper",
   "non validée : il fallait mesurer en minutes"],
  "En <b>F0</b>, le niveau est impératif : 31 s pour « 30 s au plus », c'est un écart, donc l'exigence n'est pas validée. "
  "On règle, puis on refait le test.",
  "Même logique pour 12 V en F0 : 24 V mesurés, ce n'est pas validé, même si 24 V reste une très basse tension.",
  "Valider un résultat « presque bon ».",
  ["",
   "« Presque » ne compte pas en F0 : c'est justement la classe où le client n'accepte aucun écart.",
   "Si on doute de l'instrument, on refait la mesure ; on ne valide pas un écart sur un doute.",
   "Les secondes conviennent pour mesurer 30 s ; changer d'unité ne changerait pas l'écart."],
  "F0 : aucun écart ne se valide.")

q(C, "Calculer un écart",
  "Niveau : au plus 10 L par jour. Résultat du test : 11,5 L. L'écart vaut…",
  ["+1,5 L : 1,5 L de trop",
   "−1,5 L : 1,5 L de moins",
   "21,5 L : les deux ajoutés",
   "1,15 : l'un divisé par l'autre"],
  "<b>Écart = résultat − niveau</b> : 11,5 L − 10 L = +1,5 L. Le signe + dit qu'on a dépassé le niveau.",
  "4 min mesurées pour « 2 min au plus » : écart de +2 min.",
  "Faire la soustraction à l'envers, ou ajouter au lieu de soustraire.",
  ["",
   "−1,5 L voudrait dire qu'on a utilisé moins de 10 L ; or 11,5 L, c'est plus.",
   "Ajouter le résultat et le niveau ne dit rien de l'écart entre eux.",
   "Le quotient 1,15 compare autrement ; l'écart demandé ici est une différence, en litres."],
  "Écart = résultat − niveau.")

# ═══════════════ 3e_C3.3 — Évaluer les OST selon des exigences ou des critères (10) ═══════════════
C = "3e_C3.3"

q(C, "L'égalité satisfait",
  "Exigence : « la station doit tenir 72 h au moins sur batterie ». Le boîtier B tient 72 h. L'exigence est…",
  ["satisfaite : l'égalité suffit",
   "non satisfaite : il faut plus de 72 h",
   "satisfaite seulement si elle est F3",
   "impossible à juger sans le prix"],
  "« Au moins 72 h » veut dire 72 h <b>ou plus</b> : 72 h exactement satisfait l'exigence.",
  "« Au plus 300 € » : un boîtier à 300 € pile la satisfait aussi.",
  "Croire qu'il faut dépasser strictement le niveau.",
  ["",
   "« Au moins » inclut la valeur elle-même : 72 h atteint le niveau.",
   "La flexibilité ne sert qu'en cas d'écart ; ici, il n'y en a aucun.",
   "Le prix est une autre exigence (1.5) ; il ne change rien à l'autonomie."],
  "Au moins : cette valeur ou plus.")

q(C, "Au plus",
  "Exigence : « le boîtier doit coûter 300 € au plus ». Lequel la satisfait ?",
  ["le boîtier à 290 €",
   "le boîtier à 310 €",
   "le boîtier à 350 €",
   "aucun : il faut 300 € pile"],
  "« Au plus 300 € » veut dire 300 € <b>ou moins</b> : 290 € satisfait l'exigence.",
  "Un boîtier à 240 € la satisfait aussi.",
  "Lire « au plus » comme « au moins ».",
  ["",
   "310 € dépasse 300 € : « au plus » interdit de dépasser.",
   "350 € dépasse 300 € de 50 € : l'exigence n'est pas satisfaite (la flexibilité dira si l'écart se négocie).",
   "« Au plus » n'impose pas une valeur exacte : tout prix jusqu'à 300 € convient."],
  "Au plus : cette valeur ou moins.")

q(C, "IP66 pour IP65",
  "Sur ce diagramme, l'exigence 1.1 demande « IP65 au moins ». Un boîtier IP66 la…",
  ["satisfait : 6 ≥ 6 et 6 ≥ 5",
   "ne satisfait pas : 66 n'est pas 65",
   "ne satisfait pas : il faut moins",
   "satisfait s'il coûte moins de 300 €"],
  "Le code IP a deux chiffres : poussière, puis eau. Chacun doit être au moins égal : 6 ≥ 6 et 6 ≥ 5. IP66 résiste même à "
  "des jets plus puissants.",
  "IP54 : 5 < 6 et 4 < 5, il ne satisfait pas « IP65 au moins ».",
  "Exiger le code exact, au lieu de comparer chiffre par chiffre.",
  ["",
   "« Au moins » n'exige pas le même code : un chiffre plus grand protège mieux.",
   "Pour l'IP, un chiffre plus petit protège moins : IP54 serait refusé.",
   "Le prix est l'exigence 1.5 ; il n'entre pas dans le jugement de l'étanchéité."],
  "IP : chiffre par chiffre, au moins égal.",
  img=IMG_STATION)

q(C, "Une flèche qui manque",
  "Sur ce diagramme, pourquoi aucune flèche « satisfy » ne va du boîtier A vers l'exigence 1.4 ?",
  ["Sa note de 5/10 n'atteint pas le niveau 6/10.",
   "La réparabilité ne se mesure pas vraiment.",
   "L'exigence 1.4 est une exigence en F0.",
   "La flèche a été oubliée par le dessinateur."],
  "On ne dessine « satisfy » que si la solution <b>satisfait</b> l'exigence : 5/10 pour « 6/10 au moins », ce n'est pas le cas.",
  "Le boîtier B, à 9/10, a sa flèche « satisfy » vers 1.4.",
  "Dessiner « satisfy » vers toutes les exigences par habitude.",
  ["",
   "L'indice de réparabilité est une note sur 10, affichée pour certains appareils : il se compare comme un nombre.",
   "1.4 est en F2 (5/10 accepté) ; de toute façon, la flèche dit si le niveau est atteint, pas la classe.",
   "L'absence est voulue : elle montre l'exigence que A ne satisfait pas."],
  "« Satisfy » seulement si le niveau est atteint.",
  img=IMG_STATION_A)

q(C, "Satisfy ou verify",
  "Quelle flèche relie une solution à l'exigence qu'elle satisfait ?",
  ["« satisfy », de la solution vers l'exigence",
   "« verify », du test vers l'exigence",
   "le ⊕, de l'exigence-mère vers la fille",
   "« satisfy », de l'exigence vers la solution"],
  "« Satisfy » veut dire satisfaire : la flèche en tirets va de la <b>solution</b> (un bloc « block ») vers l'exigence.",
  "Boîtier A → « satisfy » → 1.1 Étanchéité.",
  "Confondre « satisfy » et « verify », ou tracer la flèche à l'envers.",
  ["",
   "« Verify » existe bien, mais elle relie un TEST à l'exigence qu'il vérifie, pas une solution.",
   "Le ⊕ relie une exigence-mère à ses filles : il ne parle pas des solutions.",
   "La flèche part de la solution : c'est elle qui satisfait l'exigence, pas l'inverse."],
  "« Satisfy » : de la solution vers l'exigence.")

q(C, "La phrase du client",
  "Pour « 72 h au moins », la présidente du comité dit : « 60 heures, à la rigueur, si la station m'envoie un message quand sa batterie faiblit. » Quelle classe de flexibilité ?",
  ["F1 : un écart, à une seule condition",
   "F0 : aucun écart n'est accepté",
   "F2 : un petit écart, sans condition",
   "F3 : un écart large, sans condition"],
  "Un écart est accepté (60 h au lieu de 72 h), mais <b>seulement à une condition</b> précise : c'est une flexibilité "
  "faible, <b>F1</b>.",
  "« 5 sur 10, ça ira aussi » pour 6/10 : un petit écart sans condition → F2.",
  "Choisir la classe d'après l'importance de l'exigence au lieu de l'écart accepté.",
  ["",
   "F0 voudrait dire : 72 h, rien de moins. Or la présidente accepte 60 h.",
   "F2 accepterait l'écart sans condition ; ici, il faut le message de batterie faible.",
   "F3 accepterait un écart large sans rien demander ; ici, l'écart est encadré par une condition."],
  "Un écart à une condition : F1.")

q(C, "La marge en chiffres",
  "Pour « 300 € au plus », la présidente dit : « Même 400 €, on trouvera l'argent. » Écrite en chiffres, la marge est…",
  ["300 € demandé ; jusqu'à 400 € accepté",
   "300 € ± 400 €, soit de −100 € à 700 €",
   "400 € au moins, pour un boîtier sérieux",
   "300 € exactement, sans aucun écart"],
  "La flexibilité s'écrit soit par une <b>classe</b> (ici F3, très négociable), soit par une <b>tolérance chiffrée</b> : "
  "300 € demandé, jusqu'à 400 € accepté.",
  "Pour 10 L par jour en F2 : « de 9 à 11 L acceptés ».",
  "Écrire une tolérance qui ne correspond pas à ce que dit le client.",
  ["",
   "± 400 € donnerait un prix négatif ou de 700 € : rien à voir avec « même 400 € ».",
   "« Au moins 400 € » forcerait à payer plus : la présidente accepte jusqu'à 400 €, elle ne l'exige pas.",
   "« Exactement », c'est une flexibilité nulle, F0 : or elle accepte 100 € de plus."],
  "Deux écritures : une classe, ou une tolérance chiffrée.")

q(C, "Une exigence F0 manquée",
  "Le boîtier B est le moins cher et le plus réparable, mais il est IP54 pour « IP65 au moins, F0 ». Que fait-on ?",
  ["On l'élimine : en F0, aucun écart n'est accepté.",
   "On le prend : il gagne sur trois des critères.",
   "On le prend, mais on l'installe sous un abri.",
   "On le garde, si son prix baisse encore un peu."],
  "Une exigence <b>F0</b> est impérative : un boîtier qui la manque est éliminé, quels que soient ses autres atouts.",
  "Le boîtier A manque 1.4 en F2 (5/10 accepté) : lui reste possible.",
  "Rattraper une exigence impérative par d'autres qualités.",
  ["",
   "Gagner ailleurs ne rattrape pas l'eau qui entre pendant un cyclone : la sirène se tairait.",
   "Un abri réduirait la pluie, pas les rafales chargées d'eau d'un cyclone ; et le comité n'accepte aucun écart sur 1.1.",
   "Le prix est une autre exigence : le baisser ne rend pas le boîtier plus étanche."],
  "Une exigence F0 manquée élimine la solution.")

q(C, "Départager",
  "Deux boîtiers satisfont chacun quatre exigences sur cinq. Pour les départager, on regarde d'abord…",
  ["la flexibilité de l'exigence que chacun manque",
   "le prix, car c'est lui qui départage à tous les coups",
   "le nombre de niveaux que chacun dépasse",
   "la couleur et la forme de chaque boîtier"],
  "Le décompte ne dit pas <b>laquelle</b> manque. La flexibilité dit si l'écart est acceptable : en F0, jamais ; dans la "
  "marge, oui, à condition de le dire.",
  "A manque la réparabilité (F2, 5/10 accepté) ; B manque l'étanchéité (F0) : A l'emporte.",
  "Départager au prix ou « à la moyenne ».",
  ["",
   "Le prix est une exigence parmi d'autres ; le moins cher peut manquer une exigence impérative.",
   "Dépasser un niveau ne rattrape pas une exigence manquée : 150 m d'alerte n'empêchent pas l'eau d'entrer.",
   "La couleur et la forme ne figurent pas dans ce diagramme des exigences : elles ne départagent rien ici."],
  "On regarde la flexibilité de ce qui manque.")

q(C, "Faire monter la réparabilité",
  "Qu'est-ce qui fait monter l'indice de réparabilité d'un boîtier ?",
  ["un couvercle vissé et des pièces détachées en vente",
   "un couvercle collé, pour qu'il soit bien plus étanche",
   "un prix plus bas que celui des boîtiers concurrents",
   "une sirène plus puissante, entendue de plus loin"],
  "L'indice de réparabilité note la facilité à réparer : notice, <b>démontage</b> avec des outils courants, <b>pièces "
  "détachées</b> disponibles et leur prix.",
  "Un téléphone dont la batterie se change avec un simple tournevis a un meilleur indice.",
  "Confondre réparabilité et autres qualités du boîtier.",
  ["",
   "Un couvercle collé se démonte mal : l'étanchéité y gagne peut-être, la réparabilité y perd.",
   "Le prix d'achat est une autre exigence ; l'indice regarde le prix des PIÈCES, pas celui du boîtier.",
   "La puissance de la sirène est une performance (1.3) ; elle ne rend pas le boîtier plus facile à réparer."],
  "Réparable : démontable, avec des pièces détachées.")

Q = B.fin(30, {"4e_C2.2": 12, "4e_C8.3": 8, "3e_C3.3": 10})
