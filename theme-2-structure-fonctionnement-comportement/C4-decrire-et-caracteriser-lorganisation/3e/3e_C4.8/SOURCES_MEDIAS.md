# Sources des médias — Lot 3e_C4.7 · C4.8 « Le pont numérique Martinique → New York »

Tous les médias sont des **créations originales** (règle images v2 : image-objet).
Aucune image de manuel, de Google Images ou de site tiers ; aucun hotlinking.

Particularité de ce lot (règles n°1 + n°20) : les sept SVG sont des **reconstitutions
fidèles dessinées d'après notre session réelle de Cisco Packet Tracer 8.2** (07/08/2026,
poste enseignant, montage `3e_routage_MQ_NY_TECHNO-C4.pkt` fourni avec le lot — deux
routeurs 1941, câble croisé, routes statiques miroir, construit à distance et validé).
Aucune capture d'écran propriétaire n'est reproduite : chaque figure est un dessin
original CC0 qui reprend la disposition, les intitulés et les VALEURS RÉELLEMENT
MESURÉES dans le logiciel (ping 2 `Request timed out` puis `Reply… TTL=126` ; second
ping 4/4, 0% loss, 0-4 ms ; tracert 3 sauts `192.168.10.1 → 10.0.0.2 → 192.168.30.10` ;
Event List 0.000 → 0.010 s, verdict Successful ; journal IOS `no shutdown` →
`%LINK-5-CHANGED… changed state to up`). Cisco et Packet Tracer sont des marques de
Cisco Systems, Inc., citées à titre descriptif.

| Fichier | Type | Usage pédagogique (règle v2) | Licence | Poids |
|---|---|---|---|---|
| `Images/conception_deux_reseaux_recette.svg` | SVG original (Fable) | image-objet : la recette de conception du schéma à deux réseaux en 4 vignettes (act. 1, règle n°22) | CC0 | ~6 Ko |
| `Images/schema_deux_reseaux_mq_ny.svg` | SVG original (Fable) | image-objet : le schéma de référence à lire — deux réseaux, rue-pont /30, toutes les adresses (act. 1, QCM C4.7 q2, synthèses) | CC0 | ~7 Ko |
| `Images/table_routage_donnee.svg` | SVG original (Fable) | image-objet : les tables DONNÉES des deux routeurs réels + procédure du poste-frontière en 3 cas (act. 2 — conformité au libellé, QCM C4.8 q1) | CC0 | ~6 Ko |
| `Images/pt_config_interface_routeur.svg` | SVG original (Fable) | image-objet : la fenêtre Config G0/0 de R-MQ — Port Status On, 192.168.10.1, journal IOS jusqu'à `changed state to up` (act. 3, QCM C4.8 q14) | CC0 | ~7 Ko |
| `Images/pt_route_statique.svg` | SVG original (Fable) | image-objet : la fenêtre Static Routes — Network/Mask/Next Hop/Add, la ligne ajoutée, la commande `ip route`, le rappel du miroir (act. 3, QCM C4.8 q5) | CC0 | ~7 Ko |
| `Images/pt_ping_tracert_mq_ny.svg` | SVG original (Fable) | image-objet : les 3 preuves réelles — ping TTL=126, tracert 3 sauts, second ping 0% loss (act. 4, QCM C4.7 q5) | CC0 | ~8 Ko |
| `Images/pt_simulation_2routeurs.svg` | SVG original (Fable) | image-objet : l'enveloppe ICMP sur R-MQ + Event List horodatée 0.000→0.010 s + verdict Successful (act. 5, QCM C4.7 q8) | CC0 | ~9 Ko |
| `3e_routage_MQ_NY_TECHNO-C4.pkt` | Fichier Packet Tracer (Fable, sur poste Pascal) | montage maître : 2 réseaux, 2 routeurs 1941, routes statiques miroir, pings et tracert validés — corrigé enseignant et support de la version 🅲 | CC0 (contenu du montage) | ~57 Ko |

Le mini-simulateur « le poste-frontière à l'épreuve » (act. 5) est un SVG interactif
embarqué dans la page, création originale du lot (trajet en 6 arrêts, mode « sans
route » qui détruit l'enveloppe à R-MQ). Alt/desc présents dans chaque SVG (title +
desc, role="img"). Transcriptions du terminal : valeurs réellement mesurées lors de
notre session de pilotage à distance (montage construit, prouvé, sauvegardé).
