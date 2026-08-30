# 5e_C8.1 — Utiliser une simulation fournie pour valider la tenue mécanique d’un matériau.

> Utiliser une simulation fournie pour valider la tenue mécanique d’un matériau.
>
> Programme 2024 · cycle 4 · thème 3 · socle D1.3, D2, D4

## Le lot « La patère du hall — ce que la simulation voyait »

Le gestionnaire du collège avait écrit que ses crochets **pliaient**. Le banc de `5e_C8.2`,
lui, avait mesuré à quelle charge ils **cassent**. Ce lot met une simulation entre les deux et
montre que ce ne sont pas les mêmes chiffres — ni les mêmes conclusions.

| Pièce | Fichier |
|---|---|
| Séquence (2 × 55 min) | [`sequence_5e_C8.1_patere-du-hall.html`](sequence_5e_C8.1_patere-du-hall.html) |
| QCM (30 questions) | [`qcm_5e_C8.1_patere-du-hall.html`](qcm_5e_C8.1_patere-du-hall.html) |
| Synthèse élève | [`Synthèses/synthese_eleve_5e_C8.1.html`](Synthèses/synthese_eleve_5e_C8.1.html) |
| Synthèse professeur | [`Synthèses/synthese_professeur_5e_C8.1.html`](Synthèses/synthese_professeur_5e_C8.1.html) |
| Fiche pédagogique | [`fiche_pedagogique_5e_C8.1.md`](fiche_pedagogique_5e_C8.1.md) |
| Matrice de couverture | [`matrice_couverture_5e_C8.1.csv`](matrice_couverture_5e_C8.1.csv) |
| Lexique | [`lexique_5e_C8.1.html`](lexique_5e_C8.1.html) |
| Rapport de tests | [`rapport_tests_5e_C8.1.md`](rapport_tests_5e_C8.1.md) |
| Modèle de calcul | [`patere.py`](patere.py) · [`simulateur.py`](simulateur.py) |

## Ce que le lot démontre

| Matériau | Plie à | Casse à | k élastique | k rupture | Décision |
|---|---|---|---|---|---|
| Bois (pin) | 25 kg | 41 kg | 2,1 | 3,4 | **écarté** |
| PLA imprimé en 3D | 46 kg | 51 kg | 3,8 | 4,2 | retenu |
| PVC rigide | 46 kg | 53 kg | 3,8 | 4,4 | retenu |
| Aluminium | 143 kg | 194 kg | 11,9 | 16,1 | retenu |
| Acier doux | 240 kg | 408 kg | 20,0 | 34,0 | retenu |

Sous les 12 kg de service, la contrainte vaut
11,8 MPa **pour les cinq** : elle ne dépend pas du
matériau. Un seul matériau change de décision selon la limite retenue — le bois.

## Codes travaillés

| Code | Rôle | Questions |
|---|---|---|
| `5e_C8.1` | principal | 20 |
| `5e_C3.1` | appui — *repérer pour un ost les matériaux, les sources et les formes d’énergies, le traitement de l’information.* | 10 |

## Ce que ce README remplace

Ce dossier portait un **pointeur** engendré par `_outils/pointeurs_codes.py`, qui renvoyait au
mini-projet de `5e_C7.1` et affirmait « ce code y est évalué ». C'était inexact : la banque de ce
lot étiquette son groupe de validation en `5e_C8.3`, jamais en `5e_C8.1`, et
`_outils/controle_couverture.py` ne trouvait **aucune question** portant `5e_C8.1` dans tout le
dépôt. Le mini-projet reste une excellente entrée sur la validation ; il ne portait simplement
pas ce code-là.

*La table `POINTEURS` de `_outils/pointeurs_codes.py` doit être corrigée en conséquence — elle
vit hors du périmètre d'une branche de thème 3, et partira dans une livraison à part.*
