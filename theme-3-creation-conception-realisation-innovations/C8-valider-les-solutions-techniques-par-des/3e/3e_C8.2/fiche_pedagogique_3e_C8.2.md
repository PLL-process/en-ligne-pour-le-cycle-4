# Fiche pédagogique — 3e_C8.2 « Le mât de la station »

> **Proposer un protocole de test pour valider la tenue mécanique d'un matériau.**
> Programme 2024, cycle 4, thème 3 — Création, conception, réalisation : des objets
> et des systèmes techniques à créer.

| | |
|---|---|
| **Niveau** | 3<sup>e</sup> |
| **Code principal** | 3e_C8.2 — 20 questions de QCM |
| **Code d'appui** | 3e_C3.4 — *définir et mettre en œuvre un protocole pour mesurer une caractéristique, une performance d'un OST* — 10 questions |
| **Socle** | D1.3 · D2 · D3 · D4 |
| **Durée** | 2 séances de 90 min (1 h 30) — 160 min d'activités obligatoires, marge +20 min |
| **Matériel** | un navigateur, hors ligne. Aucune installation, aucun compte. |
| **Contexte de projet** | la station d'alerte cyclonique de `3e_C9.2`, une fois sa recette signée, doit être installée dehors |

---

## 1. La place du lot dans la spirale C8

| Niveau | Ce qu'on demande | Qui écrit le protocole |
|---|---|---|
| 5<sup>e</sup> — `5e_C8.2` | éprouver cinq matériaux en traction pour choisir une patère | le laboratoire ; l'élève applique |
| 3<sup>e</sup> — `3e_C8.3` | écrire la recette de la station avant livraison | l'élève — sur un **comportement** |
| **3<sup>e</sup> — `3e_C8.2`** | **décider de quoi sera fait le mât** | **l'élève — sur une matière** |

La séquence de 5<sup>e</sup> laissait délibérément la porte ouverte : son activité REFAIRE
finit sur « *une étagère plie, elle ne s'étire pas — reconnaître qu'un protocole ne convient
pas à une question, c'est déjà de la 3<sup>e</sup>* ». Ce lot reprend le fil exactement là.

## 2. Le pari didactique

Faire écrire un protocole plausible n'évalue rien : tous se ressemblent, aucun n'est mis à
l'épreuve. Ici l'erreur est rendue **mesurable**.

Les cinq candidats-mâts **ne se classent pas dans le même ordre** selon la sollicitation :

* en **traction**, la barre pleine acier gagne largement (125,7 kN) ;
* en **flexion**, cette même barre est **quatrième sur cinq** (157 N).

L'élève applique d'abord le protocole de 5<sup>e</sup> — juste, connu, correctement appliqué —
et constate **lui-même**, banc en main, qu'il désigne un mât que la flexion élimine. La
nécessité d'en proposer un autre n'est pas affirmée par la page : elle est établie par une
mesure que l'élève a faite.

Le coup de grâce est une comparaison de masses : **2,39 kg** d'aluminium en tube tiennent
**467 N** ; **4,93 kg** d'acier plein n'en tiennent que **157**. Deux fois plus lourd, trois
fois moins résistant — parce que sa matière est au centre, là où elle ne travaille pas.

## 3. Déroulé

| # | Activité | Durée | Production attendue | Verrou |
|---|---|---|---|---|
| 0 | **FAIRE** — casser trois mâts au banc | ~15 min | 2 réponses | `flex3` |
| 1 | **Le protocole de 5<sup>e</sup> ne répond pas** | ~25 min | 5 relevés de traction + 3 réponses + 1 phrase | `trac5` |
| 2 | **PROPOSER ton protocole** | ~35 min | 6 décisions + 6 lignes rédigées | — |
| 3 | **Exécuter TON protocole** | ~30 min | 10 relevés (flèche + rupture) | `flex5` |
| 4 | **Ce que ton protocole ne voit pas** | ~20 min | 5 associations | — |
| 5 | **Décider, et signer l'avis** | ~20 min | 3 réponses + avis rédigé | — |
| — | **REFAIRE** — le panneau solaire | ~15 min | 4 lignes | — |

**Découpage en deux séances suggéré :** séance 1 = activités 0 à 2 (75 min + 15 min de
mise en route et de bilan intermédiaire) ; séance 2 = activités 3 à 5 et REFAIRE (85 min).

## 4. Les valeurs du banc

Mât encastré, **L = 2 000 mm**, effort en tête.

| Candidat | Traction | Flexion | Flèche/100 N | Masse | Verdict |
|---|---|---|---|---|---|
| Tube aluminium Ø50 × 3 | 84,2 kN | **467 N** | **31,0 mm** | 2,39 kg | ✅ retenu |
| Tube acier galvanisé Ø33,7 × 2,6 | 101,6 kN | 367 N | 41,1 mm | 3,99 kg | ❌ flèche |
| Poutre bois 40 × 40 | 64,0 kN | 213 N | 113,6 mm | 1,60 kg | ❌ rupture |
| Barre pleine acier Ø20 | **125,7 kN** | 157 N | 161,7 mm | 4,93 kg | ❌ rupture |
| Tube PVC Ø50 × 3 | 23,0 kN | 128 N | 723,8 mm | 1,24 kg | ❌ rupture |

Formules employées : `F = σ·I/(v·L)` (rupture en flexion), `f = F·L³/(3·E·I)` (flèche),
`F = σ·A` (rupture en traction). Les résistances σ sont **exactement celles du banc de
5<sup>e</sup>** : bois 40 MPa, PVC 52, aluminium 190, acier 400. Tout est recalculé par
`profils.py`, dont la sortie a produit le tableau ci-dessus — aucune valeur n'a été saisie
à la main dans la page.

**Cahier des charges :** poussée équivalente **100 N** pour 180 km/h (ordre de grandeur
vérifiable : ½ρv² ≈ 1 530 Pa à 50 m/s, C<sub>x</sub> 1,2, ≈ 0,054 m² au vent) · coefficient
de sécurité **3** → rupture exigée **300 N** · flèche admise **40 mm**, soit 2 % de la hauteur,
au-delà desquels l'inclinaison de la station fausse la mesure de direction du vent.

## 5. Les trois moments qui portent la séance

1. **Activité 1 — l'inversion des classements.** Ne pas l'annoncer. Laisser relever les cinq
   valeurs en traction, laisser désigner la barre pleine acier, puis basculer le banc en
   flexion. La surprise est le levier pédagogique.
2. **Activité 2 — l'écriture.** Le vérificateur juge les six décisions et compte les lignes ;
   **il ne juge pas le texte**, et la page l'écrit à l'élève. C'est la relecture croisée en
   binôme, avec sa grille de 7 critères, qui porte l'évaluation du protocole rédigé.
3. **Activité 5 — les 1,1 mm.** La question la plus difficile : refuser un candidat pour
   1,1 mm suppose une incertitude annoncée. La bonne réponse n'est ni « on accepte » ni
   « on refuse » sèchement, mais « on refuse en l'état, et mon protocole était incomplet ».

## 6. Verrous expérientiels

| Verrou | Exigence | Ce qu'il empêche |
|---|---|---|
| `__exp.flex3` | 3 profilés rompus en flexion | répondre à l'activité 0 sans toucher au banc |
| `__exp.trac5` | 5 profilés rompus en traction | recopier le tableau de traction |
| `__exp.flex5` | 5 profilés rompus en flexion | remplir les 10 relevés sans essai |

Les dix relevés sont en outre comparés aux **vraies** valeurs du banc, à 0,05 près :
41 au lieu de 41,1 est refusé. C'est le cœur du code — on évalue la mise en œuvre.

## 7. Différenciation

* **🅰 avec le vrai laboratoire** — le « laboratoire des matériaux » du Réseau National
  Technologie Collège (gratuit, sans compte). Il fait la traction et la compression,
  **pas la flexion** : cette limite est traitée comme un objet d'étude, pas contournée.
* **🅱 avec le banc de la page** — hors ligne, sans installation. Voie par défaut.
* **🅲 sans écran** — les deux tableaux de relevés s'impriment, toutes les valeurs sont dans
  les corrections dépliables. Choisir, écrire, décider : le travail reste entier.

## 8. Ce que ce lot ne fait pas

* **Aucun essai physique** : le banc est une simulation, et la page le dit à l'élève à trois
  endroits — dont une question de QCM entièrement consacrée à ce que vaut une valeur simulée.
* **Le modèle a un domaine de validité** : la flèche de 723,8 mm du PVC est hors du domaine
  des petits déplacements, la page l'écrit et en tire une leçon plutôt qu'un chiffre.
* **Le vérificateur ne lit pas le protocole rédigé** : il compte des lignes. C'est écrit dans
  la page, et c'est la raison d'être de la grille de relecture croisée.
* **Un seul essai par candidat** : une question de QCM porte précisément sur ce manque.

## 9. Prolongements

* **📐 Défi forme** — le tube aluminium et le tube PVC ont la *même* géométrie. Que mesure
  exactement la comparaison de leurs deux flèches, et pourquoi est-ce le seul couple du
  tableau qui le permette ?
* **🌊 Défi Martinique** — classer les cinq candidats par tenue à l'air salé, et écrire le
  protocole de *cet* essai-là : que mesure-t-on, sur combien de temps, comment sait-on qu'on
  a fini ?
* **🔬 Défi laboratoire** — chercher si le laboratoire d'éduscol propose un essai de flexion.
  S'il ne le propose pas, écrire ce que cela apprend sur le choix d'un instrument.

## 10. Fichiers du lot

```
3e_C8.2/
├── sequence_3e_C8.2_mat-de-la-station.html   banc de flexion + traction intégré, 7 blocs
├── qcm_3e_C8.2_mat-de-la-station.html        30 q · 90 réfutations · C8.2 ×20, C3.4 ×10
├── lexique_3e_C8.2.html                      30 notions, généré depuis le QCM
├── synthese_eleve_3e_C8.2.html               à imprimer, noir et blanc
├── synthese_professeur_3e_C8.2.html          pari didactique, verrous, limites, LSU
├── fiche_pedagogique_3e_C8.2.md              cette fiche
├── matrice_couverture_3e_C8.2.csv            notion → activité → production → QCM
├── rapport_tests_3e_C8.2.md                  32/32 sur la séquence, 26/26 sur le QCM
└── README.md
```
