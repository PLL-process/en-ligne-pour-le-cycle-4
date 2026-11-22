---
name: relire-un-audit-externe
description: Recevoir un audit écrit ailleurs (une autre IA, un collègue, un outil en ligne) sur une page du dépôt et le vérifier remarque par remarque — sur la page rendue et dans l'historique git — avant toute correction ; classer chaque remarque confirmée, déjà corrigée, non reproduite ou idée à juger ; corriger les confirmées, chercher les mêmes défauts ailleurs, répondre à Pascal. À utiliser dès que Pascal joint un audit.
---

# Relire un audit externe

Né le 17/11/2026. Pascal joint un « Audit pédagogique du QCM de 5e — Station de vélos de Shenzhen », écrit par un autre
outil. Son anomalie « majeure » P0 : le titre du QCM afficherait « Thème 2 · Martinique — 4e · Atelier : QCM — SOS
serre ». Vérifiée dans le dépôt : **fausse aujourd'hui, vraie en août** — c'est l'incident de la règle n°51, corrigé
depuis, et `build_qcm.py` refuse toute trace du gabarit d'origine. L'outil avait lu une ancienne copie. Ses écarts de
nombres (« 4 illustrées / 5 », « 8 interacteurs / 6 ») ne correspondaient pas non plus à la page publiée. Corriger sur
la foi de l'audit aurait « corrigé » du juste.

Règles qui fondent ce skill : n°167 (vérifier avant de corriger, même quand l'auditeur a raison neuf fois sur dix),
n°191 (un audit est une production, pas un verdict), n°293 (un audit se vérifie à la ligne, puis se mesure sur tout le
dépôt), n°208 (avant de créer ce qu'un audit déclare manquant, chercher qui le fait déjà), n°172 (deux audits qui
divergent désignent la frontière entre le vérifiable et le discutable).

## 1. Découper l'audit en remarques vérifiables

Une ligne par remarque : où (page, bloc, question), ce qu'elle affirme, ce qu'elle propose. Séparer :
- les **constats** (« le titre affiche X », « la consigne dit 8, le critère 6 ») — vérifiables ;
- les **recommandations** (« ajouter des aides progressives ») — à juger, pas à vérifier ;
- les **limites avouées** de l'audit (« je n'ai pas exécuté les questions ») — elles disent ce qu'il n'a pas vu.

## 2. Vérifier chaque constat à la source

- **La page rendue**, pas le source seul : Playwright sur le fichier local (le `h1`, le texte visible, le compte des
  questions `const QUESTIONS`, l'écran du mode mission concerné). La page publiée, si elle est accessible, pour
  l'écart de déploiement.
- **L'historique** : `git log -S "<texte cité>" -- <fichier>` et le journal (`grep` du mot clé) — le constat a-t-il été
  vrai, et quand a-t-il été corrigé ?
- **Les outils du dépôt** qui mesurent déjà ce constat (skill `audit-double-regard`, § 0) — leur résultat fait foi.
- **Un constat lu dans le code se rejoue** (audit de `3e_C4.1`, 17/11/2026 : l'auditeur avait lu `CHECKS` sans rien
  cliquer). « Une justification de mots-clés passe », « l'ordre des essais n'est pas vérifié », « une réponse changée
  reste validée » : on le fait au navigateur, on voit le défaut, puis on l'écrit en cas de banc qui échoue avant la
  correction et passe après (`tests_3e_C4.1-C4.2.mjs`, tests 10 bis et 10 ter). Les validations : skill
  `validations-qui-disent-vrai` ; les questions qui soufflent : skill `propositions-sans-indice`.

- **Les critères de recette de l'audit se recopient au mot près** dans le banc (audit de l'entraînement DNB,
  21/11/2026 : « avec 6 justes et 2 blancs, afficher « 6 / 8 renseignés · seuil atteint · Q7 et Q8 à faire » »). Le
  banc échoue sur l'ancienne version, passe sur la nouvelle (n°194).

## 3. Classer

| Statut | Quand | Ce qu'on écrit |
|---|---|---|
| ✅ Confirmé | la page rendue le montre aujourd'hui | où, et la capture ou la mesure |
| ♻️ Déjà corrigé | vrai un jour, plus aujourd'hui | quand, par quelle PR ou règle (« n°51, août 2026 ») |
| ❌ Non reproduit | la page dit autre chose | ce que dit la page, mot pour mot |
| 💡 Idée à juger | une recommandation | pour ou contre, et pourquoi ; la règle qui s'y rattache |

Une remarque non reproduite peut cacher un défaut voisin : la relecture du 17/11 n'a pas trouvé les « règles de la
ville » dans la correction, mais les a trouvées dans le positionnement (« ⭐ … je pense aussi aux règles »). Chercher le
voisin avant de clore.

## 4. Corriger, puis généraliser

- Corriger les ✅ (et les voisins trouvés), lot par lot, avec leurs bancs.
- Retenir les 💡 que Pascal valide ; une idée qui vaut pour tout le site devient une règle d'or (journal, tableau de
  tête, `registre_regles.py --ecrire`), un outil de mesure, et un skill — exemple du 17/11 : n°337, n°338, n°339.
- Mesurer le même défaut sur tout le dépôt (n°293) et le dire, même si on ne le corrige pas tout de suite. Un audit
  d'une page parle souvent d'un gabarit : celui de `3e_C4.1` a fait trouver 34 pages aux onglets sans clavier
  (`onglets_clavier.py`), 6 pages qui promettaient le hors-ligne, 14 seuils codés sous le seuil annoncé dans 9
  séquences (`controle_validations.py`).
- **Demander pourquoi aucune règle ne l'avait vu.** Le 21/11/2026, l'ancienne page de l'entraînement DNB enfreignait
  quatre règles en vigueur (n°137, 144, 300, 340) : la cause n'était pas un manque de règle mais une page qu'aucun
  outil ne rejouait. La réponse décide du geste : une règle neuve, un outil qui manque, ou une page à faire entrer
  dans la mesure (`eleve_qui_ne_lit_pas.py --tout`, skill `eleve-qui-ne-lit-pas`).
- Relire aussi ce que la correction elle-même a pu casser : `controle_axe.mjs` sur tout le site après une passe qui
  touche l'accessibilité (le 17/11, l'agrandisseur annoncé « bouton » sur des schémas porteurs de texte a fait 24
  reculs graves, repris avant la fusion).

## 5. Répondre à Pascal

Format `reponses-actionnables` : d'abord ce qui est vrai et corrigé, puis le tableau des remarques avec leur statut (les
❌ et les ♻️ en une ligne chacun, avec la preuve), puis les décisions à prendre (🔶, avec un défaut), puis ➡️ la suite.
Ne jamais présenter une remarque non vérifiée comme un défaut de la page.
