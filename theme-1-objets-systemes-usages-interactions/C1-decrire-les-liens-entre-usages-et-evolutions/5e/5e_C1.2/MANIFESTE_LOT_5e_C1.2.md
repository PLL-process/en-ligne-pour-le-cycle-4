# Manifeste du lot — 5e_C1.2

## Identification

- **Thème** : 1 — Objets, systèmes, usages et interactions
- **Niveau** : 5e
- **Compétence** : 5e_C1.2 — Comparer des principes techniques pour une même fonction technique
- **Branche** : `codex/theme-1/finaliser-5e-c1-2`
- **PR** : #51
- **Date de consolidation** : 24 juillet 2026

## Ressources du paquet

- `sequence_5e_C1.2_principes_techniques.html` — séquence élève complète ;
- `qcm_principes_techniques.html` — QCM d’entraînement de 24 questions utilisant le moteur commun ;
- `synthese_eleve_5e_C1.2.html` — synthèse élève ;
- `synthese_professeur_5e_C1.2.html` — synthèse professeur ;
- `FICHE_PEDAGOGIQUE_5e_C1.2.md` — intentions, organisation et différenciation ;
- `RAPPORT_TESTS_5e_C1.2.md` — contrôles réellement exécutés et tests restant à mener ;
- `MIGRATION_QCM_5e_C1.2.md` — traçabilité de la migration vers le moteur commun ;
- `SOURCES_MEDIAS.md` — provenance et statut des médias ;
- `Images/comparer_freins_velo.svg` et `Images/eclairer_principes.svg` — illustrations originales accessibles.

## Conformité pédagogique vérifiée

- situation déclenchante contextualisée à Sainte-Luce ;
- problématique explicite ;
- trois activités progressives : identifier, comparer, choisir ;
- productions attendues, aides, corrections, exemples et erreurs fréquentes ;
- bilan placé avant les blocs de fin ;
- bloc QCM unique conforme à la règle d’or n°4 ;
- bonus facultatif placé après le QCM ;
- aucune activité de tracé des chaînes d’information et d’énergie dans ce lot : la règle d’or n°6 n’est donc pas déclenchée.

## Conformité du QCM vérifiée statiquement

- titre, sous-titre, badges et lien de retour ;
- identité : Nom, Prénom, Classe, Date ;
- sauvegarde locale et reprise ;
- sept compteurs permanents de progression ;
- minuteur avec pause et mode sans minuteur ;
- modes complet, 10 questions, erreurs et questions marquées ;
- navigation, marquage « À revoir », corrections détaillées et bilan final ;
- 24 questions comprenant explication, exemple, erreur fréquente et « À retenir » ;
- responsive, focus visible et impression A4 présents dans le code.

## Périmètre

Le lot ne modifie aucun contenu des Thèmes 2 ou 3, aucun fichier de `.github/` et aucun script de `_outils/`.

## Étapes de livraison restantes

1. ajouter l’entrée structurante dans `JOURNAL_DES_DECISIONS.md` ;
2. ajouter l’entrée 5e_C1.2 dans `nouveautes.json` sans altérer les autres thèmes ;
3. régénérer `audit_couverture.csv`, `audit_couverture.json`, `index.html` et `README.md` avec les scripts existants ;
4. exécuter les tests navigateur et clavier réels disponibles ;
5. effectuer le rebase final sur `main` et obtenir la garde de périmètre verte ;
6. passer la PR #51 en Ready for review.

Aucun test non exécuté n’est déclaré réussi dans ce manifeste.