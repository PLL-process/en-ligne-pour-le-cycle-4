# Fiche pédagogique / inspection — Le lampadaire intelligent

## Identification

| Champ | Valeur |
|---|---|
| Niveau | 5e (programme 2024, applicable rentrée 2026-2027) |
| Codes | 5e_C4.1 · C4.2 · C4.3 · C4.4 · C4.5 · C4.6 · C4.7 · C4.8 (îlot 5e complet de la compétence) |
| Thème | Thème 2 — Structure, fonctionnement, comportement |
| Compétence parente | C4 — Décrire et caractériser l'organisation d'un OST |
| Référentiel | BO n°9 du 29/02/2024 · cahier Nathan 5e (éd. 2024) |
| Domaines du socle | D1.3, D2, D3, D4, D5 |
| CRCN | 1.3 Traiter des données · 5.1 Résoudre des problèmes techniques |
| Durée | 6 séances de 55 min |

## Sous-compétences

| Code | Intitulé | Activités |
|---|---|---|
| 5e_C4.1 | Associer des solutions techniques à une ou des fonctions techniques. | 1, 7, R |
| 5e_C4.2 | Identifier des constituants de la chaîne d’énergie d’un objet technique (l’organisation de la chaîne d’énergie étant fournie). | 2, R |
| 5e_C4.3 | Indiquer la nature des énergies en entrée et en sortie des constituants de la chaîne d’énergie. | 2, R |
| 5e_C4.4 | Identifier les principaux matériaux constitutifs d’un OST. | 1, R |
| 5e_C4.5 | Identifier des constituants de la chaîne d’information d’un OST (l’organisation de la chaîne d’information étant fournie). | 3, R |
| 5e_C4.6 | Déterminer des descripteurs permettant de décrire des objets sous forme de données en précisant leurs types et leurs formats. | 4 |
| 5e_C4.7 | Identifier les composants qui constituent un réseau local (terminaux, commutateurs, liaisons filaires et sans fil (WiFi)) et sa topologie. | 5, R |
| 5e_C4.8 | Justifier la nécessité d’identifier les terminaux pour communiquer sur un réseau local (activité débranchée et vérification par un outil de simulation). | 6 |

## Prérequis

Cycle 3 : fonction d'usage, premiers objets techniques. Aucun prérequis de cycle 4 : c'est la **séquence d'entrée du niveau 5e** dans le Thème 2.

## Situation déclenchante et problématique

- **Situation** : la mairie a installé des lampadaires solaires sur le parking du collège ; l'un d'eux reste allumé en plein jour, un autre ne s'allume plus. Le club techno est chargé d'expliquer comment ils fonctionnent et d'aider la mairie à les suivre.
- **Problématique** : *Comment décrire complètement un objet technique — ses fonctions, ses chaînes d'énergie et d'information, ses matériaux, ses données — pour comprendre son comportement et le gérer à distance ?*

## Déroulé

S1 : fonctions/solutions sur l'objet réel + matériaux et critères de choix (act. 1). S2 : chaîne d'énergie fournie à compléter + natures des énergies à chaque étape (act. 2). S3 : chaîne d'information + **simulateur interactif** du lampadaire — jour / nuit / nuit + passage, avec verrou expérientiel (act. 3). S4 : décrire les 6 lampadaires de la mairie par des données — descripteurs, types, formats, lecture pour agir (act. 4). S5 : le réseau local du collège (act. 5) + **jeu du courrier débranché** sur l'identification (act. 6) — 50 min. S6 : le diagramme FAST du lampadaire complété (act. 7, exercice 2 de l'atelier FAST : trois solutions, un intrus, une lecture « pourquoi ? » — il reprend le FAST lu en séance 1 avec ce que les séances 2 et 3 ont établi) + réinvestissement sonnette connectée (R) — 35 min — puis synthèse, Bonus, bilan et QCM.

> **24/10/2026 — six séances au lieu de cinq.** La séance 5 annonçait 25 + 25 + 25 = 75 min pour 55. Le réinvestissement et la clôture sont passés dans une séance 6, complétée par l'exercice 2 de l'atelier FAST (10 min). Minutes d'activités annoncées par séance : 50 · 40 · 40 · 40 · 50 · 35. L'exercice « Compléter la bête à cornes du lampadaire » (atelier besoin) a été écarté : son code, 5e_C3.3, n'est pas un code de la séquence. Une sauvegarde faite avec la version à cinq séances se relit (activités 1 à 7 gardent leur clé ; la progression passe à 7 / 8).

## Outils, versions, sécurité

Simulateur de lampadaire intégré à la page (curseur de luminosité, bouton passage, états éteint/veille/pleine puissance) — aucune donnée envoyée, fonctionne hors ligne. Versions : 🅰 sortie sur le parking + maquette Grove (capteur lumière, PIR, LED — **très basse tension uniquement**) ; 🅱 simulateur dans la page ; 🅲 fiches papier + jeu du courrier avec enveloppes réelles.

## Différenciation, inclusion, accessibilité

Aides ×2 par activité ; corrections exhaustives ; listes déroulantes (limite la charge d'écriture, adapté DYS) ; navigation clavier ; reduced-motion ; impression A4 ; minuteur QCM désactivable ; vocabulaire FR/EN ; langue calibrée 12 ans.

## Évaluation

Formative : vérificateurs intégrés à chaque activité, verrou expérientiel au simulateur (les 3 situations doivent être réellement observées). QCM 36 q (4 par code, et 5 pour C4.1, C4.2, C4.3 et C4.6 — les quatre que nulle autre banque ne renforce ; 6 illustrées). Sommative à construire par l'enseignant, corrigé non publié.

> **Réserve sur le report au LSU — mesurée le 29/08/2026.** Le QCM porte **quatre questions par
> code**, sur les huit codes du lot (`_outils/controle_echantillonnage.py`). Quatre questions ne
> font pas une mesure : un élève qui maîtrise la moitié d'une notion obtient 2/4 ou 4/4 selon
> lesquelles il connaît, et l'écart part au bulletin. Le **bilan par code de ce QCM se lit comme
> un repérage** — ce qu'il faut revoir — et non comme une validation code par code. Ce que le lot
> permet de valider solidement, ce sont les productions des activités et le verrou du simulateur.
> *(L'audit externe ChatGPT du Thème 2 formulait exactement cette réserve ; vérification faite,
> elle est fondée.)*

## Bilan et prolongements

Vers 4e_C4 (chaînes complètes, flux) et l'îlot 5e_C6 (comportement programmé du même lampadaire — objet-fil réutilisable) ; EDD : pollution lumineuse, sobriété de l'éclairage public ; lien mairie/commune (usage citoyen des données).
