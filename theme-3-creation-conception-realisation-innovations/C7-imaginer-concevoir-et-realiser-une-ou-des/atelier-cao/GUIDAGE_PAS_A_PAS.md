# Guider un élève dans un logiciel — la méthode, et comment la transposer

Ce document n'est pas une séquence. C'est **la méthode de fabrication des TP de prise en main du
dépôt**, quel que soit le logiciel : Onshape, mBlock 5, un simulateur de circuits, un tableur, un
logiciel de planification. Il applique les règles d'or **n°72 à n°82**, écrites au journal le
9 août 2026 à partir d'un TP que Pascal a mené en classe et qui a marché.

La phrase à laquelle tout se mesure est la sienne :

> « C'est long, mais il arrive à être autonome et **personne ne reste sur la touche**. »

Ce n'est pas une image. C'est le critère de réussite, et il est vérifiable : à la fin de la séance,
combien d'élèves ont eu besoin du professeur pour autre chose qu'un vrai blocage ?

---

## 1. Ce qui est transposable, et ce qui ne l'est pas

**Transposable** — la structure, et elle seule :

| Élément | Onshape | mBlock 5 | Simulateur de circuits |
|---|---|---|---|
| Geste de rangement initial (n°79) | créer le document, le nommer | créer le projet, l'enregistrer sur le poste | nommer et enregistrer le schéma |
| Objet de la séance | le dé | un premier programme qui réagit | un circuit qui allume une LED |
| Premier geste dans l'espace de travail | choisir un plan, esquisser | glisser un bloc « quand drapeau cliqué » | poser un composant |
| L'état que le logiciel affiche (n°78) | esquisse **noire** = contrainte, **bleue** = libre | bloc **encastré** = exécuté, **isolé** = mort | fil **connecté** = point plein, sinon rien ne passe |
| Le geste qui se répète (n°76) | percer une face, puis les cinq autres | un événement, puis les autres événements | une branche, puis les autres branches |
| Récompense finale (n°82) | colorer le dé | faire dire son prénom au robot | faire clignoter en rythme |

**Non transposable** — le contenu, les noms de boutons, les captures. Chaque logiciel a ses mots et
ses icônes, et la règle n°73 exige qu'on les cite **exactement**. Il n'y a pas de raccourci : un TP
pour mBlock 5 se refait de zéro sur mBlock 5.

**C'est précisément pour ça que le générateur existe** : on réécrit le contenu, jamais la forme.

---

## 2. L'architecture d'un TP, en cinq temps

### Temps 0 — Ranger (n°79)
Créer le dossier, le nommer avec le nom de l'élève, enregistrer sous un nom **imposé**. Deux
minutes. Un travail qu'on ne retrouve pas à la séance suivante n'a pas eu lieu, et c'est la
première cause de séance perdue en salle informatique.

### Temps 1 — Le geste détaillé (aide maximale)
Le premier geste de chaque famille est écrit **au clic près**, avec pour chaque étape :

1. **l'action**, en noir, verbe à l'impératif, nom du bouton en gras **et son icône** (n°73) ;
2. **ce qui doit se produire**, dans un second registre visuel (n°72) ;
3. s'il y a lieu, **l'autorisation d'être imprécis** (n°74) et **la mention « c'est un exemple »**
   sur toute valeur visible dans une capture (n°75) ;
4. **l'image du résultat** en fin de palier (n°77) ;
5. **enregistrer**, avec l'icône (n°80).

### Temps 2 — Le même geste, allégé
Deuxième occurrence : on garde la numérotation et les valeurs, on retire les retours d'écran
évidents. Environ deux tiers du volume du temps 1.

### Temps 3 — Le geste réduit à son résultat (n°76)
Les occurrences suivantes tiennent en une ligne et **une image du résultat attendu**. C'est là que
l'autonomie se produit — pas parce qu'on l'a demandée, parce que l'étayage s'est retiré.

### Temps 4 — La récompense (n°82)
Un geste inutile et joli. Couleur, apparence, animation, son. L'élève repart avec quelque chose
dont il est fier, et c'est ce qu'il montrera chez lui.

**Et aucune question de cours nulle part** (n°81). On apprend l'outil, ou on évalue la notion,
jamais les deux à la fois. Les questions viennent après, dans la séquence.

---

## 3. Comment on l'écrit ici

Un TP n'est pas rédigé à la main : il est **décrit dans un fichier JSON**, puis engendré.

```bash
python3 _generation/build_tp.py scenarios/<mon_scenario>.json
python3 verif_guidage.py tp_<mon_tp>.html      # contrôle des règles n°72 à n°82
```

Le scénario décrit des **paliers**, chaque palier contient des **étapes**, et chaque étape porte
au minimum :

```json
{ "action": "Cliquez sur <b>Esquisse</b>",
  "icone": "Images/onshape_btn_esquisse.png",
  "voir": "Les trois plans apparaissent et le pointeur change de forme.",
  "avertissement": "Il n'est pas nécessaire d'être précis : les cotes viendront ensuite.",
  "exemple": true }
```

Le champ `voir` est **obligatoire** : le générateur refuse d'écrire une étape sans lui. C'est la
règle n°72 rendue mécanique — on ne peut pas oublier de dire à l'élève ce qu'il doit voir.

Le champ `niveau_aide` d'un palier vaut `detaille`, `allege` ou `resultat`, et le vérificateur
contrôle que **le niveau d'aide décroît** au fil du document (n°76). Un TP dont tous les paliers
sont `detaille` est refusé : il fait exécuter, il n'apprend pas.

---

## 4. Le critère de réussite, et comment on le mesure

À la fin de la séance, l'enseignant note trois nombres :

- combien d'élèves **ont terminé** le TP ;
- combien ont eu besoin d'aide pour **retrouver un bouton** (défaut de règle n°73) ;
- combien ont eu besoin d'aide pour **savoir s'ils étaient justes** (défaut de règle n°77).

Les deux derniers sont les seuls qui accusent le document. S'ils sont élevés, ce n'est pas la
classe qui a mal suivi : c'est le TP qui a mal guidé.

---

## 5. Les TP de l'atelier

| Niveau | Logiciel | Objet | Ce qui se retire par rapport au précédent |
|---|---|---|---|
| **5e** | Onshape | le dé | — (première prise en main) |
| **5e bis** | Onshape | le même dé, dont **un** creux devient une vraie calotte | la face à esquisser, la cote et l'extrusion ne sont plus détaillées : elles ont été faites au TP nº1 |
| **4e** | Onshape | assemblage du dé et d'un socle de style romain, **dé centré sur l'axe du socle** | l'esquisse et l'extrusion ne sont plus détaillées |
| **3e** | Onshape | le boîtier étanche du capteur de confort | la forme n'est plus donnée : elle est déduite d'un besoin |

Le quatrième est arrivé le 30/08/2026, et ce tableau ne l'a pas su pendant un jour : c'est ce
retard qui a donné `verif_effectifs.py`, lequel refuse désormais qu'un nombre écrit à côté du mot
« TP » cesse de dire vrai.

Et, hors CAO, la même méthode servira à **mBlock 5** et aux simulateurs : mêmes cinq temps, même
générateur, contenu entièrement réécrit.

---

*Le TP « Dé » de Pascal, dont cette méthode est tirée, reste sa propriété et n'est pas redistribué
ici : il a servi de modèle de **forme**, jamais de source de texte.*
