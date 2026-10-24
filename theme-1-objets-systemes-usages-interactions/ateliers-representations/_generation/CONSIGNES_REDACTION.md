# Rédiger un atelier de représentation — consignes communes

Ce document fixe la forme des fichiers `donnees_<module>.py` et `q_<module>.py`. Le modèle à suivre,
ligne à ligne, est l'atelier pilote : `donnees_interacteurs.py` et `q_interacteurs.py`.

## Ce qu'on écrit, et ce qu'on ne touche pas

- On écrit **seulement** `donnees_<module>.py` et `q_<module>.py`. Un dessin propre à l'atelier
  (scène, croquis) s'écrit dans `donnees_<module>.py`, avec les aides de `figures.py` (`svg`, `texte`,
  `fleche_def`, `e`).
- On ne modifie jamais le moteur : `moteur.py`, `kit.js`, `kit.css`, `figures.py`, `dessins.py`,
  `build.py`, `build_qcm.py`, `syntheses.py`, `cahiers.py`, `qbanque.py`, `gabarit_qcm.html`.
  Un manque du moteur se signale, il ne se contourne pas.
- On assemble avec `python3 build.py <module>` puis `python3 build_qcm.py <module>` (jamais `build.py`
  sans argument : il réécrit les cahiers communs).

## Les constantes du module de données

`SLUG`, `COURT` (2 lettres, unique), `EMOJI`, `TITRE` (le mot du programme), `TITRE_COURT`,
`TITRE_COMPLET`, `ETIQUETTE`, `ETIQUETTE_COURTE`, `MENTION_FICTION`, `NIVEAUX`, `MODULE`,
`NOM_PANNEAU`, `PANNEAU_TEXTE`, `IMAGES`, `SCHEMAS_SYNTHESE`, `VOCAB_EN`, `VERBES`, `CHAINE`,
`NOTES_PROF`, `DEUX_NOMS`, `QCM_SOUS_TITRE`. Voir le pilote pour le rôle de chacune.

**Identifiants uniques** : tout identifiant de SVG (`ident`) et toute case vivante (`vivant`,
`vivants`, `cible`) commence par `COURT` suivi d'un tiret (`bc-…`). Les cahiers de niveau mettent
tous les ateliers dans une même page : deux identifiants égaux s'y écraseraient.

## Les exercices

- 3 à 7 exercices **pour toute la représentation**, répartis sur les niveaux prévus au plan.
- Chaque exercice : `id`, `titre`, `code` (un code du référentiel, vérifié dans
  `_outils/data_competences.py`), `duree`, `objectif`, `production`, `mots` (le lexique de
  l'exercice : tout mot technique ou un peu difficile), `documents` (facultatif), `intro`
  (facultatif), `consigne`, `critere`, `widgets`, `aides` (deux), `jumeau` (après l'aide 2),
  `correction` (lignes de démonstration, la dernière en `("conclusion", …)`), `retenir`, `piege`.
- Types de questions (`widgets`) : `choix`, `cases`, `classer`, `liste`, `texte`, `slots`
  (cases d'un schéma vivant), `croquis` (dessin à l'écran, avec relecture). Les options d'un choix
  s'écrivent une par ligne : le moteur les met en colonne.
- Une page de niveau totalise 30 à 40 minutes d'exercices.

## Les règles du site, celles qui pèsent ici

- **Deux noms** : le mot du programme d'abord, le nom courant ensuite (« diagramme des interacteurs
  extérieurs, souvent appelé diagramme pieuvre »).
- **Une consigne explique les mots qu'elle emploie** (on redit dans la consigne ce qu'est un critère,
  une fonction technique…). Chaque mot difficile a aussi sa ligne dans `mots`.
- **On parle à l'élève** : « tu » pour guider, « je » dans le positionnement. Jamais « tu as fait »
  (ni l'an dernier, ni plus tôt) : l'ouverture (`avant`) nomme des compétences, avec leur code, et un
  lien pour les rattraper.
  Liens de rattrapage : `"@synthese#les-mots"`, `"@niveau:5e#<COURT>_5e_e1"` (page d'un autre niveau
  du même atelier), `"@atelier:<module>:<niv>#<ancre>"` (page d'un autre atelier).
- **Aucune trace de la fabrique** dans ce que lit l'élève : ni numéro de règle, ni « dépôt », ni nom
  d'agent, de lot, de Pascal. (Permis dans `NOTES_PROF`, `CHAINE`, `VERBES`.)
- **Correction exhaustive**, même quand tout est juste ; **mise en page de démonstration** : une idée
  par ligne, « → » entre les étapes ; chaque piège réfuté.
- **Aide 2 = le raisonnement**, suivie d'un **exercice jumeau** à valeurs différentes, avec sa correction.
- **Aucun sigle nu** : un sigle s'écrit en toutes lettres la première fois, et entre dans `mots`.
- **Fiction déclarée** : `MENTION_FICTION` dit ce qui est imaginé. Un chiffre réel se source.
- **Très basse tension** seulement ; le 230 V n'apparaît que comme danger.
- **Contextes** : Martinique (Sainte-Luce, cyclones, eau, soleil), collège, objets-fils —
  5e : vélo-cargo, lampadaire intelligent ; 4e : jardin connecté (système d'arrosage) ;
  3e : station d'alerte cyclonique.
- **Jamais la couleur seule** dans un schéma : chaque couleur est doublée d'un mot.

## Le QCM (`q_<module>.py`)

- 30 questions fixes, réparties par code comme le dit le plan ; au moins 5 par code évalué ;
  au moins 3 illustrées (images du dossier `Images/`, déclarées dans `IMAGES`).
- Chaque question : 4 propositions, **la bonne en premier** ; `expl`, `ex`, `err`, une réfutation par
  distracteur (dans le cas étudié, pas une loi générale), `ret`.
- Un distracteur est plausible ; le meilleur est **vrai mais hors sujet**.
- **La bonne réponse ne se devine pas à sa longueur** : `qbanque.Banque.fin` refuse plus de 2 bonnes
  réponses détachées (± 8 caractères) et plus de 40 % de bonnes réponses les plus longues.
- `Q = B.fin(30, {code: nombre, …})` à la fin du fichier.

## Avant de rendre

1. `python3 build.py <module>` et `python3 build_qcm.py <module>` sans erreur.
2. Depuis la racine du dépôt :
   `python3 _outils/controle_longueurs.py <dossier de l'atelier>`,
   `node _outils/verif_qcm_coherence.mjs <qcm>`,
   `python3 _outils/controle_hierarchie.py <dossier de l'atelier>`,
   `python3 _outils/controle_regles_visibles.py <dossier de l'atelier>`,
   `python3 _outils/controle_medias.py <dossier de l'atelier>`.
3. Ouvrir chaque page de niveau dans Chromium (Playwright) : zéro erreur JavaScript, pas de défilement
   horizontal à 390 px, chaque exercice vérifié une fois juste et une fois faux.
4. Regarder chaque dessin rendu (capture PNG) : aucun texte qui déborde, aucune flèche qui vise à côté.
