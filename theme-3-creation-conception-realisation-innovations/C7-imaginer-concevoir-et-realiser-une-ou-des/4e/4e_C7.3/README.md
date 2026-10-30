# 🪴 Le bac du jardin — `4e_C7.3`

> Trois matériaux passent toutes les exigences. Sur quoi les classe-t-on, quand le moins cher à l'achat n'est pas le moins cher ?

**Thème 3 · 4<sup>e</sup> — Comparer différents matériaux pour choisir le plus adapté.** · appui `4e_C3.2` · 2 séances de 55 min (95 min d'activités)

➡ **[Ouvrir la séquence](sequence_4e_C7.3_bac-du-jardin.html)** — hors ligne, sans installation ni compte.

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
| [`sequence_4e_C7.3_bac-du-jardin.html`](sequence_4e_C7.3_bac-du-jardin.html) | la séquence élève, hors ligne, avec le banc |
| [`qcm_4e_C7.3_bac-du-jardin.html`](qcm_4e_C7.3_bac-du-jardin.html) | 30 questions — 20 sur `4e_C7.3`, 10 sur `4e_C3.2`, 90 réfutations |
| [`lexique_4e_C7.3.html`](lexique_4e_C7.3.html) | 30 notions, engendrées depuis le QCM |
| [`synthese_eleve_4e_C7.3.html`](synthese_eleve_4e_C7.3.html) | à retenir, imprimable en noir et blanc |
| [`synthese_professeur_4e_C7.3.html`](synthese_professeur_4e_C7.3.html) | le pari, les limites, la grille LSU |
| [`fiche_pedagogique_4e_C7.3.md`](fiche_pedagogique_4e_C7.3.md) | déroulé, versions, sécurité, origine des nombres |
| [`matrice_couverture_4e_C7.3.csv`](matrice_couverture_4e_C7.3.csv) | notion → activité → production → question |
| [`rapport_tests_4e_C7.3.md`](rapport_tests_4e_C7.3.md) | la sortie des deux suites, telle quelle |
| `materiaux.py` · `banc_mat.py` · `tests_4e_C7.3_sequence.mjs` · `tests_4e_C7.3_qcm.mjs` · `reponses_4e_C7.3.json` | de quoi tout rejouer |

**Tests réels : 44/44 sur la séquence, 32/32 sur le QCM.**

## Ancrage

Les deux colonnes qui font le cœur du lot — **tenue au rayonnement solaire** et **tenue au
brouillard salin** — ne figurent dans aucun catalogue générique. Elles éliminent pourtant des
matériaux qu'un tableau écrit pour un objet d'intérieur retiendrait. Un bac dehors toute l'année,
à 900 m de la mer à Brooklyn : c'est la contrainte réelle du jardin, et elle s'écrit au cahier
des charges comme les autres.

## Sécurité

Le **PVC ne se découpe jamais au laser** : chauffé, il dégage du chlorure d'hydrogène,
qui attaque les voies respiratoires et corrode la machine. Sciage et perçage seulement, sous
aspiration. La **sciure de pin autoclave** ne se respire pas et ne se brûle pas ; les chutes vont
en déchèterie. Côté électricité, la station du jardin est alimentée en **très basse tension**, et
aucun élève ne manipule le **secteur**.
