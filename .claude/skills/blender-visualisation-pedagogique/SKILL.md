---
name: blender-visualisation-pedagogique
description: Montrer un objet technique en 3D avec Blender (film court ou image fixe, engendrés par un script) à côté de son schéma, dans une page du dépôt en-ligne-pour-le-cycle-4. À utiliser quand un mécanisme se joue dans l'espace ou quand l'élève ne voit jamais l'objet ; pas pour un schéma du programme (chaîne d'énergie, algorigramme, pieuvre), qui reste un dessin.
---

# Blender : l'objet en 3D, à côté du schéma

Créé le 26/11/2026 avec son premier lot : les trois appareils de mesure de Chengdu (5e_C1.1), demande de Pascal
(« installe les skills etc. et fais la modification après »). Exemple complet à lire avant d'en écrire un autre :
`theme-1-…/5e/5e_C1.1/_generation/films_trois_appareils/` (`generer.py`, `assembler.sh`, `captures/`).

## Quand s'en servir, quand s'en passer

| Oui | Non |
|---|---|
| un mécanisme qui se joue **dans l'espace** : frein, pompe, engrenage, vérin | une chaîne d'énergie ou d'information, un algorigramme, une pieuvre, une bête à cornes : ce sont des blocs |
| un objet que l'élève **ne voit jamais** dans la page (n°85) | un schéma qui se lit déjà bien : le réalisme ajoute des détails à lire |
| une **vue en coupe** : ce qu'un boîtier cache | une activité où l'élève doit agir : la figure à manipuler reste l'instrument (n°175) |

La 3D montre l'objet, le schéma compare et explique (n°182). **On ajoute, on ne retire pas** : le schéma et ses étapes
restent, le film s'y accroche.

## Quel outil pour quoi (skills frères, 28/11/2026)

Pascal (28/11/2026) : « il faudrait un skill pour chaque application ». Un essai comparé (la chaîne du lampadaire de
5e_C4.1 faite avec chaque outil) a tranché ainsi :

| Besoin | Outil | Skill |
|---|---|---|
| un objet **en volume**, en film court dans le lecteur pas à pas | Blender | **ce skill** |
| un objet en volume que l'élève **fait tourner** dans la page | three.js, modèle exporté de Blender en .glb | `threejs-objet-3d-pedagogique` |
| un film **2D** (schéma qui se construit) à projeter ou à déposer sur l'ENT | Remotion (par défaut), Motion Canvas (second choix) | `remotion-film-pedagogique`, `motion-canvas-film-pedagogique` |
| une chaîne, un algorigramme **lus dans une page** | le lecteur pas à pas du site (`chaine_pas_a_pas`, `lecteur_pas_a_pas`) | — pas de film |

Un même objet peut servir au film Blender et à la vue three.js : le script `generer.py` écrit aussi le `.glb`
(export glTF binaire, une pièce = un objet nommé, matières non métalliques).

## La forme retenue (décision de Pascal, 26/11/2026)

Un **film court, muet, dans le lecteur pas à pas** : il prend la place du dessin à l'étape qui présente l'objet, et un
bouton rend le schéma. Les étapes, la voix, les phrases ne changent pas : le film illustre la phrase de l'étape.

## Ce que le film doit tenir

- **n°175** : il ne tourne pas tout seul. Il se joue une fois, à l'arrivée sur l'étape ou d'un geste. Jamais `loop`.
- **n°176** : sa dernière image est **l'image complète**, et c'est aussi son affiche (`poster`).
- **n°119, n°178** : rien d'essentiel dans le mouvement seul. Des pastilles numérotées dans l'image, leur légende écrite
  dans la page, une phrase qui dit ce que le modèle simplifie.
- **n°120, n°348** : les couleurs et les mots du schéma, tels quels (les relever dans le CSS de la page avant de modéliser).
- **Sous « mouvement réduit »** : l'affiche seule, aucun film.
- **n°305** : fichiers du lot, chemins relatifs, `preload="none"` ; rien n'est demandé avant l'étape.
- **Dire ce que c'est** : un **modèle simplifié**, pas une photo. Grains grossis, rayonnement dessiné, temps accéléré :
  la page l'écrit sous le film. Ne jamais écrire « en vrai ».

## Le script d'abord, jamais de fichier .blend

Tout est construit par `generer.py` (bpy, bmesh) : formes simples, matières, lumières, caméra, clés d'animation. Le
script se relit et se compare dans git ; un `.blend` non. Aucun modèle, texture ni HDRI venu d'ailleurs (n°1).

- Un **préfixe** (`tp_`) sur tout ce que le script crée, une **scène à soi** par objet, une fonction `menage()` qui ne
  retire que ce préfixe. Dans le Blender de Pascal, sa scène et ses données ne sont jamais touchées.
- Deux fonds : `sombre` (le fond du dessin, pour que le film se pose dans son cadre) et `clair` (pour l'impression, n°102).
- Une transformation de vue **Standard** (pas AgX) : les couleurs du schéma sortent telles quelles.
- Une matière **sans ombre ni reflet** (émission seule) pour ce qui doit avoir une couleur exacte : pastilles, points.

## Travailler dans le Blender de Pascal (connecteur)

1. `get_addon_status`, puis un `execute_blender_code` qui imprime la version, le moteur et la carte graphique.
2. Demander l'accès à **un dossier créé pour le travail** (`device_request_folder_access`), y déposer `generer.py`
   (`device_commit_files`), et l'exécuter par `exec(open(…).read())` : une seule source, celle du dépôt.
3. Construire, puis **regarder** avec `look` (mode `frames`, vue `camera`) avant tout rendu : la dernière image d'abord.
4. Un appel par film : un rendu long dépasse le délai du connecteur. 108 images en EEVEE : 35 à 50 s (RTX 3070).
5. Rapporter les rendus par `device_stage_files`, puis `assembler.sh` dans l'espace de travail.
6. À la fin : `menage()`, et rendre sa scène à la fenêtre.

## Pièges de Blender 5.1, mesurés le 26/11/2026

- **`render.render(scene=…)` recopie l'image courante de la scène de la fenêtre** dans la scène rendue : sans
  précaution, on obtient l'image 1 au lieu de la dernière. Mettre sa scène dans la fenêtre et la même image partout
  (`activer()` du script).
- **`action.fcurves` n'existe plus** : passer par `action.layers[…].strips[…].channelbags[…].fcurves`.
- **Vidéo** : `image_settings.media_type = 'VIDEO'` avant `file_format = 'FFMPEG'`.
- **Pas de `Mesh.set_sharp_from_angle`** : marquer les arêtes vives dans bmesh (`edge.smooth = False`).
- **EEVEE demande une carte graphique** : pas de rendu dans l'espace de travail du cloud (2 cœurs, pas de carte).
- Fond clair : limiter la lumière du monde par `Light Path › Is Camera Ray`, sinon tout est blanc.
- Transparence : `DITHERED` pour un fondu (pas de tri), `BLENDED` pour un faisceau doux.
- Pastilles : même taille à l'image près ou loin (échelle = distance à la caméra), et **assez grandes pour 340 px**.

## Rendu, poids, encodage

960 × 676 (le rapport du dessin du lecteur), 24 images/s, 4,5 s au plus (l'étape la plus courte dure 4,6 s en mode
« Regarder »). Maître presque sans perte, puis `assembler.sh` : H.264 (`-crf 23`, `yuv420p`, `+faststart`), VP9 en
secours, affiche JPEG. Mesuré sur le premier lot : **130 à 300 Ko par film, 40 à 50 Ko par affiche**.

## Dans la page

- `<figure>` posée **par-dessus** le dessin (même cadre : aucune ligne ne bouge), `<video muted playsinline
  preload="none">`, deux `<source>`, `poster`, `aria-label` qui décrit le film ; le dessin passe `aria-hidden` tant que
  le film le couvre.
- Les adresses **écrites en entier** dans le script de la page : fabriquées par concaténation, les contrôles de liens
  et de médias ne les voient pas.
- La légende : une liste numérotée, avec les mots du schéma.
- Banc du lot : fichiers (forme, poids), rien de demandé à l'ouverture, film aux bonnes étapes seulement, pas de
  boucle, bouton « schéma », affiche seule sous « mouvement réduit », aucun débordement à 390 px.
- `SOURCES_MEDIAS.md` : chaque film, chaque affiche, le script, la version de Blender.

## Avant de livrer

Revue d'écran en trois tours (skill `revue-ecran-trois-tours`) sur des captures à 390 et 1 280 px, avant/après dans la
PR. Les contrôles du dépôt : lecteur pas à pas, médias, liens, hors ligne, mouvement, page ouverte.

**Ce qu'aucun banc ne dit** : que le film est juste et clair pour un élève, et qu'il se lit sur les postes du collège.
Cela se regarde en classe, et s'écrit dans le rapport de tests comme non vérifié.

## Sources lues, rien d'installé (veille du 26/11/2026)

Idées reprises, réécrites ici : vérifier le connecteur avant tout et ne pas lui confier un travail long
(`vladmdgolam/agent-skills`, `blender-mcp`, MIT) ; essai de rendu avant le rendu final et revue sur captures avant
verdict (`arjun988/blender-skills`, `rendering` et `qa-review`, MIT). Détail et refus : `SKILLS_AUDIT.md`.
