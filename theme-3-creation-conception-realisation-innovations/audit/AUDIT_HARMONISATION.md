# Audit d'harmonisation — les règles d'or à l'échelle du dépôt

*Produit le 11 août 2026 par `audit_spiralaire.py`. Ce document est
**engendré**, jamais écrit à la main : il se régénère d'une commande, et
il ne peut donc pas mentir sur l'état réel du dépôt.*

```bash
# depuis la racine du dépôt
python3 theme-3-creation-conception-realisation-innovations/audit/audit_spiralaire.py \
    > theme-3-creation-conception-realisation-innovations/audit/AUDIT_HARMONISATION.md
```

## Ce qu'il faut lire en premier

Les chiffres ci-dessous ne sont pas une note. Ils disent **où appliquer la
logique spiralaire** que nous venons d'écrire, et dans quel ordre.

**L'ordre que je propose, du plus rentable au moins urgent :**

**1. La clé de voûte (n°87) — 31 séances.** C'est le chantier qui change
quelque chose pour l'élève. Toutes ces séances de 4e et de 3e s'appuient sur
un prérequis sans jamais rappeler ce que l'élève a **déjà produit**. Un élève
de 4e qui ouvre « Dépanner le jardin » ne sait pas qu'il a, l'an dernier,
câblé un capteur et lu sa valeur. Le travail est court par séance — un bloc de
trois paragraphes — mais il demande de **savoir ce qui précède**, donc de
remonter la progression. C'est là que se joue la cohérence du cycle.

**2. Les impasses (n°88) — 47 pages.** Presque toutes sont des synthèses et
des QCM sans barre de navigation : on y entre depuis une séquence et on ne
peut plus revenir. C'est mécanique, rapide, et ça se corrige par lot puisque
ces pages partagent leur gabarit.

**3. Les images absentes — 3 pages.** Ce sont les trois TP de CAO, dont les
captures restent à produire. Connu, en cours.

**4. Le bonus sans corrigé (n°86) — 1 page.** La dette annoncée à 23 blocs
s'est révélée bien plus faible que craint : la plupart des blocs bonus du
dépôt n'ont tout simplement pas de section `bonus` identifiable par le script.
**À vérifier à la main** avant de conclure — un chiffre bas peut vouloir dire
« tout va bien » ou « le script ne voit pas ».

**5. Le réseau (n°40) — 84 pages.** Dette ancienne et assumée : polices
Google, Vittascience. Une page qui appelle le réseau ne fonctionne pas dans
une salle sans connexion. Chantier groupé, à faire d'un coup, hors période de
classe.

## Une mise en garde sur ce que ce rapport ne dit pas

Un script détecte l'**absence** d'un bloc, jamais la **platitude** de son
contenu. Une séance peut porter un rappel spiralaire parfaitement conforme et
parfaitement inutile — « tu as vu les capteurs en 4e » coche la case et
n'apprend rien. Le vrai critère reste celui qu'on s'est donné : le rappel
nomme-t-il une **production** de l'élève, dit-il ce qui **change**, tient-il
debout pour celui qui n'était pas là ?

Ces trois questions-là ne se mesurent pas. Elles se lisent.

---

Constats de FAITS vérifiés sur les fichiers, pas de jugements pédagogiques.
**181 pages examinées.**

| Règle | Pages concernées |
|---|---|
| n°88 | **47** |
| n°87 | **31** |
| n°86 | **1** |
| images | **3** |
| n°40 | **84** |

## n°88 — une page se juge aussi sur ce qu'on peut en faire quand on y est arrivé

47 page(s).

- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/3e/3e_C1.1/Synthèses/synthese_eleve_3e_C1.1-C1.4.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/3e/3e_C1.1/Synthèses/synthese_professeur_3e_C1.1-C1.4.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/3e/3e_C1.5/qcm_numerique_societe.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/3e/3e_C1.5/sequence-numerique-societe-economie-environnement-sante.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.4/activite-bonus-cyber-immersive-2fa.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.4/qcm_cybersecurite_usage_raisonne.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.4/sequence-cybersecurite-protection-donnees.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.4/synthese_eleve_4e_C1.4.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.4/synthese_professeur_4e_C1.4.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.2/activite_crcn_donnees_freinage_5e_C1.2.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.3/qcm_systemes_information_donnees.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.3/sequence_C1.3-C1.4_SI_gestion_donnees.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.3/synthese_eleve_5e_C1.3-C1.4.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.3/synthese_professeur_5e_C1.3-C1.4.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.5/sequence_mutualisee_avec_4e_C1_4.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.6/sequence_mutualisee_avec_4e_C1_4.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/4e/4e_C2.1/qcm_fonctionnement_objet.html` — aucune barre de navigation — page sans sortie
- `theme-1-objets-systemes-usages-interactions/_reperes/carte_des_representations.html` — aucun retour vers une séquence
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/qcm_automatisation_premium.html` — aucune barre de navigation — page sans sortie
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.4/qcm_ecall_chaine_information.html` — aucune barre de navigation — page sans sortie
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.7/qcm_xxl_40_reseaux_ip_nfc_rfid_zigbee.html` — aucune barre de navigation — page sans sortie
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.2/entrainement_dnb_algorigrammes.html` — aucun retour vers une séquence
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.2/qcm_algorigrammes_domotique.html` — aucune barre de navigation — page sans sortie
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.2/qcm_eclairage_automatique.html` — aucune barre de navigation — page sans sortie
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.2/qcm_jardin_connecte.html` — aucune barre de navigation — page sans sortie
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.2/sequence-jardin-connecte-arrosage-automatique.html` — aucun retour vers une séquence
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/qcm_3e_C7_capteur-confort-ny.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/synthese_eleve_3e_C7.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/synthese_professeur_3e_C7.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.1/qcm_4e_C7_jardin-conception.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.1/synthese_eleve_4e_C7.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.1/synthese_professeur_4e_C7.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.1/qcm_5e_C7_mini-projet.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.1/synthese_eleve_5e_C7.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.1/synthese_professeur_5e_C7.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-cao/tp_modele_demonstration.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-planification/Synthèses/synthese_eleve_C7.1_planification.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-planification/Synthèses/synthese_professeur_C7.1_planification.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-planification/qcm_C7.1_planification_taches.html` — aucun retour vers une séquence
- `theme-3-creation-conception-realisation-innovations/C8-valider-les-solutions-techniques-par-des/4e/4e_C8.1/qcm_4e_C8_jardin-validation.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C8-valider-les-solutions-techniques-par-des/4e/4e_C8.1/synthese_eleve_4e_C8.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C8-valider-les-solutions-techniques-par-des/4e/4e_C8.1/synthese_professeur_4e_C8.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/qcm_python_variables.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/vittascience_variables.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/4e/4e_C9.1/qcm_4e_C9_jardin-programme.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/4e/4e_C9.1/synthese_eleve_4e_C9.html` — aucune barre de navigation — page sans sortie
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/4e/4e_C9.1/synthese_professeur_4e_C9.html` — aucune barre de navigation — page sans sortie

## n°87 (CLÉ DE VOÛTE) — toute séance qui s'appuie sur un prérequis s'ouvre par un rappel

31 page(s).

- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/3e/3e_C1.1/sequence_3e_C1.1-C1.4_tsinghua_feux.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.1/sequence_4e_C1.1-C1.3_tsinghua_feux.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/3e/3e_C2.1/sequence_3e_C2_pekin_borne.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/4e/4e_C2.1/sequence_4e_C2_hangzhou_borne.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/3e/3e_C3.1/sequence_3e_C3.1-C3.4_shenzhen.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/4e/4e_C3.1/sequence_4e_C3.1-C3.3_hangzhou.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.1/sequence_3e_C4.1-C4.2_energie_station.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.3/sequence_3e_C4.3-C4.6_station_alerte_cyclonique.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.7/sequence_3e_C4.7-C4.8_internet_sainte_luce.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.8/sequence_3e_C4.7-C4.8_pont_numerique_packet_tracer.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/atelier_pix_crcn_jardin.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/sequence_4e_C4.1-C4.9_jardin_connecte.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1_book-train/sequence_4e_C4.1-C4.2-C4.4_book-train.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.7/sequence_4e_C4.7-C4.9_sos_serre_packet_tracer.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/3e/3e_C5.1/sequence_3e_C5.1-C5.4_sos_station_reparer.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/4e/4e_C5.1/sequence_4e_C5.1-C5.3_depanner_jardin.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.1/sequence_3e_C6.1-C6.3_programmer_alerte.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.2/sequence_3e_C6.2_auto_test_station.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.1/sequence_4e_C6.1-C6.3_ajuster_programme_jardin.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/atelier_C7.1_planification_taches.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/sequence_3e_C7_capteur-confort-ny.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.2/tp_3e_boitier_etanche.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.6/tp_3e_boitier_etanche.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.1/atelier_C7.1_planification_taches.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.1/sequence_4e_C7_jardin-conception.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.2/tp_4e_socle_assemblage.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.6/tp_4e_socle_assemblage.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-3-creation-conception-realisation-innovations/C8-valider-les-solutions-techniques-par-des/4e/4e_C8.1/sequence_4e_C8_jardin-validation.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/sequence_3e_C9.1_variables_types_systemes.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/tp_mbot2_python.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/4e/4e_C9.1/sequence_4e_C9_jardin-programme.html` — séance de 4e/3e sans rappel de ce que l'élève a déjà produit

## n°86 — un bonus sans corrigé n'est pas un bonus, c'est un devoir non rendu

1 page(s).

- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.3/sequence_C1.3-C1.4_SI_gestion_donnees.html` — bloc bonus sans corrigé replié

## Images annoncées et absentes — les « fenêtres blanches »

3 page(s).

- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.4/activite-bonus-cyber-immersive-2fa.html` — 2 image(s) annoncée(s) et absente(s)
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/qcm_automatisation_premium.html` — 1 image(s) annoncée(s) et absente(s)
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1_book-train/sequence_4e_C4.1-C4.2-C4.4_book-train.html` — 1 image(s) annoncée(s) et absente(s)

## n°40 — une page doit fonctionner hors ligne

84 page(s).

- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/3e/3e_C1.5/sequence-numerique-societe-economie-environnement-sante.html` — appelle le réseau : fonts.googleapis.com, online-python-compiler.com, online-python.com
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.4/activite-bonus-cyber-immersive-2fa.html` — appelle le réseau : chat.openai.com, fonts.googleapis.com, www.online-python.com
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.4/sequence-cybersecurite-protection-donnees.html` — appelle le réseau : cdnjs.cloudflare.com, chat.openai.com, fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.1/Synthèses/synthese_eleve_3e_C4.1-C4.2.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.1/Synthèses/synthese_professeur_3e_C4.1-C4.2.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.1/qcm_3e_C4.1-C4.2_energie_station.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.1/sequence_3e_C4.1-C4.2_energie_station.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.3/Synthèses/synthese_eleve_3e_C4.3-C4.6.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.3/Synthèses/synthese_professeur_3e_C4.3-C4.6.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.3/qcm_3e_C4.3-C4.6_station_alerte_cyclonique.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.3/sequence_3e_C4.3-C4.6_station_alerte_cyclonique.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.7/Synthèses/synthese_eleve_3e_C4.7-C4.8.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.7/Synthèses/synthese_professeur_3e_C4.7-C4.8.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.7/qcm_3e_C4.7-C4.8_internet_sainte_luce.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.7/sequence_3e_C4.7-C4.8_internet_sainte_luce.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.8/Synthèses/synthese_eleve_3e_C4.7-C4.8_atelier.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.8/Synthèses/synthese_professeur_3e_C4.7-C4.8_atelier.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.8/qcm_3e_C4.7-C4.8_pont_numerique.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.8/sequence_3e_C4.7-C4.8_pont_numerique_packet_tracer.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/Synthèses/synthese_eleve_4e_C4.1-C4.9.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/Synthèses/synthese_professeur_4e_C4.1-C4.9.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/qcm_4e_C4.1-C4.9_jardin_connecte.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/qcm_automatisation_premium.html` — appelle le réseau : www.soundjay.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/sequence_4e_C4.1-C4.9_jardin_connecte.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1_book-train/Synthèses/synthese_eleve_4e_C4.1-C4.2-C4.4.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1_book-train/Synthèses/synthese_professeur_4e_C4.1-C4.2-C4.4.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1_book-train/qcm_book-train.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1_book-train/sequence_4e_C4.1-C4.2-C4.4_book-train.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.7/Synthèses/synthese_eleve_4e_C4.7-C4.9.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.7/Synthèses/synthese_professeur_4e_C4.7-C4.9.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.7/qcm_4e_C4.7-C4.9_sos_serre.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.7/qcm_xxl_40_reseaux_ip_nfc_rfid_zigbee.html` — appelle le réseau : i.ytimg.com, m.media-amazon.com, media.istockphoto.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.7/sequence_4e_C4.7-C4.9_sos_serre_packet_tracer.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/5e/5e_C4.1/Synthèses/synthese_eleve_5e_C4.1-C4.8.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/5e/5e_C4.1/Synthèses/synthese_professeur_5e_C4.1-C4.8.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/5e/5e_C4.1/qcm_5e_C4.1-C4.8_lampadaire_intelligent.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/5e/5e_C4.1/sequence_5e_C4.1-C4.8_lampadaire_intelligent.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/5e/5e_C4.7/Synthèses/synthese_eleve_5e_C4.7-C4.8.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/5e/5e_C4.7/Synthèses/synthese_professeur_5e_C4.7-C4.8.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/5e/5e_C4.7/qcm_5e_C4.7-C4.8_reseau_local.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/5e/5e_C4.7/sequence_5e_C4.7-C4.8_reseau_local_packet_tracer.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/3e/3e_C5.1/Synthèses/synthese_eleve_3e_C5.1-C5.4.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/3e/3e_C5.1/Synthèses/synthese_professeur_3e_C5.1-C5.4.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/3e/3e_C5.1/qcm_3e_C5.1-C5.4_sos_station_reparer.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/3e/3e_C5.1/sequence_3e_C5.1-C5.4_sos_station_reparer.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/4e/4e_C5.1/Synthèses/synthese_eleve_4e_C5.1-C5.3.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/4e/4e_C5.1/Synthèses/synthese_professeur_4e_C5.1-C5.3.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/4e/4e_C5.1/qcm_4e_C5.1-C5.3_depanner_jardin.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/4e/4e_C5.1/sequence_4e_C5.1-C5.3_depanner_jardin.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/5e/5e_C5.1/Synthèses/synthese_eleve_5e_C5.1-C5.3.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/5e/5e_C5.1/Synthèses/synthese_professeur_5e_C5.1-C5.3.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/5e/5e_C5.1/qcm_5e_C5.1-C5.3_depanner_lampadaire.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/5e/5e_C5.1/sequence_5e_C5.1-C5.3_depanner_lampadaire.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.1/Synthèses/synthese_eleve_3e_C6.1-C6.3.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.1/Synthèses/synthese_professeur_3e_C6.1-C6.3.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.1/qcm_3e_C6.1-C6.3_programmer_alerte.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.1/sequence_3e_C6.1-C6.3_programmer_alerte.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.2/Synthèses/synthese_eleve_3e_C6.2.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.2/Synthèses/synthese_professeur_3e_C6.2.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.2/entrainement_dnb_algorigrammes.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.2/qcm_3e_C6.2_auto_test.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.2/sequence_3e_C6.2_auto_test_station.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.1/Synthèses/synthese_eleve_4e_C6.1-C6.3.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.1/Synthèses/synthese_professeur_4e_C6.1-C6.3.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.1/qcm_4e_C6.1-C6.3_ajuster_programme_jardin.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.1/sequence_4e_C6.1-C6.3_ajuster_programme_jardin.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.2/sequence-jardin-connecte-arrosage-automatique.html` — appelle le réseau : fonts.googleapis.com, fr.vittascience.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/5e/5e_C6.1/Synthèses/synthese_eleve_5e_C6.1-C6.3.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/5e/5e_C6.1/Synthèses/synthese_professeur_5e_C6.1-C6.3.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/5e/5e_C6.1/qcm_5e_C6.1-C6.3_programmer_lampadaire.html` — appelle le réseau : fonts.googleapis.com
- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/5e/5e_C6.1/sequence_5e_C6.1-C6.3_programmer_lampadaire.html` — appelle le réseau : fonts.googleapis.com
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/sequence_3e_C7_capteur-confort-ny.html` — appelle le réseau : fonts.googleapis.com, fr.vittascience.com
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.1/sequence_4e_C7_jardin-conception.html` — appelle le réseau : fonts.googleapis.com
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.1/sequence_5e_C7_mini-projet-objet.html` — appelle le réseau : fonts.googleapis.com, fr.vittascience.com
- `theme-3-creation-conception-realisation-innovations/C8-valider-les-solutions-techniques-par-des/4e/4e_C8.1/sequence_4e_C8_jardin-validation.html` — appelle le réseau : fonts.googleapis.com
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/Synthèses/synthese_eleve_3e_C9.1.html` — appelle le réseau : fonts.googleapis.com
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/Synthèses/synthese_professeur_3e_C9.1.html` — appelle le réseau : fonts.googleapis.com
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/qcm_3e_C9.1_variables_types_systemes.html` — appelle le réseau : fonts.googleapis.com
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/sequence_3e_C9.1_variables_types_systemes.html` — appelle le réseau : fonts.googleapis.com, fr.vittascience.com
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/4e/4e_C9.1/sequence_4e_C9_jardin-programme.html` — appelle le réseau : fonts.googleapis.com, fr.vittascience.com
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/5e/5e_C9.1/Synthèses/synthese_eleve_5e_C9.1-C9.3.html` — appelle le réseau : fonts.googleapis.com
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/5e/5e_C9.1/Synthèses/synthese_professeur_5e_C9.1-C9.3.html` — appelle le réseau : fonts.googleapis.com
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/5e/5e_C9.1/qcm_5e_C9.1-C9.3_boite_etiquetee.html` — appelle le réseau : fonts.googleapis.com
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/5e/5e_C9.1/sequence_5e_C9.1-C9.3_boite_etiquetee.html` — appelle le réseau : fonts.googleapis.com, fr.vittascience.com

---

## Périmètre de cet audit

**Vérifié mécaniquement** : présence et validité des liens de navigation, présence
d'un rappel spiralaire sur les pages de 4e et de 3e, présence d'un corrigé dans les
blocs bonus, existence réelle des images annoncées, appels réseau.

**NON couvert** : la qualité du rappel — nomme-t-il une PRODUCTION ou seulement une
notion, dit-il ce qui change, est-il auto-suffisant ? La justesse des corrigés. La
pertinence des situations déclenchantes. Un script détecte l'absence d'un bloc, jamais
la platitude de son contenu. Ces jugements-là restent humains.
