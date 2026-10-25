# Fiche pédagogique — 3e_C7.8 « Deux stations qui se parlent »

> **Interfacer deux objets techniques communicants.**
> Programme 2024 · cycle 4 · thème 3 · socle D1.3 · D2 · D3 · D4 · D5

| | |
|---|---|
| **Niveau** | 3e |
| **Code principal** | 3e_C7.8 — 20 questions de QCM |
| **Code d'appui** | 3e_C8.3 — *Proposer un protocole de test pour valider le comportement et les performances d'un objet technique.* — 10 questions |
| **Durée** | 3 séances de 55 min (depuis le 24/10/2026, au lieu de 2 séances de 90 min) — 150 min d'activités obligatoires : 45 + 55 + 50 |
| **Matériel** | un navigateur, hors ligne. Aucune installation, aucun compte. |
| **Version A** | deux cartes réelles + moniteur série ; les trames observées font alors foi |

---

## 1. Le pari didactique

Le verbe du code est **interfacer deux objets communicants** — deux, et pas un
objet et un écran. Personne ne lit, personne n'arbitre, personne ne s'étonne. Tout ce qu'un
humain compensait sans y penser doit devenir un champ, une règle ou un délai.

**Le ressort de la séance :** la règle de la mairie — « la sirène ne part que si les deux
stations sont d'accord » — est juste, et elle crée aussitôt un défaut pire que celui qu'elle
corrige. Si Sainte-Anne est détruite par le grain qui arrive sur Le Robert, il n'y a plus
d'alerte du tout. C'est une **défaillance dangereuse** : le système tombe du mauvais côté.

**Et la bonne réponse n'est pas un compromis mais un troisième terme :** on déclenche,
*et on écrit qu'on était seule*. La décision de sécurité est prise, l'incertitude est
transmise à l'humain. C'est la règle « dégradé, pas éteint » du lot de 4ᵉ, appliquée
cette fois à une sirène.


## 2. Déroulé

Trois séances de 55 min (une heure de cours par semaine). La page défile d'un seul tenant : un
en-tête « 🗓 Séance N » ouvre chaque séance (durée, question de la séance, et à partir de la
séance 2 ce dont l'élève repart), un bouton « ➡ Séance N+1 » la ferme, et des liens sous le titre
mènent à chacune. Aucune activité n'est coupée ni raccourcie : on coupe entre deux activités.

| Séance | # | Activité | Durée | Réponses attendues | Verrou expérientiel |
|---|---|---|---|---|---|
| **1 — Ce que deux machines s'échangent** (45 min) | 0 | FAIRE d'abord : faire parler les deux stations | ~20 min | 3 | msgEssaye |
| | 1 | Le message entre deux machines | ~25 min | 6 | msgOk |
| **2 — Se mettre d'accord, et quand l'autre se tait** (55 min) | 2 | Écrire la règle d'accord | ~25 min | 4 | — |
| | 3 | Et quand l'autre se tait | ~30 min | 5 | coupe |
| **3 — Prouver que la liaison tient, puis passer à trois** (50 min) | 4 | Écrire les essais qui le prouvent | ~30 min | 6 | — |
| | — | REFAIRE | ~20 min | 1 | — |
| | | puis synthèse, Bonus facultatif, bilan, renvoi au QCM | | | |

**Pourquoi ce découpage.** C'est le seul en trois séances qui ne coupe aucune activité (la
séance 1 ne peut finir qu'après l'activité 1, la séance 2 qu'après l'activité 3), et il suit le
raisonnement : la séance 1 décide du message (ce qu'une machine ne devine pas), la séance 2
porte la problématique entière (la règle d'accord, puis le silence de l'autre — sa question est
celle de la séquence), la séance 3 prouve et transfère (les six essais, la troisième station).
L'activité 3 (séance 2) se fait au banc, qui est à l'activité 0 (séance 1) : l'en-tête de la
séance 2 et la consigne y renvoient par un lien ; les cases cochées du banc sont sauvegardées,
l'état « lien coupé » non (on le recoupe d'un clic). Les 10 min libres de la séance 1 servent à
la situation, à l'idée de départ et à l'encadré « ce qui ne sort jamais » ; les 5 min de la
séance 3, à la synthèse et au bilan. **La séance 2 est pleine (55 min, sans marge).**

## 3. Le message du lot

| Champ | Ce que c'est | |
|---|---|---|
| `id` | l'identifiant de la station qui parle | ✅ à envoyer |
| `v` | la vitesse du vent mesurée | ✅ à envoyer |
| `u` | l'unité de cette vitesse | ✅ à envoyer |
| `t` | l'heure de la mesure | ✅ à envoyer |
| `niv` | le niveau d'alerte que CETTE station a calculé | ✅ à envoyer |
| `seq` | le numéro d'ordre du message | ✅ à envoyer |
| `hist` | les 2 000 mesures des dernières 24 heures | ❌ à ne pas envoyer |
| `cle` | la clé du réseau, « pour que l'autre se connecte » | ❌ à ne pas envoyer |

## 4. Les comportements hors liaison

| Comportement | Ce que le banc en dit |
|---|---|
| déclenche seule, sans rien signaler | ⚠ ALERTE déclenchée seule — et personne ne sait qu'elle n'était pas corroborée |
| ne déclenche jamais sans l'accord de l'autre | ✘ AUCUNE alerte — 124 km/h mesurés, et la sirène reste muette |
| déclenche seule, et signale qu'elle est seule | ✔ ALERTE déclenchée, marquée « NON CORROBORÉE — Sainte-Anne muette depuis 15 min » |

## 5. Sécurité et usage raisonné

Très basse tension **5 V**. **Aucune donnée personnelle** dans une mesure, **aucun secret,
aucune clé** dans un message : tout ce qui circule est lisible sur le chemin. Le réseau utilisé
est celui du collège ; on n'ouvre pas un objet vers l'extérieur sans l'accord de la personne qui
l'administre.

## 6. Différenciation

* **🅰 avec le matériel** — deux cartes, un vrai réseau, le moniteur série pour lire les trames.
* **🅱 avec le banc de la page** — hors ligne, sans installation. Seule voie qui permette de
  **couper le lien** pour voir ce que l'objet devient.
* **🅲 sans écran (débranché)** — deux élèves jouent les deux objets, une feuille pliée fait le
  message, le professeur intercepte.

## 7. Ce que ce lot ne fait pas

* **Aucune liaison réelle.** Le banc simule ; la version 🅰 le fait avec deux cartes.
* **Le routage et l'adressage ne sont ni travaillés ni évalués ici.** Ils le sont par 3e_C4.7 et 3e_C4.8, et ce lot s'appuie dessus sans les refaire.
* **La synchronisation des horloges est laissée en défi bonus.** La règle de fraîcheur suppose deux horloges à peu près justes ; le lot le dit, et n'entre pas dans le mécanisme.
* **L'accusé de réception n'est pas traité en activité** — seulement en défi. Un lot complet sur la fiabilité de transport serait un autre lot.
* **Le vérificateur ne lit pas la règle rédigée** de l'activité 2 : il compte des caractères. La relecture par le binôme reste nécessaire.

## 8. Prolongements


  **⏱ Défi horloges :** les deux stations comparent des heures. Que se passe-t-il si
  l'horloge de Sainte-Anne retarde de dix minutes ? Cherche comment deux machines
  synchronisent leurs horloges, et dis ce que ça change à ta règle de fraîcheur.
  **🔁 Défi accusé de réception :** le Robert envoie et ne sait pas si Sainte-Anne a reçu.
  Propose un mécanisme pour qu'il le sache — et dis ce qu'il faut faire quand l'accusé de
  réception, lui, se perd.
  **🗳 Défi trois capteurs :** cherche pourquoi les avions de ligne embarquent
  **trois** sondes de vitesse et non deux. Écris en trois lignes ce que ça a à voir avec la
  station du Marin.


## 9. Fichiers du lot

```
3e_C7.8/
├── sequence_3e_C7.8_deux-stations.html
├── qcm_3e_C7.8_deux-stations.html
├── lexique_3e_C7.8.html
├── synthese_eleve_3e_C7.8.html · synthese_professeur_3e_C7.8.html
├── fiche_pedagogique_3e_C7.8.md · matrice_couverture_3e_C7.8.csv
├── rapport_tests_3e_C7.8.md
└── tests_3e_C7.8_sequence.mjs · tests_3e_C7.8_qcm.mjs · reponses_3e_C7.8.json
```
