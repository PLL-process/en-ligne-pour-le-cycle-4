# Rapport de tests — Vague 1 · Conformité règles 11/13/14/15/16/17/18 (Thème 3, 01/08/2026)

Suite Playwright dédiée (Chromium, mobile 390×844), exécutée réellement sur les cinq pages livrées.
Périmètre : 3e_C7.1, 4e_C7.1, 5e_C7.1, 4e_C8.1 (refontes v2, v1 archivées règle n°12) + 4e_C9.1 (compléments règle 18).

```
— 3e_C7 capteur confort —
  ✅ nav règle 11 (⌂ + QCM)
  ✅ contrat règle 18 présent
  ✅ verrou simulateur actif (🔒 avant manipulation)
  ✅ LED réagit au seuil
  ✅ 🎉 après manipulation + bonnes réponses
  ✅ encoche ✘ sur l'erreur volontaire (seuil exact)
  ✅ message gradué 🟡
  ✅ algorigramme 5/5 → 🎉
  ✅ verrou éditeur vs1 (🔒 avant ouverture)
  ✅ 3b validée après ouverture éditeur
  ✅ restauration localStorage (hyp)
  ✅ restauration verrou __exp
  ✅ coloration règle 13 appliquée
  ✅ zéro alert() résiduel
  ✅ zéro erreur JS
— 4e_C7 jardin conception —
  ✅ nav règle 11
  ✅ contrat règle 18
  ✅ verrou banc météo (🔒 avant 3 essais)
  ✅ banc affiche un résultat
  ✅ 🎉 après 3 essais au banc
  ✅ diagramme démarche 5/5 → 🎉
  ✅ matériaux 8/9 → 🟡 + encoche ✘
  ✅ Bonus sauvegardé (règle 15)
  ✅ zéro alert() résiduel
  ✅ zéro erreur JS
— 5e_C7 mini-projet —
  ✅ nav règle 11
  ✅ contrat règle 18
  ✅ verrou simulateur (🔒 avant 2 allers-retours)
  ✅ LED verte après retour
  ✅ 🎉 après manipulation
  ✅ algorigramme 5/5 → 🎉
  ✅ verrou éditeur vs1
  ✅ 3b validée après éditeur
  ✅ coloration règle 13
  ✅ zéro alert()
  ✅ zéro erreur JS
— 4e_C8 jardin validation —
  ✅ nav règle 11
  ✅ contrat règle 18
  ✅ SVG image-objet conservé (règle 1)
  ✅ verrou banc de tests (🔒)
  ✅ banc révèle la fissure au gel
  ✅ 🎉 après 3 tests
  ✅ diagramme protocole 5/5 → 🎉
  ✅ analyse 6/6 → 🎉
  ✅ Bonus sauvegardé (règle 15)
  ✅ zéro alert()
  ✅ zéro erreur JS
— 4e_C9 compléments règle 18 —
  ✅ contrat règle 18 ajouté
  ✅ algorigramme 4e_C9 5/5 → 🎉
  ✅ encoche ✘ sur erreur algorigramme
  ✅ phrase invariant (18d) en synthèse
  ✅ régression : vérificateur act.2 intact
  ✅ zéro erreur JS
— intégrité des liens QCM —
  ✅ QCM présent : qcm_3e_C7_capteur-confort-ny.html
  ✅ QCM présent : qcm_4e_C7_jardin-conception.html
  ✅ QCM présent : qcm_5e_C7_mini-projet.html
  ✅ QCM présent : qcm_4e_C8_jardin-validation.html

RÉSULTAT : 57/57 tests réussis ✅
```
