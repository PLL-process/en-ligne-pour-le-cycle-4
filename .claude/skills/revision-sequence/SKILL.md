---
name: revision-sequence
description: Réviser une séquence du dépôt en une seule passe complète, pour alléger la charge cognitive de l'élève — règles d'or à zéro (gabarit, boutons radio n°300, mode essentiel), lecture visible par séance ramenée sous 1 200 mots, texte aéré, séances de 55 min, lecture comme un élève, revue d'écran — puis une PR et la ligne du suivi. À utiliser pour la révision des trois thèmes décidée le 08/11/2026, séquence par séquence, dans l'ordre de `docs/revision/SUIVI_REVISION.md`.
---

# Révision d'une séquence : la passe complète

Décision de Pascal du 08/11/2026. « Une révision des 3 thèmes s'impose… depuis longtemps cela me paraissait une
charge cognitive. » Il retient la **passe complète par séquence** : chaque page est ouverte une seule fois et ressort
révisée sur tous les plans, au lieu d'être rouverte à chaque vague d'une règle. Ordre : carte blanche, l'urgence
d'abord — l'ordre des classeurs de progression, ce qui passe en classe le plus tôt d'abord.

Le journal fait foi. Ce skill **enchaîne** des skills qui existent ; il ne les remplace pas.

## Ce qui est mesuré, avant et après

```bash
python3 _outils/bilan_revision.py                   # les 56 séquences : mots, ✘ de règles, menus n°300, aération, état
node _outils/mesurer_charge.mjs <page>              # par séance, à 390 px : mots visibles, essentiel, écrans, champs
python3 _outils/verif_regles_audit.py <dossier>     # les ✘ de règles d'or de la page
python3 _outils/audit_aeration.py <page>            # légendes et corrections d'un seul tenant
node _outils/controle_schemas.mjs <dossier>         # schémas premium (n°315)
```

**La charge** (`mesurer_charge.mjs`) : ce que l'élève voit à l'ouverture d'une séance, sans rien déplier. Repère :
**1 200 mots visibles au plus**, soit 10 minutes de lecture seule à 120 mots par minute (un lecteur de collège sans
aisance), sur une séance de 55 minutes. Mesure du 08/11/2026 : médiane 1 134 mots, **86 séances sur 188 au-delà**,
jusqu'à 3 570 ; le mode essentiel ne retirait que 2 % du texte.

## La passe, dans cet ordre

### 1. Mesurer
Les cinq commandes ci-dessus sur la page (et ses pages engendrées), chiffres notés dans la PR.

### 2. Les règles d'or à zéro
- **Ancien gabarit** (famille C7/C8 de 4e et 5e, 4e_C6.2, 5e_C1.5) : `python3 _outils/migrer_gabarit_306.py <page>`, avec
  `etayage_<page>.json` écrit à la main (des phrases à compléter, même niveau attendu). Les bancs gardent leurs
  questions grâce au shim `_groupesRadio(page)` (voir V2, journal du 08/11/2026).
- **n°300 sur le gabarit commun** : `python3 _outils/migrer_gabarit_306.py <page> --n300` ne convertit que les listes
  déroulantes qui posent une question. Les menus voulus (cahier des charges, bête à cornes) et les menus d'interface
  (`data-interface`) restent des listes. Quand la page sauvegarde par sa propre fonction (`collect()`, `restore()`),
  l'outil le dit : on y ajoute `fieldset.qcm-groupe` à la main, comme `patcher_save` le fait pour la forme connue.
- **Des questions qui partagent leurs réponses** (« associe chaque personne… ») : `python3 _outils/grilles_radio.py
  <page> --ecrire` les range en grille (dans une incrustation d'atelier, c'est le moteur qui le fait : le widget
  `classer` se lit en grille dès trois items et trois catégories, depuis le 08/11/2026) — les réponses une fois, lettrées A, B, C ; chaque question, une rangée de lettres.
  Sans grille, la conversion n°300 écrit cinq fois les cinq réponses (5e_C1.5 : séance 2, 1 169 → 888 mots).
- **Les autres ✘** (n°23 durée, n°301 clôture, n°304 avant de commencer…) : à la main, selon leur skill.

### 3. Alléger la lecture de chaque séance
Objectif : chaque séance sous 1 200 mots visibles. **On ne retire aucune notion** : on replie, on range, on coupe le
redondant.
- **Replier ce qui ne sert qu'au besoin** dans un `<details>` dont le titre dit ce qu'il y a dedans :
  - les captures des gestes : `python3 _outils/replier_captures.py <page> --ecrire`. Chaque geste reste écrit en toutes
    lettres ; ses captures et leurs légendes se rangent dessous, « 🖼 Le voir en images — 3 captures : ce que tu dois
    voir, et que faire si ça ne marche pas » (4e_C1.1, séance 1 : 1 641 → 921 mots) ;
  - une piqûre de rappel incrustée : l'option `replie="…"` de son entrée dans `incrustations_lots/`, puis
    `python3 incrustations.py --seq <code>` (le texte du résumé dit ce qu'elle contient et à qui elle sert) ;
  - le Bonus : `python3 _outils/replier_bonus.py <page> --ecrire`. Son titre reste visible à sa place (la clôture se
    lit Bonus → Bilan → QCM) ; ses défis, ses champs et son corrigé se déplient « quand tu as fini ». Un banc qui
    remplit les champs du Bonus ouvre d'abord le `<details>`, comme l'élève ;
  - les exemples d'une consigne, les conseils d'un devoir à faire à la maison : dans un `<details>` titré ;
  - les explications qui suivent une activité (« Pourquoi ? ») ;
  - les compléments, les « pour aller plus loin ».
- **Marquer `class="approfondissement"`** ce qui n'est pas indispensable pour faire : le mode essentiel (n°29) le cache.
- **Couper le redondant** (`clean-copy`, repris dans `texte-clair-et-aere`) : une phrase qui répète un titre, une consigne
  dite deux fois, une annonce (« Dans cette activité, tu vas… » suivie de la consigne qui le dit).
- La situation déclenchante, l'hypothèse, la problématique et la clôture ne bougent pas (n°306, n°311).
- **Ne pas défaire une décision de Pascal pour tenir le repère** : une séance qu'il a voulue telle (des exercices
  ajoutés, une séance de plus) garde son contenu ; l'écart va dans le suivi, avec les pistes, et la question dans la PR.

### 4. Aérer le texte
Skill `texte-clair-et-aere` : consignes à l'impératif, 20 mots au plus, une action par ligne ; légendes en lignes ;
corrections réponse → pourquoi → refus un par ligne → le piège.
- `python3 _outils/aerer_legendes.py <page> --ecrire` et `python3 _outils/aerer_corrections.py <page> --partout --ecrire`
  posent les retours à la ligne (entre les parties d'une légende ; entre les phrases d'une correction, d'une consigne,
  d'une définition, d'une légende de plus de 35 mots ; après chaque « ; » d'une correction), sans changer un mot ; ils
  nomment ce qui reste à réécrire à la main. Ils ne touchent jamais une incrustation des ateliers : son texte se
  corrige à la source (ci-dessous).
- `python3 _outils/audit_aeration.py --strict <page>` à zéro.
- Les consignes et annonces de plus de 25 mots (« Au programme : … », la question directrice) passent en lignes ①, ②,
  ③ ou en deux phrases. `node _outils/mesurer_charge.mjs --longs 30 <page>` les cite, séance par séance.
- **Un texte d'une incrustation d'atelier** (`<!-- ateliers-representations:debut … -->`) se corrige à sa source
  (`ateliers-representations/_generation/` : `incrustations_lots/` pour l'introduction propre à la séquence,
  `donnees_<atelier>.py` pour l'exercice), puis :
  - la séquence : `python3 incrustations.py --seq <code>` (n'écrit que cette séquence, entre ses marqueurs) ; vérifier
    par `--verifier --seq <code>` (« à jour ») ;
  - les ateliers et les cahiers qui portent le même exercice : le même remplacement, à l'identique, dans leurs pages.
    **Ne jamais lancer `build.py` dans le dépôt** (il réécrit d'autres pages, sans leur mention de licence) ; pour
    vérifier qu'il produirait le même texte, le rejouer dans une copie de travail à part (`git worktree`).

### 5. Le reste du lot, vérifié au passage
- **Séances de 55 minutes** : les durées annoncées des activités tiennent dans 55 minutes (n°23).
- **Lexique** (skill `lexique-sequence`) : chaque mot technique de la séance y est, rattaché à sa séance.
- **Situation déclenchante** illustrée et glosée (`situation-declenchante-ancree`) : faite en vagues 1 et 2 (05-06/11).
- **Code en couleurs** (n°13), **schémas premium** (n°315), **chaînes d'énergie** (n°310) : leurs contrôles verts.
- **Synthèse élève** : `audit_aeration.py --strict` et deux pages A4 (`synthese-vulgarisee`).

### 6. Lire comme un élève
Ce que la lecture attentive a trouvé sur les premières séquences, à chercher partout : le « vous » (n°302) ; le style
télégraphique (« désactive géo inutile ») ; un anglicisme non expliqué (« hover ») ; un encadré qui donne d'avance la
réponse de l'exercice qui le suit ; une correction en double (même identifiant) ou une question sans correction ; un
faux titre (texte grossi) ou un `<h1>` au milieu d'une séance ; un exemple écrit deux fois.

Lire chaque séance du début à la fin, à 390 px, comme un élève de 5e qui lit mal. Noter les trois endroits où il
décroche (mot inconnu, phrase trop longue, consigne ambiguë, aller-retour dans la page) ; les corriger.

### 7. Vérifier et livrer
- Les bancs du lot (`tests_*`), lancés comme d'habitude ; un échec présent sur `main` est dit, pas caché.
- Les contrôles du site touchés (`controle_squelette`, `controle_mode_essentiel`, `controle_hierarchie`,
  `controle_impression`, `controle_liens`, `controle_tactile`, `controle_licence`).
- **Revue d'écran en trois tours** (`controle-qualite-lot`) : 390 et 1 280 px, mode essentiel compris.
- Une PR par séquence (ou par deux ou trois petites), le journal, et la ligne de `docs/revision/SUIVI_REVISION.md` :
  avant → après pour les mots de la séance la plus lourde, les ✘, les menus, l'aération ; « livrée #PR ».

## Critères de réussite

- [ ] `verif_regles_audit.py` : 0 ✘ sur la page.
- [ ] `audit_aeration.py --strict` : 0.
- [ ] `mesurer_charge.mjs` : chaque séance sous 1 200 mots visibles, ou l'écart justifié dans le suivi (une séance-projet
      qui donne un dossier à lire, par exemple).
- [ ] Aucune notion, aucune correction, aucune question retirée : ce qui sort de la vue est replié, pas supprimé.
- [ ] Les bancs et les contrôles verts, ou les échecs anciens nommés.
- [ ] La revue d'écran faite, les captures dans la PR.
- [ ] La ligne du suivi mise à jour.
