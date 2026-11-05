# Rapport de tests — lot 5e_C1.3–C1.4

Date : 25 juillet 2026

Branche : `codex/theme-1/conformite-5e-c1-3-c1-4`

## Ressources testées

- `sequence_C1.3-C1.4_SI_gestion_donnees.html`
- `qcm_systemes_information_donnees.html`
- `donnees_velos_hangzhou_simulees.csv`
- trois SVG originaux
- synthèses élève et professeur

## Séquence — 23 contrôles sur 23 réussis

- aucune dépendance CSS, JS ou police externe ;
- titre, mission, situation déclenchante et problématique ;
- trois séances progressives ;
- deux blocs CRCN contenant compétence exacte, niveau, repère verbatim, action observable et trace ;
- principe « utiliser un ordinateur n’est pas une compétence » ;
- règle d’or n°4 : bilan, bloc QCM unique, bonus, pied de page ;
- un seul bouton vers le QCM ;
- liens locaux vers QCM, synthèses, CSV et images ;
- CSV : 8 lignes de données, 7 colonnes ;
- règle de priorité vérifiée : V-104, V-105, V-108 et V-112 ;
- sauvegarde locale des trois réponses textuelles ;
- aucun débordement à 320, 768 et 1440 px ;
- PDF A4 généré : 197 265 octets ;
- aucune erreur console.

## QCM — 35 contrôles sur 35 réussis

- 30 questions et 3 questions illustrées ;
- répartition des bonnes réponses : A 8, B 8, C 7, D 7 ;
- quatre champs d’identité ;
- sept compteurs ;
- cinq modes de travail ;
- grille de 30 questions ;
- minuteur : démarrage, pause et reprise ;
- mode 10 questions ;
- révision ciblée « traitement des données » : 9 questions ;
- mode questions marquées ;
- identité sauvegardée ;
- sélection et validation au clavier ;
- scénario tout juste : 30/30, 20,0/20 ;
- scénario tout faux : 0/30, 0,0/20 ;
- scénario mixte : 15/30, 10,0/20 ;
- réessai des 15 erreurs ;
- bilan sur cinq catégories ;
- corrections détaillées : explication, exemple, erreur fréquente, à retenir ;
- aucun débordement à 320, 768 et 1440 px ;
- PDF A4 généré : 202 680 octets ;
- aucune erreur console.

## Synthèses — 24 contrôles sur 24 réussis

- titre et liens de retour ;
- affichage à 320, 768 et 1440 px ;
- aucun débordement après correction du tableau CRCN de la synthèse élève ;
- aucune erreur console ;
- contenu aligné sur les trois séances, sans ancien développement Python hors parcours.

## Médias

- trois SVG locaux : environ 1,8 à 3,2 Ko ;
- textes alternatifs présents ;
- aucune image externe ;
- retrait des sept PNG lourds et non documentés.

## Contrôles non déclarés comme réussis

- ouverture du CSV dans Excel sur Windows ;
- ouverture du CSV dans LibreOffice Calc sur les postes du collège ;
- essai tactile sur appareil physique ;
- impression sur imprimante physique ;
- validation des liens après publication sur GitHub Pages.

## Conclusion

Le paquet est fonctionnel, accessible et conforme aux règles d’or n°4 et n°7. La règle n°6 n’est pas applicable : aucune consigne ne demande de tracer les chaînes d’information et d’énergie.

## Reprise du 4 novembre 2026 — la séquence passe à onglets (vague des séquences sans onglets)

La page était d'un seul tenant, déjà écrite en trois cartes « Séance 1 / 2 / 3 ». Elle a maintenant trois séances à onglets
(squelette n°306) et le volet « 📖 Rappel » dès la séance 2 (n°311) : séance 1 = ouverture + activité 1 (avec l'exercice
incrusté de la carte mentale) ; séance 2 = activité 2 ; séance 3 = activité 3, transfert, Bonus, bilan, QCM. Chaque séance a
sa question directrice, son programme et son bouton vers la suivante (n°101) ; l'onglet en cours est mémorisé. La carte
« 💾 Sauvegarde locale » reste un seul nœud, hors du volet, qui suit la séance ouverte et se place à sa fin. La barre
d'outils passe sous la mission et reçoit « 🖨 Imprimer / PDF ».

Écrit au passage, parce que `controle_squelette` le trouvait « à rédiger » : une hypothèse de départ (champ enregistré,
version étayée), le retour à l'hypothèse dans le bilan, « Comment j'ai travaillé » et « Je me positionne » sur 5e_C1.3 et
5e_C1.4 aux quatre niveaux du livret scolaire.

Le lot n'avait pas de banc au navigateur : `tests_5e_C1.3-C1.4_sequence.mjs` est écrit (séances, sauvegarde, exercice
incrusté). Le banc de la règle n°311 : `tests_regle_311_5e_C1.3.mjs`.

```bash
node tests_regle_311_5e_C1.3.mjs [--captures <dossier>]
node tests_5e_C1.3-C1.4_sequence.mjs
```

```
✅ les marques de l'exercice incrusté sont intactes (une ouverture, une fermeture, dans l'ordre)
✅ 1280 px : l'exercice incrusté (carte mentale) est dans l'activité 1, à la séance 1
✅ 1280 px : au chargement, la carte de sauvegarde (un seul nœud) est à la fin de la séance 1
✅ 1280 px : la mission est visible hors du volet, à la séance 1 et à la séance 2
✅ 1280 px : un outil n'est pas du décor — .toolbar, #sauvegarde, #status hors du volet, visibles aux séances 1 et 2
✅ 1280 px : à la séance 2, la carte de sauvegarde est à la fin de la séance 2
✅ 1280 px : à la séance 2, les onglets et la question directrice de la séance sont dans le premier écran
✅ 1280 px : à la séance 3, la carte de sauvegarde est à la fin, après le renvoi au QCM
✅ 1280 px : après rechargement (séance 2 mémorisée), la carte de sauvegarde est de nouveau à la fin de la séance 2 (séance s2, carte en s2)
✅ 1280 px : aucune erreur JS 
✅ 390 px : l'exercice incrusté (carte mentale) est dans l'activité 1, à la séance 1
✅ 390 px : au chargement, la carte de sauvegarde (un seul nœud) est à la fin de la séance 1
✅ 390 px : la mission est visible hors du volet, à la séance 1 et à la séance 2
✅ 390 px : un outil n'est pas du décor — .toolbar, #sauvegarde, #status hors du volet, visibles aux séances 1 et 2
✅ 390 px : à la séance 2, la carte de sauvegarde est à la fin de la séance 2
✅ 390 px : à la séance 3, la carte de sauvegarde est à la fin, après le renvoi au QCM
✅ 390 px : après rechargement (séance 2 mémorisée), la carte de sauvegarde est de nouveau à la fin de la séance 2 (séance s2, carte en s2)
✅ 390 px : aucune erreur JS 
✅ sans JavaScript : la page reste d'un seul tenant (les trois séances à la suite, ni onglets ni boutons de séance), la carte de sauvegarde en fin de page
✅ lien direct #act3 : page chargée, volet replié, la cible à l'écran
✅ 1280 px : séance 1 = ouverture complète (4/4 titres, barre d'outils), sans volet
✅ 1280 px : séance 2 (s2) = volet « Rappel » replié, ouverture masquée
✅ 1280 px : séance 2 = titre, mission, barre d'outils visible, badges masqués
✅ 1280 px : séance 2 sans défilement horizontal (0)
✅ 1280 px : séance dernière (s3) = volet « Rappel » replié, ouverture masquée
✅ 1280 px : séance dernière = titre, mission, barre d'outils visible, badges masqués
✅ 1280 px : séance dernière sans défilement horizontal (0)
✅ 1280 px : clavier — Entrée sur le volet l'ouvre (ouverture et badges de nouveau visibles)
✅ 1280 px : ce qui a été saisi dans l'ouverture est conservé et visible dans le volet
✅ 1280 px : clavier — Espace referme le volet
✅ 1280 px : retour à la séance 1 : ouverture complète
✅ 1280 px : après rechargement (séance s3), le volet suit la séance
✅ 1280 px : la sauvegarde survit au rechargement
✅ 1280 px : aucune erreur JS 
✅ 390 px : séance 1 = ouverture complète (4/4 titres, barre d'outils), sans volet
✅ 390 px : séance 2 (s2) = volet « Rappel » replié, ouverture masquée
✅ 390 px : séance 2 = titre, mission, barre d'outils visible, badges masqués
✅ 390 px : séance 2 sans défilement horizontal (0)
✅ 390 px : séance dernière (s3) = volet « Rappel » replié, ouverture masquée
✅ 390 px : séance dernière = titre, mission, barre d'outils visible, badges masqués
✅ 390 px : séance dernière sans défilement horizontal (0)
✅ 390 px : clavier — Entrée sur le volet l'ouvre (ouverture et badges de nouveau visibles)
✅ 390 px : ce qui a été saisi dans l'ouverture est conservé et visible dans le volet
✅ 390 px : clavier — Espace referme le volet
✅ 390 px : retour à la séance 1 : ouverture complète
✅ 390 px : après rechargement (séance s3), le volet suit la séance
✅ 390 px : la sauvegarde survit au rechargement
✅ 390 px : aucune erreur JS 
✅ lien direct #act3 : ouvre s3, ouverture repliée
✅ lien direct #act1 : séance 1, ouverture complète
✅ sans JavaScript : ouverture et badges affichés, sans volet
✅ impression depuis s3 (fiche papier) : la séance seule, sans l'ouverture ni le bouton du volet
✅ après l'impression : le volet est replié de nouveau
✅ impression depuis la séance 1 (fiche papier) : l'ouverture, et l'en-tête qui porte le titre

══ 5e_C1.3 : 34 / 34 tests réussis ══

✅ charge sans erreur JS
✅ aucune requête échouée
✅ trois séances à onglets — s1,s2,s3
✅ séance s1 : son onglet est actif et son panneau est le seul affiché
✅ séance s1 : la clôture (Bonus, bilan, positionnement, QCM) n'est pas là — false,false,false,false
✅ séance s2 : son onglet est actif et son panneau est le seul affiché
✅ séance s2 : la clôture (Bonus, bilan, positionnement, QCM) n'est pas là — false,false,false,false
✅ séance s3 : son onglet est actif et son panneau est le seul affiché
✅ séance s3 : la clôture (Bonus, bilan, positionnement, QCM) est là — true,true,true,true
✅ le bouton de fin de séance 1 ouvre la séance 2
✅ le bouton de fin de séance 2 ouvre la séance 3
✅ un seul bouton vers le QCM, à la séance 3
✅ les zones de réponse sont annoncées par la carte de sauvegarde — Les 12 / 12
✅ le retour à l'hypothèse relit l'hypothèse du début
✅ les 12 zones survivent au rechargement — 12 / 12
✅ le positionnement survit au rechargement
✅ l'onglet en cours survit au rechargement (séance 3)
✅ l'exercice incrusté est visible à la séance 1
✅ l'exercice incrusté, rempli juste, est validé — 🎉 Tout est juste. Ouvre quand même la c
✅ les réponses de l'exercice incrusté survivent au rechargement — 10 / 10
✅ « Effacer mes réponses locales » vide les zones et le positionnement
✅ après effacement et rechargement, rien ne revient
✅ aucune erreur JS sur tout le parcours

23 / 23
```

- `controle_squelette.mjs` : 0 défaut (D1 à D6), aucun « à rédiger », aucun signalement.
- `incrustations.py --verifier` : la page est « à jour » (les marques de l'exercice incrusté sont intactes).
- Le contrôle statique du lot dans `_outils` : les mêmes 6 erreurs qu'avant, toutes sur le QCM et un rapport ancien absent.
- Avant et après, mêmes verdicts (0 refus) : `controle_hors_ligne`, `controle_contraste_liens`, `controle_hierarchie`,
  `controle_unites`, `controle_sigles`, `controle_impression_papier`, `controle_regles_visibles`, `controle_liens`,
  `controle_verrous`, `controle_impression` ; `verif_regles_audit.py` : 0 ✘ avant et après.

- Fiche papier (`banc_papier.py`, PDF A4 de Chromium) : **3 fiches, une par séance, 9 pages en tout** ; aucun texte pâle,
  aucun champ d'écran imprimé, aucun grand fond foncé, aucune première page vide.

**Retouche du même jour.** « Effacer mes réponses locales » vidait le stockage mais pas la mémoire de la page : la première
frappe suivante réécrivait toutes les anciennes réponses. Corrigé (la mémoire est vidée avec le stockage). Le banc du lot
le vérifie — effacer, taper une lettre, recharger : seule la nouvelle valeur revient — et passe à **24 / 24** (il était
rouge sur ce test avant la correction). n°311 **54 / 54**, `controle_squelette` 0 défaut, aucun « à rédiger ».

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.
