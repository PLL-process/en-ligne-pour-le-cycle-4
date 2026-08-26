# Fiche pédagogique — 4e_C8 Valider une solution technique

**Objet-fil** : jardin connecté (suite du LOT 01)  
**Ancrage territorial** : **New York** (school garden / rooftop)  
**Codes** : 4e_C8.1 · 4e_C8.2 · 4e_C8.3  
**Durée** : 3 × 55 min  
**Domaines du socle** : D2 · D3 · D4 · D5

## Intention
Faire passer l’élève de « j’ai conçu » à « je sais prouver que ça marche » par un protocole de test simple, une analyse de résultats et une proposition d’amélioration — contraintes locales : gel, pluie, vent urbain.

## Versions A/B/C
- **A** : tests réels sur maquette (très basse tension uniquement)
- **B** : simulation + tableau de résultats fourni
- **C** : purement papier (protocole + analyse de données fictives)

## Points de vigilance
- Ne jamais brancher sur le secteur 230 V
- Critères de réussite explicités avant les tests
- Décision de validation collective argumentée
- Critères NY : gel, vent de canyon, pluie, variations saisonnières

## Évaluation LSU
Production d’équipe (protocole + tableau de résultats + décision + améliorations) + auto-positionnement.

## Harmonisation du 26 août 2026

Le lot a reçu les dispositifs communs du dépôt : billet d'entrée hors progression, mode
essentiel, tableau de bord des six activités, versions étayées, durées à la convention,
carte de référentiel recopiant le programme au mot près, sélecteur de parcours 🅰/🅱/🅲
réellement agissant, et une barre de progression qui suit les validations. Contrôle
mécanisé : **cinq manquements → zéro**. Suite committée : **41 tests, tous verts**.

**Le défaut le plus grave n'était pas là.** Les 28 bonnes réponses du QCM étaient toutes
en position B : un élève qui clique la deuxième proposition à chaque question obtenait
28/28 sans rien savoir. Les propositions ont été redistribuées (7 par position) par
`repartir_qcm.mjs`, dont la suite de positions est écrite en clair — reproductible, pas
tirée au hasard. Le détail est dans le rapport de tests.
