# Rapport de tests — lot 5e_C1.2 « Sainte-Luce »

**Exécuté le 24 octobre 2026**, après l'ajout de la **séance 4** (exercices) · Chromium via Playwright
· `python3 tests_5e_C1.2_sainte_luce.py` et `node tests_regle_311_5e_C1.2.mjs`
**Résultat : 50 contrôles sur 50 au banc du lot (33 séquence + 17 QCM), 33 sur 33 au banc de la règle
n°311, aucune erreur JavaScript.**

Ne figurent ici que des tests **réellement exécutés**. Première exécution du lot : 9 août 2026,
36 / 36 (19 séquence + 17 QCM), sur la page à trois séances.

## Périmètre déclaré (règle n°47)

**Vérifié** — les six verrous (billet + cinq activités), fermés sur une page vide et ouverts sur une
production complète ; celui de l'activité 4 ne s'ouvre qu'après l'exercice du diagramme FAST
**réellement rempli et vérifié dans la page** ; le **refus argumenté** du frein à patins en séance 3
et du frein à tambour pour Léa en séance 4 ; la progression sur cinq activités, la sauvegarde et sa
restauration ; l'exclusion des champs de l'exercice inséré hors de la sauvegarde de la séquence ; la
reprise d'un travail enregistré **avant** l'ajout de la séance 4 ; quatre onglets, le passage de la
séance 3 à la séance 4, la clôture dans la séance 4 seule ; la cible du bouton d'entraînement ; les
deux blocs de la règle n°4, corrigé du Bonus compris ; la manipulation obligatoire ; pour le QCM
(inchangé), le titre **affiché** et son sous-titre, le nombre de questions et d'illustrées, la
répartition des bonnes réponses, la réfutation de chaque distracteur, la formulation du référentiel,
l'ouverture ciblée, le chargement effectif des images et le lien de retour.

**Non vérifié** — l'exactitude pédagogique des corrigés, le rendu à l'impression au-delà de ce que
mesure `controle_impression`, l'ergonomie en classe, **la faisabilité de la manipulation sur le
vélo**, qui se vérifie devant un vélo, et la tenue réelle de la séance 4 en 50 minutes.

## Séquence — 33 contrôles

| Contrôle | Résultat |
|---|---|
| Quatre onglets de séance, s1 à s4 | ✅ |
| La clôture (Bonus, Bilan, QCM) est dans la séance 4, et nulle part ailleurs | ✅ |
| Le bouton de fin de séance 3 ouvre la séance 4 | ✅ |
| Les six verrous refusent une page vide | ✅ 6/6 |
| Le bouton QCM à zéro validation ouvre le parcours court | ✅ |
| L'exercice FAST inséré, rempli et vérifié dans la page, est enregistré réussi (`rep_fast_5e_e3`) | ✅ |
| Les six verrous s'ouvrent sur une production complète | ✅ 6/6 |
| **Le tambour est refusé pour Léa, et la raison chiffrée (10,4 m freins chauds) est donnée** | ✅ |
| **Le choix du frein à patins est refusé en séance 3, et la raison chiffrée est donnée** | ✅ |
| La progression atteint 5 / 5, et les quatre onglets portent leur ✔ | ✅ 2/2 |
| Le bouton QCM en fin ouvre le parcours complet | ✅ |
| La sauvegarde de la séquence contient la séance 4, et aucun champ de l'exercice inséré | ✅ |
| Après rechargement : zones de rédaction (séance 1 et séance 4), exercice inséré (sa propre mémoire), progression | ✅ 4/4 |
| **Un travail enregistré à trois séances se rouvre à 3 / 5**, champs rendus, séance 4 à faire | ✅ |
| Blocs « Prêt·e à t'entraîner ? », « Bonus » et corrigé du Bonus présents (règle n°4) | ✅ 3/3 |
| La manipulation est annoncée comme obligatoire (règle n°58) | ✅ |
| Zéro erreur JavaScript | ✅ |

> Rejoué sur la page d'avant (trois séances, copie de `main` dans un dossier de travail) : le banc
> s'arrête au troisième contrôle — aucun bouton ne mène à une séance 4. Il mesure donc bien ce qui
> a changé.

Le vérificateur de l'activité 5 a en plus été éprouvé à la main sur **neuf réponses d'élève**
(script hors banc) : quatre conseils justes acceptés (phrases de la version étayée, réponse courte,
« je ne conseille pas le tambour, je conseille le disque », décimales à point) ; cinq refusés avec
le bon message (tambour, patins, sans perte, sans ce qui distingue Léa du collège, sans chiffres).

## QCM — 17 contrôles (QCM inchangé)

| Contrôle | Résultat |
|---|---|
| Titre **affiché** et sous-titre propres au lot (règle n°51) | ✅ |
| Aucune trace du lot d'origine du gabarit | ✅ |
| 30 questions, 8 illustrées | ✅ |
| Bonnes réponses réparties A/B/C/D — 8/7/7/8, graine 218 | ✅ |
| Chaque distracteur porte une réfutation de plus de 20 caractères | ✅ 90/90 |
| La réfutation de la bonne réponse est vide | ✅ 30/30 |
| Chaque question a explication, exemple, erreur classique et à-retenir | ✅ 30/30 |
| La formulation du référentiel est celle du texte officiel (règle n°42) | ✅ |
| `#depart=court` ouvre 10 questions, bandeau visible | ✅ |
| Les 8 images se chargent réellement | ✅ |
| Le lien de retour vers la séquence est présent et exact | ✅ |
| Clé de sauvegarde propre au lot | ✅ |
| Zéro erreur JavaScript | ✅ |

## Règle n°311 — 33 contrôles (`tests_regle_311_5e_C1.2.mjs`)

Séance 1 complète, séance 2 et **dernière séance (s4)** repliées, à 1280 et 390 px (titre, barre
d'outils, badges masqués, aucun défilement horizontal), clavier, hypothèse conservée dans le volet,
retour à la séance 1, rechargement, sauvegarde, liens directs `#a5_1__1` (ouvre s4) et `#be_1__1`,
sans JavaScript, impression. **33 / 33.**

## À 390 px (script de vérification, hors banc)

Chaque séance s'ouvre sans défilement horizontal ; les boutons de fin de séance 1, 2 et 3 ouvrent la
suivante ; une saisie de la séance 4 revient après rechargement ; l'ouverture y est repliée ; zéro
erreur JS. **10 / 10.**

## Contrôles du dépôt (dernière ligne de chacun, 24/10/2026)

| Contrôle | Sortie | Dernière ligne |
|---|---|---|
| `controle_squelette.mjs` (dossier) | 0 | ✅ ouverture au premier écran, clôture à la dernière séance (s4), dans l'ordre — 0 défaut, 0 « à rédiger » |
| `controle_navigation_seances.py` (dépôt) | 0 | ✅ chaque séance (hors la dernière de sa page) mène explicitement à la suivante |
| `controle_hierarchie.py` | 0 | ✅ aucune énumération en ligne, aucun mur sans repère… |
| `controle_regles_visibles.py` | 0 | ✅ aucune page lue par un élève ne laisse voir la fabrique |
| `controle_liens.py` | 0 | ✅ aucun lien mort, aucune ancre introuvable |
| `controle_debordement.py` | 0 | ✅ aucun tableau de 3 colonnes ou plus sans filet mobile |
| `controle_longueurs.py` | 0 | aucune banque signalée |
| `controle_medias.py` | 0 | ✅ chaque image a une provenance écrite |
| `controle_verrous.mjs`, `controle_impression.mjs`, `controle_contraste_liens.mjs`, `controle_hors_ligne.mjs` | 0 | ✅ |
| `mesurer_temps_seances.py` | 0 | 4 × 55 min = 220 ; 190 annoncés (le script compte aussi les 5 min de la manipulation 🅰) ; marge +30 |
| `incrustations.py --verifier --seq 5e/5e_C1.2/` | 0 | à jour |

## Vérificateur de règles

`python3 _outils/verif_regles_audit.py` sur le dossier : **15 ✔, 1 ✘**. n°23 (190 min pour 220),
n°31 (8 versions étayées pour 16 zones, dont les 2 de l'exercice inséré), n°33 (aucun pavé), n°300
(aucune liste déroulante), n°301 (le bilan clôt, le Bonus le précède)… Le **✘ n°298** (la carte du
référentiel et la légende des étiquettes sur la page élève) est **antérieur** à la séance 4 et hors
de ce lot.

## Incidents

1. Un pavé de 113 mots (l'introduction du bloc inséré) a fait lever la n°33 : raccourci, le bloc
   reposé par `incrustations.py`.
2. Le tableau du vendeur montait sur huit lignes d'en-tête à 390 px : en-têtes raccourcis, unités
   insécables, la condition « freins chauds » dite dans la phrase d'avant.
