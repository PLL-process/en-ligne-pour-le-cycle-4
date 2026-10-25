---
name: sequence-pedagogique-engageante
description: Construire une séquence de technologie cycle 4 sur le squelette unique du dépôt (règle d'or n°306, vérifié par _outils/controle_squelette.mjs). À utiliser pour toute création ou refonte de séquence, avant d'écrire la moindre ligne de HTML.
---

# Séquence pédagogique engageante (squelette du dépôt)

Mis à jour le 23/10/2026 (inventaire des skills) : aligné sur le journal jusqu'à la règle d'or n°311.

Le journal fait foi (règle d'or n°10). Pour le texte complet d'une règle, chercher « Règle d'or n°NNN » dans
`JOURNAL_DES_DECISIONS.md`. Ce skill fixe la forme. Le fond pédagogique reste la décision de Pascal.

## Référence

- **Squelette** : règle d'or n°306 (22/09/2026), amendée par la n°311 (22/10/2026). On le vérifie à l'écran avec
  `node _outils/controle_squelette.mjs [chemin]` (Chromium, onglet par onglet, défauts D1 à D6).
- Séquence modèle : 5e_C3.1 (décision de Pascal du 23/10/2026) — pilote de la n°311 ; le squelette n°306 et controle_squelette.mjs restent la référence vérifiable.
  Fichier : `theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/5e/5e_C3.1/sequence_5e_C3.1-C3.4_shanghai.html`
  (banc `tests_regle_311_5e_C3.1.mjs`).
- Ne pas recopier du modèle ce qu'il ne respecte pas encore (relevé du 23/10/2026) :
  - la carte « 📚 Le référentiel de la séquence — en toutes lettres », refusée par la n°298 ;
  - un Bonus sans corrigé, annoncé « sans vérificateur » (contraire aux n°86 et n°301) ;
  - l'absence de bloc « 🔄 Avant de commencer » ;
  - des étiquettes sans `title` ni `aria-label` (n°44) ;
  - un `<summary>` au vouvoiement (n°302).
  Le modèle ne montre ni sélecteur de parcours ni lexique par séance : les exemples sont plus bas.
- Le Jardin connecté `4e_C6.2` n'est plus une référence. `verif_regles_audit.py` y relève neuf manquements
  (n°26, 29, 30, 31, 34, 298, 300, 301, 304).

## Ouverture : visible à la séance 1, repliée à partir de la séance 2

Dans l'ordre :

1. Titre `<h1>` et mission en une phrase (n°4, 24/07/2026).
2. Barre d'outils : imprimer, effacer ma sauvegarde, mode essentiel (n°29, 08/08/2026).
3. Ligne d'étiquettes sous le titre (niveau, codes, socle et CRCN, durée). Chaque étiquette a un `title` et un `aria-label`
   (n°44, 08/08/2026, maintenus par la n°298). Sur la page élève, le référentiel se limite à cette ligne.
4. « 🔄 Avant de commencer : ce que je vérifie » (n°304, 21/09/2026, titre choisi par Pascal) : les compétences qui
   devraient être en place, avec leurs codes. Chacune a un moyen de la rattraper : lexique, capsule « Je révise » ou fiche.
   Jamais « tu as fait », que ce soit l'année précédente ou plus tôt dans l'année. Une séquence de la même année se cite au conditionnel.
5. Situation déclenchante : concrète, crédible, sans solution donnée, illustrée (SVG original de préférence).
6. Problématique ouverte, plus un problème intermédiaire par séance.
7. Hypothèse de départ : champ enregistré, avec sa version étayée (n°31, 08/08/2026).
8. « Je serai capable de… » (n°302, 20/09/2026 ; n°306) : voir l'avertissement ci-dessous.
9. Billet d'entrée sans note (n°26, 08/08/2026).

À partir de la séance 2 (n°311) : titre sur une ligne, mission en une phrase, barre d'outils. Vient ensuite
`<details class="rappel-ouverture">` « 📖 Rappel : la situation et ton hypothèse », qui contient les étiquettes et tous les blocs
d'ouverture, puis la séance. À la séance 1, le volet est ouvert et n'a pas de bouton. Ensuite, il est replié derrière un
`<summary>` visible. Sans JavaScript et à l'impression, tout s'affiche. L'ouverture est repliée, jamais supprimée.

⚠ **Référentiel : tension entre la n°298 et la n°306, relevée le 23/10/2026.**
- La n°298 (15/09/2026) retire de la page élève le référentiel « en toutes lettres » : codes, formulations du BO, socle, CRCN.
  `verif_regles_audit.py` refuse la classe `referentiel-card` et les cartes titrées « Référentiel… »,
  « Ce que dit le programme… » ou « Compétences & connaissances… ».
- Le référentiel complet va dans la synthèse professeur, recopié sans réécriture, dans un `<div class="bloc referentiel-eleve">`
  placé en tête. Il est accompagné de la phrase qui distingue le BO n°9 du 29/02/2024 de la codification interne du dépôt.
- La n°306 garde pourtant un bloc « Je serai capable de… » dans l'ouverture. Au 23/10/2026, aucune page ne porte ce bloc
  sans la carte que la n°298 refuse.
- Pratique actuelle des six pages de 3e du thème 2 passées à la n°298 (`3e_C4.3`, `3e_C5.1`, `3e_C6.1`…) : aucun bloc
  référentiel sur la page élève. La suivre, et signaler l'écart dans le rapport du lot tant que Pascal n'a pas fixé cette forme.

## Séances

- Onglets `.seance-tab`, panneaux `.seance-panel`, barre `role="tablist"`. Après la barre d'onglets, tout élément visible est
  dans un panneau (défaut D5). Seuls font exception le tableau de bord des tâches (n°30), `.seance-avis`, le pied de page et le volet de la n°311.
- Pour chaque séance : question directrice, durée, objectif, organisation, matériel, consignes et activités alternées
  (observation → investigation → manipulation ou simulation → conception → test → argumentation). Ajouter les productions
  intermédiaires, les aides de niveau 1 et 2 (`details.aide1`, `details.aide2`) et les critères de réussite.
- Durée : la somme des activités plus la marge de service tient dans le temps disponible (n°23).
- Chaque production demandée a son champ (n°67) et, si elle est écrite, sa version étayée (n°31). Son corrigé complet
  est replié et vient après l'activité (n°43).
- Question à choix : `<fieldset class="qcm-groupe">`, énoncé dans la `<legend>`, un `input type="radio"` par proposition avec
  son `<label for>`, le même `name` pour tout le groupe, et le texte de la proposition comme `value`. Jamais de `<select>`
  (n°300, 20/09/2026 ; le gabarit est au journal).
- En tête de panneau, le lien « 📖 Les mots de cette séance » quand le lot a son lexique par séance (voir plus bas).
- La séance se termine par un bouton vers la suivante, nommé par sa destination (n°101, 21/08/2026).

## Clôture : à la dernière séance seulement, dans son panneau

Règles d'or n°301 (20/09/2026) et n°306. Dans cet ordre, et aucun travail demandé après le bilan :

1. « 🎁 Bonus (facultatif — hors parcours obligatoire) » : des champs de réponse et un corrigé replié (n°86, 10/08/2026).
   Un Bonus qu'on peut seulement lire n'est pas un Bonus.
2. Bilan :
   - retour à l'hypothèse de départ ;
   - métacognition, sous forme d'une question sur la démarche (ce qui m'a surpris, où j'ai hésité, ce que je dois revoir).
     Le titre « Comment j'ai travaillé » est permis, pas obligatoire ;
   - « Je me positionne » sur les codes réellement travaillés. On ne se positionne pas avant d'avoir travaillé.
3. « 🧠 Prêt·e à t'entraîner ? » : nombre de questions, nombre de questions illustrées, un seul bouton vers le QCM du lot (n°4).
   C'est un renvoi, pas un travail.

La synthèse « à retenir » se place avant le Bonus (pratique de `3e_C5.1` et `3e_C7.4`).

## Trois façons de vivre la séquence (règles d'or n°3 et n°122)

- Elle s'applique, quand c'est possible, à toute séquence avec matériel, logiciel ou manipulation (n°3, fondatrice, 23/07/2026) :
  - 🅰 matériel réel, en très basse tension uniquement ; un lot réseau ne branche rien sur le réseau pédagogique (extension du 08/08/2026) ;
  - 🅱 simulation ou logiciel, gratuit et sans compte de préférence ;
  - 🅲 sans matériel : tout est dans la page. Les trois voies visent les mêmes objectifs, et 🅲 est un chemin complet.
- Ce sont trois parcours, pas trois paragraphes (n°122, 21/08/2026). Mettre un sélecteur en tête de page : boutons `.parcours-btn`
  (`data-choix="a|b|c|tous"`, `aria-pressed`). Les éléments d'une voie portent `data-parcours="a|b|c"`. Le choix masque les
  autres voies, il est mémorisé et réversible. Chaque voie s'imprime seule (n°102).
- Exemple qui fonctionne : `3e_C9.1` (`sequence_3e_C9.1_variables_types_systemes.html`), éprouvé par `tests_3e_C9.1.mjs`.
  Un sélecteur sans aucun `data-parcours` dans la page ne masque rien (n°136) : vérifier son effet à l'écran.
- Au 23/10/2026, aucune page ne porte à la fois le sélecteur et le volet de la n°311 : leur cohabitation n'a pas été éprouvée.
- L'encadré « Choix de l'outil » se place avant les voies, et les voies avant les séances. Si la séquence est débranchée par nature,
  omettre les voies et le justifier dans la fiche pédagogique.

## Matériel

- `inventaire_materiel.csv` donne le statut de chaque matériel. Une ligne y est périmée : l'imprimante 3D, encore
  « MATÉRIEL À CONFIRMER », est confirmée depuis le 02/09/2026 (règle d'or n°281) :
  - modèle FlashForge Adventurer 5M Pro, volume utile 220 × 220 × 220 mm ;
  - PETG en classe ; ASA seulement hors présence d'élèves.
- L'imprimante papier est une HP Color LaserJet Pro MFP 3302sdw. Les multimètres restent à confirmer.
- Marquer tout matériel non confirmé « MATÉRIEL À CONFIRMER — prévoir une alternative par simulation » et prévoir une voie 🅱 ou 🅲.

## Lexique par séance

- Consigne de Pascal du 24/09/2026, au journal (ce n'est pas une règle numérotée) : tout terme technique ou un peu compliqué va au lexique.
- Écrire `vocabulaire_<lot>.json` à côté de la séquence, une entrée par mot : `{mot, formes[], definition, seance: "sN" ou "ouverture", source}`.
  Pour les mots de base (objet technique, OST…), renvoyer à `_outils/vocabulaire_commun.json` avec `"commun": true` et un `"exemple"`.
- Générer le lexique : `python3 _outils/generer_lexique.py <dossier du lot>`. Il refuse un mot absent de sa zone, une entrée sans source
  et une définition qui contredit le « à retenir » d'un QCM (entrée du 23/09/2026).
- En tête de chaque panneau, mettre le lien « 📖 Les mots de cette séance » vers `lexique_<code>.html#seance-sN`. C'est déjà fait dans
  3e_C1.1, 4e_C1.1, 4e_C9.1 et 5e_C9.1.

## Programmes en blocs, chaînes d'énergie

- Un programme en blocs montré à l'élève est une capture réelle du logiciel, avec le programme construit et exécuté
  (n°308, 18/10/2026 ; n°94). Ce qui ne peut pas être capturé devient un algorigramme, du pseudo-code ou un tableau, jamais
  des blocs dessinés.
- Contrôle : `python3 _outils/controle_blocs_dessines.py`. Il vérifie les captures `bloc_vitta_*.png` de classe `bloc-capture` :
  300 Ko au plus, `alt` d'au moins 20 caractères, déclarées « Capture d'écran réelle » dans `SOURCES_MEDIAS.md`.
- Pour une chaîne d'énergie, appliquer le skill `chaine-energie-fonctionnelle` (n°310, 21/10/2026). Il conserve la convention n°6 :
  l'information en haut, l'énergie en bas, l'ordre qui descend.

## Différenciation, synthèse, contextes

- Prévoir les aides de niveau 1 et 2, la version étayée (n°31), le mode essentiel (n°29), la version sans matériel, la simulation
  et les adaptations EBEP. Les aides guident, elles ne font pas à la place de l'élève.
- Synthèse élève du lot : notions, vocabulaire FR + EN (capteur—sensor, actionneur—actuator, réseau—network, donnée—data, boucle—loop…),
  schéma, exemple, erreurs fréquentes.
- Démarche de projet en 12 étapes (du besoin au bilan réflexif), selon le thème. Interdisciplinarité facultative (type EPI).
- Contextes à privilégier quand ils sont pertinents, jamais plaqués : le collège, Sainte-Luce, Fort-de-France, la Martinique,
  cyclones, solaire, eau, agriculture, objets connectés, cybersécurité, robotique, réparation, mobilités, réseaux.

## Lot, langue, page

- Le lot est indivisible : voir `_outils/METHODE.md`, partie « Le lot est un ensemble INDIVISIBLE ». Il comprend la séquence,
  le QCM, les synthèses élève et professeur, la fiche pédagogique, la matrice, `SOURCES_MEDIAS.md`, le rapport de tests et le manifeste.
- Unités (n°312, 25/10/2026) : à sa première apparition dans chaque activité et chaque tableau, une unité que l'élève ne
  connaît pas depuis l'école est suivie de son nom en toutes lettres, au pluriel, entre parenthèses : « 1,2 W (watts) »,
  « 12 V (volts) », « 432 Wh (wattheures) ». Dans un tableau dont toute la colonne (ou la ligne) porte la même unité, le nom
  va dans l'intitulé : « Courant (en milliampères) ». Dans une liste à choix ou un groupe de boutons où une seule option
  porte l'unité, elle s'y écrit en toutes lettres (« la pile 9 volts ») et la `value` garde le texte que le vérificateur
  compare. Pas besoin pour m, cm, mm, km, g, kg, L, s, min, h, °C, €, %, km/h.
- Personnes (n°302) : la page élève dit « tu » quand elle guide, « je » pour ce que l'élève saura faire et pour son positionnement.
  La troisième personne est réservée aux pages destinées à un collègue (synthèse professeur, fiche pédagogique).
- Prévoir la sauvegarde locale et la reprise, les exports, une impression propre (n°102), une navigation complète au clavier
  et un étiquetage visible des voies 🅰/🅱/🅲. Garder séparées les pages élève, professeur et inspection.
- Note /20 : la version précédente de ce skill exigeait dans la séquence une note /20 à pondération paramétrable. Aucune règle
  d'or ne la porte, et aucune des 60 séquences n'en a (relevé du 23/10/2026) : la note /20 est celle du QCM du lot.

## Interdits

- Recopier un contenu, un exercice ou une illustration de Nathan ou d'un autre éditeur.
- Un contexte local artificiel, des questions piège, l'humiliation en cas d'erreur, les stéréotypes, du matériel non confirmé
  présenté comme disponible.
- Affirmer ce que l'élève a déjà fait (n°304).
- Laisser une trace de la fabrique dans ce que lit l'élève : numéro de règle, « convention du dépôt », nom d'agent ou de lot
  (n°309, 21/10/2026).
- Charger quoi que ce soit depuis Internet (n°305). Encadrer fr.vittascience.com dans un `<iframe>` (le site refuse).
- Publier une correction sommative dans une page publique.

## Contrôles avant de rendre

- `node _outils/controle_squelette.mjs <dossier>` : aucun défaut D1 à D6. Relancer avec `--json` pour lire les « à rédiger »
  (Bonus sans champ ou sans corrigé, bilan sans métacognition…) : le rapport texte ne les imprime pas.
- `python3 _outils/verif_regles_audit.py <dossier>` : compter les ✘, car la sortie vaut 0 même quand il y en a.
- `python3 _outils/controle_hierarchie.py <dossier>` (n°307) ; sur tout le dépôt : `controle_navigation_seances.py`,
  `controle_blocs_dessines.py`, `controle_regles_visibles.py`, `controle_unites.py` (n°312).
- Ensuite, la revue complète du skill `controle-qualite-lot`.

## Critères de réussite

- `controle_squelette.mjs` ne refuse pas la séquence. `verif_regles_audit.py` n'imprime aucun ✘ pour les n°298, 300, 301, 302 et 304.
- Chaque rubrique est réellement remplie : aucune section vide.
- La séquence est faisable dans un collège : durée réaliste (n°23), matériel confirmé ou voies 🅱/🅲.
- La cohérence problématique ↔ activités ↔ bilan ↔ QCM se vérifie en relisant seulement ces quatre parties.
