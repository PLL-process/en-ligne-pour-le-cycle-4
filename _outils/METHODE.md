# Méthode Fable — production pédagogique harmonisée

Méthode éprouvée sur les LOTs 01-09 du Thème 2 (juillet 2026). Trois piliers :
produire un lot · livrer et gouverner · rédiger une progression annuelle.
Référence des décisions : `JOURNAL_DES_DECISIONS.md` à la racine du dépôt.

## Pilier 1 — Produire un lot pédagogique premium

### Avant de concevoir (préalables obligatoires)

1. **Lire le journal depuis un main à jour** (règle d'or n°10 : le journal
   fait foi) et consulter le registre central des règles d'or en tête de
   fichier — les règles 7 à 11 sont postérieures à ce document.
2. **Lire `_ressources-communes/`** : documents institutionnels (programme
   2024, socle, CRCN, cahiers Pix, guides matériels) et sources d'inspiration
   déposés par Pascal. Toute séquence s'y adosse ; tout CRCN déclaré suit la
   règle n°7 (compétence exacte + niveau + repère verbatim + action
   observable + trace).
3. **Doctrine logicielle : « obligatoire sur classique, bonus sur
   trouvaille »** — le parcours obligatoire d'une activité repose sur les
   logiciels classiques que les élèves ont réellement (Tinkercad, ArduBlock,
   Blockly@rduino, Vittascience, Filius, Cisco Packet Tracer, mBlock,
   Arduino IDE, Sweet Home 3D, FreeCAD) ; les trouvailles et pilotes
   (Velcio, Flowcode, Blender, CADAM…) n'apparaissent qu'en bloc 🎁 Bonus.
4. **Skills externes = FOND, règles d'or = FORME** : les skills
   pédagogiques installés (explicit-instruction, questioning-discussion,
   curriculum-assessment-cycle4, self-regulated-learning, k12…) nourrissent
   la conception ; en cas d'écart de forme, les règles d'or et le présent
   document font foi.

### Le lot est un ensemble INDIVISIBLE

Un lot = séquence HTML interactive + QCM séparé (~30 q) + synthèse élève +
synthèse professeur + fiche pédagogique + matrice de couverture (notions ↔
activités ↔ questions QCM) + SOURCES_MEDIAS.md + rapport de tests + manifest
JSON + README pointeurs pour les codes mutualisés + entrées nouveautes.json +
mise à jour OVERLAY (audit) + entrée au journal. On ne livre jamais une
séquence sans son QCM ni ses synthèses.

### Les règles d'or (registre complet en tête du journal — 12 à ce jour)

Les six fondatrices sont détaillées ci-dessous ; s'y ajoutent :
**7** CRCN observable, tracé, justifié (5 éléments obligatoires) ·
**8/9** représentations technologiques utiles, progressives, traçables
(principe Fable + cadre Codex) · **10** le journal fait foi (lecture avant
travail, entrée par lot, réservation des numéros au registre) ·
**11** navigation persistante ⌂ Accueil (+ ← Séquence) sur toute page ·
**12** cycle de vie des héritées : badge 🛠 « modernisation prévue »
(`_outils/heritees.json`) tant que le remplaçant n'existe pas, archivage
dans `_archive-anciennes-versions/` DANS LE MÊME COMMIT que la livraison du
remplaçant, avec mise à jour de tous les câblages — jamais de suppression.

### Les 6 règles d'or fondatrices (texte complet au journal)

1. **Images v2** : chaque image est un document à LIRE (jamais décorative),
   SVG original CC0 avec title/desc accessibles. Jamais Google Images, jamais
   de scan, jamais de hotlinking.
2. **En-tête QCM standard** (gabarit LOT 01) : badges niveau/codes/thème,
   tableau de bord de progression, modes, sauvegarde locale.
3. **Versions 🅰/🅱/🅲** quand c'est possible : matériel réel (très basse
   tension UNIQUEMENT — jamais le secteur) / simulation intégrée / sans
   matériel.
4. **Blocs élève obligatoires** : titre `<h1>` + sous-titre-mission EN
   PREMIER ; bloc « 🧠 Prêt·e à t'entraîner ? » (nb de questions, nb
   d'illustrées, UN SEUL bouton QCM de toute la séquence) ; bloc « 🎁 Bonus
   (facultatif — hors parcours obligatoire) » avec 2-3 défis ouverts sans
   vérificateur. Les deux blocs closent la page : après le bilan, avant le
   pied de page.
5. **Gouvernance** : voir pilier 2.
6. **Convention des chaînes** : information EN HAUT, énergie EN BAS, flèche
   d'ORDRE qui descend. À toute consigne de traçage, insérer l'encadré
   canonique : « 📐 Règle d'or du schéma : l'INFORMATION en haut, l'ÉNERGIE
   en bas, la flèche d'ORDRE qui descend — le cerveau au-dessus des muscles,
   la commande au-dessus de la puissance. La disposition EST une leçon :
   elle montre qui commande, sans un mot. »

### Titres et navigation (charte harmonisée, juillet 2026)

- **Charte des titres** (h1 + `<title>`) pour séquences, QCM et ateliers,
  généralisée aux trois thèmes (§IV du projet pédagogique, lecture PAR THÈME
  validée par Pascal le 30/07/2026 : chaque année, les trois villes) :
  `Thème <n> · <ville> — <niveau> · S<n> : <nom court>` avec Thème 1 ·
  Chine, Thème 2 · Martinique, Thème 3 · New York ; pour une ressource sans
  créneau de classeur, remplacer `S<n>` par `Atelier`. Pour le Thème 2 : le
  `S<n>` est ALIGNÉ sur l'onglet du classeur de progression du niveau
  (S4-S5 quand la séquence couvre deux créneaux ; le `<title>` ajoute les
  codes entre parenthèses). Les NOMS DE FICHIERS et URLs ne changent
  JAMAIS (liens déjà câblés).
- **Navigation (règle d'or n°11)** : chaque page porte une barre collante
  `⌂ Accueil` (lien RELATIF vers l'index racine — relatif et non absolu
  pour préserver le fonctionnement hors ligne, esprit de la règle conservé)
  et, sur les QCM, synthèses et ateliers, `← Séquence`. Clavier, focus
  visible, masquée à l'impression.

### La séquence

- **Situation déclenchante ancrée** : un objet réel de la vie du collège ou
  de la commune (Martinique), un problème posé par une personne (gardien,
  mairie, club) — l'élève devient l'expert qu'on appelle. Objet-fil par
  niveau (5e : lampadaire intelligent · 4e : jardin connecté · 3e : station
  d'alerte cyclonique) : le même objet se décrit, se programme, se dépanne.
- **Structure** : hypothèse de départ (rappelée au bilan) → séances en
  onglets → activités avec méta (objectif/compétence/production/ressources),
  consigne, exercices en LISTES DÉROULANTES exclusivement (DYS), aides à
  2 niveaux, vérificateur, correction complète repliée, « à retenir »,
  pièges classiques, critère de réussite → bilan avec auto-positionnement
  par code → blocs règle n°4.
- **Programmation : éditeur Vittascience EMBARQUÉ** (standard demandé par
  Pascal, 30/07/2026) : toute séquence de programmation intègre l'éditeur
  directement dans la page (iframe `fr.vittascience.com/python/?mode=mixed&
  console=bottom` — blocs + Python côte à côte), jamais un simple lien
  sortant. L'iframe étant hors de notre page, le verrou suit le motif
  **prédire → tester dans l'éditeur → reporter** : l'élève prédit (liste
  déroulante), exécute, puis reporte la valeur observée — une valeur que
  seule l'exécution révèle.
- **Verrous expérientiels** : les manipulations obligatoires (simulateur,
  exploration) sont tracées (`window.__exp`) et EXIGÉES par le vérificateur —
  l'élève doit vraiment faire l'expérience, pas seulement répondre.
- **Technique** : page unique hors-ligne, sauvegarde localStorage (clé
  `seq_<codes>_<slug>`), accessible (aria, clavier, reduced-motion),
  imprimable A4, aucune donnée envoyée.

### Le QCM

30 questions (réparties équitablement entre les codes), chaque question =
4 options + explication de la bonne réponse + exemple + erreur classique +
réfutation de CHAQUE distracteur + « à retenir ». 3+ questions illustrées
(images v2). Bonnes réponses RÉPARTIES sur A/B/C/D (l'assembler écrit tout
en r:0 puis exécute `fix_r.js <fichier> <graine>` — permutation déterministe).
Clé localStorage `qcm_<codes>_<slug>`.

### La barre qualité (non négociable)

- Ne déclarer QUE des tests réellement exécutés (suite Playwright : verrous,
  sauvegarde/restauration, liens, blocs règle n°4, zéro erreur JS).
- Jamais de corrigé d'évaluation sommative dans le dépôt public.
- Très basse tension uniquement ; le secteur 230 V est nommé comme interdit.
- Ne jamais modifier les fichiers existants d'un autre auteur : les intégrer
  comme ressources complémentaires (référencées dans README et séquence).
- Statuts d'audit : dossier principal = COMPLET ET VALIDABLE ; autres codes
  de la séquence mutualisée = COUVERT + README pointeur.

## Pilier 2 — Livrer et gouverner

1. **Une branche = un lot**, créée depuis un main TOUT FRAIS, nommée avec le
   motif du thème : `<agent>/theme-N/<slug-du-lot>`. La garde-périmètre
   (GitHub Actions) refuse toute PR dont les fichiers sortent du périmètre :
   dossier du thème + fichiers communs (index.html, README.md,
   audit_couverture.*, nouveautes.json, JOURNAL_DES_DECISIONS.md,
   `_progressions/`). `_outils/` = Thème 2 ; `.github/` = Pascal.
2. **Fichiers générés** (index, README racine, audit) : JAMAIS édités à la
   main, JAMAIS fusionnés manuellement. On régénère, toujours sur un arbre à
   jour de main : `python _outils/build_audit.py` puis
   `python _outils/make_index.py`. En cas de conflit : prendre n'importe
   quelle version puis régénérer.
3. **Avant livraison** : rebaser sur le main du jour, RE-régénérer, tester,
   commiter. Une PR = un lot, fusion rapide, branche supprimée.
4. **Main est protégé** : tout passe par PR + contrôle `perimetre` vert.
   Un refus de la garde ne se contourne jamais. Faux « non fusionnable » de
   GitHub : recharger la page ou fermer/rouvrir la PR. Un « Re-run » rejoue
   l'ANCIENNE version d'un workflow — pour prendre une correction, il faut
   un nouveau déclenchement (close/reopen).
5. **Circuits de livraison** : Fable → bundle git déposé chez Pascal, qui
   pousse (`git fetch <bundle> branche:branche` puis push). ChatGPT →
   push direct + PR. Grok (sans réseau) → script autonome + JSON via Pascal.
6. **Banc d'essai obligatoire** pour tout script qui touche aux classeurs
   `_progressions/` : exécution sur COPIE, vérification que seuls les
   onglets cibles changent et que les formules (Calendrier, Moteur, Frise)
   sortent intactes, AVANT toute exécution réelle. openpyxl sans
   `data_only=True` (sinon les formules sont détruites à la sauvegarde),
   écriture uniquement sur les ancres de cellules fusionnées.

## Pilier 3 — Rédiger une progression annuelle (réutilisable chaque année)

Un classeur PAR CLASSE (`_progressions/<niveau>/Progression_Techno_<niveau>_
<année>_Martinique.xlsx`), construit avec openpyxl. Structure :

1. **🏠 Accueil** : tuiles de synthèse, navigation cliquable, mode d'emploi.
2. **📅 Calendrier** : UNE ligne par semaine réelle de l'année scolaire de
   l'académie (Martinique : rentrée, Toussaint, Noël, Carnaval, Pâques —
   vérifier les fériés TOMBANT EN PÉRIODE DE CLASSE, ex. 11 nov., Vendredi
   saint, lundi de Pâques), périodes P1-P5 teintées. **1 séance de 1 h 30
   par semaine** — c'est la contrainte reine : tout le volume annuel s'y
   plie (≈ 30 séances utiles + tampons).
3. **Le moteur d'imprévus** (le cœur réutilisable) : la colonne
   « Affectation » du calendrier est calculée par formule
   (INDEX sur la liste ordonnée des créneaux de l'onglet ⚙ Moteur, via un
   rang cumulé qui SAUTE les semaines marquées d'un imprévu). Poser un
   imprévu (menu déroulant : 12 types — absence, sortie, ERASMUS, Fête de la
   science, cyclone, remplacement…) décale automatiquement TOUTES les
   séances suivantes ; l'effacer les fait revenir. Des **semaines tampons**
   en fin de période absorbent le retard (« on prend du retard, rarement de
   l'avance ») ; en 3e, réserver en plus des créneaux 🎓 RÉVISIONS DNB.
   Version .xlsm facultative : macros installées par script PowerShell/COM
   (fenêtres insérer/effacer un imprévu, aller à aujourd'hui, copier le
   cahier de texte).
4. **🗓 Frise** : gantt par formules + mise en forme conditionnelle.
5. **📚 Référentiels** : cycle 4 complet (114 codes) + référentiel du niveau.
6. **🧭 Progression** : 7-9 séquences, Début/Fin calculés AUTOmatiquement
   depuis le calendrier (INDEX/MATCH) — jamais saisis à la main.
7. **Générateurs S1-S7** (un onglet par séquence, rempli par l'IA du thème
   responsable) : identification (problématique, situation déclenchante,
   prérequis, objectifs, évaluation, DOMAINES DU SOCLE, CRCN/Pix, versions
   A/B/C, liens EPI, repères manuel, ressources en ligne) + tableau des
   compétences officielles + déroulé séance par séance avec blocs
   **📋 CAHIER DE TEXTE prêts à coller dans Pronote** (contenu de séance +
   travail à faire, 1 h 30 max de travail maison par semaine) + ligne de
   suivi enseignant (jamais pré-remplie).
8. **Règles de remplissage** : chaque IA ne remplit QUE ses onglets ;
   vérification croisée des compétences écrites entre thèmes (« parfois on
   se trompe ») ; les liens des générateurs se câblent sur les ressources
   PUBLIÉES au fil des lots.

**Pour l'année suivante** : régénérer le calendrier avec les nouvelles dates
de l'académie, reconduire la structure telle quelle, réaffecter les
séquences aux semaines — le moteur d'imprévus et les générateurs se
réutilisent sans modification.

## Skills spécialisés du dépôt (compléments)

Ce document est le chapeau ; pour le détail opérationnel, six skills
spécialisés existent dans `.claude/skills/` du dépôt :
`sequence-pedagogique-engageante` (gabarit de séquence),
`qcm-html-accessible` (chaîne QCM), `controle-qualite-lot` (revue de fin de
lot), `licences-medias-education` (médias et SOURCES_MEDIAS.md),
`audit-couverture-cycle4` (matrice des 114 codes),
`arduino-grove-college` (activités carte/capteurs, versions A/B/C, TBT).
En cas d'écart entre un skill ancien et les règles d'or du journal, LE
JOURNAL FAIT FOI (les règles n°4 et n°6 sont postérieures à ces skills).

## Code coloré façon IDE (règle d'or n°13)

Tout LISTING de programme affiché dans une ressource (simulateur de mémoire,
`pre.code`, valeurs des boîtes) est colorisé comme dans un vrai IDE, avec la
palette commune du site — sans dépendance externe (aucun CDN : les pages
restent 100 % hors ligne) :

| Famille | Classe | Couleur |
|---|---|---|
| variables | `.py-var` | cyan `var(--hl)` |
| chaînes `"…"` | `.py-str` | vert `var(--ok)` |
| nombres | `.py-num` | orange `var(--energie)` |
| mots-clés (`print`, `def`, `if`…) | `.py-kw` | violet `var(--head)`, gras |
| `=` et opérateurs | `.py-op` | jaune `var(--warn)`, gras |
| commentaires `#` | `.py-com` | gris bleu, italique |
| numéros de ligne pédagogiques | `.py-lno` | bleu discret |

Le colorisateur est la petite fonction `pyc()` embarquée dans la page (elle
tokenise : chaînes → commentaires → nombres → identifiants → opérateurs) et
s'applique au chargement à `pre.code` et `#memCode > div`. Une légende 🎨
accompagne le PREMIER listing de la page. Le `<code>` en ligne dans la prose
reste monochrome (la couleur est réservée aux listings, pour garder sa force).
Référence : règle d'or n°13 au journal (entrée du 30/07/2026, PR de la
branche `fable/theme-3/code-colore-ide`).

## L'esprit de la méthode

Ultra premium, ultra pédagogique : l'élève vit une histoire vraie, manipule
réellement (verrous), reçoit des corrections qui enseignent, et retrouve les
mêmes conventions partout. L'enseignant reçoit des outils finis, testés,
honnêtes sur ce qui a été vérifié. Et chaque leçon apprise devient une règle
écrite — le journal d'abord, le gabarit ensuite, les trois thèmes enfin.
