# banc-eleve — le programme de l'élève, jugé en l'exécutant

Source unique : `banc_eleve.js` (le cœur) et `banc_eleve.css` (le verdict sous l'éditeur). Ils sont recopiés à
l'identique dans chaque page, entre `/* banc-eleve v1 : début … */` et `/* banc-eleve v1 : fin */` ; on ne les modifie
jamais dans la page.

```
python3 _outils/banc_eleve/poser.py --verifier-tout     # chaque page porte la version de la source (4 au 25/11/2026)
python3 _outils/banc_eleve/poser.py <page.html>          # remet le cœur et le style de la source dans cette page
python3 _outils/banc_eleve/tests_poser.py                # 9 / 9 au 25/11/2026
```

## Pourquoi il existe (25/11/2026)

Mesure de la règle d'or n°333 du 22/11/2026 : sur 7 pages où l'élève écrit du Python dans la page, 4 ne jugeaient pas
son programme. Dans `3e_C7.1` et `5e_C7.1`, une exécution qui affichait **n'importe quoi** ouvrait le verrou :
`print("x")` validait l'activité 3b. Dans `4e_C6.2`, il suffisait d'une ligne « [pompe] », même avec `>` au lieu de `<`.
Dans `4e_C9.1`, l'élève écrivait sa décision dans l'éditeur de l'activité 3, et aucune vérification ne la lisait.

## Ce qu'il fait

Après chaque ▶ Exécuter d'un éditeur nommé dans la table `BANC_ELEVE` de la page :

1. il rejoue le programme sur des entrées choisies (sous, sur et au-dessus de chaque seuil, n°351), avec
   `EditeurPython.executer` (Skulpt, hors ligne) : la ligne `nom = …` est remplacée par la valeur d'essai — le modèle
   de `5e_C9.1` (`avecPlaces`) —, ou une carte simulée propre à l'essai fournit les mesures ;
2. il compare ce que le programme affiche (ou commande) à l'attendu, et écrit sous l'éditeur : « ✔ 7 / 7 essais
   conformes », ou le **premier écart en clair** : « Premier écart — seuil = 28, T = 28 °C. Attendu : « ok » (28 > 28
   est faux). Obtenu : « ALERTE ». » ;
3. il range le verdict dans `window.__exp[bloc]` avec l'**empreinte** du programme : une frappe qui le change le périme
   (« ↻ À rejouer ») et retire la validation de l'activité (`retirer`, propre à la page) ;
4. une erreur de Python se dit avec son nom et sa ligne ; un programme qui ne finit pas se dit « arrêté par le banc ».

Le lien « Vittascience, si tu préfères » se suit encore, mais il ne prouve plus rien pour une activité où l'élève
écrit : la page ne lit pas le programme écrit là-bas. Qui programme dans Vittascience recopie son programme dans
l'éditeur de la page et clique ▶.

## La table d'une page

```js
const BANC_ELEVE = {
  vs1: {
    attente: "…",          // le message tant que rien n'a été essayé (repris par la vérification de l'activité)
    resume: "…",           // la ligne sous « ✔ n / n essais conformes »
    lire: (sortie, essai) => "ALERTE" | "ok" | "rien" | …,   // ce que le programme a fait, en un mot
    dire: x => "« " + x + " »",                              // ce mot, dans une phrase
    retirer: () => …,      // retire la validation quand le programme change (absent pour un Bonus)
    essais: [{vals: {seuil: 28, T: 28}, simulation: "…", attendu: "ok", libelle: "seuil = 28, T = 28 °C", pourquoi: "28 > 28 est faux"}]
  }
};
// dans CHECKS : exp: beOk("vs1"), expMsg: beMsg("vs1")
```

## Où il sert (25/11/2026)

| Page | Éditeur | Essais |
|---|---|---|
| `3e_C7.1` | act. 3b `vs1` · Bonus `vs2` | 7 (seuil 28 et 26) · 6 (20 à 30 °C) |
| `5e_C7.1` | act. 3b `vs1` | 2 (`True`, `False`) |
| `4e_C9.1` | act. 3 `edpy-a3` | 8 (40 % pile, 6 h et 10 h pile) |
| `4e_C6.2` | act. 5 `vs2` · Bonus `vs3` | 6 (30 % pile, puis 12 → 45 %) · 6 (jour et nuit) |

## Et le banc-python, et l'éditeur commun ?

L'éditeur commun (`_ressources-communes/editeur-python/`) **exécute** ; le banc-eleve s'appuie sur lui et ne fait que
choisir les entrées et comparer. Le banc-python (`_outils/banc_python/`) reste pour le chemin suivi pas à pas
(`3e_C6.1`). Décision du 22/11/2026 : chacun à sa place.
