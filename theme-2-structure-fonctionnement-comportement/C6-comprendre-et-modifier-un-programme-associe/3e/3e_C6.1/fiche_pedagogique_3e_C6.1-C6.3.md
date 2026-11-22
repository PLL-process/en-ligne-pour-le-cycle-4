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

- **Situation** (simulation scolaire, annoncée comme telle : quartier, habitants et seuils inventés) : la sirène se déclenche pareil pour une tempête et un ouragan, et au niveau orange rien ne s'allume sur place ; le club techno implémente une alerte graduée — gyrophare/sirène selon le niveau — par simple modification du programme. Le seuil orange à 60 km/h est un réglage expérimental du club, jamais attribué à Météo-France.
- **Problématique** : *Comment modifier le programme pour créer une alerte graduée — sans casser ce qui fonctionne, et en prouvant que la modification est correcte ?*

## Déroulé

S1 : carte d'identité du programme sur la version 1 d'origine, figée (mesure, paramètre, donnée produite, mesure qui ne décide rien ; act. 1) + trace d'exécution, piège de la frontière, puis chemin suivi pas à pas (act. 2). S2 : 🔁 reprise de mémoire, 3 min (mesure ou paramètre ; vigilance à 90 km/h), avant tout rappel (n°369, en essai) ; les trois versions nommées (v1 d'origine, v1 recalibrée, v2) et le cahier des charges de la v2 ; modification de paramètre vérifiée en exécutant le programme (act. 3) + implémentation de l'alerte graduée, essayée par le banc d'essai sur 10 vents (act. 4). S3 : 🔁 reprise de mémoire, 3 min (le seuil recalibré à 57 km/h ; la pression lue qui ne décide rien) ; prévoir d'après le cahier des charges, exécuter sa version sur le banc, comparer — et diagnostiquer le bug >= d'une copie (act. 5) + réinvestissement « programme de la bouée », six questions puis trois explications écrites sans propositions, comme au brevet (n°346, 21/11/2026 : version étayée, correction avec phrases de copie, grille à trois critères cochée par l'élève, rien de noté) + bilan, qui demande ce qui reste flou et quand on le reprend (n°372, en essai) + QCM.

## Outils, versions, sécurité

**CodeLab Techno** (éditeur commun du projet : coloration, gutter, A−/A+, plein écran, export .py qui démarre dans un vrai Python grâce à une simulation de la maquette (le Bonus donne le programme corrigé, prêt pour Thonny), sauvegarde locale, surlignage de lignes, différences + / − avec la version d'origine) et son **banc d'essai** : un petit Python exécuté dans la page, hors ligne (`_outils/banc_python/`), qui joue le programme de l'élève sur des vents inventés — aucune donnée envoyée. Il lit le Python du collège (if / elif / else, affectations, textes, f-strings simples) ; une écriture qu'il ne lit pas (liste, boucle, fonction) est dite « limite du banc, pas forcément une erreur ». L'éditeur Python commun du dépôt (Skulpt) exécute un Python complet : voir `_outils/banc_python/LISEZMOI.md`. La version du programme se dit en permanence (« version 1 recalibrée », « version 2 »…). Versions : 🅰 maquette Arduino/Grove (TBT, matériel confirmé) ; 🅱 VittaScience/mBlock ; 🅲 tout dans la page. Python réel (transférable au lycée).

## Différenciation, inclusion, accessibilité

Aides ×2 ; corrections exhaustives dont correction commentée ligne par ligne (act. 4) ; A−/A+ et retour à la ligne pour le confort de lecture du code (DYS) ; navigation clavier ; reduced-motion ; impression A4 ; minuteur QCM désactivable ; vocabulaire FR/EN.

## Évaluation

Formative : vérificateurs intégrés qui **exécutent le programme réellement écrit par l'élève** (règle d'or n°333) — act. 3 : la valeur de SEUIL_ORANGE et son effet ; act. 4 : 10 vents comparés au cahier des charges, le premier écart nommé ; act. 5 : « mes prévisions » et « essais de ma version » séparés, un essai périmé dès que la version change (n°333), la version toujours dite (n°373), la prévision écrite avant l'essai (n°374). La justification d'act. 2 est écrite et relue par l'enseignant, jamais jugée par mots-clés. QCM 30 q (15/15, 6 illustrées) → bilan par compétence → LSU. Sommative à construire par l'enseignant, corrigé non publié.

## Bilan et prolongements

Vers 3e_C9.x (écrire un programme complet — Thème 3) ; défi pression (validation croisée, lien C4.3) ; transposition mBot2 ; EPI mathématiques (inéquations, encadrements).
