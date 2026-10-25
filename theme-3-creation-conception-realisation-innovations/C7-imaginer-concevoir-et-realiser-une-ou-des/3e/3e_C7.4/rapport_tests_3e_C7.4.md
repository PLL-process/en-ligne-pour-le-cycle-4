# Rapport de tests — 3e_C7.4 « La station doit tenir 72 heures sans secteur »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Les scripts sont dans ce dossier : on peut les rejouer, et cette page est la
sortie de la dernière exécution, recopiée telle quelle.


> **Correction du 31/08/2026 — le verrou expérientiel s'ouvrait en partie au chargement.**
> `_outils/controle_verrous.mjs`, écrit ce jour-là, ouvre chaque séquence du dépôt dans un
> navigateur **neuf** et lit `window.__exp` juste après le chargement. Cette page en portait
> déjà `stock` et la source sélectionnée par défaut dans `src` **avant tout geste** : la fonction d'affichage du banc était appelée à
> l'initialisation, et elle enregistrait ce qu'elle affichait. Le verrou « les cinq sources » n'en réclamait donc plus que quatre. La fonction ne trace plus que
> sur un geste ; vérifié après correction : `__exp` est **vide** à l'ouverture, et le verrou
> s'ouvre normalement dès les manipulations réelles (règles d'or n°226 et n°265).
> **Découpage du 24/10/2026 — trois séances de 55 min au lieu de deux de 90.** La séquence se fait
> désormais en une heure de cours par semaine : séance 1 = activités 0 et 1 (45 min), séance 2 =
> activités 2 et 3 (55 min), séance 3 = activité 4 et REFAIRE (50 min), puis la clôture. Aucune
> activité n'est coupée ni raccourcie. Le banc de la séquence le vérifie (bandeau, trois en-têtes
> dans l'ordre, minutes par séance, clôture à la seule séance 3, boutons et liens de séance,
> 390 px sans défilement horizontal) et recharge la page sur une sauvegarde écrite au format de
> l'ancienne page : chaque réponse revient à sa place. Le QCM n'a pas changé ; son banc a été rejoué.

```bash
node tests_3e_C7.4_sequence.mjs "$PWD/sequence_3e_C7.4_energie-de-la-station.html" 3e reponses_3e_C7.4.json
node tests_3e_C7.4_qcm.mjs      "$PWD/qcm_3e_C7.4_energie-de-la-station.html" 3e_C7.4 3e_C3.2 sequence_3e_C7.4_energie-de-la-station.html
python3 energie.py          # recalcule toutes les valeurs du banc
```

---

## 1. Séquence — **54 / 54**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ le total du jour est juste — 6,04 Wh
✅ autant de lignes que de consommateurs — 7
✅ pile 9 V : énergie stockée 4,95 Wh — 4,95 Wh
✅ pile 9 V : rendement 56 % (5 V ÷ 9 V) — 56 %
✅ pile 9 V : énergie utile 2,8 Wh — 2,8 Wh
✅ pile 9 V : autonomie annoncée — 🔋 Autonomie : 11 heures  (2,8 Wh utiles ÷ 6,04 Wh par jour)
✅ 4 AA : rendement 83 % (5 V ÷ 6 V) — 83 %
✅ accu : énergie utile 9,4 Wh — 9,4 Wh
✅ secteur : autonomie illimitée — ⚡ Autonomie illimitée — tant qu'il y a du réseau.
✅ panneau : le verdict raisonne en Wh PAR JOUR — 3,7 Wh PAR JOUR
✅ panneau 1 W : il ne suffit pas — ☁ Il récolte 3,7 Wh par jour pour 6,04 consommés : il NE SUFFIT PAS. Il en manque 2,34 Wh chaqu
✅ éteindre la carte fait chuter le total — 6,04 Wh → 0,64 Wh
✅ la ligne éteinte est barrée
✅ la barre donne la part exacte de la carte — 89.404
✅ verrou des cinq sources ouvert
✅ verrou « un consommateur éteint » ouvert
✅ bandeau de durée présent — ⏱ 3 séances de 55 min
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ encadré de sécurité TBT présent
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ bandeau : 3 séances de 55 min — ⏱ 3 séances de 55 min
✅ le bandeau de durée a un title et un aria-label
✅ trois en-têtes de séance, dans l’ordre — seance-1,seance-2,seance-3
✅ seance-1 : 45 min d’activités annoncées, au plus 55 — 45 min — 🖐️ Activité 0 + 🔢 Activité 1
✅ seance-2 : 55 min d’activités annoncées, au plus 55 — 55 min — ☀ Activité 2 + ♻️ Activité 3
✅ seance-3 : 50 min d’activités annoncées, au plus 55 — 50 min — ✍️ Activité 4 + 🔄 REFAIRE
✅ aucune activité avant la séance 1, et 150 min en tout
✅ clôture à la dernière séance seulement : Bonus → Bilan → QCM — Bonus → Bilan → QCM
✅ un bouton vers la séance suivante au bas des séances 1 et 2 — #seance-2,#seance-3
✅ des liens vers les trois séances sous le titre — #seance-1,#seance-2,#seance-3
✅ chaque lien « banc » mène à un banc qui existe
✅ à 390 px, le bouton ➡ mène à la séance 2 — haut à 60 px
✅ à 390 px, le bouton ➡ mène à la séance 3 — haut à 60 px
✅ à 390 px, aucun défilement horizontal — 390
✅ verrou eteint ouvert après les gestes exigés
✅ verrou srcAll ouvert après les gestes exigés
✅ activité 0 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 1 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 2 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 3 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 4 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 5 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ un relevé approximatif est refusé (18) — 🟡 4/5 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a3piles = 787
✅ les verrous survivent au rechargement
✅ ancienne sauvegarde : la page se recharge sans erreur JS
✅ ancienne sauvegarde : chaque réponse revient à sa place, séance 3 comprise — hyp=Un panneau sol · src=Accu Li-ion 18 · a1besoin=18,12 · a3piles=787 · a4avis=Source normale · reinv=Sur l’îlet, il
✅ ancienne sauvegarde : l’idée de départ est rappelée au bilan
✅ ancienne sauvegarde : les verrous sont conservés
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
✅ 20 questions sur 3e_C7.4 — {"3e_C7.4":20,"3e_C3.2":10}
✅ 10 questions sur 3e_C3.2 — {"3e_C7.4":20,"3e_C3.2":10}
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
✅ le lien vers la séquence pointe le bon fichier — sequence_3e_C7.4_energie-de-la-station.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours
```

## 3. Les valeurs du banc — recalculées, pas recopiées

Consommation du montage : **6,04 Wh par jour**.

```
6.04 Wh/jour
   Carte Arduino UNO                45 mA ×     24 h =  5.400 Wh  (89.4 %)
   Buzzer d'alerte                  30 mA ×      2 h =  0.300 Wh  ( 5.0 %)
   Anémomètre à impulsions           1 mA ×     24 h =  0.120 Wh  ( 2.0 %)
   Girouette                         1 mA ×     24 h =  0.120 Wh  ( 2.0 %)
   DEL indicatrice                  10 mA ×      2 h =  0.100 Wh  ( 1.7 %)
   autonomies :
      Pile 9 V alcaline                  0.46 jour(s) = 11 h
      4 piles AA alcalines               2.07 jour(s) = 50 h
      Accu Li-ion 18650 rechargeable     1.56 jour(s) = 37 h
      Secteur — adaptateur USB scellé    illimitée tant qu'il y a du réseau
      Panneau solaire 1 W crête + accu   NE SUFFIT PAS (3.7 Wh récoltés pour 6.04 consommés)
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
