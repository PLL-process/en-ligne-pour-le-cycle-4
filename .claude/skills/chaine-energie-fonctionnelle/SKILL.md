---
name: chaine-energie-fonctionnelle
description: Dessiner ou corriger tout schéma de chaîne d'énergie du dépôt selon la règle d'or n°310 — fonctions (verbes) dans les blocs, composants dessous, formes d'énergie sur les flèches, entrée et sortie, énergie stockée annotée sous son composant, et la convention « information en haut, énergie en bas, l'ordre descend » conservée. À utiliser dès qu'un schéma, un SVG, un QCM illustré ou une consigne montre une chaîne d'énergie (lampadaire, jardin, station, Book Train, vélo-cargo, TP).
---

# Chaîne d'énergie fonctionnelle (règle d'or n°310)

Mis à jour le 23/10/2026 (inventaire des skills) : aligné sur le journal jusqu'à la règle d'or n°311. Mis à jour le 29/10/2026 :
les trois schémas faits main (4e_C9.1, 4e_C6.2, 5e_C9.1) sont entrés dans le générateur ; le générateur dessine la fonction absente.
Mis à jour le 15/11/2026 : **tous les flux sont animés** (demande de Pascal), voir « Les flux animés » plus bas.
Mis à jour le 16/11/2026 : **les formes d'énergie sont celles du programme 2024** (SFC 11, connaissances : « électrique,
cinétique, potentielle, thermique, lumineuse ») — **cinétique**, plus mécanique, à la sortie d'un moteur, d'une pompe, d'une
électrovanne (décision de Pascal) ; voir « Les formes d'énergie » plus bas.

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
| **CONVERTIR** | changer la forme de l'énergie | panneau solaire, moteur, pompe (électrique → cinétique : l'eau est mise en mouvement), LED, buzzer |
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
| **Sur la flèche** | la forme d'énergie qui circule, avec les mots du programme : électrique, cinétique, potentielle, thermique, lumineuse ; chimique (une pile, une batterie) et sonore quand il le faut | un composant ; « mécanique » (voir plus bas) |
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
   23/10/2026). Le générateur la dessine avec `Diagram.absent(x, y, 'TRANSMETTRE', 'Absente : …')` (29/10/2026 : jardin de
   4e_C9.1, arrosage de 4e_C6.2). ⚠️ Pas encore appliqué partout : la figure station de 3e_C9.2 (« Pas de transmission
   mécanique séparée nécessaire ») et la page station 1 de 3e_C9.2 (« TRANSMETTRE est absent parce que rien ne se déplace »)
   l'écrivent en une phrase, sans bloc.
   La n°310 a déjà remplacé la n°131 sur un autre point : la flèche d'ordre n'arrive plus « sur le convertisseur quand la puissance est
   faible », elle arrive **toujours sur DISTRIBUER** (piège 5 ; reprise du 21/10/2026 au journal).
4. **L'eau n'est pas de l'énergie.** Un circuit de matière (eau) se dessine à part, d'une couleur distincte, avec ses propres
   flèches. La pompe convertit l'énergie électrique en énergie **cinétique** (« l'eau est mise en mouvement ») — ni hydraulique, ni mécanique depuis le 16/11/2026
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

1. **Le générateur d'abord.** `_outils/regenerer_chaines_energie.py` écrit neuf figures : lampadaire (`5e_C4.1`), jardin (`4e_C4.1`),
   chaîne à élaborer (`3e_C4.1`), station et planche des trois cas (`3e_C9.2`), Book Train (`4e_C4.1_book-train`, figure de la page
   et QCM compris), et depuis le 29/10/2026 le jardin programmé (`4e_C9.1`, `chaines_jardin_programme.svg` — nom distinct de celui
   de `4e_C4.1`), l'arrosage (`4e_C6.2`) et la barrière du Cyclone (`5e_C9.1`, avec son banc de tests).
   `python _outils/regenerer_chaines_energie.py jardin_programme` ne produit que la figure nommée (noms dans `FIGURES`).
   Depuis le 15/11/2026, `book_deux_chaines` : les deux chaînes du Book Train en **disposition étroite** (l'information en
   haut sur une ligne, l'énergie en colonne, composants à gauche des blocs : `block(…, cpos='left', csize=20)`), en deux
   versions — muette sur les énergies pour les questions, complète pour la correction (n°331). `incruster(html, svg,
   marqueur)` pose une figure en ligne dans chaque `<figure data-chaines="marqueur" data-prefixe="P">` d'une page, id
   préfixés : un schéma répété à chaque activité qui le lit.
   **La règle n°331 (15/11/2026), pour toute chaîne montrée avec une question** : la chaîne est dans le bloc de la question
   (`figure.schema-sous-les-yeux`), jamais « ci-dessus » ; muette sur ce que la question demande (fonctions, énergies,
   composants à placer), complète dans la correction ; complète si la question fait LIRE la chaîne. Le contrôle :
   `_outils/controle_schema_sous_les_yeux.py`.
   Classe `Diagram` : `block(x, y, fonction, composant, couleur, stock=…)`, `absent(x, y, fonction, raison)` (pointillés grisés,
   n°131), `arrow(points, couleur, étiquette, …)`, `section(…)`, `text(…)`, `panel(…)` (un cadre sous des textes) ; `circuit_eau(…)`
   pose le circuit d'eau à part. Il écrit aussi la **source draw.io** (`_generation/chaines_energie/`, `fichiers_drawio/` pour le Book Train).
   Le vélo-cargo a son propre générateur (`5e_C3.1/_generation/figure_iso_velo_cargo/`). La bibliothèque de formes draw.io
   des élèves (Book Train, `fichiers_drawio/bibliotheque_chaines_book-train.xml`, 34 formes) sort de
   `_outils/generer_bibliotheque_chaines.py` (24/10/2026). Ne jamais éditer un SVG ou une bibliothèque produits :
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

## Les flux animés (demande de Pascal du 15/11/2026)

« Les chaînes d'énergie et chaîne d'information devront être animées (tous les flux), et de préférence faites avec draw.io »,
« la bibliothèque pour ces chaînes dans draw.io ».
- **Sur le site** : `_outils/animer_flux.py` pose, sur chaque flèche d'un schéma de chaîne, des perles claires qui avancent
  dans le sens de la flèche (deux trains, un dans chaque sens, sur une double flèche ; un branchement « lien » n'en porte pas).
  Le trait d'origine ne change pas : couleur, pointillés de l'ordre, pointe. Les perles disparaissent à l'impression et quand
  le système demande moins de mouvement (`prefers-reduced-motion`) ; elles ne portent aucune information que le dessin ne
  porte déjà (n°119). Les générateurs l'appellent eux-mêmes : `regenerer_chaines_energie.py`, le vélo-cargo (`build.mjs`) ;
  la chaîne à compléter (`_outils/chaine_a_completer/`) dessine les siennes (`.cac-flux`).
- **Dans draw.io** : chaque flèche des sources (`_generation/chaines_energie/*.drawio`, `fichiers_drawio/`) et de la
  bibliothèque (`generer_bibliotheque_chaines.py`, que `--verifier` contrôle) porte `flowAnimation=1`, l'animation native de
  draw.io : une chaîne montée avec la bibliothèque a ses flux animés. Le SVG du site reste celui du générateur : l'export SVG
  de draw.io écrit ses textes en `foreignObject` et pèse un mégaoctet (essai du 15/11/2026, draw.io 32.6 pour Windows).
- **Un nouveau schéma de chaîne**, fait main : `python3 _outils/animer_flux.py <fichier.svg|page.html> --ecrire`, puis
  `--verifier` (0 : chaque chaîne lue a ses flux animés).
- **Le mouvement des perles** (veille du 16/11/2026 ; skill `motion-design` de Pascal, résumée dans
  `sequence-pedagogique-engageante`, « Le mouvement ») : la vitesse **linéaire** est la bonne pour un flux continu,
  et **la même dans toutes les chaînes** — 1,6 s par motif dans celles d'`animer_flux.py` et de la chaîne à
  compléter (relevé du 16/11) : une perle plus rapide laisserait croire à plus de puissance, sauf si c'est voulu et dit. Le guide conseille qu'au plus un tiers des éléments bougent ensemble ; « tous les flux animés » est la
  décision de Pascal (15/11) et prime. Les flux bouclent sans fin : `controle_mouvement.py` les compte parmi les
  boucles qu'aucun bouton n'arrête (⚠ M2, WCAG 2.2.2), en attendant la décision d'un bouton « ⏸ ».

## Vérifier

```
python _outils/regenerer_chaines_energie.py     # écrit les six figures, les sources draw.io, la figure et le QCM du Book Train
python3 _outils/animer_flux.py --verifier <fichiers>   # chaque chaîne a ses flux animés
python _outils/verifier_chaines_energie.py      # textes dans le cadre, énergies hors des blocs, convention dite ET dessinée, impression, objets HTML, scène 6
```

Puis les contrôles du dépôt (dont `controle_regles_visibles.py`, règle n°309 : aucune trace de la fabrique dans un texte lu par
l'élève — ni « règle n°310 » dans un schéma ou une légende) et les bancs des séquences touchées.

`verifier_chaines_energie.py` lit les figures par leur **chemin** (29/10/2026 ; avant, `next(glob)` ne vérifiait que le premier
de deux fichiers de même nom), contrôle la fonction absente (vocabulaire fixe, pointillés, raison) et charge les trois figures
du 29/10 dans leur page (balise `img` ou objet).

## Schémas faits main encore non conformes

Aucun (29/10/2026). Les trois relevés le 23/10/2026 — le jardin de `4e_C9.1`, l'arrosage de `4e_C6.2`, la barrière de
`5e_C9.1` — sont produits par le générateur ; leurs textes (alt, descriptions, consignes, corrigés, QCM, lexique) ont suivi.
Reste, dans une figure générée : la fonction absente de la station de `3e_C9.2`, écrite en une phrase (piège 3).

## Ce que cette règle ne couvre pas

La justesse technique d'un composant précis (à vérifier dans la documentation du matériel) ; le choix du niveau de détail
selon la classe ; les schémas de chaîne d'**information** seule (règle n°6 et gabarit des chaînes).

## Les formes d'énergie (16/11/2026)

Le programme 2024 (SFC 11, connaissances) nomme cinq formes : **électrique, cinétique, potentielle, thermique, lumineuse**.
Décision de Pascal (16/11/2026) : la sortie d'un moteur, d'une pompe, d'une électrovanne est de l'énergie
**cinétique** (« de rotation », « de translation » quand il faut préciser le mouvement) ; un objet en hauteur, un sac
suspendu, un ressort tendu gardent de l'énergie **potentielle**. « Mécanique » n'est pas faux (c'est la somme des deux) : le
lexique et la synthèse le disent une fois, pour qu'un élève qui le croise ailleurs (physique-chimie, brevet) fasse le lien.
« Mécanique » reste là où il ne désigne pas une forme d'énergie : tenue mécanique d'un matériau, frein mécanique,
résistance mécanique du mât.

Deux précisions (16/11/2026, après la fiche SFC1b de l'académie de Bordeaux, qui écrit « moteur → cinétique » mais
« vérin → mécanique » et « mécanique → génératrice ») :
- **« Mécanique » n'est jamais une mauvaise réponse.** Jamais proposé comme piège à côté de « cinétique » dans un QCM ou un
  menu ; une réponse écrite « mécanique » est acceptée, la correction ajoute « on dit aussi cinétique : l'énergie du
  mouvement ».
- **Un vérin, une génératrice** (décision de Pascal, 16/11/2026 : « en cycle 4, le détour est quasiment une
  obligation ») : moteur → **cinétique**, parce qu'il en sort un mouvement ; vérin → **mécanique**, parce qu'il pousse ou
  soulève une charge, donc donne du mouvement et de la hauteur ; génératrice, dynamo : **mécanique → électrique**, comme
  la fiche de Bordeaux (« cinétique → électrique » est juste aussi).
- **Où le détour est écrit** : une note « 📝 Cinétique ou mécanique ? » dans la synthèse de `5e_C3.1` (moteur, vérin,
  la règle) ; le bloc « 📝 Les cinq conversions à connaître » (ci-dessous) dans celle du Book Train, avec la règle ; une ligne « On dit aussi « mécanique » : c'est le
  mot qui couvre le mouvement (cinétique) et la hauteur (potentielle) » dans la correction qui nomme la sortie d'un
  moteur ou d'une pompe (`4e_C4.1`, Book Train, `5e_C4.1`, `4e_C9.1`), et pour la dynamo de `5e_C7.4`. Une nouvelle
  séquence qui fait nommer la sortie d'un moteur, d'une pompe, d'un vérin ou d'une génératrice porte la même ligne
  dans sa correction.

## Les cinq conversions du programme (17/11/2026)

Le programme 2024 (SFC 11, connaissance reprise en CCRI 14) demande « les conversions d'énergie des constituants
suivants : moteur électrique, lampe, radiateur, génératrice, vérin ». Le site les donne en cinq cases, même texte partout :

| Constituant | Conversion |
|---|---|
| Moteur électrique | électrique → cinétique (il en sort un mouvement) |
| Lampe | électrique → lumineuse |
| Radiateur | électrique → thermique |
| Génératrice | mécanique → électrique (elle reçoit le mouvement d'une roue, d'une éolienne) |
| Vérin | pneumatique ou hydraulique → mécanique (il pousse ou soulève une charge) |

Chacune perd un peu d'énergie en chaleur, sauf le radiateur, dont la chaleur est le but. Où : la synthèse du Book Train
(4e, SFC 11 en 4e_C4.2), cases avec leur raison ; la synthèse de `5e_C7.4` (5e, CCRI 14), cases courtes, à la fin de la
partie 4 (les pertes) pour tenir sur deux pages. Pas dans la synthèse du lampadaire (`5e_C4.1`, SFC 11 en 5e) : elle
s'imprime déjà sur trois pages.

**Le dessin commun (17/11/2026)** : `_outils/cinq_conversions/generer.py <dossier Images>…` dessine
`cinq_constituants_muet.svg` (la question : cinq colonnes, ce qui entre et ce qui sort en « ? ») et
`cinq_conversions.svg` (la correction, complète, avec la chaleur perdue). Jamais redessiné à la main : une séquence qui
s'en sert le reçoit par le générateur, et `--verifier` refuse une copie qui a divergé. La progression sur les trois
niveaux : `docs/specifications/progression-cinq-conversions-cycle4.md`.
