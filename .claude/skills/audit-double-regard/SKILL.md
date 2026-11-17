---
name: audit-double-regard
description: Passer une séquence du dépôt et son QCM sous deux regards — un élève de 5e qui la découvre en mode mission, écran par écran, puis un inspecteur de technologie — avec les outils du dépôt ; classer les défauts P0 / P1 / P2, les corriger, vérifier, livrer. À utiliser pour généraliser l'audit de Shenzhen (17/11/2026) à toutes les séquences, et avant qu'une séquence passe en classe.
---

# Audit « double regard » : l'élève, puis l'inspecteur

Né le 17/11/2026. Pascal transmet un audit du QCM de Shenzhen (5e_C2.1) écrit « selon deux regards complémentaires :
celui d'un élève de 5e qui découvre et utilise le QCM, puis celui d'un inspecteur de technologie ». Il fait la séquence
avec ses 5e le jour même ; elle est reprise en trois PR (#760, #761, #762), puis Pascal demande : « on va généraliser aux
autres séquences avec les skills ». Ce skill est cette généralisation. Les règles qu'il fait appliquer sont dans le
journal : n°337, n°338, n°339 (17/11/2026), n°336, n°335, n°331, n°330, n°202, n°96, n°51, n°26, n°1.

Un audit venu d'ailleurs (un autre outil, une autre IA) ne s'applique pas tel quel : skill `relire-un-audit-externe`
d'abord. Celui-ci produit l'audit, et le fait aboutir.

## 0. Avant de lire : mesurer

Depuis la racine du dépôt, sur la séquence (`<page>`), son QCM (`<qcm>`) et leur dossier (`<lot>`) :

```bash
python3 _outils/trois_lignes.py --etat <lot>                 # n°337 : la carte « Avant de commencer »
python3 _outils/qcm_aides/poser.py --etat <lot>              # n°337 côté QCM, n°339 : aides progressives, pièges
python3 _outils/controle_memes_nombres.py <lot>              # n°338 : N1 annonce du QCM, N2 « au moins N », N3 bilan recopié
python3 _outils/corriger_billet.py <page>                    # n°336 : le billet d'entrée a-t-il sa correction ?
python3 _outils/controle_correction_illustree.py <page>      # n°336 : un dessin attendu est dessiné dans la correction
python3 _outils/controle_correction_complete.py <page>       # n°332
python3 _outils/controle_schema_sous_les_yeux.py <page>      # n°331
node _outils/mode_mission/banc_generique.mjs <page>          # le mode mission joué écran par écran
node _outils/mode_mission/banc_editeur.mjs <page>            # l'éditeur Python se voit là où on l'annonce
node _outils/mesurer_charge.mjs <page>                       # mots visibles par séance (repère : 1 200)
```

Un outil qui ne lit rien (« 0 page lue ») est en panne, pas vert (n°299).

## 1. Le regard de l'élève — en mode mission, écran par écran, à 390 px

L'élève arrive en mode mission (depuis le 14/11). On joue la séquence comme lui : « 🎮 Mode mission », puis
« Suivant », écran par écran, et on capture chaque écran qui pose un problème (Playwright, 390 px).

| Ce qu'on regarde | Ce qui est attendu | Si non |
|---|---|---|
| L'ouverture | 🎯 trois lignes : ce que tu vas apprendre, ce que tu dois savoir faire, comment réussir (n°337) | skill `avant-de-commencer-trois-lignes` |
| L'écran de départ d'une activité | Il montre le schéma qu'il annonce. Vide (forme seule) si les écrans suivants le font remplir (n°331) | figure `ms-seul` + `consigne` (exemple : la bête à cornes vide de 5e_C2.1, #760) |
| Les consignes sur chaque écran | Chaque écran garde SA consigne ; aucune consigne d'une autre partie ne le suit (le mode mission reprend la « ressource » de l'activité sur chaque écran de question) | la consigne passe en `consigne` (écran de départ) ; l'écran de la partie reçoit la sienne dans son cadre (`ms-seul`) — #761 |
| Les mots | Un mot savant que l'élève ne connaît pas est glosé à son premier emploi, le mot en avant : « l'**ellipse** (la forme ovale) » | glose + entrée au lexique (skill `lexique-sequence`) |
| Le matériel nommé | Ce que l'élève a vraiment : pas de cahier → « sur une feuille de brouillon » | réécrire, sans toucher aux identifiants (sauvegardes) |
| Chaque exercice | Un bouton de correction, en page complète comme en mode mission (n°336) : billet d'entrée, activités, Bonus, billet de sortie | `corriger_billet.py --ecrire` ; corrigé du Bonus « des réponses possibles + le critère » |
| Le QCM | Illustré là où une figure fait réfléchir (6 à 8 questions, n°1 ; muette si la question fait trouver ce qu'elle montrerait) ; aides progressives ; pièges (n°339) | skill `qcm-aides-et-pieges` |

## 2. Le regard de l'inspecteur

| Ce qu'on vérifie | Ce qui est attendu |
|---|---|
| Alignement | Chaque code annoncé est travaillé par une activité, et évalué par au moins 5 questions du QCM s'il y est évalué (n°202) |
| Mêmes nombres, mêmes mots (n°338) | Fiche, consigne, critère, correction, positionnement, carte « Prêt·e », README, QCM : un seul nombre par attendu ; le positionnement ne valorise rien que la leçon écarte ; le bilan du QCM parle de ses notions |
| Preuve de compétence (n°330) | Une production autonome sur une situation NOUVELLE, seul et sans aide : un billet de sortie (5 min, un objet jamais vu, version étayée pour l'écrit, correction avec critères). Le QCM entraîne ; il ne prouve pas seul (n°202) |
| Apprentissage / bilan | Les documents et les aides servent pendant l'apprentissage ; le billet de sortie s'en passe |
| Le premier texte lu (n°51) | Le titre affiché (h1) et le sous-titre de chaque page sont ceux du lot |

## 3. Classer, puis corriger

- **P0** — empêche de comprendre ou de travailler : titre d'un autre lot, consigne d'une autre partie, réponse donnée
  avant la question, page cassée. Correction immédiate, PR à part si la séquence passe bientôt en classe.
- **P1** — trompe ou prive : nombres qui divergent, exercice sans correction, schéma annoncé et absent, mot inconnu non
  glosé, preuve de compétence absente.
- **P2** — gêne : interface chargée, illustration manquante, aide qui pourrait être graduée.

Corriger par les outils quand ils existent (ils sont rejouables et vérifient) ; à la main sinon, avec la trace dans le
journal. Une retouche d'une seule page qui contourne un défaut commun (le découpage du mode mission, le moteur du QCM)
se signale : le défaut commun se reprend dans une PR à part, toutes les pages rejouées.

## 4. Vérifier, livrer

- Les bancs du lot (`tests_<lot>`), la n°311, le mode mission joué, les contrôles ci-dessus, puis le skill
  `controle-qualite-lot`.
- Les captures avant / après à 390 px des écrans touchés.
- Une entrée au journal (ce qui a été vu, par quel regard, ce qui change, la mesure) ; une PR par lot (skill
  `livraison-depot-cycle4`). Pascal fusionne.

## L'exemple : 5e_C2.1, Shenzhen (17/11/2026)

- Élève : l'écran de départ annonçait « un schéma qui fait penser à une tête de taureau » sans le montrer → la bête à
  cornes vide ; « sur ton cahier » → « sur une feuille de brouillon » ; « ellipse » → « l'ellipse (la forme ovale) » ; en
  c) et d), la consigne de a) suivait l'élève → `consigne` ; billet d'entrée et Bonus sans correction → corrigés.
- Inspecteur : « je pense aussi aux règles » dans le positionnement (n°338) ; pas de preuve seule → billet de sortie
  (l'abribus) ; le QCM : 5 → 8 illustrées, aides progressives, six pièges, bilan qui parlait d'énergie et de réseau.
