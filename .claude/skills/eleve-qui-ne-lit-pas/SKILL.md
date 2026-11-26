---
name: eleve-qui-ne-lit-pas
description: Faire jouer à une page du dépôt en-ligne-pour-le-cycle-4 l'élève qui ne lit pas (toujours la proposition la plus longue, la plus courte, la même place, au hasard) et prouver qu'aucune activité ne se valide ainsi ; puis corriger les questions qui se devinent. À utiliser sur toute page à boutons radio avant livraison, après un générateur, et quand un audit dit « la bonne réponse se repère ». Règle d'or n°360.
---

# L'élève qui ne lit pas

**Règle d'or n°360 — Les tests jouent l'élève qui ne lit pas** (Pascal, 21/11/2026, sur l'audit de l'entraînement DNB
de `3e_C6.2`). Choisir toujours la plus longue, toujours la même place ou au hasard ne valide aucune activité.

Né d'un constat chiffré : dans l'ancienne page, la bonne réponse était strictement la plus longue dans 23 questions sur
30, et le rang suivait le motif 2-1-4-3 sur toute la banque. La stratégie « la plus longue » validait la manche 4
entière. Les règles n°137, 144, 198 et 323 existaient déjà : aucun outil ne rejouait la page.

## 1. Mesurer

```bash
python3 _outils/eleve_qui_ne_lit_pas.py <page.html>       # une page
python3 _outils/eleve_qui_ne_lit_pas.py --tout            # toutes les pages qui ont `const CHECKS`, et les 21 pages du kit
python3 _outils/tests_eleve_qui_ne_lit_pas.py             # le banc de l'outil (pages à réponse connue, dont deux du kit)
```

L'outil coche une proposition dans chaque groupe radio placé dans un `<fieldset>`, avec huit stratégies, puis appelle
chaque `CHECKS[n]()` du gabarit commun. Dans une page du kit des ateliers de représentation (`#donnees-page`, depuis
le 26/11/2026), il appuie sur le bouton « Vérifier » de chaque exercice `[data-exo]` et lit la classe `ok` de son
retour. Sortie 0 : aucune validation ; 1 : au moins une ; 2 : rien lu (n°299).

Dans un banc de page : `from eleve_qui_ne_lit_pas import mesurer`, puis `mesurer(page)` dans un contexte neuf
(exemple : `3e_C6.2/tests_entrainement_dnb.py`).

**Ce qu'il ne voit pas (n°47).** Les listes déroulantes, les champs à écrire, les simulateurs. Une page encore en
`<select>` (avant la conversion n°300) répond « rien lu » : la convertir d'abord. Une activité mixte (radios + texte)
ne peut pas être validée par les radios seuls ; la tester aussi à la main, champs remplis, pour voir si les radios
suffisent à franchir le seuil.

## 2. Lire le résultat

- **« la plus longue » ou « la plus courte » valide** → les propositions n'ont pas la même forme. Le plus souvent, la
  justification est dans la bonne réponse.
- **« toujours la ne » valide** → les places ne sont pas réparties (motif, ou une place dominante).
- **« au hasard » valide** → le seuil est trop bas pour le nombre de questions, ou il y a trop peu de propositions.

## 3. Corriger (dans cet ordre)

1. **Même forme, longueurs voisines** : les quatre propositions sont des phrases du même type ; la justification part
   dans la correction (n°144, n°341, skill `propositions-sans-indice`).
2. **Places réparties dans chaque manche** : chaque place au plus deux fois sur huit, jamais trois fois de suite,
   aucun motif (n°137, n°323). Un ordre fixe, jamais un mélange au hasard : la reprise et les corrections cassent.
3. **Corrections qui citent le texte**, jamais une lettre (n°300).
4. **Seuil écrit à côté du bouton**, appliqué tel quel (n°340, skill `validations-qui-disent-vrai`).

Puis relancer l'outil, et garder un test dans le banc de la page : il doit échouer sur l'ancienne version (n°194).

## 4. Ne pas confondre

- Corriger un biais en l'inversant n'est pas le corriger (n°199) : une bonne réponse devenue toujours la plus courte
  est refusée par la stratégie « la plus courte ».
- Une page où l'outil répond 0 peut encore souffler la réponse par un mot repris de l'énoncé ou par un document annoté
  (n°341, n°348) : l'outil mesure la forme, pas le sens.
