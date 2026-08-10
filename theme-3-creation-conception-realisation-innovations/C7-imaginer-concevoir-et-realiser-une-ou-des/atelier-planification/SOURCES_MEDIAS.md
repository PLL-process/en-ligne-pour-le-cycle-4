# Sources des médias — Atelier de planification des tâches (C7.1)

## Les cinq images de l'atelier

| Fichier | Nature | Origine |
|---|---|---|
| `Images/ganttproject_1_saisir_les_taches_et_les_durees.png` | **Capture d'écran réelle** | GanttProject 3.3, poste de l'enseignant, 9 août 2026 |
| `Images/ganttproject_2_proprietes_duree_de_la_tache.png` | **Capture d'écran réelle** | idem — boîte *Propriétés*, onglet *Général* |
| `Images/ganttproject_3_declarer_les_predecesseurs.png` | **Capture d'écran réelle** | idem — boîte *Propriétés*, onglet *Prédécesseurs* |
| `Images/ganttproject_4_les_barres_et_les_dates.png` | **Capture d'écran réelle** | idem — diagramme, chemin critique masqué |
| `Images/ganttproject_5_afficher_le_chemin_critique.png` | **Capture d'écran réelle** | idem — après clic sur *Afficher le chemin critique* |

### Ce que ces images sont, exactement

Ce sont de **vraies captures**, prises sur le logiciel réellement installé, et non des schémas
reconstruits. La version précédente de ce dossier contenait quatre schémas SVG dessinés à la main,
avec des libellés d'interface **en anglais** ; le logiciel du collège est **en français**. Ces quatre
schémas ont été supprimés : un élève qui cherche *Show critical path* dans une interface qui affiche
*Afficher le chemin critique* ne trouve rien, et croit que c'est lui qui se trompe.

Conditions de prise de vue, pour que l'enseignant puisse les refaire :

- **Logiciel** : GanttProject 3.3 (BarD Software s.r.o.), installé sous Windows, interface française.
- **Fichier ouvert** : `jardin_connecte_brooklyn.gan`, produit par ce dossier, engagé à côté de ce
  fichier. Les captures montrent donc **exactement** le projet que l'élève manipule.
- **Écran** : 3840 × 2160, captures recadrées sur la zone utile, aucune retouche du contenu — ni
  ajout de flèche, ni masquage, ni correction de texte. Le seul traitement est le recadrage et une
  réduction de taille.
- **Aucune donnée personnelle** n'apparaît : pas de nom d'utilisateur, pas de chemin de fichier
  personnel, pas de courriel. La barre de titre n'affiche que le nom du fichier de projet.

### Pourquoi une capture d'écran est acceptable ici, alors que la règle n°1 les proscrit

La règle d'or n°1 interdit les captures d'un **logiciel propriétaire** — elle est née de Cisco Packet
Tracer, dont l'interface ne peut pas être redistribuée. **GanttProject est un logiciel libre**, publié
sous licence GPL v3 par BarD Software s.r.o. Reproduire l'image de son interface dans un support
pédagogique est permis, et c'est même le seul moyen honnête de guider un geste : montrer le bouton
tel qu'il est, avec le mot qui est écrit dessus.

Le logo GanttProject visible dans l'en-tête de la table des tâches appartient à son éditeur et
n'est utilisé ici qu'incidemment, parce qu'il fait partie de l'écran capturé. Aucune image du dépôt
ne s'en sert comme illustration autonome.

Le logiciel lui-même n'est pas redistribué : l'atelier renvoie vers le site officiel du projet.

### Ce qui a été vérifié, et ce qui ne l'a pas été (règle n°47)

**Vérifié**, parce que constaté à l'écran sur les captures elles-mêmes :

- les menus **Projet · Éditer · Affichage · Tâches · Ressources · Aide** ;
- les deux onglets **Diagramme de Gantt** et **Diagramme des Ressources** ;
- les colonnes **Nom · Date de début · Date de fin · Durée** de la table des tâches ;
- la boîte **Propriétés pour …**, ses onglets **Général · Prédécesseurs · Ressources · Colonnes
  personnalisées**, son champ **Durée**, sa case **Jalon**, ses boutons **OK** et **Annuler** ;
- dans l'onglet *Prédécesseurs*, les colonnes **ID · Nom de la tâche · Relation · Retard ·
  Contrainte**, le type de lien **Fin-Début**, et les boutons **Ajouter / Supprimer** ;
- la commande **Afficher le chemin critique**, en haut à droite du diagramme, qui devient
  **Masquer le chemin critique** une fois activée ;
- le rendu du chemin critique **en hachures** dans cette version, et non en couleur pleine ;
- les commandes **Zoom avant · Zoom arrière · Début du projet · Reculer · Avancer**.

**Non vérifié** : le comportement d'autres versions de GanttProject. Une version plus ancienne ou
plus récente peut déplacer un bouton ou colorer autrement le chemin critique. **L'atelier ne fait
donc jamais dépendre une consigne de la couleur** : il dit « les tâches mises en évidence », jamais
« les tâches en rouge ». Les *gestes* enseignés — saisir une durée, déclarer un prédécesseur,
afficher le chemin critique — sont stables d'une version à l'autre ; c'est eux que l'atelier
enseigne.

**Non vérifié non plus** : le rendu sous macOS et sous Linux. Le poste de référence est un poste
Windows.

## Le jeu de données

`taches_projets_c7_simulees.csv` — **données simulées**, construites pour l'atelier. Elles décrivent
les trois projets réellement menés dans les séquences C7.1 du dépôt (l'indicateur de rangement du
hall en 5e, le jardin connecté de Brooklyn en 4e, le capteur de confort en 3e), mais les durées sont
des estimations pédagogiques et ne proviennent d'aucun relevé.

Toutes les valeurs affichées et énoncées dans l'atelier — dates, marges, chemin le plus long, durée
totale — sont **calculées** par `_verifier_planning.py` à partir de ce seul fichier, jamais recopiées
à la main (règles n°48 et n°54). Le fichier `jardin_connecte_brooklyn.gan` est lui aussi engendré à
partir du CSV : ce que l'élève ouvre dans le logiciel et ce que le corrigé annonce viennent de la
même source.

## Les trois diagrammes de planification (SVG, 10 août 2026)

`Images/gantt_indicateur-rangement-hall.svg` · `gantt_jardin-connecte-brooklyn.svg` ·
`gantt_capteur-confort-ny.svg`

**Origine** : dessins originaux engendrés par `_generation/gantt_premium.py` à partir du
seul fichier `taches_projets_c7_simulees.csv` — donc du même tableau que le corrigé
calculé. Aucune donnée saisie à la main, aucun logiciel tiers, aucune capture d'écran.

**Licence** : créés pour ce dépôt, réutilisables sous la licence du dépôt.

**Ce qu'ils montrent, et pourquoi** : chemin le plus long en barres pleines colorées ;
tâches à marge en barres sombres, chacune posée dans la **fenêtre en pointillés** qui va
de sa date au plus tôt à sa date au plus tard, avec une barre fantôme à la position la
plus tardive et la marge écrite en clair. La légende énonce les trois lectures au lieu de
nommer les couleurs. Palette lisible en niveaux de gris et sûre pour les daltonismes ;
`<title>` et `<desc>` renseignés, plus un `alt` complet dans la page.

**Pourquoi du SVG et non une capture** : net à l'impression A4, quelques kilo-octets, et
il se régénère quand une durée change — une capture, elle, mentirait dès la première
modification du CSV. Les captures de **GanttProject** restent nécessaires ailleurs : elles
montrent *le logiciel* (règle n°70) ; ces SVG montrent *le raisonnement*.

**Contrôle exécuté** : ordonnancement aller-retour avec tolérance nulle sur les marges,
corrigé écrit **puis relu** et invariant revérifié (règle n°71), et somme des durées du
chemin critique égale à la durée du projet. Valeurs identiques à celles du corrigé de
l'atelier, produites par un second calcul indépendant.

