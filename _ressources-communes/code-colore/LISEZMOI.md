# Le code coloré façon IDE (règle d'or n°13)

Pascal, le 30/07/2026 : « J'aimerais avoir des couleurs pour les variables, constantes…, comme un IDE, par exemple
Sublime Text ou PyCharm. » Puis le 05/11/2026, sur le lampadaire de `4e_C9.1` : « sa zone de code est monochrome. À
l'avenir, il faudrait changer ceci. De façon à avoir des couleurs. »

Un seul colorisateur pour tout le site : les listings, les algorithmes et l'éditeur Python de la page.

## La palette

| Famille | Classe | Écran (fond sombre) | Papier |
|---|---|---|---|
| variables, constantes | `.py-var` | cyan `#61dafb` | `#047fa0` |
| textes `"…"`, `« … »` | `.py-str` | vert `#81fba1` | `#048827` |
| nombres | `.py-num` | orange `#ffb454` | `#ab6000` |
| mots-clés (`if`, `print`, `void`, `SI`, `ALORS`…) | `.py-kw` | violet `#c68ef2`, gras | `#6a1b9a` |
| `=`, `←` et opérateurs | `.py-op` | jaune `#ffd66b`, gras | `#7a5a00` |
| commentaires (`#`, `//`) | `.py-com` | gris bleu, italique | `#555` |

Ce sont les teintes du thème sombre du dépôt (`--hl`, `--ok`, `--energie`, `--head`, `--warn`), écrites en clair : un
listing a toujours un fond sombre, même dans une page dont les variables ont été éclaircies pour l'impression. En mode
« couleurs forcées », le texte reprend la couleur du système.

## Les trois langages

- **`python`** : le Python des séquences (mots-clés, `print`, `input`, `int`, `range`…).
- **`arduino`** : le C des cartes (`void`, `int`, `const`, `analogRead`, `digitalWrite`, `delay`, `Serial`…,
  commentaires `//` et `/* … */`).
- **`algo`** : le pseudo-code en français (`DÉBUT`, `SI … ALORS … SINON … FIN SI`, `TANT QUE … FAIRE`, `POUR`,
  `Afficher`, `Lire`, `DÉMARRER`, `ARRÊTER`, `←`) ; les petits mots de la phrase (« la », « le », « du »…) restent
  en clair.

## Poser les couleurs dans une page

```html
<link rel="stylesheet" href="../../../../_ressources-communes/code-colore/code-colore.css">   <!-- dans <head> -->
<script src="../../../../_ressources-communes/code-colore/code-colore.js"></script>          <!-- dans <head> -->

<pre data-code-colore="python">seuil = 28
if T > seuil:
    print("Rouge")</pre>
```

- Seul le **texte** est découpé : un `<select>` à choisir, un `<b>` ou un trou à compléter restent en place (exemple :
  l'atelier 2 de `4e_C4.1`, `atelier_pix_crcn_jardin.html`).
- Une **légende 🎨** suit le premier listing de la page, s'il n'y en a pas déjà une (`.py-legende`).
- **L'éditeur Python** de la page (`_ressources-communes/editeur-python/`) se sert du même colorisateur : charger
  `code-colore.js` avant `editeur-python.js`.
- Un colorisateur fait main dans une page (`pyc()` de `3e_C9.1`, le CodeLab de `3e_C6.1`, l'atelier des blocs de
  `4e_C9.1`) peut appeler `window.CodeColore.html(texte, "python")`.
- **Sans JavaScript**, le code reste lisible, en une couleur.

## L'API

| | |
|---|---|
| `CodeColore.html(texte, langage)` | le HTML coloré d'un texte (échappé) |
| `CodeColore.colorer(element, langage)` | colore un élément, une seule fois (`data-code-colore-fait`) |
| `CodeColore.legende(apres, langage)` | pose la légende 🎨 après un élément, s'il n'y en a pas dans la page |
| `CodeColore.appliquer(racine)` | colore tous les `[data-code-colore]` (fait tout seul au chargement) |

## Le contrôle

`node _outils/controle_code_colore.mjs [--muet] [dossier]` ouvre chaque page et vérifie que chaque listing de
programme ou d'algorithme, et chaque zone de saisie de code, est en couleurs. Le banc de l'éditeur
(`banc_editeur_python.mjs`, partie 18) vérifie la couche colorée : même place, mêmes mesures, défilement, impression,
couleurs forcées, et l'éditeur sans `code-colore.js`.
