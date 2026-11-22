---
name: texte-clair-et-aere
description: Écrire ou réécrire le texte que lit l'élève pour qu'il soit clair et aéré — consignes, explications, légendes sous les images, corrections — avec une idée par ligne et le retour à la ligne là où il faut, sans rien retirer du fond (corrections exhaustives). Mesure avec `_outils/audit_aeration.py`, passe mécanique sur les légendes avec `_outils/aerer_legendes.py`. À utiliser en rédigeant une séquence, une synthèse ou une correction, et sur toute page signalée par l'audit.
---

# Texte clair et aéré

Créé le 08/11/2026, à la demande de Pascal : « des skills qui ordonnent et aèrent mieux certains paragraphes,
notamment quant aux textes au-dessous des images ; bien souvent un retour à la ligne est nécessaire, dans les
corrections, etc. », puis : « on devrait chercher et modifier en l'améliorant ces skills ».

Ses élèves lisent mal, même en 3e (constat de septembre 2026). Un bloc de 80 mots sous une capture, ou une correction
cousue de points-virgules, ils ne le lisent pas : ils sautent. Le fond est bon. C'est la forme qui le cache.

## D'où viennent les idées (rien n'est installé, tout est réécrit)

Inspectés en lecture seule le 08/11/2026 ; verdicts dans `SKILLS_AUDIT.md`.

| Source | Ce qu'on en prend |
|---|---|
| `francais-simple` — sachahjkl/skills (MIT), d'après l'ASD-STE100 | consigne et explication séparées ; 20 mots par consigne, 25 par explication ; une action par phrase ; la condition avant l'action ; la table du remplissage |
| `refine-prose` et `clean-copy` — petekp/claude-skills (MIT) | l'ordre du lecteur : la réponse d'abord, les raisons ensuite ; un mouvement par paragraphe ; couper la légende qui répète ce que l'image ou l'étiquette dit déjà |
| `assessment-design` — savvides/idstack (MIT) | la correction élaborée : dire **pourquoi** c'est juste et pourquoi l'erreur tente, pas seulement « bonne réponse : B » (Wisniewski, Zierer et Hattie, 2020 ; Nicol et Macfarlane-Dick) |
| `writing-clearly-and-concisely` — obra/the-elements-of-style (domaine public, Strunk) | une idée par paragraphe, la phrase-repère en tête, la voix active |
| `practical-typography` — ckorhonen/claude-skills (MIT, Butterick) | une ligne de texte se lit entre 45 et 90 caractères : au-delà, l'œil se perd |

Ce qu'on n'en prend pas : le style télégraphique, le « tout couper » (Pascal veut des corrections **exhaustives**),
la chasse aux tics de l'IA en anglais, les polices.

## Deux sortes de texte

| | Consigne (ce que l'élève fait) | Explication (ce que l'élève comprend) |
|---|---|---|
| Forme | impératif : « Clique sur OK. » | présent : « Le tableur recalcule la cellule. » |
| Longueur | 20 mots par phrase au plus | 25 mots par phrase au plus |
| Unité | une action par phrase, une phrase par ligne | une idée par phrase, une idée par ligne |
| Plus de deux étapes | liste numérotée ①, ②, ③ ou 1., 2., 3. | puces • ou ①, ②, ③ si l'ordre compte |

Ne mélange pas les deux sur une même ligne. Une explication glissée dans une consigne passe à la ligne suivante.

Ces longueurs se mesurent (veille du 15/11/2026, idée prise de `jgsystemsconsulting/plain-language`, MIT, réécrite) :
`python3 _outils/audit_aeration.py --phrases <page>` compte les **paragraphes de plus de 4 phrases** (P1) et les
**phrases trop longues** (P2 : plus de 20 mots si elle commence par un impératif, plus de 25 sinon). C'est une mesure,
hors `--strict` : le découpage en phrases est mécanique, chaque ⚠ se relit.

## Les règles d'écriture

1. **Une idée par phrase.** Une phrase qui en porte deux se coupe en deux, à la conjonction.
2. **La condition avant l'action.** « Si la fenêtre s'ouvre ailleurs, clique sur Documents », pas l'inverse.
3. **Un seul mot pour une chose** dans toute la page (« séparateur », pas « séparateur » puis « délimiteur »).
4. **Pas de point-virgule entre deux idées sur une ligne** : deux phrases, ou deux lignes. Dans une liste verticale,
   chaque item finit par « ; » et le dernier par « . » (usage français) : c'est permis, chaque item a sa ligne.
5. **Pas de chaîne de flèches** dans une phrase : plus de trois « → » ou « · » veulent une liste. Exception : la
   **ligne de vérification** (« La trottinette → à qui ? Léa ✔ → sur quoi ? elle seule ✘ → « sur quoi ? » ») reste
   sur une ligne, une ligne par objet : elle se lit comme une ligne de tableau.
6. **Le repère en tête de ligne** : un gras de trois mots au plus (« Ce que tu dois voir : », « Pourquoi : »,
   « Le piège : »). L'œil saute de repère en repère (règle d'or n°307, `controle_hierarchie.py`).
7. **Le remplissage se coupe** :

| Éviter | Écrire |
|---|---|
| afin de | pour |
| dans le cas où | si |
| il est important de noter que | (rien : donner le fait) |
| permettre de | un verbe direct (« sert à », « peut ») |
| au niveau de | dans, sur, pour |
| etc. | nommer ce qui compte |
| simplement, facilement | (rien, ou montrer pourquoi c'est simple) |

8. **Ce qui ne bouge jamais** : les mots techniques expliqués (n°312, lexique), les valeurs, les noms de menus et de
   boutons, le code, les citations. Aérer, ce n'est pas réécrire le fond.

## Une consigne : une action par ligne (règle d'or n°342, 18/11/2026)

Demande de Pascal : « Chaque consigne doit être à la ligne. » Une consigne qui demande plusieurs actions les donne
chacune sur sa ligne, numérotée dans l'ordre où l'élève les fait ; jamais enchaînées par « ; », « , puis »,
« ensuite » ou deux phrases à l'impératif sur la même ligne. La phrase de contexte ouvre la consigne, sur sa ligne.

```
<div class="consigne"><b>Consigne :</b> Météo-France recalibre ses niveaux : le seuil orange passe à 60 km/h.<br>
① Dans le programme de la station, modifie la ligne 2.<br>
② Réponds aux questions.</div>
```

- Des étapes qui se suivent : ①, ②, ③ ; des parties d'un même travail : a), b), c).
- Un bout de code à recopier va sur ses propres lignes, tel qu'il s'écrit (`<code style="white-space:pre">`, une ligne
  par ligne de code, indentation comprise).
- « Observe et décris » peut rester d'un tenant ; « recopie le tableau et complète-le avec tes mesures » se coupe
  (`controle_consignes_a_la_ligne.py`, N3 : à juger).
- Une liste d'actions séparées par des virgules (« exécute les tests, compare, rends ton verdict ») se coupe aussi ;
  un circonstant (« Pour chaque essai, compare… ») n'est pas une action.
- Des sous-étapes dans une partie a) se numérotent ①, ② sous elle ; on ne renomme pas les lettres d'une consigne
  quand des titres d'exercice les reprennent (« a) et b) Le tableau d'essais »).
- `consignes_a_la_ligne.py` fait la passe mécanique : un retour avant chaque action, son numéro, le « ; », le
  « puis » ou l'« ensuite » qui la cousait retiré, la capitale ; aucun autre mot ne change. Il nomme (✋) la ligne à
  reprendre à la main : coupure dans un gras, ligne déjà numérotée, plus de trois actions. Une page engendrée
  (`3e_C9.2`) se corrige dans sa source, puis se régénère. Un exercice d'atelier incrusté dans une séquence
  (`section.atelier-incruste`, entre les marqueurs `ateliers-representations:debut/fin`) se corrige dans
  `ateliers-representations/_generation/donnees_*.py`, puis `incrustations.py` ; `incrustations.py --verifier` le dit.
- Pilote : `3e_C6.1` (18/11/2026) ; vague 1 : les séquences des trois thèmes (18/11/2026).

## Aérer une légende (le texte sous une image)

L'anatomie, une partie par ligne :

```
<b>Ce que tu dois voir :</b> ce que l'image montre, en une ou deux phrases.<br>
Si tu vois autre chose : la variante acceptée, ou ce qu'il faut faire.<br>
<b>Puis :</b> l'action suivante.<br>
<i>La note : ce que l'image ne montre pas, ou « DUPONT est un exemple ».</i>
```

- Trois choses à voir : « trois choses. » puis ①, ②, ③, une par ligne.
- « Si tu vois ceci : » (l'erreur) se lit en trois lignes : le symptôme, la cause, la réparation.
- La mention « Image générée par IA (Canva) » et le crédit d'une image ont leur ligne, à la fin.
- Une légende ne répète pas ce que l'image ou son titre disent déjà (`clean-copy`) : on coupe la phrase, pas le mot.
- Au-delà de 35 mots d'un tenant, elle se coupe (`audit_aeration.py`, L1).

## Aérer une correction

Pascal veut des corrections exhaustives : on garde tout, on le range. L'ordre, une partie par ligne :

1. **La réponse**, en tête : « Une seule solution passe les quatre exigences : S1, le vélo-cargo. »
2. **Pourquoi**, une étape par ligne. Un calcul : une ligne par transformation, le même nombre suivi de bout en bout.
3. **Les réponses refusées**, une par ligne, chacune avec sa raison : « • « elle l'a acheté » → celui qui paie n'est
   pas toujours celui à qui l'objet rend service. »
4. **Le piège** : pourquoi l'erreur tente (« la voiture fait le transport, mais elle ne respecte pas tout le but »).
5. **Pour la prochaine fois** : le geste à retenir, en une ligne.

Un bloc de plus de 45 mots d'un tenant se coupe (C1) ; deux « ; » qui cousent des idées, ou plus de trois « → »,
se mettent en lignes (C2).

## Un listing tient à 390 px (règle d'or n°364, 21/11/2026)

Ce qui défile est caché : à 390 px, l'algorithme du débogage du TP `4e_C6.2` défilait et cachait « 50 lux », la valeur
du seuil, sans que rien le dise. Un listing, une formule, un pseudo-code se coupent **là où le sens le permet** :

```
  SI présence = oui OU
     luminosité < 50 lux
```

- couper après l'opérateur (OU, ET, +, une virgule), et décaler la suite sous ce qu'elle prolonge ;
- un tableau trop large garde son filet (n°135) et dit « ↔ fais glisser » ; un cadre qui défile est atteignable au
  clavier (`tabindex="0"` et un nom) ;
- un retour à la ligne `<br>` garde un espace devant lui : le lecteur d'écran lit le `textContent`, qui collerait
  sinon « alimentation2. dévisser » ;
- contrôle : `node _outils/controle_page_ouverte.mjs <page>` (L), page ouverte, corrections comprises — **il refuse
  (sortie 1) depuis le 22/11/2026** : plus aucun listing ne défile sur le site, un nouveau ne passe pas.

## Les outils

```bash
python3 _outils/audit_aeration.py                    # tout le site : légendes (L1, L2) et corrections (C1, C2), par page
python3 _outils/audit_aeration.py <page>…            # chaque écart cité
python3 _outils/audit_aeration.py --strict <page>…   # sortie 1 s'il reste un écart (page livrée, page pilote)
python3 _outils/aerer_legendes.py <page>… [--ecrire] # un <br> devant « Puis : », la note finale, ①… ; ne change aucun mot
python3 _outils/aerer_corrections.py <page>… [--ecrire]  # un <br> entre les phrases d'une correction, après chaque « ; »
python3 _outils/controle_consignes_a_la_ligne.py [--strict] [page…]  # n°342 : N1 étapes numérotées sur une ligne, N2 actions enchaînées, N3 « et » (à juger)
python3 _outils/consignes_a_la_ligne.py <page>… [--ecrire]         # n°342 : la passe mécanique — un retour et un numéro par action ; nomme ce qui se fait à la main
```

`aerer_legendes.py` ne touche que les légendes et n'ajoute que des retours à la ligne : il règle tout L2.
`aerer_corrections.py` (08/11/2026, révision des trois thèmes) fait de même dans les corrections : il passe à la ligne
entre les phrases d'un bloc C1 (une ligne d'au moins 12 mots, sauf un repère court en tête) et après chaque « ; » d'un
bloc C2. Il ne change aucun mot et nomme la phrase seule de plus de 45 mots, à réécrire à la main. L1, le reste de C1
et C2 se réécrivent à la main, avec les règles ci-dessus. Une page engendrée (3e_C9.2, ateliers des représentations) se
corrige dans sa source, puis se régénère ; si le générateur réécrirait d'autres pages (dérive déjà notée par l'audit),
on corrige à l'identique la source et les pages, sans régénérer.

## Le pilote

`5e_C3.1` (Shanghai), aéré le 08/11/2026 : 21 légendes et 11 blocs de correction réécrits, deux lignes de vérification
gardées telles quelles, `--strict` à zéro. C'est le
modèle : la forme exacte des légendes (« Ce que tu dois voir », « Si tu vois ceci », « Puis », la note) et des
corrections (réponse, refus un par ligne, pourquoi en lignes).

## Avant de livrer

- [ ] `audit_aeration.py --strict` à zéro sur les pages touchées.
- [ ] Aucun mot du fond retiré : relire la correction avant et après, chaque idée est toujours là.
- [ ] Chaque consigne : impératif, 20 mots au plus, une action par ligne, la condition d'abord (`audit_aeration.py --phrases` : aucun P2 de consigne sur les pages touchées, ou chaque P2 relu ; `controle_consignes_a_la_ligne.py --strict` à zéro, n°342).
- [ ] Chaque légende : une partie par ligne, la note et la mention IA en fin, rien de ce que l'image dit déjà.
- [ ] `controle_hierarchie.py`, `controle_mode_essentiel.py` et les bancs du lot inchangés ou meilleurs.
- [ ] Rendu regardé à 390 px : aucune ligne réduite à un mot orphelin sous une image.
- [ ] Une synthèse touchée tient toujours sur ses deux pages A4 (`mesurer_impression.py`, n°316).
