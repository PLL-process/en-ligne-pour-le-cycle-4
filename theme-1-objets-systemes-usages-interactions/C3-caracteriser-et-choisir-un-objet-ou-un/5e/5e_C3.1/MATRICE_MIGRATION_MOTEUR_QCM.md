# Matrice de migration — QCM Shanghai vers le moteur JavaScript commun

## Objet

Ce document fixe le contrat de migration du fichier `qcm_5e_C3.1-C3.4_shanghai.html` vers le moteur JavaScript commun de référence du Thème 2, sans modifier les contenus du Thème 2 ni créer de moteur concurrent.

## État réellement observé le 27 juillet 2026

Le fichier QCM de la branche `codex/theme-1/shanghai-c3-fiche-pedagogique-v1` a été relu directement via le connecteur GitHub.

| Contrôle exécuté | Résultat observé |
|---|---|
| Banque pédagogique présente | 30 questions couvrant `C3.1` à `C3.4` |
| Corrections détaillées | une explication associée à chaque question |
| Champs d’identité | nom et classe présents |
| Modes de travail | entraînement et examen présents |
| Progression | sept compteurs présents |
| Sauvegarde et reprise | logique `localStorage` intégrée |
| Navigation | séquentielle et directe intégrées |
| Bilan par compétence | présent |
| Moteur externe mutualisé | absent |
| Moteur autonome interne | présent dans un bloc `<script>` |
| Séparation données / moteur | absente |

## Cible obligatoire

La migration doit conserver la banque de 30 questions et les textes pédagogiques du lot, mais remplacer la logique d’exécution autonome par le moteur commun déjà utilisé dans le Thème 2.

Le fichier final doit respecter les points suivants :

1. charger explicitement le moteur commun de référence ;
2. ne contenir aucune copie concurrente des fonctions génériques de sauvegarde, affichage, progression, validation, navigation ou bilan ;
3. isoler la configuration propre au lot Shanghai : identifiant, titre, niveau, compétences, banque de questions et options d’affichage ;
4. conserver les 30 corrections détaillées ;
5. conserver les deux modes de travail ;
6. conserver les sept compteurs ;
7. conserver la sauvegarde, la reprise et le recommencement ;
8. conserver le minuteur, le marquage à revoir et la navigation clavier ;
9. conserver le bilan par compétence `C3.1` à `C3.4` ;
10. conserver l’impression et le responsive ;
11. ne modifier aucun fichier du Thème 2 ;
12. ne créer aucun second moteur partagé dans le Thème 1.

## Fonctions internes à retirer après branchement effectif du moteur commun

Les fonctions suivantes ont été observées dans le moteur autonome actuel et ne devront plus être redéfinies localement après migration :

- `sauvegarder` ;
- `afficher` ;
- `actualiser` ;
- `valider` ;
- `bilan`.

Toute autre fonction générique de navigation, minuterie, reprise, impression ou gestion d’état présente dans le bloc interne devra suivre la même règle.

## Éléments propres au lot à conserver

- titre : choix d’une solution de livraison à Shanghai ;
- niveau : 5e ;
- compétences : `C3.1`, `C3.2`, `C3.3`, `C3.4` ;
- 30 questions ;
- distribution des bonnes réponses : A/B/C/D = `8/8/7/7` ;
- lien de retour vers `sequence_5e_C3.1-C3.4_shanghai.html` ;
- vocabulaire Shanghai–Martinique et mention explicite des données simulées ;
- explications de correction existantes.

## Tests à exécuter après migration

| Test réel attendu | Critère de réussite |
|---|---|
| Chargement de la page | aucune erreur JavaScript dans la console |
| Chargement du moteur commun | ressource trouvée, aucune erreur 404 |
| Comptage des questions | 30 questions accessibles |
| Identité | nom et classe conservés après sauvegarde/reprise |
| Modes | entraînement et examen produisent les comportements attendus |
| Sept compteurs | tous se mettent à jour correctement |
| Minuteur | progression visible et cohérente |
| Navigation clavier | accès aux réponses et boutons sans souris |
| Navigation directe | accès aux 30 questions |
| Marquage à revoir | état conservé après navigation et reprise |
| Corrections | affichées seulement selon le mode choisi |
| Bilan | résultats regroupés par `C3.1` à `C3.4` |
| Impression | bilan lisible en A4 |
| Responsive | contrôlé à 320 px, 768 px et 1440 px |
| Persistance | sauvegarde, fermeture, réouverture et reprise réussies |
| Architecture | aucune fonction générique du moteur redéfinie localement |

## Critère de sortie

La migration ne pourra être déclarée terminée que lorsque :

- le chemin exact du moteur commun aura été vérifié sur `main` ;
- le QCM chargera ce moteur ;
- le moteur autonome intégré aura été supprimé ;
- les tests fonctionnels ci-dessus auront réellement été exécutés et consignés dans `RAPPORT_TESTS_REELS.md` ;
- la garde de périmètre restera verte ;
- la PR restera limitée au Thème 1 et aux seuls fichiers communs explicitement autorisés.
