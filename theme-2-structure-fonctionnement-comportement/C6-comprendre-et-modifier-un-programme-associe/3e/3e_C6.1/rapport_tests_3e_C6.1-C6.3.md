# Rapport de tests — LOT 04 « Programmer l'alerte » (3e_C6.1 + C6.3)

**Suite** : `tests_3e_C6.1-C6.3.mjs`, livrée dans ce dossier · **Outil** : Playwright
(Chromium headless), viewport téléphone 390 × 844 · **Rejouée le 22/11/2026** ·
**Verdict : 56 / 56 ✅** (38 / 38 le 21/11/2026 ; refonte du banc pour les audits des 21 et 22/11/2026)

```
cd theme-2-.../C6-.../3e/3e_C6.1 && node tests_3e_C6.1-C6.3.mjs
node _outils/banc_python/tests_banc_python.mjs      # le petit Python de la page, sans navigateur : 24 / 24
```

## Ce qui a changé le 22/11/2026 (audits des 21 et 22/11/2026 ; règle d'or n°333 appliquée, n°369 et n°370 en essai)

La page **exécute** désormais le programme de l'élève (le petit Python `banc-python`, source
`_outils/banc_python/`), au lieu de chercher des motifs dans son texte. Les critères de recette de
l'audit sont recopiés dans la suite, au mot près quand c'était possible :

- « Remplacer seulement les guillemets doubles des chaînes par des apostrophes » → même verdict, 10 / 10 (test 16) ;
- « Remplacer seulement le test strict du seuil supérieur par un test inclusif » → refusé, « 118 km/h · niveau :
  rouge attendu, violette obtenu · gyrophare : arrêté attendu, actif obtenu » (test 16 bis ; l'audit écrivait
  « violet obtenu » : la page dit l'état exact du programme, « violette ») ;
- « Avec la v1 restaurée dans l'éditeur, les sept bonnes réponses théoriques donnent 7/7 » → refusé, « Mes prévisions »
  et « Essais de ma version » séparés, « à exécuter » puis « 3 / 10 » puis « à rejouer » (tests 17 à 17 quater) ;
- « La frontière de mot après 60 accepte aussi le début de 60.5 » → refusé, la valeur lue est 60.5 (test 11 bis) ;
- « Les lignes 6 et 21 sont attendues même si un élève insère un commentaire en tête » → la version 1 est figée (test 8) ;
- « Accepter « 118 ne dépasse pas 118 ; il dépasse 90 » » → validé, sans mot-clé (test 10) ;
- « 10 bonnes réponses sur 10 travaillées ne donnent que 6,7/20 » → « 10 / 10 réussies », « 10 / 30 travaillées », pas de /20 (test 29 bis) ;
- le billet, les documents (algorigramme à 60, plan de tests authentique de la v1, récit fictif), les deux hypothèses (tests 7 bis, 20 quater, 19 sexies) ;
- une écriture Python juste que le banc ne connaissait pas (f-string) obtient 10 / 10 ; une écriture qu'il ne lit pas (liste) est dite « limite du banc, pas forcément une erreur », jamais « SyntaxError » (test 16 quinquies, audit Fable) ;
- le Bonus a désormais sa correction, et son fichier `.py` est le programme de la correction de l'activité 4, qui passe le banc 10 / 10 (test 21 bis).

## Les 56 contrôles (sortie du 22/11/2026)

| # | Contrôle | Résultat |
|---|---|---|
| 1 | chargement, titre « Programmer l'alerte » et les codes 3e_C6.1 / 3e_C6.3 | ✅ |
| 2 | programme d'origine chargé dans l'éditeur, 24 lignes annoncées et comptées | ✅ |
| 3 | coloration syntaxique active : 6 familles de jetons colorées | ✅ |
| 3 bis | séance 1 : « surligner les lignes 6-7 » surligne 2 lignes de la version 1 figée, l'éditeur ne bouge pas | ✅ |
| 4 | le bouton « surligner les lignes 2-4 » surligne exactement 3 ligne(s) | ✅ |
| 4 bis | le bouton « ne plus surligner » rend le programme à sa lecture normale | ✅ |
| 5 | A+ agrandit la police de l'éditeur (14 → 15 px, et le style suit) | ✅ |
| 6 | à l'ouverture, l'éditeur déclare le programme identique à la version 1 d'origine, et la version se dit | ✅ |
| 7 | attendus extraits des CHECKS : 22 égalités, 4 préfixes, 3 nombres, 0 rédaction | ✅ |
| 7 bis | billet sans réponse : « 0 réussie · 0 à revoir · 3 sans réponse », et jamais « rien n'est en place » | ✅ |
| 7 ter | activités 1 et 2 : la version 1 d'origine figée (24 lignes, la ligne 6 lit le vent), au lieu de l'éditeur | ✅ |
| 8 | activité 1 validée 10 / 10 (mesure, paramètre, donnée produite, mesure sans décision, lignes 6 et 21) | ✅ |
| 9 | activité 2 REFUSÉE : « Choix : 3 / 3 corrects » et « Justification : pas encore écrite », deux lignes séparées | ✅ |
| 10 | activité 2 validée avec « 118 ne dépasse pas 118 ; il dépasse 90 » (justification écrite, à relire par le professeur) | ✅ |
| 10 bis | après « Vérifier », le chemin suivi pas à pas : à 118, « 118 > 118 → faux », puis « 118 > 90 → vrai » | ✅ |
| 11 | activité 3 REFUSÉE : les 2 réponses justes, mais le banc lit SEUIL_ORANGE = 50 dans le programme | ✅ |
| 11 bis | SEUIL_ORANGE = 60.5 : refusé, le banc lit la valeur effective (« SEUIL_ORANGE = 60.5 … le club a fixé 60 ») | ✅ |
| 12 | une seule ligne changée : le comparateur annonce 1 ligne ajoutée (+) et 1 retirée (−), pas davantage | ✅ |
| 13 | activité 3 validée une fois la ligne 2 réellement recalibrée à 60 : seuil lu, « Vigilance verte » à 55 km/h | ✅ |
| 14 | activité 4 REFUSÉE sur la version 1 recalibrée : le premier écart est nommé | ✅ |
| 15 | le programme v2 est lu dans la correction publiée par la page (30 lignes) | ✅ |
| 16 | critère de l'audit : la v2 écrite avec des apostrophes obtient 10 / 10, comme avec des guillemets | ✅ |
| 16 bis | critère de l'audit : `>=` au seuil ouragan → refusé, « 118 km/h · niveau : rouge attendu, violette obtenu · gyrophare : arrêté attendu, actif obtenu » | ✅ |
| 16 ter | programme non exécutable : « IndentationError » avec sa ligne, et la version le dit | ✅ |
| 16 quinquies | une f-string juste obtient 10 / 10 ; une liste (hors du banc) donne « Le banc n'a pas pu essayer ton programme », « limite du banc », jamais « SyntaxError » | ✅ |
| 16 quater | activité 4 validée 10 / 10 sur la v2 de la correction, et la version se dit « version 2 » | ✅ |
| 17 | prévisions et diagnostic justes, rien exécuté : REFUSÉE, « Essais de ma version : à exécuter » | ✅ |
| 17 bis | la v1 restaurée exécutée : REFUSÉE, « 3 / 10 vents conformes » | ✅ |
| 17 ter | version modifiée depuis l'essai : « à rejouer », et le journal marque l'ancien essai | ✅ |
| 17 quater | la v2 exécutée sur 10 vents : activité 5 validée, « 10 / 10 … dix cas essayés, pas tous les vents possibles » | ✅ |
| 17 quinquies | le tableau des essais montre 10 vents, la prévision de l'élève et l'obtenu de sa version | ✅ |
| 18 | activité 6 validée 6 / 6 (transfert : lire un programme qu'on n'a pas écrit) | ✅ |
| 19 | toutes les activités sont validées (6 / 6 activités validées) | ✅ |
| 19 bis | les 3 onglets de séance portent leur coche | ✅ |
| 19 ter | réinvestissement : trois explications écrites, sans proposition, chacune avec sa version étayée, correction repliée avec trois phrases de copie, grille à trois critères (n°346, n°356) | ✅ |
| 19 quater | l'état compte ce qui est écrit et coché (2 / 3, 1 / 3) sans rien valider ni noter (n°340) | ✅ |
| 19 quinquies | la bouée : les lignes 4 à 7 écrites s'essaient à 2,0 · 3,0 · 4,0 · 5,0 m, sans note (5,0 m → « Baignade : rouge ») | ✅ |
| 19 sexies | bilan : les DEUX hypothèses de départ reviennent, face à deux champs | ✅ |
| 20 | rechargement : le programme v2 de l'élève est restauré, pas la version d'origine | ✅ |
| 20 bis | rechargement : réponses, validations et journal d'essai restaurés, taille de police comprise | ✅ |
| 20 ter | rechargement : les explications écrites et la case cochée de la grille reviennent | ✅ |
| 20 quater | documents : l'algorigramme (spécification de la v2) teste 60, pas 50 ; le plan de tests de la v1 ne commande aucun gyrophare ; aucun « verte/jaune » ; récit fictif, seuil du club | ✅ |
| 21 | les 14 liens internes existent | ✅ |
| 21 bis | Bonus : le fichier .py donné commence par la simulation, porte le programme de la correction de l'activité 4, et passe le banc 10 / 10 | ✅ |
| 22 | les 5 SVG référencés existent sur le disque | ✅ |
| 23 | hors ligne : aucune ressource distante, aucune modale, aucune erreur JS | ✅ |
| 24 | chargement du QCM, titre « Programmer l'alerte », taille annoncée exacte | ✅ |
| 25 | 30 questions, 2 compétences : C6.1 15 · C6.3 15 | ✅ |
| 26 | bonnes réponses A/B/C/D = 7/8/7/8 (écart max 1) et d[r] vide partout | ✅ |
| 27 | 6 questions illustrées, fichiers présents sur le disque | ✅ |
| 28 | gabarit maison complet : 4 options, 4 réfutations, explication, exemple, erreur, à retenir | ✅ |
| 29 | parcours complet 30 / 30 joué → note 20,0 /20, bilan sur 2 compétences | ✅ |
| 29 bis | parcours « 10 questions » réussi : « 10 / 10 réussies » et « 10 / 30 questions travaillées », aucune note sur 20 (pas de 6,7 /20) | ✅ |
| 30 | la clé localStorage du QCM est écrite | ✅ |
| 31 | le lien de retour vers la séquence existe et pointe sur un fichier réel | ✅ |
| 32 | aucune erreur JS sur le QCM | ✅ |

## Historique

### Ce que la suite éprouvait avant le 22/11/2026

Ce lot ne vérifie pas des menus déroulants : il **lit le programme que l'élève a écrit**.

- **L'activité 3** exige que `SEUIL_ORANGE` ait vraiment été recalibré à 60 **dans le code** —
  répondre juste aux deux questions ne suffit pas, et la page le dit : « je ne trouve pas
  SEUIL_ORANGE = 60 dans CodeLab ».
- **L'activité 4** passe **sept** expressions régulières sur le programme : l'initialisation,
  les deux passages à `True`, le bloc final, son indentation, et l'**absence** de gyrophare
  dans la branche rouge. Elle nomme précisément ce qui manque.

Les deux sont éprouvées dans les deux sens : refus tant que le code n'est pas modifié, message
qui nomme les ajouts manquants, puis validation.

## Ce que la suite ne recopie pas — y compris le programme

Le programme v2 n'est pas écrit dans le test : il est **lu dans la correction que la page
publie elle-même** (`#act4 details.correction pre`), puis collé dans l'éditeur. Si la
correction affichée à l'élève et le vérificateur divergeaient un jour, cette suite le dirait —
ce qu'un programme recopié dans le test ne pourrait pas faire (règle d'or n°268).

Le nombre de contrôles de code n'est pas compté non plus : il est **demandé à la fonction**
(`CHECKS[4]().total`). Le compter à la main dans le source donnait 11 au lieu de 7.

Les réponses sont extraites des `CHECKS` selon cinq conventions : **19 égalités**, **4 préfixes**
(`.indexOf("…") === 0`), **3 nombres**, un objet `att`, et **1 rédaction** jugée par mots-clés —
dont la suite ne prétend montrer que l'ouverture aux conditions déclarées, et dont elle vérifie
surtout le refus (contrôle 9).

## CodeLab Techno et séquence — 26 contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 1 | Chargement, titre « Programmer l'alerte », codes 3e_C6.1 / 3e_C6.3 | ✅ |
| 2 | Programme d'origine chargé, **24 lignes** annoncées et comptées | ✅ |
| 3 | Coloration syntaxique active : 4 familles de jetons colorées | ✅ |
| 4 | Le bouton « surligner les lignes 6-7 » surligne exactement 2 lignes (code et marge) | ✅ |
| 4 bis | « Ne plus surligner » rend le programme à sa lecture normale | ✅ |
| 5 | A+ agrandit la police (14 → 15 px) et le style CSS suit | ✅ |
| 6 | À l'ouverture, l'éditeur déclare le programme identique à l'origine | ✅ |
| 7 | 19 égalités, 4 préfixes, 3 nombres, 1 rédaction extraits des `CHECKS` | ✅ |
| 8 | Activité 1 validée **8 / 8** (classements + deux numéros de ligne relevés) | ✅ |
| 9 | **Activité 2 REFUSÉE** : 3 traces justes, justification trop courte | ✅ |
| 10 | Activité 2 validée **3 / 3** (118 > 118 est faux : l'opérateur est strict) | ✅ |
| 11 | **Activité 3 REFUSÉE** : 2 réponses justes, mais le code n'est pas modifié | ✅ |
| 12 | Une seule ligne changée : le comparateur en annonce **exactement une** | ✅ |
| 13 | Activité 3 validée **3 / 3** une fois la ligne 2 réellement recalibrée | ✅ |
| 14 | **Activité 4 REFUSÉE** sur le v1, et le message **nomme** les ajouts manquants | ✅ |
| 15 | Le programme v2 est lu dans la correction publiée par la page (30 lignes) | ✅ |
| 16 | Activité 4 validée **7 / 7** : les sept contrôles de code passent sur le v2 | ✅ |
| 17 | Activité 5 validée **7 / 7** (jeux d'essai aux frontières + bug diagnostiqué) | ✅ |
| 18 | Activité 6 validée **6 / 6** (lire un programme qu'on n'a pas écrit) | ✅ |
| 19 | Toutes les activités validées (6 / 6) | ✅ |
| 19 bis | Les 3 onglets de séance portent leur coche | ✅ |
| 20 | Rechargement : **le programme de l'élève** est restauré, pas la version d'origine | ✅ |
| 20 bis | Rechargement : réponses, validations et taille de police restaurées | ✅ |
| 21 | Les 6 liens internes existent | ✅ |
| 22 | Les 3 SVG référencés existent sur le disque | ✅ |
| 23 | Hors ligne : aucune ressource distante, aucune modale, aucune erreur JS | ✅ |

## QCM — 9 contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 24 | Chargement, titre, taille annoncée exacte (badge et compteur) | ✅ |
| 25 | **30 questions, 2 compétences à 15 chacune** | ✅ |
| 26 | Bonnes réponses A/B/C/D = **7 / 8 / 7 / 8** et `d[r]` vide partout | ✅ |
| 27 | **6** questions illustrées, fichiers présents sur le disque | ✅ |
| 28 | Gabarit maison complet : 4 options, 4 réfutations, `expl`, `ex`, `err`, `ret` | ✅ |
| 29 | Parcours **30 / 30 joué question par question** → **20,0 / 20**, bilan 2 lignes à 15 / 15 | ✅ |
| 30 | La clé `localStorage` du QCM est écrite | ✅ |
| 31 | Le lien de retour vers la séquence pointe sur un fichier réel | ✅ |
| 32 | Aucune erreur JS sur le QCM | ✅ |

## Contrôles restant manuels

Version 🅰 sur maquette réelle · import d'un fichier `.py` depuis l'appareil (la suite ne
simule pas un choix de fichier système) · mode plein écran sur iOS, où l'API `fullscreen` est
limitée — le bouton reste sans effet sur iPhone, comportement dégradé accepté · relecture
humaine.

## Limites connues

- Tests exécutés uniquement en Chromium/Playwright — aucune compatibilité non testée n'est
  revendiquée.
- Google Fonts inaccessible en sandbox : polices de repli, sans incidence — la suite ne compte
  pas ces requêtes comme des ressources distantes de la page (règle n°40).

## 18/11/2026 — Consignes à la ligne (n°342) et programme sous les yeux

Demande de Pascal pour la séance du matin. Chaque consigne d'activité donne une action par ligne (①, ②… ou a), b)). Le
programme de la station est sous la consigne des activités 1 à 5 ; en mission, il est sur chaque écran de question (à
gauche sur grand écran, au-dessus sur téléphone). Le programme de la bouée (activité 6) est sur ses cinq écrans.

| Contrôle | Sortie | Résultat |
|---|---|---|
| `tests_3e_C6.1-C6.3.mjs` | 0 | 35 / 35 |
| `tests_regle_311_3e_C6.1.mjs` | 0 | 34 / 34 |
| `mode_mission/banc_generique` (la page) | 0 | aucun refus ; l'éditeur présent sur chaque écran de question des activités 1 à 5 |
| `audit_aeration.py --strict` | 0 | aérée |
| `controle_squelette.mjs` | 0 | ouverture et clôture en place |
| `controle_hors_ligne.mjs` | 0 | aucune ressource réseau |
| `controle_regles_visibles.py` | 0 | aucune trace de la fabrique |
| `controle_code_colore.mjs` | 0 | 8 listings en couleurs |
| `controle_schema_sous_les_yeux.py` | 0 | rien à signaler |
| `onglets_clavier.py --etat --strict` | 0 | 0 à poser |
| `impression_papier/banc_papier.py --filtre 3e_C6.1` | 0 | la fiche papier s'imprime ; le programme déplacé n'y apparaît pas en double |

Revue d'écran : captures à 1 280 px (mission, côte à côte) et en page complète, regardées ; rien à reprendre.

## 21/11/2026 — Trois explications écrites après la bouée (règle d'or n°346)

Pilote de la n°346 (« choisir n'est pas expliquer »), choisi sur mesure : de toutes les séquences de 3e, la séance 3
de celle-ci finissait sans aucune réponse écrite (0 zone de texte, 12 groupes de boutons radio). Après les six questions
de la bouée, un bloc « ✍️ Explique comme au brevet » : le programme de la bouée repris sous les yeux (n°331), trois
questions sans propositions (le cas limite 4,0 m justifié ; la ligne 4 modifiée et l'essai qui distingue les deux
versions ; le drapeau orange écrit en `elif` et l'essai qui prouve l'ordre des tests), une version étayée par question
(n°31), une correction repliée avec trois phrases de copie (n°356), une grille à trois critères que l'élève coche. Rien
n'est noté : l'état compte ce qui est écrit et coché (n°340). Le bloc est placé hors de la zone de vérification de
l'activité 6 : écrire une explication ne retire pas sa validation (vu au banc, corrigé avant livraison).

| Contrôle | Sortie | Résultat |
|---|---|---|
| `tests_3e_C6.1-C6.3.mjs` | 0 | 38 / 38 (19 ter, 19 quater, 20 ter nouveaux) |
| `tests_regle_311_3e_C6.1.mjs` | 0 | 34 / 34 |
| `mode_mission/banc_generique.mjs` (la page) | 0 | aucun refus ; pourquoi des erreurs 48 / 48 |
| `eleve_qui_ne_lit_pas.py` (n°360) | 0 | 26 groupes radio, 8 stratégies : aucune activité validée |
| `controle_validations`, `controle_regles_visibles`, `controle_hierarchie`, `controle_debordement`, `controle_consignes_a_la_ligne`, `controle_propositions_indices`, `controle_schema_sous_les_yeux`, `controle_memes_nombres` (dossier), `controle_tactile` | 0 | rien à signaler |
| `controle_code_colore.mjs` (dossier), `controle_hors_ligne.mjs`, `controle_impression.mjs` | 0 | 8 / 8 listings en couleurs ; aucune ressource réseau ; impression lisible |
| lien direct `#ecritBouee` | — | ouvre la séance 3, le bloc visible |

Revue d'écran à 390 px : bloc, version étayée, correction ouverte, grille ; aucun défilement horizontal. Zones de
texte agrandies après le premier tour (le texte de la question 2 était coupé).

**Non vérifié** : la durée réelle du réinvestissement avec l'écrit (annoncé 25 min, à mesurer en classe) ; un essai
avec des élèves.

## 22/11/2026 — Deux aides avant la correction de l'écrit (n°367)

Le bloc « ✍️ Explique comme au brevet » reçoit deux aides repliées avant sa correction : un indice (la ligne qui
s'exécute, le signe qui inclut ou non l'égalité), puis la démarche en trois temps. Banc commun
`_outils/tests_ecrit_brevet.py` : 11 / 11 (il voyait le manque : 10 / 11 avant).

