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
