# Rapport de tests — lot 5e_C8.2 « La patère du hall »

**Environnement réel d'exécution** : Chromium (Playwright), pages ouvertes en `file://`, hors ligne.
Tests **réellement exécutés** le 29/08/2026, puis rejoués et complétés le 30/08/2026.

**Résultat : séquence 24/24 · QCM 17/17 · zéro erreur JavaScript sur les deux pages.**
Les deux suites sont dans ce dossier et se relancent&nbsp;: `tests_5e_C8.2_sequence.mjs` et
`tests_5e_C8.2_qcm.mjs`.

## Séquence — `tests_5e_C8.2_sequence.mjs` (24 tests)

    node tests_5e_C8.2_sequence.mjs sequence_5e_C8.2_patere-du-hall.html

**24 / 24**, sous Chromium (Playwright), le 30/08/2026.

> **Ce que ce bloc remplace.** Il portait un tableau de **quatorze lignes écrites à la main**,
> quatorze coches vertes, et rien pour les rejouer. Le QCM avait reçu son script le 29/08 ; la
> séquence était restée avec sa liste de bonnes intentions. Un tableau qu'on ne peut pas
> relancer ne dit pas « ça marche », il dit « ça marchait le jour où quelqu'un a regardé ».

La suite **conduit le banc pour de vrai** : elle choisit un matériau, clique sur les paliers de
charge jusqu'à la rupture, remet une éprouvette neuve, et recommence cinq fois. Les verrous ne
sont donc pas forcés dans le code — ils s'ouvrent par le geste, comme pour un élève.

Les quatorze affirmations d'origine sont toutes rejouées. S'y ajoutent dix contrôles que le
tableau ne faisait pas :

- **aucun verrou expérientiel ouvert à l'ouverture de la page** (règle d'or n°226) ;
- une éprouvette déjà cassée refuse une charge de plus, et le dit ;
- les cinq charges de rupture sont lues sur la page, une par une (41 · 51 · 53 · 194 · 408 kg) ;
- la **formulation officielle du code** est comparée à `_outils/data_competences.py` — le test la
  lit dans le référentiel plutôt que de la recopier, sinon il cesserait de tester la citation ;
- aucun identifiant HTML en double ;
- relevés, verrous et hypothèse survivent au rechargement.

### Le contrôle qui a trouvé quelque chose

**La séquence ne portait aucune consigne de sécurité.** Son voisin `5e_C8.1` écrit pourtant
« aucune manipulation électrique dans cette séquence : ni très basse tension, ni secteur ».
Celui-ci, qui décrit un banc de traction où une masse est suspendue, ne disait rien du tout.

La consigne est ajoutée au palier du banc : le banc de la page est un **simulateur**, il n'y a
pas de secteur — et si le professeur monte un banc réel, la charge se pose et se retire à
l'arrêt, personne ne reste sous la masse, et c'est lui qui l'installe.

## QCM (17 tests)

30 questions · 30 notions distinctes · 90 réfutations · `d[r]` vide partout · répartition
A/B/C/D **8/7/7/8** (graine 82) · codes C8.2 ×20 et C3.1 ×10, tous deux au-dessus du seuil de
cinq questions · aucune réponse exposée dans le HTML rendu.

**Longueur des options** : aucune bonne réponse ne se détache de plus de 8 caractères du peloton,
écart moyen **+2,1 caractères**. Surveillé dès l'écriture cette fois, et non après coup — trois
jeux d'options ont été resserrés avant la première génération (règles n°198 et n°199).

## Ce que ce rapport ne prouve pas

Que la séquence fonctionne avec des élèves de 5ᵉ. Aucun test automatique ne le dira. Il prouve que
les pages tournent, que les verrous verrouillent, qu'un relevé inventé est refusé, et que la bonne
réponse du QCM ne se devine pas sans lire la question.

---

## Contrôle du 29/08/2026 — les deux boîtes que personne n'avait comptées

Ce rapport affirmait, ligne 3 de son tableau de séquence, « Aucune boîte modale (règle n°188) ✅ ».
C'était vrai des `alert()`, et **faux du reste** : le gabarit de QCM maison ouvre aussi deux boîtes
de confirmation — valider une question sans réponse, et « Recommencer ». Elles n'avaient jamais été
comptées, parce que la règle n°188 avait été appliquée au seul mot `alert`.

Deux corrections, faites le 29/08 :

* la page ne les ouvre plus. `_outils/sans_modale.py` les remplace par une confirmation **en deux
  temps** — premier clic : le bandeau `#savedNote` (`role="status"`, `aria-live="polite"`) annonce ;
  second clic dans les six secondes : l'action s'exécute. Une confirmation ne se supprime pas :
  elle pose une question dont la réponse change ce qui arrive ;
* **le lot reçoit enfin un script de test rejouable pour son QCM.** Il n'en avait aucun : le
  tableau « QCM (17 tests) » ci-dessus était une liste écrite à la main, que personne ne pouvait
  rejouer. `tests_5e_C8.2_qcm.mjs` est livré dans le dossier, et six de ses tests empruntent
  précisément les deux chemins qui ouvraient une boîte.

```
node tests_5e_C8.2_qcm.mjs "$PWD/qcm_5e_C8.2_patere-du-hall.html" C8.2 C3.1 sequence_5e_C8.2_patere-du-hall.html
```

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ 30 questions — 30
✅ 4 options par question
✅ 3 réfutations par question
✅ la bonne réponse n’a pas de réfutation
✅ tous les champs du gabarit remplis
✅ aucune image héritée du lot voisin
✅ 30 notions distinctes — 30
✅ 20 questions sur C8.2 — {"C8.2":20,"C3.1":10}
✅ 10 questions sur C3.1 — {"C8.2":20,"C3.1":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 2.1
✅ une bonne réponse est déclarée correcte
✅ la correction déplie les trois réfutations
✅ la correction porte un « À retenir »
✅ une mauvaise réponse est déclarée incorrecte
✅ valider sans réponse n’ouvre aucune boîte modale
✅ valider sans réponse annonce et ne valide pas encore — Tu n'as choisi aucune réponse : elle comptera comme non répondue. — clique une seconde fois pour confirmer.
✅ le second clic valide bien
✅ « recommencer » n’ouvre aucune boîte modale
✅ « recommencer » demande confirmation sans rien effacer — 30
✅ le second clic remet bien à zéro — 0
✅ le mode « marquées » vide n’ouvre aucune boîte modale
✅ il affiche un bandeau à la place — Aucune question marquée « à revoir ». Utilise le bouton 🔖 sur une question.
✅ 30 bonnes réponses donnent 100 % — 100 %
✅ la note affichée est 20/20 — 20,0 /20
✅ le lien vers la séquence pointe le bon fichier — sequence_5e_C8.2_patere-du-hall.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours

32 / 32
```

*Règle d'or n°216 : un test qui affirme qu'il ne se passe rien doit passer par les chemins où
quelque chose pourrait se passer. Sinon il mesure son propre silence.*

*La séquence de ce lot n'a toujours pas de script rejouable ; son tableau de 14 tests reste une
liste écrite à la main. C'est écrit ici pour que ce soit repris, pas pour que ce soit oublié.*

## Reprise du 04/11/2026 — la séquence passe à onglets (vague de la règle d'or n°311)

Deux séances à onglets, sur le modèle du pilote 4e_C8.1 : séance 1 = ouverture + activités 0, 1 et 2 ; séance 2 =
activités 3 et 4, réinvestissement, synthèse, Bonus, bilan, QCM. L'ouverture est repliée dans le volet « 📖 Rappel » dès
la séance 2. Le banc d'essai ne sert qu'à la séance 1 : il reste dans l'activité 0. Clôture complétée : un corrigé par
défi du Bonus, « Comment j'ai travaillé », « Je me positionne » sur 5e_C3.1.

- `node tests_regle_311_5e_C8.2.mjs` : relais 8 / 8, **34 / 34**.
- `node tests_5e_C8.2_sequence.mjs sequence_5e_C8.2_patere-du-hall.html` : **24 / 24**, comme avant ; le banc ouvre la
  séance 2 pour l'activité 3 et la séance 1 pour l'hypothèse. `tests_5e_C8.2_qcm.mjs` : 32 / 32.

Contrôles du dépôt, sur ce dossier ou sur tout le dépôt : `controle_squelette` 0 défaut (D1 à D6), aucun « à rédiger »,
aucun signalement ; `controle_impression` (0 page refusée), `controle_verrous`, `controle_hors_ligne`,
`controle_contraste_liens`, `controle_regles_visibles`, `controle_liens`, `controle_navigation_seances`,
`controle_hierarchie`, `controle_unites`, `controle_sigles`, `controle_impression_papier` : verts. `banc_papier.py` :
2 fiches, 7 pages, une séance par fiche, 0 texte pâle, 0 champ d'écran imprimé. `verif_regles_audit.py` : les mêmes ✘ qu'avant
(n°29, 30, 31, 34, 300), hors périmètre de cette vague.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.

## Révision du 15/11/2026 (ligne 53 du suivi) — gabarit commun, grille, propositions, mode mission

Migration au gabarit commun (`migrer_gabarit_306.py`, étayage dans `etayage_sequence_5e_C8.2_patere-du-hall.json`) :
15 listes en boutons radio, le choix de l'éprouvette du banc déclaré commande (`data-interface`). La grille de
l'activité 4 ne nomme plus ses lignes (« Il flue… », « Solide dans le sens des couches… »), lettrée, avec une réponse de
trop. 12 groupes mélangés, 12 propositions fausses remplacées ou allongées. Le mode mission reçoit 46 pourquoi et
5 indices (`mission_5e_C8.2.json`). Bonus replié ; aération 12 → 0.

- `node tests_5e_C8.2_sequence.mjs sequence_5e_C8.2_patere-du-hall.html` : **24 / 24** (shim `_groupesRadio(page)` en
  tête du banc ; l'activité 3 lit les boutons radio d'un groupe).
- `node tests_5e_C8.2_qcm.mjs "$PWD/qcm_5e_C8.2_patere-du-hall.html" C8.2 C3.1 sequence_5e_C8.2_patere-du-hall.html` : **32 / 32**.
- `node tests_regle_311_5e_C8.2.mjs` : **34 / 34**.
- `node _outils/mode_mission/banc_generique.mjs` : la page jouée écran par écran, aucun refus.
- `controle_ordre_propositions.py`, `controle_unites.py` : verts. `verif_regles_audit.py` : 0 ✘. `audit_aeration.py --strict` : 0.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.


## Reprise du 25-26/11/2026 — six questions sur document, et le billet de sortie

Trois documents pour le téléphone (`documents_qcm.py` → `documents_qcm_5e_C8.2.json` → `_outils/document_qcm.py`) :
le relevé du banc, la fiche d'essai de l'aluminium, « ce que l'essai de traction ne voit pas ». Six questions s'y lisent.
Deux notions renommées : « Le verbe de la compétence » (n°304) et « Croiser les contraintes » (n°344). Le billet de
sortie ferme la séance 2, avant le Bonus : le fil du pot de fleurs, deux questions écrites, deux versions étayées, une
correction complète. Le réinvestissement passe à la maison, comme en 5e_C8.1.

| Commande | Résultat |
|---|---|
| `node tests_5e_C8.2_qcm.mjs qcm_5e_C8.2_patere-du-hall.html C8.2 C3.1 sequence_5e_C8.2_patere-du-hall.html` | **34 / 34** — dont : six questions sur document au moins ; des documents du lot, présents et décrits ; `documents_qcm.py --verifier` |
| `node tests_5e_C8.2_sequence.mjs sequence_5e_C8.2_patere-du-hall.html` | **26 / 26** — deux tests nouveaux : la forme du billet ; la réponse survit au rechargement |
| `node tests_regle_311_5e_C8.2.mjs .` | 34 / 34 |
| `python3 _outils/document_qcm.py documents_qcm_5e_C8.2.json --verifier` · `node _outils/controle_schemas.mjs <lot>` | 0 écart · 0 ✘, 0 ⚠ |
| `python3 _outils/controle_question_seule.py --chantiers <lot>` | 0 partout (avant : S3 1, E1 1, D1 1, P1 1) |
| `node _outils/balayer_questions_qcm.mjs --apres <lot>` · `banc_aides.mjs` · `poser.py --verifier` | 0 écart · 0 refus · à jour |
| `controle_squelette`, `banc_generique.mjs` (mode mission), `banc_papier.py`, `audit_aeration.py --strict` | verts |
| `controle_unites`, `controle_indices_qcm`, `verif_qcm_coherence`, `controle_entete_qcm`, `controle_banque_qcm`, `controle_effectifs_qcm`, `controle_sigles`, `controle_hierarchie`, `controle_liens` | sans écart |

Regardé à 312 px (les trois documents) et à 390 px (le billet) : lisible, aucun défilement de côté, 0 erreur JavaScript.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.

## 26/11/2026 — Séance 1 ramenée à 55 min : l'activité 0 casse deux éprouvettes

Décision de Pascal (carte blanche) : l'activité 0 casse **deux** éprouvettes de matériaux différents au lieu de trois
(par exemple le bois à 41 kg, puis l'aluminium à 194 kg) ; elle passe de 10 à 5 min. Les deux questions et leur
correction ne changent pas ; les pourquoi « relis tes trois essais / relevés » disent « deux » (page et `mission_5e_C8.2.json`).
Le verrou devient `banc2` (deux ruptures) ; `restore()` le rouvre depuis la liste des éprouvettes cassées, si bien qu'une
sauvegarde d'avant (qui disait `banc3`) ne bloque pas l'élève.

Exécuté, dans le dossier du lot ou à la racine :
- `node tests_5e_C8.2_sequence.mjs` : **26 / 26** — le test 7 refuse l'activité 0 après une seule rupture (le bois) ; le
  test 8 l'ouvre après la deuxième (l'aluminium) et lit « Deux éprouvettes cassées » ; le test 22 relit `banc2` et `banc5`
  après rechargement.
- `node tests_regle_311_5e_C8.2.mjs` : **34 / 34**.
- `verif_regles_audit.py` sur le lot : n°23 « 85 min annoncés (+10 de service) pour 110 disponibles », sortie 0.
- `audit_aeration.py --strict`, `controle_squelette.mjs`, `mode_mission/banc_generique.mjs`, `enrichir.py --verifier-tout`,
  `controle_liens.py` : verts.
