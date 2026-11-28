# Rapport de tests — Lot 3e_C4.1 + C4.2 « L'énergie de la station »

**Date** : 2026-07-23 · **Agent** : Fable (Thème 2) · **Outil** : Playwright
(Chromium headless), viewport mobile 390×844 · **Verdict global : 23 / 23 ✅**


> **Correction du 31/08/2026 — le verrou expérientiel s'ouvrait en partie tout seul.**
> `_outils/controle_verrous.mjs`, écrit ce jour-là, ouvre chaque séquence du dépôt dans un
> navigateur neuf et lit `window.__exp` juste après le chargement. Cette page en portait déjà
> la clé `suffisant` **avant tout geste** : la fonction d'affichage du simulateur était appelée à
> l'initialisation et enregistrait l'état affiché comme une observation. Le verrou de
> l'activité concernée s'ouvrait donc en partie sans que l'élève ait rien manœuvré, ce que la
> règle d'or n°226 interdit. La fonction ne trace plus que sur un geste ; vérifié : `__exp`
> est vide à l'ouverture, et se remplit dès le premier mouvement de curseur.
Conformément au prompt maître : tous les tests listés ont été **réellement
exécutés** le jour de la livraison (script `tests_lot06.js`). **Ce script n'est pas dans le dépôt et n'y a jamais été commité** (relevé du 31/08/2026).

> **La suite est écrite, et elle est ici.** `tests_3e_C4.1-C4.2.mjs`, **23 contrôles**, rejoue
> les vingt-trois lignes ci-dessous.
>
> Elle s'attarde sur ce que ce lot a d'unique : son verrou exige **deux essais de sens
> contraire**. La suite vérifie le refus (« fais VRAIMENT les deux essais »), puis règle le
> simulateur aux **bornes réelles de ses curseurs** — la plus petite batterie avec la plus
> grosse consommation, qui rend « ❌ Station muette après 12 h » ; puis l'inverse, qui rend
> « ✅ La station tient les 72 h ». Les deux clés `insuffisant` et `suffisant` apparaissent
> alors, et l'activité se valide.
>
> ```
> node tests_3e_C4.1-C4.2.mjs      →  23 / 23
> ```
>
> Les **35 champs** de réponse sont extraits des `CHECKS` de la page selon quatre conventions,
> dont celle des « intrus » : un `new Set` de deux champs et les deux valeurs qu'il doit
> contenir. Seule la justification en prose est rédigée par le test — et les contraintes
> qu'elle doit croiser sont lues dans le code de la page.

 Un défaut réel a été détecté par la
suite (lien inter-dossiers vers la séquence station) et corrigé avant livraison ;
la suite complète a été rejouée après correction.

## Séquence (13 tests)

| Test | Résultat |
|---|---|
| Chargement sans erreur JS | ✅ |
| Rappel d'hypothèse affiché | ✅ |
| Act. 1 élaboration (5 blocs + 4 natures + 2 intrus) : 11/11 | ✅ |
| **Verrou expérientiel** : refus de valider sans l'essai insuffisant | ✅ |
| Simulateur : 20 Ah → ❌ 40 h · 40 Ah → ✅ 72 h tenus | ✅ |
| Act. 2 validée (432 Wh, 36 Ah, choix 40 Ah + 2 essais réels) | ✅ |
| Act. 3 contraintes du site : 5/5 | ✅ |
| Act. 4 matériaux/procédés (8 choix + justification à 2 contraintes) | ✅ |
| Act. 5 réinvestissement borne du stade | ✅ |
| Progression 5/5 + coches des 2 séances | ✅ |
| Reprise après rechargement (réponses, validations, essais __exp) | ✅ |
| Zéro lien local cassé (défaut détecté puis corrigé, suite rejouée) | ✅ |
| Zéro erreur JS après l'ensemble des interactions | ✅ |

## QCM (5 tests)

| Test | Résultat |
|---|---|
| Chargement sans erreur JS · 30 questions | ✅ |
| Bonnes réponses réparties A/B/C/D = 8/8/7/7 | ✅ |
| 3 questions illustrées, SVG présents sur le disque | ✅ |
| Parcours 30/30 → 20,0/20 · bilan par 2 codes | ✅ |
| Zéro erreur JS après le scénario complet | ✅ |

## Synthèses (2) et index (3)

Synthèses élève/professeur : chargement sans erreur, schémas présents ✅.
Index : badge NEW sur 3e_C4.1 + compétence C4, ancre auto-ouverte/ciblée,
pointeur 3e_C4.2 badgé ✅.

## Limites connues

- Google Fonts inaccessible dans le bac à sable (polices de repli, sans incidence).
- Version 🅰 (panneau + batterie + multimètre réels) non testable en sandbox :
  annoncée comme option, très basse tension uniquement.

## Complément (v2, demande Pascal)

Activité bonus « Loi d'Ohm » ajoutée (I = P÷U, U = R×I, choix du fusible —
hors barre de progression) et correctif d'affichage du bouton QCM du bilan
(débordement multi-lignes, corrigé aussi sur les séquences 5e au même gabarit).
Tests rejoués : bonus validé 3/3, progression inchangée (5 activités), zéro
erreur JS, display:block confirmé sur le bouton.

## 15/11/2026 — Les chaînes sous les yeux (étiquettes posées dans le schéma)

Les questions de la chaîne se jouent dans le schéma lui-même (outil commun `_outils/chaine_a_completer/`) : l'élève
pose les étiquettes dans les blocs, sous les blocs et sur les flèches ; ce qu'il a trouvé reste écrit à l'étape suivante.

- Bancs du lot : verts (le banc de la séquence trouve un groupe posé dans le schéma à son schéma).
- `node _outils/mode_mission/banc_generique.mjs` : la page jouée écran par écran, aucun refus ; les schémas joués en étiquettes.
- `python3 _outils/controle_chaine_a_completer.py` : ✅.

Non exécuté : un vrai téléphone, une vraie tablette, Firefox, Safari.

## 15/11/2026 — le secteur entre par la gauche

Remarque de Pascal sur le schéma de l'alimentation : le secteur arrivait par la droite. Le bloc du secteur passe en haut
à gauche de la carte de basculement, sa flèche part du bord gauche ; au téléphone, le secteur à gauche, la batterie à
droite. `node tests_3e_C4.1-C4.2.mjs` : **23 / 23** ; `node tests_regle_311_3e_C4.1.mjs` : **34 / 34** ; banc générique
du mode mission : aucun refus.


## 18/11/2026 — L'activité 1 élaborée par l'élève, la séquence en trois séances

Décisions de Pascal sur l'audit externe du 17/11 :
- **L'activité 1 fait élaborer la chaîne, fonctions comprises.** Les blocs sont vides : a) l'élève place les composants
  d'après les branchements (les légendes nomment la place du bloc, et non plus sa fonction) ; b) il nomme la fonction de chaque
  bloc (CONVERTIR, ALIMENTER, STOCKER, DISTRIBUER, et TRANSMETTRE de trop) ; c) les natures ; d) les intrus. Le gabarit à
  imprimer est muet lui aussi (`Images/chaine_energie_a_elaborer_muet.svg`, engendré par
  `_outils/regenerer_chaines_energie.py gabarit_muet`). Le critère passe à 16 / 16 ; la correction donne, bloc par bloc,
  le composant et la fonction, et dessine la chaîne complète.
- **Trois séances** : S1 l'activité 1 (35 min) ; S2 les activités 2 et 3, le Bonus loi d'Ohm ; S3 les activités 4 et 5,
  puis Bonus, bilan et QCM.

Rejoué : `node tests_3e_C4.1-C4.2.mjs` **25 / 25** ; `node tests_regle_311_3e_C4.1.mjs` **34 / 34** ; banc générique du
mode mission : aucun refus (3 séances) ; `banc_mission.mjs` 50 / 50 ; `controle_squelette.mjs`,
`controle_chaine_a_completer.py`, `controle_schema_sous_les_yeux.py`, `controle_navigation_seances.py`,
`controle_correction_complete.py`, `controle_mode_essentiel.py`, `controle_hors_ligne.mjs`, `controle_axe.mjs` : verts ;
`mesurer_charge.mjs` : aucune séance au-delà de 1 200 mots ; `banc_papier.py` : chaque séance imprimée, sans champ d'écran.

## Reprise du 28/11/2026 — quatre questions sur document de plus, et un billet de sortie (n°345, n°330)

- `node tests_3e_C4.1-C4.2.mjs` : **30 / 30** (cinq tests neufs : le billet existe à la séance 3, juste avant le Bonus ;
  deux zones gardées, deux versions étayées, deux critères, des contre-exemples, aucun bouton ; la réponse survit au
  rechargement ; au moins six questions sur document ; `documents_qcm.py --verifier` à jour de la séquence).
  `node tests_regle_311_3e_C4.1.mjs` : **34 / 34**.
- `controle_question_seule.py --strict --chantiers` : tout à 0 (D1 et P1 étaient à 1). La q30 citait le code du lot,
  la q11 renvoyait « au simulateur » : réécrites. `balayer_questions_qcm.mjs --apres` : 30 questions, 7 illustrées,
  0 écart. Contrôles des QCM (aides comprises), des schémas (0 ✘), de l'aération, des règles d'or, du squelette, du
  mode mission, des liens et des statuts : verts.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.
