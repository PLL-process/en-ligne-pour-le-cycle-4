# 📋 Rapport d'intégration — branche `codex/jumeau-numerique-v1` → `main`

*Tri des 82 fichiers utiles de la branche de sauvegarde (sur 77 647 : le reste était
`node_modules/`, `coverage/` et `.idea/` d'un projet React embarqués par accident —
un `.gitignore` a été ajouté à la racine pour que ça ne se reproduise plus).*

## ✅ Promotions (nouvelles versions de référence)

| Emplacement | Nouvelle référence | Remplace |
|---|---|---|
| `4e_C1.4` | **Cybersécurité V16** (PWA + accessibilité + tests, 123 Ko, vérifiée complète) + bonus V5 « Cyber Immersive » | V4-12 (archivée) |
| `4e_C4.7` | **QCM XXL Réseaux `v2_fixed3`** (= `fixed` : le `fixed2` a été abandonné, retour arrière constaté) | v2 (archivée) |
| `3e_C9.1/Images` | `capture-01-variables.png` mise à jour (675 Ko) | ancienne capture |
| `4e_C4.4` | 🆕 **QCM eCall** (chaîne d'information d'une voiture — 5 vraies questions + questions générées à retravailler) | — |

## 🔧 Correction d'une erreur de la migration initiale (mea culpa)

La migration visait un code **`4e_C1.5` qui n'existe pas** (le C1 de 4e s'arrête à C1.4 ;
« C1.5/C1.6 » = numérotation **5e** de la cybersécurité). Résultat : la séquence cybersécurité
V4-12 et le bonus V5 avaient été **silencieusement omis** du dépôt réorganisé, et un dossier
fantôme `4e_C1.6` avait été créé. Correctif :
- fichiers **récupérés depuis l'historique git** (commit `d5b69cc`) — rien n'était perdu ;
- rangés dans **`4e_C1.4`** (code 4e le plus proche : usage raisonné, identité numérique),
  avec un README expliquant le croisement avec 5e_C1.5/5e_C1.6 ;
- dossier fantôme `4e_C1.6` supprimé ; V4-12 archivée en `…_ex-canonique.html`.

## 🗄️ Archivé (rien de supprimé)

- Cybersécurité **V7, V7_corrigé, V8-2/3/4, V10 → V15** (⚠️ V11 tronquée, sans `</html>`)
- QCM XXL : v1 modifiée localement, `v2_fixed2` (piste abandonnée), ébauche v2 de 10 Ko
- **10 sauvegardes `.bak`** de `vittascience_variables.html` (mai 2026)
- Variantes algorigrammes domotique (V1, V2, V3, V5 locale, V6 locale — la V12 reste la référence ;
  si la « V6 locale » de 80 Ko était en réalité ta préférée, dis-le : échange en 1 commit)
- `audit-skills/` (audit de dépôts de skills — travail méta, pas pédagogique)
- **`chantier-cybersecurite-react/`** : sources du projet React `cybersecurite-4e-v12`
  (src/, configs — sans `node_modules`, `coverage` ni `package-lock`). Projet inachevé
  (plusieurs composants vides) ; la V16 HTML le supplante fonctionnellement.

## 🚫 Écarté (doublons exacts vérifiés par empreinte MD5)

- `Install_manager_python1-5.png` = copies identiques des `install-manager-python-01…05.png`
  déjà dans `3e_C9.1/Images/`.
