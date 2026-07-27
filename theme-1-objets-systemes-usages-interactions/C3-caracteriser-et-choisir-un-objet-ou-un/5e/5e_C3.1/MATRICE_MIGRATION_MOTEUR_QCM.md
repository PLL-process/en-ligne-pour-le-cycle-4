# Matrice de conformité — QCM Shanghai et référence fonctionnelle du Thème 2

## Objet

Ce document fixe le contrat de conformité du fichier `qcm_5e_C3.1-C3.4_shanghai.html` par rapport au QCM de référence du Thème 2, sans modifier les contenus du Thème 2 ni créer de moteur concurrent.

## État réellement observé le 27 juillet 2026

Le fichier QCM de la branche `codex/theme-1/shanghai-c3-fiche-pedagogique-v1` a été relu directement via le connecteur GitHub.

| Contrôle exécuté | Résultat observé |
|---|---|
| Banque pédagogique présente | 30 questions couvrant `C3.1` à `C3.4` |
| Corrections détaillées | une explication associée à chaque question |
| Champs d’identité | nom et classe présents |
| Modes de travail | entraînement et examen présents |
| Progression | sept compteurs présents |
| Sauvegarde et reprise | logique `localStorage` intégrée |
| Navigation | séquentielle et directe intégrées |
| Bilan par compétence | présent |
| Architecture JavaScript | moteur fonctionnel interne au fichier |
| Séparation banque / logique | non exigée par le fichier de référence contrôlé |

## Audit direct du fichier de référence du Thème 2

Le fichier suivant a été contrôlé directement sur `main` :

`theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/5e/5e_C5.1/qcm_5e_C5.1-C5.3_depanner_lampadaire.html`

Résultat vérifiable :

- l’interface standard attendue est présente : identité, sept compteurs, minuteur, modes, navigation, corrections détaillées, reprise, bilan, responsive et impression ;
- le fichier ne charge pas de moteur JavaScript externe partagé ;
- sa banque de questions et sa logique d’exécution sont intégrées dans un bloc `<script>` interne au même fichier ;
- aucun chemin de moteur mutualisé externe n’existe dans cette référence contrôlée.

## Arbitrage technique fondé sur la référence réelle

Dans ce dépôt, l’expression « moteur JavaScript commun du Thème 2 » est interprétée comme **le modèle fonctionnel de référence du Thème 2**, et non comme une ressource externe inexistante.

Conséquences :

1. ne pas inventer de balise `<script src="…">` ni de chemin de moteur partagé ;
2. ne pas modifier le Thème 2 ;
3. conserver une seule logique d’exécution dans le QCM Shanghai ;
4. vérifier que cette logique reproduit les fonctions attendues de la référence : identité, sauvegarde, reprise, sept compteurs, minuteur, modes, navigation, corrections détaillées, bilan par compétence, responsive, clavier et impression ;
5. ne créer aucun second fichier moteur partagé dans le Thème 1.

## Éléments propres au lot à conserver

- titre : choix d’une solution de livraison à Shanghai ;
- niveau : 5e ;
- compétences : `C3.1`, `C3.2`, `C3.3`, `C3.4` ;
- 30 questions ;
- distribution des bonnes réponses : A/B/C/D = `8/8/7/7` ;
- lien de retour vers `sequence_5e_C3.1-C3.4_shanghai.html` ;
- vocabulaire Shanghai–Martinique et mention explicite des données simulées ;
- explications de correction existantes.

## Tests fonctionnels restant à exécuter

| Test réel attendu | Critère de réussite |
|---|---|
| Chargement de la page | aucune erreur JavaScript dans la console |
| Comptage des questions | 30 questions accessibles |
| Identité | nom et classe conservés après sauvegarde/reprise |
| Modes | entraînement et examen produisent les comportements attendus |
| Sept compteurs | tous se mettent à jour correctement |
| Minuteur | progression visible et cohérente |
| Navigation clavier | accès aux réponses et boutons sans souris |
| Navigation directe | accès aux 30 questions |
| Marquage à revoir | état conservé après navigation et reprise |
| Corrections | affichées seulement selon le mode choisi |
| Bilan | résultats regroupés par `C3.1` à `C3.4` |
| Impression | bilan lisible en A4 |
| Responsive | contrôlé à 320 px, 768 px et 1440 px |
| Persistance | sauvegarde, fermeture, réouverture et reprise réussies |

## Critère de sortie

La conformité architecturale est considérée comme établie par comparaison directe avec la référence réelle du Thème 2. La PR ne pourra toutefois passer en Ready for review qu’après :

- les tests fonctionnels ci-dessus réellement exécutés et consignés dans `RAPPORT_TESTS_REELS.md` ;
- le rebase sur `origin/main` ;
- la mise à jour des fichiers racine autorisés ;
- la régénération de l’audit et de l’index par les scripts autorisés ;
- une garde de périmètre finale verte.