# Sources des médias — Lot 4e_C4.7 · C4.8 · C4.9 « SOS serre : l'objet connecté muet »

Tous les médias sont des **créations originales** (règle images v2 : image-objet).
Aucune image de manuel, de Google Images ou de site tiers ; aucun hotlinking.

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
