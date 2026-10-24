# -*- coding: utf-8 -*-
"""Les 30 questions du QCM de l'atelier « Le croquis » (croquis à main levée).

Toutes les bonnes réponses sont en position 0 ici : la répartition sur A/B/C/D
est faite ensuite par `_outils/fix_r.js`, de façon déterministe.

Répartition : 4e_C2.1 (10) · 4e_C7.2 (8) · 3e_C7.2 (12). Cinq questions illustrées.
"""
from qbanque import Banque

B = Banque()
q = B.q

IMG_A = {"src": "Images/croquis_borne_A.svg",
         "alt": "Croquis à main levée : Inès pose sa carte sur le lecteur d'une borne de vélos ; la borne bipe ; une flèche rouge "
                "part du vélo et s'éloigne de la borne, avec la légende « je tire le vélo en arrière, vers moi »."}
IMG_GARDIENNE = {"src": "Images/croquis_gardienne_reglage.svg",
                 "alt": "Croquis à main levée : la main de la gardienne appuie sur le bouton plus du boîtier du jardin ; une flèche "
                        "rouge marquée « fois 24 » ; l'écran affiche 18:00 ; une bulle dit que le soleil sur l'écran l'empêche de lire."}
IMG_CAPTEUR = {"src": "Images/croquis_cote_capteur_humidite.svg",
               "alt": "Croquis coté du capteur d'humidité, cotes en millimètres : longueur totale 100, largeur 20, tête 25, et 60 "
                      "sous le niveau de la terre ; à droite, le bord du bac, une planche de 22, la terre 40 sous le haut."}
IMG_BOITIER = {"src": "Images/croquis_cote_boitier_incomplet.svg",
               "alt": "Croquis coté d'un boîtier en perspective, cotes en millimètres : longueur 120, hauteur 80 ; couvercle fixé par "
                      "4 vis de 4 mm ; trou pour le câble sur le dessous, dessiné en pointillés."}
IMG_QUATRE = {"src": "Images/station_quatre_representations.svg",
              "alt": "Quatre vues numérotées de la station d'alerte : 1, un dessin à main levée avec légendes ; 2, des symboles "
                     "reliés par des traits droits ; 3, un boîtier en volume dans une fenêtre de logiciel avec les axes x, y, z ; "
                     "4, deux axes et une courbe du vent au fil de la nuit."}

# ═══════════════ 4e_C2.1 — Décrire l'expérience de l'utilisateur, du langage naturel au croquis (10) ═══════════════
C = "4e_C2.1"

q(C, "Ce qu'est un croquis",
  "En technologie, un croquis, c'est…",
  ["un dessin rapide, à main levée, qui montre l'essentiel",
   "un dessin exact, tracé à la règle et à l'échelle",
   "une photo de l'objet, prise sous son meilleur angle",
   "un dessin en volume, fait sur ordinateur avec un logiciel"],
  "Un croquis se fait vite, sans règle, et <b>choisit</b> ce qu'il montre : ce qui sert à comprendre, rien de plus.",
  "Le croquis A de la borne : une borne, un vélo, une flèche — rien n'est à l'échelle, et on comprend le geste.",
  "Croire qu'un croquis doit être exact, ou beau.",
  ["",
   "Un dessin à la règle et à l'échelle est un dessin technique ; le croquis, lui, se fait à main levée.",
   "Une photo montre tout, même l'inutile ; le croquis garde seulement ce qui sert à comprendre.",
   "Un dessin en volume fait avec un logiciel est une modélisation ; le croquis se fait au crayon, en quelques minutes."],
  "Croquis = rapide, à main levée, l'essentiel.")

q(C, "Les deux noms",
  "Dans les ateliers, comment appelle-t-on souvent le croquis ?",
  ["un croquis à main levée",
   "un dessin d'ensemble",
   "un plan d'architecte",
   "une vue éclatée"],
  "« À main levée » veut dire sans règle ni compas : le crayon suit la main. C'est le même dessin que le croquis du programme.",
  "« Fais-moi un croquis à main levée de ton idée » : on attend un dessin rapide, pas un plan.",
  "Confondre le croquis avec les dessins techniques précis.",
  ["",
   "Le dessin d'ensemble montre toutes les pièces d'un objet assemblé, tracées avec précision : ce n'est pas un croquis.",
   "Un plan d'architecte est tracé à l'échelle, avec des instruments ou un logiciel.",
   "Une vue éclatée montre les pièces écartées les unes des autres, dessinées avec précision."],
  "Croquis = croquis à main levée.")

q(C, "Le langage naturel",
  "Le programme demande de décrire l'expérience de l'usager « en partant du langage naturel ». Le langage naturel, c'est…",
  ["les mots de tous les jours, ceux de l'usager",
   "le langage des programmes informatiques",
   "les symboles normés des schémas électriques",
   "le vocabulaire scientifique de la technologie"],
  "On part de ce que l'usager dit ou écrit avec ses mots, puis on le traduit en croquis, puis en schémas, graphiques, algorithmes.",
  "« J'appuie, j'appuie… vingt-quatre fois ! » : c'est du langage naturel.",
  "Croire qu'il faut d'abord un vocabulaire technique.",
  ["",
   "Un langage de programmation est fait pour la machine ; on y arrive à la fin, par l'algorithme.",
   "Les symboles normés sont ceux du schéma, une étape qui vient après le croquis.",
   "Le témoignage de l'usager n'emploie pas de mots savants : ce sont ses mots à lui qui comptent."],
  "Langage naturel → croquis → schémas, graphiques, algorithmes.")

q(C, "La flèche rouge",
  "Sur ce croquis, que montre la flèche rouge ?",
  ["le geste d'Inès : elle tire le vélo en arrière",
   "le vent qui pousse le vélo vers la droite",
   "le chemin qu'Inès va suivre après la borne",
   "le câble qui relie la borne au vélo"],
  "Une <b>flèche de mouvement</b> montre un geste ou un déplacement, et son sens ; sa légende rouge dit lequel : « je tire le "
  "vélo en arrière, vers moi ».",
  "Dans le croquis de la gardienne, la flèche rouge montre l'appui sur le bouton +.",
  "Lire une flèche sans lire sa légende.",
  ["",
   "Le vent n'est pas dans le témoignage, et la légende de la flèche parle du geste d'Inès.",
   "La flèche part du vélo encore pris dans la borne : elle montre comment le sortir, pas un trajet.",
   "Il n'y a pas de câble entre la borne et le vélo : la roue avant est tenue par une pince."],
  "Une flèche de mouvement = un geste et son sens.",
  img=IMG_A)

q(C, "La légende",
  "Dans un croquis, une légende, c'est…",
  ["des mots reliés par un trait à ce qu'ils nomment",
   "le titre du croquis, écrit en grand au-dessus du dessin",
   "une petite histoire racontée sous le dessin",
   "la signature de celui qui a dessiné le croquis"],
  "Une légende nomme une partie du dessin ; le trait qui la relie évite toute confusion.",
  "« bouton + : une demi-heure par appui », relié au bouton par un trait.",
  "Écrire des mots autour du dessin, sans les relier à rien.",
  ["",
   "Le titre dit ce que montre tout le croquis ; une légende nomme une seule partie.",
   "Une histoire sous le dessin, c'est le témoignage ; le croquis le remplace par des légendes courtes.",
   "La signature ne nomme aucune partie du dessin : ce n'est pas une légende."],
  "Légende = des mots + un trait vers ce qu'ils nomment.")

q(C, "Montrer le ressenti",
  "Comment montrer, dans un croquis, que la gardienne voit mal l'écran à cause du soleil ?",
  ["une bulle « je ne vois rien ! » près de sa tête",
   "une cote qui donne la taille de l'écran, en millimètres",
   "une flèche qui montre l'appui sur le bouton +",
   "une légende qui donne la marque du boîtier"],
  "Le <b>ressenti</b> se dessine comme en bande dessinée : une bulle, un signe, une main en visière.",
  "Une bulle « aïe ! » pour un cache trop dur à soulever.",
  "Oublier le ressenti, alors que le programme parle de « ressenti et facilité d'usage ».",
  ["",
   "Une cote donne une dimension ; elle ne dit rien de ce que ressent la gardienne.",
   "Cette flèche montre le geste, c'est utile — mais elle ne dit pas que la gardienne voit mal.",
   "La marque du boîtier ne dit rien de l'expérience de la gardienne."],
  "Le ressenti → une bulle.")

q(C, "Une suite de croquis",
  "Plusieurs croquis numérotés, qui racontent un usage étape par étape, forment…",
  ["un storyboard",
   "un diagramme de Gantt",
   "un algorigramme",
   "une vue éclatée"],
  "Le <b>storyboard</b> (on dit aussi scénarimage) vient du cinéma : une case par moment, dans l'ordre.",
  "Trois cases : Inès pousse le vélo, rien ne bouge, elle tire.",
  "Confondre une suite d'images de l'usage avec une suite d'instructions.",
  ["",
   "Le diagramme de Gantt place des tâches dans le temps pour organiser un projet ; il ne montre pas l'usager.",
   "Un algorigramme montre l'ordre des instructions d'un programme, avec des symboles, pas des dessins de l'usage.",
   "Une vue éclatée montre les pièces d'un objet écartées : un seul dessin, sans usager."],
  "Une suite de croquis numérotés = un storyboard.")

q(C, "Ce qu'on laisse de côté",
  "Pour montrer comment Inès prend un vélo, que faut-il laisser de côté dans le croquis ?",
  ["la carte électronique cachée dans la borne",
   "la carte qu'Inès pose sur le lecteur",
   "la flèche qui tire le vélo vers Inès",
   "Inès elle-même, ou au moins sa main"],
  "Un croquis d'usage montre ce que vit l'usager : la personne, l'objet, le geste. Ce qu'il ne voit pas — l'intérieur de la "
  "borne — n'aide pas à comprendre.",
  "Pour la gardienne : on garde l'écran et les boutons, on laisse les fils du boîtier.",
  "Vouloir tout dessiner pour être complet.",
  ["",
   "La carte sur le lecteur est le premier moment du témoignage : sans elle, le geste est incomplet.",
   "La flèche est le cœur du croquis : elle dit dans quel sens sortir le vélo.",
   "Sans Inès, on ne voit plus l'expérience de l'usager, seulement une borne."],
  "Un croquis choisit : ce que vit l'usager.")

q(C, "Commencer par un croquis",
  "Pourquoi commence-t-on souvent par un croquis pour décrire l'expérience d'un usager ?",
  ["parce qu'il se fait vite et garde ce que vit l'usager",
   "parce qu'il est plus précis qu'un schéma ou qu'un plan",
   "parce que le programme interdit de commencer par un texte",
   "parce qu'on peut l'envoyer tel quel à une imprimante 3D"],
  "Le croquis traduit vite le témoignage en image ; on passe ensuite au schéma, au graphique ou à l'algorithme quand il faut "
  "préciser.",
  "Le croquis du réglage fait voir 24 appuis et un écran illisible : de quoi écrire ensuite l'algorithme du réglage.",
  "Croire que le croquis est l'étape la plus précise.",
  ["",
   "Un croquis est moins précis qu'un schéma : c'est justement pour cela qu'il est rapide.",
   "Le programme part du langage naturel, donc d'un texte : on ne l'interdit pas, on le traduit.",
   "Une imprimante 3D (en trois dimensions) a besoin d'une modélisation exacte, pas d'un dessin à main levée."],
  "Croquis d'abord : vite, et centré sur l'usager.")

q(C, "« × 24 »",
  "Sur ce croquis, qu'indique « × 24 » à côté de la flèche rouge ?",
  ["qu'elle appuie vingt-quatre fois sur +",
   "que le boîtier mesure 24 cm de haut",
   "qu'il est 24 heures quand elle règle",
   "que l'écran peut afficher vingt-quatre chiffres"],
  "La flèche montre le geste, « × 24 » combien de fois : de 6:00 à 18:00, à une demi-heure par appui, cela fait 24 appuis.",
  "« × 3 » à côté d'une flèche qui tourne : on tourne trois fois.",
  "Prendre un nombre pour une cote, sans regarder à quoi il est accroché.",
  ["",
   "Une hauteur serait une cote, avec ses deux pointes et son unité ; « × 24 » est collé à la flèche du geste.",
   "Elle règle l'arrosage en fin d'après-midi, et l'écran passe à 18:00 : « × 24 » ne donne pas l'heure.",
   "L'écran affiche quatre chiffres (18:00) ; « × 24 » compte les appuis."],
  "Un nombre près d'une flèche : combien de fois.",
  img=IMG_GARDIENNE)

# ═══════════════ 4e_C7.2 — Proposer une solution pour ajouter une fonction (croquis…) (8) ═══════════════
C = "4e_C7.2"

q(C, "Ce qu'est une cote",
  "Sur un croquis coté, une cote, c'est…",
  ["une dimension, avec une ligne à deux pointes",
   "une note sur 20 donnée au croquis",
   "une légende qui donne le nom d'une pièce du croquis",
   "un trait qui montre un mouvement"],
  "Une <b>cote</b> donne une dimension : une ligne de cote, une pointe à chaque bout, et un nombre avec son unité (ou « cotes en "
  "mm » pour tout le croquis).",
  "« 22 » entre les deux faces de la planche : la planche fait 22 mm d'épaisseur.",
  "Confondre la cote et la légende.",
  ["",
   "En technologie, « coter » veut dire donner les dimensions, pas noter le dessin.",
   "Une légende nomme, une cote mesure ; les deux vont souvent ensemble sur un croquis coté.",
   "Un trait qui montre un mouvement est une flèche de mouvement, avec une seule pointe."],
  "Cote = dimension + unité.")

q(C, "L'unité oubliée",
  "Sur un croquis, la cote « 24 » est écrite seule, sans unité nulle part. Quel est le risque ?",
  ["qu'on fabrique la pièce en cm au lieu de mm",
   "que le croquis soit refusé, car trop moche",
   "que la pièce change de matériau toute seule",
   "qu'on ne sache plus de quel côté se mesure la cote"],
  "Sans unité, 24 peut vouloir dire 24 mm ou 24 cm : une pièce dix fois trop grande. On écrit l'unité, ou une seule fois "
  "« cotes en mm ».",
  "Le croquis du capteur porte « cotes en mm » : toutes ses cotes sont en millimètres.",
  "Penser que l'unité « va de soi ».",
  ["",
   "La beauté du trait ne compte pas ; c'est l'unité qui manque, pas l'élégance.",
   "Le matériau ne dépend pas d'une cote : il s'écrit à part, dans une légende.",
   "La ligne de cote montre où la dimension se mesure ; c'est sa valeur qui reste incertaine."],
  "Toujours l'unité, ou « cotes en mm ».")

q(C, "Main levée et cotes",
  "Un croquis coté est tracé à main levée. Ses cotes sont-elles fiables ?",
  ["oui : ce sont les cotes qui donnent les dimensions",
   "non : seul un dessin à l'échelle donne des cotes",
   "non : il faut mesurer le dessin avec une règle",
   "oui, mais seulement si le dessin est fait en couleurs"],
  "Le dessin donne la forme ; les cotes donnent les vraies dimensions, même si le trait tremble.",
  "Sur le croquis du capteur, les pointes semblent courtes, mais la cote dit 60 mm : c'est la cote qui compte.",
  "Mesurer le dessin au lieu de lire les cotes.",
  ["",
   "Un dessin à l'échelle est utile, mais pas nécessaire : sur un croquis, ce sont les nombres qui font foi.",
   "Mesurer un croquis à la règle donne des valeurs fausses : il n'est pas à l'échelle.",
   "Les couleurs n'ont aucun rôle dans la fiabilité d'une cote."],
  "Croquis coté : la cote fait foi, pas le trait.")

q(C, "Lire une cote",
  "D'après ce croquis coté, quelle longueur du capteur faut-il enfoncer dans la terre ?",
  ["60 mm",
   "100 mm",
   "25 mm",
   "22 mm"],
  "La cote « 60 » va du niveau de la terre au bout des pointes ; la cote 100 est la longueur totale.",
  "100 − 60 = 40 mm restent hors de la terre, dont la tête de 25 mm.",
  "Prendre la plus grande cote sans regarder où elle commence et où elle finit.",
  ["",
   "100 mm, c'est la longueur totale du capteur, tête comprise : la tête doit rester au sec.",
   "25 mm, c'est la hauteur de la tête, l'électronique, qui doit rester hors de la terre.",
   "22 mm, c'est l'épaisseur de la planche du bac, pas une dimension du capteur."],
  "Lire où commence et où finit une cote.",
  img=IMG_CAPTEUR)

q(C, "La flèche de montage",
  "Sur un croquis de solution, à quoi sert une flèche de montage ?",
  ["à dire dans quel sens on met la pièce en place",
   "à montrer de quel côté vient le vent sur la pièce",
   "à relier une légende à la partie qu'elle nomme",
   "à donner la longueur de la pièce, en mm"],
  "La flèche de montage dit comment la pièce se met en place : on l'enfile, on la glisse, on la visse…",
  "« On enfile le crochet sur le bord, vers le bas » : une flèche rouge vers le bas.",
  "Confondre la flèche de montage et le trait d'une légende.",
  ["",
   "Une flèche pour le vent montre une contrainte ; elle ne dit pas comment monter la pièce.",
   "Le trait d'une légende n'a pas de pointe : il relie un mot à une partie.",
   "Une longueur se donne par une cote, avec deux pointes et un nombre."],
  "Flèche de montage = comment on met la pièce en place.")

q(C, "La fonction ajoutée",
  "Le support du capteur ajoute une fonction au jardin. Laquelle ?",
  ["tenir le capteur droit, sans qu'il bouge",
   "mesurer l'humidité de la terre du bac",
   "arroser les plantes à l'heure choisie",
   "envoyer l'état du jardin sur le smartphone de la gardienne"],
  "Le capteur mesurait déjà ; le système arrosait déjà. Ce qui manquait : que le capteur reste en place, pour que ses mesures "
  "soient justes.",
  "Un porte-gobelet ajouté à une poussette : une nouvelle fonction, tenir le gobelet.",
  "Confondre la fonction de la pièce ajoutée et celles qui existaient déjà.",
  ["",
   "Mesurer l'humidité, c'est le rôle du capteur lui-même, qui existait avant le support.",
   "Arroser à l'heure choisie, c'est le service que rendait déjà le système d'arrosage.",
   "Envoyer l'état au smartphone est une fonction du système qui existait déjà."],
  "Le support ajoute : tenir le capteur en place.")

q(C, "Un peu de jeu",
  "La planche du bac fait 22 mm d'épaisseur. Quelle ouverture donner au crochet qui la coiffe ?",
  ["24 mm : un peu plus, pour l'enfiler sans forcer",
   "22 mm pile : exactement l'épaisseur de la planche",
   "20 mm : un peu moins, pour qu'il serre très fort",
   "44 mm : le double, pour pouvoir passer la main"],
  "On laisse un peu de <b>jeu</b> — un petit espace — pour enfiler la pièce sans forcer : 22 mm + 2 mm de jeu.",
  "Un capuchon de stylo a un tout petit jeu : il s'enfile, sans flotter.",
  "Donner exactement la même dimension : la pièce ne passe pas, ou elle casse.",
  ["",
   "À 22 mm pile, le moindre défaut du bois ou de l'impression bloque le crochet.",
   "À 20 mm, le crochet ne passe pas sur une planche de 22 mm, ou il casse en forçant.",
   "À 44 mm, le crochet flotte : il bouge, et le capteur avec lui."],
  "Pour s'emboîter : la dimension, plus un peu de jeu.")

q(C, "Écrire le matériau",
  "Pourquoi écrit-on le matériau sur un croquis coté ?",
  ["parce qu'il décide de la machine et de la solidité",
   "parce que le matériau donne la couleur du croquis",
   "parce que le croquis est plus beau avec des mots",
   "parce que le matériau remplace les cotes manquantes"],
  "On fabrique en PLA (un plastique) à l'imprimante 3D, en bois à la scie, en aluminium à la plieuse… et chaque matériau "
  "résiste plus ou moins à l'eau et au soleil.",
  "« Crochet en PLA, imprimé en 3D » : celui qui fabrique sait quelle machine lancer.",
  "Choisir le matériau après avoir fabriqué.",
  ["",
   "Le croquis peut être tout en noir : le matériau n'a rien à voir avec la couleur du dessin.",
   "Les mots du croquis ne sont pas là pour décorer : chacun donne une information utile.",
   "Le matériau ne donne aucune dimension : une cote qui manque reste à écrire."],
  "Le matériau s'écrit sur le croquis coté.")

# ═══════════════ 3e_C7.2 — Proposer et fabriquer un ensemble de solutions pour produire un nouvel OST (12) ═══════════════
C = "3e_C7.2"

q(C, "Plusieurs croquis",
  "Pourquoi dessiner plusieurs croquis avant de choisir une solution ?",
  ["pour comparer, et garder la meilleure avec des raisons",
   "pour avoir plus de pages à rendre au professeur",
   "parce que le premier croquis est toujours faux",
   "pour pouvoir fabriquer les trois solutions en même temps"],
  "On ne choisit bien qu'entre plusieurs possibilités : on les compare avec le cahier des charges, puis on garde la plus adaptée.",
  "Collier, platine, bras : trois principes pour fixer la sirène, comparés face au vent.",
  "Se lancer dans la première idée sans la comparer.",
  ["",
   "Le nombre de pages n'est pas le but : c'est la comparaison qui permet de choisir.",
   "Le premier croquis peut être le bon ; on ne le sait qu'après l'avoir comparé aux autres.",
   "On ne fabrique que la solution choisie ; les autres restent des croquis."],
  "Plusieurs croquis → comparer → choisir.")

q(C, "Vraiment différentes",
  "Laquelle de ces propositions contient trois solutions vraiment différentes ?",
  ["un collier, une platine au sommet, un bras",
   "un collier, un collier à trois boulons, un collier peint",
   "un bras court, un bras moyen, un bras long",
   "une platine à 4 vis, une à 6 vis, une à 8 vis"],
  "Des solutions sont vraiment différentes quand leur <b>principe</b> change : serrer autour, poser dessus, accrocher à un bras.",
  "Pour le panneau solaire : un collier, une platine, un cadre au sol.",
  "Prendre des variantes pour des solutions.",
  ["",
   "Trois colliers : un seul principe, serrer autour du poteau ; ce sont des variantes.",
   "Trois bras de longueurs différentes : toujours le même principe, accrocher à un bras.",
   "Le nombre de vis change, pas le principe : poser sur une platine."],
  "Principe différent = solution différente.")

q(C, "Le vent et le bras",
  "Pourquoi un long bras, qui éloigne la sirène du poteau, est-il risqué face au vent ?",
  ["plus la sirène est loin, plus elle force sur la fixation",
   "parce qu'un bras long rouille plus vite qu'un collier",
   "parce que le son porte moins loin au bout d'un bras",
   "parce qu'un bras ne peut pas se démonter pour l'entretien"],
  "Le vent pousse sur la sirène ; plus elle est loin du poteau, plus cet effort fait levier sur la fixation — comme une porte "
  "qu'on pousse loin de ses gonds.",
  "On ouvre une porte sans effort en poussant près de la poignée, loin des gonds.",
  "Juger une solution sur un seul critère, sans penser à l'effort du vent.",
  ["",
   "La rouille dépend du matériau (acier galvanisé, inox), pas de la longueur du bras.",
   "Le son d'une sirène ne dépend pas de la longueur du bras qui la tient.",
   "Un bras boulonné se démonte aussi bien qu'un collier."],
  "Loin du poteau → plus d'effort sur la fixation.")

q(C, "La cote qui manque",
  "Sur ce croquis coté, quelle information manque pour fabriquer le boîtier ?",
  ["la profondeur",
   "la longueur",
   "la hauteur",
   "l'unité des cotes"],
  "120 (la longueur) et 80 (la hauteur) sont cotés, « cotes en mm » est écrit ; aucune cote ne donne la profondeur.",
  "Une boîte à chaussures : sans sa profondeur, impossible de découper ses côtés.",
  "Lire les cotes présentes sans se demander lesquelles manquent.",
  ["",
   "La longueur y est : 120, au-dessus du boîtier.",
   "La hauteur y est : 80, sur le côté gauche.",
   "L'unité y est : « cotes en mm », sous le titre."],
  "Un volume : trois dimensions à coter.",
  img=IMG_BOITIER)

q(C, "Est-ce que ça rentre ?",
  "Un boîtier de 120 × 80 × 60 mm doit entrer dans un coffret de 130 × 90 × 70 mm (intérieur). Entre-t-il ?",
  ["oui, avec 10 mm de marge dans chaque direction",
   "non, car 120 + 80 + 60 dépasse 130 + 90",
   "non, car il faut au moins 20 mm de marge",
   "on ne peut pas savoir sans le peser"],
  "On compare chaque dimension à celle qui lui fait face : 120 < 130, 80 < 90, 60 < 70.",
  "Une valise entre dans un coffre si chacune de ses trois dimensions est plus petite.",
  "Additionner des dimensions au lieu de les comparer une à une.",
  ["",
   "On n'additionne pas des dimensions : on compare la longueur à la longueur, la hauteur à la hauteur…",
   "Aucune règle n'impose 20 mm de marge ici ; 10 mm suffisent pour poser le boîtier.",
   "La masse ne dit rien de la place que prend un objet : ce sont ses dimensions qui comptent."],
  "Ça rentre ? On compare dimension par dimension.")

q(C, "Les pointillés",
  "Sur un croquis, que montre un trait en pointillés, comme le trou du câble du boîtier ?",
  ["une partie cachée, que l'on ne voit pas d'ici",
   "une partie à découper avec des ciseaux",
   "une partie fragile, qui peut se casser",
   "une partie que l'on ajoutera plus tard"],
  "En dessin technique, les pointillés montrent ce qui est caché derrière une face : ici, le trou est sous le boîtier.",
  "Sur la vue de face d'une boîte, le trou percé dans le dos se dessine en pointillés.",
  "Prendre les pointillés pour un trait de découpe.",
  ["",
   "Les pointillés de découpe existent sur les patrons en papier ; en dessin technique, ils montrent ce qui est caché.",
   "La fragilité ne se dessine pas en pointillés ; elle s'écrit, si besoin, dans une légende.",
   "Ce qui reste à ajouter n'a pas de trait particulier ; le trou du boîtier existe déjà, dessous."],
  "Pointillés = caché.")

q(C, "La bonne vue",
  "Le trou du câble est sous le boîtier. Que faut-il ajouter au croquis pour le fabriquer ?",
  ["une vue de dessous, avec son diamètre et sa place",
   "une ombre sous le boîtier, pour qu'il ait l'air vrai",
   "une deuxième vue de face, plus grande que la première",
   "une photo du câble que l'on fera passer dedans"],
  "Un détail se cote sur une vue qui le montre : ici, une vue de dessous, avec le diamètre du trou (Ø 12) et sa place (à 40 mm "
  "du bord).",
  "Pour une prise sur le côté d'une boîte, on dessine aussi la vue de côté.",
  "Coter un détail caché sur une vue où on ne le voit pas.",
  ["",
   "Une ombre ne donne ni le diamètre ni la place du trou.",
   "Une autre vue de face montre encore la face avant : le dessous reste caché.",
   "Le câble ne dit pas où percer : il faut le diamètre et la place du trou."],
  "Chaque détail sur une vue qui le montre.")

q(C, "Pour câbler",
  "On veut montrer à un électricien comment brancher la sirène sur la batterie. Quelle représentation ?",
  ["un schéma électrique, avec ses symboles normés",
   "un croquis à main levée de la sirène sur son poteau",
   "une modélisation 3D de la sirène et du poteau",
   "un graphique de la tension au fil des heures"],
  "Brancher, c'est savoir comment c'est relié : le <b>schéma</b> montre les liaisons avec des symboles que tout électricien lit.",
  "Le schéma de la station : une batterie, un interrupteur, une sirène, reliés en boucle.",
  "Choisir le dessin le plus réaliste au lieu du plus utile.",
  ["",
   "Un croquis montre la sirène et sa fixation ; il ne dit pas quel fil va où.",
   "Une modélisation 3D montre la forme exacte ; les branchements n'y apparaissent pas.",
   "Un graphique montre comment une grandeur change ; il ne dit pas comment brancher."],
  "Pour câbler : le schéma.")

q(C, "Vingt secondes",
  "En réunion, tu as vingt secondes pour montrer ton idée de fixation. Quelle représentation ?",
  ["un croquis à main levée",
   "une modélisation 3D",
   "un schéma électrique",
   "un algorithme"],
  "Le croquis se fait en quelques secondes et montre l'essentiel de l'idée.",
  "Un croquis au tableau, pendant une revue de projet.",
  "Croire qu'une idée doit d'abord être modélisée.",
  ["",
   "Une modélisation 3D prend du temps : elle vient après, quand l'idée est choisie.",
   "Un schéma électrique montre des branchements, pas la forme d'une fixation.",
   "Un algorithme dit l'ordre des actions d'un programme, pas la forme d'une pièce."],
  "Vite, une idée : le croquis.")

q(C, "Reconnaître la modélisation",
  "Sur cette figure, quelle vue est une modélisation 3D ?",
  ["la vue 3",
   "la vue 1",
   "la vue 2",
   "aucune des quatre vues"],
  "La vue 3 montre un volume aux arêtes nettes et aux faces ombrées, avec les trois axes x, y, z d'un logiciel.",
  "La même pièce, modélisée, peut être envoyée à l'imprimante 3D.",
  "Prendre un croquis en perspective pour une modélisation.",
  ["",
   "La vue 1 est tracée à main levée, avec des légendes et une flèche : c'est un croquis.",
   "La vue 2 relie des symboles par des traits droits : c'est un schéma électrique.",
   "La vue 3 en est une : un volume exact, avec les trois axes d'un logiciel ; la vue 4, elle, est un graphique."],
  "Un volume exact, dans un logiciel : une modélisation.",
  img=IMG_QUATRE)

q(C, "Modéliser ou simuler",
  "Quelle est la différence entre modéliser et simuler ?",
  ["modéliser, c'est la forme ; simuler, le comportement",
   "modéliser se fait sur papier, et simuler sur ordinateur",
   "ce sont deux mots pour la même chose",
   "simuler, c'est fabriquer le prototype en vrai"],
  "La <b>modélisation</b> représente à quoi ressemble l'objet ; la <b>simulation</b> fait « fonctionner » ce modèle pour prévoir "
  "comment il se comportera.",
  "Modéliser le bras de la sirène, puis simuler l'effort d'une rafale à 250 km/h.",
  "Confondre les deux, parce qu'on les fait dans le même logiciel.",
  ["",
   "La modélisation 3D se fait aussi sur ordinateur ; la différence n'est pas l'outil, c'est ce qu'on cherche.",
   "Ce sont deux étapes différentes : on ne simule qu'un objet déjà modélisé.",
   "Le prototype est un objet réel ; la simulation se passe dans un logiciel, avant de fabriquer."],
  "Modéliser = la forme ; simuler = le comportement.")

q(C, "L'ordre de la démarche",
  "Dans quel ordre passe-t-on, le plus souvent, pour fabriquer une pièce nouvelle ?",
  ["croquis, croquis coté, modélisation 3D, prototype",
   "modélisation 3D, croquis, prototype, croquis coté",
   "prototype, croquis coté, croquis, modélisation 3D",
   "croquis coté, prototype, modélisation 3D, puis croquis"],
  "On cherche l'idée au croquis, on la précise avec des cotes, on la modélise pour une machine, puis on fabrique le prototype.",
  "Le support du capteur : un croquis, un croquis coté (24 mm), une modélisation, une impression 3D.",
  "Commencer par le logiciel, avant d'avoir trouvé l'idée.",
  ["",
   "Modéliser avant d'avoir une idée, c'est perdre du temps : le croquis vient d'abord.",
   "Le prototype vient à la fin : on ne fabrique pas avant d'avoir dessiné.",
   "Le croquis coté précise un croquis ; il ne peut pas venir avant lui."],
  "Croquis → cotes → modélisation → prototype.")

Q = B.fin(30, {"4e_C2.1": 10, "4e_C7.2": 8, "3e_C7.2": 12})
