# Rapport de tests — LOT 04 « Programmer l'alerte » (3e_C6.1 + C6.3)

**Suite** : `tests_3e_C6.1-C6.3.mjs`, livrée dans ce dossier · **Outil** : Playwright
(Chromium headless), viewport téléphone 390 × 844 · **Rejouée le 31/08/2026** ·
**Verdict : 35 / 35 ✅**

```
cd theme-2-.../C6-.../3e/3e_C6.1 && node tests_3e_C6.1-C6.3.mjs
```

> **Ce que ce rapport disait avant le 31/08/2026.** Il portait 17 coches et ne citait
> **aucun** script : une dette honnête, pas une promesse fausse (règle d'or n°259). Son
> titre annonçait « 22/22 réussis » là où ses tableaux comptaient 17 lignes — un nombre
> écrit en prose, que `_outils/controle_effectifs_qcm.py` ne lit pas et ne prétend pas
> lire (règle n°264). Les 17 lignes sont reprises, et dix-huit contrôles s'y ajoutent.

## Ce que cette suite éprouve en propre

Ce lot ne vérifie pas des menus déroulants : il **lit le programme que l'élève a écrit**.

- **L'activité 3** exige que `SEUIL_ORANGE` ait vraiment été recalibré à 60 **dans le code** —
  répondre juste aux deux questions ne suffit pas, et la page le dit : « je ne trouve pas
  SEUIL_ORANGE = 60 dans CodeLab ».
- **L'activité 4** passe **sept** expressions régulières sur le programme : l'initialisation,
  les deux passages à `True`, le bloc final, son indentation, et l'**absence** de gyrophare
  dans la branche rouge. Elle nomme précisément ce qui manque.

Les deux sont éprouvées dans les deux sens : refus tant que le code n'est pas modifié, message
qui nomme les ajouts manquants, puis validation.

## Ce que la suite ne recopie pas — y compris le programme

Le programme v2 n'est pas écrit dans le test : il est **lu dans la correction que la page
publie elle-même** (`#act4 details.correction pre`), puis collé dans l'éditeur. Si la
correction affichée à l'élève et le vérificateur divergeaient un jour, cette suite le dirait —
ce qu'un programme recopié dans le test ne pourrait pas faire (règle d'or n°268).

Le nombre de contrôles de code n'est pas compté non plus : il est **demandé à la fonction**
(`CHECKS[4]().total`). Le compter à la main dans le source donnait 11 au lieu de 7.

Les réponses sont extraites des `CHECKS` selon cinq conventions : **19 égalités**, **4 préfixes**
(`.indexOf("…") === 0`), **3 nombres**, un objet `att`, et **1 rédaction** jugée par mots-clés —
dont la suite ne prétend montrer que l'ouverture aux conditions déclarées, et dont elle vérifie
surtout le refus (contrôle 9).

## CodeLab Techno et séquence — 26 contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 1 | Chargement, titre « Programmer l'alerte », codes 3e_C6.1 / 3e_C6.3 | ✅ |
| 2 | Programme d'origine chargé, **24 lignes** annoncées et comptées | ✅ |
| 3 | Coloration syntaxique active : 4 familles de jetons colorées | ✅ |
| 4 | Le bouton « surligner les lignes 6-7 » surligne exactement 2 lignes (code et marge) | ✅ |
| 4 bis | « Ne plus surligner » rend le programme à sa lecture normale | ✅ |
| 5 | A+ agrandit la police (14 → 15 px) et le style CSS suit | ✅ |
| 6 | À l'ouverture, l'éditeur déclare le programme identique à l'origine | ✅ |
| 7 | 19 égalités, 4 préfixes, 3 nombres, 1 rédaction extraits des `CHECKS` | ✅ |
| 8 | Activité 1 validée **8 / 8** (classements + deux numéros de ligne relevés) | ✅ |
| 9 | **Activité 2 REFUSÉE** : 3 traces justes, justification trop courte | ✅ |
| 10 | Activité 2 validée **3 / 3** (118 > 118 est faux : l'opérateur est strict) | ✅ |
| 11 | **Activité 3 REFUSÉE** : 2 réponses justes, mais le code n'est pas modifié | ✅ |
| 12 | Une seule ligne changée : le comparateur en annonce **exactement une** | ✅ |
| 13 | Activité 3 validée **3 / 3** une fois la ligne 2 réellement recalibrée | ✅ |
| 14 | **Activité 4 REFUSÉE** sur le v1, et le message **nomme** les ajouts manquants | ✅ |
| 15 | Le programme v2 est lu dans la correction publiée par la page (30 lignes) | ✅ |
| 16 | Activité 4 validée **7 / 7** : les sept contrôles de code passent sur le v2 | ✅ |
| 17 | Activité 5 validée **7 / 7** (jeux d'essai aux frontières + bug diagnostiqué) | ✅ |
| 18 | Activité 6 validée **6 / 6** (lire un programme qu'on n'a pas écrit) | ✅ |
| 19 | Toutes les activités validées (6 / 6) | ✅ |
| 19 bis | Les 3 onglets de séance portent leur coche | ✅ |
| 20 | Rechargement : **le programme de l'élève** est restauré, pas la version d'origine | ✅ |
| 20 bis | Rechargement : réponses, validations et taille de police restaurées | ✅ |
| 21 | Les 6 liens internes existent | ✅ |
| 22 | Les 3 SVG référencés existent sur le disque | ✅ |
| 23 | Hors ligne : aucune ressource distante, aucune modale, aucune erreur JS | ✅ |

## QCM — 9 contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 24 | Chargement, titre, taille annoncée exacte (badge et compteur) | ✅ |
| 25 | **30 questions, 2 compétences à 15 chacune** | ✅ |
| 26 | Bonnes réponses A/B/C/D = **7 / 8 / 7 / 8** et `d[r]` vide partout | ✅ |
| 27 | **6** questions illustrées, fichiers présents sur le disque | ✅ |
| 28 | Gabarit maison complet : 4 options, 4 réfutations, `expl`, `ex`, `err`, `ret` | ✅ |
| 29 | Parcours **30 / 30 joué question par question** → **20,0 / 20**, bilan 2 lignes à 15 / 15 | ✅ |
| 30 | La clé `localStorage` du QCM est écrite | ✅ |
| 31 | Le lien de retour vers la séquence pointe sur un fichier réel | ✅ |
| 32 | Aucune erreur JS sur le QCM | ✅ |

## Contrôles restant manuels

Version 🅰 sur maquette réelle · import d'un fichier `.py` depuis l'appareil (la suite ne
simule pas un choix de fichier système) · mode plein écran sur iOS, où l'API `fullscreen` est
limitée — le bouton reste sans effet sur iPhone, comportement dégradé accepté · relecture
humaine.

## Limites connues

- Tests exécutés uniquement en Chromium/Playwright — aucune compatibilité non testée n'est
  revendiquée.
- Google Fonts inaccessible en sandbox : polices de repli, sans incidence — la suite ne compte
  pas ces requêtes comme des ressources distantes de la page (règle n°40).

## 18/11/2026 — Consignes à la ligne (n°342) et programme sous les yeux

Demande de Pascal pour la séance du matin. Chaque consigne d'activité donne une action par ligne (①, ②… ou a), b)). Le
programme de la station est sous la consigne des activités 1 à 5 ; en mission, il est sur chaque écran de question (à
gauche sur grand écran, au-dessus sur téléphone). Le programme de la bouée (activité 6) est sur ses cinq écrans.

| Contrôle | Sortie | Résultat |
|---|---|---|
| `tests_3e_C6.1-C6.3.mjs` | 0 | 35 / 35 |
| `tests_regle_311_3e_C6.1.mjs` | 0 | 34 / 34 |
| `mode_mission/banc_generique` (la page) | 0 | aucun refus ; l'éditeur présent sur chaque écran de question des activités 1 à 5 |
| `audit_aeration.py --strict` | 0 | aérée |
| `controle_squelette.mjs` | 0 | ouverture et clôture en place |
| `controle_hors_ligne.mjs` | 0 | aucune ressource réseau |
| `controle_regles_visibles.py` | 0 | aucune trace de la fabrique |
| `controle_code_colore.mjs` | 0 | 8 listings en couleurs |
| `controle_schema_sous_les_yeux.py` | 0 | rien à signaler |
| `onglets_clavier.py --etat --strict` | 0 | 0 à poser |
| `impression_papier/banc_papier.py --filtre 3e_C6.1` | 0 | la fiche papier s'imprime ; le programme déplacé n'y apparaît pas en double |

Revue d'écran : captures à 1 280 px (mission, côte à côte) et en page complète, regardées ; rien à reprendre.
