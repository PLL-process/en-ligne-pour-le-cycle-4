# Réconciliation du lot 5e_C1.3–C1.4

Date de reprise : 23 juillet 2026.

## Objectif

Reprendre le lot pilote `5e_C1.3–C1.4` au-dessus du `main` courant sans écraser les lots déjà publiés dans les Thèmes 2 et 3, puis aligner son QCM sur le moteur JavaScript commun et sur l’en-tête standard obligatoire.

## Source fonctionnelle à reprendre

Ancienne branche : `codex/theme-1/lot-5e-c1-3-c1-4-finalisation`.

Fichiers pédagogiques à réintégrer et contrôler :

- `sequence_C1.3-C1.4_SI_gestion_donnees.html` ;
- `qcm_systemes_information_donnees.html` ;
- `qcm-corrections-5e-c1-3-c1-4.js` ;
- `synthese_eleve_5e_C1.3-C1.4.html` ;
- `synthese_professeur_5e_C1.3-C1.4.html` ;
- `couverture_sequence_qcm.json` ;
- `RAPPORT_LOT_PILOTE.md`.

Les anciens composants génériques `_assets/qcm-eleve.*` ne doivent pas être réintroduits comme moteur concurrent. Le QCM doit réutiliser le moteur commun actuellement employé par les QCM du Thème 2.

## Contrôles bloquants

1. En-tête standard : titre, sous-titre, badges, retour vers la séquence et identité sauvegardée.
2. Carte `Ma progression` : barre et sept compteurs permanents.
3. Minuteur : démarrer, pause, reprendre et mode sans minuteur.
4. Modes : parcours complet, dix questions, révision ciblée, erreurs et questions marquées.
5. Corrections exhaustives : réponse, explication, exemple, erreur fréquente et notion à retenir.
6. Sauvegarde et reprise après fermeture.
7. Navigation clavier, focus visible, souris et tactile.
8. Responsive : ordinateur, tablette et téléphone.
9. Images v2 : image-objet, image-explication ou image-contexte seulement ; texte alternatif obligatoire ; aucune image décorative.
10. Liens réciproques entre séquence, QCM et synthèses.
11. Aucun fichier du Thème 2 modifié par ce lot.
12. Ajout à `nouveautes.json`, régénération de l’index et badge `NEW` seulement après publication réelle.

## Test automatisé ajouté

Le script `_outils/test_lot_theme1_5e_c1_3_c1_4.py` vérifie statiquement la présence des fichiers, les principaux marqueurs de l’en-tête standard, les sept compteurs, les modes, les textes alternatifs, les liens réciproques et la présence d’au moins trois activités.

Ce test statique ne valide pas à lui seul le minuteur, la sauvegarde, le tactile ou le rendu responsive. Ces contrôles doivent être exécutés dans un navigateur réel et consignés dans le rapport du lot.

## État de cette reprise

- nouvelle branche créée depuis le `main` courant ;
- script d’audit statique ajouté ;
- réintégration des pages pédagogiques et migration vers le moteur commun encore à effectuer ;
- aucun test fonctionnel déclaré réussi à ce stade ;
- aucune publication dans `main` pendant cette étape.
