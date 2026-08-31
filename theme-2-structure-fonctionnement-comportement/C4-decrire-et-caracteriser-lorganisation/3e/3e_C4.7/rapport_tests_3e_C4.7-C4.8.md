# Rapport de tests — LOT 02 « Internet jusqu'à Sainte-Luce » (3e_C4.7 → C4.8)

**Suite** : `tests_3e_C4.7-C4.8.mjs`, livrée dans ce dossier · **Outil** : Playwright
(Chromium headless), viewport téléphone 390 × 844 · **Rejouée le 31/08/2026** ·
**Verdict : 35 / 35 ✅**

```
cd theme-2-.../C4-.../3e/3e_C4.7 && node tests_3e_C4.7-C4.8.mjs
```

> **Ce que ce rapport disait avant le 31/08/2026.** Il portait 17 coches et ne citait
> **aucun** script : une dette honnête (règle d'or n°259). Son titre annonçait « 24/24 »
> pour 17 lignes — un nombre écrit en prose, hors de portée des contrôles de champs
> (règle n°264), corrigé ici. Les 17 lignes sont reprises, et dix-huit s'y ajoutent.

## Ce que cette suite éprouve en propre

Deux simulateurs qui ne se ressemblent pas :

- **le découpage en paquets** — le message de l'élève est coupé en trois, les paquets
  arrivent dans le désordre, et le verrou ne s'ouvre que si le réassemblage est **juste**.
  La suite se trompe d'abord d'ordre, vérifie le refus, puis remet en place ;
- **le réseau maillé** — cinq routeurs, un plus court chemin calculé par un parcours en
  largeur, des liaisons qu'on coupe au clic.

**Rien de tout cela n'est écrit dans le test** : ni le chemin initial, ni le chemin de
secours, ni les liaisons à couper. Le graphe est lu dans la page, les chemins sont ceux
qu'elle annonce, et la liaison à couper est choisie **dans le chemin réellement emprunté**.
Le rapport d'origine notait déjà qu'un chemin écrit à la main dans la correction (R1→R2→R4→R5)
était faux, le vrai étant R1→R3→R5 : un chemin recopié dans un test aurait le même sort.

## Deux verrous qui ne survivaient pas à un rechargement

Le contrôle 22 a trouvé ce que le rapport d'origine ne prétendait pas vérifier :
`window.__simOk` et `window.__rerouteVu` **n'étaient pas enregistrés**. La page sauvegardait
les réponses, les validations et jusqu'aux liaisons coupées — mais pas les deux traces
d'expérience. Un élève qui rechargeait sa page retrouvait tout, sauf le droit de valider :
les activités 3 et 5 le renvoyaient refaire une expérience qu'il avait faite.

Corrigé dans `collect()` et `restore()`, et vérifié à chaque exécution de la suite.

## Séquence — 26 contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 1 | Chargement, titre « Internet jusqu'à Sainte-Luce », codes 3e_C4.7 / C4.8 | ✅ |
| 2 | 3 onglets de séance, bascule vers S3 puis retour S1 | ✅ |
| 3 | **Aucun verrou ouvert au chargement** : ni réassemblage, ni re-routage (n°226) | ✅ |
| 4 | 20 égalités, 7 préfixes, 1 nombre, 4 rédactions extraits des `CHECKS` | ✅ |
| 5 | Activité 1 validée **6 / 6** (terminaux, switch, routeur, adresse IP) | ✅ |
| 6 | Activité 2 validée **7 / 7** (le trajet en six étapes, les câbles sous-marins) | ✅ |
| 7 | **Activité 3 REFUSÉE** malgré 3 réponses justes — le simulateur n'a pas servi | ✅ |
| 8 | Le message est découpé en 3 paquets numérotés, **arrivés dans le désordre** | ✅ |
| 9 | **Un réassemblage dans le mauvais ordre est refusé**, le verrou reste fermé | ✅ |
| 10 | Remis dans l'ordre : message reconstitué à l'identique, verrou ouvert | ✅ |
| 11 | Activité 3 validée **3 / 3** une fois le réassemblage réussi | ✅ |
| 12 | Activité 4 validée **4 / 4** (le jeu du routeur R2) | ✅ |
| 13 | **Activité 5 REFUSÉE** : l'expérience de re-routage n'a pas été faite | ✅ |
| 14 | Premier envoi : le plus court chemin **R1→R3→R5**, sur un graphe de 5 routeurs | ✅ |
| 15 | Liaison **du chemin emprunté** coupée → le réseau trouve seul **R1→R2→R4→R5** | ✅ |
| 16 | Les 2 liaisons de R5 coupées → « livraison impossible » | ✅ |
| 17 | Tout réparé → le réseau **retrouve le chemin d'origine** | ✅ |
| 18 | Activité 5 validée **2 / 2** une fois l'expérience faite | ✅ |
| 19 | Activité 6 validée **6 / 6** (le défi de transfert) | ✅ |
| 20 | Toutes les activités validées (6 / 6) | ✅ |
| 21 | Rechargement : réponses, validations et **la liaison coupée** restaurées | ✅ |
| 22 | Rechargement : **les deux verrous d'expérience survivent** (corrigé ce jour) | ✅ |
| 23 | Les 4 liens internes existent | ✅ |
| 24 | Les 4 SVG référencés existent sur le disque | ✅ |
| 25 | Hors ligne : aucune ressource distante, aucune modale, aucune erreur JS | ✅ |
| 26 | Les 6 liaisons du réseau sont atteignables au clavier (`tabindex`, `role`, `aria-label`) | ✅ |

Le contrôle 26 remplace la mention d'accessibilité du rapport d'origine par une mesure :
une affirmation d'accessibilité qui ne se rejoue pas vaut ce que vaut la mémoire de qui l'a
écrite.

## QCM — 9 contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 27 | Chargement, titre, taille annoncée exacte (badge et compteur) | ✅ |
| 28 | **30 questions, 2 compétences à 15 chacune** | ✅ |
| 29 | Bonnes réponses A/B/C/D = **8 / 7 / 8 / 7** et `d[r]` vide partout | ✅ |
| 30 | Aucune question illustrée dans cette banque, et rien ne le contredit | ✅ |
| 31 | Gabarit maison complet : 4 options, 4 réfutations, `expl`, `ex`, `err`, `ret` | ✅ |
| 32 | Parcours **30 / 30 joué question par question** → **20,0 / 20**, bilan 2 lignes | ✅ |
| 33 | La clé `localStorage` du QCM est écrite | ✅ |
| 34 | Le lien de retour vers la séquence pointe sur un fichier réel | ✅ |
| 35 | Aucune erreur JS sur le QCM | ✅ |

## Anomalie détectée et corrigée par les tests d'origine (22/07/2026)

Conservée telle quelle : la correction de l'activité 5 annonçait un chemin initial erroné
(R1→R2→R4→R5) là où le simulateur calcule R1→R3→R5. Texte corrigé avant remise. La suite
d'aujourd'hui rend cette vérification permanente : elle lit le chemin dans la page.

## Contrôles restant manuels

Appareils réels iOS/Android · séance Filius version 🅰 au labo · comptes Packet Tracer
(version 🅱) **À CONFIRMER** · relecture orthotypographique humaine.

## Limites connues

- Tests exécutés uniquement en Chromium/Playwright — aucune compatibilité non testée n'est
  revendiquée.
- Google Fonts inaccessible en sandbox : polices de repli, sans incidence (règle n°40).
