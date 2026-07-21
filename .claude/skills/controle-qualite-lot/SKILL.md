---
name: controle-qualite-lot
description: Contrôle qualité complet (pédagogique, technique, évaluation, droits) d'un lot de 3-5 codes AVANT remise à ChatGPT. À utiliser systématiquement en fin de lot, jamais sauté.
---

# Contrôle qualité de fin de lot

## Mission (unique)

Vérifier un lot terminé et produire son rapport de tests + manifeste.
Un lot qui échoue à un contrôle bloquant n'est pas remis : il est corrigé.

## Contrôles bloquants

**Pédagogie** : conformité programme 2024 (BO n°9 du 29/02/2024 prioritaire sur
tout cahier), compétence réellement travaillée par l'activité (pas de points
« décoration »), progressivité 5e→4e→3e, cohérence
problématique↔activités↔évaluation, durée réaliste, matériel confirmé ou
versions B/C présentes, exercices originaux, corrections de qualité, niveau de
langue collège.

**Technique** (scriptable — voir procédure) : HTML valide, zéro lien local
cassé, zéro erreur console, calcul des notes exact, sauvegarde/reprise, exports,
impression, mobile, clavier seul, contrastes, alt des images, poids des médias
(< 300 Ko par image sauf justification).

**Évaluation** : bonnes/mauvaises réponses, non-répondu, pondération et /20,
remise à zéro, limites, champs vides.

**Droits & sécurité** : `SOURCES_MEDIAS.md` complet, attributions affichées,
aucune donnée envoyée, aucun secret, aucune correction sommative publiée,
aucune dépendance suspecte, aucune suppression non documentée.

## Procédure technique

1. Vérif liens : script Python du lot 0 (parcours `href`/`src` locaux).
2. Console : ouvrir chaque HTML avec un navigateur headless local si disponible
   (sinon consigner « contrôle manuel restant » — ne jamais prétendre l'avoir fait).
3. Scénarios de notes : 3 jeux de réponses connus par évaluation, score attendu
   calculé à la main dans le rapport.

## Sortie obligatoire (remise à ChatGPT)

Rapport de fin de lot au format imposé (« LOT TERMINÉ » : codes traités,
fichiers créés/modifiés, tests réussis/échoués/restants, référentiel couvert,
médias/licences, éléments privés, points pour Pascal, commit + description PR
proposés), archive ou patch, `manifest.json` du lot, et la phrase finale :
« Lot préparé localement. Aucune modification distante ni publication GitHub
n'a été effectuée. Le lot est prêt pour le contrôle de ChatGPT et la validation
de Pascal. »

## Critères de réussite

- Zéro contrôle bloquant en échec non corrigé.
- Tout contrôle non exécuté est listé explicitement comme « restant à faire »,
  jamais passé sous silence.
