# Fiche pédagogique — 4e_C7 Jardin connecté (conception)

**Codes** : 4e_C7.1 · C7.2 · C7.3  
**Ancrage** : New York — school garden / rooftop  
**Durée** : 4 × 55 min  
**Socle** : D2 · D3 · D4 · D5

## Intention
Imaginer, organiser et choisir une solution technique simple (support capteur, abri, indicateur) sous contraintes NY (gel, pluie, vent, réemploi).

## CRCN règle 7 (voir aussi `CRCN_regle7.md`)

| Compétence | Niveau | Action observable | Trace |
|---|---|---|---|
| 3.1 Documents textuels | 2 | Planning + choix justifié | Tableau tâches + paragraphe |
| 1.2 Gérer des données | 1–2 | Sauvegarder / reprendre identité & hypothèse | localStorage ou export |

**3.4 Programmer** → reporté volontairement en **4e_C9** (même objet-fil).

## Versions A/B/C
A maquette TBT · B simulation · C papier

## Sécurité
Très basse tension uniquement ; secteur 230 V interdit.

## Évaluation
Planning · 2 solutions · tableau matériaux · QCM · auto-positionnement

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
