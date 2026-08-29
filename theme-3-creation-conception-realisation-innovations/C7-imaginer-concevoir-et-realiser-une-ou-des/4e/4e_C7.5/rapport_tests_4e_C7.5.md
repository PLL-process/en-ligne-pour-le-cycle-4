# Rapport de tests — 4e_C7.5 « Le jardin qui n'arrose pas encore »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Cette page est la sortie de la dernière exécution, recopiée telle quelle —
les scripts et le jeu de réponses sont dans ce dossier, on peut tout rejouer.

```bash
node tests_4e_C7.5_sequence.mjs "$PWD/sequence_4e_C7.5_jardin-incomplet.html" 4e reponses_4e_C7.5.json
node tests_4e_C7.5_qcm.mjs      "$PWD/qcm_4e_C7.5_jardin-incomplet.html" 4e_C7.5 4e_C4.4 sequence_4e_C7.5_jardin-incomplet.html
```

---

## 1. Séquence — **39 / 39**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ aucun constituant monté au départ
✅ aucune fonction tenue au départ
✅ les quatre fonctions sont tenues — 4
✅ le courant demandé est celui attendu — Courant demandé : 800 mA sur l'alimentation externe (2000 mA)
✅ le montage juste est accepté — ✔ Le sol est à 28 %, sous le seuil de 35 % : le relais colle
✅ le verdict décrit le comportement obtenu — ✔ Le sol est à 28 %, sous le seuil de 35 % : le relais colle, la pompe tourne si
✅ « cas 1, la pompe ne part jamais » : le diagnostic est le bon — ✘ La pompe est raccordée, mais rien ne la commande. Une sortie de la carte fournit 20 mA a
✅ « cas 1, la pompe ne part jamais » : le verrou exige_relais s’ouvre
✅ « cas 2, la carte redémarre » : le diagnostic est le bon — ✘ Le montage demande 800 mA et n'en a que 500. La carte s'effondre et redémarre en boucle 
✅ « cas 2, la carte redémarre » : le verrou budget s’ouvre
✅ « cas 3, la pompe ne s'arrête plus » : le diagnostic est le bon — ✘ Aucune mesure d'humidité du sol n'arrive à la carte. Le programme compare toujours la mê
✅ « cas 3, la pompe ne s'arrête plus » : le verrou requis_hum s’ouvre
✅ le montage juste est de nouveau accepté — ✔ Le sol est à 28 %, sous le seuil de 35 % : le re
✅ verrou « monte » ouvert
✅ verrou « teste » ouvert
✅ verrou « ok » ouvert
✅ verrou « panne » ouvert
✅ verrou « cas1 » ouvert
✅ verrou « cas2 » ouvert
✅ verrou « cas3 » ouvert
✅ bandeau de durée présent — ⏱ 2 séances de 55 min
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ consigne de sécurité très basse tension présente
✅ le secteur est explicitement écarté
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ activité 0 validée (7/7) — 🎉 Activité validée — 7/7. Ouvre la correction pour comparer.
✅ activité 1 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 2 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 3 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 4 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ une réponse fausse est refusée — 🟡 2/3 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a1q2 = le module relais
✅ le montage survit au rechargement — SOCLE
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
✅ 20 questions sur 4e_C7.5 — {"4e_C7.5":20,"4e_C4.4":10}
✅ 10 questions sur 4e_C4.4 — {"4e_C7.5":20,"4e_C4.4":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 2.2
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
✅ le lien vers la séquence pointe le bon fichier — sequence_4e_C7.5_jardin-incomplet.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours
```

## 3. Ce que ces tests ont attrapé pendant la fabrication

Deux défauts, trouvés par les tests et non par relecture :

* **l'établi était écrit deux fois.** Il figurait dans chaque activité qui l'utilise, si bien que
  la page portait deux jeux d'éléments avec les mêmes identifiants. La sauvegarde n'en retenait
  qu'un — le montage de l'élève était perdu au rechargement. L'établi n'est plus écrit qu'une
  fois, et les activités suivantes y renvoient ;
* **l'établi écrasait sa propre sauvegarde.** Il appelait sa mise à jour au chargement de la
  page, donc *avant* la restauration : chaque ouverture remplaçait la sauvegarde par un établi
  vide. C'est le squelette qui restaure d'abord et met à jour ensuite.

Les deux défauts avaient le même symptôme et deux causes différentes ; aucun ne se voit à la
lecture du code.

## 4. Ce que ces tests ne prouvent pas

* Ils ne prouvent **rien sur un montage réel** : l'établi simule. La version 🅰 le fait avec la
  carte et les modules, et ce sont les branchements observés qui font foi.
* Ils ne prouvent rien sur la **qualité des phrases rédigées** : le vérificateur compte des
  caractères. C'est écrit dans la page, à l'élève.
* Ils ne prouvent rien sur ce qui se passe **en classe**. Un test vert dit que la page fait ce
  qu'elle annonce, pas qu'un élève apprend.
