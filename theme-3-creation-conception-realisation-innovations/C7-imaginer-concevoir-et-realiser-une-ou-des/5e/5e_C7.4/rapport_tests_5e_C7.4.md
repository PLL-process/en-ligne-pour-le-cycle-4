# Rapport de tests — 5e_C7.4 « L'indicateur du hall »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Les scripts sont dans ce dossier : on peut les rejouer, et cette page est la
sortie de la dernière exécution, recopiée telle quelle.

```bash
node tests_5e_C7.4_sequence.mjs "$PWD/sequence_5e_C7.4_indicateur-du-hall.html" 5e reponses_5e.json
node tests_5e_C7.4_qcm.mjs      "$PWD/qcm_5e_C7.4_indicateur-du-hall.html" 5e_C7.4 5e_C3.1 sequence_5e_C7.4_indicateur-du-hall.html
python3 energie.py          # recalcule toutes les valeurs du banc
```

---

## 1. Séquence — **34 / 34**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ le total du jour est juste — 2,85 Wh
✅ autant de lignes que de consommateurs — 5
✅ pile 9 V : énergie stockée 4,95 Wh — 4,95 Wh
✅ pile 9 V : rendement 56 % (5 V ÷ 9 V) — 56 %
✅ pile 9 V : énergie utile 2,8 Wh — 2,8 Wh
✅ pile 9 V : autonomie annoncée — 🔋 Autonomie : 24 heures  (2,8 Wh utiles ÷ 2,85 Wh par jour)
✅ 4 AA : rendement 83 % (5 V ÷ 6 V) — 83 %
✅ accu : énergie utile 9,4 Wh — 9,4 Wh
✅ secteur : autonomie illimitée — ⚡ Autonomie illimitée — tant qu'il y a du réseau.
✅ panneau : le verdict raisonne en Wh PAR JOUR — 3,7 Wh PAR JOUR
✅ panneau : il suffit à ce montage — ☀ Il récolte 3,7 Wh par jour pour 2,85 consommés : il suffit, avec 30 % de marge.
✅ éteindre la carte fait chuter le total — 2,85 Wh → 0,60 Wh
✅ la ligne éteinte est barrée
✅ la barre donne la part exacte de la carte — 78.9474
✅ verrou des cinq sources ouvert
✅ verrou « un consommateur éteint » ouvert
✅ bandeau de durée présent — ⏱ 2 séances de 55 min
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ encadré de sécurité TBT présent
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ activité 0 validée (2/2) — 🎉 Activité validée — 2/2. Ouvre la correction pour comparer.
✅ activité 1 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 2 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 3 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 4 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 5 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ un relevé approximatif est refusé (3) — 🟡 4/5 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — rel1 = 12,5
✅ les verrous survivent au rechargement
```

## 2. QCM — **26 / 26**

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
✅ 20 questions sur 5e_C7.4 — {"5e_C7.4":20,"5e_C3.1":10}
✅ 10 questions sur 5e_C3.1 — {"5e_C7.4":20,"5e_C3.1":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 1.0
✅ une bonne réponse est déclarée correcte
✅ la correction déplie les trois réfutations
✅ la correction porte un « À retenir »
✅ une mauvaise réponse est déclarée incorrecte
✅ le mode « marquées » vide n’ouvre aucune boîte modale
✅ il affiche un bandeau à la place — Aucune question marquée « à revoir ». Utilise le bouton 🔖 sur une question.
✅ 30 bonnes réponses donnent 100 % — 100 %
✅ la note affichée est 20/20 — 20,0 /20
✅ le lien vers la séquence pointe le bon fichier — sequence_5e_C7.4_indicateur-du-hall.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours
```

## 3. Les valeurs du banc — recalculées, pas recopiées

Consommation du montage : **2,85 Wh par jour**.

```
2.85 Wh/jour
   Carte Arduino UNO                45 mA ×     10 h =  2.250 Wh  (78.9 %)
   DEL indicatrice                  10 mA ×     10 h =  0.500 Wh  (17.5 %)
   Capteur d'humidité du sol         2 mA ×     10 h =  0.100 Wh  ( 3.5 %)
   autonomies :
      Pile 9 V alcaline                  0.98 jour(s) = 24 h
      4 piles AA alcalines               4.39 jour(s) = 105 h
      Accu Li-ion 18650 rechargeable     3.30 jour(s) = 79 h
      Secteur — adaptateur USB scellé    illimitée tant qu'il y a du réseau
      Panneau solaire 1 W crête + accu   suffit chaque jour (3.7 Wh récoltés pour 2.85 consommés)
```

Le rendement d'un régulateur linéaire vaut V<sub>sortie</sub> ÷ V<sub>entrée</sub> : 56 % pour
la pile 9 V, 83 % pour les quatre piles AA. Ce n'est pas un réglage, c'est de la physique.

## 4. Ce que ces tests ne prouvent pas

* Ils ne prouvent **rien sur le matériel réel** : le banc calcule à partir de valeurs
  constructeur usuelles. La version 🅰 mesure au multimètre, et ce sont ces mesures qui font foi.
* Ils ne prouvent rien sur la **qualité des justifications rédigées** : le vérificateur compte
  des caractères et des lignes. C'est écrit dans la page, à l'élève.
* Ils ne prouvent rien sur ce qui se passe **en classe**. Un test vert dit que la page fait ce
  qu'elle annonce, pas qu'un élève apprend.
