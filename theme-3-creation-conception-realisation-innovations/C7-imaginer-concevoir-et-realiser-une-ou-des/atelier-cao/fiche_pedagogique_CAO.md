# Fiche pédagogique — La progression CAO du cycle 4 (C7.2, C7.6)

**Niveaux** : 5e, 4e et 3e — un TP par niveau, dans une ressource commune.
**Durée** : 1 séance de 55 minutes par TP, en salle informatique.
**Logiciel** : Onshape Éducation (navigateur, aucun poste à installer).
**Thème** : 3 — Création, conception et réalisation d'innovations.

## Les codes, en toutes lettres

| Code | Formulation du référentiel (2024) | TP qui la travaille | Où il est évalué |
|---|---|---|---|
| **5e_C7.2** | Fabriquer une solution pour améliorer un OST existant. | *aucun* — voir ci-dessous | nulle part à ce jour |
| **4e_C7.2** | Proposer et fabriquer une solution pour ajouter une nouvelle fonction à un OST (croquis, schéma, graphique, algorithme, modélisation). | TP nº2 — Le dé sur son socle (contribution) | séquence `4e_C7.1` — 10 questions |
| **3e_C7.2** | Proposer et fabriquer un ensemble de solutions pour produire un nouvel OST (croquis, schéma, graphique, algorithme, modélisation). | TP nº4 — Le boîtier étanche | QCM du lot `3e_C7.6` — 10 questions |
| **5e_C7.6** | Mettre en œuvre les moyens pour réaliser une forme selon une procédure fournie. | TP nº1 — Le dé | QCM du lot `5e_C7.6` — 30 questions |
| **4e_C7.6** | Modifier une forme à l’aide d’une modélisation. | TP nº2 — Le dé sur son socle | QCM du lot `4e_C7.6` — 30 questions |
| **3e_C7.6** | Modéliser une forme voulue. | TP nº4 — Le boîtier étanche | QCM du lot `3e_C7.6` — 20 questions |

> **Correction du 31/08/2026.** Ce tableau donnait auparavant deux formulations, identiques aux
> trois niveaux : « Imaginer, créer et simuler tout ou partie d'un objet » pour C7.2 et
> « Réaliser, de manière collaborative, le prototype d'un objet » pour C7.6. **Aucune des deux
> n'est dans le programme 2024**, et surtout : le programme différencie ces codes par niveau,
> ce que la formulation unique effaçait. Les six libellés ci-dessus sont recopiés de
> `_outils/data_competences.py`, seule autorité du dépôt sur le référentiel. Les six pages
> d'orientation des dossiers de codes portaient la même erreur ; elles sont corrigées.

> **Correction du 30/08/2026 — `5e_C7.2` ne relève pas de ce TP.** Le tableau annonçait « TP nº1
> — Le dé ». Or ce code demande de **fabriquer une solution pour améliorer un OST existant** : le
> dé n'améliore aucun objet, et rien n'est fabriqué pendant la séance (le fichier part à
> l'impression plus tard). Ce geste appartient au **mini-projet de `5e_C7.1`**, ce que dit déjà
> le README du dossier `5e_C7.2`. Le badge du TP, qui affichait « C7.2 · C7.6 », est corrigé lui
> aussi. Conséquence à assumer : **`5e_C7.2` n'est évalué nulle part dans le dépôt** — c'est un
> trou réel, et il ne se comble pas en le rattachant au mauvais TP.

Les trois TP **exposent** aussi C7.3 — choisir (5e), comparer (4e) un matériau —
sans l'évaluer : aucune question notée n'y est posée. C'est aux séquences de
niveau de le faire.

## Ce qui s'évalue, et où

Depuis le 30/08/2026, chaque TP a son **lot d'évaluation** dans le dossier du code
correspondant. Le TP reste non évaluatif ; le QCM, la synthèse et le lexique sont des pages
séparées, **hors ligne, imprimables, sans compte**.

| Niveau | Lot | Pièces |
|---|---|---|
| 5e | [`5e/5e_C7.6/`](../5e/5e_C7.6/README.md) | QCM 30 q · 2 synthèses · fiche · matrice · lexique · rapport de tests |
| 4e | [`4e/4e_C7.6/`](../4e/4e_C7.6/README.md) | QCM 30 q · 2 synthèses · fiche · matrice · lexique · rapport de tests |
| 3e | [`3e/3e_C7.6/`](../3e/3e_C7.6/README.md) | QCM 30 q (20 + 10) · 2 synthèses · fiche · matrice · lexique · rapport de tests |

## La problématique

**Comment décrire un objet assez précisément pour qu'une machine le fabrique
sans nous ?**

Elle n'est pas décorative. Un élève qui dessine « à peu près » obtient une
pièce qui ne s'imprime pas, ou qui ne s'assemble pas. La précision n'est pas
une exigence de professeur : c'est la condition pour que la machine puisse
faire son travail toute seule.

## La progression, et ce qui la commande

| Niveau | Objet | Geste nouveau | Ce qui change vraiment |
|---|---|---|---|
| **5e** | Le dé | esquisser, coter, extruder, enlever, adoucir | On fabrique **une pièce**. |
| **4e** | Le dé sur son socle | la **révolution**, puis l'**assemblage** et les contraintes | On tient **deux pièces ensemble** — et l'une peut empêcher l'autre de bouger. |
| **3e** | Le boîtier étanche | la **coque**, la rainure, le passage de câble, la vue en coupe | L'objet doit **résister à quelque chose de réel**. |

Le fil n'est pas la difficulté des outils, c'est **l'enjeu**. En 5e une pièce
ratée reste jolie à l'écran. En 4e elle ne s'assemble pas, et ça se voit tout
de suite. En 3e elle prend l'eau, et personne ne le sait avant la première
averse.

## Ce que chaque TP n'est pas

**Ce n'est pas une évaluation.** Aucune question de cours n'y figure (règle
d'or n°81) : on apprend l'outil ici, on évalue la notion après, dans le QCM du
lot de niveau (voir « Ce qui s'évalue, et où » plus haut). Mélanger
les deux, c'est punir l'élève lent à trouver un bouton.

**Ce n'est pas un tutoriel à suivre les yeux fermés.** L'aide décroît : le
premier geste de chaque famille est écrit au clic près, le deuxième est allégé,
les suivants tiennent en une ligne et une image du résultat. L'autonomie ne se
demande pas, elle se produit quand l'étayage se retire.

## Le déroulé d'une séance, côté professeur

**Les cinq premières minutes décident du reste.** Le TP commence par un geste
de rangement — créer le document, le nommer avec le nom de l'élève. Un travail
qu'on ne retrouve pas à la séance suivante n'a pas eu lieu, et c'est la
première cause de séance perdue en salle informatique.

**Pendant la séance, le professeur ne montre rien au tableau.** Le TP est écrit
pour être suivi seul ; démontrer au vidéoprojecteur casse le rythme de ceux qui
sont ailleurs. Le rôle est de circuler et de repérer *où* on bloque.

**Le seul chiffre à relever** : combien de fois un élève a levé la main pour
retrouver un bouton ou pour savoir s'il était juste. C'est le critère de
réussite du TP, et il ne se mesure pas dans un script. La phrase de référence,
d'un TP mené en classe : « c'est long, mais il arrive à être autonome et
personne ne reste sur la touche ».

**Les dix dernières minutes sont pour la récompense.** Colorer, choisir une
matière. Ça ne sert à rien et c'est ce que l'élève montrera chez lui.

## Différenciation

**Pour qui va vite** : le palier de récompense est extensible à l'infini —
autres couleurs, autres matériaux, comparaison des masses. En 4e et 3e, essayer
un troisième matériau et justifier son choix.

**Pour qui bloque** : chaque palier a un critère de réussite explicite
(« tu peux passer à la suite quand… ») et une image du résultat attendu. Un
élève en retard peut sauter à l'image, se comparer, et reprendre au palier
suivant sans avoir tout refait.

**Pour qui n'était pas là** : chaque TP de 4e et de 3e s'ouvre par un rappel de
ce qui a été produit les années précédentes, rédigé pour être **auto-suffisant**
(règle d'or n°87). En 4e, un dé tout prêt est fourni au palier 5 pour ceux qui
n'ont pas le leur.

## Matériel et contraintes

Onshape Éducation fonctionne dans un navigateur : **rien à installer**, et la
connexion se fait avec **le compte de la classe** — pas un compte par élève.
C'est ce que dit le TP de 5e au palier 1, et c'est ce qui permet de tenir la
règle de conception n°5 sur ce point.

**Sur l'autre point, la règle n'est pas tenue, et c'est assumé.** La règle n°5
demande un « fonctionnement hors connexion raisonnable ». Onshape n'a **aucun
mode hors ligne** : sans réseau, la séance ne peut pas avoir lieu, elle se
reporte. Il n'existe donc **pas de version 🅱** pour le geste de modélisation, et
le prétendre serait faux. Les trois TP le disent maintenant en tête.

Ce qui fonctionne hors ligne, en revanche, c'est tout ce qui s'évalue : les
trois QCM, les six synthèses et les trois lexiques sont des pages autonomes,
imprimables, sans compte. Un élève privé de réseau ne perd pas la notion, il
perd la manipulation — et c'est elle qu'on reporte.

> **Décision du 30/08/2026 (option a).** Plutôt que d'écrire un modeleur hors
> ligne dans la page (~1 journée) ou une version papier complète (~2 heures), on
> assume l'exception : Onshape exige le réseau, la règle n°5 le note
> explicitement pour la CAO, et la séance se reporte en cas de coupure. La ligne
> correspondante est à ajouter par l'enseignant dans `ENVIRONNEMENT_TECHNIQUE.md`,
> qui n'est accessible depuis aucune branche de thème.

Aucun risque électrique : ce sont des TP entièrement logiciels.

## Ce qui suit

Le fichier obtenu à la fin de chaque TP est un **vrai fichier de fabrication**.
En 5e et en 4e il peut être imprimé tel quel ; en 3e il l'est nécessairement,
puisque le boîtier protège un capteur réel de la séquence.

## Limites déclarées

Les images des trois TP ne sont pas toutes produites à ce jour : le générateur
signale celles qui manquent et la règle n°77 refuse le TP tant qu'il en reste.
Le détail figure dans `RELEVE_DES_CAPTURES_5e.md`, `_4e.md` et `_3e.md`.

La justesse des gestes décrits — le bouton existe-t-il, est-il au bon endroit
dans cette version d'Onshape — n'est **pas** vérifiée par script. Elle se
constate en déroulant le TP sur un poste identique à celui des élèves.
