# 🗺️ Feuille de route de complétion — Technologie cycle 4

*Établie le 21 juillet 2026 à partir de l'audit (`AUDIT_COUVERTURE_PEDAGOGIQUE.md`).
Objectif : couvrir les 114 codes par une progression cohérente, sans produire
114 séquences quasi identiques — les mutualisations pédagogiquement justifiées
sont indiquées code par code.*

**Rappels de gouvernance :** travail par lots de 3 à 5 codes, préparés en local,
transmis à ChatGPT (seul autorisé à pousser), validés par Pascal.
Aucun code validé ne sera régénéré pour des raisons cosmétiques.

---

## 1. Priorités (dans l'ordre)

1. **3e — rentrée 2026-2027** (programme 2024 applicable pour la première fois) ;
2. corrections bloquantes sur l'existant (liens cassés, mhtml) — rapides et sans risque ;
3. codes sans aucune ressource nécessaires à une progression annuelle cohérente 5e/4e ;
4. complétion des séquences existantes (différenciation, LSU, exports, fiches professeur) ;
5. accessibilité et évaluation chiffrée /20 sur tout le parc ;
6. harmonisation graphique ;
7. enrichissements facultatifs (EPI, versions bilingues des mots-clés…).

---

## 2. Progression annuelle 3e proposée (à valider par Pascal)

Cinq séquences-projets couvrent les 38 codes de 3e par mutualisation raisonnée.
Chaque séquence suit le gabarit « Jardin connecté » amélioré, avec versions
A (matériel réel), B (simulation), C (sans matériel), QCM d'entraînement public
et évaluation sommative non publiée.

| # | Séquence-projet (contexte martiniquais) | Codes principaux | Codes en croisement | Matériel principal | Logiciel principal |
|---|---|---|---|---|---|
| P1 | **Station d'alerte cyclonique connectée** — mesurer, alerter, communiquer (1er trimestre, aboutit au défi programmation) | 3e_C4.3, 3e_C4.4, 3e_C4.5, 3e_C4.6 | 3e_C1.5 (existant) | Arduino UNO/R4 + Grove (LCD, capteurs) — `MATÉRIEL À CONFIRMER` en nombre | VittaScience → Arduino IDE ; LibreOffice Calc (données) |
| P2 | **Programmer l'alerte** — algorithme, fonctions, IHM (prolonge P1) | 3e_C6.1, 3e_C6.2 (existant : algorigrammes DNB), 3e_C6.3, 3e_C9.1 (existant), 3e_C9.2 | 3e_C4.4 | mBot2 ou Arduino + Grove | mBlock 5 / VittaScience / Python |
| P3 | **Internet jusqu'à Sainte-Luce** — comment l'information circule entre réseaux | 3e_C4.7, 3e_C4.8 | 3e_C4.1, 3e_C4.2 (énergie/matériaux des infrastructures, en ouverture) | aucun (activité débranchée + simulation) | Filius (prioritaire), Packet Tracer (approfondissement, accès à confirmer) |
| P4 | **Réparer plutôt que jeter** — diagnostic, dépannage, pièce sur mesure (indice de réparabilité) | 3e_C5.1, 3e_C5.2, 3e_C5.3, 3e_C5.4, 3e_C3.3 | 3e_C3.4, 3e_C8.2, 3e_C8.3 | objets à diagnostiquer, impression 3D `MATÉRIEL À CONFIRMER — prévoir alternative simulation` | FreeCAD/SolidWorks (pièce), simulation HTML |
| P5 | **Concevoir un abri ombragé pour la cour** — projet de conception complet, préparation à l'oral du DNB | 3e_C7.1 → 3e_C7.7, 3e_C8.1, 3e_C8.3 | 3e_C3.1, 3e_C3.2, 3e_C2.1, 3e_C7.8 (si objet connecté intégré) | maquette/prototype léger | Sweet Home 3D + FreeCAD/OpenSCAD ; GanttProject (C7.1) |
| — | **Fil rouge argumentaires** — courtes activités réparties dans l'année (débats, écrits courts) | 3e_C1.1, 3e_C1.2, 3e_C1.3, 3e_C1.4, 3e_C2.1, 3e_C3.1, 3e_C3.2 | avec P4/P5 | aucun | activités HTML/papier |

Chaque code garde son dossier : soit le contenu propre, soit un README pointeur
vers la séquence mutualisée (règle du dépôt déjà appliquée pour 5e_C1.4).

## 3. Progressions 5e et 4e (seconde vague, après les lots 3e)

- **5e** : consolider l'îlot C1 existant (C1.1→C1.6, dont pointeurs cybersécurité
  vers 4e_C1.4 ou déclinaison propre) ; puis « Découvrir les objets qui nous
  entourent » (C2.1, C2.2, C3.1→C3.4 — cycle de vie, choix d'un objet) ; « Chaînes
  d'énergie et d'information » (C4.1→C4.8, réseau local simple avec Filius) ;
  « Premiers programmes » (C6.1→C6.3, C9.1→C9.3 avec mBlock/mBot2) ; « Premier
  projet guidé » (C5.1→C5.3, C7.1→C7.6, C8.1→C8.3).
- **4e** : compléter les îlots entamés — habiller les QCM isolés (C2.1, C4.1,
  C4.4 eCall, C4.7 réseaux + Filius), prolonger Jardin connecté vers
  C6.1/C6.3 et C9.x (versions B/C), créer le bloc conception C7/C8 (objet
  connecté du quotidien), diagnostic C5 (maintenance du parc mBot2 du collège).

Détail code par code : colonne `croisement` + statut du CSV d'audit ; ce plan
sera affiné lot après lot, sans jamais régénérer un code validé.

---

## 4. Corrections rapides (lot technique transversal, à glisser tôt)

| Fichier | Correction | Effort |
|---|---|---|
| `3e_C9.1/vittascience_variables.html` | `assets/` → `Images/` (17 liens) | 5 min + test |
| `5e_C1.1/sequence.html` | nom xlsx + remplacer 6 gabarits `{{…}}` par des SVG | 30 min |
| `4e_C1.4/activite-bonus….html` | chemins images + recréer `indentation_error.png` (SVG original) | 30 min |
| `3e_C1.5/sequence….html` | lien PDF propre (après arbitrage licence Delagrave) | 10 min |
| `4e_C4.1/qcm_automatisation_premium.html` | résoudre `${q.img}` | 20 min |
| `.gitignore` | ajouter `__pycache__/` + retrait du suivi des `.pyc` | 5 min |
| `5e_C1.2/sequence.mhtml` | conversion en HTML propre (après arbitrage 5e/4e) | 1-2 h |

---

## 5. Premier lot proposé — « LOT 1 : 3e, cap sur la rentrée 2026 »

**Périmètre (4 codes + corrections) :**

1. **3e_C4.3** — séquence « Station d'alerte cyclonique » séances 1-2 (chaîne
   d'information de la station : capteurs → traitement → alerte) ;
2. **3e_C4.4** — séance « du signal à la donnée » (grandeur analogique →
   conversion → seuil), versions A (Grove), B (VittaScience), C (données fournies) ;
3. **3e_C4.5 + 3e_C4.6** — mutualisées dans la même séquence (représenter les
   informations en données ; formats/stockage/transmission des fichiers) avec
   activité tableur (LibreOffice/CSV) sur données météo réelles de Martinique ;
4. **Corrections rapides** : les 3 premières lignes du §4 (liens cassés 3e_C9.1,
   5e_C1.1, 4e_C1.4).

**Livrables :** conformes au cahier des charges (README, séquence, projet élève,
QCM entraînement ~24 q, évaluation élève sans correction publiée + correction
professeur privée signalée à ChatGPT, grille /20 + LSU à pondération paramétrable,
fiche professeur, fiche inspection, SOURCES_MEDIAS.md, manifest.json, SVG
originaux, synthèses avec mots-clés FR/EN).

**Pourquoi ce lot :** il ouvre la progression 3e (P1) utilisée dès septembre 2026,
s'appuie sur du matériel confirmé (Arduino + Grove) avec repli simulation complet,
et corrige au passage les liens cassés les plus visibles.

**Lots suivants (prévision) :** LOT 2 = P2 programmation (s'appuie sur 3e_C6.2 et
3e_C9.1 existants à consolider) · LOT 3 = P3 réseaux (Filius) · LOT 4 = P4
réparation · LOT 5 = P5 conception/abri (plus long, à démarrer avant le 2e
trimestre) · puis vague 4e, puis vague 5e, puis accessibilité/harmonisation.

---

## 6. Reprise de session

À chaque nouvelle session, relire dans l'ordre : `AUDIT_COUVERTURE_PEDAGOGIQUE.md`,
cette feuille de route, `JOURNAL_DES_DECISIONS.md`, le dernier `manifest.json`
de lot, et la liste des codes déjà validés (statut `COMPLET ET VALIDABLE` dans le
CSV régénéré via `python3 _outils/build_audit.py`).
