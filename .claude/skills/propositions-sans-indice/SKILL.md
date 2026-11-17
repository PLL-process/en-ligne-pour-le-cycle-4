---
name: propositions-sans-indice
description: Relire et réécrire les questions à choix d'une séquence ET d'un QCM pour qu'aucune ne souffle sa réponse — intrus crédibles pour un élève qui n'a pas encore appris, bonne réponse qui ne porte pas sa justification, aucune question qui affiche le résultat de la précédente, échelle d'auto-positionnement rangée et décrite. Dans un QCM, chaque mauvaise proposition garde un pourquoi qui sert d'indice (jamais « ! », vide ou creux). À utiliser à chaque révision ou audit de séquence ou de QCM, avant de poser les aides d'un QCM (lot 3), et en écrivant toute question neuve.
---

# Une question ne souffle pas sa réponse

Né le 17/11/2026 de l'audit externe de `3e_C4.1`. Activité 5 : « le poteau en bord de mer : en quel matériau ? »
proposait « carton compressé » ; « le capot à produire en 200 exemplaires : par quel procédé ? » proposait
« sculpture à la main », face à « moulage par injection (la série rentabilise le moule) » — la seule proposition qui
s'expliquait. Activité 2 : la question de la capacité affichait « 432 Wh ÷ 12 V = … Ah » sous la question qui
demandait les 432 Wh. Le bilan rangeait l'auto-positionnement « fragile, en cours, expert, solide », sans dire ce que
veut dire chaque niveau. L'élève qui reconnaît réussit sans raisonner ; la page croit qu'il a compris.

Règles voisines, déjà mesurées : n°144 (la bonne réponse n'est pas la plus longue, `controle_longueurs.py`), la place
de la bonne réponse (`controle_ordre_propositions.py`), les mots des QCM (`controle_indices_qcm.mjs`), n°300 (des
boutons radio lisibles), n°338 (les mêmes nombres partout).

## 1. Mesurer

```bash
python3 _outils/controle_propositions_indices.py --detail <dossier du lot>
```

| Code | Ce qu'il voit | Gravité |
|---|---|---|
| I1 | la bonne réponse est seule à porter une justification (parenthèse de quatre mots ou plus, « — » suivi d'une explication, « car », « parce que », « donc ») | ⚠ |
| I3 | le résultat attendu d'un calcul (`num("d2_1")===432`) se lit dans une étiquette ou une légende, hors aides et corrections | ⚠ |
| I4 | une échelle d'auto-positionnement dans le désordre | ✘ — sortie 1 |
| I4 | des niveaux qui ne disent pas ce qu'ils veulent dire | ⚠ |

Mesuré le 17/11/2026 sur le site : I1 53, I3 25, I4 15, dans 21 pages.

## 2. Relire à voix haute, comme un élève qui n'a pas encore appris

Pour chaque groupe de propositions, lire la question puis chaque proposition, et se demander : **un élève qui n'a pas
fait l'activité hésiterait-il ?**

1. **Les intrus (I2, à l'œil).** Un intrus est une erreur que commet un élève, pas une plaisanterie. On le prend
   dans les pièges de la séquence (`erreurs`, « Pièges classiques »), dans les confusions du QCM du lot
   (`qcm_aides_<lot>.json`), ou dans une solution réelle mais mal placée : « bois non traité » pour un poteau en bord
   de mer, « usinage dans un bloc, pièce par pièce » pour 200 capots, « impression 3D une par une ». Chaque intrus garde
   son `data-pourquoi` (n°336) : s'il est impossible d'écrire pourquoi un élève le choisirait, il ne vaut rien.
2. **La justification (I1).** Soit aucune proposition ne porte de justification (« moulage par injection »), et le
   pourquoi vit dans la correction ; soit **toutes** en portent une, et le choix porte sur l'argument
   (« 20 Ah — moins chère, ça devrait passer » / « 40 Ah — la capacité minimale + une marge de sécurité »). Une
   énumération que seule la bonne réponse détaille (« des métaux protégés (galvanisé, inox ou aluminium) ») souffle
   aussi : la raccourcir, ou détailler les intrus.
3. **Le calcul soufflé (I3).** Une question ne montre pas le résultat d'une autre : « ton énergie, en Wh ÷ 12 V = … »,
   « U = R × I = 0,4 Ω × (ton courant du a) = … V ». Un nombre qui reste dans une proposition de la question suivante
   (« 36 Ah — pas un Ah de plus ») se juge : il ne dit plus « exactement le calcul ».
4. **L'échelle (I4).** Les niveaux dans l'ordre (classe `positionnement`, que `controle_ordre_propositions.py` ne
   mélange jamais), et chacun dit ce qu'il veut dire **pour la compétence** :
   « 🔴 fragile — je n'arrive pas encore à placer les fonctions, même avec l'aide » … « ⭐ expert — je construis la
   chaîne d'un autre objet et j'explique mes choix ». La `value` ne change pas (« 🔴 fragile ») : les sauvegardes des
   élèves se relisent.

## 3. Changer une proposition sans rien casser

La valeur d'un bouton radio est le texte de sa proposition (n°300). Changer un texte, c'est changer partout :

- `value` et `<label>` de l'option, son `data-pourquoi` ;
- la réponse attendue (`const att = {…}` ou `$("id").value === "…"` dans `CHECKS`) ;
- `mission_<lot>.json` (clés des « pourquoi ») ;
- le banc du lot s'il coche par le texte ; puis `grep -rn "<ancien texte>"` sur le dépôt : zéro.

Vérifier : banc du lot, `tests_regle_311_<lot>.mjs`, `banc_generique.mjs` (mode mission : « pourquoi des erreurs »
complet), `controle_ordre_propositions.py`, `controle_unites.py` (une unité nommée en toutes lettres, n°312).

## 4. Dans un QCM (`const QUESTIONS`) : l'intrus et son pourquoi

Né des vagues 1 à 3 du lot 3 (17/11/2026, #772, #773). Dans un QCM du gabarit maison, chaque proposition a son
pourquoi (`d`, au même rang que dans `o`), et l'indice 💡 de la n°339 l'affiche à l'élève qui l'a choisie. Un `d`
réduit à « ! » trahissait un **intrus-plaisanterie**, que personne ne choisit et que l'auteur savait tel : « parce que
le nombre 118 est plus joli », « pour user le clavier de l'ordinateur », « pour économiser l'encre de l'imprimante »,
« un jeu vidéo éducatif sur les cyclones », « parce que 6 est un chiffre porte-bonheur », « elle joue un son ». Quatorze
dans `3e_C5.1`, `3e_C6.1`, `4e_C6.2` ; d'autres dans `3e_C4.1`. Une question à quatre propositions dont deux font rire
est une question à deux propositions.

```bash
node _outils/qcm_aides/indices_creux.mjs [--detail] [dossier]     # « ! », indices vides, indices creux, par QCM
node _outils/qcm_aides/indices_creux.mjs <qcm> --liste             # les questions numérotées, et ce qui est à revoir
```

| Ce que l'outil voit | Ce qu'on fait |
|---|---|
| `d` = « ! » | l'intrus est une plaisanterie : **réécrire la proposition** (étape 2, I2), puis son pourquoi |
| `d` vide pour une mauvaise proposition | écrire son pourquoi : l'élève qui la choisit n'aurait aucun indice |
| `d` creux : moins de 25 caractères, ou « Rien à voir. », « Faux. », « Python va très bien. » sans explication à la suite | le réécrire : **pourquoi CETTE proposition ne répond pas à CETTE question** |

Un bon pourquoi nomme ce qui manque à la proposition, sans donner la bonne réponse : « Un multimètre mesure une tension
ou une intensité : il ne dit pas combien de temps dure la réparation » (et non « Il mesure une tension. ») ; « Python
lit les tests de haut en bas : le premier test vrai l'emporte, les suivants sont ignorés ». Un intrus réécrit se prend
dans les erreurs réelles de la notion (le `err` de la question, les pièges de la séquence) : « parce que Python lit
les tests de bas en haut », « parce que les anciens tests ont pu changer », « pour que l'axe soit serré et ne tourne
pas », « il est léger, donc peu polluant à fabriquer ».

Le remplacement se fait question par question, jamais par un remplacement global (« ! » ou « Rien à voir. » reviennent
d'une question à l'autre) :

```bash
python3 _outils/qcm_aides/corriger_question.py <qcm> remplacements.json
#   [["morceau unique de l'énoncé", "ancienne chaîne", "nouvelle chaîne"], …] — o et d au même rang ; r ne bouge pas
node _outils/verif_qcm_coherence.mjs <qcm>        # positions et réfutations alignées
python3 _outils/controle_longueurs.py             # la bonne réponse ne devient pas la plus longue
```

Si le lot a un générateur (`_generation/q.py`, `build_qcm.py`), la même correction s'y écrit, sinon la prochaine
régénération la défait ; un générateur qui n'est plus à jour de sa page se signale à Pascal, il ne se relance pas.

État du 17/11/2026 au soir, après la vague 4 du lot 3 : 72 QCM, **0 « ! », 0 indice vide, 0 indice creux**. Un QCM neuf
ou modifié se mesure avant sa PR (`indices_creux.mjs --strict <qcm>`).

## 5. Généraliser et dire

Mesurer tout le site (`controle_propositions_indices.py` sans chemin) et écrire le compte dans le journal (n°293).
Un ✘ I4 se corrige dans la PR ; les ⚠ se reprennent à la révision de chaque séquence. Les intrus se réécrivent avec
Pascal quand ils touchent au fond (un matériau, un procédé, une valeur de série) : c'est son terrain.
