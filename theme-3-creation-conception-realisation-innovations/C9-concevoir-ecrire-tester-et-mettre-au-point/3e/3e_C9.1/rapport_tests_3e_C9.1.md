# Rapport de tests — Atelier « Variables, types et systèmes » (3e_C9.1)

Date : 2026-08-26 (**harmonisation du lot** ; campagne initiale : 2026-07-30) ·
Agent : Fable · Environnement : Chromium headless (Playwright 1.55),
viewport 1280×900 + émulation téléphone 390×844 · Suite : `tests_3e_C9.1.mjs`
(**committée dans ce dossier**, rejouable : `node tests_3e_C9.1.mjs .`).

> **Ce qui a changé le 26 août, et qu'il faut dire.** La campagne du 30 juillet
> annonçait 30/30. Elle avait bien eu lieu — mais **aucune suite n'était
> committée** : personne, pas même moi, ne pouvait la rejouer pour vérifier que
> le lot n'avait pas dérivé depuis. Un rapport qu'on ne peut pas rejouer est une
> affirmation, pas une preuve. La suite ci-dessous ferme ce trou.

## 1. Tests automatisés exécutés — 35/35 réussis

### Les six dispositifs installés à l'harmonisation

Ces six-là n'existaient pas avant le 26 août. Chacun est vérifié **par son
effet à l'écran**, pas par la présence de sa classe CSS (règle n°135).

| Règle | Vérification exécutée | Résultat |
|---|---|---|
| n°23 | des durées ⏱ sont annoncées (6 mentions, 185 min pour 220 disponibles) | ✅ |
| n°26 | le billet d'entrée rend un feedback, **se déclare hors progression**, et la progression reste à 0 | ✅ |
| n°29 | le mode essentiel **masque réellement** la carte de référentiel — et un second clic la rétablit | ✅ |
| n°30 | le tableau de bord liste les 5 activités, aucune cochée au départ | ✅ |
| n°31 | 2 versions étayées pour 2 zones de rédaction | ✅ |
| n°34 | aucun champ de saisie sans étiquette (39 champs) | ✅ |

### Les règles d'or déjà acquises, re-vérifiées

| Règle | Vérification exécutée | Résultat |
|---|---|---|
| n°101 | 3 boutons « séance suivante », et le clic **bascule vraiment** de panneau | ✅ |
| n°122 | choisir 🅲 applique `parcours-c`, masque les blocs 🅱, **sans retirer aucun des 5 vérificateurs** | ✅ |
| n°135 | aucun tableau visible sans séparation lisible (2 tableaux mesurés au rendu) | ✅ |

### Le parcours élève

| Test | Résultat |
|---|---|
| Chargement `file://` sans erreur JS | ✅ |
| Act. 1 : les 6 étapes du simulateur de mémoire délivrent le badge 🔓 | ✅ |
| Act. 1 : validée 4/4 avec le vérificateur exact | ✅ |
| Act. 5 : **refusée** tant que les 4 tests du banc ne sont pas exécutés | ✅ |
| Progression 1/5 · la tâche 1 cochée au tableau de bord | ✅ |
| **Sauvegarde / restauration** après rechargement (progression + réponses) | ✅ |
| Aucune sortie réseau hors iframe Vittascience | ✅ |
| Mobile 390 px : débord horizontal = **0**, zéro erreur JS | ✅ |
| Zéro lien local cassé (7 HTML parcourus) | ✅ |

### QCM

| Test | Résultat |
|---|---|
| 30 questions chargées | ✅ |
| Bonne réponse **sans** réfutation, 3 réfutations non vides, sur **chacune** des 30 | ✅ |
| Répartition des bonnes réponses A/B/C/D = **8/7/7/8** | ✅ |
| Chargement sans erreur JS | ✅ |

## 2. Contrôles statiques

- **Règles d'or mécanisées** (`python3 _outils/verif_regles_audit.py …/3e_C9.1/`) :
  **0 manquement**. Avant l'harmonisation, le lot en comptait **six** — n°23, n°26,
  n°29, n°30, n°31 et n°34.
- **n°42 — formulation du référentiel** : la formulation de la carte est celle du
  programme 2024, au mot près.
- **Aucun envoi réseau** : sauvegarde localStorage seule
  (`seq_3e_C9.1_variables_types_systemes`). Seuls les `iframe` Vittascience
  sortent, et leur absence est prévue et annoncée dans la page.

## 3. Ce que la campagne a trouvé

**Le sélecteur de parcours ne masquait rien.** Les trois boutons 🅰/🅱/🅲
étaient bien là, la classe `parcours-c` s'appliquait bien au `body`, la note
annonçait bien le parcours choisi — et **aucun élément de la page ne portait
`data-parcours`**. Le dispositif était complet et sans effet : zéro bloc masqué
sur zéro bloc concerné. Un contrôle qui aurait cherché « le sélecteur est-il
présent ? » aurait répondu oui.

C'est exactement le défaut que décrit la règle n°135, transposé : *on avait posé
le sélecteur, pas ce qu'il sélectionne*. Corrigé en rattachant les trois
descriptions de parcours à leur lettre, et en ajoutant devant chaque éditeur
embarqué la consigne propre à 🅰 et à 🅲.

> **Ce qui n'a délibérément PAS été masqué** : les barres 🧪 des éditeurs
> Vittascience restent visibles dans les trois parcours, parce que ce sont
> **elles qui portent le verrou d'expérience** des activités 3 et 4. Les masquer
> en 🅲 aurait retiré deux validations — ce qu'interdit la règle n°122.

## 4. Contrôles restant manuels (non exécutés — à faire par un humain)

- le contenu **interne** des iframes Vittascience (service externe) : seuls
  l'embarquement et le suivi d'ouverture sont testés, pas l'exécution Python
  côté Vittascience ;
- **accès réseau du collège** : vérifier que `fr.vittascience.com` n'est pas
  filtré avant la séance 2 ;
- le TP mBot2 sur robot réel (version 🅰) ;
- test sur appareils réels — seul le viewport a été émulé ;
- relecture orthotypographique humaine ; rendu à l'impression.

## 5. Échecs

Aucun test en échec à la remise (35/35). Les deux échecs rencontrés en cours de
campagne — le sélecteur de parcours sans effet, et un contrôle QCM qui exigeait
à tort que le tableau `QUESTIONS` soit exposé sur `window` — ont été corrigés,
l'un dans la séquence, l'autre dans la suite elle-même.
