# Journal du lot — 5e_C1.2

Date de consolidation : 24 juillet 2026

## Décisions appliquées

1. Le paquet `5e_C1.2` est traité comme une ressource complète distincte : séquence, QCM, synthèses élève et professeur, fiche pédagogique, médias documentés et rapport de tests.
2. La séquence respecte la règle d’or n°4 : titre suivi de la mission, bilan, bloc QCM unique, puis bonus facultatif avant le pied de page.
3. Le QCM historique a été remplacé par l’interface standard commune : identité sauvegardée, sept compteurs de progression, minuteur, modes de travail, navigation, marquage « à revoir », corrections détaillées et bilan final.
4. L’ancien moteur JavaScript concurrent n’est plus conservé dans la version proposée par la PR #51.
5. Les tests non exécutés ne sont pas déclarés réussis. Les validations navigateur, clavier et GitHub Pages restent explicitement séparées des contrôles statiques.
6. Aucun contenu des Thèmes 2 et 3 n’est modifié par ce lot.

## Contrôles statiques déjà réalisés

- présence d’une situation déclenchante et d’une problématique ;
- trois activités progressives ;
- productions attendues, aides, corrections, exemples et erreurs fréquentes ;
- bouton QCM unique ;
- ordre `Bilan → QCM → Bonus` ;
- chemins relatifs vers les deux SVG et le QCM ;
- présence des 24 questions et des champs pédagogiques de correction.

## Étapes de prépublication restantes

- intégrer l’entrée du lot au fichier racine `nouveautes.json` sans altérer les entrées des autres thèmes ;
- reporter cette décision dans le journal racine ;
- régénérer l’audit et le tableau de bord avec les scripts existants ;
- exécuter les validations navigateur et clavier disponibles ;
- effectuer le rebase final et vérifier la garde de périmètre.
