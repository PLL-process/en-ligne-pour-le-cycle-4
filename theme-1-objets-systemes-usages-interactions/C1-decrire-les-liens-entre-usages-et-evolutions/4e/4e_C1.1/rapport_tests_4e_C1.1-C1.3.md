# Rapport de tests — lot 4e_C1.1 à C1.3 « Tsinghua »

**Dernière exécution : 24 octobre 2026** (ajout de la séance 5) · Chromium via Playwright ·
`python3 tests_4e_C1.1-C1.3_tsinghua.py` → **63 contrôles, 63 verts** (46 sur la séquence, 17 sur le QCM),
aucune erreur JavaScript · `node tests_regle_311_4e_C1.1.mjs` → **33 / 33**.
Première exécution : 9 août 2026, 42 contrôles sur 42 (détail plus bas, inchangé).

## 24/10/2026 — la séance 5

La séquence passe à **5 séances de 55 min**. La séance 5 accueille trois exercices des ateliers des
représentations (besoin 4e e4, carte mentale 4e e3 et e4), sur un autre objet — le jardin partagé d'un
collège —, puis la clôture (Bonus → Bilan → QCM), qui quitte la séance 4.

| Séance | Avant | Après |
|---|---|---|
| 1 | 50 min | 50 min |
| 2 | 50 min | 50 min |
| 3 | 45 min | 45 min |
| 4 | 55 min (activité 4 + bilan) | 45 min (activité 4) |
| 5 | — | 52 min (activité 5 : 12 + 15 + 15, puis bilan 10) |

**Ajouté au banc (21 contrôles)** : le sixième verrou (activité 5) fermé à vide, avec un message qui
nomme les exercices à réussir, puis ouvert ; chaque exercice inséré refusé à vide puis réussi rempli juste
(réponses lues dans la définition embarquée) ; leur numérotation 1 à 3 ; la clôture en séance 5 et plus en
séance 4 ; le bouton de la séance 4 vers la séance 5 ; la sauvegarde de la page qui laisse les champs des
exercices à leur propre sauvegarde ; leur travail retrouvé après rechargement ; la reprise d'une
sauvegarde d'avant la séance 5 (4 / 5, réponses restaurées, activité 5 fermée) ; la cible du QCM après la
seule activité 5 (`#codes=C1.2,C1.3`) ; à 390 px, les cinq séances ouvertes sans défilement horizontal,
le passage de séance en séance par les boutons, et la reprise après rechargement. Le banc 311 vise
désormais la séance 5 (`panneauSN: 's5'`, ancre `activite-5`).

**Contrôles du dépôt (24/10/2026)** — code de sortie et dernière ligne :

| Contrôle | Code | Dernière ligne |
|---|---|---|
| `node _outils/controle_squelette.mjs` | 0 | ✅ chaque séquence montre son ouverture au premier écran et sa clôture à la dernière séance, dans l'ordre |
| `python3 _outils/controle_navigation_seances.py` | 0 | ✅ chaque séance (hors la dernière de sa page) mène explicitement à la suivante |
| `python3 _outils/controle_hierarchie.py` | 0 | ✅ aucune énumération en ligne, aucun mur sans repère… |
| `python3 _outils/controle_regles_visibles.py` | 0 | ✅ aucune page lue par un élève ne laisse voir la fabrique (règle d'or n°309) |
| `python3 _outils/controle_liens.py` | 0 | ✅ aucun lien mort, aucune ancre introuvable dans le périmètre regardé |
| `python3 _outils/controle_debordement.py` | 0 | ✅ aucun tableau de 3 colonnes ou plus sans filet mobile |
| `python3 _outils/mesurer_temps_seances.py` | 0 | 5 × 55 min · 275 · 242 annoncées · marge +33 min |
| `python3 _outils/verif_regles_audit.py` | 0 | 1 manquement, **antérieur** : n°298 (la carte « référentiel en toutes lettres » et la légende des étiquettes sont encore sur la page élève) |
| `python3 _outils/generer_lexique.py` | 0 | 33 notions → lexique (section « Séance 5 », 13 mots) |

**Non exécuté** : la lecture par un lecteur d'écran réel, l'impression papier, l'essai en classe.

## Périmètre déclaré (règle n°47)

**Vérifié** — les cinq verrous, fermés à vide et ouverts sur une production complète ; les **deux
refus argumentés** ; la progression, la sauvegarde et sa restauration ; la cible du bouton
d'entraînement aux trois moments ; les blocs de la règle n°4, les garde-fous humains et le bloc
CRCN ; le rendu effectif des deux corrigés graphiques ; pour le QCM, le titre affiché, le
sous-titre, les nombres, la répartition, les réfutations, la formulation du référentiel,
l'ouverture ciblée, les images et le lien de retour.

**Non vérifié** — l'exactitude pédagogique des corrigés, le rendu à l'impression, l'ergonomie en
classe, et **la faisabilité de la mesure de température**, qui se vérifie dans une cour.

## 9 août 2026 — séquence : 25 contrôles · QCM : 17 contrôles

| Contrôle notable | Résultat |
|---|---|
| Les cinq verrous refusent une page vide, puis s'ouvrent sur une production complète | ✅ 10/10 |
| **Une exigence nommant un composant est refusée, et le message dit « c'est une solution »** | ✅ |
| **L'oubli du mot « passager » est refusé, et le message cite le nombre de places du train** | ✅ |
| Le bouton d'entraînement : parcours court → `#codes=` ciblés → parcours complet | ✅ 3/3 |
| Les deux corrigés graphiques sont réellement rendus (441 px et 450 px) | ✅ |
| Garde-fous humains et bloc CRCN présents avec leur trace | ✅ |
| QCM : titre affiché, 30 questions, 6 illustrées, 8/7/7/8, graine 404 | ✅ |
| QCM : `#codes=C1.1,C1.2` ouvre 21 questions (12 + 9) | ✅ |
| Zéro erreur JavaScript, sur les deux fichiers | ✅ |

## Vérificateur de règles : 8 sur 8

n°23 (200 min pour 220), n°26, n°29, n°30, n°31 (5 versions étayées pour 11 zones), n°33, n°34,
n°42 (les trois formulations sont celles du référentiel).

## Trois incidents, tous instructifs

**1. Cinq boutons muets, et aucune erreur pour le dire.** Le découpage du script de référence
coupait entre les vérificateurs et la progression — or le bloc qui **attache les écouteurs** se
trouve entre les deux. Les vérificateurs existaient, rien ne les appelait. Aucune erreur JavaScript
n'est levée dans ce cas : la page se charge parfaitement et ne répond simplement à rien. **Une
relecture ne l'aurait pas vu ; le premier test l'a vu immédiatement.**

**2. Trois contrôles rouges à tort.** Les corrigés graphiques sont dans des `<details>` repliés
**et** dans des panneaux de séance inactifs. Un objet non affiché a une hauteur nulle. Il fallait
lever **les deux** obstacles ; n'en lever qu'un laissait le contrôle accuser une page qui rendait
parfaitement (règle n°50).

**3. Dix minutes comptées deux fois.** Le bloc d'annonce de la manipulation affichait « ~10 min »
alors que ce temps est compris dans l'activité 1. Le vérificateur additionnait les deux et concluait
à un dépassement. Ni la page ni le contrôle n'avaient tort : c'était **l'annonce** qui laissait
croire à un temps supplémentaire.
