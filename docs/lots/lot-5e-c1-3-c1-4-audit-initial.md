# LOT pilote — 5e_C1.3–C1.4

## Ressources concernées

- Séquence : `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.3/sequence_C1.3-C1.4_SI_gestion_donnees.html`
- QCM : `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.3/qcm_systemes_information_donnees.html`

## Décision de production

La séquence et le QCM constituent un seul paquet pédagogique. Ils seront modifiés, testés, prévisualisés et validés dans une même Pull Request.

## État actuel constaté

### Séquence

- la séquence annonce les compétences 5e_C1.3 et 5e_C1.4 ;
- elle présente le système d’information, les ressources matérielles et logicielles, un programme Python de gestion de prêts, les capacités de stockage et des activités de classement ;
- le programme Python est actuellement affiché dans un bloc statique `<pre><code>` ;
- le test du programme repose principalement sur des compilateurs externes ;
- l’éditeur commun `CodeLab Techno` doit remplacer ce bloc statique sans supprimer le code existant ;
- les réponses et le travail de l’élève doivent être sauvegardés localement ;
- l’affichage tablette et téléphone doit être contrôlé ;
- la structure HTML et les styles doivent être nettoyés sans altérer le contenu pédagogique validé.

### QCM

- le QCM comporte 24 questions ;
- les questions ciblent 5e_C1.3 et 5e_C1.4 ;
- l’en-tête demande actuellement une classe avec l’exemple `4eB`, incohérent avec le niveau 5e ;
- le QCM possède un score global, une note sur 20, un bouton de correction générale et des aides ;
- il ne possède pas encore le tableau de progression détaillé, la sauvegarde/reprise, la navigation par numéros ni le bilan par sous-thème ;
- les aides actuelles sont utiles mais ne constituent pas encore des corrections exhaustives au standard retenu ;
- le QCM doit recevoir un lien direct de retour vers la séquence.

## Première matrice de couverture

| Notion | Présente dans la séquence | Présente dans le QCM | Action |
|---|---:|---:|---|
| Définition et fonctions d’un système d’information | Oui | Oui | Harmoniser le vocabulaire et les exemples |
| Informations / ressources matérielles / ressources logicielles | Oui | Partiel | Ajouter des questions de classement réellement liées à l’activité |
| ENT et partage de l’information | Oui | Oui | Conserver et enrichir les corrections |
| Droits d’accès / lecture seule | Oui ou mobilisé dans la séquence | Oui | Ajouter un exemple concret commun |
| Arborescence, dossiers et sous-dossiers | Oui | Oui | Créer un exercice et une question utilisant la même arborescence |
| Nommage de fichiers | À consolider | Oui | Ajouter une activité courte dans la séquence |
| Extensions de fichiers | Oui | Oui | Vérifier les exemples et ajouter `.csv` et `.py` |
| Octet et multiples ko/Mo/Go/To | Oui | Oui | Vérifier les conversions et limiter la surcharge |
| Relation bit / octet | À expliciter | Oui | Ajouter un rappel clair : 1 octet = 8 bits |
| Stockage local / distant / cloud | Oui ou annoncé | Oui | Structurer une comparaison avantages-limites |
| Serveur | Oui | Oui | Employer la même définition dans les deux fichiers |
| Sauvegarde et recherche de fichiers | À consolider | Oui | Ajouter une tâche pratique dans la séquence |
| Programme Python : dictionnaire, variable, fonction, condition, affichage | Oui | Non ou très insuffisant | Ajouter un sous-ensemble de questions directement lié au programme |
| Sécurité des mots de passe | Oui | Non dans le corpus actuel | Ajouter quelques questions ou déclarer cette partie hors périmètre C1.3–C1.4 |
| CSV et tableur | À relier explicitement | Oui | Ajouter une transition claire vers 5e_C1.1 |

## Corrections prioritaires

1. Corriger l’exemple de classe `4eB` en `5e…` dans le QCM.
2. Ajouter des liens réciproques séquence ↔ QCM.
3. Ajouter une version et une date communes.
4. Installer l’éditeur `CodeLab Techno` dans la séquence.
5. Réorganiser la séquence en parcours plus lisible : déclencheur, problématique, activités, synthèse, entraînement.
6. Ajouter les fonctions de progression et de reprise au QCM.
7. Transformer chaque aide du QCM en correction exhaustive : bonne réponse, raisonnement, exemple, erreur fréquente, distracteurs, `À retenir`.
8. Ajouter au QCM des questions sur le programme Python réellement étudié.
9. Produire automatiquement une matrice finale `notion → activité → question(s)`.
10. Bloquer la publication tant que les deux fichiers ne réussissent pas les tests.

## Tests prévus

- validité HTML ;
- absence d’erreur JavaScript ;
- fonctionnement sur tablette et téléphone ;
- sauvegarde et reprise locale ;
- exactitude des conversions ;
- score non cumulable ;
- correction exhaustive pour chaque question ;
- liens réciproques ;
- cohérence des compétences ;
- couverture réelle entre la séquence et le QCM ;
- aucune donnée personnelle envoyée vers un service externe.
