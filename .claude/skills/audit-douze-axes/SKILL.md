---
name: audit-douze-axes
description: Auditer une page interactive du dépôt (TP, atelier, séquence) sur les 12 axes du gabarit de Pascal — conception, didactique, contenus, évaluation, engagement, UX, accessibilité, légal, suivi, technique, innovation, stratégie — en jouant la page « en tricheur », page ouverte, à 390 et 1 280 px ; rendre un rapport noté (Doc) puis suivre jusqu'à `main` : top 5 en un lot, le reste en lot « suite », banc commité, tableau de suivi. À utiliser quand Pascal joint son gabarit d'audit ou demande « audite cette page ». Règles d'or n°361 à n°368.
---

# Audit en 12 axes d'une page du dépôt

Né le 20/11/2026 de l'audit du TP « Algorigrammes de domotique » (`4e_C6.2`), demandé par Pascal avec son gabarit
(rôles multiples, 12 axes, score sur 10, 🔴 / 🟡 / 🟢, top 5, feuille de route, quick wins, SWOT). Note : 4,6 / 10.
Suivi jusqu'à `main` : PR #832, #833, #836 (top 5), #841 (le reste), #842 (deux contrôles rouges vus en chemin).
Les huit règles d'or n°361 à n°368 en sont sorties. Ce skill garde la méthode, pour que le prochain audit aille plus
vite et ne rate pas ce que celui-ci a failli rater.

**Quel skill, quand** : un audit écrit ailleurs → `relire-un-audit-externe` ; la lecture élève + inspecteur d'une
séquence et de son QCM → `audit-double-regard` ; **une page interactive notée sur 12 axes pour Pascal → ici**.

## 0. Avant tout : la page a peut-être bougé

```bash
git fetch origin main && git log --format='%h %ad %s' --date=short origin/main -- <chemin de la page>
gh api "repos/PLL-process/en-ligne-pour-le-cycle-4/pulls?state=open" --jq '.[] | "#\(.number) \(.head.ref)"'
```

Le 21/11/2026, quatre commits d'une autre session avaient déjà livré le top 5 entre l'audit et la correction : refaire
leur travail aurait écrasé le leur. On audite le commit du jour, on le cite (`4f33a68`) et on relit l'historique avant
chaque lot.

## 1. Fixer la cible et le périmètre

Le gabarit laisse deux champs vides (URL, cible). Par défaut, sans les redemander :

- la page seule, replacée dans son dossier et dans le site ;
- des élèves du niveau de la page, programme 2024, collège en Martinique, qui lisent souvent difficilement ;
- des séances de 55 min, du travail maison plafonné à 20 min par semaine, sans cahier (« feuille de brouillon ») ;
- un rendu en PDF par l'ENT Colibri.

Les critères sans objet pour une page de TP (forum, CGV, SCORM, certification, multilinguisme) se signalent et ne
comptent jamais contre la page.

## 2. Lire tout le code

Tout le fichier, pas un échantillon. Repérer et noter la ligne de :

- chaque validation (`Vérifier`, seuils, ordre exigé) — skill `validations-qui-disent-vrai` ;
- chaque correction **fabriquée par script** (un dessin qui n'existe pas dans le HTML échappe aux contrôles statiques) ;
- la simulation : joue-t-elle le travail de l'élève ou une règle fixe (n°362) ?
- le score, le code de validation, la date du bilan (n°363, n°365) ;
- ce qui est gardé dans le navigateur, ce qui ne l'est pas, ce que l'effacement efface (n°15, n°322).

## 3. Jouer la page « en tricheur » (Playwright, contexte neuf)

Chaque geste est une mesure à citer dans l'annexe :

1. « Vérifier » sur une zone vide, puis avec des réponses bidon (« aaaaa ») ;
2. un ordre différent mais juste (deux sorties inversées, deux capteurs lus dans l'autre ordre) ;
3. recopier la correction : quel score ? un 20 / 20 sans rien savoir ?
4. le code de validation pour deux scores, deux noms proches, deux dates ;
5. la date à 22 h 30 en Martinique : `timezoneId: 'America/Martinique'` et `page.clock.install()` ;
6. recharger : qu'est-ce qui revient, qu'est-ce qui se perd ? puis « Effacer » deux fois ;
7. un même bloc ajouté trois fois ; les boutons au doigt (44 px) ; 390 px sans débordement.

## 4. Ouvrir tout, puis regarder (n°361)

```bash
node _outils/controle_page_ouverte.mjs <dossier> --axe     # L listing qui défile · B bloc dessiné · C correction recopiée · A axe (L, B, A : sortie 1)
```

Si la page fabrique ses corrections par script, lui poser `window.__toutOuvrir()` (pilote : le TP `4e_C6.2`). Puis à
l'œil, en sombre et en clair, à 390 et 1 280 px : chaque schéma corrigé (flèches qui traversent un bloc, pointes
perdues, nombre de losanges contre ce que demande la consigne — n°368), l'impression PDF (nombre de pages, ce que la
trace contient), les contrastes calculés des couleurs des schémas.

## 5. Situer la page dans le site

- La séquence du dossier la relie-t-elle (n°366, `controle_porte_sequence.py`) ?
- Le bouton « QCM » mène-t-il au bon QCM (celui du programme 2024) ?
- Le vocabulaire est-il celui des autres pages du même sujet (« ovale » ou « ellipse ») ?
- Est-elle héritée (`_outils/heritees.json`) ? L'audit devient alors son cahier des charges.

## 6. Noter

Chaque axe : constat, forces, faiblesses, recommandations 🔴 / 🟡 / 🟢, score sur 10 (0-3 à refaire, 4-6 base à
corriger, 7-10 conforme). Un constat porte sa preuve (mesure, ligne de code, capture). Ce qui n'a pas été vérifié se dit
(Safari réel, lecteur d'écran, Core Web Vitals en réseau).

## 7. Rendre

Un document (type Docs, Claude Docs), dans l'ordre du gabarit : verdict en cinq lignes, périmètre retenu,
vérifié / non vérifié, tableau de synthèse, détail des 12 axes, top 5, feuille de route, quick wins (essayés sur une
copie, avec leur code), SWOT, annexe des preuves. La réponse dans la conversation suit `reponses-actionnables`.

## 8. Suivre jusqu'à `main` (l'audit n'est fini que là)

1. Le top 5 en un lot, une branche, une PR (`livraison-depot-cycle4`).
2. Le reste des 🔴 et 🟡 en un lot « suite », relu contre l'historique (étape 0).
3. Un banc commité qui rejoue chaque constat (`tests_<page>.mjs`, sortie 0 / 1 / 2) : un banc annoncé dans une PR et
   jamais commité ne prouve rien (n°259, n°266) — c'est arrivé le 20/11.
4. Les contrôles rouges vus en chemin sur d'autres pages : un petit lot séparé, jamais mêlé au lot de la page.
5. Un tableau « Suivi des corrections » dans le document : PR, ce qu'elle corrige, état.

## Pièges rencontrés

- Une note d'auteur visible par l'élève (« Précision pédagogique », « Phrase élève à retenir ») : n°309, désormais
  refusée par `controle_regles_visibles.py`.
- Un `<br>` sans espace devant colle les mots pour le lecteur d'écran (`textContent` : « alimentation2. dévisser »).
- Une condition longue dans un listing défile à 390 px et cache sa valeur (« < 5… ») : la couper sur deux lignes (n°364).
- `toISOString().slice(0, 10)` donne le lendemain après 20 h en Martinique (n°365, `controle_date_locale.py`).
- Un contrôle qui refuse une page à tort reçoit une exception nommée, datée et vérifiée (n°273), jamais un silence.
