# 🪵 Le banc de la cour — `5e_C7.3`

> Six matériaux, aucun mauvais. Comment un cahier des charges en élimine-t-il quatre ?

**Thème 3 · 5<sup>e</sup> — Choisir un matériau parmi plusieurs proposés en fonction de leurs caractéristiques.** · appui `5e_C4.4` · 2 séances de 55 min (95 min d'activités)

➡ **[Ouvrir la séquence](sequence_5e_C7.3_banc-de-la-cour.html)** — hors ligne, sans installation ni compte.

## Trois niveaux, trois gestes

Le programme 2024 décline C7.3 en trois gestes distincts, et ce lot tient celui de
son niveau :

| Niveau | Formulation officielle | Le geste |
|---|---|---|
| 5<sup>e</sup> | Choisir un matériau **parmi plusieurs proposés** en fonction de leurs caractéristiques | **écarter** — six candidats, cinq seuils, deux survivants |
| 4<sup>e</sup> | **Comparer** différents matériaux pour choisir le plus adapté | **classer** — trois survivants, et un classement qui se retourne deux fois avec la durée |
| 3<sup>e</sup> | Choisir un matériau **constitutif** d'un objet et/ou système technique | **rouvrir** — aucun survivant, trois sorties, et un porteur à nommer pour chacune |

## L'instrument

`banc_mat.py` engendre un **banc des matériaux**. Il ne note pas, ne pondère pas et ne conseille
pas : **il élimine, et il dit sur quel critère**. Trois choses y sont manipulables, et chacune
correspond à une erreur qu'on fait vraiment :

* **le seuil** — on le déplace, et un matériau passe de recalé à retenu. Un seuil n'est pas une
  propriété du matériau : c'est une décision ;
* **le critère lui-même** — on peut le **retirer** (règle d'or n°213). Le nombre de retenus
  change, et « le meilleur matériau » cesse d'exister ;
* **la durée** — le coût d'achat et le coût sur quinze ans ne classent pas les matériaux dans le
  même ordre, parce qu'ils ne durent pas le même temps.

Toutes les valeurs viennent de `materiaux.py` : masses, coûts, épaisseurs et verdicts sont
**calculés**, jamais recopiés. `python3 materiaux.py` rejoue les trois tables.

## Ce que contient le dossier

| Fichier | Ce que c'est |
|---|---|
| [`sequence_5e_C7.3_banc-de-la-cour.html`](sequence_5e_C7.3_banc-de-la-cour.html) | la séquence élève, hors ligne, avec le banc |
| [`qcm_5e_C7.3_banc-de-la-cour.html`](qcm_5e_C7.3_banc-de-la-cour.html) | 30 questions — 20 sur `5e_C7.3`, 10 sur `5e_C4.4`, 90 réfutations |
| [`lexique_5e_C7.3.html`](lexique_5e_C7.3.html) | 30 notions, engendrées depuis le QCM |
| [`synthese_eleve_5e_C7.3.html`](synthese_eleve_5e_C7.3.html) | à retenir, imprimable en noir et blanc |
| [`synthese_professeur_5e_C7.3.html`](synthese_professeur_5e_C7.3.html) | le pari, les limites, la grille LSU |
| [`fiche_pedagogique_5e_C7.3.md`](fiche_pedagogique_5e_C7.3.md) | déroulé, versions, sécurité, origine des nombres |
| [`matrice_couverture_5e_C7.3.csv`](matrice_couverture_5e_C7.3.csv) | notion → activité → production → question |
| [`rapport_tests_5e_C7.3.md`](rapport_tests_5e_C7.3.md) | la sortie des deux suites, telle quelle |
| `materiaux.py` · `banc_mat.py` · `tests_5e_C7.3_sequence.mjs` · `tests_5e_C7.3_qcm.mjs` · `reponses_5e_C7.3.json` | de quoi tout rejouer |

**Tests réels : 41/41 sur la séquence, 32/32 sur le QCM.**

## Ancrage

Les deux colonnes qui font le cœur du lot — **tenue au rayonnement solaire** et **tenue au
brouillard salin** — ne figurent dans aucun catalogue générique. Elles éliminent pourtant des
matériaux qu'un tableau écrit sous un climat tempéré retiendrait. C'est la contrainte réelle
d'ici, et elle s'écrit au cahier des charges comme les autres.

## Sécurité

Aucune électricité dans cette séquence : le banc est une pièce de structure. La version
🅰 met six chutes de matériau au soleil et un **thermomètre infrarouge** entre les mains des
élèves — on relève une température de surface, on ne pose pas la main dessus pour vérifier.
Les chutes de **pin traité autoclave** ne se poncent pas sans aspiration et ne se brûlent jamais.
