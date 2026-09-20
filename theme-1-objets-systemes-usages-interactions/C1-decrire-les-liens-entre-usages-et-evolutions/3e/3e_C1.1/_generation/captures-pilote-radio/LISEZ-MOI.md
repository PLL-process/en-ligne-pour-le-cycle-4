# Captures du pilote de conversion — 3e_C1.1, 20/09/2026

Trois images, la même question (`a1_1`, séance 1) à **390 × 844**, l'énoncé calé
en haut de la zone utile. Elles servent de pièce à la PR du pilote et **ne sont
pas des médias pédagogiques** : elles ne sont affichées par aucune page, ne
figurent pas dans `Images/`, et n'ont donc pas d'entrée dans `SOURCES_MEDIAS.md`.

| fichier | ce qu'il montre |
|---|---|
| `avant-1-liste-fermee.png` | l'état d'avant, liste déroulante fermée — l'énoncé est lisible |
| `avant-2-liste-deployee-reconstitution.png` | la même, liste **déployée** : l'énoncé est recouvert |
| `apres-groupe-radio.png` | après conversion : énoncé et quatre propositions visibles ensemble |

**Sur la deuxième image.** Le menu d'une liste déroulante native est dessiné par
le système **hors du DOM** : aucune capture de page ne le contient, et Playwright
ne peut pas l'ouvrir. Ce qui est dessiné est une **reconstitution à l'échelle**,
calculée depuis les propositions réelles de la question et depuis la place
disponible sous le champ — d'où le fait qu'elle remonte. Le bandeau rouge la
désigne comme telle sur l'image même, pour qu'elle ne puisse pas être prise pour
une photographie du défaut.
