# Rapport de tests — lot Hangzhou 4e_C3.1 à C3.3

**Date** 08/08/2026 · **Agent** Fable · **Branche** `fable/theme-1/lot-hangzhou-4e-C3`

```
python3 tests_4e_C3.1-C3.3_hangzhou.py     # depuis ce dossier, Playwright + Chromium
```

## Résultat : 28 / 28 tests passés

**Séquence** — aucune erreur JavaScript · aucune ressource distante (n°40) · bandeau de tâches
(n°30) · 9 zones de rédaction pour 9 versions étayées (n°31) · chaque champ étiqueté (n°34) ·
alternatives longues sur les deux figures · billet d'entrée sans note (n°26) · **verrou du cahier
des charges** : l'activité 1 exige quatre exigences écrites contenant au moins quatre chiffres, et
se valide une fois rédigées · **verrou de l'analyse** en activité 2 · mode essentiel qui masque
référentiel et corrections en laissant les versions étayées visibles · sauvegarde et restauration ·
blocs de la règle n°4 · un seul bouton QCM · aucun défilement horizontal à 1280 ni à 390 px.

**QCM** — aucune erreur JavaScript · aucune ressource distante · 30 questions · 2 illustrées avec
alternative longue · réponses réparties 8/7/7/8 · aucune réfutation en face de la bonne réponse ·
chaque distracteur réfuté · les trois codes couverts · les cinq champs de correction remplis.

## Vérificateur des règles d'or

**7 règles sur 7 au vert** — n°23 (145 min annoncés plus 10 de marge pour 220 disponibles), n°26,
n°29, n°30, n°31, n°33, n°34.

## Un défaut trouvé par les tests

Quatre réfutations de distracteurs étaient **trop courtes** — « Aucun rapport. », « Une seule
suffit. » Le test qui exige plus de vingt caractères par réfutation les a rejetées, et il avait
raison : une réfutation de trois mots n'enseigne rien. Elles ont été réécrites pour dire *pourquoi*
la réponse est fausse, ce qui est tout l'intérêt de la réfutation.

C'est un test que j'avais écrit pour le lot précédent et qui a servi ici sans que j'y pense : un
contrôle utile survit à son lot d'origine.

## Ce que la suite ne couvre pas

Impression A4, contraste mesuré, lecteur d'écran réel, zoom 200 % : **non vérifiés**, donc **non
déclarés conformes**. Le travail au tableur de l'activité 2 se fait hors de la page et n'est pas
testable automatiquement ; la trace attendue est décrite dans la séquence.
