# Atelier « Le croquis » — Le croquis, souvent appelé croquis à main levée

Dans le programme de technologie, ce dessin s'appelle simplement le croquis. Dans les ateliers et les bureaux d'études, on dit souvent croquis à main levée : dessiné sans règle, en quelques minutes. Un croquis qui porte des dimensions est un croquis coté ; une suite de croquis numérotés qui raconte un usage est un storyboard. Si tu rencontres l'un de ces noms, tu sauras que c'est la même famille de dessins.

## Les pages

| Page | Rôle |
|---|---|
| `atelier_4e_croquis.html` | l'atelier de 4e |
| `atelier_3e_croquis.html` | l'atelier de 3e |
| `qcm_croquis.html` | le QCM (30 questions fixes) |
| `Synthèses/synthese_eleve_croquis.html` | la synthèse élève (le cours, à retenir, les mots) |
| `Synthèses/synthese_professeur_croquis.html` | la synthèse professeur |
| `fiche_pedagogique_croquis.md`, `matrice_couverture_croquis.csv` | gouvernance |
| `rapport_tests_croquis.md`, `manifest_croquis.json` | tests exécutés, inventaire |
| `Images/`, `SOURCES_MEDIAS.md` | schémas SVG originaux et leur provenance |

## Où chaque code est servi

| Niveau | Code | Page-pointeur | Séquence du code |
|---|---|---|---|
| 4e | 4e_C2.1 | `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/4e/4e_C2.1/atelier_atelier_croquis.html.html` | `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/4e/4e_C2.1/sequence_4e_C2_hangzhou_borne.html` |
| 4e | 4e_C7.2 | `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.2/atelier_atelier_croquis.html.html` | `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.1/sequence_4e_C7_jardin-conception.html` |
| 3e | 3e_C7.2 | `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.2/atelier_atelier_croquis.html.html` | `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/sequence_3e_C7_capteur-confort-ny.html` |

## Exercices insérés dans des séquences

| Séquence | Niveau | Exercices |
|---|---|---|
| `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/4e/4e_C2.1/sequence_4e_C2_hangzhou_borne.html` | 4e | e1 |

Ne pas modifier ces pages à la main : elles sont produites par `../_generation/` (`python3 build.py croquis`, `python3 build_qcm.py croquis`, `python3 gouvernance.py croquis`).
