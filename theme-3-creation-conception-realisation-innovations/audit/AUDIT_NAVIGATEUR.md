# Audit au navigateur — ce que la lecture du code ne montre pas

*Chaque page ouverte dans Chromium : erreurs JavaScript au chargement et images qui ne se
chargent pas. La page est **défilée jusqu'en bas** avant la mesure, sinon les images à
chargement paresseux passeraient toutes pour cassées.*

**181 pages ouvertes · aucune ne présente de défaut.**

Trois fichiers sont exclus, et pour une raison : ce sont des **gabarits**, pas des pages.
`dnb_gabarit.html` contient des emplacements du type `@@CHECKS@@` que le générateur
remplit ; les juger comme des pages produit de faux défauts, et un audit qui crie au loup
finit par ne plus être lu.

---

## Périmètre

**Vérifié** : la page s'ouvre, son JavaScript s'exécute sans erreur au chargement,
toutes ses images se chargent réellement.

**NON couvert** : ce qui ne casse qu'après une interaction précise, la justesse des
réponses, et le fait que la page enseigne quelque chose. Un script sans erreur peut
être un script qui ne fait rien.
