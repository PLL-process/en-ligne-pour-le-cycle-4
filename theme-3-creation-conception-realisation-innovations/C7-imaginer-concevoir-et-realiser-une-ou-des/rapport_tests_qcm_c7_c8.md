# Rapport de tests — les quatre QCM de C7 et C8 portés au standard C9

**Date** : 27 août 2026 · **Suite** : `tests_qcm_c7_c8.mjs` (Playwright, chromium)
**Commande** : `NODE_PATH=<node_modules> node tests_qcm_c7_c8.mjs`

## Résultat

**52 tests, 52 verts, 0 rouge.** Treize contrôles par QCM, sur quatre QCM.

| QCM | Questions | A / B / C / D | Illustrées | Tests |
|---|---:|---|---:|---:|
| `qcm_5e_C7_mini-projet.html` | 30 | 8 / 7 / 7 / 8 | 3 | 13 verts |
| `qcm_4e_C7_jardin-conception.html` | 30 | 8 / 7 / 7 / 8 | 3 | 13 verts |
| `qcm_4e_C8_jardin-validation.html` | 30 | 8 / 7 / 7 / 8 | 3 | 13 verts |
| `qcm_3e_C7_capteur-confort-ny.html` | 30 | 8 / 7 / 7 / 8 | 3 | 13 verts |

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
    de la proposition choisie** — pas celle d'une autre. C'est le test qui garde
    contre le piège des tableaux `o` et `d` désalignés.
11. **Répondre juste est compté juste.**
12. **La progression est restaurée** après rechargement de la page.
13. **Aucun lien relatif mort**, et **aucun débordement horizontal à 390 px**.

## Le piège que la suite a fait remonter

Toutes les pages ouvertes en `file://` partagent la même origine, donc le même
`localStorage`. Sans nettoyage entre deux QCM, le second héritait de la
progression du premier — et le test de restauration passait **pour de mauvaises
raisons**. La suite vide le stockage avant chaque page ; c'est écrit dans son
en-tête pour que personne ne l'enlève par mégarde.

## Ce qui n'est PAS testé, et doit être lu par un humain

- **La justesse pédagogique des 120 questions.** Aucune machine ne peut dire
  qu'un distracteur est plausible, ni qu'une réfutation enseigne. C'est la
  relecture qui reste à faire.
- Le rendu à l'impression.
- L'orthotypographie.
- Le comportement sur les navigateurs autres que chromium.
