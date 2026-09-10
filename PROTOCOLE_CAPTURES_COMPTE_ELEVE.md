# Reprendre les captures de gestes depuis un compte élève

Les quinze captures du lot pilote `4e_C1.1` sont à refaire depuis un compte Windows propre.
Ce fichier dit quoi créer, dans quel état mettre la session, et quelle image prendre à quel moment.

Il vaut pour tous les lots à venir : seule la liste des captures change.

---

## 1. Créer le compte — à faire par Pascal

Un agent ne crée pas de compte Windows et ne touche pas aux réglages de sécurité du poste.
Les deux commandes ci-dessous sont à lancer dans **PowerShell en administrateur**, sur le poste.

```powershell
New-LocalUser -Name Eleve -Description "Compte de captures pour les pages du cycle 4" -NoPassword
Add-LocalGroupMember -Group Utilisateurs -Member Eleve
```

`New-LocalUser` crée un compte **local** ; `Add-LocalGroupMember` sur le groupe `Utilisateurs`
(et non `Administrateurs`) en fait un compte **standard** — c'est ce qui garantit que la capture
ressemble au poste d'un élève et non à celui du professeur.

Si le groupe s'appelle `Users` sur ce poste, c'est celui-là qu'il faut nommer.
Pour supprimer le compte quand les captures de tous les lots seront prises :

```powershell
Remove-LocalUser -Name Eleve
```

Le dossier `C:\Users\Eleve` survit à la commande ; il se retire depuis Paramètres › Comptes, ou à
la main une fois que personne n'est connecté dessus.

## 2. Ouvrir la session et la mettre en thème clair

Se déconnecter, se connecter comme `Eleve`, puis, **dans cette session** :

Paramètres › Personnalisation › Couleurs › **Choisir votre mode** : `Clair`.

C'est un réglage par utilisateur : il n'affecte pas la session de Pascal. Il vaut aussi bien pour
les boîtes de dialogue Windows que pour l'Explorateur de fichiers, et c'est la seule chose à régler.

## 3. Ne pas toucher au profil LibreOffice

Le lot pilote avait dû forcer deux réglages dans `registrymodifications.xcu` — l'apparence claire et
les boîtes de dialogue LibreOffice à la place de celles de Windows. **Les deux sont à oublier.**

Elles ne servaient qu'à compenser le compte de travail : thème sombre, et un `Documents` plein de
dossiers privés que les boîtes Windows affichaient. Un compte `Eleve` en thème clair, au `Documents`
vide, n'a pas ce problème — et les **boîtes Windows par défaut** sont justement celles que l'élève
verra sur le poste du collège. C'est la réponse à la question laissée ouverte dans la PR #369.

Donc : profil LibreOffice **par défaut**, aucune sauvegarde à faire, aucune restauration à prévoir.

## 4. Préparer les dossiers

Dans la session `Eleve`, `Documents` doit contenir **le seul dossier du lot** au moment des captures
qui montrent son contenu :

```powershell
New-Item -ItemType Directory "$env:USERPROFILE\Documents\4E3"
```

Rien d'autre dans `Documents`. Aucun dossier de classe supplémentaire, aucun dossier d'application.
Si Windows ou LibreOffice en crée un tout seul (`Modèles Office personnalisés`, par exemple), le
déplacer ailleurs le temps des captures.

Copier le CSV du lot dans `Téléchargements` du compte `Eleve` — c'est de là que l'élève l'ouvrira.
Vérifier avant de commencer que ce CSV est bien **celui à virgule décimale** : la colonne `valeur`
doit lire `0,142`, `0,00293`, `0,167` et `4,97`. C'est la version corrigée le 10/09/2026.

## 5. Les quinze captures

L'outil est `_outils\captures-gestes\capwin.ps1` : il capture **une fenêtre seule**, jamais l'écran.

```powershell
powershell -File _outils\captures-gestes\capwin.ps1 -Out brutes\geste_tableur_1_ouvrir_import_csv.png
```

Sans `-Title`, il prend la fenêtre au premier plan. Puis, une fois les quinze brutes prises :

```powershell
python _outils\captures-gestes\reduire.py brutes finales
```

qui ramène à 1400 px de large et 256 couleurs — les images du pilote pesaient 43 à 165 Ko.

### Geste « Ouvrir » — LibreOffice Calc, Fichier → Ouvrir…, le CSV de Téléchargements

| fichier | ce que la fenêtre doit montrer |
| --- | --- |
| `geste_tableur_1_ouvrir_import_csv.png` | la boîte **Import de texte**, locale « Par défaut - Français (France) », **Point-virgule** seul coché, et l'aperçu où la colonne `valeur` lit **`0,142`** et non `0.142` |
| `geste_tableur_1b_ouvrir_resultat.png` | la feuille, huit colonnes A à H, dix lignes, une donnée par cellule |
| `geste_tableur_1c_ouvrir_erreur_separateur.png` | le contre-exemple : **Virgule** cochée à la place, tout le contenu tassé dans la colonne A |

### Geste « Nommer » — Fichier → Enregistrer sous…, en .ods, dans Documents puis dans la classe

| fichier | ce que la fenêtre doit montrer |
| --- | --- |
| `geste_tableur_2_nommer_documents.png` | la boîte **Enregistrer sous** ouverte sur `Documents`, **et rien d'autre dedans que `4E3`** |
| `geste_tableur_2b_nommer_bouton_nouveau_dossier.png` | le bouton **Nouveau dossier** désigné (surligné : l'infobulle ne s'affiche pas sous un survol simulé) |
| `geste_tableur_2c_nommer_nom_du_dossier.png` | la petite fenêtre de création de dossier, `4E3` tapé dans le champ |
| `geste_tableur_2d_nommer_dossier_cree.png` | `4E3` apparu dans la liste |
| `geste_tableur_2e_nommer_enregistrer_sous.png` | dans `4E3` : nom de fichier `4E-FEUX-DUPONT`, type **Classeur ODF (.ods)** |
| `geste_tableur_2f_nommer_resultat.png` | la barre de titre en `.ods` |
| `geste_tableur_2g_nommer_explorateur.png` | l'Explorateur, **en clair**, sur `Documents › 4E3`, un seul fichier |

Pour ces sept-là, le chemin affiché doit lire `C:\Users\Eleve\Documents\…`.
Masquer le volet de navigation de l'Explorateur (Afficher → Afficher → Volet de navigation) : il
liste OneDrive et les dossiers du compte, qui n'ont rien à faire dans l'image.

### Geste « Retrouver » — Ctrl+S, puis rouvrir

| fichier | ce que la fenêtre doit montrer |
| --- | --- |
| `geste_tableur_3_retrouver_avant_ctrl_s.png` | une modification non enregistrée, l'indicateur de la barre d'état |
| `geste_tableur_3b_retrouver_apres_ctrl_s.png` | le même écran après Ctrl+S, l'indicateur retombé |
| `geste_tableur_3c_retrouver_rouvrir.png` | la boîte **Ouvrir** dans `4E3`, le `.ods` sélectionné |

### Geste « Sortir » — faire le graphique, puis l'exporter en image

| fichier | ce que la fenêtre doit montrer |
| --- | --- |
| `geste_tableur_4_sortir_clic_droit_graphique.png` | le graphique **avec ses quatre barres**, menu contextuel ouvert sur « Exporter comme image » |
| `geste_tableur_4b_sortir_enregistrer_image.png` | la boîte **Enregistrer en tant qu'image**, dans `4E3`, type PNG |

Le graphique se fait sur la plage `D7:E10` — les quatre facteurs. Avec le CSV à virgule, les quatre
barres sortent ; celle du repas avec bœuf écrase les trois autres, et c'est la lecture attendue.
**Si une seule barre manque, le CSV importé n'est pas le bon** : reprendre au point 4.

Pour sélectionner le graphique à coup sûr : F5 (Navigateur) → Objets OLE → double-clic ; puis clic
hors du graphique, clic dessus, Shift+F10 pour le menu contextuel.

## 6. Ce qu'aucune capture ne doit montrer

- le nom de compte `PhaseLockedLoop`, nulle part, dans aucun chemin ;
- un dossier de `Documents` qui ne soit pas `4E3` ;
- un dossier ou un lecteur privé — `F:`, `.claude`, `CHESS`, des bulletins, des achats ;
- du thème sombre ;
- une barre des tâches, un bureau, un second écran : `capwin.ps1` ne prend que la fenêtre.

Relire les quinze images **une par une** avant de les verser au dépôt. C'est ce contrôle qui a
manqué au pilote : la légende de `geste_tableur_2_nommer_documents.png` décrivait une liste de
dossiers de classes, quand l'image montrait une trentaine de dossiers personnels.

## 7. Après les captures

Dans la page `sequence_4e_C1.1-C1.3_tsinghua_feux.html`, retirer les excuses devenues inutiles.
Quatre légendes et trois `alt` portent encore une phrase du genre « *PhaseLockedLoop est le nom du
compte du poste où la capture a été prise* », et une autre « *les dossiers visibles sont ceux du
poste où la capture a été prise ; les tiens seront différents* ». Avec un compte `Eleve` et un
`Documents` qui ne contient que la classe, elles n'ont plus d'objet — et chaque phrase en moins est
une phrase que l'élève n'a pas à démêler.

Reste vrai, et reste écrit : `4E3` et `DUPONT` sont des exemples, l'élève met sa classe et son nom.

Puis les contrôles habituels du lot : `controle_gestes_outil.py`, `controle_medias.py`,
`controle_liens.py`, `verif_regles_audit.py`, les tests de la séquence, `controle_impression.mjs`,
et la relecture au navigateur à 1280 px puis 390 px.
