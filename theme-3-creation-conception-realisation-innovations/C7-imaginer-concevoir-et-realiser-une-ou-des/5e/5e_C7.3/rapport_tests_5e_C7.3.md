# Rapport de tests — 5e_C7.3 « Le banc de la cour »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Cette page est la sortie de la dernière exécution, recopiée telle quelle —
les scripts et le jeu de réponses sont dans ce dossier, on peut tout rejouer.

```bash
node tests_5e_C7.3_sequence.mjs "$PWD/sequence_5e_C7.3_banc-de-la-cour.html" 5e reponses_5e_C7.3.json
node tests_5e_C7.3_qcm.mjs      "$PWD/qcm_5e_C7.3_banc-de-la-cour.html" 5e_C7.3 5e_C4.4 sequence_5e_C7.3_banc-de-la-cour.html
```

---

## 1. Séquence — **41 / 41**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ aucun verrou ouvert à l’ouverture de la page
✅ un seul établi dans la page
✅ aucun identifiant en double
✅ les seuils sont écrits à la française — 25 8 3 55 35
✅ « le cahier des charges tel qu'il est écrit » : 2 retenu(s) — lu 2
✅ « le cahier des charges tel qu'il est écrit » : ce sont les bons — Bois — pin traité autoclave classe 4 · Bois — teck (ou bois exotique dense)
✅ « le cahier des charges tel qu'il est écrit » : le moins cher est 47 € — 47 €
✅ « le cahier des charges tel qu'il est écrit » : le verdict le dit — 2 candidats tiennent : Bois — pin traité autoclave classe 4 (47 €) · Bois — teck
✅ « le cahier des charges tel qu'il est écrit » : le verrou evalue s’ouvre
✅ « sans « température au soleil » » : 3 retenu(s) — lu 3
✅ « sans « température au soleil » » : ce sont les bons — Bois — pin traité autoclave classe 4 · Bois — teck (ou bois exotique dense) · PVC rigide (
✅ « sans « température au soleil » » : le verrou retireCritere s’ouvre
✅ « sans « tenue au soleil » ni « tenue au sel » » : 3 retenu(s) — lu 3
✅ « sans « tenue au soleil » ni « tenue au sel » » : ce sont les bons — Bois — pin non traité · Bois — pin traité autoclave classe 4 · Bois — teck (ou bois exotiq
✅ « sans « tenue au soleil » ni « tenue au sel » » : le moins cher est 26 € — 26 €
✅ « sans « tenue au soleil » ni « tenue au sel » » : le verrou retireCritere s’ouvre
✅ « cahier des charges remis » : 2 retenu(s) — lu 2
✅ « cahier des charges remis » : ce sont les bons — Bois — pin traité autoclave classe 4 · Bois — teck (ou bois exotique dense)
✅ « cahier des charges remis » : le verrou evalue s’ouvre
✅ bandeau de durée présent — ⏱ 2 séances de 55 min
✅ le bandeau annonce plus de temps que les activités n’en demandent — 110 contre 95
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ consigne de sécurité d’atelier présente
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ la formulation officielle est recopiée — Choisir un matériau parmi plusieurs prop
✅ activité 0 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 1 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 2 validée (7/7) — 🎉 Activité validée — 7/7. Ouvre la correction pour comparer.
✅ activité 3 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 4 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ le verrou fermé refuse la validation — 🔒 Décoche d'abord au moins une exigence sur le banc et ré-é
✅ une réponse fausse est refusée — 🟡 4/5 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a3j = Je retiens ce matériau parce qu'il tient toutes les exigences écrites du cahier des charges, et parce que le critère que j'ajoute pour trancher entre les derniers candidats est le coût sur la durée que nous avons fixée, et non le prix d'achat. Je dis aussi ce que ce choix engage ailleurs dans le projet, et qui en porte la charge.
✅ les seuils du banc survivent au rechargement — 55
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
✅ 20 questions sur 5e_C7.3 — {"5e_C7.3":20,"5e_C4.4":10}
✅ 10 questions sur 5e_C4.4 — {"5e_C7.3":20,"5e_C4.4":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 0.8
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
✅ le lien vers la séquence pointe le bon fichier — sequence_5e_C7.3_banc-de-la-cour.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours
```

## 3. Ce que ces tests ont attrapé pendant la fabrication

* **le tableau affichait deux fois la masse.** « Masse de la pièce » est une exigence, donc
  une colonne — et le banc ajoutait par-dessus une colonne « Masse » générique. Deux en-têtes
  différents pour la même mesure : l'élève cherche ce qui les distingue, et il n'y a rien à
  trouver. La colonne générique n'apparaît plus que si la masse n'est pas une exigence ;
* **les seuils s'écrivaient à l'anglaise.** Le champ de la masse maximale affichait `1.2` au lieu
  de `1,2`. Le calcul acceptait les deux, l'élève n'en voit qu'un — et c'est celui qui est faux.

Et un troisième que **les tests ne pouvaient pas voir**, trouvé en recalculant les valeurs :
l'activité 2 demandait si l'économie de cent euros apportée par le PVC valait un banc brûlant.
**Il n'y avait pas d'économie.** Le PVC entre à 109,76 € quand le pin traité autoclave, déjà
retenu, coûte 46,82 € — les cent euros n'existaient que par rapport au *teck*, qui n'est pas le
candidat auquel il faut comparer. Tous les nombres étaient exacts et vérifiés ; c'était le point
de comparaison qui était faux. L'activité relève désormais **deux** chiffres par essai — le
nombre de retenus *et* le moins cher des retenus — et elle montre que le premier retrait n'en
change qu'un seul.

## 4. Ce que ces tests ne prouvent pas

* Ils ne prouvent **rien sur les valeurs elles-mêmes**. Elles sont cohérentes entre elles et
  calculées par `materiaux.py` ; ce sont des ordres de grandeur, pas des fiches fournisseurs.
  La version 🅰 les remplace par des mesures ou des devis réels, et l'écart se commente.
* Ils ne prouvent rien sur la **qualité des phrases rédigées** : le vérificateur compte des
  caractères. C'est écrit dans la page, à l'élève.
* Ils ne prouvent rien sur ce qui se passe **en classe**. Un test vert dit que la page fait ce
  qu'elle annonce, pas qu'un élève apprend.
