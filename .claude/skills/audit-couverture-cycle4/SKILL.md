---
name: audit-couverture-cycle4
description: Mettre à jour la matrice de couverture des 114 codes du référentiel technologie cycle 4 (programme 2024). À utiliser au début de chaque session de travail sur le dépôt, et après chaque lot terminé, pour resynchroniser audit_couverture.csv/.json et les statuts.
---

# Audit de couverture cycle 4

## Mission (unique)

Maintenir à jour l'état de couverture des 114 codes : fichiers réellement
présents, qualité pédagogique, anomalies, statut.

## Procédure

1. Lire `AUDIT_COUVERTURE_PEDAGOGIQUE.md`, `FEUILLE_DE_ROUTE_COMPLETION.md`,
   `JOURNAL_DES_DECISIONS.md` et le dernier `manifest.json` de lot.
2. Mettre à jour le dictionnaire `OVERLAY` de `_outils/build_audit.py`
   (observations qualitatives, nouveaux statuts) — jamais le CSV à la main.
3. Exécuter `python3 _outils/build_audit.py` (vérifier : « 114 codes écrits »).
4. Reporter tout changement de statut dans `JOURNAL_DES_DECISIONS.md`.

## Statuts autorisés (exclusivement)

`COMPLET ET VALIDABLE` · `EXISTANT À AMÉLIORER` · `PARTIEL` · `À CRÉER` ·
`À CORRIGER` · `LIEN CASSÉ` · `DOUBLON` · `COUVERT PAR UNE SÉQUENCE MUTUALISÉE` ·
`À VÉRIFIER PAR L'ENSEIGNANT`

## Règles

- Un dossier ne contenant qu'un README, une image ou un QCM isolé n'est JAMAIS
  `COMPLET ET VALIDABLE`.
- Un code validé ne repasse jamais en arrière pour raison cosmétique.
- Toute mutualisation exige un README pointeur dans chaque code couvert.

## Critères de réussite

- Le script s'exécute sans erreur et affiche exactement 114 codes.
- `git diff audit_couverture.csv` ne montre que les changements attendus.
- Chaque changement de statut a une entrée de journal.
