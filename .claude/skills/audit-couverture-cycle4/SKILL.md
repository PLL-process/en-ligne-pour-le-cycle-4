---
name: audit-couverture-cycle4
description: Mettre à jour la matrice de couverture des 114 codes du référentiel technologie cycle 4 (programme 2024). À utiliser au début de chaque session de travail sur le dépôt, et après chaque lot terminé, pour resynchroniser audit_couverture.csv/.json et les statuts.
---

# Audit de couverture cycle 4

Mis à jour le 23/10/2026 (inventaire des skills) : aligné sur le journal jusqu'à la règle d'or n°311.

## Mission (unique)

Maintenir à jour l'état de couverture des 114 codes : fichiers réellement
présents, preuve de couverture, anomalies, statut.

## Sources à lire

- `JOURNAL_DES_DECISIONS.md` : il fait foi (règle d'or n°10). Lire les entrées depuis la dernière
  resynchronisation.
- Le `manifest_*.json` du lot qui vient d'être livré.
- Le relevé de `python3 _outils/controle_couverture.py --muets` (voir plus bas).

Ne pas partir de `AUDIT_COUVERTURE_PEDAGOGIQUE.md` ni de `FEUILLE_DE_ROUTE_COMPLETION.md` : figés
en juillet 2026. La feuille de route dit encore « ChatGPT seul autorisé à pousser », contredit par
la règle n°5 amendée (30/07/2026 : Fable pousse ses branches et ouvre ses PR ; la fusion reste à
Pascal).

## Procédure

1. Relevé de départ : `python3 _outils/controle_couverture.py --muets`.
2. Mettre à jour le dictionnaire `OVERLAY` de `_outils/build_audit.py` (statut, `mutualise_avec`,
   qualité, anomalies) — jamais le CSV à la main. Écrire « À VÉRIFIER PAR L’ENSEIGNANT » avec
   l'apostrophe typographique `’`, comme `build_audit.py`, `controle_statut.py` et `make_index.py`.
3. Pointeurs : `python3 _outils/pointeurs_codes.py --etat` liste les README à écrire ; sans
   `--etat`, il les écrit (table `POINTEURS`, cible vérifiée sur le disque).
4. Régénérer, dans cet ordre, sur un arbre à jour de `main` :
   `python3 _outils/build_audit.py` (vérifier « 114 codes écrits »), puis `python3 _outils/make_index.py`.
5. Lire le bloc « Contrôle de statut — N code(s) recalé(s) » de `build_audit.py`, puis relancer
   `controle_couverture.py --muets`.
6. Reporter tout changement de statut dans `JOURNAL_DES_DECISIONS.md`.

## Fichiers engendrés

`audit_couverture.csv`, `audit_couverture.json`, `index.html` et `README.md` (racine) ne s'éditent
jamais à la main et ne se fusionnent jamais à la main. En cas de conflit : prendre n'importe quelle
version, puis régénérer (`_outils/METHODE.md`, pilier 2).

## Les contrôles

- `_outils/controle_statut.py` (n°190, 28/08/2026) : appelé par `build_audit.py`. Un code qui
  revendique `COMPLET ET VALIDABLE` doit montrer six pièces : séquence, QCM au gabarit maison
  (≥ 10 questions dans `const QUESTIONS`), fiche pédagogique, matrice, synthèses, rapport de tests.
  Sinon il passe en `COUVERT PAR UNE SÉQUENCE MUTUALISÉE` (s'il porte `mutualise_avec`) ou en
  `À VÉRIFIER PAR L’ENSEIGNANT` ; la colonne `preuves_manquantes` dit pourquoi. Il ne promeut jamais.
- `_outils/controle_couverture.py` (n°237-238, 31/08/2026) : où le lot nomme-t-il son propre code ?
  États ÉVALUÉ (≥ 5 questions du code), PARTAGÉ, CITÉ, RENVOI, NON NOMMÉ, VIDE. Il lit aussi
  `COMP_LABELS`, où les banques rattachent leurs étiquettes de groupe aux codes (n°242). Diagnostic
  seulement : sortie toujours 0. Options : `--muets`, `--json <fichier>`.
- `_outils/pointeurs_codes.py` : écrit le README pointeur d'un code mutualisé (formulation
  officielle, où le code est travaillé, ce que la cible en fait). Il refuse si la promesse
  « évalué » ne correspond pas aux questions réellement présentes, et n'écrase jamais un dossier
  qui porte son propre lot.

## Statuts autorisés (exclusivement)

`COMPLET ET VALIDABLE` · `EXISTANT À AMÉLIORER` · `PARTIEL` · `À CRÉER` ·
`À CORRIGER` · `LIEN CASSÉ` · `DOUBLON` · `COUVERT PAR UNE SÉQUENCE MUTUALISÉE` ·
`À VÉRIFIER PAR L’ENSEIGNANT`

## Règles

- Un dossier ne contenant qu'un README, une image ou un QCM isolé n'est JAMAIS
  `COMPLET ET VALIDABLE`.
- Un code validé ne repasse jamais en arrière pour raison cosmétique.
- Toute mutualisation exige un README pointeur dans chaque code couvert (`pointeurs_codes.py`).
- Un statut qu'aucun contrôle ne peut retirer n'est pas un statut (n°190, 28/08/2026).
- Compter les pièces n'est pas vérifier la couverture ; la preuve est une ligne : une question
  étiquetée par le code dans la banque, ou une ligne de matrice notion → code → production →
  questions (n°237-238, 31/08/2026). `controle_statut.py` ne l'exige pas encore (journal,
  31/08/2026) : lire le relevé de `controle_couverture.py`.
- Matrice de lot : colonnes normalisées — code avec niveau, verbe officiel, activité, production
  attendue, questions de QCM, niveau cognitif, socle, CRCN, critère de réussite ; la colonne
  production montre où l'élève conçoit seul (n°124, 21/08/2026). Aucun outil ne la contrôle, et
  aucune des 57 matrices de lot ne porte encore toutes ces colonnes (constat du 23/10/2026).

## Critères de réussite

- `build_audit.py` s'exécute sans erreur et écrit exactement 114 codes.
- `git diff audit_couverture.csv` ne montre que les changements attendus.
- Le relevé de `controle_couverture.py` garde à 0 ses trois listes : codes tenus pour complets sans
  preuve par des questions, dossiers muets, renvois que rien n'évalue — ou chaque exception est
  expliquée dans le journal.
- Chaque changement de statut a une entrée de journal.
