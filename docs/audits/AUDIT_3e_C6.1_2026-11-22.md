# Audit de « Programmer l'alerte » (3e_C6.1 + C6.3) — 22/11/2026

Page : `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.1/`
(séquence, QCM, synthèses, schémas, fiche, bancs). Deux regards :
- l'audit externe du 21/11/2026, que Pascal a joint (`Audit_3e_Programmer_alerte.md`), vérifié remarque par remarque
  avec le skill `relire-un-audit-externe` ;
- mon audit du 22/11/2026, page ouverte dans Chromium à 390 et 1 280 px, avec les outils de `_outils/`.

Corrections livrées : PR #886 (fusionnée) et #889 (suite). Skills : PR transversale `fable/skills-banc-essai`.

## 1. Verdict

| | Avant (21/11) | Après (22/11) |
|---|---|---|
| Grille des clés de voûte, sur 100 (skill `cadrage-cles-de-voute`, paliers) | **≈ 58** — à reprendre avant la classe | **≈ 87** — publiable ; aucune preuve en classe |
| 1. Preuve de compétence (15) | 15 : l'écrit de la bouée existait (21/11) | 15 |
| 2. Questions qui ne soufflent pas (15) | 7 : d1_8 donnait la réponse de d1_l2 ; le QCM montrait le schéma complet | 15 |
| 3. Retour qui dit quoi reprendre (12) | 6 : « branches incomplètes » pour un programme juste | 12 : le premier écart nommé, prévisions et essais séparés |
| 4. Cohérence (12) | 0 : algorigramme à 50 après la consigne qui fixe 60 ; plan de tests de la v1 avec un gyrophare | 12 : une spécification par version (n°373) |
| 5. Rappel et progression (10) | 10 | 10 : avec, en plus, une reprise de mémoire aux séances 2 et 3 |
| 6. Lisibilité au téléphone (10) | 10 | 10 : le tableau du banc devient des cartes à 390 px |
| 7. Accessibilité (8) | 4 : QCM sans `<main>` | 4 : axe au niveau de la référence ; zoom 200 % et lecteur d'écran non éprouvés |
| 8. Usage de classe (8) | 4 | 4 : 53 min annoncées pour les séances 2 et 3, jamais chronométrées |
| 9. Vérification déclarée (5) | 2 : banc 38 / 38, qui validait les défauts | 5 : banc 57 / 57, critères de recette de l'audit au mot près |
| 10. Preuve en classe (5) | 0 | 0 |

**Le défaut central.** Le bouton « Vérifier » jugeait l'écriture du programme, pas ce qu'il fait. La règle d'or n°333
(14/11/2026) le disait déjà. La page était antérieure à la règle, et aucun outil ne la mesurait hors des bancs de lot.
C'est corrigé, et la règle est maintenant mesurée sur tout le site (`controle_verification_execute.py`).

## 2. L'audit externe, remarque par remarque

✅ confirmé et corrigé · ♻️ déjà vrai ou déjà fait ailleurs · 💡 idée jugée (retenue ou non) · 🔶 décision de Pascal.

### Priorités (§ 1)

| Remarque | Statut | Ce qui a été fait |
|---|---|---|
| A4 : apostrophes → 5 / 7 et « branches incomplètes » | ✅ | Le programme est exécuté sur dix vents, avec le même verdict quelle que soit l'écriture (banc, test 16). |
| A4 : `>=` à 118 → 7 / 7 | ✅ | Refusé, avec « 118 km/h · niveau : rouge attendu, violette obtenu · gyrophare : arrêté attendu, actif obtenu » (16 bis). L'audit écrivait « violet obtenu » : la page dit l'état exact. |
| A5 : la v1 dans l'éditeur, 7 bonnes prévisions → 7 / 7 | ✅ | « Mes prévisions » et « Essais de ma version » sont comptés à part ; « à exécuter », puis « 3 / 10 », puis « à rejouer » (17 à 17 quater). |
| L'algorigramme de la spécification teste 50 | ✅ | Il teste 60. Trois versions nommées, une table par version (20 quater). |
| Plan de tests « v1 » avec un gyrophare | ✅ | C'est le vrai plan de la v1, sans gyrophare. La copie B fautive est nommée. |
| Récit : sirène en orange, Météo-France, « la moitié du quartier » | ✅ | « Dans notre maquette, au niveau orange… », « le club fixe son seuil expérimental à 60 » ; « Simulation scolaire » à l'ouverture et sur le banc. |
| A1 : constante classée « entrée » comme une mesure ; la pression ; la donnée produite puis relue | ✅ | Trois choix (mesure, paramètre, produite), avec d1_7 (la pression ne décide rien) et d1_8 (la ligne qui relit). |
| A1-A2 : lignes 6 et 21 fragiles ; justification aux mots-clés ; « 3 / 3 » à côté d'une justification jugée insuffisante | ✅ | La v1 est figée pour les lectures (test 8). La justification est écrite puis relue, jamais jugée par la machine. Les messages « Choix : x / 3 » et « Justification : écrite » sont séparés. |
| A3 : `60.5` accepté ; « verte/jaune » | ✅ | La valeur est lue dans le programme exécuté (11 bis). Les quatre états exacts sont utilisés partout. |
| QCM : 10 / 10 affiché 6,7 / 20 | ✅ | « 10 / 10 réussies », « 10 / 30 travaillées », la note sur 20 seulement au parcours complet (29 bis). |
| Billet : « rien n'est en place » | ✅ | Une ligne par question (réussie, à revoir, sans réponse), et la mention « le capteur mesure juste ». |
| Ouverture chargée ; bilan à une hypothèse | ✅ | L'éditeur est replié en séance 1 ; les deux hypothèses reviennent au bilan (19 sexies). |

### Ce que l'élève doit montrer, et la séquence question par question (§ 2 et 3)

| Remarque | Statut |
|---|---|
| Résolution du vent (« km/h entiers », 118,1 au dixième) | ✅ Écrite au cahier des charges et sur le banc ; la bouée est au dixième de mètre. |
| La boucle de la vraie station (remettre à faux n'éteint pas) | ✅ Nuance ajoutée dans la correction de A4 ; le banc part du repos à chaque essai. |
| Hypothèse 2 en deux parties (« j'essaierai… », « je prévois… ») | ✅ |
| Billet 1 : « la mesure a été vérifiée » | ✅ |
| Le traceur pas à pas après une prédiction (A2) | ✅ Affiché après « Vérifier », sans mouvement obligatoire. |
| Accepter « 118 ne dépasse pas 118 ; il dépasse 90 » | ✅ (test 10) |
| A3 : comparaison v1 / courant par lignes ajoutées et supprimées | ✅ Différences + / − en couleurs. |
| A4 : tableau d'exigences, dévoiler les emplacements à la demande, banc relié à l'éditeur | ✅ « 🪜 Je veux être guidé·e » (exemple ① puis les trois autres). |
| A5 : version essayée, 89 / 90 / 91, copie B, 118 qui départage | ✅ |
| Bouée : unité, 4,0, mini-éditeur, résolution, bornes de l'orange | ✅ Les lignes 4 à 7 s'essaient à 2,0 · 3,0 · 4,0 · 5,0 m, sans note. |
| Bonus : simulation au départ du fichier exporté, pression (ET qui perd une alerte), mBot2 (sens inversé), accessibilité | ✅ Plus une **correction complète** des quatre défis, qui manquait (§ 3 ci-dessous). |
| Bilan : deux hypothèses, une ligne du journal d'essai, choix « branche / égalité / indentation / essai », confiance facultative | ✅ |
| Animations « suivre 95 », cartes HTML, droite graduée, boîte de réception, etc. | 💡 Non retenues une à une. Le traceur et le banc couvrent l'essentiel, et l'audit lui-même conseillait de ne pas multiplier les animations. |

### Le QCM (§ 4)

| Questions | Statut |
|---|---|
| Q03, Q04, Q05, Q08, Q10, Q12, Q13, Q19, Q20, Q22, Q24, Q25, Q26, Q29, Q30 | ✅ Réécrites : incident pour Q03, convention pour Q04, nuances de Q19, Q25 et Q26, numéros de Q12 et Q22, perte au réinitialiser pour Q30… |
| Q01 (le schéma complet donne le classement) | ✅ Dans #889 : schéma à compléter et propositions crédibles. Q10 aussi. |
| Les autres propositions d'animation (Q06, Q07, Q08…) | 💡 Non retenues dans ce lot. |

### Ergonomie, outils, éthique, organisation (§ 5 à 9)

| Remarque | Statut |
|---|---|
| Version active toujours visible ; « Effacer » éloigné et qui dit ce qu'il efface | ✅ |
| Barre d'outils réordonnée ; un seul panneau de code | ✅ |
| Virgule décimale acceptée à la saisie | 💡 Non traité. Le banc explique `float("4,0")` (« un nombre décimal s'écrit avec un point »). |
| PNG de situation à 2 Mo | ✅ décidé (§ 6) — Les conditions de Canva interdisent d'en retirer les métadonnées de provenance : une version allégée se réexporte depuis Canva. |
| Skulpt « à prototyper » | ♻️ Le dépôt a, depuis le 04/11, un éditeur Python commun bâti sur Skulpt (`_ressources-communes/editeur-python/`). Il n'a pas été consulté avant d'écrire le banc-python : erreur de méthode (§ 4). ✅ décidé (§ 6) : garder les deux, chacun à sa place (`_outils/banc_python/LISEZMOI.md`). |
| Vue en blocs (Blockly) | 💡 Non retenue : trois éditeurs, c'est trop ; la n°308 veut de vraies captures de Vittascience. |
| Table de référence du banc (dix vents) | ✅ Reprise telle quelle. |
| « Simulation scolaire — seuils fictifs du club » ; accessibilité de l'alerte ; justice du retour | ✅ |
| Effacement accessible depuis le mode mission | 🔶 Outil commun `_outils/mode_mission/`, hors de ce lot. |
| Trois séances de 55 min | ✅ Durées réécrites (A1 25, A2 20 ; reprise 3, A3 15, A4 35 ; reprise 3, A5 25, A6 25) ; non chronométrées. |
| Essai au collège (binômes, PC, clavier seul, tablette) | 🔶 À faire en classe. |

## 3. Mon audit : ce que l'audit externe n'avait pas vu

| Gravité | Défaut | Statut |
|---|---|---|
| P1 | Le Bonus n'avait **pas de correction** (n°4, n°336 ; `controle_correction_complete.py`, K1). | ✅ Correction des quatre défis, avec le programme corrigé en `.py`, rejoué dans Python et au banc (10 / 10). |
| P1 | La question d1_8 nommait « la ligne 21 », réponse de d1_l2 ; le pourquoi de d1_6 aussi (n°341, `controle_propositions_indices.py`, I3). | ✅ |
| P1 | **Mon propre banc** disait « SyntaxError » à des programmes Python justes (f-string, `is True`, `a if c else b`, `;`). | ✅ banc-python 1.1 : ces écritures sont lues. Le reste est annoncé comme « limite du banc, pas forcément une erreur de ton programme » (tests 17 à 19, page 16 quinquies). |
| P2 | Le seuil de l'activité 5 se lisait « 6 / 8 » pour `controle_validations.py`. | ✅ Écrit `ok+diag===8`, ce qui revient au même et se lit juste. |
| P2 | La carte « Le contrat de la séquence » répétait l'ouverture. | ✅ Retirée. |
| P2 | Les synthèses élève et professeur parlaient de « verte/jaune » et d'« analyse du code ». | ✅ |
| P2 | Le QCM n'avait pas de `<main>` (comme **77 QCM sur 78** du site). | ✅ Pour ce QCM ; puis pour les 77 autres (§ 6). |
| P2 | Six sigles nus (CRCN, DNB, IDE, LED, OST, QCM). | ✅ En clair ou en infobulle, selon la vague n°44 du même jour. |
| P2 | Aucune reprise de mémoire aux séances 2 et 3 (n°369, posée le jour même). | ✅ Deux questions par séance, et un champ « ce qui reste flou » au bilan (n°372). |
| P2 | Le tableau du banc était serré à 390 px. | ✅ Il devient des cartes. |
| P2 | Deux bancs communs refusaient après la livraison de #886 (`qcm_aides/banc_aides.mjs` A9, `impression_papier/banc_papier.py`). | ✅ Dans #889. Leçon ajoutée à `controle-qualite-lot`. |
| P3 | Ordre des titres dans les versions 🅰 / 🅱 / 🅲 (axe, heading-order) ; pression sans unité nommée (n°312) ; différences en monochrome (n°13). | ✅ |
| P3 | Pourquoi du mode mission sans étape suivante : 36 sur 48. | Mesuré : 27 sur 69 après la réécriture ; reste à reprendre. |

## 4. Ce que cette expérience change dans la méthode

- **Règle d'or n°373 (en essai)** — Un programme qui change dit sa version.
- **Règle d'or n°374 (en essai)** — On prévoit avant d'essayer, et une prévision juste ne vaut pas un essai.
- **N°333 mesurée sur tout le site** : `_outils/controle_verification_execute.py`, éprouvé sur 12 cas connus.
  - Mesure de départ : 7 pages à éditeur ; 3 exécutent le programme, 0 le juge par son seul texte, 4 n'ont pas de vérification du code.
- **La n°333 rangée sous la clé de voûte n°6** (« un score dit quoi reprendre »), décidé le 22/11/2026 (§ 6) : un score ne dit vrai que s'il juge
  la production réelle. J'avais d'abord proposé d'en faire une huitième clé ; l'audit #867 du même jour a décidé « sept,
  pas neuf » — une règle nouvelle précise l'une des sept.
- **Skill `banc-essai-programme`** (nouveau). Mises à jour de `validations-qui-disent-vrai` (§ 2 ter), `relire-un-audit-externe`, `cadrage-cles-de-voute` (question 18, la n°333 sous la clé 6) et `controle-qualite-lot` (le nouveau contrôle ; les bancs des sous-dossiers de `_outils/`).
- **Trois erreurs de méthode, dites.**
  - Le banc-python a été écrit sans chercher l'éditeur commun.
  - Deux des trois règles prévues existaient déjà dans la n°333.
  - Deux bancs communs n'ont été rejoués qu'après la fusion.

## 5. Non vérifié

Un vrai téléphone ou une tablette, un lecteur d'écran, le zoom 200 % de bout en bout, une impression réelle, la durée
des séances en classe, un élève.

## 6. Les quatre décisions (carte blanche de Pascal, 22/11/2026)

1. **Deux moteurs Python, une seule vérité.** On garde l'éditeur commun (Skulpt) **par défaut** pour tout vrai Python,
   et le banc-python **seulement** pour le chemin suivi pas à pas ou la vérification instantanée du Python du collège.
   Garde-fou : le test 20 de `tests_banc_python.mjs` fait tourner 7 programmes du lot (et leurs variantes) dans le
   banc ET dans CPython, vent par vent, et exige les mêmes sorties (25 / 25). Unifier (donner la trace à l'éditeur
   commun) attendra qu'une deuxième séquence ait besoin du pas à pas.
2. **La n°333 se range sous la clé de voûte n°6** (« un score dit quoi reprendre ») : un score ne dit vrai que s'il juge
   la production réelle. Écrit au tableau des règles, dans `_outils/METHODE.md` et dans `cadrage-cles-de-voute`.
3. **Le `<main>` sur les 78 QCM** : `_outils/poser_main_qcm.py` (idempotent, `--ecrire`), éprouvé sur 8 cas connus
   (`tests_poser_main_qcm.py`), plus le gabarit `ateliers-representations/_generation/gabarit_qcm.tpl` (son générateur
   reproduit les 7 QCM à l'octet). 78 QCM sur 78 ont leur région principale.
4. **L'image de situation garde son fichier d'origine.** Un export JPG allégé a été fait depuis Canva (création
   `DAHaEhWWmSY`, 1 536 px, qualité 82), mais le serveur d'export de Canva n'est pas joignable depuis l'atelier : le
   fichier n'a pas pu entrer dans le dépôt. Les huit copies sont identiques (git ne stocke qu'un objet), les séquences
   la chargent en différé, les synthèses tout de suite pour l'impression. À reprendre si une page s'ouvre trop
   lentement en classe : exporter depuis Canva et remplacer les huit copies dans le même commit.

