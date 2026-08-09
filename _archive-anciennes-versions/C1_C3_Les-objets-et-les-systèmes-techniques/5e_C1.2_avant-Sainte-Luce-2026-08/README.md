# 5e_C1.2 — état antérieur au lot « Sainte-Luce » (archivé le 9 août 2026)

Douze fichiers occupaient le dossier `5e/5e_C1.2/` avant la refonte. Ils sont archivés, pas
supprimés.

## Pourquoi une refonte, et non une réparation

Pascal a signalé la séquence ; l'audit global du 8 août l'a confirmée en défaut ; la lecture
intégrale en a montré davantage.

- **Aucun champ de saisie** — ni `textarea`, ni `select`, ni `input`, ni `button` — alors que la
  page annonçait **trois fois** une « production attendue ». Les tableaux à remplir étaient des
  tableaux HTML statiques dont les cellules contenaient « … ».
- **La définition de la fonction technique était fausse** : « La fonction répond à : *à quoi cela
  sert-il ?* », et l'en-tête de tableau « Fonction : à quoi sert-il ? ». C'est la fonction d'usage.
  La même erreur figurait dans les deux synthèses.
- **Le QCM comptait 10 questions** et n'employait pas le moteur du dépôt.
- Ni hypothèse de départ, ni mode essentiel, ni tableau de bord, ni version étayée, ni
  auto-positionnement, ni sauvegarde locale.

## Ce qui a été repris (règle n°12)

- **La situation de Sainte-Luce** — les vélos de prêt, la descente, la pluie, les embruns. C'était
  le seul ancrage martiniquais du C1, et il est excellent : il est gardé entier.
- **Le cas du freinage** et son opposition fonction / principe / solution, dont l'intention était
  juste — c'est sa formulation qui était fausse.
- **Le jeu de données** `donnees_simulees_freinage_5e_C1.2.csv` : trois solutions, six critères
  chiffrés. **Plus riche que ce que la séquence en faisait** — elle n'en comparait que deux, et
  qualitativement (« Moyenne », « Bonne »). Le nouveau lot exploite les trois et les chiffres, et
  y ajoute quinze relevés d'essai dont la fiche est la moyenne exacte.
- **Le second exemple « éclairer une salle »** (LED contre filament), devenu le Bonus 2.
- **L'activité CRCN sur les données de freinage**, dont le principe est repris comme « chemin
  autonome » de la séance 2.

## Ce qui n'a pas pu l'être

- `sequence.mhtml` (180 ko) : une archive de navigateur qui se télécharge au lieu de s'afficher, et
  dont l'en-tête interne nomme un fichier `sequence_C1.2_4e_dark.html` — donc peut-être une séquence
  de **4e** rangée en 5e. Conservée ici sans être exploitée.
- La définition de la fonction technique, et les tableaux statiques.

## Remplacé par

`theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.2/sequence_5e_C1.2_sainte_luce_freinage.html`
et le lot complet — QCM de 30 questions, deux synthèses, deux jeux de données, deux corrigés
graphiques CC0, suite de 36 tests, et la première manipulation d'objet réel du dépôt placée au
parcours obligatoire.
