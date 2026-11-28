---
name: "motion-canvas-film-pedagogique"
description: "Film 2D court (schéma qui se construit, chaîne) avec Motion Canvas, licence MIT, à projeter ou déposer sur l'ENT. Par défaut préférer remotion-film-pedagogique. Pas pour une chaîne dans une page, ni un objet 3D."
---

# Motion Canvas : un film 2D écrit en code

Créé le 28/11/2026 après l'essai comparé sur la chaîne d'énergie du lampadaire (5e_C4.1). Résultat à l'œil identique à
Remotion ; **Remotion reste le choix par défaut** : il rend en une commande, Motion Canvas demande d'ouvrir son éditeur
et de cliquer « Render » (fait ici par un script), et il n'a rien publié depuis le 16/02/2025 (version 3.17.2).
Avantages de Motion Canvas : licence MIT, aucune condition d'usage ; une scène s'écrit comme une suite d'étapes
(`yield*`), très lisible.

## Quel outil pour quoi (skills frères)

| Besoin | Outil |
|---|---|
| une chaîne, un algorigramme **lus dans une page** | le lecteur pas à pas du site — **pas de film** |
| un film 2D à projeter | `remotion-film-pedagogique` (par défaut) ou **ce skill** |
| un objet en volume, en film | `blender-visualisation-pedagogique` |
| un objet en volume que l'élève fait tourner | `threejs-objet-3d-pedagogique` |

## Ce que le film doit tenir

Les mêmes règles que pour Remotion et Blender : pas de boucle ni de départ seul (n°175) ; dernière image complète,
tenue 1,5 s, qui sert d'affiche (n°176) ; pastilles numérotées et légende écrite dans la page (n°119, n°178) ; mots et
couleurs du schéma (n°120, n°348), chaîne selon n°310 ; aucune pointe ne touche un bloc ; affiche seule sous « moins
de mouvement » ; fichiers locaux, rien chargé avant le geste (n°305).

## La recette (testée le 28/11/2026)

Sources dans `<lot>/_generation/films_<sujet>/`, sans `node_modules/` ; films dans `<lot>/Films/`.

```json
{ "private": true, "type": "module",
  "dependencies": {"@motion-canvas/core": "3.17.2", "@motion-canvas/2d": "3.17.2"},
  "devDependencies": {"@motion-canvas/ui": "3.17.2", "@motion-canvas/vite-plugin": "3.17.2",
                      "typescript": "5.6.3", "vite": "4.5.5"} }
```

- `vite.config.ts` — le greffon est en CommonJS : sous `"type": "module"`, son export arrive dans `.default`
  (sans cela : « motionCanvas is not a function ») :
  `const motionCanvas = (m as any).default ?? m;` puis `plugins: [motionCanvas()]`, `server: {port: 9000}`.
- `src/project.ts` : `makeProject({scenes: [chaine]})`, avec `import chaine from './scenes/chaine?scene'`.
- `src/project.meta` (réglages ; échelles permises : 0,25 · 0,5 · 1 · 2) :
  `{"version":1,"shared":{"background":"rgb(5,15,36)","range":[0,null],"size":{"x":1600,"y":900},"audioOffset":0},
  "preview":{"fps":30,"resolutionScale":1},"rendering":{"fps":30,"resolutionScale":1,"colorSpace":"srgb",
  "exporter":{"name":"@motion-canvas/core/image-sequence","options":{"fileType":"image/png","quality":100,"groupByScene":false}}}}`
  — images PNG, assemblées ensuite par ffmpeg comme les films Blender (pas besoin du greffon ffmpeg, dont une
  dépendance est abandonnée).
- La scène (`makeScene2D`) : tout est créé invisible (`opacity={0}`, `scale={0.92}`), puis révélé dans l'ordre ;
  `Line` avec `end={0}` → `ligne().end(1, 0.8, linear)` dessine la flèche, une `Circle` dont la `position` suit
  `ligne().getPointAtPercentage(avance()).position` fait la perle ; blocs en `easeOutCubic` 0,45 s.
  `Txt` accepte `\n` ; `offset={[-1, 0]}` + `textAlign="left"` pour une étiquette alignée à gauche.

Le rendu : lancer `npx vite` (en tâche de fond), puis ouvrir l'éditeur et cliquer « RENDER » par Playwright :

```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1600, "height": 1000})
    pg.goto("http://127.0.0.1:9000/"); pg.wait_for_timeout(5000)
    pg.get_by_role("button", name="Render").first.click()
    # attendre que output/project/ compte autant d'images que la scène (affichées en bas à droite de l'éditeur)
```

Puis `assembler.sh` : 1280 × 720, H.264 `-crf 23`, VP9 de secours, affiche = dernière image.
**Mesuré** (2 cœurs, sans carte graphique) : 485 images 1600 × 900 en 26 à 30 s, assemblage 7 s ; film de 16 s : 188 Ko.

## Pièges

- **Pas de commande de rendu officielle** : sans le clic, rien ne sort. Alternative lue, non essayée : le greffon
  `motion-canvas-agent` de `videozero/skills` (Apache-2.0), qui pilote l'éditeur par HTTP (`POST /__agent/render`).
- L'éditeur cherche des ressources sur Internet (échecs sans effet sur le film).
- **Le film ne se réarrange pas** : à 358 px de large, des mots de 20 px tombent à 4-5 px.
- Le rendu prend les polices de la machine (Inter dans la session cloud, Segoe UI chez Pascal).

## Dans la page et au dépôt

Comme pour Remotion : `<video controls playsinline preload="none" poster>`, MP4 puis WebM, `aria-label`, légende
numérotée ; `SOURCES_MEDIAS.md` ; revue d'écran en trois tours ; contrôles médias, liens, hors ligne, mouvement.
Ce qu'aucun banc ne dit (le film est-il clair pour un élève ?) se regarde en classe.

## Lu, rien recopié

`videozero/skills` (`motion-canvas`, `motion-canvas-agent`, Apache-2.0) et `udnisap/skills` (sans licence) : référence
de l'API, à lire au besoin ; rien n'en est recopié ici.