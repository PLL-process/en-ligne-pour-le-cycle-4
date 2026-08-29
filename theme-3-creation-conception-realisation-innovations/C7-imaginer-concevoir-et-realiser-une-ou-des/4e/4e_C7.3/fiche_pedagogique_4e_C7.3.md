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
colonnes sont propres au climat de la Martinique et font le cœur du lot — la **tenue au
rayonnement solaire** et la **tenue au brouillard salin**. Un tableau générique retiendrait des
matériaux que ces deux colonnes éliminent.

Pour rejouer les tables des trois niveaux :

```bash
python3 materiaux.py
```

## Ce que la fiche ne dit pas

Ce qui se passe en classe. Un test vert dit que la page fait ce qu'elle annonce, pas qu'un élève
apprend. La grille LSU de la synthèse professeur est là pour observer, pas pour noter une page.
