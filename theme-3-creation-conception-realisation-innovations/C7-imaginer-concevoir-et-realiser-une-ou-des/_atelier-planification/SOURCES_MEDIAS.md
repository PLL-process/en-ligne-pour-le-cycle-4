# Sources des médias — Atelier de planification des tâches (C7.1)

## Les quatre schémas d'interface

| Fichier | Nature | Licence |
|---|---|---|
| `Images/ganttproject_1_saisir_les_taches.svg` | **Schéma original reconstruit** | CC0 — dépôt |
| `Images/ganttproject_2_declarer_les_dependances.svg` | **Schéma original reconstruit** | CC0 — dépôt |
| `Images/ganttproject_3_lire_le_diagramme.svg` | **Schéma original reconstruit** | CC0 — dépôt |
| `Images/ganttproject_4_chemin_le_plus_long.svg` | **Schéma original reconstruit** | CC0 — dépôt |

### Ce que « reconstruit » veut dire, et pourquoi

**Ce ne sont pas des captures d'écran.** GanttProject n'est ni dans les dépôts de paquets de
l'environnement de production, ni téléchargeable depuis celui-ci. Les quatre schémas sont **dessinés
à la main en SVG**, à partir de la documentation officielle du logiciel, selon le même principe que
les schémas de réseau du Thème 2 (règle d'or n°1).

Chaque schéma **porte la mention** « schéma reconstruit de l'interface — ce n'est pas une capture
d'écran », visible sous son titre. Un élève ne doit jamais croire qu'il regarde une photographie de
son écran : ce qu'il voit est une **carte** de l'interface, pas son portrait.

### Ce qui a été vérifié, et ce qui ne l'a pas été (règle n°47)

**Vérifié** dans la documentation officielle de GanttProject :
les colonnes de la table des tâches (*Name, Begin date, End date, Duration*, et *Predecessors* parmi
les colonnes ajoutables) · la création d'une tâche par *Tasks → New task* · la case *Milestone* dans
les propriétés · la déclaration d'une dépendance par glisser-déposer d'une barre à l'autre **ou** par
l'onglet *Predecessors* · le type de lien *Finish-Start* · la case *Show critical path* du menu
*Gantt view* · les deux onglets *Gantt* et *Resources chart*.

**Non vérifié, parce que le logiciel n'a pas pu être ouvert** : l'**apparence exacte** — couleurs des
barres, rendu précis de la mise en évidence du chemin critique, position des panneaux, police. La
documentation consultée décrit un rendu par hachures ; d'autres versions emploient une couleur pleine.
Les schémas emploient donc des hachures, **et l'atelier ne fait jamais dépendre une consigne de la
couleur** : on dit « les tâches mises en évidence », jamais « les tâches en rouge ».

**Conséquence pratique** : si la version installée au collège diffère, les **gestes** restent justes
— ce sont eux que les schémas enseignent — et seule l'apparence changera.

## Le jeu de données

`taches_projets_c7_simulees.csv` — **données simulées**, construites pour l'atelier. Elles décrivent
les trois projets réellement menés dans les séquences C7.1 du dépôt (l'indicateur de rangement du
hall en 5e, le jardin connecté de Brooklyn en 4e, le capteur de confort en 3e), mais les durées sont
des estimations pédagogiques et ne proviennent d'aucun relevé.

Toutes les valeurs affichées dans les schémas — dates, marges, chemin le plus long, durée totale —
sont **calculées** par `_verifier_planning.py` à partir de ce seul fichier, jamais recopiées à la
main (règles n°48 et n°54).

## Le logiciel lui-même

GanttProject est un logiciel **libre** (GPL). Il n'est pas redistribué ici : l'atelier renvoie
l'enseignant vers le site officiel du projet pour l'installation.
