# Rapport de tests — lot 4e_C1.1 à C1.3 « Tsinghua »

**Exécuté le 9 août 2026** · Chromium via Playwright · `python3 tests_4e_C1.1-C1.3_tsinghua.py`
**Résultat : 42 contrôles, 42 verts, aucune erreur JavaScript.**

## Périmètre déclaré (règle n°47)

**Vérifié** — les cinq verrous, fermés à vide et ouverts sur une production complète ; les **deux
refus argumentés** ; la progression, la sauvegarde et sa restauration ; la cible du bouton
d'entraînement aux trois moments ; les blocs de la règle n°4, les garde-fous humains et le bloc
CRCN ; le rendu effectif des deux corrigés graphiques ; pour le QCM, le titre affiché, le
sous-titre, les nombres, la répartition, les réfutations, la formulation du référentiel,
l'ouverture ciblée, les images et le lien de retour.

**Non vérifié** — l'exactitude pédagogique des corrigés, le rendu à l'impression, l'ergonomie en
classe, et **la faisabilité de la mesure de température**, qui se vérifie dans une cour.

## Séquence — 25 contrôles · QCM — 17 contrôles

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

n°23 (205 min pour 220), n°26, n°29, n°30, n°31 (5 versions étayées pour 11 zones), n°33, n°34,
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
