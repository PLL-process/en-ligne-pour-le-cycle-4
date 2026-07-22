# Fiche pédagogique / inspection — Station d'alerte cyclonique connectée

## Identification

| Champ | Valeur |
|---|---|
| Niveau | 3e (programme 2024, applicable rentrée 2026-2027) |
| Codes | 3e_C4.3 · 3e_C4.4 · 3e_C4.5 · 3e_C4.6 |
| Thème | Thème 2 — Structure, fonctionnement, comportement : des objets et des systèmes techniques à comprendre |
| Compétence parente | C4 — Décrire et caractériser l'organisation interne d'un OST et ses échanges avec son environnement (énergies, données) |
| Référentiel | BO n°9 du 29/02/2024 · cahier Nathan 3e (éd. 2024) |
| Domaines du socle | D1.3, D1.4, D2, D4, D5 |
| CRCN | 1.2 Gérer des données · 1.3 Traiter des données · 3.4 Programmer (initiation, pseudo-code) · 5.2 Évoluer dans un environnement numérique |
| Durée | 4 séances de 55 min |
| Discipline pilote | Technologie |

## Sous-compétences travaillées

| Code | Intitulé (Nathan 3e / BO 2024) | Activités |
|---|---|---|
| 3e_C4.3 | Décrire un OST en caractérisant sa chaîne d'information. | 1, 2, R |
| 3e_C4.4 | Associer des grandeurs analogiques issues d'un OST à des données exploitables. | 3, R |
| 3e_C4.5 | Représenter sous forme de données les informations de diverses natures utilisées par un OST. | 4, R |
| 3e_C4.6 | Identifier, selon les cas, leur mise en forme, leur transmission ou leur stockage dans des fichiers (texte, image, son…). | 5, 6, R |

## Prérequis

- Cycle 4 (5e/4e) : notion de capteur et d'actionneur, chaînes d'énergie et d'information abordées en 5e_C4.5 et 4e_C4.4 ;
- Mathématiques : proportionnalité, puissances (2ⁿ introduit progressivement) ;
- Usage élémentaire d'un tableur (5e_C1.x).

## Situation déclenchante et problématique

- **Situation** : vigilance météo en Martinique ; le collège de Sainte-Luce veut une station d'alerte autonome capable de prévenir le quartier même sans Internet.
- **Problématique** : *Comment la station transforme-t-elle des grandeurs physiques (vent, pluie, pression) en données numériques fiables, afin de déclencher l'alerte au bon moment ?*
- **Ancrage local** : risque cyclonique réel, mémoire des épisodes récents, autonomie énergétique et redondance des communications.

## Déroulé séance par séance

### Séance 1 — Qui fait quoi dans la station ? (C4.3)
1. Accroche (10 min) : situation déclenchante, recueil des hypothèses (traces conservées dans la page).
2. Activité 1 (25 min) : décoder la station — attribution des fonctions aux 8 constituants + justification énergie/information.
3. Activité 2 (20 min, débordement possible en début de S2) : construction de la chaîne d'information, nature des signaux, seuil d'alerte.

### Séance 2 — Du signal à la donnée (C4.4)
1. Rappel (5 min) : chaîne complète au tableau.
2. Activité 3 (40 min) : simulateur de CAN intégré (version C), calculs de paliers/précision/conversion. Atelier parallèle possible en version A (Arduino + Grove, lecture analogRead) ou B (VittaScience).
3. Bilan intermédiaire (10 min) : formule de conversion verbalisée.

### Séance 3 — Représenter les informations en données (C4.5)
1. Rappel express (5 min).
2. Activité 4 (40 min) : typage, descripteurs, enregistrement, codage binaire de la vigilance, dimensionnement 2ⁿ ≥ V.
3. Synthèse partielle (10 min) : lecture commune du SVG « types et codage ».

### Séance 4 — Fichiers et réinvestissement (C4.6 + bilan)
1. Activité 5 (20 min) : formats de fichiers, transmission = copie, redondance.
2. Activité 6 (20 min) : enquête dans les 48 h de données (page ou LibreOffice Calc).
3. Réinvestissement (15 min, achevable à la maison) : bouée houlographe — transfert intégral sans modèle.
4. Bilan personnel + annonce du QCM d'entraînement (à la maison ou en AP).

## Organisation de la classe

- Travail en binômes sur postes ou tablettes ; activités individualisables à la maison (page autonome, hors connexion après chargement).
- Version A en îlot encadré (6-8 élèves en rotation) pendant que le reste travaille en versions B/C.
- Aucune donnée personnelle ne quitte l'appareil (sauvegarde localStorage uniquement).

## Matériel et logiciels

| Type | Retenu | Alternatives |
|---|---|---|
| Matériel (version A) | Arduino UNO / UNO R4 Minima + Grove Base Shield V2 (5 V) + capteur luminosité + LCD RGB Grove | — |
| Simulation (version B) | VittaScience (en ligne, gratuit) | mBlock 5 |
| Sans matériel (version C) | Simulateur HTML intégré + jeu de données CSV/ODS/XLSX | — |
| Tableur | LibreOffice Calc | tableau intégré à la page ; XLSX fourni |

**MATÉRIEL À CONFIRMER — prévoir une alternative par simulation** : compatibilité bibliothèque LCD ↔ UNO R4 Minima non testée.

**Sécurité** : très basse tension uniquement ; jamais de secteur manipulé par les élèves ; sélecteur 3,3 V/5 V du shield vérifié ; câblage validé par l'enseignant avant mise sous tension.

## Différenciation, inclusion, accessibilité

- Aides graduées à deux niveaux dans chaque activité ; corrections exhaustives repliables.
- Trois versions (A/B/C) : aucun élève pénalisé par l'absence de matériel.
- Accessibilité : navigation clavier, contrastes conformes, textes alternatifs sur tous les SVG, `prefers-reduced-motion` respecté, minuteur du QCM désactivable, impression A4.
- Élèves allophones : vocabulaire FR/EN dans la synthèse ; schémas très visuels.

## Évaluation

- **Formative** : vérificateurs intégrés à chaque activité (score + feedback), progression visible, bilan personnel guidé.
- **Entraînement** : QCM séparé de 32 questions (8 par code) avec bilan par compétence et note indicative /20.
- **Sommative éventuelle** : à construire par l'enseignant à partir de la matrice de couverture ; **aucune correction sommative publiée dans le dépôt public**.
- **Critères LSU** (par code) : maîtrise ≥ 75 % des items du code au QCM = « maîtrisé » ; 50-74 % = « en cours » ; < 50 % = « fragile » — à croiser avec l'observation en classe.

## Bilan et prolongements

- Vers P2 (3e_C6.x, C9.x) : programmer réellement le seuil d'alerte (mBlock/Arduino/Python).
- Vers P3 (3e_C4.7, C4.8) : connecter la station au réseau, circulation de l'information sur Internet (Filius).
- EDD : sobriété énergétique des transmissions, résilience des infrastructures en milieu insulaire.
- EPI possible : Physique-Chimie (pression atmosphérique), Géographie (risques naturels aux Antilles).
