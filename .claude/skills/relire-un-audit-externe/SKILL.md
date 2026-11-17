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
- Mesurer le même défaut sur tout le dépôt (n°293) et le dire, même si on ne le corrige pas tout de suite.

## 5. Répondre à Pascal

Format `reponses-actionnables` : d'abord ce qui est vrai et corrigé, puis le tableau des remarques avec leur statut (les
❌ et les ♻️ en une ligne chacun, avec la preuve), puis les décisions à prendre (🔶, avec un défaut), puis ➡️ la suite.
Ne jamais présenter une remarque non vérifiée comme un défaut de la page.
