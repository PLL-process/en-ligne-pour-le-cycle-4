# Rapport de tests — 3e_C8.2 « Le mât de la station »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot
tels qu'ils sont livrés. Les deux scripts sont dans ce dossier : on peut les rejouer.

```bash
node tests_3e_C8.2_sequence.mjs "$PWD/sequence_3e_C8.2_mat-de-la-station.html"
node tests_3e_C8.2_qcm.mjs      "$PWD/qcm_3e_C8.2_mat-de-la-station.html"
python3 profils_3e_C8.2.py      # recalcule toutes les valeurs du banc
```

---

## 1. Séquence — **32 / 32**

### Chargement
| # | Test | Résultat |
|---|---|---|
| 1 | charge sans erreur JS | ✅ |
| 2 | aucune requête réseau échouée (page 100 % hors ligne) | ✅ |
| 3 | aucune boîte modale | ✅ |

### Le banc de flexion
| # | Test | Mesuré |
|---|---|---|
| 4 | à 100 N, la flèche du tube alu vaut 31,0 mm | `31,0` |
| 5 | le banc signale la charge d'essai atteinte | ✅ |
| 6 | le tube alu casse au pied | `CASSÉ AU PIED` |
| 7 | la rupture annonce 467 N | ✅ |
| 26 | le tracé du mât se courbe sous la charge | le `d` du path change |
| 27 | le tracé se rompt au pied (deux tronçons) | `M80,230 L80,208 M91,213 L198,229` |
| 28 | le point de rupture est marqué | rayon > 0 |

### Le banc de traction
| # | Test | Mesuré |
|---|---|---|
| 12 | les pas passent en kN au changement de mode | `+ 25 kN` |
| 13 | verrou des 5 profilés rompus en traction ouvert | ✅ |

### Verrous expérientiels
| # | Test | Résultat |
|---|---|---|
| 8 | l'activité 0 refuse de se valider tant que 3 profilés ne sont pas cassés | 🔒 |
| 9 | `__exp.flex3` s'ouvre à 3 ruptures en flexion | ✅ |
| 10 | `__exp.flex5` s'ouvre à 5 ruptures en flexion | ✅ |
| 13 | `__exp.trac5` s'ouvre à 5 ruptures en traction | ✅ |

### Vérificateurs — et ce qu'ils refusent
| # | Test | Mesuré |
|---|---|---|
| 11 | activité 0 validée | `2/2` |
| 14 | activité 1 validée avec les 5 relevés de traction justes | `9/9` |
| 15 | **un relevé approximatif est refusé** (84 au lieu de 84,2) | `8/9` |
| 16 | activité 2 validée | `7/7` |
| 17 | **un seuil faux est refusé** (500 au lieu de 300) | `6/7` |
| 18 | activité 3 validée avec les 10 relevés justes | `10/10` |
| 19 | **une flèche arrondie est refusée** (41 au lieu de 41,1) | `9/10` |
| 29 | activité 4 validée — 5 angles morts associés | `5/5` |
| 24 | activité 5 validée | `4/4` |
| 25 | réinvestissement validé | `1/1` |

Les trois tests en gras sont ceux qui comptent : ils prouvent qu'un chiffre **recopié à peu
près** est rejeté. C'est le cœur du code — on évalue la mise en œuvre, pas la capacité à
retrouver un ordre de grandeur.

### Structure de la page
| # | Test | Mesuré |
|---|---|---|
| 20 | les cinq listes de l'activité 4 offrent les mêmes 5 angles morts | 5 listes × 6 options |
| 21 | bandeau de durée présent | `⏱ 2 séances de 90 min (1 h 30)` |
| 22 | **un seul** bouton de QCM | `1` |
| 23 | hypothèse d'entrée présente | `#hyp` |
| 30 | grille de relecture du binôme : 7 critères | `7` |

### Persistance
| # | Test | Mesuré |
|---|---|---|
| 31 | les relevés survivent au rechargement | `467` |
| 32 | les verrous survivent au rechargement | `flex5` toujours ouvert |

---

## 2. QCM — **26 / 26**

### La banque
| # | Test | Mesuré |
|---|---|---|
| 3 | 30 questions | `30` |
| 4 | 4 options par question | ✅ |
| 5 | 3 réfutations par question | ✅ |
| 6 | la bonne réponse n'a pas de réfutation (`d[r] === ""`) | ✅ |
| 7 | tous les champs du gabarit remplis (`q`, `expl`, `ex`, `err`, `ret`) | ✅ |
| 8 | aucune image héritée du lot voisin | ✅ |
| 9 | 30 notions distinctes | `30` |

### Échantillonnage des compétences
| # | Test | Mesuré |
|---|---|---|
| 10 | 20 questions sur 3e_C8.2 | `20` |
| 11 | 10 questions sur 3e_C3.4 | `10` |
| 12 | les deux codes dépassent le seuil de 5 questions évaluables | ✅ |
| 13 | bonnes réponses réparties sur les 4 positions | `8/7/7/8` |

### Le biais de longueur
| # | Test | Mesuré |
|---|---|---|
| 14 | aucune bonne réponse détachée de plus de 8 caractères | `0` sur 30 |
| 15 | écart moyen de longueur de la bonne réponse | **+1,7 caractère** |

Surveillé **dès l'écriture**, comme pour le lot 5e : une seule question a dû être resserrée
avant la première génération (« ce que reconnaît le coefficient de sécurité », 49 → 46
caractères), et le contrôle du script a refusé de livrer tant qu'elle ne l'était pas.

### Le parcours réel
| # | Test | Mesuré |
|---|---|---|
| 16 | une bonne réponse est déclarée correcte | `✔ Correct` |
| 17 | la correction déplie les trois réfutations | `3` |
| 18 | la correction porte un « À retenir » | ✅ |
| 19 | une mauvaise réponse est déclarée incorrecte | `✘ Incorrect` |
| 22 | 30 bonnes réponses donnent 100 % | `100 %` |
| 23 | la note affichée est 20/20 | `20,0 /20` |
| 24 | le lien vers la séquence pointe le bon fichier | ✅ |
| 25 | la progression survit au rechargement | `30` répondues |

### Règle d'or n°188 — une page d'élève ne s'arrête pas pour parler
| # | Test | Mesuré |
|---|---|---|
| 20 | le mode « marquées » vide n'ouvre **aucune** boîte modale | `0` |
| 21 | il affiche un bandeau `aria-live` à la place | texte lu dans `#savedNote` |
| 26 | aucune boîte modale sur tout le parcours | `0` |

Le gabarit hérité du lot 4e_C8.1 ouvrait **trois** `alert()`. Le script de génération les
compte, refuse de continuer s'il n'en trouve pas exactement trois, et les remplace par le
bandeau `#savedNote`, qui portait déjà `role="status"` et `aria-live="polite"`.

> **Mesure à porter au journal.** Comptage fait hors `_archive-anciennes-versions/`, sur les
> seuls appels situés dans un `<script>` : **46 QCM sur 51** en ouvrent au moins une (224 appels
> au total) et **35 séquences sur 46** (38 appels). Ce lot en corrige trois, dans le seul fichier
> qu'il produit. Le reste demande une passe dédiée, mesurée, et hors du périmètre d'un lot du
> thème 3.
>
> *Premier comptage, faux : « 49 QCM sur 68 ». Le glob ramassait les copies archivées, et le
> motif attrapait aussi les `.alert(` d'un commentaire. Corrigé avant publication — mais c'est
> la même famille d'erreur que les règles n°184 et n°194 : je comptais le fichier, pas l'appel.*

---

## 3. Les valeurs du banc — recalculées, pas recopiées

`profils_3e_C8.2.py` rejoué au moment d'écrire ce rapport :

```
profilé                             flexion   flèche   traction     masse  verdict
Tube aluminium Ø50 × 3                467 N   31.0 mm    84.2 kN   2.39 kg  RETENU
Barre pleine acier Ø20                157 N  161.7 mm   125.7 kN   4.93 kg  rupture
Tube PVC Ø50 × 3                      128 N  723.8 mm    23.0 kN   1.24 kg  rupture
Poutre bois 40 × 40                   213 N  113.6 mm    64.0 kN   1.60 kg  rupture
Tube acier galvanisé Ø33,7 × 2,6      367 N   41.1 mm   101.6 kN   3.99 kg  flèche

exigé : rupture ≥ 300 N · flèche ≤ 40 mm sous 100 N
rang traction : Barre pleine acier > Tube acier galvanisé > Tube aluminium > Poutre bois > Tube PVC
rang flexion  : Tube aluminium > Tube acier galvanisé > Poutre bois > Barre pleine acier > Tube PVC
```

**L'inversion sur laquelle repose la séquence est donc vérifiée par le calcul et par le banc :**
la barre pleine acier est 1<sup>re</sup> en traction et 4<sup>e</sup> en flexion.

---

## 4. Ce que ces tests ne prouvent pas

* Ils ne prouvent **rien sur la matière** : le banc est une simulation, et son modèle
  (poutre encastrée, domaine élastique) est cité dans la page comme dans cette page-ci.
* Ils ne prouvent rien sur la **qualité du protocole rédigé** par l'élève : le vérificateur
  compte des lignes et une longueur. La page le dit à l'élève, et c'est pourquoi la grille
  de relecture croisée en binôme existe.
* Ils ne prouvent rien sur ce qui se passe **en classe**. Un test vert dit que la page fait
  ce qu'elle annonce, pas qu'un élève apprend.
