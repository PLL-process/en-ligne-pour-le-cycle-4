# Audit des séquences cycle 4 — Étape 4 : campagne technique sur le dépôt cloné

Date : 8 novembre 2026. Dépôt à `5a714ba` (après fusion de la PR #621).
Suite des étapes 1 à 3 du 1er novembre (audit documentaire, sans navigateur ni code source).

> Cette étape **exécute** ce que les trois premières n'avaient pas pu faire : lecture du code source,
> clic sur chaque bouton « Vérifier », inspection de la sauvegarde locale, contrôles du dépôt entier.
> Chaque constat des étapes 1 à 3 reçoit un verdict : **confirmé**, **nuancé** ou **infirmé**.
> Ce qui n'a pas été exécuté est listé à la fin, et n'est pas présenté comme réussi.

## Méthode

| Moyen | Périmètre | Résultat brut |
|---|---|---|
| Lecture du code source (HTML, JS, générateurs Python) | 4 séquences ciblées + recherche sur tout le dépôt | voir fiches |
| Banc Playwright (Chromium, 1 100 px puis 375 px) — clic sur chaque « Vérifier » à vide, console, `localStorage`, `Effacer`, Tab | Chengdu 5e_C1.1 · Jardin 4e_C4.1 · Station 3e_C4.3 · Station 3e_C9.2 | 29 boutons, 0 erreur console, 0 réussite à vide |
| `_outils/controle_liens.py` | dépôt entier (hors `_archive`) | ✅ aucun lien mort, aucune ancre introuvable |
| `_outils/controle_fichiers_telechargeables.py` | dépôt entier | ✅ chaque fichier nommé se prend d'un clic |
| `_outils/controle_boutons_vivants.py` | 410 pages | ✅ 157 fonctions appelées, 0 écart |
| Lecture des 88 CSV (encodage, séparateur, régularité des colonnes) | dépôt entier | 5 fichiers irréguliers (fiche T4) |
| Analyse de `index.html` et de `_outils/make_index.py` | 114 repères | fiche T1 |

---

## Partie 1 — Verdict sur les constats des étapes 1 à 3

### A01 / A3-01 à A3-03 / Fiche A — Traçabilité des repères mutualisés → **confirmé, cause trouvée, portée élargie**

- **Mesuré** : 58 repères portent « 🔗 Couvert par une séquence mutualisée » dans l'index ; **aucun des 58** n'offre un lien vers la séquence qui le travaille ; 43 affichent en plus « Aucune ressource pédagogique publiée pour ce repère ».
- **Cause** : le dossier de chaque repère mutualisé contient bien un `README.md` pointeur qui nomme la séquence, l'activité et la production (ex. `5e_C1.6/README.md` → « Le compte du club », activités 0, 1, 4, 15 questions du QCM sur 30). Mais `_outils/make_index.py` (ligne 590) n'affiche que les fichiers HTML du dossier ; quand il n'en trouve pas, il écrit « Aucune ressource… » et range le README sous « 🔧 Fichiers de gouvernance ». L'information existe, l'index ne la lit pas.
- **Correction** (une seule, dans le générateur, règle n°283) : dans `make_index.py`, pour un repère au statut mutualisé, lire le premier lien `sequence_*.html` du `README.md` et écrire « Travaillé dans la séquence [titre] (lot X) → ouvrir », à la place de « Aucune ressource pédagogique publiée ». 58 repères corrigés d'un coup ; `tests_index.py` à compléter d'un cas.
- Priorité : **élevée** (c'est le constat le plus répété des trois étapes).

### A02 — Définition de la précision (Chengdu) → **confirmé**

- Texte en page : « précision (± 10 % contre ± 2 %) », puis dans « Les mots de la planche » la précision définie comme écart possible à la vraie valeur.
- Correction éditoriale : ajouter « valeurs supposées pour cet exercice » au tableau « Les chiffres pour choisir », et dans le lexique distinguer en une ligne chacune : *justesse* (près de la vraie valeur), *fidélité* (même résultat quand on recommence), *incertitude* (le ± annoncé). Priorité moyenne.

### A03 — Nettoyage d'un boîtier fermé (Chengdu) → **confirmé**

- Le tableau dit : « un nettoyage régulier — sinon la mesure dérive sans prévenir (boîtier fermé : le collège ne peut pas l'entretenir) » ; la correction complète de l'activité 1 propose « …à une autre source, ou nettoyer ».
- Correction : dans la correction, remplacer « ou nettoyer » par « ou faire remplacer le module (boîtier fermé, maintenance externe) ». Priorité moyenne.

### A04 — Titre de l'échauffement tableur (Chengdu) → **confirmé, éditorial**

- Titre en page : « Avant de commencer (échauffement) — les quatre gestes du tableur », placé entre l'activité 1 et l'activité 2.
- Le libellé « (échauffement) » est une décision de Pascal (encarts des gestes d'outil, PR #369) : **on ne le change pas**. Proposition minimale : sous-titre « Pour l'activité 2 » en une ligne. Priorité faible.

### A05 — Sauvegarde locale sur poste partagé → **confirmé et aggravé** (voir fiches T2 et T3)

### Fiche B — 612 ÷ 1023 ≈ 60 % (Jardin) → **confirmé**

- Texte en page, trois fois : « un TRAITEMENT de la carte : 612 ÷ 1023 ≈ 60 % ». Le « × 100 » est implicite ; le statut « indice simulé » n'est pas dit à cet endroit.
- Correction : « 612 ÷ 1023 × 100 ≈ 60 % — un indice d'humidité **simulé pour l'exercice** (un vrai capteur se règle avec deux mesures : sol sec, sol trempé) ». Trois occurrences + la ligne `3_1:` du JS de correction. Priorité moyenne.

### Fiche C — « 12 V est une très basse tension, sans danger au toucher » → **confirmé, portée élargie**

- Présent dans **10 pages** (jardin 4e_C4.1 et 4e_C6.2, 4e_C8.1, 3e_C7.1, ateliers interacteurs/exigences/FAST, cahiers 4e et 3e, synthèse FAST). La phrase vient de **4 générateurs** : `donnees_fast.py` (l. 664), `donnees_interacteurs.py` (l. 687), `synthese_fast.py` (l. 153), `donnees_exigences.py` (l. 639, variante « 24 V »).
- Correction **dans les générateurs** puis régénération (règle n°283, même leçon que la PR #621) : « 12 V est une très basse tension : dans la maquette, avec une alimentation adaptée et protégée, sous la surveillance du professeur, on peut la manipuler. On n'intervient jamais sur une installation sous tension. » Priorité **élevée** (sécurité, texte lu par l'élève).

### Fiche D — Scores de quiz ≠ compétence validée → **nuancé**

- Mesuré : les compteurs « 9/9 », « 4/4 »… ne comptent que les widgets (radios, menus) ; les productions manuscrites (schéma recopié, argumentaire) ne sont pas comptées — c'est la conception, pas une panne.
- Décision pour Pascal : afficher « quiz : 9/9 » et, séparément, « production : à montrer au professeur » avec les critères des quatre niveaux LSU (déjà présents dans les séquences différenciées). Priorité moyenne.

### Fiche E — IP fixe hors plage DHCP → **confirmé, faible**

- Texte : « …hors de la plage distribuée par le DHCP ». Ajouter une note : « Autre solution : la réservation DHCP sur la box ». Priorité faible.

### Fiche F — Station d'alerte cyclonique → **partiellement exécuté**

- Dynamique : 3e_C4.3 (7 boutons) et 3e_C9.2 (8 boutons) : chaque « Vérifier » répond, aucun ne réussit à vide, 0 erreur console, pas de défilement de côté à 375 px, 45 images toutes avec `alt`.
- Non fait : cohérence des seuils avec la vigilance Météo-France, comportement aux valeurs limites et capteur débranché — ce sont des tests pédagogiques qui demandent de jouer les simulateurs valeur par valeur (reste à l'étape 5).

---

## Partie 2 — Constats nouveaux de la campagne technique

### T1 — L'index ignore les README pointeurs — **élevée** (détail en A01 ci-dessus)

### T2 — « Effacer ma sauvegarde » n'efface pas tout — **élevée**

- **Mesuré** (Playwright) : sur le jardin 4e_C4.1, après saisie puis double clic sur « 🗑 Effacer ma sauvegarde », la clé `seq_4e_C4.1-C4.9_jardin_connecte` disparaît mais **`rep_interacteurs-pieuvre_4e_e6` reste** (l'exercice d'atelier incrusté). Même chose sur 3e_C9.2 : `rep_rappel-cdc_station-programmee-3e` reste.
- **Cause** : le bouton `#btnReset` ne retire que la clé `KEY` de la page ; les incrustations d'atelier écrivent sous leurs propres clés `rep_*` et ne sont pas prévenues.
- **Portée** : 58 pages ont le bouton ; **33** portent aussi une clé `rep_*` → l'effacement est incomplet sur 33 pages. Sur Chengdu (pas d'incrustation), l'effacement est complet ✅.
- **Correction** : dans le gabarit, au clic sur « Effacer », supprimer aussi toute clé `rep_*` présente dans la page (`document.querySelectorAll('[data-cle^="rep_"]')`) ; ajouter un contrôle `_outils/controle_effacement.mjs` qui saisit, efface, et refuse toute clé restante (règle n°299 : sortie 0/1/2).

### T3 — L'identité de l'élève est écrite en clair dans le navigateur — **élevée**

- **Mesuré** : Nom, Prénom, Classe saisis dans la carte d'identité sont écrits en clair dans `localStorage` (jardin, station C4.3, station C9.2 : `identite_en_clair = true`). **95 pages** portent les champs `id_nom`/`id_prenom`/`id_classe` ; **0** page affiche un avertissement « poste partagé ».
- **Risque** : sur un poste de collège à session commune, l'élève suivant voit le nom et les réponses du précédent.
- **Correction** (deux lignes dans le gabarit) : sous la carte d'identité, « ⚠ Poste partagé ? Clique sur Effacer ma sauvegarde avant de partir : ton nom et tes réponses restent sinon dans ce navigateur. » ; et proposer « Ne pas enregistrer mon nom » (case cochée par défaut sur `id_nom`/`id_prenom`), le nom servant alors seulement à l'impression de la séance.

### T4 — Cinq CSV irréguliers sur 88 — **faible**

- Élève : `3e_C4.3/donnees/mesures_station_48h_simulees.csv` commence par une ligne de commentaire `# Données SIMULÉES…` : utile, mais à l'ouverture dans un tableur les en-têtes tombent en **ligne 2**. Écrire en page : « ligne 1 = note, en-têtes en ligne 2 », ou déplacer la note dans un `LISEZMOI.txt` à côté.
- Enseignant (matrices de couverture) : `4e_C1.1` l. 37 et `3e_C9.2` l. 25 ont un « ; » non échappé dans une cellule (9 champs au lieu de 8) ; `4e_C6.2` l. 14-18 et `4e_C7.6` l. 7 portent des lignes `#`. Aucun élève ne les lit ; à corriger quand on repasse dessus.

### T5 — Ce qui est vert et le reste

- **Boutons « Vérifier »** : 29 sur 4 pages, tous répondent, aucun ne réussit à vide ; messages gradués (🔴/🟡/🎉) ; retours insérés par `textContent`/`echapper()` dans le jardin (pas d'injection HTML possible par ce chemin). Les tests « synonyme, casse, accents » des étapes 1-3 **ne s'appliquent pas** : il n'y a aucune réponse libre notée par la page — tout est radios ou menus ; la seule saisie libre notée (table + courbe du jardin) vérifie date, heure, ordre chronologique, doublons et unité, et renvoie des liens vers la case fautive ✅.
- **Clavier** : parcours Tab complet sur Chengdu (37 arrêts) et jardin (10 arrêts visibles, les onglets masquent les autres séances) : chaque élément atteint porte un indicateur de focus ✅.
- **Mobile 375 px** : 0 px de défilement horizontal sur les 4 pages ✅. **Images** : 73 images, toutes avec `alt` ✅. Un seul `h1` par page ✅.

---

## Partie 3 — Non exécuté (à ne pas lire comme réussi)

1. Contrastes WCAG AA mesurés (`controle_contraste_liens.mjs` : dépendance Node absente dans l'environnement).
2. Zoom 200 %, orientation tablette, lecteur d'écran.
3. Mode essentiel (`controle_mode_essentiel.py`) et verrous (`controle_verrous.mjs`) sur les 4 pages.
4. Seuils, valeurs limites et capteur débranché des simulateurs de la station (fiche F).
5. Matrice exhaustive compétence → URL → consigne → production → critère : le `rapport_audit.py` du 07/11 en tient déjà la partie couverture (114 codes) ; la colonne « production observable » reste à ajouter.

---

## Ordre proposé pour le lot correctif

| # | Correction | Fichiers | Effet |
|---|---|---|---|
| 1 | Index lit les README pointeurs (T1/A01) | `_outils/make_index.py`, `tests_index.py` | 58 repères |
| 2 | Effacer efface aussi les `rep_*` + contrôle (T2) | gabarit, `_outils/controle_effacement.mjs` | 33 pages |
| 3 | Avertissement poste partagé + nom non enregistré (T3) | gabarit, carte d'identité | 95 pages |
| 4 | « 12 V sans danger » dans les 4 générateurs, puis régénération (Fiche C) | `donnees_fast.py`, `donnees_interacteurs.py`, `synthese_fast.py`, `donnees_exigences.py` | 10 pages |
| 5 | Chengdu A02, A03 ; Jardin B, E ; note CSV station (T4) | 3 pages | éditorial |
| 6 | Décision de Pascal : Fiche D (quiz / production), A04 | — | — |

Chaque ligne = une PR, contrôle qualité du lot avant livraison (skill `controle-qualite-lot`).
