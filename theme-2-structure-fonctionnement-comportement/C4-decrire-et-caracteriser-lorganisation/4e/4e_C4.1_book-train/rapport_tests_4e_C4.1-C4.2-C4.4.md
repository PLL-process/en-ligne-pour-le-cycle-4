# Rapport de tests — Lot 4e_C4.1 · C4.2 · C4.4 « Un Book Train pour la Schœlcher »

**Exécution réelle** le 08/08/2026, suite Playwright (Chromium headless) : **32/32 verts**.
Seuls des tests réellement exécutés sont déclarés ici (barre qualité du dépôt).

Ce lot **achève** une séquence qui existait seule depuis le 05/08/2026, sans QCM, sans synthèses, sans
fiche ni manifest — ce qui contredisait la règle du lot indivisible. La séquence elle-même n'a pas été
réécrite : elle a été complétée et mise aux règles d'or n°23 à n°34.

## Séquence (18 tests)

| Test | Vérifie | Résultat |
|---|---|---|
| SEQ-01 | chargement sans erreur JS | ✔ |
| SEQ-02 | titre conforme à la charte | ✔ |
| SEQ-03/04/05 | blocs règle n°4 : « 🧠 Prêt·e à t'entraîner ? », UN SEUL bouton QCM, « 🎁 Bonus » | ✔ |
| SEQ-06 | toutes les figures de la page se chargent (naturalWidth > 0) | ✔ |
| SEQ-07 | le lien QCM pointe un fichier réellement présent | ✔ |
| SEQ-08 | le nombre de questions annoncé correspond au QCM livré (30 dont 4 illustrées) | ✔ |
| SEQ-09 | sauvegarde locale : champ restauré après rechargement | ✔ |
| AUD-23 | durées annoncées par activité + badge « 3 séances de 55 min » (154 min pour 165) | ✔ |
| AUD-26 | billet d'entrée présent et annoncé **sans note** | ✔ |
| AUD-26b | le billet refuse les réponses vides **sans sanctionner** (« aucune note à la clé ») | ✔ |
| AUD-26c | 2 sur 3 → orientation vers la capsule de rattrapage | ✔ |
| AUD-26d | 3 sur 3 → l'élève est invité à poursuivre | ✔ |
| AUD-29 | bouton « mode essentiel » présent | ✔ |
| AUD-29b/c | activation : les corrections deviennent effectivement invisibles | ✔ |
| AUD-29d | retour au mode complet | ✔ |
| AUD-29e | choix du mode persistant après rechargement | ✔ |
| AUD-31 | une version étayée pour **chacune** des 3 productions écrites | ✔ |
| AUD-34 | **tout** select de la page porte une étiquette (`label for` ou `aria-label`) | ✔ |

## QCM (11 tests)

| Test | Vérifie | Résultat |
|---|---|---|
| QCM-01 | chargement sans erreur JS | ✔ |
| QCM-02 | 30 questions | ✔ |
| QCM-03 | répartition 10 / 10 / 10 sur C4.1, C4.2, C4.4 | ✔ |
| QCM-04 | bonnes réponses réparties sur A/B/C/D (8/7/8/7, `fix_r.js` graine 4127) | ✔ |
| QCM-05 | 4 questions illustrées | ✔ |
| QCM-06 | chaque distracteur réfuté + explication, exemple, erreur classique, à retenir | ✔ |
| QCM-07 | les images des questions existent sur le disque | ✔ |
| QCM-08/09 | correction détaillée affichée et tableau de bord mis à jour | ✔ |
| QCM-10 | sauvegarde locale restaurée après rechargement | ✔ |
| QCM-11 | navigation « ← Séquence » (règle n°11) | ✔ |

## Vérification des règles d'or n°23 à n°34

`python _outils/verif_regles_audit.py` sur ce lot : **n°23 ✔ · n°26 ✔ · n°29 ✔ · n°31 ✔ · n°33 ✔ · n°34 ✔**,
n°30 sans objet (les tâches de cette séquence ne passent pas par des vérificateurs numérotés).

## Environnement et limites (honnêteté)

- Tests exécutés hors ligne : l'appel aux polices Google échoue proprement (repli sur la police système),
  non bloquant, identique aux autres lots ; cet échec de ressource est journalisé mais non compté comme erreur.
- **Non testé automatiquement** : l'impression A4 (vérifiée visuellement), le rendu dans draw.io et dans
  LibreOffice Impress, et la lecture des SVG par un lecteur d'écran réel. Les deux SVG portent `role="img"`
  avec `title` et `desc` complets, ce qui est vérifiable dans le code mais ne remplace pas un essai avec NVDA
  ou VoiceOver.
- **Non testé non plus** : la règle n°30 (tableau de bord des tâches) n'est pas applicable en l'état à cette
  séquence, dont la progression repose sur des marqueurs de validation différents des `data-check` numérotés
  des autres lots. C'est un écart assumé et signalé, pas une conformité.
- Script de test : suite Playwright du lot (32 vérifications), rejouable.

---

## Relecture du 24/10/2026 — vidéo, chiffres vérifiés, Bonus corrigé

Exécution réelle le 24/10/2026, Chromium (Playwright) en conteneur Linux, page ouverte en `file:`, réseau coupé
(toute requête autre que `file:`, `data:`, `blob:` est refusée et comptée).

**Le banc annoncé le 08/08/2026 n'existe pas.** Le rapport ci-dessus citait une « suite Playwright du lot (32
vérifications), rejouable » : aucun script n'a jamais été commité. Le banc
`tests_4e_C4.1-C4.2-C4.4_book-train.mjs` est donc **nouveau** ; il rejoue aussi une part de ce qui existait
(vérificateur des listes, sauvegarde, mode essentiel, plan de mission).

### Banc du lot — `node tests_4e_C4.1-C4.2-C4.4_book-train.mjs` : **28 / 28**

| Tests | Vérifie |
|---|---|
| 1-2 | chargement sans erreur JS ; aucune requête hors de la page (n°305) |
| 3-5 | ouverture n°304 sans affirmation du passé ; le lien de rattrapage ouvre l'onglet Départ et la capsule depuis la séance 2 ; le plan de mission mène toujours à la séance 2 |
| 6-7 | mode essentiel : le billet d'entrée reste visible, les corrections partent |
| 8-13 | vidéo : lien en nouvel onglet, annonce « connexion Internet » et repli ; deux groupes radio conformes (légende, étiquettes, un nom, valeur = texte) ; vérificateur : 0 réponse, 1/2, 2/2 |
| 14-15 | Bonus : six défis, huit champs étiquetés et sauvegardés, version étayée, corrigé, avant le bilan |
| 16-17 | rechargement : boutons radio, champs du Bonus et case d'ouverture reviennent ; aucune erreur |
| 18 | l'activité 1.2 (listes déroulantes) se valide comme avant |
| 19-20 bis | figures 1 et 5 : aucun texte recouvert, coupé par le cadre ni caché sous une forme ; la figure 5 dit 480 V ~ → 24 V ⎓ |
| 21-22 | plus de « change de nature » ni de « 4 niveaux » ; source des chiffres citée |
| 23 | 390 px : aucun défilement horizontal (Départ, séances 1 et 3) |
| 24-27 | QCM : 30 questions (10/10/10), indices de bonne réponse identiques à `origin/main`, plus de « domaine » ni de rail qui DISTRIBUE, chargement sans erreur |

**Mesuré sur la page de `main` avant le lot** (mêmes mesures, script de captures) : billet d'entrée invisible en
mode essentiel à 1280 et 390 px ; séance 3 à +143 px de défilement horizontal à 390 px ; figure 1 : trois
étiquettes cachées, trois hors du cadre.

### Contrôles du dépôt (racine, sur la branche)

| Contrôle | Sortie | Périmètre lu |
|---|---|---|
| `verif_regles_audit.py <lot>` | 3 ✘, tous antérieurs : n°300 (44 listes), n°302 (« Si vous êtes trois ou quatre », bloc commun) — n°298 et n°304 passent au vert ; n°23 : 154 min (+10) pour 165 | 1 séquence |
| `verif_regles_audit.py` (dépôt) | 240 ✘ (242 sur `main`) | 60 séquences |
| `controle_squelette.mjs <lot>` | 0 | 1 séquence à onglets |
| `controle_verrous.mjs`, `controle_hors_ligne.mjs`, `controle_impression.mjs` | 0 | toutes les pages |
| `controle_contraste_liens.mjs <lot>` | 0 (1 refus au premier passage : lien de la synthèse professeur en bleu par défaut, corrigé) | 5 pages |
| `audit_cloture_sequence.mjs <lot>` | 0 — Bonus avec champs et corrigé, avant le bilan | 1 séquence |
| `audit_lisibilite_qcm.mjs` | 0 — mesure (cet audit ne refuse rien) | tous les QCM |
| `verif_qcm_coherence.mjs qcm_book-train.html` | 0 — 30 q, positions 8/7/8/7, réfutations alignées | 1 QCM |
| `controle_hierarchie.py` | 0 (1 refus au premier passage : trois énumérations en ligne dans le corrigé du Bonus, passées en listes) | 145 pages |
| `controle_regle4`, `navigation_seances`, `gestes_outil`, `formulations`, `regles_visibles`, `blocs_dessines`, `liens`, `atteignabilite`, `fichiers_telechargeables`, `boutons_vivants`, `debordement`, `marqueurs`, `banque_qcm`, `effectifs_qcm`, `entete_qcm`, `echantillonnage`, `longueurs`, `medias`, `cadres`, `rapports_tests`, `couverture` | 0 | dépôt |
| `verifier_chaines_energie.py` | 54 / 54 | figures générées |
| `regenerer_chaines_energie.py` | rejoué : aucun écart sur la page ni le QCM | — |
| `generer_lexique.py <lot>` | 30 notions ; sur `main`, régénéré à l'identique ; sur la branche, trois définitions changent (celles du QCM retouché) | 1 lot |
| `poser_ressource.py` | 1 bloc posé (`res-4e-C4-1-book-train`), 5 « aucun changement » | registre |

### Non exécuté, ou non vérifiable ici

- **La vidéo elle-même** : la page YouTube refuse le conteneur. Existence et titre relevés indirectement (page Poets &
  Writers qui l'intègre, résultat de recherche) ; auteur, durée, licence, publicité : à regarder.
  `verificateur_ressources.mjs` doit être lancé depuis une machine avec Internet.
- Lecteur d'écran réel, clavier seul rejoué de bout en bout, impression papier, Safari/iPad : non faits.
