# Fiche pédagogique / inspection — Le jardin connecté : arrosage automatique (4e_C6.2)

> **Correction préalable.** J'avais annoncé à Pascal que ce lot « ne se répare pas avec une
> fiche : il se refait ». C'était faux, et pour la troisième fois cette semaine de la même
> manière : **j'avais jugé le lot sur ce que son dossier ne contenait pas, sans lire la page.**
> La page porte un contrat de séquence (règle n°18), un référentiel avec capacité observable,
> huit activités minutées, deux verrous expérientiels, une grille LSU à quatre niveaux, un bloc
> de différenciation, un bonus à trois défis, une fiche professeur intégrée — et un rapport de
> tests réels à 27/27. Ce lot n'est pas à refaire. Il lui manquait trois pièces et un bandeau.

## Identification

| Champ | Valeur |
|---|---|
| Niveau | 4e (programme 2024, applicable rentrée 2026-2027) |
| Code principal | 4e_C6.2 — *Compléter un programme pour répondre à une fonctionnalité d'un OST* |
| Codes mobilisés | 4e_C4.1 (chaîne d'énergie) · 4e_C4.4 (chaîne d'information) · 4e_C4.5 (transformation des données) · 4e_C1.4 (usage raisonné) |
| Thème | Thème 2 — Structure, fonctionnement, comportement |
| Socle | D1.3 · D2 · D4 |
| Objet-fil | Le jardin connecté du collège — même objet que `4e_C4.1-C4.9`, vu ici par son **programme** |
| Durée | **3 séances de 55 min** (bandeau posé le 28/08/2026) · **145 min d'activités**, soit 20 min de marge |
| Version | 🅰 prototype réel / 🅱 éditeur embarqué / 🅲 sans machine — déclarées en tête |
| Éditeur | Vittascience Python, **3 iframes** — voir « Dépendances » ci-dessous |

## Découpage en séances

La page énonce elle-même trois **problèmes intermédiaires, « un par séance »**. Le découpage
ci-dessous est le sien, pas le mien :

| Séance | Problème intermédiaire (texte de la page) | Activités | Durée |
|---|---|---|---|
| S1 | *Comment mesurer l'humidité du sol et transmettre cette information ?* | 1 · 2 · 3 | 50 min |
| S2 | *Comment décider si la plante doit être arrosée, et commander la pompe ?* | 4 · 5 | 35 min |
| S3 | *Comment vérifier que le système répond au besoin, et quel est son impact ?* | 6 · 7 · 8 | 55 min |

*(Ces trois séances ne sont pas matérialisées en onglets dans la page : elles existent dans le
texte, pas dans la navigation. L'élève déroule les huit activités d'un seul tenant.)*

## Situation, problématique, mission

- **Situation** : le prototype d'arrosage automatique du jardin connecté du collège.
- **Mission** (texte de la page) : compléter le programme du prototype — les blocs à remettre en
  ordre, puis les trous du Python —, le tester dans l'éditeur embarqué, et valider son
  comportement sur un banc de tests, **cas frontière compris**.
- **Production attendue** : un programme complété et testé, le banc de tests au vert, et un court
  argumentaire justifiant le seuil choisi.

## Capacité attendue (observable), telle que la page l'écrit

> Remettre en ordre puis compléter la condition (seuil d'humidité) d'un programme **fourni**,
> l'exécuter dans l'éditeur, et prouver son comportement par un banc de tests.

C'est bien « **compléter** », le verbe du code 4e_C6.2 — et non « programmer », qui est le verbe
de la 3ᵉ. Le lot ne surestime pas ce qu'il fait faire.

## Déroulé, activité par activité

| # | Activité | Durée | Production | Verrou |
|---|---|---|---|---|
| 1 | La chaîne d'information du prototype | 10 min | 3 cases complétées | — |
| 2 | Le capteur parle en nombres (0–1023 → %) | 15 min | conversion justifiée | — |
| 3 | Les blocs en désordre — programme de MESURE | 25 min | 5 lignes ordonnées + exécution | **éditeur 🧪 exigé** |
| 4 | La décision — en français d'abord | 10 min | règle complétée, pseudo-code généré | — |
| 5 | Le Python à trous | 25 min | 3 trous **prédits** puis exécutés | **éditeur 🧪 exigé** |
| 6 | Le banc de tests — seuil et preuve | 20 min | 3 tests prédits puis exécutés | **banc 3/3** |
| 7 | Le verdict — cahier des charges | 20 min | verdict ligne par ligne, preuve citée | — |
| 8 | L'impact — moins d'eau, vraiment ? | 15 min | 2 arguments pour le débat | — |
| — | Où en es-tu ? | 5 min | auto-positionnement 4 niveaux | — |

La démarche **prédire → exécuter → comparer** est présente aux activités 5 et 6 : l'élève écrit
son attendu *avant* de cliquer. C'est précisément ce que l'audit ChatGPT réclamait pour la 3ᵉ ;
ici, en 4ᵉ, c'est déjà en place.

## Différenciation, inclusion, accessibilité

Deux niveaux d'aide par activité (un indice, puis la démarche), à ouvrir **avant** la correction.
Élèves rapides : bloc bonus à trois défis (condition de nuit, seuil réglable, journal). Pont vers
la 3ᵉ explicitement nommé : la version multi-conditions attend dans `3e_C9.1`.
**Manque : le mode essentiel.** Seule séquence des dix-sept du Thème 2 à ne pas l'avoir.

## Évaluation

Grille LSU à quatre niveaux, appliquée à 4e_C6.2 en séance 3, sur la capacité observable :
insuffisante (condition non complétée même aidée) · fragile (complétée avec les deux aides) ·
satisfaisante (complétée et exécutée seul·e) · très bonne (banc au vert, frontière justifiée).
QCM d'entraînement : `qcm_4e_C6.2_arrosage_automatique.html` — **30 questions, 90 réfutations**
(une par distracteur), 30 notions nommées, codes 4e_C6.2 (16) · C4.4 (5) · C4.5 (4) · C4.1 (3) ·
C1.4 (2), répartition A/B/C/D 8/7/7/8. Écrit le 28/08/2026 à partir des 24 questions du QCM
hérité du lot, qui portaient sur le bon sujet mais exposaient la bonne réponse dans le code de
la page (`value="v0"`). Correspondance notion → numéro de question dans
`matrice_couverture_4e_C6.2.csv`.
> **Ce que ce QCM évalue, et ce qu'il ne fait que mobiliser.** Un seul code y est assez
> échantillonné pour être conclu seul : **4e_C6.2, avec 16 questions**. Les quatre autres sont des
> appuis — C4.4 (5 q.), C4.5 (4 q.), C4.1 (3 q.), C1.4 (2 q.) : ils donnent au QCM son ancrage
> dans l'objet, ils ne se reportent pas au LSU. Deux questions ne valident pas une compétence.
> Mesure : `_outils/controle_echantillonnage.py`.

**Sommative** : à construire par l'enseignant. Aucun corrigé sommatif publié.

## Dépendances — à lire avant de réserver la salle

**Trois iframes `fr.vittascience.com/python/`.** La voie principale des activités 3 et 5 passe par
cet éditeur distant. Conséquences, dites franchement :

- il faut du réseau, et selon la configuration de l'ENT, un compte ;
- le rapport de tests du lot **le dit lui-même** : « Non testé (hors périmètre local) : le contenu
  de l'iframe Vittascience (cross-origin, connexion requise) — seul le suivi d'ouverture est
  vérifié ». 27 tests sur 27 passent ; aucun ne prouve que l'éditeur fonctionne ;
- la mention « données conservées localement » vaut pour la page, **pas** pour l'éditeur : ce que
  l'élève tape dans l'iframe part chez un tiers.

**Repli si le réseau tombe** : les activités 1, 2, 4, 6, 7, 8 (soit 90 des 145 minutes) ne
demandent aucun éditeur. Les activités 3 et 5 peuvent se faire sur papier — l'élève ordonne les
lignes et complète les trous —, mais le **verrou expérientiel** ne s'ouvrira pas, et c'est
normal : il atteste d'une exécution qui n'aura pas eu lieu.

## Traces et preuves (honnêteté du lot)

Deux SVG originaux (`schema_chaines_arrosage.svg`, `schema_eclairage_automatique.svg`).
Rapport de tests : **27 / 27**, suite Playwright réelle sous Chromium en 390×844, zéro erreur JS.

**Ce que le lot ne porte pas :**

1. **Le mode essentiel** — absent, seul cas du Thème 2.
2. **Les séances ne sont pas navigables** : trois séances annoncées dans le texte, aucun onglet.
3. ~~Aucun bouton de QCM dans la page~~ — **corrigé le 28/08/2026** : le lot a désormais son QCM
   au gabarit, et un seul bouton (règle n°4). Les trois fichiers `qcm_` historiques restent dans
   le dossier sans être boutonnés : un QCM au gabarit mais sur l'**éclairage**, codé en
   vocabulaire privé (CAP/PRG/SYS) ; le QCM hérité de 24 questions, devenu matière première du
   nouveau ; et un TP dont le nom de fichier ment (`qcm_algorigrammes_domotique.html`).
   *(Le lexique du lot suit le bouton, pas le dossier : il tient 30 notions, pas 60.)*
4. **Les synthèses élève et professeur ne sont pas des fichiers.** La page porte une section
   « Synthèse — à retenir » et une « Fiche professeur » repliée ; le dossier `Synthèses/` ne
   contient qu'un `.gitkeep`. Le contenu existe, le fichier non — ce qui est exactement ce que le
   contrôle de statut mesurait.
5. **La chaîne d'énergie est lue, jamais tracée** : le code 4e_C4.1 est mobilisé par un schéma
   fourni, pas par une production de l'élève.

## Ce qui reste à faire, dans l'ordre

1. ~~Un QCM du lot au gabarit maison~~ — **fait le 28/08/2026.**
2. Le mode essentiel, aligné sur les seize autres séquences.
3. Les onglets de séances, sur les trois que la page nomme déjà.
4. Exporter les deux synthèses en fichiers, depuis le contenu qui est déjà dans la page.
   *C'est la dernière pièce qui manque au contrôle de statut — elle sera écrite parce qu'un élève
   absent en a besoin, pas pour faire passer une mesure au vert (règle n°197).*
