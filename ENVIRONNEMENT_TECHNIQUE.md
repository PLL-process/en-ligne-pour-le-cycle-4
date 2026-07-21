# 🖥️ Environnement technique de référence — collège (Martinique)

*Synthèse opérationnelle établie le 21 juillet 2026 d'après les informations
fournies par Pascal. Sert de contrat de conception pour toutes les séquences.
Détails ligne par ligne : `inventaire_logiciels.csv`, `inventaire_materiel.csv`,
`matrice_compatibilite_logiciels_materiels.csv`, `INVENTAIRE_PEDAGOGIQUE.md`.*

## 1. Règles de conception qui en découlent

1. Toute séquence matérielle est livrée en **trois versions** : A matériel réel,
   B simulation (VittaScience/Proteus/Filius/Packet Tracer/HTML), C sans matériel.
   Un élève n'est jamais pénalisé par un matériel indisponible.
2. **Cartes distinguées systématiquement** : UNO classique (`arduino:avr:uno`)
   vs UNO R4 Minima (`arduino:renesas_uno:minima`, USB-C). Aucun programme n'est
   déclaré compatible avec une carte sans vérification. mBlock + R4 Minima et
   Proteus + R4 Minima : **non acquis**, repli VittaScience → Arduino IDE →
   simulation HTML.
3. **Très basse tension uniquement** pour les manipulations élèves (Grove, pompes
   TBT) ; jamais de secteur ; consignes de sécurité dans chaque version A.
4. Boutons éventuellement câblés en `INPUT_PULLUP` : logique inversée expliquée
   dans le programme (commenté ligne par ligne en français) et cohérente avec le
   schéma. Brochages historiques (D2 bouton, D3/D5 DEL, D4 entrée, I2C LCD,
   A0-A2 analogique) = point de départ, revérifiés à chaque montage.
5. **Postes potentiellement limités** : ressources HTML légères, chemins relatifs,
   fonctionnement hors connexion raisonnable, pas de compte obligatoire pour
   l'élève, sauvegarde locale uniquement, impression A4 propre, basse résolution
   supportée. Blender/SolidWorks/Proteus : fichiers simplifiés + travail par
   groupe + repli vidéo/visionneuse.
6. **Fichiers d'échange ouverts** : CSV pour les données (+ ods/xlsx), SVG pour
   les schémas, STL pour l'impression 3D, STEP pour la CAO, PDF pour
   l'impression, PNG/WebP optimisés pour les images.
7. Chaque séquence comporte un encadré **« Choix de l'outil »** (outil retenu,
   pourquoi, matériel associé, difficultés prévisibles, alternatives gratuite /
   sans installation / sans matériel).

## 2. Statuts à date (résumé)

- **Confirmés (usage régulier)** : mBlock 5 + mLink, Arduino IDE, Python,
  Sweet Home 3D, Inkscape, GIMP, Filius, LibreOffice, VLC ; matériel : UNO
  classique, UNO R4 Minima, Grove Base Shield V2 + modules listés, mBot2.
- **En ligne** : VittaScience (prioritaire Arduino blocs/simulation), draw.io,
  MIT App Inventor (compte → à arbitrer), Packet Tracer (compte Cisco à vérifier).
- **À vérifier avant toute séquence dépendante** : Proteus 9 (version/licence),
  SolidWorks (licence éducation), Fritzing, XMind, Microsoft 365, puissance des
  postes pour Blender.
- **À confirmer (jamais présumés disponibles)** : imprimante 3D, quantités
  exactes (cartes, mBot2, kits Grove), multimètres, alimentation labo,
  oscilloscopes, fers à souder, matériel réseau physique, VR, découpe laser,
  fraiseuse, consommables 3D. Mention type dans les séquences :
  `MATÉRIEL À CONFIRMER — prévoir une alternative par simulation.`

## 3. Téléchargements et installations

Aucun téléchargement ni installation n'a été effectué lors de l'audit.
Toute opération future sera consignée dans `JOURNAL_INSTALLATIONS.md`
(créé au premier téléchargement réel), selon les règles de sécurité du projet
(sources officielles uniquement, licence et empreinte vérifiées, pas de `sudo`
injustifié, pas de source tierce type MediaFire/Malavida).
