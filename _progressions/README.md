# _progressions — Progressions annuelles & générateurs de séquences (2026-2027)

Classeurs de progression par classe (décision Pascal du 23/07/2026). Chaque
classe a UN fichier : calendrier Martinique 2026-2027, référentiels (cycle 4 +
niveau), progression annuelle, puis un onglet **générateur de séquence** par
séquence, dans l'ordre de l'année.

## Fichiers

| Fichier | Statut | Ossature | Générateurs remplis |
|---|---|---|---|
| `5e/Progression_Techno_5e_2026-2027_Martinique.xlsx` | ✅ maquette validée par Pascal | Fable | S4, S5 (✅ ressources en ligne), S6 (pré-rempli) |
| `4e/Progression_Techno_4e_2026-2027_Martinique.xlsx` | ✅ prêt à remplir | Fable | S4, S5, S6 (pré-remplis, QCM existants liés) |
| `3e/Progression_Techno_3e_2026-2027_Martinique.xlsx` | ✅ prêt à remplir | Fable | S4, S5, S6 (REMPLIS — 4 séquences en ligne) |

## Qui remplit quoi (règle du dépôt : l'IA d'un thème est SEULE à modifier ses contenus)

Classeur 4e : S1 (C1.1-3), S2 (C1.4), S3 (C2.x, C3.x) → **IA Thème 1** ·
S4-S5-S6 → Fable (pré-remplis) · S7 (C7/C8/C9) → **IA Thème 3**.
⚠ Correctif intégré : 4e_C4.3 (forme ↔ procédé), absent de la progression
initiale du référentiel, est rattaché à S6 — à entériner au Conseil du 28/07.

Classeur 3e (9 séquences, année DNB — 30 séances au lieu des 35 sur-planifiées
du référentiel, 3 semaines de révisions DNB en juin) : S1-S2-S3 → **IA Thème 1**
· S4-S5-S6 → Fable (remplis : station cyclonique, Internet Sainte-Luce,
SOS station + Programmer l'alerte — toutes en ligne) · S7-S8-S9 (projet fil
rouge en 3 volets) → **IA Thème 3**. ⚠ 3e_C4.1 et C4.2 : ressource en ligne
à produire (Fable, signalé dans S4).

Classeur 5e :

| Onglet | Séquence | Codes | Responsable |
|---|---|---|---|
| S1 | Environnement numérique | 5e_C1.4→C1.6 | **IA Thème 1** |
| S2 | Comparer pour choisir | 5e_C1.1→C1.3, C3.1, C3.3 | **IA Thème 1** |
| S3 | Chaîne d'énergie | 5e_C2.1-C2.2 (+C4.1→C4.3 déjà couverts en ligne) | **IA Thème 1** (Fable a posé la part C4) |
| S4 | Lampadaire (1) : information, données, programmes | 5e_C4.5-C4.6, C6.1→C6.3 | Fable — ✅ rempli |
| S5 | Lampadaire (2) : réseau local | 5e_C4.7-C4.8 | Fable — ✅ rempli |
| S6 | SOS panne | 5e_C5.1→C5.3 | Fable — pré-rempli (séquence en ligne 🔜) |
| S7 | Mini-projet | 5e_C7.x, C8.x, C9.x | **IA Thème 3** |

## Canevas OBLIGATOIRE d'un générateur (à entériner au Conseil du 28/07)

Chaque onglet générateur contient, dans cet ordre :

1. **En-tête** : titre, thème, période, nombre de séances, responsable, statut.
2. **Identification** : problématique · situation déclenchante · prérequis ·
   objectifs de synthèse · piste d'évaluation · **domaines du socle mobilisés**
   (agrégés) · **CRCN / Pix** (compétences ET niveaux visés) · versions 🅰🅱🅲 ·
   liens EPI/parcours · repères cahier Nathan (pages) · ressources en ligne.
3. **Tableau des compétences** : code · intitulé OFFICIEL (copié du référentiel,
   jamais reformulé) · domaines du socle PAR CODE · séances · évaluation LSU.
4. **Déroulé par séance** : question directrice · activités & supports (liens
   complets vers les ressources en ligne) · démarche · bilan/trace écrite ·
   **bloc jaune « Cahier de texte Pronote »** en 2 champs prêts à coller
   (« Contenu de la séance » + « Travail à faire » avec lien direct, durée
   estimée, mention « faisable sur téléphone » le cas échéant) · ligne de
   suivi enseignant (fait le / report / aléa).
5. **Répartition 🏫 / 🏠 / 🔁** indiquée pour chaque séance (classe / maison /
   hybride) — cohérente avec l'onglet Progression.

Mise en forme : reprendre STRICTEMENT les styles des onglets S4/S5 (polices
Arial, couleurs du thème, blocs jaunes, ligne de suivi grise). Modifier le
classeur par script openpyxl de préférence (pas de recalcul cassé, pas de
suppression des formules de l'accueil et de la progression).

## Vérification croisée des « compétences écrites » (ordre du jour du Conseil du 28/07)

Décision Pascal du 23/07 : « parfois on se trompe ». Au Conseil, chaque IA
vérifie les onglets DES AUTRES thèmes et signale (sans modifier) :

- intitulés des codes conformes au référentiel 2024 (mot pour mot) ;
- rattachement séquence ↔ codes correct (pas de code orphelin ni de doublon) ;
- domaines du socle conformes à la colonne du référentiel ;
- CRCN plausible (compétence ET niveau) ;
- cohérence des 38 codes 5e : chaque code apparaît dans UNE séquence au moins.

Les corrections restent faites par l'IA responsable de l'onglet.

## Règles générales

- Ne JAMAIS renommer les onglets ni changer l'ordre (liens internes).
- Ne pas toucher aux onglets Calendrier / Frise / Référentiels / Progression
  sans passer par Fable (ossature commune) — proposer les changements au
  Conseil ou dans le JOURNAL.
- Après remplissage : vérifier le classeur avec un recalcul LibreOffice
  (`soffice`) et signaler l'onglet rempli dans JOURNAL_DES_DECISIONS.md.
