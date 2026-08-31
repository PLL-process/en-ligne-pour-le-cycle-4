# Rapport de tests — lot Pékin 3e_C2.1

**Date** 8 août 2026 · **Suite** `tests_3e_C2.1_pekin.py` (Playwright, Chromium 1280×900)
**Résultat** **54 / 54 tests passés**


> **Correction du 31/08/2026 — la suite de ce lot était rouge, et c'est le test qui avait tort.**
> Réexécutée ce jour-là (personne ne l'avait relancée depuis sa livraison), elle échouait sur
> « séquence : hors ligne, aucune ressource distante (n°40) ». La cause n'était pas dans la
> page : le contrôle cherchait la chaîne `http://` dans le HTML sérialisé, où **chaque SVG en
> ligne porte son `xmlns="http://www.w3.org/2000/svg"** — un identifiant d'espace de noms, que
> nul navigateur ne va chercher. Le contrôle regarde désormais ce que la page **irait charger**
> (`src`, `link href`, `object data`, `iframe`, `use`), sans les hyperliens, qui ont le droit
> d'être distants. Vérifié dans les deux sens : la suite passe, et elle redevient rouge si l'on
> injecte une vraie ressource distante dans la page.
>
> ```
> 54 / 54 tests passés
> ```
Ce rapport ne mentionne que des tests **réellement exécutés**. La suite est livrée avec le lot :
elle se relance depuis le dossier du lot par `python3 tests_3e_C2.1_pekin.py`.

## Les données (6 tests)

La suite vérifie les **chiffres que la séquence et les corrigés affirment**, en relisant les CSV.
Si quelqu'un régénère les données sans refaire les corrigés, le test tombe.

| Ce qui a été vérifié | Résultat |
|---|---|
| 40 observations, 8 abandons — soit 20 %, « un sur cinq » | ✔ |
| **Aucun habitué n'abandonne (0 %)** | ✔ |
| Touristes **43 %**, personnes âgées **50 %** | ✔ |
| Durée moyenne **77 s**, habitué **41 s**, personne âgée **123 s** | ✔ |
| 8 verbatims et 3 incidents | ✔ |
| **Les six modes offerts ont tous leur corrigé** (règle n°43 précisée) | ✔ |

Le dernier contrôle est nouveau et il vaut d'être signalé : il lit les fichiers de corrigé et vérifie
qu'aucun des six modes proposés à l'élève n'y manque. C'est la garantie mécanique de la précision
apportée à la règle n°43 — *un choix offert engage un corrigé par option*.

## La séquence (28 tests)

| Ce qui a été vérifié | Résultat |
|---|---|
| Aucune erreur JavaScript, hors ligne intégral (n°40), lien d'accueil valide (n°11) | ✔ |
| Bandeau de tâches (n°30), 8 zones de rédaction / 8 versions étayées (n°31) | ✔ |
| Étiquettes (n°34), alternatives longues sur les figures (n°1) | ✔ |
| Compteur : 4 activités annoncées, 4 comptées (n°39) | ✔ |
| **n°44** — aucun badge ni bouton sans infobulle, légende lisible sans survol | ✔ |
| **n°42** — l'ambiguïté de « choisis » est **dite à l'élève** | ✔ |
| La marche du C2 sur trois niveaux est écrite à l'élève | ✔ |
| Billet d'entrée sans note (n°26), sauvegarde restaurée, un seul bouton QCM (n°4) | ✔ |

**Les quatre verrous, testés dans les deux sens** — et trois d'entre eux avec un refus *spécifique* :

| Verrou | Le refus vérifié |
|---|---|
| Act. 1 — la lecture par profil | une lecture qui **ne nomme pas les extrêmes** est refusée |
| Act. 2 — le vocabulaire | tant que les six mots ne sont pas reliés : « on ne choisit pas parmi des mots qu'on ne connaît pas » |
| Act. 3 — l'algorigramme | quand **seul l'ordre** est faux : « tout y est, sauf l'essentiel » |
| Act. 4 — la défense | sans le troisième point : « une représentation qui ne cache rien n'a rien choisi » |

**n°43** : les planches de corrigé sont présentes **et repliées** ; le Bonus a le sien, et il traite
les trois défis. **n°45** : le bouton propose le parcours court tant que la séquence n'est pas
terminée, et le parcours complet une fois les quatre activités validées.

## Le QCM (11 tests)

30 questions · répartition A/B/C/D **8 / 7 / 7 / 8** (graine 317) · 5 illustrées · aucune réfutation
de 20 caractères ou moins · explication, exemple, erreur classique et à-retenir partout · parcours
complet des 30 accepté · bilan par compétence affiché.

Deux contrôles propres à ce lot : la question « lequel des six modes est le meilleur » a bien pour
réponse **« aucun »** ; et l'arrivée `#depart=court` ouvre bien **10 questions**, tandis que
l'arrivée sans ancre ouvre le parcours complet.

## Les synthèses (7 tests)

Élève et professeur : aucune erreur JavaScript, figures au bon nombre, tous les liens résolus. Et un
contrôle de contenu : **les deux variantes d'usage** — l'élève choisit / l'enseignant impose — sont
bien écrites dans la synthèse professeur.

## Un test rouge, et qui avait raison

Le contrôle « une lecture qui ne nomme pas les extrêmes est refusée » a d'abord échoué, et
**c'était le vérificateur de la séquence qui avait tort** — pas le test.

Mon expression cherchait `0 %` sans garde. Or « 0 % » se trouve aussi dans « **3**0 % » et
« 4**0** % » : une lecture fausse, qui donnait 5 % aux habitués et 30 % aux personnes âgées, était
donc **acceptée**. Le vérificateur validait une réponse erronée.

Corrigé par une garde de chiffre — `(?:^|[^0-9])0\s*%` — et un commentaire dans le fichier explique
pourquoi. C'est la première fois dans ce dépôt qu'un test rouge désigne un défaut du **vérificateur
pédagogique** et non du test lui-même : la leçon « chercher lequel des deux a tort » vaut donc dans
les deux sens.

## Ce qui n'a pas été testé

- L'impression A4 : les feuilles `@media print` viennent du gabarit maison, aucune sortie papier
  n'a été produite ni relue.
- Un vrai lecteur d'écran : `aria-label`, `title`, `aria-describedby` et `desc` SVG sont en place et
  vérifiés dans le DOM, mais aucun test avec NVDA ou VoiceOver n'a été mené.
- Les infobulles **sur tablette** : c'est parce qu'on ne peut pas s'y fier que la règle n°44 impose
  une mention en clair — la mention, elle, a été vérifiée.
- La séquence sur mobile réel : seule la fenêtre 1280×900 a été utilisée.
- La **variante B** (l'enseignant impose le mode) : elle ne demande aucune modification de la page,
  donc rien de mécanique à vérifier — mais elle n'a pas été essayée en classe.
