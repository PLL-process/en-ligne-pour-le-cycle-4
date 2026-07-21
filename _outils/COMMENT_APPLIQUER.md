# 🚀 Comment appliquer la réorganisation sur GitHub

Le plus simple (10 minutes, avec git installé) :

```bash
git clone https://github.com/PLL-process/en-ligne-pour-le-cycle-4.git
cd en-ligne-pour-le-cycle-4
# 1. Vider l'ancienne structure (l'historique git conserve tout, rien n'est perdu)
git rm -r "C1_C3_Les-objets-et-les-systèmes-techniques" "C4_C6_Structure, fonctionnement, comportement" \
  "C7_C9_Creation-conception-realisation-innovations" t1-* t2-* t3-* t4-* .github
# 2. Extraire le zip "en-ligne-pour-le-cycle-4_reorganise.zip" ICI (à la racine du dépôt)
# 3. Commit + push
git add -A
git commit -m "Réorganisation programme 2024 : Thème > Compétence > Niveau > Code"
git push
```

Sans git : GitHub → ton dépôt → bouton **Add file → Upload files** → glisser les dossiers
extraits du zip (par lots), puis supprimer les anciens dossiers via l'interface web
(chaque dossier : ouvrir un fichier → ⋯ → Delete directory).

Ensuite : Settings → Pages doit déjà pointer sur la branche main — la nouvelle page
d'accueil `index.html` s'affichera automatiquement à
https://pll-process.github.io/en-ligne-pour-le-cycle-4/

## Régénérer l'index après ajout de séances

```bash
cd _outils && python3 make_index.py   # adapter la variable DST au chemin local si besoin
```
