# Rapport de tests — 5e_C1.5 + 5e_C1.6 « Le compte du club »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Cette page est la sortie de la dernière exécution, recopiée telle quelle.


> **Correction du 31/08/2026 — deux verrous expérientiels s'ouvraient au chargement.**
> `_outils/controle_verrous.mjs` ouvre chaque séquence du dépôt dans un navigateur **neuf** et
> lit `window.__exp` juste après le chargement. Cette page en portait **deux** avant tout
> geste : `anonyme` (un profil vide n'a aucun indice, donc la condition « zéro indice » était
> vraie d'emblée) et `regarde` (la fonction qui affiche ce que le profil laisse voir était
> appelée à l'initialisation). Les activités qui exigent « j'ai regardé ce que mon profil
> laisse voir » et « j'ai composé un profil anonyme » étaient donc déverrouillées avant que
> l'élève ait coché une seule case. `majPubli` et `regarder` prennent désormais un `tracer` et
> n'enregistrent que sur un geste ; l'initialisation passe `false`. Vérifié : `__exp` est
> **vide** à l'ouverture, et vaut `{anonyme, compose, regarde}` dès la première case cochée
> (règles d'or n°226 et n°265).
```bash
node tests_5e_C1.5-C1.6_sequence.mjs "$PWD/sequence_5e_C1.5-C1.6_le-compte-du-club.html" 5e reponses_5e_C1.5-C1.6.json
node tests_5e_C1.5-C1.6_qcm.mjs      "$PWD/qcm_5e_C1.5-C1.6_le-compte-du-club.html" 5e_C1.5 5e_C1.6 sequence_5e_C1.5-C1.6_le-compte-du-club.html 15 15
```

---

## 1. Séquence — **38 / 38**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ le banc part vide — [0,0]
✅ la publication du club compte 7 indices — [7,3]
✅ elle enfreint 3 règle(s) — [7,3]
✅ le banc énumère 9 constats — 9
✅ publier est refusé, et le banc dit pourquoi — Refusé — Droit à l'image : publier le visage d'une personne reconnaissable demande son acc
✅ « on retire le visage » → 6 indice(s) / 2 règle(s) — [6,2]
✅ « accord écrit des responsables légaux » → 6 indice(s) / 1 règle(s) — [6,1]
✅ « image sous licence CC BY, auteur cité » → 6 indice(s) / 0 règle(s) — [6,0]
✅ « on retire le nom et la classe » → 4 indice(s) / 0 règle(s) — [4,0]
✅ « on retire la rue, l'heure, le collège et la géolocalisation » → 0 indice(s) / 0 règle(s) — [0,0]
✅ la publication corrigée est acceptée — Publié. La photo montre le jardin connecté et rien d'autre :
✅ verrou « charge » ouvert
✅ verrou « regarde » ouvert
✅ verrou « compose » ouvert
✅ verrou « refuse » ouvert
✅ verrou « anonyme » ouvert
✅ verrou « legal » ouvert
✅ verrou « publie » ouvert
✅ bandeau de durée présent — ⏱ 3 séances de 55 min
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ encadré de règle de la séquence présent
✅ le numéro national est indiqué
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ activité 0 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 1 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 2 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 3 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 4 validée (7/7) — 🎉 Activité validée — 7/7. Ouvre la correction pour comparer.
✅ activité 5 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ une réponse fausse est refusée — 🟡 4/5 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a1q1 = son nom, sa classe et son collège le désignent toujours
✅ la publication survit au rechargement — jardin coché
✅ les verrous survivent au rechargement
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
✅ 15 questions sur 5e_C1.5 — {"5e_C1.5":15,"5e_C1.6":15}
✅ 15 questions sur 5e_C1.6 — {"5e_C1.5":15,"5e_C1.6":15}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 1.5
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
✅ le lien vers la séquence pointe le bon fichier — sequence_5e_C1.5-C1.6_le-compte-du-club.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours
```

## 3. Ce que ces tests vérifient de particulier

Cinq d'entre eux suivent **le compteur d'indices pas à pas**, et c'est là tout l'intérêt :

* la publication du club en compte **7**, et enfreint **3** règles ;
* retirer le visage : **6 indices** — un seul de moins, alors que c'est l'élément le plus visible ;
* obtenir l'accord écrit : **6 indices**, **1 règle**. *Le compteur d'indices ne bouge pas :*
  une autorisation rend licite, elle ne rend pas anonyme ;
* citer l'auteur de l'image sous CC BY : **0 règle** ;
* tout retirer sauf la photo du jardin : **0 indice**, et la publication est acceptée.

Un test qui se contenterait de vérifier « la publication est refusée » puis « la publication est
acceptée » passerait tout aussi bien — et ne prouverait rien du raisonnement que la séquence
demande. Ce sont les **valeurs intermédiaires** qui font la preuve.

## 4. Ce que ces tests ne prouvent pas

* Ils ne prouvent **rien sur une publication réelle** : le banc simule, avec des personnes
  inventées. La version 🅰 le fait avec le compte du collège, et c'est elle qui engage.
* Ils ne prouvent rien sur la **qualité du texte rédigé** au réinvestissement : le vérificateur
  compte des caractères, et la page le dit à l'élève.
* Ils ne prouvent rien sur ce qui se passe **en classe** — et cette séquence-là touche à des
  situations que des élèves vivent. Un test vert ne dit rien de cela.
