# Fiche pédagogique / inspection — Le jardin connecté (4e_C4.1 → C4.9)

> Cette fiche manquait. Son absence est ce qui a fait perdre au lot phare de la 4ᵉ son statut
> « complet et validable » au contrôle du 28/08/2026 (`_outils/controle_statut.py`, PR #263) —
> alors que le lot porte séquence, QCM, matrice, synthèses, images et rapport de tests. Elle est
> écrite **d'après la séquence elle-même**, pas d'après une intention : chaque durée, chaque
> production et chaque critère ci-dessous est recopié de la page.

## Identification

| Champ | Valeur |
|---|---|
| Niveau | 4e (programme 2024, applicable rentrée 2026-2027) |
| Codes | 4e_C4.1 · C4.2 · C4.3 · C4.4 · C4.5 · C4.6 · C4.7 · C4.8 · C4.9 — **les neuf codes de l'îlot C4** |
| Thème | Thème 2 — Structure, fonctionnement, comportement |
| Compétence parente | C4 — Décrire et caractériser l'organisation d'un OST |
| Référentiel | BO n°9 du 29/02/2024 · codes arbitrés par `_outils/data_competences.py` (règle n°21) |
| Domaines du socle | D1.3, D2, D3, D4, D5 (déclarés en tête de séquence) |
| CRCN | 1.3 (traiter des données : table structurée, filtres) · 3.4 (programmer — amorce, par le comportement de la carte) · 5.1 (résoudre un problème technique : les trois pannes réseau) |
| Objet-fil | Le jardin pédagogique du collège, Sainte-Luce. Suite du lampadaire intelligent de 5ᵉ, préparation de la station d'alerte de 3ᵉ |
| Durée annoncée | 4 séances de 55 min (220 min) · **189 min d'activités** — mesure `_outils/mesurer_temps_seances.py` |
| Version | 🅰 réel / 🅱 simulation intégrée / 🅲 documents imprimés — déclarées en tête |

## Sous-compétences

| Code | Intitulé officiel (abrégé) | Activité | Durée | Production |
|---|---|---|---|---|
| 4e_C4.1 | Fonctions des constituants d'une chaîne d'énergie | Act. 1a | 45 min | 5 associations |
| 4e_C4.2 | Transformations et flux d'énergie | Act. 1b | (idem) | 4 lectures de flux |
| 4e_C4.4 | Constituants de la chaîne d'information | Act. 2 | 20 min | 4 associations |
| 4e_C4.5 | Transformation d'une donnée téléversée | Act. 3 | 35 min | exploration 3 bacs |
| 4e_C4.6 | Structure de la table qui range la donnée | Act. 3 | (idem) | 6 réponses |
| 4e_C4.7 | Adresse IP fixe sur un réseau local | Act. 4 | 45 min | 3 pannes résolues |
| 4e_C4.8 | Résoudre un problème de communication | Act. 4 | (idem) | 4 réponses |
| 4e_C4.9 | Compléter une simulation fournie | Act. 4 | (idem) | simulateur intégré |
| 4e_C4.3 | Forme d'une pièce → procédé de réalisation | Act. 5 | 40 min | 4 diagnostics + 2 justifications |

Couverture détaillée notion par notion : `matrice_couverture_4e_C4.1-C4.9.csv` (28 lignes).

## Prérequis

Séquence 5ᵉ « Le lampadaire intelligent » (5e_C4.1–C4.8) : tracer une chaîne d'énergie, dire qui
décide, ranger les informations d'un parc, mettre en réseau. La séquence le rappelle elle-même en
ouverture (« Ce que tu as déjà fait ») et **prévoit l'élève qui n'était pas là** : « l'essentiel
tient en une image : l'information en haut, l'énergie en bas, et la flèche d'ordre qui descend ».

Billet d'entrée intégré : 3 questions, 4 min, **sans note et sans regard** — il aiguille, il ne
juge pas. Capsule de rattrapage de 3 minutes en dessous.

## Garde-fou de progressivité (4e = faire cohabiter deux chaînes, et faire voyager une donnée)

Ce qui change depuis la 5ᵉ, dit par la page : « l'objet arrose au lieu d'éclairer, et surtout il
**mesure** ». Une chaîne d'énergie est acquise ; la nouveauté est de la faire cohabiter avec une
chaîne d'information partant d'un capteur, et de donner une adresse à chaque machine.

Vocabulaire INTRODUIT : mesure brute vs donnée utile, horodatage, table structurée (1 ligne =
1 mesure), filtre, adresse IP fixe vs DHCP, conflit d'adresse, passerelle, portée, indices de
surface (stries, ligne de joint, bords brunis).
Vocabulaire EXCLU (réservé 3ᵉ) : routeur, table de routage, TTL, CAN, dimensionnement en Wh.

## Situation déclenchante et problématique

- **Situation** : le jardin pédagogique du collège vient d'être « connecté » — trois bacs, des
  capteurs d'humidité, une pompe alimentée par un panneau solaire, une électrovanne, une carte
  reliée au wifi, une application de courbes. Le club jardin est dépassé : « on appuie sur des
  boutons, mais on ne comprend pas comment tout ça tient ensemble ». Le principal confie à la
  classe la production du **dossier technique du jardin**.
- **Problématique** : *Comment décrire l'organisation complète d'un système connecté — de
  l'énergie qui l'alimente aux données qu'il produit — pour pouvoir l'expliquer, l'entretenir et
  l'améliorer ?*
- **Hypothèse d'entrée** (reprise au bilan) : quel chemin parcourt la mesure d'humidité du bac B
  entre le capteur planté dans la terre et la courbe sur la tablette ? Version étayée fournie —
  phrases à trous, *même exigence scientifique, obstacle de rédaction retiré*.

## Déroulé

**S1 — La chaîne d'énergie du jardin (C4.1 · C4.2) · act. 1, 45 min.**
Question directrice : d'où vient l'énergie qui arrose les bacs, et sous quelles formes voyage-t-elle ?
Production : 5 associations + 4 lectures de flux. Pièges nommés dans la page : croire que la
batterie *fabrique* l'électricité ; confondre distribuer et convertir ; oublier le flux d'**eau**,
qui n'est pas un flux d'énergie électrique.
Critère : **9 / 9 et la chaîne recopiée au cahier avec les natures d'énergie**.

**S2 — De la mesure à la table de données (C4.4 · C4.5 · C4.6) · act. 2 (20 min) + act. 3 (35 min).**
Question directrice : que devient la mesure entre la terre du bac B et la courbe sur la tablette ?
Act. 2 : chaîne d'information du jardin réel — critère 4 / 4 et la chaîne au cahier.
Act. 3 : le voyage de la donnée, avec l'explorateur de table intégré (filtres bac_A/B/C). La mesure
brute (612) devient donnée utile (60 %) et **horodatée**. Pièges : confondre brut et utile ; oublier
l'horodatage ; croire qu'une ligne = un bac.
Critère : 3 bacs explorés (3/3) et 6 / 6.

**S3 — Le réseau du jardin et ses adresses (C4.7 · C4.8 · C4.9) · act. 4, 45 min.**
Question directrice : pourquoi la carte a-t-elle une adresse FIXE, et que faire quand ça ne
communique plus ? Simulateur de dépannage intégré, **trois pannes** : conflit, passerelle, portée.
Pièges : donner la même IP à deux appareils ; choisir une IP fixe dans la plage DHCP ; accuser le
wifi quand c'est la passerelle.
Critère : 3 pannes résolues au simulateur **ET** 4 / 4.

**S4 — La forme d'une pièce raconte sa fabrication (C4.3) · act. 5, 40 min.**
Question directrice : en regardant une pièce du jardin, peut-on deviner comment elle a été
fabriquée ? Quatre pièces, indices de surface → procédé, croisés avec la **quantité**. En 🅰, les
vraies pièces circulent en classe. Pièges : croire que tout plastique est injecté ; oublier le
critère de quantité ; confondre stries d'impression et rayures d'usure.
Critère : 6 / 6 et le tableau indices → procédés recopié.

**Bilan.** L'hypothèse d'entrée est ressortie et confrontée au trajet réel (capteur → carte →
wifi → table du serveur → application). Auto-positionnement par famille de codes.

## Outils, versions, sécurité

Aucun logiciel tiers, aucun compte : tout est intégré à la page (schémas interactifs, explorateur
de table, simulateur réseau). Fonctionne hors ligne, en `file://`.
**Sécurité 🅰** : le jardin réel et toute maquette sont en **très basse tension uniquement** —
déclaré en tête de séquence. Aucun geste sur le secteur. L'eau reste à distance des postes.

## Différenciation, inclusion, accessibilité

Trois versions déclarées (🅰 réel · 🅱 simulation · 🅲 imprimé). Hypothèse en version étayée à
phrases trouées, *à exigence égale*. Billet d'entrée sans note avec capsule de rattrapage. Aides
à deux niveaux par activité. Exercices en listes déroulantes (DYS). Mode essentiel qui masque
référentiel et corrections. Sauvegarde locale, impression A4, dix SVG originaux lisibles en
niveaux de gris (étiquettes textuelles systématiques).

## Évaluation

Formatif : vérificateurs par activité avec critères chiffrés (9/9 · 4/4 · 3 bacs + 6/6 · 3 pannes
+ 4/4 · 6/6), verrous expérientiels sur l'explorateur (`__exp.table`) et le simulateur
(`__exp.reseau`) — un mauvais diagnostic est explicitement refusé —, hypothèse reprise au bilan,
auto-positionnement par famille.
QCM d'entraînement : `qcm_4e_C4.1-C4.9_jardin_connecte.html`, **30 questions dont 4 portent
une image** (`chaines_jardin_connecte`, `energie_stockage_transformation`, `table_donnees_jardin`,
`reseau_jardin_ip`). *La séquence en annonce 3 : elle a une image de retard sur son propre QCM.*
> **Ce que le bilan du QCM permet de conclure.** Ses 30 questions se répartissent en quatre
> familles — Énergie (7 q., C4.1·C4.2), Information et données (10 q., C4.4·C4.5·C4.6), Réseau
> (10 q., C4.7·C4.8·C4.9) et **Forme et procédé (3 q., C4.3)**. Les trois premières familles
> portent assez de questions pour situer un élève ; la quatrième, non. **4e_C4.3 se lit dans la
> production de l'activité 5** — les quatre diagnostics et leurs deux justifications — pas dans
> le score du QCM. Mesure : `_outils/controle_echantillonnage.py`.

**Sommative** : à construire par l'enseignant sur un objet transféré. **Aucun corrigé sommatif
n'est publié dans le dépôt.**

## Traces et preuves (honnêteté du lot)

Dix SVG originaux CC0 (`SOURCES_MEDIAS.md`), aucune image tierce, aucun hotlinking ; adresses en
plage locale 192.168.x.x, valeurs électriques cohérentes en 12 V TBT.
Rapport de tests : **21 / 21 réussis**, réellement exécutés le 24/07/2026 sous Chromium/Playwright
en viewport 390×844, hors ligne, aucune erreur JavaScript sur les deux pages.

**Ce que le lot ne porte pas, et qu'il faut savoir avant d'entrer en classe :**

1. **La version 🅰 est déclarée, pas outillée.** La page propose « le vrai jardin du collège, ou
   une maquette capteur + pompe ». Le lot ne fournit ni liste de matériel, ni protocole de
   montage, ni fiche de sécurité imprimable. Sans préparation d'atelier, la classe bascule de
   fait en 🅱 — et les élèves qui ont besoin de la main pour comprendre restent en représentation.
   *(Défaut D02 des trois audits externes, vérifié.)*
2. ~~Deux boutons de QCM dans la page~~ — **c'était faux, corrigé le 29/08/2026.** Je comptais
   les liens `href` vers un fichier `qcm_`, pas les boutons. La page porte **un seul bouton**, et
   un renvoi « pour aller plus loin » vers `qcm_xxl_40_reseaux_ip_nfc_rfid_zigbee.html`, placé
   dans le bilan — ce que la règle d'or n°4 autorise expressément. Mesure refaite sur les
   17 séquences du Thème 2 : **17 boutons pour 17 séquences, un chacune.** La règle est tenue
   partout.
3. **Aucun rôle de groupe nommé, aucun lexique** — comme les 16 autres séquences du Thème 2. Les
   outils existent (`poser_roles.py`, `generer_lexique.py`, écrits pour le Thème 1) et
   s'appliquent tels quels.
4. **Neuf codes en une séquence.** La couverture est réelle et la matrice le montre notion par
   notion ; la *maîtrise individuelle* de neuf repères en quatre séances ne se déduit pas de la
   couverture. Le lot gagne à être joué comme **vue système**, l'approfondissement réseau étant
   porté par « SOS serre » (`4e_C4.7-C4.9`) et l'approfondissement chaîne par le Book Train.
5. **31 minutes de marge sur les 220 annoncées.** C'est la troisième plus grande marge du thème (après le lampadaire 5ᵉ, +40, et « programmer le lampadaire », +35) :
   la séquence ne déborde pas, contrairement à ce que les trois audits supposaient.
