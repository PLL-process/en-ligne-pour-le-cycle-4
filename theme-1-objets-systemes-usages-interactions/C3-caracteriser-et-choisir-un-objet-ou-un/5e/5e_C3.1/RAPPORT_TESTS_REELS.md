# Rapport des tests réellement exécutés — Shanghai 5e_C3.1 à C3.4

**Date d’exécution :** 2026-07-26  
**Branche contrôlée :** `codex/theme-1/shanghai-c3-fiche-pedagogique-v1`  
**Fichier contrôlé :** `sequence_5e_C3.1-C3.4_shanghai.html`

## Méthode

Contrôle statique manuel effectué sur le contenu UTF-8 récupéré directement depuis la branche GitHub. Ce rapport ne revendique aucun test navigateur, aucune simulation de lecteur d’écran et aucune impression PDF tant que ces essais n’ont pas été réellement exécutés.

## Résultats

| Contrôle exécuté | Résultat | Élément vérifié |
|---|---:|---|
| Document HTML déclaré et langue définie | ✅ Réussi | `<!doctype html>` et `<html lang="fr">` |
| Adaptation aux écrans déclarée | ✅ Réussi | balise `meta viewport` |
| Titre principal unique puis mission | ✅ Réussi | un seul `<h1>` suivi du bloc `.mission` |
| Situation déclenchante et problématique | ✅ Réussi | sections présentes avant les activités |
| Progression pédagogique | ✅ Réussi | quatre activités numérotées de 1 à 4 |
| Productions, aides et corrections | ✅ Réussi | productions explicites, blocs `.aide` et corrections dépliables |
| Bloc « À retenir » | ✅ Réussi | six acquis essentiels listés |
| Ordre imposé par la règle d’or n°4 | ✅ Réussi | bilan, puis QCM, puis bonus, avant le pied de page |
| Bloc QCM unique | ✅ Réussi | une occurrence de `🧠 Prêt·e à t’entraîner ?` |
| Bouton QCM unique | ✅ Réussi | une occurrence de `🚀 Ouvrir le QCM d’entraînement` |
| Bonus facultatif | ✅ Réussi | titre canonique et trois défis ouverts |
| SVG intégré accessible | ✅ Réussi | `role="img"`, `<title>` et `<desc>` sur le cycle de vie |
| Préparation à l’impression | ✅ Réussi | règle CSS `@media print` présente |
| Ancrage territorial et ouverture | ✅ Réussi | Shanghai, caractères simplifiés, pinyin, transfert Martinique |
| Données simulées explicitement signalées | ✅ Réussi | avertissement répété dans les activités et la synthèse |

**Bilan de ce contrôle statique : 15/15 réussis.**

## Contrôles restant à exécuter avant passage en Ready for review

- validation HTML avec un outil dédié ;
- navigation clavier complète ;
- essais responsive aux largeurs 320 px, 768 px et 1440 px ;
- impression A4 ou export PDF ;
- vérification des contrastes ;
- ouverture effective du futur QCM séparé ;
- tests fonctionnels du moteur QCM commun : identité, sauvegarde, reprise, sept compteurs, minuteur, modes, navigation, corrections, bilan par compétence et impression ;
- exécution de la garde de périmètre ;
- régénération de l’audit et de l’index par les scripts autorisés.

## Conclusion

La séquence HTML possède déjà sa structure pédagogique complète et respecte statiquement la règle d’or n°4. Le lot reste volontairement en brouillon : le QCM séparé, les contrôles fonctionnels, le journal, `nouveautes.json` et les fichiers générés restent à finaliser.