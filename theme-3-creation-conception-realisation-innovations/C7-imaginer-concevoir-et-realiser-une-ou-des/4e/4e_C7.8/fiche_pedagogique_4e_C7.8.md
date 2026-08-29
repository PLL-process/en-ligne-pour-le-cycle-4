# Fiche pédagogique — 4e_C7.8 « Le jardin publie sa mesure »

> **Interfacer un objet technique avec un réseau.**
> Programme 2024 · cycle 4 · thème 3 · socle D1.3 · D2 · D4 · D5

| | |
|---|---|
| **Niveau** | 4e |
| **Code principal** | 4e_C7.8 — 20 questions de QCM |
| **Code d'appui** | 4e_C1.4 — *Identifier et appliquer les règles pour un usage raisonné des objets communicants et des environnements numériques (propriété intellectuelle, identité numérique, témoins de connexion, géolocalisation).* — 10 questions |
| **Durée** | 2 séances de 55 min — 95 min d'activités obligatoires |
| **Matériel** | un navigateur, hors ligne. Aucune installation, aucun compte. |
| **Version A** | deux cartes réelles + moniteur série ; les trames observées font alors foi |

---

## 1. Le pari didactique

Le verbe du code est **interfacer**, et le piège de la séance est là : l'adressage
est déjà fait. Le jardin a une adresse IP fixe depuis l'atelier SOS serre, il est joignable, et
il ne dit rien. **Un objet branché n'est pas un objet qui communique.**

Le geste qui porte la séance est le bouton **✂ Couper le lien**. Un élève qui a composé un
message parfait mais n'a pas décidé ce que l'objet fait hors ligne n'a pas fini le travail — et
la page le lui montre plutôt que de le lui dire.

**Le moment le plus réussi du lot** est l'apparition différée du champ `t` :
coché à l'activité 1 sans qu'on voie bien pourquoi (le récepteur sait quand il reçoit, non ?),
il trouve sa raison d'être deux activités plus tard, quand douze mesures libérées d'un coup
seraient toutes datées de la même minute.


## 2. Déroulé

| # | Activité | Durée | Réponses attendues | Verrou expérientiel |
|---|---|---|---|---|
| 0 | FAIRE d'abord : composer un message | ~20 min | 3 | msgEssaye |
| 1 | Composer le message qui suffit | ~20 min | 5 | msgOk |
| 2 | Qui prend l'initiative, et à quel rythme | ~15 min | 3 | — |
| 3 | Couper le lien, et voir ce que l'objet devient | ~20 min | 4 | coupe |
| 4 | Ce qu'on n'envoie pas, et pourquoi | ~10 min | 4 | — |
| — | REFAIRE | ~10 min | 1 | — |

## 3. Le message du lot

| Champ | Ce que c'est | |
|---|---|---|
| `id` | l'identifiant de l'objet qui parle | ✅ à envoyer |
| `h` | la valeur lue par le capteur d'humidité | ✅ à envoyer |
| `u` | l'unité de cette valeur | ✅ à envoyer |
| `t` | l'heure à laquelle la mesure a été prise | ✅ à envoyer |
| `pompe` | l'état de la pompe au moment de la mesure | ✅ à envoyer |
| `etat` | les 127 variables internes de la carte | ❌ à ne pas envoyer |
| `eleve` | le prénom de l'élève qui a programmé la carte | ❌ à ne pas envoyer |

## 4. Les comportements hors liaison

| Comportement | Ce que le banc en dit |
|---|---|
| perd la mesure et passe à la suivante | ✘ PERDUE  la mesure n'existe plus nulle part |
| garde les mesures en file et les envoie au retour du lien | ⚠ en file (N en attente) — elles partiront au retour |
| cesse d'arroser jusqu'au retour du lien | ✘ l'objet s'est ARRÊTÉ — et le réseau n'y était pour rien |

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

* **Aucune liaison réelle.** Le banc simule l'échange ; la version 🅰 le fait avec deux cartes et le moniteur série, et ce sont les trames observées qui font foi.
* **L'adressage n'est ni travaillé ni évalué ici.** Il l'est par l'atelier SOS serre (4e_C4.7), et ce lot s'appuie dessus sans le refaire — c'est délibéré, et c'est écrit dans la première section de la séquence.
* **Le format est imposé.** Le banc écrit du JSON ; le choix d'un format est traité en question de QCM et en défi bonus, pas en activité.
* **Le vérificateur ne lit pas la phrase rédigée** de l'activité 3 : il compte des caractères. C'est écrit dans la page.

## 8. Prolongements


  **🔤 Défi format :** le message du banc est en JSON. Cherche à quoi ressemblerait le même
  message en CSV, et dis ce qu'on gagne et ce qu'on perd en changeant de format.
  **📏 Défi taille :** compte les caractères du message complet, puis de la version où tous
  les champs porteraient leur nom en entier (`humidite`, `horodatage`…).
  Sur 288 envois par jour, combien de caractères d'écart ? Et est-ce que ça vaut la perte de
  lisibilité ?
  **🔌 Défi réel :** avec ta carte et le réseau du collège, fais afficher une seule mesure
  sur le moniteur série d'un autre poste. Note ce qui a été plus difficile que dans le banc.


## 9. Fichiers du lot

```
4e_C7.8/
├── sequence_4e_C7.8_le-jardin-publie.html
├── qcm_4e_C7.8_le-jardin-publie.html
├── lexique_4e_C7.8.html
├── synthese_eleve_4e_C7.8.html · synthese_professeur_4e_C7.8.html
├── fiche_pedagogique_4e_C7.8.md · matrice_couverture_4e_C7.8.csv
├── rapport_tests_4e_C7.8.md
└── tests_4e_C7.8_sequence.mjs · tests_4e_C7.8_qcm.mjs · reponses_4e_C7.8.json
```
