# 5e_C9.1 → C9.3 — Atelier « La boîte étiquetée » (Thème 3 · New York)

> **5e_C9.1** — Analyser un programme simple fourni et tester s'il répond au besoin ou au problème posé.
> **5e_C9.2** — Modifier un programme fourni pour répondre au besoin ou à un problème posé.
> **5e_C9.3** — Réaliser et mettre au point un programme simple commandant un OST.

Le compteur de places du **Cyclone de Coney Island** affiche « 87 places libres » pour un
train de 24 sièges. Le programme est fourni, il est court, et il tourne sans planter :
c'est en le **lisant** et en le **testant** qu'on découvre qu'il ne répond pas au besoin.
Première marche de l'**arc variables** du cycle (5e → 4e → 3e).

## Ressources

* **`sequence_5e_C9.1-C9.3_boite_etiquetee.html`** — l'atelier complet (3 séances, 5 activités) :
  simulateur de mémoire pas à pas, motif **prédire → tester → reporter** dans l'éditeur Python
  Vittascience embarqué, banc de tests du programme **fourni** (le bug des descendus), modification
  ciblée puis barrière commandée avec son **cas frontière** (zéro place pile).
  Sauvegarde locale, DYS, verrous expérientiels.
* **`qcm_5e_C9.1-C9.3_boite_etiquetee.html`** — QCM 30 questions (boîte / lire / modifier),
  réfutation de chaque distracteur, 3 illustrées.
* **`Synthèses/`** — synthèse élève (imprimable A4) et synthèse professeur.
* **`tests_5e_C9.1-C9.3.mjs`** — la suite Playwright du lot, **rejouable** :
  `node tests_5e_C9.1-C9.3.mjs .` (44 tests ; ce qui n'est PAS testé est écrit dans le rapport).
* **`fiche_pedagogique_5e_C9.1-C9.3.md`**, **`matrice_couverture_5e_C9.1-C9.3.csv`**,
  **`SOURCES_MEDIAS.md`**, **`rapport_tests_5e_C9.1-C9.3.md`**.

`5e_C9.2/` et `5e_C9.3/` ne portent qu'un README pointeur : les deux codes sont travaillés
dans l'activité 5 de cet atelier — ① modifier le programme fourni, ② commander la barrière.

## Harmonisation du 26 août 2026

Le lot a reçu les dispositifs communs du dépôt qui lui manquaient : billet d'entrée hors
progression, mode essentiel, tableau de bord des cinq activités, versions étayées, durées à la
convention, **carte de référentiel** recopiant le programme au mot près, sélecteur de parcours
réellement agissant, et boutons de séance suivante. Le contrôle mécanisé passe de quatre
manquements à **zéro**.

Ce README lui-même a été réécrit : il annonçait encore « COUVERT — mutualisé dans le
mini-projet Thème 3 », état antérieur à la création de l'atelier. Un lecteur qui arrivait ici
était renvoyé ailleurs alors que la ressource était sous ses yeux.
