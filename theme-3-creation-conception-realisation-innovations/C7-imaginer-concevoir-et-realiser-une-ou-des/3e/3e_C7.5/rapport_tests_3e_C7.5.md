# Rapport de tests — 3e_C7.5 « La station qu'il faut équiper »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Cette page est la sortie de la dernière exécution, recopiée telle quelle —
les scripts et le jeu de réponses sont dans ce dossier, on peut tout rejouer.

```bash
node tests_3e_C7.5_sequence.mjs "$PWD/sequence_3e_C7.5_station-a-equiper.html" 3e reponses_3e_C7.5.json
node tests_3e_C7.5_qcm.mjs      "$PWD/qcm_3e_C7.5_station-a-equiper.html" 3e_C7.5 3e_C4.3 sequence_3e_C7.5_station-a-equiper.html
```

---

## 1. Séquence — **42 / 42**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ aucun constituant monté au départ
✅ aucune fonction tenue au départ
✅ les quatre fonctions sont tenues — 4
✅ le courant demandé est celui attendu — Courant demandé : 580 mA sur l'alimentation externe (2000 mA)
✅ le montage juste est accepté — ✔ Vent moyen à 104 km/h, au-delà des 90 km/h du cahier des c
✅ le verdict décrit le comportement obtenu — ✔ Vent moyen à 104 km/h, au-delà des 90 km/h du cahier des charges : le bandeau 
✅ « le capteur de pluie à la place de l'anémomètre » : le diagnostic est le bon — ✘ Rien ne mesure le vent. Le cahier des charges déclenche l'alerte « au-delà de 90 km/h de
✅ « le capteur de pluie à la place de l'anémomètre » : le verrou requis_anemo s’ouvre
✅ « l'écran LCD au lieu du bandeau » : le diagnostic est le bon — ✘ L'alerte n'est pas visible depuis la cour. Un écran LCD se lit à trente centimètres ; le
✅ « l'écran LCD au lieu du bandeau » : le verrou requis_bandeau s’ouvre
✅ « la station sans carte SD » : le diagnostic est le bon — ✘ Rien ne garde les mesures. La commission de sécurité demande l'historique : une station 
✅ « la station sans carte SD » : le verrou requis_sd s’ouvre
✅ « la station sans batterie » : le diagnostic est le bon — ✘ Le montage demande 580 mA et n'en a que 500. La carte s'effondre et redémarre en boucle 
✅ « la station sans batterie » : le verrou budget s’ouvre
✅ « le bandeau sur D2 » : le diagnostic est le bon — ✘ Le programme écrit sur D6, et Bandeau de 8 DEL de puissance est sur D2 : l'ordre et la m
✅ « le bandeau sur D2 » : le verrou attendu_bandeau s’ouvre
✅ le montage juste est de nouveau accepté — ✔ Vent moyen à 104 km/h, au-delà des 90 km/h du ca
✅ verrou « monte » ouvert
✅ verrou « teste » ouvert
✅ verrou « ok » ouvert
✅ verrou « panne » ouvert
✅ verrou « retire » ouvert
✅ bandeau de durée présent — ⏱ 2 séances de 90 min
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ consigne de sécurité très basse tension présente
✅ le secteur est explicitement écarté
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ activité 0 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 1 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 2 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 3 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 4 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 5 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ une réponse fausse est refusée — 🟡 3/4 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a2q1 = parce que le programme écrit sur D6, et qu'on ne le modifie pas ici
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
✅ 20 questions sur 3e_C7.5 — {"3e_C7.5":20,"3e_C4.3":10}
✅ 10 questions sur 3e_C4.3 — {"3e_C7.5":20,"3e_C4.3":10}
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
✅ le lien vers la séquence pointe le bon fichier — sequence_3e_C7.5_station-a-equiper.html
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
