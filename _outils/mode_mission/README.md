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
- **Vérifie** chaque écran avec les réponses que la page porte déjà dans ses vérifications. Trois écritures sont
  lues : `const att = {id:"texte"}` (ou `attendu`), `$("id").value === "texte"`, `$("id").value.startsWith("début")`
  (ou `.indexOf("début") === 0`). Une réponse n'est retenue que si elle désigne **une** proposition du groupe, et une
  seule ; au moindre doute, l'écran ne se vérifie pas ici (la page le vérifie toujours, à la fin de l'activité).
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

## Ce qu'il ne fait pas

- Rien tant que l'élève n'a pas appuyé sur « 🎮 Mode mission » (dans le cadre « Ma progression ») : la page s'ouvre
  comme avant, et son contenu n'est pas touché. « 📄 Page complète », dans la barre de la mission, y ramène.
  Les contrôles et les bancs du dépôt mesurent et jouent donc la page qui défile.
- Rien à l'impression : tout ce qui cache est sous `@media screen`. La fiche papier sort entière.
- Il ne bloque jamais « Suivant », ne chronomètre rien, ne classe personne.

## Fichiers

| Fichier | Rôle |
|---|---|
| `mission.css`, `mission.js` | la source unique |
| `poser.py` | pose ou met à jour le bloc dans une page (`--verifier` : ne rien écrire) |
| `banc_mission.mjs` | joue le pilote comme un élève, à 390 px et à 1 180 px (22 tests par largeur) |
| `banc_generique.mjs` | joue **toute** page qui porte le bloc, écran par écran (`--detail` : la liste des écrans) |
| `enrichir.py` | écrit dans une page le pourquoi des erreurs et les réponses leurres, depuis `mission_<lot>.json` |
| `../controle_mode_mission.py` | le bloc d'une page est celui de la source, une fois |

## Poser le mode mission sur une séquence

```bash
python3 _outils/mode_mission/poser.py <sequence.html>
node _outils/mode_mission/banc_generique.mjs <sequence.html> --detail
python3 _outils/controle_mode_mission.py
```

Le banc générique entre en mission, parcourt chaque séance par « Suivant », répond juste à chaque écran qui se
vérifie, puis revient à la page complète. Il **refuse** : une erreur JavaScript, un écran vide, un défilement de
côté à 390 px, un écran qui n'accepte pas les bonnes réponses, un bouton de vérification de la page laissé visible
dans un écran de question, une page complète mal rétablie — et **une réponse retenue par le mode qui ne vaut pas un
point à la vérification de la page** (chaque réponse lue est rejouée contre `CHECKS`). Avec `--detail`, lire la
liste des écrans : le découpage doit avoir du sens pour un élève.

Ce que le découpage reconnaît (gabarit commun, `.seance-panel > section.card > .activite`) :
- une ou plusieurs zones d'exercice (`.exo`) par activité, leurs parties en `h4` ;
- le bouton de vérification (`button[data-check]`) et son message dans la zone, ou après les aides ;
- un exercice incrusté avant la zone (`.atelier-incruste`, `details.incruste-repliee`) : il a son écran ;
- une activité sans zone d'exercice (un Bonus replié) et toute autre carte : un écran, tels quels.

Une page d'un autre gabarit reste telle quelle (le bouton n'apparaît pas). Sans réponse lisible, un écran ne se
vérifie pas seul : la vérification de la page joue à la dernière question de l'activité.

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
- Non essayé sur une vraie tablette : le glisser au doigt n'a été joué qu'en simulation. Au doigt, une étiquette
  se glisse depuis la réserve ; une case ne se glisse pas (la page défile) : on la touche pour reprendre l'étiquette.
- Gabarit « atelier » (`3e_C4.8`, `3e_C6.2` : des `.ligne-exo` posées dans la carte, sans `.activite`) : non
  découpé — le mode n'y est pas posé. `4e_C4.1_book-train` : autre gabarit, non reconnu.
- Leurres et « pourquoi » : écrits pour `5e_C4.1` seulement (le modèle) ; ailleurs, le message d'erreur reste
  général. Les « pourquoi » ne se voient qu'en mode mission : la page qui défile garde sa correction complète.
