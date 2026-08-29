# Rapport de tests — 3e_C7.7 « Produire le boîtier »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Cette page est la sortie de la dernière exécution, recopiée telle quelle —
les scripts et le jeu de réponses sont dans ce dossier, on peut tout rejouer.

```bash
node tests_3e_C7.7_sequence.mjs "$PWD/sequence_3e_C7.7_produire-le-boitier.html" 3e reponses_3e_C7.7.json
node tests_3e_C7.7_qcm.mjs      "$PWD/qcm_3e_C7.7_produire-le-boitier.html" 3e_C7.7 3e_C8.1 sequence_3e_C7.7_produire-le-boitier.html
```

---

## 1. Séquence — **52 / 52**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ aucun verrou ouvert à l’ouverture de la page
✅ un seul atelier dans la page
✅ aucun identifiant en double
✅ les cotes sont écrites à la française — 2,9 70,0 0,3 0,1 0,0
✅ « le dessin tel qu'il sort de la modélisation » : 0 moyen(s) capable(s) — lu 0
✅ « le dessin tel qu'il sort de la modélisation » : seconde jauge à 0 — lu 0
✅ « le dessin tel qu'il sort de la modélisation » : ce sont les bons
✅ « le dessin tel qu'il sort de la modélisation » : la colonne d’état dit exactement cela — epaisseur:✔ surplomb:✘ res_z:✘ tol:✘ r_int:✔
✅ « le dessin tel qu'il sort de la modélisation » : le verdict le dit — Aucun moyen de l'atelier ne sait produire cette forme. Ce n'est pas une panne : 
✅ « le dessin tel qu'il sort de la modélisation » : le verrou zero s’ouvre
✅ « la casquette seule corrigée » : 0 moyen(s) capable(s) — lu 0
✅ « la casquette seule corrigée » : seconde jauge à 0 — lu 0
✅ « la casquette seule corrigée » : ce sont les bons
✅ « la casquette seule corrigée » : la colonne d’état dit exactement cela — epaisseur:✔ surplomb:✔ res_z:✘ tol:✘ r_int:✔
✅ « les deux premières corrigées » : 0 moyen(s) capable(s) — lu 0
✅ « les deux premières corrigées » : seconde jauge à 0 — lu 0
✅ « les deux premières corrigées » : ce sont les bons
✅ « les deux premières corrigées » : la colonne d’état dit exactement cela — epaisseur:✔ surplomb:✔ res_z:✔ tol:✘ r_int:✔
✅ « les trois corrections » : 1 moyen(s) capable(s) — lu 1
✅ « les trois corrections » : seconde jauge à 0 — lu 0
✅ « les trois corrections » : ce sont les bons — Impression 3D (dépôt de fil, buse 0,4 mm, couche 0,2 mm)
✅ « les trois corrections » : la colonne d’état dit exactement cela — epaisseur:✔ surplomb:✔ res_z:✔ tol:✔ r_int:✔
✅ « les trois corrections » : le verdict le dit — 1 moyen(s) savent la produire : Impression 3D (dépôt de fil, buse 0,4 mm, couche
✅ « les trois corrections » : le verrou unSeul s’ouvre
✅ « les trois, plus deux cotes touchées sans nécessité » : 1 moyen(s) capable(s) — lu 1
✅ « les trois, plus deux cotes touchées sans nécessité » : seconde jauge à 2 — lu 2
✅ « les trois, plus deux cotes touchées sans nécessité » : ce sont les bons — Impression 3D (dépôt de fil, buse 0,4 mm, couche 0,2 mm)
✅ « les trois, plus deux cotes touchées sans nécessité » : le verdict le dit — 2 cote(s) modifiée(s) sans nécessité : Paroi étanche de 2,9 mm · Angles internes
✅ bandeau de durée présent — ⏱ 2 séances de 90 min
✅ le bandeau annonce plus de temps que les activités n’en demandent — 180 contre 160
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ consigne de sécurité d’atelier présente
✅ le secteur est explicitement écarté
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ la formulation officielle est recopiée — Choisir les moyens et produire la forme 
✅ le code d’appui est cité — 3e_C8.1
✅ activité 0 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 1 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 2 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 3 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 4 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ le verrou fermé refuse la validation — 🔒 Amène d'abord l'atelier à retenir UN moyen, en corrigeant
✅ une réponse fausse est refusée — 🟡 5/6 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a3j = Je retiens ce moyen parce que son domaine contient la pièce à produire, et parce que le temps machine dont nous disposons avant la date le permet pour la série demandée. Je dis aussi ce que la machine fera de mon dessin, et ce que j'ai corrigé pour cela. Je retiens ce moyen parce que son domaine contient la pièce à produire, et parce que le temps machine dont nous disposons avant la date le permet pour la série demandée. Je dis aussi ce que la machine fera de mon dessin, et ce que j'ai corrigé pour cela.
✅ l’état de l’atelier survit au rechargement — tr_surplomb = 45
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
✅ 20 questions sur 3e_C7.7 — {"3e_C7.7":20,"3e_C8.1":10}
✅ 10 questions sur 3e_C8.1 — {"3e_C7.7":20,"3e_C8.1":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 0.5
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
✅ le lien vers la séquence pointe le bon fichier — sequence_3e_C7.7_produire-le-boitier.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours
```

## 3. Ce que ces tests ont attrapé pendant la fabrication

* **la colonne d'état contredisait le texte de l'activité.** La séquence annonce
  « trois lignes portent une croix » ; l'instrument n'en affichait aucune, parce qu'il lisait
  l'état d'une cote sur *l'ensemble* des moyens au lieu de le lire sur celui que le cahier des
  charges a retenu. Le texte était juste, l'instrument racontait autre chose ;
* **la paroi contredisait le lot précédent.** Le dessin d'origine portait une paroi de 1,2 mm —
  alors que `3e_C7.3` avait calculé **2,9 mm** pour le PETG. Deux lots voisins auraient affirmé
  deux épaisseurs différentes pour la même pièce. La cote a été remise à sa valeur calculée, et
  le défaut déplacé sur le **jeu du couvercle**, qui est un vrai défaut de dessin d'impression.

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
