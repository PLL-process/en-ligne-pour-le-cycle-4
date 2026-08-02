# PR (draft) — Lot « Book Train NYPL » (4e)

## 🚃 Contenu du lot
- `sequence_4C4.1-C4.2-C4.4_book-train.html` — séquence 4e complète (titre charte : « Thème 2 · Martinique — 4e · Un Book Train pour la Schœlcher »), page unique hors-ligne, **design aligné jardin connecté** (palette bleu nuit, Poppins, identité, toolbar 💾🖨🗑, barre de progression 6 activités, problématique, parcours 🅰🅱🅲, badges Thème/Socle/Durée/CRCN)
  - 3 séances : Décoder (chaînes info/énergie) → Algorigramme draw.io → Exporter & présenter (Impress)
  - 2 guides logiciels inclusifs (règle candidate n°20) : draw.io A→H (dont bibliothèque de formes) et Impress A→H (dont extensions/Grammalecte), 8 captures SVG reconstituées CC0
  - Fichiers de travail **embarqués** (téléchargement hors-ligne en Blob) ; verrou expérientiel zoom SVG/PNG ; hypothèse↔bilan ; 5 défis bonus dont « L'IA, assistante jamais pilote » (audit 48 V→24 V vécu)
- `fichiers_drawio/` — modèle énergie, chaîne info à compléter + correction, bibliothèque mxlibrary (11 formes), 2 SVG animés des chaînes
- Règles d'or candidates jointes : n°19 (infinitif), n°20 (guide inclusif) + tri-conventions-copilot.md

## ✅ Règles d'or respectées
n°6 (chaînes canoniques, ordre depuis Communiquer, 24 V DC sourcé NYPL 21/09/2016) · n°7 (2 compétences CRCN max : 3.4 + 3.3) · n°18 candidate (algorigramme : boucles au trait vertical, infinitif, correction bloc par bloc) · n°19-20 candidates appliquées

## ⚠️ À câbler avant merge (raison du statut *draft*)
- [x] **Codes compétences séance 1 câblés** : `4C4.1` (constituants chaîne d'énergie — **diagramme fonctionnel** nommé explicitement dans l'activité 1.2), `4C4.2` (transformations et flux), `4C4.4` (constituants chaîne d'information)
- [x] **Arbitrage codes rendu** : `C6.2` réservé au code réel (Python, C++/Arduino, mBlock, Vittascience, Tinkercad…) — l'algorigramme du Book Train reste en périmètre C4. `C4.7-C4.9` (réseaux : IP fixe, communication, simulation — Packet Tracer/Filius) notés pour de futures séquences.
- [x] **Ancrage Martinique restauré — plus aucune dérogation** : nouvelle problématique « Un Book Train pour la bibliothèque Schœlcher » (mécènes + Collectivité → étude du système de référence NYPL) ; Défi 2 promu en suite officielle de la mission (adaptation Schœlcher).
- [x] **Audit qualité (audit_Book_Train.md) intégré** : plan de mission cliquable + bouton retour en haut · compétences en toutes lettres sous chaque activité · consigne 1.1 avec document de référence nommé + rappel dépliable de la mission · distinction magasinier / bibliothécaire du comptoir · pièges en liste lisible · nommage élève `sujet_classe_NOM_Prenom` · **nouvelle activité 1.2 A** (diagramme fonctionnel 2 colonnes, rappel `5C4.1`) placée avant la chaîne d'énergie · 1.2 ter renommée « Complète TA chaîne d'énergie » (le diagramme fonctionnel et la chaîne d'énergie sont deux objets distincts) · frise animée des 4 énergies · progression 9 activités · 5 règles d'or candidates dans `REGLES_OR_CANDIDATES.md`.
- [x] **Modèle énergétique v2 (recherche sourcée)** : ALIMENTER = réseau bâtiment 480 V ~ tri (équivalent US du 400 V tri, via 13,2 kV urbain) + transfo/redresseur/lisseur → bus 24 V ⎓ + alimentations auxiliaires secourues (onduleur) pour automate et capteurs · DISTRIBUER = armoire de puissance (protections, contacteurs, relais, variateur) qui autorise et dose sur ORDRE — flèche d'ordre re-légitimée sur Distribuer. SVG premium, drawio modèle et rappels mis à jour.
- [x] **Activité 1.2 ter (`4C4.1`)** : l'élève REMPLIT son diagramme fonctionnel — nouveau fichier `chaine_energie_a_completer.drawio` (4 blocs vides + réserves fonctions/composants/énergies), checklist 4 étapes auto-vérifiée.
- [x] **Schéma d'ensemble embarqué** avant l'activité 1.1 (JPEG 243 Ko, généré par IA puis vérifié — présenté aux élèves comme document d'étude à auditer, dans l'esprit du Défi 5).
- [x] **Nouvelle activité 1.2 bis (`4C4.2`)** : énergies d'entrée/sortie de chaque bloc + repérage du changement de nature (CONVERTIR) — 7 questions auto-vérifiées · progression totale : 8 activités.
- [ ] `qcm_book-train.html` (30 questions dont 3 illustrées) + 2 synthèses — prochaine session
- [ ] Fiche péda + matrice de couverture
- [ ] `SOURCES_MEDIAS.md` (réponse NYPL en attente — lettre envoyée à press@nypl.org)
- [ ] Photos 2008 remaniées → décommenter le bloc figure du Défi 4
- [ ] Tests réels : rendu navigateur, flowAnimation draw.io, import bibliothèque, menus Impress 7.x FR

## 📍 Emplacement proposé
`theme-2-.../C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.x_book-train/` (même thème que le jardin connecté — à confirmer)
