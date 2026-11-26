# Mode lecture — une partie par écran

Demande de Pascal du 25/11/2026 : « que le mode mission soit pour tous les documents élèves ». Une synthèse et un
lexique ne se jouent pas, ils se lisent : ils reçoivent le pendant du mode mission, sans étoile ni vérification.
Mesure de départ : une synthèse élève fait 8 000 px de haut sur un téléphone, d'un seul tenant.

Le mode lecture est une **seconde vue de la même page**. Il n'écrit rien dans la page et n'en retire rien : il montre
ses parties une à la fois, avec une barre d'étapes et deux boutons — Précédent · Suivant.

## Ce que le bloc fait

- **Découpe la page en parties.** Une partie : une carte de la page (`section`, `article`, `.card`, `.carte`, `.bloc`,
  `.box`), un bloc qui s'ouvre sur son titre, ou — dans une page écrite à plat — un titre `h2` et ce qui le suit
  jusqu'au titre suivant. Le conteneur est celui qui porte le plus de parties, parmi `main`, `.page`, `.wrap`,
  `.container` et `body`. Dans une synthèse : la carte « 🧠 Ce que je dois retenir », puis chaque partie, puis les
  mots de la séquence. Dans un lexique : une séance, ou une compétence.
- **Garde le haut de la page à la première partie.** Le titre reste ; sa question et sa barre d'outils (« 🖨 Imprimer »)
  se lisent à la première partie, puis s'effacent : elles prenaient un quart d'écran de téléphone à chaque partie.
- **Dit où l'on est** : « Partie 3 sur 8 · 2. Quelles sont les deux chaînes du lampadaire ? », et une barre d'étapes
  où chaque trait mène à sa partie (cible de 24 px de haut, nom accessible « Partie 3 sur 8 : … »).
- **Suit les liens de la page.** « ↑ La carte », un lien de la carte vers « #partie-3 », une adresse
  `lexique_x.html#seance-s2` venue de la séquence : la partie de l'ancre s'ouvre.
- **S'allume d'emblée pour l'élève.** « 📄 Page complète » ramène à la page qui défile ; « 📖 Mode lecture : une
  partie à la fois », posé avant la première partie, y retourne.
- **Tient la navigation du site sur une ligne** (elle défile de côté) et se cale sous elle.

## Ce qu'il ne fait pas

- **Rien à l'impression** : tout ce qui cache est sous `@media screen`. La fiche papier sort entière, en mode lecture
  comme en page complète.
- **Rien dans le navigateur, sauf le choix d'affichage** : tant que l'élève ne choisit rien, le mode n'écrit rien ;
  « 📄 Page complète » laisse une marque (`lecture:<page>` = 0), comme le mode mission garde son choix, et « 📖 Mode
  lecture » la retire. Ni réponse, ni progression : rien de ce qu'a fait un élève n'attend le suivant (règle d'or
  n°322 ; `controle_sauvegarde_locale.py` lit le bloc à part). Le premier jet gardait ce choix le temps de l'onglet
  (`sessionStorage`) : il est gardé comme celui du mode mission — l'élève qui préfère la page complète la retrouve —,
  et un banc peut le vérifier depuis un second onglet.
- **Un robot de test ouvre la page complète** (`navigator.webdriver`) : les contrôles et les bancs du dépôt mesurent la
  page qui défile, comme avant ; `banc_lecture.mjs` allume le mode lui-même.
- **Une page d'une seule partie reste telle quelle**, sans bouton (un lexique d'une seule compétence, un lexique en
  tableau) : il n'y a rien à découper. Elle porte le bloc quand même — le contrôle n'a pas à deviner ce que le
  navigateur verra —, et le banc la compte.
- Il ne chronomètre rien, ne note rien, ne bloque jamais « Suivant ».

## Fichiers

| Fichier | Rôle |
|---|---|
| `lecture.css`, `lecture.js` | la source unique |
| `poser.py` | pose ou met à jour le bloc dans une page (`--verifier` : ne rien écrire) ; un générateur appelle `poser(html)` |
| `banc_lecture.mjs` | joue **toute** page qui porte le bloc, partie par partie, en navigateur d'élève à 390 px (`--detail` : la liste des parties) |
| `../controle_mode_lecture.py` | chaque synthèse élève et chaque lexique porte le bloc, celui de la source, une fois (L1 à L4) ; `../tests_controle_mode_lecture.py` l'éprouve |

## Poser le mode lecture

```bash
python3 _outils/mode_lecture/poser.py <synthese_eleve.html> <lexique.html>
node _outils/mode_lecture/banc_lecture.mjs <page.html> --detail
python3 _outils/controle_mode_lecture.py
```

Une page **engendrée** ne se retouche pas à la main : c'est son générateur qui pose le bloc —
`_outils/generer_lexique.py` (les lexiques), `ateliers-representations/_generation/build.py` (les synthèses des
ateliers de représentation). Les autres synthèses élèves sont écrites à la main : `poser.py`.

Le banc **refuse** : une erreur JavaScript ; une page qui ne s'ouvre pas en mode lecture pour l'élève ; une partie
vide ; un défilement de côté à 390 px ; du texte perdu (les parties, bout à bout, ne font pas la page) ; « Suivant »
qui n'avance pas ; un lien d'ancre qui ne mène pas à sa partie ; « Page complète » qui ne rend pas la page entière ou
que la page oublie au rechargement ; une fiche papier amputée ; autre chose dans `localStorage` que le choix
d'affichage ; un robot de test qui arrive en mode lecture. Avec `--detail`, lire la liste des parties : le découpage doit avoir du sens pour un élève.

## Limites connues

- Le nom d'une partie est son premier titre (`h2`, `h3`), à défaut son `aria-label`, à défaut « Partie n ». Pour
  nommer une partie, lui donner un titre.
- Un lexique d'une seule compétence, même long, tient en une partie : le mode n'y fait rien.
- La barre a ses propres couleurs (fond marine, texte clair) : elle se lit sur une page sombre comme sur une page
  claire, mais ne suit pas le thème de la page.
