
## 26/09/2026 — n°306, thème 2, vague 5 : seize pages à onglets, la clôture entre dans la dernière séance

**Le relevé, `controle_squelette` sur main à la fusion de #438** : 17 refusées, toutes au thème 2 (C4, C5, C6).
Le geste de la vague 4 s'applique à seize d'entre elles ; **4e_C4.1-C4.2-C4.4 book-train** est laissée à part
(voir plus bas).

**Le geste, identique à la vague 4.** La clôture posée après le dernier panneau (synthèse, bilan, positionnement,
QCM, Bonus — parfois « Évaluation » et « Différenciation », adressées à l'élève, en 4e_C6.2) entre d'un bloc dans
le dernier panneau, Bonus juste avant le bilan. En **3e_C6.1**, le bloc outil « ⌨ Le programme de la station —
CodeLab Techno », posé entre la barre d'onglets et `#s1`, remonte au-dessus de la barre (comme le banc de
3e_C9.2). En **3e_C6.2**, la clôture était déjà dans `#seance3` : seul le Bonus remonte avant le bilan.

**Trois vrais défauts de page trouvés en chemin, corrigés.**
- **3e_C4.1** et **5e_C6.1** : le pied de page s'ouvrait par `<<footer>` — un « < » isolé s'affichait en texte
  sous la page, et le script ne trouvait pas le pied. Corrigé en `<footer>` (un caractère). Aucune autre page du
  dépôt n'a cette coquille.
- **4e_C4.1-C4.9 jardin connecté** : le lien « 🧪 Atelier Pix — Les données du jardin connecté » était collé
  **après** `</html>` ; le navigateur le repêchait en bas de page, visible sous chaque onglet (D5). Il est déplacé
  tel quel dans la séance 4, juste avant le Bonus. Aucune autre page n'a de contenu après `</html>`.

Hors ces trois corrections, lignes triées identiques avant et après sur les seize pages (deux lignes vides en
plus au total, autour des blocs déplacés).

**Aucune réponse décalée.** Aller-retour des sauvegardes dans Chromium à 390 px, servi en HTTP à la même adresse :
**696 / 696** champs repris, 0 faux, 0 erreur, 0 boîte modale, 0 px de débordement ; témoin à 0.

### Vérifié

- `controle_squelette` : quinze des seize pages à **0 défaut** ; dépôt **17 → 2** refusées (jardin connecté en D3,
  book-train en D3, D4, D5 — voir plus bas).
- `verif_regles_audit.py` : **253 → 239** ✘ ; les 14 lignes disparues sont exactement « n°301 le bilan clôt — le Bonus vient
  APRÈS le bilan ». Aucune autre ligne ne change.
- Bancs `tests_controle_squelette` 25 / 25, `tests_verif_regles_audit` 56 / 56.
- Verts : `controle_impression`, `controle_hors_ligne`, `controle_verrous`, `controle_contraste_liens`,
  `controle_boutons_vivants`, `controle_medias`, `controle_liens`, `controle_cadres`, `controle_longueurs`,
  `controle_regle4`, `controle_gestes_outil`, `controle_formulations`.

**Laissé à part, à trancher.**
- **book-train** (4e_C4.1-C4.2-C4.4) : architecture différente (`section.panneau`, onglet d'ouverture `#s0`). Ses
  défauts : D3, D5 (le champ « Nom » de l'en-tête, après la barre de gares) et **D4** — le billet d'entrée est au
  fond de la séance 1, invisible au premier écran. Le remonter dans l'ouverture est un choix pédagogique, pas un
  déplacement de clôture : à décider avec Pascal.
- **jardin connecté** reste en **D3** : dans le bilan, la ligne « Pour aller plus loin » porte un lien « QCM XXL
  réseaux » que le contrôle compte comme un bloc QCM, placé avant l'auto-positionnement. L'ordre des cartes est
  juste (Bonus → Bilan → QCM) ; déplacer ce lien est un choix de rédaction, non fait ici.
