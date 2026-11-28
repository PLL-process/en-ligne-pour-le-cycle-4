# L'atelier Blender : l'outillage commun des films en 3D

`atelier.py` ne dessine aucun objet. Il fournit ce que le script `generer.py` d'un lot emploie pour construire ses scènes de
zéro dans Blender (5.0 ou plus, moteur EEVEE), selon le skill du dépôt `blender-visualisation-pedagogique` :

- couleurs du schéma (`hexa`), formes simples (`m_boite`, `m_cyl`, `m_sphere`, `m_disque`, `m_tore`, `m_anneau`, `m_arc`),
  tiges et tubes (`tige`, `tuyau`), fil tendu qui suit une pièce (`fil`) ;
- matières (`matiere`, et `aplat` pour une couleur exacte, sans ombre ni reflet), clés d'animation (`cle`, `interpoler`) ;
- `Atelier` : une scène à soi, son fond (sombre pour l'écran, clair pour l'impression), ses caméras, ses lumières, ses pastilles ;
- `couper` : une vue en coupe sans rien découper (le plan avant de la caméra passe par un point) ;
- `projeter` : où un point de la scène tombe dans l'image rendue (pour poser une pastille ensuite) ;
- `activer`, `rendre_image`, `rendre_film` : la dernière image et le film maître ;
- `menage` : retire ce que le script a créé, et rien d'autre (tout porte le préfixe `PRE`).

```python
import atelier as A
A.PRE = "fr_"                       # le préfixe du lot : rien d'autre n'est touché dans le Blender de Pascal
at = A.Atelier("patins", "sombre")
...
A.rendre_image(at.sc, "rendus/patins_large_sombre.png")
A.menage()
```

## Qui s'en sert

| Lot | Script | Depuis |
|---|---|---|
| 5e_C1.2, Sainte-Luce : les trois freins | `theme-1-…/5e/5e_C1.2/_generation/films_trois_freins/generer.py` | 28/11/2026 |

Le premier lot (5e_C1.1, les trois appareils de Chengdu, 26/11/2026) garde sa propre copie de ces fonctions : il a été
vérifié tel quel ; il sera branché ici le jour où ses films seront refaits.

## Ce qu'il faut savoir

- Rien ne se rend dans l'espace de travail du cloud : EEVEE demande une carte graphique. Le rendu se fait dans le Blender
  de Pascal, par son connecteur ; le skill dit comment.
- `couper()` lit la pose de la caméra (`location`, `rotation_euler`), pas `matrix_world` : juste après sa création,
  Blender n'a pas encore calculé `matrix_world`, et la coupe tombait à 1 mm de l'objectif (mesuré le 27/11/2026).
- Vérifié avec Blender 5.1.1 (RTX 3070) les 26 et 27/11/2026.

Licence : celle du dépôt, CC BY-NC-SA 4.0 (règle d'or n°321). Blender (GPL) n'est pas dans le dépôt.
