# Corrections des chaînes d’énergie — 21 octobre 2026

## Résultat

Six schémas harmonisés : lampadaire de 5e, jardin connecté de 4e, alimentation autonome de 3e à élaborer, station d’alerte de 3e, Book Train de 4e et assistance du vélo-cargo de 5e. Les fonctions sont dans les blocs, les composants en dessous, les formes d’énergie sur les flèches. Les batteries portent l’annotation « Énergie chimique stockée ».

- Solaire : régulation de charge reliée au panneau et à la branche batterie ; échanges électriques de charge et décharge identifiés.
- Jardin : commande des actionneurs, énergie hydraulique à la sortie de la pompe et circuit d’eau distinct.
- Station à élaborer : repères 1 à 5 conservés ; batterie en branche ; alimentation secteur adaptée et sélection de source distinguées. Les intrus sont définis par le périmètre de l’alimentation.
- Station d’alerte : commande par les sorties/interfaces, sans supposer l’absence d’un transistor intégré ; A1 analogique/CAN distinct de D2 logique.
- Book Train : modèle fonctionnel, contrôle de puissance dans DISTRIBUER ; version incorporée, alternatives accessibles et téléchargements draw.io complets/à compléter synchronisés.
- Vélo : contrôleur dessiné et raccordé, quatre fonctions correspondant au moteur de moyeu ; scène 6 synchronisée avec son bandeau et sa narration. Le bandeau reste masqué aux scènes 1 à 5.

Les consignes, corrigés et questions illustrées directement concernés sont adaptés aux schémas corrigés.

## Narration et audio

« La batterie stocke de l’énergie chimique et fournit de l’énergie électrique. Le contrôleur distribue cette énergie au moteur, qui la convertit en énergie mécanique. Dans le moyeu arrière, le moteur entraîne la roue et aide à déplacer le vélo et sa charge. »

Nouvelle prise Piper/SIWIS, même voix et mêmes réglages ; 14,63 secondes. Opus et MP3 de secours. Scènes 1 à 5 inchangées à l’octet. La nouvelle prise est à écouter ; aucune validation humaine de sa diction n’est revendiquée. La traçabilité et les empreintes sont enregistrées dans `voix.json`.

## Vérifications

Les commandes sont exécutées depuis le dossier du lot correspondant, sauf la vérification transversale depuis la racine.

| Vérification | Résultat |
|---|---|
| `python _outils/verifier_chaines_energie.py` | 41/41 |
| Géométrie du vélo, `node …/_generation/figure_iso_velo_cargo/build.mjs` | audit passed : aucun défaut géométrique détecté |
| Lampadaire : `node tests_5e_C4.1-C4.8_sequence.mjs` | 30/30 |
| Lampadaire QCM : `node tests_5e_C4.1-C4.8_qcm.mjs` | 25/25 |
| Jardin : `node tests_4e_C4.1-C4.9.mjs` | 35/35 |
| Station énergie : `node tests_3e_C4.1-C4.2.mjs` | 23/23 |
| Station programmée : `node tests_3e_C9.2-C8.3.mjs` | 135/135 |
| Voix du vélo : `python tests_voix_velo_cargo.py` | 24/24 |
| Lot Shanghai : `python tests_5e_C3.1-C3.4_shanghai.py` | 28/29 : échec préexistant décrit ci-dessous |

Quatre suites JavaScript utilisaient `new URL(import.meta.url).pathname` comme chemin de disque ; elles utilisent désormais `fileURLToPath`, pour une exécution correcte sous Windows et Linux.

### Limite préexistante du test Shanghai

Le test « chaque zone de rédaction a sa version étayée (n°31) » exige exactement 8 zones et 8 étayages. Le fichier avant correction contient déjà 10 zones et 9 étayages ; les mêmes comptes sont observés après correction. Ce point extérieur aux schémas et à l’audio reste signalé, sans revendiquer un succès global de cette suite.

### Contrôles de rendu

Textes dans les cadres et sans chevauchements sur les six SVG ; formes d’énergie hors des blocs de fonction ; titres et descriptions accessibles ; fond blanc à l’impression des cinq schémas reconstruits ; dimensions vérifiées dans les objets HTML du site servi localement. Le lecteur joue le nouveau fichier de la scène 6 sans erreur JavaScript. Les générateurs sont relancés et leur stabilité est vérifiée.


## Reprise Fable (21 octobre 2026) — convention rétablie, liste des changements

La PR #485 a retiré, dans les cinq schémas d'information et d'énergie, la convention « information en haut, énergie en bas, l'ordre descend »
(titres, descriptions, repères de chaînes, pieds de schéma, textes alternatifs, légendes). La reprise la **rétablit**, par le générateur
`_outils/regenerer_chaines_energie.py`, en la combinant avec la présentation fonctions / composants / énergies sur les flèches :
titre « …l'information (en haut) commande l'énergie (en bas) », chaînes repérées « en haut (elle décide) » / « en bas (elle obéit) »,
flèche d'ordre étiquetée « l'ordre descend », pied de schéma, `<desc>` qui commence par la convention. Les textes des pages (alt, description,
légende) disent de nouveau « En haut… En bas… ». `verifier_chaines_energie.py` contrôle maintenant que la convention est **dite et dessinée**
(chaîne d'information au-dessus de la chaîne d'énergie).

Corrections de placement faites au passage (étiquettes qui se posaient sur un trait ou sous un autre bloc) : lampadaire (charge / décharge,
ordre d'allumage), jardin, station (ordres de commande), Book Train.

### Activités changées (avant → après)

| Lot | Avant | Après |
|---|---|---|
| **5e_C4.1** lampadaire | Activité « remets les constituants dans l'ordre » : quatre listes à numéroter 1 à 4 (attendu : batterie 2, panneau 1, LED 4, régulateur + interrupteur 3) | « associe les constituants à leurs fonctions » : quatre listes de fonctions (attendu : batterie = STOCKER / ALIMENTER, panneau = CONVERTIR la lumière en électricité, LED = CONVERTIR l'électricité en lumière, régulateur + interrupteur = RÉGULER la charge / DISTRIBUER vers les LED). Consigne, production attendue, aide, corrigé et trace écrite suivent. |
| **4e_C4.1** jardin | Régulateur : « DISTRIBUER l'énergie électrique en protégeant la batterie » ; pompe : « …énergie mécanique (pousser l'eau) » ; électrovanne : « DISTRIBUER l'eau vers le bon bac » ; transformation de la pompe : électrique → mécanique ; trajet : … → mécanique | Régulateur : « RÉGULER la charge et protéger la batterie » ; pompe : « …énergie hydraulique (mettre l'eau en mouvement) » ; électrovanne : « OUVRIR ou FERMER un passage d'eau » ; pompe : électrique → hydraulique ; trajet : … → hydraulique. Batterie : « stocke de l'énergie chimique : conversion électrique vers chimique à la charge, puis inverse à la décharge ». Options et corrigés suivent. |
| **3e_C4.1** station (gabarit) | Position 1 « CAPTER + CONVERTIR » · 2 « STOCKER » · 3 « RÉGULER + DISTRIBUER » · 4 « CONVERTIR POUR ALIMENTER » · 5 « SECOURS (avant la coupure) » ; « Suis le chemin de l'énergie… » ; « Intrus » | 1 « CONVERTIR (lumière en électricité) » · 2 « STOCKER / ALIMENTER (branche batterie) » · 3 « RÉGULER la charge » · 4 « ADAPTER la tension » · 5 « DISTRIBUER : sélectionner la source disponible » ; « Repère le trajet… La batterie est une branche » ; « Hors du périmètre de l'alimentation » (ampoule, haut-parleur) |
| **Book Train** | Figure à quatre blocs (réseau 480 V, 24 V continu…) ; QCM n°16 (image), n°18 (parcours de l'énergie) | Figure fonctionnelle (ALIMENTER / DISTRIBUER / CONVERTIR / TRANSMETTRE) ; copie élève « à compléter » (4 fonctions, 5 énergies) ; téléchargements draw.io synchronisés ; QCM n°18 refait |
| **3e_C9.2** station | Description des deux chaînes (« En haut… En bas… ») ; ordre « atterrit sur CONVERTIR » ; **encadré « Deux questions que le schéma soulève »** et **planche des trois cas** (`ordre_preactionneur_trois_cas.svg`, avec sa description et la règle « l'ordre atterrit sur le premier bloc de la chaîne d'énergie qu'il commande ») | Descriptions réécrites ; l'ordre arrive sur DISTRIBUER ; **l'encadré et la planche des trois cas sont retirés de la page** (le fichier SVG reste dans le dossier et dans le manifeste, sans plus être affiché). Un encadré « Un même composant peut appartenir aux deux analyses » les remplace. |
| **5e_C3.1** vélo-cargo | Quatre cases ; scène 6 : « Source, puis forme, puis transformation… » ; prise 6 validée à l'oreille | Bandeau fonctionnel, contrôleur dans le dessin ; scène 6 : « La batterie stocke de l'énergie chimique… » ; **nouvelle prise 6, non écoutée**, scènes 1 à 5 inchangées à l'octet |

### QCM changés : avant → après, et bonne réponse

L'indice de la bonne réponse (A/B/C/D) **n'a changé nulle part** ; ce qui change, c'est l'énoncé et donc le **contenu** de la bonne réponse.

| QCM | N° | Avant | Après | Bonne réponse |
|---|---|---|---|---|
| lampadaire 5e (36 q.) | 6 | « Quel est le bon ordre de la chaîne d'énergie du lampadaire ? » → panneau → batterie → régulateur → LED | « Quel trajet correspond à l'alimentation des LED sur le schéma ? » → panneau → régulateur → interrupteur → LED | **changée** (le contenu) |
| lampadaire 5e | 8 | « …le bloc « régulateur + interrupteur commandé »… » | « …l'interrupteur commandé qui alimente les LED ? » | identique |
| lampadaire 5e | 14 | explication | explication réécrite | identique |
| jardin 4e (30 q.) | 1 | « …le panneau solaire a pour fonction de… » → « ALIMENTER : la lumière devient courant » | « …que fait le panneau solaire ? » → « il convertit l'énergie lumineuse en énergie électrique » | **changée** |
| jardin 4e | 3 | « Dans la POMPE, quelle transformation… » → électrique → mécanique | « Quelle conversion réalise l'électropompe… » → électrique → hydraulique | **changée** |
| jardin 4e | 4 | « Le trajet COMPLET des natures d'énergie… » → lumineuse → électrique → chimique → mécanique | « Si l'énergie passe par le stockage… » → lumineuse → électrique → chimique stockée → électrique → hydraulique | **changée** |
| jardin 4e | 5 | « La batterie transforme-t-elle l'énergie comme la pompe ? » → non : elle la STOCKE, puis la restitue | « Quel rôle distingue la batterie de la pompe ? » → la batterie stocke l'énergie ; la pompe fournit de l'énergie à l'eau | **changée** |
| station 3e (30 q.) | 2 | « Quel est le bon ordre de la chaîne d'énergie autonome ? » → panneau → batterie → régulateur → convertisseur | « Quelle organisation respecte le rôle du régulateur et de la batterie ? » → panneau → régulateur ; batterie reliée au régulateur ; sélection de source → adaptation à 5 V | **changée** |
| Book Train 4e (30 q.) | 16 | (image) | (image) | identique |
| Book Train 4e | 18 | « Quelle suite décrit le parcours de l'énergie ? » → réseau alternatif 480 V → continu 24 V → rail → moteur → wagonnet | idem, option juste : réseau → alimentation adaptée → commande de puissance → moteur → transmission → déplacement | **changée** |

3e_C9.2 : le QCM n'est pas touché.

**Provenance des QCM.** Aucun de ces quatre QCM n'a de banque ni de générateur dans `_outils/` (`banks_*.py`, `qcm_generator.py` ne les contiennent pas) :
le HTML est la source, comme pour les autres QCM du thème 2. La #485 les a donc modifiés **à la main**, sauf celui du Book Train, retouché
par des remplacements de texte dans `regenerer_chaines_energie.py` (rejouables, et rejoués : aucun écart). Il n'y a rien à « refaire par le générateur » ;
la vérification est celle des contrôles de banque, d'effectifs et d'en-tête de QCM (verts).
