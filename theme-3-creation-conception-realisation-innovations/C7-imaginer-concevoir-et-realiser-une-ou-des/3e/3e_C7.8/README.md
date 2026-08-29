# 3e_C7.8 — Deux stations qui se parlent

> **Interfacer deux objets techniques communicants.**
> Programme 2024 · cycle 4 · thème 3 · socle D1.3 · D2 · D3 · D4 · D5

➡ **[Ouvrir la séquence](sequence_3e_C7.8_deux-stations.html)** — 2 séances de 90 min (1 h 30), banc de liaison intégré, hors ligne,
sans installation ni compte.

---

## Ce que le lot fait

Le verbe du code est **interfacer deux objets communicants** — deux, et pas un
objet et un écran. Personne ne lit, personne n'arbitre, personne ne s'étonne. Tout ce qu'un
humain compensait sans y penser doit devenir un champ, une règle ou un délai.

**Le ressort de la séance :** la règle de la mairie — « la sirène ne part que si les deux
stations sont d'accord » — est juste, et elle crée aussitôt un défaut pire que celui qu'elle
corrige. Si Sainte-Anne est détruite par le grain qui arrive sur Le Robert, il n'y a plus
d'alerte du tout. C'est une **défaillance dangereuse** : le système tombe du mauvais côté.

**Et la bonne réponse n'est pas un compromis mais un troisième terme :** on déclenche,
*et on écrit qu'on était seule*. La décision de sécurité est prise, l'incertitude est
transmise à l'humain. C'est la règle « dégradé, pas éteint » du lot de 4<sup>e</sup>, appliquée
cette fois à une sirène.


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
| `id` | l'identifiant de la station qui parle | ✅ à envoyer |
| `v` | la vitesse du vent mesurée | ✅ à envoyer |
| `u` | l'unité de cette vitesse | ✅ à envoyer |
| `t` | l'heure de la mesure | ✅ à envoyer |
| `niv` | le niveau d'alerte que CETTE station a calculé | ✅ à envoyer |
| `seq` | le numéro d'ordre du message | ✅ à envoyer |
| `hist` | les 2 000 mesures des dernières 24 heures | ❌ à ne pas envoyer |
| `cle` | la clé du réseau, « pour que l'autre se connecte » | ❌ à ne pas envoyer |

## Tests

**34 / 34** sur la séquence, **32 / 32** sur le QCM, rejouables : scripts et jeu de réponses
livrés dans le dossier. Voir [`rapport_tests_3e_C7.8.md`](rapport_tests_3e_C7.8.md).

## Fichiers

| Fichier | Contenu |
|---|---|
| [`sequence_3e_C7.8_deux-stations.html`](sequence_3e_C7.8_deux-stations.html) | 6 activités chronométrées, banc intégré |
| [`qcm_3e_C7.8_deux-stations.html`](qcm_3e_C7.8_deux-stations.html) | 30 q · 90 réfutations · 3e_C7.8 ×20, 3e_C8.3 ×10 |
| [`lexique_3e_C7.8.html`](lexique_3e_C7.8.html) | 30 notions, générées depuis le QCM du lot |
| [`synthese_eleve_3e_C7.8.html`](synthese_eleve_3e_C7.8.html) | à imprimer, lisible en noir et blanc |
| [`synthese_professeur_3e_C7.8.html`](synthese_professeur_3e_C7.8.html) | pari didactique, verrous, limites, LSU |
| [`fiche_pedagogique_3e_C7.8.md`](fiche_pedagogique_3e_C7.8.md) | déroulé, message, comportements, différenciation |
| [`matrice_couverture_3e_C7.8.csv`](matrice_couverture_3e_C7.8.csv) | notion → activité → production → questions |
| [`rapport_tests_3e_C7.8.md`](rapport_tests_3e_C7.8.md) | la sortie des deux suites, telle quelle |
