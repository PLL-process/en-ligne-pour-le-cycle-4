# Rapport d'audit des trois thèmes — 2026-11-22

*Écrit par `_outils/rapport_audit.py` (complet). Il mesure et classe ; il ne corrige rien. Les décisions sont à la fin.*

## Résumé

| | Compte | Priorité |
|---|---|---|
| Contrôles bloquants rouges | 1 (controle_medias.py) | P1 |
| Codes À VÉRIFIER / ABSENT | 4 | P1 |
| Codes COUVERT sans preuve au QCM (0 question marquée, QCM marqué par code) | 6 sur 58 | P1 |
| Codes COUVERT dont la preuve n'est pas mesurable (QCM non marqué par code, ou absent de la racine) | 12 sur 58 | décision |
| ✘ de règles d'or (à cribler) | 3 sur 3 pages | P2 |
| Codes EXISTANT À AMÉLIORER | 3 | P2 |
| Fichiers qu'une régénération changerait | 36 | P2 |
| Anomalies notées dans la matrice | 107 codes | P3 |

## Depuis la semaine dernière

*Rapport précédent : `RAPPORT_AUDIT_2026-11-15.md` (main du 15/11 à 21 h 35 UTC après #718 ; deux post-scriptum jusqu'à #723). Celui-ci : lancé **à la demande de Pascal**, avant l'heure de la tâche du dimanche — `--complet --generateurs`, main du 22/11 à 4 h 53 UTC (0 h 53 Martinique), après #860 (`e0a9fc5`). Chromium 153 ; **`axe-core` 4.10.2 installé dans le bac à sable de la session** (outil de contrôle retenu le 11/11, jamais versionné) : `controle_axe.mjs` a tourné pour la première fois dans un rapport.*

| Ligne du résumé | 15/11 (post-scriptum après #723) | 22/11 | Lecture |
|---|---|---|---|
| Contrôles bloquants rouges | 0 | **1** (`controle_medias.py`) | un manifeste (`3e_C6.2/manifest_entrainement_dnb.json`, #848-849 du 21/11) déclare comme fichier « 12 algorigrammes SVG écrits dans la page » : rien ne manque à l'élève, la promesse est mal rangée — voir le crible |
| Codes À VÉRIFIER / ABSENT | 4 | 4 | décision de Pascal attendue depuis le 07/11 (3e_C7.1, 3e_C7.2, 4e_C8.1, 5e_C7.1) |
| Codes COUVERT sans preuve au QCM | 0 sur 58 | **6 sur 58** | **artefact de mesure** : le QCM hérité `qcm_automatisation_premium.html` de 4e_C4.1, passé au gabarit commun le 19/11, marque ses questions par code ; `rapport_audit.py` en conclut que le lot « marque par code » et compte 0 pour 4e_C4.2, C4.3, C4.5, C4.6 (le QCM du jardin, lui, marque par thème : `EN`, `ID`, `PRO`, `RES`) ; 4e_C4.8 et C4.9 sont prouvés **10 fois chacun** dans `qcm_4e_C4.7-C4.9_sos_serre.html`, mais leur README pointe vers 4e_C4.1 |
| Codes COUVERT dont la preuve n'est pas mesurable | 19 sur 58 | 12 sur 58 | les 7 de 4e_C4.x passés dans la ligne du dessus |
| ✘ de règles d'or | 3 sur 3 pages (n°301, 3e_C9.2) | **3 sur 3 pages (n°23 seulement)** | n°301 réglée par l'exemption « page N sur M » (#725) ; n°300 et ancien gabarit à **zéro** sur les 56 séquences ; **3 dépassements de minutes nouveaux** : 3e_C1.1 (+5), 3e_C2.1 (+13), 4e_C9.1 (+17) |
| Séquences propres sur 56 (`bilan_revision.py`) | 52 | **52** | ce ne sont plus les mêmes : 3e_C1.1, 3e_C2.1, 4e_C9.1 (n°23) et 3e_C8.1 (1 écart d'aération) |
| Codes EXISTANT À AMÉLIORER | 3 | 3 | matrice non relue (5e_C1.3, 4e_C1.4, 3e_C1.5) |
| Fichiers qu'une régénération changerait | 11 | **36** | 20 lexiques, 15 ateliers engendrés (12 des représentations, 3 de planification), 1 page de 3e_C9.2 — **dans les deux sens** : certaines pages sont en retard sur leur source, d'autres portent une retouche que la source n'a pas (crible) |
| Contrôles rouges non bloquants | 4 (`regle4`, `schemas`, `sauvegarde_locale`, `schema_sous_les_yeux`) + `chaine_a_completer` hors rapport | **4** (`competences`, `regle4`, `flux_animes`, `schemas` intermittent) | `sauvegarde_locale`, `schema_sous_les_yeux`, `chaine_a_completer`, `contraste_liens` **verts** ; `axe` vert (409 pages, 109 nœuds connus restent à corriger) ; `indices_qcm` vert (76 banques, 2 301 questions) |
| Anomalies notées dans la matrice | 107 codes | 107 codes | — |

**PR fusionnées dans l'intervalle** (#726 → #860, **134 PR** en sept jours ; règles d'or **n°331 → n°368**, prochain n°369 selon `registre_regles.py`). Les grandes lignes : la veille du 15/11 installée, réécrite (#724) et les chantiers 1 et 5 de l'audit (#725) ; la veille du 16/11 (motion design, vues isométriques `anatomy` du lampadaire et de la station) ; « cinétique » au lieu de « mécanique » et les cinq conversions du programme 2024 par niveau ; l'audit « double regard » devenu méthode (n°337-339) et généralisé : 72 QCM sur 72 aident avant de corriger, chaque séquence a ses trois lignes « Avant de commencer » ; n°340 (une validation dit vrai), n°341 (une question ne souffle pas : banques de 13-20/30 à 4-5), n°342 (consigne à la ligne, mesurée) ; les six QCM de l'ancien format au gabarit commun ; n°343-345 (une question se lit seule) ; n°346-360 dont trois clés de voûte (choisir n'est pas expliquer, un score dit quoi reprendre, la langue du cours) et trois écrits « comme au brevet » ; n°361-368 (audit en 12 axes du TP algorigrammes) ; n°5 amendée (les PR de thème se fusionnent seules, contrôles verts) ; n°364 (ce qui défile est caché, 390 px).

**Ce que ça veut dire.** Les règles d'or mesurées par `verif_regles_audit.py` sont à zéro sauf la durée, et c'est le signe de la semaine : **les ajouts (billets de sortie n°330, écrits « comme au brevet » n°346, enquête facultative) coûtent des minutes**, et trois séquences dépassent maintenant leurs 55 minutes. La dérive des générateurs remonte (11 → 36) parce que plusieurs vagues transversales ont posé à la main, sur des pages engendrées, ce que les générateurs ne savent pas encore (n°364, onglets au clavier, « (volts) ») — le défaut de la licence du 08/11 sous une autre forme. Rien n'empêche un élève de travailler : le seul rouge bloquant est un manifeste mal rangé.

## 1. Couverture (pédagogie) — 114 codes

| Thème | COMPLET ET VALIDABLE | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | EXISTANT À AMÉLIORER | À VÉRIFIER PAR L’ENSEIGNANT |
|---|---|---|---|---|
| 1 | 11 | 17 | 3 | 0 |
| 2 | 16 | 28 | 0 | 0 |
| 3 | 22 | 13 | 0 | 4 |

### Codes non complets

| Code | Statut | Priorité | Ce que dit la matrice |
|---|---|---|---|
| 5e_C1.3 | EXISTANT À AMÉLIORER | P2 | 8 images PNG de 1,1 à 1,9 Mo chacune (≈ 9,3 Mo au total) à compresser (WebP/redimensionnement) ; pas de différenciation ; provenance/licence des 8 images extrai |
| 5e_C7.1 | À VÉRIFIER PAR L’ENSEIGNANT | P1 |  |
| 4e_C1.4 | EXISTANT À AMÉLIORER | P2 | L'activité bonus référence images/tab_key.png et images/indentation_error.png : le premier est en fait dans _ressources-communes/Images/Ressources transversales |
| 4e_C8.1 | À VÉRIFIER PAR L’ENSEIGNANT | P1 |  |
| 3e_C1.5 | EXISTANT À AMÉLIORER | P2 | Pas de différenciation. |
| 3e_C7.1 | À VÉRIFIER PAR L’ENSEIGNANT | P1 |  |
| 3e_C7.2 | À VÉRIFIER PAR L’ENSEIGNANT | P1 | Le dossier ne porte aucune ressource propre : c'est un renvoi. Le statut reste « à vérifier par l'enseignant » parce que le report d'un score évalué dans un AUT |

### Codes COUVERT par mutualisation : la preuve au QCM

Preuve retenue : au moins deux questions du QCM du lot principal marquées du code (`c:"Cx.y"`). Zéro = couvert sans preuve (P1). La mesure ne vaut que pour les QCM qui marquent leurs questions par code (convention des lots du thème 1) ; ailleurs elle dit « non marqué » — ce qui est une décision à prendre, pas un défaut.

| Code | Thème | Lot principal | Questions marquées | Note de la matrice |
|---|---|---|---|---|
| 4e_C4.2 | 2 | 4e_C4.1 | **0 — sans preuve** | 4e_C4.1 |
| 4e_C4.3 | 2 | 4e_C4.1 | **0 — sans preuve** | 4e_C4.1 |
| 4e_C4.5 | 2 | 4e_C4.1 | **0 — sans preuve** | 4e_C4.1 |
| 4e_C4.6 | 2 | 4e_C4.1 | **0 — sans preuve** | 4e_C4.1 |
| 4e_C4.8 | 2 | 4e_C4.1 | **0 — sans preuve** | 4e_C4.7 |
| 4e_C4.9 | 2 | 4e_C4.1 | **0 — sans preuve** | 4e_C4.7 |
| 3e_C7.6 | 3 | C7-imaginer-concevoir-et-realiser-une-ou-des | *pas de QCM à la racine du lot* | atelier CAO — TP nº4 « Le boîtier étanche », mutualisé entre les trois niveaux |
| 3e_C8.3 | 3 | C8-valider-les-solutions-techniques-par-des | *pas de QCM à la racine du lot* |  |
| 4e_C7.2 | 3 | 4e_C7.1 | *QCM non marqué par code* | 4e_C7.1 |
| 4e_C7.6 | 3 | C7-imaginer-concevoir-et-realiser-une-ou-des | *pas de QCM à la racine du lot* | atelier CAO — TP nº2 « Le dé sur sa pointe », mutualisé entre les trois niveaux |
| 4e_C8.2 | 3 | 4e_C8.1 | *QCM non marqué par code* | 4e_C8.1 |
| 4e_C8.3 | 3 | 4e_C8.1 | *QCM non marqué par code* | 4e_C8.1 |
| 5e_C1.6 | 1 | 5e_C1.5 | *QCM non marqué par code* | Croisement déclaré avec 4e_C1.4 (cybersécurité V16) — pointeur manquant. |
| 5e_C7.2 | 3 | C7-imaginer-concevoir-et-realiser-une-ou-des | *pas de QCM à la racine du lot* | atelier CAO — TP nº1 bis « Le dé, en mieux » |
| 5e_C7.6 | 3 | C7-imaginer-concevoir-et-realiser-une-ou-des | *pas de QCM à la racine du lot* | atelier CAO — TP nº1 « Le dé », mutualisé entre les trois niveaux |
| 5e_C8.3 | 3 | C8-valider-les-solutions-techniques-par-des | *pas de QCM à la racine du lot* | 5e_C7.1 |
| 5e_C9.2 | 3 | 5e_C9.1 | *QCM non marqué par code* |  |
| 5e_C9.3 | 3 | 5e_C9.1 | *QCM non marqué par code* |  |
| 3e_C1.2 | 1 | 3e_C1.1 | 7 | 3e_C1.1 |
| 3e_C1.3 | 1 | 3e_C1.5 | 10 | 3e_C1.1 |
| 3e_C1.4 | 1 | 3e_C1.5 | 10 | 3e_C1.1 |
| 3e_C3.2 | 1 | 3e_C3.1 | 7 |  |
| 3e_C3.3 | 1 | 3e_C3.1 | 8 |  |
| 3e_C3.4 | 1 | 3e_C3.1 | 7 |  |
| 3e_C4.2 | 2 | 3e_C4.1 | 15 | 3e_C4.1 |
| 3e_C4.4 | 2 | 3e_C4.3 | 8 | 3e_C4.3 |
| 3e_C4.5 | 2 | 3e_C4.3 | 8 | 3e_C4.3 |
| 3e_C4.6 | 2 | 3e_C4.3 | 8 | 3e_C4.3 |
| 3e_C5.2 | 2 | 3e_C5.1 | 8 | 3e_C5.1 |
| 3e_C5.3 | 2 | 3e_C5.1 | 8 | 3e_C5.1 |
| 3e_C5.4 | 2 | 3e_C5.1 | 8 | 3e_C5.1 |
| 3e_C6.3 | 2 | 3e_C6.1 | 15 | 3e_C6.1 |
| 4e_C1.2 | 1 | 4e_C1.1 | 9 | 4e_C1.1 |
| 4e_C1.3 | 1 | 4e_C1.1 | 12 | 4e_C1.1 |
| 4e_C2.2 | 1 | 4e_C2.1 | 30 |  |
| 4e_C3.2 | 1 | 4e_C3.1 | 10 |  |
| 4e_C3.3 | 1 | 4e_C3.1 | 9 |  |
| 4e_C4.4 | 2 | 4e_C4.1 | 8 | 4e_C4.1 |
| 4e_C5.2 | 2 | 4e_C5.1 | 10 | 4e_C5.1 |
| 4e_C5.3 | 2 | 4e_C5.1 | 10 | 4e_C5.1 |
| 4e_C6.3 | 2 | 4e_C6.1 | 15 | 4e_C6.1 |
| 4e_C9.2 | 3 | 4e_C9.1 | 10 | 4e_C9.1 |
| 4e_C9.3 | 3 | 4e_C9.1 | 10 | 4e_C9.1 |
| 5e_C1.4 | 1 | 5e_C1.3 | 14 | Mutualisé avec 5e_C1.3 (README pointeur en place). |
| 5e_C2.2 | 1 | 5e_C2.1 | 15 |  |
| 5e_C3.2 | 1 | 5e_C3.1 | 7 |  |
| 5e_C3.3 | 1 | 5e_C3.1 | 8 |  |
| 5e_C3.4 | 1 | 5e_C3.1 | 7 |  |
| 5e_C4.2 | 2 | 5e_C4.1 | 5 | 5e_C4.1 |
| 5e_C4.3 | 2 | 5e_C4.1 | 5 | 5e_C4.1 |
| 5e_C4.4 | 2 | 5e_C4.1 | 4 | 5e_C4.1 |
| 5e_C4.5 | 2 | 5e_C4.1 | 4 | 5e_C4.1 |
| 5e_C4.6 | 2 | 5e_C4.1 | 5 | 5e_C4.1 |
| 5e_C4.8 | 2 | 5e_C4.7 | 14 | 5e_C4.7 |
| 5e_C5.2 | 2 | 5e_C5.1 | 10 | 5e_C5.1 |
| 5e_C5.3 | 2 | 5e_C5.1 | 10 | 5e_C5.1 |
| 5e_C6.2 | 2 | 5e_C6.1 | 10 | 5e_C6.1 |
| 5e_C6.3 | 2 | 5e_C6.1 | 10 | 5e_C6.1 |

## 2. Règles d'or (`verif_regles_audit.py`, sortie 0)

| Règle | ✘ | Pages | Thèmes | Exemple de message | Lecture |
|---|---|---|---|---|---|
| n°23 | 3 | 3 | T1:2 T3:1 | 270 min annoncés (+10 de service) pour 275 disponibles — dépassement de 5 min | à lire page par page |

### Par page

| Page | Thème | Règles en ✘ |
|---|---|---|
| 3e_C1.1/sequence_3e_C1.1-C1.4_tsinghua_feux.html | 1 | n°23 |
| 3e_C2.1/sequence_3e_C2_pekin_borne.html | 1 | n°23 |
| 4e_C9.1/sequence_4e_C9_jardin-programme.html | 3 | n°23 |

### Crible du 22/11/2026 (vrai défaut / contrôle périmé) (Fable, après les sorties complètes de `verif_regles_audit.py` et des quatre contrôles rouges relancés à part, et une régénération d'essai des générateurs dans une copie hors git — `git archive`, jamais dans le dépôt —, page par page comparée au dépôt)

*Ce qui tient toujours est reporté du crible du 15/11 ; ce qui est réglé est barré, avec sa PR.*

| Règle | Verdict | Ce qu'il faut faire | Taille |
|---|---|---|---|
| **n°23** (3 pages) | **Vrai défaut, nouveau, et c'est un signal.** 3e_C1.1 : 270 min annoncées + 10 de service pour 275 (+5) ; 3e_C2.1 : 168 + 10 pour 165 (+13) ; 4e_C9.1 : 172 + 10 pour 165 (+17). Les trois ont reçu cette semaine un billet de sortie (n°330), un écrit ou une enquête (4e_C9.1, 19/11 : « l'enquête devient facultative et ferme la séance 2 ») sans que les minutes soient reprises. | Par page : couper une activité, rendre une partie facultative **en le comptant hors durée**, ou une séance de plus (décision de Pascal, comme 4e_C2.1 le 11/11). Et une ligne de méthode : **toute règle qui ajoute un bloc à une séance dit combien de minutes il coûte** (le skill `tache-finale-redigee` ne le dit pas). | 3 pages + 1 ligne de skill |
| ~~**n°300**~~ (3 pages, 57 listes au 15/11) | **Réglé** : 5e_C8.1 (#719), 5e_C8.2 (#720), 5e_C9.1 (#723) — zéro liste à convertir sur les 56 séquences. | — | 0 |
| ~~**n°29 · n°30 · n°34**~~ | **Réglé** : les deux dernières pages de l'ancien gabarit migrées (#719, #720). | — | 0 |
| ~~**n°301**~~ (3e_C9.2 pages 1-3) | **Réglé côté contrôle** (#725) : une page « Page N sur M » avec N < M est sans objet. | — | 0 |

**Hors règles d'or, criblé aussi.**

- **`controle_medias.py` ✘ — P1 par la liste des bloquants, sans effet pour l'élève.** `3e_C6.2/manifest_entrainement_dnb.json` (#848-849, 21/11) range dans la liste des médias une entrée « 12 algorigrammes SVG écrits dans la page par `_outils/dnb_schemas.py` (la page ne charge aucun fichier voisin) » ; le contrôle cherche un fichier de ce nom et ne le trouve pas. La page n'en dépend pas. | Déplacer la phrase dans un champ de note du manifeste (ou la déclarer `"inline": true` si le contrôle l'apprend) ; une PR d'une ligne. **À faire en premier** : c'est le seul rouge bloquant, et un rouge bloquant qui ne bloque rien habitue à ne plus regarder.
- **Codes COUVERT « sans preuve » (6) : contrôle à affiner, et deux README à corriger.** `preuves_couverts()` de `rapport_audit.py` conclut qu'un lot « marque par code » dès qu'**un** QCM de son dossier porte `c:"Cx.y"` ; dans 4e_C4.1, c'est le QCM hérité `qcm_automatisation_premium.html` (au gabarit commun depuis le 19/11 : C4.4, C6.1-C6.3), pas le QCM du lot (`qcm_4e_C4.1-C4.9_jardin_connecte.html`, marqué `EN`, `ID`, `PRO`, `RES`). D'où 0 pour 4e_C4.2, C4.3, C4.5, C4.6 : non mesurable, pas « sans preuve ». **4e_C4.8 et C4.9** : leur README renvoie vers 4e_C4.1, alors que la matrice dit 4e_C4.7, dont le QCM `qcm_4e_C4.7-C4.9_sos_serre.html` marque **10 questions de chacun**. | `rapport_audit.py` : lire le QCM dont le nom porte le code du lot principal ; README de 4e_C4.8 et 4e_C4.9 vers 4e_C4.7. Puis la décision attendue depuis le 07/11 : la convention `c:"Cx.y"` pour le QCM du jardin.
- **`controle_regle4.py` ✘ — 4 pages, deux familles.** (1) `4e_C6.2/tp_algorigrammes_domotique.html`, **sorti des ressources héritées le 20/11** (n°12) : il est maintenant jugé comme une page élève et n'a ni « Prêt·e à t'entraîner », ni Bonus, ni bouton QCM. Vrai défaut, ou TP à déclarer « toléré » comme un atelier sans QCM — à Pascal. (2) Les **3 ateliers de planification** (3e, 4e, 5e) : bouton QCM à 53-54 % de la page. **Nouveau depuis le 15/11** ; ces pages portent aussi un script « onglets-seance » posé à la main par `_outils/onglets_seance.py` que `build_atelier.py` ne connaît pas (voir la dérive) : la régénération effacerait le clavier des onglets. | Pour (2) : apprendre l'onglet clavier et la place du bouton à `build_atelier.py` (n°283), régénérer, rejouer `controle_regle4`. Pour (1) : décision.
- **`controle_competences.py` ✘ (n°314) — `index.html`, ligne 158** : « CRCN 3.4 » écrit deux fois sans son intitulé (« Programmer »), dans l'accès rapide des algorigrammes (21/11). Vrai défaut, une ligne — mais `index.html` est **engendré** (`make_index.py`) : la source est `_outils/index_complements.json`, deux champs `"repere": "CRCN 3.4"`. | « CRCN 3.4 Programmer » dans le JSON, puis `make_index.py` ; une PR d'une ligne.
- **`controle_flux_animes.py` ✘ — `5e_C4.1/Images/chaine_ventilateur_corrige.svg`** : une chaîne aux flux fixes. Dernier commit : la passe « cinétique » du 16/11 (#752), qui a réécrit le fichier sans repasser `animer_flux.py`. | `python3 _outils/animer_flux.py <fichier>`, une PR courte.
- **`controle_schemas.mjs` — intermittent.** Rouge dans le rapport (1), vert relancé seul (0 ✘, 0 schéma) : la fragilité notée le 11/11 (un schéma dessiné par script après chargement) n'est pas réglée. ~~La spirale de Fibonacci~~ — déclarée illustration, hors score (#725). | Attendre le rendu du script avant de mesurer (`waitForFunction`), une PR d'outil.
- **Dérive des générateurs : 11 → 36 fichiers, dans les deux sens** (régénération d'essai comparée page par page) :
  - **Pages en retard sur leur source — la régénération est bonne** : les 12 ateliers des représentations disent « 7 illustrées » quand leur QCM en compte 8 ; `lexique_5e_C2.1.html` affiche encore « Ce qu'on fera l'an prochain — en 4e on décrira… » (contraire à la n°304) alors que son `vocabulaire_*.json` dit « Expliquer sur un autre objet ».
  - **Pages qui portent une retouche que la source n'a pas — la régénération l'effacerait** : `lexique_5e_C5.1.html` « 230 V (volts) » (n°312, posé à la main) ; les 3 ateliers de planification (script des onglets au clavier, 19/11) ; `3e_C9.2/…station_3_interaction.html` (règle n°364, feuille « ce qui défile est caché » posée à la main le 22/11).
  - | Reporter chaque retouche dans sa source (`vocabulaire_*.json`, `build_atelier.py`, `generer_les_quatre_pages.py`), puis régénérer **tout** et vérifier « zéro fichier changé » — exactement la méthode qui a ramené la licence de 70 à 0 le 10/11. Tant que ce n'est pas fait, personne ne régénère ces 36 pages. Une PR d'outils.
- **Registre** : `registre_regles.py` ✅ — 356 numéros, aucun en double, prochain n°369. ~~La collision n°322/323~~ — réglée (#725 : n°333/334). **Au registre, mais pas dans la grille de cadrage** : la n°331 (le schéma sous les yeux) et la n°361 (un contrôle regarde la page ouverte) sont marquées « clé de voûte » sans figurer parmi les sept clés de `cadrage-cles-de-voute` et de `METHODE.md`. À Pascal : neuf clés, ou deux à requalifier.
- **Matrice et couverture** (inchangées depuis le 07/11) : 4 codes à vérifier, 3 codes à améliorer (5e_C1.3, 4e_C1.4, 3e_C1.5), la convention `c:"Cx.y"`. **Quatrième rapport de suite sans décision.**

**Lecture d'ensemble.** La semaine a été productive et propre : zéro liste, zéro ancien gabarit, quatre contrôles rouges du 15/11 passés au vert, `axe` mesuré pour la première fois. Les rouges d'aujourd'hui sont petits et tous datés de la semaine (un manifeste, une ligne de l'index, un SVG, trois ateliers). Deux tendances méritent une règle de méthode plutôt qu'une correction : **ce qu'on ajoute coûte des minutes** (n°23), et **ce qu'on pose à la main sur une page engendrée revient en dérive** (36 fichiers). Ce qui ne bouge pas, c'est la couverture : elle attend Pascal depuis le 07/11.

## 3. Contrôles du site (technique)

| Contrôle | Sortie | Dernière ligne | Priorité si rouge |
|---|---|---|---|
| `controle_liens.py` | ✅ 0 | ✅ aucun lien mort, aucune ancre introuvable dans le périmètre regardé | P1 |
| `controle_regles_visibles.py` | ✅ 0 | ✅ aucune page lue par un élève ne laisse voir la fabrique (règle d'or n°309) | P1 |
| `controle_tactile.py` | ✅ 0 | ✅ chaque champ passe à 16 px au toucher (170 pages, 5 gabarits) ; « Aller au contenu » est le premier lien (23 pages) | P1 |
| `controle_hierarchie.py` | ✅ 0 | 195 page(s) lues · ✅ aucune énumération en ligne, aucun mur sans repère, aucun paragraphe tout en gras, aucune cellule-pavé, aucun item-pavé, aucun pavé hors séquence | P2 |
| `controle_mode_essentiel.py` | ✅ 0 | ✅ en mode essentiel, aucune carte ne se réduit à son titre | P2 |
| `controle_debordement.py` | ✅ 0 | 195 page(s) lues · ✅ aucun tableau de 3 colonnes ou plus sans filet mobile | P2 |
| `controle_competences.py` | ✘ 1 |      « Ici : » (ce que l'élève fait dans la séquence) s'écrit à la main. | P2 |
| `controle_formulations.py` | ✅ 0 | Toute autre façon d'écrire une formulation échappe à ce contrôle. | P2 |
| `controle_impression_papier.py` | ✅ 0 | ✅ chaque séquence s'imprime en fiche papier, à jour | P2 |
| `controle_boutons_vivants.py` | ✅ 0 | ✅ chaque bouton appelle une fonction qui existe dans sa page | P2 |
| `controle_longueurs.py` | ✅ 0 | Aucune banque signalée. | P2 |
| `controle_regle4.py` | ✘ 1 |      le bouton QCM est à 53 % de la page, pas à la fin · 1 lien(s) vers un QCM avant la région finale (à 53 % de la page) | P2 |
| `controle_medias.py` | ✘ 1 |      ne peut pas faire, c'est exister sans que rien ne dise d'où elle vient. | P1 |
| `controle_sigles.py` | ✅ 0 | ✅ chaque sigle garde ses capitales (règle d'or n°313) | P2 |
| `controle_unites.py` | ✅ 0 | ✅ chaque unité est nommée en toutes lettres dans son activité, son tableau, sa question ou son schéma (règle d'or n°312) | P2 |
| `controle_fichiers_telechargeables.py` | ✅ 0 | ✅ chaque fichier nommé dans une séquence se prend d'un clic | P2 |
| `controle_atteignabilite.py` | ✅ 0 | ✅ toute page du dépôt est atteignable depuis l'index, hors tolérées déclarées | P2 |
| `controle_rapports_tests.py` | ✅ 0 | ✅ aucun rapport n'attribue ses résultats à un script absent | P2 |
| `controle_blocs_dessines.py` | ✅ 0 | 490 page(s) lues · 10 dessin(s) en attente · ✅ aucun dessin de blocs hors registre | P2 |
| `controle_schemas.mjs` | ✘ 1 | charge (mesure, hors score) : 115 schéma(s) sur 548 au-dessus du repère (9 entités ou 12 flèches) · médiane 5 entité(s), 43 mot(s) | P2 |
| `controle_sauvegarde_locale.py` | ✅ 0 | ✅ chaque page qui garde les réponses (séquence, atelier, QCM) sait les effacer et prévient du poste partagé | P2 |
| `controle_gestes_outil.py` | ✅ 0 | ✅ chaque encart « les N gestes » nomme l'outil de sa page et se tient à sa porte | P2 |
| `controle_licence.py` | ✅ 0 | ✓ licence : 414 pages portent la mention, LICENSE.md présent | P2 |
| `controle_ordre_propositions.py` | ✅ 0 | ✅ nulle part la bonne réponse ne se devine à sa place | P2 |
| `controle_mode_mission.py` | ✅ 0 | ✅ chaque page qui porte le mode mission porte celui de la source, une fois | P2 |
| `controle_schema_sous_les_yeux.py` | ✅ 0 | 0 ✘ (renvoi explicite vers un schéma qui n'est pas dans le bloc) · 3 ⚠ (schéma nommé sans figure : à juger) · 0 ⚠ S3 (schéma replié) · 1 page(s) concernées · 25 bloc(s) jugés justes (--juges pour les lire) | P2 |
| `controle_flux_animes.py` | ✘ 1 | 686 fichier(s) lus, 65 portent un nom de fonction · ✘ 1 fichier(s) aux flux fixes | P2 |
| `controle_correction_complete.py` | ✅ 0 | ✅ chaque activité qui fait produire avec un outil montre la production complète, et donne son fichier | P2 |
| `controle_correction_illustree.py` | ✅ 0 | ✅ chaque correction d'un dessin attendu montre le dessin | P2 |
| `controle_chaine_a_completer.py` | ✅ 0 | ✅ chaque chaîne à compléter utilise l'outil commun, à jour, et ses étapes sont complètes | P2 |
| `registre_regles.py` | ✅ 0 | ✅ aucun numéro de règle d'or n'est défini deux fois (356 numéros lus, prochain n°369) | P2 |
| `controle_consigne_question.py` | ✅ 0 | ✅ chaque question porte sa consigne | P2 |
| `controle_mouvement.py` | ✅ 0 | 244 page(s) animée(s), 470 animation(s) · ⚠ M1 0 sans repli « moins de mouvement » · ⚠ M2 1 page(s) dont une boucle sans fin ne s'arrête pas · 20 image(s) SVG en boucle | P2 |
| `controle_consignes_a_la_ligne.py` | ✅ 0 | 273 page(s) lues · 390 consigne(s) · N1 étapes numérotées sur une ligne : 0 · N2 actions enchaînées : 5 · N3 actions jointes par « et » (à juger) : 47 · 2 page(s) à reprendre | P2 |
| `controle_squelette.mjs` | ✅ 0 | ✅ chaque séquence montre son ouverture au premier écran et sa clôture à la dernière séance, dans l'ordre | P1 |
| `controle_hors_ligne.mjs` | ✅ 0 | ✅ aucune page ne dépend du réseau pour s'afficher, et chaque activité en ligne le dit | P1 |
| `controle_impression.mjs` | ✅ 0 | ✅ aucune page n'imprime un texte que le papier ne rendra pas | P2 |
| `controle_verrous.mjs` | ✅ 0 | ✅ aucun verrou expérientiel ouvert au chargement | P2 |
| `controle_contraste_liens.mjs` | ✅ 0 | ✅ chaque lien de chaque page se lit sur son fond réel | P2 |
| `controle_code_colore.mjs` | ✅ 0 | ✅ chaque listing de code est en couleurs, comme dans un IDE (132 listing(s), 17 page(s) ; règle d'or n°13) | P2 |
| `controle_indices_qcm.mjs` | ✅ 0 | ✅ aucune banque ne livre sa bonne réponse par un mot absolu ou par l'écho de l'énoncé (76 banque(s), 2301 questions). | P2 |
| `controle_axe.mjs` | ✅ 0 | ✅ aucune page ne porte plus de défauts graves que la référence (409 page(s) ; 109 nœud(s) connus restent à corriger). | P2 |

## 4. Dérive des générateurs

| Générateur | Sortie | Dernière ligne |
|---|---|---|
| `build.py` | ✅ 0 | cahiers : 3 page(s) |
| `build_atelier.py` | ✅ 0 | écrit : atelier_3e_C7.1_planification_taches.html (99932 o) |
| `build_tp.py tp_5e_de_onshape.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_5e_de_onshape.html |
| `build_tp.py tp_5e_de_calottes.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_5e_de_calottes.html |
| `build_tp.py tp_4e_socle_assemblage.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_4e_socle_assemblage.html |
| `build_tp.py tp_3e_boitier_etanche.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_3e_boitier_etanche.html |
| `generer_les_quatre_pages.py` | ✅ 0 | écrit : sequence_3e_C9.2-C8.3_station_4_recette.html 309 Ko |
| `_outils/generer_lexique.py --tous theme-1-objets-systemes-usages-interactions theme-2-structure-fonctionnement-comportement theme-3-creation-conception-realisation-innovations` | ✅ 0 | 5e_C9.1                                                     30 notions → lexique_5e_C9.1.html |

Fichiers qu'une régénération changerait (36) — une retouche faite à la main sur ces pages sera écrasée :

- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/3e/3e_C1.5/lexique_3e_C1.5.html`
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.1/lexique_4e_C1.1.html`
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.4/lexique_4e_C1.4.html`
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.3/lexique_5e_C1.3.html`
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.5/lexique_5e_C1.5.html`
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/3e/3e_C2.1/lexique_3e_C2.1.html`
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/4e/4e_C2.1/lexique_4e_C2.1.html`
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/5e/5e_C2.1/lexique_5e_C2.1.html`
- `theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/4e/4e_C3.1/lexique_4e_C3.1.html`
- `theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/5e/5e_C3.1/lexique_5e_C3.1.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/cas-utilisation-sysml/atelier_3e_cas-utilisation-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/cas-utilisation-sysml/atelier_4e_cas-utilisation-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/cas-utilisation-sysml/atelier_5e_cas-utilisation-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/croquis/atelier_3e_croquis.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/croquis/atelier_4e_croquis.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/exigences-sysml/atelier_3e_exigences-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/exigences-sysml/atelier_4e_exigences-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/fast/atelier_3e_fast.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/fast/atelier_4e_fast.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/fast/atelier_5e_fast.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/interacteurs-pieuvre/atelier_4e_interacteurs-pieuvre.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/interacteurs-pieuvre/atelier_5e_interacteurs-pieuvre.html`
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.1/lexique_3e_C4.1.html`
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/lexique_4e_C4.1.html`
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.7/lexique_4e_C4.7.html`
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/3e/3e_C5.1/lexique_3e_C5.1.html`
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/4e/4e_C5.1/lexique_4e_C5.1.html`
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/5e/5e_C5.1/lexique_5e_C5.1.html`
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/5e/5e_C6.1/lexique_5e_C6.1.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.1/lexique_5e_C7.1.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.4/lexique_5e_C7.4.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.5/lexique_5e_C7.5.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-planification/atelier_3e_C7.1_planification_taches.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-planification/atelier_4e_C7.1_planification_taches.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-planification/atelier_5e_C7.1_planification_taches.html`
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.2/sequence_3e_C9.2-C8.3_station_3_interaction.html`

## 5. Anomalies notées dans la matrice (pratique de classe, médias, différenciation) — P3

| Famille | Codes concernés |
|---|---|
| QCM | 15 |
| différenciation | 3 |
| licence | 3 |
| provenance des médias | 2 |
| manipulation réelle (n°58) | 1 |
| images lourdes | 1 |

<details><summary>Le détail, code par code (107)</summary>

| Code | Statut | Anomalie |
|---|---|---|
| 5e_C1.1 | COMPLET ET VALIDABLE | Aucune manipulation d'un objet réel (règle n°58) — geste manquant identifié et déclaré dans la fiche, la synthèse professeur et le README. La donnée est traitée, jamais produite. |
| 5e_C1.2 | COMPLET ET VALIDABLE | Les quinze mesures sont fournies, non relevées par les élèves. Le prix d'achat est volontairement absent. L'état antérieur — page sans aucun champ de saisie annonçant trois « productions attendues », et définition de la fonction technique confondue avec la fon |
| 5e_C1.3 | EXISTANT À AMÉLIORER | 8 images PNG de 1,1 à 1,9 Mo chacune (≈ 9,3 Mo au total) à compresser (WebP/redimensionnement) ; pas de différenciation ; provenance/licence des 8 images extraites non documentée (pas de SOURCES_MEDIAS.md). |
| 5e_C1.4 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 5e_C1.5 | COMPLET ET VALIDABLE | Aucune publication reelle : le banc simule avec des personnes inventees, et la version A le fait avec le compte du college. Le droit est presente, pas enseigne : droit a l'image, donnees personnelles et licences sont donnes au niveau utile a une decision d'ele |
| 5e_C1.6 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. Le pointeur qui renvoyait ce code vers 4e_C1.4 est archive le 30/08/2026. |
| 5e_C2.1 | COMPLET ET VALIDABLE | CORRIGÉ EN v1.1 : la v1.0 nommait « esthétique » le troisième domaine de conception, alors que le référentiel dit « ou en lien avec des objectifs de développement durable ». Une dimension du programme avait été remplacée par une dimension inventée, et enseigné |
| 5e_C2.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Voir 5e_C2.1 : dossier principal du lot. |
| 5e_C3.1 | COMPLET ET VALIDABLE | Aucune : les 7 règles mécanisables sont au vert. Les données du fichier CSV sont ENTIÈREMENT SIMULÉES et annoncées comme telles dès la situation déclenchante (règle n°27) — aucun véhicule commercialisé n'est décrit. |
| 5e_C3.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Voir 5e_C3.1 : dossier principal du lot. |
| 5e_C3.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Voir 5e_C3.1 : dossier principal du lot. |
| 5e_C3.4 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Voir 5e_C3.1 : dossier principal du lot. |
| 5e_C4.1 | COMPLET ET VALIDABLE | Quatre des huit codes n'ont que 4 questions DANS cette banque (C4.4, C4.5, C4.7, C4.8) : ils sont renforcés ailleurs, et le manifeste nomme la banque de renfort pour chacun (règle n°250). Les quatre autres — C4.1, C4.2, C4.3, C4.6 — n'étaient renforcés nulle p |
| 5e_C4.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 5e_C4.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 5e_C4.4 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 5e_C4.5 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 5e_C4.6 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 5e_C4.7 | COMPLET ET VALIDABLE | Aucune. |
| 5e_C4.8 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 5e_C5.1 | COMPLET ET VALIDABLE | Aucune. Version A en très basse tension uniquement — le secteur est explicitement interdit. |
| 5e_C5.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 5e_C5.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 5e_C6.1 | COMPLET ET VALIDABLE | Aucune. Version A en très basse tension uniquement. |
| 5e_C6.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 5e_C6.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 5e_C7.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Reclassé par contrôle : le dossier ne porte pas séquence. Le geste est porté ailleurs (voir « atelier CAO — TP nº1 bis « Le dé, en mieux » »). Les gestes Onshape (plan décalé, primitive Sphère en mode Retirer) sont décrits d'après la documentation et NON const |
| 5e_C7.3 | COMPLET ET VALIDABLE | Les valeurs sont des ordres de grandeur d'usage pedagogique, tirees de plages courantes en construction — c'est le CLASSEMENT qui doit etre juste, pas la troisieme decimale, et la sequence le dit. Aucune mesure n'est faite par l'eleve : la version A releve les |
| 5e_C7.4 | COMPLET ET VALIDABLE | Aucune mesure reelle : courants constructeur usuels et capacites du commerce, la version A (multimetre en serie) les remplace par des mesures et ce sont elles qui font foi. Le banc ignore l'eclairement interieur, ce qui est exactement le ressort de l'activite  |
| 5e_C7.5 | COMPLET ET VALIDABLE | Aucun assemblage reel : l'etabli simule, et la version A le fait avec la carte, le Base Shield et deux modules Grove — c'est elle qui fait foi. Le programme est donne, charge et lu, jamais modifie : le modifier releve de C6.2. Le catalogue est reduit au strict |
| 5e_C7.6 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Reclassé par contrôle : le dossier ne porte pas séquence. Le geste est porté ailleurs (voir « atelier CAO — TP nº1 « Le dé », mutualisé entre les trois niveaux »). Aucun parcours hors connexion pour le geste de modélisation : Onshape n'a pas de mode hors ligne |
| 5e_C8.1 | COMPLET ET VALIDABLE | Aucune manipulation d'objet réel sur le parcours 🅱 : le geste sur la matière est celui de 5e_C8.2, dont ce lot est la suite. Fatigue et vieillissement hors modèle — déclaré à l'élève dans la synthèse, pas tu. |
| 5e_C8.2 | COMPLET ET VALIDABLE | Aucun essai physique : le banc est une simulation, et la page le dit a l'eleve (une question du QCM porte precisement la-dessus). La version A renvoie au « laboratoire des materiaux » du Reseau National Technologie College (eduscol STI, gratuit, sans compte, C |
| 5e_C8.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. Dossier squelette, README pointeur à écrire. |
| 4e_C1.1 | COMPLET ET VALIDABLE | Aucune donnée n'est produite par les élèves sauf la température. Les chiffres sont datés de juillet 2026 et vieilliront — c'est déclaré, et posé comme un prolongement possible plutôt que comme un défaut. |
| 4e_C1.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 4e_C1.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 4e_C1.4 | EXISTANT À AMÉLIORER | L'activité bonus référence images/tab_key.png et images/indentation_error.png : le premier est en fait dans _ressources-communes/Images/Ressources transversales/touche-tabulation.png, le second n'existe nulle part dans le dépôt (lien cassé) ; pas de grille LSU |
| 4e_C2.1 | COMPLET ET VALIDABLE | Aucune : 8 règles mécanisables au vert. PREMIÈRE APPLICATION des règles n°43 étendue (le Bonus a son corrigé), n°44 (aucun sigle ni bouton nu) et n°45 (l'entraînement s'ouvre sur ce qui a été fait). Le QCM hérité qcm_fonctionnement_objet.html (25 questions, au |
| 4e_C2.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Voir 4e_C2.1 : dossier principal du lot. |
| 4e_C3.1 | COMPLET ET VALIDABLE | Aucune : 7 règles mécanisables au vert. La marche depuis la 5e est explicite et tenue : en 5e le cahier des charges et le protocole sont FOURNIS, en 4e l'élève les ÉCRIT et choisit les appareils de mesure. Données simulées annoncées comme telles, et bilan carb |
| 4e_C3.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Voir 4e_C3.1 : dossier principal du lot. |
| 4e_C3.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Voir 4e_C3.1 : dossier principal du lot. |
| 4e_C4.1 | COMPLET ET VALIDABLE | Aucune sur le lot. L'ancien QCM automatisation conserve son gabarit ${q.img} non résolu (consolidation post-Conseil). |
| 4e_C4.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Reclassé par contrôle : le dossier ne porte pas séquence, QCM au gabarit maison, fiche pédagogique, matrice de couverture, synthèses, rapport de tests. Le geste est porté ailleurs (voir « 4e_C4.1 »). Aucune. Règle n°30 (tableau de bord des tâches) non applicab |
| 4e_C4.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 4e_C4.4 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Reclassé par contrôle : le dossier ne porte pas séquence, fiche pédagogique, matrice de couverture, synthèses, rapport de tests. Le geste est porté ailleurs (voir « 4e_C4.1 »). Aucune. |
| 4e_C4.5 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 4e_C4.6 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 4e_C4.7 | COMPLET ET VALIDABLE | Héritées du QCM XXL existant : licences des images *_hd.jpg non documentées — LICENCE À VÉRIFIER (consolidation post-Conseil) ; doc3_schema_parcours.png (2,6 Mo) à trier. |
| 4e_C4.8 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 4e_C4.9 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 4e_C5.1 | COMPLET ET VALIDABLE | Aucune. Version A en très basse tension uniquement — le secteur est explicitement interdit (y compris au réinvestissement). |
| 4e_C5.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 4e_C5.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 4e_C6.1 | COMPLET ET VALIDABLE | Aucune. Version A en très basse tension uniquement — le secteur est explicitement interdit. |
| 4e_C6.2 | COMPLET ET VALIDABLE | Le programme n'est pas ecrit de zero : il est fourni, remis en ordre puis complete — ecrire un programme entier releve de 4e_C9.3, et la sequence le dit a l'eleve. L'execution est SIMULEE dans l'editeur embarque : elle prouve la logique, pas le montage. Le QCM |
| 4e_C6.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 4e_C7.1 | COMPLET ET VALIDABLE | Le QCM etiquette ses questions par MOT-CLE THEMATIQUE (ORG, SOL, MAT) et non par code de competence : c'est une convention des premiers lots du depot. La matrice porte le lien notion → code, et elle seule. Une harmonisation des etiquettes rendrait le controle  |
| 4e_C7.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Le dossier ne porte aucune ressource propre, et c'est voulu : le geste est travaille dans le lot voisin. Le README precedent disait « Voir le lot 01 dans 4e_C7.1 » — une reference interne que personne ne pouvait resoudre, et sans lien cliquable. |
| 4e_C7.3 | COMPLET ET VALIDABLE | Tout le raisonnement repose sur les durees de vie annoncees, et le bonus demande justement a l'eleve d'ou elles viennent ; la version A les remplace par des garanties de fournisseurs reels. Le banc ne compte que la matiere : ni l'energie de fabrication, ni les |
| 4e_C7.4 | COMPLET ET VALIDABLE | Aucune mesure reelle. Les 5 mA de la carte sobre sont une hypothese d'etude, et la correction dit explicitement qu'une UNO complete ne descend pas sous 30 mA a cause de sa DEL d'alimentation et de son composant USB : c'est la carte qu'il faudrait changer, pas  |
| 4e_C7.5 | COMPLET ET VALIDABLE | Aucun montage reel : l'etabli charge les trois cas, et la version A les prepare sur trois plateaux. Le programme n'est ni ecrit ni modifie — il est correct dans les trois cas, ce qui est justement ce qui rend la recherche du manque interessante. Le quatrieme c |
| 4e_C7.6 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Reclassé par contrôle : le dossier ne porte pas séquence. Le geste est porté ailleurs (voir « atelier CAO — TP nº2 « Le dé sur sa pointe », mutualisé entre les trois niveaux »). Aucun parcours hors connexion pour le geste de modélisation (voir 5e_C7.6). Le lot |
| 4e_C7.7 | COMPLET ET VALIDABLE | Les temps sont des ordres de grandeur d'atelier de college, pas des fiches constructeur : ce qui doit etre vrai est QUEL MOYEN SAIT FAIRE QUOI, pas la seconde pres. Aucune piece n'est reellement produite — la version A lance les deux moyens sur une chute et me |
| 4e_C7.8 | COMPLET ET VALIDABLE | Aucune liaison reelle : le banc simule l'echange, et la version A le fait avec deux cartes et le moniteur serie — ce sont alors les trames observees qui font foi. Le format JSON est impose par le banc ; le choix d'un format est traite en question de QCM et en  |
| 4e_C8.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. Le dossier 4e_C8.2 reste un squelette, ce qui est normal pour un code mutualisé — mais il gagnerait un README pointeur (règle n°205). |
| 4e_C8.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. Dossier squelette, README pointeur à écrire. |
| 4e_C9.1 | COMPLET ET VALIDABLE | L'execution est simulee dans l'editeur embarque : elle prouve la logique, pas le montage. Le lot couvre trois codes a lui seul, ce qui est coherent avec la sequence — six activites, dont trois consacrees a C9.3 — mais laisse peu de place a chacun : 10 question |
| 4e_C9.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Le dossier ne porte aucune ressource propre, et c'est voulu. |
| 4e_C9.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Le dossier ne porte aucune ressource propre, et c'est voulu. |
| 3e_C1.1 | COMPLET ET VALIDABLE | Aucune. |
| 3e_C1.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 3e_C1.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 3e_C1.4 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 3e_C1.5 | EXISTANT À AMÉLIORER | Pas de différenciation. |
| 3e_C2.1 | COMPLET ET VALIDABLE | Aucune : 8 règles mécanisables au vert. AMBIGUÏTÉ DU RÉFÉRENTIEL DÉCLARÉE : « à l'aide de modes de représentation CHOISIS » ne dit pas par qui. La séquence retient « par l'élève » et le dit comme une lecture, à l'élève comme au professeur (règle n°42, troisièm |
| 3e_C3.1 | COMPLET ET VALIDABLE | Aucune : 7 règles mécanisables au vert. CONTRAINTE D'USAGE à respecter : le tableau des six solutions ne se distribue pas en séance 1, sinon l'élève lit une liste au lieu de l'établir et 3e_C3.1 n'est pas couvert. C'est écrit au README, à la fiche et à la synt |
| 3e_C3.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Voir 3e_C3.1 : dossier principal du lot. |
| 3e_C3.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Voir 3e_C3.1 : dossier principal du lot. |
| 3e_C3.4 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Voir 3e_C3.1 : dossier principal du lot. |
| 3e_C4.1 | COMPLET ET VALIDABLE | Aucune. Version A en très basse tension uniquement. |
| 3e_C4.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 3e_C4.3 | COMPLET ET VALIDABLE | Compatibilité LCD Grove ↔ UNO R4 Minima non testée au labo (MATÉRIEL À CONFIRMER — alternative VittaScience prévue). Évaluation sommative laissée à l'enseignant (non publiée, conforme). |
| 3e_C4.4 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 3e_C4.5 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 3e_C4.6 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 3e_C4.7 | COMPLET ET VALIDABLE | Packet Tracer 8.2 CONFIRMÉ en conditions réelles (session du 07/08/2026, atelier 3e_C4.8) — version B débloquée. Évaluation sommative laissée à l'enseignant. |
| 3e_C4.8 | COMPLET ET VALIDABLE | Aucune. Évaluation sommative laissée à l'enseignant. |
| 3e_C5.1 | COMPLET ET VALIDABLE | Multimètres : MATÉRIEL À CONFIRMER (alternative simulation prévue). Imprimante 3D confirmée le 02/09/2026 : FlashForge Adventurer 5M Pro, volume 220 × 220 × 220 mm. Évaluation sommative à l'enseignant. |
| 3e_C5.2 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 3e_C5.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 3e_C5.4 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 3e_C6.1 | COMPLET ET VALIDABLE | Aucune. Exécution Python réelle proposée en bonus uniquement. |
| 3e_C6.2 | COMPLET ET VALIDABLE | Aucune : les 7 règles mécanisables (n°23, 26, 29, 30, 31, 33, 34) sont au vert sur la séquence. Le dossier propose en outre un ENTRAÎNEMENT DNB réécrit au gabarit maison (30 exercices en 4 manches, 90 réfutations de distracteurs, 60 aides, sauvegarde locale, m |
| 3e_C6.3 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Aucune. |
| 3e_C7.2 | À VÉRIFIER PAR L’ENSEIGNANT | Le dossier ne porte aucune ressource propre : c'est un renvoi. Le statut reste « à vérifier par l'enseignant » parce que le report d'un score évalué dans un AUTRE lot est une décision d'enseignant, pas une conséquence mécanique. |
| 3e_C7.3 | COMPLET ET VALIDABLE | Aucune eprouvette n'est cassee : la loi en racine carree est admise, pas mesuree — la version A imprime trois plaques a 1, 2 et 3 mm et les casse sur le banc de flexion de 3e_C8.2. Cette loi est une simplification : paroi plane, meme chargement, meme critere d |
| 3e_C7.4 | COMPLET ET VALIDABLE | Aucune mesure reelle. « Moins d'un dixieme » de recolte solaire sous cyclone est un ordre de grandeur, pas un releve, et la page ne le presente pas autrement. Le vieillissement des accus est traite en un seul chiffre (environ 20 % apres quelques centaines de c |
| 3e_C7.5 | COMPLET ET VALIDABLE | Aucune station reelle : l'etabli simule, la version A utilise le carton complet et la contrainte de courant s'y mesure au multimetre. L'autonomie n'est pas calculee ici — elle l'a ete en 3e_C7.4 ; ce lot montre seulement que le choix du bandeau la remet en cau |
| 3e_C7.6 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Reclassé par contrôle : le dossier ne porte pas séquence. Le geste est porté ailleurs (voir « atelier CAO — TP nº4 « Le boîtier étanche », mutualisé entre les trois niveaux »). Aucun parcours hors connexion pour le geste de modélisation (voir 5e_C7.6). Aucun e |
| 3e_C7.7 | COMPLET ET VALIDABLE | Aucune piece n'est imprimee dans la version B : la version A imprime une EPROUVETTE DE COIN — 15 mm de boitier, 8 min — ou les trois defauts se voient a l'oeil nu, et c'est elle qui fait foi. Aucune simulation n'est lancee : 3e_C8.1 est mobilise, pas reenseign |
| 3e_C7.8 | COMPLET ET VALIDABLE | Aucune liaison reelle : le banc simule. Le routage et l'adressage ne sont ni travailles ni evalues ici — ils le sont par 3e_C4.7 et 3e_C4.8, et le lot s'appuie dessus sans les refaire. La synchronisation des horloges est laissee en defi bonus : la regle de fra |
| 3e_C8.1 | COMPLET ET VALIDABLE | La vitesse du vent n'est pas réglable dans le simulateur : c'est délibéré, et c'est l'objet du réinvestissement (savoir ce qu'un outil ne permet pas). Encastrement supposé parfait ; fatigue hors modèle — l'angle mort est nommé dans la séquence, la synthèse et  |
| 3e_C8.2 | COMPLET ET VALIDABLE | Aucun essai physique : le banc est une simulation, calculee par profils_3e_C8.2.py avec les formules de la poutre encastree et les resistances deja utilisees par le banc de 5e — la page le dit a l'eleve a trois endroits, dont une question de QCM. Le modele a u |
| 3e_C9.1 | COMPLET ET VALIDABLE | Ancienne ressource archivée (règle n°12) avec stub de redirection sur l'URL historique ; qcm_python_variables.html, QCM complémentaire, réécrit au gabarit maison le 19/11/2026 (30 q, l'ancien de 24 archivé) ; l'iframe Vittascience exige une connexion (versions |
| 3e_C9.2 | COMPLET ET VALIDABLE | Planches ArduBlock = reconstitutions schématiques étiquetées (pas de captures : site DuinoEdu inaccessible le 19/08/2026, version 1.7 à revalider en début d'année) ; banc Docker non exécuté en session (réservé au poste enseignant). Aucun corrigé sommatif publi |

</details>

## Veille du 2026-11-22 — skills, plugins, règles d'or et clés de voûte (lecture seule, aucune installation)

*Demande de Pascal (22/11/2026, 0 h 50 Martinique) : « faire cet audit maintenant et rechercher les skills qui me seraient utiles, plugins, règles d'or et clefs de voûte » ; « ils seront à installer automatiquement ensuite ». Méthode : WebSearch (sept requêtes : récupération espacée et exemples résolus, places de marché de plugins pour l'enseignement, FALC et skills en français, accessibilité automatisée, métacognition et explication par l'élève, skills d'enseignants français, double codage et charge cognitive), puis inspection des candidats absents de `SKILLS_AUDIT.md` : dix dépôts clonés en lecture seule (`git clone --depth 1`) dans le bac à sable de la session, SKILL.md, manifestes, crochets (hooks) et licences lus, **aucun script exécuté**, rien installé. « Installer », dans ce dépôt, veut dire **réécrire de zéro** dans `.claude/skills/` et `_outils/` (pratique constante depuis le 23/10 : licences, crochets, réseau) : c'est ce que propose la dernière colonne.*

| Nom | Dépôt | Licence | Ce qu'il fait | Ce qui gêne | Verdict proposé |
|---|---|---|---|---|---|
| **learning-to-learn** (OpenMAIC, 28 skills) | `THU-MAIC/OpenMAIC` — Université Tsinghua, dernier commit 21/11/2026 | MIT | Fait de la métacognition un **objectif parallèle** de la leçon, posé à **quatre endroits** : ouverture (rappeler, prédire avant d'apprendre), concept (le dire avec ses mots, « pourquoi ? »), manipulation (prédire, puis retour ; l'erreur mène à un rattrapage, jamais à une impasse), clôture (ce que j'ai compris, comment je l'ai appris, ce qui reste flou, **quand je le reprendrai**). Deux interdits : les mots de la fabrique (« métacognition », « intention ») ne vont jamais sur la page élève ; les stratégies s'écrivent en gestes (« ne regarde pas, écris d'abord »). | Une plateforme entière (3 388 fichiers de code, 47 crochets) ; texte en chinois ; agents « élèves » simulés. | **Idée à reprendre, réécrite de zéro** → clé de voûte proposée K1 ci-dessous (la reprise espacée) et une ligne dans `cadrage-cles-de-voute`. Les deux interdits sont déjà des règles du dépôt (n°309, n°342). |
| **learn** (agent-tutor-skill) | `Bhala-Srinivash/agent-tutor-skill` — 01/03/2026 | MIT | Boucle expliquer → exemple → vérifier → évaluer → s'exercer ; **la révision commence par faire rappeler, sans réexpliquer** ; maîtrise suivie concept par concept avec répétition espacée (FSRS) ; « ne jamais accepter “j'ai compris” sans preuve ». | Profil de « style d'apprentissage » (mythe écarté par le dépôt, `differenciation-dans-la-page`) ; fichiers dans `~/.learn/` ; tuteur individuel, pas page de classe. | **Idée à reprendre** → K1 (rappeler avant de réexpliquer ; la maîtrise se confirme plus tard). Rien d'autre. |
| **apprendre** (traduction française de `mattpocock/skills/teach`) | `bretzay/skills-fr` — 18/09/2026 | MIT | Sépare **force de restitution** (on retrouve tout de suite, illusion de maîtrise) et **force de stockage** (on retrouve des semaines après) (Bjork) ; trois difficultés désirables : rappel actif, espacement, **entrelacement** (« pour la pratique du savoir-faire seulement »). | Espace de travail personnel sur plusieurs sessions, pour un adulte. | **Idée à reprendre** → règle candidate R3 (le QCM entrelace) et K1. |
| **learning-opportunities** | `DrCatHicks/learning-opportunities` — 19/08/2026 | CC BY 4.0 | Exercices courts proposés après un travail de code ; **pause dure après la question** : rien après, ni indice déguisé, ni exemple de réponse ; « une prédiction fausse est une donnée utile ». | Pour le développeur adulte ; crochets et manifestes de plugin. | **Refusé comme plugin.** L'idée (prédire sans indice) est la n°349, déjà en essai. |
| **claude-teacher-plugin** (15 skills, 5 crochets) | `yarikleto/claude-teacher-plugin` — 15/11/2026 | MIT | Tuteur socratique, base de connaissances de l'élève, quiz espacés. | **Cinq crochets** dont `SessionStart` et `UserPromptSubmit` (scripts bash à chaque session et chaque message) ; « style d'apprentissage » ; tuteur individuel. | **Refusé** (même motif qu'ECC le 23/10 : du code qui tourne à chaque action). |
| **memory-retrieval-learning** | `lyndonkl/claude` (271 skills) — 22/08/2026 | non déclarée | Plan de révision espacée, rappel actif, entrelacement, élaboration. | Pas de licence ; catalogue de 271 skills ; vise l'adulte qui prépare un examen. | **Refusé** (sans licence, rien ne se reprend). |
| **auditing-wcag**, **reviewing-a11y**, **a11y-knowledge** (6 skills) | `masuP9/a11y-specialist-skills` — 11/11/2026 | MIT | Audit WCAG 2.2 AA critère par critère (Passe / Échec / Non testé / Sans objet), avec une liste de vérifications **sans effet de bord** : **refusion (reflow) à 320 px, zoom 200 %, espacement du texte (WCAG 1.4.12), taille des cibles (2.5.8 : 24 × 24 px)**, orientation, limite de temps, et, à part, focus visible et piège clavier. | Lance `npx -y @a11y-skills/audit` (paquet téléchargé et exécuté) et `npx playwright install` ; anglais / japonais. | **Refusé comme plugin ; idée à reprendre, réécrite** → règle candidate R2 et un contrôle Playwright : le dépôt mesure 390 px, le contraste et les champs à 16 px, **pas** le zoom 200 %, l'espacement du texte ni la taille des cibles — trois critères qui comptent pour les élèves dyslexiques et malvoyants. |
| **a11y-playwright-testing** | `fugazi/test-automation-skills-agents` — 16/11/2026 | MIT | Tests axe-core sous Playwright. | Doublon de `controle_axe.mjs` (11/11). | **Refusé**, rien de neuf. |
| **cognitive-load-theory** (skill-graph, 199 skills) | `jacob-balslev/skill-graph` — 16/06/2026 | Apache 2.0 | Charge intrinsèque / extrinsèque / germane, attention partagée, redondance. | Catalogue général, pas pédagogique. | **Pas d'objet** : l'attention partagée est déjà tenue par la n°331 (le schéma sous les yeux) ; c'était une des trois idées du 08/11, réglée par une autre voie. |
| **skills-fr** (20 skills traduites) | `FabriceFx/skills-fr` — 28/10/2026 | non déclarée | Traductions françaises des skills d'Anthropic (`docx`, `pdf`, `frontend-design`, `webapp-testing`…). | Doublons des originaux déjà sur le compte ; licence non déclarée sur le dépôt. | **Refusé.** |

**Déjà jugés, pas rejugés** : `education-agent-skills` et sa copie (dont `self-explanation-prompt-designer`, `dual-coding-designer`, `productive-failure-protocol` vus dans les résultats : bibliothèque jugée les 08, 11 et 15/11 — CC BY-SA, idées seulement), `k12-teacher-skills`, `moodle-mcq`, `plain-language`, `diagram-design-skill` (15/11, installés réécrits par #724), les skills `motion-design` et `anatomy` du compte (16/11). Rien de neuf sur Arduino / Grove / Vittascience, Filius / Packet Tracer, la CAO ou Python au collège : les résultats restent des skills d'ingénierie ou des catalogues généraux.

### Règles d'or et clés de voûte proposées (à la décision de Pascal, en essai si oui — n°147)

*Chacune s'appuie sur une mesure faite ce soir sur `main`, ou sur une étude nommée ; chacune dit comment elle se contrôlera. Aucune n'est inscrite au registre : le rapport propose.*

**K1 — clé de voûte candidate : « Ce qui compte revient. »** Toute séance, à partir de la deuxième, s'ouvre sur **deux ou trois questions de récupération** : sans réexplication d'abord, sans propositions d'abord, sur les acquis 🔑 (n°353) des séances précédentes de l'année ; la maîtrise d'un acquis 🔑 se confirme **à une séance suivante**, jamais le jour où on l'a appris ; le bilan dit **quand** l'élève le reprendra. *Pourquoi* : l'effet de test et l'espacement sont parmi les résultats les plus solides de la psychologie de l'apprentissage (Roediger et Karpicke, 2006 ; Cepeda et al., 2006 ; Adesope et al., 2017, méta-analyse, déjà citée dans `docs/mode-mission/PLAN.md`). *Où le dépôt en est* : le volet « 📖 Rappel » (n°311) **réexplique** ; il ne fait pas récupérer — **mesuré ce soir : sur les 113 séances n°2 et suivantes des 60 pages de séquence, 8 au plus s'ouvrent sur une question de mémoire** (repérage par les mots « billet d'entrée », « de mémoire », « sans regarder », « reprise », dans le début de la séance ; 7 pages) ; le « rappel en début de séance » et la « maîtrise confirmée plus tard » sont **« à concevoir »** dans `PLAN.md` depuis le 11/11. La n°304 (pas de suite d'une année sur l'autre) n'est pas contredite : la reprise se fait **dans l'année**, entre séances et entre séquences d'un même niveau. *Contrôle* : `controle_reprise_espacee.py` — chaque séance ≥ 2 porte un bloc `data-reprise` d'au moins deux questions qui renvoient à un 🔑 d'une séance antérieure. *Skill* : `reprise-espacee` (nouveau), et une huitième ligne dans `cadrage-cles-de-voute`.

**R2 — règle candidate : « Une page se lit à 200 % et avec des lettres espacées. »** Une page reste lisible et utilisable quand le navigateur l'agrandit à 200 % et quand l'élève espace lettres, mots et lignes (hauteur de ligne 1,5 ; paragraphes 2 ; lettres 0,12 em ; mots 0,16 em — WCAG 2.2, critères 1.4.4 et 1.4.12) ; aucune cible tactile sous 24 × 24 px (2.5.8). *Pourquoi* : c'est le réglage des élèves dyslexiques et malvoyants, et le dépôt ne le mesure pas (`balayage-navigateur` l'a toujours écrit « non exécuté »). *Contrôle* : `controle_zoom_espacement.mjs` (Playwright, sans effet de bord : on injecte la feuille d'espacement, on mesure les textes coupés et les débordements, à 1 280 px et 640 px de fenêtre).

**R3 — règle candidate : « Le QCM entrelace ses compétences. »** Mesuré ce soir : **69 QCM sur 70** posent leurs questions **par blocs de compétence** (médiane : 3 changements de compétence pour 30 questions) ; le mode « 10 questions » prend un échantillon régulier, le parcours complet garde l'ordre des blocs. Proposition prudente : un mode **« Entraînement mélangé »** (ordre déterministe qui alterne les compétences, comme `melanger_propositions.py` le fait pour les propositions), **sans** toucher au parcours complet, dont l'ordre est parfois voulu (la question 7 de 3e_C6.1 posée avant le schéma). *Pourquoi* : l'entrelacement aide surtout à **distinguer** des notions voisines (Rohrer et Taylor, 2007 ; méta-analyse Brunmair et Richter, 2019 — effet net en mathématiques et pour des catégories proches, plus faible ailleurs) : c'est exactement le cas des chaînes d'énergie et d'information, ou des formes d'énergie. *Contrôle* : `controle_longueurs.py` ou un nouveau `--entrelacement` qui compte les changements de compétence du mode mélangé.

**R4 — règle candidate : « Le bilan dit ce qui reste flou et quand on le reprend. »** La clôture de chaque séquence demande, en gestes et non en mots de la fabrique : ce que j'ai compris, ce qui reste flou, et la séance où je le reprendrai (lien vers K1). *Pourquoi* : OpenMAIC, et la règle de l'auto-positionnement déjà en place qui ne demande pas le « quand ». *Contrôle* : `verif_regles_audit.py`, un champ du bilan reconnu au libellé. *Peut se fondre dans K1 si Pascal préfère une seule règle.*

**Les trois idées du 08/11, refermées.** (1) Quatre niveaux d'une correction : couverts par la n°347 « un score dit quoi reprendre » et la n°367 « un exercice aide avant de corriger » — **à retirer de la liste d'attente**. (2) Grille de charge cognitive : l'attention partagée est tenue par la n°331, la longueur par `mesurer_charge.mjs` — **à retirer**. (3) Trois niveaux de vocabulaire pour `lexique-sequence` : **toujours ouverte, petite** (une passe « mots de niveau 2 », ceux qu'on oublie de définir).

**Ce que la veille améliorerait, en une phrase par skill du dépôt** : `cadrage-cles-de-voute` — une huitième clé, la reprise espacée (K1) ; `sequence-pedagogique-engageante` — le bloc de reprise en tête de séance ≥ 2, à côté du « 📖 Rappel » qui reste ; `qcm-html-accessible` — le mode « Entraînement mélangé » (R3) ; `controle-qualite-lot` — le zoom 200 % et l'espacement du texte (R2) dans la liste des contrôles ; `lexique-sequence` — la passe des mots de niveau 2.

## 6. Décisions pour Pascal

- [ ] Ordre des vagues : P1 d'abord, puis une règle d'or par vague (la plus nombreuse en premier), puis les P3 ?
- [ ] Pour chaque règle qui tombe sur toute une famille : corriger le contrôle, ou les pages ?
- [ ] Les codes COUVERT sans preuve : ajouter deux questions au QCM du lot principal, ou retirer la mutualisation ?
- [ ] Les QCM non marqués par code : adopter la convention `c:"Cx.y"` partout (règle d'or candidate), pour que la preuve se mesure ?
- [ ] Les codes À VÉRIFIER (thème 3) : qui regarde, et quand ?
- [ ] **`controle_medias.py`** (seul rouge bloquant) : sortir de la liste des médias de `manifest_entrainement_dnb.json` la phrase « 12 algorigrammes SVG écrits dans la page » — une PR d'une ligne, à faire en premier ?
- [ ] **n°23** sur 3e_C1.1 (+5 min), 3e_C2.1 (+13), 4e_C9.1 (+17) : couper, rendre facultatif hors durée, ou une séance de plus — page par page ? Et la ligne de méthode « toute règle qui ajoute un bloc dit combien de minutes il coûte » ?
- [ ] **Petites PR** : « CRCN 3.4 Programmer » dans `_outils/index_complements.json` ; `animer_flux.py` sur `chaine_ventilateur_corrige.svg` ; README de 4e_C4.8 et 4e_C4.9 vers 4e_C4.7 ; `preuves_couverts()` lit le QCM du lot, pas n'importe quel QCM du dossier ?
- [ ] **TP algorigrammes de 4e_C6.2** (sorti des héritées le 20/11) : blocs « Prêt·e » et Bonus, ou TP déclaré toléré dans `controle_regle4.py` ?
- [ ] **Dérive (36 fichiers)** : une PR d'outils qui reporte dans les sources les retouches faites à la main (onglets clavier et bouton QCM dans `build_atelier.py`, n°364 dans `generer_les_quatre_pages.py`, « (volts) » dans le vocabulaire de 5e_C5.1), puis régénère tout jusqu'à « zéro fichier changé » ?
- [ ] **Clés de voûte** : la n°331 et la n°361 sont « clé de voûte » au registre mais absentes de la grille des sept — neuf clés, ou deux à requalifier ? Et les candidates de la veille : **K1 « Ce qui compte revient »** (reprise espacée en tête de séance), **R2** (lisible à 200 % et lettres espacées), **R3** (le QCM entrelace : 69 QCM sur 70 posent leurs questions par blocs), **R4** (le bilan dit ce qui reste flou et quand on le reprend) — lesquelles installer, en essai (n°147) ?
- [ ] Les trois idées du 08/11 : retirer « quatre niveaux d'une correction » et « grille de charge » (couvertes par n°347, n°367, n°331) ; garder les mots de niveau 2 pour `lexique-sequence` ?
