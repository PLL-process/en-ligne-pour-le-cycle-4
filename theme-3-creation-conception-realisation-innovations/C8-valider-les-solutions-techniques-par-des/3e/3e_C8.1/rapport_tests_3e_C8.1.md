# Rapport de tests — 3e_C8.1

> **Révision du 15/11/2026.** Propositions fausses allongées (la bonne réponse se devinait à sa place et à sa longueur), places changées, piqûre de rappel et Bonus repliés, aération. Bancs : séquence **62 / 62**, QCM **32 / 32**, n°311 **34 / 34**. Mode mission (`banc_generique.mjs`) : 28 écrans, 44 / 44 pourquoi, aucun refus.

Ce rapport ne déclare que des tests **réellement exécutés**, sous Chromium (Playwright), le
31/08/2026. Les attendus ne sont pas recopiés à la main : ils sont **engendrés par
`attendus.py`** depuis les modèles Python du lot. Un chiffre corrigé dans le modèle change
l'attendu ; si la page ne suit pas, le test tombe.

## Séquence — `tests_3e_C8.1_sequence.mjs`

    node tests_3e_C8.1_sequence.mjs sequence_3e_C8.1_mat-de-la-station.html attendus_3e.json 3e

**62 / 62**. Ce que la suite vérifie :

- chargement sans erreur JavaScript, sans requête échouée, sans boîte modale ;
- **aucun verrou expérientiel ouvert à l'ouverture de la page** (règle d'or n°226) ;
- chaque activité verrouillée **refuse** avant le geste, et l'écrit à l'élève ;
- aucun identifiant HTML en double ; un seul bouton vers le QCM ; hypothèse d'entrée présente ;
- le bandeau de durée annonce **plus** de temps que les activités n'en demandent (165 min annoncés, 135 demandés, +30) ;
- la formulation officielle du code **et celle du code d'appui** sont recopiées exactement —
  comparées au référentiel `_outils/data_competences.py`, pas à ma mémoire ;
- la consigne de sécurité et l'écartement explicite du secteur sont présents ;
- les trois versions 🅰 🅱 🅲 sont annoncées ; aucun marqueur de gabarit ne subsiste ;
- **le simulateur calcule ce que le modèle Python calcule**, valeur par valeur ;
- les 5 activités se valident intégralement avec les réponses attendues ;
- une réponse fausse est refusée et le dit ;
- réponses, verrous et état du simulateur survivent au rechargement ; l'hypothèse est rappelée
  au bilan.

## QCM — `tests_3e_C8.1_qcm.mjs`

    node tests_3e_C8.1_qcm.mjs qcm_3e_C8.1_mat-de-la-station.html 3e_C8.1 3e_C3.4 sequence_3e_C8.1_mat-de-la-station.html

**32 / 32**. Ce que la suite vérifie : 30 questions, 4 options et 3 réfutations chacune,
la bonne réponse sans réfutation, tous les champs du gabarit remplis, la répartition des bonnes
réponses (8/7/7/8), aucune bonne réponse détachée par sa longueur, la correction qui déplie les
trois réfutations et porte un « à retenir », les deux confirmations sans boîte modale, la note
20/20 sur un parcours complet, le lien vers la séquence, et la persistance au rechargement.

## Outils du dépôt

| Outil | Résultat |
|---|---|
| `_outils/fix_r.js` | répartition 8/7/7/8, `d[r]` vide partout |
| `_outils/sans_modale.py` | rien à faire — aucune boîte modale |
| `_outils/controle_longueurs.py` | 0 bonne réponse détachée (0 %) |
| `_outils/controle_echantillonnage.py` | `3e_C8.1` : 20 q · code d'appui : 10 q — les deux au-dessus du seuil |
| `_outils/mesurer_temps_seances.py` | 165 min annoncés, 135 demandés, +30 |
| `_outils/controle_couverture.py` | `3e_C8.1` → **ÉVALUÉ** |

## Ce qui n'a pas été testé

- Le rendu à l'impression A4 n'a pas été vérifié automatiquement.
- Les lecteurs d'écran n'ont pas été essayés : l'accessibilité repose sur les `label`, les
  `title`/`desc` des SVG et le signalement non chromatique, contrôlés à la lecture.
- Aucun essai avec des élèves n'a encore eu lieu.

## Reprise du 04/11/2026 — la séquence passe à onglets (vague de la règle d'or n°311)

Trois séances à onglets (squelette n°306), sur le modèle du pilote 4e_C8.1 : séance 1 = ouverture + activité 1 ;
séance 2 = activités 2 et 3 ; séance 3 = activité 4, réinvestissement, synthèse, Bonus, bilan, QCM. L'ouverture est
repliée dans le volet « 📖 Rappel » dès la séance 2. Le simulateur, qui sert aux activités 1 à 4, sort de l'activité 1 ;
le script des onglets le place dans la séance ouverte, juste après son en-tête. Clôture complétée : un corrigé par défi du Bonus, « Comment j'ai travaillé », « Je me
positionne » sur 3e_C8.1 (quatre niveaux du livret) et 3e_C3.4.

- `node tests_regle_311_3e_C8.1.mjs` : l'outil suit la séance 12 / 12 (un seul nœud, après l'en-tête, état gardé,
  onglets et en-tête dans le premier écran, sans JavaScript à sa place), puis relais 8 / 8 et banc commun **34 / 34**.
- `node tests_3e_C8.1_sequence.mjs … attendus_3e.json 3e` : **62 / 62**, comme avant ; le banc ouvre la séance qui porte
  chaque champ, comme l'élève (`ouvrirSeanceDe`). `tests_3e_C8.1_qcm.mjs` : 32 / 32, comme avant.

Contrôles du dépôt, sur ce dossier ou sur tout le dépôt : `controle_squelette` 0 défaut (D1 à D6), aucun « à rédiger »,
aucun signalement ; `controle_impression` (0 page refusée), `controle_verrous`, `controle_hors_ligne`,
`controle_contraste_liens`, `controle_regles_visibles`, `controle_liens`, `controle_navigation_seances`,
`controle_hierarchie`, `controle_unites`, `controle_sigles`, `controle_impression_papier` : verts. `banc_papier.py` :
3 fiches, 6 pages, une séance par fiche, 0 texte pâle, 0 champ d'écran imprimé. `verif_regles_audit.py` : les mêmes ✘ qu'avant
(n°29, 30, 31, 34, 300), hors périmètre de cette vague.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.

## 08/11/2026 — V2 de la boucle d'audit : gabarit commun (n°306) et groupes de boutons radio (n°300)

Page migrée par `_outils/migrer_gabarit_306.py` (rejouable depuis `main`, résultat identique octet pour octet) : chaque
question posée par une liste déroulante devient un `fieldset.qcm-groupe` qui porte sa valeur ; bouton « mode essentiel »
(n°29), bandeau des tâches (n°30), versions étayées `etayage_sequence_3e_C8.1_….json` (n°31), `aria-label` sur les zones de
texte (n°34). Les listes d'interface (`data-interface` : commandes du simulateur, ports de l'établi) restent des menus.

Les bancs n'ont pas changé de questions : un shim `_groupesRadio(page)` en tête de `tests_3e_C8.1_sequence.mjs` fait
porter `selectOption` / `fill` / `inputValue` sur le groupe (valeur ou libellé, `{index}` accepté), comme sur l'ancienne
liste. Adaptations du banc : la liste des propositions se lit sur `option` **ou** `input[type=radio]` (la réponse fausse est prise parmi les boutons).

Exécuté le 08/11/2026 (Chromium Playwright, session cloud) : `tests_3e_C8.1_sequence.mjs` **62 / 62** ; `tests_3e_C8.1_qcm.mjs`
**32 / 32** ; `tests_regle_311_3e_C8.1.mjs` **34 / 34** ; `verif_regles_audit.py` **0 ✘** sur la page ; `controle_squelette`,
`controle_hors_ligne`, `controle_contraste_liens`, `controle_impression_papier`, `banc_papier.py --filtre 3e_C8.1`,
`controle_impression --muet`, `controle_regles_visibles`, `controle_liens`, `controle_tactile`, `controle_mode_essentiel`,
`controle_navigation_seances`, `controle_verrous`, `controle_rapports_tests` : 0 refus. Captures 390 px avant/après/essentiel
dans `_outils/captures_v2_3e_2026-11-08/`. Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.

## 22/11/2026 — Trois explications écrites après le réinvestissement (règle d'or n°346)

La séance 3 finissait sans aucune réponse écrite (0 zone de texte, 6 groupes de boutons radio). Après le réinvestissement
du quai du port, une carte « ✍️ Explique comme au brevet — sans propositions » (~10 min, faisable à la maison) : les
données sous les yeux (le tube aluminium Ø50 × 3 à 150 km/h, coefficient 3,4 et flèche 27 mm ; le cahier des charges,
coefficient d'au moins 3 et flèche de 40 mm au plus ; le vent de 180 km/h au port ; la formule de la pression, ses
lettres expliquées), trois questions — pourquoi la pression est multipliée par 1,44 et non 1,2 ; le coefficient
(3,4 ÷ 1,44 ≈ 2,4, sous 3) et la flèche (27 × 1,44 ≈ 39 mm, sous 40) au port, et la conclusion : le tube ne convient plus ;
ce qu'on dit à la mairie, et la fatigue qui reste à étudier —, une version étayée par question, deux aides (n°367),
une correction avec trois phrases de copie (n°356), une grille à trois critères. Rien n'est noté (n°340) ; la carte est
hors de la zone de vérification du réinvestissement ; les cases de la grille sont sauvegardées avec le travail.

| Contrôle | Sortie | Résultat |
|---|---|---|
| `_outils/tests_ecrit_brevet.py` (banc commun des écrits) | 0 | 11 / 11 |
| `node tests_3e_C8.1_sequence.mjs sequence_3e_C8.1_mat-de-la-station.html attendus_3e.json 3e` | 0 | 62 / 62 |
| `tests_regle_311_3e_C8.1.mjs` | 0 | 34 / 34 |
| `mode_mission/banc_generique.mjs` | 0 | aucun refus |
| `controle_page_ouverte.mjs`, `controle_impression.mjs`, `controle_hors_ligne.mjs`, `controle_squelette.mjs` | 0 | rien à signaler |
| `controle_regles_visibles`, `controle_hierarchie`, `controle_consignes_a_la_ligne`, `controle_propositions_indices`, `controle_tactile`, `controle_validations`, `controle_debordement`, `eleve_qui_ne_lit_pas.py` | 0 | rien à signaler |

Revue d'écran à 390 px : le texte d'exemple de la question 1 donnait la réponse (« 1,44 ») : retiré (n°341) ; la lettre
ρ de la formule est expliquée.

**Non vérifié** : la durée réelle (~10 min annoncées) ; un essai en classe.

