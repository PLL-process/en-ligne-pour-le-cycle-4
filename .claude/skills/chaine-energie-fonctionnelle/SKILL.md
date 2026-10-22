---
name: chaine-energie-fonctionnelle
description: Dessiner ou corriger tout schéma de chaîne d'énergie du dépôt selon la règle d'or n°310 — fonctions (verbes) dans les blocs, composants dessous, formes d'énergie sur les flèches, entrée et sortie, énergie stockée annotée sous son composant, et la convention « information en haut, énergie en bas, l'ordre descend » conservée. À utiliser dès qu'un schéma, un SVG, un QCM illustré ou une consigne montre une chaîne d'énergie (lampadaire, jardin, station, Book Train, vélo-cargo, TP).
---

# Chaîne d'énergie fonctionnelle (règle d'or n°310)

> **Règle d'or n°310.** Dans une chaîne d'énergie, les blocs disent ce qui est fait, les flèches disent ce qui circule.
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
3. **Ne pas dessiner un bloc absent « pour faire complet »** (pas de TRANSMETTRE si rien ne se déplace) : le dire en une phrase.
4. **L'eau n'est pas de l'énergie.** Un circuit de matière (eau) se dessine à part, d'une couleur distincte, avec ses propres
   flèches ; l'énergie hydraulique est la forme à la sortie de la pompe.
5. **L'ordre arrive toujours sur DISTRIBUER.** Le préactionneur — sortie de la carte, transistor intégré au module (buzzer Grove) ou carte
   séparée (relais, pont en H) — se dit **sous le bloc DISTRIBUER**, jamais en déplaçant la flèche (planche des trois cas de 3e_C9.2).
6. **Le même composant peut apparaître dans deux chaînes** (le voyant convertit de l'énergie, et communique une information) :
   le dire, ne pas le dédoubler en deux composants.
7. **L'étiquette d'une flèche se place à côté d'elle, jamais dessus ni sous un autre bloc** : sur un trait vertical, l'étiquette
   commence à droite du trait (`lanchor='start'` dans le générateur).
8. **Un bandeau de cinq blocs ne tient pas sur une ligne à 390 px** : prévoir une disposition large (une ligne) et une disposition
   étroite (une colonne), choisies selon la largeur affichée ; ne jamais descendre sous 10 px à l'écran.

## Comment le faire

1. **Le générateur d'abord.** Les schémas des séquences de thème 2 et 3 sont écrits par `_outils/regenerer_chaines_energie.py`
   (classe `Diagram` : `block(x, y, fonction, composant, couleur, stock=…)`, `arrow(points, couleur, étiquette, …)`,
   `section(…)`, `text(…)`), qui écrit aussi la **source draw.io** de chaque schéma. Le vélo-cargo a son propre générateur
   (`5e_C3.1/_generation/figure_iso_velo_cargo/`). Ne jamais éditer un SVG produit : modifier le générateur, relancer.
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
python _outils/regenerer_chaines_energie.py     # écrit les cinq schémas, les sources draw.io, la figure du Book Train
python _outils/verifier_chaines_energie.py      # textes dans le cadre, énergies hors des blocs, convention dite ET dessinée, impression, objets HTML, scène 6
```

Puis les contrôles du dépôt (dont `controle_regles_visibles.py`, règle n°309 : aucune trace de la fabrique dans un texte lu par
l'élève — ni « règle n°310 » dans un schéma ou une légende) et les bancs des séquences touchées.

## Ce que cette règle ne couvre pas

La justesse technique d'un composant précis (à vérifier dans la documentation du matériel) ; le choix du niveau de détail
selon la classe ; les schémas de chaîne d'**information** seule (règle n°6 et gabarit des chaînes).
