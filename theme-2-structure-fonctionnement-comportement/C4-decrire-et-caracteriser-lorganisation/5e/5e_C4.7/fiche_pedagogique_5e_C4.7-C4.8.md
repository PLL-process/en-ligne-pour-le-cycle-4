# Fiche pédagogique / inspection — Le réseau de la salle techno (Packet Tracer)

## Identification

| Champ | Valeur |
|---|---|
| Niveau | 5e (programme 2024, applicable rentrée 2026-2027) |
| Codes | 5e_C4.7 · 5e_C4.8 (approfondissement dédié « réseaux » de l'îlot C4) |
| Thème | Thème 2 — Structure, fonctionnement, comportement |
| Compétence parente | C4 — Décrire et caractériser l'organisation d'un OST |
| Référentiel | BO n°9 du 29/02/2024 · codes arbitrés par `_outils/data_competences.py` (règle n°21) |
| Domaines du socle | D2 « Les méthodes et outils pour apprendre » (coopération pilote/copilote, jeu de rôles, outils numériques) · D4 « Les systèmes naturels et les systèmes techniques » (conception-réalisation du schéma, démarche scientifique du doublon) — détail par activité dans la séquence |
| CRCN | 5.1 Résoudre des problèmes techniques (niv. 2, cartouche règle n°7 en act. 5) · 5.2 travaillée non évaluée |
| Logiciel embarqué | Cisco Packet Tracer **8.2** (version vérifiée en conditions réelles) — doctrine « obligatoire sur classique » |
| Durée | 3 séances de 55 min |

## Sous-compétences

| Code | Intitulé officiel | Activités | QCM |
|---|---|---|---|
| 5e_C4.7 | Identifier les composants qui constituent un réseau local (terminaux, commutateurs, liaisons filaires et sans fil (WiFi)) et sa topologie. | 2, 3 | 16 q |
| 5e_C4.8 | Justifier la nécessité d'identifier les terminaux pour communiquer sur un réseau local (activité débranchée et vérification par un outil de simulation). | 1, 4, 5 | 14 q |

## Prérequis

Séquence-îlot « Le lampadaire intelligent » (5e_C4.1→C4.8) recommandée en amont — ses activités 5-6 posent
la première rencontre avec le réseau du collège. Le présent atelier fonctionne aussi en autonomie :
**aucun vocabulaire réseau n'est supposé connu** (première découverte : chaque mot est introduit par le jeu
ou par le schéma, jamais par une définition parachutée).

## Garde-fou de progressivité (5e = première découverte)

Vocabulaire INTRODUIT : terminal, commutateur, liaison filaire / sans fil (WiFi), point d'accès, topologie
(étoile), adresse IP (lecture « rue + numéro de maison »), SSID, ping.
Vocabulaire EXCLU (réservé 4e/3e) : masque de sous-réseau (montré uniquement comme « case qui se remplit
toute seule »), passerelle, routeur, serveur, table de routage, protocole, débit. Progressivité du dépôt :
décrire (5e, ce lot) → paramétrer une IP fixe et dépanner (4e, « SOS jardin connecté ») → routage Internet
(3e, « Internet jusqu'à Sainte-Luce »).

## Situation déclenchante et problématique

- **Situation** : salle de technologie, Sainte-Luce. L'imprimante de la salle imprime le compte rendu d'un
  autre élève ; M. Firmin, gestionnaire du réseau du collège, missionne la classe : reconstruire le réseau de
  la salle dans Packet Tracer — tablette et smartphone compris — et prouver que chaque message arrive au bon
  appareil.
- **Problématique** : *Comment organiser et identifier les appareils de la salle pour que chaque message
  arrive, à coup sûr, au bon destinataire ?*

## Déroulé

S1 : jeu du facteur débranché — prénoms, doublon, enveloppe sans nom (act. 1) ; CONCEPTION guidée de son
propre schéma (recette en 4 étapes, règle n°22) puis lecture du schéma de référence comme correction, et
les 4 mots du réseau (act. 2). S2 : construction complète dans Packet Tracer 8.2 — guide inclusif A→H
(règle n°20) avec figures reconstituées d'après le vrai logiciel, binômes pilote/copilote, 4 relevés 🔎 faits
dans le logiciel, sauvegarde `reseau_5X_NOM_Prenom.pkt` (act. 3). S3 : adresses IP par l'analogie de la rue,
table .10→.50 (act. 4) ; preuves — ping filaire vs WiFi, enveloppe du mode Simulation, « panne interdite » du
doublon d'adresse, mini-simulateur intégré à verrou expérientiel (act. 5) ; bilan, auto-positionnement par
code, QCM 30 q.

## Outils, versions, sécurité

Packet Tracer 8.2 (compte Cisco de classe à préparer AVANT la séance : la fenêtre de connexion est
obligatoire). Mini-simulateur d'enveloppe intégré à la page (hors ligne, aucune donnée envoyée).
Versions : 🅰 observation réelle des prises et de la borne de la salle — **observation seulement, on ne
touche jamais au réseau pédagogique** ; 🅱 Packet Tracer (cœur de l'atelier) ; 🅲 sans matériel — jeu du
facteur + schémas + mini-simulateur. Aucune manipulation électrique : tout est logiciel.

## Différenciation, inclusion, accessibilité

Pratique exhaustivement guidée « comme une recette » (règle n°22) : l'élève conçoit son schéma avant de
voir la référence, et pose les appareils selon SON plan dans Packet Tracer. Guide logiciel inclusif A→H
sans étape implicite, chaque geste illustré par une figure fidèle au logiciel
(règle n°20) ; binômes à rôles tournants ; aides ×2 par activité ; corrections exhaustives ; exercices en
listes déroulantes exclusivement (DYS) ; navigation clavier + skip-link ; reduced-motion respecté (y compris
par l'animation du mini-simulateur) ; impression A4 ; minuteur QCM désactivable ; vocabulaire FR/EN ;
langue calibrée 12 ans.

## Évaluation

Formatif : vérificateurs par activité (encoches ✔/✘, messages gradués), 4 relevés logiciels, verrou
expérientiel du mini-simulateur, QCM 30 q avec bilan par compétence (report LSU direct sur les 2 codes).
Auto-positionnement par code en fin de séquence. Sommative : à construire par l'enseignant sur un objet
transféré (ex. le réseau du CDI) — **aucun corrigé sommatif dans le dépôt public**.

## Traces et preuves (honnêteté du lot)

Les figures des activités 3-5 sont des reconstitutions SVG originales CC0 dessinées d'après des captures
réelles de Packet Tracer 8.2 effectuées sur poste enseignant (session du 05/08/2026) : menus de câblage,
24 ports du 2960, SSID, module WPC300N, IP Configuration, transcription ping exacte (`<1ms` filaire,
`57-260 ms` WiFi), Event List `0.001 PC0 / 0.002 Switch0 / 0.003 PC1`. Le fichier maître
`5e_reseau_local_TECHNO-C4.pkt` (7 équipements adressés, ping validé) accompagne le lot.
