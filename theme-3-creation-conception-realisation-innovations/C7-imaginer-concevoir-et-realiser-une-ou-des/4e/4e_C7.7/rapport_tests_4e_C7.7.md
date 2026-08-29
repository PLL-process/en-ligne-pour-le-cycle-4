# Rapport de tests — 4e_C7.7 « Le support du capteur »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Cette page est la sortie de la dernière exécution, recopiée telle quelle —
les scripts et le jeu de réponses sont dans ce dossier, on peut tout rejouer.

```bash
node tests_4e_C7.7_sequence.mjs "$PWD/sequence_4e_C7.7_support-du-capteur.html" 4e reponses_4e_C7.7.json
node tests_4e_C7.7_qcm.mjs      "$PWD/qcm_4e_C7.7_support-du-capteur.html" 4e_C7.7 4e_C4.3 sequence_4e_C7.7_support-du-capteur.html
```

---

## 1. Séquence — **38 / 38**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ aucun verrou ouvert à l’ouverture de la page
✅ un seul atelier dans la page
✅ aucun identifiant en double
✅ « quatre supports » : 2 moyen(s) capable(s) — lu 2
✅ « quatre supports » : seconde jauge à 2 — lu 2
✅ « quatre supports » : ce sont les bons — Découpe laser CO₂ (plaque à plat) · Fraiseuse numérique 3 axes (fraise Ø 3 mm)
✅ « quatre supports » : la colonne d’état dit exactement cela — epaisseur:✔ tol:✔ traversant:✔
✅ « quatre supports » : le verdict le dit — 2 moyen(s) savent la produire : Découpe laser CO₂ (plaque à plat) · Fraiseuse nu
✅ « quatre supports » : le verrou evalue s’ouvre
✅ « trente supports » : 2 moyen(s) capable(s) — lu 2
✅ « trente supports » : seconde jauge à 1 — lu 1
✅ « trente supports » : ce sont les bons — Découpe laser CO₂ (plaque à plat) · Fraiseuse numérique 3 axes (fraise Ø 3 mm)
✅ « trente supports » : le verdict le dit — Mais pour 30 pièces, 1 d'entre eux dépassent les 3 h de machine disponibles : Fr
✅ « trente supports » : le verrou quantite s’ouvre
✅ bandeau de durée présent — ⏱ 2 séances de 55 min
✅ le bandeau annonce plus de temps que les activités n’en demandent — 110 contre 95
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ consigne de sécurité d’atelier présente
✅ le secteur est explicitement écarté
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ la formulation officielle est recopiée — Choisir les moyens et produire la forme 
✅ le code d’appui est cité — 4e_C4.3
✅ activité 0 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 1 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 2 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 3 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 4 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ le verrou fermé refuse la validation — 🔒 Change d'abord la quantité sur l'atelier (le menu « Nombr
✅ une réponse fausse est refusée — 🟡 4/5 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a3j = Je retiens ce moyen parce que son domaine contient la pièce à produire, et parce que le temps machine dont nous disposons avant la date le permet pour la série demandée. Je dis aussi ce que la machine fera de mon dessin, et ce que j'ai corrigé pour cela.
✅ l’état de l’atelier survit au rechargement — qte = 30
✅ les verrous survivent au rechargement
✅ le tableau est reconstruit au rechargement
```

## 2. QCM — **32 / 32**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ 30 questions — 30
✅ 4 options par question
✅ 3 réfutations par question
✅ la bonne réponse n’a pas de réfutation
✅ tous les champs du gabarit remplis
✅ aucune image héritée du lot voisin
✅ 30 notions distinctes — 30
✅ 20 questions sur 4e_C7.7 — {"4e_C7.7":20,"4e_C4.3":10}
✅ 10 questions sur 4e_C4.3 — {"4e_C7.7":20,"4e_C4.3":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 0.1
✅ une bonne réponse est déclarée correcte
✅ la correction déplie les trois réfutations
✅ la correction porte un « À retenir »
✅ une mauvaise réponse est déclarée incorrecte
✅ valider sans réponse n’ouvre aucune boîte modale
✅ valider sans réponse annonce et ne valide pas encore — Tu n'as choisi aucune réponse : elle comptera comme non répondue. — clique une seconde fois pour confirmer.
✅ le second clic valide bien
✅ « recommencer » n’ouvre aucune boîte modale
✅ « recommencer » demande confirmation sans rien effacer — 30
✅ le second clic remet bien à zéro — 0
✅ le mode « marquées » vide n’ouvre aucune boîte modale
✅ il affiche un bandeau à la place — Aucune question marquée « à revoir ». Utilise le bouton 🔖 sur une question.
✅ 30 bonnes réponses donnent 100 % — 100 %
✅ la note affichée est 20/20 — 20,0 /20
✅ le lien vers la séquence pointe le bon fichier — sequence_4e_C7.7_support-du-capteur.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours
```

## 3. Ce que ces tests ont attrapé pendant la fabrication

* **la colonne d'état des cotes ne disait rien.** Elle affichait un point sur presque
  toutes les lignes, parce qu'elle se lisait « au moins un moyen bloque » — une information vraie
  et inutilisable. Elle se lit désormais pour le moyen que le cahier des charges a déjà retenu,
  ou, à défaut, pour l'ensemble de l'atelier ;
* **un distracteur du jeu de réponses ne correspondait pas à la page.** Le fichier d'attendus
  portait « seuls ses coins sont adoucis » quand la séquence écrivait « seuls les coins ». Le
  test a refusé de continuer plutôt que de valider approximativement — c'est exactement ce qu'on
  lui demande.

## 4. Ce que ces tests ne prouvent pas

* Ils ne prouvent **rien sur les valeurs elles-mêmes**. Elles sont cohérentes entre elles et
  calculées par `moyens.py` ; ce sont des ordres de grandeur d'atelier, pas des fiches
  constructeur. La version 🅰 les remplace par des temps et des mesures réels, et l'écart se
  commente.
* Ils ne prouvent **rien sur une pièce réellement produite** : l'atelier simule. Ce sont les
  pièces sorties de la machine, mesurées au pied à coulisse, qui font foi.
* Ils ne prouvent rien sur la **qualité des phrases rédigées** : le vérificateur compte des
  caractères. C'est écrit dans la page, à l'élève.
* Ils ne prouvent rien sur ce qui se passe **en classe**. Un test vert dit que la page fait ce
  qu'elle annonce, pas qu'un élève apprend.
