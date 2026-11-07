---
name: "mutualisation-couverture"
description: "Analyse une séquence ou un ensemble de ressources du dépôt en-ligne-pour-le-cycle-4 pour repérer les codes du référentiel non couverts, les doublons, et proposer des mutualisations (un dossier principal COMPLET ET VALIDABLE, les autres codes COUVERT + README pointeur). Complète audit-couverture-cycle4 par une revue qualitative. À utiliser avant de lancer un nouveau lot ou lors d'un audit général."
---

# Mutualisation et couverture

Origine : idée n°14 de la liste Grok du 07/11/2026, branchée sur
`audit-couverture-cycle4` (matrice des 114 codes), sur les statuts d'audit
du dépôt et sur les décisions de Pascal (priorité au thème 1 et à la
compétence C1 en septembre 2026, séquences mutualisées déjà existantes).

`audit-couverture-cycle4` compte ; ce skill **juge** : il dit si la
couverture déclarée est réelle, où un même objet pourrait servir deux
codes, et ce qu'il manque pour qu'un dossier passe de COUVERT à COMPLET.

## Avant tout : le journal fait foi (règle n°10)

1. `main` du jour, journal lu, registre des règles d'or consulté.
2. Régénérer l'audit sur un arbre à jour : `python _outils/build_audit.py`
   (jamais éditer `audit_couverture.*` à la main).
3. Lire `_outils/heritees.json` : une héritée avec badge 🛠 n'est pas une
   couverture définitive (règle n°12).

## Entrées attendues

- Le périmètre : un thème, un niveau, une compétence (C1 à C9) ou tout le
  dépôt.
- La matrice `audit_couverture.*` fraîchement régénérée.
- Les classeurs `_progressions/<niveau>/` : ce qui est **programmé dans
  l'année** compte plus que ce qui existe sur le site.
- Les contraintes de Pascal du moment (journal) : ordre de priorité, objets
  imposés, décisions d'octobre 2026 (diagramme pieuvre en C2, vélo-cargo en
  5e_C2.1, etc.).

## Procédure

### 1. Lire la couverture déclarée — puis la vérifier
Pour chaque code du périmètre, noter le statut : COMPLET ET VALIDABLE ·
COUVERT (+ README pointeur) · HÉRITÉE 🛠 · ABSENT.

Un code COUVERT par mutualisation n'est accepté que si, dans la séquence
principale, **au moins une activité avec vérificateur** et **au moins deux
questions du QCM** portent réellement sur ce code. Sinon il est reclassé
« déclaré sans preuve » : règle n°299, un contrôle qui n'a rien vérifié
n'est pas vert.

### 2. Chercher les doublons
Deux séquences du même niveau traitent-elles le même code avec le même
objet et la même problématique ? Si oui :
- garder celle qui respecte le squelette n°306 et le volet Rappel n°311 ;
- proposer l'archivage de l'autre dans `_archive-anciennes-versions/`
  **dans le même commit** que le recâblage (règle n°12, jamais de
  suppression), après lecture et récupération de ce qui vaut (règle n°66).

### 3. Proposer des mutualisations — sur trois critères, tous les trois
Une mutualisation n'est proposée que si :
1. **Même objet-fil** (lampadaire 5e, jardin 4e, station 3e, ou objet fixé au
   journal) : le même objet se décrit, se programme, se dépanne.
2. **Même séance ou séance contiguë** dans le classeur de progression : on ne
   mutualise pas deux codes enseignés à quatre mois d'écart.
3. **Une activité peut porter les deux codes sans grossir** : si la
   mutualisation ajoute plus d'une activité à la séquence, c'est un
   nouveau lot, pas une mutualisation.

Pour chaque proposition, nommer le **dossier principal** (COMPLET ET
VALIDABLE) et les **dossiers pointeurs** (COUVERT), et écrire le texte du
README pointeur.

### 4. Lister les manques, dans l'ordre utile
Les codes ABSENT sont classés par :
1. date de passage dans le classeur de progression (le plus proche d'abord) ;
2. priorité déclarée par Pascal au journal ;
3. possibilité d'adossement à un lot existant (moins cher qu'un lot neuf).

Chaque manque reçoit une recommandation : « lot neuf », « adosser à <code> »
ou « sortir l'héritée de 🛠 ».

### 5. Ne jamais recommander de « spirale »
Pascal change de collège chaque année ; aucun élève n'a fait ses séquences
précédentes. Une progression 5e → 4e → 3e qui suppose des acquis des années
passées n'a pas de sens ici. Chaque séquence doit se suffire (règle n°304 :
compétences attendues + moyen de les rattraper).

## Format de sortie

Un fichier `RAPPORT_MUTUALISATION_<perimetre>_<date>.md`, déposé par
branche transversale `fable/<slug>` (règle n°302), avec ces sections dans
cet ordre :

1. **Résumé en cinq lignes** : nb de codes du périmètre, COMPLET, COUVERT
   vérifiés, COUVERT sans preuve, ABSENT.
2. **Couvertures sans preuve** (tableau : code · séquence · ce qui manque).
3. **Doublons** (paire · laquelle garder · motif · recâblages à faire).
4. **Mutualisations proposées** (tableau : codes · objet · séance · dossier
   principal · pointeurs · texte README).
5. **Manques, triés** (code · date classeur · recommandation).
6. **Décisions attendues de Pascal** : liste à cocher, une ligne par choix.
   Rien n'est exécuté avant la fusion de sa réponse au journal.

## Contrôles avant livraison

- [ ] Audit régénéré sur un arbre à jour avant toute lecture.
- [ ] Chaque COUVERT accepté a son activité vérifiée et ses deux questions QCM.
- [ ] Aucune suppression proposée : archivage + recâblage, même commit.
- [ ] Chaque mutualisation remplit les trois critères, pas deux.
- [ ] Manques triés par date de classeur, pas par numéro de code.
- [ ] Zéro proposition fondée sur des acquis « de l'année précédente ».
- [ ] Rapport livré par branche `fable/<slug>`, entrée au journal thème par thème (règle n°307).

## Ce que ce skill ne fait pas

- Il ne modifie aucune séquence : il produit un rapport et des décisions à
  prendre.
- Il ne remplace pas `audit-couverture-cycle4` : il part de sa matrice.
- Il ne remplit pas les classeurs `_progressions/` : banc d'essai obligatoire
  sur copie avant tout script (pilier 2, point 7).
