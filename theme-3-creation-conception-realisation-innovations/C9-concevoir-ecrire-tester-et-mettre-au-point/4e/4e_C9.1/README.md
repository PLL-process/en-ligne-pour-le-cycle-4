# 4e_C9.1 — « Le jardin connecté se programme » (Thème 3)

> **4e_C9.1** — Modifier un algorithme permettant de répondre au besoin ou au problème posé.
> **4e_C9.2** — Traduire un algorithme permettant de répondre à un besoin ou à un problème simple en un programme.
> **4e_C9.3** — Réaliser et mettre au point un programme commandant un système réel incluant éventuellement une interaction entre un humain et une machine.
>
> *Formulations recopiées de `_outils/data_competences.py`. L'exergue résumait
> auparavant les trois codes en une phrase de son cru — à l'endroit même où le
> gabarit met la citation officielle.*

Dossier principal du lot **4e_C9.1 + 4e_C9.2 + 4e_C9.3**. Objet-fil de 4e : le
jardin connecté, dont le support a été conçu (C7) puis validé (C8), reçoit enfin
le programme qui décide d'arroser — et qu'il faudra mettre au point.

## Ressources

* **`sequence_4e_C9_jardin-programme.html`** — la séquence complète (3 séances de
  55 min, 6 activités) : les deux chaînes et le relais, l'algorigramme, l'écriture
  en blocs puis en Python sur **Vittascience**, le jeu d'essais avec ses quatre
  familles, la mise au point par **hystérésis**, et le réinvestissement sur un
  lampadaire **sans squelette fourni**.
  **Banc d'essai du jardin intégré** (humidité, heure, règle à un ou deux seuils,
  compteur de basculements) avec verrous expérientiels : les activités 3, 4 et 5
  exigent des manipulations réellement faites.
* **`qcm_4e_C9_jardin-programme.html`** — QCM 30 questions (10 par code,
  4 illustrées), corrections détaillées avec **réfutation de chaque distracteur**,
  bilan par compétence.
* **`Synthèses/`** — synthèse élève (imprimable) et synthèse professeur (attendus,
  obstacles, remédiations, sécurité, évaluation).
* **`Images/`** — 4 SVG originaux, tous des **documents à lire** ; le
  chronogramme de l'hystérésis est la figure centrale du lot.
* **`fiche_pedagogique_4e_C9.md`**, **`matrice_couverture_4e_C9.csv`**,
  **`SOURCES_MEDIAS.md`**, **`rapport_tests_4e_C9.md`**, **`CRCN_regle7.md`**.
* **`tests_4e_C9.mjs`** — la suite de tests (58 tests, Playwright) :
  `node tests_4e_C9.mjs .`

## Le banc d'essai — pourquoi il est au centre

Il rend visible un phénomène que le papier ne montre pas. Mode **UN seuil**, on
clique sur « faire trembler la mesure » : le compteur de basculements monte à six
ou huit. Mode **DEUX seuils**, on remet à zéro, **même tremblement** : zéro ou un.

La mesure n'a pas changé d'un point — c'est la **règle** qui a changé. Trente
secondes, et l'idée est acquise.

> Le tremblement est une suite de valeurs **figée dans le code**, pas un tirage au
> hasard : sans cela, la comparaison entre les deux règles ne prouverait rien.

Le banc **fonctionne hors connexion**. Seul l'éditeur Vittascience demande une
connexion, et un repli complet est prévu.

## Matériel (version 🅰)

Carte + capteur d'humidité (entrée analogique) + **module relais** + pompe 12 V
avec son **alimentation séparée**.

> **Le relais n'est pas un détail de câblage : c'est le contenu de l'activité 1.**
> Une broche de carte fournit quelques dizaines de milliampères ; un moteur de
> pompe en demande plus de mille. La flèche d'ORDRE s'arrête donc sur le relais —
> alors que sur la station d'alerte de 3e, dont la sortie n'est qu'un voyant, elle
> va droit sur CONVERTIR. **Les deux lots forment une paire** : c'est en les
> comparant que la règle devient visible.

**Sécurité** : la carte reste en très basse tension ; l'alimentation de la pompe
est branchée **par le professeur**, après relecture du câblage. Aucun secteur
230 V dans cette séquence.

## Une correction de fond, à signaler

La version précédente de ce lot annonçait « concevoir » pour 4e_C9.1 et
« réinvestir » pour 4e_C9.3. **Ce ne sont pas les verbes du programme 2024** — et
« concevoir » est un verbe de 3e. Le référentiel dit :

| Code | Formulation officielle |
|---|---|
| 4e_C9.1 | **Modifier** un algorithme permettant de répondre au besoin ou au problème posé. |
| 4e_C9.2 | **Traduire** un algorithme permettant de répondre à un besoin ou à un problème simple en un programme. |
| 4e_C9.3 | **Réaliser et mettre au point** un programme commandant un système réel incluant éventuellement une interaction entre un humain et une machine. |

Les activités ont été remises en face des bons codes (règles d'or n°105 et n°106).
Conséquence concrète en classe : **on ne demande jamais la page blanche en 4e**.
L'algorithme est fourni, amputé d'une exigence ; l'élève trouve où intervenir.
