---
name: chaine-energie-fonctionnelle
description: Dessiner ou corriger tout schéma de chaîne d'énergie du dépôt selon la règle d'or n°310 — fonctions (verbes) dans les blocs, composants dessous, formes d'énergie sur les flèches, entrée et sortie, énergie stockée annotée sous son composant, et la convention « information en haut, énergie en bas, l'ordre descend » conservée. À utiliser dès qu'un schéma, un SVG, un QCM illustré ou une consigne montre une chaîne d'énergie (lampadaire, jardin, station, Book Train, vélo-cargo, TP).
---

# Chaîne d'énergie fonctionnelle (règle d'or n°310)

Mis à jour le 23/10/2026 (inventaire des skills) : aligné sur le journal jusqu'à la règle d'or n°311.

> **Règle d'or n°310 (21/10/2026).** Dans une chaîne d'énergie, les blocs disent ce qui est fait, les flèches disent ce qui circule.
> Les blocs portent les fonctions techniques, avec un verbe ; sous chaque bloc, le composant qui la réalise ; les formes
> d'énergie sur les flèches, entre les blocs, à l'entrée et à la sortie ; l'action finale à la sortie ; une énergie stockée
> s'annote sous son composant.
> **Vocabulaire fixe des fonctions : ALIMENTER (STOCKER pour la batterie), DISTRIBUER, CONVERTIR, TRANSMETTRE.**
> Source : Éduscol STI, *La chaîne d'énergie*.

Elle **s'ajoute** à la convention de la technologie, qui reste en vigueur : **l'information EN HAUT, l'énergie EN BAS, l'ordre
qui descend** (la disposition montre qui commande). Une chaîne d'énergie seule n'a pas de chaîne d'information à placer
au-dessus : la convention ne s'applique alors qu'à l'ordre de lecture (gauche → droite).

## Vocabulaire fixe des fonctions (aucun autre verbe dans un bloc)

| Bloc | Ce qu'il dit | Où va la précision (sous le bloc) |
|---|---|---|
| **ALIMENTER** | fournir l'énergie au reste de la chaîne | batterie (le bloc s'appelle alors **STOCKER**, avec « Énergie chimique stockée » dessous), alimentation secteur, USB, **régulateur de charge**, **convertisseur 12 V → 5 V** |
| **DISTRIBUER** | acheminer et commander l'énergie vers les récepteurs | interrupteur électronique, relais, pont en H, sortie de la carte, **électrovanne** (ouvre ou ferme le passage) |
| **CONVERTIR** | changer la forme de l'énergie | panneau solaire, moteur, pompe (électrique → mécanique : l'eau est mise en mouvement), LED, buzzer |
| **TRANSMETTRE** | acheminer et adapter un mouvement | réducteur, courroie, crémaillère |

**Interdits dans un bloc** : RÉGULER, ADAPTER, OUVRIR / FERMER, STOCKER / ALIMENTER, et tout verbe d'une autre liste. « Réguler la charge »,
« adapter la tension » et « ouvrir ou fermer » sont des **précisions** : elles s'écrivent sous le bloc (ALIMENTER : régulateur de charge ;
ALIMENTER : convertisseur 12 V → 5 V ; DISTRIBUER : électrovanne). Pour la chaîne d'information, les verbes restent ACQUÉRIR, TRAITER, COMMUNIQUER.
`verifier_chaines_energie.py` refuse tout autre texte dans un bloc de fonction.

## Ce que porte chaque élément

| Élément | Il contient | Il ne contient jamais |
|---|---|---|
| **Bloc** | une fonction du vocabulaire fixe, en majuscules, à l'infinitif : ALIMENTER, DISTRIBUER, CONVERTIR, TRANSMETTRE ; STOCKER pour une batterie | un nom de composant, une précision de fonction, une forme d'énergie |
| **Sous le bloc** | le composant qui réalise la fonction (« Moteur dans le moyeu arrière »), et la précision utile (« Régulateur de charge », « Pont en H, carte séparée ») | un verbe de fonction |
| **Sur la flèche** | la forme d'énergie qui circule : électrique, mécanique, lumineuse, hydraulique, sonore, chimique… | un composant |
| **Entrée** | une flèche étiquetée qui arrive au premier bloc (« Énergie lumineuse » vers le panneau) ; la source est nommée si utile | — |
| **Sortie** | une flèche étiquetée qui quitte le dernier bloc, **puis l'action finale écrite en gras** (« Éclairer la zone », « Déplacer le vélo et sa charge ») | — |
| **Énergie stockée** | l'annotation « Énergie chimique stockée », **sous le composant** (la batterie), en jaune ; ce n'est pas une flèche | — |

## Pièges déjà rencontrés (ne pas les refaire)

1. **La batterie n'est pas sur le trajet principal.** Dans un montage solaire, panneau → *régulateur de charge* → distribution ;
   la batterie est une **branche** reliée au régulateur, avec une double flèche « Énergie électrique — Charge / décharge ».
   Placer la batterie avant la régulation est une erreur technique, pas une variante de dessin.
2. **Une fonction n'est pas une forme d'énergie.** « Électrique » ne va jamais dans un bloc ; « CONVERTIR » ne va jamais sur
   une flèche. Les trois mélanges (fonction / composant / énergie dans le même bloc) sont ce que la règle corrige.
3. **Fonction absente** (pas de TRANSMETTRE si rien ne se déplace) : ne jamais inventer un bloc plein « pour faire complet ».
   **La dessiner en pointillés, grisée, avec sa raison écrite à côté** (règle d'or n°131, 26/08/2026 ; confirmé par Pascal le
   23/10/2026). ⚠️ Pas encore appliqué partout : le générateur (station 3e_C9.2 : « Pas de transmission mécanique séparée
   nécessaire ») et la page station 1 de 3e_C9.2 (« TRANSMETTRE est absent parce que rien ne se déplace ») l'écrivent en une
   phrase, sans bloc — à mettre en conformité par un lot du thème 2 (générateur, `_outils/`) puis du thème 3 (page).
   La n°310 a déjà remplacé la n°131 sur un autre point : la flèche d'ordre n'arrive plus « sur le convertisseur quand la puissance est
   faible », elle arrive **toujours sur DISTRIBUER** (piège 5 ; reprise du 21/10/2026 au journal).
4. **L'eau n'est pas de l'énergie.** Un circuit de matière (eau) se dessine à part, d'une couleur distincte, avec ses propres
   flèches. La pompe convertit l'énergie électrique en énergie **mécanique** (« l'eau est mise en mouvement »), pas hydraulique
   (décision de Pascal du 21/10/2026, n°4 de la reprise au journal).
5. **L'ordre arrive toujours sur DISTRIBUER.** Le préactionneur — sortie de la carte, transistor intégré au module (buzzer Grove) ou carte
   séparée (relais, pont en H) — se dit **sous le bloc DISTRIBUER**, jamais en déplaçant la flèche (planche des trois cas de 3e_C9.2).
6. **Le même composant peut apparaître dans deux chaînes** (le voyant convertit de l'énergie, et communique une information) :
   le dire, ne pas le dédoubler en deux composants.
7. **L'étiquette d'une flèche se place à côté d'elle, jamais dessus ni sous un autre bloc** : sur un trait vertical, l'étiquette
   commence à droite du trait (`lanchor='start'` dans le générateur).
8. **Un bandeau de cinq blocs ne tient pas sur une ligne à 390 px** : prévoir une disposition large (une ligne) et une disposition
   étroite (une colonne), choisies selon la largeur affichée ; ne jamais descendre sous 10 px à l'écran.

## Comment le faire

1. **Le générateur d'abord.** `_outils/regenerer_chaines_energie.py` écrit six figures : lampadaire (`5e_C4.1`), jardin (`4e_C4.1`),
   chaîne à élaborer (`3e_C4.1`), station et planche des trois cas (`3e_C9.2`), Book Train (`4e_C4.1_book-train`, figure de la page
   et QCM compris). Classe `Diagram` : `block(x, y, fonction, composant, couleur, stock=…)`, `arrow(points, couleur, étiquette, …)`,
   `section(…)`, `text(…)`. Il écrit aussi la **source draw.io** (`_generation/chaines_energie/`, `fichiers_drawio/` pour le Book Train).
   Le vélo-cargo a son propre générateur (`5e_C3.1/_generation/figure_iso_velo_cargo/`). Ne jamais éditer un SVG produit :
   modifier le générateur, relancer. Tout autre schéma est fait main : voir la liste ci-dessous.
2. **Couleurs** (les mêmes partout) : ALIMENTER `#ffd66b` · DISTRIBUER `#61dafb` · CONVERTIR `#c68ef2` · TRANSMETTRE `#81fba1` ;
   flux d'énergie en orange `#ffb454`, d'information en cyan `#61dafb`, ordre en vert pointillé `#81fba1`. La couleur ne porte
   jamais une information que le texte ne porte pas : le schéma se lit en niveaux de gris.
3. **Textes natifs** (`<text>`, jamais `foreignObject`), `<title>` et `<desc>` qui nomment les blocs, les flèches et la
   convention (« En haut… En bas… l'ordre descend »), aucun fichier ni police distante, fond blanc à l'impression.
4. **Titre du schéma** : il dit la convention quand il y a deux chaînes (« …l'information (en haut) commande l'énergie (en bas) »),
   et chaque chaîne porte son repère (« en haut (elle décide) », « en bas (elle obéit) »). Le pied de schéma la rappelle.
5. **Les textes qui accompagnent** (alt, description détaillée, légende, consignes, corrigés, QCM illustré) suivent le schéma :
   mêmes fonctions, mêmes composants, mêmes énergies. Un QCM dont l'énoncé change **change aussi sa bonne réponse** : le dire
   dans le journal, liste avant / après.

## Vérifier

```
python _outils/regenerer_chaines_energie.py     # écrit les six figures, les sources draw.io, la figure et le QCM du Book Train
python _outils/verifier_chaines_energie.py      # textes dans le cadre, énergies hors des blocs, convention dite ET dessinée, impression, objets HTML, scène 6
```

Puis les contrôles du dépôt (dont `controle_regles_visibles.py`, règle n°309 : aucune trace de la fabrique dans un texte lu par
l'élève — ni « règle n°310 » dans un schéma ou une légende) et les bancs des séquences touchées.

Limite de `verifier_chaines_energie.py` : il cherche chaque nom avec `next(ROOT.glob('theme-*/**/Images/'+nom))` et ne contrôle
donc que le **premier** fichier trouvé. Deux fichiers portent le nom `chaines_jardin_connecte.svg` (`4e_C4.1`, généré, et `4e_C9.1`,
fait main) : seul celui de `4e_C4.1` est vérifié. Il ne voit pas non plus les schémas faits main ci-dessous.

## Schémas faits main encore non conformes (relevé du 23/10/2026)

Vérifiés fichier par fichier. Les autres SVG du dépôt qui dessinent une chaîne d'énergie sont produits par un générateur.

- `theme-3-…/C9-…/4e/4e_C9.1/Images/chaines_jardin_connecte.svg` (séquence et QCM `4e_C9_jardin-programme`) : aucune forme
  d'énergie sur les flèches, ni entrée ni sortie ; TRANSMETTRE justifié par « quelque chose SE DÉPLACE — l'eau » (piège 4), alors
  que le jardin généré n'a pas de TRANSMETTRE ; le texte du schéma fait arriver l'ordre sur CONVERTIR pour un voyant (piège 5).
- `theme-2-…/C6-…/4e/4e_C6.2/Images/schema_chaines_arrosage.svg` (séquence `jardin-connecte-arrosage-automatique`) : bloc
  « AGIR » (verbe hors vocabulaire ; l'action va à la sortie, hors chaîne) ; « COMMANDER » ajouté à la chaîne d'information ;
  TRANSMETTRE = « Circulation de l'eau » (piège 4) ; composant en gros et fonction en petit dans le bloc ; aucune énergie sur les
  flèches ; ni `<title>` ni `<desc>`.
- `theme-3-…/C9-…/5e/5e_C9.1/Images/barriere_cyclone_condition.svg` (séquence, QCM et synthèse élève `5e_C9.1`) : blocs
  « MOTEUR » et « BARRIÈRE » (des composants, pas des fonctions) ; la barrière, qui est l'action, dessinée dans la chaîne (cas
  déjà relevé par la règle d'or n°123, 21/08/2026) ; pas de DISTRIBUER : l'ordre descend sur le moteur ; aucune énergie sur les flèches.

Pour les corriger : les faire entrer dans le générateur (nom de fichier distinct pour le jardin de `4e_C9.1`), puis ajuster alt,
descriptions, consignes, corrigés et QCM (étape 5). Ce lot de skills ne les modifie pas.

## Ce que cette règle ne couvre pas

La justesse technique d'un composant précis (à vérifier dans la documentation du matériel) ; le choix du niveau de détail
selon la classe ; les schémas de chaîne d'**information** seule (règle n°6 et gabarit des chaînes).
