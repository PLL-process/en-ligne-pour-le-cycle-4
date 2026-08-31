# Rapport de tests — Lot 5e_C6.1 → C6.3 « Programmer le lampadaire »

**Suite** : `tests_5e_C6.1-C6.3.mjs`, livrée dans ce dossier · **Outil** : Playwright
(Chromium headless), viewport mobile 390 × 844 · **Rejouée le 31/08/2026** ·
**Verdict : 32 / 32 ✅**

```
cd theme-2-.../C6-.../5e/5e_C6.1 && node tests_5e_C6.1-C6.3.mjs
```

> **Ce que ce rapport disait avant le 31/08/2026.** Il portait 23 coches et les
> attribuait à un script nommé `tests_lot07.js` — qui n'a jamais été commité. Le
> relevé de `_outils/controle_rapports_tests.py` l'a mis en tête de la file des
> lots à payer ; la suite ci-dessus le paie (règles d'or n°259 et n°266). Les
> observations d'origine sont conservées plus bas, sous leur date.

> **Correction du 31/08/2026 — le verrou expérientiel s'ouvrait à moitié tout seul.**
> `_outils/controle_verrous.mjs` ouvre chaque séquence du dépôt dans un navigateur
> neuf et lit `window.__exp` juste après le chargement. Cette page en portait déjà la
> clé `defaut` **avant tout geste** : la fonction d'affichage du simulateur était
> appelée à l'initialisation et enregistrait l'état affiché comme une observation. Le
> verrou de l'activité 3 s'ouvrait donc en partie sans que l'élève ait rien manœuvré,
> ce que la règle d'or n°226 interdit. La fonction ne trace plus que sur un geste. Les
> contrôles 3, 9, 12, 14, 15 et 19 ci-dessous éprouvent maintenant les deux moitiés de
> ce verrou, dans les deux sens.

## Ce que la suite ne recopie pas

Aucune réponse attendue n'est écrite dans le script : elles sont extraites des
fonctions `CHECKS` de la page — **28 champs**, selon les deux conventions que ce lot
emploie, l'objet `att = {id: "valeur"}` **et** le champ numérique comparé à part,
`num("e1_7") === 30`. Ne lire que la première rendait 7 / 8 à une activité que la page
compte juste : une convention oubliée fait accuser la page à tort.

Les trois nombres de la mission (réglage d'origine, seuil minimal, luminosité) sont
lus dans le source de `majSim`, et les positions de curseur sont bornées par les `min`
et `max` réels des curseurs — la suite ne pilote pas des valeurs qu'elle aurait
décidées elle-même (règle d'or n°268).

## Séquence — 22 contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 1 | Chargement, titre, les trois codes 5e_C6.1 / C6.2 / C6.3 annoncés | ✅ |
| 2 | Trois onglets de séance, bascule S3 puis S1 | ✅ |
| 3 | **Aucune expérience enregistrée au chargement** — `__exp` vide (n°226) | ✅ |
| 4 | 28 champs attendus extraits des `CHECKS` de la page | ✅ |
| 5 | Rappel d'hypothèse : caché tant que rien n'est écrit, puis affiché mot pour mot | ✅ |
| 6 | Activité 1 validée **8 / 8** (entrées, sorties, paramètres, états) | ✅ |
| 7 | Activité 2 validée **9 / 9** (six étapes + SI / ET / SINON) | ✅ |
| 8 | Formes de l'algorigramme **4 / 4** (rectangle, losange, boucle) | ✅ |
| 9 | **Activité 3 REFUSÉE malgré 3 réponses justes** — le verrou tient | ✅ |
| 10 | Réglage de la mission lu dans la page : origine 30, seuil > 45, luminosité 45 ; curseur seuil borné à [10 ; 60] | ✅ |
| 11 | Au réglage d'origine, la lampe passe de « éteint » (jour) à « veille » (nuit) | ✅ |
| 12 | Le premier essai est enregistré comme expérience — **et lui seul** | ✅ |
| 13 | Passage détecté → PLEINE PUISSANCE, durée annoncée suivant le curseur (2 s → 10 s) | ✅ |
| 13 bis | Le passage retombe seul après les 2 s **en vigueur au moment du clic** | ✅ |
| 14 | Mission mairie : seuil à 50 puis luminosité à 45 → vérifiée, lampe en veille | ✅ |
| 15 | Activité 3 validée **3 / 3** une fois les deux essais faits — le verrou s'ouvre | ✅ |
| 16 | Activité 4 validée **4 / 4** (réinvestissement : arrosage du jardin) | ✅ |
| 17 | Progression 4 / 4 et les trois onglets portent leur coche | ✅ |
| 18 | Le tableau de bord des tâches suit l'onglet actif et coche ce qui est fait | ✅ |
| 19 | Rechargement : réponses, validations **et les deux moitiés du verrou** restaurées | ✅ |
| 20 | Les 7 liens internes (QCM, lexique, synthèses, îlot 5e_C4.1, index) existent | ✅ |
| 21 | Les 2 SVG référencés par la séquence existent sur le disque | ✅ |
| 22 | Hors ligne : aucune ressource distante, aucune modale, aucune erreur JS | ✅ |

Le contrôle 13 bis note un comportement de la page qui n'est pas un défaut, mais qui
se raconte : le minuteur du passage retient la durée **en vigueur au clic**. Déplacer
le curseur pendant un passage change l'affichage, pas la durée déjà lancée.

## QCM — 9 contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 23 | Chargement, titre, taille annoncée exacte (badge et compteur) | ✅ |
| 24 | 30 questions, **10 par code** sur les trois codes | ✅ |
| 25 | Bonnes réponses A/B/C/D = **7 / 7 / 8 / 8** (écart 1) et `d[r]` vide partout | ✅ |
| 26 | **3** questions illustrées, fichiers SVG présents sur le disque | ✅ |
| 27 | Gabarit maison complet : 4 options, 4 réfutations, `expl`, `ex`, `err`, `ret` | ✅ |
| 28 | Parcours **30 / 30 joué question par question** → **20,0 / 20**, bilan sur 3 compétences à 10 / 10 | ✅ |
| 29 | La clé `localStorage` du QCM est écrite | ✅ |
| 30 | Le lien de retour vers la séquence pointe sur un fichier réel | ✅ |
| 31 | Aucune erreur JS sur le QCM | ✅ |

## Deux nombres du manifeste remis d'aplomb

Le contrôle 26 a fait apparaître un écart que `manifest_lot_07.json` portait depuis le
25/07/2026 : il annonçait **2** questions illustrées et **2** images, alors que le LOT 12
avait ajouté un troisième SVG (`Images/lampadaire_seuil_jour_nuit.svg`) — documenté
dans `SOURCES_MEDIAS.md`, mais jamais reporté dans le manifeste. Les trois champs
concernés (`questions_illustrees`, `fichiers.images`, `medias_licences`) sont corrigés.

**Ce lot n'est pas le seul.** La mesure faite le 31/08/2026 sur les 32 manifestes du
dépôt en trouve **dix** dans ce cas — dont un second écart de `questions_illustrees`
(`5e_C2.1`, thème 1) et huit listes `images` incomplètes.
`_outils/controle_effectifs_qcm.py` ne confronte pas encore ces deux champs : le
contrôle est à étendre, et c'est le prochain travail annoncé (règle d'or n°261 —
corriger l'occurrence qu'on a sous les yeux, c'est croire qu'il n'y en a qu'une).

## Ce que le manifeste ne disait pas non plus

Le bloc `fichiers` de ce manifeste — et de six autres manifestes du thème 2 — ne
nommait aucune suite de tests, alors qu'une suite était livrée à côté. La convention
`suite_de_tests`, née au thème 1, y est maintenant portée. Les huit manifestes du
thème 3 dans le même cas sont hors du périmètre d'une branche « thème 2 » : ils feront
l'objet d'une PR sœur.

## Observations d'origine du 23/07/2026 (non rejouables telles quelles)

Le rapport initial portait 23 coches : séquence 13, QCM 5, synthèses 2, index 3. La
suite ci-dessus reprend et élargit les 18 premières. Les 5 dernières — synthèses élève
et professeur sans erreur, badge NEW sur l'index, ancre auto-ouverte, pointeur 5e_C6.3
— portent sur des pages hors de ce dossier et restent couvertes par les contrôles de
dépôt (`_outils/build_audit.py`, `_outils/make_index.py`, `_outils/controle_verrous.mjs`).

## Limites connues

- Google Fonts inaccessible en sandbox : polices de repli, sans incidence — la suite
  ne compte pas ces requêtes comme des ressources distantes de la page (règle n°40).
- Version 🅰 (maquette + VittaScience) non testable en sandbox : annoncée comme option,
  **très basse tension uniquement**.
