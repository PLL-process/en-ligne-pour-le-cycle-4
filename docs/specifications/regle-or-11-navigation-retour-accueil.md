# Règle d’or n°11 — Navigation persistante et retour à l’accueil

**Statut : proposée par Pascal pour adoption et fusion**

## Principe

Toute page HTML publiée dans le dépôt doit permettre de revenir à la page d’accueil en un seul clic, sans dépendre du bouton « Précédent » du navigateur.

Un bouton persistant **« 🏠 Accueil »** doit être présent sur :

- les pages de séquence ;
- les pages de QCM ;
- les synthèses élève et professeur ;
- les pages internes, ateliers, simulateurs et ressources HTML autonomes.

Le lien canonique vers l’accueil est :

```text
https://pll-process.github.io/en-ligne-pour-le-cycle-4/
```

Pour les pages publiées sous GitHub Pages, l’implémentation recommandée est :

```html
<a class="nav-home"
   href="/en-ligne-pour-le-cycle-4/"
   aria-label="Retour à la page d’accueil">
  🏠 Accueil
</a>
```

## Exigences d’ergonomie et d’accessibilité

Le bouton doit :

1. rester visible pendant le défilement de la page ;
2. être utilisable au clavier ;
3. présenter un contraste suffisant ;
4. ne pas masquer le contenu ni les commandes de la page ;
5. conserver une zone cliquable confortable sur ordinateur, tablette et téléphone ;
6. afficher un focus visible ;
7. rester lisible lorsque le zoom du navigateur est augmenté ;
8. ne pas ouvrir un nouvel onglet.

Exemple de style minimal :

```css
.nav-home {
  position: fixed;
  top: 0.75rem;
  left: 0.75rem;
  z-index: 1000;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  min-height: 44px;
  padding: 0.65rem 0.9rem;
  border: 2px solid currentColor;
  border-radius: 999px;
  background: #ffffff;
  color: #111827;
  font-weight: 700;
  text-decoration: none;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.22);
}

.nav-home:hover {
  text-decoration: underline;
}

.nav-home:focus-visible {
  outline: 3px solid #ffd54f;
  outline-offset: 3px;
}

@media (max-width: 520px) {
  .nav-home {
    top: 0.5rem;
    left: 0.5rem;
    padding: 0.6rem 0.75rem;
  }
}

@media print {
  .nav-home {
    display: none;
  }
}
```

## Navigation contextuelle complémentaire

En plus du bouton d’accueil :

- un QCM doit proposer un lien clair **« Retour à la séquence »** lorsqu’une séquence parente existe ;
- une synthèse doit proposer un lien clair **« Retour à la séquence »** ;
- les longues pages peuvent comporter un bouton **« Haut de page »** ;
- un fil d’Ariane est recommandé lorsque la profondeur de navigation le justifie.

Le bouton « Accueil » reste obligatoire, même lorsqu’un fil d’Ariane ou un bouton « Retour à la séquence » est présent.

## Intégration aux gabarits

Cette règle doit être intégrée :

- aux gabarits de séquence ;
- au gabarit QCM standard ;
- aux gabarits de synthèse ;
- aux générateurs et scripts produisant des pages HTML ;
- aux contrôles qualité des futurs lots.

Une page générée sans bouton « 🏠 Accueil » est considérée comme non conforme à la règle n°11.

## Contrôles avant publication

Pour chaque page concernée, vérifier réellement :

- que le lien aboutit à la page d’accueil ;
- que le bouton reste visible pendant le défilement ;
- qu’il fonctionne avec la touche Tab puis Entrée ;
- qu’il ne masque aucune question, consigne ou commande ;
- qu’il reste utilisable à 200 % de zoom ;
- qu’il est adapté aux petits écrans ;
- qu’il n’apparaît pas à l’impression.

## Déploiement sur l’existant

L’application aux pages déjà publiées doit être progressive et contrôlée :

1. tester d’abord sur une séquence, un QCM, une synthèse et une page interne ;
2. vérifier le rendu sur ordinateur et téléphone ;
3. corriger les conflits de style éventuels ;
4. généraliser ensuite par thème ou par lot ;
5. ne jamais modifier automatiquement un fichier sans vérifier que la structure HTML reste valide.

## Point de vigilance

La règle porte sur la navigation. Elle ne permet pas, à elle seule, d’affirmer une réduction chiffrée de la charge cognitive, ni de classer automatiquement une absence de bouton en anomalie P1 ou P2. Les niveaux de gravité doivent être définis dans une grille d’audit commune avant d’être employés.
