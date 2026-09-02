# Sources des médias — Lot 4e_C4.7 · C4.8 · C4.9 « SOS serre : l'objet connecté muet »

Tous les médias sont des **créations originales** (règle images v2 : image-objet).
Aucune image de manuel, de Google Images ou de site tiers ; aucun hotlinking.
*(Cette affirmation a été prise en défaut le 11 août 2026 pour un fichier ; voir la
correction en fin de document. Elle est de nouveau exacte.)*

Particularité de ce lot (règles n°1 + n°20) : les quatorze SVG sont des **reconstitutions
fidèles dessinées d'après nos sessions réelles de Cisco Packet Tracer 8.2** (06-07/08/2026,
poste enseignant, montage `4e_serre_TECHNO-C4.pkt` fourni avec le lot). Aucune capture
d'écran propriétaire n'est reproduite : chaque figure est un dessin original CC0 qui
reprend la disposition, les intitulés et les VALEURS RÉELLEMENT MESURÉES dans le logiciel
(transcriptions ping `<1ms`→`12ms` TTL=128, `Request timed out` ×4 et 100% loss,
Port Status Off, chronologie de l'Event List). Cisco et Packet Tracer sont des marques
de Cisco Systems, Inc., citées à titre descriptif.

| Fichier | Type | Usage pédagogique (règle v2) | Licence | Poids |
|---|---|---|---|---|
| `Images/pt_palette_choisir_materiel.svg` | SVG original (Fable) | image-objet : la palette du logiciel — ① Network Devices ② Switches ③ le 2960, et End Devices pour les terminaux (act. 2, aide au démarrage) | CC0 | ~8 Ko |
| `Images/pt_choisir_cable_fa0.svg` | SVG original (Fable) | image-objet : le bon câble (Copper Straight-Through entouré, croisé barré) et la fenêtre de choix du port FastEthernet0 + encadré « triangles orange ~30 s » (act. 2) | CC0 | ~9 Ko |
| `Images/pt_renommer_enregistrer.svg` | SVG original (Fable) | image-objet : Config → Display Name pour renommer, puis File → Save As `serre_4A_NOM_Prenom.pkt` — leçon « sauvegarder AVANT les pannes » (act. 2) | CC0 | ~8 Ko |
| `Images/pt_ping_capteur_50.svg` | SVG original (Fable) | image-objet : LA preuve de C4.7 — `ping 192.168.20.50`, 4 Reply, TTL=128, 0% loss, avec les encadrés « pourquoi CE ping » et « premier ping : ne panique pas » (act. 3) | CC0 | ~9 Ko |
| `Images/pt_realtime_simulation_pdu.svg` | SVG original (Fable) | image-objet : la bascule Realtime/Simulation cerclée + l'enveloppe Add Simple PDU fléchée, avec les astuces vécues en session (act. 5) | CC0 | ~9 Ko |
| `Images/conception_plan_recette.svg` | SVG original (Fable) | image-objet : la recette de conception du plan d'adressage en 4 vignettes (act. 1, règle n°22, QCM q7) | CC0 | ~6 Ko |
| `Images/plan_adressage_serre.svg` | SVG original (Fable) | image-objet : le plan de référence à lire — rue, porte .1, maisons .10/.30/.50/.100 (act. 1, QCM q9, synthèses) | CC0 | ~7 Ko |
| `Images/serre_topologie_etoile.svg` | SVG original (Fable) | image-objet : le montage terminé à comparer au sien — étoile, prises, triangles verts (act. 2) | CC0 | ~7 Ko |
| `Images/pt_ip_configuration_passerelle.svg` | SVG original (Fable) | image-objet : la fenêtre d'adressage avec la ligne Default Gateway en évidence + analogie de la porte (act. 3, QCM q2) | CC0 | ~7 Ko |
| `Images/pt_ping_reussi_serre.svg` | SVG original (Fable) | image-objet : transcriptions ping réelles à interpréter — 0% loss, temps 0-12 ms (act. 3) | CC0 | ~7 Ko |
| `Images/pt_panne_mauvaise_rue.svg` | SVG original (Fable) | image-objet : la transcription réelle de la panne — 2 réussites puis 100% loss, indice « 21 » (act. 4, QCM q3) | CC0 | ~7 Ko |
| `Images/demarche_diagnostic.svg` | SVG original (Fable) | image-objet : la boucle du dépanneur symptôme→hypothèse→test→remède (act. 4, QCM q1, synthèses) | CC0 | ~6 Ko |
| `Images/pt_panne_liaison_coupee.svg` | SVG original (Fable) | image-objet : le montage avec la liaison rouge + loupe Port Status Off (act. 5, QCM q6) | CC0 | ~7 Ko |
| `Images/pt_simulation_enveloppe.svg` | SVG original (Fable) | image-objet : l'enveloppe en transit + Event List horodatée + verdict Successful (act. 5, QCM q4) | CC0 | ~7 Ko |
| `4e_serre_DEPART.pkt` | Fichier Packet Tracer (Fable, sur poste Pascal) | fichier de DÉPART : les 5 équipements sont câblés (liens verts), les adresses IP, masques et passerelles sont **vides** — l'élève n'a qu'à adresser et prouver (act. 2/3) | CC0 (contenu du montage) | ~55 Ko |
| `4e_serre_TECHNO-C4.pkt` | Fichier Packet Tracer (Fable, sur poste Pascal) | montage maître FOURNI (contrat 4e_C4.9) : 5 équipements, plan .10→.100 appliqué, pings validés — support de l'act. 5 et corrigé enseignant | CC0 (contenu du montage) | ~55 Ko |
| `4e_serre_PANNE_A.pkt` | Fichier Packet Tracer (Fable, sur poste Pascal) | panne « adressage » RÉELLE : capteur en 192.168.21.50, ping vers .50 → 100% loss **vérifié en session** (intervention réelle, S3) | CC0 (contenu du montage) | ~55 Ko |
| `4e_serre_PANNE_B.pkt` | Fichier Packet Tracer (Fable, sur poste Pascal) | panne « liaison » RÉELLE : Port Status de l'imprimante sur Off, triangle rouge visible (intervention réelle, S3) | CC0 (contenu du montage) | ~55 Ko |
| `4e_serre_PANNE_C.pkt` | Fichier Packet Tracer (Fable, sur poste Pascal) | panne « masque » RÉELLE : capteur en 255.255.255.240, ping vers .50 → 100% loss **vérifié en session** — la panne la plus formatrice (intervention réelle, S3) | CC0 (contenu du montage) | ~55 Ko |

Le mini-simulateur « la clinique du réseau » (act. 4) est un SVG interactif embarqué dans
la page, création originale du lot. Alt/desc présents dans chaque SVG (title + desc,
role="img"). Transcriptions du terminal : valeurs réellement mesurées lors de nos sessions
de pilotage (pings 0-12 ms, moyenne 5 ms ; pannes provoquées, testées au ping puis réparées en conditions
réelles, les 07 et 08/08/2026).

**Honnêteté technique.** La panne « doublon d'adresse IP » n'a pas pu être fabriquée en fichier : l'interface
de Packet Tracer 8.2 refuse la saisie d'une adresse déjà utilisée sur le réseau (« This address is already
used in the network. ») et vide le champ. Le doublon reste donc traité à l'oral et en bonus. La panne C
(mauvais masque) a été retenue à sa place — elle est réelle, vérifiée, et pédagogiquement plus riche.

---

## Correction du 11 août 2026 — dix images de sites tiers remplacées

Ce document affirmait, en tête, « aucune image de manuel, de Google Images ou de
site tiers ; aucun hotlinking ». C'était faux pour un fichier : le QCM
`qcm_xxl_40_reseaux_ip_nfc_rfid_zigbee.html` appelait **dix images hébergées
ailleurs** — Wikimedia, Amazon, iStock, YouTube, et quatre sites commerciaux —
et huit copies `.jpg` de ces mêmes images traînaient dans `Images/` sans être
déclarées ici. Une déclaration de médias fausse est plus grave qu'une image
manquante : elle empêche la prochaine relecture de voir le problème.

Les dix images sont remplacées par **dix schémas originaux CC0**, dessinés pour
ce dépôt. Le choix du schéma plutôt que de la photo n'est pas seulement légal :
une photo montre *un* boîtier, un schéma montre la **structure** — et c'est la
structure qu'on enseigne.

| Fichier | Type | Ce qu'il montre | Licence |
|---|---|---|---|
| `Images/reseau_routeur_lan_internet.svg` | SVG original (Fable) | le routeur à la jonction du réseau local et d'Internet | CC0 |
| `Images/reseau_switch_ports.svg` | SVG original (Fable) | un commutateur et ses huit prises : il distribue, il ne sort pas du réseau | CC0 |
| `Images/reseau_filaire_vs_sansfil.svg` | SVG original (Fable) | filaire contre sans-fil, avec ce que chacun coûte et rapporte | CC0 |
| `Images/reseau_zigbee_maillage.svg` | SVG original (Fable) | le maillage : chaque objet relaie ceux qui sont trop loin de la passerelle | CC0 |
| `Images/reseau_nfc_paiement.svg` | SVG original (Fable) | le NFC, où la portée très courte fait la sécurité | CC0 |
| `Images/reseau_rfid_portique.svg` | SVG original (Fable) | l'étiquette RFID sans pile, alimentée par le portique lui-même | CC0 |
| `Images/reseau_bluetooth_paire.svg` | SVG original (Fable) | le Bluetooth : un lien entre deux appareils, pas un réseau | CC0 |
| `Images/reseau_rj45_cable.svg` | SVG original (Fable) | quatre paires torsadées, huit broches — et pourquoi elles sont torsadées | CC0 |
| `Images/reseau_local_schema.svg` | SVG original (Fable) | le réseau local complet, d'Internet jusqu'aux appareils | CC0 |

Les huit fichiers `*_hd.jpg` et `doc3_schema_parcours.png` qui n'étaient déclarés
nulle part ont été **supprimés** du dépôt.

## Post-scriptum du 31/08/2026 — la suppression annoncée n'avait pas eu lieu

La phrase ci-dessus était écrite au passé, et elle était fausse : **les neuf fichiers étaient
toujours là** le 31 août 2026, vingt jours plus tard. `_outils/controle_medias.py`, écrit ce
jour-là, les a relevés — huit médias qu'aucun `SOURCES_MEDIAS.md` ne nommait, et neuf que plus
aucune page n'affichait.

Ouverts et regardés avant de trancher :

- les huit `*_hd.jpg` sont des rasters de 3 à 223 Ko, de 225×225 à 1600×1600 px, dont
  **trois ne sont même pas des JPEG** — un PNG et deux WebP portant l'extension `.jpg`, la
  signature d'une image enregistrée depuis un navigateur ;
- `doc3_schema_parcours.png` est un **extrait de manuel scolaire** : la légende « DOC 3 —
  Structure d'un réseau informatique » dans la mise en page d'un éditeur, avec sa typographie
  et son cadre de couleur.

Ils sont **retirés pour de bon** ce 31/08/2026. Ils restent dans l'historique git si la
décision doit être revue. La leçon vaut d'être écrite : *une suppression annoncée au passé
dans un document n'est pas une suppression* — c'est une intention, et personne ne la vérifie.

## Les dix schémas de remplacement — et l'accusation qui visait le mauvais commit

Le relevé du 31/08 constatait que les dix SVG originaux du 11/08 n'étaient affichés par
**aucune page**, et en concluait qu'ils avaient été « dessinés et documentés, mais jamais
câblés ».

**C'était faux, et l'historique git le dit.** Le commit `ca35a77f` du 11/08 les a bel et bien
posés, un par un, à la place exacte des dix images tierces : `git show ca35a77f` montre dix
lignes retirées (Wikimedia, Amazon, iStock, YouTube, quatre sites commerciaux) et dix lignes
ajoutées, chacune avec son `alt`. Le remplacement a été fait, et il a fonctionné.

Ce sont les **commits suivants** qui les ont perdus. Le 12/08, `834480c0` — « l'éclairage
automatique refait, le *XXL 40* scindé en trois » — a reconstruit ce QCM de 77 questions en
trois QCM de 30, pilotés par un tableau `QUESTIONS` au lieu de HTML statique. La refonte a
gardé les questions et **laissé les images derrière elle**.

La leçon n'est donc pas celle qu'on avait écrite :

> **Une refonte perd ce qu'elle ne recopie pas, et le silence qui suit ressemble à un
> travail jamais fait.** Vingt jours plus tard, le relevé a accusé le commit qui avait
> raison, parce que c'était le dernier à avoir parlé de ces fichiers.

## Les neuf schémas de réseau sont recâblés (02/09/2026)

Ils ne sont pas replacés au hasard : **la version d'avant la scission dit où chacun était**,
et le câblage suit ce que la page faisait déjà.

| Schéma | Question d'origine (avant la scission) | Où il revient |
|---|---|---|
| `reseau_routeur_lan_internet.svg` | « Le routeur sert principalement à… » | QCM 1/3, Q11 — mot pour mot |
| `reseau_switch_ports.svg` | « Un commutateur (switch) sert à… » | QCM 1/3, Q12 — mot pour mot |
| `reseau_bluetooth_paire.svg` | « Le vidéoprojecteur de la salle est relié en… » | QCM 1/3, Q24 — mot pour mot |
| `reseau_rj45_cable.svg` | « Quel câble pour relier un PC au switch ? » | QCM 1/3, Q3 — l'héritière |
| `reseau_filaire_vs_sansfil.svg` | « Coche les liaisons filaires » | QCM 1/3, Q25 — comparer câble et Wi-Fi |
| `reseau_local_schema.svg` | « À partir du schéma *Document 3*, choisis le parcours d'une trame » | QCM 1/3, Q28 — lire un schéma |
| `reseau_zigbee_maillage.svg` | « Zigbee utilise typiquement la bande… » | QCM 3/3, Q7 — ce qu'apporte le maillage |
| `reseau_nfc_paiement.svg` | « NFC a une portée… » | QCM 3/3, Q21 — mot pour mot |
| `reseau_rfid_portique.svg` | « Donne un usage typique de la RFID » | QCM 3/3, Q23 — l'étiquette sans pile |

Chaque `alt` **transcrit ce qui est visible** — traits pleins, ondes, annotations, légendes —
et non ce qu'il faut en conclure : c'est la convention des sept questions illustrées du QCM
*SOS serre*, où l'image est un **document à lire pour répondre**, jamais une décoration.

## Le dixième schéma part au thème 1

`licences_symboles.svg` (©, CC, CC0, ™) illustrait la question « Dans une chanson, le droit
d'auteur protège… », qui **n'a pas survécu à la scission** : les trois QCM de ce lot parlent
de réseau local, d'adressage et de liaisons sans fil, pas de licences.

Les quatre questions du dépôt qui portent sur les licences vivent au **thème 1**, dans
`5e_C1.5/qcm_5e_C1.5-C1.6_le-compte-du-club.html` — dont la première demande mot pour mot :
*« Une image en ligne ne porte aucune mention de licence. Que faut-il en déduire ? »*, ce que
ce schéma répond en toutes lettres. Le fichier y est déplacé par une PR sœur du thème 1 ; il
est retiré d'ici par celle-ci.

