# Rapport de tests — Lot 4e_C6.2 « Le jardin connecté : arrosage automatique »

**Suite** : `tests_4e_C6.2.mjs`, livrée dans ce dossier · **Outil** : Playwright
(Chromium headless), viewport mobile 390 × 844 · **Rejouée le 31/08/2026** ·
**Verdict : 35 / 35 ✅**

```
cd theme-2-.../C6-.../4e/4e_C6.2 && node tests_4e_C6.2.mjs
```

> **Ce que ce rapport disait avant le 31/08/2026.** Il portait 16 coches et les attribuait
> à `tests.mjs`, jamais commité ; le rapport voisin `rapport_tests_jardin_v2.md` annonçait
> « 27/27 » sans coche ni script. Deux dettes, payées ensemble ici (règles n°259 et n°266).
> C'était le **dernier lot** de la file publiée par `_outils/controle_rapports_tests.py`.

## Ce que cette suite éprouve en propre : la coupure réseau

Cette séquence est la seule du thème 2 qui charge des ressources distantes — **trois
éditeurs Vittascience en `<iframe>`** — et deux de ses huit activités ont un verrou qui exige
d'ouvrir un de ces éditeurs.

La question n'est donc pas « la page cite-t-elle un domaine distant » : elle le fait, et son
pied de page l'assume. La question est **« que reste-t-il quand le collège n'a pas de
réseau ? »**. La suite y répond en fermant vraiment le robinet : toute requête `http(s)` est
**abandonnée avant de partir**, pour toute la session, et les huit activités sont jouées dans
cet état.

**Résultat mesuré** : les verrous `vs1` et `vs2` s'ouvrent sur le **geste** d'ouvrir le
dépliant, pas sur le chargement de l'iframe. Hors réseau, l'élève perd l'éditeur — il ne perd
ni la séquence, ni la possibilité de valider les huit activités. **La version 🅲 « sans
matériel » annoncée par la page est tenue**, et on le sait désormais par mesure et non par
confiance.

## Ce que la suite ne recopie pas, et comment elle s'y prend ici

Les six lots précédents laissaient lire leurs `CHECKS` depuis la console : leur script est
classique, ses `const` sont des variables globales. **Celui-ci enferme tout dans une fonction
anonyme** — `(function(){ "use strict"; … })()` — et rien n'en sort. Un pilote qui compte sur
les globales échoue net, et c'est ce qui est arrivé au premier jet.

La suite lit donc le **fichier source**, qui est la page elle-même. C'est plus robuste que
d'interroger la fenêtre : cela marche que le script soit enfermé ou non. La convention de ce
lot est une **sixième** : l'appel d'aide `sv("id", "valeur")`. Le banc de tests — T1, T2, T3
et leurs attendus — est lu dans la table `BENCH` du même source. Même chose pour la liste des
activités validées, enfermée elle aussi : la suite lit ce que la page **montre**, la classe du
bandeau de retour.

## Séquence, réseau coupé — 25 contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 1 | Chargement **réseau coupé** : la page s'affiche, code 4e_C6.2 présent | ✅ |
| 2 | 3 onglets de séance, bascule S3 puis retour S1 | ✅ |
| 3 | **Aucun verrou ouvert au chargement** — les trois casiers sont vides (n°226) | ✅ |
| 4 | 25 valeurs et 1 rédaction extraites des `CHECKS`, sur 8 activités | ✅ |
| 5 | Activité 1 validée **3 / 3** (capteur, carte, écran) — sans réseau | ✅ |
| 6 | Activité 2 validée **4 / 4** (de la mesure brute au pourcentage) | ✅ |
| 7 | **Activité 3 REFUSÉE** malgré les 5 étapes en ordre — l'éditeur n'a pas servi | ✅ |
| 8 | Ouvrir le dépliant pose `vs1` : **le geste suffit**, l'iframe n'est pas exigée | ✅ |
| 9 | Activité 3 validée **5 / 5**, réseau toujours coupé | ✅ |
| 10 | Activité 4 validée **3 / 3**, et le pseudo-code s'écrit en direct (`<`, MARCHE) | ✅ |
| 11 | **Activité 5 REFUSÉE** à son tour : le second éditeur n'est pas ouvert | ✅ |
| 12 | Activité 5 validée **4 / 4** (le trou de la condition et les deux appels) | ✅ |
| 13 | Simulateur : 10 sous le seuil 30 → pompe en marche ; 50 au-dessus → arrêt | ✅ |
| 14 | **Activité 6 REFUSÉE** : le banc de tests n'a pas été exécuté | ✅ |
| 15 | Les 3 tests du banc rendent l'attendu déclaré : T1 MARCHE · T2 arrêt · T3 arrêt | ✅ |
| 16 | Le badge s'affiche et `__exp.tests` s'ouvre — cas frontière compris | ✅ |
| 17 | Activité 6 validée une fois le banc au vert | ✅ |
| 18 | Activité 7 validée **4 / 4** (chaque exigence du besoin et SA preuve) | ✅ |
| 19 | Activité 8 validée **2 / 2** (le bénéfice, et la phrase de l'élève) | ✅ |
| 20 | **Progression 8 / 8, réseau coupé d'un bout à l'autre** | ✅ |
| 21 | 2 requêtes distantes refusées, vers un seul hôte : `fr.vittascience.com` | ✅ |
| 22 | Les 3 éditeurs sont dans un dépliant **refermé par défaut** : rien ne part avant un geste | ✅ |
| 23 | Rechargement : réponses, progression 8 / 8 et les trois verrous restaurés | ✅ |
| 24 | Les 3 liens internes existent | ✅ |
| 25 | Aucune modale, aucune erreur JS malgré les iframes refusées | ✅ |

## QCM — 10 contrôles

Les 16 lignes du rapport d'origine sont reprises, y compris **le test n°12, le plus utile de
la série** (voir plus bas), et regroupées ici :

| # | Contrôle | Résultat |
|---|---|---|
| 26 | Chargement, titre à la charte portant le code 4e_C6.2 | ✅ |
| 27 | **30 questions, 30 notions toutes distinctes** | ✅ |
| 28 | **90 réfutations** — une par distracteur — aucune posée sur la bonne réponse | ✅ |
| 29 | Bonnes réponses A/B/C/D = **8 / 7 / 7 / 8** (écart max 1) | ✅ |
| 30 | 5 codes du programme, aucun inventé : C6.2×16 · C4.4×5 · C4.5×4 · C4.1×3 · C1.4×2 | ✅ |
| 31 | Gabarit complet partout (`c n q o r expl ex err d ret`), aucune option dupliquée | ✅ |
| 32 | **Aucune bonne réponse détachée de plus de 8 caractères** ; écart moyen −1,6 | ✅ |
| 33 | Aucune réponse exposée dans le HTML rendu (plus de `value="v0"`) | ✅ |
| 34 | Le lien de retour vers la séquence pointe sur un fichier réel | ✅ |
| 35 | Aucune erreur JS sur le QCM | ✅ |

## Le test n°32 (n°12 d'origine) a d'abord échoué, et c'est le plus utile de la série

Conservé tel quel, parce qu'il raconte une correction qui vaut d'être connue.

Première exécution : **24 questions sur 30** avaient la bonne réponse la plus longue, avec
**12,5 caractères d'avance** en moyenne. Un élève qui coche systématiquement la plus longue
obtenait un score honorable sans rien savoir.

| État | bonne = la plus longue | bonne = la plus courte | écart moyen |
|---|---|---|---|
| version initiale | 24 / 30 | 3 / 30 | **+12,5** car. |
| après 1ʳᵉ passe | 3 / 30 | 24 / 30 | **−6,7** car. |
| après 2ᵉ passe | 6 / 30 | 15 / 30 | **−1,6** car. |

La première passe avait **échangé le biais contre son miroir** : « coche la plus courte »
marchait aussi bien. Le rang seul n'est donc pas un bon critère — ce qui compte est l'écart
**visible**. La correction a consisté à **allonger les distracteurs**, pas à tronquer les
bonnes réponses : un distracteur détaillé et plausible est un meilleur piège, et il
correspond à une vraie erreur d'élève. La suite rejoue cette mesure à chaque exécution.

## Ce que ce rapport ne prouve pas

Que les 30 questions sont pédagogiquement justes pour des élèves de 4ᵉ. Aucun test
automatique ne le dira : cela se voit en classe. Le rapport prouve que la banque est conforme
au gabarit, que la page fonctionne, que la bonne réponse ne se devine pas sans lire la
question — et, pour la séquence, qu'elle tient sans réseau.

Il ne dit rien non plus du **contenu** des éditeurs Vittascience : ce qui se passe dans une
iframe d'un autre domaine est hors d'atteinte d'une suite locale, et le restera.
