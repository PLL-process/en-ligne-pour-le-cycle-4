# Rapport de tests — 3e_C8.1

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

    node tests_3e_C8.1_qcm.mjs qcm_3e_C8.1_mat-de-la-station.html 3e_C8.1 … sequence…

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
