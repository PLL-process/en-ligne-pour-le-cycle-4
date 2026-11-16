# Veille du 16/11/2026 : le motion design

Pascal, le 16/11/2026, a partagé une liste de vingt dépôts « pour faire de Fable 5.2 un studio de motion design »,
puis : « installe la veille motion ». Le tri est au journal (même date). Deux dépôts sont retenus ; **aucun n'est
installé tel quel** : leurs idées sont réécrites dans nos outils et nos skills, comme pour la veille du 15/11.

## 1. `lottiefiles/motion-design-skill` (licence MIT, commit f9a8a04) → nos skills et une mesure

- **`sequence-pedagogique-engageante`, « Le mouvement »** : une animation dit une seule chose ; les durées (geste
  100–150 ms, apparition 200–350 ms, secousse d'erreur 300–450 ms sans rebond) ; les courbes (ce qui entre ralentit,
  ce qui sort accélère, linéaire seulement pour un mouvement continu) ; une cascade sous une demi-seconde ; un repli
  « moins de mouvement » pour chaque animation ; un bouton pour arrêter une boucle de plus de cinq secondes.
- **`chaine-energie-fonctionnelle`** : la vitesse linéaire et la même dans toutes les chaînes (1,6 s par motif) ;
  « tous les flux animés », décision de Pascal, prime sur le conseil « un tiers des éléments en mouvement au plus ».
- **`controle-qualite-lot`** : la mesure dans la liste des contrôles.
- **`_outils/controle_mouvement.py`** (banc `tests_controle_mouvement.py`, 11 / 11 ; inscrit au rapport d'audit) :
  ⚠ seulement, sortie 0.

**Mesure sur `main` (16/11/2026)** : 237 pages animées, 461 animations.
- **⚠ M1, 3 animations sans repli « moins de mouvement »** : `typing` et `blink` (le terminal de
  `4e_C1.4/activite-bonus-cyber-immersive-2fa.html`) et `glow` (`3e_C9.1/tp_mbot2_python.html`). La loupe des images
  (`loupe-ouvre`, 68 pages) ne joue que sous `prefers-reduced-motion: no-preference` : elle est son propre repli.
- **⚠ M2, 35 pages HTML dont une boucle sans fin ne s'arrête d'aucun bouton** (WCAG 2.2.2) : `vsPulse` (21, le
  gabarit Vittascience), les flux des chaînes (`flux-avance`, `cac-flux`), `del-pulse`, `buzz`, `ph-tourne`,
  `ph-courant`… S'y ajoutent **16 images SVG en boucle** (les chaînes animées) : une image ne porte pas de bouton,
  c'est la page qui l'affiche qui devrait savoir les arrêter. Toutes ont leur repli « moins de mouvement », sauf le curseur qui clignote du terminal de `4e_C1.4` : ailleurs, seul
  le bouton manque.

**Les suites** — Pascal, sur les trois questions ci-dessous : « tu as carte blanche » (16/11/2026). Elles sont
faites dans une PR à part, qui dit ses choix :
1. les trois animations sans repli : leur en donner un ;
2. un bouton « ⏸ Arrêter les animations » dans la barre d'outils des séquences, qui fige toutes les boucles de la page
   (flux compris) et se souvient du choix.

## 2. `wheresryan22/anatomy` (licence MIT © 2026 Ryan, commit 1482e84) → un pilote, à juger sur pièce

Anatomy dessine un objet technique réel en vue isométrique, en SVG, avec un petit moteur (« kit ») inclus dans la page :
aucune bibliothèque chargée, rien depuis Internet.

**Le pilote : le lampadaire de la cour (`5e_C4.1`)** — `pilote_lampadaire.build.mjs`, captures
`pilote_lampadaire_sombre.png` (700 px, « passage ») et `pilote_lampadaire_clair_390.png` (téléphone, thème clair).
- Les constituants de la séquence, nommés comme elle : panneau solaire, coffret (batterie, régulateur de charge,
  carte programmable), détecteur de mouvement (PIR), capteur de luminosité (sur la tête, à l'abri de sa propre lumière),
  tête à LED, mât, socle.
- Les trois états du simulateur de la séquence : jour (80 lux) → LED éteinte ; nuit (10 lux) → en veille, faible ;
  nuit + passage → pleine puissance. Un toucher ou les flèches font passer d'un état à l'autre, jamais tout seul ; la
  lumière s'allume en une seconde environ, et d'un coup quand l'élève a demandé « moins de mouvement ».
- Page de 85 Ko (dont 35 Ko de kit), thème sombre et clair, lisible à 390 px, aucune erreur JavaScript.

**Ce qui va, ce qui coince** :
- ✅ l'objet se reconnaît d'un coup d'œil, ses parties sont celles du cours ; la lumière au sol montre ce que fait la
  LED sans flèche ni étiquette ;
- ⚠ la méthode d'anatomy veut des figures « très détaillées » (40 à 80 pièces au moins, sans flèches ni étiquettes) :
  c'est l'inverse des schémas premium (simples, des entités qui ne se touchent pas, lisibles en 6e). Le pilote est
  volontairement sobre (une trentaine de pièces) ;
- ⚠ une figure isométrique **ne remplace pas une chaîne d'énergie** : elle montre l'objet, pas les fonctions. Sa place
  serait la situation déclenchante ou la synthèse (« une vision plus synthétique de l'objet »), à côté du schéma ;
- ⚠ le kit, inclus dans chaque page, devrait porter sa mention MIT, et la page passer nos contrôles (licence,
  atteignabilité, impression papier) avant d'entrer dans le site.

**La suite** (carte blanche, PR à part) : la refaire selon la skill `anatomy` installée par Pascal le 16/11 (même
commit audité, ses règles : pièces numérotées et nomenclature sous la carte, 40 à 80 pièces, fiche A4 fixe, mention
MIT en pied de page), puis la verser dans `5e_C4.1`.
