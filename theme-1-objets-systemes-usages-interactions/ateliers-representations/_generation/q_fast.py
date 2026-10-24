# -*- coding: utf-8 -*-
"""Les 30 questions du QCM de l'atelier « Des fonctions aux solutions techniques » (diagramme FAST).

Toutes les bonnes réponses sont en position 0 ici : la répartition sur A/B/C/D
est faite ensuite par `_outils/fix_r.js`, de façon déterministe.

Répartition : 5e_C4.1 (8) · 5e_C1.2 (5) · 4e_C4.4 (6) · 4e_C7.2 (5) · 3e_C7.2 (6). Quatre questions illustrées.
"""
from qbanque import Banque

B = Banque()
q = B.q

IMG_LAMPADAIRE = {"src": "Images/fast_lampadaire_complet.svg",
                  "alt": "Diagramme FAST du lampadaire intelligent : la fonction d'usage « éclairer la rue la nuit quand un piéton "
                         "passe » se décompose en six fonctions techniques, chacune avec sa solution : détecter la nuit, le capteur "
                         "de luminosité ; détecter un passant, le détecteur de mouvement ; décider quand allumer, la carte "
                         "programmable ; produire la lumière, le bloc de LED ; stocker l'énergie pour la nuit, la batterie ; capter "
                         "l'énergie du soleil, le panneau solaire."}
IMG_VELO = {"src": "Images/fast_velo_cargo_freinage.svg",
            "alt": "Extrait du diagramme FAST du vélo-cargo : la fonction « ralentir la roue » a deux solutions reliées par « ou » : "
                   "frein à patins, frottement sur la jante, ou frein à disque, frottement sur un disque."}
IMG_JARDIN = {"src": "Images/fast_jardin_arrosage.svg",
              "alt": "Diagramme FAST du système d'arrosage : mesurer l'humidité du sol, le capteur d'humidité du sol ; décider quand "
                     "arroser, la carte programmable ; envoyer l'état au smartphone, le module Wi-Fi ; laisser passer l'eau ou la "
                     "bloquer, l'électrovanne ; faire circuler l'eau jusqu'aux bacs, la pompe et les tuyaux ; stocker l'eau de "
                     "pluie, la cuve."}
IMG_STATION = {"src": "Images/fast_station_alerte.svg",
               "alt": "Diagramme FAST de la station d'alerte cyclonique : mesurer la vitesse du vent, l'anémomètre ; décider du "
                      "niveau d'alerte, la carte programmable ; diffuser l'alerte aux habitants, la sirène ou un message sur les "
                      "téléphones ou un panneau lumineux à LED ; stocker l'énergie pour la nuit, la batterie 12 V ; capter "
                      "l'énergie du soleil, le panneau solaire."}

# ═══════════════ 5e_C4.1 — Associer des solutions techniques à des fonctions techniques (8) ═══════════════
C = "5e_C4.1"

q(C, "Reconnaître une fonction",
  "Dans un diagramme FAST, laquelle de ces étiquettes est une fonction technique ?",
  ["stocker l'énergie pour la nuit",
   "la batterie du lampadaire",
   "le panneau solaire du toit",
   "le capteur de luminosité du mât"],
  "Une <b>fonction technique</b> dit ce que l'objet doit faire : elle commence par un <b>verbe à l'infinitif</b>. Les trois autres "
  "étiquettes sont des noms : ce sont des <b>solutions techniques</b>, des éléments qu'on peut toucher.",
  "« Détecter un passant », « capter l'énergie du soleil » : des fonctions. « Le détecteur de mouvement » : une solution.",
  "Prendre « capteur » pour un verbe, parce qu'il ressemble à « capter ».",
  ["",
   "« La batterie » est un nom : c'est l'élément qui réalise « stocker l'énergie », pas la fonction elle-même.",
   "« Le panneau solaire » est un nom : c'est la solution de « capter l'énergie du soleil ».",
   "« Le capteur » ressemble au verbe « capter », mais c'est un composant : une solution, pas une fonction."],
  "Fonction : un verbe. Solution : un nom.")

q(C, "Lire vers la droite",
  "Sur ce FAST du lampadaire, comment le lampadaire détecte-t-il un passant ?",
  ["avec le détecteur de mouvement",
   "avec le capteur de luminosité",
   "avec la carte programmable",
   "avec le bloc de LED qui s'allume"],
  "Vers la droite, le FAST répond à « <b>comment ?</b> ». Sur la ligne « détecter un passant », la case de droite dit : le "
  "détecteur de mouvement.",
  "Comment produire la lumière ? → vers la droite → le bloc de LED.",
  "Lire la case d'une autre ligne, ou lire le schéma dans le mauvais sens.",
  ["",
   "Le capteur de luminosité est sur la ligne « détecter la nuit » : il dit s'il fait jour ou nuit, il ne voit pas les passants.",
   "La carte programmable est sur la ligne « décider quand allumer » : elle décide, elle ne détecte rien elle-même.",
   "Le bloc de LED répond à « comment produire la lumière ? » : il éclaire, il ne détecte pas."],
  "Vers la droite : « comment ? ».",
  img=IMG_LAMPADAIRE)

q(C, "Lire vers la gauche",
  "Pourquoi le lampadaire intelligent a-t-il un panneau solaire ?",
  ["pour capter l'énergie du soleil",
   "pour stocker l'énergie la nuit",
   "pour détecter le lever du jour",
   "pour produire la lumière le soir"],
  "Vers la gauche, le FAST répond à « <b>pourquoi ?</b> » : le panneau solaire → capter l'énergie du soleil → éclairer la rue la nuit "
  "quand un piéton passe.",
  "Pourquoi une batterie ? → vers la gauche → stocker l'énergie pour la nuit.",
  "Confondre le panneau, qui capte, et la batterie, qui stocke.",
  ["",
   "La nuit, le panneau ne reçoit plus de lumière et ne garde rien : c'est la batterie qui stocke l'énergie.",
   "Dans ce lampadaire, c'est le capteur de luminosité qui dit s'il fait jour ou nuit, sur sa propre ligne.",
   "Produire la lumière, c'est la ligne du bloc de LED : le panneau ne s'allume pas le soir."],
  "Vers la gauche : « pourquoi ? ».")

q(C, "Le sens de lecture",
  "Dans un diagramme FAST, quand on va d'une fonction technique vers la droite, on répond à la question…",
  ["« Comment ? »",
   "« Pourquoi ? »",
   "« Combien ? »",
   "« Pour qui ? »"],
  "Vers la droite, on cherche <b>comment</b> la fonction est réalisée : la solution technique. Vers la gauche, on cherche "
  "<b>pourquoi</b> elle existe.",
  "Détecter la nuit → comment ? → le capteur de luminosité.",
  "Inverser les deux sens de lecture.",
  ["",
   "« Pourquoi ? » se lit vers la gauche : de la solution vers la fonction, puis vers la fonction d'usage.",
   "Le FAST ne compte rien : aucune case ne donne une quantité ou un nombre de pièces.",
   "« Pour qui ? » est une question de la bête à cornes (à qui l'objet rend service), pas une lecture du FAST."],
  "Droite : comment. Gauche : pourquoi.")

q(C, "À quoi sert le FAST",
  "Un diagramme FAST sert à…",
  ["relier la fonction d'usage aux solutions",
   "lister ce qui entoure l'objet et agit sur lui",
   "placer les tâches d'un projet dans le temps",
   "dire à qui l'objet rend service, et pourquoi"],
  "Le FAST part de la <b>fonction d'usage</b>, la décompose en <b>fonctions techniques</b> et associe à chacune la <b>solution "
  "technique</b> qui la réalise.",
  "Éclairer la rue → détecter un passant → le détecteur de mouvement.",
  "Confondre les schémas de l'analyse fonctionnelle entre eux.",
  ["",
   "Lister ce qui entoure l'objet, c'est le diagramme des interacteurs extérieurs (le diagramme pieuvre).",
   "Placer des tâches dans le temps, c'est le diagramme de Gantt : il organise un projet, pas un objet.",
   "Dire à qui l'objet rend service, sur quoi il agit et dans quel but, c'est la bête à cornes."],
  "FAST : fonction d'usage → fonctions techniques → solutions.")

q(C, "Le nom du schéma",
  "D'où vient le nom « diagramme FAST » ?",
  ["des initiales de quatre mots anglais",
   "du mot anglais « fast », qui veut dire rapide",
   "du nom de l'ingénieur qui l'a inventé",
   "d'une marque de logiciel de dessin"],
  "FAST est un sigle anglais : <i lang=\"en\">Function Analysis System Technique</i>, c'est-à-dire « technique d'analyse "
  "fonctionnelle ».",
  "Le programme, lui, ne dit pas « FAST » : il parle de fonctions techniques et de solutions techniques.",
  "Lire « fast » comme le mot anglais « rapide ».",
  ["",
   "Le mot anglais « fast » veut bien dire « rapide », mais ici chaque lettre est l'initiale d'un mot : c'est un sigle.",
   "Aucun nom de personne : les quatre lettres sont les initiales de Function, Analysis, System, Technique.",
   "Le FAST se dessine sur papier comme sur n'importe quel logiciel : ce n'est pas une marque."],
  "FAST = Function Analysis System Technique.")

q(C, "La case de la batterie",
  "Dans le FAST du lampadaire, quelle solution met-on en face de « stocker l'énergie pour la nuit » ?",
  ["la batterie",
   "le panneau solaire",
   "le bloc de LED",
   "la carte programmable"],
  "La batterie se charge le jour et rend l'énergie la nuit : c'est elle qui <b>stocke</b>.",
  "Dans une lampe de poche, ce sont les piles qui stockent l'énergie.",
  "Mettre le panneau solaire, qui capte mais ne garde rien.",
  ["",
   "Le panneau solaire capte l'énergie du soleil, le jour ; la nuit, il ne donne plus rien et ne garde rien.",
   "Le bloc de LED consomme l'énergie pour produire la lumière : il ne la stocke pas.",
   "La carte programmable décide quand allumer : elle ne garde aucune réserve d'énergie."],
  "Stocker l'énergie : la batterie.")

q(C, "Une solution, deux fonctions",
  "Dans certaines lampes de jardin, le panneau solaire capte l'énergie et sert aussi à détecter la nuit. Que montre leur FAST ?",
  ["la même solution en face de deux fonctions",
   "une erreur : une solution n'a qu'une fonction",
   "deux panneaux solaires, un pour chaque fonction",
   "une seule fonction, écrite deux fois de suite"],
  "Une même solution peut réaliser <b>deux</b> fonctions : le panneau capte l'énergie, et quand il ne donne plus rien, la carte "
  "sait que c'est la nuit.",
  "Le module Wi-Fi du jardin envoie l'état de l'arrosage et peut aussi envoyer une alerte : une solution, deux fonctions.",
  "Croire qu'à chaque fonction correspond une pièce différente.",
  ["",
   "Ce n'est pas une erreur : une solution peut servir deux fonctions, et cela fait une pièce de moins à fabriquer.",
   "Un seul panneau suffit dans ces lampes : il fait les deux choses, on n'en ajoute pas un second.",
   "« Capter l'énergie » et « détecter la nuit » sont deux actions différentes : deux fonctions, pas une seule répétée."],
  "Une solution peut servir plusieurs fonctions.")

# ═══════════════ 5e_C1.2 — Comparer des principes techniques pour une même fonction technique (5) ═══════════════
C = "5e_C1.2"

q(C, "Le mot « ou »",
  "Sur cet extrait du FAST du vélo-cargo, que veut dire le mot « ou » sur la ligne « ralentir la roue » ?",
  ["deux principes possibles : on en choisira un",
   "il faut monter les deux freins à la fois",
   "le frein à disque remplace la chaîne",
   "la fonction a été écrite deux fois par erreur"],
  "Deux cases reliées par « ou » sont une <b>alternative</b> : deux principes techniques pour la même fonction. On les compare, "
  "puis on choisit.",
  "Pour la station d'alerte, « diffuser l'alerte » a trois solutions reliées par « ou ».",
  "Lire « ou » comme « et ».",
  ["",
   "« Ou » propose un choix : Léa n'a besoin que d'un seul système de freinage par roue.",
   "La chaîne est sur une autre ligne, « transmettre l'effort de Léa à la roue » : le frein ne la remplace pas.",
   "La fonction « ralentir la roue » n'est écrite qu'une fois ; ce sont ses solutions qui sont deux."],
  "« Ou » : une alternative, à trancher.",
  img=IMG_VELO)

q(C, "Ce qu'est un principe",
  "Un principe technique, c'est…",
  ["la façon physique de réaliser une fonction",
   "le prix de la solution qu'on achète",
   "le nom de la pièce choisie au magasin",
   "ce à quoi sert l'objet, pour celui qui l'utilise"],
  "Le <b>principe</b> dit par quel phénomène, et à quel endroit, la fonction est réalisée : frotter des patins sur la jante, "
  "frotter des plaquettes sur un disque.",
  "Sécher le linge : l'air chaud d'une machine, ou le soleil et le vent sur un étendoir — deux principes.",
  "Confondre le principe et la solution qu'on achète.",
  ["",
   "Le prix est un critère de choix entre principes, pas le principe lui-même.",
   "Le nom de la pièce achetée, c'est la solution ; le principe dit comment elle agit.",
   "Ce à quoi sert l'objet, c'est sa fonction d'usage, tout à gauche du FAST."],
  "Principe : quel phénomène, à quel endroit.")

q(C, "Le même phénomène",
  "Le frein à patins et le frein à disque ralentissent tous les deux la roue par…",
  ["frottement",
   "aimantation",
   "aspiration de l'air",
   "électricité"],
  "Les deux freins serrent une pièce qui tourne avec la roue : la <b>jante</b> pour l'un, un <b>disque</b> pour l'autre. Même "
  "phénomène, le frottement, mais pas au même endroit.",
  "Frotter ses mains l'une contre l'autre les chauffe : le frottement freine et chauffe.",
  "Croire que deux principes différents utilisent forcément deux phénomènes différents.",
  ["",
   "Aucun aimant dans ces deux freins : ce sont des patins ou des plaquettes qui serrent.",
   "Ni le patin ni le disque n'aspirent l'air : ils serrent une pièce qui tourne.",
   "Ces deux freins de vélo sont mécaniques : ils ne consomment pas d'électricité pour freiner."],
  "Même phénomène, endroits différents.")

q(C, "Pour Léa, sous la pluie",
  "Léa descend des côtes sous la pluie avec ses deux enfants dans le bac. Quel frein lui conseiller ?",
  ["le frein à disque : il freine bien mouillé",
   "le frein à patins : il est moins cher",
   "le frein à patins : il use bien la jante",
   "aucun : en descente, il suffit de ne pas pédaler"],
  "Sous la pluie, le pneu projette l'eau sur la jante et les patins glissent ; le disque, au centre de la roue, est plus à "
  "l'abri. Pour Léa, le freinage sous la pluie compte plus que le prix.",
  "Pour un vélo qui ne roule que par beau temps, sur du plat, le frein à patins peut suffire.",
  "Choisir d'après le prix sans regarder la situation.",
  ["",
   "Moins cher, c'est vrai, mais Léa descend des côtes sous la pluie : le freinage mouillé passe avant le prix.",
   "User la jante est un inconvénient du frein à patins, pas une raison de le choisir.",
   "Pour ralentir, il faut justement un frein : un vélo-cargo chargé prend de la vitesse tout seul en descente."],
  "On choisit selon la situation.")

q(C, "Le meilleur, pour qui ?",
  "Pourquoi ne peut-on pas dire « le frein à disque est meilleur », sans rien ajouter ?",
  ["parce que le bon choix dépend de la situation",
   "parce que le frein à disque freine moins bien",
   "parce que les deux freins sont toujours égaux",
   "parce que le frein à disque est interdit en ville"],
  "Chaque principe a des avantages et des inconvénients. Le disque freine mieux sous la pluie, le patin coûte moins cher et se "
  "règle facilement : le choix dépend de l'usage, de la météo, du budget.",
  "Pour un petit vélo d'enfant, léger et lent, le frein à patins est souvent un bon choix.",
  "Chercher un « meilleur » dans l'absolu.",
  ["",
   "Le frein à disque freine mieux sous la pluie : ce n'est pas lui qui freine moins bien.",
   "Ils utilisent le même phénomène, mais pas au même endroit : ils ne se valent pas sous la pluie.",
   "Les freins à disque sont autorisés sur les vélos : ce n'est pas une question de règle."],
  "Meilleur, oui, mais dans quelle situation ?")

# ═══════════════ 4e_C4.4 — Constituants de la chaîne d'information et leur fonction (6) ═══════════════
C = "4e_C4.4"

q(C, "Acquérir",
  "Dans le système d'arrosage, quel constituant acquiert l'information « la terre est sèche » ?",
  ["le capteur d'humidité du sol",
   "la carte programmable",
   "le module Wi-Fi",
   "le smartphone de la gardienne"],
  "<b>Acquérir</b>, c'est prendre une information sur le monde : c'est le rôle d'un <b>capteur</b>. Le capteur d'humidité, planté "
  "dans la terre, mesure l'eau qu'elle contient.",
  "Dans le lampadaire, le détecteur de mouvement acquiert l'information « quelqu'un passe ».",
  "Donner ce rôle à la carte, parce que c'est elle qui « sait » qu'il faut arroser.",
  ["",
   "La carte reçoit la mesure et la compare au seuil : elle traite l'information, elle ne la prend pas dans la terre.",
   "Le module Wi-Fi envoie l'état du jardin au smartphone : il communique, il ne mesure rien.",
   "Le smartphone reçoit l'état du jardin, loin des bacs : il ne mesure pas l'eau de la terre."],
  "Acquérir : le capteur.")

q(C, "Traiter",
  "Sur ce FAST du jardin, quel constituant réalise « décider quand arroser » ?",
  ["la carte programmable",
   "le capteur d'humidité du sol",
   "l'électrovanne",
   "le smartphone de la gardienne"],
  "Décider, c'est <b>traiter</b> l'information : la carte programmable compare la mesure d'humidité au seuil et suit son programme.",
  "Dans le lampadaire, la carte programmable décide quand allumer.",
  "Croire que le capteur décide, parce qu'il « sent » la sécheresse.",
  ["",
   "Le capteur mesure l'humidité, il ne compare rien : il donne une valeur, la carte décide.",
   "L'électrovanne s'ouvre sur ordre de la carte : elle exécute, elle ne décide pas.",
   "Le smartphone reçoit l'état du jardin ; il n'est pas une solution du FAST et ne décide pas de l'arrosage."],
  "Traiter : la carte programmable.",
  img=IMG_JARDIN)

q(C, "Communiquer",
  "Le module Wi-Fi envoie l'état du jardin au smartphone. Dans la chaîne d'information, il…",
  ["communique",
   "acquiert",
   "traite",
   "distribue l'énergie"],
  "<b>Communiquer</b>, c'est envoyer l'information à une personne ou à un autre appareil : c'est le rôle du module Wi-Fi.",
  "Un afficheur à l'entrée d'un parking communique le nombre de places libres.",
  "Confondre « envoyer » et « prendre » une information.",
  ["",
   "Acquérir, c'est prendre une mesure sur le monde : le capteur d'humidité le fait, pas le module Wi-Fi.",
   "Traiter, c'est comparer et décider : la carte programmable le fait.",
   "Distribuer l'énergie est une fonction de la chaîne d'énergie : le module, lui, envoie une information."],
  "Communiquer : envoyer l'information.")

q(C, "Hors de la chaîne d'information",
  "Lequel de ces constituants du jardin n'appartient pas à la chaîne d'information ?",
  ["l'électrovanne",
   "le capteur d'humidité",
   "la carte programmable",
   "le module Wi-Fi"],
  "L'électrovanne reçoit l'ordre de la carte, mais elle ne traite aucune information : elle <b>agit</b> sur l'eau. Elle "
  "appartient à la chaîne d'énergie.",
  "Dans le lampadaire, le bloc de LED reçoit l'ordre d'allumer : il est dans la chaîne d'énergie.",
  "Mettre dans la chaîne d'information tout ce qui reçoit un ordre.",
  ["",
   "Le capteur d'humidité prend une information sur la terre : il acquiert, il est dans la chaîne d'information.",
   "La carte compare et décide : elle traite, au cœur de la chaîne d'information.",
   "Le module Wi-Fi envoie l'état au smartphone : il communique, il est dans la chaîne d'information."],
  "Ce qui agit sur le monde : chaîne d'énergie.")

q(C, "Pourquoi une électrovanne",
  "Lis le FAST vers la gauche : pourquoi le système d'arrosage a-t-il une électrovanne ?",
  ["pour laisser passer l'eau ou la bloquer",
   "pour mesurer l'humidité de la terre",
   "pour envoyer l'état au smartphone",
   "pour décider à quelle heure arroser les bacs"],
  "Vers la gauche, l'électrovanne mène à « laisser passer l'eau ou la bloquer », puis à la fonction d'usage : arroser les plantes "
  "quand la terre est sèche.",
  "Pourquoi une cuve ? → vers la gauche → stocker l'eau de pluie.",
  "Attribuer à un constituant la fonction de son voisin.",
  ["",
   "Mesurer l'humidité, c'est la ligne du capteur d'humidité du sol.",
   "Envoyer l'état au smartphone, c'est la ligne du module Wi-Fi.",
   "Décider, c'est la ligne de la carte programmable : l'électrovanne ne fait qu'obéir."],
  "Vers la gauche : la fonction du constituant.")

q(C, "Deux constituants, une fonction",
  "La pompe et les tuyaux sont tous les deux en face de « faire circuler l'eau jusqu'aux bacs ». Est-ce possible ?",
  ["oui : une fonction peut demander deux constituants",
   "non : chaque fonction n'a qu'un seul constituant",
   "non : les tuyaux ne sont pas des constituants",
   "oui, mais seulement s'ils sont faits de la même matière"],
  "Une fonction technique peut demander <b>plusieurs</b> constituants qui travaillent ensemble : la pompe pousse l'eau, les tuyaux "
  "la conduisent jusqu'aux bacs.",
  "Pour « ralentir la roue », un frein à patins demande un levier, un câble et deux patins.",
  "Croire qu'il faut un trait par ligne, une pièce par fonction.",
  ["",
   "Dans ce jardin, l'eau ne circule qu'avec la pompe ET les tuyaux : il en faut deux pour une même fonction.",
   "Les tuyaux sont des éléments du système d'arrosage : ce sont bien des constituants.",
   "La matière ne décide rien : la pompe et les tuyaux sont de matières différentes, et ils servent la même fonction."],
  "Une fonction peut demander plusieurs constituants.")

# ═══════════════ 4e_C7.2 — Ajouter une nouvelle fonction à un OST (5) ═══════════════
C = "4e_C7.2"

q(C, "La fonction qui manque",
  "Pour « prévenir la gardienne quand la cuve est presque vide », quelle fonction technique manque d'abord au FAST du jardin ?",
  ["mesurer le niveau d'eau de la cuve",
   "un capteur de niveau dans la cuve",
   "arroser les plantes plus souvent",
   "le module Wi-Fi déjà présent au jardin"],
  "Pour prévenir, le système doit d'abord <b>savoir</b> combien d'eau reste : aucune branche ne le mesure. La fonction s'écrit "
  "avec un verbe : « mesurer le niveau d'eau de la cuve ».",
  "Pour prévenir quand la batterie du lampadaire est faible, il faut d'abord « mesurer la charge de la batterie ».",
  "Écrire le nom d'un objet dans une case de fonction.",
  ["",
   "« Un capteur de niveau » est un objet : c'est la solution, qui ira dans la case de droite.",
   "Arroser plus souvent viderait la cuve plus vite, sans prévenir personne.",
   "Le module Wi-Fi est déjà dans le FAST, et c'est un objet : il enverra l'alerte, mais il ne mesure rien."],
  "D'abord la fonction qui manque, avec un verbe.")

q(C, "Réutiliser",
  "Quelle solution, déjà dans le FAST du jardin, enverra l'alerte « cuve presque vide » au smartphone ?",
  ["le module Wi-Fi",
   "la carte programmable",
   "le capteur d'humidité",
   "l'électrovanne"],
  "Le module Wi-Fi envoie déjà l'état du jardin au smartphone : on le <b>réutilise</b> pour un message de plus. Une même solution "
  "peut servir deux fonctions.",
  "Le panneau solaire de certaines lampes de jardin capte l'énergie et détecte aussi la nuit.",
  "Ajouter une pièce alors qu'une solution présente sait déjà le faire.",
  ["",
   "La carte décide qu'il faut prévenir, mais elle n'a pas de liaison sans fil : c'est le module Wi-Fi qui envoie.",
   "Le capteur d'humidité mesure la terre : il n'envoie aucun message.",
   "L'électrovanne agit sur l'eau : elle ne prévient personne."],
  "Réutiliser ce qui existe déjà.")

q(C, "Ce qui change dans la carte",
  "Après l'ajout du capteur de niveau d'eau, que faut-il modifier dans la carte programmable ?",
  ["son programme : comparer le niveau à un seuil",
   "son alimentation : la brancher sur le 230 V",
   "rien : le capteur de niveau prévient tout seul",
   "sa place : la poser au fond de la cuve"],
  "La carte traite la nouvelle mesure : son <b>programme</b> reçoit une condition, « si le niveau est sous le seuil, alors envoyer "
  "un message à la gardienne ».",
  "Ajouter un capteur de pluie demanderait aussi une condition de plus : « s'il pleut, ne pas arroser ».",
  "Oublier qu'une nouvelle fonction change souvent le programme.",
  ["",
   "Le système reste en très basse tension : le 230 V au jardin, sous la pluie, serait un danger mortel.",
   "Un capteur acquiert une mesure, il ne décide pas et n'envoie rien : il faut la carte et le module Wi-Fi.",
   "La carte reste au sec dans son boîtier : c'est le capteur de niveau qui va dans la cuve."],
  "Nouvelle fonction → nouveau programme.")

q(C, "Une case de fonction bien écrite",
  "Laquelle de ces propositions est bien écrite pour une case de fonction du FAST ?",
  ["surveiller le niveau de la cuve",
   "le flotteur qui monte et descend dans la cuve",
   "niveau de la cuve trop bas",
   "la cuve est presque vide"],
  "Une case de fonction commence par un <b>verbe à l'infinitif</b>, suivi de ce sur quoi il porte : « surveiller le niveau de la "
  "cuve ».",
  "« Détecter un passant », « décider quand arroser » : verbe + complément.",
  "Écrire un objet, un état ou une phrase qui raconte.",
  ["",
   "« Le flotteur » est un objet : c'est une solution, pour la case de droite.",
   "« Niveau trop bas » décrit un état, sans verbe : on ne sait pas ce que le système doit faire.",
   "« La cuve est presque vide » raconte une situation : ce n'est pas une action du système."],
  "Une fonction : verbe à l'infinitif + complément.")

q(C, "Ajouter une branche",
  "Dans un diagramme FAST, ajouter une nouvelle fonction à un objet, c'est surtout…",
  ["ajouter une branche : fonction et solution",
   "changer la fonction d'usage de l'objet",
   "effacer une branche pour faire de la place",
   "redessiner l'objet entier, sans le FAST"],
  "On ajoute une <b>branche</b> : la fonction technique qui manque et sa solution. Le reste du FAST est gardé, et parfois réutilisé.",
  "Jardin : nouvelle branche « mesurer le niveau d'eau de la cuve » → le capteur de niveau d'eau.",
  "Croire qu'il faut tout recommencer.",
  ["",
   "La fonction d'usage reste « arroser les plantes quand la terre est sèche » : on lui ajoute une fonction, on ne la change pas.",
   "Rien n'est effacé : les branches existantes restent nécessaires, et l'une d'elles (le module Wi-Fi) est réutilisée.",
   "Le FAST sert justement à voir où ajouter : on garde ce qui marche, on ajoute ce qui manque."],
  "Nouvelle fonction : nouvelle branche.")

# ═══════════════ 3e_C7.2 — Proposer un ensemble de solutions pour un nouvel OST (6) ═══════════════
C = "3e_C7.2"

q(C, "Un nom dans une case de fonction",
  "Dans le FAST d'une équipe, une case de fonction contient « le programme d'alerte ». Pourquoi est-ce une erreur ?",
  ["c'est un nom : il faut un verbe d'action",
   "un programme n'a pas sa place dans un FAST",
   "il manque le prix du programme dans la case",
   "la case devrait être tout à gauche du schéma"],
  "Une case de fonction dit ce que l'objet doit <b>faire</b> : elle commence par un verbe à l'infinitif. Ici : « décider du niveau "
  "d'alerte », réalisé par la carte programmable.",
  "« Le capteur d'obstacle » dans une case de fonction → « détecter les obstacles ».",
  "Accepter un nom dans une case de fonction parce qu'il « parle » de la bonne chose.",
  ["",
   "Le programme peut apparaître dans une solution (« la carte programmable et son programme ») : c'est sa place qui est fausse.",
   "Le FAST ne porte aucun prix : ce n'est pas ce qui manque.",
   "Tout à gauche, il n'y a que la fonction d'usage : « prévenir les habitants quand un cyclone approche »."],
  "Case de fonction : un verbe.")

q(C, "Quand le réseau tombe",
  "Pendant un cyclone, le réseau téléphonique tombe. Sur ce FAST, quelle solution d'alerte ne marche plus ?",
  ["le message sur les téléphones",
   "la sirène de la station",
   "le panneau lumineux à LED",
   "aucune des trois solutions"],
  "Le message passe par les antennes du réseau téléphonique. La sirène et le panneau sont reliés à la station, qui a sa batterie et "
  "son panneau solaire.",
  "Une radio à piles marche sans réseau téléphonique : elle reçoit les ondes d'un émetteur.",
  "Oublier de quoi chaque solution a besoin pour atteindre les habitants.",
  ["",
   "La sirène est branchée sur la station, alimentée par sa batterie : elle n'a pas besoin du réseau.",
   "Le panneau lumineux est relié à la station : il s'allume sans antenne de téléphone.",
   "Le message, lui, dépend des antennes : sans réseau, il n'arrive pas."],
  "Une solution dépend de ce qu'elle utilise.",
  img=IMG_STATION)

q(C, "Un critère qui élimine",
  "Le critère « alimentée en très basse tension » est rempli par les trois solutions d'alerte. Ce critère…",
  ["écarte toute solution qui ne le remplit pas",
   "peut être effacé : il ne départage rien",
   "désigne la solution la plus économe",
   "ne concerne que la sirène de la station"],
  "C'est une <b>exigence impérative</b> (flexibilité F0) : elle ne départage pas, elle <b>élimine</b>. Une solution sur le 230 V, "
  "sous la pluie d'un cyclone, serait écartée d'office.",
  "« Résister à des vents de cyclone » élimine aussi tout panneau qui s'envolerait.",
  "Effacer un critère parce que toutes les solutions le remplissent.",
  ["",
   "Effacé, le critère ne protégerait plus contre une solution dangereuse proposée plus tard.",
   "Il dit oui ou non, il ne classe pas les consommations : il ne désigne aucune solution.",
   "La sirène, le module de messages et le panneau sont tous concernés : tous doivent rester en très basse tension."],
  "Un critère impératif élimine.")

q(C, "Combiner deux solutions",
  "Pourquoi une équipe peut-elle choisir de combiner la sirène et le panneau lumineux ?",
  ["chacune couvre le point faible de l'autre",
   "deux appareils coûtent moins cher qu'un seul",
   "la sirène ne marche pas sans le panneau",
   "il est interdit de n'avoir qu'une alerte"],
  "La sirène réveille la nuit mais n'atteint pas une personne sourde ; le panneau l'atteint mais ne réveille personne. Ensemble, "
  "elles couvrent les deux cas, et marchent sans réseau.",
  "Un vélo a un phare (voir) et un catadioptre (être vu même phare éteint) : deux solutions qui se complètent.",
  "Croire qu'on doit toujours garder une seule solution par fonction.",
  ["",
   "Deux appareils coûtent plus cher qu'un : on les combine malgré le coût, pour couvrir plus de cas.",
   "La sirène fonctionne seule, branchée sur la station : elle n'a pas besoin du panneau.",
   "Aucune règle n'impose deux alertes : c'est le tableau des critères qui conduit à les combiner."],
  "Combiner : couvrir les points faibles.")

q(C, "Ce que le FAST fait vraiment",
  "Laquelle de ces phrases sur le diagramme FAST est vraie ?",
  ["il associe des solutions à des fonctions",
   "il dessine la forme de chaque solution",
   "il fait partie du cahier des charges",
   "il liste toutes les pièces de l'objet"],
  "Le FAST décompose la fonction d'usage en fonctions techniques et <b>associe</b> à chacune une ou plusieurs solutions. Il les "
  "nomme, sans les dessiner.",
  "Station : « mesurer la vitesse du vent » → l'anémomètre.",
  "Confondre le FAST avec le croquis, avec le cahier des charges ou avec la nomenclature.",
  ["",
   "Le FAST nomme les solutions dans des cases : leur forme se dessine ensuite, dans un croquis ou un schéma.",
   "Le cahier des charges dit ce qu'on attend de l'objet ; le FAST, qui vient après, dit comment on y répond.",
   "Le FAST ne garde que les éléments qui réalisent les fonctions étudiées : pas les vis, ni chaque câble."],
  "Le FAST associe ; il ne dessine pas, ne liste pas tout.")

q(C, "Un argumentaire complet",
  "Lequel de ces textes est un argumentaire complet pour choisir une alerte ?",
  ["« La sirène, car elle réveille ; mais elle consomme. »",
   "« La sirène, parce que c'est la meilleure alerte. »",
   "« La sirène réveille. Le panneau, lui, s'allume. »",
   "« J'aime la sirène : elle fait beaucoup de bruit. »"],
  "Un argumentaire complet dit le <b>choix</b>, le <b>critère</b> qui le justifie (réveiller la nuit) et la <b>limite</b> qui reste "
  "(la consommation).",
  "« Le message, car il atteint les personnes sourdes ; mais il dépend du réseau. »",
  "Donner un avis sans critère, ou cacher la limite de son choix.",
  ["",
   "« La meilleure » n'est pas un critère : on ne sait ni pourquoi, ni dans quelle situation.",
   "Ce texte décrit deux solutions, mais ne choisit rien et ne justifie rien.",
   "« J'aime » est un goût personnel : il ne s'appuie sur aucun critère du tableau."],
  "Argumenter : choix + critère + limite.")

Q = B.fin(30, {"5e_C4.1": 8, "5e_C1.2": 5, "4e_C4.4": 6, "4e_C7.2": 5, "3e_C7.2": 6})
