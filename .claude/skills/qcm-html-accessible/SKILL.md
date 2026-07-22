---
name: qcm-html-accessible
description: Créer ou compléter un QCM HTML autonome pour le dépôt cycle 4 (entraînement public ou sommatif privé). À utiliser pour tout nouveau QCM, en réutilisant la chaîne _outils/qcm_generator.py + banks_*.py quand c'est possible.
---

# QCM HTML accessible

## Deux usages, deux régimes

- **Entraînement (public, GitHub Pages)** : correction immédiate + explication
  pédagogique par réponse + nouvelle tentative + conseils de révision.
- **Sommatif (privé)** : version élève SANS correction ; correction professeur
  dans un fichier séparé marqué `PRIVÉ — NE PAS PUBLIER` dans le manifeste du
  lot. Une page statique publique n'est JAMAIS une protection (réponses
  lisibles dans la source) ; un mot de passe JavaScript non plus.

## Spécification par défaut

Banque 20-30 questions, 15 tirées aléatoirement, 4 propositions (multi-réponses
seulement si annoncé), mélange connaissance/application/analyse, questions sur
schéma ou données, distracteurs plausibles, zéro double négation.

Interface : champs Nom/Prénom/Classe/Groupe/Date, progression visible,
navigation clavier complète (focus visible, fonctionnement sans souris),
gros boutons, sauvegarde locale + reprise, score final + /20 + temps passé +
bilan par compétence, impression A4 propre, exports PDF et JSON/CSV, remise à
zéro, responsive téléphone/tablette/PC, messages jamais fondés sur la seule
couleur, aria-live pour les retours.

Technique : HTML5 valide, UTF-8, `lang="fr"`, aucun tracker/cookie/envoi
distant, pondération dans des constantes nommées (`const POIDS_QCM = 0.30` …),
commentaires français par fonction, zéro erreur console.

## Procédure

1. Vérifier si le sujet a déjà une banque dans `_outils/banks_*.py` (étendre
   plutôt que dupliquer) ; sinon créer la banque puis générer.
2. Tester : chaque bonne/mauvaise réponse, non-répondu, calcul /20, pondération,
   reprise après fermeture, remise à zéro, exports, champs vides, valeurs limites.
3. Consigner le test dans le rapport de lot.

## Critères de réussite

- Le QCM fonctionne en `file://` (hors connexion) et sur GitHub Pages.
- Un tirage différent à chaque lancement, score exact vérifié sur 3 scénarios
  scriptés (tout juste, tout faux, mixte connu).
- Aucune réponse d'évaluation sommative dans un fichier destiné au site public.

## En-tête standard obligatoire des QCM — RÈGLE (décision Pascal, 22/07/2026 — à entériner au Conseil du 28/07)

Tout QCM du dépôt (les trois thèmes) reprend l'en-tête du modèle
`3e_C4.3/qcm_3e_C4.3-C4.6_station_alerte_cyclonique.html`, dans cet ordre :

1. **Titre** H1 avec émoji discret + **sous-titre** (notions couvertes en clair) ;
2. **Badges** : niveau, chaque code couvert, « N questions · corrections
   détaillées » (+ mention des questions illustrées le cas échéant) ;
3. **Lien de retour vers la séquence** associée (obligatoire, en haut) ;
4. **Identité élève** : Nom, Prénom, Classe, Date (sauvegardée localement) ;
5. **Carte « Ma progression »** : barre de progression + 7 compteurs permanents
   (Répondu, Correctes, Incorrectes, Restantes, À revoir 🔖, Score %, Note /20)
   + **minuteur** (Démarrer/Pause/Reprendre + case « travailler sans minuteur ») ;
6. **Carte « Mode de travail »** : Parcours complet (N), 10 questions,
   Révision ciblée (par compétence), Uniquement mes erreurs, Marquées « à revoir ».

Suivent : carte Navigation (filtres + grille), écran question, écran résultat.
Palette et classes CSS de la charte commune (fond `#050f24`, cartes `#0d2347`,
accents `#61dafb`/`#c68ef2`/`#ffd66b`). Jamais d'appellation « XXL ».
Le moteur JS de référence (sauvegarde/reprise, modes, corrections exhaustives,
bilan par compétence, champ `img` optionnel par question) est celui des QCM du
Thème 2 : le RÉUTILISER plutôt que réécrire.
