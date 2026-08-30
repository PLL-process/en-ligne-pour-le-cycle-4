# 3e_C8.1 — Mettre en œuvre une simulation pour valider la tenue mécanique d’un matériau.

> Mettre en œuvre une simulation pour valider la tenue mécanique d’un matériau.
>
> Programme 2024 · cycle 4 · thème 3 · socle D1.3, D2, D4, D5

## Le lot « Le mât de la station — la simulation avant le banc »

Le bureau d'études conteste la méthode, pas la conclusion : le banc de `3e_C8.2` poussait
100 N en tête de **chaque** mât, alors que le vent ne pousse pas de la même façon
sur un tube de 50 mm et sur une barre de 20. Ce lot fait régler la simulation par l'élève, et
lui fait découvrir de combien le banc s'était trompé de charge.

| Pièce | Fichier |
|---|---|
| Séquence (3 × 55 min) | [`sequence_3e_C8.1_mat-de-la-station.html`](sequence_3e_C8.1_mat-de-la-station.html) |
| QCM (30 questions) | [`qcm_3e_C8.1_mat-de-la-station.html`](qcm_3e_C8.1_mat-de-la-station.html) |
| Synthèse élève | [`Synthèses/synthese_eleve_3e_C8.1.html`](Synthèses/synthese_eleve_3e_C8.1.html) |
| Synthèse professeur | [`Synthèses/synthese_professeur_3e_C8.1.html`](Synthèses/synthese_professeur_3e_C8.1.html) |
| Fiche pédagogique | [`fiche_pedagogique_3e_C8.1.md`](fiche_pedagogique_3e_C8.1.md) |
| Matrice de couverture | [`matrice_couverture_3e_C8.1.csv`](matrice_couverture_3e_C8.1.csv) |
| Lexique | [`lexique_3e_C8.1.html`](lexique_3e_C8.1.html) |
| Rapport de tests | [`rapport_tests_3e_C8.1.md`](rapport_tests_3e_C8.1.md) |
| Modèle de calcul | [`mat_station.py`](mat_station.py) |

## Ce que le lot démontre

| Profilé | Moment du banc | Moment du vent | Écart |
|---|---|---|---|
| Tube aluminium Ø50 × 3 | 200 N·m | 204 N·m | +2 % |
| Barre pleine acier Ø20 | 200 N·m | 128 N·m | -36 % |
| Tube PVC Ø50 × 3 | 200 N·m | 204 N·m | +2 % |
| Poutre bois 40 × 40 | 200 N·m | 298 N·m | +49 % |
| Tube acier galvanisé Ø33,7 × 2,6 | 200 N·m | 163 N·m | -19 % |

Douze réglages possibles (3 hauteurs × 2 cas de charge × 2 limites), tous vérifiés par le banc de
tests contre le modèle Python. Le réglage conforme au cahier des charges —
2000 mm, vent, limite élastique — retient le
Tube aluminium Ø50 × 3, comme le banc, mais pour des raisons que le banc ne pouvait pas donner.

## Codes travaillés

| Code | Rôle | Questions |
|---|---|---|
| `3e_C8.1` | principal | 20 |
| `3e_C3.4` | appui — *définir et mettre en œuvre un protocole pour mesurer une caractéristique, une performance d’un ost.* | 10 |

## À faire avant

`3e_C8.2` « Le mât de la station — proposer un protocole » : ce lot en reprend les cinq
profilés, leurs géométries et leurs résistances à la rupture, et y ajoute la limite élastique.
