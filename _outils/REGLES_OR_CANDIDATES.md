# Règles d'or candidates — issues de l'audit Book Train (à valider par Pascal)

Chaque règle, une fois validée, déclenche un AUDIT de tous les documents de tous les thèmes.

## RC-1 · Navigation
Toute séquence est navigable : plan de mission cliquable (ancres vers les séances),
bouton « retour en haut » flottant accessible en permanence, aucune section à plus d'un clic.

## RC-2 · Compétences affichées
Chaque activité affiche, sous son titre, le CODE et le LIBELLÉ INTÉGRAL de la compétence
visée (badge = repère rapide ; libellé complet = lisible sans souris, sur tablette et à l'impression).

## RC-3 · Consigne référencée
Toute consigne nomme explicitement son document de référence et le situe spatialement
(« le schéma d'ensemble ci-dessus », « Fig. 2 », « le récit de la mission »).
Un rappel dépliable de la situation déclenchante accompagne les activités qui s'y réfèrent.

## RC-4 · Lisibilité en diagonale
Sur une page web, on n'économise pas le papier : À retenir, Pièges, Corrections
se présentent en paragraphes ou puces distincts — une idée par ligne, lisible en diagonale.

## RC-5 · Nommage des fichiers élèves
Tout fichier rendu se nomme `sujet_classe_NOM_Prenom.extension`
(ex. `book-train_4B_PAYET_Chloe.odp`) — underscores, sans espaces ni accents.

## Décision didactique actée (audit du jour)
- Le « diagramme fonctionnel » = fonctions techniques ↔ solutions techniques (5C4.1, deux colonnes).
  La colonne « fonction d'usage » n'apparaît qu'en 3e (3C4.1, schéma-bloc).
- Déclinaison du Book Train par niveau (à créer) : 5e découverte du diagramme fonctionnel ·
  4e chaînes à compléter + flux (4C4.1/4C4.2/4C4.4) · 3e élaboration du schéma-bloc (3C4.1).
- Distinction des acteurs : magasinier (sous-sol) ≠ bibliothécaire du comptoir (3e étage).

## RC-6 · Notation homogène des compétences (+ proposition de migration à arbitrer)
La convention EN VIGUEUR du dépôt est `NIVEAUe_CX.Y` (`5e_C4.1`, `4e_C4.2`), documentée au README
(ambiguïté Nathan levée par le préfixe). Règle immédiate : AUCUN code nu (`C4.1` sans niveau),
aucune notation mixte — audit sur tous les thèmes.
**Proposition de migration** (à trancher au JOURNAL_DES_DECISIONS) : format compact `4C4.1`
(plus court, triable, grepable). Coût mesuré : ~91 HTML + ~126 MD + README + générateur xlsx
+ noms de dossiers. Migration 100 % scriptable via `_outils/audit_conformite.py` étendu.
