# Rapport de tests — Atelier « La boîte étiquetée » (5e_C9.1 → C9.3)

Date : 2026-08-26 (**harmonisation du lot** ; campagne initiale : 2026-07-30) ·
Agent : Fable · Environnement : Chromium headless (Playwright 1.55),
viewport 1280×900 + émulation téléphone 390×844 · Suite : `tests_5e_C9.1-C9.3.mjs`
(**committée dans ce dossier**, rejouable : `node tests_5e_C9.1-C9.3.mjs .`).

> Comme pour le lot 3e_C9.1, la campagne du 30 juillet avait bien eu lieu (27/27) mais
> **aucune suite n'était committée** : rien n'était rejouable, et le lot pouvait dériver
> sans que personne ne le voie. Ce fichier ferme ce trou. Chaque dispositif est vérifié
> par la **mesure de son effet** — un nombre —, jamais par la présence de ses commandes
> (règle d'or n°136).

## 1. Tests automatisés exécutés — 44/44 réussis

### Les dispositifs installés à l'harmonisation

| Règle | Vérification exécutée | Résultat |
|---|---|---|
| n°23 | 5 durées d'activité à la convention `⏱ ~n min`, total 130 min pour 165 disponibles | ✅ |
| n°26 | le billet d'entrée rend un feedback, **se déclare hors progression**, la progression reste à 0 | ✅ |
| n°29 | le mode essentiel masque la carte de référentiel **et les 5 corrections** ; un second clic rétablit | ✅ |
| n°30 | le tableau de bord liste les 5 activités, aucune cochée au départ | ✅ |
| n°31 | une version étayée pour chacune des 2 zones de rédaction | ✅ |
| n°34 | aucun champ sans étiquette, et **24 listes déroulantes sur 24** portent un `for=` explicite | ✅ |
| n°42 | les **3 formulations** de la carte sont celles du programme 2024, au mot près | ✅ |
| n°101 | 2 boutons « séance suivante », et le clic bascule vraiment de panneau | ✅ |
| n°122 · n°136 | choisir 🅲 masque **1 bloc 🅱 sur 1**, sans retirer aucun des 5 vérificateurs | ✅ |
| n°135 | aucun tableau visible sans séparation lisible (2 tableaux mesurés au rendu) | ✅ |

### Le cœur pédagogique : un programme qui tourne, et qui ment

C'est la démonstration dont dépend tout l'atelier, et elle est exécutée telle qu'un élève
la vivra.

| Test | Résultat |
|---|---|
| Act. 4 — **T1 et T2 passent** : le programme fourni a l'air correct | ✅ 24 ✔ |
| Act. 4 — **T3 échoue** et démasque le bug des descendus | ✅ 19 ✘ (attendu 23) |
| Act. 4 — les 3 essais délivrent le badge de test | ✅ |
| Act. 5 — le **cas frontière** (0 place pile) ferme bien la barrière | ✅ FERMÉE ✔ |
| Act. 5 — les 3 essais de barrière délivrent le badge de réglage | ✅ |

> Deux essais sur trois passent. C'est exactement ce qui rend l'activité honnête : un
> programme qui échouerait partout n'apprendrait rien. Ici, il faut **choisir le bon
> essai** — celui où quelqu'un descend — pour que le défaut apparaisse.

### Le parcours élève

| Test | Résultat |
|---|---|
| Chargement `file://` sans erreur JS | ✅ |
| Act. 1 : les 4 étapes du simulateur de mémoire délivrent le badge 🔓 | ✅ |
| Act. 1 : validée 3/3 avec le vérificateur exact | ✅ |
| Act. 5 : **refusée** tant que les 3 tests de barrière ne sont pas exécutés | ✅ |
| Progression 1/5 · la tâche 1 cochée au tableau de bord | ✅ |
| **Sauvegarde / restauration** après rechargement (progression + réponses) | ✅ |
| Aucune sortie réseau hors iframe Vittascience | ✅ |
| Mobile 390 px : débord horizontal = **0**, zéro erreur JS | ✅ |
| Zéro lien local cassé (4 HTML parcourus) | ✅ |

### QCM

| Test | Résultat |
|---|---|
| 30 questions chargées | ✅ |
| Bonne réponse **sans** réfutation, 3 réfutations non vides, sur **chacune** des 30 | ✅ |
| Répartition des bonnes réponses A/B/C/D = **8/7/7/8** | ✅ |
| Chargement sans erreur JS | ✅ |

## 2. Contrôles statiques

- **Règles d'or mécanisées** (`python3 _outils/verif_regles_audit.py …/5e/`) : **0 manquement**.
  Avant l'harmonisation : quatre — n°29, n°30, n°31, n°34, plus une durée non reconnue (n°23).
- **Aucun envoi réseau** : sauvegarde localStorage seule
  (`seq_5e_C9.1-C9.3_boite_etiquetee`). Seuls les `iframe` Vittascience sortent, et leur
  absence est prévue et annoncée dans la page.

## 3. Ce que la campagne a trouvé

**Un README qui renvoyait ailleurs.** `5e_C9.1/README.md` annonçait encore
« **COUVERT** — mutualisé dans le mini-projet Thème 3 », état antérieur à la création de
l'atelier. Un collègue arrivant dans le dossier était renvoyé vers une autre ressource
alors que celle qu'il cherchait était sous ses yeux, complète. Réécrit.

**Deux erreurs commises pendant l'harmonisation, et corrigées :**

1. La feuille de style des nouveaux dispositifs a d'abord été insérée **hors de toute
   balise `<style>`**. Résultat : le bouton « mode essentiel » basculait bien, la classe
   `parcours-c` s'appliquait bien au `body` — et rien ne se masquait. Encore un mécanisme
   complet branché sur rien ; encore trouvé par un test qui **compte** les blocs masqués
   plutôt que de constater la présence du bouton.
2. L'ajout automatique des `for=` sur les étiquettes a d'abord mangé le `>` fermant de la
   balise `<label>`, avalant les listes déroulantes dans leur propre étiquette. La page
   se chargeait sans erreur ; c'est Playwright qui a refusé de sélectionner une option
   « dans un élément qui n'est pas un `<select>` ». Le remplacement a été réécrit pour
   préserver la balise, et l'avertissement est inscrit en commentaire dans le script.

## 4. Contrôles restant manuels (non exécutés — à faire par un humain)

- le contenu **interne** des iframes Vittascience (service externe) : seuls l'embarquement
  et le suivi d'ouverture sont testés, pas l'exécution Python côté Vittascience ;
- **accès réseau du collège** : vérifier que `fr.vittascience.com` n'est pas filtré ;
- la version 🅰 sur carte réelle (LED en barrière, très basse tension) ;
- test sur appareils réels — seul le viewport a été émulé ;
- relecture orthotypographique humaine ; rendu à l'impression.

## 5. Échecs

Aucun test en échec à la remise (44/44). Les trois échecs rencontrés en cours de campagne —
la feuille de style hors balise, les étiquettes mal réécrites, et un critère de test qui
comptait à tort la mention d'en-tête « 3 séances de 55 min » comme une durée d'activité —
ont été corrigés : les deux premiers dans la séquence, le troisième dans la suite elle-même.
