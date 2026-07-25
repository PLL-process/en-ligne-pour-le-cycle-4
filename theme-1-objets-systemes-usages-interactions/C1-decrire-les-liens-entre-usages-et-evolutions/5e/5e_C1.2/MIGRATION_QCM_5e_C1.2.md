# Migration du QCM 5e_C1.2 vers le moteur commun

Date : 24 juillet 2026

## Objectif

Remplacer l’ancien moteur autonome de `qcm_principes_techniques.html` par le moteur de référence du Thème 2, sans modifier le contenu pédagogique des 24 questions.

## Éléments à conserver

- les 24 questions de la banque actuelle ;
- la compétence unique `5e_C1.2` ;
- les exemples sur les freins de vélo, l’éclairage et les critères de choix ;
- les explications, aides et erreurs fréquentes déjà présentes ;
- les illustrations locales et leurs textes alternatifs.

## Interface cible obligatoire

1. H1 avec emoji discret et sous-titre explicitant fonction, principe et critères de comparaison ;
2. badges `5e`, `5e_C1.2`, `24 questions · corrections détaillées` et mention des questions illustrées ;
3. lien de retour vers `sequence_5e_C1.2.html` ;
4. identité sauvegardée localement : Nom, Prénom, Classe, Date ;
5. carte « Ma progression » avec les sept compteurs permanents ;
6. minuteur avec démarrage, pause, reprise et mode sans minuteur ;
7. modes Parcours complet, 10 questions, Révision ciblée, Erreurs et À revoir ;
8. grille de navigation filtrable ;
9. écran question unique avec validation et correction détaillée ;
10. écran final avec note sur 20, temps, bilan par compétence, impression et reprise des erreurs.

## Transposition de la banque

Chaque question doit être convertie vers la structure commune :

```text
{
  c: "C1.2",
  n: "notion ciblée",
  q: "énoncé",
  o: ["proposition A", "proposition B", "proposition C", "proposition D"],
  r: 0,
  expl: "explication raisonnée",
  ex: "exemple concret",
  err: "erreur fréquente",
  d: ["raison A", "raison B", "raison C", "raison D"],
  ret: "à retenir",
  img: "chemin optionnel",
  alt: "texte alternatif optionnel"
}
```

Le champ `r` désigne l’index de la bonne réponse. Le tableau `d` explique chaque distracteur ; l’entrée correspondant à la bonne réponse reste vide.

## Tests à exécuter avant Ready for review

| Test | Résultat attendu |
|---|---|
| Chargement hors connexion en `file://` | Le QCM s’affiche sans erreur bloquante |
| Scénario tout juste | 24/24, 100 %, 20/20 |
| Scénario tout faux | 0/24, 0 %, 0/20 |
| Scénario mixte connu | Score et note conformes au scénario préparé |
| Une question non répondue | Compteurs et bilan distinguent la question restante |
| Sauvegarde puis rechargement | Identité, réponses, marques et progression restaurées |
| Remise à zéro | Stockage local et interface réinitialisés |
| Mode 10 questions | Exactement 10 questions actives |
| Mode erreurs | Seulement les questions précédemment incorrectes |
| Mode à revoir | Seulement les questions marquées |
| Navigation clavier | Tous les contrôles atteignables et focus visible |
| Impression | Résultat lisible en A4 sans boutons inutiles |
| Liens relatifs | Retour séquence et images valides |

## Critère de fin

La migration n’est considérée terminée qu’après remplacement effectif de l’ancien moteur, exécution et consignation des tests réalisables, régénération de l’audit et de l’index, garde de périmètre verte et passage de la PR en Ready for review.
