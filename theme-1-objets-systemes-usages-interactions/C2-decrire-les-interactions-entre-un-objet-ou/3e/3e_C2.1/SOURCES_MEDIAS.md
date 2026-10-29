# Sources des médias — lot Pékin 3e_C2.1

**Règle d'or n°1** : chaque image est un document à lire, produite pour le dépôt, sous licence
libre, avec `<title>` et `<desc>` accessibles.

| Fichier | Nature | Auteur | Licence | Rôle pédagogique |
|---|---|---|---|---|
| `Images/six_modes_de_representation.svg` | SVG original écrit à la main | Fable, pour ce dépôt | CC0 1.0 | Les six modes, chacun avec **ce qu'il montre ET son angle mort** — c'est ce couple qui fonde la justification |
| `Images/trois_destinataires.svg` | SVG original écrit à la main | Fable, pour ce dépôt | CC0 1.0 | Ce que chaque destinataire peut faire, le temps dont il dispose, et **ce qu'il ne supporte pas** |
| `Images/corrige_trois_representations.svg` | SVG original écrit à la main | Fable, pour ce dépôt | CC0 1.0 | **Corrigé** — le même constat en algorigramme, graphique et storyboard |
| `Images/corrige_trois_autres_modes.svg` | SVG original écrit à la main | Fable, pour ce dépôt | CC0 1.0 | **Corrigé** — le même constat en parcours utilisateur, carte d'empathie et tableau comparatif |

## Pourquoi quatre figures, et pourquoi deux corrigés

Les deux premières sont des **documents à lire**, dans le fil de la page. Les deux dernières sont
des **corrigés** : elles n'apparaissent que dans les corrections repliées (règle n°43).

**Il en fallait deux, et c'est le point important.** La séquence propose **six** modes à l'élève. Un
corrigé qui n'en aurait traité que trois — les trois « bons » appariements — aurait pénalisé celui
qui prend une porte que la séquence a elle-même ouverte.

> **Règle n°43, précision du 08/08/2026** : quand une consigne offre un choix, le corrigé couvre
> **toutes les options offertes**. Sinon « choisis » est un mensonge. Et si corriger toutes les
> options coûte trop cher, il faut réduire le nombre d'options — pas le corrigé.

Effet secondaire heureux : les six fiches mises côte à côte démontrent la thèse de la séquence mieux
qu'aucune phrase. Chacune porte son **angle mort**, et l'on voit d'un coup que **les six disent la
vérité, qu'aucun ne la dit tout entière**.

Aucune photographie de borne réelle : elle donnerait à voir une solution existante là où l'élève
doit d'abord observer des usages. La synthèse élève, lue après les activités, montre une borne générée par IA
(section « Image générée par IA (Canva) », ci-dessous) : à ce moment-là, elle aide à se souvenir de l'objet, elle ne
donne plus de solution à recopier.

## Les données

Toutes **simulées**, construites pour l'exercice. Elles ne décrivent aucun réseau réellement
exploité.

`observations_borne_pekin_simulees.csv` — 40 usagers : profil, durée totale, abandon, étape
d'abandon.

**Les effectifs d'abandon sont fixés, non tirés au hasard.** Un premier tirage aléatoire avait donné
**zéro abandon chez les touristes** — alors que tout le lot repose sur eux. Les corrigés auraient
alors décrit une réalité que le fichier ne contenait pas. Seules les **durées** gardent une part
d'aléa, avec une graine.

> Une donnée simulée n'a pas à être imprévisible : elle a à être **vraie par rapport à ce qu'on en
> dit**.

L'intention est dans les chiffres : 8 abandons sur 40 — « un sur cinq », exact — mais **0 % chez les
habitués**, 43 % chez les touristes, 50 % chez les personnes âgées. Et 77 s de durée moyenne, quand
l'habitué met 41 s et la personne âgée 123 s.

`verbatims_usagers_pekin_simules.csv` — 8 verbatims, dont un en **anglais approximatif** (le
touriste). Le langage naturel de la 4e revient, mais il n'est plus le point de départ : il est une
source parmi d'autres.

`incidents_maintenance_pekin_simules.csv` — 3 incidents, dont celui qui porte l'activité 3 : la
borne **encaisse puis échoue à imprimer**. Ce n'est pas l'organe qui est fautif, c'est **l'ordre des
opérations** — et cela, seul un algorigramme le montre.

## Polices

**Aucune police distante** (règle d'or n°40). Séquence, QCM et synthèses utilisent une pile système.
La page entière fonctionne sans connexion, et aucune donnée n'est envoyée.

## Image générée par IA (Canva) pour la synthèse élève

Demande de Pascal du 29/10/2026 : « une capture d'écran ou une illustration permet d'avoir une vision plus synthétique
de l'objet » ; Canva autorisé « pour des images réalistes et autres ». Règles : skill `synthese-vulgarisee`, §4.

| Fichier | Ce qu'elle montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/synthese_borne_tickets_pekin.png` | Une borne de vente de tickets dans une station de métro : écran tactile, fentes, bac de sortie. PNG 1 536 × 1 024, 2.1 Mo. | **Image générée par IA** avec Canva (génération d'image), compte de Pascal, 29/10/2026. Demande : « Realistic photo of a self-service metro ticket vending machine in a modern subway station: large touchscreen, coin and banknote slots, ticket tray, clean tiled wall, soft station lighting, no people, no readable text on the screen, no logos, the machine seen from a slight angle and filling the centre of the frame » | Conditions Canva AI Product Terms : l'image appartient à Pascal, sans attribution exigée ; interdit de la présenter comme faite par un humain (légende « Image générée par IA (Canva) ») et d'en retirer les métadonnées de provenance (manifeste C2PA et XMP Canva gardés : **fichier non modifié**, d'où son poids). | Synthèse élève, carte « Ce que je dois retenir » |

