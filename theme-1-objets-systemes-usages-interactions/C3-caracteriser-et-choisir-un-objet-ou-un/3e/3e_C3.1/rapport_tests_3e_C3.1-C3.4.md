# Rapport de tests — lot Shenzhen 3e_C3.1 à C3.4

**Date** 08/08/2026 · **Agent** Fable · **Branche** `fable/theme-1/lot-shenzhen-3e-C3`


> **Correction du 31/08/2026 — la suite de ce lot était rouge, et c'est le test qui avait tort.**
> Réexécutée ce jour-là (personne ne l'avait relancée depuis sa livraison), elle échouait sur
> « séquence : hors ligne, aucune ressource distante (n°40) ». La cause n'était pas dans la
> page : le contrôle cherchait la chaîne `http://` dans le HTML sérialisé, où **chaque SVG en
> ligne porte son `xmlns="http://www.w3.org/2000/svg"** — un identifiant d'espace de noms, que
> nul navigateur ne va chercher. Le contrôle regarde désormais ce que la page **irait charger**
> (`src`, `link href`, `object data`, `iframe`, `use`), sans les hyperliens, qui ont le droit
> d'être distants. Vérifié dans les deux sens : la suite passe, et elle redevient rouge si l'on
> injecte une vraie ressource distante dans la page.
>
> ```
> 28 / 28 tests passés
> ```
```
python3 tests_3e_C3.1-C3.4_shenzhen.py     # depuis ce dossier, Playwright + Chromium
```

## Résultat : 28 / 28 tests passés

**Séquence** — aucune erreur JavaScript · aucune ressource distante (n°40) · bandeau de tâches
(n°30) · 9 zones de rédaction pour 9 versions étayées (n°31) · chaque champ étiqueté (n°34) ·
alternative longue sur la figure · billet d'entrée sans note (n°26) · **verrou de la liste** :
l'activité 1 exige une liste nommant les trois familles, et se valide une fois écrite ·
**verrou de la grille** en activité 2 · mode essentiel qui masque référentiel et corrections en
laissant les versions étayées visibles · sauvegarde et restauration · blocs de la règle n°4 · un
seul bouton QCM · aucun défilement horizontal à 1280 ni à 390 px.

**QCM** — aucune erreur JavaScript · aucune ressource distante · 30 questions · 1 illustrée avec
alternative longue · réponses réparties 8/7/7/8 · aucune réfutation en face de la bonne réponse ·
chaque distracteur réfuté · les quatre codes couverts · les cinq champs de correction remplis.

## Vérificateur des règles d'or

**7 règles sur 7 au vert** — n°23 (145 min annoncés plus 10 de marge pour 220 disponibles), n°26,
n°29, n°30, n°31, n°33, n°34.

## Un défaut trouvé par les tests, pour la deuxième fois

Quatre réfutations de distracteurs étaient **trop courtes** — « Aucun lien. », « Rien ne le
garantit. » Le même contrôle qui les avait attrapées dans le lot de 4e les a rejetées ici. Elles
ont été réécrites pour dire *pourquoi* la réponse est fausse.

C'est un défaut que je reproduis : quand une réponse fausse me paraît évidente, j'écris une
réfutation courte. Or c'est exactement là qu'un élève a besoin d'explication. Le test compense un
biais que la relecture ne voit pas.

## Ce que la suite ne couvre pas

Impression A4, contraste mesuré, lecteur d'écran réel, zoom 200 % : **non vérifiés**, donc **non
déclarés conformes**. Le travail au tableur de la séance 2 et la mise en œuvre réelle du protocole
de la séance 3 se font hors de la page et ne sont pas testables automatiquement ; les traces
attendues sont décrites dans la séquence et dans la synthèse professeur.
