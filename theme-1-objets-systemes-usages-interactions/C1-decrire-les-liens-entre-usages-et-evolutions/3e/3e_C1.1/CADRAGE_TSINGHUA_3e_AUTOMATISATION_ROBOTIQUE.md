# Cadrage — 3e — Tsinghua : automatisation et robotique

## Identité du lot

- **Thème** : 1 — Usages et interactions
- **Niveau** : 3e
- **Ancrage territorial** : Université Tsinghua 清华大学 — *Qīnghuá Dàxué*, Beijing 北京 — *Běijīng*
- **Appuis institutionnels** : Department of Automation et Institute for Embodied Intelligence and Robotics
- **Codes principaux** : `3e_C1.1`, `3e_C1.2`, `3e_C1.3`, `3e_C1.4`
- **Code associé proposé** : `3e_C2.1`, uniquement si la production relative à l’expérience utilisateur est effectivement réalisée et évaluée
- **Titre provisoire** : **Pourquoi créer un robot mobile d’assistance, pour qui et sous quelles contraintes ?**

## Appui documentaire officiel

Le Département d’automatisation de Tsinghua travaille dans le champ de l’automatisation et présente des activités de robotique. L’Institut d’intelligence incarnée et de robotique de Tsinghua met notamment en avant des problématiques de corps robotique robuste, de perception de l’environnement, de modèles multimodaux, de planification dynamique et de coopération entre plusieurs disciplines.

La séquence n’affirmera pas reproduire un robot ou un projet réel de Tsinghua. Le robot, les utilisateurs, les mesures et les résultats seront entièrement fictifs, mais le questionnement sera inspiré de ces domaines de recherche déclarés.

## Situation déclenchante envisagée

Une équipe fictive liée à Tsinghua étudie un robot mobile destiné à transporter de petits équipements entre des salles et des laboratoires. Le robot doit circuler parmi des personnes, attendre devant une porte, éviter un obstacle, respecter une vitesse maximale, préserver les données captées et permettre à un humain de reprendre le contrôle.

Une première démonstration fonctionne dans un couloir vide. Lors d’un usage réel, plusieurs difficultés apparaissent : personne mal détectée, attente devant un ascenseur, bruit, autonomie insuffisante, arrêt d’urgence peu visible et inquiétudes sur les images enregistrées.

## Problématique

**Pourquoi ce robot existe-t-il, quels besoins et usages réels doit-il satisfaire, quelles innovations ont rendu son développement possible et quelles contraintes faut-il définir avant d’étudier son fonctionnement ou de le concevoir ?**

## Compétences du programme couvertes

### `3e_C1.1`
Identifier les innovations de rupture attachées à l’évolution d’un objet ou système technique.

**Production** : frise raisonnée distinguant amélioration progressive et innovation de rupture dans la robotique mobile.

### `3e_C1.2`
Mettre en relation une découverte scientifique avec ses développements technologiques et leurs effets sur la société.

**Production** : carte « avancée scientifique ou technique — application robotique — effet possible sur la société ».

### `3e_C1.3`
Exprimer dans un argumentaire court l’incidence d’un objet ou système technique sur la société.

**Production** : argumentaire équilibré sur les bénéfices, limites et conditions d’acceptabilité d’un robot d’assistance.

### `3e_C1.4`
Exprimer dans un argumentaire court l’incidence des contraintes sociétales sur les objets et systèmes techniques.

**Production** : justification de contraintes relatives à la sécurité, à l’accessibilité, à la vie privée, au travail humain, à la sobriété et à la responsabilité.

### `3e_C2.1` — couverture conditionnelle
Décrire l’expérience de l’utilisateur à l’aide de modes de représentation choisis.

**Production obligatoire pour revendiquer la couverture** : parcours utilisateur ou storyboard montrant une interaction réussie, une difficulté et une solution attendue.

## Déroulé envisagé — 4 séances

### Séance 1 — Pourquoi un robot plutôt qu’un autre moyen ?

- identifier le problème initial et les utilisateurs concernés ;
- distinguer besoin, souhait, solution et fonction ;
- comparer robot mobile, chariot manuel, convoyeur fixe et organisation humaine différente ;
- déterminer les situations où le robot apporte réellement une valeur et celles où il n’est pas pertinent.

**Trace** : formulation du besoin et tableau des solutions possibles.

### Séance 2 — Quelles innovations rendent le robot possible ?

- distinguer découverte scientifique, invention, innovation et amélioration ;
- relier perception, calcul, batteries, motorisation, communication et planification à des fonctions attendues ;
- identifier une ou deux innovations de rupture et justifier ce classement ;
- éviter une histoire simpliste où un seul inventeur ou un seul pays expliquerait le robot moderne.

**Trace** : frise argumentée et carte des liens science–technologie–société.

### Séance 3 — Que se passe-t-il lors des usages réels ?

- analyser plusieurs scénarios fictifs : couloir encombré, personne malvoyante, obstacle mobile, batterie faible, arrêt d’urgence, données vidéo ;
- représenter l’expérience de l’utilisateur ;
- distinguer fonctionnement prévu, usage réel, erreur humaine, limite technique et situation dangereuse ;
- identifier les acteurs concernés : utilisateur direct, personne croisée, maintenance, responsable de la sécurité, direction, concepteur.

**Trace** : storyboard ou parcours utilisateur commenté.

### Séance 4 — Quelles contraintes avant le programme et le prototype ?

- hiérarchiser les contraintes : sécurité, vitesse, arrêt, autonomie, bruit, accessibilité, protection des données, réparabilité, coût, environnement ;
- transformer les difficultés observées en exigences vérifiables ;
- rédiger un argumentaire sur les incidences du robot et les conditions de son acceptabilité ;
- préparer la fiche de passage vers les Thèmes 2 et 3.

**Trace** : tableau des contraintes priorisées, argumentaire et critères de réussite.

## CRCN observable, tracé et justifié

- **Compétence exacte** : CRCN 1.3 — Traiter des données.
- **Niveau visé** : niveau 2.
- **Repère pour enseigner verbatim** : « Insérer, saisir et trier des données dans un tableur pour les exploiter. »
- **Action observable** : insérer une colonne de gravité dans un journal d’essais simulés, saisir une qualification, trier les incidents, filtrer les situations critiques et calculer une fréquence simple fournie par le professeur.
- **Trace produite** : fichier ODS/XLSX transformé et export PDF comprenant le tableau filtré, un graphique simple et trois contraintes justifiées.

**Principe** : utiliser un ordinateur n’est pas une compétence. La preuve repose sur les transformations du journal d’essais et sur l’interprétation conservée.

## Préparation explicite du Thème 2

La séquence doit aboutir à une liste de questions techniques, sans encore fournir les réponses :

- comment le robot acquiert-il des informations sur son environnement ?
- comment traite-t-il les données et prend-il une décision ?
- comment transmet-il un ordre aux actionneurs ?
- comment l’énergie est-elle stockée et distribuée ?
- comment communique-t-il avec l’utilisateur ou le réseau ?
- comment détecter un dysfonctionnement ?

Ces questions prépareront l’étude des chaînes d’information et d’énergie, des capteurs, des actionneurs, des données, du programme, du réseau et du diagnostic.

## Préparation explicite du Thème 3

La fiche de passage fournira :

- le besoin et les utilisateurs ;
- les scénarios d’usage ;
- les contraintes hiérarchisées ;
- les critères de réussite mesurables ;
- les fonctions essentielles ;
- les situations de test ;
- les risques et limites à prendre en compte.

Elle préparera l’architecture du robot, le choix des constituants, la modélisation, la programmation, les protocoles de test et la mise au point, sans réaliser prématurément ces activités dans le Thème 1.

## Ouverture mondiale et transfert

- comparer le contexte universitaire de Beijing à un collège ou à un établissement de Martinique ;
- déterminer quelles contraintes restent identiques et lesquelles changent : largeur des circulations, humidité, chaleur, qualité du réseau, maintenance, budget, usages ;
- demander explicitement ce qu’il faudrait conserver, modifier ou abandonner pour transférer la solution.

## Vigilances

- ne pas présenter un robot humanoïde comme nécessaire lorsque des roues ou une autre organisation suffisent ;
- ne pas assimiler automatiquement automatisation, intelligence artificielle et robotique ;
- distinguer le scénario fictif des activités réelles de Tsinghua ;
- traiter les effets sur le travail humain, la sécurité, l’accessibilité et les données sans discours technophile ou technophobe ;
- ne pas valider les compétences du Thème 2 ou du Thème 3 avant les productions correspondantes ;
- ne revendiquer `3e_C2.1` que si le parcours utilisateur est effectivement produit et évalué.

## Livrables prévus

- séquence HTML de 4 séances ;
- QCM séparé de 30 à 32 questions ;
- synthèses élève et professeur ;
- journal d’essais simulés au format CSV ;
- trois SVG originaux : scénario d’usage, acteurs et contraintes, passage vers Thèmes 2–3 ;
- fiche pédagogique ;
- matrice de couverture ;
- `SOURCES_MEDIAS.md` ;
- rapport de tests réellement exécutés ;
- pointeurs de mutualisation pour `3e_C1.2`, `3e_C1.3`, `3e_C1.4` et éventuellement `3e_C2.1`.
