# Rapport des tests réellement exécutés — Shanghai 5e_C3.1 à C3.4

**Branche contrôlée :** `codex/theme-1/shanghai-c3-fiche-pedagogique-v1`  
**Dernière actualisation documentaire :** 2026-07-27

## Méthode

Contrôles statiques et vérifications GitHub réalisés directement sur les contenus UTF-8 de la branche. Ce rapport ne revendique aucun test navigateur, aucune simulation de lecteur d’écran et aucune impression PDF tant que ces essais n’ont pas été réellement exécutés.

## Jeu de données CSV simulées

| Contrôle exécuté | Résultat | Preuve observée |
|---|---:|---|
| Fichier présent | ✅ Réussi | `donnees_vehicules_dernier_kilometre_shanghai_simulees.csv` |
| Encodage lisible | ✅ Réussi | contenu UTF-8 récupéré par le connecteur GitHub |
| Séparateur homogène | ✅ Réussi | point-virgule sur l’en-tête et les trois lignes |
| Nombre de solutions | ✅ Réussi | vélo-cargo, fourgonnette électrique, robot mobile |
| Cohérence pédagogique | ✅ Réussi | indicateurs de performance, d’usage, de cycle de vie et de contexte présents |
| Caractère simulé explicite | ✅ Réussi | aucune donnée commerciale réelle revendiquée |

**Bilan CSV : 6/6 réussis.**

## Séquence

| Contrôle exécuté | Résultat |
|---|---:|
| Document HTML et langue française | ✅ Réussi |
| Balise viewport | ✅ Réussi |
| Titre principal suivi de la mission | ✅ Réussi |
| Situation déclenchante et problématique | ✅ Réussi |
| Quatre activités progressives | ✅ Réussi |
| Productions, aides et corrections | ✅ Réussi |
| Bloc « À retenir » | ✅ Réussi |
| Ordre `Bilan → QCM → Bonus` | ✅ Réussi |
| Bloc QCM unique | ✅ Réussi |
| Bouton QCM unique | ✅ Réussi |
| Bonus canonique | ✅ Réussi |
| SVG avec titre et description | ✅ Réussi |
| Préparation à l’impression déclarée | ✅ Réussi |
| Ancrage Shanghai–Martinique | ✅ Réussi |
| Données simulées signalées | ✅ Réussi |

**Bilan statique de la séquence : 15/15 réussis.**

## QCM séparé

| Contrôle exécuté | Résultat |
|---|---:|
| Document HTML autonome et langue française | ✅ Réussi |
| En-tête pédagogique | ✅ Réussi |
| Retour vers la séquence | ✅ Réussi |
| Champs d’identité | ✅ Réussi |
| Modes entraînement et examen | ✅ Réussi |
| Sauvegarde et reprise prévues | ✅ Réussi |
| Sept compteurs de progression | ✅ Réussi |
| Minuteur prévu | ✅ Réussi |
| Navigation séquentielle | ✅ Réussi |
| Navigation directe | ✅ Réussi |
| Marquage « à revoir » | ✅ Réussi |
| Corrections détaillées | ✅ Réussi |
| Bilan par compétence | ✅ Réussi |
| Responsive déclaré | ✅ Réussi |
| Impression prévue | ✅ Réussi |
| Trente questions couvrant C3.1 à C3.4 | ✅ Réussi |

**Bilan statique du QCM : 16/16 réussis.**

## Répartition des bonnes réponses

| Position correcte | Nombre observé |
|---|---:|
| A | 8 |
| B | 8 |
| C | 7 |
| D | 7 |

**Bilan : distribution équilibrée 8/8/7/7.**

## Pointeurs de mutualisation

| Code | Séquence | QCM | Synthèse élève | Synthèse professeur | Trace propre | Résultat |
|---|---:|---:|---:|---:|---:|---:|
| `5e_C3.2` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ Réussi |
| `5e_C3.3` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ Réussi |
| `5e_C3.4` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ Réussi |

**Bilan : 3/3 pointeurs conformes.**

## Conformité au modèle fonctionnel du Thème 2

Le QCM de référence du Thème 2 contrôlé sur `main` utilise lui aussi une banque de questions et une logique JavaScript intégrées dans le même fichier HTML. Aucun moteur JavaScript externe mutualisé n’a été observé dans cette référence.

| Contrôle exécuté | Résultat | Preuve observée |
|---|---:|---|
| Une seule logique d’exécution dans le QCM Shanghai | ✅ Conforme | un seul bloc fonctionnel interne au fichier |
| Aucun second moteur concurrent créé dans le Thème 1 | ✅ Conforme | aucun fichier moteur séparé ajouté |
| Fonctions attendues du modèle de référence | ✅ Présentes statiquement | identité, sauvegarde, reprise, sept compteurs, minuteur, modes, navigation, corrections et bilan |

**Bilan architectural : conforme au modèle fonctionnel réellement observé dans le Thème 2.** Cette conclusion ne remplace pas les tests navigateur restant à exécuter.

## Garde de périmètre et état GitHub

- garde de périmètre GitHub Actions déjà observée en succès sur la branche ;
- fichiers modifiés exclusivement dans le Thème 1 lors du dernier contrôle ;
- aucun fichier `_outils/`, `.github/`, Thème 2 ou Thème 3 modifié ;
- PR #75 toujours en brouillon ;
- branche divergente de `main` : rebase obligatoire avant livraison finale.

## Contrôles restant à exécuter avant Ready for review

- rebaser la branche sur `origin/main` ;
- valider le HTML avec un outil dédié ;
- tester le QCM dans un navigateur : identité, sauvegarde, reprise, sept compteurs, minuteur, deux modes, navigation, marquage à revoir, corrections et bilan ;
- tester entièrement le clavier ;
- vérifier les largeurs 320 px, 768 px et 1440 px ;
- vérifier les contrastes ;
- produire et contrôler l’impression A4 ou l’export PDF ;
- ajouter le lot dans `JOURNAL_DES_DECISIONS.md` et `nouveautes.json` racine sans écraser les autres thèmes ;
- exécuter `python _outils/build_audit.py`, puis `python _outils/make_index.py`, sans modifier les scripts ;
- intégrer uniquement les fichiers générés autorisés ;
- exécuter une nouvelle garde de périmètre sur le commit final.

## Conclusion

Les contrôles statiques totalisent **37 réussites sur 37** : 15 pour la séquence, 16 pour le QCM et 6 pour le CSV. La répartition des réponses est équilibrée, les trois pointeurs de mutualisation sont conformes et l’ancienne conclusion erronée imposant un moteur JavaScript externe a été supprimée. Le lot reste en brouillon jusqu’au rebase, aux essais fonctionnels réels, à la mise à jour des fichiers racine, à la régénération de l’audit et de l’index et à la garde finale.