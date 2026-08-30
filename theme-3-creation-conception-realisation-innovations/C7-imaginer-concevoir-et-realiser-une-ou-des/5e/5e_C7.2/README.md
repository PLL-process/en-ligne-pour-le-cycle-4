# 5e_C7.2 — Fabriquer une solution pour améliorer un OST existant

> Fabriquer une solution pour améliorer un OST existant.
>
> Programme 2024 · cycle 4 · thème 3 · socle D2, D3, D4

## Le lot « Le dé, en mieux »

Ce code n'était évalué **nulle part** dans le dépôt — et il n'y était pas vraiment enseigné
non plus. Le TP nº1 « Le dé » l'avait annoncé sans l'écrire : *« une calotte demanderait de
soustraire une sphère, et ça, c'est un geste d'après »*. Ce lot est ce geste d'après.

L'élève reprend **son** dé, garde la version d'avant, remplace **un** creux à fond plat par une
vraie calotte — puis décide si l'amélioration vaut d'être répétée vingt fois.

| Pièce | Fichier |
|---|---|
| TP (≈ 40 min) | [`tp_5e_de_calottes.html`](../../atelier-cao/tp_5e_de_calottes.html) — dans l'atelier, non dupliqué ici |
| QCM (30 questions) | [`qcm_5e_C7.2_le-de-ameliore.html`](qcm_5e_C7.2_le-de-ameliore.html) |
| Synthèse élève | [`Synthèses/synthese_eleve_5e_C7.2.html`](Synthèses/synthese_eleve_5e_C7.2.html) |
| Synthèse professeur | [`Synthèses/synthese_professeur_5e_C7.2.html`](Synthèses/synthese_professeur_5e_C7.2.html) |
| Fiche pédagogique | [`fiche_pedagogique_5e_C7.2.md`](fiche_pedagogique_5e_C7.2.md) |
| Matrice de couverture | [`matrice_couverture_5e_C7.2.csv`](matrice_couverture_5e_C7.2.csv) |
| Lexique | [`lexique_5e_C7.2.html`](lexique_5e_C7.2.html) |
| Rapport de tests | [`rapport_tests_5e_C7.2.md`](rapport_tests_5e_C7.2.md) |
| Modèle de calcul | [`calotte.py`](calotte.py) |
| Suite de tests | [`tests_5e_C7.2_qcm.mjs`](tests_5e_C7.2_qcm.mjs) |

## Ce que le modèle donne

| Bille | Centre au-dessus de la face | Creux obtenu | Matière retirée |
|---|---|---|---|
| Ø10 | 3,5 mm | Ø7,14 | 31,8 mm³ |
| Ø20 | 8,5 mm | Ø10,54 | 67,2 mm³ |
| Ø30 | 13,5 mm | Ø13,08 | 102,5 mm³ |

Retenue : **Ø20**, soit un creux de **Ø10,54** — 0,54 mm de plus que les
Ø10 d'aujourd'hui. Le dé garde son allure ; il ne gagne que la douceur du fond. Et la
calotte retire **43 % de matière en moins** que le cylindre, parce qu'elle se referme
vers le bas.

## Codes travaillés

| Code | Rôle | Questions |
|---|---|---|
| `5e_C7.2` | principal | 30 |

## Ce que ce README remplace

Ce dossier portait un **pointeur** engendré par `_outils/pointeurs_codes.py`, qui renvoyait au
mini-projet de `5e_C7.1` et disait la vérité de l'époque : « ce code y est enseigné, et il n'y
est pas évalué ». La suite est plus nuancée — le mini-projet enseigne bien l'amélioration d'un
objet scolaire, mais il s'arrête **avant** de fabriquer. Le geste manquait ; il est ici.

*L'entrée `5e_C7.2` de la table `POINTEURS` doit être retirée en conséquence. Elle vit dans
`_outils/`, hors du périmètre d'une branche de thème 3 : elle part dans une livraison à part.
En attendant, `pointeurs_codes.py` signale ce dossier comme « ayant grandi » et n'écrase rien.*
