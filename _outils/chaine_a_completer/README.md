# Chaîne à compléter — les étiquettes posées dans le schéma

Demande de Pascal du 15/11/2026 : « L'élève a beaucoup de questions sur la chaîne d'énergie et la chaîne
d'information, mais n'a pas la représentation sous les yeux. Il n'arrive pas à l'avoir en tête ; quand on lui
demandera de la construire, il aura des difficultés. » Il veut que l'élève pose les étiquettes **directement dans la
chaîne**, que le schéma soit **toujours sous ses yeux**, qu'il le voie **se bâtir progressivement**, pour les deux
chaînes, et qu'il y manipule.

## Ce que fait l'outil

- **Le schéma est la question.** Les cases sont à la place des mots : la fonction dans le bloc, le composant dessous,
  la forme d'énergie sur la flèche, ce que porte la flèche d'ordre. L'élève touche une étiquette, puis sa case ; ou il
  la fait glisser ; au clavier, Entrée sur l'étiquette mène à la première case vide.
- **Le schéma se bâtit.** Une étape montre en clair ce que l'élève a trouvé aux étapes d'avant (`acquis`), en
  pointillés ce qui viendra plus tard (`vides`, « tu la construiras en séance 3 »). Au lampadaire de 5e : les
  fonctions du bas, puis les formes d'énergie, puis la chaîne d'information au-dessus de la chaîne d'énergie déjà
  bâtie, puis les deux chaînes de mémoire en séance 6.
- **Toujours la même image** : celle des schémas du dépôt (n°6, n°310) — l'information en haut, l'énergie en bas,
  l'ordre qui descend ; les couleurs des fonctions (n°120). Tant qu'une fonction est à trouver, son bloc reste
  neutre : la couleur la soufflerait.
- **Rien ne change pour la page** : poser une étiquette coche le bouton radio du groupe (`fieldset.qcm-groupe`) que
  la case désigne. La sauvegarde, la vérification de la page, le mode mission, les bancs et l'impression lisent
  toujours ces groupes. Sans JavaScript, les groupes restent visibles.
- **Le mode mission** voit l'étape comme un écran : il vérifie les groupes, laisse les justes, rend les fausses à la
  réserve (classe `ms-origine`) et dit leur pourquoi ; le dessin suit leurs marques (✓, ✗).
- **Deux dispositions** : en ligne à partir de 760 px, en colonne au téléphone (le dessin prend toute la largeur de
  l'écran ; la réserve tient sur une ligne qui défile de côté). Une étape peut recadrer la colonne sur la seule
  chaîne travaillée (`vue`).
- **Sur le papier** : le dessin, en encre, avec ce que l'élève a posé ; les cases vides sont des cases à remplir au
  stylo ; la liste des étiquettes est écrite dessous.

## Écrire une étape

1. Le dessin, une fois par page, dans un `<script>` : `window.CAC_DESSINS.<nom> = {seuil, large: {vue}, etroit:
   {vue, max}, elements: [...]}`. Le mode d'emploi des éléments (titre, bloc, flèche, texte) est en tête de
   `chaine.js`. Modèle : le lampadaire, `5e_C4.1`.
2. À la place des questions :

```html
<div class="cac" data-cac='{"dessin": "lampadaire", "cases": {"convertir-panneau.fonction": "e2_f1", …},
                             "acquis": {…}, "vides": ["g:information"], "reutilisables": true}'>
<div class="cac-questions">
<fieldset class="qcm-groupe" id="e2_f1"> <legend>La fonction du panneau solaire</legend> … </fieldset>
…
</div>
</div>
```

   Chaque groupe porte les mêmes propositions, dans le même ordre : ce sont les étiquettes de la réserve. Une ou deux
   de trop, plausibles (règle du mode mission contre le tâtonnement). La légende nomme la case : le mode mission la
   cite dans le pourquoi d'une erreur.
3. Les bonnes réponses restent dans la vérification de la page (`const att = {…}`) ; le pourquoi de chaque mauvaise
   étiquette, case par case, dans `mission_<lot>.json`, posé par `_outils/mode_mission/enrichir.py`.

## Fichiers

| Fichier | Rôle |
|---|---|
| `chaine.js`, `chaine.css` | la source unique |
| `poser.py` | pose ou met à jour le bloc dans une page (`python3 _outils/chaine_a_completer/poser.py <page>`) |
| `../controle_chaine_a_completer.py` | le bloc d'une page est celui de la source, une fois ; chaque étape nomme un dessin déclaré et des groupes qui existent |

Le banc générique du mode mission (`_outils/mode_mission/banc_generique.mjs`) joue aussi ces étapes : il pose les
bonnes étiquettes dans le schéma, comme un élève qui sait, puis vérifie.
