# Rapport d'audit des trois thèmes — 2026-11-08

*Écrit par `_outils/rapport_audit.py` (complet). Il mesure et classe ; il ne corrige rien. Les décisions sont à la fin.*

## Résumé

| | Compte | Priorité |
|---|---|---|
| Contrôles bloquants rouges | 0 (aucun) | P1 |
| Codes À VÉRIFIER / ABSENT | 4 | P1 |
| Codes COUVERT sans preuve au QCM (0 question marquée, QCM marqué par code) | 0 sur 58 | P1 |
| Codes COUVERT dont la preuve n'est pas mesurable (QCM non marqué par code, ou absent de la racine) | 19 sur 58 | décision |
| ✘ de règles d'or (à cribler) | 91 sur 39 pages | P2 |
| Codes EXISTANT À AMÉLIORER | 3 | P2 |
| Fichiers qu'une régénération changerait | 73 | P2 |
| Anomalies notées dans la matrice | 107 codes | P3 |

## Depuis la semaine dernière

*Rapport précédent : `RAPPORT_AUDIT_2026-11-07.md` (main du 07/11 au soir, après #610, mode rapide + générateurs ; les six contrôles Playwright avaient tourné à part). Celui-ci : `--complet --generateurs`, main du 08/11 à 21 h 35 UTC (17 h 35 Martinique), après #625.*

| Ligne du résumé | 07/11 | 08/11 | Lecture |
|---|---|---|---|
| Contrôles bloquants rouges | 0 | 0 | — |
| Codes À VÉRIFIER / ABSENT | 4 | 4 | décision de Pascal toujours attendue (3e_C7.1, 3e_C7.2, 4e_C8.1, 5e_C7.1) |
| Codes COUVERT sans preuve au QCM | 0 sur 58 | 0 sur 58 | — |
| Codes COUVERT dont la preuve n'est pas mesurable | 19 sur 58 | 19 sur 58 | la convention `c:"Cx.y"` n'est pas tranchée |
| ✘ de règles d'or | **135 sur 51 pages** | **91 sur 39 pages** | −44 ✘, −12 pages : V1 (#612, exemption n°317/318), V2 de 3e (#614, 7 pages à 0), 5e_C1.5 révisée (#619) |
| dont n°300 (listes déroulantes à convertir) | 51 pages · 1 196 listes après V1 | **38 pages · 1 030 listes** | `verif_regles_audit.py` ; 1 057 après V2 de 3e |
| dont n°29 · 30 · 31 · 34 (ancien gabarit) | 19 pages | **11 pages** (+ 2 pages de 3e_C9.2 en n°34 seule) | les 3e de la famille C7/C8 et 5e_C1.5 sont passées |
| Codes EXISTANT À AMÉLIORER | 3 | 3 | 5e_C1.3, 4e_C1.4 et 3e_C1.5 ont pourtant été révisées cette semaine (#620, #624) : la matrice n'a pas été relue |
| Fichiers qu'une régénération changerait | 12 | **73** | +61 : les 59 pages des ateliers des représentations et les 3 de l'atelier planification — **62 d'entre elles perdraient leur mention de licence** (voir le crible) |
| Contrôles rouges non bloquants | 2 (`regle4`, `schemas`) | **3** (`regle4`, `schemas`, **`contraste_liens`**) | le troisième est nouveau : le lien « CC BY-NC-SA 4.0 » de #616, en bleu par défaut sur fond sombre, 93 pages |
| Anomalies notées dans la matrice | 107 codes | 107 codes | — |

**Autre mesure, nouvelle cette semaine** (`_outils/bilan_revision.py`, révision des trois thèmes décidée le 08/11) : **7 séquences propres sur 56** (0 ✘, 0 menu, 0 écart d'aération : les 6 révisées + 5e_C3.1) ; 49 à faire, dans l'ordre du suivi `docs/revision/SUIVI_REVISION.md` ; 816 écarts d'aération restent sur les pages de séquence.

**PR fusionnées dans l'intervalle** (`git log --merges --since=2026-11-07`, 13 lots) : #611 audit tranche 0 · #612 V1, exemption n°317/318 dans le contrôle n°300 · #614 V2 de 3e, famille C7/C8 au gabarit commun · #615 export Moodle XML des 72 QCM pour Éléa · #616 règle n°321, CC BY-NC-SA sur 410 pages · #617 l'index retrouve les ressources rangées ailleurs · #618 skill `texte-clair-et-aere` · #619 révision des trois thèmes, passe complète, 5e_C1.5 · #620 révision 2-3 (5e_C1.3, 4e_C1.1) · #621 fiche arts plastiques, `build_tp.py` apprend la licence · #622 audit des séquences, étape 4 · #624 révision 4-6 (4e_C1.4, 3e_C1.5, 3e_C2.1 ; séance 5 de 4e_C1.1 coupée) · #625 4e_C1.4, les leçons des situations repliées. Fermées sans fusion : #613, #623, #626 (doublons).

**Ce que ça veut dire.** Les chiffres de la pédagogie et de la couverture n'ont pas bougé : la semaine a été celle de la forme (licence, aération, révision) et des outils. Les ✘ de règles baissent d'un tiers. En contrepartie, deux lots transversaux ont laissé une dette que seul l'audit voit : la mention de licence posée **à la main** sur des pages **engendrées** (62 fichiers), et un lien de licence illisible sur 93 pages.

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
| n°300 | 38 | 38 | T2:16 T3:22 | question dans le flux 33 question(s) posée(s) par une liste déroulante (b1_1, b1_2, b1_3, b1_4, b1_5, n1_1 …) — le menu  | toute une famille de pages : vérifier le CONTRÔLE avant les pages |
| n°34 | 13 | 13 | T2:1 T3:12 | select#a3o1 sans étiquette · select#a3o2 sans étiquette · select#a3o3 sans étiquette · select#a3o4 sans étiquette (+1) | toute une famille de pages : vérifier le CONTRÔLE avant les pages |
| n°29 | 11 | 11 | T2:1 T3:10 | pas de bouton « mode essentiel » | toute une famille de pages : vérifier le CONTRÔLE avant les pages |
| n°30 | 11 | 11 | T2:1 T3:10 | 8 tâches enchaînées sans tableau de bord | toute une famille de pages : vérifier le CONTRÔLE avant les pages |
| n°31 | 11 | 11 | T2:1 T3:10 | 6 zone(s) de rédaction, aucune version étayée | toute une famille de pages : vérifier le CONTRÔLE avant les pages |
| n°301 | 5 | 5 | T2:2 T3:3 | le Bonus vient APRÈS le bilan — du travail demandé après la clôture | à lire page par page |
| n°23 | 2 | 2 | T1:1 T3:1 | 165 min annoncés (+10 de service) pour 165 disponibles — dépassement de 10 min | à lire page par page |

### Par page

| Page | Thème | Règles en ✘ |
|---|---|---|
| 4e_C6.2/sequence-jardin-connecte-arrosage-automatique.html | 2 | n°29 n°30 n°31 n°34 n°300 n°301 |
| 4e_C7.3/sequence_4e_C7.3_bac-du-jardin.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 4e_C7.4/sequence_4e_C7.4_energie-du-jardin.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 4e_C7.5/sequence_4e_C7.5_jardin-incomplet.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 4e_C7.7/sequence_4e_C7.7_support-du-capteur.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 4e_C7.8/sequence_4e_C7.8_le-jardin-publie.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 5e_C7.3/sequence_5e_C7.3_banc-de-la-cour.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 5e_C7.4/sequence_5e_C7.4_indicateur-du-hall.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 5e_C7.5/sequence_5e_C7.5_eclairage-du-preau.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 5e_C8.1/sequence_5e_C8.1_patere-du-hall.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 5e_C8.2/sequence_5e_C8.2_patere-du-hall.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 3e_C9.2/sequence_3e_C9.2-C8.3_station_2_programmer.html | 3 | n°34 n°300 n°301 |
| 3e_C4.3/sequence_3e_C4.3-C4.6_station_alerte_cyclonique.html | 2 | n°300 n°301 |
| 4e_C7.1/sequence_4e_C7_jardin-conception.html | 3 | n°23 n°300 |
| 3e_C9.2/sequence_3e_C9.2-C8.3_station_1_besoin-et-algorithme.html | 3 | n°300 n°301 |
| 3e_C9.2/sequence_3e_C9.2-C8.3_station_3_interaction.html | 3 | n°300 n°301 |
| 3e_C9.2/sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html | 3 | n°34 n°300 |
| 4e_C2.1/sequence_4e_C2_hangzhou_borne.html | 1 | n°23 |
| 3e_C4.1/sequence_3e_C4.1-C4.2_energie_station.html | 2 | n°300 |
| 3e_C4.7/sequence_3e_C4.7-C4.8_internet_sainte_luce.html | 2 | n°300 |
| 3e_C4.8/sequence_3e_C4.7-C4.8_pont_numerique_packet_tracer.html | 2 | n°300 |
| 4e_C4.1/sequence_4e_C4.1-C4.9_jardin_connecte.html | 2 | n°300 |
| 4e_C4.7/sequence_4e_C4.7-C4.9_sos_serre_packet_tracer.html | 2 | n°300 |
| 5e_C4.1/sequence_5e_C4.1-C4.8_lampadaire_intelligent.html | 2 | n°300 |
| 5e_C4.7/sequence_5e_C4.7-C4.8_reseau_local_packet_tracer.html | 2 | n°300 |
| 3e_C5.1/sequence_3e_C5.1-C5.4_sos_station_reparer.html | 2 | n°300 |
| 4e_C5.1/sequence_4e_C5.1-C5.3_depanner_jardin.html | 2 | n°300 |
| 5e_C5.1/sequence_5e_C5.1-C5.3_depanner_lampadaire.html | 2 | n°300 |
| 3e_C6.1/sequence_3e_C6.1-C6.3_programmer_alerte.html | 2 | n°300 |
| 3e_C6.2/sequence_3e_C6.2_auto_test_station.html | 2 | n°300 |
| 4e_C6.1/sequence_4e_C6.1-C6.3_ajuster_programme_jardin.html | 2 | n°300 |
| 5e_C6.1/sequence_5e_C6.1-C6.3_programmer_lampadaire.html | 2 | n°300 |
| 3e_C7.1/sequence_3e_C7_capteur-confort-ny.html | 3 | n°300 |
| 5e_C7.1/sequence_5e_C7_mini-projet-objet.html | 3 | n°300 |
| 4e_C8.1/sequence_4e_C8_jardin-validation.html | 3 | n°300 |
| 3e_C9.1/sequence_3e_C9.1_variables_types_systemes.html | 3 | n°300 |
| 3e_C9.2/sequence_3e_C9.2-C8.3_station_4_recette.html | 3 | n°300 |
| 4e_C9.1/sequence_4e_C9_jardin-programme.html | 3 | n°300 |
| 5e_C9.1/sequence_5e_C9.1-C9.3_boite_etiquetee.html | 3 | n°300 |

### Crible du 08/11/2026 (vrai défaut / contrôle périmé) (Fable, après lecture des messages de `verif_regles_audit.py`, d'une page témoin par règle, et d'une régénération d'essai dans une copie)

*Ce qui tient toujours est reporté du crible du 07/11 ; ce qui est réglé est barré, avec sa PR.*

| Règle | Verdict | Ce qu'il faut faire | Taille |
|---|---|---|---|
| **n°300** (38 pages, **1 030 listes**) | **Vrai défaut, en cours.** ~~Le contrôle comptait les menus voulus par les n°317/318~~ — réglé par V1 (#612). ~~Les 7 pages de 3e de la famille C7/C8~~ — converties par V2 (#614, 0 ✘). ~~5e_C1.5~~ — révisée (#619). Depuis le 08/11, la conversion ne se fait plus par vague mais **dans la passe complète par séquence** (`revision-sequence`, ordre du suivi) : `migrer_gabarit_306.py` pour les 11 pages de l'ancien gabarit, `--n300` pour les 27 autres, `grilles_radio.py` quand les questions partagent leurs réponses. En tête : 5e_C4.1 (64), 3e_C9.2 (62 sur 4 pages, **engendrées** : convertir dans `generer_les_quatre_pages.py`), 4e_C9.1 (54), 4e_C4.7 (40), 4e_C4.1 (39). | Suivre l'ordre du suivi (prochaines : 5e_C1.1, 5e_C1.2, 5e_C3.1, 4e_C2.1, 4e_C3.1, 3e_C4.1, 3e_C4.3) ; les pages qui ne sont pas dans l'ordre de passage immédiat mais qui passent en classe tôt (5e_C4.1 en P4) y arriveront à leur tour. | 38 pages |
| **n°29 · n°30 · n°31 · n°34** (11 pages, les mêmes) | **Vrai défaut, une famille** : 4e_C7.3→C7.8 (5), 5e_C7.3→C7.5 et C8.1-C8.2 (5), 4e_C6.2 — l'ancien gabarit (ids `a0q1`, `textarea#hyp` sans étiquette). ~~Les 7 pages de 3e~~ — V2 de 3e (#614). ~~5e_C1.5~~ (#619). L'outil est prêt et rejouable. **Nouveau, à part** : 3e_C9.2 `station_2` et `station_alerte` tombent en n°34 seule pour « image sans alternative textuelle » — pages engendrées, corriger `generer_les_quatre_pages.py`. | V2 de 4e (6 pages) et V2 de 5e (5 pages) : `migrer_gabarit_306.py` page par page, bancs, revue d'écran — ou, puisque la passe complète prime, les prendre à leur tour du suivi (toutes sont en P4-P5). À Pascal de dire lequel des deux ordres. | 11 pages × 4 règles + 2 pages |
| **n°301** (5 pages) | **Deux vrais défauts, et trois ✘ à vérifier côté contrôle.** 3e_C4.3 (le Bonus vient après le bilan) et 4e_C6.2 (aucun bilan) : inchangés. Les trois pages `station_1`, `station_2`, `station_3` de 3e_C9.2 n'ont « aucun bilan » parce que la séquence est **éclatée en quatre pages** et que le bilan vit en page 4 par construction (le générateur l'écrit : « synthèse → Bonus → bilan → QCM dans s8 ») ; le contrôle lit chaque page seule. **Interroger le contrôle d'abord** : une page d'une séquence éclatée qui renvoie à la page qui porte le bilan ne devrait pas tomber. | Une PR courte : remonter le Bonus de 3e_C4.3, écrire le bilan de 4e_C6.2 (en même temps que son passage au gabarit commun) ; et décider pour le contrôle (exemption des pages intermédiaires d'une séquence éclatée, déclarées dans la page tout-en-un). | 2 pages + 1 règle de contrôle |
| **n°23** (2 pages) | **Vrai défaut, à trancher par Pascal, inchangé** : 4e_C2.1 (165 min pour 165, +10 de service), 4e_C7.1 (145 min pour 110). 4e_C2.1 est la 10e du suivi : la passe complète peut couper une activité si Pascal le dit. | Couper une activité ou annoncer une séance de plus dans le classeur. | 2 pages |

**Hors règles d'or, criblé aussi.**

- **`controle_contraste_liens.mjs` ✘ (nouveau)** — 93 liens sur 93 pages sous 4,5:1, **tous le même** : le lien « CC BY-NC-SA 4.0 » de la mention de licence (n°321, #616), en bleu par défaut du navigateur (rgb(0,0,238)) sur le fond sombre (2,03:1), sur les pages qui ne colorent pas leurs `a` : 58 lexiques, 17 synthèses professeur, 13 séquences (dont 4e_C6.2), 5 QCM. Vrai défaut, **une seule source** : `_outils/licence_cc.py` (la `MENTION`) doit donner sa couleur au lien (`color:inherit` ou la couleur des liens du site), puis la mention se repose sur les 410 pages (`controle_licence.py --corriger` après retrait de l'ancienne, ou un remplacement textuel), et `generer_lexique.py` / `make_index.py` / `build_tp.py` la reprennent par import. Une PR d'outil.
- **Dérive des générateurs : 12 → 73 fichiers.** Régénération d'essai faite dans une copie hors git et comparée au dépôt : (1) **62 fichiers perdraient leur mention de licence** — les 59 pages des ateliers des représentations (`build.py` : 35 ateliers, cahiers et synthèses, 24 incrustations rangées dans 19 dossiers de repères) et les 3 pages de l'atelier planification (`build_atelier.py`) ont reçu la mention à la main par #616, et ces deux générateurs ne la connaissent pas — exactement le défaut réparé dans `build_tp.py` par #621 (n°283 : une page engendrée se change dans son générateur) ; (2) les mêmes pages recevraient la **grille des exercices « classer »** et les corrections aérées à leur source (#624 : « à leur prochaine régénération ») — voulu ; (3) les **11 lexiques** retouchés à la main, constat du 07/11, inchangés ; ~~la page `station_1` de 3e_C9.2~~ — régénérée par #618. **À faire d'abord** : `build.py` et `build_atelier.py` importent `MENTION` depuis `_outils/licence_cc.py` et la posent eux-mêmes (comme `build_tp.py`), vérification « identique octet pour octet » sur une page, **puis** régénération des 62 pages (qui pose la grille au passage), bancs des ateliers (`banc_ateliers.py`), `controle_licence`. Tant que ce n'est pas fait, **personne ne relance `build.py`** sur le dépôt.
- `controle_regle4.py` ✘ (3e_C9.2 recette, bouton QCM à 54 %) et `controle_schemas.mjs` ✘ (1 schéma, 10 ✘, n°315) : inchangés depuis le 07/11, deux PR courtes ; la première se règle dans le générateur de 3e_C9.2 avec le reste.
- **Matrice** : 5e_C1.3, 4e_C1.4 et 3e_C1.5 sont « EXISTANT À AMÉLIORER » pour « pas de différenciation » et « images lourdes » ; les trois ont été révisées cette semaine (#620, #624) sans que la matrice soit relue. À passer par `audit-couverture-cycle4` : soit les anomalies sont levées, soit elles restent et la passe complète doit les prendre (le skill `revision-sequence` n'inclut pas la différenciation ni le poids des images).

**Lecture d'ensemble.** 91 ✘, mais le chantier qui prime n'est plus dans les règles d'or : c'est la **licence posée à la main sur des pages engendrées** (62 fichiers) et son lien illisible (93 pages) — deux PR d'outil, courtes, à faire avant toute régénération. Les règles d'or se résorbent par la passe complète (7 séquences propres sur 56, six en une journée).

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
| `controle_regle4.py` | ✘ 1 |      le bouton QCM est à 54 % de la page, pas à la fin · 1 lien(s) vers un QCM avant la région finale (à 54 % de la page) | P2 |
| `controle_medias.py` | ✅ 0 | ✅ chaque image du dépôt a une provenance écrite, et aucune n'est promise en vain | P1 |
| `controle_sigles.py` | ✅ 0 | ✅ chaque sigle garde ses capitales (règle d'or n°313) | P2 |
| `controle_unites.py` | ✅ 0 | ✅ chaque unité est nommée en toutes lettres dans son activité, son tableau, sa question ou son schéma (règle d'or n°312) | P2 |
| `controle_fichiers_telechargeables.py` | ✅ 0 | ✅ chaque fichier nommé dans une séquence se prend d'un clic | P2 |
| `controle_atteignabilite.py` | ✅ 0 | ✅ toute page du dépôt est atteignable depuis l'index, hors tolérées déclarées | P2 |
| `controle_rapports_tests.py` | ✅ 0 | ✅ aucun rapport n'attribue ses résultats à un script absent | P2 |
| `controle_blocs_dessines.py` | ✅ 0 | 480 page(s) lues · 10 dessin(s) en attente · ✅ aucun dessin de blocs hors registre | P2 |
| `controle_schemas.mjs` | ✘ 1 | 1 schéma(s) avec au moins un ✘ · 10 ✘ · 553 ⚠ | P2 |
| `controle_squelette.mjs` | ✅ 0 | ✅ chaque séquence montre son ouverture au premier écran et sa clôture à la dernière séance, dans l'ordre | P1 |
| `controle_hors_ligne.mjs` | ✅ 0 | ✅ aucune page ne dépend du réseau pour s'afficher, et chaque activité en ligne le dit | P1 |
| `controle_impression.mjs` | ✅ 0 | ✅ aucune page n'imprime un texte que le papier ne rendra pas | P2 |
| `controle_verrous.mjs` | ✅ 0 | ✅ aucun verrou expérientiel ouvert au chargement | P2 |
| `controle_contraste_liens.mjs` | ✘ 1 | ⛔ Un lien qu'on ne peut pas lire n'est pas un lien. Règle d'or n°303. | P2 |
| `controle_code_colore.mjs` | ✅ 0 | ✅ chaque listing de code est en couleurs, comme dans un IDE (106 listing(s), 15 page(s) ; règle d'or n°13) | P2 |

## 4. Dérive des générateurs

| Générateur | Sortie | Dernière ligne |
|---|---|---|
| `build.py` | ✅ 0 | cahiers : 3 page(s) |
| `build_atelier.py` | ✅ 0 | écrit : atelier_3e_C7.1_planification_taches.html (92029 o) |
| `build_tp.py tp_5e_de_onshape.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_5e_de_onshape.html |
| `build_tp.py tp_5e_de_calottes.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_5e_de_calottes.html |
| `build_tp.py tp_4e_socle_assemblage.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_4e_socle_assemblage.html |
| `build_tp.py tp_3e_boitier_etanche.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_3e_boitier_etanche.html |
| `generer_les_quatre_pages.py` | ✅ 0 | écrit : sequence_3e_C9.2-C8.3_station_4_recette.html 183 Ko |
| `_outils/generer_lexique.py --tous theme-1-objets-systemes-usages-interactions theme-2-structure-fonctionnement-comportement theme-3-creation-conception-realisation-innovations` | ✅ 0 | 5e_C9.1                                                     30 notions → lexique_5e_C9.1.html |

Fichiers qu'une régénération changerait (73) — une retouche faite à la main sur ces pages sera écrasée :

- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/3e/3e_C1.3/atelier_carte_mentale.html`
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.2/atelier_carte_mentale.html`
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.3/atelier_bete_a_cornes.html`
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.2/atelier_diagramme_fast.html`
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.3/lexique_5e_C1.3.html`
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.4/atelier_carte_mentale.html`
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/3e/3e_C2.1/atelier_diagramme_cas_utilisation.html`
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/4e/4e_C2.1/atelier_croquis.html`
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/4e/4e_C2.1/atelier_diagramme_cas_utilisation.html`
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/4e/4e_C2.2/atelier_diagramme_des_exigences.html`
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/4e/4e_C2.2/atelier_diagramme_pieuvre.html`
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/5e/5e_C2.1/atelier_diagramme_cas_utilisation.html`
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/5e/5e_C2.1/atelier_diagramme_pieuvre.html`
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/5e/5e_C2.2/atelier_diagramme_pieuvre.html`
- `theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/3e/3e_C3.1/atelier_bete_a_cornes.html`
- `theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/3e/3e_C3.3/atelier_diagramme_des_exigences.html`
- `theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/4e/4e_C3.1/atelier_bete_a_cornes.html`
- `theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/5e/5e_C3.3/atelier_bete_a_cornes.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/besoin-bete-a-cornes/Synthèses/synthese_eleve_besoin-bete-a-cornes.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/besoin-bete-a-cornes/Synthèses/synthese_professeur_besoin-bete-a-cornes.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/besoin-bete-a-cornes/atelier_3e_besoin-bete-a-cornes.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/besoin-bete-a-cornes/atelier_4e_besoin-bete-a-cornes.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/besoin-bete-a-cornes/atelier_5e_besoin-bete-a-cornes.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/cahiers/cahier_3e_representations.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/cahiers/cahier_4e_representations.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/cahiers/cahier_5e_representations.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/carte-mentale/Synthèses/synthese_eleve_carte-mentale.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/carte-mentale/Synthèses/synthese_professeur_carte-mentale.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/carte-mentale/atelier_3e_carte-mentale.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/carte-mentale/atelier_4e_carte-mentale.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/carte-mentale/atelier_5e_carte-mentale.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/cas-utilisation-sysml/Synthèses/synthese_eleve_cas-utilisation-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/cas-utilisation-sysml/Synthèses/synthese_professeur_cas-utilisation-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/cas-utilisation-sysml/atelier_3e_cas-utilisation-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/cas-utilisation-sysml/atelier_4e_cas-utilisation-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/cas-utilisation-sysml/atelier_5e_cas-utilisation-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/croquis/Synthèses/synthese_eleve_croquis.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/croquis/Synthèses/synthese_professeur_croquis.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/croquis/atelier_3e_croquis.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/croquis/atelier_4e_croquis.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/exigences-sysml/Synthèses/synthese_eleve_exigences-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/exigences-sysml/Synthèses/synthese_professeur_exigences-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/exigences-sysml/atelier_3e_exigences-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/exigences-sysml/atelier_4e_exigences-sysml.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/fast/Synthèses/synthese_eleve_fast.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/fast/Synthèses/synthese_professeur_fast.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/fast/atelier_3e_fast.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/fast/atelier_4e_fast.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/fast/atelier_5e_fast.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/interacteurs-pieuvre/Synthèses/synthese_eleve_interacteurs-pieuvre.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/interacteurs-pieuvre/Synthèses/synthese_professeur_interacteurs-pieuvre.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/interacteurs-pieuvre/atelier_4e_interacteurs-pieuvre.html`
- `theme-1-objets-systemes-usages-interactions/ateliers-representations/interacteurs-pieuvre/atelier_5e_interacteurs-pieuvre.html`
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.1/lexique_3e_C4.1.html`
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/lexique_4e_C4.1.html`
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.4/atelier_diagramme_fast.html`
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.7/lexique_4e_C4.7.html`
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/5e/5e_C4.1/atelier_diagramme_fast.html`
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/3e/3e_C5.1/lexique_3e_C5.1.html`
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/4e/4e_C5.1/lexique_4e_C5.1.html`
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/5e/5e_C5.1/lexique_5e_C5.1.html`
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/5e/5e_C6.1/lexique_5e_C6.1.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.2/atelier_croquis.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.2/atelier_diagramme_fast.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.2/atelier_croquis.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.2/atelier_diagramme_fast.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.1/lexique_5e_C7.1.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.4/lexique_5e_C7.4.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.5/lexique_5e_C7.5.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-planification/atelier_3e_C7.1_planification_taches.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-planification/atelier_4e_C7.1_planification_taches.html`
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-planification/atelier_5e_C7.1_planification_taches.html`
- `theme-3-creation-conception-realisation-innovations/C8-valider-les-solutions-techniques-par-des/4e/4e_C8.3/atelier_diagramme_des_exigences.html`

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

## Veille du 2026-11-08 — skills et plugins (lecture seule, aucune installation)

*Méthode : WebSearch (six requêtes : ressources HTML pédagogiques et accessibles, SVG et schémas, QCM et évaluation, Arduino / Packet Tracer / Filius / Vittascience, langage clair / FALC, enseignement explicite / différenciation / évaluation formative), puis inspection des candidats absents de `SKILLS_AUDIT.md` : dépôts clonés en lecture seule (`git clone --depth 1`) dans le bac à sable de la session, SKILL.md et manifestes lus, **aucun script exécuté**, rien installé. Les pages web des dépôts n'ont pas pu être lues par l'outil de lecture web (demande d'autorisation sans réponse, session sans surveillance) ; le clone en lecture seule est la méthode du registre (08/11). Les verdicts sont des propositions : `SKILLS_AUDIT.md` n'est modifié que sur décision de Pascal.*

| Nom | Dépôt | Licence | Ce qu'il fait | Ce qui gêne | Verdict proposé | Question à Pascal |
|---|---|---|---|---|---|---|
| **Education Agent Skills** (165 skills, 20 domaines) | `GarethManning/education-agent-skills` — 914 ★, v3.1.0 du 22/10/2026, auteur enseignant (écoles internationales) | **CC BY-SA 4.0** | Un SKILL.md par geste pédagogique, chacun un **gabarit de prompt** à champs (`{{task_context}}`, « context engine ») avec ses sources (Hattie & Timperley, Sweller, Beck-McKeown-Kucan, Rosenshine…) et une échelle de preuve ; domaines `explicit-instruction`, `questioning-discussion`, `self-regulated-learning` — **les mêmes noms que trois skills du compte claude.ai de Pascal**, qui en viennent probablement. Lus : `feedback-quality-analyser` (quatre niveaux de rétroaction, feed up / back / forward, spécificité, menace), `cognitive-load-analyser` (charge intrinsèque / extrinsèque / germane, attention partagée, redondance, inversion de l'expertise), `vocabulary-tiering-tool` (trois niveaux de vocabulaire, priorité au niveau 2, 5-8 mots à enseigner), `differentiation-adapter` (même objectif, autre chemin ; refuse les « styles d'apprentissage »). | Plugin Claude Code + serveur MCP (`mcp-server/`, Node) + scripts Python de validation (non lancés) ; vocabulaire britannique (« Year 9 ») ; **licence BY-SA : reprendre un texte imposerait BY-SA au dépôt, qui est BY-NC-SA (n°321)** — seules les idées se reprennent, réécrites. | **Idée à reprendre, réécrite de zéro** (pas d'installation) : (a) le crible de la correction en quatre niveaux — tâche / démarche / autorégulation / personne — et « où j'en suis, où je vais, comment j'y vais », pour `texte-clair-et-aere` (ordre d'une correction) et `qcm-html-accessible` (réfutation des distracteurs) ; (b) la grille de charge cognitive (attention partagée, redondance, un seul tenant) pour `revision-sequence`, qui mesure les mots mais ne nomme pas encore les causes ; (c) les trois niveaux de vocabulaire pour `lexique-sequence` (passe « lisibilité » : les mots de niveau 2 sont ceux qu'on oublie de définir). | Les skills `explicit-instruction`, `questioning-discussion`, `self-regulated-learning` du compte viennent-ils de ce dépôt (quelle version) ? S'ils sont à la v2 et le dépôt à la v3.1, faut-il relire les écarts (inventaire du 23/10) ? |
| **Inclusive Design Skills** (58 skills, 6 plugins) | `owl-listener/inclusive-design-skills` — MC Dean, dernier commit 09/06/2026, ~108 ★ | MIT | Accessibilité cognitive et contenu lisible : `plain-language-design` (test des 5 secondes, test du jargon, test de l'action, voix active, **15-20 mots par phrase, une idée par phrase, une consigne par paragraphe**, table de remplacements, niveau de lecture visé), `readable-content` (pyramide inversée, **3-4 phrases par paragraphe**, pas plus de 7 items par liste, une action par étape et « ce que tu dois voir après »), `memory-load-reduction` (4 éléments en mémoire de travail, ne jamais redemander ce que la page sait, sauvegarde et reprise, « étape 2 sur 4 »). Pas de script, pas de hook : du texte seulement. | Anglais, orienté produits numériques (formulaires, erreurs, tunnels d'achat) ; installation par `npx skills add` (CLI tiers). | **Idée à reprendre, réécrite de zéro** : (a) le « test de l'action » (un bouton dit ce qu'il fait : « Vérifier mes réponses », pas « OK ») et « ce que tu dois voir après chaque étape » — déjà la légende en trois temps de `texte-clair-et-aere`, à étendre aux **messages des vérificateurs** ; (b) les seuils 3-4 phrases par paragraphe et 7 items par liste pour `audit_aeration.py` (qui compte des mots, pas des phrases) ; (c) la liste « la page se souvient » pour `sequence-pedagogique-engageante` (bandeau des tâches, sauvegarde : déjà là ; « ne jamais redemander » : à vérifier dans les verrous). | Veut-il que `audit_aeration.py` compte aussi les phrases par paragraphe (seuil 4) ? |
| **schematic-diagram** (plugin) | `Tachy/claude-skills` — Johannes Güntert, v1.1.1 du 17/05/2026 | MIT (manifeste) | Un schéma électrique en Graphviz DOT → SVG + PNG à partir d'une description ; quatre archétypes (énergie, capter → traiter → agir, multi-cartes, bus) ; **place la couche énergie EN HAUT et la commande en bas** — le contraire de la convention du dépôt (information en haut, énergie en bas, règle d'or n°6). | Binaire Graphviz à installer ; connecteur MCP distant proposé par l'agrégateur ; pas de `title`/`desc` accessibles (règle n°1). | **Refusé.** Rien à reprendre : les chaînes du dépôt sont dessinées à la main en SVG fonctionnel (`chaine-energie-fonctionnelle`, n°310) et la convention est inverse. | — |
| **embedded-engineering-skills** (46 skills) | `wedsamuel1230/arduino-skills` — dernier commit 15/10/2026 | MIT | Ingénierie embarquée professionnelle : ESP32, STM32, Zephyr, FreeRTOS, OTA ; `arduino-code-generator` passe par `uv run scripts/generate_snippet.py` ; `wiring-safety-check` : contrat électrique avant d'alimenter (niveaux 3,3 V / 5 V, courants, pull-up, roue libre), tableau « anti-rationalisation » (« c'est un capteur 5 V donc sa broche est sûre » → non). | Scripts Python et `uv` exécutés par le skill ; hors du périmètre collège (pas de Grove, pas d'UNO R4 nommée, pas de blocs, pas de très basse tension au sens TBT scolaire) ; 46 skills présentés au modèle. | **Refusé comme plugin.** **Une idée à reprendre, réécrite** : le tableau « raccourci → réponse » de `wiring-safety-check`, transposé aux pièges de classe (« 12 V sans danger au toucher » vu par l'audit externe dans dix pages, #622) pour `arduino-grove-college` §sécurité TBT. | — |
| **wcag-accessibility-audit** | `mastepanoski/claude-skills` (14 skills : UX, WCAG, gouvernance IA) — dernier commit 29/10/2026, 67 ★ | MIT | Liste de contrôle WCAG 2.1/2.2 par principe POUR, niveaux A/AA/AAA ; renvoie à axe DevTools, WAVE, Lighthouse ; aucun script. | Audit « papier » : ne mesure rien ; anglais ; `npx skills add`. | **Refusé.** Les contrôles de `_outils/` mesurent déjà (tactile 16 px, contraste des liens, débordement, mode essentiel, aria des champs) ; une liste WCAG ne ferait que doublonner `balayage-navigateur`. | — |
| **lesson-quiz** | `luongnv89/claude-howto` — 03/11/2026 | MIT | Quiz de 10 questions sur les leçons… du tutoriel Claude Code lui-même. | — | **Hors sujet, refusé.** | — |
| **teaching-skills** | `full-stack-skills/teaching-skills` (PartMe.AI) — 04/10/2026, 2 ★ | Apache 2.0 | Trois skills génériques en chinois (`learning-assessor` : 124 mots). | Maigre ; dossiers `.zcode`, `.kimi-code` ; `npx`. | **Refusé.** Rien de neuf face à `qcm-html-accessible`. | — |
| **teaching-skills** (université) | `YujxZJCN/teaching-skills` — 49 ★ | MIT | 15 skills pour professeurs d'université (Bloom, accréditation, « passeport de cours » YAML). | Scripts Python, cadre universitaire. | **Hors cible (collège), refusé.** Seule piste : le diagnostic de cohorte, sans objet ici (n°26 : le diagnostic d'entrée est déjà dans chaque séquence). | — |

**Déjà jugés, pas rejugés** : `francais-simple`, `refine-prose`, `clean-copy`, `assessment-design`, `school-skills`, `style-prose` (08/11) ; UI UX Pro Max, Taste, Impeccable, Ponytail, ECC (07/11 et 23/10). Rien de nouveau sur Filius, Packet Tracer, Vittascience, la CAO ou l'impression : les résultats sont des skills d'ingénierie réseau CCNA ou de CAO professionnelle, hors sujet.

**Ce que la veille améliorerait, en une phrase par skill du dépôt** : `texte-clair-et-aere` — nommer les quatre niveaux d'une correction et le « test de l'action » sur les boutons et messages ; `revision-sequence` — une grille des causes de charge (attention partagée, redondance, pavé d'un seul tenant) à côté du compte de mots ; `lexique-sequence` — les trois niveaux de vocabulaire dans la passe « lisibilité » ; `arduino-grove-college` — un tableau « raccourci dangereux → réponse » pour la TBT ; `audit_aeration.py` — compter les phrases par paragraphe. Chaque réécriture se fait dans une PR à part, si Pascal la demande.

## 6. Décisions pour Pascal

- [ ] Ordre des vagues : P1 d'abord, puis une règle d'or par vague (la plus nombreuse en premier), puis les P3 ?
- [ ] Pour chaque règle qui tombe sur toute une famille : corriger le contrôle, ou les pages ?
- [ ] Les codes COUVERT sans preuve : ajouter deux questions au QCM du lot principal, ou retirer la mutualisation ?
- [ ] Les QCM non marqués par code : adopter la convention `c:"Cx.y"` partout (règle d'or candidate), pour que la preuve se mesure ?
- [ ] Les codes À VÉRIFIER (thème 3) : qui regarde, et quand ?
- [ ] **Licence (n°321) sur les pages engendrées** : apprendre la mention à `build.py` (ateliers des représentations) et `build_atelier.py` comme à `build_tp.py` (#621), puis régénérer les 62 pages (grille des « classer » posée au passage) — une PR d'outil, **avant toute autre régénération** ?
- [ ] **Lien « CC BY-NC-SA 4.0 » illisible sur 93 pages** (2,03:1) : donner sa couleur au lien dans `_outils/licence_cc.py` et reposer la mention — une PR d'outil ?
- [ ] V2 de 4e et de 5e (11 pages de l'ancien gabarit) : par vague tout de suite, ou à leur tour dans la passe complète (toutes en P4-P5) ?
- [ ] n°301 sur les pages intermédiaires d'une séquence éclatée (3e_C9.2) : exempter dans le contrôle, ou poser un renvoi vers le bilan sur chaque page ?
- [ ] Matrice : relire 5e_C1.3, 4e_C1.4, 3e_C1.5 après leur révision (différenciation, poids des images) ?
- [ ] Veille : les trois idées proposées (quatre niveaux de correction, grille de charge, trois niveaux de vocabulaire) — lesquelles réécrire, et dans quel ordre ? Les skills `explicit-instruction` / `questioning-discussion` / `self-regulated-learning` du compte viennent-ils de `education-agent-skills` ?
