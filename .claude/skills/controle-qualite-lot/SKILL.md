---
name: controle-qualite-lot
description: Contrôle qualité complet (pédagogique, technique, évaluation, droits) d'un lot AVANT sa livraison — contrôles de _outils/, bancs du lot, balayage navigateur, et liste de ce qui n'a pas été exécuté. À utiliser systématiquement en fin de lot, jamais sauté ; la livraison suit par le skill livraison-depot-cycle4.
---

# Contrôle qualité de fin de lot

Mis à jour le 23/10/2026 (inventaire des skills) : aligné sur le journal jusqu'à la règle d'or n°311.

## Mission (unique)

Vérifier un lot terminé, puis écrire son rapport de tests et son manifeste. Si un contrôle bloquant échoue, le lot n'est pas livré :
on le corrige d'abord. Une fois le lot vert, on le livre avec le skill `livraison-depot-cycle4`.

## Contrôles bloquants

**Pédagogie** :
- conformité au programme 2024 (BO n°9 du 29/02/2024, prioritaire sur tout cahier) ;
- compétence réellement travaillée par l'activité, pas de points « décoration » ;
- progressivité 5e → 4e → 3e et cohérence problématique ↔ activités ↔ évaluation ;
- durée réaliste, matériel confirmé ou versions 🅱/🅲 présentes ;
- exercices originaux, corrections de qualité, niveau de langue collège ;
- sigles en capitales, FAST et non « fast » (n°313, 25/10/2026) : `python3 _outils/controle_sigles.py` ;
- squelette respecté : n°306 (22/09/2026) et n°311 (22/10/2026), voir le skill `sequence-pedagogique-engageante` ;
- chaque unité savante nommée en toutes lettres dans son activité, son tableau, sa question, son schéma : n°312
  (25/10/2026), `python3 _outils/controle_unites.py` ; un schéma reçoit sa ligne « Unités : … » par
  `python3 _outils/legende_unites.py`.

**Technique** :
- HTML valide, aucun lien local cassé, aucune erreur console ;
- calcul des notes exact, sauvegarde et reprise, exports, impression ;
- mobile, clavier seul, contrastes, `alt` des images ;
- page lisible sans Internet ;
- poids des médias : moins de 300 Ko par image, sauf justification.

**Évaluation** : bonnes et mauvaises réponses, question non répondue, pondération et /20, remise à zéro, cas limites, champs vides.

**Droits & sécurité** :
- `SOURCES_MEDIAS.md` complet et attributions affichées ;
- aucune donnée envoyée, aucun secret ;
- aucune correction sommative publiée ;
- aucune dépendance suspecte, aucune suppression non documentée.

## Lire un code de sortie (règles d'or n°47, 08/08/2026, et n°299, 19/09/2026)

- `0` : le contrôle a tourné et n'a rien à refuser. `1` : il a tourné et refuse. `2` : il n'a **rien pu vérifier**, il est en panne.
- Un vert ne compte que s'il annonce ce qu'il a lu (« 340 page(s) lues »). Un « 0 écart » sur 0 page est une panne, pas une réussite.
- Une trace Python ou `ERR_MODULE_NOT_FOUND` est une panne, même si la sortie vaut 1. On la note « non exécuté », jamais « refus ».
- Douze outils ne suivent pas encore la n°299 : sur une racine vide, ils sortent à 0 (mesuré le 23/10/2026, liste ci-dessous).
  Pour eux, lire le compte des entrées imprimé avant de conclure.
- Devant un rouge, vérifier d'abord que l'outil sait lire la page (n°50, 08/08/2026 ; n°270, 31/08/2026).

## Les contrôles de `_outils/`, par bloc

Lancer depuis la racine du dépôt. Python : `python3 _outils/<outil>.py`. Node : `node _outils/<outil>.mjs`.
« ⚠ 0 » signale un outil qui sort à 0 sur une racine vide.

**Pédagogie et forme de la page**

| Outil | Vérifie |
|---|---|
| `controle_squelette.mjs [--json] [chemin]` | n°306 et n°311 dans Chromium, onglet par onglet : ouverture, clôture Bonus → Bilan → QCM à la dernière séance, rien hors des panneaux, volet « Rappel » (D1 à D6). Les « à rédiger » (Bonus sans corrigé…) ne sortent qu'en `--json` |
| `verif_regles_audit.py [chemin]` | les règles mécanisables : n°23, 26, 29, 30, 31, 33, 34, 42, 51, 53, 54, 67, 298, 300, 301, 302, 304. **Sortie 0 même avec des ✘ : compter les ✘** |
| `controle_regle4.py` ⚠ 0 | « Prêt·e à t'entraîner » et Bonus présents, un seul bouton QCM, en fin de page. L'ordre est jugé par `controle_squelette` (son message de réussite dit encore l'ancien ordre) |
| `controle_navigation_seances.py` | chaque séance mène à la suivante (n°101, 21/08/2026) |
| `controle_hierarchie.py [chemin]` | n°307 (27/09/2026) : la hiérarchie se voit (listes en ligne, pavés) |
| `controle_gestes_outil.py` | l'encart « les N gestes » nomme l'outil de sa page et se place à sa porte |
| `controle_formulations.py` | « Ce que dit le programme » cite le programme mot pour mot |
| `controle_regles_visibles.py` | n°309 (21/10/2026) : aucune trace de la fabrique dans ce que lit l'élève |
| `controle_blocs_dessines.py` | n°308 (18/10/2026) : aucun bloc dessiné ; captures `bloc_vitta_*.png` déclarées, 300 Ko au plus |
| `verifier_chaines_energie.py` | n°310 (21/10/2026) : les figures générées des chaînes d'énergie, dans Chromium (Playwright Python) |
| `controle_couverture.py` ⚠ 0 | le lot nomme le code qu'il prétend couvrir. Diagnostic, sortie toujours 0 (`controle_statut.py` est son module, sans point d'entrée) |
| `audit_cloture_sequence.mjs`, `audit_personne_eleve.mjs` | inventaires de la clôture (n°301) et de la personne (n°302). Mesure, pas verdict (0 / 2) ; `--csv` écrit dans `_outils/` |

**Technique**

| Outil | Vérifie |
|---|---|
| `controle_liens.py [--tout]` | liens et images locaux cités dans le source, ancres |
| `controle_atteignabilite.py` ⚠ 0 | chaque page est atteignable depuis `index.html` |
| `controle_fichiers_telechargeables.py` | chaque fichier nommé dans une page se télécharge d'un clic |
| `controle_boutons_vivants.py` ⚠ 0 | chaque bouton appelle une fonction qui existe dans sa page |
| `controle_verrous.mjs` | n°226 (31/08/2026) : aucun verrou expérientiel ouvert au chargement |
| `controle_hors_ligne.mjs [--source]` | n°305 (21/09/2026) : aucune ressource chargée depuis Internet |
| `controle_impression.mjs` | rendu `media: print` : aucun texte sombre sur fond sombre |
| `controle_contraste_liens.mjs [chemin]` | n°303 (21/09/2026) : chaque lien se lit (contraste) |
| `controle_debordement.py` | n°135 (second passage du 27/09/2026) : un tableau large défile au lieu de casser la page sur mobile |
| `controle_marqueurs.py` | pointes de flèche SVG mesurées en pixels |
| `controle_loupe.py` | n°92 : l'agrandisseur de chaque page est le v2, une seule fois (25/10/2026) |
| `banc_loupe.py [racine] [--captures <dossier>]` | n°92 au navigateur : un schéma SVG agrandi garde ses couleurs (écart mesuré), la légende ne recouvre pas l'image, à 1280, 390, 1920 px et 1280 px zoomé 150 % |
| `controle_lecteur_pas_a_pas.py` | décision 4b (25/10/2026) : chaque animation pas à pas utilise le lecteur commun (`_outils/lecteur_pas_a_pas/`), posé une fois, à jour |
| `lecteur_pas_a_pas/banc_lecteur.py [racine]` | chaque animation pas à pas, au navigateur : étapes, 390 px, mouvement réduit, voix sur le disque, impression, lien direct |

**Évaluation (QCM)**

| Outil | Vérifie |
|---|---|
| `controle_banque_qcm.py` ⚠ 0 | la ligne « Banque : … » dit ce que le QCM contient |
| `controle_effectifs_qcm.py` ⚠ 0 | le QCM dit vrai sur sa taille (manifeste, lexique) |
| `controle_entete_qcm.py` ⚠ 0 | titre, menu « Compétence à réviser » et pied de page sont ceux du lot |
| `controle_echantillonnage.py [chemin]` ⚠ 0 | n°202 (28/08/2026) : au moins 5 questions par code évalué. Ne prend pas `--muet` : il le lit comme un chemin |
| `controle_longueurs.py [chemin]` ⚠ 0 | la bonne réponse ne se devine pas à sa longueur. Même piège avec `--muet` |
| `verif_qcm_coherence.mjs <qcm.html…>` ⚠ 0 | réfutations alignées sur les propositions. Sans argument, il ne lit rien et sort à 0 |
| `audit_lisibilite_qcm.mjs` | n°300 (20/09/2026) : inventaire des propositions qui masquent la question (0 / 2) |

**Droits & sécurité**

| Outil | Vérifie |
|---|---|
| `controle_medias.py` | provenance de chaque image (`SOURCES_MEDIAS.md`), images inemployées. **Ne juge pas le poids** |
| `controle_cadres.py` | aucun `<iframe>` vers fr.vittascience.com (le site refuse d'être encadré) |
| `controle_rapports_tests.py` ⚠ 0 | un rapport de tests qui cite un script le livre |

`audit_conformite.py` (règles RC-1 à RC-6 du lot 0) lit le répertoire courant et sort à 0 sur une racine vide. Ce n'est pas un contrôle de fin de lot.

**Dans le navigateur, ce que la lecture du HTML ne voit pas** : skill `balayage-navigateur` (claude.ai). Il repère les images non décodées,
les 404 (y compris les adresses fabriquées par script), la casse des noms de fichiers et les erreurs JS et console. Le lancer après
`controle_liens.py` et `controle_atteignabilite.py`. Il ne voit pas ce qui n'apparaît qu'après un clic : ça relève des bancs du lot.

**Prérequis.** Les `.mjs` en navigateur et `verifier_chaines_energie.py` demandent Playwright et Chromium. Sans le paquet `playwright`
pour Node, les `.mjs` tombent en `ERR_MODULE_NOT_FOUND` (constaté le 23/10/2026 en session cloud) : c'est une panne, à noter « non exécuté ».

## Hors outils : bancs du lot et vérifications à la main

- Bancs du lot (`tests_<lot>.mjs` ou `.py`), lancés comme on les lance vraiment, en sous-processus (n°299, second corollaire).
  Ils couvrent la sauvegarde et la reprise, les exports, les verrous, le sélecteur de parcours (n°122, 21/08/2026), le clavier
  et 390 px. Ils testent la page telle que le navigateur la rend (n°49, 08/08/2026).
- Scénarios de notes : trois jeux de réponses connus par évaluation, avec le score attendu calculé à la main dans le rapport et rejoué
  par le banc (par exemple 32/32 → 20,0/20, 16+16 → 10,0/20, 8+8+16 non répondues → 5,0/20).
- Poids des images, à la main : `find <dossier du lot> -type f \( -name '*.png' -o -name '*.jpg' -o -name '*.jpeg' \) -size +300k`.
- Aucun outil du dépôt ne valide le HTML, ne vérifie le parcours au clavier seul ni ne cherche les secrets : les faire à la main, ou les lister comme restants.

## Sortie obligatoire

- `rapport_tests_<lot>.md` dans le dossier du lot :
  - chaque contrôle exécuté, avec son code de sortie et son périmètre (pages lues) ;
  - les scénarios de notes ;
  - ce que la suite ne couvre pas ;
  - les contrôles **non exécutés**, chacun avec sa raison.
  - Il ne cite que des scripts livrés (`controle_rapports_tests.py`).
- Le manifeste du lot (`manifest_lot_*.json`) et l'entrée au journal : voir `_outils/METHODE.md`, « Le lot est un ensemble INDIVISIBLE ».
- Puis la livraison, par le skill `livraison-depot-cycle4` : régénération, branche, PR sous garde-périmètre. Depuis la règle d'or n°5
  amendée (30/07/2026), Fable pousse sa branche et ouvre sa PR ; la fusion reste la validation de Pascal ; le colis
  (bundle → Downloads) est le plan B.

## Critères de réussite

- Aucun contrôle bloquant en échec non corrigé.
- Aucun contrôle en panne (sortie 2, trace, module manquant) compté comme vert.
- Tout contrôle non exécuté est listé explicitement comme « restant à faire », jamais passé sous silence (n°47).
