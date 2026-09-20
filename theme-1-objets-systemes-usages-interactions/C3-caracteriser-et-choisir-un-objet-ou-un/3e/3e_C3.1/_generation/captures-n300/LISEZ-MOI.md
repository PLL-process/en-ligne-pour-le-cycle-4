# Captures de la conversion n°300 — 3e_C3.1, 20/09/2026

La **plus longue proposition du dépôt** — 199 caractères, question `a4_3`, séance 4 —
à **390 × 844**, l'énoncé calé en haut de la zone utile.

| fichier | ce qu'il montre |
|---|---|
| `avant-liste-deployee-reconstitution.png` | l'état d'avant, liste **déployée** : l'énoncé est recouvert |
| `apres-groupe-radio.png` | après conversion : énoncé et propositions visibles ensemble |

**Sur la première image.** Le menu d'une liste déroulante native est dessiné par le
système **hors du DOM** : aucune capture de page ne le contient, et Playwright ne peut
pas l'ouvrir. Ce qui est dessiné est une **reconstitution à l'échelle**, calculée depuis
les propositions réelles de la question et depuis la place disponible sous le champ. Le
bandeau rouge la désigne comme telle sur l'image même.

Ces images ne sont pas des médias pédagogiques : aucune page ne les affiche, elles ne
vivent pas dans `Images/`, et n'ont donc pas d'entrée dans `SOURCES_MEDIAS.md`.
