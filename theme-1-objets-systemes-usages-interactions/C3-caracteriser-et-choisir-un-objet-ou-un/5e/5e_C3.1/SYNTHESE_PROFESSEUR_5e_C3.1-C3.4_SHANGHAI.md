# Synthèse professeur — 5e_C3.1 à 5e_C3.4

## Choisir une solution de livraison du dernier kilomètre à Shanghai

### Finalité du lot

Cette séquence conduit les élèves à comparer trois solutions techniques à partir de données simulées, à construire une décision multicritère et à vérifier la transférabilité de leur choix vers un autre territoire. Le but n’est pas de désigner une solution universellement « meilleure », mais de rendre visibles les critères, les unités, les pondérations, les limites et les incertitudes qui structurent une décision technique.

## Compétences travaillées

| Code | Attendu observable | Trace produite |
|---|---|---|
| **5e_C3.1** | Repérer des caractéristiques, grandeurs, unités et sources | Tableau de données annoté |
| **5e_C3.2** | Comparer des performances à partir de critères explicites | Graphique ou tableau comparatif légendé |
| **5e_C3.3** | Prendre en compte plusieurs étapes du cycle de vie | Diagramme du cycle de vie commenté |
| **5e_C3.4** | Choisir une solution adaptée et justifier la décision | Matrice pondérée et argumentaire |

## Points de vigilance didactiques

1. Le fichier CSV est **simulé**. Il sert à apprendre une méthode et ne doit jamais être présenté comme une source industrielle ou commerciale réelle.
2. Les élèves ne doivent pas additionner directement des kilogrammes, kilomètres, décibels, Wh/km ou indices sur 5 et sur 10.
3. Une valeur élevée n’est pas toujours favorable : pour le bruit, la consommation, le rayon de braquage ou la distance de freinage, une valeur plus faible peut être préférable.
4. Une solution électrique n’est pas automatiquement sans impact. La masse, les matériaux, la durée de vie, la réparabilité, l’entretien et la fin de vie doivent rester visibles.
5. Une matrice multicritère aide à décider, mais le résultat dépend des coefficients. Toute pondération doit être justifiée.
6. Le transfert Shanghai–Martinique doit éviter les stéréotypes. Les élèves comparent des contraintes concrètes : pluie, pente, largeur des voies, distance, maintenance, disponibilité des pièces, sécurité et organisation des livraisons.

## Corrigé synthétique des quatre activités

### Activité 1 — Lire les données et les unités

Réponses attendues :

- `charge_utile_kg`, `autonomie_km`, `distance_freinage_m_a_15_kmh`, `rayon_braquage_m`, `bruit_dba` et `energie_usage_wh_par_km` sont des grandeurs mesurées avec des unités différentes ;
- `reparabilite_sur_10`, `adaptation_ruelles_sur_5` et `adaptation_pluie_sur_5` sont des indices ;
- une charge utile ou une autonomie plus élevée peut être favorable ;
- une consommation, un bruit, une distance de freinage ou un rayon de braquage plus faibles peuvent être favorables ;
- les valeurs ne sont comparables que si la grandeur, l’unité et le contexte sont connus.

### Activité 2 — Représenter et comparer

Exemples de conclusions recevables :

- la fourgonnette transporte nettement plus, mais consomme davantage par kilomètre ;
- le robot est très maniable dans les données simulées, mais son adaptation à la pluie est faible ;
- le vélo-cargo présente un compromis intéressant entre réparabilité, maniabilité et consommation, avec une charge utile inférieure à celle de la fourgonnette.

Une conclusion n’est validée que si elle cite au moins deux indicateurs et leurs unités ou échelles.

### Activité 3 — Cycle de vie

Éléments attendus :

- matières et masse de la structure ;
- fabrication et transport ;
- énergie consommée pendant l’usage ;
- entretien, réparation et disponibilité des composants ;
- durée de vie estimée ;
- réemploi, reconditionnement, recyclage et déchets ultimes.

Conclusion attendue : aucune solution ne peut être déclarée « écologique » à partir d’un seul indicateur.

### Activité 4 — Matrice multicritère

Le résultat dépend des critères et des coefficients. Une copie correcte doit :

- utiliser cinq critères au minimum ;
- attribuer des coefficients explicites de 1 à 3 ;
- appliquer la même méthode de notation aux trois solutions ;
- calculer les scores sans erreur ;
- citer une limite ou une incertitude ;
- vérifier que le résultat reste cohérent avec la situation réelle.

## Exemple de matrice possible

| Critère | Coefficient | Vélo-cargo | Fourgonnette | Robot |
|---|---:|---:|---:|---:|
| Charge utile | 3 | 2 | 5 | 2 |
| Consommation | 3 | 5 | 1 | 3 |
| Maniabilité | 2 | 4 | 2 | 5 |
| Adaptation à la pluie | 2 | 3 | 5 | 2 |
| Réparabilité | 2 | 5 | 4 | 2 |

Cette matrice constitue un **exemple construit pour l’activité**. D’autres résultats sont acceptables si les notes et coefficients sont argumentés.

## Erreurs fréquentes et remédiations

| Erreur observée | Remédiation |
|---|---|
| Addition de valeurs ayant des unités différentes | Faire nommer la grandeur et l’unité avant tout calcul |
| Choix fondé sur un seul indicateur | Exiger au moins trois critères dans l’argumentaire |
| Confusion entre donnée réelle et donnée simulée | Faire inscrire « données simulées » dans le titre du tableau et du graphique |
| Graphique sans titre, unité ou source | Utiliser une grille de vérification avant validation |
| Coefficients choisis après avoir vu le résultat | Faire justifier les coefficients avant le calcul |
| Présentation de l’électrique comme « sans impact » | Reprendre le diagramme du cycle de vie complet |
| Transfert territorial trop général | Exiger trois contraintes concrètes et localisées |

## Différenciation

- **Aide renforcée** : tableau partiellement complété, critères proposés et exemple de calcul pondéré.
- **Niveau attendu** : choix autonome de cinq critères et justification écrite.
- **Approfondissement** : comparaison de deux jeux de pondérations et analyse de sensibilité du classement.

## Évaluation formative

Barème indicatif sur 20 :

| Critère | Points |
|---|---:|
| Lecture correcte des données et des unités | 4 |
| Représentation pertinente, titrée et légendée | 4 |
| Prise en compte du cycle de vie | 4 |
| Matrice multicritère cohérente | 4 |
| Argumentaire et transfert territorial | 4 |

## À retenir pour la correction

Une réponse différente du corrigé peut être pleinement recevable. La conformité repose sur la méthode : données identifiées, unités respectées, critères multiples, pondérations justifiées, limite explicitée et adaptation au contexte argumentée.
