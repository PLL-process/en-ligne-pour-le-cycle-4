# Fiche pédagogique — 3e_C8.1 « Le mât de la station »

> **Mettre en œuvre une simulation pour valider la tenue mécanique d’un matériau.**
> Programme 2024, cycle 4, thème 3 — Création, conception, réalisation.

| | |
|---|---|
| **Niveau** | 3<sup>e</sup> |
| **Code principal** | `3e_C8.1` — 20 questions de QCM |
| **Code d'appui** | `3e_C3.4` — *définir et mettre en œuvre un protocole pour mesurer une caractéristique, une performance d’un ost.* — 10 questions |
| **Socle** | D1.3 · D2 · D4 · D5 |
| **Durée** | 3 séances de 55 min — 135 min d'activités obligatoires, marge +30 min |
| **Matériel** | un navigateur, hors ligne. Aucune installation, aucun compte. |
| **Prérequis** | `3e_C8.2` « proposer un protocole » — ce lot en reprend les cinq profilés |

---

## 1. Le geste de la 3<sup>e</sup>

Utiliser (5<sup>e</sup>) → paramétrer (4<sup>e</sup>) → **mettre en œuvre** (3<sup>e</sup>). Ici,
l'élève choisit **la hauteur**, **le cas de charge** et **la limite de comparaison**. Douze
réglages possibles, quatre verdicts différents.

## 2. Ce que le lot démontre

| Profilé | Section | Moment du banc | Moment du vent | Écart |
|---|---|---|---|---|
| Tube aluminium Ø50 × 3 | ronde | 200 N·m | 204 N·m | +2 % |
| Barre pleine acier Ø20 | ronde | 200 N·m | 128 N·m | -36 % |
| Tube PVC Ø50 × 3 | ronde | 200 N·m | 204 N·m | +2 % |
| Poutre bois 40 × 40 | carrée | 200 N·m | 298 N·m | +49 % |
| Tube acier galvanisé Ø33,7 × 2,6 | ronde | 200 N·m | 163 N·m | -19 % |

Le banc appliquait 200 N·m **à tout le monde**. Le vent, non :
il dépend de la largeur offerte et de la forme de la section (1.2 pour un tube rond,
2 pour un carré).

| Réglage à 2000 mm | Retenus |
|---|---|
| poussée du banc + rupture | 1 — Tube aluminium Ø50 × 3 |
| poussée du banc + limite élastique | 1 — Tube aluminium Ø50 × 3 |
| vent + rupture | 2 — Tube aluminium Ø50 × 3, Tube acier galvanisé Ø33,7 × 2,6 |
| vent + limite élastique | 1 — Tube aluminium Ø50 × 3 |

## 3. Le piège délibéré

Un élève qui recopie le réglage du banc obtient **le bon profilé**. Le lot ne le sanctionne pas
par une mauvaise réponse : il montre, à l'activité 2, que ce bon résultat reposait sur une charge
fausse pour deux candidats sur cinq. *Un bon résultat obtenu par un mauvais raisonnement ne se
reproduira pas.*

## 4. Déroulé

| Séance | Activité | Durée | Verrou exigé | Production |
|---|---|---|---|---|
| 1 | 1 — Refaire dire au calcul ce que le banc a dit | 25 min | `regle` | 2 réponses |
| 1 | 2 — Le vent ne pousse pas comme le banc | 35 min | `vent` | 3 réponses |
| 2 | 3 — À quelle limite compares-tu ? | 25 min | `bonreglage` | 2 nombres + 1 réponse |
| 2 | 4 — Le bon réglage, et ce qu'il ne voit pas | 30 min | `bonreglage` | 1 profilé + 1 réserve |
| 3 | 5 — Réinvestissement (le quai du port, 180 km/h) | 20 min | — | 2 réponses |

## 5. Les trois versions

- **🅰** avec le banc réel de `3e_C8.2` — consigne de sécurité : personne dans l'axe du mât
  pendant l'essai, charge par paliers, lunettes à la rupture.
- **🅱** avec le simulateur de la page — hors ligne, voie par défaut.
- **🅲** sans écran — tableau des moments imprimé, coefficients calculés à la main.

Aucune manipulation électrique : ni très basse tension, ni secteur.

## 6. Les limites du modèle, à dire aux élèves

- La **vitesse du vent n'est pas réglable** : c'est volontaire, et c'est l'objet du
  réinvestissement.
- L'**encastrement est supposé parfait** : une platine qui tourne augmente la flèche (bonus).
- La **fatigue** est hors modèle, comme elle l'était hors du banc : c'est l'angle mort partagé.
- Le **coefficient de forme** est une valeur d'ordre de grandeur, suffisante au collège.

## 7. Évaluation

Les 20 questions `3e_C8.1` et les 10 questions `3e_C3.4` sont toutes au-dessus du seuil
d'évaluabilité. Le bilan propose un auto-positionnement sur `3e_C8.1`.
