# Mode mission — un exercice à la fois

Décision de Pascal du 11/11/2026, après le prototype « Mission lampadaire » : « On peut valider pour toutes les
séquences, c'est plus clair de voir un exercice à la fois. Apporte aussi des améliorations, tu as carte blanche. »

## Le principe retenu

Le mode mission est **une seconde vue de la même page**. Les exercices, les réponses attendues, la sauvegarde, les
verrous et la validation restent ceux de la séquence : le mode mission ne fait que montrer un écran à la fois, et
habiller certaines questions en étiquettes à placer. La page qui défile reste entière : c'est elle qui s'imprime,
qui se projette, et que mesurent les contrôles du dépôt.

- Source unique : `_outils/mode_mission/` (`mission.css`, `mission.js`), posée dans chaque page par `poser.py`,
  entre deux marqueurs — comme la fiche papier. Contrôle : `_outils/controle_mode_mission.py`.
- Aucune donnée propre à une page dans le bloc : les réponses attendues sont lues dans la page elle-même
  (tables `const att = {…}` de ses vérifications).

## Les écrans d'une séance

1. **La séance** : son titre, sa question directrice — et la situation de départ (`#ouverture`).
2. Pour chaque activité : **l'atelier incrusté** s'il y en a un ; **le départ** (objectif, ressources, consigne) ;
   **un écran par partie** (a, b, c… : ce qui suit chaque `h4` de `.exo`) ; **je retiens** (correction, erreurs
   fréquentes, à retenir, critère de réussite).
3. Chaque autre carte de la séance (synthèse, Bonus, bilan, QCM) : un écran.

## Les choix de jeu (carte blanche du 11/11)

- Étoiles par écran, comptées sur les **erreurs** (pas sur les appuis sur « Vérifier ») : 3 sans erreur ; 2 avec
  une erreur (deux sur un jeu de trois réponses ou plus) ; 1 au-delà. Ouvrir une aide ne retire rien.
- La barre affiche les étoiles **de la séance** (un but qu'on peut atteindre) ; le bilan, celles de la séquence et
  les erreurs corrigées en route.
- Les réponses justes restent ; les étiquettes fausses retournent dans la réserve.
- Après une erreur, « Vérifier » souffle deux secondes. Au deuxième essai manqué sur le même écran, le coup de
  pouce de l'activité s'ouvre sous le message ; au quatrième, le second.
- Ni chronomètre, ni vies, ni classement. « Suivant » n'est jamais bloqué.
- La dernière question d'une activité lance la vérification de la séquence : c'est elle qui valide l'activité.

## Ce que dit la recherche (rapport du 11/11/2026)

Ce qui est établi, et que le mode fait : découper en écrans (méta-analyse de Rey et al., 2019), garder le schéma
à côté de la question (Ginns, 2006 : d = 0,85), donner un retour qui explique plutôt que « juste / faux »
(Van der Kleij et al., 2015 : 0,49 contre 0,05), sans classement ni vies (Hanus et Fox, 2015).

**Le risque principal : le tâtonnement.** Étiquettes fausses rendues + essais illimités = on peut réussir par
élimination, sans comprendre. Les élèves qui « jouent le système » apprennent environ deux tiers de ce
qu'apprennent les autres, et ce sont d'abord les plus fragiles (Baker, Corbett, Koedinger, 2004).

| Mesure | État |
|---|---|
| Erreurs comptées réponse par réponse ; ce sont elles qui font les étoiles | fait (moteur) |
| Deux secondes avant de revérifier ; coup de pouce ouvert au 2e essai manqué | fait (moteur) |
| Retour jamais par la seule couleur (✓, « ✗ à revoir », texte) ; animations coupées si l'appareil le demande | fait (moteur) |
| Toucher puis toucher (sans glisser), clavier ; cibles de 44 px au moins (WCAG 2.2, 2.5.7 et 2.5.8) | fait (moteur) |
| Au doigt, la page défile quand le doigt part d'une case | fait (moteur) |
| **Étiquettes leurres** (une ou deux de trop, plausibles) : sans elles, la dernière étiquette est donnée | moteur et outil faits ; contenu écrit pour `5e_C4.1` (3 leurres), à écrire ailleurs |
| **Le pourquoi de l'erreur**, dit dès la première erreur (une phrase par mauvaise réponse) | moteur et outil faits ; contenu écrit pour `5e_C4.1` (97 pourquoi, 17 indices), à écrire ailleurs |
| Une justification écrite par activité : gardée (les écrits ont leur écran, jamais transformés en étiquettes) | fait, à surveiller |
| Rappel en début de séance : trois questions des séances d'avant (Adesope et al., 2017) | à concevoir |
| Maîtrise confirmée plus tard, pas le jour même (modèle Khan Academy) | à concevoir |
| Code bilan sans serveur, pour le suivi du professeur (modèle La Quizinière) | à concevoir |

À ne pas faire : classement, vies, chronomètre, solution montrée au premier échec, tout convertir en étiquettes,
police « spéciale dyslexie » (aucun gain mesuré), compter sur la nouveauté (l'effet des étoiles s'use en un
trimestre : Bai et al., 2020).

Limite de la recherche : aucune étude ne compare directement « un écran par exercice » et « page qui défile »
chez des collégiens lecteurs fragiles. Le seul juge sera la classe : nombre de vérifications par écran, et
réussite une semaine après.

**Sauvegarde sur iPad.** Safari efface ce qu'un site garde sur l'appareil après sept jours sans visite ; un site
ajouté à l'écran d'accueil y échappe. Cela vaut pour tout le dépôt, pas seulement pour le mode mission.

## Étapes

- [x] Prototype hors dépôt (artefact « Mission lampadaire »), validé.
- [x] **Pilote** : le lampadaire de 5e (`5e_C4.1`), #657. Vue éteinte par défaut ; le bouton « 🎮 Mode mission » est
      dans le cadre « Ma progression », la sortie (« 📄 Page complète ») dans la barre de la mission.
- [x] **Lot 1** : les séquences révisées du thème 2 au gabarit commun — `3e_C4.1`, `3e_C4.3`, `3e_C4.7`, `3e_C5.1`,
      `3e_C6.1`, `4e_C4.1`, `4e_C5.1`, `4e_C6.1`, `5e_C6.1`. Le moteur a appris trois écritures de réponses, les
      activités à plusieurs zones d'exercice, la vérification placée après les aides. Banc générique
      (`banc_generique.mjs`) : chaque page jouée écran par écran, chaque réponse croisée avec la vérification de la page.
- [x] Essai sur une vraie tablette, par Pascal (11/11/2026) : « Sur une tablette c'est bon. » Reste l'essai en classe.
- [ ] Décider de la vue par défaut. L'allumer d'office demande d'apprendre aux bancs et aux contrôles à ouvrir la
      page complète (`?vue=page`) : ils mesurent et jouent la page qui défile.
- [ ] Gabarit « atelier » (`3e_C4.8`, `3e_C6.2`) et `4e_C4.1_book-train` : à apprendre au moteur.
- [ ] Ancien gabarit (`div.act` posées dans une seule carte, sans `.exo` : `4e_C6.2` et la famille C7/C8 du thème 3) :
      le banc générique le refuse — un écran par séance, aucune question vérifiée. À apprendre au moteur.
- [ ] Autres habillages : cartes à remettre dans l'ordre (séries de numéros), texte à trous.
- [ ] Les séquences suivantes : à chaque révision (skill `revision-sequence`, étape 7), poser le mode et jouer le
      banc générique. Thèmes 1 et 3 : même geste.
- [x] Leurres et pourquoi des erreurs : le modèle, sur le lampadaire (`mission_5e_C4.1.json`, `enrichir.py`).
- [x] Avis de Pascal sur le modèle (11/11) : « Je te laisse carte blanche ». Faits : `5e_C6.1`, `4e_C6.1`.
- [ ] Les pourquoi des sept autres séquences qui portent le mode.
- [ ] **« Le mode mission doit être partout »** (Pascal, 11/11) : apprendre au moteur l'ancien gabarit et le gabarit
      « atelier », puis poser le mode sur toutes les séquences des trois thèmes que le banc générique accepte.
- [ ] Rappel en début de séance, maîtrise confirmée, code bilan.
