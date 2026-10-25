---
name: qcm-html-accessible
description: Créer ou compléter un QCM HTML autonome pour le dépôt cycle 4 (entraînement public ou sommatif privé). À utiliser pour tout nouveau QCM — moteur du gabarit maison (`const QUESTIONS`), générateur de lot `_generation/q.py` + `build_qcm.py` quand le lot en a un, contrôles `_outils/controle_*`. Ne jamais relancer `_outils/build_qcms.py`.
---

# QCM HTML accessible

Mis à jour le 23/10/2026 (inventaire des skills) : aligné sur le journal jusqu'à la règle d'or n°311.

## Deux usages, deux régimes

- **Entraînement (public, GitHub Pages)** : correction immédiate et exhaustive, y compris pour les
  questions réussies (règle d'or n°96, 21/08/2026) ; nouvelle tentative ; « à retenir ».
- **Sommatif** : version élève SANS correction. Le corrigé ne va jamais dans le dépôt public
  (`_outils/METHODE.md`, barre qualité). Une page statique ne protège rien : les réponses se lisent
  dans la source, et un code JavaScript n'est qu'un loquet de confort (journal, 30/07/2026).

## Spécification par défaut

- **30 questions fixes, sans tirage aléatoire (décision de Pascal du 23/10/2026).** Le mode
  « 10 questions » du gabarit prend un échantillon régulier et stable, sans aléatoire.
- 4 propositions (multi-réponses seulement si annoncé), mélange connaissance/application/analyse,
  questions sur schéma ou données (champ `img` + `alt`), zéro double négation.
- Pour qu'un code soit évalué, lui donner au moins 5 questions. En dessous, il est seulement
  mobilisé : on le cite en appui, on ne le reporte pas seul au LSU (n°202, 28/08/2026).
- Champs d'une question : `c, n, q, (img), o, r, expl, ex, err, d, ret`. `d` porte la réfutation de
  chaque distracteur (`""` pour la bonne réponse). `COMP_LABELS` relie chaque `c` à son code.

## Distracteurs et bonnes réponses

- Un distracteur est plausible et reçoit sa réfutation propre (n°125, 21/08/2026).
- Le meilleur distracteur est vrai, mais hors sujet (n°148, 27/08/2026).
- Une réfutation écarte la proposition DANS LE CAS ÉTUDIÉ ; elle n'énonce pas une loi (n°139, 27/08/2026).
- La bonne réponse n'est pas la plus longue et ne se reconnaît pas sans lire la question
  (n°144, 27/08/2026 ; n°198, 28/08/2026).
- Les bonnes réponses se répartissent sur toutes les positions offertes, à une unité près
  (n°137, 26/08/2026).

## En-tête standard (règle d'or n°2, 22/07/2026)

Modèle : `3e_C4.3/qcm_3e_C4.3-C4.6_station_alerte_cyclonique.html`. Dans cet ordre :

1. Titre H1 avec émoji discret + sous-titre (notions couvertes en clair) ;
2. Badges : niveau, chaque code couvert, « N questions · corrections détaillées » (+ questions illustrées) ;
3. Lien de retour vers la séquence associée (obligatoire, en haut) ;
4. Identité élève : Nom, Prénom, Classe, Date (sauvegardée localement) ;
5. « Ma progression » : barre + 7 compteurs (Répondu, Correctes, Incorrectes, Restantes, À revoir 🔖,
   Score %, Note /20) + minuteur (Démarrer/Pause/Reprendre + « travailler sans minuteur ») ;
6. « Mode de travail » : Parcours complet (N), 10 questions, Révision ciblée, Uniquement mes erreurs,
   Marquées « à revoir ».

Suivent : carte Navigation (filtres + grille), écran question, écran résultat (bilan par compétence,
bouton « Imprimer / PDF »).

- Titre, sous-titre, badges, pied et menu de révision se déduisent des questions et de `COMP_LABELS`,
  jamais d'un gabarit copié ; les options du menu sont exactement les codes des questions
  (n°292, 09/09/2026 ; n°51, 08/08/2026).
- Palette de la charte : fond `#050f24`, cartes `#0d2347`, accents `#61dafb`/`#c68ef2`/`#ffd66b`.
  Jamais d'appellation « XXL ».
- Clavier complet et focus visible, retours en `aria-live`, jamais la couleur seule (n°119,
  21/08/2026), impression A4 propre (n°102, 21/08/2026), responsive, HTML5 valide, UTF-8,
  `lang="fr"`, aucun tracker ni envoi distant, zéro erreur console.
- Sauvegarde locale + reprise (clé `qcm_<codes>_<slug>`), remise à zéro.
- Ouverture ciblée : le QCM lit `#depart=court` et `#codes=…` dans l'adresse (n°45, 08/08/2026).
- Exports JSON/CSV, champ « Groupe », constantes `POIDS_QCM` : absents du gabarit et des 71 QCM en
  service (constat du 23/10/2026). Ne pas les annoncer comme fournis.

## Produire le QCM

**Ne pas relancer `_outils/build_qcms.py`** (ni `qcm_generator.py` + `banks_a.py`/`banks_b.py`).
Constat du 23/10/2026 :

- il produit l'ancien format `checkMCQ`, en découpant un modèle (`4e_C4.7/qcm_xxl_40_…`) qui a
  été scindé en trois et réécrit depuis (commit `834480c0`) ;
- il écraserait six QCM en service retouchés à la main depuis le 22/07 (4 à 14 commits chacun ;
  trois sont passés depuis au moteur `const QUESTIONS`) ;
- il recréerait dans les dossiers actifs deux QCM archivés (`5e_C1.1/qcm_donnees_tableur.html`,
  `5e_C1.2/qcm_principes_techniques.html`) et déplacerait l'eCall en service vers l'archive,
  par-dessus l'ébauche qui s'y trouve ;
- puis il planterait sur `/tmp/lanwlan_questions.pkl`, absent — après avoir écrit.

Raison : un fichier engendré modifié à la main cesse d'être engendré ; la chaîne ne redevient vraie
qu'au prochain qui régénère, en effaçant le travail fait à la main (règle d'or n°257, 30/08/2026).

Pratique actuelle :

- Sur 71 QCM en service, 63 n'ont pas de générateur, et deux ont un générateur figé : pour ces 65,
  le HTML est la source (constat du 23/10/2026 ; journal, 21/10/2026). Partir d'un QCM récent au
  gabarit maison ; ne remplacer que `const QUESTIONS`, `COMP_LABELS` et les libellés du lot ; ne
  jamais réécrire le moteur.
- Huit lots ont un générateur : `_generation/q.py` (banque, bonnes réponses toutes en position 0) +
  `_generation/build_qcm.py` (assemble à partir du gabarit). Six tournent : 5e_C1.1, 5e_C1.2,
  5e_C2.1, 4e_C2.1, 3e_C2.1, `atelier-planification` (C7). Deux sont FIGÉS depuis le 24/09/2026 et
  refusent de tourner : 3e_C1.1 et 4e_C1.1 — leur page HTML est la source. Exemple :
  `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.1/_generation/`.
- Usage : `python3 build_qcm.py <gabarit.html> <sortie.html>`, puis `node _outils/fix_r.js <sortie.html> <GRAINE>`.
  Prendre la constante `GRAINE` du script (il l'imprime en « Étape suivante »), pas la graine de sa
  docstring : dans 5e_C1.2, seule `GRAINE = 218` redonne les positions publiées (la docstring dit 317).
- Avant de régénérer un QCM de lot : générer dans le scratchpad et comparer à la page publiée. Écart
  non nul → reporter d'abord dans `q.py` ce qui a été retouché à la main (journal, 27/09/2026), ou
  modifier `q.py` ET la page à l'identique (cas de 5e_C1.1, journal, 21/10/2026). Seul
  `atelier-planification` a un contrôle automatique : `verif_chaine_qcm.py`.

Répartition des bonnes réponses (n°137) :

- Banque écrite en `r:0` : `node _outils/fix_r.js <fichier.html> <graine>` (permutation déterministe).
  Attention (n°149, 27/08/2026) : `fix_r.js` réécrit chaque question depuis une liste fixe de champs.
  Un champ inconnu (`nuance`) disparaît ; un `err` absent devient `err:undefined`. Vérifier après coup.
- QCM existant : `node _outils/repartir_qcm.mjs <fichier.html>` — rotation vers un motif écrit en
  clair, `d` tourné avec `o`, assertion que la bonne réponse suit ; édition chirurgicale.

## Contrôler (depuis la racine du dépôt)

- `python3 _outils/controle_entete_qcm.py --muet` — titre, badges, pied, menu (n°292). Sortie 1 si écart.
- `python3 _outils/controle_banque_qcm.py --muet` — la ligne « Banque : … » dit ce que le tableau contient.
- `python3 _outils/controle_effectifs_qcm.py --muet` — chaque nombre annoncé (page, manifeste,
  lexique) vaut la taille réelle de la banque (n°261, 31/08/2026).
- `python3 _outils/controle_echantillonnage.py` — codes évaluables (≥ 5 questions) ou seulement
  mobilisés (n°202). N'interdit rien.
- `python3 _outils/controle_longueurs.py` — bonnes réponses détachées par leur longueur (n°144,
  n°198) ; banque signalée au-delà de 15 %.
- `node _outils/mesures_qcm.mjs` — position des bonnes réponses (n°137).
- `python3 _outils/controle_sigles.py` — sigles en capitales dans les questions et les options, FAST et non « fast »
  (n°313) ; seul le mot cité entre guillemets (« fast », le mot anglais) garde ses minuscules.
- `node _outils/verif_qcm_coherence.mjs <fichiers…>` — après rotation : réfutation vide pour la
  bonne réponse, non vide pour les autres.

## Tester et consigner

1. Dans le navigateur : chaque bonne/mauvaise réponse, non-répondu, note /20, reprise après
   fermeture, remise à zéro, les cinq modes, `#codes=` / `#depart=court`, champs vides.
2. Score exact vérifié sur 3 scénarios scriptés (tout juste, tout faux, mixte connu).
3. Ne déclarer que les tests réellement exécutés ; un contrôle qui n'a rien lu est en panne, pas
   vert (n°299, 19/09/2026). Consigner dans le rapport de tests du lot.

## Critères de réussite

- Le QCM fonctionne en `file://` (hors connexion) et sur GitHub Pages.
- Mêmes questions, même ordre à chaque lancement.
- Les contrôles ci-dessus passent, ou chaque signalement est expliqué dans le rapport de tests.
- Aucun corrigé d'évaluation sommative dans le dépôt.
