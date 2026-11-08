# Rapport d'audit des trois thèmes — 2026-11-07

*Écrit par `_outils/rapport_audit.py` (rapide, avec générateurs). Il mesure et classe ; il ne corrige rien. Les décisions sont à la fin.*

## Résumé

| | Compte | Priorité |
|---|---|---|
| Contrôles bloquants rouges | 0 (aucun) | P1 |
| Codes À VÉRIFIER / ABSENT | 4 | P1 |
| Codes COUVERT sans preuve au QCM (0 question marquée, QCM marqué par code) | 0 sur 58 | P1 |
| Codes COUVERT dont la preuve n'est pas mesurable (QCM non marqué par code, ou absent de la racine) | 19 sur 58 | décision |
| ✘ de règles d'or (à cribler) | 135 sur 51 pages | P2 |
| Codes EXISTANT À AMÉLIORER | 3 | P2 |
| Fichiers qu'une régénération changerait | 12 | P2 |
| Anomalies notées dans la matrice | 107 codes | P3 |

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
| n°300 | 51 | 51 | T1:6 T2:16 T3:29 | question dans le flux 4 question(s) posée(s) par une liste déroulante (bc_4e_rappel-feux__aqui, bc_4e_rappel-feux__surqu | toute une famille de pages : vérifier le CONTRÔLE avant les pages |
| n°34 | 21 | 21 | T1:1 T2:1 T3:19 | textarea#hyp sans étiquette · select#a0q1 sans étiquette · select#a0q2 sans étiquette · select#a0q3 sans étiquette (+24) | toute une famille de pages : vérifier le CONTRÔLE avant les pages |
| n°29 | 19 | 19 | T1:1 T2:1 T3:17 | pas de bouton « mode essentiel » | toute une famille de pages : vérifier le CONTRÔLE avant les pages |
| n°30 | 19 | 19 | T1:1 T2:1 T3:17 | 6 tâches enchaînées sans tableau de bord | toute une famille de pages : vérifier le CONTRÔLE avant les pages |
| n°31 | 18 | 18 | T2:1 T3:17 | 6 zone(s) de rédaction, aucune version étayée | toute une famille de pages : vérifier le CONTRÔLE avant les pages |
| n°301 | 5 | 5 | T2:2 T3:3 | le Bonus vient APRÈS le bilan — du travail demandé après la clôture | à lire page par page |
| n°23 | 2 | 2 | T1:1 T3:1 | 165 min annoncés (+10 de service) pour 165 disponibles — dépassement de 10 min | à lire page par page |

### Par page

| Page | Thème | Règles en ✘ |
|---|---|---|
| 4e_C6.2/sequence-jardin-connecte-arrosage-automatique.html | 2 | n°29 n°30 n°31 n°34 n°300 n°301 |
| 3e_C7.3/sequence_3e_C7.3_boitier-de-la-station.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 3e_C7.4/sequence_3e_C7.4_energie-de-la-station.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 3e_C7.5/sequence_3e_C7.5_station-a-equiper.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 3e_C7.7/sequence_3e_C7.7_produire-le-boitier.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 3e_C7.8/sequence_3e_C7.8_deux-stations.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 4e_C7.3/sequence_4e_C7.3_bac-du-jardin.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 4e_C7.4/sequence_4e_C7.4_energie-du-jardin.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 4e_C7.5/sequence_4e_C7.5_jardin-incomplet.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 4e_C7.7/sequence_4e_C7.7_support-du-capteur.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 4e_C7.8/sequence_4e_C7.8_le-jardin-publie.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 5e_C7.3/sequence_5e_C7.3_banc-de-la-cour.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 5e_C7.4/sequence_5e_C7.4_indicateur-du-hall.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 5e_C7.5/sequence_5e_C7.5_eclairage-du-preau.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 3e_C8.1/sequence_3e_C8.1_mat-de-la-station.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 3e_C8.2/sequence_3e_C8.2_mat-de-la-station.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 5e_C8.1/sequence_5e_C8.1_patere-du-hall.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 5e_C8.2/sequence_5e_C8.2_patere-du-hall.html | 3 | n°29 n°30 n°31 n°34 n°300 |
| 5e_C1.5/sequence_5e_C1.5-C1.6_le-compte-du-club.html | 1 | n°29 n°30 n°34 n°300 |
| 3e_C9.2/sequence_3e_C9.2-C8.3_station_2_programmer.html | 3 | n°34 n°300 n°301 |
| 4e_C2.1/sequence_4e_C2_hangzhou_borne.html | 1 | n°23 n°300 |
| 3e_C4.3/sequence_3e_C4.3-C4.6_station_alerte_cyclonique.html | 2 | n°300 n°301 |
| 4e_C7.1/sequence_4e_C7_jardin-conception.html | 3 | n°23 n°300 |
| 3e_C9.2/sequence_3e_C9.2-C8.3_station_1_besoin-et-algorithme.html | 3 | n°300 n°301 |
| 3e_C9.2/sequence_3e_C9.2-C8.3_station_3_interaction.html | 3 | n°300 n°301 |
| 3e_C9.2/sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html | 3 | n°34 n°300 |
| 4e_C1.1/sequence_4e_C1.1-C1.3_tsinghua_feux.html | 1 | n°300 |
| 5e_C2.1/sequence_5e_C2_shenzhen_station_velos.html | 1 | n°300 |
| 3e_C3.1/sequence_3e_C3.1-C3.4_shenzhen.html | 1 | n°300 |
| 4e_C3.1/sequence_4e_C3.1-C3.3_hangzhou.html | 1 | n°300 |
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

### Crible du 07/11/2026 (vrai défaut / contrôle périmé) (Fable, après lecture des messages et de pages témoins)

| Règle | Verdict | Ce qu'il faut faire | Taille |
|---|---|---|---|
| **n°300** (51 pages, ≈ 1 200 listes déroulantes) | **Vrai défaut, et le plus gros chantier du dépôt** — la conversion en boutons radio n'a été faite que sur le pilote 3e_C1.1 et les familles C1-C3 du thème 1. **Plus un contrôle en retard** : il compte aussi les menus de la bête à cornes (`bc_*…__aqui/surquoi/objet/but`, `bac_*`) et ceux des cahiers des charges (`*cdcf*`), que la n°317 (31/10) et la n°318 (04/11) imposent. (Correction du 07/11 au soir, V1 : les `be_*` sont les **billets d'entrée**, pas la bête à cornes — ils restent à convertir.) **Après V1** : 130 ✘, 46 pages, **1 196 listes** réellement à convertir. | 1) Une PR d'outil : `verif_regles_audit.py` exempte les menus n°317/318 (et les signale « voulus »). 2) Une vague par thème, dans l'ordre des classeurs de progression (ce qui passe en classe le plus tôt d'abord) ; chaque page convertie passe par `controle_mode_essentiel`, son banc, et la revue d'écran (le bord de `<fieldset>` coupé par la `<legend>` est le défaut connu). | 48 pages réelles après exemption · 4e_C4.1 (61), 5e_C4.1 (64), 4e_C9.1 (54), 3e_C9.2 (4 pages, 134) en tête |
| **n°29 · n°30 · n°31 · n°34** (19 pages, les mêmes) | **Vrai défaut, une famille** : 3e/4e/5e C7.3→C7.8, C8.1-C8.2, plus 4e_C6.2 et 5e_C1.5 — passées aux onglets le 04/11 mais restées sur l'ancien gabarit (ids `a0q1`, `textarea#hyp` sans étiquette) : pas de mode essentiel, pas de tableau de bord des tâches, aucune version étayée, champs sans étiquette. | Une vague par niveau (3e : 7 pages · 4e : 6 · 5e : 6), par script sur le gabarit n°306 (bouton + `body.essentiel`, bandeau des tâches, `details.etayage` par zone de rédaction, `<label>`), bancs du lot, revue d'écran. Ces mêmes pages portent aussi la n°300 : les deux vagues se font ensemble, page par page. | 19 pages × 4 règles |
| **n°301** (3 pages) | **Vrai défaut, ponctuel** : 3e_C4.3 (le Bonus vient après le bilan), 4e_C6.2 et 3e_C9.2 (aucun bilan). | Une PR : remonter le Bonus, écrire les deux bilans (auto-positionnement sur les 4 niveaux LSU). 3e_C9.2 est engendrée (`generer_les_quatre_pages.py`) : corriger le générateur. | 3 pages |
| **n°23** (2 pages) | **Vrai défaut, à trancher par Pascal** : 4e_C2.1 annonce 165 min pour 165 disponibles (+10 de service), 4e_C7.1 145 min pour 110. | Couper une activité, ou annoncer une séance de plus dans le classeur. | 2 pages |

**Lecture d'ensemble.** 135 ✘, mais trois chantiers : la conversion n°300 (le gros), la famille C7/C8 sur l'ancien gabarit (qui se fait en même temps), et quatre pages ponctuelles. Les règles d'or elles-mêmes tiennent ; le contrôle n°300 a une exemption à écrire.

### Les autres plans, lus à la main

- **Couverture (P1)** — 4 codes « À VÉRIFIER PAR L'ENSEIGNANT » (3e_C7.1, 3e_C7.2, 4e_C8.1, 5e_C7.1) : ce sont les séquences-projets du thème 3, dont le statut attend un regard de Pascal sur le report des scores, pas un lot. **Décision à prendre, pas de travail.**
- **Preuve des COUVERT** — la mesure « deux questions marquées du code » ne vaut que pour les QCM qui marquent leurs questions par code (thème 1). Les QCM du thème 2 marquent `EN`/`ID`, ceux des projets du thème 3 ne marquent pas ou vivent ailleurs. Le rapport le dit « non mesurable » au lieu d'inventer un zéro. **Décision** : adopter la convention `c:"Cx.y"` partout (règle candidate) — alors la preuve se mesure chaque lundi.
- **Dérive des générateurs (P2)** — 11 lexiques et une page de 3e_C9.2 changeraient à la régénération : les lexiques ont reçu des retouches à la main (constat déjà écrit le 23/09 : 4e_C1.1, 4e_C1.4, C8.1) ; le script `build_tp.py` de l'atelier CAO ne se lance pas sans scénario (le rapport l'appelle mal, à corriger dans l'outil). **Vague « générateurs » : reporter chaque retouche dans la source, puis régénérer.**
- **Contrôles (P2)** — `controle_regle4` : un bouton QCM à 54 % d'une page ; `controle_schemas` : 1 schéma avec 10 ✘ (règle n°315). Deux PR courtes.
- **Matrice (P3)** — 107 codes annotés ; familles les plus fréquentes : QCM, provenance des médias, images lourdes, différenciation, manipulation réelle (n°58). À reprendre après les P1/P2, par famille.

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
| `controle_squelette.mjs`, `controle_hors_ligne.mjs`, `controle_impression.mjs`, `controle_verrous.mjs`, `controle_contraste_liens.mjs`, `controle_code_colore.mjs` | non exécutés (lancer `--complet`) | | |

*Exécutés à part le 07/11/2026 au soir, sur les mêmes pages (branches des PR #608 et #610, fusionnées) : `controle_squelette`, `controle_hors_ligne`, `controle_impression`, `controle_verrous` ✅ ; `controle_contraste_liens` page par page sur les 72 pages touchées ✅. `controle_code_colore` : non exécuté ce soir. Le rapport du lundi les relance tous (`--complet`).*

## 4. Dérive des générateurs

| Générateur | Sortie | Dernière ligne |
|---|---|---|
| `build.py` | ✅ 0 | cahiers : 3 page(s) |
| `build_atelier.py` | ✅ 0 | écrit : atelier_3e_C7.1_planification_taches.html (92029 o) |
| `build_tp.py tp_5e_de_onshape.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_5e_de_onshape.html |
| `build_tp.py tp_5e_de_calottes.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_5e_de_calottes.html |
| `build_tp.py tp_4e_socle_assemblage.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_4e_socle_assemblage.html |
| `build_tp.py tp_3e_boitier_etanche.json` | ✅ 0 | Étape suivante : python3 verif_guidage.py tp_3e_boitier_etanche.html |
| `generer_les_quatre_pages.py` | ✅ 0 | écrit : sequence_3e_C9.2-C8.3_station_4_recette.html 182 Ko |
| `_outils/generer_lexique.py --tous theme-1-objets-systemes-usages-interactions theme-2-structure-fonctionnement-comportement theme-3-creation-conception-realisation-innovations` | ✅ 0 | 5e_C9.1                                                     30 notions → lexique_5e_C9.1.html |

Fichiers qu'une régénération changerait (12) — une retouche faite à la main sur ces pages sera écrasée :

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
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.2/sequence_3e_C9.2-C8.3_station_1_besoin-et-algorithme.html`

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

## 6. Décisions pour Pascal

- [ ] Ordre des vagues : P1 d'abord, puis une règle d'or par vague (la plus nombreuse en premier), puis les P3 ?
- [ ] Pour chaque règle qui tombe sur toute une famille : corriger le contrôle, ou les pages ?
- [ ] Les codes COUVERT sans preuve : ajouter deux questions au QCM du lot principal, ou retirer la mutualisation ?
- [ ] Les QCM non marqués par code : adopter la convention `c:"Cx.y"` partout (règle d'or candidate), pour que la preuve se mesure ?
- [ ] Les codes À VÉRIFIER (thème 3 : 3e_C7.1, 3e_C7.2, 4e_C8.1, 5e_C7.1) : qui regarde, et quand ?
- [ ] Ordre proposé par Fable pour les vagues (une par semaine et par thème) : **V1** l'exemption n°317/318 dans le contrôle n°300 (une PR d'outil, tout de suite) ; **V2** la famille C7/C8 sur l'ancien gabarit, par niveau, avec sa conversion n°300 (3 vagues) ; **V3** la conversion n°300 des autres pages, dans l'ordre des classeurs de progression (ce qui passe en classe le plus tôt d'abord) ; **V4** les 4 pages ponctuelles (n°301, n°23) ; **V5** générateurs (reporter les retouches des 11 lexiques et de 3e_C9.2 dans leurs sources) ; **V6** les deux contrôles rouges (regle4, schemas) ; **V7** la matrice, par famille (P3). D'accord, ou un autre ordre ?
- [ ] n°23 : couper une activité de 4e_C2.1 et 4e_C7.1, ou annoncer une séance de plus ?

