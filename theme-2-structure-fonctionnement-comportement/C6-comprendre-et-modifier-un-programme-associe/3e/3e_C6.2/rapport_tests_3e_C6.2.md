# Rapport de tests — 3e_C6.2 « L'auto-test de la station »

**Date** 08/08/2026 · **Agent** Fable (Thème 2) · **Branche** `fable/theme-2/lot-algorigrammes-3e`

Ce rapport ne déclare **que des tests réellement exécutés**. La suite est reproductible :

```
python3 tests_3e_C6.2.py     # depuis ce dossier, Playwright + Chromium
```

## Résultat : 22 / 22 tests passés

| Test exécuté | Résultat |
|---|---|
| séquence : aucune erreur JS au chargement | ✅ passé |
| séquence : bandeau de tâches affiché (n°30) | ✅ passé |
| billet d'entrée : oriente sans sanctionner (n°26) | ✅ passé |
| banc d'essai : compte 2 défauts et ne redescend pas | ✅ passé |
| banc d'essai : détecte la défaillance silencieuse | ✅ passé |
| verrou expérientiel : l'activité 4 refuse sans les deux essais | ✅ passé |
| mode essentiel : bascule et masque le référentiel (n°29) | ✅ passé |
| sauvegarde puis restauration après rechargement | ✅ passé |
| onglets de séance : le bandeau suit la séance affichée | ✅ passé |
| blocs règle n°4 présents (entraînement + bonus) | ✅ passé |
| un seul bouton QCM dans toute la séquence | ✅ passé |
| n°34 : tout champ de saisie porte une étiquette | ✅ passé |
| n°34 : pas de défilement horizontal à 1280 px | ✅ passé |
| n°34 : pas de défilement horizontal à 420 px | ✅ passé |
| n°34 : le focus clavier reste visible (Tab) | ✅ passé |
| QCM : aucune erreur JS au chargement | ✅ passé |
| QCM : 30 questions | ✅ passé |
| QCM : 3 questions illustrées, alt renseigné | ✅ passé |
| QCM : bonnes réponses réparties sur A/B/C/D | ✅ passé |
| QCM : aucune réfutation en face de la bonne réponse | ✅ passé |
| QCM : chaque distracteur est réfuté | ✅ passé |
| QCM : les 5 champs obligatoires sont remplis partout | ✅ passé |

## Ce que la suite couvre, et ce qu'elle ne couvre pas

Elle couvre : l'absence d'erreur JavaScript sur les deux pages, le bandeau de tâches et son
suivi des onglets de séance, le billet d'entrée sans note et son message d'orientation, le banc
d'essai (comptage à deux pannes, détection de la défaillance silencieuse), le verrou
expérientiel de l'activité 4, le mode essentiel, la sauvegarde et la restauration après
rechargement, les blocs de la règle n°4, l'unicité du bouton QCM, l'étiquetage de tous les
champs de saisie, l'absence de défilement horizontal à 1280 px et à 420 px, la persistance du
focus clavier, puis côté QCM le compte de questions, les figures et leurs alternatives, la
répartition des bonnes réponses sur A/B/C/D, l'absence de réfutation en face de la bonne
réponse, la réfutation de chaque distracteur et la présence des cinq champs de correction.

Elle ne couvre **pas** : le rendu à l'impression A4, le contraste mesuré point par point, la
lecture réelle par un lecteur d'écran, et le comportement sous zoom navigateur à 200 %. Ces
quatre points de la check-list n°34 n'ont pas été vérifiés automatiquement — ils sont donc
déclarés **non vérifiés**, et non « conformes ».

## Vérificateur des règles d'or

```
python3 _outils/verif_regles_audit.py theme-2-.../C6-.../3e/
```

Sur `sequence_3e_C6.2_auto_test_station.html` : **7 règles sur 7 au vert** — n°23 (144 min
annoncés plus 10 de marge de service, pour 165 disponibles), n°26, n°29, n°30, n°31 (5 versions
étayées pour 5 zones de rédaction), n°33, n°34.

## Écarts assumés dans le dossier

`sequence_algorigrammes_dnb.html`, la banque d'entraînement héritée, reste signalée en échec sur
la règle n°29 : elle n'est pas bâtie sur le gabarit maison, et l'outil de rétrofit a refusé de la
traiter plutôt que d'y poser un mode essentiel à moitié câblé. Elle n'est pas modifiée ici ; son
statut devient **ressource d'entraînement**, ce qui est la vérité, et non « séquence incomplète ».

## Correction faite au passage

Le lien « ⌂ Accueil » de la séquence pointait cinq niveaux au-dessus du dossier au lieu de
quatre, et ne menait donc nulle part. Corrigé. Le même défaut existe dans
`qcm_book-train.html` (lot 4e_C4.1, déjà fusionné) : corrigé également, puisqu'il s'agit d'un
lien mort dans un lot dont je suis l'auteur.
