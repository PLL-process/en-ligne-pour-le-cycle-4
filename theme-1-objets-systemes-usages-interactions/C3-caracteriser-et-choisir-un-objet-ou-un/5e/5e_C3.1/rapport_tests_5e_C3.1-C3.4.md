# Rapport de tests — lot Shanghai 5e_C3.1 à C3.4

**Date** 08/08/2026 · **Agent** Fable · **Branche** `fable/theme-1/lot-shanghai-5e-C3`


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
> 27 / 27 tests passés
> ```
Ce rapport ne déclare **que des tests réellement exécutés** :

```
python3 tests_5e_C3.1-C3.4_shanghai.py     # depuis ce dossier, Playwright + Chromium
```

## Résultat : 27 / 27 tests passés

**Séquence** — aucune erreur JavaScript · aucune ressource distante appelée (règle n°40) · bandeau
de tâches affiché (n°30) · 8 zones de rédaction pour 8 versions étayées (n°31) · chaque champ
étiqueté (n°34) · chaque figure dotée d'une alternative de plus de 120 caractères · billet d'entrée
qui oriente sans note (n°26) · activité 1 reconnue à 7/7 · progression mise à jour · **verrou de
rédaction de l'activité 2** : la justification écrite est exigée, et l'activité se valide une fois
rédigée · mode essentiel qui masque référentiel et corrections **en laissant les versions étayées
visibles** · sauvegarde et restauration après rechargement · blocs de la règle n°4 présents · un
seul bouton QCM · aucun défilement horizontal à 1280 px ni à 390 px.

**QCM** — aucune erreur JavaScript · aucune ressource distante · 30 questions · 3 illustrées avec
alternative longue · bonnes réponses réparties 8/7/7/8 sur A/B/C/D · aucune réfutation en face de la
bonne réponse · chaque distracteur réfuté · les quatre codes couverts · les cinq champs de
correction remplis partout.

## Vérificateur des règles d'or

```
python3 _outils/verif_regles_audit.py theme-1-.../C3-.../
```

**7 règles sur 7 au vert** — n°23 (145 min annoncés plus 10 de marge, pour 220 disponibles), n°26,
n°29, n°30, n°31, n°33, n°34.

## Deux défauts trouvés par les tests, et corrigés

**Le champ `img` du QCM était un tableau, pas un objet.** Ma fonction de construction rangeait le
couple `(source, alternative)` tel quel, alors que le gabarit du dépôt attend `{src, alt}`. Les
trois questions illustrées n'auraient affiché **aucune image** — et le défaut ne se voyait pas à la
lecture du fichier source, seulement à l'exécution.

**Un test qui interrogeait l'affichage au lieu du document.** Le contrôle des blocs de la règle n°4
utilisait `innerText`, qui ignore les panneaux de séance masqués : il déclarait absents des blocs
présents dans une séance non affichée. Le test lit désormais le document. C'est la troisième fois
de la journée qu'un test accuse à tort une page conforme — le réflexe est acquis : chercher lequel
des deux a tort avant de toucher au code.

## Ce que la suite ne couvre pas

Le rendu à l'impression A4, le contraste mesuré point par point, la lecture par un vrai lecteur
d'écran et le zoom navigateur à 200 % **n'ont pas été vérifiés automatiquement**. Ils sont déclarés
**non vérifiés**, et non « conformes ».

Le travail au tableur de l'activité 4 n'est pas testable automatiquement : il se fait hors de la
page, dans le logiciel de l'élève. La séquence en décrit précisément la trace attendue (colonne
calculée par formule, tri, filtre), et c'est cette trace qui fait la preuve du CRCN 1.3.
