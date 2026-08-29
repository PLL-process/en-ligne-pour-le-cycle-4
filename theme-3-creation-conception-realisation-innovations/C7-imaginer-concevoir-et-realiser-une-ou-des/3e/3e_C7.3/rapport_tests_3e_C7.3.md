# Rapport de tests — 3e_C7.3 « Le boîtier de la station »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Cette page est la sortie de la dernière exécution, recopiée telle quelle —
les scripts et le jeu de réponses sont dans ce dossier, on peut tout rejouer.

```bash
node tests_3e_C7.3_sequence.mjs "$PWD/sequence_3e_C7.3_boitier-de-la-station.html" 3e reponses_3e_C7.3.json
node tests_3e_C7.3_qcm.mjs      "$PWD/qcm_3e_C7.3_boitier-de-la-station.html" 3e_C7.3 3e_C4.2 sequence_3e_C7.3_boitier-de-la-station.html
```

---

## 1. Séquence — **43 / 43**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ aucun verrou ouvert à l’ouverture de la page
✅ un seul établi dans la page
✅ aucun identifiant en double
✅ les seuils sont écrits à la française — 30 10 5 60 1,2
✅ « le cahier des charges tel qu'il est écrit » : 0 retenu(s) — lu 0
✅ « le cahier des charges tel qu'il est écrit » : ce sont les bons
✅ « le cahier des charges tel qu'il est écrit » : le verdict le dit — Aucun matériau ne tient ce cahier des charges. Ce n'est pas une panne du banc : 
✅ « le cahier des charges tel qu'il est écrit » : le verrou zero s’ouvre
✅ « sortie A — tenue au sel 5 → 4 » : 1 retenu(s) — lu 1
✅ « sortie A — tenue au sel 5 → 4 » : ce sont les bons — Aluminium anodisé
✅ « sortie A — tenue au sel 5 → 4 » : le moins cher est 2,90 € — 2,90 €
✅ « sortie A — tenue au sel 5 → 4 » : le verrou unSeul s’ouvre
✅ « sortie B — masse 1,2 → 1,4 kg » : 1 retenu(s) — lu 1
✅ « sortie B — masse 1,2 → 1,4 kg » : ce sont les bons — Acier inoxydable 316 (dit « marine »)
✅ « sortie B — masse 1,2 → 1,4 kg » : le moins cher est 8,58 € — 8,58 €
✅ « sortie B — masse 1,2 → 1,4 kg » : le verrou unSeul s’ouvre
✅ « sortie C — tenue au soleil 10 → 5 ans » : 3 retenu(s) — lu 3
✅ « sortie C — tenue au soleil 10 → 5 ans » : ce sont les bons — PETG (filament d'impression 3D technique) · PVC rigide (stabilisé anti-UV) · Polypropylène
✅ « sortie C — tenue au soleil 10 → 5 ans » : le moins cher est 1,27 € — 1,27 €
✅ « sortie C — tenue au soleil 10 → 5 ans » : le verdict le dit — 3 candidats tiennent : PETG (filament d'impression 3D technique) (12,74 €) · PVC
✅ bandeau de durée présent — ⏱ 2 séances de 90 min
✅ le bandeau annonce plus de temps que les activités n’en demandent — 180 contre 160
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ consigne de sécurité d’atelier présente
✅ le secteur est explicitement écarté
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ la formulation officielle est recopiée — Choisir un matériau constitutif d’un obj
✅ activité 0 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 1 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 2 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 3 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 4 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ le verrou fermé refuse la validation — 🔒 Amène d'abord le banc à retenir EXACTEMENT UN matériau, e
✅ une réponse fausse est refusée — 🟡 5/6 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a3j = Je retiens ce matériau parce qu'il tient toutes les exigences écrites du cahier des charges, et parce que le critère que j'ajoute pour trancher entre les derniers candidats est le coût sur la durée que nous avons fixée, et non le prix d'achat. Je dis aussi ce que ce choix engage ailleurs dans le projet, et qui en porte la charge. Je retiens ce matériau parce qu'il tient toutes les exigences écrites du cahier des charges, et parce que le critère que j'ajoute pour trancher entre les derniers candidats est le coût sur la durée que nous avons fixée, et non le prix d'achat. Je dis aussi ce que ce choix engage ailleurs dans le projet, et qui en porte la charge.
✅ les seuils du banc survivent au rechargement — 5
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
✅ 20 questions sur 3e_C7.3 — {"3e_C7.3":20,"3e_C4.2":10}
✅ 10 questions sur 3e_C4.2 — {"3e_C7.3":20,"3e_C4.2":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 1.7
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
✅ le lien vers la séquence pointe le bon fichier — sequence_3e_C7.3_boitier-de-la-station.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours
```

## 3. Ce que ces tests ont attrapé pendant la fabrication

* **un verrou expérientiel s'ouvrait tout seul.** Le boîtier ne retient aucun matériau tel
  que le cahier des charges est écrit : le drapeau « l'élève a vu zéro candidat » se posait donc
  au chargement de la page, avant tout geste. Le banc distingue maintenant une mise à jour venue
  d'une action et une mise à jour venue de l'ouverture — et un test vérifie qu'aucun verrou
  n'est ouvert à l'arrivée ;
* **les masses s'affichaient au dixième de kilo.** 0,545 kg de PVC et 0,557 kg d'aluminium
  devenaient « 0,5 » et « 0,6 » : la page affichait le contraire de ce qu'elle démontre. La
  précision se règle désormais sur l'ordre de grandeur de l'objet.

## 4. Ce que ces tests ne prouvent pas

* Ils ne prouvent **rien sur les valeurs elles-mêmes**. Elles sont cohérentes entre elles et
  calculées par `materiaux.py` ; ce sont des ordres de grandeur, pas des fiches fournisseurs.
  La version 🅰 les remplace par des mesures ou des devis réels, et l'écart se commente.
* Ils ne prouvent rien sur la **qualité des phrases rédigées** : le vérificateur compte des
  caractères. C'est écrit dans la page, à l'élève.
* Ils ne prouvent rien sur ce qui se passe **en classe**. Un test vert dit que la page fait ce
  qu'elle annonce, pas qu'un élève apprend.
