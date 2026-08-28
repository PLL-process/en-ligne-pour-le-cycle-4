# Les dix QCM que l'audit ne savait pas lire

Trente-six QCM du dépôt portent une banque `const QUESTIONS = […]`, et l'audit
les mesure. Dix n'en portent pas. Ils étaient déclarés **non mesurés** — jamais
« sains » (règle n°146). Ce document est ce qu'on trouve quand on va les
regarder.

## Comment on les lit maintenant

Ces dix pages n'ont pas un moteur, elles en ont **cinq**. Écrire cinq
analyseurs de texte aurait été cinq occasions de se tromper, et il en aurait
fallu un sixième au prochain QCM écrit autrement.

`lecteur_qcm_dom.mjs` change de point de vue : au lieu de lire le code qui
fabrique les questions, il **ouvre la page et lit les questions** — celles que
l'élève a sous les yeux. Cinq stratégies, essayées dans l'ordre, et chaque
question lue déclare par laquelle elle l'a été.

| Stratégie | Ce qu'elle exploite | QCM lus |
|---|---|---:|
| `checkMCQ('q1','v0',…)` | la bonne réponse est la **valeur** du radio | 5 |
| `checkQcm(0, 2, …)` | la bonne réponse est un **rang** | 1 |
| table globale `{ q1:{correct:"B"} }` | table des réponses à part | 1 |
| banque JS d'une autre forme | `[{q, options, answer}]` | 1 |
| marqueur `✔️` visible | la page n'a aucun code | 1 |

**Dix sur dix se lisent.** Le lecteur a d'abord échoué sur deux d'entre eux :
un `const` au premier niveau d'un `<script>` classique n'est pas une propriété
de `window`, et `Object.getOwnPropertyNames(window)` ne le voit pas. La donnée
était là, sous le nez de l'outil, qui regardait au mauvais endroit.

---

## Ce que la mesure a trouvé

### 1. Le défaut principal n'était pas la longueur

| QCM | bonne réponse en A |
|---|---|
| `qcm_numerique_societe` | **21 / 21** |
| `qcm_cybersecurite_usage_raisonne` | **20 / 20** |
| `qcm_jardin_connecte` | **21 / 21** |
| `qcm_python_variables` | **21 / 21** |
| `qcm_ecall_chaine_information` | **30 / 33** |

Cocher la première proposition sans rien lire donnait **100 %** sur quatre de
ces QCM. Le biais de longueur demande au moins de comparer les propositions ;
celui-ci ne demande rien du tout.

### 2. Un QCM qui répétait la même question vingt-neuf fois

`qcm_automatisation_premium.html` annonçait « 40 questions uniques ». Il en
contenait **onze**. Une boucle `while(questions.length < 40)` poussait la même
question — même énoncé, même bonne réponse — jusqu'à 40, et la note se
calculait sur 40. Voir la règle n°155.

### 3. Le biais de longueur, tout de même

**203 des 254 questions** avaient pour bonne réponse la plus longue (80 %),
122 de façon visible.

---

## Après

| QCM | thème | lu par | q | plus longue | visible | A/B/C/D |
|---|---|---|---:|---:|---:|---|
| `qcm_numerique_societe` | 1 | checkMCQ | 21 | 16 | 0 | 6/5/5/5 |
| `qcm_cybersecurite_usage_raisonne` | 1 | checkMCQ | 20 | 13 | 0 | 5/5/5/5 |
| `qcm_fonctionnement_objet` | 1 | table globale | 25 | 13 | 0 | 7/6/6/6 |
| `qcm_automatisation_premium` | 2 | banque JS | 11 | 7 | 0 | 5/3/3/– |
| `qcm_ecall_chaine_information` | 2 | checkMCQ | 33 | 16 | 0 | 9/9/8/7 |
| `qcm_xxl_40_reseaux…zigbee` | 2 | checkMCQ | 51 | 34 | 0 | 20/20/11/– |
| `qcm_algorigrammes_domotique` | 2 | checkQcm | 2 | 1 | 0 | 1/1/–/– |
| `qcm_eclairage_automatique` | 2 | marqueur ✔️ | 20 | 9 | 0 | 5/13/2/– |
| `qcm_jardin_connecte` | 2 | checkMCQ | 21 | 13 | 0 | 6/5/5/5 |
| `qcm_python_variables` | 3 | checkMCQ | 21 | 6 | 0 | 6/5/5/5 |
| **total** | | | **225** | **129 (57 %)** | **0** | |

Les tirets marquent les questions à deux ou trois propositions : il n'y a pas
de D à distribuer. La répartition y est uniforme **à l'intérieur de chaque
taille** — c'est la seule cible qui ait un sens.

Le total passe de 254 à 225 questions : les vingt-neuf clones ont disparu.

---

## Trois choses qui ne sont PAS réglées, et qui demandent une décision

### `qcm_eclairage_automatique` affiche ses réponses

Chaque proposition juste porte un `✔️` **visible**, et la correction détaillée
est imprimée juste en dessous, sans rien à cliquer. Ce n'est pas un QCM : c'est
un **corrigé**. Il est parfaitement utile comme tel — mais alors il doit le
dire dans son titre, et cesser d'être compté parmi les QCM. L'autre voie est
d'en faire un exercice : masquer le `✔️` et les corrections derrière un bouton.

Le choix est pédagogique, pas technique : il n'a pas été fait ici.

### `qcm_automatisation_premium` : vingt-neuf questions à écrire

La boucle est retirée, le QCM annonce et note sur onze questions. Écrire les
vingt-neuf autres est un travail d'auteur. Il n'a pas été fait à la sauvette.

### `qcm_xxl_40` : onze questions à deux propositions

Une question à deux propositions se joue à pile ou face : 50 % sans rien
savoir. Ce n'est pas un défaut de longueur et rien n'y a été touché — mais
c'est un choix, et il vaut mieux qu'il soit décidé que subi.

---

## Comment refaire la mesure

```bash
node lecteur_qcm_dom.mjs <fichier.html> [autres…]     # JSON par fichier
node audit_qcm_trois_themes.mjs                       # les 36 à banque standard
```

Les deux outils partagent désormais le même indicateur : « visiblement la plus
longue » exige un écart **relatif** d'au moins 20 % ET un écart **absolu** d'au
moins 8 caractères (règle n°154).
