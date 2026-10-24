# Atelier « La carte mentale » — La carte mentale, aussi appelée carte heuristique (mind map en anglais)

Le programme de technologie ne donne pas de nom à ce schéma : il demande d'exprimer et de structurer sa pensée avec des outils de représentation, et de classer des données. On l'appelle carte mentale, ou carte heuristique (du grec heuriskein, « trouver ») ; en anglais, mind map. Si tu rencontres l'un de ces noms, tu sauras que c'est le même schéma : une idée centrale, des branches, des feuilles.

## Les pages

| Page | Rôle |
|---|---|
| `atelier_5e_carte-mentale.html` | l'atelier de 5e |
| `atelier_4e_carte-mentale.html` | l'atelier de 4e |
| `atelier_3e_carte-mentale.html` | l'atelier de 3e |
| `qcm_carte-mentale.html` | le QCM (30 questions fixes) |
| `Synthèses/synthese_eleve_carte-mentale.html` | la synthèse élève (le cours, à retenir, les mots) |
| `Synthèses/synthese_professeur_carte-mentale.html` | la synthèse professeur |
| `fiche_pedagogique_carte-mentale.md`, `matrice_couverture_carte-mentale.csv` | gouvernance |
| `rapport_tests_carte-mentale.md`, `manifest_carte-mentale.json` | tests exécutés, inventaire |
| `Images/`, `SOURCES_MEDIAS.md` | schémas SVG originaux et leur provenance |

## Où chaque code est servi

| Niveau | Code | Page-pointeur | Séquence du code |
|---|---|---|---|
| 5e | 5e_C1.4 | `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.4/atelier_atelier_carte_mentale.html.html` | `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.3/sequence_C1.3-C1.4_SI_gestion_donnees.html` |
| 4e | 4e_C1.2 | `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.2/atelier_atelier_carte_mentale.html.html` | `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.1/sequence_4e_C1.1-C1.3_tsinghua_feux.html` |
| 3e | 3e_C1.3 | `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/3e/3e_C1.3/atelier_atelier_carte_mentale.html.html` | `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/3e/3e_C1.5/sequence-numerique-societe-economie-environnement-sante.html` |

## Exercices insérés dans des séquences

| Séquence | Niveau | Exercices |
|---|---|---|
| `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.3/sequence_C1.3-C1.4_SI_gestion_donnees.html` | 5e | e1 |
| `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/3e/3e_C1.5/sequence-numerique-societe-economie-environnement-sante.html` | 3e | e5 |
| `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.1/sequence_4e_C1.1-C1.3_tsinghua_feux.html` | 4e | e3, e4 |

Ne pas modifier ces pages à la main : elles sont produites par `../_generation/` (`python3 build.py carte_mentale`, `python3 build_qcm.py carte_mentale`, `python3 gouvernance.py carte_mentale`).
