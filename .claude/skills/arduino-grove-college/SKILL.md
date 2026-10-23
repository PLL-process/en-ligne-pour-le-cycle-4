---
name: arduino-grove-college
description: Concevoir les activités Arduino/Grove du dépôt (UNO classique et UNO R4 Minima) avec les 20 éléments obligatoires, les 3 versions A/B/C et les règles de sécurité TBT. À utiliser pour toute séquence mettant en jeu une carte, un capteur ou un actionneur.
---

# Arduino & Grove au collège

Mis à jour le 23/10/2026 (inventaire des skills) : aligné sur le journal jusqu'à la règle d'or n°311.

Le journal (`JOURNAL_DES_DECISIONS.md`) fait foi (règle n°10) : les règles citées ici y sont en entier.

## Cartes (ne jamais confondre)

| Carte | Profil | Rôle |
|---|---|---|
| UNO classique | `arduino:avr:uno` | référence des versions A, Grove, Proteus |
| UNO R4 Minima | `arduino:renesas_uno:minima` (USB-C) | approfondissement ; mBlock et Proteus NON vérifiés → repli VittaScience → IDE → simulation HTML |

Aucun programme n'est livré pour une carte sans vérification de compatibilité
(bibliothèques comprises). Source : `ENVIRONNEMENT_TECHNIQUE.md`.

## Les 20 éléments d'une séquence Arduino/Grove

photo/SVG du matériel · rôle de chaque composant · tableau des broches · type
des signaux · logique vs analogique · niveaux logiques · chaîne d'information ·
chaîne d'énergie (si existante) · algorithme en langage naturel · algorigramme ·
programme par blocs · C++ commenté LIGNE PAR LIGNE en français
(variables françaises explicites, rôle des broches et bibliothèques, logique
`INPUT_PULLUP` inversée expliquée) · test progressif · moniteur série ·
correction · dépannage · QCM · grille d'évaluation · approfondissement ·
solution sans matériel.

- **Élément sans objet** (règle d'or n°215, 29/08/2026) : ne pas le forcer, ne pas le taire. L'écrire dans la fiche pédagogique, ligne par ligne, avec sa raison. Modèle : `5e_C7.4/fiche_pedagogique_5e_C7.4.md`, §9 (rien n'y est programmé).
- **Programme par blocs** = capture d'écran réelle de Vittascience, programme construit et exécuté (règle d'or n°308, 18/10/2026, avec la n°94, 21/08/2026). Jamais de blocs dessinés (CSS, SVG « reconstitution », blocs inventés). Ce qui ne peut pas être capturé devient un algorigramme, du pseudo-code ou un tableau. Nommage, poids, `alt` et déclaration : skill `licences-medias-education`.
- **Chaîne d'énergie** : la dessiner selon le skill `chaine-energie-fonctionnelle` (règle d'or n°310, 21/10/2026) — fonctions dans les blocs, composants dessous, énergies sur les flèches, l'ordre arrive sur DISTRIBUER.

Pour tout capteur analogique : grandeur physique, signal, plage, conversion,
étalonnage, seuil, incertitudes, limites.

## Versions A/B/C = trois parcours

Règle d'or n°122 (21/08/2026) : les versions 🅰 / 🅱 / 🅲 se choisissent en tête de page
et modifient l'affichage ; le choix est mémorisé et réversible. Pas trois paragraphes que
tout le monde lit. Chaque parcours s'imprime seul (n°102, 21/08/2026) : c'est le plan de
secours si le réseau tombe.

## Outil en ligne (Vittascience)

- Le nommer avec sa modalité exacte : « Vittascience, interface Arduino, mode blocs » (n°108, 21/08/2026).
- L'ouvrir par un lien-bouton, dans un nouvel onglet, jamais dans un `<iframe>` : le site refuse d'être encadré (mesuré le 13/09/2026). Gabarit : `_outils/gabarits/vittascience_embed.html`. Contrôle : `_outils/controle_cadres.py`.
- Gestes de l'outil réenseignés à chaque niveau, captures réelles, encart placé juste avant la première activité qui l'ouvre (n°93, 11/08/2026 ; n°297, 10/09/2026, complétée le 13/09). Contrôle : `_outils/controle_gestes_outil.py`.

## Code C++ ou blocs

⏳ À trancher par Pascal (question du 23/10/2026) : garder l'exigence « C++ commenté
ligne par ligne + compilation Arduino CLI », ou passer en priorité par les blocs de
Vittascience (interface Arduino) ? — en attendant : pratique constatée dans `3e_C9.2`.
L'élève programme dans Vittascience, interface Arduino, mode blocs, avec le simulateur,
puis lit le C++ généré. Le programme de référence
`station_alerte_cyclonique/station_alerte_cyclonique.ino` est commenté ligne à ligne ;
sa compilation pour `arduino:avr:uno` est vérifiée par `banc-docker/` (arduino-cli,
enseignant seulement).

## Brochages de départ (à revérifier à chaque montage)

D2 bouton/microrupteur · D3 DEL associée · D4 entrée bouton/magnétique ·
D5 DEL externe · I2C LCD RGB · A0-A2 luminosité/potentiomètre/humidité ·
sorties numériques relais/buzzer/DEL · PWM servomoteur.
Vérifier : carte, shield, module, câble, tension, bibliothèque, conflits.

## Sécurité (non négociable)

- Très basse tension uniquement ; jamais de secteur manipulé par un élève.
- Si la liste de matériel nomme le « secteur » : c'est un adaptateur USB fermé, jamais la prise ni le câble (lots C7.4, journal du 29/08/2026).
- Dans chaque version A : risques, EPI, gestes interdits, procédure d'arrêt.
- Alternative en simulation toujours présente.

## Critères de réussite

- Les 20 éléments présents, ou écrits « sans objet » avec leur raison dans la fiche (n°215).
- Trois parcours A/B/C sélectionnables en tête de page (n°122).
- Le programme compile pour la carte annoncée (Arduino CLI si disponible, sinon « compilation à vérifier » consigné dans le rapport) — voir la question ouverte ci-dessus.
- Un élève sans matériel peut réaliser la version C de bout en bout.
- `python3 _outils/controle_blocs_dessines.py` : « aucun dessin de blocs hors registre ». Ne jamais ajouter de dessin. Registre `EN_ATTENTE` au 23/10/2026 : 11 dessins dans 6 pages (3e_C9.2 : 8 ; 5e_C6.1 : 3) ; le lot qui les capture retire ses lignes dans le même commit.
- `python3 _outils/controle_cadres.py` : 0 cadre.
