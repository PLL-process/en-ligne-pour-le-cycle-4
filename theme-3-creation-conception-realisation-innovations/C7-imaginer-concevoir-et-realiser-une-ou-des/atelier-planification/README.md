# Atelier — Le diagramme de planification des tâches (C7.1)

**Ce dossier n'est pas une séquence de plus.** C'est une ressource **transversale**, appelée depuis
les trois séquences C7.1 du thème, au moment du lancement de projet.

## Pourquoi il existe

Le programme 2024 nomme, dans les connaissances associées : « **Le diagramme de planification des
tâches : notion de tâches, durée et contraintes entre tâches.** » Le dépôt n'en contenait aucune
occurrence, alors que les trois codes C7.1 étaient revendiqués. La séquence de 3e, qui doit faire
*élaborer* un processus « avec des tâches identifiées », ne contenait pas une seule fois le mot
« tâche ».

## Où cliquer

| Fichier | Pour qui |
|---|---|
| `atelier_5e_C7.1_planification_taches.html` | **l'élève de 5e** — rappel spiralaire, les mots, suivre un planning, le logiciel |
| `atelier_4e_C7.1_planification_taches.html` | **l'élève de 4e** — rappel spiralaire, les mots, organiser les tâches, le logiciel |
| `atelier_3e_C7.1_planification_taches.html` | **l'élève de 3e** — rappel spiralaire, les mots, élaborer le processus, le logiciel |
| `qcm_C7.1_planification_taches.html` | l'élève — 30 questions, 10 par niveau, 5 illustrées |
| `Synthèses/synthese_eleve_C7.1_planification.html` | l'élève — à imprimer, à coller |
| `Synthèses/synthese_professeur_C7.1_planification.html` | **le professeur** — déroulé, corrigés, pièges |
| `fiche_pedagogique_C7.1_planification.md` | le professeur — la fiche de préparation |

## Les trois parcours

| Niveau | Verbe du référentiel | Reçoit | Produit |
|---|---|---|---|
| 5e | **suivre** | un planning déjà fait | un point d'avancement qui dit ce que le retard décale |
| 4e | **organiser** | les tâches et leurs durées | les dates au plus tôt, et une décision d'équipe |
| 3e | **élaborer** | le projet seul | le chemin le plus long, et une tâche où se précipiter ne sert à rien |

## Les codes couverts

`5e_C7.1`, `4e_C7.1`, `3e_C7.1` — **COUVERT** par cette ressource partagée ; le dossier principal de
chaque niveau reste celui de sa séquence, qui pointe ici.

## Comment on régénère

```bash
python3 _verifier_planning.py                 # recalcule et réécrit _corrige_calcule.json
python3 _generation/build_atelier.py          # réassemble la page de l'atelier
cd _generation && python3 build_qcm.py <gabarit> ../qcm_C7.1_planification_taches.html
node ../../../../_outils/fix_r.js ../qcm_C7.1_planification_taches.html 617
python3 tests_atelier_C7.1.py                 # 17 contrôles
```

Aucun nombre n'est écrit à la main dans les pages : durées, dates, marges, chemin le plus long et
durée totale viennent tous de `_corrige_calcule.json`, lui-même produit à partir du seul
`taches_projets_c7_simulees.csv`.

## Le logiciel

`jardin_connecte_brooklyn.gan` s'ouvre dans **GanttProject** (libre, GPL v3). Les cinq images du
dossier `Images/` sont de **vraies captures** de ce fichier, prises en français — conditions,
version et limites dans `SOURCES_MEDIAS.md`. Une **voie B sans ordinateur** existe pour toutes les
activités : bandes de papier, mêmes questions, même valeur.
