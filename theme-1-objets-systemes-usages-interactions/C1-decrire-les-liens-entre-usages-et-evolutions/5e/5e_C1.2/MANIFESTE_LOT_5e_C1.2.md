# Manifeste du lot — 5e_C1.2

## Identification

- **Thème** : 1 — Objets, systèmes, usages et interactions
- **Niveau** : 5e
- **Compétence** : 5e_C1.2 — Comparer des principes techniques pour une même fonction technique
- **Branche** : `codex/theme-1/finaliser-5e-c1-2`
- **PR** : #51
- **Date de consolidation** : 25 juillet 2026

## Ressources du paquet

- `sequence_5e_C1.2_principes_techniques.html` — séquence élève complète ;
- `activite_crcn_donnees_freinage_5e_C1.2.html` — activité originale Chine–Martinique rendant le CRCN observable ;
- `donnees_simulees_freinage_5e_C1.2.csv` — jeu de données original, entièrement simulé, 3 lignes × 8 colonnes ;
- `qcm_principes_techniques.html` — QCM d’entraînement de 24 questions utilisant le moteur commun ;
- `synthese_eleve_5e_C1.2.html` — synthèse élève ;
- `synthese_professeur_5e_C1.2.html` — synthèse professeur ;
- `FICHE_PEDAGOGIQUE_5e_C1.2.md` — intentions, organisation, différenciation et preuve CRCN ;
- `RAPPORT_TESTS_5e_C1.2.md` — contrôles réellement exécutés et limites ;
- `MIGRATION_QCM_5e_C1.2.md` — traçabilité de la migration vers le moteur commun ;
- `SOURCES_MEDIAS.md` — provenance et statut des médias ;
- `Images/comparer_freins_velo.svg` et `Images/eclairer_principes.svg` — illustrations originales accessibles.

## Conformité pédagogique

- situation déclenchante contextualisée à Sainte-Luce ;
- ouverture sur Shenzhen 深圳 — *Shēnzhèn* et transfert critique vers Sainte-Luce ;
- données chinoises explicitement fictives et simulées ;
- problématique explicite ;
- trois activités progressives : identifier, comparer, choisir ;
- productions attendues, aides, corrections, exemples et erreurs fréquentes ;
- bilan placé avant les blocs de fin ;
- bloc QCM unique conforme à la règle d’or n°4 ;
- bonus facultatif placé après le QCM ;
- aucune activité de tracé des deux chaînes : règle d’or n°6 non déclenchée.

## 📌 Règle d’or n°7 — CRCN observable, tracé et justifié

| Champ obligatoire | Valeur du lot |
|---|---|
| Compétence exacte | CRCN 1.3 — Traiter des données |
| Niveau visé | Niveau 2 |
| Repère pour enseigner verbatim | « Insérer, saisir et trier des données dans un tableur pour les exploiter. » |
| Action observable | Enregistrer le CSV au format tableur, insérer une colonne, saisir, trier et filtrer. |
| Trace produite | Fichier `.ods` ou `.xlsx` transformé et export PDF contenant le tableau final et la recommandation. |

Le lot inscrit explicitement le principe : **« utiliser un ordinateur n’est pas une compétence »**. Le CRCN n’est donc pas attribué à l’ouverture d’un fichier, mais aux transformations constatables et aux traces remises.

Le cahier PIX 2026 a servi uniquement à étudier la progressivité des actions et le repère de niveau. Tous les scénarios, données, consignes, corrections et supports du lot sont originaux.

## Conformité du QCM

- titre, sous-titre, badges et lien de retour ;
- identité : Nom, Prénom, Classe, Date ;
- sauvegarde locale et reprise ;
- sept compteurs permanents de progression ;
- minuteur avec pause et mode sans minuteur ;
- modes complet, 10 questions, révision ciblée, erreurs et questions marquées ;
- navigation, marquage « À revoir », corrections détaillées et bilan final ;
- 24 questions comprenant explication, exemple, erreur fréquente et « À retenir » ;
- responsive, focus visible et impression A4.

## Tests réellement exécutés

- QCM : 44/44 contrôles Chromium ;
- activité CRCN, premier passage : 15/16, débordement de 17 px détecté à 320 px ;
- correction CSS appliquée ;
- activité CRCN, second passage : 16/16 ;
- affichages 320, 768 et 1440 px ;
- génération PDF A4, 3 pages, 91 806 octets ;
- aucune erreur console ;
- CSV : 3 lignes, 8 colonnes, aucune donnée personnelle.

## Périmètre

Le lot ne modifie aucun contenu des Thèmes 2 ou 3, aucun fichier de `.github/` et aucun script de `_outils/`.

## Étapes de livraison restantes

1. synchroniser le statut final du manifeste JSON ;
2. obtenir la garde de périmètre verte sur le dernier commit ;
3. repasser la PR #51 en Ready for review ;
4. fusion manuelle par Pascal.

Aucun test non exécuté n’est déclaré réussi dans ce manifeste.
