# banc-python — le petit Python des bancs d'essai

Source unique : `banc_python.js`. Posé dans une page par `poser.py`, entre deux commentaires
`<!-- banc-python v1 : début … -->` et `<!-- banc-python v1 : fin -->` ; on ne le modifie jamais dans la page.

```
python3 _outils/banc_python/poser.py <page.html>         # pose ou met à jour le bloc
python3 _outils/banc_python/poser.py --verifier-tout     # chaque page porte la version de la source
node _outils/banc_python/tests_banc_python.mjs           # 25 / 25 au 22/11/2026, sans navigateur (test 20 : contre CPython)
```

## Pourquoi il existe (audit de « Programmer l'alerte », 3e_C6.1, 21 et 22/11/2026)

Le bouton « Vérifier » de l'activité 4 cherchait des motifs dans le texte du programme : une version juste écrite
avec des apostrophes était refusée, une version fausse à 118 km/h était acceptée. La règle d'or n°333 demande de juger
ce que fait le programme. Le banc exécute donc le programme de l'élève sur des entrées inventées, avec des fonctions
simulées (`lire_capteur`, `envoyer`, `activer_sirene`…), et compare ses sorties au cahier des charges.

## Et l'éditeur Python intégré (Skulpt) ?

Le dépôt a, depuis le 04/11/2026, un éditeur Python commun : `_ressources-communes/editeur-python/` (Skulpt 1.2.0).
Son API `EditeurPython.executer(code, {simulation, entrees})` exécute un vrai Python et sert déjà de vérification
(5e_C9.1, 3e_C9.1). **C'est l'outil par défaut pour juger un programme.** Le banc-python a été écrit sans l'avoir
consulté d'abord.

**Décision du 22/11/2026** (carte blanche de Pascal) : **on garde les deux, chacun à sa place.**
- **L'éditeur commun (Skulpt) par défaut**, dès que l'élève écrit un vrai Python : boucles, fonctions, listes, `print`
  à la console.
- **Le banc-python** seulement quand il faut le chemin suivi pas à pas, avec chaque test évalué, ou une vérification
  instantanée du Python du collège (`if` / `elif` / `else`, affectations, textes) — comme dans `3e_C6.1`.
- **Garde-fou** (test 20 de `tests_banc_python.mjs`) : sur les programmes du lot et leurs variantes (apostrophes, `>=`,
  f-string, `is True`, expression conditionnelle, `;`, initialisation oubliée, `==` au lieu de `=`), le banc et le vrai
  Python (CPython) donnent les mêmes sorties, vent par vent. Une écriture que le banc accepte et que Python juge
  autrement est un défaut du banc, à corriger dans la source.
- Unifier (ajouter la trace à l'éditeur commun) ne se fera que si une deuxième séquence a besoin du pas à pas.

Ce que chacun sait faire :

| Besoin de la séquence | banc-python | EditeurPython (Skulpt) |
|---|---|---|
| Un vrai Python : boucles, fonctions, listes | ✘ sous-ensemble du collège (`if`/`elif`/`else`, `=`, `+=`, nombres, textes, booléens, f-strings simples, appels) ; le reste est refusé en le disant | ✔ |
| Le chemin suivi, pas à pas, avec chaque test évalué (« 118 > 118 → faux ») | ✔ (la trace du traceur) | ✘ (sortie de la console seulement) |
| Synchrone, sans chargement : la version du programme se dit à chaque frappe, la vérification répond tout de suite | ✔ (quelques millisecondes, aucun fichier à charger) | ✘ (asynchrone ; 945 Ko chargés au premier ▶) |
| Messages d'erreur en français, avec la ligne | ✔ | ✔ |
| Banc du lot sans navigateur (Node) | ✔ | ✘ |

## Ce qu'il promet, et ce qu'il refuse (n°340, n°146)

- Une écriture Python juste qu'il connaît obtient le même verdict qu'en Python : apostrophes ou guillemets,
  `== True` ou `is True`, `f"Vigilance {vigilance}"`, `a if c else b`, deux instructions séparées par `;`.
- Une écriture qu'il ne connaît pas (liste, `for`, `while`, `def`, `lambda`, `{ }`, f-string formatée) n'est **jamais**
  une « SyntaxError » : l'élève lit « limite du banc, pas forcément une erreur de ton programme », et le conseil
  d'essayer son programme dans Python sur ordinateur (le Bonus donne le fichier `.py`).
- Une vraie erreur reste une vraie erreur, avec le nom de Python et la ligne : `IndentationError`, `SyntaxError`
  (deux-points oubliés, `=` au lieu de `==`), `NameError` (variable sans valeur au repos), `TypeError`, `ValueError`
  (`float("4,0")`).

## API

```
BancPython.executer(code, {fonctions, entrees}) → {ok, erreur, trace, sorties, variables}
BancPython.analyser(code)                      → {ok, programme | erreur}
BancPython.phraseErreur(erreur)                → « Ligne 29 · IndentationError : … — conseil »
BancPython.phraseTrace(pas)                    → « ligne 12 · if vent_kmh > SEUIL_OURAGAN → 118 > 118 → faux : … »
BancPython.empreinte(code)                     → 8 caractères : un essai se rattache à la version essayée (n°333)
```

Une fonction simulée reçoit `(args, ligne, machine)` et peut lever `new BancPython.Erreur(type, ligne, message, conseil)`.
