---
name: synthese-vulgarisee
description: Écrire ou réécrire une synthèse élève du dépôt pour qu'un élève de 6e la comprenne seul (règle d'or n°316) — carte « Ce que je dois retenir » en tête, puis chaque partie en cinq temps (titre-question, en une phrase, comme dans la vie, dans notre séquence, les mots, le piège, vérifie-toi). À utiliser pour toute synthèse élève, neuve ou existante.
---

# Synthèse vulgarisée (règle d'or n°316)

Créé le 29/10/2026, à la demande de Pascal : « je trouve que les synthèses ne sont pas assez vulgarisées », en
montrant la partie 5 de `5e_C1.1` (Chengdu). Modèles qu'il a désignés : les synthèses de **Pascal Pujades**, surtout,
celles des académies de **Toulouse** (« un bon exemple ») et de **Bordeaux**.

Le journal fait foi (règle d'or n°10) : le texte complet de la règle est à « Règle d'or n°316 » dans
`JOURNAL_DES_DECISIONS.md`. Ce skill dit comment l'appliquer.

## Ce qui ne va pas, et ce que les formules ne voient pas

Les synthèses du dépôt ont des phrases courtes : un calcul de lisibilité (Kandel-Moles) les classe « très faciles »
(médiane 86). Le défaut est ailleurs : elles sont **abstraites et elliptiques**, écrites comme des maximes.

- « Stockage : le fichier est déposé. Il conserve, il ne juge pas. » — juste, mais il faut déjà avoir compris pour le lire.
- Aucun exemple de la vie de l'élève ; les mots techniques sont posés, pas expliqués.

**Vulgariser, c'est expliquer avec ce que l'élève connaît déjà**, pas raccourcir les phrases.

## Ce qu'on prend aux modèles (et ce qu'on n'en prend pas)

- **Toulouse, fiches de synthèse 2024** (`pedagogie.ac-toulouse.fr/sii/fiches-de-synthese-2024`) — une page A4 paysage,
  « Ce que je dois retenir » : un titre au centre, quatre à six blocs autour, chacun avec un titre en pastille, une ou
  deux phrases, un pictogramme, un exemple concret (« Logique : froid / chaud — Analogique : 32 °C »), un chiffre sourcé.
  Très visuel, très peu de texte. **Principe affiché** : la fiche vient d'un **bilan fait en classe après les
  activités** ; elle n'est jamais donnée sans ce travail. → On en prend la **carte en tête de synthèse**.
- **Toulouse, fiches de connaissances 2024** (`…/sii/CF-2024`) — 2 à 3 pages : le tableau des connaissances du
  programme 2024 (OST, SFC, CCRI) en tête, des définitions « Le capteur est un composant qui… », une phrase-clé
  (« le signal transporte l'information »), des comparaisons en deux colonnes (logique / analogique) avec un exemple
  chacune, un seul fil d'exemple (le robot de téléprésence), une capsule audio de 5 minutes. → On en prend
  **la définition suivie d'un exemple**, **la comparaison en deux colonnes**, **le fil d'exemple unique**.
  On n'en prend pas : le « il faut » impersonnel, les paragraphes de cinq lignes, et on **vérifie les faits** (une fiche
  y écrit « les 3 fonctions d'une chaîne d'énergie : acquérir, traiter, communiquer » : c'est la chaîne d'information).
- **Pujades** — chaque synthèse est **titrée par une question** (« Comment récupérer l'eau de pluie et l'utiliser ? »)
  et ponctue la séquence, après les séances qu'elle résume. → **Le titre de chaque partie est une question.**
- **Bordeaux, fiches de structuration des connaissances** — une fiche par connaissance du programme, donnée **après**
  les activités et **commentée avant l'évaluation**. → La synthèse s'appuie sur ce que la séquence a fait faire, et
  sert à réviser.

Aucun texte de ces fiches n'est recopié : on en prend la forme, jamais les phrases ni les images (n°1 : nos images
sont originales, CC0).

## La forme

### 1. La carte « Ce que je dois retenir » (en tête de page)

Une grille de cartes HTML (pas une image) : au centre ou en tête, **la question de la séquence** ; autour, **une carte
par partie** (4 à 6) avec un pictogramme, le titre-question de la partie et **sa réponse en une phrase**. Chaque carte
est un lien vers sa partie (`#partie-N`). Elle tient seule sur une page A4 à l'impression. Elle obéit à la n°315 :
aucune carte n'en touche une autre, aucun texte ne déborde.

### 2. Chaque partie, en cinq temps

```
<div class="bloc savoir">
  <h2 id="partie-5">5. Comment une donnée voyage-t-elle, et qui a le droit d'y toucher ?</h2>   ← titre-question
  <p class="une-phrase">🎯 <b>En une phrase</b> : …</p>                                          ← 1
  <p class="comme-vie">🏠 <b>Comme dans la vie</b> : …</p>                                       ← 2
  … l'exemple de la séquence, avec son schéma (n°315) …                                         ← 3
  <dl class="voc">… les mots …</dl>                                                             ← 4
  <p class="piege">⚠️ <b>Le piège</b> : …</p>                                                    ← 5
  <details class="verifie"><summary>✅ Vérifie-toi : …</summary> la réponse expliquée </details>
</div>
```

1. **En une phrase** — l'idée à retenir, en mots de tous les jours. Si on ne sait pas l'écrire en une phrase, la
   partie mélange deux idées : la couper.
2. **Comme dans la vie** — une comparaison avec ce que l'élève vit déjà : le collège (cantine, notes, casier,
   emploi du temps), la maison, la rue, la Martinique (cyclone, sargasses, coupure de courant). Une seule, bien choisie,
   menée jusqu'au bout. Elle doit être **juste** : si la comparaison trompe sur un point, le dire (« sauf que… »).
3. **Dans notre séquence** — l'exemple que l'élève a manipulé (la station de Shenzhen, l'air de Chengdu…), pas un
   nouveau. Les étapes numérotées, une phrase chacune. Le schéma de la séquence, premium (n°315).
4. **Les mots** — chaque mot technique de la partie : **mot** (EN : *word*) — définition en une phrase simple — un
   exemple. Le vocabulaire anglais du skill `sequence-pedagogique-engageante` reste là.
5. **Le piège** — l'erreur que font vraiment les élèves (celle que le QCM et les aides de la séquence ciblent), dite
   simplement, avec pourquoi c'est faux.
6. **Vérifie-toi** — une seule question, concrète, dont la réponse est cachée (`<details>`) et **expliquée** (pas
   seulement « réponse B »).

### 3. La langue

- **Tu**, voix active, présent. Phrases de 15 mots en moyenne ; aucune au-delà de 25.
- **Un mot technique est expliqué la première fois qu'il paraît**, dans la phrase même ou dans « Les mots ».
- **Pas de maximes** : « Il conserve, il ne juge pas » devient « Le fichier garde les mesures. Il ne vérifie pas si
  elles sont justes. » Ce qui est sous-entendu s'écrit.
- **Du concret avant l'abstrait** : l'exemple d'abord, la règle ensuite.
- Unités en toutes lettres à la première apparition (n°312), sigles en capitales (n°313).
- Le test : **un élève de 6e lit la partie seul, puis l'explique avec ses mots**. S'il bute sur un mot ou une
  phrase, on réécrit.

## Ce qui ne bouge pas

- **Les ancres `id="partie-N"`** : les blocs « Avant de commencer » (n°304), les billets d'entrée (n°26) et les liens
  de rattrapage y renvoient. Une partie coupée en deux garde son ancre sur la première moitié.
- **Toutes les notions** que la séquence, le QCM et la synthèse professeur supposent : on explique mieux, on n'enlève
  rien. La synthèse professeur, elle, reste technique.
- La page : la navigation, le bouton d'impression, les règles n°135, n°303 ; à l'impression, la carte sur la première
  page, puis les parties, `<details>` ouverts (`@media print`), **deux pages A4 au plus** pour les parties.

## Avant de livrer

- [ ] La carte en tête : une carte par partie, sa phrase, son lien ; tient sur une page A4.
- [ ] Chaque partie : titre-question, en une phrase, comme dans la vie, l'exemple de la séquence, les mots (FR + EN),
      le piège, vérifie-toi (réponse expliquée).
- [ ] Aucun mot technique sans explication ; aucune phrase au-delà de 25 mots ; aucune maxime.
- [ ] Chaque comparaison est juste, ou dit où elle s'arrête ; chaque fait est conforme à la séquence et au programme 2024.
- [ ] Les ancres `#partie-N` intactes ; `python3 _outils/controle_liens.py` vert.
- [ ] Les schémas : `node _outils/controle_schemas.mjs <dossier Synthèses>` sans ✘ (n°315).
- [ ] `controle_impression.mjs`, `controle_impression_papier.py`, `controle_unites.py`, `controle_sigles.py`,
      `controle_regles_visibles.py` identiques à `main` ou meilleurs.
- [ ] Rendu regardé à 390 px et à l'impression (capture).

## Exemple : la partie 5 de `5e_C1.1` (Chengdu)

**Avant**

> **5. Le chemin de la donnée, et les droits**
> Un système d'information, ce sont des personnes, des outils et des règles — les trois, ou ce n'en est pas un.
> Source : le capteur mesure. Il ne décide de rien. Personne n'écrit ici. Stockage : le fichier est déposé. Il
> conserve, il ne juge pas. […] Savoir qui a le droit d'écrire, c'est savoir où chercher quand quelque chose a changé.

**Après**

> **5. Comment une donnée voyage-t-elle, et qui a le droit d'y toucher ?**
>
> 🎯 **En une phrase** : une donnée fait un voyage en quatre étapes, et à chaque étape, seules certaines personnes ont
> le droit de la modifier.
>
> 🏠 **Comme pour tes notes** : le professeur corrige ta copie, il recopie la note dans le logiciel, le logiciel calcule
> ta moyenne, puis le bulletin part chez toi. Si la note est mal recopiée au début, la moyenne et le bulletin seront
> faux aussi.
>
> **À Chengdu, les quatre étapes**
> 1. **La source** : le capteur mesure l'air. Il ne choisit rien, il ne corrige rien.
> 2. **Le stockage** : le fichier garde les mesures sans les vérifier. Seuls le professeur et l'administrateur y déposent.
> 3. **Le traitement** : on trie, on enlève les valeurs impossibles, on calcule. C'est là que la donnée devient une
>    information… donc là qu'on peut se tromper. La classe travaille sur une copie.
> 4. **La diffusion** : le graphique est publié. Seul le professeur publie.
>
> **Les mots** — **système d'information** (EN : *information system*) : des personnes, des outils et des règles qui
> font circuler les données. Exemple : le capteur, le fichier, le tableur, et qui a le droit de faire quoi.
>
> ⚠️ **Le piège** : croire que l'ordinateur corrige les erreurs tout seul. Une valeur fausse au départ reste fausse
> jusqu'au bout, tant qu'une personne ne l'enlève pas.
>
> ✅ **Vérifie-toi** : ta copie dit 12, ton bulletin dit 2. À quelle étape chercher d'abord ? — *Au stockage : la note a
> été mal recopiée. Le calcul de la moyenne était juste, mais il est parti d'une valeur fausse.*
