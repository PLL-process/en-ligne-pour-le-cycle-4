# Fiche pédagogique / inspection — Le pont numérique Martinique → New York (Packet Tracer)

## Identification

| Champ | Valeur |
|---|---|
| Niveau | 3e (programme 2024, applicable rentrée 2026-2027) |
| Codes | 3e_C4.7 · 3e_C4.8 (atelier routage dédié, complément de la séquence-îlot 3e_C4.7) |
| Thème | Thème 2 — Structure, fonctionnement, comportement |
| Compétence parente | C4 — Décrire et caractériser l'organisation d'un OST |
| Référentiel | BO n°9 du 29/02/2024 · codes arbitrés par `_outils/data_competences.py` (règle n°21) |
| Domaines du socle | D2 « Les méthodes et outils pour apprendre » (jeu de rôle coopératif du poste-frontière, binômes pilote/copilote, fichier .pkt nommé et rangé) · D4 « Les systèmes naturels et les systèmes techniques » (conception du schéma à deux réseaux, démarche expérimentale preuve/contre-épreuve) — détail par activité dans la séquence |
| CRCN | 5.1 Résoudre des problèmes techniques (niv. 3 — l'élève monte, prouve et contre-éprouve son propre pont ; cartouche règle n°7 en act. 4) · 1.3 travaillée non évaluée |
| Logiciel embarqué | Cisco Packet Tracer **8.2** (vérifié en conditions réelles) — doctrine « obligatoire sur classique » |
| Durée | 3 séances de 55 min |

## Sous-compétences

| Code | Intitulé officiel | Activités | QCM |
|---|---|---|---|
| 3e_C4.7 | Identifier et représenter la circulation d'une information dans le réseau Internet. | 1, 4, 5 | 12 q |
| 3e_C4.8 | Justifier la nécessité d'un protocole de routage pour faire communiquer plusieurs réseaux (activité débranchée, table de routage donnée). | 2, 3, 5 | 18 q |

## Prérequis

Séquence 4e « SOS serre » (4e_C4.7-C4.9) : adresse IP fixe, masque, **passerelle** (le routeur lui donne
enfin un corps), ping, familles de pannes. La séquence-îlot 3e « Internet jusqu'à Sainte-Luce »
(dossier `3e_C4.7`) peut précéder ou suivre : elle traite les mêmes codes côté Internet mondial,
l'atelier les traite côté construction réelle du pont. Fonctionne aussi en autonomie : l'activité 3
reprend pas à pas tous les gestes de montage.

## Garde-fou de progressivité (3e = franchir la frontière)

Vocabulaire INTRODUIT : routeur (poste-frontière), interfaces G0/0-G0/1, table de routage, route
statique, prochain saut (next hop), rue-pont /30, câble croisé, TTL, tracert, protocole de routage.
Réinvesti de 4e : adresse fixe, masque, passerelle, ping, Port Status, mode Simulation.
Conformité au libellé : l'argumentation du protocole passe par une **activité débranchée** (act. 2)
avec **table de routage donnée** — la table réelle du montage, recopiée telle quelle.

## Situation déclenchante et problématique

- **Situation** : le club journal du collège de Sainte-Luce monte un partenariat avec une école
  partenaire de New York (bibliothèque NYPL) : les articles doivent voyager du réseau du collège
  jusqu'au réseau américain. Deux réseaux, un océan — la classe construit et prouve le pont numérique.
- **Problématique** : *Comment un message franchit-il la frontière entre deux réseaux — et pourquoi
  Internet a-t-il besoin d'un protocole de routage ?*

## Déroulé

S1 : CONCEPTION guidée de SON schéma à deux réseaux (recette 4 étapes : deux rues, un routeur par porte,
la rue-pont, les commutateurs restent), production écrite, puis schéma de référence en correction
(act. 1) ; jeu du poste-frontière avec la table DONNÉE — transmettre / distribuer / détruire — et
justification rédigée de la nécessité du protocole (act. 2). S2 : construction complète du pont dans
Packet Tracer — recette A→H : deux réseaux, deux routeurs 1941, câble croisé, 2×2 interfaces, routes
statiques miroir (act. 3). S3 : les preuves — ping (TTL=126), tracert (3 sauts), valeurs réellement
mesurées (act. 4) ; le film en mode Simulation (Event List 0.000→0.010 s) + contre-épreuve « route
effacée » sur le mini-simulateur à verrou (act. 5) ; bilan, auto-positionnement par code, QCM 30 q.

## Outils, versions, sécurité

Packet Tracer 8.2 (compte Cisco de classe à préparer AVANT la séance : la fenêtre de connexion est
obligatoire). Mini-simulateur « le poste-frontière à l'épreuve » intégré à la page (hors ligne, aucune
donnée envoyée). Versions : 🅰 observation réelle — `tracert` vers un site lointain sur un poste
autorisé, **observation seulement, jamais de modification du réseau pédagogique** ; 🅱 Packet Tracer
(cœur de l'atelier) ; 🅲 sans matériel — schémas + jeu débranché + simulateur intégré (le fichier
`3e_routage_MQ_NY_TECHNO-C4.pkt` sert alors de corrigé à lire). Aucune manipulation électrique :
tout est logiciel.

## Différenciation, inclusion, accessibilité

Règle « concevoir guidé, comme une recette » : l'élève conçoit SON schéma avant de voir la référence,
chaque étape essentielle est illustrée par une figure fidèle au logiciel avec explication exhaustive.
Binômes à rôles tournants ; aides ×2 par activité ; corrections exhaustives ; exercices en listes
déroulantes exclusivement (DYS) ; navigation clavier + skip-link ; reduced-motion respecté (simulateur
compris) ; impression A4 ; minuteur QCM désactivable ; vocabulaire FR/EN ; langue calibrée 14 ans.

## Évaluation

Formatif : vérificateurs par activité, production de concepteur exigée (act. 1), justification rédigée
du protocole (act. 2), verrou expérientiel du poste-frontière — les DEUX passages, avec et sans route —
(act. 5), QCM 30 q avec bilan par compétence (report LSU direct sur les 2 codes). Auto-positionnement
par code. Sommative : à construire par l'enseignant sur un objet transféré (ex. relier le réseau du
collège à celui de la mairie de Sainte-Luce) — **aucun corrigé sommatif dans le dépôt public**.

## Traces et preuves (honnêteté du lot)

Les figures sont des reconstitutions SVG originales CC0 dessinées d'après notre session réelle Packet
Tracer 8.2 (07/08/2026, poste enseignant) : montage complet à deux routeurs 1941 construit à distance,
fenêtres Config (G0/0 `192.168.10.1`, Port Status On, journal `no shutdown` → `changed state to up`),
fenêtre Static Routes (`192.168.30.0/24 via 10.0.0.2` et sa route miroir), transcriptions exactes
(ping : 2 `Request timed out` puis `Reply… TTL=126` ; second ping 4/4, 0% loss, 0-4 ms ; tracert :
3 sauts `192.168.10.1 → 10.0.0.2 → 192.168.30.10`, `Trace complete`), Event List horodatée
(0.000 → 0.010 s, verdict Successful). Le fichier maître `3e_routage_MQ_NY_TECHNO-C4.pkt`
(montage validé en conditions réelles) accompagne le lot.
