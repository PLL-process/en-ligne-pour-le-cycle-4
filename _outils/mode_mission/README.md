# Mode mission — un exercice à la fois

Décision de Pascal du 11/11/2026 (voir `docs/mode-mission/PLAN.md` et le journal).

Le mode mission est une **seconde vue de la même page**. Il n'invente aucun exercice : il montre ceux de la
séquence, un écran à la fois, avec une barre d'étapes et trois boutons — Précédent · Vérifier · Suivant.

## Ce que le bloc fait

- **Découpe** chaque séance en écrans : la séance (et la situation de départ) ; pour chaque activité l'atelier
  incrusté, le départ (objectif, ressources, consigne), puis **une question par écran**, puis « je retiens »
  (correction, erreurs fréquentes, à retenir, critère) ; enfin chaque autre carte (synthèse, Bonus, bilan, QCM).
- **Habille** une grille de boutons radio (`.qcm-cles` + `fieldset.qcm-grille`) en **étiquettes à poser** : on
  touche l'étiquette puis sa case, on la glisse, ou on fait les deux au clavier. Poser une étiquette coche le
  bouton radio de la page : la sauvegarde, la vérification et l'impression de la page ne voient aucune différence.
- **Vérifie** chaque écran avec les réponses que la page porte déjà. Cinq écritures sont lues : `const att =
  {id:"texte"}` (ou `attendu`, ou `ATTENDUS = {1:{id:"texte"}, 2:{…}}`, une table par activité) ;
  `$("id").value === "texte"` ; `$("id").value.startsWith("début")` (ou `.indexOf("début") === 0`) ;
  `sv("id", "texte")` (l'ancien gabarit) ; `<fieldset data-bonne="texte">`, la réponse écrite sur la question
  elle-même (Book Train). Une question est un groupe de boutons radio, ou une liste déroulante
  qui pose une question (les pages pas encore révisées ; une liste d'interface, `data-interface`, n'en est pas une).
  Une réponse n'est retenue que si elle désigne **une** proposition de la question, et une seule ; au moindre
  doute, l'écran ne se vérifie pas ici (la page le vérifie toujours, à la fin de l'activité).
  Les réponses justes restent, les étiquettes fausses retournent dans la réserve. La dernière question d'une
  activité lance la vérification de la page : c'est elle qui valide l'activité (verrous, justification écrite,
  atelier réussi).
- **Décourage le tâtonnement** : les erreurs se comptent réponse par réponse et font les étoiles (3 sans erreur ;
  2 avec une erreur, deux sur un jeu de trois réponses ou plus ; 1 au-delà) ; après une erreur, « Vérifier » souffle
  deux secondes ; au deuxième essai manqué sur le même écran, le coup de pouce de l'activité (`details.aide1`,
  ou le premier `details.aide`) s'ouvre sous le message, au quatrième le second. Ouvrir une aide ne retire rien.
- **Garde** sur l'appareil le mode, l'écran en cours, les erreurs et les étoiles (`localStorage`, clé
  `mission:<page>`) ; « Effacer ma sauvegarde » les efface aussi. La barre affiche les étoiles de la séance, le
  bilan celles de la séquence et les erreurs corrigées en route.
- **Montre chaque écran depuis son début**, même quand l'élève avait défilé dans le précédent. Dans une séquence
  découpée en pages, qui passe à la page suivante en mission y arrive en mission.

## Ce qu'il ne fait pas

- Rien tant que l'élève n'a pas appuyé sur « 🎮 Mode mission » : la page s'ouvre comme avant, et son contenu n'est
  pas touché. Le bouton est dans le cadre « Ma progression » ; quand la page n'a pas ce cadre, il est juste
  au-dessus des onglets des séances — jamais dans la barre d'outils, jamais entre les onglets et leur séance. « 📄 Page complète », dans la barre de la mission, y ramène.
  Les contrôles et les bancs du dépôt mesurent et jouent donc la page qui défile.
- Rien à l'impression : tout ce qui cache est sous `@media screen`. La fiche papier sort entière.
- Il ne bloque jamais « Suivant », ne chronomètre rien, ne classe personne.

## Fichiers

| Fichier | Rôle |
|---|---|
| `mission.css`, `mission.js` | la source unique |
| `poser.py` | pose ou met à jour le bloc dans une page (`--verifier` : ne rien écrire) |
| `banc_mission.mjs` | joue le pilote comme un élève, à 390 px et à 1 180 px (25 tests par largeur) |
| `banc_generique.mjs` | joue **toute** page qui porte le bloc, écran par écran (`--detail` : la liste des écrans) |
| `enrichir.py` | écrit dans une page le pourquoi des erreurs et les réponses leurres, depuis `mission_<lot>.json` |
| `../controle_mode_mission.py` | le bloc d'une page est celui de la source, une fois |

## Poser le mode mission sur une séquence

```bash
python3 _outils/mode_mission/poser.py <sequence.html>
node _outils/mode_mission/banc_generique.mjs <sequence.html> --detail
python3 _outils/controle_mode_mission.py
```

Une page **engendrée** ne se retouche pas à la main : c'est son générateur qui pose le bloc, comme il pose la fiche
papier (`3e_C9.2/generer_les_quatre_pages.py`). Une page engendrée sans `</head>` le reçoit juste avant `<body>`.

Le banc générique entre en mission, parcourt chaque séance par « Suivant », répond juste à chaque écran qui se
vérifie, puis revient à la page complète. Il **refuse** : une erreur JavaScript, un écran vide, un défilement de
côté à 390 px, un écran qui n'accepte pas les bonnes réponses, un bouton de vérification de la page laissé visible
dans un écran de question, un écran suivant qui ne se montre pas depuis son début (le banc descend en bas de chaque
écran avant d'appuyer sur « Suivant »), une page complète mal rétablie — et **une réponse retenue par le mode qui
ne vaut pas un point à la vérification de la page** (chaque réponse lue est rejouée contre `CHECKS` ; sans
`CHECKS`, contre les marques que la page pose). Avec `--detail`, lire la
liste des écrans : le découpage doit avoir du sens pour un élève.

Ce que le découpage reconnaît. D'abord **les séances**, écrites de trois façons dans le dépôt :

| Les séances | Où | Ce que le moteur en fait |
|---|---|---|
| `.seance-panel`, ouvert par son `.seance-tab[data-panel]` | gabarit commun | suit l'onglet ouvert |
| `section.panneau[role=tabpanel]`, ouvert par `[role=tab][aria-controls]` | `4e_C4.1_book-train` | suit l'onglet ouvert ; ses cartes sont des `div.carte` |
| des `.seance-bloc` à la suite, tous visibles | une page sans onglets (les quatre pages « station » de `3e_C9.2`) | n'en montre qu'un à la fois, mène de l'un à l'autre ; au dernier écran, le lien « Page suivante » se montre, et la page suivante s'ouvre en mission |

Ensuite **les activités**. Une activité est le bloc qui porte un exercice et son bouton de vérification
(`button[data-check]`, ou `button.verif[data-exo="x"]` qui désigne sa zone `#x` et son message `#res-x`). Trois formes :

| Forme | Où | Ce que le moteur en fait |
|---|---|---|
| `.activite` dans une carte | gabarit commun (thème 2, séquences révisées) | une ou plusieurs zones `.exo`, leurs parties en `h4` ; la vérification dans la zone, ou après les aides |
| la carte **est** l'activité (`section.card`) | thèmes 1 et 3, gabarit « atelier » (`3e_C4.8`, `3e_C6.2`) | sa zone `.exo` si elle porte la vérification ; sinon la zone va de la première question à la vérification |
| `.act` posées à la suite dans une carte | ancien gabarit (famille C7/C8) | même règle : de la première question à la vérification, les aides à part |

- Une zone qui porte **deux boutons de vérification** est coupée en deux : chaque bouton clôt ses questions.
- Des réponses courtes qui se suivent (`qcm-rangee`, `qcm-court`) tiennent sur un même écran ; un tableau de
  questions (`qcm-cellule`) aussi.
- Un exercice incrusté avant la zone (`.atelier-incruste`, `details.incruste-repliee`) a son écran.
- Un outil posé entre la dernière zone et sa vérification (l'éditeur Python où l'on prouve, un écrit) a son écran,
  « Avant de vérifier », après la dernière question : c'est là que la vérification de la page parle.
- Une activité sans zone d'exercice (un Bonus replié) et toute autre carte : un écran, tels quels.
- En tête de séance, un lien seul, sans titre ni question (« 📖 Les mots de cette séance »), n'a pas d'écran : il
  accompagne le premier.
- Un bloc que la page cache n'a pas d'écran ; un écran qui serait vide est sauté.

Une page qui n'a aucune de ces trois formes de séances reste telle quelle (le bouton n'apparaît pas). Sans réponse lisible, un écran ne se
vérifie pas seul : la vérification de la page joue à la dernière question de l'activité.

Pour savoir où en est chaque séquence (écrans, écrans vérifiés par le mode, vérifications de la page) :
`node _outils/mode_mission/banc_generique.mjs` sans argument joue toutes les pages qui portent le bloc.

## Le pourquoi des erreurs et les leurres (contenu, séquence par séquence)

Un retour qui explique l'erreur aide bien plus qu'un « juste / faux », et une grille qui a autant de réponses que
de lignes donne la dernière (rapport du 11/11/2026). Ce contenu s'écrit dans `mission_<lot>.json`, à côté de la
séquence — modèle : `5e_C4.1/mission_5e_C4.1.json` — puis :

```bash
python3 _outils/mode_mission/enrichir.py <sequence.html> <mission_<lot>.json>      # --verifier : dit si la page est à jour
```

| Clé | Ce qu'on écrit | Où cela va | Ce que voit l'élève en mission |
|---|---|---|---|
| `pourquoi` | par question à choix, pour chaque **mauvaise** proposition : pourquoi elle ne convient pas | `data-pourquoi` sur le bouton radio | « Pas encore. Le carton se ramollit dès qu'il est mouillé… » |
| `indices` | par ligne de grille ou de rangée : ce que la ligne demande | `data-indice` sur le groupe | « “le mât” ne va pas avec “Décider…”. Décider, c'est comparer… » |
| `leurres` | par grille : une ou deux réponses de trop, plausibles, qui ne vont avec aucune ligne | la légende et chaque ligne, relettrées ; le titre le dit | deux étiquettes restent dans la réserve (« attention, 2 en trop ») |

Règles d'écriture : une phrase, vingt mots au plus, le vocabulaire de la séance ; **jamais la bonne réponse**, ni
celle d'une autre question de la séquence ; pour une observation au simulateur, renvoyer à l'expérience. Un leurre
change aussi la page qui défile et la fiche papier : compléter la correction (« deux réponses ne servent à aucune
ligne : … ») et remesurer la séance (`mesurer_charge.mjs`). Le banc générique refuse un « pourquoi » posé sur une
bonne réponse et dit combien de mauvaises réponses ont le leur.

## Limites connues (pilote)

- Les séries de numéros à ordonner et les textes à trous ne sont pas encore habillés (ils restent des boutons radio).
- Un lien vers une ancre (`#act3`) ouvre la bonne séance, pas le bon écran.
- Essayé sur une vraie tablette par Pascal le 11/11/2026 (« c'est bon ») ; pas encore en classe. Au doigt, une étiquette
  se glisse depuis la réserve ; une case ne se glisse pas (la page défile) : on la touche pour reprendre l'étiquette.
- **Une carte par écran, sans vérification par le mode** : `3e_C1.5`, `4e_C1.4`, `5e_C1.3`. Ces trois pages du
  thème 1 n'ont pas de vérification par activité : glisser-déposer et blocs de questions propres à la page, une
  seule vérification par section, des corrections à déplier. Les découper par titres séparerait les questions de
  leur seul bouton « Vérifier » : elles demandent d'abord d'être ramenées au squelette commun.
- Sur `4e_C4.1_book-train`, une étiquette retournée dans la réserve reste dans la sauvegarde de la page : rechargée,
  la page la montre de nouveau posée (non vérifiée). La page n'a pas de moyen d'effacer une réponse.
- Leurres et « pourquoi » : écrits pour le pilote (`5e_C4.1`), les neuf séquences du premier lot (`5e_C6.1`, `4e_C4.1`,
  `4e_C5.1`, `4e_C6.1`, `3e_C4.1`, `3e_C4.3`, `3e_C4.7`, `3e_C5.1`, `3e_C6.1`) et `3e_C9.1` ; ailleurs, le
  message d'erreur reste général. Les « pourquoi » ne se voient qu'en mode mission : la page qui défile garde sa correction complète.
- Une liste déroulante n'a pas de « pourquoi » par proposition (`enrichir.py` écrit sur des boutons radio) : ce
  contenu vient avec la révision de la page, quand ses listes deviennent des boutons radio (n°300).
