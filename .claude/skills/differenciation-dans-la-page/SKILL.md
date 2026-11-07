---
name: "differenciation-dans-la-page"
description: "Ajoute la différenciation à une séquence du dépôt en-ligne-pour-le-cycle-4 sans créer trois pages : aides à deux niveaux repliées, Bonus outillé pour les rapides, critères de réussite gradués sur les quatre niveaux LSU, versions 🅰/🅱/🅲 (matériel réel TBT / simulation / sans matériel). À utiliser sur une séquence existante ou en fin de rédaction d'un lot."
---

# Différenciation dans la page

Origine : idée n°9 de la liste Grok du 07/11/2026 (« trois versions :
soutien, standard, approfondissement »), **refusée telle quelle** : trois
pages pour une séquence, c'est trois pages à maintenir, trois fois les
captures, trois fois les contrôles, et un élève étiqueté par l'URL qu'on
lui donne. Dans ce dépôt, la différenciation vit **dans la page unique**,
avec les outils que les règles d'or imposent déjà : aides à deux niveaux,
Bonus, critères gradués, versions 🅰/🅱/🅲.

Le skill externe `k12-lesson-differentiation` nourrit le fond
(stratégies) ; la forme suit ce document et le journal (règle n°10).

## Avant tout : le journal fait foi

`main` du jour, journal lu. Si une règle d'or postérieure fixe la forme des
aides, du Bonus ou de l'auto-positionnement, elle l'emporte.

## Entrées attendues

- La séquence HTML (toutes séances), son QCM et ses synthèses.
- Pour chaque activité : l'objectif, la compétence, la production attendue.
- Le matériel réellement disponible (`_ressources-communes/` guides
  matériels, fiche matériel de classe de Pascal).

## Les quatre leviers — tous dans la même page

### Levier 1 — Aides à deux niveaux, repliées (règle n°4 / exercice vivant)
Chaque activité porte deux aides, chacune dans un `<details>` fermé :
- **Aide 1 — un coup de pouce** : reformule la consigne, montre où regarder,
  rappelle le mot du lexique. Ne donne pas la méthode.
- **Aide 2 — la méthode** : la démarche étape par étape, sans la réponse.
L'ouverture d'une aide est tracée (`window.__exp.aides`) : le vérificateur
ne la pénalise pas, mais la synthèse professeur sait combien d'élèves en ont
eu besoin. La correction complète reste un troisième volet, repliée,
visible après vérification seulement.

### Levier 2 — Bonus outillé pour les rapides (règles n°4, 301, 306)
Un seul bloc « 🎁 Bonus (facultatif — hors parcours obligatoire) », à la
dernière séance, avant le Bilan. Il **approfondit**, il ne rallonge pas :
une variante de l'objet, une contrainte en plus, un cas limite. Il a ses
champs de réponse sauvegardés et son corrigé. Jamais de Bonus « lis cette
page en plus ».

### Levier 3 — Critères de réussite gradués sur les quatre niveaux LSU
Chaque activité affiche son critère de réussite (règle de l'exercice vivant)
**sous forme graduée**, avec l'échelle de référence du dépôt (décision du
23/10/2026) : maîtrise insuffisante · fragile · satisfaisante · très bonne
maîtrise. L'élève voit où il en est, pas seulement « juste / faux ». Le
Bilan reprend la même échelle pour l'auto-positionnement par code ; le bloc
« Où j'en suis » se replie dès la séance 2 comme le reste de l'ouverture
(règle n°311, vague du 04/11/2026).

Formulation : un verbe observable par niveau, sur la même production.
Exemple (chaîne d'énergie) : *insuffisante* : place les blocs sans ordre ·
*fragile* : ordonne les blocs, oublie les formes d'énergie · *satisfaisante* :
blocs et énergies justes, une fonction absente non justifiée · *très bonne* :
tout juste, fonction absente en pointillés avec sa raison (règle n°131).

### Levier 4 — Versions 🅰/🅱/🅲 (règle n°3)
Quand l'activité manipule : 🅰 matériel réel (très basse tension
uniquement, le 230 V nommé comme interdit) · 🅱 simulation intégrée (pour la
programmation : l'éditeur Python intégré à la page, décision du 05/11/2026,
le code coloré façon IDE, règle n°13) · 🅲 sans matériel (cahier, papier,
captures réelles, règle n°308). Les trois versions mènent à la **même
production** et au **même vérificateur**. L'élève ou le professeur choisit
par un groupe de boutons radio dans un `<fieldset>` (règle n°300), le choix
est sauvegardé. Une version 🅰 peut être un logiciel quand c'est l'outil réel
du métier (5e_C8.1, 05/11/2026).

## Ce qu'on ne fait pas

- Pas de page « soutien » ni de page « approfondissement » séparées.
- Pas de consigne simplifiée qui change l'objectif : on simplifie l'accès,
  pas la compétence visée.
- Pas de commentaire pédagogique dans la page élève (« cette aide est
  prévue pour… ») : décision d'octobre 2026, charge cognitive inutile. Ces
  remarques vont dans la synthèse professeur.
- Pas d'allongement de la séance : les 55 minutes restent remplies, pas
  débordées ; le chronométrage indicatif est revu après ajout des aides.

## Procédure

1. Lister les activités et, pour chacune, écrire les deux aides, le critère
   gradué, et décider si 🅰/🅱/🅲 s'applique.
2. Rédiger le Bonus unique de clôture et son corrigé.
3. Injecter dans la page : `<details class="aide" data-niveau="1|2">`,
   `<fieldset class="version">`, bloc `critere` à quatre lignes.
4. Mettre à jour la synthèse professeur : où les aides sont attendues, quels
   élèves viser avec le Bonus, lecture des traces `__exp.aides`.
5. Passer la suite Playwright du lot (sauvegarde des choix, zéro erreur JS)
   puis `_outils/controle_squelette.mjs`.
6. Capture avant/après à 390 px pour toute activité dont un champ de réponse
   change de forme (pilier 2, point 6).

## Contrôles avant livraison

- [ ] Deux aides par activité, repliées, sans réponse dans l'aide.
- [ ] Un seul Bonus, en clôture, avec champs sauvegardés et corrigé.
- [ ] Critère gradué sur quatre niveaux LSU pour chaque activité ; même échelle au Bilan.
- [ ] Versions 🅰/🅱/🅲 → même production, même vérificateur ; 230 V nommé interdit.
- [ ] Aucun commentaire pédagogique dans la page élève.
- [ ] Durée de séance inchangée, chronométrage indicatif mis à jour.
- [ ] Tests exécutés réellement et listés dans le rapport (règle n°299).
- [ ] Captures 390 px jointes à la PR si un champ a changé de forme.

## Ce que ce skill ne fait pas

- Il ne crée pas d'activité nouvelle : `sequence-pedagogique-engageante`.
- Il ne rédige pas les synthèses : il y ajoute les remarques de
  différenciation.
- Il ne décide pas du matériel disponible : `arduino-grove-college` et la
  fiche matériel de Pascal.
