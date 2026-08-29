# 4e_C7.8 — Le jardin publie sa mesure

> **Interfacer un objet technique avec un réseau.**
> Programme 2024 · cycle 4 · thème 3 · socle D1.3 · D2 · D4 · D5

➡ **[Ouvrir la séquence](sequence_4e_C7.8_le-jardin-publie.html)** — 2 séances de 55 min, banc de liaison intégré, hors ligne,
sans installation ni compte.

---

## Ce que le lot fait

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


## Ce que ce lot ne refait PAS

Le réseau est déjà largement couvert par le Thème 2, et ce lot s'appuie dessus **sans le
refaire** :

| Ce qui existe déjà | Ce que ça traite |
|---|---|
| `5e_C4.7` — le réseau de la salle techno | topologie, composants, Packet Tracer |
| `4e_C4.7` — SOS serre | plan d'adressage, IP fixe, passerelle |
| `3e_C4.7` / `3e_C4.8` | circulation d'un paquet, routage, deux réseaux |

C7.8 est au Thème 3 : le verbe est **interfacer**, et tout ce qui se décide ici est du côté de
**l'objet** — ce qu'il envoie, quand, à qui, et ce qu'il fait quand plus personne n'écoute.

## Le banc de liaison

Original, écrit pour ces deux lots, en HTML et JavaScript, sans dépendance et sans réseau.
L'élève **compose le message case par case** et le banc lui dit, ligne par ligne, ce que le
destinataire peut ou ne peut pas en faire. Puis il **coupe le lien** et regarde ce que l'objet
devient.

| Champ | Ce que c'est | |
|---|---|---|
| `id` | l'identifiant de l'objet qui parle | ✅ à envoyer |
| `h` | la valeur lue par le capteur d'humidité | ✅ à envoyer |
| `u` | l'unité de cette valeur | ✅ à envoyer |
| `t` | l'heure à laquelle la mesure a été prise | ✅ à envoyer |
| `pompe` | l'état de la pompe au moment de la mesure | ✅ à envoyer |
| `etat` | les 127 variables internes de la carte | ❌ à ne pas envoyer |
| `eleve` | le prénom de l'élève qui a programmé la carte | ❌ à ne pas envoyer |

## Tests

**35 / 35** sur la séquence, **32 / 32** sur le QCM, rejouables : scripts et jeu de réponses
livrés dans le dossier. Voir [`rapport_tests_4e_C7.8.md`](rapport_tests_4e_C7.8.md).

## Fichiers

| Fichier | Contenu |
|---|---|
| [`sequence_4e_C7.8_le-jardin-publie.html`](sequence_4e_C7.8_le-jardin-publie.html) | 6 activités chronométrées, banc intégré |
| [`qcm_4e_C7.8_le-jardin-publie.html`](qcm_4e_C7.8_le-jardin-publie.html) | 30 q · 90 réfutations · 4e_C7.8 ×20, 4e_C1.4 ×10 |
| [`lexique_4e_C7.8.html`](lexique_4e_C7.8.html) | 30 notions, générées depuis le QCM du lot |
| [`synthese_eleve_4e_C7.8.html`](synthese_eleve_4e_C7.8.html) | à imprimer, lisible en noir et blanc |
| [`synthese_professeur_4e_C7.8.html`](synthese_professeur_4e_C7.8.html) | pari didactique, verrous, limites, LSU |
| [`fiche_pedagogique_4e_C7.8.md`](fiche_pedagogique_4e_C7.8.md) | déroulé, message, comportements, différenciation |
| [`matrice_couverture_4e_C7.8.csv`](matrice_couverture_4e_C7.8.csv) | notion → activité → production → questions |
| [`rapport_tests_4e_C7.8.md`](rapport_tests_4e_C7.8.md) | la sortie des deux suites, telle quelle |
