# Rapport de tests — 4e_C7.4 « De quoi vit le jardin connecté »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Les scripts sont dans ce dossier : on peut les rejouer, et cette page est la
sortie de la dernière exécution, recopiée telle quelle.

```bash
node tests_4e_C7.4_sequence.mjs "$PWD/sequence_4e_C7.4_energie-du-jardin.html" 4e reponses_4e.json
node tests_4e_C7.4_qcm.mjs      "$PWD/qcm_4e_C7.4_energie-du-jardin.html" 4e_C7.4 4e_C3.1 sequence_4e_C7.4_energie-du-jardin.html
python3 energie.py          # recalcule toutes les valeurs du banc
```

---

## 1. Séquence — **35 / 35**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ le total du jour est juste — 5,87 Wh
✅ autant de lignes que de consommateurs — 7
✅ pile 9 V : énergie stockée 4,95 Wh — 4,95 Wh
✅ pile 9 V : rendement 56 % (5 V ÷ 9 V) — 56 %
✅ pile 9 V : énergie utile 2,8 Wh — 2,8 Wh
✅ pile 9 V : autonomie annoncée — 🔋 Autonomie : 11 heures  (2,8 Wh utiles ÷ 5,87 Wh par jour)
✅ 4 AA : rendement 83 % (5 V ÷ 6 V) — 83 %
✅ accu : énergie utile 9,4 Wh — 9,4 Wh
✅ secteur : autonomie illimitée — ⚡ Autonomie illimitée — tant qu'il y a du réseau.
✅ panneau : le verdict raisonne en Wh PAR JOUR — 3,7 Wh PAR JOUR
✅ panneau 1 W : il ne suffit pas — ☁ Il récolte 3,7 Wh par jour pour 5,87 consommés : il NE SUFFIT PAS. Il en manque 2,17 Wh chaqu
✅ éteindre la carte fait chuter le total — 5,87 Wh → 0,47 Wh
✅ la ligne éteinte est barrée
✅ la barre donne la part exacte de la carte — 91.9801
✅ verrou des cinq sources ouvert
✅ verrou « un consommateur éteint » ouvert
✅ bandeau de durée présent — ⏱ 2 séances de 55 min
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ encadré de sécurité TBT présent
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ verrou compare ouvert après les gestes exigés
✅ activité 0 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 1 validée (9/9) — 🎉 Activité validée — 9/9. Ouvre la correction pour comparer.
✅ activité 2 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 3 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 4 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 5 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ un relevé approximatif est refusé (100) — 🟡 5/6 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a2piles = 131
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
✅ 20 questions sur 4e_C7.4 — {"4e_C7.4":20,"4e_C3.1":10}
✅ 10 questions sur 4e_C3.1 — {"4e_C7.4":20,"4e_C3.1":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 1.8
✅ une bonne réponse est déclarée correcte
✅ la correction déplie les trois réfutations
✅ la correction porte un « À retenir »
✅ une mauvaise réponse est déclarée incorrecte
✅ le mode « marquées » vide n’ouvre aucune boîte modale
✅ il affiche un bandeau à la place — Aucune question marquée « à revoir ». Utilise le bouton 🔖 sur une question.
✅ 30 bonnes réponses donnent 100 % — 100 %
✅ la note affichée est 20/20 — 20,0 /20
✅ le lien vers la séquence pointe le bon fichier — sequence_4e_C7.4_energie-du-jardin.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours
```

## 3. Les valeurs du banc — recalculées, pas recopiées

Consommation du montage : **5,87 Wh par jour**.

```
5.87 Wh/jour
   Carte Arduino UNO                45 mA ×     24 h =  5.400 Wh  (92.0 %)
   Capteur d'humidité du sol         2 mA ×     24 h =  0.240 Wh  ( 4.1 %)
   Écran LCD RGB                    40 mA ×      1 h =  0.200 Wh  ( 3.4 %)
   Pompe immergée 5 V              300 mA × 0.0167 h =  0.025 Wh  ( 0.4 %)
   Module relais                    70 mA × 0.0167 h =  0.006 Wh  ( 0.1 %)
   autonomies :
      Pile 9 V alcaline                  0.48 jour(s) = 12 h
      4 piles AA alcalines               2.13 jour(s) = 51 h
      Accu Li-ion 18650 rechargeable     1.60 jour(s) = 38 h
      Secteur — adaptateur USB scellé    illimitée tant qu'il y a du réseau
      Panneau solaire 1 W crête + accu   NE SUFFIT PAS (3.7 Wh récoltés pour 5.87 consommés)
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
