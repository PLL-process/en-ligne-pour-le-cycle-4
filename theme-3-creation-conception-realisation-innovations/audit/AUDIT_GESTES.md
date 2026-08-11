# Audit des gestes d'outil — règle d'or n°93

*Engendré par `audit/audit_gestes.py`. Aucun nombre n'est écrit à la main.*

182 pages lues, 63 mettent un logiciel entre les mains de l'élève.
Parmi elles, **21 séquences destinées aux élèves** ne parlent pas d'au moins
un des quatre gestes : *ouvrir · nommer · retrouver · sortir*.

| Séquence | Logiciel(s) | Geste(s) absent(s) |
|---|---|---|
| `sequence_3e_C4.7-C4.8_internet_sainte_luce.html` | Filius, Packet Tracer | ouvrir, nommer, retrouver |
| `sequence_4e_C9_jardin-programme.html` | Vittascience | ouvrir, retrouver, sortir |
| `sequence_5e_C4.1-C4.8_lampadaire_intelligent.html` | Vittascience, Filius, Arduino | ouvrir, nommer |
| `sequence_3e_C6.1-C6.3_programmer_alerte.html` | Vittascience, Arduino | ouvrir, retrouver |
| `sequence_4e_C6.1-C6.3_ajuster_programme_jardin.html` | Vittascience, Arduino | ouvrir, retrouver |
| `sequence-jardin-connecte-arrosage-automatique.html` | Vittascience | ouvrir, retrouver |
| `sequence_5e_C6.1-C6.3_programmer_lampadaire.html` | Vittascience, Scratch, Arduino | ouvrir, retrouver |
| `sequence_3e_C7_capteur-confort-ny.html` | Onshape, Vittascience | ouvrir, sortir |
| `sequence_4e_C7_jardin-conception.html` | Onshape | ouvrir, sortir |
| `sequence_3e_C9.1_variables_types_systemes.html` | Vittascience, Arduino | ouvrir, nommer |
| `sequence_5e_C9.1-C9.3_boite_etiquetee.html` | Vittascience | ouvrir, nommer |
| `sequence_3e_C1.1-C1.4_tsinghua_feux.html` | Tableur | ouvrir |
| `sequence_4e_C1.1-C1.3_tsinghua_feux.html` | Arduino, Tableur | ouvrir |
| `sequence_5e_C1.1-C1.6_chengdu_air.html` | Tableur | ouvrir |
| `sequence_5e_C1.2_sainte_luce_freinage.html` | Tableur | ouvrir |
| `sequence_5e_C3.1-C3.4_shanghai.html` | Tableur | ouvrir |
| `sequence_3e_C4.3-C4.6_station_alerte_cyclonique.html` | Vittascience, Arduino, Tableur | ouvrir |
| `sequence_3e_C4.7-C4.8_pont_numerique_packet_tracer.html` | Packet Tracer | ouvrir |
| `sequence_4e_C4.7-C4.9_sos_serre_packet_tracer.html` | Packet Tracer | ouvrir |
| `sequence_5e_C4.7-C4.8_reseau_local_packet_tracer.html` | Filius, Packet Tracer | ouvrir |
| `sequence_5e_C7_mini-projet-objet.html` | Onshape, Vittascience | ouvrir |

## Comment lire ce tableau

Une ligne ne dit pas « c'est mal fait ». Elle dit « le sujet n'est pas abordé
dans cette page », et donc qu'un élève arrivé en cours de cycle — muté, ou dont
l'année précédente n'a pas eu lieu telle qu'on l'imaginait — n'y trouvera pas de
quoi s'en sortir seul.

À l'inverse, une page absente de ce tableau n'est pas innocentée : « comme tu
l'as vu en 5e » satisfait le script et viole la règle n°93. Le contrôle mécanique
trouve où regarder ; il ne remplace pas la lecture.

## L'ordre de traitement proposé

Les séquences de **programmation** viennent en tête : Vittascience produit un
fichier que l'élève doit retrouver d'une séance à l'autre, et c'est là que le
travail perdu coûte le plus cher. Viennent ensuite les séquences **réseau**
(Packet Tracer, Filius), puis celles qui n'utilisent le tableur qu'en appui.
