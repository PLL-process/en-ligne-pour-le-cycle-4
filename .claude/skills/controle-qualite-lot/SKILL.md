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
- chaque compétence du CRCN en toutes lettres, à l'écran et au survol (n°314, 26/10/2026) :
  `python3 _outils/controle_competences.py` ; chaque étiquette de code du programme dit son intitulé au survol
  (17/11/2026) : `python3 _outils/intituler_codes.py --etat --strict` ; l'outil `python3 _outils/nommer_competences.py <page>` écrit les intitulés et
  les deux premiers étages de la bulle (intitulé et niveau, le cadre) ; le « Ici : » s'écrit à la main ;
- en mode essentiel, aucune carte réduite à son titre (n°29, contrôle du 26/10/2026) : `python3 _outils/controle_mode_essentiel.py` ;
- tout schéma est premium (n°315, 28/10/2026) : aucune entité n'en touche une autre, aucun texte ne sort de son cadre,
  aucune flèche ne traverse un cadre ou un texte, un repère vit à part sans flèche, les tailles écrites sont celles qu'on voit —
  `node _outils/controle_schemas.mjs <dossier du lot> --planche <dossier>` ; puis chaque schéma regardé sur la planche :
  simple et vulgarisé (lisible par un élève de 6e), pédagogique, beau ; refait avec le meilleur outil disponible ;
- l'élève répond le schéma sous les yeux (n°331, clé de voûte, 15/11/2026) : toute question qui porte sur un schéma
  l'affiche **dans le même bloc** (`figure.schema-sous-les-yeux`, épinglée sur téléphone, à gauche des questions sur grand
  écran), jamais « ci-dessus » ; répété à chaque activité qui le lit ; **muet** sur ce que la question fait produire
  (étiquettes, types, formats, énergies à trouver), la version complète dans la correction — sauf une compétence de
  LECTURE, qui se vérifie sur le document complet. `python3 _outils/controle_schema_sous_les_yeux.py` : 0 ✘ ; chaque ⚠
  (schéma nommé sans figure, schéma replié) se juge à l'œil : corrigé dans la page, ou, s'il est juste (question de
  connaissance, production de l'élève, chemin de menu…), nommé dans `JUGES` avec sa raison (`--juges` les relit). Une
  chaîne à compléter (`div.cac[data-cac]`) compte comme le schéma du bloc ;
- toute synthèse élève se lit par un élève de 6e et tient sur deux pages A4 (n°316, révisée le 29/10/2026) : carte
  « Ce que je dois retenir », puis chaque partie de l'exemple vers la règle (titre-question, exemple de la séquence en
  deux lignes, encadré « À retenir », le piège en une ligne), un seul lexique à la fin — voir le skill
  `synthese-vulgarisee` ; `python3 _outils/mesurer_impression.py <page>` : deux pages ; ancres `#partie-N` intactes ;
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
| `audit_aeration.py [--strict] [--phrases] [page…]` | 08/11/2026 (skill `texte-clair-et-aere`) : chaque légende et chaque correction est aérée — une partie par ligne, pas de bloc de plus de 35 mots sous une image ni de 45 mots dans une correction, pas d'idées cousues de « ; » ou de « → ». Mesure sur le site (sortie 0) ; `--strict` sur les pages du lot (sortie 1 s'il reste un écart). Une légende « collée » se règle par `aerer_legendes.py --ecrire`, une correction d'un seul tenant par `aerer_corrections.py --ecrire`. `--phrases` (15/11/2026, mesure hors `--strict`) : paragraphes de plus de 4 phrases, consignes de plus de 20 mots, explications de plus de 25 |
| `controle_consignes_a_la_ligne.py [--strict] [page…] [--json <f>]` | n°342 (18/11/2026) : chaque consigne donne une action par ligne — N1 deux étapes numérotées sur une ligne, N2 deux actions enchaînées (« ; », « puis », deux phrases à l'impératif), N3 deux actions jointes par « et » (à juger, hors `--strict`). Lit les éléments dont une classe nomme la consigne et les paragraphes qui commencent par « Consigne ». Mesure sur le site (sortie 0) ; `--strict` sur les pages du lot (sortie 1 sur N1 ou N2) ; banc `tests_controle_consignes_a_la_ligne.py` |
| `replier_captures.py`, `replier_bonus.py` `<page> [--ecrire]` | 08/11/2026 (skill `revision-sequence`) : les captures d'un geste, le Bonus se déplient à la demande ; rien n'est retiré. Pas des contrôles : des outils de la passe |
| `replier_fiches_activite.py [page…] [--ecrire] [--etat]` | 15/11/2026 (décision de Pascal) : la fiche de chaque activité (objectif, compétence, production attendue, ressources) se replie sous un résumé qui nomme ses rubriques ; rejouable, rien n'est retiré. Sans `--ecrire`, il dit ce qui reste à replier |
| `mesurer_charge.mjs [page…] [--longs 30] [--json <f>]` | 08/11/2026 (skill `revision-sequence`) : au navigateur, à 390 px, les mots que l'élève voit à l'ouverture de chaque séance, mode essentiel compris ; `--longs` cite les blocs d'un seul tenant. Repère : 1 200 mots (10 min de lecture seule). Mesure, sortie 0 ; sortie 2 si aucune page lue |
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
| `trois_lignes.py --etat [--strict]` | n°337 (17/11/2026) : chaque séquence s'ouvre sur « 🎯 Avant de commencer : trois choses à lire » (apprendre, savoir faire, réussir ; 1 à 3 lignes et 40 mots au plus par rubrique), avant la barre d'onglets. Mesure (⚠) pendant la généralisation ; `--poser` la pose |
| `corriger_billet.py [--ecrire]` | n°336 (17/11/2026) : le billet d'entrée a sa correction complète (la bonne réponse, le pourquoi de chaque leurre, tirés des `data-pourquoi` et confrontés au vérificateur). Sortie 1 tant qu'un billet en manque ; « refus » = le pourquoi des leurres reste à écrire |
| `controle_correction_illustree.py [--strict] [--juges] [chemin]` ⚠ 0 | n°336 (16/11/2026) : la correction se voit ; quand la réponse se dessine (schéma, chaîne, algorigramme, carte mentale…), elle montre le dessin. D1 ✘ (un schéma muet jamais montré complet) ; D2/D3 ⚠ (le dessin attendu absent de la correction, ou pas de correction) ; `JUGES` pour les blocs justes ; banc `tests_controle_correction_illustree.py`. En mode mission, la correction s'ouvre une fois l'activité vérifiée : `banc_generique.mjs` le refuse autrement |
| `controle_correction_complete.py [--strict] [chemin]` ⚠ 0 | n°332 (15/11/2026) : une activité qui fait produire avec un outil a une correction (K1), qui montre la production entière (K2), et donne son fichier (K3). ⚠ par défaut (sortie 0) ; `--strict` fait sortir à 1 sur K1 et K2, pour la vague ; banc `tests_controle_correction_complete.py` |
| `controle_boutons_vivants.py` ⚠ 0 | chaque bouton appelle une fonction qui existe dans sa page |
| `controle_verrous.mjs` | n°226 (31/08/2026) : aucun verrou expérientiel ouvert au chargement |
| `banc_effacement.mjs [--muet] [page ou dossier…]` | n°322, point 4 (20/11/2026), au navigateur : « effacer, c'est tout effacer ». Sur chaque page à bouton d'effacement, écrit un témoin dans chaque champ (exercices incrustés compris) et dans la mémoire du mode mission, efface, recharge ; refuse la page si quelque chose reste (clé du navigateur, champ, case, menu). Trois à quatre minutes sur tout le site ; sortie 2 si rien n'a été joué ; banc `tests_banc_effacement.mjs` |
| `controle_hors_ligne.mjs [--source]` | n°305 (21/09/2026) : aucune ressource chargée depuis Internet |
| `controle_impression.mjs` | rendu `media: print` : aucun texte sombre sur fond sombre ; sur une page qui porte la fiche papier, aucun texte sous 4,5 : 1 (25/10/2026) |
| `controle_contraste_liens.mjs [chemin]` | n°303 (21/09/2026) : chaque lien se lit (contraste) |
| `controle_axe.mjs [--muet] [chemin] [--json <f>] [--reference]` | 11/11/2026, au navigateur : axe-core (WCAG 2.0, 2.1 et 2.2 A/AA, bonnes pratiques) sur chaque page à 1 280 px. Refuse qu'une page porte PLUS de défauts graves (critical, serious) que `_outils/axe_reference.json` ; les défauts de structure (`region`, `heading-order`) sont mesurés, jamais refusés. `--reference` réécrit la référence, sur tout le dépôt, en fin de lot et après lecture de ce qui a changé. Demande le paquet `axe-core`, non versionné ; banc `tests_controle_axe.mjs` |
| `controle_debordement.py` | n°135 (second passage du 27/09/2026) : un tableau large défile au lieu de casser la page sur mobile |
| `controle_tactile.py` | 06/11/2026 : sur iPhone et iPad, chaque champ passe à 16 px au toucher (sinon la page zoome) ; « Aller au contenu » est le premier lien de la page ; les gabarits qui fabriquent des pages portent la règle |
| `onglets_clavier.py --etat --strict` | n°326 (17/11/2026, audit de `3e_C4.1`) : les onglets des séances se manient au clavier — ← → Début Fin, un seul onglet dans l'ordre de tabulation, chaque onglet relié à son panneau. Sans `--etat`, `--ecrire` pose le bloc sur les pages qui ne gèrent pas les flèches ; banc `tests_onglets_clavier.py` |
| `controle_code_colore.mjs [--muet] [dossier]` | n°13 (05/11/2026), au navigateur : chaque listing de programme ou d'algorithme, et chaque éditeur de code, est en couleurs comme dans un IDE |
| `controle_marqueurs.py` | pointes de flèche SVG mesurées en pixels |
| `controle_loupe.py` | n°92 : l'agrandisseur de chaque page est le v2, une seule fois (25/10/2026) |
| `banc_loupe.py [racine] [--captures <dossier>]` | n°92 au navigateur : un schéma SVG agrandi garde ses couleurs (écart mesuré), la légende ne recouvre pas l'image, à 1280, 390, 1920 px et 1280 px zoomé 150 % |
| `controle_lecteur_pas_a_pas.py` | décision 4b (25/10/2026) : chaque animation pas à pas utilise le lecteur commun (`_outils/lecteur_pas_a_pas/`), posé une fois, à jour |
| `lecteur_pas_a_pas/banc_lecteur.py [racine]` | chaque animation pas à pas, au navigateur : étapes, 390 px, mouvement réduit, voix sur le disque, impression, lien direct |
| `controle_competences.py` | n°314 (26/10/2026) : chaque code CRCN montré à l'élève porte son intitulé officiel ; la bulle d'une étiquette CRCN donne, pour chaque compétence, l'intitulé, la description du cadre et « Ici : » ; celle du socle, chaque domaine en toutes lettres |
| `intituler_codes.py [--ecrire] [--etat [--strict]]` | 17/11/2026 (demande de Pascal) : chaque étiquette de code du programme (« 3e_C4.1 », « 4e_C7.1 · C7.2 », « 5e_C9.1 → C9.3 ») dit sa compétence au survol — « Programme 2024 — code : intitulé », une ligne par code, intitulés de `data_competences.py`, OST en toutes lettres. `--ecrire` pose les bulles ; les générateurs de pages qui écrivent des étiquettes l'appellent avant d'écrire. Banc `tests_intituler_codes.py` |
| `controle_mode_essentiel.py [racine]` | n°29, au navigateur (26/10/2026) : le mode essentiel ne laisse aucune carte réduite à son titre |
| `controle_schemas.mjs [dossier…] [--planche <dossier>] [--json <fichier>] [--charge [n]]` | n°315 (28/10/2026), au navigateur : chaque schéma (fichier SVG ou SVG d'une page) — cadres qui se touchent, texte qui déborde, textes superposés, flèche qui traverse un cadre ou un texte, taille de police écrasée, étiquette de flèche collée à son trait (⚠ à moins de 6 unités, 15/11/2026) ; classe du pire au meilleur, fabrique la planche de captures pour la revue à l'œil ; `--charge` (11/11/2026) liste les schémas les plus chargés — entités (cadres hors cellules de tableau et pastilles), flèches, mots — au-dessus du repère de 9 entités ou 12 flèches : une mesure, hors score et hors sortie ; banc `tests_controle_schemas.mjs` |
| `mesurer_voix.py [racine] [--muet] [--json <f>]` | 11/11/2026 : le débit de chaque voix d'animation pas à pas, étape par étape (mots prononcés ÷ durée du fichier `.ogg`, par ffprobe) ; nomme les étapes au-dessus de 170 mots/min. Mesure, sortie 0 ; sortie 2 si ffprobe manque ou si une étape n'a pas son fichier ; banc `tests_mesurer_voix.py` |
| `controle_impression_papier.py` | décision 1a (25/10/2026) : chaque séquence porte la fiche papier (`_outils/impression_papier/`), posée une fois, à jour |
| `impression_papier/banc_papier.py [racine] [--pdf <dossier>] [--filtre <texte>]` | chaque séquence imprimée en PDF A4, séance par séance : pages comptées, en-tête, une seule séance, aucun champ d'écran, aucun texte pâle, zéro erreur JavaScript |

**Évaluation (QCM)**

| Outil | Vérifie |
|---|---|
| `qcm_aides/poser.py --etat [--strict]` | n°337 et n°339 (17/11/2026) : chaque QCM a sa carte « Avant de commencer », les aides progressives (indice, règle, correction) et ses pièges. Généralisation achevée le 17/11/2026 (72 QCM sur 72) : en fin de lot, `--strict` (sortie 1 si un QCM n'a pas les trois) ; banc `tests_audit_double_regard.py` |
| `controle_memes_nombres.py [--strict]` | n°338 (17/11/2026) : N1 le QCM annoncé par la séquence ou le README a ce nombre de questions et d'illustrées ; N2 « au moins N » garde son N dans un bloc ; N3 le message du bilan n'est pas recopié d'un autre lot. Mesure (sortie 0) ; `--strict` sort à 1 |
| `controle_banque_qcm.py` ⚠ 0 | la ligne « Banque : … » dit ce que le QCM contient |
| `controle_effectifs_qcm.py` ⚠ 0 | le QCM dit vrai sur sa taille (manifeste, lexique) |
| `controle_entete_qcm.py` ⚠ 0 | titre, menu « Compétence à réviser » et pied de page sont ceux du lot |
| `controle_echantillonnage.py [chemin]` ⚠ 0 | n°202 (28/08/2026) : au moins 5 questions par code évalué. Ne prend pas `--muet` : il le lit comme un chemin |
| `controle_longueurs.py [chemin]` ⚠ 0 | la bonne réponse ne se devine pas à sa longueur. Même piège avec `--muet`. Place par longueur (15/11/2026, mesure) : la bonne réponse strictement la plus longue / la plus courte / au milieu, cible 15 / 15 / 70, ⚠ au-delà de 40 % de « la plus longue » ; même mesure dans les séquences avec `controle_ordre_propositions.py --longueur` |
| `controle_validations.py [--detail] [chemin]` | n°340 (18/11/2026) ; 17/11/2026 (skill `validations-qui-disent-vrai`, audit de `3e_C4.1`) : V1 ✘ un seuil codé (`valide: ok>=5`) qui contredit le critère annoncé (« 6 / 6 ») — sortie 1 ; ⚠ une tolérance non annoncée, une réponse changée qui garde la validation (V3), une réponse écrite validée sans relecture annoncée (V4), un simulateur qui ne dit pas qu'il est simplifié (V5) ; banc `tests_controle_validations.py` |
| `controle_propositions_indices.py [--detail] [chemin]` | n°341 (18/11/2026) ; 17/11/2026 (skill `propositions-sans-indice`) : dans les séquences, I1 ⚠ la bonne réponse seule à porter sa justification, I3 ⚠ le résultat attendu d'un calcul lisible dans une étiquette, I4 ✘ une échelle d'auto-positionnement dans le désordre (⚠ sans description) ; même banc |
| `controle_indices_qcm.mjs [--muet] [--strict] [chemin] [--json <f>]` | 11/11/2026 : la bonne réponse ne se devine pas à ses mots. Refuse une banque où un mot absolu (« toujours », « jamais »…) ne vit que dans les mauvaises réponses (95 % sur 12 au moins) ou dont plus d'une bonne réponse sur quatre est seule à reprendre un mot de l'énoncé ; liste les propositions fourre-tout (« les deux », « aucune des réponses ») sans les refuser. Ne voit ni l'indice grammatical ni les questions des séquences ; banc `tests_controle_indices_qcm.mjs` |
| `qcm_aides/indices_creux.mjs [--detail] [--strict] [chemin]` | 17/11/2026 (skill `propositions-sans-indice`, § 4) : dans chaque QCM, le pourquoi (`d`) de chaque mauvaise proposition, qui sert d'indice (n°339) — « ! » (un intrus-plaisanterie), vide, ou creux (moins de 25 caractères, « Rien à voir. »). `--strict` sort à 1 sur un « ! » ou un vide ; `--liste <qcm>` numérote les questions pour écrire les pièges |
| `verif_qcm_coherence.mjs <qcm.html…>` ⚠ 0 | réfutations alignées sur les propositions. Sans argument, il ne lit rien et sort à 0 |
| `audit_lisibilite_qcm.mjs` | n°300 (20/09/2026) : inventaire des propositions qui masquent la question (0 / 2) |
| `controle_question_seule.py [--strict] [--chantiers] [chemin]` | n°343, n°344, n°345 (21/11/2026, skill `question-qui-se-lit-seule`) : dans chaque QCM, S1 un code sans son nom (« S2 »), S2 un renvoi sans document (« du tableau »), S3 une autre année (n°304), S4 une notion affichée qui souffle la réponse, E1 une liste annoncée et tronquée — refus avec `--strict` ; D1 moins de six questions sur document, P1 une séquence sans billet de sortie (n°330) — chantiers, comptés. 2 si rien n'est lu. Banc `tests_controle_question_seule.py`. Zéro refus ne dit pas que le QCM est bon : la suite se lit, question par question |
| `balayer_questions_qcm.mjs [--muet] [--apres] [chemin]` | n°343, n°345 (21/11/2026), au navigateur : chaque question de chaque QCM jouée à 390 px — B1 la page plus large que l'écran, B2 une figure non décodée, B3 sans description, B4 un document de QCM sous 300 px, B5 une erreur ; `--apres` joue une réponse fausse et mesure les trois écrans de l'aide. Sortie 1 si une question est en écart, 2 si aucun QCM n'est lu. Banc `tests_balayer_questions_qcm.py` |

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
`controle_axe.mjs` demande en plus le paquet `axe-core` (licence MPL-2.0, non versionné dans le dépôt) : `npm install axe-core` dans le dossier
parent du dépôt, ou `AXE_CORE=/chemin/vers/axe.min.js`. Sans lui il sort à 2 (en panne), jamais à 0.

**Le mouvement** (veille du 16/11/2026) : `python3 _outils/controle_mouvement.py <dossier du lot>` — ⚠ M1, une animation
sans repli « moins de mouvement » ; ⚠ M2, une boucle sans fin qu'aucun bouton n'arrête. Sortie toujours 0 : c'est une
mesure, à citer dans le rapport ; banc `tests_controle_mouvement.py`.

## Hors outils : bancs du lot et vérifications à la main

- Bancs du lot (`tests_<lot>.mjs` ou `.py`), lancés comme on les lance vraiment, en sous-processus (n°299, second corollaire).
  Ils couvrent la sauvegarde et la reprise, les exports, les verrous, le sélecteur de parcours (n°122, 21/08/2026), le clavier
  et 390 px. Ils testent la page telle que le navigateur la rend (n°49, 08/08/2026).
- Scénarios de notes : trois jeux de réponses connus par évaluation, avec le score attendu calculé à la main dans le rapport et rejoué
  par le banc (par exemple 32/32 → 20,0/20, 16+16 → 10,0/20, 8+8+16 non répondues → 5,0/20).
- Poids des images, à la main : `find <dossier du lot> -type f \( -name '*.png' -o -name '*.jpg' -o -name '*.jpeg' \) -size +300k`.
- Aucun outil du dépôt ne valide le HTML, ne vérifie le parcours au clavier seul ni ne cherche les secrets : les faire à la main, ou les lister comme restants.

### La revue d'écran en trois tours (décision de Pascal, 07/11/2026)

Un contrôle mesure ce qu'on lui a appris à mesurer ; une capture montre ce à quoi personne n'avait pensé (pilier 2, point 6
de `_outils/METHODE.md`). La méthode capturait déjà ; elle ne bouclait pas. Idée reprise de l'inspection du skill externe
« Taste Skill » du 07/11/2026 (refusé, voir `SKILLS_AUDIT.md`) et réécrite de zéro pour le dépôt — aucun code tiers.

1. **Capturer** chaque page élève du lot, telle que le navigateur la rend, à **390 px** et à **1 280 px**, au premier écran
   et sur chaque bloc dont la forme a changé (les captures vont dans `_outils/captures_<sujet>_<date>/`, comme les vagues
   précédentes).
2. **Regarder** les captures — vraiment, avec l'outil de lecture d'image — et nommer **les trois pires défauts**, dans
   l'ordre : ce qui empêche de lire ou de répondre, puis ce qui gêne, puis ce qui est laid. Un défaut nommé dit la page,
   la largeur, l'endroit, et ce qu'on voit (« à 390 px, la `<legend>` passe à la ligne et coupe le bord du `<fieldset>` »).
3. **Corriger** ces trois-là, pas davantage, puis **recapturer** à la même position de défilement.
4. **Trois tours au plus.** Au troisième, ce qui reste est écrit dans le rapport du lot comme restant, avec sa capture ;
   on ne prolonge pas la boucle, on livre.
5. Les captures du premier et du dernier tour vont dans la description de la PR (deux images de la même question, même
   position de défilement), et le rapport de tests dit combien de tours ont été faits et ce que chacun a corrigé.

Ce que la boucle ne remplace pas : les contrôles de `_outils/` (ils passent avant), les bancs du lot, et le regard de Pascal.
Ce qu'elle n'est pas : une « direction artistique » — la forme des pages est fixée par les règles d'or (n°306, n°311, n°315),
la boucle corrige des défauts, elle ne choisit pas un style.

## Sortie obligatoire

- `rapport_tests_<lot>.md` dans le dossier du lot :
  - chaque contrôle exécuté, avec son code de sortie et son périmètre (pages lues) ;
  - les scénarios de notes ;
  - ce que la suite ne couvre pas ;
  - les contrôles **non exécutés**, chacun avec sa raison.
  - Il ne cite que des scripts livrés (`controle_rapports_tests.py`).
- Le manifeste du lot (`manifest_lot_*.json`) et l'entrée au journal : voir `_outils/METHODE.md`, « Le lot est un ensemble INDIVISIBLE ».
- Puis la livraison, par le skill `livraison-depot-cycle4` : régénération, branche, PR sous garde-périmètre. Depuis la règle d'or n°5
  amendée (30/07/2026), Fable pousse sa branche et ouvre sa PR ; le colis (bundle → Downloads) est le plan B.
  Depuis le 21/11/2026 (n°5 amendée), **une PR de thème (`theme-1/2/3` dans la branche) se fusionne seule dès que
  `perimetre` est vert** : tout ce qui doit partir (accès rapide, index, audit, journal) est dans la PR AVANT de l'ouvrir ;
  un choix pédagogique que Pascal doit lire d'abord part avec l'étiquette `attendre-Pascal`. Les PR transversales
  (`fable/<slug>`) restent à sa fusion.

## Critères de réussite

- Aucun contrôle bloquant en échec non corrigé.
- Aucun contrôle en panne (sortie 2, trace, module manquant) compté comme vert.
- Tout contrôle non exécuté est listé explicitement comme « restant à faire », jamais passé sous silence (n°47).
