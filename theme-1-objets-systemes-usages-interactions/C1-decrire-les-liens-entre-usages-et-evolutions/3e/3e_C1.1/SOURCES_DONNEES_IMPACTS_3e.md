# Sources des données — 3e · Tsinghua · robotique, feux et impacts

Date de vérification : 25 juillet 2026

## Sources institutionnelles

| Ensemble | Source | Données retenues | Limites à enseigner |
|---|---|---|---|
| Feux en France en 2026 | Ministère de l’Intérieur, 24/07/2026 | Plus de 50 000 ha brûlés depuis le début de l’année ; 32 feux encore en cours | Situation évolutive ; 50 000 ha est un minimum annoncé, pas le bilan final. |
| Feux dans l’Union européenne en 2023 | Joint Research Centre / EFFIS | 504 002 ha brûlés ; environ 20 Mt de CO₂ estimées | Estimation modélisée à l’échelle de l’UE et sur une année entière. Son ratio moyen n’est qu’un proxy pour d’autres territoires. |
| Facteurs d’activités humaines | Impact CO₂ / ADEME / Base Empreinte / Agribalyse | Voiture thermique, TGV, avion moyen-long courrier, repas avec du bœuf | Les unités et les périmètres diffèrent : véhicule-km, passager-km ou repas ; infrastructures parfois exclues. |
| Impacts environnementaux du conflit à Gaza | Programme des Nations Unies pour l’environnement, évaluations 2024 et 2025 | 39 puis 61 millions de tonnes de débris ; 78 % des bâtiments endommagés ou détruits ; pertes de végétation | Accès au terrain limité ; résultats fondés sur télédétection et observations d’agences partenaires ; les indicateurs ne sont pas des tonnes de CO₂e. |

## Liens consultés

- https://www.interieur.gouv.fr/actualites/actualites-du-ministere/sur-terre-et-dans-airs-combattre-feu-sur-tous-fronts
- https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/wildfires-2023-among-worst-eu-century-2024-04-10_en
- https://impactco2.fr/outils/transport/voiturethermique
- https://impactco2.fr/outils/transport/tgv
- https://impactco2.fr/outils/transport/avion-moyenlongcourrier
- https://impactco2.fr/outils/alimentation/repasavecduboeuf
- https://www.unep.org/fr/resources/rapport/impact-environnemental-du-conflit-gaza-evaluation-preliminaire-des-impacts
- https://www.unep.org/news-and-stories/press-release/environmental-damage-gaza-strip-harming-human-health-threatening

## Format du fichier — la virgule décimale (12/09/2026)

`donnees_impacts_feux_activites_conflit_3e.csv` écrivait ses quatre décimales **au point** :
`0.142`, `0.00293`, `0.167`, `4.97`. Sur un poste en locale française — celle de la salle — le
tableur les lit alors comme du **texte** : ni tri, ni moyenne, ni graphique. Mesuré avant de
toucher au fichier : à l'import sous `Français (France)`, ces quatre cellules-là, et elles seules,
ressortaient de type `string` ; toutes les autres valeurs étaient déjà des nombres.

Elles passent donc **à la virgule**, dans la colonne `valeur` et elle seule — zéro point ailleurs
dans le fichier, vérifié champ par champ avant d'écrire. Le séparateur `;` et les fins de ligne ne
bougent pas, et le fichier fait **exactement le même poids qu'avant**.

Vérification rejouée après : import sous la même locale, **14 lignes × 10 colonnes**, colonne
`valeur` **entièrement de type `float`**, minimum `0,00293`, maximum `61 000 000`. Les quatre
valeurs se relisent `0,142`, `0,00293`, `0,167`, `4,97`.

Les chiffres eux-mêmes n'ont pas changé : ce sont toujours ceux des sources ci-dessus. Seule
l'écriture du séparateur décimal change — et elle s'aligne sur celle que la séquence emploie déjà
dans son texte, où l'on lit `0,142 kgCO₂e/km` et `0,00293 kgCO₂e/passager-km`.

## Règle éthique

Les exercices comparent des données, des unités, des périmètres et des méthodes. Ils ne comparent jamais la valeur des vies, la légitimité des victimes ni l’intensité des souffrances humaines. Le conflit étudié ne doit pas être réduit à un chiffre carbone.
