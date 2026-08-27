# Rapport de tests — les quatre QCM de C7 et C8

**Date** : 27 août 2026 · **Suite** : `tests_qcm_c7_c8.mjs` (Playwright, chromium)
**Commande** : `NODE_PATH=<node_modules> node tests_qcm_c7_c8.mjs`

## Résultat

**63 tests, 63 verts, 0 rouge.** Quinze contrôles par QCM sur quatre QCM, plus
trois contrôles transversaux.

| QCM | Questions | A / B / C / D | Illustrées | Nuances | Tests |
|---|---:|---|---:|---:|---:|
| `qcm_5e_C7_mini-projet.html` | 30 | 8 / 7 / 7 / 8 | 3 | 9 | 15 verts |
| `qcm_4e_C7_jardin-conception.html` | 30 | 8 / 7 / 7 / 8 | 3 | 22 | 15 verts |
| `qcm_4e_C8_jardin-validation.html` | 30 | 8 / 7 / 7 / 8 | 3 | 16 | 15 verts |
| `qcm_3e_C7_capteur-confort-ny.html` | 30 | 8 / 7 / 7 / 8 | 3 | 16 | 15 verts |
| *le cliquet des absolus* | — | — | — | 13 déclarés | 3 verts |

## Ce que la suite vérifie — et rien d'autre

1. **Aucune erreur JavaScript** au chargement.
2. **30 questions** par banque.
3. **Chaque question est complète** : 4 propositions, 4 réfutations, explication,
   exemple, « à retenir ».
4. **`d[r]` est vide** : la case de la bonne réponse ne porte pas de réfutation.
5. **Chaque distracteur est réfuté** : aucune chaîne vide ailleurs qu'en `d[r]`.
6. **Bonnes réponses réparties** : au moins 6 par position.
7. **Trois questions illustrées**, et le fichier SVG **se charge réellement**
   (`naturalWidth > 0`). Un `src` cassé serait invisible autrement : l'image
   manquante ne fait pas d'erreur JS.
8. **Chaque image porte une alternative rédigée** de plus de 40 caractères.
9. **Chaque SVG porte `<title>` et `<desc>`** (règle images v2).
10. **Répondre faux est compté faux**, et **la réfutation affichée est bien celle
    de la proposition choisie** — pas celle d'une autre.
11. **Répondre juste est compté juste.**
12. **Aucune correction rendue ne contient « undefined »** — les trente
    corrections de chaque QCM sont produites et relues (voir ci-dessous).
13. **Chaque nuance écrite est effectivement affichée** dans le bloc de
    correction. Un champ ajouté à la banque et jamais rendu ne sert à personne.
14. **La progression est restaurée** après rechargement de la page.
15. **Aucun lien relatif mort**, et **aucun débordement horizontal à 390 px**.

Puis, sur les quatre banques à la fois — **le cliquet des absolus** :

16. aucune tournure de loi (*toujours, jamais, systématiquement, il suffit de,
    tous les*) dans une réfutation ou un « à retenir » qui ne figure pas dans
    `absolus_declares.json` ;
17. l'inventaire ne cite aucun absolu qui aurait disparu du texte ;
18. chacun des treize absolus déclarés porte une raison écrite.

## Le défaut que ce contrôle a fait sortir — il était en production

Le moteur écrivait la ligne « Erreur fréquente » sans vérifier que la question
en portait une :

```js
<div class="bloc-detail"><b>Erreur fréquente :</b> ${Q.err}</div>
```

Sur une question sans `err`, l'élève lisait donc, dans sa correction :

> **Erreur fréquente :** undefined

**140 questions du Thème 3 étaient dans ce cas** : 80 dans les quatre QCM de ce
lot, et 60 dans les deux QCM de C9 **déjà fusionnés** — chacun portait
`err:undefined` trente fois. Aucun test ne pouvait le voir : un `undefined`
affiché ne lève aucune erreur JavaScript, et les suites précédentes ne
validaient qu'une ou deux questions par fichier.

Le contrôle n°12 valide **les trente questions** et relit chaque bloc de
correction produit. C'était le seul moyen.

## Ce que ce rapport ne peut pas dire

- **La justesse pédagogique des 120 questions.** Aucune machine ne dit qu'un
  distracteur est plausible, ni qu'une réfutation enseigne. Soixante-trois
  questions ont été reprises après la relecture d'août ; les cinquante-sept
  autres n'ont reçu aucune remarque, ce qui n'est pas la même chose qu'avoir
  été validées.
- **La justesse des treize absolus déclarés.** Le cliquet garantit qu'aucun
  absolu n'entre sans décision humaine ; il ne garantit pas que les treize
  décisions déjà prises soient les bonnes. Elles sont écrites, une par une,
  dans `absolus_declares.json` — c'est fait pour être contesté.
- Le rendu à l'impression, l'orthotypographie, et le comportement sur les
  navigateurs autres que chromium.
