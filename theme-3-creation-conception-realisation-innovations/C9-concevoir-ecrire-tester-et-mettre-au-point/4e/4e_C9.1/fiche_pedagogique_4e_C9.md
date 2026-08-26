# Fiche pédagogique — 4e_C9 « Le jardin connecté se programme »

**Objet-fil** : le jardin connecté du collège (suite de C7 — concevoir le support — et C8 — le valider)
**Codes** : 4e_C9.1 · 4e_C9.2 · 4e_C9.3
**Durée** : 3 séances de 55 min — **155 min d'activités annoncées** pour 165 disponibles
**Socle évalué** : D1.3 · D2 · D4 — *D5 est du contexte, non évalué (règle n°126)*
**CRCN** : 3.4 (programmer, niveaux 2-3) · 1.3 (traiter des données, niveau 2)

---

## 1. Ce que dit le référentiel — au mot près

| Code | Formulation officielle | Verbe | Où |
|---|---|---|---|
| **4e_C9.1** | Modifier un algorithme permettant de répondre au besoin ou au problème posé. | **modifier** | Act. 2 (ajout de la plage horaire) · Act. 5 (correction par hystérésis) |
| **4e_C9.2** | Traduire un algorithme permettant de répondre à un besoin ou à un problème simple en un programme. | **traduire** | Act. 3 (algorigramme → blocs → Python) |
| **4e_C9.3** | Réaliser et mettre au point un programme commandant un système réel incluant éventuellement une interaction entre un humain et une machine. | **réaliser · mettre au point** | Act. 4, 5 et 6 |

> **Correction d'une erreur héritée.** La version précédente annonçait « concevoir »
> pour C9.1 et « réinvestir » pour C9.3. Ce ne sont pas les verbes du programme —
> et « concevoir » est un verbe de 3e. La séquence a été remise en face des bons
> codes (règles d'or n°105 et n°106), ce qui a d'ailleurs simplifié le découpage :
> chaque activité tombe naturellement sur un verbe.

**Ce que « modifier » impose en classe** : on ne demande jamais la page blanche en
4e. L'algorithme d'arrosage est **fourni** à l'activité 2, amputé de la plage
horaire ; l'élève doit trouver **où** intervenir. Beaucoup préfèrent tout
réécrire — c'est précisément le réflexe à corriger.

---

## 2. Intention et fil conducteur

Faire vivre les quatre gestes — concevoir, écrire, tester, mettre au point — sur
un objet dont l'élève connaît déjà le support, et faire découvrir que **le plus
long n'est pas d'écrire**.

Le pivot de la séquence est l'activité 5 : la pompe clignote, et **il n'y a aucun
bug**. Chaque décision du programme est juste ; c'est la règle qui est mal
choisie. Cette idée — *un programme peut être juste et inutilisable* — est ce qui
reste quand tout le reste est oublié.

---

## 3. Déroulé

| Séance | Activité | Durée | Production |
|---|---|---|---|
| **1** — Comprendre et dessiner | 1. Les deux chaînes et le relais | 20 min | Organes classés + justification écrite sur « l'heure est une entrée » |
| | 2. De la règle à l'algorigramme | 25 min | Ordre des 5 blocs + pseudo-code **modifié** |
| **2** — Écrire et tester | 3. Écrire et exécuter | 30 min | Programme enregistré + journal chiffré |
| | 4. Le jeu d'essais | 25 min | Tableau à 6 essais, ATTENDU rempli **avant** |
| **3** — Mettre au point | 5. Le clignotement | 30 min | Diagnostic + programme à trois cas + démonstration au banc |
| | 6. Le lampadaire | 25 min | Programme écrit **sans squelette** + justification chiffrée |

---

## 4. Le banc d'essai — le cœur du dispositif

Intégré à la page, **fonctionne hors connexion**, trace les manipulations.
Curseurs d'humidité et d'heure, sélecteur de règle (un seuil / deux seuils),
compteur de basculements, bouton « faire trembler la mesure ».

**La démonstration décisive tient en trente secondes** : mode UN seuil, on fait
trembler → le compteur monte à 6 ou 8. Mode DEUX seuils, on remet à zéro, **même
tremblement** → 0 ou 1. La mesure n'a pas changé d'un point ; c'est la règle qui a
changé.

> Le tremblement est une suite de valeurs **figée dans le code**, pas un tirage au
> hasard : c'est ce qui rend la comparaison honnête et reproductible d'un poste à
> l'autre.

**Cinq verrous expérientiels** : humidité variée · essai hors plage horaire ·
frontières 39 et 40 · clignotement provoqué · clignotement supprimé. Les activités
3, 4 et 5 **refusent** de se valider sans eux.

---

## 5. Les trois parcours

| Version | Ce qu'il faut | Ce qu'on y fait |
|---|---|---|
| **🅰 Matériel réel** | carte + capteur d'humidité + **module relais** + pompe 12 V à alimentation séparée | Tout, jusqu'au téléversement |
| **🅱 Simulation** | une connexion (éditeur Vittascience) | Écriture réelle du programme + banc d'essai |
| **🅲 Sans matériel** | rien | Banc d'essai + traces fournies — **mêmes validations** |

Le sélecteur de parcours, en haut de page, masque ce qui ne concerne pas l'élève
sans retirer aucune question (règle n°122).

**Sécurité (🅰)** : la carte reste en très basse tension. L'alimentation de la
pompe est branchée **par le professeur**, après relecture du câblage. Aucun
secteur 230 V n'entre dans cette séquence.

---

## 6. Les trois obstacles à anticiper

| Obstacle | Ce qu'on observe | Remédiation |
|---|---|---|
| **« Entre 6 et 10 »** | L'élève écrit `6 < heure < 10` d'un trait, comme en maths | Faire dire à voix haute : « il est **au moins** 6 h **et au plus** 10 h ». Deux affirmations, deux tests. |
| **ET / OU** | Le programme tourne sans erreur et arrose n'importe quand | Le banc, en une manipulation : sol à 90 %, 8 h. Avec OU, la pompe s'allume. Il faut le **voir**. |
| **« Cherchons le bug »** | Vingt minutes à relire un code correct | C'est le moment pédagogique : laisser chercher un peu, puis demander « et si aucune ligne n'était fausse ? ». La question 2 de l'act. 5 y amène. |

---

## 7. Évaluation — ce qui fait trace

- **Act. 2** : le pseudo-code modifié — on évalue **l'endroit** de l'intervention
  autant que le résultat (4e_C9.1) ;
- **Act. 3** : le programme enregistré + le journal chiffré (4e_C9.2, D1.3) ;
- **Act. 4** : le tableau d'essais, colonne ATTENDU remplie **avant** — c'est le
  seul indicateur fiable de la compétence « tester » ;
- **Act. 5** : le diagnostic écrit et le programme à trois cas (4e_C9.3) ;
- **Act. 6** : le lampadaire **sans squelette** et la justification chiffrée de
  l'écart entre les seuils — c'est elle qui distingue la copie du transfert.

Le **QCM** (30 questions, 10 par code, 4 illustrées, réfutation de chaque
distracteur) donne un bilan par compétence ; il sert d'entraînement autonome, pas
d'évaluation sommative.

---

## 8. Amont et aval

**Amont** — 5e : l'élève avait **testé et modifié** un programme fourni (la boîte
étiquetée). 4e, C7 et C8 : le support de capteur a été conçu puis validé.

**Aval** — 3e : les mêmes gestes se disent **écrire** et **concevoir**, et le
protocole de test devient une **recette** avec procès-verbal (lot 3e_C9.2 +
3e_C8.3, la station d'alerte cyclonique). Les deux lots forment d'ailleurs une
paire sur la chaîne d'énergie : ici la flèche d'ORDRE s'arrête sur un **relais**
(la pompe est trop gourmande) ; là-bas elle va droit sur **CONVERTIR** (la sortie
n'est qu'un voyant). C'est en les comparant que la règle devient visible.
