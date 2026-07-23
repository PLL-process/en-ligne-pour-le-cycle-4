# Fiche pédagogique / inspection — Programmer l'alerte

## Identification

| Champ | Valeur |
|---|---|
| Niveau | 3e (programme 2024, applicable rentrée 2026-2027) |
| Codes | 3e_C6.1 · 3e_C6.3 (3e_C6.2 déjà couvert par la séquence « Algorigrammes DNB » existante, liée en révision) |
| Thème | Thème 2 — Structure, fonctionnement, comportement |
| Compétence parente | C6 — Comprendre et modifier un programme associé à une fonctionnalité d'un OST |
| Référentiel | BO n°9 du 29/02/2024 · cahier Nathan 3e (éd. 2024) |
| Domaines du socle | D1.3, D2, D4 |
| CRCN | 3.4 Programmer |
| Durée | 3 séances de 55 min |

## Sous-compétences

| Code | Intitulé | Activités |
|---|---|---|
| 3e_C6.1 | Déterminer les données utilisées et produites par un programme associé à une fonctionnalité en vue de le modifier. | 1, 2, R |
| 3e_C6.3 | Modifier et tester le programme associé à une nouvelle fonctionnalité d'un OST. | 3, 4, 5, R |

## Prérequis

3e_C6.2 (algorigrammes — séquence existante à réviser avant la séance 2) ; 4e_C6.2 « Jardin connecté » (compléter un programme) ; variables et conditions vues en 5e/4e ; le projet-fil station (C4, C5).

## Situation déclenchante et problématique

- **Situation** : la sirène « tout ou rien » n'est plus crédible (alerte orange ignorée) ; le club techno implémente une alerte graduée — gyrophare/sirène selon le niveau — par simple modification du programme.
- **Problématique** : *Comment modifier le programme pour créer une alerte graduée — sans casser ce qui fonctionne, et en prouvant que la modification est correcte ?*

## Déroulé

S1 : CodeLab découverte + carte d'identité entrées/sorties (act. 1) + trace d'exécution, piège de la frontière (act. 2). S2 : modification de paramètre avec vérification du code réel (act. 3) + implémentation de l'alerte graduée d'après l'algorigramme, vérificateur analysant le code de l'élève (act. 4). S3 : plan de tests aux frontières + diagnostic d'un bug >= (act. 5) + réinvestissement « programme de la bouée » + bilan + QCM.

## Outils, versions, sécurité

**CodeLab Techno** (éditeur commun du projet : coloration, gutter, A−/A+, plein écran, export .py, sauvegarde locale, surlignage de lignes, comparaison) — aucune exécution requise, aucune donnée envoyée. Versions : 🅰 maquette Arduino/Grove (TBT, matériel confirmé) ; 🅱 VittaScience/mBlock ; 🅲 tout dans la page. Python réel (transférable au lycée).

## Différenciation, inclusion, accessibilité

Aides ×2 ; corrections exhaustives dont correction commentée ligne par ligne (act. 4) ; A−/A+ et retour à la ligne pour le confort de lecture du code (DYS) ; navigation clavier ; reduced-motion ; impression A4 ; minuteur QCM désactivable ; vocabulaire FR/EN.

## Évaluation

Formative : vérificateurs intégrés, dont **analyse du code réellement écrit par l'élève** dans CodeLab (act. 3 : seuil modifié ; act. 4 : les 4 ajouts, avec liste explicite de ce qui manque). QCM 30 q (15/15, 6 illustrées) → bilan par compétence → LSU. Sommative à construire par l'enseignant, corrigé non publié.

## Bilan et prolongements

Vers 3e_C9.x (écrire un programme complet — Thème 3) ; défi pression (validation croisée, lien C4.3) ; transposition mBot2 ; EPI mathématiques (inéquations, encadrements).
