# Fiche pédagogique — 4e_C8 Valider une solution technique

**Objet-fil** : jardin connecté (suite du LOT 01)  
**Ancrage territorial** : **New York** (school garden / rooftop)  
**Codes** : 4e_C8.1 · 4e_C8.2 · 4e_C8.3  
**Durée** : 4 × 55 min (3 jusqu'au 25/11/2026 : la console a désormais sa séance)  
**Domaines du socle** : D2 · D3 · D4 · D5

## Intention
Faire passer l’élève de « j’ai conçu » à « je sais prouver que ça marche » par un protocole de test simple, une analyse de résultats et une proposition d’amélioration — contraintes locales : gel, pluie, vent urbain.

## Versions A/B/C
- **A** : tests réels sur maquette (très basse tension uniquement)
- **B** : simulation + tableau de résultats fourni
- **C** : purement papier (protocole + analyse de données fictives)

## Points de vigilance
- Ne jamais brancher sur le secteur 230 V
- Critères de réussite explicités avant les tests
- Décision de validation collective argumentée
- Critères NY : gel, vent de canyon, pluie, variations saisonnières

## Évaluation LSU
Production d’équipe (protocole + tableau de résultats + décision + améliorations) + auto-positionnement.

## Harmonisation du 26 août 2026

Le lot a reçu les dispositifs communs du dépôt : billet d'entrée hors progression, mode
essentiel, tableau de bord des six activités, versions étayées, durées à la convention,
carte de référentiel recopiant le programme au mot près, sélecteur de parcours 🅰/🅱/🅲
réellement agissant, et une barre de progression qui suit les validations. Contrôle
mécanisé : **cinq manquements → zéro**. Suite committée : **41 tests, tous verts**.

**Le défaut le plus grave n'était pas là.** Les 28 bonnes réponses du QCM étaient toutes
en position B : un élève qui clique la deuxième proposition à chaque question obtenait
28/28 sans rien savoir. Les propositions ont été redistribuées (7 par position) par
`repartir_qcm.mjs`, dont la suite de positions est écrite en clair — reproductible, pas
tirée au hasard. Le détail est dans le rapport de tests.

## Découpage en séances à onglets (31/10/2026, pilote des séquences sans onglets)

| Séance | Question directrice | Contenu | Temps |
|---|---|---|---|
| 1 — Faire d'abord, puis écrire le protocole | Comment prouver qu'un prototype répond au besoin, sans se contenter d'un avis ? | Ouverture (situation, problématique, hypothèse, billet), activité 0 (banc virtuel), activité 1 (diagramme puis protocole) | ~15 + 10 + 20 min |
| 2 — Analyser les résultats, ligne par ligne | Que disent les résultats du banc, exigence par exigence ? | Activité 2 (diagramme des exigences, grille « Conforme ? », diagnostic) | ~35 min |
| 3 — La console : simuler, puis proposer l'essai réel | La console de la jardinière tiendra-t-elle sur le toit ? | Activité 2 bis (régler la simulation), activité 2 ter (proposer le protocole de l'essai réel) | ~15 + 20 min |
| 4 — Améliorer, refaire, conclure | Et si un critère change ? | Activité 3 (améliorations), réinvestissement, synthèse, Bonus, bilan (retour à l'hypothèse, « Comment j'ai travaillé », « Je me positionne » sur 4e_C8.1 à C8.3), renvoi au QCM | ~15 + 15 + 15 min |

Dès la séance 2, l'ouverture est repliée dans le volet « 📖 Rappel » (règle d'or n°311) ; le sélecteur de parcours, la progression et « Où j'en suis » restent visibles.

## Activité 2 bis — paramétrer une simulation de tenue mécanique (22/11/2026)

**Pourquoi.** L'audit hebdomadaire du 22/11/2026 (#867) a relevé que le lot ne portait pas son code : 4e_C8.1 demande de
**paramétrer une simulation fournie pour valider la tenue mécanique d'un matériau**, et l'activité 0 est un banc de
**comportement** (pluie, gel, LED) — ni matériau, ni charge, ni déformation. Pascal a décidé d'ajouter une activité courte
(« 1 oui », 22/11/2026).

**Ce que fait l'élève (≈ 15 min, séance 2).** Le club accroche ses jardinières au muret du toit, chacune sur deux consoles.
L'élève règle une simulation fournie — matériau, épaisseur, longueur, charge — et la lance :
- Q1 : la charge à entrer pour UNE console, dans le cas le plus lourd (terre 16 kg + neige 6 kg, sur deux consoles → 11 kg) ;
- Q2 : la console du club (PLA imprimé en 3D, 6 mm) → elle casse ;
- Q3 : en ne changeant que l'épaisseur, la plus petite qui donne k ≥ 3 ;
- Q4 : pourquoi un seul réglage à la fois ; Q5 : la décision écrite, avec le nombre.

**C'est la spirale C8 voulue par le dépôt** : en 5e (`5e_C8.1`, la patère du hall), la simulation arrive réglée ; en 4e,
l'élève entre les valeurs ; en 3e, il choisit la question. Les matériaux sont ceux de la patère, tirés du même modèle.

**Les nombres** ne sont écrits qu'à un endroit : `_generation/console_jardiniere.py` (règle d'or n°233). Il écrit
l'activité, la partie 7 de la synthèse élève et `console_attendus.json` ; lancé sans option, il imprime le tableau
(plus petite épaisseur validée : bois 20 mm, PLA et PVC 15 mm, aluminium 10 mm, acier 8 mm) et dit si la page est à jour.

**La validation dit vrai** (n°340) : l'activité ne se valide pas tant que la simulation n'a pas été lancée sur la console
du club ET sur au moins trois épaisseurs de PLA, sans changer le reste. La décision écrite (Q5) n'est pas corrigée aux
mots-clés : la correction donne une réponse attendue.

**Ce que la simulation suppose** (écrit dans la page) : console neuve, encastrée, poids au milieu de la jardinière,
température ordinaire. Elle ne dit rien du soleil (le PLA ramollit vers 55 degrés Celsius), de l'eau ou du gel : la
correction le relie à un essai réel : c'est l'activité 2 ter, ajoutée le 25/11/2026 (ci-dessous).

## Activité 2 ter — proposer le protocole de l'essai réel (4e_C8.2, 25/11/2026)

**Pourquoi.** 4e_C8.2 demande de **proposer un protocole de test pour valider la tenue mécanique d'un matériau** ; le lot ne
le faisait que sur le comportement du système. La simulation vient de dire quelle épaisseur de PLA tient : l'activité fait
proposer l'essai qui le prouvera sur de vraies pièces, avant d'en visser quarante sur le toit (décision de Pascal du
25/11/2026). Pour tenir dans des séances de 55 min, la console a maintenant **sa séance** : la séquence passe de 3 à 4
séances (2 bis quitte la séance 2, qui ne garde que l'activité 2).

**Ce que fait l'élève (≈ 20 min, séance 3).** Sous les yeux, le schéma du banc (montant, console, sacs de sable, règle
graduée, bac) et sa légende ; sept questions à boutons radio, puis le protocole écrit :
- Q1 : pourquoi un essai réel après la simulation — le modèle calcule une pièce pleine, une console imprimée a des couches
  et un remplissage ;
- Q2 : la charge d'essai — 3 × 11 = **33 kg**, ce que le cahier des charges exige (pas la casse : c'était le protocole de
  5e, fait pour comparer des matériaux) ;
- Q3 : par **paliers** sur la même console, 11, 22 puis 33 kg (deux sacs de 5,5 kg par palier) ;
- Q4 : la mesure — la **flèche**, lue sur une règle graduée fixée debout ;
- Q5 : la flèche attendue à 33 kg — tant que la console est élastique, elle grandit comme la charge : 4,1 → **12,3 mm** ;
- Q6 : le critère écrit avant — à 33 kg tenus 5 min, aucune fissure ; déchargée, le bout revient à 1 mm près ;
- Q7 : **trois** consoles, imprimées pareil ;
- Q8 : le protocole en six lignes (pièce, montage, charge, mesure, critère, sécurité), avec sa version étayée et une
  grille « je relis mon protocole » à trois cases, sans note.

**La spirale C8** : en 5e (`5e_C8.2`), l'élève **suit** un protocole fourni et **casse** l'éprouvette pour comparer des
matériaux ; en 4e, il **propose** l'essai d'une pièce, et ne casse rien.

**Les nombres** viennent du même modèle (`_generation/console_jardiniere.py`, n°233) : épaisseur validée, charge d'essai,
paliers, flèches (f = F·L³ / 3EI, avec le module du PLA de la patère de 5e). À 33 kg, σ = 43,2 MPa, sous les 45 MPa de la
limite élastique du PLA : l'essai ne casse rien, et une console imprimée comme le modèle revient en place.

**La validation dit vrai** : les sept questions se vérifient ; le protocole écrit n'est pas corrigé aux mots-clés (il doit
être là, au moins 120 caractères) — l'élève le compare au protocole modèle de la correction. Banc :
`tests_protocole_4e_C8.1.mjs` (18 tests : la page dit ce que dit le modèle, un protocole de deux mots ne valide rien,
« jusqu'à ce qu'elle casse » est refusé avec son pourquoi, tout revient au rechargement, rien ne déborde à 390 px, les
étiquettes du schéma ne se chevauchent pas).

**Ce qui reste** : les dix questions du QCM rangées sous 4e_C8.2 portent sur le protocole d'un **comportement** (étanchéité,
gel, diagnostic) ; aucune ne porte encore sur l'essai d'un matériau.

