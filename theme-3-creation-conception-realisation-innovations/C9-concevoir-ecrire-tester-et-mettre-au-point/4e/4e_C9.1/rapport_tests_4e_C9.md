# Rapport de tests — Lot 4e_C9 « Le jardin connecté se programme »

Date : 2026-08-26 (**réécriture complète** ; v1 : 2026-07-25, agent Grok) ·
Agent : Fable · Environnement : Chromium headless (Playwright 1.55),
viewport 1280×900 + émulation téléphone 390×844 · Suite : `tests_4e_C9.mjs`
(committée dans ce dossier, rejouable : `node tests_4e_C9.mjs .`).

La suite **simule la séquence comme un élève** et prend une capture d'écran à
chaque action (23 captures). Elle ne déclare que ce qu'elle exécute.

## 1. Tests automatisés exécutés — 60/60 réussis

### La démonstration centrale : un seuil contre deux seuils

C'est le test dont dépend toute la séance 3. Il exécute la démonstration **comme
un élève la fera**, avec le même tremblement de mesure dans les deux modes.

| Test | Résultat |
|---|---|
| Banc : en **UN seuil**, la mesure qui tremble fait clignoter la pompe | ✅ 8 basculements |
| Banc : en **DEUX seuils**, le **même** tremblement ne fait plus clignoter | ✅ 0 basculement |
| La démonstration est probante (au moins 4 basculements évités) | ✅ 8 → 0 |

> Le tremblement est une suite de valeurs **figée dans le code**
> (41, 39, 41, 40, 39, 40, 39, 41, 40, 39, 41, 40), pas un tirage aléatoire.
> Sans cela, la comparaison entre les deux modes ne prouverait rien : on
> comparerait deux mesures différentes. C'est aussi ce qui rend la démonstration
> **reproductible d'un poste à l'autre** — un élève qui la rejoue obtient
> exactement les mêmes nombres, et peut donc les inscrire dans son compte rendu.

### Le banc d'essai — le comportement, valeur par valeur

| Entrées | Attendu | Résultat |
|---|---|---|
| H = 25 %, 8 h | POMPE ON | ✅ |
| H = 55 %, 8 h | POMPE OFF | ✅ |
| H = 25 %, **23 h** | POMPE OFF — le ET exige les deux conditions | ✅ |
| H = **39 %**, 7 h | POMPE ON (frontière basse) | ✅ |
| H = **40 %** pile, 7 h | POMPE OFF — `40 < 40` est **faux** | ✅ |

### Les verrous : la page refuse de valider ce qui n'a pas été fait

| Test | Résultat |
|---|---|
| Act. 1 refusée tant que la justification écrite manque | ✅ |
| Act. 3 refusée tant que le journal ne cite pas de **valeurs** (3 nombres exigés) | ✅ |
| Act. 3 refusée tant que les essais au banc ne sont pas faits | ✅ |
| Act. 4 refusée tant que les deux frontières ne sont pas exécutées au banc | ✅ |
| Act. 5 refusée tant que la démonstration au banc n'est pas jouée dans les deux modes | ✅ |
| Act. 6 refusée tant que le programme du lampadaire n'a pas **deux seuils distincts** | ✅ |

### Le parcours élève, de bout en bout

| Test | Résultat |
|---|---|
| Chargement `file://` sans erreur JS (début et fin de parcours) | ✅ |
| Billet d'entrée : feedback affiché, **déclaré hors progression**, et la progression reste à 0 | ✅ |
| Tableau de bord : les 6 activités listées, puis les 6 cochées en fin de parcours | ✅ |
| Activités 1 à 6 validées avec leurs vérificateurs exacts | ✅ |
| Progression 6/6 · les 3 séances cochées ✔ | ✅ |
| Rappel de l'hypothèse de départ affiché au bilan | ✅ |
| **Sauvegarde / restauration** après rechargement : progression, réponses, verrous du banc | ✅ |
| Zéro lien local cassé | ✅ |
| Mobile 390 px : aucun défilement horizontal (débord = 0), zéro erreur JS | ✅ |

### Les règles d'or vérifiables à l'écran

| Règle | Vérification | Résultat |
|---|---|---|
| n°4 | un **seul** bouton QCM dans la séquence | ✅ |
| n°29 | le mode essentiel masque réellement le référentiel | ✅ |
| n°92 | la loupe ouvre l'image en grand, Échap referme | ✅ |
| n°101 | 2 boutons « séance suivante », et le clic bascule vraiment | ✅ |
| n°117 | chaque figure a un `alt` ≥ 120 caractères **et** une description dépliable rattachée par `aria-describedby` | ✅ |
| n°122 | sélecteur de parcours actif ; choisir 🅲 masque les blocs 🅱 **sans retirer aucune question** | ✅ |

### QCM

| Test | Résultat |
|---|---|
| 30 questions · **10 par code** (C9.1 / C9.2 / C9.3) · 4 illustrées | ✅ |
| Bonnes réponses réparties A/B/C/D = **8/7/7/8** | ✅ |
| `d[r]` vide et 3 réfutations non vides sur **chacune** des 30 questions | ✅ |
| Chaque question porte explication, exemple, erreur fréquente et à-retenir | ✅ |
| Correction complète affichée · question illustrée · marquage 🔖 | ✅ |
| Révision ciblée 4e_C9.3 = 10 questions · mode « mes erreurs » = 1 | ✅ |
| Scénario 30/30 → **20,0 /20 · 100 %** · bilan à 3 lignes maîtrisées | ✅ |
| Scénario 15 justes / 15 fausses → **10,0 /20 · 50 %** | ✅ |
| Scénario 6 justes, 6 fausses, 18 non répondues → **4,0 /20 · 18 NR** | ✅ |
| Zéro erreur JS sur tout le parcours | ✅ |

## 2. Contrôles statiques

- **Règles d'or mécanisées** (`python3 _outils/verif_regles_audit.py …/4e_C9.1/`) :
  **0 manquement**, et **aucune alerte**. La v1 en comptait **cinq** — n°23 (aucune
  durée annoncée), n°26 (pas de diagnostic d'entrée), n°29 (pas de mode essentiel),
  n°30 (5 tâches sans tableau de bord), n°31 (6 zones de rédaction, aucune version
  étayée), n°34 (16 champs sans étiquette).
- **n°42 — formulations du référentiel** : les 3 formulations de la carte sont
  celles du programme, **au mot près**. C'est ce contrôle qui a révélé l'erreur de
  fond du lot (voir §4).
- **Poids des médias** : 4 SVG originaux de 7 à 9 Ko. `<title>` et `<desc>`
  accessibles dans chacun.
- **Matrice de couverture** : 31 lignes, 8 colonnes normalisées ; les 30 questions
  du QCM sont rattachées à une notion enseignée.
- **Aucun envoi réseau** : sauvegardes localStorage uniquement
  (`seq_4e_C9_jardin-connecte` / `qcm_4eC9_jardin-connecte`). Seul l'`iframe`
  Vittascience sort, et son absence est prévue.

## 3. Contrôles restant manuels (non exécutés — à faire par un humain)

- **version 🅰 au labo** : capteur d'humidité, **module relais**, pompe 12 V avec
  son alimentation séparée, et le téléversement depuis Vittascience. Le câblage
  doit être relu avant toute mise sous tension ;
- **accès réseau** : vérifier que `fr.vittascience.com` n'est pas filtré par le
  réseau du collège avant la séance 2 (sinon, le banc d'essai prend le relais) ;
- test sur appareils réels (tablette, téléphone) — seul le viewport a été émulé ;
- relecture orthotypographique humaine ; rendu GitHub Pages après publication.

## 4. Ce que la campagne a trouvé

**Une erreur de fond, héritée de la v1 : les mauvais verbes en face des codes.**
Le lot annonçait « concevoir » pour 4e_C9.1 et « réinvestir » pour 4e_C9.3. Le
programme 2024 dit **modifier**, **traduire**, **réaliser et mettre au point** — et
« concevoir » est un verbe de **3e**. Ce n'est pas un détail de rédaction : cela
change ce qu'on demande à l'élève. « Modifier » interdit la page blanche, et
impose de fournir l'algorithme amputé d'une exigence.

Ce défaut est resté invisible pendant un mois parce qu'il ne se voit ni à l'écran,
ni à l'exécution : la page fonctionnait parfaitement. Il a fallu un contrôle qui
compare **mot à mot** la carte de référentiel au texte officiel (règle n°42) pour
qu'il apparaisse.

**Deux défauts de lisibilité**, trouvés en cours de campagne :

1. Le verrou « avoir fait varier l'humidité » comptait le **nombre de valeurs
   touchées** (six distinctes). Un élève qui saisit directement 25 puis 55 dans le
   champ de valeur exacte n'en touchait que deux, et restait bloqué sans comprendre
   pourquoi. Remplacé par une exigence qui a du sens : **avoir vu la pompe des deux
   côtés du seuil**.
2. Dans l'encadré des trois niveaux (lot 3e, corrigé au passage), les trois bords
   colorés sortaient tous de la même couleur : `.trois-niveaux .niv` (deux classes)
   l'emportait sur `.niv-mesure` (une seule). Invisible à l'œil sur fond sombre ;
   trouvé par un test qui **compare les trois couleurs entre elles**.

## 5. Échecs

Aucun test exécuté en échec au moment de la remise (60/60). La suite complète a été
rejouée intégralement, pas seulement les tests ajoutés.
