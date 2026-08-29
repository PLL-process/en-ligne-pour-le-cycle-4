# Fiche pédagogique / inspection — La patère du hall : éprouver un matériau (5e_C8.2)

## Identification

| Champ | Valeur |
|---|---|
| Niveau | 5e (programme 2024, applicable rentrée 2026-2027) |
| Code principal | **5e_C8.2** — *Mettre en œuvre un protocole de test fourni pour valider la tenue mécanique d'un matériau.* |
| Code d'appui | 5e_C3.1 — *Identifier les caractéristiques à prendre en compte dans le choix d'un OST.* |
| Thème | Thème 3 — Création, conception, réalisation, innovations |
| Socle | D1.3 · D4 · D5 |
| Objet-fil | Le hall du collège — suite directe du **mini-projet d'indicateur de rangement** (5e_C7.1) |
| Durée | **2 séances de 55 min** (110 min) · **100 min d'activités**, soit 10 min de marge |
| Versions | 🅰 le vrai laboratoire (application à installer) · 🅱 le banc de cette page · 🅲 sans écran |
| Dépendances | **aucune** — le banc d'essai est dans la page, hors ligne, sans compte |

## Place dans la spirale C8

| | simuler (C8.1) | **éprouver (C8.2)** | comportement (C8.3) |
|---|---|---|---|
| 5e | utiliser une simulation fournie | **mettre en œuvre un protocole fourni ← ce lot** | vérifier en suivant un protocole |
| 4e | paramétrer une simulation | proposer un protocole *(lot 4e_C8.1)* | proposer, sur l'objet entier |
| 3e | mettre en œuvre une simulation | *proposer un protocole de tenue mécanique — **reste à créer*** | *(porté par la station, 3e_C9.2)* |

Ce lot est la **première marche** de la colonne du milieu. La dernière — `3e_C8.2` — est le seul
code C8 encore réellement absent du dépôt.

## Situation, problématique, verbe

- **Situation** : trois patères du hall ont cédé, toujours de la même façon — un sac trempé,
  accroché d'un coup sec. Le gestionnaire veut les remplacer, mais refuse de choisir au feeling :
  « Vous avez un laboratoire. Je veux un chiffre. »
- **Problématique** : *Comment savoir, avant de fabriquer, si un matériau tiendra la charge ?*
- **Le verbe est « mettre en œuvre », pas « inventer ».** Le protocole est fourni et il est juste.
  Ce qui s'évalue, c'est l'exécution fidèle. Proposer le protocole est le travail de 3ᵉ ; analyser
  les écarts, celui de 4ᵉ.

## Déroulé

| # | Activité | Durée | Production | Verrou |
|---|---|---|---|---|
| 0 | FAIRE d'abord : casser trois éprouvettes | 10 min | 2 réponses | **3 ruptures au banc** |
| 1 | Lire le protocole AVANT d'y toucher | 15 min | 4 réponses + 1 phrase | — |
| 2 | Mettre en œuvre : les cinq relevés | 25 min | 5 charges relevées | **5 ruptures au banc** |
| 3 | Décider, et le justifier | 20 min | 3 réponses + recommandation chiffrée | — |
| 4 | Ce que l'essai ne dit pas | 15 min | 5 associations | — |
| — | REFAIRE — l'étagère du CDI | 15 min | 3 lignes de protocole | — |

**Le vérificateur de l'activité 2 compare les cinq relevés aux vraies valeurs du banc** : un
chiffre recopié sur le voisin est refusé, et un chiffre inventé aussi. C'est le cœur du code —
en C8.2 on évalue la mise en œuvre, pas le nombre.

## Le banc d'essai

Original, écrit pour ce lot, en SVG et JavaScript : aucune dépendance, aucun compte, fonctionne
hors ligne. Cinq matériaux, éprouvette identique de 2 × 5 mm, charge par paliers de 10 ou 50 kg,
l'éprouvette s'allonge puis casse.

| Matériau | Charge de rupture | Ce que l'essai ne voit pas |
|---|---|---|
| Bois (pin) | 41 kg | un nœud, et la pièce casse bien plus tôt |
| PLA imprimé en 3D | 51 kg | en travers des couches, moins de la moitié |
| PVC rigide | 53 kg | il flue sous charge permanente |
| Aluminium | 194 kg | il se raye et se plie définitivement |
| Acier doux | 408 kg | en bord de mer, il rouille |

**Valeurs simulées, et la page le dit à l'élève.** Elles viennent des résistances à la traction
usuelles appliquées à une section de 10 mm² : l'ordre de grandeur est juste, les décimales
n'existent pas.

## Les deux moments qui font la séance

1. **Les cinq matériaux passent la barre des 40 kg.** C'est voulu : la traction ne départage pas,
   donc il faut un autre critère. C'est le pivot entre mesurer (C8.2) et choisir (C3.1).
2. **Le bois passe à 41 pour 40 exigés.** Beaucoup valideront — 41 > 40. La reprise tient en une
   phrase : *ton éprouvette était un morceau de bois parfait ; la planche du magasin a un nœud.*
   C'est là que le coefficient de sécurité cesse d'être une formule.

## Différenciation, inclusion, accessibilité

Hypothèse d'entrée non notée, reprise au bilan. Exercices en listes déroulantes (DYS). Corrections
dépliables activité par activité. Version 🅲 entièrement sans écran : le tableau de relevés
s'imprime et les cinq charges sont dans la correction — le travail reste lire, relever, décider.
Le banc est utilisable au clavier et sa figure porte `title` et `desc`.

## Évaluation

Formatif : verrous expérientiels aux activités 0 et 2, vérificateurs chiffrés partout,
auto-positionnement sur quatre niveaux. QCM : `qcm_5e_C8.2_patere-du-hall.html`, **30 questions,
90 réfutations**, codes 5e_C8.2 (20) et 5e_C3.1 (10) — les deux au-dessus du seuil de cinq
questions, donc le bilan par code est lisible (règle n°202).
**Sommative** à construire par l'enseignant. Aucun corrigé sommatif publié.

## Traces et preuves (honnêteté du lot)

Suite de tests réels : **14/14** sur la séquence, **17/17** sur le QCM, sous Chromium/Playwright,
hors ligne. Zéro erreur JavaScript, zéro boîte modale, aucune requête échouée.

**Ce que le lot ne porte pas :**

1. **Aucun essai physique.** Le banc est une simulation et la page l'écrit noir sur blanc
   (question 18 du QCM porte précisément là-dessus). Un essai réel, même rudimentaire — élastique,
   dynamomètre, éprouvettes de balsa — reste un ajout de valeur que ce lot ne fournit pas.
2. **La version 🅰 renvoie à une application à installer** : le « laboratoire des matériaux » du
   Réseau National Technologie Collège (éduscol STI), gratuit, sans compte, CC BY-NC-SA 3.0,
   versions PC et Mac. Elle n'est **pas** un prérequis : une séquence qui exige un téléchargement
   de plus est une séquence qui ne se fait pas.
3. **Aucune image.** Le banc *est* la figure, et il est interactif. Le lot n'a donc pas de dossier
   `Images/` rempli — ce qui est un choix, pas un oubli.
4. **Pas de bloc de rôles de groupe** : aucune activité n'est écrite comme un travail à plusieurs,
   et on ne pose pas un dispositif là où il ne sert pas (règle n°186).
