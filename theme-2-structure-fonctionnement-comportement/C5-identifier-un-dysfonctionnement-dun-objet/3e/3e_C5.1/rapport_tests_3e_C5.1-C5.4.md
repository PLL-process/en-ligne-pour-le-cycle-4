# Rapport de tests — LOT 03 « SOS station : réparer plutôt que jeter » (3e_C5.1 → C5.4)

**Suite** : `tests_3e_C5.1-C5.4.mjs`, livrée dans ce dossier · **Outil** : Playwright
(Chromium headless), viewport téléphone 390 × 844, pages en `file://` ·
**Rejouée le 31/08/2026** · **Verdict : 34 / 34 ✅**

```
cd theme-2-.../C5-.../3e/3e_C5.1 && node tests_3e_C5.1-C5.4.mjs
```

> **Ce que ce rapport disait avant le 31/08/2026.** Il portait 18 coches et ne citait
> **aucun** script : une dette honnête, pas une promesse fausse (règle d'or n°259). Son
> titre annonçait pourtant « 30/30 réussis » alors que ses tableaux comptaient 18 lignes —
> un nombre écrit en prose, que `_outils/controle_effectifs_qcm.py` ne lit pas et ne
> prétend pas lire. Les 18 lignes sont toutes reprises ci-dessous, et seize s'y ajoutent.

## Ce que cette suite éprouve en propre

Le simulateur de dépannage de ce lot est **le plus exigeant du dépôt** : il ne demande pas
seulement de faire un geste, il fait **payer le mauvais**. Remplacer une pièce saine est
refusé (« cet élément était sain ») **et** incrémente le compteur de mesures — une
réparation inutile coûte cher, exactement comme en atelier.

La suite se trompe donc exprès, vérifie le refus **et le coût**, puis répare les deux pannes
successives — la seconde s'activant toute seule après la première.

## Ce que la suite ne recopie pas

Ce lot n'emploie pas la convention `att = {id: "valeur"}`, sauf pour une de ses six
activités. Il écrit ses attendus en **quatre formes**, toutes extraites du source des
`CHECKS` : **20 égalités** (`$("id").value === "…"`), **9 préfixes**
(`.startsWith("…")`, l'option exacte étant retrouvée dans le menu réel de la page),
**5 nombres** (`num("id") === N`) et **1 objet `att`**. Les relevés du simulateur et le
coupable de chaque panne sont lus dans la table `PANNES` (règle d'or n°268).

### La prose, et ce que cette suite n'affirme pas

Trois activités demandent une justification rédigée, que la page juge par **mots-clés et
longueur**. La suite lit ces contraintes dans le code et compose un texte qui les satisfait :
elle montre donc que le verrou de rédaction s'ouvre **aux conditions déclarées**, et non que
la page sait reconnaître une bonne justification. Elle vérifie surtout l'inverse, qui est la
partie utile : le contrôle 6 donne les trois parcours justes avec une justification de quatre
mots, et **l'activité est refusée**.

## Séquence — 24 contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 1 | Chargement, titre « SOS station », les quatre codes 3e_C5.1 → C5.4 | ✅ |
| 2 | 4 onglets de séance, bascule vers S4 puis retour S1 | ✅ |
| 3 | **Aucun état de simulateur au chargement** — le verrou de l'activité 4 est fermé | ✅ |
| 4 | 20 égalités, 9 préfixes, 5 nombres, 3 rédactions extraits des `CHECKS` | ✅ |
| 5 | Activité 1 validée **7 / 7** (symptôme ou hypothèse, trois pistes classées) | ✅ |
| 6 | **Activité 2 REFUSÉE** : 3 parcours justes, justification de quatre mots | ✅ |
| 7 | Activité 2 validée **3 / 3** une fois la justification aux conditions déclarées | ✅ |
| 8 | Activité 3 validée **9 / 9** (protocole ordonné, localisation, sécurité) | ✅ |
| 9 | **Activité 4 REFUSÉE** malgré 2 réponses justes — pannes non résolues | ✅ |
| 10 | Le test sirène constate le symptôme, panne n°1 active | ✅ |
| 11 | T1 → T2 → T3 → T4 mesurés dans l'ordre : les relevés de la page s'affichent | ✅ |
| 12 | **Remplacer une pièce saine est refusé** : « cet élément était sain » | ✅ |
| 13 | **Et la réparation inutile COÛTE** : le compteur passe de 4 à 5 | ✅ |
| 14 | La bonne pièce réparée → la panne n°2 **s'active seule** | ✅ |
| 15 | Panne n°2 localisée en **2 mesures** (premier relevé anormal) et réparée | ✅ |
| 16 | Le retest final déclare « SIRÈNE OPÉRATIONNELLE » | ✅ |
| 17 | Activité 4 validée **2 / 2** une fois les deux pannes réellement résolues | ✅ |
| 18 | Activité 5 validée **8 / 8** (plan coté et procédés de fabrication) | ✅ |
| 19 | Activité 6 validée **5 / 5** (réparer ou jeter : la décision pèse deux critères) | ✅ |
| 20 | Progression 6 / 6 et les quatre onglets portent leur coche | ✅ |
| 21 | Rechargement : réponses, validations **et l'état du simulateur** restaurés | ✅ |
| 22 | Les 4 liens internes existent | ✅ |
| 23 | Les 5 SVG référencés existent sur le disque | ✅ |
| 24 | Hors ligne : aucune ressource distante, aucune modale, aucune erreur JS | ✅ |

## QCM — 10 contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 25 | Chargement, titre, taille annoncée exacte (badge et compteur) | ✅ |
| 26 | **32 questions, 4 compétences à 8 chacune** | ✅ |
| 27 | Bonnes réponses A/B/C/D = **8 / 8 / 8 / 8** et `d[r]` vide partout | ✅ |
| 28 | **10** questions illustrées : fichiers présents, `alt` renseigné partout | ✅ |
| 29 | Gabarit maison complet : 4 options, 4 réfutations, `expl`, `ex`, `err`, `ret` | ✅ |
| 30 | Moteur étendu : zone figure **masquée** sans image, **visible** avec | ✅ |
| 31 | Parcours **32 / 32 joué question par question** → **20,0 / 20**, bilan 4 lignes à 8 / 8 | ✅ |
| 32 | La clé `localStorage` du QCM est écrite | ✅ |
| 33 | Le lien de retour vers la séquence pointe sur un fichier réel | ✅ |
| 34 | Aucune erreur JS sur le QCM | ✅ |

## Ce que la suite a fait apparaître, et qui dépasse ce lot

Le contrôle 22 ne trouve que **4 liens internes** dans cette séquence : l'index, le lexique,
le QCM, et une ancre. **Ses deux synthèses n'y sont pas liées.**

Vérification faite sur le dépôt entier, en marchant depuis `index.html` de lien en lien :
**56 des 76 synthèses ne sont atteignables par aucun chemin** — ni depuis le tableau de bord,
ni depuis la séquence à laquelle elles appartiennent. Une page de plus est dans ce cas,
`_reperes/carte_des_representations.html`.

Ce n'est pas un défaut de ce lot : 40 séquences sur 46 sont dans la même situation, ce qui
en fait la règle et non l'exception. La synthèse est pourtant le document que l'élève
emporte. Le contrôle et le correctif — qui se fait au générateur d'index, en un endroit
plutôt qu'en quarante — font l'objet d'une PR à part.

## Contrôles restant manuels

Appareils réels ; atelier version 🅰 (multimètres **MATÉRIEL À CONFIRMER**) ; impression 3D
(**À CONFIRMER**) ; relecture humaine.

## Limites connues

- Tests exécutés uniquement en Chromium/Playwright — aucune compatibilité non testée n'est
  revendiquée.
- Google Fonts inaccessible en sandbox : polices de repli, sans incidence — la suite ne
  compte pas ces requêtes comme des ressources distantes de la page (règle n°40).
