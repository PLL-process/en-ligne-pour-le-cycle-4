# Rapport de tests — lot Shenzhen 5e_C2.1 · C2.2

## 04/11/2026 (nuit) — les mots de référence de la bête à cornes

**Suite** `python3 tests_5e_C2.1-C2.2_shenzhen.py` : **151 / 151** (141 / 141 avant ; 10 tests ajoutés, 3 adaptés).
**Banc n°311** `node tests_regle_311_5e_C2.1.mjs` : **34 / 34**.

| Les tests nouveaux ou adaptés vérifient | |
|---|---|
| a), second temps : un menu dans chacune des quatre cases du gabarit vide (sept mots), posé dans sa forme à 1280 px ; le gabarit au dixième près | ✔ |
| chacun des 24 mots faux a son retour propre à sa case, chaque bon mot le sien (les textes de l'atelier « Le besoin ») ; l'acheteur, le matériau, la fonction technique réfutés ; le miroir ; 4 / 4 | ✔ |
| le dessin de référence (généré par l'atelier) à la fin de a), avant b) : le gabarit, ses quatre mots, « La bête à cornes (méthode APTE) », APTE développé | ✔ |
| l'activité 1 se valide à 15 / 15 (11 / 11 avant : les quatre mots s'ajoutent) | ✔ |
| le QCM : 34 questions (19 pour 5e_C2.1), « Les mots de référence » en quatrième (leurres utilisateur, matériau, fonction, réfutés), nouvelle clé `qcm_5e_C2_shenzhen_34q` | ✔ |

Les retours de c) emploient les mots (« ✔ c'est l'utilisateur : la personne qui emprunte le vélo » ; « ✘ La ville paie
la station, mais ce n'est pas l'utilisatrice : elle n'emprunte pas de vélo ») : le test existant, qui compare chaque
retour affiché à `BAC`, les couvre. **Non testé** : un vrai téléphone, Safari, Firefox, un lecteur d'écran, une
impression réelle.

## 04/11/2026 (soir) — la bête à cornes, exactement le modèle de Pascal

**Suite** `python3 tests_5e_C2.1-C2.2_shenzhen.py` : **141 / 141** (122 / 122 avant ; les tests de la séance 1 suivent la
nouvelle forme : contrôles posés sur le gabarit, retours sous le dessin, miroir). **Banc n°311** : **34 / 34**.

| Les tests nouveaux ou refaits vérifient | |
|---|---|
| Les quatre bêtes à cornes de la séance 1 (a, c, d, le cadre imprimé) sont le gabarit : cadre `50 150 960 570`, les trois ellipses et le rectangle au dixième près, fonds blancs, contours `#1f3864`, corne et flèche `#2e75b6`, la corne tracée après le produit | ✔ |
| a) la question de droite est « Sur quoi agit-il ? » ; à 1280 px, chaque menu est posé à la place de sa question ; le choix s'écrit aussi, en miroir, à cette place dans le dessin | ✔ |
| a) et c) les retours s'écrivent sous le dessin, chacun avec son repère (« ② En haut à droite — ✘ à revoir… », « ① À qui le produit rend-il service ? — … ») ; la case fausse a un contour rouge et une marque ✘ écrite sur le menu, la juste un contour vert et ✔ | ✔ |
| 1280 px : les menus de c) et les champs de d) sont posés dans leurs formes (les quatre coins dans l'ellipse ou le rectangle), en cibles de 44 px ; d) un texte long rapetisse (deux lignes au plus), la forme ne bouge pas | ✔ |
| 390 px : le gabarit entier dans l'écran ; les menus et les champs sous le dessin, chacun avec sa question ; le choix écrit dans sa forme ; aucun défilement de côté | ✔ |
| Impression : a) une ligne pointillée à la place de chaque question et la liste des sept questions ; c) les 13 propositions en cases à cocher, à côté du dessin ; le gabarit en noir (corne et flèche gris foncé), jamais coupé | ✔ |

Le seuil : sous **800 px de dessin**, les contrôles passent sous le dessin (mesuré de 700 à 910 px, chaque choix de chaque
menu, avec sa marque : de 800 px à 910 px, tous tiennent dans leur forme ; à 790 px, « le vélo qu'on emprunte et qu'on
rend » demande trois lignes). La séance 1 s'imprime en **3 pages A4** (4 avant). `controle_schemas` : 0 ✘ sur la page.
**Non testé** : un vrai téléphone, Safari, Firefox, un lecteur d'écran, une impression réelle.

## 04/11/2026 — quatre séances : la bête à cornes en séance 1, « Entoure » à l'écran

**Suite** `python3 tests_5e_C2.1-C2.2_shenzhen.py` (depuis le dossier du lot, sans argument) : **122 / 122**
(50 / 50 avant ; les 50 passent, adaptés aux quatre séances : boutons `data-check` 2 à 4, onglets `s2` à `s4`,
« / 4 activités », QCM à 33 questions). **Banc n°311** `node tests_regle_311_5e_C2.1.mjs` : **34 / 34** (le lien
direct `#a3_1__1` ouvre maintenant `s4`).

| Les 72 tests nouveaux vérifient | |
|---|---|
| Les quatre séances : quatre onglets et panneaux, la question et le lien « 📖 Les mots de cette séance » de chacune, le bouton vers la suivante, la clôture en séance 4, les titres « Activité 1 » à « Activité 4 », le billet en tête de la séance 1, le bandeau des tâches | ✔ |
| Aucun identifiant de champ ancien n'a changé (`be_*`, `hyp1`, `a1_*`, `a2_*`, `a3_*`, bilan, positionnement, bonus) | ✔ |
| Point 1 : la note du billet et la capsule nomment la fonction d'usage (EN : *use function*), avec la définition des ateliers mot pour mot ; `CHECKS[0]` la nomme quand l'élève choisit « à quoi l'objet SERT » | ✔ |
| a) un menu nommé dans chaque case du schéma ; **chacune des 21 réponses possibles** (3 cases × 7 questions) donne son retour propre, écrit dans la case ; le choix s'écrit en entier ; changer de réponse efface le retour périmé ; 2 / 3 puis 3 / 3 | ✔ |
| b) l'exercice « Lire la bête à cornes du vélo-cargo » incrusté entre a) et c), son introduction (le même vélo-cargo, son pieuvre en séance 2), sa vérification « Tout est juste » | ✔ |
| c) **chacune des 13 options** de la station donne son retour (la ville qui paie, le fabricant, le vélo ; l'usager, le trottoir, la pluie ; fonction technique, solution, phrase à sujet, contrainte) ; « verrouiller le vélo » est refusé comme fonction technique et renvoyé à la fonction d'usage ; l'encadré « À retenir » mot pour mot | ✔ |
| d) le miroir (le produit, la case « à qui ? », le but) ; les critères sur six buts : case vide, « Un cartable avec deux bretelles », « Le cartable porte les livres », « Fermer avec une fermeture éclair », le nom de l'objet dans le but, puis un but juste ; la consigne « Dessine-la à main levée sur ton cahier » | ✔ |
| `CHECKS[1]` : refusé sans le vélo-cargo ni le dessin déclaré ; 11 / 11 quand tout est fait ; la progression passe à 1 / 4 avec la coche de la séance 1 | ✔ |
| L'entourage : huit boutons « non entourés », de 44 px au moins ; à 1280 px posés sur le dessin, sans chevauchement ; un clic entoure (`aria-pressed`, le mot « entourée » écrit, l'ellipse), un second le retire ; Espace et Entrée au clavier ; « Vérifier » : huit retours, le vélo refusé, le câble demandé, le trottoir et le sol justes, une marque ✔ ou ✘ sur chaque bouton ; tout juste : 8 / 8 et la phrase « tu viens de tracer sa limite » ; la correction repliée | ✔ |
| Sauvegarde : l'entourage et son retour, les menus, le miroir et la case du cahier reviennent après un rechargement ; une sauvegarde d'avant le 04/11/2026 (trois activités, sans version) voit ses validations passer aux activités 2 à 4 | ✔ |
| 390 px : aucun défilement de côté en séances 1 et 2 ; la bête à cornes garde sa forme ; les noms deviennent une rangée de puces de 44 px sous la figure, et l'ellipse se dessine sur la figure | ✔ |
| Impression : en séance 2, « Entoure uniquement ce qui appartient à la station » et la figure sans boutons ni traits ; en séance 1, le cadre vide du dessin, la liste des sept questions et une ligne dans chaque case de a), les 13 propositions de c) en cases à cocher | ✔ |
| Le lexique : une section par séance jusqu'à `#seance-s4` ; en séance 1, besoin, bête à cornes, fonction d'usage, en français et en anglais ; la définition des ateliers | ✔ |
| Le QCM : en tête, les trois questions de la bête à cornes, chacune avec ses trois réfutations ; la bonne réponse « fonction d'usage » ; la dernière question reste la frontière avec la 4e ; l'en-tête annonce 33 ; la nouvelle clé de sauvegarde | ✔ |
| La synthèse élève : la partie « Pour commencer » (`#partie-0`) et sa carte ; les ancres `#partie-1` à `#partie-6` intactes, sur les mêmes titres | ✔ |

**Contrôles du dépôt sur le lot** : `controle_squelette` (0 défaut D1 à D6), `controle_impression`, `controle_verrous`,
`controle_hors_ligne`, `controle_contraste_liens`, `controle_unites`, `controle_sigles`, `controle_liens`,
`controle_hierarchie`, `controle_regles_visibles`, `controle_medias`, `controle_longueurs` (1 question détachée sur 33),
`controle_impression_papier`, `controle_entete_qcm`, `controle_banque_qcm`, `controle_effectifs_qcm` : verts, comme
avant. `controle_schemas` : 0 ✘ ; 12 ⚠ « serré » au lieu de 10, les deux de plus viennent du dessin « de la bête à
cornes au diagramme pieuvre » du cours de l'atelier « Le besoin », incrusté (même ⚠ que son jumeau de l'atelier
pieuvre, déjà présent). `mesurer_impression.py` sur la synthèse élève : **2 pages** en Inter (95 % et 91 %) et en
Liberation Sans (95 % et 86 %), aucun titre seul. La séance 1 imprimée tient en 4 pages A4, aucun titre seul en bas de
page. `verif_regles_audit.py` : **un ✘ nouveau, voulu** — la n°300 compte les six menus de la bête à cornes (a et c),
posés dans le schéma à la demande de Pascal, dans l'esprit de la n°317 (exception à écrire au journal). La n°23 reste
verte : 191 min annoncées pour 220.

**Non testé** : un vrai téléphone, Safari, Firefox, un lecteur d'écran, une impression réelle (les PDF de Chromium ont
été regardés).


**Date** 8 août 2026 · **Suite** `tests_5e_C2.1-C2.2_shenzhen.py` (Playwright, Chromium 1280×900)
**Résultat** **45 / 45 tests passés** (v1.1)


> **Correction du 31/08/2026 — la suite de ce lot était rouge, et c'est le test qui avait tort.**
> Réexécutée ce jour-là (personne ne l'avait relancée depuis sa livraison), elle échouait sur
> « séquence : hors ligne, aucune ressource distante (n°40) ». La cause n'était pas dans la
> page : le contrôle cherchait la chaîne `http://` dans le HTML sérialisé, où **chaque SVG en
> ligne porte son `xmlns="http://www.w3.org/2000/svg"** — un identifiant d'espace de noms, que
> nul navigateur ne va chercher. Le contrôle regarde désormais ce que la page **irait charger**
> (`src`, `link href`, `object data`, `iframe`, `use`), sans les hyperliens, qui ont le droit
> d'être distants. Vérifié dans les deux sens : la suite passe, et elle redevient rouge si l'on
> injecte une vraie ressource distante dans la page.
>
> ```
> 47 / 47 tests passés
> ```
Ce rapport ne mentionne que des tests **réellement exécutés**. La suite est livrée avec le lot :
elle se relance depuis le dossier du lot par `python3 tests_5e_C2.1-C2.2_shenzhen.py`.

## La séquence (27 tests)

| Ce qui a été vérifié | Résultat |
|---|---|
| Aucune erreur JavaScript au chargement ni pendant le parcours | ✔ |
| Hors ligne intégral : aucune ressource distante (n°40) | ✔ |
| Lien d'accueil résolu sur le fichier réel (n°11) | ✔ |
| Bandeau de tâches affiché et mis à jour par séance (n°30) | ✔ |
| 7 zones de rédaction, 7 versions étayées (n°31) | ✔ |
| Chaque champ porte une étiquette ou un `aria-label` (n°34) | ✔ |
| Les deux figures sont chargées, avec une alternative longue (n°1) | ✔ |
| Le compteur annonce 3 activités et en compte 3 (n°39) | ✔ |
| Billet d'entrée : oriente sans note, ne compte pas dans la progression (n°26) | ✔ |
| Activité 1 : une liste de six **personnes** est refusée | ✔ |
| Activité 1 : validée seulement quand les quatre familles sont nommées | ✔ |
| Activité 2 : le relevé de quatre choix est exigé avant validation | ✔ |
| Activité 2 : un relevé **sans développement durable** est refusé | ✔ |
| Activité 3 : le transfert martiniquais (trois interacteurs) est exigé | ✔ |
| Mode essentiel : bascule et `aria-pressed` cohérent (n°29) | ✔ |
| L'hypothèse de départ est rappelée au bilan | ✔ |
| Sauvegarde locale restaurée après rechargement (textes et progression) | ✔ |
| Blocs « Prêt·e à t'entraîner » et « Bonus » présents, **un seul** bouton QCM (n°4) | ✔ |

Les trois verrous de production ont été testés **dans les deux sens** : refus quand la production
manque ou reste incomplète, validation quand elle est là. C'est le point qui distingue une activité
d'un questionnaire déguisé.

## Le QCM (12 tests)

| Ce qui a été vérifié | Résultat |
|---|---|
| Aucune erreur JavaScript | ✔ |
| 30 questions, 15 par code | ✔ |
| Les trois domaines du code sont ceux du référentiel : ergonomie, sécurité, **développement durable** | ✔ |
| Bonnes réponses réparties A/B/C/D = **8 / 7 / 7 / 8** (graine 502) | ✔ |
| 4 questions illustrées | ✔ |
| Aucune réfutation de distracteur de 20 caractères ou moins ; `d[r]` vide partout | ✔ |
| Chaque question porte explication, exemple, erreur classique et à-retenir | ✔ |
| Parcours complet des 30 questions : les 30 bonnes réponses sont acceptées | ✔ |
| Bilan par compétence affiché avec les deux codes | ✔ |
| Sauvegarde restaurée après rechargement (30 questions validées) | ✔ |
| Une mauvaise réponse affiche la réfutation **du distracteur choisi** | ✔ |

La répartition des bonnes réponses n'a pas été jugée à la lecture, elle a été **comptée** : c'est le
seul moyen de la voir. Le contrôle de longueur des réfutations relève du même principe — trois lots
de suite, des réfutations trop courtes s'étaient glissées là où l'auteur trouvait la réponse fausse
évidente, c'est-à-dire précisément là où l'élève a besoin d'une explication.

## Les synthèses (6 tests)

Élève et professeur : aucune erreur JavaScript, figures référencées au bon nombre, et **tous les
liens de navigation résolus sur des fichiers existants**.

## Ce que ces tests n'auraient pas attrapé

La v1.0 de ce lot enseignait « ergonomie, sécurité, **esthétique** » là où le référentiel dit
« ergonomie et sécurité, ou en lien avec des objectifs de **développement durable** ». Les 43 tests
passaient tous. Aucun ne comparait le contenu enseigné au **texte du référentiel** — ils
vérifiaient la mécanique, la cohérence interne et l'accessibilité, c'est-à-dire tout sauf la seule
chose qui était fausse.

Un test a été ajouté en v1.1 : il lit la bonne réponse de la question « Trois domaines » du QCM et
la compare à la formulation attendue. C'est peu, mais c'est le premier test de ce dépôt qui
contrôle un **contenu institutionnel** plutôt qu'un comportement.

## Ce qui n'a pas été testé

- L'impression A4 (rendu papier) : les feuilles `@media print` sont reprises du gabarit maison, mais
  aucune sortie papier n'a été produite ni relue.
- Le comportement sur un vrai lecteur d'écran : les `aria-label`, `title`/`desc` SVG et le
  signalement non chromatique sont en place et vérifiés dans le DOM, mais aucun test avec NVDA ou
  VoiceOver n'a été mené.
- La séquence sur mobile réel : seule la fenêtre 1280×900 a été utilisée.
