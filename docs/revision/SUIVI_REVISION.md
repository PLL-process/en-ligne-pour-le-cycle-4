# Suivi de la révision des trois thèmes

Décision de Pascal du 08/11/2026 : « une révision des 3 thèmes s'impose » ; « depuis longtemps cela me paraissait une
charge cognitive » ; « 1. Oui [la passe complète par séquence] 2. Ordre : c'est urgent, donc tu as carte blanche pour tous
les thèmes de toutes les séquences ». Méthode : skill `revision-sequence`. Une ligne par séquence, dans l'ordre de passage
(les classeurs de progression : ce qui passe en classe le plus tôt d'abord, les trois niveaux entrelacés).

**Les colonnes.**
- **Séance la plus lourde** : les mots que l'élève voit à l'ouverture de sa séance la plus chargée, sans rien déplier, à
  390 px (`node _outils/mesurer_charge.mjs`). Repère : 1 200 mots, soit 10 minutes de lecture seule.
- **✘ règles** : `verif_regles_audit.py` sur la page. **Menus** : questions encore posées par une liste déroulante (n°300).
- **Aération** : écarts de `audit_aeration.py` (légendes et corrections d'un seul tenant).
- Avant → après quand la passe est faite. La dernière colonne est lue par `_outils/bilan_revision.py`.

**État de départ, 08/11/2026** (56 séquences, 188 séances) : médiane 1 134 mots visibles par séance ; **86 séances au-delà
de 1 200** ; le mode essentiel retire 2 % du texte ; 87 ✘ de règles, 995 questions en listes déroulantes et 897 écarts d’aération sur les pages de séquence (914 comptés d'abord : l'audit lisait aussi la description des schémas SVG, corrigé le jour même) ; **1 séquence propre** (5e_C3.1).

**Changement commun, 15/11/2026** (décision de Pascal, #696) : la fiche de chaque activité se replie, sur toutes les
séquences (`_outils/replier_fiches_activite.py`, 241 fiches dans 53 pages) : −7 868 mots visibles ; séances au-delà de
1 200 mots, 69 → 63 ; aucune n'augmente. Les chiffres des lignes ci-dessous sont ceux de leur passe ; ils baissent
d'autant.

| N° | Séquence | Séance la plus lourde (mots) | ✘ règles | Menus | Aération | État |
|---|---|---|---|---|---|---|
| 1 | `5e_C1.5` | 1549 → 1206 | 4 → 0 | 27 → 0 | 18 → 0 | livrée #619 |
| 2 | `5e_C1.3` | 1050 → 1043 → 1199 | 0 | 0 | 5 → 0 | livrée #620 ; #681 : 24 questions fermées vérifiées par la page (thème 1) |
| 3 | `4e_C1.1` | 3570 → 1836 | 0 | 0 | 22 → 0 | livrée #620 ; séance 5 coupée en deux (décision de Pascal) #624 |
| 4 | `4e_C1.4` | 1291 → 1056 → 1350 | 0 | 0 | 9 → 0 | livrée #624 ; #625 replie les leçons des situations ; #627 répare le jeu des licences (6.c) ; #684 : les cinq quiz réécrits (35 questions à quatre propositions, vérifiées quiz par quiz) ; #686 : une séance 4 (la section 6 et la clôture) — séance 3, 1 350 → 439 |
| 5 | `3e_C1.5` | 2017 → 1448 | 0 | 0 | 19 → 0 | livrée #624 ; #628 ramène la séance 4 à 1 448 — au-dessus du repère, justifiée ; #685 : 13 questions fermées vérifiées par la page (séance 2 : 1 234, justifiée) |
| 6 | `3e_C2.1` | 1861 → 1424 | 0 | 0 | 6 → 0 | livrée #624 — séances 2 et 3 au-dessus du repère, justifiées |
| 7 | `5e_C1.1` | 1629 → 1301 | 0 | 0 | 26 → 0 | livrée #630 — séances 1 et 5 au-dessus du repère, justifiées |
| 8 | `5e_C1.2` | 2117 → 1967 | 0 | 0 | 26 → 0 | livrée #630 — séance 4 au-dessus du repère, justifiée |
| 9 | `5e_C3.1` | 2912 → 1994 | 0 | 0 | 0 | livrée #630 — séances 1 et 4 au-dessus du repère, justifiées |
| 10 | `4e_C2.1` | 2625 → 1548 | 1 → 0 | 0 | 24 → 0 | livrée #630 ; quatrième séance (décision de Pascal) #643 — séances 1 et 3 au-dessus du repère, justifiées |
| 11 | `4e_C3.1` | 1850 → 1299 | 0 | 0 | 10 → 0 | livrée #630 — séance 1 au-dessus du repère, justifiée |
| 12 | `3e_C4.1` | 1444 → 1032 | 1 → 0 | 33 → 0 | 6 → 0 | livrée #632 |
| 13 | `3e_C4.3` | 1928 → 817 | 2 → 0 | 33 → 0 | 8 → 0 | livrée #633 ; #646 coupe la séance 4 en deux (décision de Pascal du 11/11) : cinq séances, 817 · 460 · 437 · 737 · 551 |
| 14 | `5e_C2.1` | 2272 → 2166 | 0 | 0 | 20 → 0 | #687 — séances 1 (2 166) et 2 (2 004) au-dessus du repère : un exercice d'atelier chacune (bête à cornes, pieuvre), gardé par décision de Pascal (15/11/2026) |
| 15 | `4e_C4.1` | 2394 → 782 | 1 → 0 | 39 → 0 (22 menus du cahier des charges, voulus) | 11 → 0 | livrée #639 |
| 16 | `4e_C4.1_book-train` | 2752 → 1510 | 0 | 0 | 14 → 0 | livrée #642 — séances 2 (1 307) et 3 (1 510) au-dessus du repère : exercices à six positions, deux chaînes à étiqueter, fichiers draw.io à télécharger ; le reste est replié |
| 17 | `3e_C4.7` | 1169 → 1075 | 1 → 0 | 28 → 0 (1 menu d'interface, simulateur) | 8 → 0 | livrée #644 |
| 18 | `3e_C4.8` | 2076 → 1504 | 1 → 0 | 30 → 0 | 9 → 0 | livrée #645 — séances 1 (1 504) et 3 (1 485) au-dessus du repère : ce qui reste visible, ce sont les questions (deux activités de 20 min + billet ; deux activités de 25 min + clôture) |
| 19 | `3e_C5.1` | 1238 → 1132 | 1 → 0 | 30 → 0 | 5 → 0 | livrée #647 |
| 20 | `3e_C6.1` | 1135 → 1009 | 1 → 0 | 23 → 0 | 9 → 0 | livrée #648 |
| 21 | `3e_C6.2` | 1285 → 1185 | 1 → 0 | 32 → 0 | 5 → 0 | livrée #649 |
| 22 | `5e_C4.1` | 2663 → 2113 | 1 → 0 | 64 → 0 | 17 → 3 | livrée #650 — séance 6 au-delà du repère (positionnement sur 8 compétences : 512 mots ; FAST incrusté : 680) ; pistes : une séance 7 « synthèse et bilan », ou un positionnement en grille. Aération : 3 lectures fléchées du FAST, à la source de l'atelier (thème 1) ; leurres et pourquoi des erreurs (mode mission) : séance 1 à 1 218 mots (1 196 avant : deux réponses leurres dans la grille, +22 mots), la règle de décision de la séance 3 réparée |
| 23 | `5e_C6.1` | 1023 → 912 | 1 → 0 | 30 → 0 | 5 → 0 | livrée #651 |
| 24 | `4e_C5.1` | 1316 → 1179 | 1 → 0 | 30 → 0 | 4 → 0 | livrée #652 |
| 25 | `4e_C6.1` | 1460 → 1216 | 1 → 0 | 28 → 0 | 6 → 0 | livrée #656 — séance 2 à 1 216 mots (1 200 en mode essentiel) : sa clôture (concept invariant, retour sur l'hypothèse, bilan, auto-positionnement) pèse 290 mots et ne se replie pas |
| 26 | `4e_C6.2` | 1990 → 1329 | 6 → 0 | 25 → 0 (4 menus du tableau de vérification du cahier des charges, voulus) | 18 → 0 | livrée #660 — séance 1 à 1 329 mots : l'échauffement de l'éditeur Python (quatre gestes à faire, règles n°93 et n°297) reste déplié, 370 mots ; ses « ce que tu dois voir » se déplient. Séances 2 et 3 : 732 · 997. Mode mission : posé le 11/11, une fois l'ancien gabarit appris au moteur (48 écrans, 13 vérifiés par le mode) |
| 27 | `3e_C9.1` | 1597 → 1116 | 1 → 0 | 33 → 0 | 11 → 0 | livrée #672 — révisée en priorité le 12/11 (Pascal la fait en classe ce jour). Billet d'entrée réparé : une mauvaise réponse était comptée juste. Seconde passe #673 : le pourquoi de chaque erreur (79 phrases, 27 questions), 15 questions à réponses courtes en rangée, quatre passages réécrits en lignes ; lue comme un élève du début à la fin (lignes numérotées à l'activité 2, programmes lisibles, consignes en ①②③). Pastilles du positionnement rendues visibles (aussi sur `5e_C9.1`). Question ouverte : les documents 1, 2 et 3 contiennent les réponses des activités 1, 3 et 5. Mode mission rejoué (46 écrans, 21 vérifiés : les rangées qui se suivent partagent un écran). Moteur corrigé (#674) : l'éditeur de l'activité 4 passe avant la vérification. Troisième passe #677 : lecture au téléphone (banc de tests de l'activité 5, documents, code des expériences). À décider : en mission sur grand écran, la question commence deux écrans sous la ressource. Audit du 12/11 (`docs/audits/AUDIT_3e_C9.1_2026-11-12.md`) : règles d'or n°322 à n°330 ; première étape #678 — l'activité 5 teste la fonction de l'élève (7 appels, frontières 99/100/101, deux conditions vraies), les verrous 3 et 4 jugent le résultat, la règle du + corrigée (QCM, lexique), commandes nommées, onglets au clavier, crédits à 8,3:1. Deuxième étape (#679) : les quatre dessins deviennent du texte HTML (aucun texte sous 14 px à 390 px), simulateur pas à pas, impression sans trous (281 → 163 mm de blanc perdu, 15 pages). Écart : séances 2 et 4 à 1 352 et 1 431 mots visibles (le texte des dessins est maintenant compté) — piste : replier les documents, décision de Pascal. Troisième étape (#680) : billet de sortie seul et sans aide (séance 3), expérience D (`float`, `bool`), « une cause, deux symptômes », scénario annoncé, transition vers la ventilation. À décider : le transfert individuel (branche `fable/revision/3e-c9-1-transfert`, +10 min en séance 4) ; replier les documents |
| 28 | `3e_C7.1` | 3512 → 2213 | 1 → 0 | 20 → 0 | 12 → 0 | #688, puis une séance 4 #695 — séance 3, 3 147 → 1 024 ; au-dessus du repère : séance 4 (2 213 : l'exercice d'atelier des croquis, voulu par Pascal le 24/10) et séance 2 (1 755) |
| 29 | `5e_C5.1` | 1109 → 1040 | 1 → 0 | 30 → 0 | 4 → 0 | livrée #689 — les 30 questions se devinaient (bonne réponse toujours la première et la plus longue) : 11 réécrites (n°144), 3 grilles, validation au tout-juste comme le disent les critères, corrections exhaustives, protocole replié pendant qu'on le range ; bilan avec retour à l'hypothèse et métacognition |
| 30 | `4e_C4.7` | 2023 → 1791 | 1 → 0 | 40 → 0 (la commande du simulateur reste une liste) | 7 → 0 | livrée #690 — la bonne réponse était 32 fois sur 40 la plus longue : 35 questions réécrites (n°144), chaque erreur « à revoir » et expliquée ; replis (contrat du binôme, cartouche CRCN, lignes Socle, Bonus) ; séances 1, 2 et 4 encore au-dessus du repère (1 647 · 1 791 · 1 470) — question à Pascal : replier les fiches d'activité sur toutes les séquences |
| 31 | `5e_C4.7` | 1807 → 1695 | 1 → 0 | 35 → 0 (la commande du simulateur reste une liste) | 6 → 0 | livrée #691 — la bonne réponse était 23 fois sur 35 la plus longue : 32 questions réécrites (n°144), chaque erreur « à revoir » et expliquée ; Bonus avec son corrigé ; séances 1 et 3 encore au-dessus du repère (1 695 · 1 584) — même question que 4e_C4.7 |
| 32 | `3e_C7.3` | 1796 → 908 | 0 | 0 | 29 → 0 | livrée #692 — deux grilles, places mélangées (la bonne réponse était 9 fois sur 14 la première), pourquoi des erreurs ; piqûre de rappel du cahier des charges repliée (séance 1, 1 796 → 868) ; banc réparé (67 → 68 / 68) |
| 33 | `3e_C7.4` | 1220 → 1132 | 0 | 0 | 27 → 0 | livrée #693 — une grille (le coût de chaque source), places mélangées (la bonne réponse était 12 fois sur 16 la première), pourquoi des erreurs ; banc réparé (53 → 54 / 54) |
| 34 | `3e_C7.5` | 1439 → 1311 | 0 | 0 | 26 → 0 | livrée #697 — piqûre de rappel repliée à sa source, trois grilles avec réponses de trop, places mélangées, pourquoi des erreurs ; banc réparé (53 → 54 / 54) ; séance 4 (1 311) au-dessus du repère : l'établi y est l'outil de la séance |
| 35 | `3e_C7.7` | 1959 → 1267 | 0 | 0 | 24 → 0 | livrée #698 — piqûre de rappel repliée à sa source, trois grilles avec une réponse de trop, places mélangées (la bonne réponse était 11 fois sur 18 la première), pourquoi des erreurs ; n°304 ; banc réparé (76 → 77 / 77) ; séances 2 (1 267) et 4 (1 245) à peine au-dessus : l'atelier des moyens (432 mots) est l'outil de chaque séance |
| 36 | `3e_C7.8` | 1530 → 1088 | 0 | 0 | 21 → 0 | livrée #699 — la bonne réponse se devinait (11 fois sur 24 la plus longue, 17 fois la première) : 24 propositions fausses allongées, une remplacée (elle était défendable), une grille avec une réponse de trop, places mélangées, pourquoi des erreurs ; banc réparé (57 → 58 / 58) ; chaque séance sous le repère |
| 37 | `3e_C8.1` | 1888 → 1243 | 0 | 0 | 23 → 0 | livrée #700 — la bonne réponse se devinait (14 fois sur 17 la première, 10 fois la plus longue) : 24 propositions fausses allongées, places changées, pourquoi des erreurs ; piqûre de rappel repliée à sa source ; séance 3 (1 243) à peine au-dessus : le simulateur y est l'outil de la séance |
| 38 | `3e_C8.2` | 1414 → 982 | 0 | 0 | 28 → 0 | livrée #701 — la bonne réponse était 9 fois sur 20 la plus longue : 21 propositions fausses allongées, places changées, une grille avec une réponse de trop, pourquoi des erreurs ; piqûre de rappel repliée à sa source ; banc réparé (42 → 44 / 44) ; chaque séance sous le repère |
| 39 | `3e_C9.2` | 2597 → 1496 | 2 → 0 | 62 → 0 | 48 → 0 | livrée #702 et #705 — les 62 listes deviennent des boutons radio (les quatre pages engendrées gardent la sauvegarde) ; piqûre de rappel repliée à sa source, captures des gestes et du programme de référence repliées ; puis 85 propositions fausses allongées (la bonne réponse était la plus longue 33 fois sur 48) et 135 pourquoi ; séance 3 (1 496) au-dessus : séance d'atelier, les cinq gestes se lisent en faisant |
| 40 | `4e_C7.1` | 1780 → 1488 | 2 → 0 | 22 → 0 | 28 → 0 | livrée #703 — 20 listes en boutons radio (les deux du banc météo restent des commandes) ; le ✘ n°23 était un faux (les « 15 minutes » du rappel) ; piqûre de rappel repliée à sa source, séance 1 1 244 → 580 ; séance 2 (1 488) au-dessus : activité 3, exercice FAST et toute la clôture ; banc n°311 : les onglets de la séance 2 hors du premier écran à 390 px, sur `main` comme ici |
| 41 | `4e_C7.3` | 1866 → 1551 | 5 → 0 | 13 → 0 | 27 → 0 | livrée #704 — ✘ et menus déjà à 0 sur `main` (migration du 07/11) ; piqûre de rappel repliée à sa source, séance 1 1 597 → 938 ; une réponse de trop dans les deux grilles ; séance 2 (1 551) au-dessus : le banc des matériaux, outil de la séance, et la clôture |
| 42 | `4e_C7.4` | 1582 → 1362 | 5 → 0 | 22 → 0 | 23 → 0 | livrée #706 — ✘ et menus déjà à 0 sur `main` (migration du 07/11) ; 10 groupes mélangés, réponses chiffrées dans l'ordre, 3 propositions allongées ; une réponse de trop dans la grille ; séance 2 (1 362) au-dessus : le banc, outil de la séance, et la clôture |
| 43 | `4e_C7.5` | 2077 → 1572 | 5 → 0 | 23 → 0 | 25 → 0 | livrée #707 — ✘ et menus déjà à 0 sur `main` (migration du 07/11) ; piqûre de rappel repliée à sa source, séance 1 1 728 → 1 078 ; une réponse de trop dans la grille ; séance 2 (1 572) au-dessus : l'établi, outil des deux séances (471 mots), et la clôture |
| 44 | `4e_C7.7` | 1831 → 1698 | 5 → 0 | 16 → 0 | 19 → 0 | livrée #709 — ✘ et menus déjà à 0 sur `main` (migration du 07/11) ; une réponse de trop dans les deux grilles ; « allonger la fente à 23 mm » réfuté ; une phrase de la fabrique retirée ; séance 2 (1 698) au-dessus : l'atelier, outil de la séance, des propositions longues par construction, et la clôture |
| 45 | `4e_C7.8` | 1880 → 1616 | 5 → 0 | 19 → 0 | 15 → 0 | livrée #710 — ✘ et menus déjà à 0 sur `main` (migration du 07/11) ; la bonne réponse était la plus longue 11 fois sur 13 : 19 propositions fausses allongées ; une réponse de trop dans la grille ; séance 2 (1 616) au-dessus : le banc du lien, outil de la séance, et la clôture |
| 46 | `4e_C8.1` | 1975 → 1320 | 1 → 0 | 25 → 0 | 22 → 0 | livrée #711 — 16 listes en boutons radio, grille « Conforme ? » comprise (ordre, noms et retours gardés) ; les 8 menus du tableau de l'exercice incrusté reconnus comme voulus (n°317) ; piqûre de rappel repliée ; six corrections de l'exercice aérées à leur source ; séance 2 (1 320) juste au-dessus : l'exercice du diagramme des exigences |
| 47 | `4e_C9.1` | 2909 → 2378 | 1 → 0 | 54 → 0 | 34 → 0 | livrée #713 — 43 questions en boutons radio, les 11 commandes de l'atelier de programmation déclarées (`data-interface`) ; 25 groupes mélangés ; échauffement, rappel de l'algorigramme, rôles et nuit simulée repliés ; 91 pourquoi ; séances 2 et 3 (2 064, 2 378) loin au-dessus : séances d'atelier, l'éditeur et l'atelier sont dans la page — couper une activité ou ajouter une séance, décision de Pascal |
| 48 | `5e_C7.1` | 1685 → 1239 | 1 → 0 | 17 → 0 | 17 → 0 | livrée #714 — 17 listes en boutons radio ; l'algorigramme ne se lit plus dans l'ordre de la réponse (et `3e_C7.1`, même défaut) ; séance 2 : 1 239 mesurés, dont 109 de légendes pour le lecteur d'écran (1 130 vus) |
| 49 | `5e_C7.3` | 1694 → 1607 | 5 → 0 | 15 → 0 | 15 → 0 | livrée #715 — migrée au gabarit commun ; deux grilles lettrées, l'une se devinait par la grammaire, l'autre avait deux réponses justes ; une réponse de trop dans chacune ; séance 2 (1 607) au-dessus : le banc, outil de la séance, la synthèse et le bilan |
| 50 | `5e_C7.4` | 1607 → 1302 | 5 → 0 | 18 → 0 | 16 → 0 | livrée #716 — migrée au gabarit commun ; l'activité 1 se joue dans la chaîne d'énergie de l'indicateur (outil commun de #708) ; séance 2 (1 302) un peu au-dessus : le banc, la synthèse, le bilan |
| 51 | `5e_C7.5` | 1528 → 1317 | 5 → 0 | 22 → 0 | 8 → 0 | livrée #718 — migrée au gabarit commun ; l'activité 0 dans le schéma du prototype ; l'ordre du montage ne se lit plus à l'écran ; séance 2 (1 317) un peu au-dessus : l'établi, la synthèse, le bilan |
| 52 | `5e_C8.1` | 1421 → 1364 | 5 → 0 | 17 → 0 | 13 → 0 | livrée #719 — migrée au gabarit commun ; une réponse en double remplacée ; 18 propositions fausses allongées ; séance 2 (1 364) au-dessus : le simulateur, deux tableaux, la synthèse et le bilan |
| 53 | `5e_C8.2` | 1412 → 1035 | 5 → 0 | 16 → 0 | 12 → 0 | livrée #720 — migrée au gabarit commun ; la grille de l'activité 4 ne se lit plus toute seule ; 12 propositions fausses remplacées ou allongées ; les deux séances sous le repère |
| 54 | `5e_C9.1` | 1761 → 1282 | 1 → 0 | 24 → 0 | 5 → 0 | livrée #723 — 24 listes en boutons radio ; pas à pas de l'Explorateur, notes Vittascience et Bonus repliés ; séance 2 (1 282) juste au-dessus : l'encart des gestes, commun à six pages |
| 55 | `3e_C1.1` | 1451 → 1259 | 0 → 0 | 0 → 0 | 23 → 0 | livrée #728 — 15 captures du tableur et le Bonus repliés ; deux encadrés qui donnaient les réponses passés en aide ; la bonne réponse ne se devine plus à sa longueur ; 84 pourquoi avec leur étape suivante ; séance 1 (1 259) juste au-dessus : une activité de 50 min, définitions et neuf questions |
| 56 | `3e_C3.1` | 1939 → 1181 | 0 → 0 | 0 → 0 | 19 → 0 | livrée #729 — les deux piqûres de rappel et le Bonus repliés ; la bonne réponse ne se devine plus à sa longueur (18 raccourcies, 18 leurres allongés) ; 78 pourquoi avec leur étape suivante ; chaque séance sous le repère |

## Deuxième passe (15/11/2026)

Décision de Pascal du 15/11/2026 : « une deuxième passe en commençant par les plus lourdes, sur tout avec tes nouveaux
outils, ainsi tu pourras améliorer toutes les séquences ». Mesure de départ, sur `main` (56 séquences) : **1 094 questions
vérifiées, dont 560 où la bonne réponse est la plus longue** (353 de plus de 10 signes : elle se devine à sa longueur) ;
**1 296 mauvaises propositions sans « pourquoi »** ; 56 séances au-delà de 1 200 mots visibles.

Ce que fait la passe, séquence par séquence, de la plus lourde à la plus légère :
- **la bonne réponse ne se devine plus à sa longueur** : de préférence, c'est elle qui raccourcit (moins à lire) ; sa
  justification reste dans la correction et dans le « pourquoi » des erreurs ; sinon, une proposition fausse s'allonge ;
- **chaque mauvaise proposition a son « pourquoi »** (mode mission), sans dire la bonne réponse ;
- ce qui ne sert qu'au besoin se replie, à la source quand c'est une incrustation d'atelier ; les exercices d'atelier
  restent à découvert (décision de Pascal du 15/11/2026 sur `5e_C2.1`) ;
- l'aération à zéro, y compris dans les incrustations, corrigées à leur source.

Colonnes : séance la plus lourde (mots visibles) ; bonnes réponses plus longues de 10 signes ou plus que toutes les
autres ; mauvaises propositions sans « pourquoi ». Avant → après.

| N° | Séquence | Séance la plus lourde | Bonne réponse la plus longue | Sans pourquoi | État |
|---|---|---|---|---|---|
| 2.1 | `5e_C4.1` | 2171 → 2171 | 12 → 0 | 8 → 0 | lot 1, livré #740 — 12 questions rééquilibrées ; les trois lectures fléchées du FAST aérées, à la source et dans l'atelier et le cahier de 5e ; séance 6 inchangée (positionnement sur 8 compétences, FAST incrusté) |
| 2.2 | `3e_C7.1` | 2095 → 2095 | 0 → 0 | 35 → 0 | lot 1, livré #740 — 35 pourquoi ; la question du seuil disait « à partir de 28 °C » quand la LED s'allume au-dessus : « au-dessus de » |
| 2.3 | `5e_C2.1` | 2090 → 2090 | 19 → 0 | 66 → 0 | lot 1, livré #740 — 19 questions rééquilibrées, 66 pourquoi ; séances 1 et 2 : les exercices d'atelier gardés |
| 2.4 | `5e_C3.1` | 1874 → 1823 | 21 → 0 | 90 → 0 | lot 1, livré #740 — 22 questions rééquilibrées, 90 pourquoi |
| 2.5 | `5e_C1.2` | 1844 → 1803 | 20 → 0 | 66 → 0 | lot 1, livré #740 — 20 questions rééquilibrées, 66 pourquoi ; séance 4 : le FAST du freinage |
| 2.6 | `4e_C1.1` | 1698 → 1698 | 22 → 0 | 69 → 0 | lot 1, livré #740 — 22 questions rééquilibrées, 69 pourquoi ; séance 5 : deux exercices d'atelier |
| 2.7 | `4e_C7.5` | 1576 → 1576 | 0 → 0 | 30 → 0 | lot 2, livré #740 — les 30 pourquoi de la chaîne à compléter ; la page à jour de son fichier de mission |
| 2.8 | `4e_C2.1` | 1477 → 1451 | 19 → 0 | 69 → 0 | lot 2, livré #740 — 21 questions rééquilibrées, 69 pourquoi |
| 2.9 | `3e_C2.1` | 1362 → 1363 | 18 → 0 | 63 → 0 | lot 2, livré #740 — 20 questions rééquilibrées, 63 pourquoi |

Le lot 1 est arrivé sur `main` avec le lot 2 (#740, qui le contenait ; #739, qui le portait seul, est fermée). Les lignes 2.1 à 2.6 sont mesurées avant la vague n°335 du thème 1 (#737), les lignes 2.7 à 2.9 après : ses énoncés en questions ajoutent quelques mots. La remesure du lot 1 après la fusion est au journal.

## Notes par séquence

- **5e_C1.5** (le compte du club), 08/11/2026 : ancien gabarit → gabarit commun (`migrer_gabarit_306.py`, 25 listes →
  groupes, 4 versions étayées) ; trois **grilles** (`grilles_radio.py`) : 14 questions qui partageaient leurs réponses
  les lisent une fois, lettrées ; 40 retours à la ligne dans les corrections (`aerer_corrections.py`) ; 13 consignes et
  annonces de plus de 25 mots coupées en lignes. Séance 3 : 1 549 → 1 322 mots, au-dessus du repère : c'est la séance
  de clôture (synthèse, banc de publication pour le Bonus, Bonus facultatif, bilan) ; sans le Bonus et son banc, elle
  passe sous 1 000.
- **5e_C1.3** (les vélos de Hangzhou), 08/11/2026 : déjà sous le repère (1 050 / 217 / 718 mots). 14 retours à la ligne
  dans les corrections, 5 hors corrections (`aerer_corrections.py --partout`) ; les trois « Au programme », la consigne
  de l'activité 2, le transfert et le bilan en lignes ;
  l'incrustation de l'atelier « carte mentale » allégée (la définition de « donnée » y était dite trois fois, l'intro ne
  la redit plus ; la consigne passe en ① ② ⚠), corrigée à l'identique dans sa source (`donnees_carte_mentale.py`,
  `incrustations_lots/donnees_et_validation.py`), l'atelier de 5e et le cahier de 5e — le générateur, rejoué à part,
  produit le même texte.
- **4e_C1.1** (Tsinghua, les feux), 08/11/2026 :
  - séance 1 : 1 641 → 921 mots. Les 15 captures des quatre gestes du tableur se déplient à la demande
    (`replier_captures.py`) : chaque geste reste écrit en toutes lettres, ses images et leurs légendes sont à un clic ;
  - séance 5 : 3 570 → 2 911 mots. La piqûre de rappel de la bête à cornes est repliée (option `replie` des
    incrustations) ; les introductions des deux blocs d'exercices et de l'activité 5 ne redisent plus l'objectif ;
  - 75 retours à la ligne (corrections, consignes, définitions, légendes) ; trois légendes réécrites ; six corrections
    des ateliers aérées à leur source (`donnees_besoin.py`, `donnees_carte_mentale.py`), dans les ateliers, les cahiers
    et les séquences qui les portent ;
  - **la séance 5 restait au-dessus du repère** (trois exercices d'atelier voulus le 24/10/2026). Pascal, le
    08/11/2026 : « la couper en deux séances ». Séance 5 : le rappel et les exercices 1 et 2 (1 836 mots) ; séance 6 :
    l'exercice 3 et la clôture (1 106 mots). La séance 5 reste au-dessus du repère : deux exercices d'atelier, dont le
    texte visible vient des exercices eux-mêmes (énoncés, schémas de la bête à cornes, propositions).
- **4e_C1.4** (cybersécurité), 08/11/2026 : séance 3, 1 291 → 1 056 mots (le Bonus replié compris). Les exemples de l'activité 5.b se déplient à
  la demande (l'un d'eux était écrit deux fois) ; le titre de 5.a ne répète plus la question ; la phrase « Personne n'est
  pénalisé… » du Bonus (son titre dit déjà « facultatif ») et la redite du bilan retirées ; les étiquettes du Bonus ne
  recopient plus la consigne. Lu comme un élève : « hover », « désactive géo inutile », « cite les sources pour œuvres »
  et les « Risques » en style télégraphique réécrits en phrases. 76 retours à la ligne ; deux corrections coupées à la main. Puis (#625, fusionnée après #624) : les cinq « Mise en situation » donnaient la réponse avant l'exercice (« Risques impliqués », « Bonne attitude à avoir ») — ces paragraphes se replient dans « 💡 Ce que cette situation apprend — à ouvrir après avoir répondu » ; le texte repris est celui de #624.
- **Le Bonus se déplie quand on a fini** (`replier_bonus.py`, 08/11/2026) : posé aussi sur 5e_C1.5 (séance 3 : 1 322 →
  1 206 mots), 5e_C1.3 et 4e_C1.1, déjà révisées. Le titre du Bonus reste visible ; ses défis, ses champs et son corrigé
  sont à un clic.
- **3e_C1.5** (numérique et société), 08/11/2026 : séance 4 (clôture), 2 017 → 1 588 mots ; séance 2, 1 219 → 1 184.
  Le Bonus replié ; le devoir sur les troubles musculo-squelettiques garde sa consigne, ses conseils (INRS) se
  déplient ; la conclusion passe du « vous » au « tu ». Séance 2 : deux faux titres (texte de 28 px) et un `<h1>` au
  milieu d'une séance deviennent des titres de leur niveau ; une correction en double (même identifiant sous deux
  questions, la première question sans bouton) coupée en deux corrections, chacune à sa question ; l'encadré
  d'introduction ne donne plus d'avance les réponses du tri 2.a ; l'introduction de l'incrustation de la carte
  mentale allégée (à sa source). 89 retours à la ligne ; un argumentaire modèle de l'atelier de 3e en lignes, à sa
  source. **La séance 4 reste au-dessus du repère** : c'est la clôture la plus longue du site (activité 5 de 25 min,
  bilan, synthèse sur l'écologie du numérique, autoévaluation, devoir).
- **3e_C2.1** (Pékin, la borne), 08/11/2026 : séance 3, 1 861 → 1 424 mots ; séance 2, 1 246 → 1 243. **Les exercices
  « classer » des ateliers se lisent en grille** (`moteur.py`, 08/11/2026) : six questions qui partageaient cinq modes de
  représentation les écrivaient trente fois ; les modes s'écrivent une fois, lettrés, et chaque question a sa rangée
  de lettres. Le Bonus replié ; l'introduction de l'incrustation allégée (à sa source) ; une légende et deux
  corrections en lignes. **Les séances 2 et 3 restent au-dessus du repère** : séance 2, deux activités (six modes, trois
  destinataires ; l'algorigramme de l'incident), avec le document de six modes à lire ; séance 3, l'exercice d'atelier
  et la production défendue, avant la clôture. Le banc de la séquence : 55 / 58, comme sur `main` (n°298, liens des
  deux synthèses).
- **5e_C1.1, 5e_C1.2, 5e_C3.1, 4e_C2.1, 4e_C3.1**, 10/11/2026 — la passe outillée : captures des gestes repliées (53),
  Bonus replié, 327 retours à la ligne, grilles des exercices « classer », les gestes « Nommer » et « Sortir » en lignes
  (• et ①②③), les légendes des gestes du tableur coupées en deux phrases.
  - **5e_C1.1** (Chengdu) : séance 2, 1 629 → 907 mots (les captures) ; séance 1, 1 347 → 1 301 (la variante de la pesée en
    continu passe en « Pour aller plus loin ») ; séance 5, 1 393 → 1 258. Séances 1 et 5 au-dessus du repère : le
    document des trois principes (déjà vulgarisé, avec son animation) ; la clôture.
  - **5e_C1.2** (Sainte-Luce) : séance 2, 1 696 → 923 ; séance 4, 2 117 → 1 967. Séance 4 au-dessus du repère :
    l'exercice d'atelier sur le diagramme FAST (719 mots à lui seul), l'activité 5 et le bilan.
  - **5e_C3.1** (Shanghai) : séance 4, 2 912 → 1 447 ; séance 1, 2 164 → 1 994. Séance 1 au-dessus du repère : les deux
    exercices d'atelier de la bête à cornes (1 092 mots) avant l'activité 1.
  - **4e_C2.1** (Hangzhou, la borne) : séance 3, 2 625 → 1 716 (la piqûre de rappel du cahier des charges repliée :
    799 mots) ; séance 1 inchangée (1 548 : l'exercice d'atelier du croquis, 786 mots). **n°23 reste ✘** : 165 min
    annoncés pour 165 disponibles, sans les 10 min de service. Les trois séances sont pleines (5 + 50, 30 + 25,
    45 + 10) : question posée à Pascal (une quatrième séance, ou l'exercice du croquis rendu facultatif).
  - **4e_C3.1** (Hangzhou, les vélos) : séance 1, 1 850 → 1 299 (la piqûre de rappel de la bête à cornes repliée).
- **Les incrustations s'aèrent à leur source** (10/11/2026) : `incrustations.py` passe chaque incrustation par
  `aerer_corrections.aerer` ; les corrections du rappel du cahier des charges s'écrivent une idée par ligne
  (`donnees_rappel_cdc.py`). Les neuf séquences révisées qui portent une incrustation sont remises à jour ; les 17
  autres le seront à leur tour de passe (`incrustations.py --verifier` les dit « à mettre à jour » d'ici là).
- **4e_C2.1, la quatrième séance** (11/11/2026 ; Pascal : « une 4e »). Le n°23 est réglé : 165 minutes annoncées pour
  220 disponibles. La séance 3 garde l'activité 4 (1 716 → 1 306 mots) ; la séance 4, « Conclure », porte le Bonus, le
  bilan et le QCM (439 mots). La séance 1 reste à 1 548 mots (l'exercice d'atelier du croquis).
- **Thème 1, les activités qui ne se vérifiaient pas** (14/11/2026 ; Pascal : « Claude écrit les questions »).
  - **5e_C1.3** (#681) : 24 questions fermées (9 / 9 / 6), vérifiées par la page, une correction complète chacune ; la
    tâche se coche au tableau de bord quand tout est juste. Séance 1, 1 043 → 1 199 mots (la grille des huit rôles :
    64 lettres ; le redondant retiré de la vue pour tenir le repère) ; séance 2, 224 → 579 ; séance 3, 645 → 962.
    Fiche papier 9 → 11 pages.
  - **4e_C1.4** (#684) : les cinq quiz, 35 questions à deux propositions, deviennent 35 questions à quatre propositions
    (7 par quiz), vérifiées quiz par quiz ; tableau de bord des tâches ; mode mission 10 → 47 écrans, 35 réponses lues.
    Séance 1, 893 → 1 043 ; séance 2, 532 → 839 ; **séance 3, 1 014 → 1 350** : deux sections et la clôture (environ
    300 mots qui ne bougent pas). Pistes : replier les mises en situation des sections 5 et 6, ou une séance 4 (section 6
    et clôture) — question posée à Pascal ; réponse : « créer une séance 4 » (#686 : séance 3, 439 mots ; séance 4,
    917).
  - **3e_C1.5** (#685) : quatre blocs, 13 questions à quatre propositions, dans les activités 1, 2, 3.a et 3.b ; les
    vérifications de 1 bis et de l'activité 5 lisibles par le mode mission ; mode mission 13 → 27 écrans, 19 réponses
    lues. Séance 1, 868 → 1 009 ; **séance 2, 1 098 → 1 234** (l'activité 2 et l'exercice d'atelier 2.d) ; séance 3,
    792 → 1 084. Le thème 1 est fait.
- **5e_C2.1** (Shenzhen, la station de vélos), 14/11/2026 (#687) : aération 20 → 0, dont sept textes d'ateliers corrigés à
  leur source et reportés dans `5e_C3.1`, les deux ateliers de 5e et le cahier ; le billet d'entrée ne donne plus sa
  réponse (note repliée) ; séance 1, 2 272 → 2 166 ; séance 2, 2 052 → 2 004. Au-dessus du repère : les exercices
  d'atelier (bête à cornes, environ 700 mots ; pieuvre, environ 1 280) — question posée à Pascal.
  Pascal, le 15/11/2026 : **on garde les exercices d'atelier** ; l'écart au repère est justifié (ils sont la pratique de la
  séance). Le repli des fiches d'activité, sur toutes les séquences, allège ce qui les entoure.
- **3e_C7.1** (New York, le capteur de confort), 14/11/2026 (#688) : 20 questions en listes → boutons radio (les bancs
  gardent leurs appels par le shim `_groupesRadio`) ; aération 12 → 0, dont quatre textes d'ateliers (FAST, croquis)
  corrigés à leur source ; Bonus replié. Séance 3, 3 512 → 3 147 : les activités 6 et 7 avec leurs exercices d'atelier,
  la clôture, et deux cartes après le bilan — une séance 4 est proposée à Pascal.
  15/11/2026 (#695), décision de Pascal : **une séance 4** « Proposer, puis représenter » — l'activité 7, la synthèse et
  la clôture y passent, déplacées sans être réécrites ; les deux cartes de la suite du projet remontent avant le Bonus
  (n°301). Séances 612 · 1 755 · 1 024 · 2 213. La séance 4 reste au-dessus du repère : l'exercice d'atelier des croquis
  (1 438 mots), voulu par Pascal le 24/10 ; la séance 3, courte (13 min), laisse de la marge pour finir la séance 2.
- **5e_C5.1** (dépanner le lampadaire), 14/11/2026 (#689) : la page était légère, mais ses 30 questions se devinaient — la
  bonne réponse toujours la première et la plus longue. Trois grilles, onze questions réécrites (n°144), la validation au
  tout-juste comme le disent les critères, chaque erreur marquée « à revoir » et expliquée ; en séance 2, le protocole se
  replie pendant qu'on le range et les boutons du simulateur ne sont plus dans l'ordre. Bilan complété (retour à
  l'hypothèse, métacognition), Bonus replié avec son corrigé. Séances 508 · 554 · 1 040.
- **4e_C4.7** (SOS serre, Packet Tracer), 14/11/2026 (#690) : la même faille que `5e_C5.1` — la bonne réponse était 32 fois sur
  40 la plus longue. 35 questions réécrites, le défi et le positionnement en boutons, la commande du simulateur laissée en
  liste ; corrections question par question ; n°304 (« tu as appris en 5e ») corrigée ; contrat du binôme, cartouche CRCN,
  lignes Socle et Bonus repliés. Séances 1 647 · 1 791 · 918 · 1 470 : les recettes Packet Tracer et les fiches d'activité
  pèsent — question posée à Pascal (replier les fiches d'activité partout).
- **5e_C4.7** (le réseau de la salle, Packet Tracer), 14/11/2026 (#691) : même famille que `4e_C4.7` — la bonne réponse était
  23 fois sur 35 la plus longue. 32 questions réécrites, positionnement en boutons, commande du simulateur en liste ;
  corrections question par question ; n°304 ; lignes Socle, cartouche CRCN et Bonus repliés, le Bonus avec son corrigé.
  Séances 1 695 · 1 136 · 1 584.
- **3e_C7.3** (le boîtier de la station), 14/11/2026 (#692) : deux grilles (le verdict des matériaux, les trois sorties),
  8 groupes mélangés, 27 pourquoi pour le mode mission ; la piqûre de rappel du cahier des charges repliée à sa source ;
  aération 29 → 0 ; « avait écarté … en 3e_C8.2 » (n°304) corrigé ; le banc de la séquence, en échec sur `main` depuis
  l'étape 2 de l'audit externe, suit la page. Séances 868 · 908 · 779 · 896.
- **3e_C7.4** (l'énergie de la station), 15/11/2026 (#693) : une grille (ce que coûte chaque source), 13 groupes mélangés,
  39 pourquoi pour le mode mission ; aération 27 → 0 ; n°304 ; le banc de la séquence suit la page (réponse libre).
  Séances 681 · 912 · 1 132.
- **3e_C7.5** (la station qu'il faut équiper), 15/11/2026 (#697) : la piqûre de rappel du cahier des charges se replie à
  sa source (elle reçoit au passage les corrections aérées du générateur) ; trois grilles (ce qu'impose chaque exigence, le
  constituant retenu, ce que coûte chaque retrait), avec des réponses de trop pour que la dernière ligne ne se devine pas ;
  places mélangées ; 15 pourquoi, 12 indices ; Bonus replié ; aération 26 → 0 ; n°304 (« Tu as calculé… en 3e_C7.4 »).
  Séances 1 286 · 256 · 1 020 · 1 439 → 386 · 257 · 896 · 1 311. Au-dessus du repère : la séance 4, dont l'établi
  (260 mots) est l'outil même de la séance.
- **3e_C7.7** (produire le boîtier), 15/11/2026 (#698) : la piqûre de rappel du cahier des charges se replie à sa source
  (elle reçoit au passage les corrections aérées du générateur) ; trois grilles (l'empreinte de chaque moyen, ce qui bloque
  chaque cote, ce qu'une seule fournée impose), chacune avec une réponse de trop ; 8 groupes mélangés ; deux bonnes
  réponses raccourcies (elles étaient nettement les plus longues) ; 24 pourquoi, 10 indices ; Bonus replié ; aération
  24 → 0. n°304 : le bloc « Ce que tu sais déjà faire » devient « Avant de commencer : où en est le projet », avec de quoi
  rattraper (la synthèse de 3e_C7.3, le TP de 3e_C7.6). Séances 1 123 · 1 959 · 969 · 1 337 → 977 · 1 267 · 903 · 1 245.
- **3e_C7.8** (deux stations qui se parlent), 15/11/2026 (#699) : la bonne réponse était 11 fois sur 24 la plus longue,
  souvent de loin, et 17 fois la première ; 24 propositions fausses s'allongent d'une justification plausible, une est
  remplacée (« utile une fois par jour, pas à chaque message » : la correction elle-même le disait) ; la grille des essais
  reçoit une réponse de trop ; 19 groupes mélangés ; 51 pourquoi, 6 indices ; Bonus replié ; aération 21 → 0.
  Séances 855 · 1 003 · 1 530 → 890 · 1 088 · 1 002 : les séances 1 et 2 prennent quelques mots (les propositions
  allongées), la séance 3 en perd 528, et toutes passent sous le repère.
- **3e_C8.1** (le mât de la station, la simulation), 15/11/2026 (#700) : la bonne réponse était 14 fois sur 17 la
  première et 10 fois la plus longue, souvent de loin (141 caractères contre 63) ; 24 propositions fausses s'allongent
  d'une raison plausible, 7 bonnes réponses quittent la première place, les réponses chiffrées vont dans l'ordre ; la
  piqûre de rappel du cahier des charges se replie à sa source ; 50 pourquoi ; Bonus replié ; aération 23 → 0.
  Séances 355 · 760 · 1 825 → 381 · 827 · 1 243 (les deux premières prennent les mots des propositions allongées).
- **3e_C8.2** (le mât de la station, le protocole), 15/11/2026 (#701) : la bonne réponse était 9 fois sur 20 la plus
  longue (jusqu'à 27 caractères de plus) ; 21 propositions fausses s'allongent d'une raison plausible ; mélange, puis 5
  bonnes réponses déplacées hors de la première place ; la grille des angles morts reçoit une réponse de trop ; la piqûre de
  rappel du cahier des charges se replie à sa source ; 43 pourquoi, 5 indices ; Bonus replié ; aération 28 → 0.
  Séances 756 · 1 348 · 1 041 · 1 138 → 812 · 766 · 663 · 982.
- **3e_C9.2** (la station d'alerte cyclonique), 15/11/2026 (#702) : 62 listes déroulantes deviennent des boutons
  radio, et les quatre pages engendrées gardent la sauvegarde ; le texte de remplacement à chevrons (n°34) est échappé ;
  49 groupes mélangés ; piqûre de rappel repliée à sa source ; captures des cinq gestes, programme de référence,
  tableau du montage, raccourci et pourquoi repliés ; Bonus replié ; aération 48 → 0. Séances 1 132 · 906 · 2 504 ·
  1 459 · 475 · 898 · 514 · 1 132 → 488 · 879 · 1 416 · 1 132 · 463 · 904 · 499 · 976. La séance 3 reste au-dessus :
  séance d'atelier, les gestes se lisent en faisant. Reste, pour la PR suivante : la bonne réponse la plus longue dans
  33 questions sur 48, et le pourquoi des erreurs pour le mode mission.
  Seconde passe, 15/11/2026 (#705) : 85 propositions fausses allongées d'une raison plausible (la bonne réponse était
  la plus longue 33 fois sur 48) ; 135 pourquoi pour le mode mission, recopiés dans les quatre pages ; la correction de
  l'activité 1 réfute aussi « un choix fait pour l'exercice ». Séance 3 : 1 416 → 1 496 (les propositions allongées).
- **4e_C7.1** (le jardin connecté, concevoir), 15/11/2026 (#703) : 20 listes deviennent des boutons radio ; le ✘ n°23
  comptait les « (15 minutes au lieu de 5) » du rappel comme des durées : l'écart s'écrit « un quart d'heure au lieu de
  5 minutes » ; piqûre de rappel repliée à sa source ; 14 groupes mélangés, les échelles du tableau des matériaux dans
  l'ordre ; billet d'entrée sans « En 5e, on commençait par » ; 42 pourquoi ; Bonus replié ; aération 28 → 0. Séances
  1 244 · 1 726 → 580 · 1 488. Reste : la séance 2 au-dessus (la clôture n'est pas repliable), et l'en-tête de l'ancien
  gabarit qui pousse les onglets hors du premier écran à 390 px (banc n°311, sur `main` aussi).
- **4e_C7.3** (le bac du jardin), 15/11/2026 (#704) : déjà sur le gabarit commun, sans ✘ ni menu ; piqûre de rappel
  repliée à sa source ; 7 groupes mélangés, 2 propositions allongées ; 12 pourquoi, 7 indices, une réponse de trop dans chacune des deux grilles ;
  Bonus replié ; aération 27 → 0. Séances 1 597 · 1 665 → 938 · 1 551. Reste : la séance 2 au-dessus (le banc des
  matériaux, outil de la séance, 332 mots ; la synthèse et le bilan, 440).
- **4e_C7.4** (l'énergie du jardin), 15/11/2026 (#706) : déjà sur le gabarit commun, sans ✘ ni menu ; 10 groupes
  mélangés, réponses chiffrées dans l'ordre croissant, 3 propositions fausses allongées ; 29 pourquoi, 5 indices, une
  réponse de trop dans la grille ; note des sources du banc et Bonus repliés ; aération 23 → 0. Séances 1 069 · 1 581
  → 1 028 · 1 362. Reste : la séance 2 au-dessus (le banc, outil de la séance, et la clôture).
- **4e_C7.5** (le jardin incomplet), 15/11/2026 (#707) : déjà sur le gabarit commun, sans ✘ ni menu ; piqûre de
  rappel repliée à sa source ; 8 groupes mélangés, 4 propositions allongées ; 18 pourquoi, 6 indices, une réponse de trop dans la grille ; Bonus
  replié ; aération 25 → 0. Séances 1 728 · 1 655 → 1 078 · 1 572. Reste : la séance 2 au-dessus (l'établi, outil des
  deux séances, et la clôture).
- **4e_C7.7** (le support du capteur), 15/11/2026 (#709) : déjà sur le gabarit commun, sans ✘ ni menu ; 10 groupes
  mélangés ; 21 pourquoi, 7 indices, une réponse de trop dans chacune des deux grilles ; la correction réfute aussi
  « allonger la fente à 23 mm » ; la phrase de la fabrique sous les renvois à l'atelier retirée ; Bonus replié ; aération
  19 → 0. Séances 863 · 1 846 → 910 · 1 698. Reste : la séance 2 au-dessus (l'atelier, les propositions longues, la clôture).
- **4e_C7.8** (le jardin publié), 15/11/2026 (#710) : déjà sur le gabarit commun, sans ✘ ni menu ; la bonne réponse
  était la plus longue 11 fois sur 13 : 19 propositions fausses allongées ; 17 groupes mélangés ; 39 pourquoi, 4 indices,
  une réponse de trop dans la grille ; Bonus replié ; aération 15 → 0. Séances 872 · 1 705 → 925 · 1 616. Reste : la
  séance 2 au-dessus (le banc du lien, outil de la séance, et la clôture).
- **4e_C8.1** (le jardin, valider), 15/11/2026 (#711) : 16 listes deviennent des boutons radio, la grille « Conforme ? »
  comprise (son ordre, le nom de chaque case et le retour sous chaque case sont gardés) ; les 8 menus du tableau de
  l'exercice incrusté sont reconnus comme voulus par la n°317 (`verif_regles_audit.py`, `migrer_gabarit_306.py`) ;
  piqûre de rappel repliée ; 9 groupes mélangés ; 34 pourquoi ; six corrections de l'exercice des exigences aérées à
  leur source et dans l'atelier et le cahier ; aération 22 → 0. Séances 432 · 1 878 · 528 → 493 · 1 320 · 485.
- **4e_C9.1** (le jardin programmé), 15/11/2026 (#713) : 43 questions deviennent des boutons radio ; les 11 commandes
  de l'atelier de programmation restent des listes, déclarées `data-interface` ; 25 groupes mélangés ; le pas à pas de
  l'Explorateur (ouvert d'office), Vittascience facultatif, le rappel de l'algorigramme, les rôles et la nuit simulée
  repliés ; 91 pourquoi ; aération 34 → 0. Séances 1 127 · 2 562 · 2 782 → 1 089 · 2 064 · 2 378. Reste : les séances
  2 et 3, séances d'atelier ; les ramener sous le repère demande de couper une activité ou d'ajouter une séance.
- **5e_C7.1** (le mini-projet : l'indicateur de place), 15/11/2026 (#714) : 17 listes en boutons radio (grille de
  validation reliée à ses lignes) ; l'algorigramme mélangé, ses groupes nommés, les énoncés dans les légendes — même
  correction sur `3e_C7.1` ; 31 pourquoi ; consignes en lignes, note Vittascience repliée ; aération 17 → 0. Séances
  274 · 1 685 · 696 → 268 · 1 239 · 658 (séance 2 : 1 130 mots vus, 109 de légendes pour le lecteur d'écran).
- **5e_C7.3** (le banc de la cour), 15/11/2026 (#715) : migrée au gabarit commun (5 ✘ → 0, 15 listes en boutons
  radio, rangées en deux grilles lettrées, quatre versions étayées) ; la grille de l'activité 0 ne se devine plus par
  la grammaire ; une seule réponse juste par ligne dans l'activité 1 (l'acier et le béton) ; une réponse de trop dans
  chaque grille ; 7 groupes mélangés, 9 propositions allongées ; 47 pourquoi, 9 indices ; la phrase de la fabrique
  retirée ; Bonus replié ; aération 15 → 0. Séances 1 095 · 1 694 → 840 · 1 607. Reste : la séance 2 au-dessus (le
  banc, la synthèse, le bilan).
- **5e_C7.4** (l'indicateur du hall), 15/11/2026 (#716) : migrée au gabarit commun (5 ✘ → 0, 17 listes en boutons
  radio, la liste des sources du banc déclarée commande, quatre versions étayées) ; l'activité 1 se joue dans la chaîne
  d'énergie de l'indicateur (sources, carte, DEL ; l'énergie stockée sous son composant, celle qui arrive par la
  gauche), les réponses sans indice ; grille de l'activité 4 avec une réponse de trop ; 53 pourquoi ; Bonus et note
  technique du banc repliés ; aération 16 → 0. Séances 779 · 1 582 → 544 · 1 302. Reste : la séance 2 un peu au-dessus.
- **5e_C7.5** (l'éclairage du préau), 15/11/2026 (#718) : migrée au gabarit commun (5 ✘ → 0, 17 listes en boutons
  radio, les ports de l'établi déclarés commandes, trois versions étayées) ; l'activité 0 dans le schéma du prototype
  (la carte ne se devine plus au féminin) ; les gestes du montage dans le désordre, deux branchements réunis, un geste
  de vérification avant la mise sous tension ; grille des retraits avec une réponse de trop ; 63 pourquoi ; phrase de
  la fabrique retirée ; Bonus replié ; aération 8 → 0. Séances 860 · 1 528 → 676 · 1 317.
- **5e_C8.1** (la patère du hall), 15/11/2026 (#719) : migrée au gabarit commun (5 ✘ → 0, 16 listes en boutons radio,
  le choix du matériau du simulateur déclaré commande, trois versions étayées) ; « 10,0 h » proposé deux fois devient
  « 24,0 h » (le prix lu à la place des heures) ; 16 groupes mélangés, 18 propositions fausses allongées ; 47 pourquoi ;
  Bonus replié ; aération 13 → 0. Séances 523 · 1 400 → 518 · 1 364. Reste : la séance 2 au-dessus.
- **5e_C8.2** (la patère du hall : l'essai de traction), 15/11/2026 (#720) : migrée au gabarit commun (5 ✘ → 0, 15
  listes en boutons radio, l'éprouvette du banc déclarée commande, six versions étayées) ; la grille de l'activité 4
  ne nomme plus ses lignes, avec une réponse de trop ; 12 groupes mélangés, 12 propositions fausses remplacées ou
  allongées ; 46 pourquoi, 5 indices ; Bonus replié ; aération 12 → 0. Séances 689 · 1 393 → 735 · 1 035.
- **5e_C9.1** (la boîte étiquetée), 15/11/2026 (#723) : 24 listes en boutons radio ; 22 groupes mélangés, 5 propositions
  allongées ; le pas à pas de l'Explorateur, les notes Vittascience et le Bonus repliés ; 55 pourquoi ; aération 5 → 0.
  Séances 550 · 1 678 · 1 246 → 539 · 1 282 · 923. Reste : la séance 2 juste au-dessus (l'encart des gestes).
