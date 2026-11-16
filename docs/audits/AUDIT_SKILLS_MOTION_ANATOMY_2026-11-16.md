# Audit du 16/11/2026 — où servent les skills motion-design, anatomy et anatomy-reveal

Demande de Pascal, 16/11/2026 : « Audit dans quelles séquences tu pourrais utiliser ces skills et utilise-les »,
puis « les mêmes séquences sont prioritaires » : **le thème 1 d'abord** (C1 dans l'ordre, puis C2, puis C3) ;
les thèmes 2 et 3 sont relevés ici pour plus tard.

Les trois skills sont ceux que Pascal a installés le 16/11 (sources auditées et épinglées : LottieFiles
`f9a8a04`, Anatomy `1482e84`, Anatomy Reveal `dd01e1c`). La veille du même jour (PR #741) a déjà versé
motion-design dans les skills du dépôt et mesuré le mouvement (`_outils/controle_mouvement.py`) : cet audit
s'appuie sur cette mesure au lieu de la refaire.

**Règles d'or tenues pour juger** : n°1 (une image n'est jamais décorative), n°85 (l'élève voit l'objet avant
son nom), n°119 (jamais l'animation seule), n°174 à 177 (une animation ne se justifie que si son sujet change
dans le temps ; celle que l'élève déclenche est un instrument ; l'état final est l'image complète ; elle ne montre
pas la réponse), n°179 (une ressource hors du dépôt a son repli), n°182 (la vidéo montre un fonctionnement, le
schéma compare), n°102 (impression claire).

**Périmètre** : les 60 pages de séquence des trois thèmes (dossiers mutualisés compris), lues par mots-clés
(composants, pièces, matériaux, vues éclatées, images, animations), puis les pages du thème 1 ouvertes une à une.

## 1. motion-design — le mouvement des animations

| Où | Constat | Ce qui est fait |
|---|---|---|
| Lecteur pas à pas commun (`_outils/lecteur_pas_a_pas/`) — 6 animations : Herschel 3e_C1.1, trois principes 5e_C1.1, vélo-cargo 5e_C3.1, lampadaire 5e_C4.1, jardin 4e_C8.1 et 4e_C9.1 | Une partie du dessin apparaissait par un fondu seul de 0,35 s, courbe `ease` dans les deux sens. Le skill demande : ni opacité seule, ce qui entre ralentit, ce qui sort accélère, une étape de schéma de 0,6 à 1,2 s. | ✅ **Fait dans ce lot** : apparition en 0,6 s avec une montée de 6 unités (courbe qui décélère), disparition en 0,4 s (courbe qui accélère), rien ne bouge sous « moins de mouvement ». Banc commun vert. |
| Relais animé (4e_C7.4, 7.5, 9.1, 6.1) | Déjà conforme : l'aimant ferme la lame en accélérant, le ressort la relève en ralentissant, mouvement réduit respecté. | Rien. |
| Thème 1, mesure de la PR #741 | M1 : le terminal de `4e_C1.4/activite-bonus-cyber-immersive-2fa.html` n'avait pas de repli. M2 : boucles sans bouton d'arrêt dans 5e_C1.5 (`vsPulse`) et 5e_C3.1 (`flux-avance`, `vppLueur`). | Fait à part par la PR #743 (carte blanche du 16/11) : bouton « ⏸️ Figer les animations », pulsations qui s'arrêtent seules, replis posés ; M1 et M2 à 0 sur `main`. Rien de plus ici. |

## 2. anatomy — l'objet réel en figure isométrique

Une figure Anatomy **montre l'objet** ; elle ne remplace pas un schéma du programme (chaîne d'énergie,
pieuvre, bête à cornes). Elle sert là où l'élève doit **voir, nommer ou comparer des pièces** et où la page ne
lui montre pas l'objet.

### Thème 1 (prioritaire)

| Séquence | Objet | Besoin | Verdict |
|---|---|---|---|
| **5e_C1.2** Sainte-Luce, quel frein ? | patins, disque, tambour | L'activité 1 demande ce qui bouge, ce qui frotte et à quelle distance de l'axe ; la version 🅱 renvoie à « un schéma coté » qui n'existait pas ; les trois vidéos sont hors du dépôt (n°179). | ✅ **Fait** : « Trois freins, la même roue » (ci-dessous). |
| 4e_C3.1 Hangzhou, quelle flotte de vélos ? | vélo en libre-service robuste | Choisir entre solutions par critères ; une photo montre le vélo. | Possible plus tard : vue éclatée des pièces anti-vandalisme. À juger par Pascal. |
| 3e_C3.1 Shenzhen, refroidir un local | climatiseur, ventilation | Trois familles de solutions présentées par un tableau. | Possible : l'unité extérieure et intérieure d'un climatiseur (n°85). À juger. |
| 5e_C1.1 Chengdu, capteur de particules | le capteur de la cour | Une photo et l'animation des trois principes de mesure. | Non : l'animation dit déjà comment il mesure. |
| 5e_C3.1 Shanghai, vélo-cargo | vélo-cargo | A déjà sa figure isométrique dans le lecteur. | Non. |
| 3e_C1.1, 4e_C1.1 Tsinghua (feux) ; 3e_C2.1, 4e_C2.1, 5e_C2.1 (bornes, station) | drone, borne, station | Photos et schémas présents ; la compétence porte sur les usages et les représentations. | Non. |
| 3e_C1.5, 4e_C1.4, 5e_C1.3, 5e_C1.5 | numérique, données | Pas d'objet physique à décrire. | Non. |

### Thèmes 2 et 3 (plus tard)

| Objet | Séquences | Pourquoi |
|---|---|---|
| **La station d'alerte cyclonique** (mât, coffret, panneau, batterie, sirène) | 3e_C4.1, C4.3, C5.1, C6, C7.3 à C7.8, C8.1, C8.2, C9.2 | Douze séquences de 3e et **aucune image de la station** : l'élève ne voit jamais l'objet (n°85). Le plus utile pour le niveau que Pascal a le plus cette année. |
| Le lampadaire de la cour | 5e_C4.1, C5.1, C6.1 | Pilote de la veille (#741), à refaire selon le skill puis verser : prévu par la veille. |
| Le banc de la cour, la patère du hall | 5e_C7.3, 5e_C8.1, C8.2 | Assemblages de pièces et de matériaux : la vue éclatée est le bon outil. |
| Le jardin connecté (bac, support du capteur) | 4e_C4.1, C5.1, C7.3, C7.7 | Pièces nombreuses, une seule image dans les pages. |

## 3. anatomy-reveal — le film de démontage

| Question | Réponse |
|---|---|
| Ce que fait le film | L'objet arrive, gros plans, une fonction en marche, éclatement, remontage ; 10 s par défaut, au format des réseaux sociaux. |
| n°175 | Un film qui se déroule seul est un spectacle ; la figure Anatomy, que l'élève manipule, est l'instrument. |
| n°182 | La vidéo est faite pour montrer un fonctionnement : en 5e_C1.2, les vidéos d'Alain Le Berre le font mieux, avec un vrai vélo. Un film « produit » ne compare pas trois freins ; la figure, si. |
| Thème 1 | **Aucune séquence** où le film apporte plus que la figure, sans enfreindre n°174-175. |
| Où il aurait un sens | Une situation déclenchante dont l'objet n'a aucune image (n°85) : la station d'alerte de 3e. Le film montrerait l'objet, sans mots, lancé par l'élève. |
| Coût | 2 à 4 h de modélisation par objet, environ 2 min de rendu par seconde de film ; il demande ImageMagick 7, absent de l'espace de travail (version 6 seulement). |

**Pas utilisé dans ce lot**, faute d'une séquence du thème 1 qui le justifie. Décision proposée à Pascal :
l'essayer sur la station d'alerte, quand le thème 2 viendra.

## 4. Le pilote livré : « Trois freins, la même roue » (5e_C1.2)

- **L'objet** : la roue avant d'un vélo du collège (26 pouces), posée dans un range-vélo, avec au choix un frein
  à patins, à disque ou à tambour. Mêmes roue, fourche et levier : seul le frein change.
- **L'instrument** : l'élève serre le levier (bouton, toucher ou Espace) ; le levier tourne, puis les pièces qui
  frottent viennent toucher. Un trait s'allume de l'axe jusqu'à l'endroit qui frotte, et la ligne du bas dit la
  distance (28,5 cm, 7 cm, 3,5 cm). Rien ne bouge sans un geste de l'élève (n°175).
- **La loupe** : une coupe à plat de l'endroit qui frotte (la jante entre les patins, le disque dans l'étrier, les
  mâchoires dans le tambour, flasque ôtée), parce que les écarts vrais (2 mm, moins d'1 mm, 1 mm) ne se voient
  pas à l'échelle de la roue.
- **Les cotes** sont vraies et écrites dans le générateur : roue ETRTO 559, disque Ø 160 mm, tambour Ø 70 mm,
  écart patin-jante 2 mm (celui du relevé de la séquence).
- **Ce qu'elle ne fait pas** : elle ne nomme pas les deux pièces qui se touchent et ne dit pas où apparaît la
  chaleur. C'est le relevé que l'élève écrit (n°177).
- **Impression** : thème clair, les trois freins côte à côte, la légende en trois colonnes (n°102, n°176).
- **Mouvement** : levier τ 0,12 s à l'aller, 0,09 s au retour (le ressort), métal rigide sans rebond ;
  « moins de mouvement » : l'état final tout de suite.
- **Fichiers** : `5e_C1.2/_generation/freins_iso/build.mjs` (le générateur ; le kit n'est pas versé dans le
  dépôt), `Images/freins_iso.html` (la figure, posée dans la page par un cadre), `Images/freins_iso_planche.svg`
  (planche fixe claire, pour une synthèse ou une fiche).
