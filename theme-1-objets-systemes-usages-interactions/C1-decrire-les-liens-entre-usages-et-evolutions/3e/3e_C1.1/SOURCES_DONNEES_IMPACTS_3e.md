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

## Définitions — invention, innovation, évolution technologique, innovation de rupture (22/09/2026)

Sources ouvertes et lues le 22/09/2026. Chaque définition de l'encadré « 📌 » et des questions « Invention », « Innovation », « Évolution technologique », « Innovation de rupture » du QCM
est confrontée phrase par phrase ; ce qu'une source ne dit pas est signalé, pas prêté.

| Mot | Source primaire | Passage (mot pour mot) | Ce qu'il fonde dans notre définition |
|---|---|---|---|
| Innovation | OCDE/Eurostat, *Oslo Manual 2018*, 4ᵉ éd., §2.99 (définition générale, reprise au §1.25) | « An innovation is a new or improved product or process (or combination thereof) that differs significantly from the unit's previous products or processes and that has been made available to potential users (product) or brought into use by the unit (process). » | « nouveau ou nettement amélioré » (*differs significantly*) ; « mise à la disposition de ceux qui peuvent s'en servir » (*made available to potential users*). **Corrigé** : la première rédaction disait « qui arrive jusqu'à ceux qui s'en servent » — le manuel exige la mise à disposition, pas l'usage effectif. |
| Innovation | *Oslo Manual 2018*, §2.2 | « Innovation is more than a new idea or an invention. An innovation requires implementation, either by being put into active use or by being made available for use by other parties […] » | « Une idée, même excellente, n'est pas encore une innovation. » |
| Innovation | *Oslo Manual 2018*, §2.19 | « The requirement for implementation is a defining characteristic of innovation that distinguishes it from inventions, prototypes, new ideas, etc. » | « Une invention n'est pas forcément utilisée. » |
| Innovation de produit (services inclus) | *Oslo Manual 2018*, §3.24 (et encadré du §1.31) | « A product innovation is a new or improved good or service that differs significantly from the firm's previous goods or services and that has been introduced on the market. » — §3.24 : « The term "product" […] encompasses both goods and services. » | « objet, procédé ou service » |
| Innovation | Eurostat, *Statistics Explained*, Glossary: Innovation | « Innovation is the use of new ideas, products or methods where they have not been used before. For the Community Innovation Survey (CIS), an innovation is defined as a new or significantly improved product (good or service) introduced to the market, or the introduction within an enterprise of a new or significantly improved process. » | « nouveau ou nettement amélioré » ; « bien ou service » |
| Invention | TLFi (CNRTL), « inventer », A.1 ; « invention », I.A.1-2 renvoie à « inventer A » | « Trouver par la force de l'imagination créatrice et réaliser le premier quelque chose de nouveau. Inventer un instrument, un jeu, une machine, un médicament, une mode, un procédé. » | « mise au point pour la première fois » (*réaliser le premier*) ; « un objet, un procédé » |
| Invention | INPI, « Les critères de brevetabilité », rubrique « Qu'est-ce qu'une invention brevetable ? » (publié le 27/11/2024) | « L'invention doit apporter une solution technique originale qui n'est pas évidente pour un expert dans le domaine concerné. » | « une solution technique » — la page parle de l'invention **brevetable** : notre définition, plus large, s'appuie d'abord sur le TLFi. |
| Innovation de rupture | *Oslo Manual 2018*, §3.62 | « Radical innovations are considered to transform the status quo, while a disruptive innovation takes root in simple applications in a niche market and then diffuses throughout the market, eventually displacing established competitors (Christensen, 1997). » | « change profondément […] les marchés » (*transform the status quo*, *transform (or create) a market*). Les **usages**, les **métiers** et le **savoir-faire d'avant qui ne suffit plus** ne sont pas dans le manuel : c'est le critère que la séquence enseigne depuis sa création (« Regarde le métier. S'il change, c'est une rupture. »). **À relire par Pascal.** |
| Évolution technologique | — | aucune des sources ci-dessus ne définit ce terme du programme | La définition vient de la séquence elle-même (« Une amélioration fait mieux la même chose. Le métier ne change pas. »). Elle est cohérente avec le manuel d'Oslo, pour qui un produit **amélioré** mis à disposition est aussi une innovation (§2.99). **À relire par Pascal.** |

Liens :
- https://www.oecd.org/content/dam/oecd/en/publications/reports/2018/10/oslo-manual-2018_g1g9373b/9789264304604-en.pdf
- https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Innovation
- https://www.cnrtl.fr/definition/inventer · https://www.cnrtl.fr/definition/invention
- https://www.inpi.fr/realiser-demarches/propriete-intellectuelle/criteres-de-brevetabilite

## L'expérience de Herschel, 1800 — activité 1 b), « pas à pas » (24/09/2026)

Sources ouvertes et lues le 24/09/2026. Chaque phrase de l'animation, du volet « Ce qu'Herschel a observé » et
des deux schémas est confrontée ; ce qu'une source contredit a été corrigé.

| Phrase de la page | Source | Passage (mot pour mot) |
|---|---|---|
| Étape 1 — « quelle couleur de la lumière du Soleil chauffe le plus ? » | W. Herschel, « Investigation of the Powers of the Prismatic Colours to Heat and Illuminate Objects », *Phil. Trans.* 90 (1800) — titre ; Cool Cosmos, « Herschel's Experiment » | titre : « the Powers of the Prismatic Colours to Heat » ; Cool Cosmos : « He wanted to know how much heat was passed through the different colored filters he used to observe sunlight. » |
| Étape 2 — « La lumière du Soleil entre par une fenêtre presque masquée, puis traverse un prisme. » | W. Herschel, « Experiments on the Refrangibility of the Invisible Rays of the Sun », *Phil. Trans.* 90 (1800), p. 285 | « the precaution of darkening the window in which the prism was placed, by fixing up a thick dark green curtain » |
| Étape 4 — « l'une après l'autre, en y avançant un thermomètre ; deux autres, restés à l'ombre, servent à comparer » | *Investigation*, 1ʳᵉ expérience | « I then placed three thermometers upon small inclined planes […] their balls were blacked with japan ink » ; « advancing No. 1 to the red rays, and leaving the other two close by, in the shade, I marked down what they shewed » |
| Étape 5 — « Du violet au rouge, la température monte de plus en plus. » | Cool Cosmos | « He found that the temperatures of the colors increased from the violet to the red part of the spectrum. » |
| Étape 7 — « C'est au-delà du rouge […] que le thermomètre monte le plus. » | *Investigation* ; *Refrangibility*, p. 285 ; Cool Cosmos | « the full red falls still short of the maximum of heat; which perhaps lies even a little beyond visible refraction » ; « the thermometer No. 1 rose 6½ degrees, in 10 minutes, when its centre was placed ½ inch beyond visible light » ; « this region had the highest temperature of all » |
| Étape 7 — « des rayons invisibles qui chauffent […] “rayons calorifiques” » | *Investigation* ; Cool Cosmos | « radiant heat will at least partly, if not chiefly, consist […] of invisible light » ; « the refrangibility of calorific rays » ; « calorific rays (derived from the Latin word for heat) » |

**Corrigé parce que la source le contredisait** :
- « place un thermomètre sous chaque couleur » (texte de b)), « Sept thermomètres sont debout sur la table »
  (description du schéma), « un thermomètre est posé dans chaque zone » (schéma) et « met un thermomètre sous
  chaque couleur » (frise du corrigé) : Herschel utilisait **trois** thermomètres, en avançait **un** dans la
  couleur étudiée et laissait les deux autres à l'ombre pour comparer. Le schéma garde un thermomètre par zone,
  mais dit désormais qu'il montre **les mesures**, faites l'une après l'autre.
- « volet et fente » (schéma) : aucune des deux sources ne parle d'une fente avant le prisme ; le prisme est
  dans une fenêtre assombrie par un rideau. Le dessin dit « fenêtre masquée ». (L'ouverture découpée dans un
  carton, dans *Investigation*, est placée **après** le prisme, pour ne laisser passer qu'une couleur.)

**Frise du corrigé** : seule date sourcée, 1800. Le reste vient de la page elle-même (« plus d'un siècle avant
les premières caméras thermiques, puis les satellites, puis le drone ») : les caméras thermiques et les
satellites sont placés dans une bande « XXᵉ siècle », sans année, faute de source primaire lue.

Liens :
- https://archive.org/details/philtrans01364503 (*Investigation…*, 1800)
- https://archive.org/details/philtrans08733349 (*Experiments on the Refrangibility…*, 1800)
- https://coolcosmos.ipac.caltech.edu/page/herschel_experiment
