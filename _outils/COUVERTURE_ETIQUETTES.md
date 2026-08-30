# Ce que les banques évaluent vraiment — relevé corrigé

> **Correction du 31/08/2026.** La première version de ce fichier, livrée en
> #289, affirmait que sept banques du dépôt n'étiquetaient leurs questions par
> aucun code, et proposait de les réétiqueter. **C'était faux.** Les sept
> banques nomment toutes leur code, dans le dictionnaire `COMP_LABELS` que le
> gabarit maison place au-dessus de la banque. Mon outil ne lisait que le champ
> `c:` de chaque question. Il n'a pas mesuré une absence : il a mesuré sa propre
> myopie. Le relevé ci-dessous est celui qu'on obtient une fois les légendes
> lues, et la proposition de réétiquetage est retirée.

## 1. Comment une banque nomme son code

Le champ `c:` d'une question porte un mot de groupe, pas un code :

```js
const COMP_LABELS = { "PAR":"4e_C8.1 — 🖐️ Paramétrer la simulation",
                      "PRO":"4e_C8.2 — 📐 Proposer un protocole",
                      "PER":"4e_C8.3 — 📊 Comportement et performances" };
…
{ c:"PAR", n:"Le verbe de la compétence", q:"La compétence 4e_C8.1 dit…" }
```

C'est un choix de gabarit défendable : l'élève voit « 🖐️ Paramétrer la
simulation » dans son tableau de bord, pas « 4e_C8.1 ». Le code est là,
au-dessus, pour l'enseignant et pour l'audit.

Une légende peut nommer :

- **un seul code** — les questions du groupe lui reviennent en propre ;
- **plusieurs codes** (`"ID":"Information et données — 4e_C4.4 · C4.5 · C4.6"`)
  — les questions sont *partagées*, réellement couvrantes mais diluées ;
- **aucun code du programme** (`"SEU":"CRCN 3.4 · 1.3 · 5.1"`) — le groupe
  déclare travailler hors référentiel. C'est une information sur le lot, pas un
  manque.

## 2. L'état réel du dépôt

`python3 _outils/controle_couverture.py` au 31/08/2026 :

| état | codes |
|---|---:|
| ÉVALUÉ (≥ 5 questions en propre) | 51 |
| PARTAGÉ (seuil atteint par un groupe partagé) | 1 |
| CITÉ (nommé par une pièce qui enseigne ou atteste) | 8 |
| RENVOI (nommé seulement par un README ou un lexique) | 43 |
| VIDE | 11 |

L'outil indexe aussi **toutes** les banques du dépôt, parce qu'un code
mutualisé ne porte pas ses questions : elles vivent dans la banque du lot qui
l'enseigne. Résultat : **aucun renvoi orphelin.** Les 43 RENVOI et les 11 VIDE
sont tous évalués quelque part, et l'outil dit où.

Un seul code tenu pour complet ne démontre pas sa couverture par des
questions : `5e_C4.1`.

## 3. Ce qui reste vraiment

### 3.1 Six codes qu'aucune question du dépôt n'évalue

| code | intitulé | ce que le dossier porte |
|---|---|---|
| `5e_C7.2` | Fabriquer une solution pour améliorer un OST existant | `tp_5e_de_onshape.html` |
| `5e_C7.6` | Mettre en œuvre les moyens pour réaliser une forme selon une procédure fournie | `tp_5e_de_onshape.html` |
| `4e_C7.6` | Modifier une forme à l'aide d'une modélisation | `tp_4e_socle_assemblage.html` |
| `3e_C7.2` | Proposer et fabriquer un ensemble de solutions pour produire un nouvel OST | `tp_3e_boitier_etanche.html` |
| `3e_C7.6` | Modéliser une forme voulue | `tp_3e_boitier_etanche.html` |
| `5e_C8.1` | Utiliser une simulation fournie pour valider la tenue mécanique d'un matériau | un README, rien d'autre |

Les cinq premiers forment une famille : **modéliser et fabriquer**. Chacun a un
TP Onshape réel et rien d'autre — ni séquence, ni QCM, ni synthèse. Le
sixième est le seul code du dépôt dont aucune pièce, nulle part, ne parle.

### 3.2 Quatre codes évalués à quatre questions

`5e_C4.1` (dans sa propre banque) et `5e_C4.2`, `5e_C4.3`, `5e_C4.6` (dans
celle du lampadaire) sont couverts par quatre questions chacun. Le seuil
d'évaluabilité est de cinq.

La banque `qcm_5e_C4.1-C4.8_lampadaire_intelligent.html` est pourtant
irréprochable : trente-deux questions, huit codes, quatre chacun, étiquetés par
codes réels. Ce n'est pas une négligence, c'est une soustraction. Un lot
mutualisé sur huit codes **ne peut pas** donner cinq questions à chacun avec
une banque de trente.

### 3.3 Dix questions déclarées hors référentiel

`qcm_3e_C7_capteur-confort-ny.html` déclare `"SEU":"CRCN 3.4 · 1.3 · 5.1"`. Ces
dix questions — seuil, algorigramme, condition Python, boucle, mise au point —
travaillent des compétences numériques transversales, pas un code du programme
de Technologie. Le lot le dit lui-même. Rien à corriger ; il fallait le lire.

## 4. Le seul arbitrage qui reste

**Le seuil face aux lots mutualisés.** Cinq questions par code, c'est le seuil
de `controle_echantillonnage.py`. Un lot qui couvre huit codes ne peut pas le
tenir. Trois issues possibles :

1. un seuil qui dépend du nombre de codes portés par le lot, par exemple
   `min(5, questions_de_la_banque // nombre_de_codes)` ;
2. l'aveu écrit qu'un code mutualisé n'est pas « évaluable seul », et un état
   PARTAGÉ qui vaut couverture sans valoir évaluation ;
3. quatre questions de plus dans la banque du lampadaire.

Les deux autres arbitrages annoncés en #289 tombent : les prérequis (VAR, TYP,
BOI) sont rattachés à leur code par la légende de leur propre banque, et les
« neuf codes sous le seuil » n'existaient que dans mon relevé fautif.

## 5. Ce que cette erreur laisse comme méthode

L'outil sait maintenant lire les légendes, et son banc de tests contient les
deux cas précis sur lesquels je m'étais trompé — `PAR → 4e_C8.1` et
`PRO → 4e_C8.2` — pour qu'aucune version future ne puisse les reperdre en
silence.

Règle d'or n°242 : **un instrument ne prouve une absence que là où il a
regardé.** Avant de conclure qu'une chose manque, chercher l'endroit où elle
serait écrite si elle existait, et vérifier qu'on y a regardé.
