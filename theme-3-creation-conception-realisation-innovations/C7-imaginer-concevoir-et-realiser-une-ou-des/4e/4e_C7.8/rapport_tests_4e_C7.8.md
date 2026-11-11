# Rapport de tests — 4e_C7.8 « Le jardin publie sa mesure »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Cette page est la sortie de la dernière exécution, recopiée telle quelle —
les scripts et le jeu de réponses sont dans ce dossier, on peut tout rejouer.

> **Clé de sauvegarde propre, 25/10/2026.** Jusque-là, la page enregistrait sous la clé de
> 4e_C7.4 (`seq_4e_C7_4`) : les deux séquences mélangeaient le travail de l'élève dans un même
> navigateur. Elle enregistre désormais sous `seq_4e_C7_8`. À la première ouverture, si cette clé
> n'existe pas et que `seq_4e_C7_4` existe, elle en fait une copie (sans rien effacer), puis ne la
> relit plus jamais. Le banc vérifie la clé, la migration, la copie sans effacement, qu'écrire
> dans 4e_C7.8 ne touche plus `seq_4e_C7_4`, et que la migration ne se rejoue pas.

```bash
node tests_4e_C7.8_sequence.mjs "$PWD/sequence_4e_C7.8_le-jardin-publie.html" 4e reponses_4e_C7.8.json
node tests_4e_C7.8_qcm.mjs      "$PWD/qcm_4e_C7.8_le-jardin-publie.html" 4e_C7.8 4e_C1.4 sequence_4e_C7.8_le-jardin-publie.html
```

---

## 1. Séquence — **46 / 46**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ message vide au départ — {}
✅ rien n’est lisible avec un message vide
✅ le message partiel est celui attendu — {"id":"jardin-cour","h":38,"u":"%"}
✅ certaines lectures restent impossibles — 3 non
✅ le message complet est celui attendu — {"id":"jardin-cour","h":38,"u":"%","t":"14:07","pompe":false}
✅ tout devient lisible
✅ verrou du message valide ouvert
✅ un champ de trop est signalé au lieu d’être ignoré — 1
✅ le canal passe en coupé
✅ « perd la mesure et passe à la suiva… » : le journal dit « PERDUE » — 14:05  ✂ lien coupé14:10  ✘ PERDUE  la mesure n'existe plus nulle part
✅ « garde les mesures en file et les e… » : le journal dit « 2 en attente » — t au retour14:20  ⚠ en file (2 en attente) — elles partiront au retour
✅ « cesse d'arroser jusqu'au retour du… » : le journal dit « s'est ARRÊTÉ » — retour14:25  ✘ l'objet s'est ARRÊTÉ — et le réseau n'y était pour rien
✅ au rétablissement, ce qui était en attente repart — 0  🔌 lien rétabli14:35  ✔ 2 message(s) en attente envoyé(s) d'un coup
✅ verrou « coupe » ouvert
✅ verrou « file » ouvert
✅ lien rétabli : le message est reçu — "id":"jardin-cour","h":38,"u":"%","t":"14:07","pompe":false}
✅ bandeau de durée présent — ⏱ 2 séances de 55 min
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ encadré de sécurité présent
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ activité 0 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 1 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 2 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 3 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 4 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 5 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ une réponse fausse est refusée — 🟡 2/3 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a1msg = {"id":"jardin-cour","h":38,"u":"%","t":"14:07","pompe":false}
✅ les verrous survivent au rechargement
✅ les champs cochés survivent au rechargement
✅ la page enregistre sous sa propre clé — seq_4e_C7_8
✅ première ouverture : la clé propre est créée, rien sous seq_4e_C7_4
✅ migration : la page se recharge sans erreur JS
✅ migration : chaque réponse de seq_4e_C7_4 apparaît à sa place, bilan compris — hyp=Le jardin doit · hors=garde les mesu · a3ph=Hors ligne, le · reinv=Avec trois jar · bilan=Je sais compos
✅ migration : les cases cochées reviennent
✅ migration : l’idée de départ est rappelée au bilan
✅ migration : les verrous sont conservés
✅ migration : copie sans effacer — seq_4e_C7_4 est intacte
✅ écrire dans 4e_C7.8 ne modifie plus seq_4e_C7_4
✅ … et ce qui est écrit va sous seq_4e_C7_8
✅ migration une seule fois : 4e_C7.8 ne relit plus seq_4e_C7_4 — Nouvelle idée, écrite dans 4e_C7.8.
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
✅ 20 questions sur 4e_C7.8 — {"4e_C7.8":20,"4e_C1.4":10}
✅ 10 questions sur 4e_C1.4 — {"4e_C7.8":20,"4e_C1.4":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 3.7
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
✅ le lien vers la séquence pointe le bon fichier — sequence_4e_C7.8_le-jardin-publie.html
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

## Reprise du 04/11/2026 — la séquence passe à deux séances à onglets (vague C7 de la règle d'or n°311)

Découpage, volet « 📖 Rappel » et clôture complétée : voir la fiche pédagogique.

- `node tests_regle_311_4e_C7.8.mjs` : 16 / 16 « l'outil suit la séance » (un seul nœud ; à sa place à la séance 1 ; juste après l'en-tête à la séance 2, état gardé ; onglets et en-tête dans le premier écran à 1280 px ; retour à sa place ; rechargement ; sans JavaScript, à sa place), relais 8 / 8, banc commun **34 / 34**.
- `tests_4e_C7.8_sequence.mjs` : **46 / 46**, avant comme après (le banc ouvre la séance qui porte chaque champ, comme l'élève ; la migration de l'ancienne clé passe toujours) ; `tests_4e_C7.8_qcm.mjs` : **32 / 32**.
- `controle_squelette.mjs` : 0 défaut (D1 à D6), aucun « à rédiger », aucun signalement.
- `banc_papier.py` : une fiche par séance (deux fiches), aucun texte pâle, aucun champ d'écran imprimé.
- Sorties inchangées : `controle_impression`, `controle_impression_papier`, `controle_verrous`, `controle_hors_ligne`,
  `controle_contraste_liens`, `controle_regles_visibles`, `controle_liens`, `controle_hierarchie`, `controle_unites`,
  `controle_sigles`, `controle_navigation_seances` ; `verif_regles_audit.py` : autant de ✘ qu'avant, aucun nouveau.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle. Non fait : le lexique par séance.

## 10/11/2026 — V2 de la boucle d'audit (4e) : gabarit commun (n°306), groupes de boutons radio (n°300), grilles

Page migrée par `_outils/migrer_gabarit_306.py` (rejouable depuis `main`, résultat identique octet pour octet) : chaque
question posée par une liste déroulante devient un `fieldset.qcm-groupe` ; mode essentiel (n°29), bandeau des tâches
(n°30), versions étayées `etayage_sequence_4e_C7.8_….json` (n°31), `aria-label` des zones de texte (n°34). Les questions
qui partagent leurs réponses se lisent en grille (`_outils/grilles_radio.py` : 1 grille(s), 4 questions) — les
réponses une fois, lettrées ; chaque question, une rangée de lettres. Le lien de la licence (pied de page, #616) restait au bleu par défaut du navigateur (2,03:1) : la règle `a,a:where(:visited){color:#9ecbff}` des pages sœurs est posée (n°303).

Les bancs n'ont pas changé de questions : shim `_groupesRadio(page)` en tête de `tests_4e_C7.8_sequence.mjs`.

Exécuté le 10/11/2026 (Chromium Playwright, session cloud) : `tests_4e_C7.8_sequence.mjs` **46 / 46** ; `tests_4e_C7.8_qcm.mjs`
**32 / 32** ; `tests_regle_311_4e_C7.8.mjs` **34 / 34** ; `verif_regles_audit.py` **0 ✘** ; `controle_squelette`,
`controle_hors_ligne`, `controle_contraste_liens`, `controle_impression_papier`, `banc_papier.py --filtre 4e_C7.8`,
`controle_impression --muet`, `controle_regles_visibles`, `controle_liens`, `controle_tactile`, `controle_mode_essentiel`,
`controle_navigation_seances`, `controle_rapports_tests`, `controle_licence` : 0 refus. Captures 390 px avant/après/essentiel
dans `_outils/captures_v2_4e_2026-11-10/`. Non exécuté : vrai téléphone, Firefox, Safari, impression réelle.
