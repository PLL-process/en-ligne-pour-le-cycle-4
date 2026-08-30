# Rapport de tests — 5e_C7.2

Ce rapport ne déclare que des tests **réellement exécutés**, sous Chromium (Playwright), le
30/08/2026.

## Modèle — `calotte.py`

    python3 calotte.py

Le modèle donne les cotes que citent le TP, la synthèse et le QCM : hauteur du centre de la
bille (8,5 mm), diamètre du creux obtenu (Ø10,54), volumes comparés
(117,8 mm³ contre 67,2), et la profondeur à laquelle l'ancien creux déborde la calotte
(0,16 mm). **Aucune de ces valeurs n'est écrite à la main dans une page** : le scénario du
TP et les synthèses les reçoivent du modèle (règle d'or n°246).

## QCM — `tests_5e_C7.2_qcm.mjs`

    node tests_5e_C7.2_qcm.mjs qcm_5e_C7.2_le-de-ameliore.html 5e_C7.2 "" ../../atelier-cao/tp_5e_de_calottes.html

**31 / 31.** Ce que la suite vérifie : chargement sans erreur JavaScript ni requête
échouée, 30 questions, 4 options et 3 réfutations chacune, la bonne réponse sans réfutation,
tous les champs du gabarit remplis, 30 notions distinctes, la répartition par code **mesurée**
dans la banque (30 sur `5e_C7.2`), la répartition des bonnes réponses (8/7/7/8), aucune bonne
réponse détachée par sa longueur, l'écart moyen sous 5 caractères (+2.3 caractère), la correction qui
déplie les trois réfutations et porte un « à retenir », les deux confirmations sans boîte
modale, la note 20/20 sur un parcours complet, le lien vers le TP, et la persistance au
rechargement.

## TP — les contrôles de l'atelier

    python3 verif_guidage.py tp_5e_de_calottes.html
    python3 verif_chaine.py

Le premier passe **10 règles sur 11** : seule la n°77 échoue, cinq paliers sur huit n'ayant pas
d'image de résultat. Le second est neuf : il régénère chaque TP depuis son scénario dans un
fichier temporaire et le compare octet par octet à la page du disque. Il a trouvé, en naissant,
que **trois empreintes sur quatre étaient fausses** et que **trois pages avaient été modifiées à
la main** — elles ne sont plus.

## Outils du dépôt passés sur ce lot

| Outil | Résultat |
|---|---|
| `_outils/sans_modale.py` | rien à faire — aucune boîte modale |
| `_outils/fix_r.js` | répartition A/B/C/D = 8/7/7/8, graine 764 |
| `_outils/generer_lexique.py` | 30 notions → `lexique_5e_C7.2.html` |
| `_outils/controle_liens.py` | aucune adresse morte, aucune ancre introuvable |
| `_outils/controle_couverture.py` | `5e_C7.2` : ÉVALUÉ 30 question(s) |
| `_outils/controle_formulations.py` | les citations du référentiel sont exactes |

## Ce qui n'est pas testé, et ne peut pas l'être ici

- **Les gestes Onshape ne sont pas constatés sur poste.** Le plan décalé et la primitive Sphère
  en mode Retirer sont décrits d'après la documentation. C'est la limite déclarée de tout
  l'atelier, et elle pèse plus lourd ici puisque le TP est neuf : à dérouler une fois en salle.
- **L'amélioration elle-même n'est pas démontrée.** Le TP le dit à l'élève : elle se juge la
  pièce en main, et cela demande deux impressions.
