# Fiche pédagogique — 5e_C8.1 « La patère du hall »

> **Utiliser une simulation fournie pour valider la tenue mécanique d’un matériau.**
> Programme 2024, cycle 4, thème 3 — Création, conception, réalisation.

| | |
|---|---|
| **Niveau** | 5<sup>e</sup> |
| **Code principal** | `5e_C8.1` — 20 questions de QCM |
| **Code d'appui** | `5e_C3.1` — *repérer pour un ost les matériaux, les sources et les formes d’énergies, le traitement de l’information.* — 10 questions |
| **Socle** | D1.3 · D2 · D4 |
| **Durée** | 2 séances de 55 min — 85 min d'activités obligatoires, marge +25 min |
| **Matériel** | un navigateur, hors ligne. Aucune installation, aucun compte. |
| **Prérequis** | `5e_C8.2` « éprouver un matériau » — ce lot en reprend les cinq relevés |

---

## 1. La place du lot dans la spirale C8

| Niveau | Ce qu'on demande de la simulation | Qui la règle |
|---|---|---|
| **5<sup>e</sup> — `5e_C8.1`** | **l'utiliser pour décider** | **elle arrive réglée** |
| 4<sup>e</sup> — `4e_C8.1` | la paramétrer | l'élève entre les valeurs |
| 3<sup>e</sup> — `3e_C8.1` | la mettre en œuvre | l'élève choisit la question |

## 2. Ce que le lot démontre

Le simulateur reproduit **exactement** les cinq charges de rupture relevées au banc de
`5e_C8.2` : 41, 51, 53, 194, 408 kg. Puis il change
de question et compare à la **limite élastique**.

| Matériau | σ_e | Plie à | Casse à | k élastique | k rupture | Décision |
|---|---|---|---|---|---|---|
| Bois (pin) | 25 MPa | 25 kg | 41 kg | 2,1 | 3,4 | **écarté** |
| PLA imprimé en 3D | 45 MPa | 46 kg | 51 kg | 3,8 | 4,2 | retenu |
| PVC rigide | 45 MPa | 46 kg | 53 kg | 3,8 | 4,4 | retenu |
| Aluminium | 140 MPa | 143 kg | 194 kg | 11,9 | 16,1 | retenu |
| Acier doux | 235 MPa | 240 kg | 408 kg | 20,0 | 34,0 | retenu |

**Un seul matériau change de camp** — le bois. C'est vérifié par le banc de tests, pas espéré.

## 3. Déroulé

| Séance | Activité | Durée | Verrou exigé | Production |
|---|---|---|---|---|
| 1 | 1 — Prendre le simulateur en main | 15 min | `simule` | 3 réponses |
| 1 | 2 — Cinq matériaux, une seule contrainte | 20 min | `tous` | tableau rempli |
| 2 | 3 — Le banc ne disait pas la même chose | 20 min | `bois` | 3 réponses |
| 2 | 4 — Choisir, et signer l'avis | 20 min | — | 1 choix + 1 réserve |
| 2 | 5 — Réinvestissement (étagère murale) | 10 min | — | 2 réponses |

## 4. Les trois versions

- **🅰** avec le banc réel du laboratoire (celui de `5e_C8.2`) — consigne de sécurité : ne jamais
  placer une main ni la tête sous une charge suspendue, charger par paliers, lunettes à la rupture.
- **🅱** avec le simulateur de la page — hors ligne, voie par défaut.
- **🅲** sans écran — tableau imprimé, calculs à la main.

Aucune manipulation électrique : ni très basse tension, ni secteur.

## 5. Erreurs à attendre

| Erreur | Ce qu'elle révèle | Comment la traiter |
|---|---|---|
| « l'acier subit moins de contrainte » | confusion contrainte / limite | deux clics dans le simulateur : 11,8 MPa dans les deux cas |
| « le banc s'est trompé » | on cherche un coupable au lieu de la question | faire énoncer la question de chaque instrument |
| « le moins cher gagne » | un seul critère lu sur quatre | PLA imprimé en 3D : 24 € et 30 h pour 8 h disponibles |

## 6. Ce que ce lot ne fait pas

- Aucune manipulation d'objet réel en 🅱 : le geste sur la matière est dans `5e_C8.2`.
- La fatigue et le vieillissement sont hors modèle — c'est dit à l'élève, pas tu.
- Aucun corrigé d'évaluation sommative n'est publié ici.

## 7. Évaluation

Les 20 questions `5e_C8.1` du QCM sont au-dessus du seuil d'évaluabilité (5). Le code d'appui
`5e_C3.1` porte 10 questions et se reporte lui aussi. Le bilan de la séquence propose un
auto-positionnement sur `5e_C8.1`.
