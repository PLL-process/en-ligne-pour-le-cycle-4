# objet3d — un objet en 3D que l'élève fait tourner

Créé le 28/11/2026 (skill `threejs-objet-3d-pedagogique`). Premier usage : le vélo-cargo de 5e_C3.1
(`theme-1-…/5e/5e_C3.1/`, volet `#vc3dVolet`). Une seule copie pour tout le site.

| Fichier | Rôle | Chargé |
|---|---|---|
| `objet3d-amorce.js` | 2 Ko : branche le bouton de chaque figure ; charge le reste au clic | avec la page (`defer`) |
| `objet3d.css` | la figure, l'affiche, les pastilles, le bouton, l'impression | avec la page |
| `objet3d.js` | three.js 0.187.0 + la vue (650 Ko, 162 Ko compressé), **un script classique** | au clic seulement |
| `source/` | `objet3d.src.js` (la vue), `package.json`, `construire.sh` | jamais (sources) |

Ne pas modifier `objet3d.js` à la main : modifier `source/objet3d.src.js`, puis `sh source/construire.sh` (npm, esbuild).
`source/node_modules/` n'entre pas dans le dépôt (`.gitignore`). La licence MIT de three.js reste en fin de `objet3d.js`.

## Pourquoi un script classique

Pascal emporte le site sur une clé ou le réseau du collège : les pages s'ouvrent alors en `file://`, où le navigateur
refuse les modules ES (`<script type="module">` qui importe) et `fetch()`. D'où un seul script IIFE (esbuild), et le
modèle `.glb` fourni en base64 dans un script (`window.MODELE_X = "…"`), lu par `GLTFLoader.parse`.

## Dans une page

```html
<!-- dans <head> (chemins relatifs à la page) -->
<link rel="stylesheet" href="../../../../_ressources-communes/objet3d/objet3d.css">
<script src="../../../../_ressources-communes/objet3d/objet3d-amorce.js" defer></script>

<figure class="o3d" id="vc3d" data-o3d-moteur="../../../../_ressources-communes/objet3d/objet3d.js"
 data-o3d-modele="Images/velo_cargo_3d_modele.js" data-o3d-global="MODELE_VELO_CARGO" data-o3d-aide="vc3dAide"
 data-o3d-options='{"direction":[-0.7,0.5,-1.3],"etiquettes":[{"piece":"batterie","numero":1}]}'>
  <picture>
    <source media="(max-width: 600px)" srcset="Images/…_affiche_etroite.png">
    <img src="Images/…_affiche.png" width="800" height="600" loading="lazy" alt="…ce que montre l'image, pastilles comprises">
  </picture>
</figure>
<button type="button" class="o3d-btn" aria-controls="vc3d" hidden>🔄 Tourner … en 3D</button>
<p class="o3d-aide" id="vc3dAide">Fais glisser pour tourner ; molette ou deux doigts pour zoomer. Au clavier : flèches
pour tourner, + et − pour zoomer, 0 pour revenir au départ.</p>
<ol>…la légende des pastilles, avec les mots du schéma…</ol>
```

- **`direction`** : d'où l'on regarde au départ (axes du glTF : Y en haut ; Z = −Y de Blender). La distance se calcule :
  tous les points de l'objet tiennent dans l'image, avec 12 % de marge.
- **`etiquettes`** : une pastille par pièce (`piece` = nom de l'objet dans le modèle). Elle se pose sur l'objet vide
  `repere_<piece>` s'il existe (à placer dans Blender, sur une face que la vue de départ montre), sinon sur le point de
  la pièce le plus proche du centre de sa boîte. Une pastille dont la pièce est cachée par une autre s'estompe.
- **Le bouton** est sous la figure (posé sur l'image, il en cachait le bas à 390 px). Il reste après l'ouverture et
  devient « ↺ Revenir à la vue de départ ». Le focus passe à la vue, qui se tourne aussi au clavier.
- **Sans WebGL** : pas de bouton, l'affiche reste, l'aide le dit. **À l'impression** : l'affiche.
- Rien ne tourne seul ; rendu à la demande ; sous « moins de mouvement », pas d'inertie ; pas de déplacement latéral.

## Les pièges déjà rencontrés (28/11/2026)

- `display:block` l'emporte sur l'attribut `hidden` : `.o3d img[hidden]` et `.o3d-btn[hidden]` le remettent.
- Une matière glTF sans `metallicFactor` est **métallique** : noire sans carte d'environnement. Exporter Metallic = 0 ;
  la vue ramène à 0 ce qui aurait échappé (avec un avertissement en console).
- `reset()` d'OrbitControls juste après un glisser : l'inertie continuait de tourner. La vue coupe l'inertie le temps
  du retour.
- L'affiche doit être rendue à la taille où elle s'affiche, sinon les pastilles tombent à 8 px sur un téléphone : d'où
  deux affiches (800 × 600 et 360 × 270, rendues ×2).
- Un fichier écrit dans la session puis aussitôt envoyé sur le poste de Pascal peut partir dans son ancienne version :
  vérifier sur le poste (empreinte) avant de lancer Blender.

## Vérifier

Le banc du lot (`tests_objet3d_velo_cargo.py` pour le vélo-cargo) : `file://`, réseau coupé, rien avant le clic, clic,
glisser, flèches, « 0 », bouton de retour, impression, sans WebGL, 390 px. Non vérifié par un banc : la fluidité sur les
vieux postes du collège (se regarde en classe).
