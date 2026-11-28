---
name: "threejs-objet-3d-pedagogique"
description: "Objet technique en 3D que l'élève fait tourner dans une page du dépôt (three.js), modèle glTF venu de Blender, qui marche hors ligne et en file://. Pas pour un film (Blender, Remotion), ni un schéma de blocs."
---

# three.js : l'objet en 3D, que l'élève fait tourner

Créé le 28/11/2026 (Pascal : « il faudrait un skill pour chaque application »), avec une page d'essai : un lampadaire
solaire simplifié, pièces aux couleurs de la chaîne d'énergie, ouvert **depuis un fichier local, réseau coupé**.
Premier usage réel le même jour : le **vélo-cargo de 5e_C3.1** (volet `#vc3dVolet`, après le dessin animé).

**La vue existe déjà, ne pas la refaire** : `_ressources-communes/objet3d/` (amorce, CSS, `objet3d.js`, sources ;
mode d'emploi dans son `LISEZMOI.md`). Un nouvel objet = un modèle, deux affiches, une figure dans la page, un banc.
Modèle à suivre : `5e_C3.1/_generation/objet_3d_velo_cargo/` (`generer.py` dans Blender, puis `assembler.py`) et
`5e_C3.1/tests_objet3d_velo_cargo.py`.

## Quel outil pour quoi (skills frères)

| Besoin | Outil |
|---|---|
| l'élève doit **voir l'objet sous tous les angles**, ou repérer une pièce cachée | **ce skill** |
| montrer un mécanisme **qui bouge** (frein, pompe) | un film : `blender-visualisation-pedagogique` |
| un schéma de blocs (chaîne, algorigramme) | le lecteur pas à pas du site |

La 3D s'**ajoute** au schéma, elle ne le remplace pas (n°182) : seulement sur les pages où tourner l'objet apprend
quelque chose, parce que le moteur pèse 647 Ko.

## Ce que la vue doit tenir

- **Rien ne se charge à l'ouverture** : la page montre une **image fixe** de l'objet (l'affiche) et, **sous** la
  figure, un bouton « 🔄 Tourner l'objet en 3D » (44 px de haut au moins ; posé sur l'image, il en cachait le bas à
  390 px). La 3D s'ouvre au clic, **par-dessus l'image** (canevas en `position:absolute; inset:0`). Le bouton reste et
  devient « ↺ Revenir à la vue de départ » : rien ne bouge dans la page, et le doigt a son retour.
- **Au clavier** : la vue reçoit le focus à l'ouverture ; flèches pour tourner, + et − pour zoomer, 0 pour revenir.
  L'aide, sous la figure, dit les gestes et les touches.
- **Rien ne tourne seul** (n°175) : pas de rotation automatique ; rendu **à la demande** (seulement quand l'élève
  bouge l'objet) ; sous « moins de mouvement », pas d'inertie (`enableDamping = false`).
- **Les pastilles numérotées** sont du HTML posé sur les pièces (`CSS2DRenderer`, `aria-hidden`) ; **la légende est
  écrite dans la page**, en liste numérotée, avec les mots du schéma (n°119, n°120). Chaque pastille se pose sur un
  **objet vide `repere_<pièce>`** placé dans Blender sur une face que la vue de départ montre (sans lui, la pastille
  du cadre du vélo-cargo tombait sur le bac) ; une pastille dont la pièce est cachée s'estompe.
- **Le cadrage se calcule** : tous les points de l'objet tiennent dans l'image vue depuis `direction`, 12 % de marge
  (la sphère englobante laissait un objet long au milieu d'un grand vide). Choisir `direction` pour que les pièces de
  la légende soient **devant** (vélo-cargo : trois quarts arrière, côté du contrôleur et des câbles).
- **Impression** : l'image fixe, jamais le canevas. **Sans WebGL** : l'image reste, et une phrase le dit.
- **L'affiche** est la vue de départ elle-même, pastilles comprises (la légende s'y rapporte encore sans 3D), rendue
  par `objet3d.js` dans Chromium, fond transparent (rien de sombre sur papier). **Deux tailles**, rendues à la taille
  où elles s'affichent, ×2 (800 × 600 et 360 × 270 pour 600 px et moins) : une seule affiche réduite au téléphone
  ramenait les pastilles à 8 px. `<picture>` + `<source media="(max-width: 600px)">`.
- Écrire que c'est **un modèle simplifié**, pas une photo.

## Hors ligne ET en file:// (le piège qui casse tout)

Pascal emporte le site sur une clé ou le réseau du collège (`controle_hors_ligne.mjs`) : les pages s'ouvrent alors en
`file://`, où le navigateur **refuse les modules ES** (`<script type="module">` qui importe un fichier) **et `fetch()`**.
Donc :
- three.js et le code de la vue sont **un seul script classique**, construit par esbuild (format IIFE) :
  `npx esbuild src/objet3d.js --bundle --minify --format=iife --legal-comments=eof --outfile=objet3d.js`
  (three 0.187.0 : 647 Ko, 162 Ko compressé). Une seule copie pour tout le site, dans `_ressources-communes/`, avec
  sa source et sa commande de construction ; la licence MIT de three.js reste en fin de fichier.
- Le modèle `.glb` est fourni **en base64 dans un script** (`window.MODELE_X = "…"`, +33 %) et lu par
  `new GLTFLoader().parse(octets, '', ok, ko)`.
- **Mesuré** : page ouverte en `file://`, tout le réseau coupé : aucune requête, 3D ouverte en 0,4 à 0,6 s (rendu
  logiciel, sans carte graphique), 5 pastilles, la vue tourne au glisser, à 1 280 et à 390 px, sans défilement de côté.
  Vélo-cargo (5e_C3.1) : 35 tests sur 35 (`tests_objet3d_velo_cargo.py`), modèle 203 Ko, affiches 39 et 18 Ko.

## Le modèle, depuis Blender

Export **glTF binaire (.glb)**, Y en haut, modificateurs appliqués, **une pièce = un objet nommé** (la page y accroche
ses pastilles par `getObjectByName`). Couleurs : celles du schéma (n°120), en matière **non métallique** (Metallic = 0).
Viser moins de 300 Ko ; pas de texture si une couleur suffit. Le script `generer.py` du film Blender peut écrire le
`.glb` du même objet : une seule source pour le film et la 3D.

## Pièges mesurés le 28/11/2026

- **Pièces noires** : le glTF suppose `metallicFactor = 1` quand rien n'est dit ; un métal sans carte d'environnement
  sort noir. Exporter non métallique, et la vue ramène à 0 ce qui aurait échappé (avec un avertissement en console).
- **L'image restait derrière la 3D** : `.o3d > img {display:block}` l'emporte sur l'attribut `hidden` ; ajouter
  `.o3d > img[hidden] {display:none}`.
- **Le canevas sous l'image** : posé dans le flux, il descendait sous l'image tant qu'elle n'était pas cachée ; le
  glisser tombait à côté. Canevas en `position:absolute`.
- **Débordement à 390 px** : `<figure>` a des marges de 40 px par défaut ; `margin: 0 0 12px`.
- Au doigt : `touch-action:none` **sur le canevas seulement** (la page défile encore autour) ; déplacement latéral
  coupé (`enablePan = false`) et distance bornée : l'élève ne perd pas l'objet. `setPixelRatio(min(dpr, 2))`.
- **`reset()` juste après un glisser** : l'inertie (`enableDamping`) continuait de tourner. Couper l'inertie, un
  `update()`, `reset()`, puis la remettre (fait dans la vue commune).
- **Le bouton visible sans WebGL** : `.o3d-btn {display:block}` l'emporte sur `hidden`, comme l'image.
- **Fichier envoyé sur le poste de Pascal dans son ancienne version** : un fichier écrit dans la session puis aussitôt
  déposé par le pont peut partir avant d'être à jour. Vérifier sur le poste (une ligne, ou l'empreinte) avant de lancer
  Blender ; vérifier le `.glb` ramené (position d'un repère) avant d'assembler.

## Avant de livrer

Banc du lot : la page s'ouvre en `file://` réseau coupé sans requête ; rien de chargé avant le clic ; le clic ouvre
la vue et cache l'image ; un glisser change la vue ; pastilles présentes ; impression = image ; sans WebGL = image et
phrase ; pas de défilement de côté à 390 px. Revue d'écran en trois tours. Contrôles : hors ligne, liens, médias,
mouvement. **Non vérifié par un banc** : la fluidité sur les vieux postes du collège ; se regarde en classe.

## Lu, rien recopié

`cloudai-x/threejs-skills` (MIT, treize skills de référence sur three.js) et `emalorenzo/three-agent-skills`
(`three-best-practices`, MIT) : références générales de l'API, à lire au besoin ; rien n'en est recopié ici.
