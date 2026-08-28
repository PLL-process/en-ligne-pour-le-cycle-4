# 4e_C4.7 — Paramétrer une adresse IP fixe pour ajouter un objet connecté à un réseau local

✅ **Compétence couverte par un lot complet dédié** (atelier réseau, mutualisé C4.7 · C4.8 · C4.9),
en complément de la séance 3 du « Jardin connecté ».

## 🥬 Atelier « SOS serre : l'objet connecté muet » (ce dossier)

➡ **[Séquence complète](sequence_4e_C4.7-C4.9_sos_serre_packet_tracer.html)** — **4 séances de 55 min** :
passeport réseau d'entrée, conception de SON plan d'adressage (règle n°22), adresse fixe passerelle comprise
prouvée au ping, clinique du réseau et **intervention réelle sur trois fichiers en panne**, validation par
simulation et **défi sans tutoriel** (Packet Tracer 8.2, valeurs réellement mesurées). Un **mode essentiel**
allège la page pour les élèves qui en ont besoin.
➡ **[QCM d'entraînement](qcm_4e_C4.7-C4.9_sos_serre.html)** — 30 questions (10 par code), 7 illustrées.
➡ Synthèses : [élève](Synthèses/synthese_eleve_4e_C4.7-C4.9.html) · [professeur](Synthèses/synthese_professeur_4e_C4.7-C4.9.html)
➡ [Fiche pédagogique](fiche_pedagogique_4e_C4.7-C4.9.md) · [Matrice de couverture](matrice_couverture_4e_C4.7-C4.9.csv) · [Rapport de tests](rapport_tests_4e_C4.7-C4.9.md)
### 📦 Les cinq fichiers Packet Tracer du lot

| Fichier | À quoi il sert |
|---|---|
| [`4e_serre_DEPART.pkt`](4e_serre_DEPART.pkt) | montage **câblé, adresses vides** — l'élève n'a qu'à adresser et prouver |
| [`4e_serre_TECHNO-C4.pkt`](4e_serre_TECHNO-C4.pkt) | montage **maître** tout adressé, pings validés (contrat 4e_C4.9) |
| [`4e_serre_PANNE_A.pkt`](4e_serre_PANNE_A.pkt) | panne **adressage** : capteur en 192.168.21.50 (100% loss vérifié) |
| [`4e_serre_PANNE_B.pkt`](4e_serre_PANNE_B.pkt) | panne **liaison** : Port Status de l'imprimante sur Off (triangle rouge) |
| [`4e_serre_PANNE_C.pkt`](4e_serre_PANNE_C.pkt) | panne **masque** : capteur en 255.255.255.240 (100% loss vérifié) |

Les trois pannes sont documentées, avec leur remède, dans la **synthèse professeur** uniquement.

## 🌱 Le même code dans la séquence-îlot (version courte)

➡ [« Le jardin connecté »](../4e_C4.1/sequence_4e_C4.1-C4.9_jardin_connecte.html) — séance 3 :
adresse IP fixe de la carte du jardin · [QCM îlot](../4e_C4.1/qcm_4e_C4.1-C4.9_jardin_connecte.html) (questions RES).

## 🧰 Ressource complémentaire déjà présente dans ce dossier

### 🧠 Les trois QCM « réseaux » (ex-« XXL 40 »)

Le fichier hérité posait 51 questions d'un seul tenant, sur trois sujets sans
rapport entre eux, et onze d'entre elles n'avaient que **deux** propositions —
autant dire pile ou face. Il est scindé en **trois QCM de trente questions**,
chacun à quatre propositions, avec une réfutation par distracteur :

| QCM | Ce qu'il travaille |
|---|---|
| [Réseau local et matériels](qcm_xxl_40_reseaux_ip_nfc_rfid_zigbee.html) | LAN et WLAN · hub, switch, routeur : qui fait quoi · choisir et raisonner |
| [Adresser et identifier](qcm_4e_C4.7_adressage_ip.html) | l'adresse IP · DHCP, MAC, DNS · conflits et diagnostic |
| [Zigbee et les liaisons sans fil](qcm_4e_C4.7_zigbee_domotique.html) | Zigbee · les trois rôles du maillage · comparer NFC, RFID, Bluetooth, Wi-Fi |

Le premier **garde le chemin du fichier d'origine** : tous les liens du site
continuent de fonctionner, et mènent désormais à un vrai QCM plutôt qu'à un
fourre-tout.

*Atelier réseau 4e — Thème 2 · objet-fil « Le jardin connecté » (la serre du jardin).*
