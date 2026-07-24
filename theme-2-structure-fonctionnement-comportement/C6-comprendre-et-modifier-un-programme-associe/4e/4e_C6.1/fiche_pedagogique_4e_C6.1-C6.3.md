# Fiche pédagogique — Ajuster le programme du jardin (4e_C6.1 · C6.3)

## Identification

| | |
|---|---|
| **Niveau** | 4e (cycle 4) |
| **Thème** | 2 — Structure, fonctionnement et comportement des objets et systèmes techniques |
| **Compétence parente** | C6 — Comprendre et modifier un programme associé à une fonctionnalité d'un objet ou d'un système technique |
| **Codes travaillés** | 4e_C6.1 (analyser les données et en déduire des modifications à apporter au programme) · 4e_C6.3 (tester et valider, dans un environnement simulé ou réel, une modification du programme) |
| **Code volontairement non traité** | 4e_C6.2 (compléter un programme) — couvert par la séquence modèle existante `4e_C6.2/sequence-jardin-connecte-arrosage-automatique.html`, non modifiée, référencée au bilan |
| **Socle** | D1.3, D2, D4 |
| **CRCN / Pix** | 1.3 Traiter des données (lecture de relevés) · 3.4 Programmer — usage transversal |
| **Durée** | 2 séances de 55 min |
| **Objet-fil** | « Le jardin connecté » (clôture de l'arc 4e : C4 structure → C6.2 programme → C5 dépannage → C6.1/C6.3 ajustement) |
| **Place dans l'année** | Après le LOT 10 (« SOS jardin connecté ») : le matériel vient d'être innocenté, la panne restante est logicielle |

## Problématique

Comment corriger un programme qui « marche »… mais qui fatigue la pompe et gaspille
l'eau — sans risquer de casser ce qui fonctionne ?

## Déroulé

| Séance | Question directrice | Activités | Production |
|---|---|---|---|
| 1 — Analyser et déduire (C6.1) | Que racontent les relevés — et comment les transformer en corrections ? | Act. 1 : lecture des relevés (battement 47 démarrages, arrosage 13 h, cas normal de contrôle) · Act. 2 : spécifier l'hystérésis (35/45) et la plage horaire, algorithme à compléter | 2 anomalies + causes au cahier · algorithme corrigé en 3 lignes SI/ALORS |
| 2 — Tester et valider (C6.3) | Comment modifier sans casser ? | Act. 3 : méthode en 5 étapes, banc de test à 4 scénarios (verrou 4/4), sauvegarde, non-régression · Act. 4 : transfert (lampadaire qui clignote au crépuscule) | Tableau scénario→verdict · 4/4 au transfert |

## Différenciation

- **Versions** : 🅰 maquette + programme réel Vittascience/mBlock (sauvegarde du fichier d'origine obligatoire ; TBT uniquement) · 🅱 banc de test intégré · 🅲 relevés imprimés + cahier.
- **Aides à 2 niveaux** partout ; corrections complètes après vérification.
- **Élèves rapides** : défis bonus (seuils cachés des appareils de la maison, compromis 35/45 vs 30/50, enquête « mise à jour qui casse »).
- **EBEP / DYS** : listes déroulantes exclusivement, banc au clic en ordre libre, navigation clavier, reduced-motion.

## Évaluation

- **Formative** : vérificateurs intégrés (verrou : 4 scénarios joués) + auto-positionnement par code.
- **Entraînement** : QCM 30 questions (15 par code, 3 illustrées, corrections exhaustives, réponses réparties 8/7/7/8).
- **Sommative** : à construire par l'enseignant (corrigé non publié dans le dépôt public). Items suggérés : relevés inédits à diagnostiquer (réfrigérateur qui bat) ; scénarios de test d'une hystérésis donnée.
- **LSU** : saisie par code (C6.1 / C6.3) via les critères de réussite affichés.

## Sécurité (transversale à la séquence)

- Très basse tension uniquement (12 V) pour la version 🅰 ; le secteur 230 V est explicitement désigné comme interdit.
- Règle logicielle de sécurité enseignée comme telle : sauvegarde AVANT modification, simulation AVANT réel, périmètre limité (plant témoin) AVANT généralisation.

## Matériel (version 🅰)

Maquette jardin des lots précédents (carte, capteur d'humidité, pompe 12 V), ordinateur avec
Vittascience ou mBlock, le fichier programme d'origine À SAUVEGARDER avant toute modification,
un verre d'eau et le plant témoin pour la validation réelle.
