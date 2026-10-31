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
* **L'animation « la pompe qui s'affole »** (activité 5 b, bloc `#pompe-pas-a-pas`, 30/10/2026) — neuf étapes : la
  trace de l'activité 5 rejouée tour de boucle par tour de boucle, un jeton qui porte chaque mesure dans l'algorigramme
  pendant que le chronogramme se dessine ; puis les deux seuils, une **prédiction** (« Regarder » s'arrête tant que
  l'élève n'a pas répondu), le même tremblement sans basculement, et le sol qui sèche. Voix SIWIS (`Audio/pompe_etape…`,
  générateur `_generation/voix_pompe/`) : étapes 1 à 8 **écoutées et validées par Pascal le 31/10/2026** ; étape 9 **nouvelle
  prise du 31/10/2026, à réécouter** (sa phrase renvoie maintenant à l'atelier). Le chronogramme fixe reste dans un volet sous
  l'animation, et c'est lui qui s'imprime. Le dessin est fait par le **moteur** `_generation/moteur_algorigramme/`
  (`moteur.js`, `moteur.css`, `poser.py` : la page déclare ses blocs, ses flèches, ses règles et sa série).
* **L'atelier du programme** (activité 5 c et d, bloc `#atelier`, 31/10/2026) — juste sous l'animation, à la place de
  l'ancienne zone de texte : un petit éditeur **dans la page**, à la manière du mode mixte de Vittascience. Des blocs
  (Variables : les réglages, à un ou deux seuils, et la mesure ; Logique : SI / + SINON SI / + SINON, avec leurs actions),
  le Python qu'ils écrivent tout seuls (`lire_humidite()`, la mémoire `pompe_allumee`, `pass`, `commander_relais(…)`),
  et l'exécution : ▶, ⏭ pas à pas, ⏩ jusqu'à la fin, sur **le tremblement du banc** (la même suite `TREMBLEMENT`) et sur
  **une vraie matinée** figée (le sol répond à la pompe). Console, ligne Python éclairée, chronogramme, compteur, et une
  phrase à la fin de chaque essai : l'atelier ne corrige pas, il montre. Le programme est sauvegardé (champs `at_*`) et
  son Python écrit dans `prog3` ; `CHECKS[5]` juge le programme **par son exécution** sur les deux essais. Les verrous
  « pompe affolée » et « pompe calmée » se cochent dans l'atelier. Sans JavaScript et à l'impression : une fiche.
* **`qcm_4e_C9_jardin-programme.html`** — QCM 30 questions (10 par code,
  4 illustrées), corrections détaillées avec **réfutation de chaque distracteur**,
  bilan par compétence.
* **`Synthèses/`** — synthèse élève (imprimable) et synthèse professeur (attendus,
  obstacles, remédiations, sécurité, évaluation).
* **`Images/`** — 4 SVG originaux, tous des **documents à lire** ; le
  chronogramme de l'hystérésis est la figure centrale du lot.
* **`fiche_pedagogique_4e_C9.md`**, **`matrice_couverture_4e_C9.csv`**,
  **`SOURCES_MEDIAS.md`**, **`rapport_tests_4e_C9.md`**, **`CRCN_regle7.md`**.
* **`tests_4e_C9.mjs`** — la suite de tests (105 tests, Playwright, le 31/10/2026, dont 28 pour l'atelier) :
  `node tests_4e_C9.mjs . [dossier_captures]`

## Le banc d'essai — pourquoi il est au centre

Il rend visible un phénomène que le papier ne montre pas. Mode **UN seuil**, on
clique sur « faire trembler la mesure » : le compteur de basculements monte à six
ou huit. Mode **DEUX seuils**, on remet à zéro, **même tremblement** : zéro ou un.

La mesure n'a pas changé d'un point — c'est la **règle** qui a changé. Trente
secondes, et l'idée est acquise.

> Depuis le 31/10/2026, la **preuve** de l'activité 5 se fait dans l'atelier du programme : il exécute le programme que
> l'élève a construit, sur la même suite que ce banc. Le banc garde son rôle pour les activités 3 et 4.

> Le tremblement est une suite de valeurs **figée dans le code**, pas un tirage au
> hasard : sans cela, la comparaison entre les deux règles ne prouverait rien.

Le banc **fonctionne hors connexion**. Seul l'éditeur Vittascience demande une
connexion, et un repli complet est prévu.

## Le relais de l'activité 1

Le jardin étudié : carte + capteur d'humidité (entrée analogique) + **module relais** + pompe 12 V
avec son **alimentation séparée**. Les élèves ne le montent pas : ils le lisent sur le schéma de l'activité 1.

> La version 🅰 « Matériel réel » (montage et téléversement) a été **retirée le 05/10/2026** : l'éditeur Python ne pilote aucune carte. Elle pourra revenir avec la future version carte réelle, en interface Arduino (voir `JOURNAL_DES_DECISIONS.md`).

> **Le relais n'est pas un détail de câblage : c'est le contenu de l'activité 1.**
> Une broche de carte fournit quelques dizaines de milliampères ; un moteur de
> pompe en demande plus de mille. La flèche d'ORDRE arrive donc sur DISTRIBUER, et
> DISTRIBUER, ici, c'est le relais. Sur la station d'alerte de 3e, dont la sortie
> n'est qu'un voyant, elle arrive aussi sur DISTRIBUER, mais c'est la broche de la
> carte qui distribue. **Les deux lots forment une paire** : c'est en les comparant
> que la règle devient visible — l'ordre arrive toujours sur DISTRIBUER ; ce qui
> change, c'est le composant qui distribue.

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
