# Rapport de tests — Thème 2 · LOT 01 « Station d'alerte cyclonique » (3e_C4.3 → C4.6)

Date : 2026-07-22 · Agent : Fable (Thème 2) · Environnement : Chromium headless (Playwright), viewport téléphone 390×844 + vérifications scriptées Python/Node.


> **Suite livrée le 31/08/2026 — `tests_3e_C4.3-C4.6.mjs`, 23 contrôles, `23 / 23`.**
> Ce lot était le plus fourni de la file d'attente publiée par
> `_outils/controle_rapports_tests.py` : vingt-six coches vertes qu'aucun script ne relançait
> (règles d'or n°259 et n°266). La suite conduit le simulateur de CAN au curseur, remplit les
> sept activités avec les réponses **extraites des `CHECKS` de la page** (45 champs), recharge,
> et joue le QCM **trois fois** pour rejouer les trois scénarios de notes que ce rapport
> calculait à la main.
>
> ```
> node tests_3e_C4.3-C4.6.mjs      →  23 / 23
> ```
>
> **Deux limites déclarées plutôt que masquées.** Les activités 4 et 6 emploient deux
> conventions d'écriture que le pilote ne parse pas — la concaténation de trois champs binaires
> (`a4_b1..b3`) et le texte normalisé de `a6_1`. Elles se valident donc à `8/9` et `3/4`, ce que
> la page elle-même accepte (`ok>=8`, `ok>=3`), et le contrôle nº7 bis exige exactement ces deux
> scores : si un troisième point venait à manquer, il tomberait.
>
> **Une erreur du test, pas de la page.** La première version cherchait le lien d'évitement par
> son libellé (« évitement », « aller au ») ; celui de cette page dit « Aller directement aux
> activités » et n'était pas trouvé. Il se reconnaît à sa classe `skip-link` — convention du
> dépôt —, et le contrôle vérifie en plus qu'il vise une ancre réelle et se montre au focus
> clavier.
## 1. Tests automatisés exécutés — 40/40 réussis (suite principale) + 10/10 (scénarios de notes)

### Séquence (`sequence_3e_C4.3-C4.6_station_alerte_cyclonique.html`)

| Test | Résultat |
|---|---|
| Chargement `file://` sans erreur JS (hors police externe facultative) | ✅ |
| Table de données : 48 enregistrements rendus | ✅ |
| Simulateur CAN : N(943 hPa) = 512 ± 1 | ✅ |
| Activité 1 : validation des 8 réponses justes + justification → feedback « ok » | ✅ |
| Progression 1/7 mise à jour puis **restaurée après rechargement** (localStorage) | ✅ |
| Onglets de séances fonctionnels | ✅ |
| Zéro lien local cassé (SVG, CSV/ODS/XLSX, QCM) — vérification `fs` + parcours `href/src/data` de tous les HTML | ✅ |
| Lien d'évitement (skip-link) accessible au clavier | ✅ |

### QCM (`qcm_3e_C4.3-C4.6_station_alerte_cyclonique.html`)

| Test | Résultat |
|---|---|
| Chargement sans erreur JS · grille de 32 questions | ✅ |
| Réponse correcte comptée · correction complète affichée (bonne réponse en toutes lettres, explication, exemple, erreur fréquente, distracteurs expliqués, « À retenir », encouragement) | ✅ |
| Minuteur : démarrage auto à la 1re validation, pause fige le temps, reprise, option « sans minuteur » | ✅ |
| Bouton « Réessayer » : question réinitialisée et compteurs exacts | ✅ |
| Réponse fausse comptée · marquage 🔖 « à revoir » | ✅ |
| « Prochaine non répondue » | ✅ |
| **Sauvegarde/reprise après fermeture** : réponses, erreurs, marquages restaurés | ✅ |
| Mode « uniquement mes erreurs » (1 question) · mode « 10 questions » | ✅ |
| Écran final : note /20, %, temps, bilan par compétence (4 lignes), notions maîtrisées/à revoir | ✅ |
| Question non répondue correctement comptée | ✅ |

### Scénarios de notes (calculés à la main, puis vérifiés en machine)

| Scénario | Attendu | Obtenu |
|---|---|---|
| S1 : 32/32 correctes | 32 pts · 20,0/20 · 100 % | ✅ identique |
| S2 : 16 correctes + 16 incorrectes | 16 pts · 10,0/20 · 50 % | ✅ identique |
| S3 : 8 correctes + 8 incorrectes + 16 non répondues | 8 pts · 5,0/20 · 25 % · 16 NR | ✅ identique |

### Tableau de bord (`index.html` régénéré + badge NEW)

| Test | Résultat |
|---|---|
| Badge NEW sur le code `3e_C4.3`, sur la compétence C4, sur le thème 2 | ✅ |
| Badge NEW sur les liens séquence/QCM nouveaux | ✅ |
| Aucun badge sur le thème 1 (non concerné) | ✅ |
| Ancre directe `index.html#3e_C4.3` : ouvre la compétence, défile jusqu'au code, met la ligne en évidence | ✅ |
| Zéro erreur JS | ✅ |

## 2. Contrôles statiques

- **Syntaxe JavaScript** : `node --check` sur les scripts extraits de la séquence, du QCM et de l'index → OK.
- **Liens locaux** : parcours automatique de tous les `href/src/data` des HTML du lot → aucun lien cassé.
- **Poids des médias** : 5 SVG originaux entre 5 et 7 Ko, données 3-7 Ko → très en dessous du seuil de 300 Ko.
- **Matrice de couverture** : les 32 questions du QCM sont rattachées à une notion enseignée ; aucune question hors séquence ; aucune notion essentielle sans question (vérification scriptée de l'ensemble 1-32).
- **Aucun secret, aucune donnée personnelle envoyée** : sauvegardes en localStorage uniquement, aucune requête sortante indispensable (la police Google est décorative avec repli système ; tout fonctionne hors connexion après chargement).

## 3. Accessibilité et confort

- Navigation clavier (skip-link testé, focus visibles), `aria-label`/`role`/`aria-live` posés, `<title>/<desc>` dans chaque SVG.
- `prefers-reduced-motion` respecté (badge NEW, défilements, transitions).
- Contrastes de la palette commune du projet ; l'information ne repose jamais sur la seule couleur (étiquettes textuelles).
- Impression A4 : styles dédiés séquence, synthèse élève (1 page) et QCM.
- Minuteur désactivable (travail sans contrainte de temps).

## 4. Contrôles restant manuels (non exécutés — à faire par un humain)

- Test sur appareils réels (iOS/Android, tablette) — seul le viewport mobile a été émulé ;
- test du montage **version A** (Arduino UNO/R4 + Grove luminosité + LCD) au labo : compatibilité bibliothèque LCD ↔ UNO R4 Minima **À CONFIRMER — prévoir l'alternative VittaScience** ;
- relecture orthotypographique humaine ;
- vérification du rendu GitHub Pages après publication (ancre + badge sur l'URL publique).

## 5. Échecs

Aucun test exécuté en échec au moment de la remise.

## 15/11/2026 — Les chaînes sous les yeux (étiquettes posées dans le schéma)

Les questions de la chaîne se jouent dans le schéma lui-même (outil commun `_outils/chaine_a_completer/`) : l'élève
pose les étiquettes dans les blocs, sous les blocs et sur les flèches ; ce qu'il a trouvé reste écrit à l'étape suivante.

- Bancs du lot : verts (le banc de la séquence trouve un groupe posé dans le schéma à son schéma).
- `node _outils/mode_mission/banc_generique.mjs` : la page jouée écran par écran, aucun refus ; les schémas joués en étiquettes.
- `python3 _outils/controle_chaine_a_completer.py` : ✅.

Non exécuté : un vrai téléphone, une vraie tablette, Firefox, Safari.

## 16/11/2026 — La station pièce par pièce (figure Anatomy, activité 1)

Une figure à manipuler, `station_en_pieces.html`, posée dans l'activité 1 (séance 1) sous le schéma annoté, dans un
dépliant fermé (`#a1-figure-station`, cadre ; sur un téléphone, un lien vers la page de la figure). Un bouton ouvre le
coffret : la porte s'écarte et ses 7 pièces sortent en colonne. 18 pièces numérotées, nommées sous la figure par leur
place, jamais par leur fonction (l'activité la fait trouver), ni leur matériau ni leurs valeurs (`3e_C4.1`).
Fiche A4 : `station_fiche_A4.pdf`, une page.

**Contrôles et bancs, sur la branche** :

- Bancs du lot, lancés depuis leur dossier : `tests_3e_C4.3-C4.6.mjs` 23 / 23 (sortie 0) ; `tests_regle_311_3e_C4.3.mjs` 34 / 34 (sortie 0).
- Mode mission : `poser.py --verifier` ✅ ; `enrichir.py … mission_3e_C4.3.json --verifier` ✅ ; `banc_generique.mjs` : la page
  jouée écran par écran, aucun refus (61 / 61 pourquoi). Sur les écrans de l'activité 1, la figure suit le schéma annoté
  comme ressource (« 📎 »).
- `controle_schemas.mjs` sortie 0 : la figure est déclarée illustration (`data-illustration`), hors score.
- `controle_axe.mjs` sortie 0 (6 pages, la page de la figure comprise) ; `controle_hors_ligne.mjs` sortie 0 ;
  `controle_impression.mjs` sortie 0 (la page de la figure imprime en clair).
- `controle_mouvement.py` : M1 0, M2 0 sur le dossier. Les deux boucles du kit (flux, pulsation), inutiles ici, sont
  retirées de la page. « 1 image SVG en boucle » existait avant ce lot (le dossier `Images/` n'est pas touché).
- `mesurer_charge.mjs` : aucune séance au-delà de 1 200 mots visibles (le dépliant est fermé ; le mode essentiel le cache,
  classe `approfondissement`). `audit_aeration.py --strict` ✅ ; `verif_regles_audit.py` 0 ✘.
- Contrôles Python de `_outils/` : tous à 0 sauf `controle_flux_animes.py`, qui refuse
  `5e/5e_C4.1/Images/chaine_ventilateur_corrige.svg` : le même refus existe sur `main`, hors de ce lot.
- `impression_papier/banc_papier.py --filtre 3e_C4.3` : sortie 1, « séance 1 — 6 champs d'écran imprimés (boutons) ».
  Le même refus existe sur `main`, avant ce lot ; la figure n'est pas imprimée (classe `pp-ecran`).

**Revue d'écran en trois tours** (captures dans `_outils/captures_station_anatomy_2026-11-16/`) :

1. Tour 1 : le bas de la planche était un toit vide (un quart de la hauteur) ; le numéro de la sirène tombait sous le
   pavillon, près du câble ; le fusible et le baromètre, sortis du coffret, étaient trop petits pour se reconnaître.
2. Tour 2 : toit réduit (la figure grandit), numéro 7 à côté du pavillon, fusible et baromètre grossis. Mesuré coffret
   ouvert : l'écart minimal entre deux pastilles est de 42 px à 1 280 px et de 23 px à 390 px, pour un rayon de 11 et 8 px :
   elles ne se touchent pas.
3. Tour 3 : ce qui reste — le dépliant ouvert fait environ 1 700 px de haut à 1 280 px (la liste de 18 pièces) ; les
   pièces 12 à 17 restent de petites silhouettes, leur nom est dans la liste.

Non exécuté : un vrai téléphone, une vraie tablette, Firefox, Safari ; la validation HTML ; le parcours au clavier à la
main (le bouton et la figure s'ouvrent à Espace et à Entrée, vérifié par script seulement).

## Reprise du 28/11/2026 — six questions sur document, et un billet de sortie (n°345, n°330)

- `node tests_3e_C4.3-C4.6.mjs` : **29 / 29** (six tests neufs : le billet existe à la séance 5, juste avant le Bonus ;
  deux zones gardées, deux versions étayées, deux critères, des contre-exemples, aucun bouton ; la réponse survit au
  rechargement ; au QCM, au moins six questions sur document, chaque document décrit, `documents_qcm.py --verifier` à
  jour). `node tests_regle_311_3e_C4.3.mjs` : **34 / 34**.
- Le moteur du QCM n'affichait pas d'image (aucune question n'en avait) : il reçoit la figure du gabarit maison
  (`#qFigure`, comme `3e_C4.1`). `balayer_questions_qcm.mjs --apres` : 32 questions, 6 illustrées, 0 écart (la q19
  débordait de 84 px sur sa correction, une ligne de CSV sans espace : des espaces après les « ; »).
- `controle_question_seule.py --strict --chantiers` : tout à 0 (D1 et P1 étaient à 1). Contrôles des QCM (aides
  comprises), des schémas (0 ✘), de l'aération de la séquence et du QCM, des règles d'or, du squelette, du mode
  mission, des liens et des statuts : verts. (`station_en_pieces.html` garde un signalement d'aération L1 ancien,
  hors de ce lot de travail.)

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.
