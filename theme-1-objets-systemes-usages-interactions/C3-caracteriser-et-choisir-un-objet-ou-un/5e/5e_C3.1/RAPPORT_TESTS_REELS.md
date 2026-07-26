# Rapport des tests réellement exécutés — Shanghai 5e_C3.1 à C3.4

**Date d’exécution :** 2026-07-26  
**Branche contrôlée :** `codex/theme-1/shanghai-c3-fiche-pedagogique-v1`  
**Fichiers contrôlés :**
- `sequence_5e_C3.1-C3.4_shanghai.html` ;
- `qcm_5e_C3.1-C3.4_shanghai.html`.

## Méthode

Contrôle statique manuel effectué sur les contenus UTF-8 récupérés directement depuis la branche GitHub. Ce rapport ne revendique aucun test navigateur, aucune simulation de lecteur d’écran et aucune impression PDF tant que ces essais n’ont pas été réellement exécutés.

## Résultats — séquence

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

**Bilan du contrôle statique de la séquence : 15/15 réussis.**

## Résultats — QCM séparé

| Contrôle exécuté | Résultat | Élément vérifié |
|---|---:|---|
| Document HTML autonome et langue définie | ✅ Réussi | `<!doctype html>` et `<html lang="fr">` |
| En-tête pédagogique | ✅ Réussi | titre, sous-titre, badges niveau/compétences/30 questions |
| Retour vers la séquence | ✅ Réussi | lien relatif vers la séquence Shanghai |
| Champs d’identité | ✅ Réussi | nom et classe |
| Modes de travail | ✅ Réussi | entraînement et examen |
| Sauvegarde et reprise prévues | ✅ Réussi | `localStorage`, bouton de reprise et bouton de recommencement |
| Progression à sept compteurs | ✅ Réussi | question, répondues, correctes, incorrectes, restantes, à revoir, temps |
| Minuteur prévu | ✅ Réussi | compteur `cTemps` initialisé à `00:00` |
| Navigation séquentielle | ✅ Réussi | boutons précédente et suivante |
| Navigation directe | ✅ Réussi | navigation générée pour les 30 questions |
| Marquage « à revoir » | ✅ Réussi | état dédié et bouton de marquage |
| Corrections détaillées | ✅ Réussi | explication associée à chacune des 30 questions |
| Bilan par compétence | ✅ Réussi | regroupement C3.1, C3.2, C3.3 et C3.4 |
| Responsive déclaré | ✅ Réussi | `meta viewport` et règle CSS sous 520 px |
| Impression prévue | ✅ Réussi | règle `@media print` et bouton d’impression |
| Répartition des questions | ✅ Réussi | 30 questions couvrant C3.1 à C3.4 |

**Bilan du contrôle statique du QCM : 16/16 réussis.**

## Test supplémentaire — répartition des bonnes réponses

Le champ d’index de bonne réponse de chacune des 30 questions a été relevé directement dans la banque JavaScript après permutation des options, puis compté par position.

| Position correcte | Nombre observé | Résultat |
|---|---:|---:|
| A — index `0` | 8 | ✅ Équilibré |
| B — index `1` | 8 | ✅ Équilibré |
| C — index `2` | 7 | ✅ Équilibré |
| D — index `3` | 7 | ✅ Équilibré |

**Bilan du test de répartition : réussi.** La distribution est désormais A/B/C/D = **8/8/7/7**. Le contenu pédagogique et les explications ont été conservés ; seules les positions des options ont été permutées. Correction enregistrée dans le commit `bad96eb3eab736e83e5068986770a5c8658b0cc9`.

## Résultat — garde de périmètre

| Contrôle exécuté | Résultat | Preuve |
|---|---:|---|
| Garde de périmètre GitHub Actions | ✅ Réussi | exécution n°109 sur le commit `321b6882e6afb7916528533542a2b5c5eeda214f` |
| Liste des fichiers modifiés de la PR | ✅ Réussi | contrôle GitHub du 26/07/2026 : uniquement Thème 1 ; aucun contenu des Thèmes 2 et 3 |

## Contrôles restant à exécuter avant passage en Ready for review

- validation HTML avec un outil dédié ;
- navigation clavier complète dans un navigateur ;
- essais responsive aux largeurs 320 px, 768 px et 1440 px ;
- impression A4 ou export PDF ;
- vérification des contrastes ;
- tests fonctionnels réels du moteur QCM : identité, sauvegarde, reprise, sept compteurs, minuteur, modes, navigation, corrections, bilan par compétence et impression ;
- ajout du lot dans `JOURNAL_DES_DECISIONS.md` et `nouveautes.json` racine ;
- régénération de l’audit et de l’index par les scripts autorisés ;
- nouvelle garde de périmètre sur le commit final.

## Conclusion

La séquence et le QCM séparé possèdent leur structure pédagogique complète. Les contrôles statiques de structure totalisent **31 réussites sur 31 contrôles**. Le défaut bloquant de distribution des bonnes réponses a été corrigé et le nouveau comptage est **8/8/7/7**. Le lot reste en brouillon jusqu’aux essais fonctionnels réels, à la mise à jour des deux fichiers racine, à la régénération des fichiers communs et à la garde finale.