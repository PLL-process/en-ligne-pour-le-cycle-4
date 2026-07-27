# Rapport des tests réellement exécutés — Shanghai 5e_C3.1 à C3.4

**Date d’exécution :** 2026-07-26, actualisations GitHub les 2026-07-27  
**Branche contrôlée :** `codex/theme-1/shanghai-c3-fiche-pedagogique-v1`  
**Fichiers contrôlés :**
- `sequence_5e_C3.1-C3.4_shanghai.html` ;
- `qcm_5e_C3.1-C3.4_shanghai.html` ;
- `donnees_vehicules_dernier_kilometre_shanghai_simulees.csv` ;
- `nouveautes.json` local du lot ;
- les pointeurs `5e_C3.2/README.md`, `5e_C3.3/README.md` et `5e_C3.4/README.md`.

## Méthode

Contrôle statique manuel effectué sur les contenus UTF-8 récupérés directement depuis la branche GitHub. Ce rapport ne revendique aucun test navigateur, aucune simulation de lecteur d’écran et aucune impression PDF tant que ces essais n’ont pas été réellement exécutés.

## Test réellement exécuté — jeu de données CSV simulées

Le fichier CSV référencé par la séquence et la fiche pédagogique a été récupéré directement depuis la branche puis relu ligne par ligne.

| Contrôle exécuté | Résultat | Preuve observée |
|---|---:|---|
| Fichier présent au chemin annoncé | ✅ Réussi | `donnees_vehicules_dernier_kilometre_shanghai_simulees.csv` |
| Encodage textuel lisible | ✅ Réussi | contenu UTF-8 récupéré par le connecteur GitHub |
| Séparateur homogène | ✅ Réussi | point-virgule sur l’en-tête et les trois lignes de données |
| Nombre de solutions | ✅ Réussi | 3 lignes : vélo-cargo, fourgonnette électrique, robot mobile |
| Cohérence avec les activités | ✅ Réussi | charge utile, autonomie, freinage, braquage, bruit, énergie, durée de vie, réparabilité, matière recyclée, ruelles et pluie |
| Caractère simulé explicite | ✅ Réussi | nature pédagogique indiquée dans les documents du lot ; aucune donnée commerciale revendiquée |

**Bilan du contrôle CSV : 6/6 réussis.**

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
| Garde de périmètre GitHub Actions sur la tête `baa93f4d2e459ba764a2102064760f5daacf3c06` | ✅ Réussi | exécution n°119, workflow `Garde-périmètre des thèmes`, état `completed`, conclusion `success` |
| Liste des fichiers modifiés de la PR | ✅ Réussi | contrôle GitHub du 27/07/2026 : 12 fichiers, tous situés dans le Thème 1 ; aucun contenu des Thèmes 2 et 3 |
| État de fusion GitHub avant le présent commit documentaire | ✅ Réussi | PR #75 déclarée fusionnable sans conflit (`mergeable: true`) |

## Actualisation GitHub réellement exécutée le 27/07/2026

| Contrôle exécuté | Résultat | Preuve observée |
|---|---:|---|
| Relecture de la PR #75 par le connecteur GitHub | ✅ Réussi | PR ouverte, en brouillon et fusionnable sans conflit |
| Vérification de la tête de branche avant cette actualisation | ✅ Réussi | tête observée : `3e396be157823bceb1914cf6d78853f49ac547b6` |
| Comparaison avec `main` | ⚠️ Rebase requis | branche observée en retard sur `main` ; le rebase reste obligatoire avant livraison |
| Nouvelle énumération du périmètre | ✅ Réussi | 12 chemins modifiés, tous sous `theme-1-objets-systemes-usages-interactions/C3-.../5e/` |
| Contrôle des zones interdites | ✅ Réussi | aucun chemin sous `_outils/`, `.github/`, `theme-2-structure-fonctionnement-comportement/` ou `theme-3-creation-conception-realisation-innovations/` |
| Statut CI sur la tête observée | ℹ️ Non revendiqué | aucun nouveau test CI n’a été exécuté dans cette actualisation documentaire |

Cette actualisation ne revendique aucun nouveau test navigateur. Elle consigne seulement les contrôles GitHub effectivement observés et rend explicite le rebase nécessaire avant livraison.

## Test réellement exécuté — pointeurs de mutualisation 5e_C3.2 à C3.4

Les trois fichiers `README.md` ont été relus directement sur la branche via le connecteur GitHub.

| Code | Séquence | QCM | Synthèse élève | Synthèse professeur | Trace observable propre | Résultat |
|---|---:|---:|---:|---:|---:|---:|
| `5e_C3.2` | ✅ | ✅ | ✅ | ✅ | ✅ tableau ou graphique comparatif multicritère | ✅ Réussi |
| `5e_C3.3` | ✅ | ✅ | ✅ | ✅ | ✅ schéma du cycle de vie et limites d’un indicateur unique | ✅ Réussi |
| `5e_C3.4` | ✅ | ✅ | ✅ | ✅ | ✅ matrice multicritère, pondérations et transfert Shanghai–Martinique | ✅ Réussi |

Les quatre liens de chaque pointeur utilisent les mêmes chemins relatifs valides vers le lot porteur `5e_C3.1` : séquence, QCM, synthèse élève et synthèse professeur. Chaque compétence mutualisée conserve en outre une production observable distincte.

**Bilan du contrôle des pointeurs : 3/3 fichiers conformes.**

## Contrôles restant à exécuter avant passage en Ready for review

- rebaser la branche sur `origin/main` ;
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

La séquence, le QCM séparé et le jeu de données CSV possèdent leur structure pédagogique complète. Les contrôles statiques totalisent **37 réussites sur 37 contrôles** : 15 pour la séquence, 16 pour le QCM et 6 pour le CSV. La répartition des réponses est **8/8/7/7** et les trois pointeurs de mutualisation sont conformes. La garde de périmètre déjà exécutée est verte sur l’exécution n°119. Le contrôle GitHub du 27 juillet 2026 confirme un périmètre strictement limité au Thème 1, mais la branche reste à rebaser sur `main`. Le lot demeure donc en brouillon jusqu’au rebase, aux essais fonctionnels réels, à la mise à jour des deux fichiers racine, à la régénération des fichiers communs et à la garde finale.
