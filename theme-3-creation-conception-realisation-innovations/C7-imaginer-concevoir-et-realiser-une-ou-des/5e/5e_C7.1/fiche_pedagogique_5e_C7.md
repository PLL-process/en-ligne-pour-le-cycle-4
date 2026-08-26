# Fiche pédagogique — 5e mini-projet objet scolaire

**Codes** : 5e_C7 (principal) · 5e_C8 · 5e_C9 (mutualisés)  
**Ancrage** : New York — indicateur de place (hall)  
**Durée** : 6 × 55 min  
**Socle** : D2 · D3 · D4 · D5

## Intention
Chaîne C7→C8→C9 accessible en 5e.

## Versions A/B/C
A maquette TBT · B simulation · C papier

## Sécurité
Très basse tension uniquement.

## Harmonisation du 26 août 2026

Dispositifs communs du dépôt installés — billet d'entrée hors progression, mode essentiel,
tableau de bord des six activités, versions étayées, durées à la convention, sélecteur de
parcours 🅰/🅱/🅲 réellement agissant, barre de progression reliée aux validations.
Contrôle mécanisé : **quatre manquements → zéro**. Suite committée : **37 tests, tous verts**
(`node tests_5e_C7.mjs .`).

**Le QCM avait ses 24 bonnes réponses toutes en position B** : cliquer la deuxième
proposition à chaque question donnait 24/24 sans rien savoir. Elles sont redistribuées sur
les quatre positions (outil `repartir_qcm.mjs`, dans `4e/4e_C7.1/`). Le QCM reste de la
génération ancienne — 24 questions, sans réfutation par distracteur : la mise à niveau au
standard des lots C9 n'est pas faite, et c'est dit plutôt que sous-entendu.
