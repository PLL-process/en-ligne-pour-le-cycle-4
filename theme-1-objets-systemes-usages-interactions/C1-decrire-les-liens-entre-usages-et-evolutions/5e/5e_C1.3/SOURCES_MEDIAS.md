# Sources et médias — 5e_C1.3–C1.4

## Médias originaux

| Fichier | Usage | Statut | Poids indicatif |
|---|---|---|---|
| `Images/schema_systeme_information_velos.svg` | Comprendre le rôle des acteurs, données, traitements, réseau et stockage | SVG original créé pour le lot ; aucun média externe | < 3 Ko |
| `Images/arborescence_donnees_velos.svg` | Visualiser l’organisation des dossiers | SVG original créé pour le lot ; aucun média externe | < 2 Ko |
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
| `Images/strategie_sauvegarde.svg` | Stratégie de sauvegarde | ~2 Ko |
| `Images/programme_python_annote.svg` | Programme Python annoté | ~2 Ko |

Deux d'entre eux — `arborescence_fichiers.svg` et `local_serveur_distant.svg` — traitent
précisément le sujet de l'extrait de manuel retiré ci-dessus. Ils sont peut-être les
remplaçants annoncés, dessinés puis jamais câblés dans la séquence. À trancher, pas à deviner.
`_outils/controle_medias.py` les compte et les nomme sans les refuser.
