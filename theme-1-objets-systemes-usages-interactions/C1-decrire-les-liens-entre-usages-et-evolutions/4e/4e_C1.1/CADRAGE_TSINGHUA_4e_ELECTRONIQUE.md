# Cadrage — 4e — Tsinghua : ingénierie électronique

## Identité du lot

- **Thème** : 1 — Usages et interactions
- **Niveau** : 4e
- **Ancrage territorial** : Université Tsinghua 清华大学 — *Qīnghuá Dàxué*, Beijing 北京 — *Běijīng*
- **Département étudié** : Department of Electronic Engineering
- **Codes principaux** : `4e_C1.1`, `4e_C1.2`, `4e_C1.3`
- **Titre provisoire** : **Pourquoi un système électronique de mesure existe-t-il et pourquoi doit-il évoluer ?**

## Appui documentaire officiel

Le Département d’ingénierie électronique de Tsinghua présente des activités en circuits et systèmes, communications, systèmes d’information, détection, traitement intelligent, optoélectronique et systèmes intelligents. La séquence ne reproduira aucun projet de laboratoire : elle utilisera un cas pédagogique fictif inspiré de ces domaines généraux.

## Situation déclenchante envisagée

Une équipe fictive d’étudiants de Tsinghua doit proposer un système électronique permettant de suivre le confort d’une salle de travail partagée : température, bruit et occupation. Une première version affiche seulement une alerte locale. Les utilisateurs demandent ensuite un historique, une meilleure lisibilité, une alerte accessible et une transmission limitée aux seules données nécessaires.

Toutes les données, fiches d’usage, contraintes et performances seront inventées pour l’apprentissage.

## Problématique

**Pourquoi ce système électronique existe-t-il, comment ses usages réels font-ils évoluer le besoin, et quelles contraintes faut-il identifier avant d’étudier son fonctionnement ou de le concevoir ?**

## Compétences du programme couvertes

### `4e_C1.1`
Mettre en relation les objets ou systèmes techniques avec leurs usages.

**Production** : carte « utilisateur — situation — usage — résultat attendu ».

### `4e_C1.2`
Identifier les avantages et les inconvénients associés aux évolutions technologiques et informatiques.

**Production** : tableau argumenté comparant la version locale, la version connectée et une version sobre en données.

### `4e_C1.3`
Justifier l’évolution d’un objet ou système technique pour répondre à l’évolution des besoins.

**Production** : note de justification reliant un nouveau besoin à une modification précise du système.

## Déroulé envisagé — 3 séances

### Séance 1 — Pourquoi mesurer ? Partir des usages réels

- distinguer objet, fonction d’usage et situation d’usage ;
- identifier étudiants, personnels, maintenance et personnes ayant des besoins d’accessibilité ;
- transformer des remarques d’utilisateurs en besoins explicites ;
- repérer les usages prévus, détournés et non satisfaits.

**Trace** : carte des usages et formulation du besoin principal.

### Séance 2 — Pourquoi le système évolue-t-il ?

- comparer trois générations fictives du système ;
- relier chaque évolution à une demande ou à une difficulté constatée ;
- examiner avantages, limites et effets possibles : consommation, données, maintenance, accessibilité, coût ;
- éviter l’idée que toute nouveauté constitue nécessairement un progrès.

**Trace** : tableau « évolution — besoin — avantage — limite — compromis ».

### Séance 3 — Quelles contraintes avant de parler de composants ?

- classer les contraintes : usage, sécurité, environnement, énergie, données, ergonomie, fiabilité, coût ;
- distinguer exigence et solution technique ;
- hiérarchiser les contraintes critiques ;
- préparer les questions qui seront reprises dans les Thèmes 2 et 3.

**Trace** : cahier des contraintes simplifié et fiche de passage aux autres thèmes.

## CRCN observable, tracé et justifié

- **Compétence exacte** : CRCN 1.3 — Traiter des données.
- **Niveau visé** : niveau 2.
- **Repère pour enseigner verbatim** : « Insérer, saisir et trier des données dans un tableur pour les exploiter. »
- **Action observable** : insérer une colonne de priorité dans un tableau d’avis d’utilisateurs, saisir les priorités, trier les besoins et filtrer les contraintes critiques.
- **Trace produite** : fichier ODS/XLSX transformé et export PDF contenant le tableau filtré et une justification.

**Principe** : utiliser un ordinateur n’est pas une compétence. La validation repose sur les transformations visibles du tableau et sur la trace conservée.

## Préparation explicite du Thème 2

La séquence ne détaillera pas encore les composants. Elle fera émerger les questions suivantes :

- quelles grandeurs faut-il acquérir ?
- quelles données faut-il traiter et communiquer ?
- quelle énergie faut-il fournir ?
- quelles informations doivent rester locales ?
- comment vérifier la fiabilité d’une alerte ?

Ces questions prépareront l’étude des capteurs, de la chaîne d’information, de l’énergie, des données et de la communication.

## Préparation explicite du Thème 3

La fiche de passage précisera :

- le besoin retenu ;
- les utilisateurs ;
- les contraintes prioritaires ;
- les critères de réussite ;
- les données indispensables ;
- les fonctions à conserver ou améliorer.

Elle servira de point de départ à l’imagination de solutions, à la modélisation, au prototypage et aux tests.

## Vigilances

- ne pas présenter Tsinghua comme un décor prestigieux ou comme un modèle parfait ;
- distinguer les domaines réels du département et le scénario fictif de la séquence ;
- ne pas entrer prématurément dans le fonctionnement interne, réservé au Thème 2 ;
- ne pas demander de concevoir une solution complète avant le Thème 3 ;
- intégrer accessibilité, sobriété des données et réparabilité parmi les contraintes ;
- conserver une ouverture vers la Martinique : quelles contraintes changeraient avec le climat tropical, l’humidité, les embruns ou une connexion plus fragile ?

## Livrables prévus

- séquence HTML de 3 séances ;
- QCM séparé de 30 questions ;
- synthèses élève et professeur ;
- jeu CSV original d’avis et de contraintes ;
- deux ou trois SVG originaux ;
- fiche pédagogique ;
- matrice de couverture ;
- `SOURCES_MEDIAS.md` ;
- rapport de tests réellement exécutés ;
- pointeurs de mutualisation pour `4e_C1.2` et `4e_C1.3`.
