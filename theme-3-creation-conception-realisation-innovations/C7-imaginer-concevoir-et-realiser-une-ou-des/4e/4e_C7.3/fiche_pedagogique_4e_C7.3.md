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
| 4 | REFAIRE — réinvestissement | 10 min | — |
| 5 | Billet de sortie, seul et sans aide | 5 min | — |

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
| 2 — Comparer sur une durée, puis conclure | Sur combien d'années compare-t-on, et lequel retenir ? | Activités 2 et 3, réinvestissement, billet de sortie, synthèse, Bonus (corrigé), bilan, QCM | 25 + 15 + 10 + 5 min + clôture |

**À trancher par Pascal :** la séance 2 porte 55 min d'activités, plus la clôture.

Dès la séance 2, l'ouverture (étiquettes, « Avant de commencer », situation, problématique et idée de départ, ce que les matériaux imposent à l'atelier, trois façons, billet d'entrée) est repliée dans le volet « 📖 Rappel » ; elle est complète à la séance 1. L'en-tête de la séance 2 rappelle en une ligne la consigne de sécurité de la carte, et renvoie au volet. Restent visibles à chaque séance : le titre, la mission (elle remplace le sous-titre « Thème 3 · 4e — … », comme au pilote), la barre d'outils (🖨 Imprimer / PDF, que la page n'avait pas) et **le banc des matériaux**, qui sert aux deux séances : un seul bloc ; à la séance 1, il reste à sa place, dans l'activité 1 (au-dessus de l'activité 0, sa colonne « Pourquoi ce seuil » en donnerait les réponses) ; dès la séance 2, le script des onglets le place juste après l'en-tête de la séance ouverte. Sans JavaScript, toutes les séances s'affichent à la suite, l'outil à sa place.

La clôture reçoit un corrigé replié du défi (les bascules à 9 et 16 ans, calcul à l'appui ; d'où viennent les durées de vie) ; au bilan, « Comment j'ai travaillé » et « Je me positionne » aux quatre niveaux du livret scolaire, sur `4e_C7.3` et `4e_C3.2` (appui) (le menu existant passe aux quatre niveaux ; une réponse sur l'ancienne échelle se relit au niveau voisin).

## Le billet de sortie et les documents du QCM (27/11/2026, règles d'or n°330 et n°345)

**Billet de sortie**, en fin de séance 2, juste avant le Bonus (environ 5 min, seul et sans aide ; le réinvestissement
passe de 15 à 10 min pour que la séance tienne en 55). Un objet que la séquence n'a pas étudié : **le bac de tri des
déchets du jardin**, en acier galvanisé (20 ans, 120 €) ou en polypropylène recyclé (5 ans, 40 €).
- Question 1 (4e_C7.3) : le coût sur 10 ans, puis sur 20 ans — le classement se retourne. On regarde le nombre de bacs
  calculé pour chaque durée, puis multiplié par le prix.
- Question 2 (4e_C3.2) : ce qu'il faut encore examiner pour l'environnement. On regarde au moins deux étapes du cycle de
  vie nommées, et le nombre de bacs à fabriquer sur la durée.

**QCM** : sept questions sur trente se lisent sur un document dessiné pour le téléphone, calculé par
`documents_qcm.py` depuis `materiaux.py` — « Six matériaux pour le bac du jardin » (les six exigences, puis ce que tient
chaque matériau ; q10, q12, q13) et « Les trois retenus, sur 15 ans » (durée, prix d'un bac, coût sur quinze ans ; q5,
q6, q14, q18). La q12 perd sa notion « Deux motifs pour l'acier », qui soufflait le nombre de motifs. La q13 parlait
de « douze kilomètres » sous un énoncé à deux cents : ses propositions disent deux cents.
