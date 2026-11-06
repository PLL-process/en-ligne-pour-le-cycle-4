# Sources et médias — 5e_C1.3–C1.4

## Médias originaux

| Fichier | Usage | Statut | Poids indicatif |
|---|---|---|---|
| `Images/schema_systeme_information_velos.svg` | Comprendre le rôle des acteurs, données, traitements, réseau et stockage | SVG original créé pour le lot ; aucun média externe | < 3 Ko |
| `Images/arborescence_donnees_velos.svg` | Visualiser l’organisation des dossiers (dossiers dessinés, redessiné le 29/10/2026, règle d’or n°315) | SVG original créé pour le lot ; aucun média externe | < 3 Ko |
| `Images/extrait_donnees_velos.svg` | Question illustrée et règle de priorité | SVG original créé pour le lot ; aucun média externe | < 4 Ko |

Les SVG sont locaux, légers, imprimables en niveaux de gris et possèdent un titre, une description ou un texte alternatif dans les pages HTML.

## Données

`donnees_velos_hangzhou_simulees.csv` est un jeu entièrement inventé pour l’apprentissage. Les stations, identifiants et valeurs ne décrivent aucun service réel. Le fichier ne contient aucune donnée personnelle.

## Inspiration CRCN / PIX

Le *Cahier PIX 2026* a été consulté uniquement pour la progressivité des niveaux et les repères associés aux compétences CRCN 1.2 et 1.3. Aucun exercice, tableau, illustration ou correction éditoriale n’est reproduit. Les scénarios, données, consignes, corrections et médias du lot sont originaux.

## Retrait des anciens médias

Les sept fichiers `image_extraite_01.png` à `image_extraite_07.png`, lourds et sans documentation de licence suffisante, sont retirés du lot. Ils sont remplacés par les trois SVG originaux ci-dessus.

## Le huitième PNG, resté derrière (31/08/2026)

La section ci-dessus annonce le retrait des fichiers `image_extraite_01.png` à
`image_extraite_07.png`, « lourds et sans documentation de licence suffisante ». Sept commits
les ont retirés un par un. **`image_extraite_08.png` est resté** — 151 Ko, 662 × 259 px,
affiché par aucune page du lot.

Ouvert et regardé : c'est un **extrait de manuel scolaire** — une capture annotée d'un
gestionnaire de fichiers Windows, avec la légende « DOC. Visualisation d'un dossier dans un
gestionnaire de fichiers » dans la mise en page d'un éditeur. C'est exactement ce que la règle
images v2 interdit, et exactement le motif du retrait des sept autres.

Il est retiré à son tour. Le fichier reste dans l'historique git si la décision doit être
revue : `git show <commit-parent>:.../Images/image_extraite_08.png`.

## Six SVG présents mais employés par aucune page (relevé du 31/08/2026)

Ces six fichiers sont des **créations originales (Fable, CC0)**, du SVG écrit à la main, sans
raster embarqué ni référence distante. Ils sont documentés ici pour que leur licence ne dépende
de personne. Mais **aucune page du lot ne les affiche** — le lot n'emploie que les trois SVG du
tableau initial :

| Fichier | Titre porté par le SVG | Poids |
|---|---|---|
| `Images/systeme_information_cdi.svg` | Système d'information du CDI | ~2 Ko |
| `Images/arborescence_fichiers.svg` | Arborescence de fichiers | ~3 Ko |
| `Images/local_serveur_distant.svg` | Stockage local et serveur distant | ~2 Ko |
| `Images/capacites_stockage.svg` | Comparaison de capacités de stockage | ~2 Ko |
| `Images/strategie_sauvegarde.svg` | Stratégie de sauvegarde (copier / restaurer, redessiné le 29/10/2026, règle d’or n°315) | ~3 Ko |
| `Images/programme_python_annote.svg` | Programme Python annoté | ~2 Ko |

Deux d'entre eux — `arborescence_fichiers.svg` et `local_serveur_distant.svg` — traitent
précisément le sujet de l'extrait de manuel retiré ci-dessus. Ils sont peut-être les
remplaçants annoncés, dessinés puis jamais câblés dans la séquence. À trancher, pas à deviner.
`_outils/controle_medias.py` les compte et les nomme sans les refuser.

## Image générée par IA (Canva) pour la situation déclenchante (05/11/2026)

Elle montre le problème de la séquence, jamais sa solution. Demande de Pascal du 05/11/2026 : « il manque aussi des images réalistes ».

| Fichier | Ce qu'elle montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/situation_fichiers_melanges.png` | Un bureau en désordre : un ordinateur portable dont l'écran est couvert de fichiers, des feuilles de tableaux éparpillées, des notes adhésives, une clé USB. PNG 1 536 × 1 024, 2.1 Mo. | **Image générée par IA** avec Canva (génération d'image), compte de Pascal, 05/11/2026. Demande : « Realistic photo, top-down view of a cluttered school desk: a laptop showing a messy folder full of file icons with unreadable names, scattered printed spreadsheets, sticky notes, a USB stick and a bicycle key, everything mixed up, no people, no readable text, no logos » | Conditions Canva AI Product Terms : l'image appartient à Pascal, sans attribution exigée ; interdit de la présenter comme faite par un humain (légende « Image générée par IA (Canva) ») et d'en retirer les métadonnées de provenance (manifeste C2PA et XMP Canva gardés : **fichier non modifié**, d'où son poids). | Séquence, situation déclenchante (05/11/2026) |
