# Réconciliation du lot 5e_C1.3–C1.4

Date de reprise : 23 juillet 2026.

## Objectif

Reprendre le lot pilote `5e_C1.3–C1.4` au-dessus du `main` courant sans écraser les lots déjà publiés dans les Thèmes 2 et 3, puis aligner son QCM sur le moteur JavaScript commun et sur l’en-tête standard obligatoire.

## État actuel

- Branche : `codex/theme-1/lot-5e-c1-3-c1-4-reconciliation-v2`.
- La séquence principale `sequence_C1.3-C1.4_SI_gestion_donnees.html` a été réintégrée depuis l’ancienne branche de finalisation.
- Les six SVG originaux, les deux synthèses, la matrice de couverture et `SOURCES_MEDIAS.md` sont présents.
- Le QCM historique n’est pas réintroduit tel quel : son moteur doit être remplacé par le moteur commun du Thème 2 conformément au skill `qcm-html-accessible`.

## Contrôles bloquants

1. Intégrer les six SVG dans les activités, corrections et questions qui les utilisent réellement.
2. Vérifier au moins trois activités progressives avec consigne, production attendue, aide, correction, exemple, erreur fréquente et À retenir.
3. Migrer le QCM vers l’en-tête standard : identité, sept compteurs, minuteur, modes de travail, navigation et résultat.
4. Réutiliser le moteur JavaScript de référence du Thème 2 ; ne pas réintroduire `_assets/qcm-eleve.*` comme moteur concurrent.
5. Garantir des corrections exhaustives : réponse, explication, exemple, erreur fréquente et notion à retenir.
6. Tester sauvegarde/reprise, minuteur, clavier, souris, tactile et responsive.
7. Contrôler les images v2 : image-objet, image-explication ou image-contexte seulement ; texte alternatif obligatoire ; aucune image décorative.
8. Vérifier les liens réciproques entre séquence, QCM et synthèses.
9. Ne modifier aucun fichier du Thème 2.
10. Mettre à jour `nouveautes.json` et régénérer l’index seulement après validation complète.

## Tests réellement effectués

- validation XML des six SVG ;
- présence de `title`, `desc` et `role="img"` ;
- poids de chaque SVG très inférieur à 300 Ko ;
- périmètre contrôlé : aucun fichier du Thème 2 modifié ;
- présence vérifiée de la séquence principale sur la branche de réconciliation.

Le script `_outils/test_lot_theme1_5e_c1_3_c1_4.py` est présent mais doit être relancé après migration du QCM. Aucun test fonctionnel navigateur n’est encore déclaré réussi.
