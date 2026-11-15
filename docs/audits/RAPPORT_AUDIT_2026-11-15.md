# Rapport d'audit des trois thèmes — 2026-11-15

*Écrit par `_outils/rapport_audit.py` (complet). Il mesure et classe ; il ne corrige rien. Les décisions sont à la fin.*

## Résumé

| | Compte | Priorité |
|---|---|---|
| Contrôles bloquants rouges | 0 (aucun) | P1 |
| Codes À VÉRIFIER / ABSENT | 4 | P1 |
| Codes COUVERT sans preuve au QCM (0 question marquée, QCM marqué par code) | 0 sur 58 | P1 |
| Codes COUVERT dont la preuve n'est pas mesurable (QCM non marqué par code, ou absent de la racine) | 19 sur 58 | décision |
| ✘ de règles d'or (à cribler) | 12 sur 6 pages | P2 |
| Codes EXISTANT À AMÉLIORER | 3 | P2 |
| Fichiers qu'une régénération changerait | 11 | P2 |
| Anomalies notées dans la matrice | 107 codes | P3 |

## Depuis la semaine dernière

*Rapport précédent : `RAPPORT_AUDIT_2026-11-08.md` (main du 08/11 à 21 h 35 UTC, après #625, `--complet --generateurs`). Celui-ci : `--complet --generateurs`, main du 15/11 à 21 h 35 UTC (17 h 35 Martinique), après #718 (`d03a574`). Les six contrôles Playwright ont tourné (Chromium 153, `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`). Les six contrôles ajoutés à `rapport_audit.py` cette semaine (`gestes_outil`, `licence`, `sauvegarde_locale`, `ordre_propositions`, `mode_mission`, `schema_sous_les_yeux` — 20 + 6 contrôles le 08/11, 26 + 6 ce soir) tournent pour la première fois dans un rapport : leurs rouges ne sont pas forcément nouveaux sur `main` — c'est écrit, ligne par ligne, dans le crible.*

| Ligne du résumé | 08/11 | 15/11 | Lecture |
|---|---|---|---|
| Contrôles bloquants rouges | 0 | 0 | — |
| Codes À VÉRIFIER / ABSENT | 4 | 4 | décision de Pascal toujours attendue (3e_C7.1, 3e_C7.2, 4e_C8.1, 5e_C7.1) ; rien au journal cette semaine |
| Codes COUVERT sans preuve au QCM | 0 sur 58 | 0 sur 58 | — |
| Codes COUVERT dont la preuve n'est pas mesurable | 19 sur 58 | 19 sur 58 | la convention `c:"Cx.y"` n'est toujours pas tranchée |
| ✘ de règles d'or | **91 sur 39 pages** | **12 sur 6 pages** | −79 ✘, −33 pages : la révision des trois thèmes a pris 45 séquences en une semaine (révisions 7 à 51, plus les reprises 4 bis et 5 bis ; #627 → #718), plus la V2 de 4e (#635) |
| dont n°300 (listes déroulantes à convertir) | 38 pages · 1 030 listes | **3 pages · 57 listes** | 5e_C8.1 (17), 5e_C8.2 (16), 5e_C9.1 (24) — les trois prochaines du suivi (52, 53, 54) |
| dont n°29 · 30 · 31 · 34 (ancien gabarit) | 11 pages (+ 2 pages de 3e_C9.2 en n°34 seule) | **2 pages** (5e_C8.1, 5e_C8.2 ; n°29, 30, 34 — la n°31 ne tombe plus) | 4e_C7.3→C7.8 par #635, 4e_C6.2 par #660, 5e_C7.3/C7.4/C7.5 par #715/#716/#718 ; 3e_C9.2 par #702 (`&lt;`/`&gt;` dans le texte de remplacement) |
| dont n°301 | 5 pages | **3 pages** (3e_C9.2 `station_1`, `station_2`, `station_3`) | 3e_C4.3 : faux positif réglé (#633) ; 4e_C6.2 : un bilan clôt la page (#660) ; les trois pages intermédiaires de 3e_C9.2 : inchangées, le contrôle n'a pas été interrogé |
| dont n°23 | 2 pages | **0** | 4e_C2.1 : quatrième séance, décision de Pascal (#643) ; 4e_C7.1 : faux ✘ (les « 15 minutes » du rappel), réglé (#703) |
| Codes EXISTANT À AMÉLIORER | 3 | 3 | 5e_C1.3, 4e_C1.4, 3e_C1.5 ont reçu des questions fermées vérifiées (#681, #684, #685) ; la matrice n'a toujours pas été relue (différenciation, poids des images) |
| Fichiers qu'une régénération changerait | **73** | **11** | −62 : `build.py`, `moteur.py`, `cahiers.py`, `syntheses.py` et `build_atelier.py` posent eux-mêmes la mention n°321 (#637) — le chantier n°1 de la semaine dernière est fait. Restent les **11 lexiques retouchés à la main** (constat du 07/11, inchangés) |
| Contrôles rouges non bloquants | 3 (`regle4`, `schemas`, `contraste_liens`) | **4** (`regle4`, `schemas`, `sauvegarde_locale`, `schema_sous_les_yeux`) | `contraste_liens` **93 → 0** (la mention porte sa feuille, 410 pages, #637 puis #638) ; `sauvegarde_locale` entre dans le rapport avec ses 15 refus **déjà présents au #637** (vérifié sur l'arbre de #637) ; `schema_sous_les_yeux` est la règle n°331 de ce jour (#717), sa vague n'a pas commencé |
| Anomalies notées dans la matrice | 107 codes | 107 codes | — |

**Autres mesures.** Révision des trois thèmes (`bilan_revision.py --md`) : **49 séquences propres sur 56** (0 ✘, 0 menu, 0 écart d'aération) contre **7** la semaine dernière ; restent 5e_C8.1, 5e_C8.2, 5e_C9.1 (ancien gabarit ou listes) et 3e_C1.1, 3e_C3.1 (aération seule : 23 et 18 écarts). Séances au-dessus de 1 200 mots visibles : 69 → 63 (#696). Hors `rapport_audit.py`, relancés à part : `controle_indices_qcm.mjs` ✅ (72 banques, 2 181 questions) ; `controle_chaine_a_completer.py` **✘** (voir le crible) ; `controle_axe.mjs` **non exécuté** (`axe-core` absent de la session, contrôle en panne par construction — règle n°299).

**PR fusionnées dans l'intervalle** (`git log --merges --since=2026-11-08`, **83 lots**, #627 → #718 ; 6 le 10/11, 25 le 11/11, 11 le 12/11, 11 le 14/11, 30 le 15/11) : révision des trois thèmes 4 bis à 51 (#627, #628, #630, #632, #633, #639, #642, #644 → #652, #656, #660, #672, #673, #677 → #681, #684 → #693, #695, #697 → #707, #709 → #711, #713 → #716, #718) · V2 de 4e, famille C7 au gabarit commun (#635) · audit externe, étape 1 (#637 : licence dans les générateurs, n°322 sauvegarde locale, n°323 place des bonnes réponses, contraste de la mention) · découpages de séances (#643 4e_C2.1, #646 3e_C4.3, #686 4e_C1.4, #695 3e_C7.1) · mélange des propositions et son contrôle (#653, #655) · mode mission : pilote, lot 1, partout, d'emblée, pourquoi des erreurs (#657 → #659, #661, #662, #665, #669, #671, #674 → #676, #682) · veille et registre (#663 `controle_indices_qcm`, #666, #667 mesures schémas et voix, #668 adresses de fichiers n°299) · impression compacte et photos de situation (#683, #694) · fiches d'activité repliées (#696) · chaînes sous les yeux, règle n°331 (#708, #712, #717) · divers (#636, #638, #654, #664, #670). Fermées sans fusion : #640 (remplacée).

**Ce que ça veut dire.** La semaine a vidé les règles d'or : 12 ✘ sur 6 pages, dont 8 sur les deux dernières pages de l'ancien gabarit, et 3 que le contrôle n°301 compte par construction. Les deux dettes de la semaine dernière (licence dans les générateurs, lien illisible) sont réglées. Ce qui prime maintenant n'est plus une famille de pages mais **quatre contrôles rouges à cribler** : deux sont des contrôles en retard sur les pages (`regle4` ne lit pas `?codes=`, `schemas` compte une spirale de Fibonacci comme un schéma), deux sont des vrais défauts courts (`sauvegarde_locale` : 8 pages ; `chaine_a_completer` : 5e_C7.4 porte une copie de l'outil différente de la source). La couverture et la matrice n'ont pas bougé depuis trois rapports.

**Post-scriptum (22 h 20 UTC).** Pendant que ce rapport tournait, #719 et #720 ont été fusionnées (révisions 52 et 53 : 5e_C8.1 et 5e_C8.2 au gabarit commun). Rejoués seuls sur `main` après #720 (`4a32a69`), **sans refaire le rapport complet** : `verif_regles_audit.py` → **4 ✘ sur 4 pages** (3 × n°301 sur 3e_C9.2 pages 1-3, 1 × n°300 : les 24 listes de 5e_C9.1) ; l'ancien gabarit (n°29/30/34) est à **zéro page** ; `bilan_revision.py` → **51 séquences propres sur 56** (restent 5e_C9.1, et 3e_C1.1, 3e_C3.1 pour l'aération). Les autres chiffres de ce rapport datent de 21 h 35, après #718 ; les contrôles du site et les générateurs n'ont pas été rejoués après #720.

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
| 3e_C7.6 | 3 | C7-imaginer-concevoir-et-realiser-une-ou-des | *pas de QCM à la racine du lot* | atelier CAO — TP nº4 « Le boîtier étanche », mutualisé entre les trois niveaux |
| 3e_C8.3 | 3 | C8-valider-les-solutions-techniques-par-des | *pas de QCM à la racine du lot* |  |
| 4e_C4.2 | 2 | 4e_C4.1 | *QCM non marqué par code* | 4e_C4.1 |
| 4e_C4.3 | 2 | 4e_C4.1 | *QCM non marqué par code* | 4e_C4.1 |
| 4e_C4.4 | 2 | 4e_C4.1 | *QCM non marqué par code* | 4e_C4.1 |
| 4e_C4.5 | 2 | 4e_C4.1 | *QCM non marqué par code* | 4e_C4.1 |
| 4e_C4.6 | 2 | 4e_C4.1 | *QCM non marqué par code* | 4e_C4.1 |
| 4e_C4.8 | 2 | 4e_C4.1 | *QCM non marqué par code* | 4e_C4.7 |
| 4e_C4.9 | 2 | 4e_C4.1 | *QCM non marqué par code* | 4e_C4.7 |
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
| 4e_C2.2 | 1 | 4e_C2.1 | 15 |  |
| 4e_C3.2 | 1 | 4e_C3.1 | 10 |  |
| 4e_C3.3 | 1 | 4e_C3.1 | 9 |  |
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
| n°300 | 3 | 3 | T3:3 | question dans le flux 17 question(s) posée(s) par une liste déroulante (mat, a1q1, a1q2, a1q3, a2q1, a2q2 …) — le menu n | à lire page par page |
| n°301 | 3 | 3 | T3:3 | aucun bilan : la séquence ne se termine par rien | à lire page par page |
| n°29 | 2 | 2 | T3:2 | pas de bouton « mode essentiel » | à lire page par page |
| n°30 | 2 | 2 | T3:2 | 5 tâches enchaînées sans tableau de bord | à lire page par page |
| n°34 | 2 | 2 | T3:2 | textarea#hyp sans étiquette · textarea#bilan sans étiquette | à lire page par page |

### Par page

| Page | Thème | Règles en ✘ |
|---|---|---|
| 5e_C8.1/sequence_5e_C8.1_patere-du-hall.html | 3 | n°29 n°30 n°34 n°300 |
| 5e_C8.2/sequence_5e_C8.2_patere-du-hall.html | 3 | n°29 n°30 n°34 n°300 |
| 3e_C9.2/sequence_3e_C9.2-C8.3_station_1_besoin-et-algorithme.html | 3 | n°301 |
| 3e_C9.2/sequence_3e_C9.2-C8.3_station_2_programmer.html | 3 | n°301 |
| 3e_C9.2/sequence_3e_C9.2-C8.3_station_3_interaction.html | 3 | n°301 |
| 5e_C9.1/sequence_5e_C9.1-C9.3_boite_etiquetee.html | 3 | n°300 |

### Crible du 15/11/2026 (vrai défaut / contrôle périmé) (Fable, après lecture des messages de `verif_regles_audit.py`, d'une page témoin par règle, des sorties complètes des quatre contrôles rouges relancés à part, et des mêmes contrôles rejoués sur l'arbre de #637 et de #625 dans des copies de travail `git worktree`)

*Ce qui tient toujours est reporté du crible du 08/11 ; ce qui est réglé est barré, avec sa PR.*

| Règle | Verdict | Ce qu'il faut faire | Taille |
|---|---|---|---|
| **n°300** (3 pages, **57 listes**) | **Vrai défaut, en fin de course.** ~~35 des 38 pages~~ — converties dans la passe complète par séquence (révisions 12 à 51, #632 → #718) et par la V2 de 4e (#635) ; ~~3e_C9.2 (62 listes, 4 pages engendrées)~~ — converties dans `generer_les_quatre_pages.py` (#702). Doctrine fixée en route : les menus d'interface (`data-interface`) et les menus de cahier des charges (n°317/318) restent des listes et ne sont plus comptés. Restent **5e_C8.1 (17), 5e_C8.2 (16), 5e_C9.1 (24)** — les numéros 52, 53 et 54 du suivi `docs/revision/SUIVI_REVISION.md`. | Suivre l'ordre du suivi : trois révisions, puis la règle est à zéro sur les 56 séquences. | 3 pages |
| **n°29 · n°30 · n°34** (2 pages, les mêmes) | **Vrai défaut, les deux dernières pages de l'ancien gabarit** : 5e_C8.1 et 5e_C8.2 (ids `a0q1`, `textarea#hyp` et `#bilan` sans étiquette). ~~4e_C7.3→C7.8~~ (#635) ; ~~4e_C6.2~~ (#660) ; ~~5e_C7.3, 5e_C7.4, 5e_C7.5~~ (#715, #716, #718, à leur tour de révision) ; ~~3e_C9.2 en n°34 seule~~ (#702 : `&lt;`/`&gt;` dans le texte de remplacement). La n°31 ne tombe plus sur ces deux pages (1 version étayée pour 4 zones : le contrôle se contente d'une). | `migrer_gabarit_306.py` à leur tour du suivi (52, 53), avec la conversion n°300 dans la même passe — comme 5e_C7.3/4/5 cette semaine. | 2 pages × 3 règles |
| **n°301** (3 pages) | **Trois ✘ comptés par construction, inchangés.** ~~3e_C4.3~~ — faux positif (« ton bilan personnel ci-dessous » lu comme le bilan), réglé par #633 ; ~~4e_C6.2~~ — un bilan clôt la page après le Bonus (#660). Les pages `station_1`, `station_2`, `station_3` de 3e_C9.2 n'ont « aucun bilan » parce que la séquence est éclatée en quatre pages et que le bilan vit en page 4 (#702 l'écrit : « les pages 1 à 3 gardent leur ✘ n°301, comme sur main »). `controle_regle4.py` sait déjà écarter « une étape d'une séquence en plusieurs pages » (3 pages écartées pour cette raison) ; `verif_regles_audit.py` ne le sait pas. | **Décision** : la même exemption dans `verif_regles_audit.py` (une page qui se déclare « page N sur M » avec N < M et renvoie à la page M) — ou un renvoi explicite vers le bilan sur chaque page. Une PR d'outil, 20 lignes. | 1 règle de contrôle |
| ~~**n°23** (2 pages)~~ | **Réglé.** ~~4e_C2.1~~ — quatrième séance « Conclure », décision de Pascal (#643) ; ~~4e_C7.1~~ — faux ✘ : la règle comptait les « 15 minutes au lieu de 5 » du rappel du cahier des charges (#703). | — | 0 |

**Hors règles d'or, criblé aussi.**

- **`controle_regle4.py` ✘ — 21 pages, dont 18 d'une seule famille : contrôle périmé.** Les 18 ateliers des représentations (thème 1, engendrés par `build.py`) ont bien leur bouton unique vers le QCM, mais il porte le code du niveau en paramètre : `<a class="btn qcm" href="qcm_fast.html?codes=3e_C7.2">`. L'expression `LIEN_QCM` du contrôle (`href="[^"]*qcm[^"]*\.html"`) exige que l'adresse se termine par `.html"` et ne voit pas le `?codes=…` ; vérifié : avec une expression qui tolère `?…` ou `#…` après `.html`, **18 ateliers sur 18** retrouvent leur bouton. Ces 21 écarts étaient **déjà là le 08/11** (22 écarts sur l'arbre de #625 — le rapport ne montrait que la dernière ligne, celle de 3e_C9.2) ; ~~la recette de 3e_C9.2 (bouton à 54 %)~~ est réglée (#702). Restent, **à juger**, les 3 copies `atelier_bete_a_cornes.html` rangées dans 4e_C1.3, 3e_C3.1 et 4e_C3.1 (engendrées aussi) : ni bloc « Prêt·e à t'entraîner » ni Bonus pour l'élève — gabarit voulu pour un atelier rangé dans le dossier d'un code, ou oubli du générateur ? | Une ligne dans `controle_regle4.py` ; la question des 3 copies à Pascal.
- **`controle_schemas.mjs` ✘ (1 schéma, 10 ✘, inchangé depuis le 07/11) : contrôle à interroger.** Le schéma est le svg n°1 de `atelier-cao/fiche_arts_tp_4e_socle.html` (#621) : la **spirale de Fibonacci** dessinée par `_generation/spirale_fibonacci.py`, dont les grands nombres « 55 » et « 34 » (la taille des carrés) sont lus comme des « cadres qui se chevauchent » (n°315). C'est une illustration d'arts plastiques, pas un schéma technique : à déclarer hors score (attribut sur le `<svg>`, ou liste des illustrations dans le contrôle) plutôt qu'à redessiner. La fragilité notée le 11/11 (premier schéma de `sequence_4e_C8_jardin-validation.html`, dessiné par script, tantôt 98 points tantôt 0) ne s'est pas manifestée ce soir. La mesure `--charge` dit 107 schémas sur 481 au-dessus du repère (9 entités ou 12 flèches) — mesure, hors score, inchangée (108 le 11/11). | Une PR d'outil courte.
- **`controle_sauvegarde_locale.py` ✘ (règle n°322 du 10/11) — 15 refus sur 8 pages : vrai défaut, pas nouveau.** Rejoué sur l'arbre de #637 : **15 refus déjà**, les mêmes. Le lot A05 a réparé « 10 séquences » et posé 109 notes ; sont restées en dehors : la séquence **3e_C1.5** (stocke sans aucun moyen d'effacer, aucune note poste partagé — révisée depuis par #628 et #685 sans que le contrôle soit relancé), la séquence **4e_C1.4** et son activité bonus 2FA, l'atelier Pix de **4e_C4.1**, le QCM hérité `qcm_algorigrammes_domotique.html` de **4e_C6.2**, et les **3 copies `atelier_bete_a_cornes.html`** (4e_C1.3, 3e_C3.1, 4e_C3.1 — engendrées : à réparer dans `build.py`, n°283). `--corriger` existe. À part : 4 pages ouvrent encore une boîte `confirm()` (`_outils/dnb_gabarit.html`, `entrainement_dnb_algorigrammes.html`, deux QCM) et 73 QCM gardent un score sans note poste partagé (le contrôle l'écrit comme une décision, pas un refus). | Une PR courte (`--corriger` + le générateur pour les 3 copies) ; la note sur les QCM : décision de Pascal (déjà posée le 10/11, sans réponse au journal).
- **`controle_schema_sous_les_yeux.py` ✘ (règle n°331 du 15/11, #717) — 5 ✘, 39 ⚠, 28 pages : vrai défaut, vague annoncée.** Les 5 renvois « ci-dessus » vers un schéma hors du bloc : 3e_C4.3 (deux activités), 5e_C4.1, 3e_C5.1, 3e_C6.1 — exactement la liste que l'entrée du journal de 17 h donne comme première vague. Les 39 ⚠ (schéma nommé sans figure) sont « à juger » un par un. Rien d'autre à cribler : le contrôle est né aujourd'hui, le rapport le lit pour la première fois. | La vague n°331 (déjà décidée : « 1, 2, 3 ok »), puis écrire la règle dans `chaine-energie-fonctionnelle` et `controle-qualite-lot`.
- **`controle_chaine_a_completer.py` ✘ (15/11 ; absent de `rapport_audit.py`, relancé à part) : vrai défaut, un fichier.** `5e_C7.4/sequence_5e_C7.4_indicateur-du-hall.html` porte un bloc de l'outil « chaîne à compléter » **différent de la source** `_outils/chaine_a_completer/` : la révision 50 (#716) a posé l'outil, puis la suite des chaînes (#712, le secteur « vient de la gauche ») a changé la source sans reposer la copie — ou l'inverse. 7 pages portent l'outil, 6 sont identiques à la source. | `poser.py` sur la page, banc, PR courte ; **et ajouter ce contrôle à `CONTROLES_PY` de `rapport_audit.py`**, avec `controle_indices_qcm.mjs` dans `CONTROLES_MJS` (vert ce soir) — `controle_axe.mjs` aussi, qui dira « en panne » tant qu'`axe-core` manque (règle n°299), ce qui est la vérité.
- ~~**`controle_contraste_liens.mjs` ✘ (93 pages)**~~ — **réglé** : la mention de licence porte sa feuille (`.licence-cc a` et `a:visited` en `color:inherit`, souligné, noir sur papier), reposée sur 410 pages (#638, branche `n303-lien-licence-lisible-2`, après un premier essai en ligne dans #637 et la PR #640 fermée) ; 93 → 0, vérifié ce soir (écran, visité, papier).
- ~~**Dérive des générateurs : 62 pages perdraient leur licence**~~ — **réglé** (#637) : `moteur.py`, `cahiers.py`, `build.py`, `syntheses.py` et `build_atelier.py` posent eux-mêmes la mention n°321 ; régénération d'essai de ce soir dans une copie hors git : **73 → 11 fichiers**, et les 11 sont les **lexiques retouchés à la main** (5e_C1.3, 3e_C4.1, 4e_C4.1, 4e_C4.7, 3e_C5.1, 4e_C5.1, 5e_C5.1, 5e_C6.1, 5e_C7.1, 5e_C7.4, 5e_C7.5), constat du 07/11, inchangés depuis trois rapports. Tant qu'ils ne sont pas repris, `generer_lexique.py --tous` les écraserait. | Reporter la retouche dans `vocabulaire_<lot>.json` et régénérer (skill `lexique-sequence`), ou décider que ces 11 pages sortent du générateur. Décision à prendre, puis une PR.
- **Matrice** : 5e_C1.3, 4e_C1.4 et 3e_C1.5 restent « EXISTANT À AMÉLIORER » (différenciation, poids des images, image manquante) ; elles ont reçu cette semaine des questions fermées vérifiées par activité (#681, #684, #685 — « ces questions ne valident pas le CRCN », dit le journal) mais la matrice n'a pas été relue. Inchangé depuis le 08/11.
- **Registre des règles d'or** (vu en lisant le journal, hors mesure) : **les numéros n°322 et n°323 ont été attribués deux fois** — le 10/11 (#637 : n°322 sauvegarde locale, n°323 place des bonnes réponses) puis le 14/11 (audit de 3e_C9.1 : n°322 une réussite affichée prouve la production réelle, n°323 une règle enseignée est juste dans toute sa portée). Les skills `revision-sequence`, `sequence-pedagogique-engageante` et `controle_indices_qcm.mjs` citent l'une ou l'autre. La cause est lisible : le tableau « Registre central » en tête du journal s'arrête au **n°21**, alors que la règle de réservation dit que tout numéro s'y prend. | À trancher par Pascal : renuméroter les deux du 14/11 (n°332, n°333 — les premiers libres après la n°331) et compléter le registre de tête, ou l'inverse.

**Lecture d'ensemble.** 12 ✘ sur 6 pages : les règles d'or se vident par la révision (49 séquences propres sur 56, sept de plus et c'est fini). Le chantier qui prime est **court et technique** : deux contrôles à remettre à jour sur les pages (`regle4` : une ligne ; `schemas` : une illustration à déclarer), deux vrais défauts d'un fichier ou de huit (`chaine_a_completer` sur 5e_C7.4 ; `sauvegarde_locale` sur 8 pages), et trois contrôles de la semaine à inscrire dans `rapport_audit.py` pour que l'audit du 22/11 les lise. Puis la vague n°331 décidée aujourd'hui. La couverture (4 codes à vérifier, 19 preuves non mesurables, 3 codes à améliorer) attend Pascal depuis trois rapports.

## 3. Contrôles du site (technique)

| Contrôle | Sortie | Dernière ligne | Priorité si rouge |
|---|---|---|---|
| `controle_liens.py` | ✅ 0 | ✅ aucun lien mort, aucune ancre introuvable dans le périmètre regardé | P1 |
| `controle_regles_visibles.py` | ✅ 0 | ✅ aucune page lue par un élève ne laisse voir la fabrique (règle d'or n°309) | P1 |
| `controle_tactile.py` | ✅ 0 | ✅ chaque champ passe à 16 px au toucher (171 pages, 5 gabarits) ; « Aller au contenu » est le premier lien (23 pages) | P1 |
| `controle_hierarchie.py` | ✅ 0 | 194 page(s) lues · ✅ aucune énumération en ligne, aucun mur sans repère, aucun paragraphe tout en gras, aucune cellule-pavé, aucun item-pavé, aucun pavé hors séquence | P2 |
| `controle_mode_essentiel.py` | ✅ 0 | ✅ en mode essentiel, aucune carte ne se réduit à son titre | P2 |
| `controle_debordement.py` | ✅ 0 | 194 page(s) lues · ✅ aucun tableau de 3 colonnes ou plus sans filet mobile | P2 |
| `controle_competences.py` | ✅ 0 | ✅ chaque compétence du CRCN se lit en toutes lettres, et chaque étiquette la détaille au survol — intitulé, cadre, « Ici : » (règle d'or n°314) | P2 |
| `controle_formulations.py` | ✅ 0 | Toute autre façon d'écrire une formulation échappe à ce contrôle. | P2 |
| `controle_impression_papier.py` | ✅ 0 | ✅ chaque séquence s'imprime en fiche papier, à jour | P2 |
| `controle_boutons_vivants.py` | ✅ 0 | ✅ chaque bouton appelle une fonction qui existe dans sa page | P2 |
| `controle_longueurs.py` | ✅ 0 | Aucune banque signalée. | P2 |
| `controle_regle4.py` | ✘ 1 |      aucun bouton QCM hors de la barre de navigation | P2 |
| `controle_medias.py` | ✅ 0 | ✅ chaque image du dépôt a une provenance écrite, et aucune n'est promise en vain | P1 |
| `controle_sigles.py` | ✅ 0 | ✅ chaque sigle garde ses capitales (règle d'or n°313) | P2 |
| `controle_unites.py` | ✅ 0 | ✅ chaque unité est nommée en toutes lettres dans son activité, son tableau, sa question ou son schéma (règle d'or n°312) | P2 |
| `controle_fichiers_telechargeables.py` | ✅ 0 | ✅ chaque fichier nommé dans une séquence se prend d'un clic | P2 |
| `controle_atteignabilite.py` | ✅ 0 | ✅ toute page du dépôt est atteignable depuis l'index, hors tolérées déclarées | P2 |
| `controle_rapports_tests.py` | ✅ 0 | ✅ aucun rapport n'attribue ses résultats à un script absent | P2 |
| `controle_blocs_dessines.py` | ✅ 0 | 480 page(s) lues · 10 dessin(s) en attente · ✅ aucun dessin de blocs hors registre | P2 |
| `controle_schemas.mjs` | ✘ 1 | charge (mesure, hors score) : 107 schéma(s) sur 481 au-dessus du repère (9 entités ou 12 flèches) · médiane 5 entité(s), 40 mot(s) | P2 |
| `controle_sauvegarde_locale.py` | ✘ 1 | ✘ une page qui garde les réponses de l'élève doit savoir les effacer et prévenir du poste partagé | P2 |
| `controle_gestes_outil.py` | ✅ 0 | ✅ chaque encart « les N gestes » nomme l'outil de sa page et se tient à sa porte | P2 |
| `controle_licence.py` | ✅ 0 | ✓ licence : 410 pages portent la mention, LICENSE.md présent | P2 |
| `controle_ordre_propositions.py` | ✅ 0 | ✅ nulle part la bonne réponse ne se devine à sa place | P2 |
| `controle_mode_mission.py` | ✅ 0 | ✅ chaque page qui porte le mode mission porte celui de la source, une fois | P2 |
| `controle_schema_sous_les_yeux.py` | ✘ 1 | 5 ✘ (renvoi explicite vers un schéma qui n'est pas dans le bloc) · 39 ⚠ (schéma nommé sans figure : à juger) · 28 page(s) concernées | P2 |
| `controle_squelette.mjs` | ✅ 0 | ✅ chaque séquence montre son ouverture au premier écran et sa clôture à la dernière séance, dans l'ordre | P1 |
| `controle_hors_ligne.mjs` | ✅ 0 | ✅ aucune page ne dépend du réseau pour s'afficher, et chaque activité en ligne le dit | P1 |
| `controle_impression.mjs` | ✅ 0 | ✅ aucune page n'imprime un texte que le papier ne rendra pas | P2 |
| `controle_verrous.mjs` | ✅ 0 | ✅ aucun verrou expérientiel ouvert au chargement | P2 |
| `controle_contraste_liens.mjs` | ✅ 0 | ✅ chaque lien de chaque page se lit sur son fond réel | P2 |
| `controle_code_colore.mjs` | ✅ 0 | ✅ chaque listing de code est en couleurs, comme dans un IDE (121 listing(s), 16 page(s) ; règle d'or n°13) | P2 |

## 4. Dérive des générateurs

| Générateur | Sortie | Dernière ligne |
|---|---|---|
| `build.py` | ✅ 0 | cahiers : 3 page(s) |
| `build_atelier.py` | ✅ 0 | écrit : atelier_3e_C7.1_planification_taches.html (93306 o) |
| `build_tp.py tp_5e_de_onshape.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_5e_de_onshape.html |
| `build_tp.py tp_5e_de_calottes.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_5e_de_calottes.html |
| `build_tp.py tp_4e_socle_assemblage.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_4e_socle_assemblage.html |
| `build_tp.py tp_3e_boitier_etanche.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_3e_boitier_etanche.html |
| `generer_les_quatre_pages.py` | ✅ 0 | écrit : sequence_3e_C9.2-C8.3_station_4_recette.html 264 Ko |
| `_outils/generer_lexique.py --tous theme-1-objets-systemes-usages-interactions theme-2-structure-fonctionnement-comportement theme-3-creation-conception-realisation-innovations` | ✅ 0 | 5e_C9.1                                                     30 notions → lexique_5e_C9.1.html |

Fichiers qu'une régénération changerait (11) — une retouche faite à la main sur ces pages sera écrasée :

- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.3/lexique_5e_C1.3.html`
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

## 5. Anomalies notées dans la matrice (pratique de classe, médias, différenciation) — P3

| Famille | Codes concernés |
|---|---|
| QCM | 16 |
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
| 4e_C4.4 | COUVERT PAR UNE SÉQUENCE MUTUALISÉE | Reclassé par contrôle : le dossier ne porte pas séquence, QCM au gabarit maison (un QCM hérité est présent : qcm_ecall_chaine_information.html), fiche pédagogique, matrice de couverture, synthèses, rapport de tests. Le geste est porté ailleurs (voir « 4e_C4.1  |
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
| 3e_C9.1 | COMPLET ET VALIDABLE | Ancienne ressource archivée (règle n°12) avec stub de redirection sur l'URL historique ; qcm_python_variables.html (24 q) hérité encore en place — remplacement possible par le QCM 30 q ; l'iframe Vittascience exige une connexion (versions 🅲 hors ligne prévues) |
| 3e_C9.2 | COMPLET ET VALIDABLE | Planches ArduBlock = reconstitutions schématiques étiquetées (pas de captures : site DuinoEdu inaccessible le 19/08/2026, version 1.7 à revalider en début d'année) ; banc Docker non exécuté en session (réservé au poste enseignant). Aucun corrigé sommatif publi |

</details>

## Veille du 2026-11-15 — skills et plugins (lecture seule, aucune installation)

*Méthode : WebSearch (dix requêtes : skills pédagogiques Claude Code / claude.ai, langage clair et lisibilité, QCM et évaluation formative, schémas SVG accessibles, impression et typographie, Python et Arduino au collège, enseignement explicite / différenciation / métacognition, accessibilité cognitive, nouveautés de « Claude for Teachers »), puis inspection des candidats absents de `SKILLS_AUDIT.md` : onze dépôts clonés en lecture seule (`git clone --depth 1`) dans le bac à sable de la session, SKILL.md, manifestes, scripts et licences lus, **aucun script exécuté**, rien installé, rien écrit dans le dépôt depuis ces clones. Les verdicts sont des propositions : `SKILLS_AUDIT.md` n'est modifié que sur décision de Pascal.*

| Nom | Dépôt | Licence | Ce qu'il fait | Ce qui gêne | Verdict proposé | Question à Pascal |
|---|---|---|---|---|---|---|
| **k12-teacher-skills** (plugin `k12-education` v0.10.0, 4 skills) | `anthropics/k12-teacher-skills` — Anthropic + Learning Commons, dernier commit 13/10/2026 ; **la source des skills `k12-lesson-planning` et `k12-lesson-differentiation` du compte de Pascal** (gardés le 23/10), et de « Claude for Teachers » | **Apache 2.0** (compatible avec une reprise d'idées ; le texte lui-même est en anglais, cadre des *standards* américains) | Deux skills que le registre ne connaît pas : **`k12-check-for-understanding`** (1 à 3 items formatifs sur UN composant d'apprentissage, **chaque leurre tiré d'une erreur documentée** — l'un d'un prérequis manquant, l'autre d'une confusion du niveau — et un guide professeur qui **route chaque réponse vers l'étape suivante** ; deux « portes » de vérification lues sur le fichier écrit : A — une seule réponse défendable, en écrivant pour chaque option « le meilleur argument pour qu'elle soit juste » ; B — chaque leurre est un endroit où le raisonnement d'un élève atterrit vraiment ; longueur des phrases par cycle, grades 6-8 — nos 6e à 4e — ≈ 15 mots ; figures avec `<title>`/`<desc>`, `role="img"`) et **`k12-lesson-prep`** (préparer un cours existant : faire la tâche clé soi-même, nommer où une réponse presque juste dérape). | Mathématiques seulement pour le CFU ; connecteur Learning Commons (standards des 50 États) ; `.mcp.json` du plugin déclare **neuf serveurs MCP distants tiers** (MagicSchool, Diffit, Canva, Eedi, Brisk…) ; rendu en artefacts « Slides » ou `.docx` par scripts Python (`python-docx`, hors ligne, sans réseau). | **Idée à reprendre, réécrite de zéro** (pas d'installation du plugin : neuf MCP distants, cadre américain) : (a) les deux portes de vérification, écrites sur le fichier produit et non de mémoire, pour `qcm-html-accessible` (aujourd'hui : réfutation de chaque distracteur ; manque le test « quel est le meilleur argument POUR ce leurre ? », qui attrape les deux réponses justes — vu cette semaine sur 5e_C7.3 et 3e_C7.8) ; (b) « chaque leurre vient d'une erreur documentée, et sa correction nomme l'étape suivante » pour le **pourquoi des erreurs** du mode mission (`enrichir.py`) ; (c) la pratique de `k12-lesson-prep` — faire la tâche clé avant de juger la page — est déjà « lire comme un élève » de `revision-sequence`, rien à prendre. | Les deux skills `k12-*` du compte sont-ils à jour de cette version (13/10, « rendu en artefacts ») ? Faut-il noter dans `SKILLS_AUDIT.md` que ce dépôt est leur source ? |
| **moodle-mcq** v3.1.0 | `danielcregg/moodle-mcq` — un enseignant du supérieur, 24/03/2026 | MIT | Générer et relire des questions Moodle (GIFT, XML, Aiken) ; **répartition des longueurs 15/15/70** (la bonne réponse est la plus courte dans ~15 % des questions, la plus longue dans ~15 %, au milieu sinon, mesurée en caractères sans balises, avec un tableau de contrôle), énoncés autoportants (jamais « comme vu en cours »), **balise `<name>` obligatoire** à l'import Moodle. Pas de script, pas de réseau. | Cadre universitaire (Java), questions « 10 à 15 » (le dépôt en fait 30 fixes), taux de réussite visés par difficulté. | **Idée à reprendre, réécrite de zéro** : la cible 15/15/70 donne un **chiffre** à la règle n°323 « ne se devine pas à ses mots » (candidate du 11/11) que le dépôt mesure déjà à la main (« la bonne réponse était 32 fois sur 40 la plus longue », #690) — `controle_ordre_propositions.py` pourrait compter la place par longueur comme il compte la place par position. **Vérifié en passant** sur l'export Éléa du dépôt (#615) : `export_moodle_xml.mjs` écrit bien `<name><text>…` sur les 2 181 questions des quatre fichiers ; rien à corriger. | Faut-il une mesure « place par longueur » dans `controle_ordre_propositions.py` (seuil : la bonne réponse la plus longue dans plus de 30 % des questions = refus) ? |
| **plain-language** (Federal Plain Language Guidelines + ISO 24495-1) | `jgsystemsconsulting/plain-language` — 13/10/2026 | MIT (sources : domaine public US) | Classer chaque paragraphe **procédure** (impératif, **20 mots** par phrase) ou **information** (voix active, **25 mots**), condition avant la commande, **six phrases par paragraphe au plus**, un **vérificateur mécanique** `plain_check.py` (stdlib, sans réseau : longueur des phrases, passif, verbes cachés, liste de mots à surveiller, indice Flesch-Kincaid). | Anglais (l'indice de lisibilité et la liste de mots ne valent pas en français) ; renvoie à un `~/.zcode/scripts/prose_check.py` extérieur. | **Idée à reprendre, réécrite de zéro** — c'est la suite de `francais-simple` (08/11), qui avait déjà donné 20/25 mots et la condition avant l'action à `texte-clair-et-aere` : ce qui manque est **la mesure**. `audit_aeration.py` compte des mots par pavé ; il pourrait compter **les phrases par paragraphe (seuil 4, proposé le 08/11, sans réponse) et les mots par phrase (20 consigne / 25 explication)**. | Même question que le 08/11 : `audit_aeration.py` doit-il compter aussi les phrases ? |
| **diagram-design-skill** v2.6 (dérivé) | `luffy666code/diagram-design-skill` — 17/09/2026, dérivé de `cathrynlavery/diagram-design` (jugé le 11/11) | MIT | Même squelette que l'original, mais **hors ligne** (polices locales, aucune Google Fonts : la n°305 est respectée ici), 40 types, et deux scripts non lancés : `self_check.py` (contrat du SVG accessible : `role="img"`, `<title>`/`<desc>`, ids préfixés, fichier unique sans ressource distante) et `verify-geometry.py` (une étiquette de flèche ne touche jamais son trait : **6 à 10 px d'écart**, et son fond opaque ne chevauche aucun cadre dessiné après elle). | Étiquettes à **7-9 px** (le dépôt exige 14 px à 390 px, n°325) ; charte « éditoriale » étrangère ; 5 800 mots présentés au modèle. | **Refusé comme skill ; une idée à reprendre, réécrite** : la mesure « étiquette de flèche à moins de 6 px de son trait, ou dont le fond chevauche un cadre » pour `controle_schemas.mjs`, qui voit les cadres qui se touchent et les textes qui débordent mais pas l'étiquette posée SUR la flèche. | — |
| **test-skill** | `vladmoseev/test-skill` — 22/09/2026 | MIT | Transformer une pile de questions ouvertes en questionnaire HTML autonome avec brouillon `localStorage` ; note : sous `file://`, certains navigateurs lèvent `SecurityError` sur `localStorage`. | Hors sujet (questionnaires de décision pour l'agent) ; `serve.py` local. | **Hors sujet, refusé.** Vérifié en passant : les pages du dépôt enveloppent déjà chaque accès `localStorage` dans `try/catch` avec un message « sauvegarde impossible » (5e_C4.1, trois fonctions). Rien à prendre. | — |
| **typography-check** | `thomasguillot/typography-skills` — 06/10/2026 | MIT | Audit typographique **mesuré** par le médium (web, impression, PDF) : `extract-web-type.js` sous Playwright (police rendue vs déclarée, caractères par ligne, contraste **opacité comprise**), `inspect-pdf.py`, table « habitudes du web fausses à l'impression ». | Anglais ; un site Astro à côté ; charte de typographe (45-75 caractères par ligne — `practical-typography` l'a déjà donné le 08/11). | **Refusé.** Déjà couvert : `controle_contraste_liens` (fond réel, visité, papier), `controle_impression.mjs`, fiche papier, n°325/327. Une seule idée mince : le contraste **avec l'opacité** appliquée, que la n°327 (14/11) demande déjà « contre le fond affiché ». | — |
| **plain-language-iso-24495** | `nikdumroese/plain-language-skill` — 30/07/2026 | MIT | Les quatre principes ISO (pertinent, trouvable, compréhensible, utilisable) pour des documents d'entreprise (RFC, PRD, postmortem). | Public adulte, documents de travail ; rien pour l'élève. | **Hors cible, refusé.** | — |
| **clarity** v0.2.1 | `addyosmani/clarity` — 04/09/2026 | MIT | Prose « non IA » pour essais, articles, documentation ; `prose_stats.py` ; un éditeur web Netlify à côté. | Même famille que `refine-prose` (jugé le 08/11) ; anglais ; vise l'auteur adulte, pas le lecteur de 12 ans. | **Refusé.** Rien que `texte-clair-et-aere` et `synthese-vulgarisee` ne fassent déjà pour l'élève. | — |
| **skills-education** (30 skills) | `poorvith-mp/skills-education` — 02/10/2026 | MIT | Skills pour l'étudiant qui révise seul (fiches, quiz à partir de ses notes, plan de révision, citations). | Public lycée-université ; le quiz est générique, sans leurre documenté ni correction élaborée. | **Hors cible, refusé.** | — |
| **quiz-maker** | `OneWave-AI/claude-skills` (234 skills) — 19/10/2026 | MIT | 181 mots : « QCM, vrai/faux, textes à trous, appariement, leurres plausibles ». | Maigre ; catalogue de 234 skills présenté au modèle. | **Refusé.** Rien de neuf face à `qcm-html-accessible`. | — |
| **claude-education-skills** (111 skills) | `JoyTim-777/claude-education-skills` — copie du 24/04/2026 de la bibliothèque de Gareth Manning (v3.1 : 165 skills, jugée les 08 et 11/11) | CC BY-SA 4.0 (celle de l'original) | La même bibliothèque, six mois plus tôt. | Copie non mise à jour ; licence BY-SA incompatible avec la n°321. | **Pas rejugé** : même verdict que l'original (idées seulement, réécrites). | — |

**Déjà jugés, pas rejugés** : `education-agent-skills` (Gareth Manning), `inclusive-design-skills`, `diagram-design` (cathrynlavery), `francais-simple`, `refine-prose`, `clean-copy`, `assessment-design`, `school-skills`, `style-prose`, `study-guide-maker`, `print-styles`, `ai-edu-skills-FR`, `dsfr-skill`, `animated-explainer-skills`, `webapp-testing`, `k12-lesson-planning`, `k12-lesson-differentiation` (08 et 11/11 ; 23/10). Rien de nouveau sur Filius, Packet Tracer, Vittascience, Grove, Tinkercad ou la CAO au collège : les résultats sont des skills d'ingénierie (ESP32, STM32, CCNA) déjà écartés le 08/11, ou des catalogues généraux de skills. Les agrégateurs (Skillselion, SkillMD, claudemarketplaces) proposent un skill « cognitive-accessibility » (`community-access/accessibility-agents`) dont le dépôt source n'est pas nommé : **non inspecté**, pas de verdict.

**Ce que la veille améliorerait, en une phrase par skill du dépôt** : `qcm-html-accessible` — les deux portes « une seule réponse défendable / chaque leurre est un vrai raisonnement d'élève », écrites sur le fichier produit (k12-check-for-understanding) ; `controle_ordre_propositions.py` — la place par longueur, cible 15/15/70 (moodle-mcq), pour chiffrer la candidate « ne se devine pas à ses mots » ; `audit_aeration.py` — phrases par paragraphe et mots par phrase selon consigne/explication (plain-language, suite de `francais-simple`) ; `controle_schemas.mjs` — l'étiquette de flèche posée sur son trait (diagram-design-skill) ; mode mission (`enrichir.py`) — chaque pourquoi d'erreur nomme l'étape suivante (k12-check-for-understanding). Les trois idées du 08/11 (quatre niveaux d'une correction, grille de charge cognitive, trois niveaux de vocabulaire) n'ont pas été reprises cette semaine et restent en attente. Chaque réécriture se fait dans une PR à part, si Pascal la demande.

## 6. Décisions pour Pascal

- [ ] Ordre des vagues : P1 d'abord, puis une règle d'or par vague (la plus nombreuse en premier), puis les P3 ?
- [ ] Pour chaque règle qui tombe sur toute une famille : corriger le contrôle, ou les pages ?
- [ ] Les codes COUVERT sans preuve : ajouter deux questions au QCM du lot principal, ou retirer la mutualisation ?
- [ ] Les QCM non marqués par code : adopter la convention `c:"Cx.y"` partout (règle d'or candidate), pour que la preuve se mesure ?
- [ ] Les codes À VÉRIFIER (thème 3) : qui regarde, et quand ?
- [ ] **`controle_regle4.py`** : accepter `?codes=…` après `.html` dans `LIEN_QCM` (18 ateliers) — une PR d'outil ? Et les 3 copies `atelier_bete_a_cornes.html` sans bloc « Prêt·e » ni Bonus : gabarit voulu, ou à compléter dans `build.py` ?
- [ ] **`controle_schemas.mjs`** : déclarer la spirale de Fibonacci de `fiche_arts_tp_4e_socle.html` hors score (illustration, pas schéma) ?
- [ ] **`controle_sauvegarde_locale.py`** (n°322, 15 refus sur 8 pages depuis le 10/11) : `--corriger` sur 3e_C1.5, 4e_C1.4 (+ bonus 2FA), atelier Pix 4e_C4.1, QCM hérité 4e_C6.2, et `build.py` pour les 3 copies d'atelier — une PR courte ? La note poste partagé sur les 73 QCM : oui ou non (question du 10/11) ?
- [ ] **5e_C7.4** : reposer l'outil « chaîne à compléter » (`poser.py`) — et inscrire `controle_chaine_a_completer.py`, `controle_indices_qcm.mjs`, `controle_axe.mjs` dans `rapport_audit.py` ?
- [ ] **n°301 sur les pages intermédiaires d'une séquence éclatée** (3e_C9.2, question du 08/11 toujours ouverte) : la même exemption que `controle_regle4.py` dans `verif_regles_audit.py`, ou un renvoi vers le bilan sur chaque page ?
- [ ] **Les 11 lexiques retouchés à la main** (dérive depuis le 07/11) : reporter dans `vocabulaire_<lot>.json` et régénérer, ou les sortir du générateur ?
- [ ] **Registre** : n°322 et n°323 attribués deux fois (10/11 et 14/11) — renuméroter les deux du 14/11 en n°332 et n°333, et compléter le tableau de tête du journal (arrêté au n°21) ?
- [ ] **Vague n°331** (5 ✘, 39 ⚠ à juger) : dans l'ordre annoncé (3e_C4.3, 5e_C4.1, 3e_C5.1, 3e_C6.1), puis les ⚠ un par un ?
- [ ] Matrice : relire 5e_C1.3, 4e_C1.4, 3e_C1.5 après leurs questions fermées (différenciation, poids des images) — toujours en attente depuis le 08/11.
- [ ] Veille : les cinq idées proposées (deux portes de vérification du QCM, place par longueur 15/15/70, phrases par paragraphe dans `audit_aeration.py`, étiquette sur son trait dans `controle_schemas.mjs`, pourquoi d'erreur → étape suivante) et les trois du 08/11 toujours en attente — lesquelles réécrire, dans quel ordre ? Noter `anthropics/k12-teacher-skills` comme source des deux skills `k12-*` du compte ?
- [ ] Journal : l'entrée du 15/11 de la révision 51 (`5e_C7.5`, #718) garde un marqueur `CONTROLES_ICI` non remplacé dans son paragraphe « Mesure » — à compléter (ce rapport ne touche pas aux entrées existantes).
