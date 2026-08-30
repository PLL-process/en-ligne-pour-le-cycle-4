# Rapport de tests — 5e_C8.1

Ce rapport ne déclare que des tests **réellement exécutés**, sous Chromium (Playwright), le
31/08/2026. Les attendus ne sont pas recopiés à la main : ils sont **engendrés par
`attendus.py`** depuis les modèles Python du lot. Un chiffre corrigé dans le modèle change
l'attendu ; si la page ne suit pas, le test tombe.

## Séquence — `tests_5e_C8.1_sequence.mjs`

    node tests_5e_C8.1_sequence.mjs sequence_5e_C8.1_patere-du-hall.html attendus_5e.json 5e

**39 / 39**. Ce que la suite vérifie :

- chargement sans erreur JavaScript, sans requête échouée, sans boîte modale ;
- **aucun verrou expérientiel ouvert à l'ouverture de la page** (règle d'or n°226) ;
- chaque activité verrouillée **refuse** avant le geste, et l'écrit à l'élève ;
- aucun identifiant HTML en double ; un seul bouton vers le QCM ; hypothèse d'entrée présente ;
- le bandeau de durée annonce **plus** de temps que les activités n'en demandent (110 min annoncés, 85 demandés, +25) ;
- la formulation officielle du code **et celle du code d'appui** sont recopiées exactement —
  comparées au référentiel `_outils/data_competences.py`, pas à ma mémoire ;
- la consigne de sécurité et l'écartement explicite du secteur sont présents ;
- les trois versions 🅰 🅱 🅲 sont annoncées ; aucun marqueur de gabarit ne subsiste ;
- **le simulateur calcule ce que le modèle Python calcule**, valeur par valeur ;
- les 5 activités se valident intégralement avec les réponses attendues ;
- une réponse fausse est refusée et le dit ;
- réponses, verrous et état du simulateur survivent au rechargement ; l'hypothèse est rappelée
  au bilan.

## QCM — `tests_5e_C8.1_qcm.mjs`

    node tests_5e_C8.1_qcm.mjs qcm_5e_C8.1_patere-du-hall.html 5e_C8.1 … sequence…

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
| `_outils/controle_echantillonnage.py` | `5e_C8.1` : 20 q · code d'appui : 10 q — les deux au-dessus du seuil |
| `_outils/mesurer_temps_seances.py` | 110 min annoncés, 85 demandés, +25 |
| `_outils/controle_couverture.py` | `5e_C8.1` → **ÉVALUÉ** |

## Ce qui n'a pas été testé

- Le rendu à l'impression A4 n'a pas été vérifié automatiquement.
- Les lecteurs d'écran n'ont pas été essayés : l'accessibilité repose sur les `label`, les
  `title`/`desc` des SVG et le signalement non chromatique, contrôlés à la lecture.
- Aucun essai avec des élèves n'a encore eu lieu.
