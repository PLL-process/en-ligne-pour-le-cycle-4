# -*- coding: utf-8 -*-
"""Insère les captures des gestes dans l'encart « Avant de commencer » de 4e_C1.1.
Ne touche à aucun mot des <li> : chaque <figure> est ajoutée juste avant le </li>."""
import re, sys, html
P = sys.argv[1]
t = open(P, encoding='utf-8').read()

def fig(src, w, h, alt, cap):
    return ('\n      <figure class="geste-capture">\n'
            f'        <img src="Images/{src}" width="{w}" height="{h}" loading="lazy"\n'
            f'             alt="{alt}">\n'
            f'        <figcaption>{cap}</figcaption>\n'
            '      </figure>\n    ')

F = {
 'Ouvrir': [
  fig('geste_tableur_1_ouvrir_import_csv.png', 1400, 774,
      "Boîte de dialogue « Import de texte » de LibreOffice Calc, en français, pour le fichier donnees_feux_impacts_4e.csv. En haut : Jeu de caractères, Locale « Par défaut - Français (France) », À partir de la ligne 1. Dans « Options de séparateur », le bouton « Séparé par » est sélectionné ; parmi les cases Tabulation, Virgule, Point-virgule, Espace et Autre, seule Point-virgule est cochée. En bas, l'aperçu montre les données réparties en colonnes : type_donnee, date, territoire, indicateur, valeur, unite, source, statut. Les boutons OK et Annuler sont en bas à droite.",
      "<b>Ce que tu dois voir&nbsp;:</b> dans «&nbsp;Options de séparateur&nbsp;», la case <b>Point-virgule</b> cochée, et l'aperçu du bas déjà découpé en colonnes. Si c'est «&nbsp;Détecté (;)&nbsp;» qui est sélectionné, c'est bon aussi&nbsp;: le (;) dit que le point-virgule a été reconnu. <b>Puis&nbsp;:</b> clique <b>OK</b>. <i>Le nom de fichier de la barre de titre est celui de la consigne.</i>"),
  fig('geste_tableur_1b_ouvrir_resultat.png', 1400, 876,
      "Fenêtre de LibreOffice Calc, en français, dont la barre de titre indique donnees_feux_impacts_4e.csv. La feuille montre huit colonnes, de A à H : type_donnee, date, territoire, indicateur, valeur, unite, source, statut, et dix lignes de données, chaque donnée dans sa propre cellule.",
      "<b>Comment savoir que c'est fait&nbsp;:</b> chaque donnée est dans sa propre colonne, de A à H, avec les titres sur la ligne 1. <i>Les valeurs visibles sont celles du fichier de la consigne.</i>"),
  fig('geste_tableur_1c_ouvrir_erreur_separateur.png', 1400, 876,
      "La même fenêtre de LibreOffice Calc, mais chaque ligne de données est écrite en entier dans la seule colonne A, avec ses points-virgules ; les colonnes B à H sont vides.",
      "<b>Si tu vois ceci&nbsp;:</b> tout est collé dans la colonne A, points-virgules compris — le séparateur n'était pas le bon. Ferme le fichier sans l'enregistrer (<b>Fichier → Fermer</b>), recommence <b>Fichier → Ouvrir…</b> et coche <b>Point-virgule</b>."),
 ],
 'Nommer': [
  fig('geste_tableur_2_nommer_enregistrer_sous.png', 1400, 728,
      "Boîte de dialogue « Enregistrer sous » de LibreOffice Calc, en français. En haut, le dossier de destination. En bas, le champ « Nom de fichier » contient 4E-FEUX-DUPONT, et le champ « Type de fichier » affiche « Classeur ODF (.ods) », surligné. La case « Extension automatique du nom de fichier » est cochée. À droite, les boutons Enregistrer, Annuler et Aide.",
      "<b>Ce que tu dois voir&nbsp;:</b> <b>Type de fichier&nbsp;: Classeur ODF (.ods)</b> — si tu lis encore «&nbsp;Texte CSV (.csv)&nbsp;», ouvre la liste et choisis Classeur ODF. Le <b>Nom de fichier</b> suit la consigne. <b>Puis&nbsp;:</b> <b>Enregistrer</b>. <i>DUPONT est un exemple&nbsp;: mets ton nom. Le dossier affiché est celui du poste où la capture a été prise&nbsp;; le tien est ton dossier personnel.</i>"),
  fig('geste_tableur_2b_nommer_resultat.png', 1400, 876,
      "Fenêtre de LibreOffice Calc dont la barre de titre indique désormais 4E-FEUX-DUPONT.ods — LibreOffice Calc. La feuille de données est inchangée.",
      "<b>Comment savoir que c'est fait&nbsp;:</b> la barre de titre, tout en haut, affiche ton nom de fichier suivi de <b>.ods</b>, et non plus .csv. <i>DUPONT est un exemple.</i>"),
 ],
 'Retrouver': [
  fig('geste_tableur_3_retrouver_avant_ctrl_s.png', 1400, 857,
      "Fenêtre de LibreOffice Calc, fichier 4E-FEUX-DUPONT.ods. Une cellule vient d'être modifiée : « total » a été tapé en A11. En bas à gauche, dans la barre d'état, l'icône du document est rouge, ce qui signale des modifications non enregistrées ; dans la barre d'outils, l'icône Enregistrer porte un point rouge.",
      "<b>Ce que tu dois voir avant Ctrl+S&nbsp;:</b> tu as tapé quelque chose (ici «&nbsp;total&nbsp;» en A11, un exemple), et en bas à gauche de la fenêtre, la petite icône de la barre d'état est <b>rouge</b>&nbsp;: ce qui est à l'écran n'est pas encore sur le disque. Le raccourci n'ouvre aucune fenêtre&nbsp;: c'est cette icône qui te répond."),
  fig('geste_tableur_3b_retrouver_apres_ctrl_s.png', 1400, 857,
      "La même fenêtre après Ctrl+S : l'icône de la barre d'état, en bas à gauche, est redevenue grise, et l'icône Enregistrer de la barre d'outils n'a plus de point rouge.",
      "<b>Comment savoir que c'est fait&nbsp;:</b> après <kbd>Ctrl</kbd>+<kbd>S</kbd>, l'icône en bas à gauche redevient <b>grise</b>. Rien d'autre ne change à l'écran&nbsp;: c'est normal."),
  fig('geste_tableur_3c_retrouver_rouvrir.png', 1400, 732,
      "Boîte de dialogue « Ouvrir » de LibreOffice Calc, dans le dossier de travail. La liste montre deux fichiers : 4E-FEUX-DUPONT.ods, sélectionné, de type Feuille de calcul, et donnees_feux_impacts_4e.csv. Le champ « Nom de fichier » contient 4E-FEUX-DUPONT.ods. Le bouton Ouvrir est à droite.",
      "<b>Pour rouvrir à la séance suivante&nbsp;:</b> <b>Fichier → Ouvrir…</b>, va dans ton dossier personnel et choisis le fichier qui finit par <b>.ods</b> — pas le .csv, qui est le fichier de départ, sans ton travail. <i>Le nom et le dossier sont des exemples.</i>"),
 ],
 'Sortir': [
  fig('geste_tableur_4_sortir_clic_droit_graphique.png', 1400, 1172,
      "Fenêtre de LibreOffice Calc avec un diagramme en colonnes posé sur la feuille et sélectionné (huit petits carrés autour). Un menu contextuel est ouvert sur le diagramme : Couper, Copier, Coller, Position et taille, Ancre, Positionner, Nom, Texte alternatif, Assigner la macro, Exporter comme image, Éditer.",
      "<b>Ce que tu dois voir&nbsp;:</b> un <b>clic</b> sur le graphique (des petits carrés apparaissent autour), puis un <b>clic droit</b>&nbsp;: le menu propose <b>Copier</b> (pour le coller dans le compte rendu) et <b>Exporter comme image</b>. <i>Le graphique montré est un exemple.</i>"),
  fig('geste_tableur_4b_sortir_enregistrer_image.png', 1400, 732,
      "Boîte de dialogue « Enregistrer en tant qu'image » de LibreOffice Calc. Le champ « Nom de fichier » contient graphique-4E-FEUX-DUPONT ; « Type de fichier » affiche PNG - Portable Network Graphics ; la case « Extension automatique du nom de fichier » est cochée. Le bouton Enregistrer est à droite.",
      "<b>Comment savoir que c'est fait&nbsp;:</b> après <b>Exporter comme image</b>, cette boîte s'ouvre&nbsp;; garde le type <b>PNG</b>, donne un nom, <b>Enregistrer</b>. Le fichier image apparaît dans ton dossier, à côté du classeur. <i>Le nom est un exemple.</i>"),
 ],
}

m = re.search(r'<section class="card gestes-outil".*?</section>', t, re.S)
enc = m.group(0)
new = enc
# 1. le titre
old_h2 = '🧰 Avant de commencer — les quatre gestes du tableur'
assert new.count(old_h2) == 1
new = new.replace(old_h2, '🧰 Avant de commencer (échauffement) — les quatre gestes du tableur')
# 2. une figure par geste, avant le </li>
for geste, figs in F.items():
    pat = re.compile(r'(<li><b>' + geste + r'\.</b>.*?)(</li>)', re.S)
    assert len(pat.findall(new)) == 1, geste
    new = pat.sub(lambda mm: mm.group(1) + ''.join(figs) + mm.group(2), new, count=1)
t = t.replace(enc, new)

# 3. le CSS, dans le bloc de style de l'encart
css_old = '  .gestes-outil li b:first-child{color:#ffb300}\n'
assert t.count(css_old) == 1
css_new = css_old + (
 '  .gestes-outil figure.geste-capture{margin:.6rem 0 .9rem;max-width:560px}\n'
 '  .gestes-outil figure.geste-capture img{width:100%;height:auto;display:block;border:1px solid var(--border,#2a3550);\n'
 '    border-radius:8px;background:#fff}\n'
 '  .gestes-outil figure.geste-capture figcaption{margin:.35rem 0 0;font-size:.88em;line-height:1.45;opacity:.92}\n'
 '  .gestes-outil figure.geste-capture figcaption b{color:inherit}\n'
 '  @media print{.gestes-outil figure.geste-capture{break-inside:avoid;page-break-inside:avoid}\n'
 '    .gestes-outil figure.geste-capture img{border-color:#999}}\n')
t = t.replace(css_old, css_new)
open(P, 'w', encoding='utf-8', newline='').write(t)
print("ok", sum(len(v) for v in F.values()), "figures")
