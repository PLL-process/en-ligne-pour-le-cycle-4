# 📓 Journal des décisions — écosystème cycle 4

*À relire au début de chaque session de travail. Une entrée par décision
structurante. Les décisions « pédagogiques ou matérielles » restent à Pascal ;
les décisions de publication restent à ChatGPT.*

## 2026-07-21 — Lot 0 : audit initial (Claude, branche `audit/couverture-initiale-2026-07`)

1. **Référentiel opérationnel** : `_outils/data_competences.py` (114 codes
   vérifiés : 38 × 3 niveaux) est la transcription opérationnelle retenue,
   fondée sur la proposition Nathan correspondant au référentiel 2024.
   **CONFIRMÉ par la gouvernance le 21/07/2026** (le classeur Excel n'est pas
   versionné ; `data_competences.py` fait foi). La convention d'identifiants
   préfixés (`5e_C1.1`, `4e_C4.4`…) est la convention interne officielle du
   dépôt et est conservée.
2. **Générateur d'audit** : la matrice de couverture est produite par un script
   régénérable (`_outils/build_audit.py`) plutôt qu'à la main, pour rester
   synchronisable après chaque lot. Le script n'importe pas `make_index`
   (son import régénère l'index par effet de bord).
3. **Statuts** : `4e_C6.2` est le seul code `COMPLET ET VALIDABLE` (séquence
   modèle). Un QCM isolé = `PARTIEL`, jamais « séquence ».
4. **Mutualisations reconnues** : 5e_C1.4 → 5e_C1.3 (pointeur existant).
   Croisements déclarés mais sans pointeur (5e_C1.5/C1.6 → 4e_C1.4) : à
   matérialiser par des README dans un prochain lot.
5. **Progression 3e** : proposition de 5 séquences-projets (P1 station d'alerte
   cyclonique, P2 programmation, P3 réseaux/Internet, P4 réparation, P5 abri de
   cour) + fil rouge argumentaires — couvrant les 38 codes de 3e. **À VALIDER PAR PASCAL**
6. **Premier lot proposé** : 3e_C4.3, 3e_C4.4, 3e_C4.5+3e_C4.6 (mutualisés) +
   corrections des liens cassés 3e_C9.1 / 5e_C1.1 / 4e_C1.4. **À VALIDER**
7. **Aucune modification de ressource existante** dans ce lot 0 : uniquement des
   fichiers nouveaux (audit, feuille de route, inventaires, skills). Les `.pyc`
   versionnés et le `.gitignore` seront traités dans un lot ultérieur par
   ChatGPT (décision de dépôt, pas de contenu).
8. **Aucun téléchargement / aucune installation** effectués ; aucune skill
   externe ajoutée (skills locales uniquement — voir `SKILLS_AUDIT.md`).

### Arbitrages (état au 21/07/2026, mis à jour après retour gouvernance)

| # | Question | Décideur | Statut |
|---|---|---|---|
| A1 | Classeur Excel référentiel | — | **RÉSOLU** : `data_competences.py` fait foi (transcription retenue) |
| A2 | QCM eCall : 4e_C4.4 → 4e_C4.5 ? | — | **RÉSOLU** : reste en 4e_C4.4 (rattachement correct ; erreur d'analyse de l'audit initial, confondue avec 5e_C4.4) |
| A3 | `5e_C1.2/sequence.mhtml` : contenu 5e ou 4e ? | Pascal | ouvert |
| A4 | QCM domotique/éclairage : rester en 4e_C6.2 ? | Pascal | ouvert |
| A5 | Affiche Delagrave : droit de rediffusion ? | Pascal | ouvert |
| A6 | Progression 3e (P1→P5) et périmètre du LOT 1 | Pascal | ouvert |
| A7 | Publication du lot 0 (audit) sur `main` | ChatGPT | en cours (PR brouillon depuis `draft/agent-sequences`) |

## 2026-07-21 — Gouvernance GitHub configurée (retour ChatGPT/Pascal)

- `main` protégée : intégration uniquement par Pull Request ; fusion finale par
  ChatGPT après validation de Pascal.
- Branche de travail autorisée pour Claude : **`draft/agent-sequences`**
  (poussées et PR brouillon autorisées ; jamais de poussée sur `main`, de
  fusion, de modification des règles, de suppression de branche, ni de demande
  de clé/jeton).
- Corrections apportées au LOT 0 avant poussée : A1 et A2 résolus (voir tableau),
  convention d'identifiants préfixés explicitement confirmée dans l'audit.
- Lots suivants autorisés en préparation (PR distinctes, sans fusion) :
  corrections techniques rapides, puis LOT 1 « Station d'alerte cyclonique
  connectée » (3e_C4.3, 3e_C4.4, 3e_C4.5, 3e_C4.6) en versions A/B/C, avec QCM
  d'entraînement public et évaluation sommative à corrigé non publié.
- Statut de relecture : les séquences peuvent rester `A_RELIRE_PASCAL` sans
  bloquer la préparation des lots suivants.
