---
name: "situation-declenchante-ancree"
description: "Rédige la situation déclenchante, l'hypothèse de départ et la problématique d'une séquence du dépôt en-ligne-pour-le-cycle-4 (technologie collège, programme 2024), ancrées en Martinique ou dans la ville du thème, avec son image réaliste et ses mots techniques glosés, conformes aux règles d'or n°298, 304, 305, 306, 311, 315 et aux décisions des 05-06/11/2026. À utiliser au tout début d'un lot, avant le squelette de séquence."
---

# Situation déclenchante ancrée

Origine : idée n°2 de la liste Grok du 07/11/2026, reprise et branchée sur la
méthode Fable, le registre des règles d'or et les deux vagues « situations
déclenchantes illustrées » du journal (05 et 06/11/2026). Ce skill produit
**l'ouverture** d'une séquence ; le reste de la page suit
`sequence-pedagogique-engageante`.

## Avant tout : le journal fait foi (règle n°10)

1. Partir d'un `main` du jour ; lire les entrées postérieures à ce skill et le
   registre central. Toute règle postérieure l'emporte.
2. Lire la fiche de la compétence visée dans `_ressources-communes/`
   (programme 2024, BO n°9 du 29/02/2024) et la progression du niveau dans
   `_progressions/` : la situation sert la sous-compétence `<niveau>_Cx.y`
   du lot, pas l'inverse.
3. Vérifier qu'aucune séquence du même niveau n'a déjà le même objet avec la
   même problématique (`audit_couverture.*`, skill `mutualisation-couverture`).

## Entrées attendues

- Code de la sous-compétence (ex. `4e_C2.2`) et son intitulé officiel verbatim.
- Niveau, thème et ville du thème (Thème 1 · Chine, Thème 2 · Martinique,
  Thème 3 · New York).
- Objet-fil du niveau, sauf décision contraire au journal : 5e lampadaire
  intelligent · 4e jardin connecté · 3e station d'alerte cyclonique
  (ex. vélo-cargo pour 5e_C2.1, décision d'octobre 2026).
- Nombre de séances et créneaux `S<n>` du classeur de progression.

## Procédure

### 1. Trouver la personne qui a un problème
La situation part toujours d'**une personne réelle** qui appelle l'élève à
l'aide : gardien du collège, agent de la mairie, animateur du club, gérant
d'une exploitation, régie d'un réseau de la ville du thème. L'élève devient
l'expert·e qu'on sollicite. Jamais « imagine que… », jamais de problème
abstrait sans commanditaire.

### 2. Ancrer dans un lieu nommé, avec des faits vrais
- Thème 2 : commune, quartier ou établissement de Martinique nommés, avec
  un fait vérifiable (relief, saison cyclonique, sargasses, vigilance
  météo, réseau électrique insulaire).
- Thèmes 1 et 3 : la ville du thème, avec un fait documenté dans
  `_ressources-communes/` ou `SOURCES_MEDIAS.md`. Un chiffre est sourcé ou
  annoncé comme **ordre de grandeur** ; aucune donnée inventée présentée
  comme vraie.

### 3. Gloser les mots techniques dans la phrase même
Décision du 05/11/2026 : chaque mot technique que la situation pose reçoit
son explication **dans la phrase**, pas dans une note (« l'électrovanne, la
vanne qui s'ouvre à l'électricité » ; « on l'entend claquer depuis la classe »).
Le mot entre ensuite au `vocabulaire_<lot>.json` sous `"seance": "ouverture"`
(skill `lexique-sequence`). Les paragraphes gardent un repère en gras en tête
quand ils dépassent une centaine de mots (`controle_hierarchie`, « mur sans
repère »).

### 4. Poser l'image réaliste — qui montre le problème, jamais la solution
Décisions des 05 et 06/11/2026, règle n°315 (tout schéma est premium) :
- Une `figure.situation-photo` à la **fin** de la situation, image réaliste
  générée dans le Canva de Pascal (il la télécharge depuis son Chrome) ou
  reprise d'un lot voisin à l'octet près, avec la mention dans
  `SOURCES_MEDIAS.md` (« Image reprise d'un lot voisin »).
- **Règle de choix** : l'image n'entre que si elle ne donne pas la réponse de
  la séquence. Refusées au journal : le panneau solaire quand on cherche
  l'alimentation autonome, le boîtier fini, le kit monté, le mât « en
  aluminium », le drone qui oriente vers une solution.
- `alt` qui décrit l'image ; légende qui **pose la question** sans y répondre
  et finit par `<i>Image générée par IA (Canva).</i>` ; `loading="lazy"`,
  `width`/`height` renseignés, 640 px maximum à l'écran, 60 % de la largeur à
  l'impression.

### 5. Écrire l'hypothèse de départ
Une phrase que l'élève peut croire vraie avant d'avoir travaillé, et que la
séquence va confirmer, nuancer ou démentir. Elle est **rappelée mot pour
mot au bilan** (règle n°301) : la noter dans le manifest du lot.

### 6. Formuler la problématique
- Une seule question, qui finit par ` ?` (espace insécable, charte
  typographique du dépôt).
- Investigable par les activités prévues : chaque séance apporte une partie
  de la réponse, le bilan la boucle.
- Le verbe reprend celui de la compétence officielle (décrire, identifier,
  concevoir, programmer…), pour que l'élève voie le lien sans qu'on le lui
  explique.

### 7. Dire ce qu'il faut savoir, jamais « l'an dernier » (règle n°304)
Pascal change de collège chaque année : aucun élève n'a fait ses séquences
précédentes. L'ouverture nomme :
- les **compétences attendues** avant de commencer (2 ou 3 maximum, codes du
  référentiel) ;
- un **moyen de les rattraper** sur place : lien relatif vers la séquence,
  l'atelier ou la synthèse du dépôt, lisible hors ligne (règle n°305).
Interdits : « l'an dernier tu as vu… », « comme en 5e… », « tu te souviens
de… ».

### 8. Respecter la page élève (règles n°298, 306, 311)
- Sous le titre : la **ligne d'étiquettes** (niveau, code, thème, durée). Le
  référentiel complet va dans la synthèse professeur, pas ici.
- L'ouverture complète n'apparaît **qu'en séance 1**. À partir de la séance 2,
  elle est repliée dans le volet « 📖 Rappel », lien vers les autres pages
  compris ; `controle_squelette.mjs` (D6 obligatoire depuis le 04/11/2026)
  le vérifie.
- Aucun commentaire sur la démarche de conception dans ce que lit l'élève
  (décision d'octobre 2026) : pas de « règle n°… », pas de « nous avons
  choisi… ».

## Gabarit de sortie

```html
<section class="ouverture" id="ouverture">
  <h1>Thème <n> · <ville> — <niveau> · S<n> : <nom court></h1>
  <p class="mission"><!-- sous-titre-mission, EN PREMIER (règle n°4) --></p>
  <p class="etiquettes"><!-- niveau · code · thème · durée --></p>

  <h2>🚨 La situation</h2>
  <p><strong>Repère en gras.</strong> <!-- la personne, le lieu nommé, le problème,
     les mots techniques glosés dans la phrase, l'appel à l'élève --></p>
  <figure class="situation-photo">
    <img src="Images/situation_<slug>.png" width="1536" height="1024" loading="lazy"
         alt="<!-- ce que l'image montre -->">
    <figcaption><!-- la question posée par l'image, sans sa réponse -->
      <i>Image générée par IA (Canva).</i></figcaption>
  </figure>

  <h2>💭 Hypothèse de départ</h2>
  <p><!-- une phrase, rappelée mot pour mot au bilan --></p>

  <h2>❓ Problématique</h2>
  <p class="problematique"><!-- une question, insécable avant « ? » --></p>

  <h2>🧰 Ce qu'il faut savoir pour commencer</h2>
  <ul>
    <li><!-- compétence attendue (code) — « pour la revoir : » lien relatif --></li>
  </ul>
</section>
```

Le manifest JSON du lot reçoit `situation.personne`, `situation.lieu`,
`situation.image` (fichier, origine), `hypothese_depart` (texte exact),
`problematique`, `prerequis[]` `{code, lien_relatif}` ; `SOURCES_MEDIAS.md`
reçoit l'image.

## Contrôles avant livraison

- [ ] Une personne nommée par son rôle, un lieu nommé, un problème concret.
- [ ] Aucune donnée chiffrée non sourcée présentée comme un fait.
- [ ] Mots techniques glosés dans la phrase et présents au `vocabulaire_<lot>.json` (`ouverture`).
- [ ] Image : montre le problème, pas la solution ; `alt`, légende-question, mention Canva, `loading="lazy"`, 640 px max ; entrée `SOURCES_MEDIAS.md`.
- [ ] Hypothèse de départ recopiée à l'identique dans le bilan.
- [ ] Problématique = une question, verbe de la compétence, ` ?` insécable.
- [ ] Zéro « l'an dernier », « en 5e/4e », « tu te souviens ».
- [ ] Prérequis : codes + liens relatifs qui ouvrent hors ligne.
- [ ] Ligne d'étiquettes sous le titre ; référentiel complet absent de la page élève.
- [ ] Ouverture visible en séance 1 seulement, repliée dans « 📖 Rappel » ensuite.
- [ ] `controle_squelette.mjs`, `controle_hierarchie`, `controle_medias` verts ; aucun défilement de côté à 390 px.

## Ce que ce skill ne fait pas

- Il n'écrit pas les séances ni le bilan : `sequence-pedagogique-engageante`.
- Il ne génère pas l'image lui-même : elle vient du Canva de Pascal ou d'un
  lot voisin ; `licences-medias-education` tient `SOURCES_MEDIAS.md`.
- Il ne décide pas de l'objet-fil : la décision appartient à Pascal et au journal.
