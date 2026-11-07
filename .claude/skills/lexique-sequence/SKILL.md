---
name: "lexique-sequence"
description: "Construit ou complète le vocabulaire d'une séquence du dépôt en-ligne-pour-le-cycle-4 (technologie collège) : relève les mots techniques ou simplement difficiles que l'élève rencontre, les définit en langage vulgarisé et sourcé dans `vocabulaire_<lot>.json`, les rattache à leur séance, puis engendre et câble la page `lexique_<lot>.html` avec les outils du dépôt. À utiliser à la fin de la rédaction d'un lot et lors des audits de lisibilité."
---

# Lexique de séquence

Origine : idée n°10 de la liste Grok du 07/11/2026, recadrée sur les constats
de classe de Pascal (septembre 2026) : des 3e qui ne savent pas ce qu'est un
objet technique, un objet naturel ou un système technique ; des élèves qui
ont du mal à lire, même en 3e ; le mot « innovation » qui en bloque certains.
D'où la règle du dépôt : **par prudence, tout terme technique ou
relativement compliqué entre au vocabulaire**, rattaché à la séance où il sert.

Ce skill n'invente pas d'outil : il décrit comment **remplir** ce que
`_outils/generer_lexique.py` sait déjà lire (entrées du journal des 23 et
24/09/2026), et comment ne pas se faire refuser.

## Avant tout : le journal fait foi (règle n°10)

Lire les entrées postérieures à ce skill. Si une règle d'or a depuis fixé la
forme du lexique, elle l'emporte sur ce qui suit.

## Ce que l'outil fait déjà — ne pas le refaire à la main

- `generer_lexique.py <dossier du lot>` écrit `lexique_<lot>.html` : d'abord
  les mots de `vocabulaire_<lot>.json` (une section par séance, « 📚 Séance N —
  les mots de la séance », ancre `#seance-sN` ; les mots de base sous
  « 🔄 Avant de commencer », ancre `#ouverture`), puis les notions des QCM avec
  leur « à retenir », mot pour mot (règle n°146 : un lexique n'invente rien).
- `_outils/vocabulaire_commun.json` porte les mots de base définis **une
  fois** (objet technique, objet naturel, système technique, OST…) : un lot y
  **renvoie**, il ne les redéfinit pas.
- `poser_lien_lexique.py --theme <dossier>` pose le lien « 📖 Lexique » dans
  `<nav id="navharm">`, seulement si la page existe (règle n°183 : pas de
  bouton vers le vide).
- `tests_generer_lexique.py` est le banc de l'outil ; on ne touche pas au
  script sans le repasser.

## Entrées attendues

- La séquence HTML complète (ouverture, tous les panneaux `#sN`, Bonus, Bilan),
  le QCM (30 questions fixes) et les synthèses du lot.
- Le niveau (5e, 4e, 3e) : le seuil de « mot difficile » n'est pas le même.
- Le `vocabulaire_<lot>.json` existant, s'il y en a un : on le complète, on
  n'écrase pas (règle n°66, on ouvre le dossier avant d'y écrire).

## Procédure

### 1. Relever — deux passes, pas une
**Passe technique** : tout terme du référentiel ou du métier présent dans la
page (capteur, actionneur, chaîne d'énergie, contrainte, fonction d'usage,
cahier des charges, bête à cornes, diagramme pieuvre, algorithme, variable,
boucle, très basse tension…).

**Passe lisibilité** : tout mot que l'on croit connu et qui ne l'est pas
forcément — innovation, évolution, usage, besoin, performant, autonome,
prototype, norme, dispositif, optimiser, simuler, caduc. En cas de doute, le
mot entre : une définition en trop ne coûte rien, un mot bloquant coûte la
séance.

Ne pas relever : les mots de la langue courante vraiment transparents ; les
noms propres déjà expliqués dans la situation ; les mots que la situation
glose déjà dans la phrase (décisions des 05 et 06/11/2026 : « on l'entend
claquer », « l'électrovanne, la vanne qui s'ouvre à l'électricité ») — ceux-là
peuvent quand même entrer au vocabulaire s'ils reviennent dans une séance.

### 2. Classer chaque mot dans sa zone — l'outil le vérifie
- `"seance": "ouverture"` : le mot figure dans la zone **avant** la barre
  d'onglets (Avant de commencer, situation, problématique). Les quatre mots
  de base y vont par renvoi au commun : `{"mot": "objet technique",
  "commun": true, "exemple": "…", "seance": "ouverture"}`.
- `"seance": "sN"` : la **première** séance dont le panneau `#sN` contient une
  des `formes` du mot (accents et casse ignorés ; le texte des `<script>` et
  `<style>` ne compte pas).
Un mot absent de sa zone fait refuser tout le lot (sortie ≠ 0, lexique non
écrit) : relire le panneau avant d'écrire la ligne.

### 3. Définir — en langage élève, sourcé, jamais en langage référentiel
Chaque entrée : `{"mot", "formes": [...], "seance", "definition", "source"}`.
- **Une ou deux phrases** lisibles par un élève de 6e, avec un exemple pris
  dans la séquence (lampadaire, jardin connecté, station cyclonique, vélo-
  cargo…). Modèles de ton : les synthèses de Pascal Pujades, celles des
  académies de Limoges et de Bordeaux ; règle n°316 pour le niveau de langue.
- **Toujours une source** : TLFi (CNRTL), guide Éduscol STI mai 2024, BO n°9
  du 29/02/2024, ou l'atelier des représentations du dépôt qui a déjà défini le
  mot (forme déjà employée en 5e_C2.1 : « l'atelier des représentations
  « Le besoin » (5e), « Les mots de cet exercice » »). Sans source, refus.
- Les quatre mots de la méthode APTE (utilisateur, matière d'œuvre, produit,
  fonction) sont des **références** (décision du 05/11/2026) : même définition
  d'un lot à l'autre, copiée depuis le lot qui l'a écrite en premier, source
  reprise.
- `formes` liste singulier, pluriel, féminin, et la forme verbale si elle
  apparaît (« claque », « claquer »).
- Jamais de définition circulaire ; jamais de renvoi au programme dans la
  page élève (règle n°298).

### 4. Ne pas contredire le QCM
Un mot qui est aussi une **notion** d'une question du QCM doit porter
**exactement** le « à retenir » de cette question, sinon l'outil refuse (deux
vérités pour un mot). Deux issues : copier le « à retenir » dans la
définition, ou corriger le « à retenir » du QCM si c'est lui qui est obscur
(et repasser les contrôles du QCM, skill `qcm-html-accessible`).

### 5. Engendrer, câbler, contrôler
```bash
python3 _outils/generer_lexique.py <dossier du lot>          # sortie 0, aucun REFUSÉ
python3 _outils/poser_lien_lexique.py --etat                 # dit où le lien manque
python3 _outils/poser_lien_lexique.py --theme <dossier du thème>
```
Dans la séquence, la première occurrence d'un mot de séance peut renvoyer à
`lexique_<lot>.html#seance-sN` ; celle d'un mot de base à `#ouverture`. Les
liens restent relatifs (règle n°305, page lisible hors ligne).

### 6. Harmoniser avec les synthèses
Les synthèses élève et professeur reprennent les définitions du vocabulaire
**mot pour mot** ; la synthèse professeur peut ajouter la formulation du
référentiel en dessous, pas la page élève.

## Contrôles avant livraison

- [ ] Chaque terme du référentiel présent dans la page a son entrée.
- [ ] Chaque mot de la passe lisibilité en a une (en cas de doute : dedans).
- [ ] Chaque entrée : `formes` complètes, `seance` exacte, `definition` courte avec exemple, `source` non vide.
- [ ] Mots de base par renvoi au commun (`"commun": true`), jamais redéfinis.
- [ ] Mots APTE identiques aux autres lots.
- [ ] `generer_lexique.py` : sortie 0, zéro REFUSÉ ; `tests_generer_lexique.py` intact.
- [ ] Lien « 📖 Lexique » posé par `poser_lien_lexique.py`, vérifié depuis l'index publié.
- [ ] Synthèses : mêmes définitions ; aucune formulation « référentiel » ni commentaire de conception dans la page élève.
- [ ] Lexique imprimable sans page quasi vide (contrôle `controle_impression`).

## Ce que ce skill ne fait pas

- Il ne modifie pas `generer_lexique.py` ni son banc.
- Il ne rédige pas les synthèses : `synthese-vulgarisee` (règle n°316).
- Il ne produit pas de fiche de connaissances séparée : la structuration va
  dans la synthèse élève, pas dans un troisième document.
- Il ne tranche pas un mot limite : en cas de doute il l'inclut, et Pascal
  retire ce qu'il juge superflu.
