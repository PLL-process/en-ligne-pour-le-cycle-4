# Sources des médias — lot Shanghai 5e_C3.1 à C3.4

**Règle d'or n°1** : chaque image est un document à lire, produite pour le dépôt, sous licence
libre, avec `<title>` et `<desc>` accessibles. Aucune capture propriétaire, aucune image trouvée
sur un moteur de recherche, aucun hotlinking.

## Les trois figures

| Fichier | Nature | Auteur | Licence | Rôle pédagogique |
|---|---|---|---|---|
| `Images/trois_solutions_shanghai.svg` | SVG original écrit à la main | Fable (agent Thème 2), pour ce dépôt | CC0 1.0 | La planche comparative : matériaux, masse, énergie, information, charge, autonomie, réparabilité des trois solutions |
| `Images/cycle_de_vie_ost.svg` | SVG original écrit à la main | Fable, pour ce dépôt | CC0 1.0 | Les cinq étapes du cycle de vie, avec les trois que les choix de matériaux et d'énergie influencent directement |
| `Images/protocole_freinage.svg` | SVG original écrit à la main | Fable, pour ce dépôt | CC0 1.0 | Le protocole de mesure et ses trois conditions à maintenir identiques |

Les trois sont du SVG écrit directement, sans police embarquée, sans image tramée, sans appel
réseau. Ils s'affichent hors ligne.

## Accessibilité

Chaque figure porte un `<title>` court et un `<desc>` long qui **décrit le contenu, pas
l'apparence** : un élève qui n'accède qu'au texte alternatif doit pouvoir répondre à la question.
Les descriptions font de 690 à 850 caractères, et l'attribut `alt` du HTML reprend la même
information. Aucune information n'est portée par la seule couleur : les étapes clés du cycle de
vie sont à la fois encadrées en orange **et** annoncées en toutes lettres dans la légende.

## Les données

`donnees_vehicules_dernier_kilometre_shanghai_simulees.csv` — **données entièrement simulées**,
construites pour l'exercice par le dépôt. Elles sont réalistes et cohérentes entre elles, mais
elles ne décrivent **aucun véhicule réellement commercialisé**. La séquence le dit à l'élève dès la
situation déclenchante, et le rappelle dans la synthèse professeur.

C'est l'application de la règle d'or n°27 : ce qui n'est vrai que chez nous se dit comme tel.

## Polices

**Aucune police distante** (règle d'or n°40). La séquence et le QCM utilisent une pile système —
`Segoe UI`, `system-ui`, `-apple-system`, `Arial`. Ce sont les deux premières pages du dépôt à
n'appeler aucune ressource réseau : elles fonctionnent à l'identique dans un collège au réseau
filtré.
