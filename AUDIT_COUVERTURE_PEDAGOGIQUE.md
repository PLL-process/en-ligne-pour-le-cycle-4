# 🔍 Audit de couverture pédagogique — Technologie cycle 4 (programme 2024)

*Audit initial réalisé le 21 juillet 2026 sur la branche locale
`audit/couverture-initiale-2026-07` (commit de départ : `81acfb5`).
Aucune modification distante n'a été effectuée.*

**Fichiers compagnons :** `audit_couverture.csv` (tableur, séparateur `;`),
`audit_couverture.json` (machine), `FEUILLE_DE_ROUTE_COMPLETION.md` (plan d'action),
`_outils/build_audit.py` (générateur régénérable).

---

## 1. Périmètre et méthode

### 1.1 Ce qui a été réellement analysé

Fichiers ouverts et lus intégralement ou par sondage structuré :

| Élément | Méthode |
|---|---|
| `README.md`, `RAPPORT_MIGRATION.md`, `RAPPORT_QCMS.md`, `RAPPORT_INTEGRATION_BRANCHE.md` | lecture intégrale |
| `index.html` | lecture + vérification automatique des 33 liens locaux (0 cassé) |
| `_outils/` (make_index.py, data_competences.py, qcm_generator.py, build_qcms.py, banks_a/b.py) | lecture du code |
| Les 114 dossiers de codes | inventaire automatique des fichiers réels (hors `.gitkeep`) |
| Les 8 séquences HTML existantes | scan structuré de 13 marqueurs pédagogiques (situation déclenchante, problématique, mission, référentiel, socle, CRCN, séances, synthèse, évaluation/LSU, différenciation, EDD, mode enseignant, sauvegarde/export) |
| La séquence modèle « Jardin connecté » 4e_C6.2 | lecture détaillée (référence de gabarit) |
| Tous les HTML actifs | vérification automatique des liens locaux `href`/`src` |
| `_archive-anciennes-versions/` | inventaire (93 fichiers, non modifiés) |
| `_ressources-communes/` | inventaire (13 fichiers) |

### 1.2 Chiffres clés

| Indicateur | Valeur |
|---|---|
| Codes du référentiel | **114** (38 par niveau, confirmé par `data_competences.py`) |
| Codes avec au moins un fichier réel | **13** |
| Codes entièrement vides (squelette `Images/` + `Synthèses/`) | **101** |
| Séquences HTML réellement enseignables en l'état | **1** (Jardin connecté 4e_C6.2) — les autres nécessitent des compléments |
| Liens locaux cassés dans les HTML actifs | **29** occurrences dans 5 fichiers (détail §4) |
| Taille du dépôt | 62 Mo (dont ~9,3 Mo d'images non optimisées dans 5e_C1.3 et ~2,6 Mo dans 4e_C4.7) |

### 1.3 Référentiel opérationnel et convention de nommage (confirmés)

Le référentiel opérationnel du dépôt est **`_outils/data_competences.py`**
(114 codes, formulations, domaines du socle) : transcription retenue, fondée sur
la proposition Nathan correspondant au référentiel de technologie 2024
(*confirmé par la gouvernance le 21/07/2026*). Le classeur
`Référentiel_Technologie_Cycle4_2024.xlsx` n'est pas versionné dans le dépôt ;
`data_competences.py` fait foi. L'audit s'appuie donc sur ce fichier.

Les identifiants préfixés (`5e_C1.1`, `4e_C4.4`, `3e_C9.1`…) sont la
**convention interne officielle du dépôt** : le niveau placé devant le code
rend chaque sous-compétence unique et classable (la numérotation `C1.1 → C9.3`
repart de zéro dans chaque cahier). Cette convention est conservée dans tous
les livrables.

---

## 2. État par statut (vue d'ensemble)

| Statut | Nombre | Codes |
|---|---|---|
| `COMPLET ET VALIDABLE` | 1 | 4e_C6.2 (Jardin connecté — séquence modèle) |
| `EXISTANT À AMÉLIORER` | 5 | 5e_C1.1 · 5e_C1.3 · 4e_C1.4 · 3e_C1.5 · 3e_C6.2 |
| `À CORRIGER` | 2 | 5e_C1.2 (mhtml) · 3e_C9.1 (17 liens d'images cassés) |
| `PARTIEL` (QCM isolé, pas de séquence) | 4 | 4e_C2.1 · 4e_C4.1 · 4e_C4.4 · 4e_C4.7 |
| `COUVERT PAR UNE SÉQUENCE MUTUALISÉE` | 1 | 5e_C1.4 (→ 5e_C1.3, README pointeur en place) |
| `À CRÉER` | 101 | tout le reste (détail complet dans le CSV/JSON) |

Le détail code par code (formulation officielle, socle, fichiers présents, qualité,
anomalies, statut) est dans **`audit_couverture.csv`** — 114 lignes, ouvrable dans
LibreOffice Calc.

### Couverture par niveau et par compétence (codes non vides / total)

| | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | Total niveau |
|---|---|---|---|---|---|---|---|---|---|---|
| **5e** | 4/6 | 0/2 | 0/4 | 0/8 | 0/3 | 0/3 | 0/6 | 0/3 | 0/3 | **4/38** |
| **4e** | 1/4 | 1/2 | 0/3 | 3/9 | 0/3 | 1/3 | 0/8 | 0/3 | 0/3 | **6/38** |
| **3e** | 1/5 | 0/1 | 0/4 | 0/8 | 0/4 | 1/3 | 0/8 | 0/3 | 1/2 | **3/38** |

Lecture : la couverture est concentrée sur C1 (données/cybersécurité) et sur trois
îlots (réseaux 4e_C4.x, programmation C6/C9). **Les thèmes « conception-réalisation »
(C7, C8) et le diagnostic (C5) sont entièrement vides**, de même que C2/C3 à
l'exception d'un QCM. Le niveau 3e — prioritaire pour la rentrée 2026-2027 —
n'a que 3 codes partiellement couverts sur 38.

---

## 3. Analyse des ressources existantes

### 3.1 La séquence modèle — 4e_C6.2 « Jardin connecté » ✅

Seule ressource conforme au gabarit complet : situation déclenchante (plantes du
collège pendant les vacances), problématique, mission + production attendue,
tableau référentiel (compétence, sous-compétence, connaissances, capacité observable,
socle, CRCN), 3 séances à onglets avec question directrice chacune, exercices
interactifs à correction immédiate, simulation seuil/pompe, schéma SVG original
des deux chaînes, synthèse repliable, grille LSU 4 niveaux, différenciation, EDD,
mode enseignant (`GJEP`).

Améliorations à prévoir pour en faire le gabarit v2 (sans régénérer l'existant) :

1. note chiffrée /20 avec pondération dans des constantes modifiables (actuellement grille LSU seule) ;
2. sauvegarde locale + reprise + exports (PDF/CSV/JSON) au niveau de la séquence (les QCM compagnons en ont déjà) ;
3. séparation élève / professeur / inspection en fichiers distincts (le mode enseignant `GJEP` est un simple mot de passe JavaScript dans une page publique : utilisable comme confort, **pas comme protection** — les corrections sommatives devront être des fichiers séparés non publiés) ;
4. `SOURCES_MEDIAS.md` (même pour des SVG originaux : auteur, licence) ;
5. navigation clavier des onglets de séances (rôle `tab`/`tabpanel`, flèches) à vérifier ;
6. version B (simulation seule) et C (sans matériel) explicites — la simulation existe déjà, il manque l'étiquetage A/B/C.

### 3.2 Ressources substantielles à consolider

| Code | Contenu | Manques principaux |
|---|---|---|
| 5e_C1.1 | Séquence tableur/données + QCM 24 q + 3 fichiers tableur | lien xlsx cassé, gabarits `{{icon}}` non résolus, pas de différenciation, pas de séances explicites |
| 5e_C1.3 (+C1.4) | Séquence SI/gestion de données + QCM | 8 PNG de 1,1–1,9 Mo à compresser, licences non documentées, pas de différenciation |
| 4e_C1.4 | Cybersécurité V16 (PWA, tests) + bonus 2FA + QCM | 2 liens d'images cassés dans le bonus, pas de grille LSU, pas de fichier professeur séparé |
| 3e_C1.5 | Séquence numérique & société + QCM | lien PDF cassé (nom DOS `DELAGR~1.PDF`), licence de l'affiche Delagrave à vérifier |
| 3e_C6.2 | Banque algorigrammes DNB + QCM | pas de situation déclenchante/problématique/synthèse : à « habiller » en séquence |
| 3e_C9.1 | Vittascience variables + TP mBot2 + QCM + 15 images | **17 liens d'images cassés** (`assets/` → `Images/`), pas de mise en situation, vidéo YouTube (RGPD) |

### 3.3 QCM isolés (ne constituent pas des séquences)

`4e_C2.1`, `4e_C4.1` (gabarit `${q.img}` non résolu), `4e_C4.4` (eCall 40 q),
`4e_C4.7` (XXL réseaux 77 q + 9 images aux licences non documentées).
Bonne matière première : chacun appelle une séquence d'accueil.

**4e_C4.4 — rattachement confirmé :** le QCM eCall est correctement rangé,
4e_C4.4 = « Identifier les constituants de la chaîne d'information d'un objet
réel et les associer à leur fonction » (confirmation gouvernance du 21/07/2026 ;
une première version de cet audit avait à tort confondu avec le C4.4 de 5e,
qui porte sur les matériaux).

Dans 4e_C6.2, les QCM « algorigrammes domotique » et « éclairage
automatique » cohabitent avec le Jardin connecté ; leur rattachement
(4e_C6.1 « lire un programme » ? 4e_C6.3 ?) mérite arbitrage.

### 3.4 Outils du dépôt

`make_index.py` : fonctionnel, déterministe (régénération testée : index et README
identiques à l'octet). `qcm_generator.py` + `banks_*.py` + `build_qcms.py` :
chaîne de génération de QCM réutilisable — les futures banques de questions
s'ajouteront dans des fichiers `banks_*.py`.
Anomalie mineure : **`_outils/__pycache__/*.pyc` sont versionnés** (à ajouter au
`.gitignore` et retirer du suivi dans un prochain commit ChatGPT).

---

## 4. Liens cassés (HTML actifs, hors archive)

29 occurrences détectées automatiquement, regroupées :

| Fichier | Problème | Correction proposée |
|---|---|---|
| `3e_C9.1/vittascience_variables.html` | 17 images en `assets/…` alors qu'elles sont dans `Images/` | remplacement `assets/` → `Images/` (1 passe) |
| `5e_C1.1/sequence.html` | `C11_exo_tableur_debut.xlsx` (fichier réel : `exo_tableur_debut.xlsx`) + 6 gabarits `{{sensor_icon}}` etc. | corriger le nom ; remplacer les gabarits par de vrais SVG |
| `4e_C1.4/activite-bonus-cyber-immersive-2fa.html` | `images/tab_key.png` (existe dans `_ressources-communes/Images/`) et `images/indentation_error.png` (**n'existe nulle part**) | chemin relatif vers ressources communes ; recréer l'image manquante |
| `3e_C1.5/sequence-….html` | `DELAGR~1.PDF` (nom court DOS 8.3) | pointer vers `_ressources-communes/delagrave_….pdf` **après** vérification de la licence |
| `4e_C4.1/qcm_automatisation_premium.html` | gabarit `${q.img}` non résolu | fournir les images ou retirer le champ |

*(Faux positifs exclus : gabarits JavaScript volontaires vérifiés un à un.)*

---

## 5. Points de vigilance transversaux

1. **Corrections publiées** : tous les QCM actuels embarquent leurs réponses dans le
   HTML public (GitHub Pages). Acceptable pour l'entraînement, **inutilisable en
   sommatif**. Le futur gabarit devra séparer version élève / correction professeur
   non publiée.
2. **Licences médias** : aucun `SOURCES_MEDIAS.md` n'existe. À documenter en
   priorité : 9 images réseau de 4e_C4.7 (`*_hd.jpg`), 8 PNG de 5e_C1.3, affiche
   Delagrave (3e_C1.5), `porte_logique_*.png` et `creative_commons_icons_hd.jpg`
   des ressources communes, captures Vittascience/mBlock de 3e_C9.1 (captures
   d'interface : usage pédagogique généralement toléré, à consigner quand même).
3. **Dépendances externes** : Google Fonts (jardin connecté), cdnjs (highlight.js),
   iframes Vittascience et YouTube (3e_C9.1). À terme : polices locales et
   activation des iframes sur clic pour le hors-connexion et le RGPD.
4. **Poids** : `doc3_schema_parcours.png` (2,6 Mo, placement incertain signalé par la
   migration), images 5e_C1.3, `capture-01-variables.png` (675 Ko).
5. **`5e_C1.2/sequence.mhtml`** : archive navigateur Edge, se télécharge au lieu de
   s'afficher sur Pages ; l'en-tête interne révèle un fichier d'origine
   `sequence_C1.2_4e_dark.html` — **le contenu est peut-être un support de 4e**.
   → *Décision Pascal : ce support est-il bien du 5e ?*
6. **`.gitignore`** : n'exclut pas `__pycache__/` (des `.pyc` sont versionnés).

---

## 6. Ce que l'audit ne couvre pas encore (honnêteté de périmètre)

- Pas d'exécution navigateur réelle des 8 séquences et 14 QCM (pas de contrôle
  console JavaScript exhaustif ni de test clavier/lecteur d'écran) — prévu au
  contrôle qualité de chaque lot, avec tests automatisés.
- Pas de validation W3C systématique des HTML existants.
- Le contenu du `.mhtml` (5e_C1.2) n'a pas été déplié.
- Les 93 fichiers d'archive n'ont été qu'inventoriés (conformes au principe
  « rien n'est perdu », aucune intervention).
- Les connaissances associées détaillées et le CRCN code par code seront
  vérifiés lot par lot contre le BO n°9 du 29/02/2024 et Éduscol (le programme
  officiel restant prioritaire sur toute transcription en cas d'écart).

---

## 7. Décisions demandées à Pascal (arbitrages réellement pédagogiques)

*(Résolus le 21/07/2026 par la gouvernance : `data_competences.py` fait foi
comme transcription du référentiel ; le QCM eCall reste en 4e_C4.4.)*

1. `5e_C1.2/sequence.mhtml` : contenu 5e ou 4e ?
2. QCM domotique/éclairage de 4e_C6.2 : conserver ici ou rattacher à 4e_C6.1/C6.3 ?
3. Affiche Delagrave : disposes-tu d'un droit de diffusion (offre enseignant) ?
   Sinon : lien externe vers le site de l'éditeur au lieu du PDF embarqué.
4. Priorités de la feuille de route (cf. `FEUILLE_DE_ROUTE_COMPLETION.md` §5) :
   valider le premier lot 3e proposé.
