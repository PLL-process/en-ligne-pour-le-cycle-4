# Audit externe des séquences élèves — étapes 1 et 2, instruites et corrigées

Audit reçu le 1er novembre 2026 (« état intermédiaire vérifié », cinq constats A01–A05 et cinq points restant à auditer).
Instruit les 8 et 10 novembre 2026 sur la branche `fable/audit-externe/etape-1`, carte blanche de Pascal.
Site : https://pll-process.github.io/en-ligne-pour-le-cycle-4/

> Règle de lecture : chaque constat est **vérifié avant d'être déclaré** (n°248), chaque correction est **mesurée après** par
> un contrôle de `_outils/` ou au navigateur, et la section « Non vu » dit ce qui n'a pas été regardé.

## Résumé

| | Avant | Après | Comment c'est mesuré |
|---|---|---|---|
| Codes « couverts par mutualisation » sans lien vers la séquence qui les porte (A01) | 43 | 0 | `make_index.py`, lecture de l'index |
| Pages qui gardent les réponses sans aucun bouton d'effacement (A05) | 10 séquences | 0 séquence (reste 8 pages hors gabarit, listées) | `controle_sauvegarde_locale.py` |
| Pages prévenant du poste partagé (A05) | 0 | 85 séquences et ateliers + 24 ateliers de représentation | idem |
| Boîtes modales `confirm()` | 58 pages | 4 pages | idem |
| Groupes de boutons radio où la bonne réponse est **toujours la première** | 256 sur 256 (10 séquences) | 0 | `controle_ordre_propositions.py` |
| Réinvestissements « 🎉 Activité validée » pour n'importe quel texte | 20 séquences | 0 | banc navigateur (texte arbitraire) |
| axe-core, nœuds en contraste insuffisant | 428 (237 pages) | 117 (20 pages, dont 83 sur deux pages anciennes) | axe-core 4.10, 408 pages |
| axe-core, champs sans nom accessible (critical) | 146 | 30 | idem |
| Barres de progression sans nom | 115 | 0 | idem |
| Fichiers qu'une régénération changerait (dérive des générateurs) | 70 sur la branche avant alignement (12 le 07/11) | 0 pour les ateliers de représentation, la planification, la CAO | `rapport_audit.py --generateurs`, `verif_chaine.py` |
| Balayage navigateur (images, 404, JS, console) | — | 408 pages, 0 constat | script du skill `balayage-navigateur` |
| Impression : textes que le papier ne rend pas | 0 | 0 (2 pendant le lot, réparées) | `controle_impression.mjs` |

## 1. Les cinq constats de l'étape 1

### A01 — Couverture mutualisée : l'index dit maintenant où aller — **corrigé**

Constat confirmé, et plus large que les trois codes cités : **43 codes** des trois thèmes affichaient « Couvert par une
séquence mutualisée » puis « Aucune ressource pédagogique publiée pour ce repère ».

Correction : `_outils/make_index.py` lit le **README pointeur** du dossier du code — premier lien `.html` existant sur
le disque, titre `<title>` de la page cible, et le paragraphe du README qui nomme l'activité ou la séance (jamais deviné,
jamais la formulation du référentiel déjà affichée, jamais la formule creuse « ✅ couverte par… »). L'index affiche
« Ressource dédiée absente — compétence traitée dans : [titre] » puis la phrase du README. Exemples : 5e_C1.6 → « Le compte
du club (5e_C1.5) », 3e_C1.2 → activité 1 de Tsinghua, 5e_C4.2 → « L'activité 2 (…) porte spécifiquement cette
sous-compétence ».

Reste à Pascal (pas un défaut) : trois README pointeurs disent seulement « couverte par une séquence mutualisée » sans
nommer l'activité (4e_C4.x, 4e_C5.x, 4e_C6.1, 3e_C4.7) — l'index montre le lien seul. Une phrase dans chaque README suffit.

### A02 — « Précision ± 10 % » — **corrigé, sans introduire justesse/fidélité**

Dans Chengdu (5e_C1.1), la ligne du tableau devient « Précision *(incertitude supposée pour cet exercice)* », une note
sous le tableau dit que les chiffres sont des ordres de grandeur choisis pour comparer les trois principes, et le lexique
précise « un vrai appareil a une fiche technique qui dit la sienne ». La distinction justesse / fidélité / incertitude
**n'est pas introduite en 5e** : c'est un choix de niveau, laissé à Pascal.

### A03 — « Nettoyer » un capteur fermé — **corrigé**

Incohérence confirmée. Le tableau et la correction disent maintenant la même chose : contrôle régulier face à une mesure de
référence (la station officielle la plus proche), remplacement du module quand l'écart grandit, entretien extérieur ; le
boîtier fermé ne se nettoie pas soi-même. Rien d'autre dans le lot (QCM, synthèses) ne disait « nettoyer ».

### A04 — « Avant de commencer (échauffement) » placé avant l'activité 2 — **corrigé sur les 16 encarts du dépôt**

L'encart est à sa place (règle n°297 : juste avant la première activité qui ouvre l'outil ; dans la vue à onglets, il
ouvre la séance 2). C'est son titre qui laissait croire qu'il précédait tout. Sur les 16 encarts « les N gestes » du
dépôt, le titre devient **« Avant l'activité N (échauffement) »** ou **« Avant la séance N (échauffement) »**, N lu dans
le titre qui suit l'encart. `controle_gestes_outil.py` et ses tests : verts.

**Effet de bord trouvé et réparé** : `papier.js` (fiche papier) reconnaît les blocs d'écran à leur titre, dont « avant de
commencer » ; sous le nouveau titre, l'encart des gestes s'imprimait et `controle_impression.mjs` refusait 2 pages
(texte ambre 1,79 : 1 sur papier). La regex `TITRES_ECRAN` connaît les nouveaux titres ; bloc reposé sur 60 pages par
`poser.py` ; 0 page refusée.

### A05 — Sauvegarde locale sur poste partagé — **corrigé, et mesuré par un nouveau contrôle**

Risque confirmé et aggravé par deux formules fausses (« personne d'autre ne les voit », Shanghai et Shenzhen) et par
**10 séquences sans aucun moyen d'effacer** (l'une promettait « tu peux tout effacer quand tu veux »).

Nouveau contrôle `_outils/controle_sauvegarde_locale.py` (mesure + `--corriger`, inscrit dans `rapport_audit.py`) :
1. chaque page qui écrit dans `localStorage` sait l'effacer (bouton nommé, ou « Recommencer entièrement » des QCM) ;
2. chaque séquence ou atelier porte la note **« 🖥️ Ordinateur partagé (salle de techno, CDI) : un autre élève qui ouvre
   cette page sur la même session verra tes réponses. Quand tu as fini : imprime en PDF si tu veux garder une trace, puis
   clique sur « 🗑 Effacer ma sauvegarde » »** (`data-note="poste-partage"`) ;
3. aucune boîte modale `confirm()` : confirmation **en deux clics dans la page** (le bouton s'arme six secondes).

Fait : bouton + script autonome posés sur les 10 séquences ; note posée sur 85 séquences et ateliers (après la note de
sauvegarde ou la barre d'outils) ; dans les ateliers de représentation, la note et l'effacement en deux clics
(`armerDeuxClics` dans `kit.js`) sont posés **dans le générateur** (moteur.py, cahiers.py, build.py), qui pose aussi la
licence ; même chose dans `build_atelier.py` (planification). Vérifié au navigateur : écrire → effacer → page vide,
zéro erreur console.

**L'export local « sans données personnelles » proposé par l'audit n'est pas fait** : « Imprimer / PDF » existe déjà sur
chaque page et c'est l'export que Pascal demande aux élèves (dossier de la classe dans Documents). Un export JSON serait
une fonctionnalité transversale nouvelle → décision 1.

Reste, listé par le contrôle (hors gabarit, pas corrigé à la main) : 3 panneaux `atelier_bete_a_cornes.html` engendrés
(kit croquis sans bouton de page), `atelier_pix_crcn_jardin.html`, `activite-bonus-cyber-immersive-2fa.html` (un seul
drapeau stocké), `sequence-cybersecurite-protection-donnees.html` et `sequence-numerique-societe…` (pages anciennes, hors
gabarit n°306), `qcm_algorigrammes_domotique.html` ; 4 `confirm()` restants ; les **73 QCM** gardent un score sans note
(décision 2).

## 2. Les cinq points restant à auditer

### Point 2 — Boutons « Vérifier » : deux défauts réels, corrigés

Mesuré au navigateur sur les **56 séquences** à boutons « Vérifier » (310 boutons, 464 zones de texte) : réponses
attendues cochées quand la page a une table `att`, texte arbitraire de 300 caractères dans chaque zone de texte.

1. **La place trahissait la réponse.** Dans les 10 séquences du thème 1 au gabarit n°300 (Chengdu, Sainte-Luce, Tsinghua
   4e et 3e, Pékin, Hangzhou, Shenzhen, Shanghai, Beijing 4e, Shanghai 3e), la bonne réponse était la **première
   proposition dans 256 groupes sur 256**. Nouveau contrôle `_outils/controle_ordre_propositions.py` (mesure +
   `--corriger`) : les blocs `<div class="qcm-option">` sont réordonnés de façon déterministe (graine = page + id du
   groupe), chaque `input` gardant son `label` et son `id` ; « aucune des… » reste en dernier. La valeur transmise étant
   le texte de la proposition (n°300), les tables `att` et les bancs qui cochent `#id__n` n'ont pas bougé. Vérifié : les
   réponses attendues font toujours le plein sur les 10 pages. Quatre pages (jardin 4e_C4.1, station 3e_C4.3…) mélangeaient
   déjà au chargement : non touchées.
2. **Un texte quelconque était « validé ».** Dans 20 séquences (thèmes 1, 2, 3 : famille C7/C8, Chengdu, club 5e_C1.5,
   arrosage 4e_C6.2), le réinvestissement se vérifiait par la seule longueur (`pres("reinv", N)`) et répondait
   « 🎉 Activité validée — 1/1 ». Ces vérifications portent `libre: true` et répondent **« ✍️ Réponse enregistrée, et
   assez développée pour être relue. Elle n'est pas corrigée automatiquement : ouvre la correction et compare, point par
   point. »** La classe `.ok` est gardée : billets, bandeaux et bancs inchangés (3e_C7 80/80, 5e_C7 55/55, 4e_C7 47/47 ;
   4e_C8 53/54, l'écart « débord mobile 15 px » est préexistant sur `main`).

Ce que les validateurs font bien : les textes libres des activités notées sont jugés par **mots-clés et motifs**
(`criteres`, regex), pas par égalité stricte — tolérants à l'orthographe courante, impossibles à satisfaire par du
remplissage. Les menus déroulants et les radios comparent la valeur exacte. Aucun bouton ne plante (0 erreur JS sur
56 pages).

Reste (décision 3) : dans les mêmes 10 séquences, la bonne réponse est souvent **la plus longue** des propositions
(`controle_longueurs.py` ne regarde que les QCM) ; trois seuils de réinvestissement sont faibles (`pres(…, 25)`).

### Point 3 — Accessibilité : le mécanique est fait, le structurel est à décider

axe-core 4.10 (wcag2a, 2aa, 2.1aa, bonnes pratiques) sur les 408 pages à 1 280 px, avant/après :

| Règle | Impact | Avant | Après | Fait |
|---|---|---|---|---|
| color-contrast | serious | 428 nœuds / 237 pages | 117 / 20 | mention de licence sans `opacity:.85`, lien CC qui hérite la couleur du pied (il prenait le bleu par défaut sur fond sombre dans 93 lexiques et synthèses) ; `.timer-off` des 72 QCM #5b7bb8 → #7d9bd4 (5,6 : 1) |
| select-name | critical | 84 / 10 | 20 / 9 | `aria-label` lu dans le titre en gras ou la question qui précède (108 menus) |
| label | critical | 62 / 13 | 10 / 4 | `aria-label` lu dans l'en-tête de ligne des tableaux d'exigences (52 cases) |
| aria-progressbar-name | serious | 113 / 113 | 0 | `aria-label="Progression"` |
| empty-table-header | minor | 20 / 17 | 1 | coins `<th></th>` → `<td></td>` |
| meta-refresh | critical | 1 | 0 | renvoi `vittascience_variables.html` sans délai |
| region / landmark-one-main | moderate | 385 / 266 pages | inchangé | **décision 4** : poser `<main>` dans le gabarit n°306 |
| heading-order (h2 → h4) | moderate | 74 / 51 pages | inchangé | **décision 4** : « 💡 Ton idée à toi » et « 🅰 Matériel réel » en h4 sous un h2 |

Les 117 contrastes restants : 83 sur `tp_mbot2_python.html` et `atelier_pix_crcn_jardin.html` (pages anciennes, palette
à revoir), 11 sur `sequence_3e_C6.1-C6.3_programmer_alerte.html`, le reste dispersé (légendes `figcaption`, badges).
Les 30 champs restants : menus `a3o1…` de l'arrosage (« pos. ? »), `input number` des seuils (station, 3e_C9.2).

Contrôles du dépôt : `controle_tactile`, `controle_debordement`, `controle_hierarchie`, `controle_contraste_liens`
(2 liens CC pâles **sur le papier** dans 2 QCM dont le pied s'imprime en gris ; 119 pages colorent `a` sans `a:visited`,
déjà connu), `controle_hors_ligne` ✅, `controle_impression` ✅.

Non vu : navigation au clavier pas à pas (ordre de tabulation, focus visible) ; lecteur d'écran réel ; zoom 200 % ;
smartphone (le banc 4e_C8 signale un débord de 15 px à 390 px, préexistant).

### Point 4 — Liens, ressources, CSV, JavaScript, sauvegardes : rien à signaler

- Balayage navigateur (script du skill, serveur sensible à la casse comme GitHub Pages) : **408 pages ouvertes, 0 constat**
  (aucune image non décodée, aucun 404, aucune erreur JS, aucun `console.error`).
- `controle_liens.py`, `controle_atteignabilite.py`, `controle_fichiers_telechargeables.py`, `controle_medias.py` : verts.
- Sauvegardes : voir A05 ; effacement vérifié au navigateur.
- `controle_regle4.py` (bouton QCM à 54 %) et `controle_effectifs_qcm.py` (manifest Shenzhen 18/19) : rouges **déjà
  connus** du rapport du 07/11.

### Point 1 — Thèmes 2 et 3 : jardin connecté, capteurs d'humidité, station cyclonique

Lecture ciblée des trois séquences nommées, chiffres et unités relevés ligne à ligne :
- **Arrosage / humidité (4e_C6.1-C6.3)** : cohérent de bout en bout — seuil unique à 40 % → battement, hystérésis 35/45,
  plage horaire, scénarios 33/38/46/33 %, transposition au lampadaire 20/40 lux ; ordres de grandeur d'éclairement exacts.
- **Station cyclonique (3e_C4.3-C4.6)** : CAN 10 bits sur 868–1 018 hPa → 0,1466 hPa par palier, N = 512 ↔ 943 hPa : juste.
  Point de rigueur, même nature que A02 (**décision 5**) : « 132 > 118 → vigilance violette » assimile un **seuil de vent
  d'ouragan** (118 km/h, vent moyen) à un **niveau de vigilance**, qui est une décision préfectorale ; dire « la station
  propose un niveau d'alerte, le préfet décide de la vigilance », et préciser que 118 km/h vaut pour le vent moyen, pas la
  rafale.
- **Jardin connecté (4e_C4.1-C4.9)** : rien à signaler sur les grandeurs (10 L/j, 12 V, flexibilités F0/F2).

### Point 5 — Traçabilité compétence → production → critère

Le rapport hebdomadaire (`docs/audits/RAPPORT_AUDIT_2026-11-07.md`) tient déjà la matrice des 114 codes et la preuve au
QCM. Croisement fait ici sur les 60 séquences : **24 séquences n'ont pas l'échelle des quatre niveaux LSU** décidée le
23/10 (dont jardin connecté 4e_C4.1, station cyclonique 3e_C4.3, Book Train, SOS station, dépanner lampadaire,
programmer l'alerte 3e_C6.1, les trois pages de la station 3e_C9.2) ; 10 n'ont pas d'auto-positionnement. C'est la
matière de la révision séquence par séquence déjà planifiée (`revision-sequence`, `SUIVI_REVISION.md`) — **décision 6**.

## 3. Décisions pour Pascal

1. **Export local des réponses** (A05) : « Imprimer / PDF » suffit-il, ou veut-il un export JSON « sans données
   personnelles » sur chaque séquence (fonctionnalité transversale, règle d'or à écrire) ?
2. **QCM et poste partagé** : les 73 QCM gardent un score dans le navigateur sans note. Note obligatoire aussi sur les
   QCM (le contrôle la refuserait alors), ou tolérée (état actuel : comptée, pas refusée) ?
3. **Longueur des bonnes réponses** dans les 10 séquences au gabarit n°300 : étendre `controle_longueurs.py` aux séquences
   et réécrire les distracteurs trop courts — travail d'auteur, pas mécanique.
4. **Structure accessible du gabarit n°306** : un `<main>` par page (266 pages) et des titres sans saut h2 → h4
   (51 pages) ; à poser dans le squelette et `controle_squelette.mjs`, puis par vagues.
5. **Vigilance violette** (3e_C4.3) : reformuler comme proposé ci-dessus.
6. **Échelle LSU** dans les 24 séquences qui ne l'ont pas : confirmer que c'est le fil des vagues de révision.
7. **Pages hors gabarit** (cybersécurité, numérique-société, Pix, bonus 2FA, QCM algorigrammes) : les passer au gabarit
   n°306, ou les archiver.

## 4. Ce que ce lot ajoute au dépôt

- `_outils/controle_sauvegarde_locale.py` — effacement, note poste partagé, pas de `confirm()` (+ `--corriger`).
- `_outils/controle_ordre_propositions.py` — la bonne réponse ne se devine pas à sa place (+ `--corriger`).
- Les deux inscrits dans `rapport_audit.py`, avec `controle_gestes_outil.py` et `controle_licence.py`.
- `make_index.py` : renvoi des codes mutualisés ; `licence_cc.py` : mention lisible ; `papier.js` : nouveaux titres
  d'écran ; `kit.js` : `armerDeuxClics` ; quatre générateurs posent la licence eux-mêmes (n°321, n°283).

## 5. Non vu

Le réseau extérieur hors `controle_hors_ligne` ; tout ce qui n'apparaît qu'après plusieurs clics (question suivante d'un
QCM, panneaux ouverts) ; la version publiée (GitHub Pages) — à ouvrir depuis l'index publié après fusion ; lecteur
d'écran ; clavier pas à pas ; les 60 pages lues en entier (seules les trois nommées l'ont été, et par leurs chiffres).
