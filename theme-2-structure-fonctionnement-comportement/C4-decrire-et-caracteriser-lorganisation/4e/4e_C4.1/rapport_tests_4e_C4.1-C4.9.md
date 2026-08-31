# Rapport de tests — Lot 4e_C4.1 → C4.9 « Le jardin connecté »

**Suite** : `tests_4e_C4.1-C4.9.mjs`, livrée dans ce dossier · **Outil** : Playwright
(Chromium headless), viewport mobile 390 × 844, pages en `file://` (hors ligne) ·
**Rejouée le 31/08/2026** · **Verdict : 35 / 35 ✅**

```
cd theme-2-.../C4-.../4e/4e_C4.1 && node tests_4e_C4.1-C4.9.mjs
```

> **Ce que ce rapport disait avant le 31/08/2026.** Il portait 21 coches et les
> attribuait à `tests_lot09.js`, un script qui n'a jamais été commité. Le relevé de
> `_outils/controle_rapports_tests.py` l'a mis en tête de la file des lots à payer ;
> la suite ci-dessus le paie (règles d'or n°259 et n°266). Les 21 lignes d'origine
> sont toutes reprises, et treize contrôles s'y ajoutent.

## Ce que cette suite éprouve en propre

Ce lot porte **deux verrous expérientiels de natures différentes**, et c'est ce qui le
rend intéressant à conduire :

- **l'explorateur de table** — trois bacs à filtrer, un compteur 3 / 3, et l'activité 3
  refusée tant que les trois n'ont pas été ouverts ;
- **le simulateur réseau** — trois pannes à diagnostiquer, où un **mauvais** diagnostic
  est refusé sans faire avancer le compteur.

La suite se trompe donc **exprès** une fois, vérifie que la page refuse et que le compteur
ne bouge pas, puis répare. Les deux verrous sont éprouvés dans les deux sens : l'activité
est d'abord refusée avec **toutes les réponses justes**, puis validée une fois le geste fait.

## Ce que la suite ne recopie pas

Les **32 champs** de réponse sont extraits des fonctions `CHECKS` de la page — billet
d'entrée compris, qui est rangé dans `CHECKS[0]`. La bonne cause de chaque panne est lue
dans la table `PANNES` de la page ; la mauvaise que la suite donne exprès est prise dans
les options réelles du menu déroulant, jamais écrite ici (règle d'or n°268).

## Séquence — 26 contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 1 | Chargement, titre « Le jardin connecté », codes du lot en tête | ✅ |
| 2 | 4 onglets de séance, bascule vers S4 puis retour S1 | ✅ |
| 3 | **Aucune expérience enregistrée au chargement** — les deux verrous fermés (n°226) | ✅ |
| 4 | 32 champs attendus extraits des `CHECKS`, billet d'entrée compris | ✅ |
| 5 | Billet d'entrée : réclame d'abord les réponses manquantes, puis rend 3 / 3 | ✅ |
| 5 bis | **Le billet ne compte pas comme une activité** : la progression reste 0 / 5 | ✅ |
| 6 | Activité 1 validée **9 / 9** (alimenter, stocker, distribuer, convertir) | ✅ |
| 7 | Activité 2 validée **4 / 4** (acquérir, traiter, communiquer, restituer) | ✅ |
| 8 | **Activité 3 REFUSÉE malgré 6 réponses justes** — les bacs ne sont pas explorés | ✅ |
| 9 | Un bac filtré affiche sa requête et ses mesures ; compteur 1 / 3, verrou toujours fermé | ✅ |
| 10 | Les 3 bacs explorés → compteur 3 / 3 et `__exp.table` posé | ✅ |
| 11 | Activité 3 validée **6 / 6** une fois la table réellement explorée | ✅ |
| 12 | **Activité 4 REFUSÉE malgré 4 réponses justes** — les pannes ne sont pas résolues | ✅ |
| 13 | **Un mauvais diagnostic est refusé**, et le compteur ne bouge pas | ✅ |
| 13 bis | Les SYMPTÔMES de la panne sont affichés avant le diagnostic | ✅ |
| 14 | Les 3 pannes réparées → « 3 / 3 réseau réparé » et `__exp.reseau` posé | ✅ |
| 15 | Activité 4 validée **4 / 4** une fois les trois pannes diagnostiquées | ✅ |
| 16 | Activité 5 validée **6 / 6** (3D, injection, laser, perçage) | ✅ |
| 17 | Progression 5 / 5 et les quatre onglets portent leur coche | ✅ |
| 18 | Rechargement : réponses, validations **et les deux verrous** restaurés | ✅ |
| 18 bis | Les compteurs des deux simulateurs repartent à 3 / 3 après rechargement | ✅ |
| 19 | Blocs « Prêt·e » et « Bonus », un seul bouton vers le QCM | ✅ |
| 20 | Le bouton de fin de bilan tient dans sa largeur à 390 px (`scrollWidth` mesuré) | ✅ |
| 21 | Les 9 liens internes existent, y compris vers 4e_C4.7 et 4e_C6.2 | ✅ |
| 22 | Les 3 SVG référencés par la séquence existent sur le disque | ✅ |
| 23 | Hors ligne : aucune ressource distante, aucune modale, aucune erreur JS | ✅ |

Le contrôle 20 remplace la vérification visuelle d'origine (« bouton QCM sans
débordement ») par une **mesure** : `scrollWidth − clientWidth ≤ 1 px`. Un débordement
constaté à l'œil se reconstate à l'œil ; mesuré, il se rejoue.

## QCM — 9 contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 24 | Chargement, titre, taille annoncée exacte (badge et compteur) | ✅ |
| 25 | 30 questions sur 4 familles : **EN 7 · ID 10 · RES 10 · PRO 3** | ✅ |
| 26 | Bonnes réponses A/B/C/D = **7 / 7 / 8 / 8** et `d[r]` vide partout | ✅ |
| 27 | **4** questions illustrées, fichiers présents sur le disque | ✅ |
| 28 | Gabarit maison complet : 4 options, 4 réfutations, `expl`, `ex`, `err`, `ret` | ✅ |
| 29 | Parcours **30 / 30 joué question par question** → **20,0 / 20**, bilan sur 4 familles | ✅ |
| 30 | La clé `localStorage` du QCM est écrite | ✅ |
| 31 | Le lien de retour vers la séquence pointe sur un fichier réel | ✅ |
| 32 | Aucune erreur JS sur le QCM | ✅ |

Le rapport d'origine annonçait **3** questions illustrées ; la banque en porte **4**. Le
manifeste de ce lot ne déclarait pas `questions_illustrees`, il n'était donc pas en écart —
mais le nombre écrit ici l'était, et il est corrigé.

## Six pictogrammes qui n'étaient documentés nulle part

`_outils/controle_medias.py`, livré en PR #322, relevait six SVG de ce dossier que le
`SOURCES_MEDIAS.md` ne nommait pas : les pictogrammes de la seconde banque,
`qcm_automatisation_premium.html`. Vérifiés un par un — SVG écrits à la main, sans raster
embarqué —, ils sont maintenant documentés. La dette du dépôt passe de 88 à **82** médias.

## Limites connues

- Tests exécutés uniquement en Chromium/Playwright — aucune compatibilité non testée n'est
  revendiquée.
- La version 🅰 (jardin réel) relève de l'enseignant : elle n'est pas simulable ici.
- Google Fonts inaccessible en sandbox : polices de repli, sans incidence — la suite ne
  compte pas ces requêtes comme des ressources distantes de la page (règle n°40).
