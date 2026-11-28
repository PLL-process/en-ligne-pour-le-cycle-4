# Audit du 26/11/2026 — les dix skills de design joués sur toutes les pages vivantes

**Demande de Pascal (26/11/2026, 17 h 30)** : « lancer directement tout sur toutes les séquences etc. », puis
« si quelque chose d'autre ne va pas, tu le corriges […] puisque tu reverras chaque activité élève ».

**Ce que cet audit est, et ce qu'il n'est pas.** Chaque page vivante a été passée au crible de son code et ouverte
dans un navigateur, à 1 280 px, 390 px et 320 px. **Les activités n'ont pas été lues une à une** : une seule séquence
(`5e_C3.1`) a été regardée à l'écran, sur ses deux premiers écrans de téléphone. La lecture d'une séquence comme un
élève reste le travail de `audit-double-regard` et de `revision-sequence`, séquence par séquence.

> **Rectificatif du 27-28/11/2026 — la vue de l'élève.** Les mesures de rendu du 26/11 ont été prises par un navigateur
> piloté (`navigator.webdriver`). Le site lui donne la **page complète** ; l'élève, lui, arrive **en mode mission**, un
> écran à la fois (décision du 14/11/2026). Deux constats décrivaient donc une page que l'élève ne voit pas d'abord :
> le bouton « Mode mission » flottant (il n'apparaît qu'une fois l'élève sorti du mode mission, à la demande de Pascal
> du 16/11/2026 : **retiré**, voir les fausses alertes) et la hauteur de `5e_C3.1` (11,8 écrans en page complète, 4,7 en
> mission). Les deux scripts de mesure prennent maintenant `--eleve` ; toutes les mesures ci-dessous marquées « vue
> élève » ont été refaites ainsi, sur `main` (avant) et sur la branche (après). La vague « lisibilité au téléphone » est
> faite : `_outils/lisibilite_ecran/` (voir son `README.md`).

## Périmètre et couverture

- **Périmètre** : 413 pages (60 séquences, 78 QCM, 69 synthèses élève, 69 synthèses professeur, 60 lexiques,
  49 ateliers, 13 TP, 15 autres) ; 410 mesurées dans le navigateur, 3 ne font que renvoyer vers une autre.
- **Le site** : HTML, CSS et JavaScript à la main, un seul thème, sombre ; l'impression passe en clair.
- **Limite de toutes les mesures de rendu** : la page **telle qu'elle s'affiche au chargement**. Ce qui est replié
  (`details` fermé) ou dans une autre séance n'est pas mesuré. **Deux vues** : page complète (navigateur piloté, 26/11)
  et vue élève, en mode mission (`--eleve`, 27-28/11).
- **Ce que le dépôt dit de son interface** : `JOURNAL_DES_DECISIONS.md` (n°34, 119, 299, 302, 305, 306, 311, 315,
  321, 331, 370), `_outils/METHODE.md`, les skills de `.claude/skills/`, `_outils/axe_reference.json`.

| Domaine (skill) | Ce qui a été regardé | Résultat |
|---|---|---|
| Accessibilité (`better-accessibility`, `web-design-guidelines`) | crible du code, 413 pages ; noms accessibles, souris seule, 60 arrêts de Tab, 410 pages ; `controle_tactile.py` | 5 constats, **4 corrigés** |
| Mise en page (`better-layout`) | défilement horizontal à 390 et 320 px, cibles, éléments flottants, 410 pages | 3 constats |
| Textes d'interface (`better-writing`) | crible des textes, 413 pages | 1 constat |
| Typographie (`better-typography`) | longueur de ligne, interligne, tailles, texte centré, 410 pages | 3 constats |
| Couleurs (`better-colors`) | `color-scheme` ; **contraste non rejoué** (voir « Non vérifié ») | 1 constat ; contraste : non revu |
| Finitions (`better-ui`) | règles `:hover`, barre du haut | 2 constats |
| Mouvement (`review-animations`, `motion-design`) | crible des transitions et animations ; `controle_mouvement.py` | 1 constat |
| Utilisabilité (`ux-heuristics`) | `5e_C3.1`, deux écrans de téléphone sur douze | **non noté** : lecture partielle |

## Constats

Quinze constats, du plus grave au moins grave, puis par nombre de pages. « Corrigé » = fait dans ce lot. Au 28/11 :
le bouton « Mode mission » flottant est retiré (page complète seulement), le focus sous les barres est ajouté.

| Gravité | Domaine | Où | Avant | Après | Pourquoi |
|---|---|---|---|---|---|
| HIGH — **corrigé** (28/11) | Accessibilité | vue élève : 144 pages, 748 arrêts de Tab (63 synthèses élève, 44 séquences, 21 ateliers) ; source : barre du haut collée, pied « Suivant » fixe du mode mission | le champ atteint au clavier finit sous la barre ou sous le pied | `html{scroll-padding-top:64px}`, `html:has(body.ms){scroll-padding-bottom:104px}`, posés par `_outils/lisibilite_ecran/` | Focus caché (WCAG 2.4.11). Après : 27 pages à la mesure instantanée, dont 23 tiennent au défilement doux (rejouées en attendant 0,4 s : 0) ; restent 4 cas réels, ci-dessous « Non vérifié » |
| HIGH — **corrigé** | Accessibilité | `4e_C1.4/sequence-cybersecurite-protection-donnees.html:2790` (12 croix) ; `tp_mbot2_python.html` refondu sur `main` le 27/11, sans croix à la souris | `<span class="close" onclick="…">×</span>` | `role="button" tabindex="0" aria-label="Fermer"`, Entrée et Espace | Une fenêtre qui ne se ferme qu'à la souris : un chemin au pointeur sans chemin au clavier |
| HIGH — **corrigé** | Accessibilité | 7 synthèses élève des représentations (ex. `synthese_eleve_besoin-bete-a-cornes.html`) ; la même règle sur 38 pages, **toutes engendrées** (`ateliers-representations/_generation/build.py`, `syntheses.py`) | `.evitement:focus{left:10px;top:10px;…}` sans `z-index`, sous `nav#navharm` | `;z-index:2000`, **dans les générateurs** (28/11 : posé le 26/11 dans les pages seules, une régénération l'effaçait, n°283) | « Aller au contenu » prenait le focus caché sous la barre du haut. Mesuré : 7 pages, puis 0 |
| MEDIUM — **corrigé** | Accessibilité | 16 pages, 77 champs (relevés des C7 et C8, `5e_C1.5`, `tp_mbot2_python.html`) | `<input id="trac0" placeholder="… kN">` | `aria-label="Rupture en traction (kN) — Tube aluminium Ø50 × 3"`, ou `aria-labelledby` vers la question, ou `for` sur le `label` | Un texte d'exemple n'est pas un nom : le lecteur d'écran annonçait « … kN » |
| MEDIUM — **corrigé** | Accessibilité | `5e_C9.1`, `sequence-jardin-connecte-arrosage-automatique.html`, 9 boutons | `<button>▶</button>` | `aria-label="Lancer le test T1 — sol sec"` | Trois boutons au même symbole dans un tableau : le nom dit l'action |
| MEDIUM — **corrigé** | Texte (hors design) | `3e_C8.2/sequence_3e_C8.2_mat-de-la-station.html:2848` | deux paragraphes, 110 mots, sans repère | `<b>La situation.</b>` en tête du second | `controle_hierarchie.py` était rouge sur `main` (mur sans repère) ; il est vert |
| MEDIUM — **corrigé** (28/11) | Typographie | vue élève, 390 px : `p.saved-note` (33 pages), `p.problematique` (32), chapeaux `p.subtitle` (58 pages), `p.sub.ms-entete` (58 lexiques), `p.mission` (18 ateliers) | `text-align:center` sur 3 lignes et plus | note et problématique : `text-align:start` sous 700 px ; chapeau : centré s'il tient sur une ligne, à gauche s'il est long (`width:fit-content`) | Un texte centré n'a pas de bord gauche où reprendre la ligne. Après : 0 page pour ces cinq-là. Laissés : `p.question` (titre-question en gras, 54 synthèses), mentions de licence |
| MEDIUM — **corrigé** (28/11) | Typographie | 57 synthèses élève (`figcaption`, 11,9 px, et son `i`) | légende sous 12 px à l'écran | même sélecteur que la page, `font-size:max(13px, taille d'origine)`, sous `@media screen` | La légende est un texte à lire, pas un décor. Texte sous 12 px en synthèse élève (vue élève) : 58 pages → 1. Impression : 11 pages capturées en A4, identiques au pixel |
| MEDIUM | Accessibilité | `4e_C7.5`, `5e_C7.4` (8 pages portent le composant) ; source `_outils/chaine_a_completer/chaine.css` | `button.cac-case` prend le focus sous `div.cac-reserve` collante | `scroll-margin-bottom` égal à `--cac-bas` | Focus en partie caché. **À confirmer** : un seul point de la case a été sondé |
| MEDIUM | Mise en page (Vercel) | 171 pages, 414 images (57 synthèses élève, 30 séquences, 74 QCM où l'image de la question est remplie par script) | `<img src="…">` sans `width` ni `height` | les deux attributs, tirés du fichier | Le texte saute pendant que l'image arrive, et une ancre vers une séance tombe à côté |
| LOW | Finitions | 396 pages, 1 068 règles ; sources `mission.css` (`.ms-lab:hover`, 261 pages), `#navharm a:hover` (240), `.option:hover` (76 QCM) | `:hover` hors de `@media (hover:hover)` | l'envelopper | Au doigt, le survol reste collé après un toucher et ressemble à une sélection |
| LOW | Couleurs (Vercel) | 363 pages sombres sur 365 ; 122 portent des listes déroulantes natives (523 listes) | pas de `color-scheme` | `:root{color-scheme:dark}`, `light` à l'impression | Barres de défilement et listes natives restent claires sur une page sombre. À essayer sur un gabarit d'abord |
| LOW | Mise en page | `a.retour-carte` 84 × 23 px (66 synthèses élève, 418 liens), lien du lexique 186 × 20 (58), case du QCM 166 × 20 (76) | cible de moins de 24 px de haut | `min-height:24px` | Critère 2.5.8 : 24 × 24 px au moins |
| LOW | Textes | 108 pages, 550 fois ; dont la phrase tenue par `controle_sauvegarde_locale.py` (89 pages) | « clique sur… » dans des pages lues aussi au doigt | un seul verbe sur le site (« Touche ou clique » existe déjà dans une page) | Le verbe suit le geste ; aussi « Mode essentiel : OFF » sur 64 pages, où l'état est écrit en anglais dans le libellé |
| LOW | Mouvement, typographie | `.ms-jauge i` (261 pages, `width` en 0,9 s), `.progress-bar>div` (99) ; `body{font-size:17px}` (49) ; `transition: all` (2 pages anciennes) | — | `transform:scaleX` ; fond opaque ; `rem` ; propriétés nommées | Finitions sans effet sur la tâche. 20 % des paragraphes de séquence dépassent 90 caractères par ligne à 1 280 px (6 % dépassent 110) |

**Aussi corrigé le 28/11, hors des quinze** : la barre du haut collée, opaque à 93-94 % sans flou (129 pages en vue
élève), laissait lire le texte qui défile dessous ; même couleur, opaque (`nav#navharm{background:rgb(…)}`). Une barre
floutée (119 pages, verre dépoli voulu) n'est pas touchée. Après : 0.

## Ce qui va bien (mesuré)

- **Aucun contrôle sans nom** dans l'arbre d'accessibilité, **aucun élément à la souris seulement**, sur 410 pages.
- **Aucune page ne défile de côté**, ni à 390 px ni à 320 px.
- Chaque page animée a son repli « moins de mouvement » ; aucune image sans `alt` ; le zoom n'est bloqué nulle part.
- Longueur de ligne : médiane de 70 caractères en séquence, 60 en synthèse élève, 58 en QCM (le dépôt vise 45 à 90).

## Quatre fausses alertes de l'audit lui-même (n°248)

1. Huit boutons « vides » du pont en H (`3e_C9.2`) : leur texte est posé par le script (« A : fermé »).
2. Sept boutons « sans focus visible » (`4e_C1.4`) : l'anneau arrive par une transition de 0,2 s, la mesure passait trop tôt.
3. Des titres et des boutons « vides » : ils étaient dans un `details` fermé, qui garde une taille. Les deux scripts de
   mesure demandent maintenant au navigateur si l'élément est réellement affiché (`checkVisibility`).
4. `.cac{width:calc(100vw - 16px)}` : voulu, au téléphone seulement.
5. **Le bouton « Mode mission » flottant sur le texte (85 séquences)** : mesuré en page complète. L'élève arrive en
   mission, où le bouton n'existe pas ; il n'apparaît qu'une fois l'élève sorti du mode mission, ce que Pascal a demandé
   le 16/11/2026. Constat retiré, bouton laissé tel quel.
6. **Le focus « caché » de 23 pages après correction** (ateliers, cahiers, une séquence) : leur page défile en douceur
   (`scroll-behavior:smooth`) et la mesure lit le focus tout de suite. Rejoué en attendant 0,4 s : aucun.
7. **Trois boutons « au symbole seul » de `tp_mbot2_python.html`** (« 50 », « 1 », « 15 ») : ce sont des étiquettes de
   code à glisser ; leur nom est leur valeur.

## Vérification

- `python3 docs/audits/skills-design-2026-11-26/crible_design.py .` — 413 pages lues ; après correction, 0 champ sans
  étiquette, 0 `onclick` sans clavier, 0 bouton au symbole seul.
- `python3 docs/audits/skills-design-2026-11-26/mesures_rendu.py . --json …` — 410 pages mesurées, 3 renvois, 0 panne.
- `python3 docs/audits/skills-design-2026-11-26/mesures_telephone.py . --json …` — 410 pages mesurées, 0 panne.
- Bancs des 18 pages corrigées : **36 / 36 verts** (`tests_*_sequence.mjs`, `tests_regle_311_*.mjs`, `tests_3e_C1.5_seances.py`,
  `tests_3e_C9.1.mjs`, `tests_5e_C9.1-C9.3.mjs`, `tests_4e_C6.2.mjs`, `tests_tp_algorigrammes_4e_C6.2.mjs`).
- Contrôles du dépôt, verts : `controle_tactile`, `controle_mouvement`, `controle_hierarchie` (rouge avant ce lot),
  `controle_liens`, `controle_regles_visibles`, `controle_licence`, `controle_mode_mission`,
  `controle_sauvegarde_locale`, `controle_sigles_expliques`, `controle_squelette.mjs`, `registre_regles.py --verifier`.

**Non vérifié.**
- Le **contraste** : `controle_axe.mjs` n'a pas tourné (axe-core absent de la session). Sa référence, à zéro nœud
  grave, n'a pas été rejouée ; le contraste des contenus repliés et de la page imprimée n'a jamais été mesuré ici.
- Tout ce qui est replié ou dans une autre séance ; l'impression ; un lecteur d'écran réel ; un vrai téléphone.
- Les 15 bancs des QCM et des quiz des dossiers touchés : leurs pages n'ont pas changé, ils n'ont pas été relancés.
- L'utilisabilité, activité par activité.

**Vérifié le 28/11/2026** (branche rebasée sur `main` = `cdf79c9b`) :
- `python3 _outils/lisibilite_ecran/poser.py --verifier --site` — 412 pages à jour, 1 sans objet, code 0.
- Mesures en vue élève, `main` contre la branche (`--eleve`) : focus caché 144 → 27 pages (23 fausses alertes, voir 6) ;
  texte sous 12 px en synthèse élève 58 → 1 ; texte centré de 3 lignes et plus, pour les cinq textes visés, 199 → 0 (58 lexiques, 58 QCM, 33 + 32 séquences, 18 ateliers) ;
  barre du haut translucide sans flou 129 → 0 ; aucune page ne défile de côté.
- Impression : onze pages (séquences, synthèses, atelier, QCM, lexique, index) capturées en A4, `main` contre la
  branche : identiques au pixel.
- Les 56 contrôles Python de `_outils/` sur `main` et sur la branche : **mêmes codes de sortie** partout. Trois sont
  rouges des deux côtés, venus des lots du 27/11 : `controle_hierarchie` (3 murs sur `main`, 2 sur la branche),
  `controle_lexique_a_jour` (7 lexiques périmés), `controle_sigles_expliques` (PLA, DEL).
- Générateurs rejoués après branchement de l'outil (n°283) : `ateliers-representations/_generation/build.py`, les quatre
  scénarios de l'atelier CAO, l'atelier de planification, les quatre pages de la station `3e_C9.2` — chacun réécrit ses
  pages à l'identique ; `controle_lexique_a_jour` retrouve les 7 périmés de `main` (58 avant branchement).
- Bancs du mode mission : `banc_mission.mjs` 52 / 52, `banc_defaut.mjs` vert sur toutes les pages à mode mission,
  `banc_barre.mjs` 112 / 112 (thème 3) et 47 / 47 (début du thème 1) ; le reste n'a pas tourné.

**Non vérifié** (28/11) : les trois générateurs Node (`lampadaire_en_pieces`, `station_en_pieces`, `freins_iso`) n'ont
pas tourné — le kit `anatomy` qu'ils importent n'est pas dans la session ; leur ligne ajoutée est vérifiée à la syntaxe
seulement. Les sept `build_qcm.py` n'ont pas été rejoués (il leur faut un gabarit et `fix_r.js`) : leur import charge.
Quatre focus réellement cachés restent : le bouton « ↑ » du Book Train sous le pied, trois boutons de `freins_iso.html`
sous la tête de mission, le lien de licence au bas du TP mBot2, un schéma plus haut que l'écran (`entrainement_dnb`).

## Verdict

`Approve` pour ce qui a été regardé : les trois constats HIGH sont corrigés (le troisième le 28/11), aucun ne reste ;
quatre focus cachés isolés sont nommés plus haut. Domaines non revus,
nommés : **couleurs (contraste)**, **utilisabilité activité par activité**, et tout contenu replié au chargement.

## La lecture de `5e_C3.1` au téléphone (ux-heuristics, partielle)

- **Vue élève (mode mission)** : 4,7 écrans de téléphone, 619 mots au premier écran de mission ; la synthèse, 2,2 écrans.
- *Page complète (26/11)* : 11,8 écrans au chargement (médiane des séquences : 16 ; maximum : 38). La première activité
  commence au sixième écran, les onglets des séances au quatrième : c'est l'ouverture voulue par la n°306.
- 29 volets, un seul ouvert ; 16 boutons visibles ; le mode mission (« un exercice à la fois ») est proposé.
- Deux gênes vues à l'œil, comptées ensuite sur tout le site : le bouton flottant sur le texte (page complète
  seulement : retiré), la note de sauvegarde centrée sur six lignes (corrigée le 28/11).

## Suite proposée, en vagues

1. ~~**Lisibilité au téléphone**~~ : **faite le 28/11/2026** (texte centré, légendes, barre du haut, focus sous les barres) ;
   le bouton flottant est retiré des constats.
2. **Images** : `width` et `height`, par outil, avec mesure avant et après.
3. **Finitions** : `:hover`, `color-scheme`, cibles de 24 px, « clique ».
