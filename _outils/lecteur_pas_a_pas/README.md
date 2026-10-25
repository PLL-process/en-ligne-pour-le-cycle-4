# Lecteur pas à pas commun

**Décisions de Pascal, 25/10/2026 : « 1a 2a 3b 4b ».** Branche `fable/lecteur-pas-a-pas` (transversale).

- **1a** — 4e_C8.1 jardin (`theme-3-…/C8-…/4e/4e_C8.1/sequence_4e_C8_jardin-validation.html`) : animer
  **la situation déclenchante** (« Une année sur le toit ») **et le banc de l'activité 0** (quatre postes).
- **2a** — voix SIWIS (Piper `fr_FR-siwis-medium`, mêmes réglages et même chaîne audio que les trois principes
  de Chengdu : `5e_C1.1/_generation/voix_trois_principes/`).
- **3b** — l'ancien schéma fixe de la situation (trois boîtes, « IMAGE-OBJET ») est **supprimé** ; à l'impression
  et sous « mouvement réduit », l'animation montre sa planche fixe (règle n°119).
- **4b** — **maintenant** : un lecteur pas à pas **commun** à toutes les animations, source unique + contrôle,
  comme l'agrandisseur (`theme-3-…/audit/loupe.py`, `_outils/controle_loupe.py`).

## Les animations concernées

| Animation | Page | Préfixe actuel | Voix | Particularités |
|---|---|---|---|---|
| Herschel | `theme-1-…/C1-…/3e/3e_C1.1/sequence_3e_C1.1-C1.4_tsinghua_feux.html` | `hpp` | non | 7 étapes ; prédiction obligatoire à l'étape 6 (« Voir le résultat ») ; bouton d'ouverture ; volet du schéma fixe ouvert à l'impression |
| Vélo-cargo | `theme-1-…/C3-…/5e/5e_C3.1/sequence_5e_C3.1-C3.4_shanghai.html` | `vpp` | oui | figure isométrique (`figure_iso_velo_cargo`), rotation ; bouton d'ouverture |
| Trois principes | `theme-1-…/C1-…/5e/5e_C1.1/sequence_5e_C1.1-C1.6_chengdu_air.html` | `tpa` | oui | 11 étapes ; chapitres ; Regarder / Écouter / Pause ; compteur, lentille, horloge, balance, jauge ; finale à curseur |
| Jardin (nouveau) | `theme-3-…/C8-…/4e/4e_C8.1/sequence_4e_C8_jardin-validation.html` | — | oui | situation : dernière étape = tâche (« écris ton hypothèse ») ; banc : 4 postes, des mesures sans verdict |

**Comment une page s'en sert** (voir l'appel dans Chengdu) : la page marque ses éléments `data-lpp="dessin"`,
`titre`, `texte`, `compte`, `prec`, `suiv`, `zero`, `regarder`, `ecouter`, `sansvoix` (et `ouvrir` + `panneau`
pour un bloc replié), ses chapitres `data-aller="n"`, les parties du dessin `data-de="n"` / `data-a="n"`, puis
appelle `LecteurPasAPas(bloc, {scenes, voix, onglet, imprimer, maj, fixe, tourne, entrer, avant, ouvrir})`.

Commun aux trois : un dessin SVG dont les éléments `[data-des="n"]` apparaissent à l'étape n (décalés par
`--i`), une phrase par étape dans une zone `aria-live`, Précédent / Suivant / Recommencer, « Étape n / N »,
`data-loupe="non"`, rien sans geste, aucune transition sous « mouvement réduit », lien direct `#…-pas-a-pas`.

## Plan et avancement

- [x] 0. Branche `fable/lecteur-pas-a-pas` et plan (ce fichier).
- [x] 1. Relevé des trois lecteurs (tableau ci-dessus) ; le lecteur commun est tiré de celui de Chengdu, le plus complet.
- [x] 2. Lecteur commun : `lecteur.css`, `lecteur.js` (source unique), `poser.py` (pose ou met à jour le bloc
      entre marqueurs, avant `</head>`), `_outils/controle_lecteur_pas_a_pas.py` et son banc (11 / 11).
- [x] 3. Chengdu passe au lecteur commun : `tests_animation_trois_principes.py` 50 / 50, `tests_5e_C1.1_chengdu.py`
      43 / 43, `tests_regle_311_5e_C1.1.mjs` 33 / 33.
- [x] 4. Jardin : situation « Une année sur le toit » (7 étapes, voix SIWIS `Audio/situation_scene1…7`, générateur
      `_generation/voix_situation/`, prises **à écouter**) ; banc de l'activité 0 animé (4 postes, mesures sans
      verdict, script `banc_anime`) ; ancien schéma et « IMAGE-OBJET » retirés ; `tests_4e_C8.mjs` 48 / 48.
- [x] 5. Vélo-cargo passe au lecteur commun (`mot: "Scène"`, `data-des`/`data-seul` lus tels quels, « Regarder »
      s'arrête à la scène 4 par `avant(…, auto)`) : `tests_5e_C3.1-C3.4_shanghai.py` 35 / 35, `tests_voix_velo_cargo.py`
      24 / 24, `tests_regle_311_5e_C3.1.mjs` 26 / 26.
- [x] 6. Herschel passe au lecteur commun : `tests_3e_C1.1-C1.4_tsinghua.py` 50 / 50, `tests_regle_311_3e_C1.1.mjs` 33 / 33.
      **Banc commun** `banc_lecteur.py` : les 4 animations parcourues à 1280 / 390 px et sous « mouvement réduit »,
      voix sur le disque, impression, lien direct — vert. `controle_lecteur_pas_a_pas.py` : sortie 0.
- [x] 7. Journal (entrée du 25/10/2026), nouveautés, SOURCES_MEDIAS du jardin, rapport de tests, audit et index,
      contrôles du dépôt comparés à `main`, captures, PR.

## Ajouter une animation

1. Écrire le bloc dans la page : un élément d'id `<nom>-pas-a-pas` qui porte `data-lpp-racine`, le dessin, les zones
   `data-lpp` (voir plus haut) ; les parties du dessin avec `data-de` / `data-a`.
2. Écrire son script : le tableau `SCENES` (`t`, `p`, `d`), puis `LecteurPasAPas(bloc, {…})`.
3. `python3 _outils/lecteur_pas_a_pas/poser.py <page.html>` pose le lecteur.
4. Voix : copier un générateur (`4e_C8.1/_generation/voix_situation/`), puis faire écouter les prises à Pascal.
5. `python3 _outils/controle_lecteur_pas_a_pas.py` et `python3 _outils/lecteur_pas_a_pas/banc_lecteur.py`.

**Corriger le lecteur** : modifier `lecteur.js` ou `lecteur.css` ici, puis relancer `poser.py` sur chaque page qui le
porte (le contrôle les nomme), puis le banc commun et les bancs des quatre pages.
