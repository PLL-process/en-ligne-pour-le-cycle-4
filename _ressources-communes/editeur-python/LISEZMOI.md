# L'éditeur Python intégré à la page

Pascal, le 04/11/2026, sur `3e_C9.1` : « Dans cette séquence on demande d'aller sur l'interface Vittascience et
l'interface n'est pas jointe à l'exercice. » Vittascience refuse d'être affiché dans une autre page : l'éditeur
vient donc **dans la page**, comme le mode code de Vittascience — la zone de code, ▶ Exécuter, la console.
Vittascience reste un lien facultatif, écrit dans chaque bloc.

## Les fichiers

| Fichier | Rôle |
|---|---|
| `editeur-python.js` | le composant : monte chaque `.editeur-py` de la page, charge Skulpt au premier ▶ Exécuter |
| `editeur-python.css` | son habit (couleurs de la page, 390 px, cibles de 44 px, impression) |
| `skulpt/skulpt.min.js`, `skulpt/skulpt-stdlib.js` | le moteur Python 3 (Skulpt 1.2.0), déposé tel quel |
| `skulpt/LICENSE.txt` | la licence de Skulpt, copiée du paquet |
| `banc_editeur_python.mjs` | le banc du composant (page d'essai fabriquée hors du dépôt) |
| `eprouver_exercices.mjs` | un test par exercice outillé, pour les bancs des séquences |
| `captures_gestes.mjs` | les captures de l'encart des gestes, page par page |

## Le bloc à poser dans un exercice

```html
<link rel="stylesheet" href="../../../../_ressources-communes/editeur-python/editeur-python.css">   <!-- dans <head> -->
<link rel="stylesheet" href="../../../../_ressources-communes/code-colore/code-colore.css">        <!-- dans <head> -->
<script src="../../../../_ressources-communes/code-colore/code-colore.js"></script>               <!-- dans <head> -->

<div class="editeur-py" id="vs1" data-fichier="3e-VARIABLES-act3-TON NOM" [data-simulation="id-du-script"]>
  <label for="py_a3">🐍 L'éditeur Python de la page — …</label>
  <textarea id="py_a3" class="editeur-py-code" rows="5" wrap="off" spellcheck="false">CODE DE DÉPART</textarea>
  <p class="editeur-py-vitta">Avec Vittascience (facultatif) : <a class="btn vs-lien" href="https://fr.vittascience.com/python/?mode=code&amp;console=bottom" target="_blank" rel="noopener">Vittascience, si tu préfères</a></p>
  <p class="editeur-py-sansjs">Sans JavaScript : écris ton programme dans la zone, puis exécute-le dans Vittascience.</p>
</div>

<script src="../../../../_ressources-communes/editeur-python/editeur-python.js" defer></script>   <!-- avant </body> -->
```

- **Le code de départ** est le texte du `<textarea>` ; ↺ le remet (en deux clics, avec ↶ pour revenir).
- **La sauvegarde** est celle de la page : le programme est la valeur du `<textarea>` (son identifiant ne change
  pas), le nom du fichier celle de `<id>_nom`. Le composant envoie un `change` après chaque frappe (une demi-seconde
  plus tard) et suit la restauration de la page, qui écrit `.value`.
- **`data-simulation`** nomme un `<script type="text/x-python" id="…">` de la page : des fonctions simulées
  (capteur, pompe…) exécutées AVANT le programme de l'élève, sans décaler ses numéros de ligne. La consigne les
  nomme et les décrit (exemple : l'encadré 🔌 de `4e_C6.2`).
- **Une simulation qui finit son essai** (une nuit, une journée) lève `SystemExit` (`raise SystemExit`) : le programme
  s'arrête sans erreur, comme en Python 3, même au milieu d'un `while True:` (Skulpt n'a pas `sys.exit()`). Exemple :
  la nuit du lampadaire de `4e_C9.1`, activité 6, qui écrit son bilan puis s'arrête.
- **Sans JavaScript**, la zone et le lien restent : la consigne se fait encore.

## Le code en couleurs, comme dans un IDE (règle d'or n°13)

Pascal, le 05/11/2026, sur le lampadaire de `4e_C9.1` : « sa zone de code est monochrome. À l'avenir, il faudrait
changer ceci. De façon à avoir des couleurs. » Quand la page charge `code-colore.js` (voir le bloc ci-dessus), la zone
de saisie est posée sur **le même code en couleurs**, la palette du site : variables cyan, `"textes"` verts, nombres
orange, mots-clés violets en gras, `=` et opérateurs jaunes, `# commentaires` gris bleu en italique.

- Une couche `<pre class="editeur-py-couleurs">` (muette pour un lecteur d'écran) est dessous, aux mêmes mesures que
  la zone (police, interligne, marges, tabulations) ; le texte de la zone devient transparent, le curseur et la
  sélection restent. Elle est redessinée à chaque frappe et défile avec la zone.
- Une légende 🎨 suit le premier éditeur de la page, si la page n'en a pas déjà une.
- À l'impression, le programme écrit garde ses couleurs, en teintes foncées pour le papier.
- En mode « couleurs forcées » (contraste élevé de Windows), la couche disparaît et la zone redevient du texte
  ordinaire. Sans `code-colore.js`, l'éditeur reste en une couleur, lisible.

## L'échauffement : un éditeur d'essai, et les quatre gestes qui se cochent

Pascal, le 05/11/2026, sur `5e_C7.1` : « que l'élève, dans l'échauffement, puisse pratiquer ». L'encart « les quatre
gestes de l'éditeur Python » des six séquences outillées n'est plus fait de captures de l'éditeur (une image qu'on ne
peut pas cliquer) : il a **son propre éditeur, un vrai**, sur un programme d'essai (`nom = "Camille"` …), et la liste
des gestes se coche d'elle-même.

```html
<div class="gestes-pratique-atelier">                      <!-- ≥ 1000 px : les gestes à gauche, l'éditeur à droite, collé -->
  <ol class="gestes-pratique" data-editeur="py_echauffement" data-bilan="gestes-bilan">
    <li data-geste="1" data-si-inchange="…"><span class="geste-coche" aria-hidden="true">☐</span><span class="geste-texte">…</span></li>
    … (2, 3, 4)
  </ol>
  <div class="gestes-pratique-poste">
    <p class="gestes-pratique-bilan" id="gestes-bilan" role="status"></p>
    <div class="editeur-py editeur-py-essai" id="vsEssai" data-fichier="5e-HALL-essai-TON NOM"> … </div>
  </div>
</div>
```

- **Les coches** : 1 — un ▶ mené au bout sur un programme **changé** (sur le programme de départ, le bilan dit
  `data-si-inchange`) ; 2 — un nom de fichier sans « TON NOM » ; 3 — un ⬇ fait ; 4 — un 📂 fait. Une erreur ne coche
  rien. Elles sont gardées sur cet ordinateur (`localStorage`, s'il répond) ; sans JavaScript, la liste reste une liste
  à cocher à la main. L'éditeur d'essai ne compte pas dans la progression.
- **Les événements**, pour toute page : `editeur-py:telecharge` après un ⬇ réussi et `editeur-py:ouvert` après un 📂
  réussi (`detail = {bloc, champ, fichier}`), en plus de `editeur-py:fin`.
- Les captures de l'Explorateur de Windows restent dans l'encart (ce que la page ne peut pas montrer), dans
  `<details class="gestes-fenetres" open>`. Les captures de l'éditeur (`geste_editeur_*.png`, faites par
  `captures_gestes.mjs`) ne sont plus affichées depuis le 05/11/2026 : elles restent dans les dossiers `Images/`.

## Ce que fait l'éditeur

Zone numérotée à chasse fixe (Tab = 4 espaces, Maj + Tab retire, Entrée garde le décalage et l'ajoute après « : »,
Échap puis Tab pour sortir de la zone) ; ▶ Exécuter, ⏹ Arrêter ; la console (`role="log"`, `aria-live`) ; `input()`
**dans la console** — un champ et ↵ Valider, jamais `prompt` ni `alert` ; les erreurs **expliquées en français**,
avec leur ligne marquée dans la marge et le message de Python dessous ; une boucle qui calcule sans pause arrêtée
après **5 s** (« Boucle sans fin ? »), un programme qui attend (`time.sleep`, `attendre`) arrêté après **60 s**,
une console arrêtée après **1 000 lignes** ; ⬇ Télécharger mon .py (rappelle d'abord de remplacer « TON NOM ») ;
📂 Ouvrir mon .py (sélecteur de fichier ; l'en-tête d'un fichier de Vittascience est retiré) ; à l'impression, le
programme écrit et la dernière sortie, ou des lignes vides.

Pour une page qui **juge en exécutant** :

- `window.EditeurPython.executer(code, {simulation, entrees})` → `Promise<{sortie, erreur, arret}>`, sans rien
  afficher (3 s de calcul, 10 s en tout) — exemple : la barrière de `5e_C9.1`, exécutée avec 10, 32 puis 0 places ;
- l'événement `editeur-py:fin` (bulle depuis le bloc) après chaque ▶ : `detail = {bloc, champ, code, sortie, erreur,
  arret}` — exemple : les verrous des activités, ouverts par une exécution menée au bout.

## Le moteur : Skulpt 1.2.0

| | |
|---|---|
| Fichiers | `skulpt.min.js` (547 Ko) et `skulpt-stdlib.js` (398 Ko), **non modifiés**, chargés au premier ▶ Exécuter seulement (≈ 950 Ko, ≈ 250 Ko compressés par le serveur) |
| Source | paquet npm `skulpt@1.2.0`, https://registry.npmjs.org/skulpt/-/skulpt-1.2.0.tgz (intégrité `sha512-T0cv0sdSOXLlIJTuyXSeYJ3TFdWYSZfX2PcBLpRKrKZ3dTbVQXRMiYudSuko2xzcyMif47DS2ShatCwjCbsSsA==`) ; projet : https://github.com/skulpt/skulpt — consulté le 04/11/2026 |
| Empreintes SHA-256 | `skulpt.min.js` 1a319d8eedf314dba5af2444313e3cf2ac072a335df0f5100277e8f49b64eae9 · `skulpt-stdlib.js` e3ecccbc17c6164d19ed3c5561aaaeb752c38c8efa2d88b62b5fb7a7e1b086a7 |
| Licence | **MIT** (© 2009-2016 Scott Graham et les contributeurs de Skulpt) ; les parties traduites de CPython et de PyPy relèvent de la licence de la Python Software Foundation. Texte complet : `skulpt/LICENSE.txt`. Redistribution permise, la notice de licence jointe. |
| Attribution | « Moteur Python : Skulpt (MIT), https://skulpt.org » — dite dans ce fichier ; la page ne l'affiche pas à l'élève |

**Pourquoi Skulpt.** Il fait tourner du Python 3 dans la page, sans réseau, et c'est le seul des candidats qui
**suspend** le programme : `input()` attend la réponse dans la console, ⏹ arrête même pendant une attente, et une
boucle sans fin s'arrête au bout d'un temps donné sans figer la page. Brython (BSD, plus fidèle sur le détail)
traduit le programme en JavaScript qui s'exécute d'un bloc : `input()` y passe par une fenêtre `prompt`, et un
`while True` fige l'onglet. Pyodide (CPython complet) pèse une dizaine de mégaoctets et se charge par morceaux.
Ce que les élèves écrivent — `print`, variables, types, `int()`, `str()`, `float()`, `input()`, `if`/`elif`/`else`,
`while`, `for … in range`, fonctions, f-strings, `import time` / `random` / `math` — s'exécute comme en Python 3
(mesuré au banc : `5 / 2` → 2.5, `7 // 2` → 3, `round(2.567, 1)` → 2.6, `print` sépare par des espaces).

**Ce qui diffère de Python 3, et ce que l'éditeur en fait.**

- Les messages d'erreur de Skulpt ne sont pas ceux de CPython : l'éditeur écrit l'explication en français et
  ramène le message à celui de Python 3 quand il le connaît (`can only concatenate str (not "int") to str`,
  `division by zero`, `invalid syntax`).
- Une erreur d'écriture est souvent un vague « bad input » : l'éditeur la diagnostique lui-même sur la ligne
  (deux-points, décalage, `=` dans un test, guillemet, parenthèse, trou `___`, accent dans un nom).
- Un nom de variable accentué (`humidité`) est refusé : l'éditeur le dit (les cartes programmables le refusent aussi).
- Un nombre à virgule s'affiche avec 16 chiffres au plus : `(98 - 32) / 1.8` donne `36.66666666666666`, là où
  CPython écrit `36.666666666666664`. Aucun exercice outillé n'en dépend.
- Un mélange de tabulations et d'espaces n'est pas refusé (CPython lèverait `TabError`) ; Tab écrit 4 espaces.

## Les bancs

```
node _ressources-communes/editeur-python/banc_editeur_python.mjs [--captures <dossier>]
node _ressources-communes/editeur-python/captures_gestes.mjs [3e_C9.1 …]
```

Le banc fabrique sa page d'essai dans un dossier temporaire : aucune page n'est ajoutée au dépôt. Chaque séquence
outillée éprouve ses exercices dans sa propre suite, par `eprouver_exercices.mjs`.
