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

| N° | Séquence | Séance la plus lourde (mots) | ✘ règles | Menus | Aération | État |
|---|---|---|---|---|---|---|
| 1 | `5e_C1.5` | 1549 → 1206 | 4 → 0 | 27 → 0 | 18 → 0 | livrée #619 |
| 2 | `5e_C1.3` | 1050 → 1043 | 0 | 0 | 5 → 0 | livrée #620 |
| 3 | `4e_C1.1` | 3570 → 1836 | 0 | 0 | 22 → 0 | livrée #620 ; séance 5 coupée en deux (décision de Pascal) #624 |
| 4 | `4e_C1.4` | 1291 → 1056 | 0 | 0 | 9 → 0 | livrée #624 ; #625 replie les leçons des situations ; #627 répare le jeu des licences (6.c) |
| 5 | `3e_C1.5` | 2017 → 1448 | 0 | 0 | 19 → 0 | livrée #624 ; #628 ramène la séance 4 à 1 448 — au-dessus du repère, justifiée |
| 6 | `3e_C2.1` | 1861 → 1424 | 0 | 0 | 6 → 0 | livrée #624 — séances 2 et 3 au-dessus du repère, justifiées |
| 7 | `5e_C1.1` | 1629 → 1301 | 0 | 0 | 26 → 0 | livrée #630 — séances 1 et 5 au-dessus du repère, justifiées |
| 8 | `5e_C1.2` | 2117 → 1967 | 0 | 0 | 26 → 0 | livrée #630 — séance 4 au-dessus du repère, justifiée |
| 9 | `5e_C3.1` | 2912 → 1994 | 0 | 0 | 0 | livrée #630 — séances 1 et 4 au-dessus du repère, justifiées |
| 10 | `4e_C2.1` | 2625 → 1548 | 1 → 0 | 0 | 24 → 0 | livrée #630 ; quatrième séance (décision de Pascal) #643 — séances 1 et 3 au-dessus du repère, justifiées |
| 11 | `4e_C3.1` | 1850 → 1299 | 0 | 0 | 10 → 0 | livrée #630 — séance 1 au-dessus du repère, justifiée |
| 12 | `3e_C4.1` | 1444 → 1032 | 1 → 0 | 33 → 0 | 6 → 0 | livrée #632 |
| 13 | `3e_C4.3` | 1928 → 817 | 2 → 0 | 33 → 0 | 8 → 0 | livrée #633 ; #646 coupe la séance 4 en deux (décision de Pascal du 11/11) : cinq séances, 817 · 460 · 437 · 737 · 551 |
| 14 | `5e_C2.1` | 2272 | 0 | 0 | 20 | à faire |
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
| 26 | `4e_C6.2` | 1990 | 6 | 25 | 18 | à faire |
| 27 | `3e_C9.1` | 1597 | 1 | 33 | 11 | à faire |
| 28 | `3e_C7.1` | 3512 | 1 | 20 | 12 | à faire |
| 29 | `5e_C5.1` | 1109 | 1 | 30 | 4 | à faire |
| 30 | `4e_C4.7` | 2022 | 1 | 40 | 7 | à faire |
| 31 | `5e_C4.7` | 1807 | 1 | 35 | 6 | à faire |
| 32 | `3e_C7.3` | 1796 | 0 | 0 | 29 | à faire |
| 33 | `3e_C7.4` | 1220 | 0 | 0 | 27 | à faire |
| 34 | `3e_C7.5` | 1439 | 0 | 0 | 26 | à faire |
| 35 | `3e_C7.7` | 1959 | 0 | 0 | 24 | à faire |
| 36 | `3e_C7.8` | 1530 | 0 | 0 | 21 | à faire |
| 37 | `3e_C8.1` | 1888 | 0 | 0 | 23 | à faire |
| 38 | `3e_C8.2` | 1414 | 0 | 0 | 28 | à faire |
| 39 | `3e_C9.2` | 2597 | 2 | 62 | 48 | à faire |
| 40 | `4e_C7.1` | 1780 | 2 | 22 | 28 | à faire |
| 41 | `4e_C7.3` | 1866 | 5 | 13 | 27 | à faire |
| 42 | `4e_C7.4` | 1582 | 5 | 22 | 23 | à faire |
| 43 | `4e_C7.5` | 2077 | 5 | 23 | 25 | à faire |
| 44 | `4e_C7.7` | 1831 | 5 | 16 | 19 | à faire |
| 45 | `4e_C7.8` | 1880 | 5 | 19 | 15 | à faire |
| 46 | `4e_C8.1` | 1975 | 1 | 25 | 22 | à faire |
| 47 | `4e_C9.1` | 2909 | 1 | 54 | 34 | à faire |
| 48 | `5e_C7.1` | 1685 | 1 | 17 | 17 | à faire |
| 49 | `5e_C7.3` | 1694 | 5 | 15 | 15 | à faire |
| 50 | `5e_C7.4` | 1607 | 5 | 18 | 16 | à faire |
| 51 | `5e_C7.5` | 1528 | 5 | 22 | 8 | à faire |
| 52 | `5e_C8.1` | 1421 | 5 | 17 | 13 | à faire |
| 53 | `5e_C8.2` | 1412 | 5 | 16 | 12 | à faire |
| 54 | `5e_C9.1` | 1761 | 1 | 24 | 5 | à faire |
| 55 | `3e_C1.1` | 1451 | 0 | 0 | 23 | à faire |
| 56 | `3e_C3.1` | 1939 | 0 | 0 | 19 | à faire |

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
