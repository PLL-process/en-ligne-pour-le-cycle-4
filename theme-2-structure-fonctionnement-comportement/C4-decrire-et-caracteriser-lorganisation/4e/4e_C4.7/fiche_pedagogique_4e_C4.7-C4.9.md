# Fiche pédagogique / inspection — SOS serre : l'objet connecté muet (Packet Tracer)

## Identification

| Champ | Valeur |
|---|---|
| Niveau | 4e (programme 2024, applicable rentrée 2026-2027) |
| Codes | 4e_C4.7 · 4e_C4.8 · 4e_C4.9 (atelier réseau dédié, complément de l'îlot C4) |
| Thème | Thème 2 — Structure, fonctionnement, comportement |
| Compétence parente | C4 — Décrire et caractériser l'organisation d'un OST |
| Référentiel | BO n°9 du 29/02/2024 · codes arbitrés par `_outils/data_competences.py` (règle n°21) |
| Domaines du socle | D1 « Les langages pour penser et communiquer » (lire un plan d'adressage comme un document technique, rédiger un diagnostic en 6 lignes) · D2 « Les méthodes et outils pour apprendre » (coopération pilote/copilote, revue de plan croisée, fichier .pkt nommé et rangé) · D4 « Les systèmes naturels et les systèmes techniques » (conception du plan d'adressage, démarche de diagnostic) — détail par activité dans la séquence |
| CRCN | **2.3 Collaborer** et **5.2 Développer des documents multimédia / résoudre en équipe** : compétences explicitement citées par le programme 2024 pour ces codes. **5.1 Résoudre des problèmes techniques** travaillée en complément — repère verbatim « Identifier des problèmes techniques liés à un environnement informatique. » (niv. 2 consolidé, niv. 3 visé : l'élève élabore SA démarche ; cartouche règle n°7 en act. 4 et défi sans procédure en séance 4) |
| Logiciel embarqué | Cisco Packet Tracer **8.2** (vérifié en conditions réelles) — doctrine « obligatoire sur classique » |
| Durée | 4 séances de 55 min |

## Sous-compétences

| Code | Intitulé officiel | Activités | QCM |
|---|---|---|---|
| 4e_C4.7 | Paramétrer une adresse IP fixe pour ajouter un objet connecté à un réseau local. | Passeport, 1, 3 | 10 q |
| 4e_C4.8 | Résoudre des problèmes pour assurer la communication entre les différents terminaux dans un réseau informatique (simulation ou réseau local déconnecté du réseau pédagogique). | 2, 4, Intervention réelle | 10 q |
| 4e_C4.9 | Compléter une simulation fournie pour valider le comportement d'un réseau informatique. | 5, Défi sans tutoriel | 10 q |

## Prérequis

Séquence 5e « Le réseau de la salle techno » (5e_C4.7-C4.8) : composants, topologie en étoile, lecture
d'une adresse « rue + maison », premier ping. La séance 3 de « SOS jardin connecté » (4e_C4.1→C4.9) peut
précéder ou suivre : l'atelier approfondit les mêmes codes. Fonctionne aussi en autonomie : l'activité 2
reprend en version courte les gestes de construction.

## Garde-fou de progressivité (4e = paramétrer et dépanner)

Vocabulaire INTRODUIT : adresse fixe (statique) vs DHCP (et réservation DHCP, en approfondissement),
passerelle (gateway), masque de sous-réseau (lecture 255.255.255.0), plan d'adressage, familles de pannes
(adressage / liaison / masque), démarche de diagnostic, fiche d'intervention, PDU/scénario de simulation,
verdict Successful.
Vocabulaire EXCLU (réservé 3e) : routeur, table de routage, protocole de routage, adresse publique/privée.
Progressivité du dépôt : décrire (5e) → **paramétrer une IP fixe et dépanner (4e, ce lot)** → routage
Internet (3e, « Internet jusqu'à Sainte-Luce » + atelier routage MQ→NY).

## Situation déclenchante et problématique

- **Situation** : la serre du jardin connecté du collège, à Sainte-Luce. Un capteur d'ambiance neuf,
  correctement branché, n'envoie aucune mesure — et l'imprimante à étiquettes est muette. M. Firmin
  missionne la classe : concevoir le plan d'adressage, paramétrer l'adresse fixe (passerelle comprise),
  et dépanner avec méthode — dans le simulateur, jamais sur le réseau pédagogique.
- **Problématique** : *Comment ajouter un objet connecté à un réseau local — et comment retrouver, avec
  méthode, la panne qui l'empêche de communiquer ?*

## Déroulé

S1 (55 min) : passeport réseau — 5 questions de diagnostic sans note, avec capsule de rattrapage 5e —
puis CONCEPTION guidée de SON plan d'adressage (recette en 4 étapes : recenser, rue, numéros uniques + .1
réservé, masque), production écrite, revue croisée, puis plan de référence en correction (act. 1).
S2 (55 min) : montage express du banc d'essai — recette A→G, ou départ direct depuis `4e_serre_DEPART.pkt`
(câblé, adresses vides) si le temps manque (act. 2) ; adressage des 4 terminaux avec passerelle et LA preuve
n°1 — `ping 192.168.20.50` vers le capteur qu'on vient d'adresser — puis deux preuves complémentaires aux
valeurs réellement observées (act. 3).
S3 (55 min) : la clinique du réseau — panne « mauvaise rue » (192.168.21.50) avec la boucle du dépanneur,
le mini-simulateur à verrou et les phrases guidées « J'observe / Je pense / Le test montre » (act. 4) ;
**intervention réelle** : les trois fichiers `4e_serre_PANNE_A/B/C.pkt` à diagnostiquer, fiche d'intervention
en 6 lignes.
S4 (55 min) : panne « liaison coupée » (Port Status Off) + validation par simulation sur le fichier fourni
`4e_serre_TECHNO-C4.pkt` (act. 5) ; **défi SANS tutoriel** — prouver la communication capteur↔serveur sans
procédure sous les yeux, en justifiant le test choisi ; bilan, auto-positionnement par code, QCM 30 q.

Un **mode essentiel** (bouton en tête de page) masque référentiel, corrections et approfondissements pour
les élèves que la densité de la page met en difficulté.

## Outils, versions, sécurité

Packet Tracer 8.2 (compte Cisco de classe à préparer AVANT la séance : la fenêtre de connexion est
obligatoire). Mini-simulateur « clinique du réseau » intégré à la page (hors ligne, aucune donnée envoyée).
Versions : 🅰 **matériel réel sur réseau ISOLÉ** — soit l'observation d'une étiquette IP d'un objet du collège
(**observation seulement, on ne touche jamais au réseau pédagogique**), soit, si l'établissement dispose d'un
switch dédié non relié au réseau pédagogique, un TP à 2 PC + switch (192.168.50.10 / .20, puis panne provoquée
192.168.51.20) ; 🅱 Packet Tracer (cœur de l'atelier) ; 🅲 sans
matériel — plan papier + schémas + clinique intégrée. Aucune manipulation électrique : tout est logiciel.

## Différenciation, inclusion, accessibilité

Règle « concevoir guidé, comme une recette » : l'élève conçoit SON plan avant de voir la référence, chaque
étape essentielle est illustrée par une figure fidèle au logiciel avec explication exhaustive. Binômes à
rôles tournants ; aides ×2 par activité ; corrections exhaustives ; exercices en listes déroulantes
exclusivement (DYS) ; navigation clavier + skip-link ; reduced-motion respecté (clinique comprise) ;
impression A4 ; minuteur QCM désactivable ; vocabulaire FR/EN ; langue calibrée 13 ans.

## Évaluation

Formatif : passeport d'entrée sans note (S1), vérificateurs par activité, production de concepteur exigée
(act. 1), verrou expérientiel de la clinique (act. 4), diagnostic rédigé, fiche d'intervention en 6 lignes
(S3), justification du test choisi au défi (S4), QCM 30 q avec bilan par compétence (report LSU direct sur
les 3 codes). Auto-positionnement par code.
Évaluation pratique proposée (10 min, S4) : « Serre de Rivière-Salée — intervention n°47 » — un des trois
fichiers PANNE remis à l'élève, diagnostic + réparation + fiche d'intervention avec preuve du re-test ;
grille à 3 niveaux (fragile / satisfaisante / très bonne) dans la synthèse professeur. **Aucun corrigé
d'évaluation n'est publié** : les trois pannes sont documentées dans la seule synthèse professeur.
Sommative écrite : à construire par l'enseignant sur un objet transféré (ex. ajouter une caméra au réseau
du CDI) — **aucun corrigé sommatif dans le dépôt public**.

## Traces et preuves (honnêteté du lot)

Les 14 figures sont des reconstitutions SVG originales CC0 dessinées d'après nos sessions réelles Packet
Tracer 8.2 (06-07/08/2026, poste enseignant) : palette et choix du matériel, choix du câble droit, renommage
et enregistrement, fenêtre IP Configuration avec passerelle, transcriptions ping exactes (`<1ms` à `12ms`,
moy. 5 ms, TTL=128), ping de preuve vers le capteur, panne « mauvaise rue » (`Request timed out` ×4,
100% loss), panne « liaison coupée » (triangles rouges, Port Status Off), bascule Realtime/Simulation et
Add Simple PDU, mode Simulation (Event List). **Aucune capture d'écran propriétaire n'est reproduite**
(règle n°1).
Cinq fichiers Packet Tracer accompagnent le lot, tous construits ET vérifiés au ping sur le poste
enseignant : `4e_serre_DEPART.pkt` (câblé, adresses vides), `4e_serre_TECHNO-C4.pkt` (maître, 5 équipements
adressés, pings validés), `4e_serre_PANNE_A.pkt` (mauvaise rue, 100% loss vérifié),
`4e_serre_PANNE_B.pkt` (Port Status Off, triangle rouge), `4e_serre_PANNE_C.pkt` (masque 255.255.255.240,
100% loss vérifié). La panne « doublon d'adresse » n'a pas pu être fabriquée : Packet Tracer refuse la
saisie d'une IP déjà utilisée — elle reste traitée à l'oral.
