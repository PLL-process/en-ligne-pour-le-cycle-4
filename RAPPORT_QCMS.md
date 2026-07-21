# 📋 Rapport — génération des QCM (modèle « QCM XXL Réseaux »)

Tous les QCM ci-dessous reprennent **exactement** le modèle du QCM XXL Réseaux (fixed3) :
mêmes styles, même moteur de correction (QCM, cases multiples, réponse libre à mots-clés,
réponse numérique), aides détaillées repliables, score global ramené sur 20, identité élève.

## ✅ Terminé / fusionné

| Fichier | Contenu |
|---|---|
| `4e_C4.4/qcm_ecall_chaine_information.html` | **eCall terminé : 40 vraies questions** (les 5 d'origine conservées + 35 nouvelles ; l'ébauche aux questions auto-générées est archivée) |
| `4e_C4.7/qcm_xxl_40_reseaux_ip_nfc_rfid_zigbee.html` | **Fusion : 77 questions** = 40 du XXL + 37 du « QCM LAN/WLAN/Hub/Switch/Routeur/Zigbee » (3 doublons retirés : rôle du switch, rôle du routeur, fréquence Zigbee). L'ancien fichier est archivé. |

## 🆕 Un QCM par contenu du site (9 nouveaux, 232 questions au total)

| Dossier | QCM créé | Cible |
|---|---|---|
| `5e_C1.1` | `qcm_donnees_tableur.html` (24 q) | données, capteurs, tableur, graphiques |
| `5e_C1.2` | `qcm_principes_techniques.html` (24 q) | fonction vs principe, comparaison par critères |
| `5e_C1.3` | `qcm_systemes_information_donnees.html` (24 q) | SI, arborescence, stockage (couvre C1.4) |
| `4e_C1.4` | `qcm_cybersecurite_usage_raisonne.html` (24 q) | accompagne la séquence Cybersécurité V16 |
| `3e_C1.5` | `qcm_numerique_societe.html` (24 q) | impacts économie/environnement/santé |
| `4e_C4.4` | `qcm_ecall_chaine_information.html` (40 q) | chaîne d'information d'un objet réel |
| `4e_C6.2` | `qcm_jardin_connecte.html` (24 q) | accompagne la séquence Jardin connecté |
| `3e_C6.2` | `qcm_algorigrammes_dnb.html` (24 q) | symboles, logique, préparation brevet |
| `3e_C9.1` | `qcm_python_variables.html` (24 q) | accompagne Vittascience variables + TP mBot2 |

**Non dupliqués volontairement** : `4e_C2.1` (qcm_fonctionnement_objet) et `4e_C4.1`
(qcm_automatisation_premium) sont déjà des QCM — pas de QCM sur un QCM.

**Outil réutilisable** : `_outils/qcm_generator.py` + `_outils/banks_*.py` + `_outils/build_qcms.py`
permettent de régénérer ou d'étendre n'importe quel QCM (ajouter des questions = ajouter des
lignes dans la banque, relancer le script).
