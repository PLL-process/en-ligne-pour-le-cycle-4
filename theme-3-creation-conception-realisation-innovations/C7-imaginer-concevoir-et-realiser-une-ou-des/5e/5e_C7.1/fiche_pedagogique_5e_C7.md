# Fiche pédagogique — 5e mini-projet objet scolaire

**Codes** : 5e_C7 (principal) · 5e_C8 · 5e_C9 (mutualisés)  
**Ancrage** : New York — indicateur de place (hall)  
**Durée** : 6 × 55 min  
**Socle** : D2 · D3 · D4 · D5

## Intention
Chaîne C7→C8→C9 accessible en 5e.

## Versions B/C
B simulation · C papier.

La version 🅰 (maquette TBT) a été **retirée le 05/10/2026** : l'éditeur Python ne pilote aucune carte. Elle pourra revenir avec la future version carte réelle, en interface Arduino (voir `JOURNAL_DES_DECISIONS.md`).

## Sécurité
Très basse tension uniquement.

## Harmonisation du 26 août 2026

Dispositifs communs du dépôt installés — billet d'entrée hors progression, mode essentiel,
tableau de bord des six activités, versions étayées, durées à la convention, sélecteur de
parcours 🅱/🅲 réellement agissant, barre de progression reliée aux validations.
Contrôle mécanisé : **quatre manquements → zéro**. Suite committée : **37 tests, tous verts**
(`node tests_5e_C7.mjs .`).

**Le QCM avait ses 24 bonnes réponses toutes en position B** : cliquer la deuxième
proposition à chaque question donnait 24/24 sans rien savoir. Elles sont redistribuées sur
les quatre positions (outil `repartir_qcm.mjs`, dans `4e/4e_C7.1/`). Le QCM reste de la
génération ancienne — 24 questions, sans réfutation par distracteur : la mise à niveau au
standard des lots C9 n'est pas faite, et c'est dit plutôt que sous-entendu.

## Découpage en séances à onglets (04/11/2026, vague n°311, sur le modèle du pilote 4e_C8.1)

La page était d'un seul tenant. Elle a maintenant trois séances à onglets ; les blocs ont été déplacés, pas réécrits.

| Séance | Question directrice | Contenu | Temps |
|---|---|---|---|
| 1 — Faire, puis imaginer | Comment un voyant peut-il savoir qu'une case est occupée, et quelles solutions imaginer pour le construire ? | Ouverture (situation, problématique, idée de départ, billet, contrat, deux façons), activité 0 (simulateur de place), activité 1 (planning, deux solutions, choix) | ouverture + 10 + 30 min |
| 2 — Valider, puis programmer | Le voyant fait-il ce qu'on attend, et comment écrire la règle qui le commande ? | Activité 2 (grille de validation), les quatre gestes de Vittascience, activité 3 (algorigramme, puis programme) | 25 + 30 min |
| 3 — Refaire, conclure | La même règle SI marche-t-elle sur un autre objet ? | Réinvestissement (casier de bibliothèque), synthèse, Bonus (un corrigé replié par défi), bilan (retour à l'idée de départ, « Comment j'ai travaillé », « Je me positionne » sur 5e_C7.1, C8.3 et C9.3 aux quatre niveaux du livret), TP « Le dé », atelier de planification, renvoi au QCM | 15 min + clôture |

Dès la séance 2, l'ouverture est repliée dans le volet « 📖 Rappel » (règle d'or n°311). Restent dehors, parce qu'ils servent à
chaque séance : la mission, l'identité, la barre d'outils, le sélecteur de parcours et ses deux notes, la progression et
« 🗺 Où j'en suis ». Le simulateur de place sert aux séances 1 et 2 (activités 0 et 2) : un seul exemplaire, que la page range
dans la séance ouverte, sous son en-tête. Sans JavaScript, les trois séances s'affichent à la suite.
