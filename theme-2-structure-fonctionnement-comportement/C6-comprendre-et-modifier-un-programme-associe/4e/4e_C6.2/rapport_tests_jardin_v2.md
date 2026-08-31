# Rapport de tests — Jardin connecté v2 (4e_C6.2, densification du 30/07/2026)

> **Ce document est un relevé historique, daté du 30/07/2026.** Il annonçait « 27/27 PASS »
> sans citer de script et sans coche : une dette honnête, mais non rejouable. La suite qui
> la paie est `tests_4e_C6.2.mjs`, livrée le 31/08/2026 dans ce dossier, et le rapport à
> jour est `rapport_tests_4e_C6.2_qcm.md` — il couvre la séquence ET le QCM, **réseau
> coupé**. Ce qui suit est conservé pour mémoire.

Suite Playwright réelle (Chromium, mobile 390×844) : **27/27 PASS**.

Couverture : titre charte, navigation ⌂, 3 barres 🧪, image des chaînes,
parcours complet des 8 activités (encoches ✔/✘, messages gradués), verrous
expérientiels (act. 3 et 5 : éditeur 🧪 exigé ; act. 6 : banc 3/3), pseudo-code
en direct (act. 4), simulateur de pompe, banc T1/T2/T3 avec frontière,
coloration règle n°13 des corrections, panneau professeur fermé par défaut,
sauvegarde/restauration localStorage, zéro erreur JS.

Non testé (hors périmètre local) : le contenu de l'iframe Vittascience
(cross-origin, connexion requise) — seul le suivi d'ouverture est vérifié.
