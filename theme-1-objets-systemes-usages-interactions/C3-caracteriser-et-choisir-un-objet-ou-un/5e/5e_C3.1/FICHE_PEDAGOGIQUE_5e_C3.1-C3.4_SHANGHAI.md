# Fiche pédagogique — 5e_C3.1 à 5e_C3.4

## Choisir une solution de livraison du dernier kilomètre à Shanghai

### Cadre

- **Niveau** : 5e
- **Thème** : 1 — Objets, systèmes, usages et interactions
- **Ancrage principal** : Shanghai — 上海 — Shànghǎi
- **Ouverture territoriale** : comparaison avec Fort-de-France et Sainte-Luce en Martinique
- **Durée prévisionnelle** : 4 séances de 55 minutes
- **Organisation** : groupes de 3 ou 4 élèves
- **Données utilisées** : jeu de données **simulées** `donnees_vehicules_dernier_kilometre_shanghai_simulees.csv`

## Situation déclenchante

Une plateforme de distribution doit livrer de petits colis dans un quartier dense de Shanghai. Trois solutions sont envisagées :

1. un vélo-cargo à assistance électrique ;
2. une fourgonnette électrique compacte ;
3. un robot mobile de livraison supervisé.

Aucune solution n’est parfaite. Le choix doit tenir compte de la charge utile, de l’autonomie, du bruit, de la consommation d’énergie, de la réparabilité, du coût et de l’adaptation aux rues étroites ou à la pluie.

## Problématique

> **Comment comparer plusieurs objets techniques afin de choisir la solution la plus adaptée à un besoin réel, sans réduire la décision à un seul critère ?**

## Compétences principales

| Code | Intention d’apprentissage | Action observable |
|---|---|---|
| **5e_C3.1** | Identifier et exploiter des caractéristiques d’objets techniques | Lire les données, repérer les unités et sélectionner les critères utiles |
| **5e_C3.2** | Comparer des performances à partir de critères | Construire un tableau comparatif et argumenter les écarts |
| **5e_C3.3** | Prendre en compte le cycle de vie et les impacts | Relier matériaux, durée de vie, réparabilité et matière recyclée |
| **5e_C3.4** | Choisir une solution adaptée à un contexte | Produire une décision multicritère justifiée et transférable |

## Productions attendues

- un tableau de données nettoyé et annoté ;
- un graphique pertinent réalisé à partir de deux ou trois indicateurs ;
- une matrice multicritère avec pondération simple ;
- une justification écrite de 8 à 12 lignes ;
- une courte analyse de transférabilité vers une commune de Martinique ;
- une trace individuelle de synthèse.

# Déroulement

## Séance 1 — Comprendre les données et les unités

### Objectif

Identifier ce que mesure chaque colonne et vérifier que les comparaisons sont possibles.

### Activité 1 — Lire sans se faire piéger

Les élèves ouvrent le fichier CSV et classent les colonnes dans quatre familles :

- caractéristiques physiques ;
- performances d’usage ;
- impacts et durée de vie ;
- adaptation au contexte.

Ils doivent ensuite repérer :

- les unités ;
- les valeurs qui ne sont pas directement comparables ;
- les indicateurs pour lesquels une valeur élevée est favorable ;
- les indicateurs pour lesquels une valeur faible est favorable.

### Aide

Avant de comparer deux nombres, répondre à trois questions :

1. Mesurent-ils la même grandeur ?
2. Sont-ils exprimés dans la même unité ?
3. Une valeur plus grande représente-t-elle toujours une meilleure performance ?

### Correction attendue

- `charge_utile_kg`, `autonomie_km`, `distance_freinage_m_a_15_kmh`, `rayon_braquage_m`, `bruit_dba` et `energie_usage_wh_par_km` sont des performances mesurées avec des unités différentes.
- Une charge utile ou une autonomie plus élevée peut être favorable.
- Une distance de freinage, un rayon de braquage, un niveau sonore ou une consommation plus faibles peuvent être favorables.
- `reparabilite_sur_10`, `adaptation_ruelles_sur_5` et `adaptation_pluie_sur_5` sont des indices ; ils ne doivent pas être mélangés directement avec des kilogrammes, kilomètres ou Wh/km.
- Le jeu de données est simulé : il sert à apprendre une méthode de comparaison et ne constitue pas une fiche commerciale réelle.

### Erreurs fréquentes

- additionner des valeurs ayant des unités différentes ;
- conclure qu’une grande masse est nécessairement un avantage ;
- croire que « électrique » signifie automatiquement « sans impact » ;
- oublier qu’un indice sur 5 et un indice sur 10 n’ont pas la même échelle.

## Séance 2 — Représenter et comparer

### Objectif

Choisir une représentation adaptée à la question posée.

### Activité 2 — Un graphique pour une question précise

Chaque groupe choisit une question parmi les suivantes :

- quelle solution transporte le plus tout en consommant le moins par kilomètre ?
- quelle solution semble la plus maniable en rues étroites ?
- quelle solution combine durée de vie et réparabilité ?

Les élèves produisent un graphique ou un tableau comparatif et rédigent une phrase d’interprétation.

### Aide

- Un diagramme en barres convient à la comparaison de quelques valeurs.
- Deux grandeurs d’unités différentes ne doivent pas être placées sur un même axe sans explication.
- Un graphique doit comporter un titre, des axes, des unités et une source.

### Correction attendue

Exemples d’interprétations recevables :

- La fourgonnette possède la charge utile la plus élevée, mais sa consommation par kilomètre est nettement supérieure.
- Le robot présente le plus petit rayon de braquage dans le jeu simulé, mais son adaptation à la pluie est faible.
- Le vélo-cargo obtient les meilleurs indices combinés de réparabilité et d’adaptation aux ruelles, avec une charge utile plus faible que la fourgonnette.

Aucune conclusion ne doit être admise sans citer au moins deux indicateurs.

## Séance 3 — Prendre en compte le cycle de vie

### Objectif

Éviter une comparaison limitée à la phase d’utilisation.

### Activité 3 — Du matériau à la fin de vie

Les élèves complètent pour chaque solution un schéma simple :

`matières → fabrication → transport → utilisation → entretien/réparation → réemploi ou recyclage → déchets ultimes`

Ils utilisent les colonnes suivantes :

- matériau de structure ;
- masse ;
- durée de vie estimée ;
- réparabilité ;
- proportion de matière recyclée ;
- énergie consommée pendant l’usage.

### Aide

Un matériau recyclable n’est pas automatiquement le meilleur choix. Il faut aussi considérer :

- la quantité de matière utilisée ;
- la durée de vie ;
- la facilité de réparation ;
- la consommation pendant l’usage ;
- la possibilité de réemploi des composants.

### Correction attendue

- La fourgonnette utilise davantage de matière et d’énergie par kilomètre, mais elle transporte une charge beaucoup plus importante.
- Le vélo-cargo est plus léger et plus réparable dans les données simulées, mais protège moins l’utilisateur contre les intempéries.
- Le robot est compact et silencieux, mais sa durée de vie, sa réparabilité et son comportement sous la pluie doivent être vérifiés.
- Aucune solution ne peut être déclarée « écologique » à partir d’un seul indicateur.

## Séance 4 — Décider et transférer

### Objectif

Construire une décision multicritère explicite.

### Activité 4 — Matrice de choix

Chaque groupe sélectionne cinq critères et attribue un coefficient de 1 à 3 selon leur importance pour le contexte étudié.

Exemple de critères :

- charge utile ;
- consommation ;
- maniabilité ;
- pluie ;
- réparabilité ;
- coût ;
- bruit.

Chaque solution reçoit une note de 1 à 5 par critère. Le groupe calcule le score pondéré, puis vérifie si le résultat correspond réellement à la situation.

### Règle de décision

La matrice aide à décider ; elle ne remplace pas le jugement. Toute pondération doit être expliquée.

### Transfert Martinique

Les élèves répondent ensuite à la question :

> La solution choisie pour un quartier dense de Shanghai conviendrait-elle à Fort-de-France ou à Sainte-Luce ?

Ils doivent citer au moins trois contraintes locales possibles :

- pente ;
- pluie intense ;
- chaleur ;
- largeur des voies ;
- stationnement ;
- distance entre les points de livraison ;
- entretien et disponibilité des pièces ;
- sécurité des usagers.

### Correction attendue

Une réponse correcte peut différer selon les pondérations, à condition de :

- citer au moins trois critères ;
- utiliser des données du tableau ;
- expliciter les coefficients ;
- signaler une limite ou une incertitude ;
- distinguer le contexte de Shanghai de celui de la Martinique.

# À retenir

1. Comparer exige des unités, des sources et un périmètre clairement définis.
2. Une performance ne suffit pas pour choisir une solution.
3. Une matrice multicritère rend la décision visible, mais les coefficients doivent être justifiés.
4. Le cycle de vie inclut fabrication, usage, entretien, réparation, réemploi, recyclage et déchets ultimes.
5. Une solution adaptée à un territoire n’est pas automatiquement transférable ailleurs.
6. Les données simulées permettent d’apprendre une méthode ; elles ne doivent pas être présentées comme des mesures réelles.

# Représentations mobilisées — règle d’or n°9

| Représentation | Pertinence | Action de l’élève | Trace produite | Séance | Évaluation prévue |
|---|---|---|---|---|---|
| Tableau de données structuré | Comparer les mêmes indicateurs | Trier, annoter et repérer les unités | Tableau corrigé | 1 | Interprétation de colonnes |
| Graphique comparatif | Visualiser des écarts | Choisir le graphique et le légender | Graphique exporté | 2 | Lecture et choix de représentation |
| Diagramme du cycle de vie | Élargir l’analyse au-delà de l’usage | Compléter les étapes et impacts | Schéma annoté | 3 | Repérage d’un oubli ou d’une conclusion abusive |
| Matrice multicritère | Rendre la décision explicite | Pondérer, noter, calculer et justifier | Matrice et argumentaire | 4 | Application et détection d’une pondération incohérente |

# Évaluation formative

Critères de réussite :

- données et unités correctement identifiées ;
- graphique lisible et pertinent ;
- au moins deux dimensions du cycle de vie mobilisées ;
- décision fondée sur plusieurs critères ;
- pondérations justifiées ;
- limite ou incertitude explicitée ;
- transfert territorial argumenté sans stéréotype.

# Différenciation

- **Aide renforcée** : tableau partiellement rempli, critères proposés, calcul pondéré guidé.
- **Niveau attendu** : choix de cinq critères et justification autonome.
- **Approfondissement** : comparaison de deux jeux de pondérations et analyse de la sensibilité du résultat.

# Versions matérielles

- **A — Réel** : mesures complémentaires sur un vélo ou un chariot disponible dans l’établissement.
- **B — Simulation** : exploitation du CSV fourni et d’un tableur.
- **C — Sans matériel** : impressions du tableau, cartes-critères et calcul manuel simplifié.

# Liens à produire dans le lot complet

- séquence élève HTML ;
- QCM séparé conforme au moteur commun ;
- synthèse élève ;
- synthèse professeur ;
- images ou schémas originaux accessibles ;
- `SOURCES_MEDIAS.md` ;
- rapport de tests réellement exécutés ;
- entrée `nouveautes.json` et journal au moment de la livraison finale.
