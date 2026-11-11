# Rapport de tests — 4e_C7.3 « Le bac du jardin »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Cette page est la sortie de la dernière exécution, recopiée telle quelle —
les scripts et le jeu de réponses sont dans ce dossier, on peut tout rejouer.

> **Mise à jour du 30/10/2026 — les deux suites rejouées.** Le rapport affichait encore
> « écart moyen de longueur sous 5 caractères — 1.5 », sortie d'une exécution antérieure : la
> page du QCM a été retouchée depuis. Les deux suites ont été rejouées le 30/10/2026 avec les
> arguments ci-dessous. La séquence redonne **44 / 44**, ligne pour ligne la sortie déjà
> recopiée. Le QCM redonne **32 / 32** ; une seule ligne change, l'écart moyen de longueur, qui
> vaut **1.3**. Les sorties ci-dessous sont celles du 30/10/2026.

```bash
node tests_4e_C7.3_sequence.mjs "$PWD/sequence_4e_C7.3_bac-du-jardin.html" 4e reponses_4e_C7.3.json
node tests_4e_C7.3_qcm.mjs      "$PWD/qcm_4e_C7.3_bac-du-jardin.html" 4e_C7.3 4e_C3.2 sequence_4e_C7.3_bac-du-jardin.html
```

---

## 1. Séquence — **44 / 44**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ aucun verrou ouvert à l’ouverture de la page
✅ un seul établi dans la page
✅ aucun identifiant en double
✅ les seuils sont écrits à la française — 20 5 3 4 40 60
✅ « à l'achat » : 3 retenu(s) — lu 3
✅ « à l'achat » : ce sont les bons — PVC rigide (stabilisé anti-UV) · Polypropylène recyclé (plastique de récupération) · Bois 
✅ « à l'achat » : le moins cher est 90 € — 90 €
✅ « à l'achat » : le verdict le dit — 3 candidats tiennent : PVC rigide (stabilisé anti-UV) (167 €) · Polypropylène re
✅ « à l'achat » : le verrou evalue s’ouvre
✅ « sur 10 ans » : 3 retenu(s) — lu 3
✅ « sur 10 ans » : ce sont les bons — PVC rigide (stabilisé anti-UV) · Polypropylène recyclé (plastique de récupération) · Bois 
✅ « sur 10 ans » : le moins cher est 181 € — 181 €
✅ « sur 10 ans » : le verrou duree s’ouvre
✅ « sur 15 ans » : 3 retenu(s) — lu 3
✅ « sur 15 ans » : ce sont les bons — PVC rigide (stabilisé anti-UV) · Polypropylène recyclé (plastique de récupération) · Bois 
✅ « sur 15 ans » : le moins cher est 271 € — 271 €
✅ « sur 15 ans » : le verrou duree s’ouvre
✅ « sur 20 ans » : 3 retenu(s) — lu 3
✅ « sur 20 ans » : ce sont les bons — PVC rigide (stabilisé anti-UV) · Polypropylène recyclé (plastique de récupération) · Bois 
✅ « sur 20 ans » : le moins cher est 362 € — 362 €
✅ « sur 20 ans » : le verrou duree s’ouvre
✅ bandeau de durée présent — ⏱ 2 séances de 55 min
✅ le bandeau annonce plus de temps que les activités n’en demandent — 110 contre 95
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ consigne de sécurité d’atelier présente
✅ le secteur est explicitement écarté
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ la formulation officielle est recopiée — Comparer différents matériaux pour chois
✅ activité 0 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 1 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 2 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 3 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 4 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ le verrou fermé refuse la validation — 🔒 Change d'abord la durée de comparaison sur le banc (le me
✅ une réponse fausse est refusée — 🟡 4/5 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a3j = Je retiens ce matériau parce qu'il tient toutes les exigences écrites du cahier des charges, et parce que le critère que j'ajoute pour trancher entre les derniers candidats est le coût sur la durée que nous avons fixée, et non le prix d'achat. Je dis aussi ce que ce choix engage ailleurs dans le projet, et qui en porte la charge.
✅ les seuils du banc survivent au rechargement — 40
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
✅ 20 questions sur 4e_C7.3 — {"4e_C7.3":20,"4e_C3.2":10}
✅ 10 questions sur 4e_C3.2 — {"4e_C7.3":20,"4e_C3.2":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 1.3
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
✅ le lien vers la séquence pointe le bon fichier — sequence_4e_C7.3_bac-du-jardin.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours
```

## 3. Ce que ces tests ont attrapé pendant la fabrication

* **le tableau affichait deux fois la masse** — « Masse de la pièce » est une exigence, donc
  une colonne, et le banc en ajoutait une seconde, générique. Deux en-têtes pour la même mesure ;
* **le bonus demandait une manipulation impossible.** Il invitait à chercher « sur le banc » les
  deux années où le classement bascule, alors que le menu ne propose que cinq durées. Le bonus
  demande maintenant le calcul à la main, et il donne les deux nombres nécessaires.

## 4. Ce que ces tests ne prouvent pas

* Ils ne prouvent **rien sur les valeurs elles-mêmes**. Elles sont cohérentes entre elles et
  calculées par `materiaux.py` ; ce sont des ordres de grandeur, pas des fiches fournisseurs.
  La version 🅰 les remplace par des mesures ou des devis réels, et l'écart se commente.
* Ils ne prouvent rien sur la **qualité des phrases rédigées** : le vérificateur compte des
  caractères. C'est écrit dans la page, à l'élève.
* Ils ne prouvent rien sur ce qui se passe **en classe**. Un test vert dit que la page fait ce
  qu'elle annonce, pas qu'un élève apprend.

## Reprise du 04/11/2026 — la séquence passe à deux séances à onglets (vague C7 de la règle d'or n°311)

Découpage, volet « 📖 Rappel » et clôture complétée : voir la fiche pédagogique.

- `node tests_regle_311_4e_C7.3.mjs` : 16 / 16 « l'outil suit la séance » (un seul nœud ; à sa place à la séance 1 ; juste après l'en-tête à la séance 2, état gardé ; onglets et en-tête dans le premier écran à 1280 px ; retour à sa place ; rechargement ; sans JavaScript, à sa place), relais 8 / 8, banc commun **34 / 34**.
- `tests_4e_C7.3_sequence.mjs` : **44 / 44**, avant comme après (le banc ouvre la séance qui porte chaque champ, comme l'élève) ; `tests_4e_C7.3_qcm.mjs` : **32 / 32**.
- `controle_squelette.mjs` : 0 défaut (D1 à D6), aucun « à rédiger », aucun signalement.
- `banc_papier.py` : une fiche par séance (deux fiches), aucun texte pâle, aucun champ d'écran imprimé.
- Sorties inchangées : `controle_impression`, `controle_impression_papier`, `controle_verrous`, `controle_hors_ligne`,
  `controle_contraste_liens`, `controle_regles_visibles`, `controle_liens`, `controle_hierarchie`, `controle_unites`,
  `controle_sigles`, `controle_navigation_seances` ; `verif_regles_audit.py` : autant de ✘ qu'avant, aucun nouveau.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle. Non fait : le lexique par séance.

## 10/11/2026 — V2 de la boucle d'audit (4e) : gabarit commun (n°306), groupes de boutons radio (n°300), grilles

Page migrée par `_outils/migrer_gabarit_306.py` (rejouable depuis `main`, résultat identique octet pour octet) : chaque
question posée par une liste déroulante devient un `fieldset.qcm-groupe` ; mode essentiel (n°29), bandeau des tâches
(n°30), versions étayées `etayage_sequence_4e_C7.3_….json` (n°31), `aria-label` des zones de texte (n°34). Les questions
qui partagent leurs réponses se lisent en grille (`_outils/grilles_radio.py` : 2 grille(s), 7 questions) — les
réponses une fois, lettrées ; chaque question, une rangée de lettres.

Les bancs n'ont pas changé de questions : shim `_groupesRadio(page)` en tête de `tests_4e_C7.3_sequence.mjs`.

Exécuté le 10/11/2026 (Chromium Playwright, session cloud) : `tests_4e_C7.3_sequence.mjs` **44 / 44** ; `tests_4e_C7.3_qcm.mjs`
**32 / 32** ; `tests_regle_311_4e_C7.3.mjs` **34 / 34** ; `verif_regles_audit.py` **0 ✘** ; `controle_squelette`,
`controle_hors_ligne`, `controle_contraste_liens`, `controle_impression_papier`, `banc_papier.py --filtre 4e_C7.3`,
`controle_impression --muet`, `controle_regles_visibles`, `controle_liens`, `controle_tactile`, `controle_mode_essentiel`,
`controle_navigation_seances`, `controle_rapports_tests`, `controle_licence` : 0 refus. Captures 390 px avant/après/essentiel
dans `_outils/captures_v2_4e_2026-11-10/`. Non exécuté : vrai téléphone, Firefox, Safari, impression réelle.
