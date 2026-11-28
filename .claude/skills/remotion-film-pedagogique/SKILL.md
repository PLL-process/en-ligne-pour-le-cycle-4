---
name: "remotion-film-pedagogique"
description: "Film 2D court (schéma qui se construit, chaîne) avec Remotion, rendu en une commande, à projeter ou déposer sur l'ENT. Défaut pour un film 2D du dépôt. Pas pour une chaîne dans une page, ni un objet 3D."
---

# Remotion : un film 2D, rendu en une commande

Créé le 28/11/2026 après un essai comparé (Pascal : « il faudrait un skill pour chaque application »). Même chaîne
d'énergie du lampadaire (5e_C4.1), même minutage, faite avec Remotion et avec Motion Canvas : images identiques à
l'œil. Remotion est retenu **par défaut** : rendu par **une seule commande** (Motion Canvas demande d'ouvrir son éditeur
et de cliquer « Render »), et outil entretenu (version 4.0.547 du 24/11/2026 ; Motion Canvas : rien depuis le 16/02/2025).
Le skill frère `motion-canvas-film-pedagogique` reste pour qui préfère sa licence MIT.

## Quel outil pour quoi (skills frères)

| Besoin | Outil |
|---|---|
| une chaîne, un algorigramme **lus dans une page** | le lecteur pas à pas du site (`5e_C4.1/_generation/chaine_pas_a_pas/`, `_outils/lecteur_pas_a_pas/`) : voix, questions, deux dispositions — **pas de film** |
| un film 2D **à projeter**, à déposer sur l'ENT, à lire sans la page | **ce skill** (ou `motion-canvas-film-pedagogique`) |
| un objet **en volume**, en film | `blender-visualisation-pedagogique` |
| un objet en volume que l'élève **fait tourner** | `threejs-objet-3d-pedagogique` |

## Ce que le film doit tenir (règles d'or)

- **n°175** : il ne boucle pas, il ne part pas seul : `<video controls preload="none">`, jamais `loop` ni `autoplay`.
- **n°176** : sa dernière image est **l'image complète**, tenue 1,5 s ; elle sert d'affiche (`poster`).
- **n°119, n°178** : rien d'essentiel dans le mouvement seul. Pastilles numérotées dans l'image, **légende écrite dans
  la page** (le texte d'une vidéo n'existe pas pour un lecteur d'écran).
- **n°120, n°348** : les mots et les couleurs du schéma du site, tels quels. Une chaîne suit **n°310** (skill
  `chaine-energie-fonctionnelle`) : fonctions dans les blocs, composants dessous, énergies sur les flèches.
- **Schémas premium** (Pascal) : aucune pointe de flèche ne touche un bloc (12 px d'air au bout, 6 px au départ), aucun
  texte ne touche un trait.
- **Moins de mouvement** : la page montre l'affiche seule.
- **n°305** : fichiers du lot, chemins relatifs ; rien n'est chargé avant le geste.

## La recette (testée le 28/11/2026)

Les sources vont dans `<lot>/_generation/films_<sujet>/` (comme `films_trois_appareils/` de 5e_C1.1) ; `node_modules/`
n'entre jamais dans le dépôt (`.gitignore`). Les films vont dans `<lot>/Films/`.

```json
{ "private": true,
  "dependencies": {"remotion": "4.0.547", "@remotion/cli": "4.0.547", "react": "19.1.0", "react-dom": "19.1.0"},
  "devDependencies": {"typescript": "5.6.3", "@types/react": "19.1.8"} }
```

- `src/index.ts` : `registerRoot(Racine)` ; `src/Racine.tsx` : `<Composition id="Chaine" component={Chaine}
  durationInFrames={485} fps={30} width={1600} height={900} />`.
- La scène : **un SVG** (`viewBox="-800 -450 1600 900"`), chaque élément lit `useCurrentFrame()` ;
  `interpolate(f, [debut, debut + duree], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})` ; entrée
  des blocs en `Easing.out(Easing.cubic)` (0,45 s), traits et perles à vitesse **linéaire** (motion-design : un flux
  continu va droit). Une flèche se dessine en traçant sa ligne brisée jusqu'à la fraction `t` de sa longueur, pointe
  orientée sur le dernier segment, perle blanche à la pointe tant que `t < 1`.
- Textes en `<text>` + `<tspan>` (une ligne chacun), `dominantBaseline="middle"`, police
  `Inter, "Segoe UI", Arial, sans-serif` : le rendu prend les polices **de la machine qui rend**.

```bash
npx remotion render src/index.ts Chaine out/film.mp4 --crf=23
# session cloud : le navigateur que Remotion télécharge est bloqué ; donner celui de Playwright
#   --browser-executable=$(python3 -c "from playwright.sync_api import sync_playwright as s; p=s().start(); print(p.chromium.executable_path); p.stop()")
```

Puis `assembler.sh`, comme pour Blender : 1280 × 720, H.264 (`-crf 23 -preset slow -pix_fmt yuv420p -movflags
+faststart`), VP9 de secours, affiche = dernière image (`ffmpeg -sseof -0.05 -i film.mp4 -frames:v 1`).

**Mesuré** (2 cœurs, sans carte graphique) : 485 images 1600 × 900 en 57 s ; film de 16 s en 1280 × 720 : 220 Ko.

## Pièges

- **Le film ne se réarrange pas.** À 358 px de large, des mots de 20 px tombent à 4-5 px. Pour un écran de téléphone,
  une seconde `Composition` en colonne (non essayé), ou pas de film.
- **Sans l'identifiant de composition**, `remotion render` ouvre un menu interactif, ou échoue sans terminal.
- **Licence** : gratuit pour un particulier et une structure de trois personnes au plus ; au-delà, licence d'entreprise
  (remotion.dev/license). À revoir si le film sert à un établissement.
- Un texte écrit deux fois (page et film) diverge : quand un film entre dans le dépôt, ses mots se lisent dans la même
  source que le schéma (le générateur des chaînes), jamais recopiés.

## Dans la page et au dépôt

`<figure>` avec `<video controls playsinline preload="none" poster="…">`, deux `<source>` (MP4 puis WebM),
`aria-label` qui dit ce que montre le film, légende en liste numérotée, phrase « modèle simplifié » si besoin. Ligne
dans `SOURCES_MEDIAS.md` (film, affiche, script, version de Remotion). Revue d'écran en trois tours ; contrôles
`controle_medias.py`, `controle_liens.py`, `controle_hors_ligne.mjs`, `controle_mouvement.py`.

**Ce qu'aucun banc ne dit** : que le film est clair pour un élève. Se regarde en classe ; s'écrit « non vérifié ».

## Lu, rien recopié

Skills officiels de Remotion (`remotion-dev/skills`, dont `remotion-render` et `remotion-best-practices`) : utiles en
complément sur le PC de Pascal (`npx skills add remotion-dev/skills`) ; pas de fichier de licence dans leur dépôt, donc
rien n'en est recopié ici.