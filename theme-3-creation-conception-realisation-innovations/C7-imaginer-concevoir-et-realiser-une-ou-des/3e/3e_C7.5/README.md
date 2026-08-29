# 🌀 La station qu'il faut équiper — `3e_C7.5`

> Le catalogue contient plus de constituants qu'il n'en faut. Comment un cahier des charges décide-t-il, à lui seul, lesquels on garde ?

**Thème 3 · 3<sup>e</sup> — Choisir les constituants et assembler un prototype.** · appui `3e_C4.3` · 2 séances de 90 min (150 min d'activités)

## Ce que ce lot travaille, et ce qu'il ne refait pas

Le programme 2024 décline C7.5 en trois gestes distincts : **assembler** des constituants
fournis en 5e, **compléter** un prototype incomplet en 4e, **choisir** puis assembler en 3e.
Ce lot tient le geste de son niveau et s'appuie sur les autres codes sans les refaire —
la chaîne d'information est travaillée par `3e_C4.3`, et elle est ici <b>mobilisée</b>, pas
réenseignée.

## L'instrument

`etabli.py` engendre un **établi Grove** : on place chaque constituant sur un port, on teste, et
la page ne répond jamais « ça ne marche pas ». Elle répond *pourquoi* — le port n'est pas du bon
type, une fonction n'est tenue par personne, un constituant en exige un autre, le budget de
courant est dépassé, ou le programme lit ailleurs que là où c'est branché. Le diagnostic est
ordonné du plus grossier au plus fin, comme celui d'un dépanneur.

On peut aussi **retirer** un constituant d'un montage qui marchait (règle d'or n°213) : c'est ce
geste, et pas un tableau, qui montre à quoi servait la fonction manquante.

## Ce que contient le dossier

| Fichier | Ce que c'est |
|---|---|
| [`sequence_3e_C7.5_station-a-equiper.html`](sequence_3e_C7.5_station-a-equiper.html) | la séquence élève, hors ligne, avec l'établi |
| [`qcm_3e_C7.5_station-a-equiper.html`](qcm_3e_C7.5_station-a-equiper.html) | 30 questions — 20 sur `3e_C7.5`, 10 sur `3e_C4.3`, 90 réfutations |
| [`lexique_3e_C7.5.html`](lexique_3e_C7.5.html) | 30 notions, engendrées depuis le QCM |
| [`synthese_eleve_3e_C7.5.html`](synthese_eleve_3e_C7.5.html) | à retenir, imprimable en noir et blanc |
| [`synthese_professeur_3e_C7.5.html`](synthese_professeur_3e_C7.5.html) | le pari, les limites, la grille LSU |
| [`fiche_pedagogique_3e_C7.5.md`](fiche_pedagogique_3e_C7.5.md) | déroulé, sécurité, relevé de la skill Grove |
| [`matrice_couverture_3e_C7.5.csv`](matrice_couverture_3e_C7.5.csv) | notion → activité → production → question |
| [`rapport_tests_3e_C7.5.md`](rapport_tests_3e_C7.5.md) | la sortie des deux suites, telle quelle |
| `tests_3e_C7.5_sequence.mjs` · `tests_3e_C7.5_qcm.mjs` · `reponses_3e_C7.5.json` · `etabli.py` | de quoi tout rejouer |

**Tests réels : 42/42 sur la séquence, 32/32 sur le QCM.**

## Sécurité

Très basse tension **uniquement**, 5 V partout, et aucun élève ne manipule le secteur.
On câble hors tension, l'alimentation en dernier.
