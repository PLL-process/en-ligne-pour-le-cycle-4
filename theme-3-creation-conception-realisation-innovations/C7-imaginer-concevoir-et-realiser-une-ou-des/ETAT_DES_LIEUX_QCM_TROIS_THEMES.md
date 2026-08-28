# État des lieux des QCM des trois thèmes

**Date** : 27 août 2026 · **Outil** : `audit_qcm_trois_themes.mjs`
**Reproduire** : `NODE_PATH=<node_modules> node audit_qcm_trois_themes.mjs --csv`

Cet outil ne corrige rien et ne juge rien. Il compte, sur les 46 QCM du
dépôt, ce que les règles d'or permettent de compter.

## Le chiffre qui commande tout le reste

> **945 questions sur 1086 — soit 87 % — ont pour bonne réponse la
> proposition la plus longue.**
>
> Sur **807 d'entre elles**, la bonne réponse dépasse la deuxième de plus de
> 20 % : l'écart se VOIT, sans lire.

Le hasard donnerait 25 %. Un élève qui n'ouvre aucun cours, ne lit aucune
question et coche systématiquement la ligne la plus longue obtient donc
**environ 87 %** sur l'ensemble du dépôt.

Ce n'est pas une imperfection de rédaction. C'est un défaut qui **inverse ce
que le QCM mesure** : il récompense l'élève qui a compris la mécanique du
questionnaire, et pénalise celui qui lit vraiment les quatre propositions.

La cause est la même partout, et elle vient d'une bonne intention : la bonne
réponse porte sa justification (« un rectangle : c'est un traitement, l'entrée
de l'information »), les distracteurs n'ont rien à justifier et tiennent en
quatre mots. On croit écrire une réponse claire ; on écrit une réponse
repérable. C'est la **règle d'or n°144**, née de cette mesure.

## Le tableau, QCM par QCM

`+long` = part des questions où la bonne réponse est la plus longue ·
`visib` = nombre de questions où l'écart dépasse 20 % · `absol` = tournures de
loi dans les réfutations et les « à retenir » (règle n°139) · `img` = questions
illustrées (règle n°1).

| QCM | q | +long | visib | A/B/C/D | absol | img |
|---|---:|---:|---:|---|---:|---:|
| **Thème 1** | | | | | | |
| `qcm_3e_C1.1-C1.4_tsinghua` | 30 | **100 %** | 30 | 8/7/7/8 | 8 | 11 |
| `qcm_4e_C1.1-C1.3_tsinghua` | 30 | **100 %** | 29 | 8/7/7/8 | 8 | 6 |
| `qcm_5e_C1.1-C1.6_chengdu` | 30 | **100 %** | 28 | 8/7/7/8 | 11 | 13 |
| `qcm_5e_C1.2_freinage` | 30 | 97 % | 27 | 8/7/7/8 | 8 | 8 |
| `qcm_3e_C2_pekin_borne` | 30 | 90 % | 25 | 8/7/7/8 | 12 | 5 |
| `qcm_5e_C2_shenzhen_station_velos` | 30 | 90 % | 24 | 8/7/7/8 | 4 | 5 |
| `qcm_3e_C3.1-C3.4_shenzhen` | 30 | 90 % | 24 | 8/7/7/8 | 5 | 1 |
| `qcm_4e_C2_hangzhou_borne` | 30 | 87 % | 26 | 8/7/7/8 | 3 | 5 |
| `qcm_systemes_information_donnees` | 30 | 87 % | 21 | **7/16/6/1** | · | 3 |
| `qcm_4e_C3.1-C3.3_hangzhou` | 30 | 77 % | 15 | 8/7/7/8 | 5 | 2 |
| `qcm_5e_C3.1-C3.4_shanghai` | 30 | 77 % | 21 | 8/7/7/8 | 3 | 3 |
| **Thème 2** | | | | | | |
| `qcm_3e_C4.7-C4.8_pont_numerique` | 30 | **100 %** | 30 | 8/7/7/8 | 8 | 6 |
| `qcm_4e_C6.1-C6.3_ajuster_programme_jardin` | 30 | **100 %** | 30 | 8/7/7/8 | 6 | 3 |
| `qcm_5e_C6.1-C6.3_programmer_lampadaire` | 30 | **100 %** | 30 | 7/7/8/8 | 7 | 3 |
| `qcm_4e_C4.1-C4.9_jardin_connecte` | 30 | **100 %** | 29 | 7/7/8/8 | 6 | 4 |
| `qcm_4e_C5.1-C5.3_depanner_jardin` | 30 | **100 %** | 29 | 8/7/7/8 | 11 | 4 |
| `qcm_5e_C5.1-C5.3_depanner_lampadaire` | 30 | **100 %** | 28 | 8/7/7/8 | 12 | 3 |
| `qcm_4e_C4.7-C4.9_sos_serre` | 30 | **100 %** | 27 | 8/7/7/8 | 3 | 7 |
| `qcm_3e_C4.7-C4.8_internet_sainte_luce` | 30 | 97 % | 27 | 8/7/8/7 | 5 | · |
| `qcm_3e_C6.2_auto_test` | 30 | 97 % | 28 | 8/7/7/8 | 8 | 3 |
| `qcm_3e_C6.1-C6.3_programmer_alerte` | 30 | 93 % | 28 | 7/8/7/8 | 3 | 6 |
| `qcm_3e_C5.1-C5.4_sos_station_reparer` | 32 | 91 % | 25 | 8/8/8/8 | 9 | 10 |
| `qcm_3e_C4.1-C4.2_energie_station` | 30 | 90 % | 27 | 8/8/7/7 | 3 | 3 |
| `qcm_book-train` | 30 | 90 % | 21 | 8/7/8/7 | 5 | 4 |
| `qcm_5e_C4.1-C4.8_lampadaire_intelligent` | 32 | 88 % | 26 | 8/8/8/8 | 5 | 6 |
| `qcm_5e_C4.7-C4.8_reseau_local` | 30 | 80 % | 19 | 8/7/7/8 | 5 | 6 |
| `qcm_3e_C4.3-C4.6_station_alerte_cyclonique` | 32 | 75 % | 14 | 8/8/8/8 | 2 | · |
| **Thème 3** | | | | | | |
| `qcm_5e_C9.1-C9.3_boite_etiquetee` | 30 | 97 % | 25 | 8/7/7/8 | 8 | 3 |
| `qcm_3e_C9.2-C8.3_station_alerte_cyclonique` | 30 | 93 % | 26 | 8/7/7/8 | 5 | 4 |
| `qcm_3e_C9.1_variables_types_systemes` | 30 | 90 % | 25 | 8/7/7/8 | 9 | 3 |
| `qcm_4e_C9_jardin-programme` | 30 | 83 % | 25 | 8/7/7/8 | 9 | 4 |
| `qcm_C7.1_planification_taches` | 30 | 70 % | 16 | 8/7/7/8 | 8 | 5 |
| `qcm_4e_C8_jardin-validation` | 30 | **60 %** | **0** | 8/7/7/8 | 3 | 3 |
| `qcm_4e_C7_jardin-conception` | 30 | **57 %** | **0** | 8/7/7/8 | 8 | 3 |
| `qcm_3e_C7_capteur-confort-ny` | 30 | **47 %** | **1** | 8/7/7/8 | 6 | 3 |
| `qcm_5e_C7_mini-projet` | 30 | **43 %** | **1** | 8/7/7/8 | 3 | 3 |

Les quatre dernières lignes sont celles du lot du 27 août. Elles montrent où
l'on peut arriver : de 100 % à 43-60 %, et de ~28 questions visiblement
déséquilibrées à 0 ou 1.

## Ce qui va bien, et qu'il faut dire

- **La répartition des bonnes réponses** (règle n°137) est tenue partout :
  8/7/7/8 ou équivalent sur 34 QCM sur 36. Le travail de l'été a porté.
- **Plus aucun « undefined »** affiché dans une correction : le lot de la
  veille a réglé le problème pour le Thème 3, et les Thèmes 1 et 2 n'étaient
  pas atteints (toutes leurs questions portent une erreur fréquente).
- **Aucune question incomplète** : explication, exemple et « à retenir » sont
  présents dans les 1086 questions lues.
- **Une seule banque d'ancienne génération** sans réfutation par distracteur.

## Les deux anomalies isolées

- **`qcm_systemes_information_donnees`** : répartition **7/16/6/1**. Seize
  bonnes réponses en position B, une seule en D. C'est la règle n°137 qui
  n'a jamais été appliquée à ce fichier — probablement parce que son moteur
  diffère et qu'il est passé au travers de `fix_r.js`.
- **Dix QCM que l'outil ne sait pas lire**, tous d'anciennes générations avec
  un moteur différent :
  `qcm_numerique_societe`, `qcm_cybersecurite_usage_raisonne`,
  `qcm_fonctionnement_objet`, `qcm_automatisation_premium`,
  `qcm_ecall_chaine_information`, `qcm_xxl_40_reseaux_ip_nfc_rfid_zigbee`,
  `qcm_algorigrammes_domotique`, `qcm_eclairage_automatique`,
  `qcm_jardin_connecte`, `qcm_python_variables`.
  Ils ne sont **pas** comptés comme sains : ils sont comptés comme non
  mesurés, ce qui n'est pas la même chose. Rien ne dit qu'ils échappent au
  biais — au contraire.

## Ce que ce document ne dit pas

Il ne dit rien de la **justesse pédagogique**. Aucune machine ne dit qu'un
distracteur est plausible, ni qu'une réfutation enseigne, ni qu'une question
mesure la compétence qu'elle prétend mesurer. Les 87 % mesurés ici disent
qu'un défaut de FORME rend les QCM devinables ; ils ne disent pas que le fond
est mauvais — la répartition tenue et la complétude des corrections suggèrent
plutôt l'inverse.

C'est aussi pour cela que le chantier vaut la peine : le fond est là, et il
est masqué par une mécanique qui permet de s'en passer.

## L'ordre de bataille proposé

Un lot par thème, parce que la garde-périmètre l'impose et parce que c'est la
bonne granularité pour une relecture.

| Lot | Portée | Questions | Ce qu'on y fait |
|---|---|---:|---|
| ~~**1**~~ | ~~Thème 3, les 5 QCM restants~~ | ~~150~~ | **fait le 27 août** — voir ci-dessous |
| **2** | Thème 1, 11 QCM lisibles | 330 | idem, plus la répartition de `qcm_systemes_information_donnees` |
| **3** | Thème 2, 16 QCM lisibles | 490 | idem |
| **4** | les 10 QCM non lisibles | ? | d'abord les rendre mesurables, ensuite les traiter |

Chaque lot porte sa propre mesure avant/après, et la suite de tests reçoit les
deux contrôles de longueur en cliquet — comme pour les quatre QCM du 27 août.


## Lot 1 — le Thème 3 est bouclé

Les cinq QCM restants ont été repris le 27 août. Le thème entier tient
désormais entre 40 % et 57 %, avec zéro ou une question visiblement
déséquilibrée par fichier.

| QCM | avant | après | visibles avant → après |
|---|---:|---:|---|
| `qcm_5e_C9.1-C9.3_boite_etiquetee` | 97 % | **43 %** | 25 → 0 |
| `qcm_3e_C9.2-C8.3_station_alerte_cyclonique` | 93 % | **47 %** | 26 → 1 |
| `qcm_3e_C9.1_variables_types_systemes` | 90 % | **47 %** | 25 → 1 |
| `qcm_4e_C9_jardin-programme` | 83 % | **40 %** | 25 → 1 |
| `qcm_C7.1_planification_taches` | 70 % | **50 %** | 16 → 0 |

Au-delà des longueurs, une vingtaine de distracteurs plaisantins ont été
remplacés — « pour user les boutons », « l'imprimer en grand », « que
l'ordinateur est fatigué », « Achetez un nouveau manège », « humeur du
testeur », « quand le professeur a le dos tourné ». Chaque remplacement a
emporté la réécriture de sa réfutation.

C'est en les remplaçant qu'est née la **règle n°148** : le meilleur
distracteur n'est pas une erreur, c'est une vérité mal placée. « Vérifier
qu'il s'exécute sans message d'erreur » est une vraie vérification, et elle
est insuffisante. Sa réfutation ne dit pas « c'est faux », elle dit « c'est
vrai, et ce n'est pas la question » — et c'est cette phrase-là qui enseigne.

**Total du dépôt : 87 % → 81 %.** Le reste tient dans les Thèmes 1 et 2, où
rien n'a encore été touché.
