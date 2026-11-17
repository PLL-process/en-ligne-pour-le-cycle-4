---
name: avant-de-commencer-trois-lignes
description: Écrire et poser la carte « 🎯 Avant de commencer : trois choses à lire » d'une séquence et de son QCM (règle d'or n°337) — ce que tu vas apprendre, ce que tu dois savoir faire, comment réussir — dans la langue d'un élève de 6e, à partir du référentiel, des critères de réussite et des pièges de la séquence. À utiliser sur chaque séquence (généralisation décidée le 17/11/2026) et pour toute séquence neuve.
---

# Avant de commencer : trois lignes

Pascal, le 17/11/2026 : « Avant de commencer, et dans toutes les séquences, l'élève devrait lire trois informations
très simples : ce qu'il va apprendre, ce qu'il doit savoir faire et comment réussir. » Règle d'or n°337. Pilote :
`5e_C2.1` (Shenzhen, #762).

## Où, et sous quelle forme

- **Séquence** : en tête de l'ouverture, dans le volet `#ouverture` (« 📖 Rappel », n°311), juste après les badges —
  avant le référentiel replié, la situation, la problématique. Repliée avec le reste de l'ouverture dès la séance 2.
  Le squelette (`controle_squelette.mjs`) la reconnaît : 🎯 trois lignes → 🔄 Avant de commencer → situation → …
- **QCM** : avant « 📊 Ma progression » ; la première rubrique devient « 📚 Ce que tu vas revoir ».
- Trois rubriques, toujours les mêmes titres : **📚 Ce que tu vas apprendre**, **🛠 Ce que tu dois savoir faire**,
  **✅ Comment réussir**. De une à trois lignes chacune, 40 mots au plus, une idée par ligne (skill
  `texte-clair-et-aere`).

## Écrire les trois rubriques

Sources, dans le lot : le tableau « Je serai capable de… » du référentiel replié, les critères de réussite des
activités, la problématique, les pièges du QCM (skill `qcm-aides-et-pieges`), la synthèse élève (« Ce que je dois
retenir »).

| Rubrique | Ce qu'elle dit | Ce qu'elle ne dit pas |
|---|---|---|
| 📚 Apprendre | la notion, avec ses mots à elle, le mot technique en gras et glosé (« ses **interacteurs** ») ; pourquoi elle sert | les codes (5e_C2.1), les formulations du programme |
| 🛠 Savoir faire | des gestes observables, à l'infinitif, sur l'objet de la séquence (« Faire la liste des interacteurs d'un objet, pas seulement les personnes ») | « comprendre », « connaître » sans geste |
| ✅ Réussir | la méthode qui marche et le piège à éviter (« Pense aux quatre familles… », « Devant chaque détail : pourquoi pas autrement ? ») ; « Après chaque exercice, compare avec la correction » | des encouragements vides, la note |

Lisible par un élève de 6e (n°316) ; aucun sigle sans sa glose (n°313) ; aucune unité sans son nom (n°312) ; rien de la
fabrique (n°309). Les nombres sont ceux de la séquence (n°338) : si la carte dit « quatre familles », la consigne et le
critère le disent aussi.

## Poser, vérifier

Les données vont dans le dossier du lot, un fichier par page :

```json
// trois_lignes_<lot>.json — séquence
{"page": "sequence_….html",
 "apprendre": ["…", "…"], "savoir_faire": ["…", "…"], "reussir": ["…", "…", "…"]}
```

```bash
python3 _outils/trois_lignes.py --poser <page> <lot>/trois_lignes_<lot>.json     # pose ou réécrit, et le style
python3 _outils/trois_lignes.py --verifier <page> <lot>/trois_lignes_<lot>.json  # 0 à jour · 1 à reposer
python3 _outils/trois_lignes.py --etat [--strict]                                 # le dépôt
```

Le QCM : rubrique `avant_de_commencer` de `qcm_aides_<lot>.json`, posée par `_outils/qcm_aides/poser.py` (skill
`qcm-aides-et-pieges`). Une page sans volet `#ouverture` (les quatre pages engendrées de `3e_C9.2`) est refusée : sa
carte se pose dans son générateur.

Puis : le banc du lot, `controle_squelette.mjs`, le mode mission (la carte est sur le premier écran,
`banc_generique.mjs`), la fiche papier, une capture à 390 px et à 1 280 px. La carte ajoute environ 100 mots à
l'ouverture ; `mesurer_charge.mjs` mesure les panneaux de séance, pas l'ouverture : ses chiffres ne bougent pas
(mesuré le 17/11/2026 sur onze séquences).

**Gabarits anciens.** La carte porte son propre cadre (960 px au plus, centrée, fond et bordure) : dans `3e_C1.5` et
`4e_C1.4`, la classe `card` n'a pas de style à l'écran, et la carte s'étalait sans fond sur toute la largeur. Quand
le titre de la séquence est **dans** le volet (`4e_C1.4` : « Bienvenue dans la cybersécurité »), la carte se déplace à
la main juste sous ce titre : reposer la réécrit à sa place, sans la remonter.

## L'exemple (5e_C2.1)

> 📚 **Ce que tu vas apprendre** — Tout ce qui entoure un objet et agit sur lui : ses **interacteurs**. / Et pourquoi
> ils expliquent la forme de l'objet.
> 🛠 **Ce que tu dois savoir faire** — Faire la liste des interacteurs d'un objet, pas seulement les personnes. /
> Expliquer un détail de sa forme : « il est ainsi parce que… ».
> ✅ **Comment réussir** — Pense aux quatre familles : les usagers, les données, les autres objets, l'environnement. /
> Devant chaque détail, demande-toi : « pourquoi pas autrement ? ». / Après chaque exercice, compare avec la correction.
