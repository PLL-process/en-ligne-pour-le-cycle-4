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

## 14/11/2026 — les questions fermées vérifiées par la page

- Banc du lot (`tests_5e_C1.3-C1.4_sequence.mjs`) : **44 / 44** (24 avant). Les 20 nouveaux tests :
  - les réponses attendues se lisent dans la page (9 / 9 / 6), chacune présente une seule fois parmi au moins trois propositions ;
  - activité 3 : les réponses **recalculées** depuis `donnees_velos_hangzhou_simulees.csv` — 4 prioritaires (V-104, V-105,
    V-108, V-112), V-104 premier après le tri, V-108 à 3 incidents prioritaire, V-105 à 31 % prioritaire, un vélo à 35 %
    et 1 incident non prioritaire ;
  - pour chaque activité : deux aides, une correction et un message, repliés au départ ; rien coché → « Il reste N
    questions » ; une erreur → « à revoir » sur cette question seule, tâche non cochée ; tout juste → « activité validée »
    et tâche cochée ;
  - rechargement : les 24 réponses et les trois tâches cochées reviennent ; changer une réponse retire sa marque ;
  - « Effacer mes réponses locales » vide aussi les questions fermées et décoche les tâches.
- Banc n°311 : 34 / 34. Mode mission (`banc_generique.mjs`) : page acceptée, 24 écrans, 44 / 44 pourquoi ;
  `enrichir.py --verifier` : à jour (30 pourquoi, 14 indices).
- Fiche papier : 11 pages (5 / 2 / 4) ; la quatrième page de la séance 3 ne porte que la licence.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.

## 21/11/2026 — Le QCM, question par question (règles d'or n°343 à n°345)

- **Cinq questions réécrites** (24 à 28). Les notions « La compétence CRCN 1.2 » et « La compétence CRCN 1.3 »
  s'affichaient au-dessus de la bonne réponse : elles sont renommées (« Ranger et sauvegarder : quelle compétence ? »…),
  et les énoncés nomment la compétence en toutes lettres (n°314) ; « le fichier de la séquence » devient « un fichier
  d'exercice ». `qcm_aides_5e_C1.3.json` suit, les aides sont reposées (`qcm_aides/poser.py --verifier` : à jour).
- **Question 15, au téléphone.** Ses propositions sont des chemins de fichier, sans espace : à 390 px, la proposition
  mesurait 558 px et la page défilait de côté. Les chemins se coupent maintenant après chaque « / » (`<wbr>`), et une
  proposition sans espace se coupe au bord de l'écran (`.option span`). Le défaut était déjà en ligne ; il a été trouvé
  en jouant les 30 questions une à une.
- `node _outils/balayer_questions_qcm.mjs --apres` sur le lot : 30 questions jouées à 390 px, 90 écrans d'aide après
  une réponse fausse, 0 écart. `controle_question_seule.py --strict` : 0 refus ; le QCM porte 3 questions sur document
  pour 6 attendues (n°345, chantier).
- Bancs rejoués : `tests_5e_C1.3-C1.4_sequence.mjs` 44 / 44 ; n°311 34 / 34.

Non fait : les 25 autres questions n'ont pas été relues une à une ; aucun document neuf n'a été dessiné pour ce QCM.

## 21/11/2026 — Une question se lit seule : le QCM relu question par question, et le billet de sortie

- Onze questions avaient des leurres qu'aucun élève ne choisirait (« peindre et entretenir les stations », « informer → supprimer → fabriquer → peindre », « rendre les vélos un peu plus lourds »…) : un leurre absurde désigne la bonne réponse. Ils sont remplacés par des confusions réelles (le réseau pris pour le stockage, l'ordre des étapes, le tri croissant…), chacun avec son pourquoi. La question 30 dit maintenant ce qu'est le transfert de Hangzhou à Sainte-Luce.

- Trois questions de plus sur document (3 → 6, n°345) : le dossier du projet (13), une **capture réelle** recadrée de LibreOffice Calc, prise sur le poste de Pascal le 12/09/2026, où toute la ligne reste dans la case A1 (19), et un tableau de cinq vélos à trier (22).

- **Billet de sortie** (n°330), à la fin de la dernière séance, juste avant le Bonus : les prêts de livres du CDI. Deux réponses écrites, chacune sa version étayée ; une correction avec ses deux critères et ses contre-exemples ; aucun bouton. Le banc le vérifie.

Exécuté : Banc 45 / 45 ; n°311 34 / 34. `node _outils/balayer_questions_qcm.mjs --apres` sur les huit QCM de C1 : 247 questions jouées à 390 px, 741 écrans d'aide après une réponse fausse, 0 écart. `controle_question_seule.py --strict` : 0 refus ; le thème 1 n'a plus de chantier D1 ni P1. Mode mission joué (`banc_generique.mjs`) : aucun refus. La dernière séance compte maintenant 1099 mots visibles (repère : 1 200 ; `mesurer_charge.mjs`).

Non fait : les questions n'ont pas été essayées en classe.
