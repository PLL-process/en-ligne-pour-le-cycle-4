# Les trois audits C4–C6, vérifiés un par un

**Documents lus** — `AUDIT_C4-C6_MATRICE_REMPLACEMENTS.md` (32,6 ko, 25 défauts D01→D25,
24 activités de remplacement) · `ChatGPT — Audit pédagogique Thème 2, C4 à C6` (48,1 ko) ·
`Grok — Audit pédagogique Thème 2, C4 à C6` (37,0 ko).

**Principe de lecture** — *un audit est une production, pas un verdict.* Chacune des
affirmations vérifiables ci-dessous a été transformée en mesure sur le dépôt avant d'être
retenue ou écartée. Les scripts qui les mesurent sont dans `_outils/controle_statut.py` et
dans le corps de ce document ; aucune n'est reprise sur parole.

Bilan : **sur 24 affirmations vérifiables, 18 sont exactes, 3 sont fausses, 3 sont exactes
sur le fond et fausses sur le chiffre.** Et une chose qu'aucun des trois n'a vue.

> **Corrigé le 28/08/2026 — trois verdicts de ce document étaient faux, et pour la même raison.**
> Cf. §6. La première version annonçait « 17 exactes, 4 fausses », affirmait que cinq séquences
> n'annonçaient aucune durée, et déclarait introuvable un critère qui est écrit dans la page.
> Trois fois, je mesurais une convention d'écriture au lieu de la chose. Les chiffres ci-dessous
> sont ceux de la mesure corrigée, produite par `_outils/mesurer_temps_seances.py`.

---

## 1. Ce que les trois ont vu juste

| Affirmation | Source | Mesure |
|---|---|---|
| « L'exécution n'est pas indispensable » figure bien dans `3e_C6.1` | ChatGPT §4.2 | citation retrouvée mot pour mot |
| `3e_C4.1–C4.2` : 115 min d'activités obligatoires pour 110 disponibles | ChatGPT §4 | **exact** : 25+30+15+30+15 = 115 ; le bonus Ohm (20 min) est déjà marqué *facultatif* et n'a pas été compté |
| `4e_C6.1–C6.3` : exactement 110 min pour 110 disponibles, zéro marge | ChatGPT §11 | **exact au chiffre près** : 30+25+40+15 = 110 |
| `4e_C6.2` : trois `<iframe>` Vittascience | ChatGPT §7 | 3 iframes |
| `4e_C6.2` : pas de fiche pédagogique, pas de matrice | ChatGPT §7 | dossier vérifié : ni l'une ni l'autre |
| `4e_C4.1–C4.9` (jardin) : fiche pédagogique absente | ChatGPT §4 | **exact** — 16 fiches dans le Thème 2, aucune pour ce lot |
| Mode essentiel présent partout **sauf** `4e_C6.2` | ChatGPT §3 | exactement 1 séquence sur 17 sans mode essentiel |
| `3e_C6.2` : « huit lignes remises dans l'ordre + la ligne manquante » | ChatGPT §4.3 | production citée mot pour mot dans la page |
| Multimètres et impression 3D « matériel à confirmer » en `3e_C5` | ChatGPT §6 | mention retrouvée |
| Aucun rôle de binôme nommé dans les 17 séquences | matrice D16, Grok P1 | **0 bloc de rôles sur 17** |
| Aucun glossaire / lexique dans tout le Thème 2 | Grok P1, matrice D18 | **0 fichier `lexique*.html`** (le Thème 1 en a 13) |
| Bandeau « ⏱ 4 séances de 55 min » du jardin | matrice D01 | présent |
| « recopie la chaîne d'énergie au cahier » | matrice D22 | présent |
| « clique sur les 6 zones » (`5e_C5.1`) | matrice D03 | présent |
| H2 « les quatre gestes de Packet Tracer » | matrice D05 | présent |
| « M. Firmin, le gestionnaire » | matrice D21 | présent |
| « La loi d'Ohm au chevet de la station » | matrice D09 | présent |
| Critère « **9 / 9** et la chaîne recopiée au cahier » | matrice D22 | présent — *j'avais dit le contraire, voir §6* |

---

## 2. Ce qui est faux

### 2.1 L'erreur de passerelle de SOS serre — l'affirmation la plus grave, et elle ne tient pas

ChatGPT §5 écrit : « Dans SOS serre, `192.168.20.1` est configurée comme passerelle par défaut
alors qu'aucun routeur portant cette adresse n'est présent », et propose trois correctifs :
ajouter un routeur, ou laisser la passerelle vide en expliquant pourquoi, ou préciser que le
`.1` est une convention et non une obligation.

La page fait déjà les deux derniers, en toutes lettres :

> « Remarque d'urbaniste : la passerelle 192.168.20.1 est prévue au plan mais **non installée
> dans notre montage d'entraînement** — la porte est réservée, la maison n'est pas encore
> construite. Elle prendra corps en 3ᵉ, avec le routeur. »

> « À savoir : le `.1` n'est pas une loi d'Internet — c'est le choix du gestionnaire, une
> convention très courante. Un autre gestionnaire aurait pu choisir `.254`. »

L'objection avait été anticipée et traitée avant d'être formulée. **Rien à corriger.**

### 2.2 « Le corpus déborde de partout »

Les trois documents s'accordent : les durées écrites sont incompatibles avec le volume
d'activités. Mesuré sur les 17 séquences (`_outils/mesurer_temps_seances.py`) :

| Séquence | annoncé | demandé | marge |
|---|---:|---:|---|
| `3e_C4.1–C4.2` énergie station | 110 | 115 | **−5** |
| `4e_C6.1–C6.3` ajuster jardin | 110 | 110 | **0** |
| `3e_C4.3–C4.6` station alerte | 220 | 215 | +5 |
| `3e_C4.7–C4.8` Internet Sainte-Luce | 165 | 160 | +5 |
| `3e_C6.1–C6.3` programmer alerte | 165 | 160 | +5 |
| `4e_C4.1–C4.2–C4.4` Book Train | 165 | 154 | +11 |
| `4e_C4.7–C4.9` SOS serre | 220 | 205 | +15 |
| `5e_C4.7–C4.8` réseau local | 165 | 144 | +21 |
| `3e_C6.2` auto-test station | 165 | 144 | +21 |
| `3e_C5.1–C5.4` SOS station | 220 | 195 | +25 |
| `3e_C4.7–C4.8` pont numérique | 165 | 139 | +26 |
| `4e_C5.1–C5.3` dépanner jardin | 165 | 135 | +30 |
| `5e_C5.1–C5.3` dépanner lampadaire | 165 | 135 | +30 |
| `4e_C4.1–C4.9` jardin | 220 | 189 | +31 |
| `5e_C6.1–C6.3` programmer lampadaire | 165 | 130 | +35 |
| `5e_C4.1–C4.8` lampadaire | 275 | 235 | +40 |
| `4e_C6.2` arrosage automatique | *aucun bandeau* | 145 | — |

**Deux séquences sur seize sont sans marge. Les quatorze autres en ont de 5 à 40 minutes.**
Le débordement existe : il fait exactement deux lots de large, pas dix-sept. Les deux chiffres
annoncés par ChatGPT (115/110 et 110/110) sont exacts au chiffre près.

Le vrai décalage est ailleurs. **Seize séquences écrivent « séances de 55 min ». Le créneau
réel est de 90.** Une séquence qui tient dans 2 × 55 tient à l'aise dans 2 × 90 : le problème
n'est pas qu'elle déborde, c'est qu'elle annonce un **nombre de séances** qui ne se pose pas
sur les semaines. Le calage Pronote proposé par la matrice (§3) est donc le bon remède —
appliqué au bon diagnostic.

Et la maison a déjà tranché ailleurs : les cinq pages du lot `3e_C9.2` (Thème 3, les plus
récentes du dépôt) écrivent **« 4 séances de 90 min (1 h 30) »**. Le gabarit existe ; ce sont
les seize bandeaux du Thème 2 qui sont restés à l'ancienne convention.

### 2.3 « 16 séquences »

La matrice et Grok annoncent 16 séquences C4–C6, ChatGPT 17. **Il y en a 17.** La différence
compte : la dix-septième est `sequence-jardin-connecte-arrosage-automatique.html` (`4e_C6.2`),
c'est-à-dire précisément celle qui pose le plus de problèmes. Deux audits sur trois ont bâti
leur périmètre sans elle.

*(La section 2.4 de la première version — « le critère 9/9 n'existe pas » — était fausse.
Elle est retirée : voir §6.)*

---

## 3. Exact sur le fond, faux sur le chiffre

| Affirmation | Mesure |
|---|---|
| « Les trois QCM de `4e_C6.2` sont signalés **en brouillon** » (ChatGPT §7) | Ils portent le badge 🛠 **« ressource héritée »** (règle d'or n°12), pas « brouillon ». Le fond tient : sur les trois, **un seul** porte une vraie banque (`eclairage_automatique`, 30 q) ; `algorigrammes_domotique` et `jardin_connecte` n'ont **aucune** banque de questions. |
| « Les 17 pages comportent entre 26 et 60 éléments de réponse » (ChatGPT §9) | **28 à 70.** La densité est réelle et un peu sous-estimée : `5e_C4.1–C4.8` en porte 70. |
| « QCM multiples sur le même objet 4ᵉ », 4 QCM cités (matrice D19) | La règle Fable n°4 dit *un seul bouton QCM dans la séquence*. Une seule séquence sur 17 l'enfreint : le jardin `4e_C4.1–C4.9`, qui en propose **deux**. Les autres fichiers existent mais ne sont pas boutonnés dans la page. |

---

## 4. Ce qu'aucun des trois n'a vu

**Une séquence n'annonce aucune durée** : `4e_C6.2` (`sequence-jardin-connecte-arrosage-automatique`),
seule des dix-sept à n'avoir ni bandeau, ni nombre de séances. L'enseignant qui l'ouvre n'a
aucun chiffre sous les yeux. C'est le lot qui cumule déjà tout le reste.

*(La première version de ce document annonçait **cinq** séquences muettes. C'était faux : les
quatre autres écrivent bien « N séances de 55 min », simplement sans l'emoji ⏱ juste devant,
et c'est l'emoji que je comptais. Voir §6.)*

**Le statut public de quatre codes n'est pas soutenable.** Les trois audits disent, chacun à
sa manière, que la gouvernance de validation est trop généreuse. Aucun ne dit de combien.
Le contrôle posé par la PR #263 (`_outils/controle_statut.py`) mesure, pour chaque code
revendiquant « ✅ complet et validable », la présence effective des six pièces que ce label
implique — séquence, QCM avec une vraie banque, fiche, matrice, synthèses, rapport de tests.

Sur les 31 codes qui le revendiquaient :

| Code | Ce qui manque | Devient |
|---|---|---|
| `4e_C4.1` — jardin connecté | fiche pédagogique | À vérifier par l'enseignant |
| `4e_C4.2` — Book Train | dossier **vide** (Images/, Synthèses/, README) | Couvert par une séquence mutualisée |
| `4e_C4.4` — Book Train | dossier **vide** | Couvert par une séquence mutualisée |
| `4e_C6.2` — arrosage automatique | fiche, matrice, synthèses | À vérifier par l'enseignant |

**27 sur 31 tiennent leur promesse.** Le défaut est réel et il fait quatre codes de large.
Les deux codes du Book Train ne perdent rien : leur travail existe, dans
`4e_C4.1_book-train/` — c'est leur étiquette qui était fausse, pas leur contenu.

## 5. Ce qui reste à faire, dans l'ordre

1. **Écrire la fiche pédagogique du jardin `4e_C4.1–C4.9`** — c'est la seule pièce qui
   manque au lot phare de la 4ᵉ, et la seule raison de sa rétrogradation.
2. **Poser un bandeau `⏱` sur les cinq séquences qui n'en ont pas**, calculé sur leurs
   propres activités.
3. **Trancher 55 → 90 min.** Douze séquences annoncent un découpage qui ne correspond pas au
   créneau réel. Deux voies : réécrire les bandeaux en créneaux de 90 min, ou publier le
   calage Pronote de la matrice §3 comme document d'accompagnement sans toucher aux pages.
   *C'est une décision d'enseignant, pas de dépôt : elle attend Pascal.*
4. **`4e_C6.2`** — la séquence n'a ni fiche, ni matrice, ni mode essentiel, ni bouton QCM,
   et deux de ses trois « QCM » n'en sont pas. C'est le lot le plus faible des trois thèmes.
5. **Rôles de groupe et lexiques** — 0 sur 17 dans les deux cas. Les outils existent déjà
   (`poser_roles.py`, `generer_lexique.py`, écrits pour le Thème 1) et s'appliquent tels quels.

Le reste — kits TBT, quiz sécurité en quatre images, carrousel des défauts, réglette CAN,
algorigramme magnétique, captures Packet Tracer — sont de **bonnes propositions de classe**
qui ne se rangent pas dans un dépôt HTML. Elles valent d'être faites ; elles ne valent pas
d'être commitées.

---

## 6. Correction — trois verdicts de ce document étaient faux

Publiés le 28/08/2026 dans la PR #263, corrigés le même jour. Les trois erreurs sont la même.

| Ce que j'avais écrit | Ce qui est vrai | Ce que je mesurais |
|---|---|---|
| « Le critère *9/9* n'existe pas dans la page » | La page écrit « Critère de réussite : **9 / 9** et la chaîne recopiée au cahier avec les natures d'énergie ». La matrice D22 avait raison. | les espaces |
| « Cinq séquences n'annoncent aucune durée » | **Une** seule. Les quatre autres écrivent « N séances de 55 min » sans ⏱ devant. | l'emoji |
| `5e_C4.7–C4.8` : 4 min d'activités pour 3 séances | 144 min. La page écrit « ⏱ **≈** 20 min » ; mon lecteur n'admettait pas le `≈`. | le signe |

Trois fois la règle d'or n°184 — *un indicateur bâti sur une convention d'écriture mesure la
convention, pas la chose* — commise dans le document qui la reprochait à trois audits externes.
Un audit qui se trompe une fois sur quatre reste un bon audit ; le mien se trompait une fois
sur huit, ce qui ne vaut pas mieux tant qu'on ne sait pas laquelle.

Le remède n'est pas la vigilance, c'est le contrôle : `_outils/mesurer_temps_seances.py`
**refuse de rendre son tableau** si une seule séquence ressort sans aucune durée d'activité —
parce que zéro n'est presque jamais un résultat, c'est une panne de lecture. Passé sur les
trois thèmes, ce contrôle a immédiatement signalé quatre pages du Thème 1 : deux pointeurs de
mutualisation (normal) et **les deux lots héritage `4e_C1.4` et `3e_C1.5`, qui n'écrivent
aucune durée d'activité**. Sixième indicateur indépendant à désigner ces deux-là.

**Règle d'or n°194** — un outil de mesure se teste d'abord sur un cas dont on connaît la
réponse. Un résultat nul n'est pas une découverte : c'est la première chose à vérifier.
