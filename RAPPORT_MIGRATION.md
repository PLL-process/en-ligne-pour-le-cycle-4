# 📋 Rapport de migration — réorganisation programme 2024

*Réorganisation du dépôt `en-ligne-pour-le-cycle-4` : passage de la double arborescence
(ancien programme 2016 `t1…t4` + dossiers 2024 « à plat ») vers la structure
**Thème → Compétence → Niveau → Code** alignée sur le référentiel 2024.*

**Aucun fichier n'a été supprimé** : tout ce qui n'est pas rangé dans un code est conservé
dans `_archive-anciennes-versions/`.

---

## 🔧 Corrections apportées au passage

| Fichier | Problème constaté | Correction |
|---|---|---|
| `SEQUENCE_C11_accessible_v6.html` → `5e_C1.1/sequence.html` | Bug JavaScript : un script d'ajout automatique d'`aria-label` avait remplacé la variable `inputs` par `input aria-label="Champ de saisie"s` dans **2 boucles** (export HTML et sauvegarde cassés) + une accolade orpheline dans `toggle()` | Variable restaurée (`inputs.length`), fonction `toggle` réparée |
| `SEQUENCE_C13_C14_5e_SI_Gestion_donnees.html` (12,5 Mo !) → `5e_C1.3/` | 8 images encodées en **base64** directement dans le HTML | Images extraites dans `Images/` ; le fichier passe de **12,5 Mo à 72 Ko** |
| `SEQUENCE_C13_C14_5e_SI_Gestion_donnees.txt` (12,5 Mo) | Copie `.txt` identique au `.html` | Archivée (doublon) |
| `SEQUENCE_C15_C16_4e_Cybersecurite_V6.html` | Fichier **vide (0 octet)** | Archivé — la V6 n'a jamais existé en réalité |
| README de `vittascience_variables` | Liens GitHub Pages pointant vers l'ancien chemin `C7_C9_…` | Réécrit avec les nouveaux chemins |

## 🏷️ Choix des versions canoniques (vérifiées, pas juste « le numéro le plus haut »)

| Groupe | Version conservée | Pourquoi |
|---|---|---|
| Cybersécurité 4e (V4, V4-11, V4-12, V5, V6) | **V4-12** (= identique octet pour octet à V4-11) comme séquence principale + **V5** conservée comme *activité bonus distincte* (« Cyber Immersive », mini-exercice 2FA, pas une évolution de la V4) | V6 vide ; V4 plus ancienne |
| QCM algorigrammes domotique (V4→V12) | **V12** | Dernière itération d'une même lignée |
| TP mBot2 Python (v3-9→v4-6) | **v4-6** (116 Ko, la plus complète) | Lignée v3 puis v4 clairement incrémentale |
| QCM XXL Réseaux (v1, v2) | **v2** | Même titre, version resserrée |
| Vittascience variables (v1, v2, v3) | **v1** | ⚠️ La « v3 corrigée » est en réalité une **page de redirection vers la v1** (la v2 avait perdu des exercices) — la v1 est donc bien la référence |

Toutes les autres versions sont dans `_archive-anciennes-versions/` (25 fichiers).

## 📦 Rangement dans les codes 2024

| Nouveau chemin (code) | Contenu | Provenance |
|---|---|---|
| `5e_C1.1` | Séquence « Collecter, trier, analyser des données » (corrigée) + 3 fichiers tableur | `C1_C3_…` |
| `5e_C1.2` | Séquence « Comparer des principes techniques » (.mhtml) | `C1_C3_…` |
| `5e_C1.3` | Séquence SI / gestion de données (allégée) — couvre aussi C1.4 (README pointeur dans `5e_C1.4/`) | `C1_C3_…` |
| `4e_C1.5` | Séquence cybersécurité (V4-12) + activité bonus 2FA (V5) — couvre aussi C1.6 (README pointeur) | `C1_C3_…` |
| `3e_C1.5` | Séquence « Numérique, société, économie, environnement, santé » | `C1_C3_…` |
| `4e_C2.1` | QCM « expliquer le fonctionnement d'un objet » — *reclassé* : mieux aligné C2 (expérience utilisateur) que C1 | `C1_C3_…` |
| `4e_C4.1` | QCM automatisation | `C4_C6_…` |
| `4e_C4.7` | 2 QCM réseaux (LAN/WLAN/Zigbee + XXL 40 questions) + 9 images réseau — *reclassés* : le contenu réseau relève du thème 2 | `C1_C3_…` + `C4_C6_…` |
| `4e_C6.2` | QCM algorigrammes domotique (V12) + QCM éclairage automatique + schéma éclairage + 🆕 **séquence « Jardin connecté »** | ancien `t2`/`t4` + création |
| `3e_C6.2` | Séquence algorigrammes DNB (niveau brevet ⇒ 3e) | ancien `t2` |
| `3e_C9.1` | Vittascience variables (v1 + 16 images ré-organisées dans `Images/`) + TP mBot2 (v4-6) + README réécrit | `C7_C9_…` + ancien `t4` |

**Cas signalé à vérifier :** `Images/doc3_schema_parcours.png` a été placé dans `4e_C4.7` faute de
certitude sur la séance d'origine — à déplacer si besoin.

## 🗄️ Anciens dossiers du programme 2016

Les racines `t1-…-dic`, `t2-…-otscis`, `t3-…-msost`, `t4-…-ip` (nomenclature DIC/OTSCIS/MSOST/IP
du programme 2016) disparaissent : leur contenu réel a été reclassé dans les codes 2024 ci-dessus,
le reste n'était que des `.gitkeep`. Les 3 workflows GitHub Actions « one-shot » (déjà exécutés)
sont archivés dans `_archive-anciennes-versions/anciens-workflows-one-shot/`.

## 🆕 Contenu créé

- 🌱 **`4e_C6.2/sequence-jardin-connecte-arrosage-automatique.html`** — séquence complète et notée
  (situation déclenchante → problématique → référentiel/socle/CRCN → 3 séances avec exercices
  interactifs et simulation seuil/pompe → synthèse → grille LSU → différenciation → EDD),
  dans le thème visuel du dépôt, mode enseignant `GJEP`.
- 🖼️ **`schema_chaines_arrosage.svg`** — schéma original chaîne d'information + chaîne d'énergie.
- 🏠 **`index.html`** — page d'accueil GitHub Pages listant les 114 codes avec liens directs vers
  chaque ressource (régénérable via `make_index.py` fourni à part).
- 📄 **`README.md`** racine + README pointeurs (`5e_C1.4`, `4e_C1.6`) + README `3e_C9.1` réécrit.

## 📊 Bilan chiffré

- **114 dossiers Code** créés (38 par niveau), chacun avec `Images/` et `Synthèses/`
- **44 fichiers** rangés dans un code précis · **12** en ressources communes · **28** archivés
- **10 codes** contiennent déjà du contenu ; 104 sont prêts à accueillir tes prochaines séances
- Taille du dépôt : **52 Mo → 33 Mo** (grâce à l'extraction base64 et au tri des doublons)
