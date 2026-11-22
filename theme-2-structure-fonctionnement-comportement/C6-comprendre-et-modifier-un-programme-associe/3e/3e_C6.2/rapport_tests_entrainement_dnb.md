# Rapport de tests — Entraînement DNB « algorigrammes »

**Date** 21/11/2026 · **Agent** Fable (Thème 2) · révision après l'audit pédagogique et fonctionnel du même jour

Ce rapport ne déclare **que des tests réellement exécutés**. Le banc se rejoue depuis ce dossier :

```
python3 tests_entrainement_dnb.py     # Playwright + Chromium ; sortie 2 si Playwright manque (n°299)
```

La page se reconstruit avec `python3 _outils/dnb_build.py <page>`, puis les quatre outils d'injection
(`onglets_clavier`, `retrait_validation`, `onglets_seance`, `entete_telephone`, avec `--ecrire`).

## Résultat : 54 / 54 tests passés

| Ce que le banc vérifie | Résultat |
|---|---|
| aucune erreur JavaScript, au chargement et pendant tout le banc | ✅ |
| 30 exercices, 4 manches et l'épreuve écrite ; aucune liste déroulante (n°300) | ✅ |
| chaque exercice : fieldset, légende, 4 boutons radio d'un même groupe, valeur = texte de l'étiquette | ✅ |
| trois propositions fausses par exercice, chacune avec son pourquoi ; 2 aides et 3 réfutations par exercice | ✅ |
| corrections citées par leur texte, jamais par une lettre ; aides et corrections repliées au chargement | ✅ |
| onglets Symboles, Déroulement, Auto-test, Transfert, Épreuve écrite ; liens vers l'atelier en haut et en fin de manche 3 ; ancre `#banc-essai` présente dans l'atelier | ✅ |
| lien direct de l'accès rapide de l'index (ajouté le 21/11/2026, après la PR #844) : l'adresse `#ep` ouvre l'onglet « Épreuve écrite », `#exo17` ouvre la manche 3 | ✅ |
| rappel « cinq repères pour cet entraînement » ; chaque envoi au gardien dessiné dans un parallélogramme | ✅ |
| bonne réponse : chaque place dans chaque manche, au plus 2 fois ; jamais 3 fois de suite ; aucun motif répété | ✅ |
| **choisir toujours la plus longue ne valide aucune manche** ; répondre toujours à la même place non plus | ✅ |
| outil commun de la règle n°360 (`_outils/eleve_qui_ne_lit_pas.py`, ajouté le 21/11/2026) : aucune des huit stratégies sans lecture (plus longue, plus courte, chaque place, deux tirages au hasard) ne valide une manche | ✅ |
| manche parfaite : validée, « 8 / 8 renseignés », progression, deux tâches cochées, chaque exercice « ✔ juste » | ✅ |
| **6 justes + 2 blancs : « 6 / 8 renseignés · seuil atteint », exercices 15 et 16 à faire, tâche « Répondre aux 8 » non cochée** | ✅ |
| **une erreur en 17 : « À revoir : exercice 17 », « Revoir mon erreur » sans la bonne réponse, aide 1 ouverte d'un appui** | ✅ |
| une réponse changée après « Vérifier » retire la validation et le dit (n°340) | ✅ |
| trace de l'exercice 18 marquée case par case, sans retirer la validation ; « À toi » du rappel validé | ✅ |
| prédiction : les propositions attendent « Voir les propositions », la prédiction est gardée | ✅ |
| **après rechargement, les mêmes propositions sont cochées à la même place**, états et « Revoir » reviennent, « Où en suis-je ? » dit ce qui est à revoir | ✅ |
| mode essentiel : rappel replié mais présent, corrections et « Revoir » gardés, textes d'accompagnement retirés | ✅ |
| épreuve écrite : 4 réponses et grille gardées ; bandeau (réponses, correction lue, grille) ; aucun bouton qui note | ✅ |
| « Ma fiche bilan » : manches, erreurs avec leur pourquoi, réponses écrites | ✅ |
| contour d'un choix ≥ 3:1 sur la carte (mesuré ≈ 5:1) | ✅ |
| stockage refusé par le navigateur : l'élève est prévenu | ✅ |
| **page copiée seule dans un dossier vide, réseau coupé** : aucune erreur, aucun fichier manquant, schémas et couleurs présents | ✅ |
| aucun défilement horizontal à 320, 390 et 1 280 px, sur les cinq pages | ✅ |
| impression : manche ouverte seule, sans boutons ni replis fermés, texte foncé ; manche 4 en 6 pages A4 au plus (5 mesurées) | ✅ |

Rejoué sur l'ancienne page (`main`, d2a39ea), le banc échoue dès la structure : il sait voir ce que l'audit a vu.

## Contrôles du dépôt exécutés

Sur le dossier ou la page : `controle_validations`, `controle_propositions_indices`, `controle_schemas` (0 ✘ ; les deux
⚠ restants portent sur `trace_banc_essai.svg`, non modifié), `controle_schema_sous_les_yeux`, `controle_hors_ligne`,
`controle_code_colore` (8 listings en couleurs), `controle_contraste_liens`, `controle_tactile`, `controle_liens`,
`controle_hierarchie`, `controle_debordement`, `controle_impression`, `controle_verrous`, `banc_effacement`,
`sans_modale`, `controle_consignes_a_la_ligne`, `controle_ordre_propositions`, `controle_unites`, `controle_sigles`,
`controle_memes_nombres`, `controle_navigation_seances`, `controle_atteignabilite`, `controle_rapports_tests` : verts.

**axe-core 4.14** (WCAG 2.2 AA et bonnes pratiques), en 20 états — cinq onglets, 390 et 1 280 px, mode essentiel ou
non, après une vérification avec erreurs, tous les replis ouverts : **0 défaut**. Pendant la mesure, la barre de
navigation collante est rendue statique : sans cela, elle recouvrait un bouton radio au moment du calcul de
`target-size`, ce qui n'est pas un défaut de la page.

Atelier voisin (ancre `#banc-essai` ajoutée) : `tests_3e_C6.2.py` 22 / 22, `tests_regle_311_3e_C6.2.mjs` 34 / 34.

## Revue d'écran (trois tours, 390 px)

1. Schémas lus à 11 px environ → texte des schémas passé à 16, schéma pleine largeur de la carte au téléphone (≈ 13 px) ;
   tableau modèle à cinq colonnes qui débordait → filet mobile et région atteignable au clavier ; instruction citée
   coupée en fin de ligne (« pieces ← pieces + / 1 ») → espaces insécables.
2. Impression : 39 pages A4 pour la page entière, un schéma séparé de sa question → manche ouverte seule, replis fermés
   exclus, schémas hauts réduits à 5,7 cm de large, exercice insécable : 8, 4, 6, 5 et 2 pages.
3. Pied de page seul sur sa dernière page → retiré du papier, licence gardée.

## Ce qui n'a pas été vérifié

Lecteur d'écran réel ; appareils Android et Galaxy Tab physiques ; zoom réel du navigateur à 200 % (la largeur de
320 px, qui lui correspond, est vérifiée) ; impression sur une vraie imprimante (les PDF A4 de Chromium sont vérifiés) ;
durée réelle de chaque manche ; essai avec des élèves.
