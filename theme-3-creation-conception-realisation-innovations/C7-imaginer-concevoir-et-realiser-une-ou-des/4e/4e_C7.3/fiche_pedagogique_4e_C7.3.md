# Fiche pédagogique — 4e_C7.3 « Le bac du jardin »

| | |
|---|---|
| **Code** | `4e_C7.3` — Comparer différents matériaux pour choisir le plus adapté. |
| **Appui** | `4e_C3.2` — Comparer qualitativement et/ou quantitativement (incidences environnementales, bilan carbone, efficacité énergétique) plusieurs OST répondant au même besoin et arrêter un choix. |
| **Niveau** | 4<sup>e</sup> · Thème 3 |
| **Durée** | 2 séances de 55 min (95 min d'activités) |
| **Socle** | D3 · D4 · D5 |
| **Matériel** | aucun matériel obligatoire — le banc fonctionne dans un navigateur, hors ligne |

## Problématique

> Trois matériaux passent toutes les exigences. Sur quoi les classe-t-on, quand le moins cher à l'achat n'est pas le moins cher ?

## Déroulé

| # | Activité | Durée | Verrou expérientiel |
|---|---|---|---|
| 0 | « Le plus adapté » : adapté à quoi ? | 15 min | — |
| 1 | Trois recalés, trois motifs qui n'ont rien à voir | 25 min | verrou : `evalue` |
| 2 | Le classement se retourne | 25 min | verrou : `duree` |
| 3 | Choisir la durée avant de choisir le matériau | 15 min | — |
| 4 | REFAIRE — réinvestissement | 15 min | — |

## Les trois versions

| Version | Ce qu'elle demande |
|---|---|
| 🅰 avec les devis réels | trois demandes de prix à des fournisseurs locaux et leurs durées de garantie |
| 🅱 avec le banc de la page | un navigateur, hors ligne, rien à installer |
| 🅲 sans écran | une frise de vingt ans au tableau et trois bandes de couleur |

## Sécurité

Le **PVC ne se découpe jamais au laser** : chauffé, il dégage du chlorure d'hydrogène,
qui attaque les voies respiratoires et corrode la machine. Sciage et perçage seulement, sous
aspiration. La **sciure de pin autoclave** ne se respire pas et ne se brûle pas ; les chutes vont
en déchèterie. Côté électricité, la station du jardin est alimentée en **très basse tension**, et
aucun élève ne manipule le **secteur**.

## D'où viennent les nombres

Toutes les valeurs affichées — masses, coûts, épaisseurs, verdicts — sont calculées par
`materiaux.py`, livré dans ce dossier. **Aucun nombre n'est recopié à la main dans une page.**
Ce sont des **ordres de grandeur d'usage pédagogique**, tirés de plages courantes en construction
et en aménagement : c'est le *classement* qui doit être juste, pas la troisième décimale. Deux
colonnes sont propres à un objet installé dehors, près de la mer — ici le bac du jardin, à 900 m
de la mer à Brooklyn — et font le cœur du lot : la **tenue au rayonnement solaire** et la
**tenue au brouillard salin**. Un tableau générique retiendrait des
matériaux que ces deux colonnes éliminent.

Pour rejouer les tables des trois niveaux :

```bash
python3 materiaux.py
```

## Ce que la fiche ne dit pas

Ce qui se passe en classe. Un test vert dit que la page fait ce qu'elle annonce, pas qu'un élève
apprend. La grille LSU de la synthèse professeur est là pour observer, pas pour noter une page.

## Découpage en séances à onglets (04/11/2026, vague de la règle d'or n°311)

La page était d'un seul tenant ; elle a maintenant deux séances à onglets, sur le modèle du pilote 4e_C8.1 et de la vague C8. Les blocs sont déplacés, pas réécrits ; le nombre de séances annoncé (2 × 55 min) ne change pas.

| Séance | Question directrice | Contenu | Temps annoncé |
|---|---|---|---|
| 1 — Adapté à quoi ? Le banc trie | « Le plus adapté », c'est adapté à quoi — et pourquoi trois matériaux sur six tombent-ils ? | Ouverture, activités 0 et 1 | ouverture + 15 + 25 min |
| 2 — Comparer sur une durée, puis conclure | Sur combien d'années compare-t-on, et lequel retenir ? | Activités 2 et 3, réinvestissement, synthèse, Bonus (corrigé), bilan, QCM | 25 + 15 + 15 min + clôture |

**À trancher par Pascal :** la séance 2 porte 55 min d'activités, plus la clôture.

Dès la séance 2, l'ouverture (étiquettes, « Avant de commencer », situation, problématique et idée de départ, ce que les matériaux imposent à l'atelier, trois façons, billet d'entrée) est repliée dans le volet « 📖 Rappel » ; elle est complète à la séance 1. L'en-tête de la séance 2 rappelle en une ligne la consigne de sécurité de la carte, et renvoie au volet. Restent visibles à chaque séance : le titre, la mission (elle remplace le sous-titre « Thème 3 · 4e — … », comme au pilote), la barre d'outils (🖨 Imprimer / PDF, que la page n'avait pas) et **le banc des matériaux**, qui sert aux deux séances : un seul bloc ; à la séance 1, il reste à sa place, dans l'activité 1 (au-dessus de l'activité 0, sa colonne « Pourquoi ce seuil » en donnerait les réponses) ; dès la séance 2, le script des onglets le place juste après l'en-tête de la séance ouverte. Sans JavaScript, toutes les séances s'affichent à la suite, l'outil à sa place.

La clôture reçoit un corrigé replié du défi (les bascules à 9 et 16 ans, calcul à l'appui ; d'où viennent les durées de vie) ; au bilan, « Comment j'ai travaillé » et « Je me positionne » aux quatre niveaux du livret scolaire, sur `4e_C7.3` et `4e_C3.2` (appui) (le menu existant passe aux quatre niveaux ; une réponse sur l'ancienne échelle se relit au niveau voisin).
