---
name: arduino-grove-college
description: Concevoir les activités Arduino/Grove du dépôt (UNO classique et UNO R4 Minima) avec les 20 éléments obligatoires, les 3 versions A/B/C et les règles de sécurité TBT. À utiliser pour toute séquence mettant en jeu une carte, un capteur ou un actionneur.
---

# Arduino & Grove au collège

## Cartes (ne jamais confondre)

| Carte | Profil | Rôle |
|---|---|---|
| UNO classique | `arduino:avr:uno` | référence des versions A, Grove, Proteus |
| UNO R4 Minima | `arduino:renesas_uno:minima` (USB-C) | approfondissement ; mBlock et Proteus NON vérifiés → repli VittaScience → IDE → simulation HTML |

Aucun programme n'est livré pour une carte sans vérification de compatibilité
(bibliothèques comprises).

## Les 20 éléments obligatoires d'une séquence Arduino/Grove

photo/SVG du matériel · rôle de chaque composant · tableau des broches · type
des signaux · logique vs analogique · niveaux logiques · chaîne d'information ·
chaîne d'énergie (si existante) · algorithme en langage naturel · algorigramme ·
programme par blocs (si possible) · C++ commenté LIGNE PAR LIGNE en français
(variables françaises explicites, rôle des broches et bibliothèques, logique
`INPUT_PULLUP` inversée expliquée) · test progressif · moniteur série ·
correction · dépannage · QCM · grille d'évaluation · approfondissement ·
solution sans matériel.

Pour tout capteur analogique : grandeur physique, signal, plage, conversion,
étalonnage, seuil, incertitudes, limites.

## Brochages de départ (à revérifier à chaque montage)

D2 bouton/microrupteur · D3 DEL associée · D4 entrée bouton/magnétique ·
D5 DEL externe · I2C LCD RGB · A0-A2 luminosité/potentiomètre/humidité ·
sorties numériques relais/buzzer/DEL · PWM servomoteur.
Vérifier : carte, shield, module, câble, tension, bibliothèque, conflits.

## Sécurité (non négociable)

TBT uniquement, jamais de secteur manipulé par un élève, risques + EPI + gestes
interdits + procédure d'arrêt dans chaque version A, alternative simulation
toujours présente.

## Critères de réussite

- Les 20 éléments présents ; versions A/B/C étiquetées.
- Le programme compile pour la carte annoncée (Arduino CLI si disponible,
  sinon « compilation à vérifier » consigné dans le rapport).
- Un élève sans matériel peut réaliser la version C de bout en bout.
