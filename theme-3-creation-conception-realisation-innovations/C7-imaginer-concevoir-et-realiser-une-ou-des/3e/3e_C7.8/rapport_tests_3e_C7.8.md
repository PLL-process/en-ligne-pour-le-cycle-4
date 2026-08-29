# Rapport de tests — 3e_C7.8 « Deux stations qui se parlent »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Cette page est la sortie de la dernière exécution, recopiée telle quelle —
les scripts et le jeu de réponses sont dans ce dossier, on peut tout rejouer.

```bash
node tests_3e_C7.8_sequence.mjs "$PWD/sequence_3e_C7.8_deux-stations.html" 3e reponses_3e_C7.8.json
node tests_3e_C7.8_qcm.mjs      "$PWD/qcm_3e_C7.8_deux-stations.html" 3e_C7.8 3e_C8.3 sequence_3e_C7.8_deux-stations.html
```

---

## 1. Séquence — **34 / 34**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ message vide au départ — {}
✅ rien n’est lisible avec un message vide
✅ le message partiel est celui attendu — {"id":"robert","v":124,"u":"km/h"}
✅ certaines lectures restent impossibles — 5 non
✅ le message complet est celui attendu — {"id":"robert","v":124,"u":"km/h","t":"14:07","niv":2,"seq":417}
✅ tout devient lisible
✅ verrou du message valide ouvert
✅ un champ de trop est signalé au lieu d’être ignoré — 1
✅ le canal passe en coupé
✅ « ne déclenche jamais sans l'accord … » : le journal dit « AUCUNE alerte » — pé14:10  ✘ AUCUNE alerte — 124 km/h mesurés, et la sirène reste muette
✅ « déclenche seule, sans rien signale… » : le journal dit « déclenchée seule » —  déclenchée seule — et personne ne sait qu'elle n'était pas corroborée
✅ « déclenche seule, et signale qu'ell… » : le journal dit « NON CORROBORÉE » — lenchée, marquée « NON CORROBORÉE — Sainte-Anne muette depuis 15 min »
✅ verrou « coupe » ouvert
✅ verrou « degrade » ouvert
✅ lien rétabli : le message est reçu — ":"robert","v":124,"u":"km/h","t":"14:07","niv":2,"seq":417}
✅ bandeau de durée présent — ⏱ 2 séances de 90 min (1 h 30)
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ encadré de sécurité présent
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ activité 0 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 1 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 2 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 3 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 4 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 5 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ une réponse fausse est refusée — 🟡 4/5 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a1msg = {"id":"robert","v":124,"u":"km/h","t":"14:07","niv":2,"seq":417}
✅ les verrous survivent au rechargement
✅ les champs cochés survivent au rechargement
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
✅ 20 questions sur 3e_C7.8 — {"3e_C7.8":20,"3e_C8.3":10}
✅ 10 questions sur 3e_C8.3 — {"3e_C7.8":20,"3e_C8.3":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 3.8
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
✅ le lien vers la séquence pointe le bon fichier — sequence_3e_C7.8_deux-stations.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours
```

## 3. Six de ces tests existent parce qu'une règle avait été mal appliquée

La règle d'or n°188 — *une page d'élève ne s'arrête pas pour parler* — avait été appliquée au
seul mot `alert`. Le gabarit de QCM maison ouvre aussi **deux boîtes de confirmation** : valider
une question sans avoir choisi de réponse, et « Recommencer ». Personne ne les avait comptées, et
le test qui affirmait « aucune boîte modale sur tout le parcours » **ne passait par aucun de ces
deux chemins** : il était vert sans rien prouver.

Six tests l'accompagnent maintenant, qui les empruntent : `valider sans réponse n'ouvre aucune
boîte modale` / `annonce et ne valide pas encore` / `le second clic valide bien`, puis les trois
mêmes pour « recommencer », dont `demande confirmation sans rien effacer` — celui-là vérifie que
les 30 réponses sont **toujours là** après le premier clic.

Une confirmation ne se supprime pas : elle pose une question dont la réponse change ce qui arrive.
`_outils/sans_modale.py` la remplace par une confirmation **en deux temps** (premier clic : le
bandeau `aria-live` annonce ; second clic dans les six secondes : l'action s'exécute) et refuse
tout motif qu'il ne reconnaît pas plutôt que de deviner.

*Règle d'or n°216 : un test qui affirme qu'il ne se passe rien doit passer par les chemins où
quelque chose pourrait se passer. Sinon il mesure son propre silence.*

## 4. Ce que ces tests ne prouvent pas

* Ils ne prouvent **rien sur une liaison réelle** : le banc simule l'échange. La version 🅰 le
  fait avec deux cartes, et ce sont les trames observées qui font foi.
* Ils ne prouvent rien sur la **qualité des phrases rédigées** : le vérificateur compte des
  caractères et des lignes. C'est écrit dans la page, à l'élève.
* Ils ne prouvent rien sur ce qui se passe **en classe**. Un test vert dit que la page fait ce
  qu'elle annonce, pas qu'un élève apprend.
