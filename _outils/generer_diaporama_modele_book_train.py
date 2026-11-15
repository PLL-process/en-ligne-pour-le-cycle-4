#!/usr/bin/env python3
"""generer_diaporama_modele_book_train.py — le diaporama modèle de l'activité 4.3 du Book Train (15/11/2026).

Règle d'or n°332 (demande de Pascal du 15/11/2026) : la correction montre la production complète, telle que l'outil la
rend, et donne son fichier. En 4.3, l'élève construit pour la première fois un diaporama de six diapositives dans
LibreOffice Impress, selon un plan imposé : il n'a aucune référence de ce qu'on attend de lui.

CE QUE FAIT L'OUTIL
-------------------
  · écrit la source du modèle, en ODF « à plat » (`_generation/diaporama_modele/book-train_diaporama_modele.fodp`, un
    fichier texte) : six diapositives qui suivent le plan imposé, avec les règles du guide (trois couleurs, une police,
    titres ≥ 32 pt, texte ≥ 24 pt, fond uni identique, transition Fondu partout) ; l'algorigramme corrigé (diapo 4) et
    les deux chaînes complètes (diapo 5) y entrent en SVG, comme le guide le demande à l'élève ;
  · LibreOffice (sans écran) en fait le fichier `fichiers_modeles/book-train_diaporama_modele.odp`, que l'élève
    télécharge et ouvre dans Impress, et un PDF ;
  · le PDF donne la planche des six diapositives (`Images/book-train_diaporama_modele.png`), montrée dans la correction.

Usage : python3 _outils/generer_diaporama_modele_book_train.py             # écrit tout
        python3 _outils/generer_diaporama_modele_book_train.py --verifier  # 0 : la source est à jour et le .odp existe
"""
from html import escape
from pathlib import Path
import base64
import re
import shutil
import subprocess
import sys
import tempfile

RACINE = Path(__file__).resolve().parents[1]
LOT = RACINE / 'theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1_book-train'
SOURCE = LOT / '_generation/diaporama_modele/book-train_diaporama_modele.fodp'
ODP = LOT / 'fichiers_modeles/book-train_diaporama_modele.odp'
PLANCHE = LOT / 'Images/book-train_diaporama_modele.png'

FOND, ENCRE, ACCENT = '#f6f3ec', '#1d3557', '#c45f0a'   # trois couleurs pour tout le diaporama (étape E du guide)
POLICE = 'Liberation Sans'
L, H = 28.0, 15.75   # cm, 16:9

DIAPOS = [
    dict(titre='Un Book Train pour la Schœlcher ?', sous=['Prénom NOM — 4e B'],
         accroche='24 wagonnets, 290 m de rails'),
    dict(titre='Le problème',
         points=['NYPL : les livres dorment sous Bryant Park, le lecteur est au 3ᵉ étage',
                 'Schœlcher : un monument historique, des ouvrages fragiles',
                 'Il faut les livrer vite, à plat, sans choc']),
    dict(titre='La solution technique : le Book Train',
         points=['24 wagonnets électriques sur un rail',
                 '23 m par minute, soit environ 1,4 km/h',
                 'Une nacelle à cardan : le livre reste à plat, même à la verticale']),
    dict(titre='L’algorigramme du trajet', image='algorigramme',
         points=['Il se lit de haut en bas, du DÉBUT à la FIN.',
                 'Chaque losange pose une question : NON fait attendre, OUI fait avancer.']),
    dict(titre='Qui décide, qui exécute ?', image='chaines',
         points=['En haut, l’information décide : capteurs, automate, ordres',
                 'En bas, l’énergie exécute : alimenter, distribuer, convertir, transmettre',
                 'L’ordre descend : il arrive sur DISTRIBUER']),
    dict(titre='Le choix du format',
         points=['SVG : net à n’importe quel zoom, et léger (≈ 14 Ko)',
                 'PNG à 300 % : accepté partout, même sur Pronote',
                 'Le bon format, c’est celui qui convient à la destination']),
]


def _svg(nom):
    """Le dessin à insérer, en SVG (le guide fait insérer le SVG) ; les perles animées des flux sont retirées : une
    diapositive les figerait en pointillés."""
    if nom == 'algorigramme':
        t = (LOT / 'Images/algorigramme_book-train_correction.svg').read_text(encoding='utf-8')
    else:
        t = (LOT / 'Images/chaines_book-train_complete.svg').read_text(encoding='utf-8')
        t = re.sub(r'<style id="flux-anime">.*?</style>', '', t, flags=re.S)
        t = re.sub(r'<(path|line|polyline) class="flux[^"]*"[^>]*/>', '', t)
        t = re.sub(r'\scontent="[^"]*"', '', t, count=1)
    w, h = (float(x) for x in re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', t).groups())
    return base64.b64encode(t.encode('utf-8')).decode('ascii'), w / h


def _cadre_texte(style, x, y, w, h, paragraphes, para='P1'):
    ps = ''.join(f'<text:p text:style-name="{para}">{escape(p)}</text:p>' for p in paragraphes)
    return (f'<draw:frame draw:style-name="{style}" draw:layer="layout" svg:x="{x}cm" svg:y="{y}cm" svg:width="{w}cm" '
            f'svg:height="{h}cm"><draw:text-box>{ps}</draw:text-box></draw:frame>')


def fodp():
    pages = []
    for n, d in enumerate(DIAPOS, 1):
        e = []
        if n == 1:
            e.append(_cadre_texte('gr_cadre', 1.5, 3.4, 25, 3.0, [d['titre']], 'P_titre1'))
            e.append(_cadre_texte('gr_cadre', 1.5, 6.8, 25, 1.4, d['sous'], 'P_sous'))
            e.append(_cadre_texte('gr_accroche', 3.0, 9.6, 22, 2.2, [d['accroche']], 'P_accroche'))
        else:
            e.append(_cadre_texte('gr_cadre', 1.5, 0.8, 25, 2.0, [d['titre']], 'P_titre'))
            e.append(f'<draw:line draw:style-name="gr_filet" svg:x1="1.5cm" svg:y1="2.9cm" svg:x2="6.5cm" svg:y2="2.9cm"/>')
            if d.get('image'):
                donnees, ratio = _svg(d['image'])
                hi = 11.8
                wi = round(hi * ratio, 2)
                e.append(f'<draw:frame draw:style-name="gr_image" svg:x="1.5cm" svg:y="3.4cm" svg:width="{wi}cm" svg:height="{hi}cm">'
                         f'<draw:image><office:binary-data>{donnees}</office:binary-data></draw:image></draw:frame>')
                x = round(1.5 + wi + 1.2, 2)
                e.append(_cadre_texte('gr_cadre', x, 4.2, round(L - x - 1.5, 2), 10, ['• ' + p for p in d['points']], 'P_texte'))
            else:
                e.append(_cadre_texte('gr_cadre', 1.5, 3.8, 25, 10.5, ['• ' + p for p in d['points']], 'P_texte'))
        pages.append(f'<draw:page draw:name="Diapo {n}" draw:style-name="dp1" draw:master-page-name="Standard">' + ''.join(e) + '</draw:page>')
    texte = lambda taille, gras=False, couleur=ENCRE: (
        f'<style:text-properties fo:font-size="{taille}pt" style:font-name="{POLICE}" fo:font-family="{POLICE}" '
        f'fo:color="{couleur}"' + (' fo:font-weight="bold"' if gras else '') + '/>')
    cadre = '<style:graphic-properties draw:stroke="none" draw:fill="none" draw:textarea-vertical-align="top" fo:padding="0.1cm"/>'
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<office:document xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0" xmlns:smil="urn:oasis:names:tc:opendocument:xmlns:smil-compatible:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" office:version="1.3" office:mimetype="application/vnd.oasis.opendocument.presentation">
<office:meta><dc:title>Un Book Train pour la Schœlcher ? — diaporama modèle</dc:title><dc:creator>Séquence « Book Train » — modèle de correction</dc:creator></office:meta>
<office:font-face-decls><style:font-face style:name="{POLICE}" svg:font-family="{POLICE}"/></office:font-face-decls>
<office:automatic-styles>
<style:page-layout style:name="PM1"><style:page-layout-properties fo:margin-top="0cm" fo:margin-bottom="0cm" fo:margin-left="0cm" fo:margin-right="0cm" fo:page-width="{L}cm" fo:page-height="{H}cm" style:print-orientation="landscape"/></style:page-layout>
<style:style style:name="dp1" style:family="drawing-page"><style:drawing-page-properties draw:fill="solid" draw:fill-color="{FOND}" presentation:background-visible="true" presentation:background-objects-visible="true" presentation:transition-speed="medium" smil:type="fade" smil:subtype="crossfade"/></style:style>
<style:style style:name="gr_cadre" style:family="graphic">{cadre}</style:style>
<style:style style:name="gr_accroche" style:family="graphic"><style:graphic-properties draw:stroke="solid" svg:stroke-color="{ACCENT}" svg:stroke-width="0.08cm" draw:fill="none" draw:textarea-vertical-align="middle" fo:padding="0.2cm"/></style:style>
<style:style style:name="gr_filet" style:family="graphic"><style:graphic-properties draw:stroke="solid" svg:stroke-color="{ACCENT}" svg:stroke-width="0.12cm"/></style:style>
<style:style style:name="gr_image" style:family="graphic"><style:graphic-properties draw:stroke="none" draw:fill="none"/></style:style>
<style:style style:name="P_titre1" style:family="paragraph"><style:paragraph-properties fo:text-align="center"/>{texte(40, True)}</style:style>
<style:style style:name="P_sous" style:family="paragraph"><style:paragraph-properties fo:text-align="center"/>{texte(24)}</style:style>
<style:style style:name="P_accroche" style:family="paragraph"><style:paragraph-properties fo:text-align="center"/>{texte(28, True, ACCENT)}</style:style>
<style:style style:name="P_titre" style:family="paragraph">{texte(36, True)}</style:style>
<style:style style:name="P_texte" style:family="paragraph"><style:paragraph-properties fo:margin-bottom="0.45cm"/>{texte(24)}</style:style>
</office:automatic-styles>
<office:master-styles><style:master-page style:name="Standard" style:page-layout-name="PM1" draw:style-name="dp1"/></office:master-styles>
<office:body><office:presentation>
{chr(10).join(pages)}
</office:presentation></office:body>
</office:document>
'''


def construire():
    SOURCE.parent.mkdir(parents=True, exist_ok=True)
    ODP.parent.mkdir(parents=True, exist_ok=True)
    SOURCE.write_text(fodp(), encoding='utf-8')
    with tempfile.TemporaryDirectory() as tmp:
        profil = Path(tmp) / 'profil'
        base = ['soffice', '--headless', f'-env:UserInstallation=file://{profil}']
        for fmt in ('odp', 'pdf'):
            # le premier lancement crée le profil de LibreOffice et peut sortir en erreur sans rien écrire : on relance
            for _ in range(3):
                subprocess.run(base + ['--convert-to', fmt, '--outdir', tmp, str(SOURCE)], capture_output=True, timeout=180)   # --outdir APRÈS --convert-to
                if (Path(tmp) / f'{SOURCE.stem}.{fmt}').exists():
                    break
            else:
                raise SystemExit(f'LibreOffice n’a pas écrit le {fmt}')
        shutil.copy(Path(tmp) / (SOURCE.stem + '.odp'), ODP)
        subprocess.run(['pdftoppm', '-png', '-r', '48', str(Path(tmp) / (SOURCE.stem + '.pdf')), str(Path(tmp) / 'd')], check=True)
        from PIL import Image, ImageDraw
        vues = [Image.open(p).convert('RGB') for p in sorted(Path(tmp).glob('d-*.png'))]
        if len(vues) != len(DIAPOS):
            raise SystemExit(f'{len(vues)} diapositive(s) rendue(s) au lieu de {len(DIAPOS)}')
        w, h = vues[0].size
        marge = 14
        planche = Image.new('RGB', (2 * w + 3 * marge, 3 * h + 4 * marge), '#ffffff')
        trait = ImageDraw.Draw(planche)
        for i, v in enumerate(vues):
            x, y = marge + (i % 2) * (w + marge), marge + (i // 2) * (h + marge)
            planche.paste(v, (x, y))
            trait.rectangle([x - 1, y - 1, x + w, y + h], outline='#9aa5b8')
        planche.save(PLANCHE, optimize=True)
    for f in (SOURCE, ODP, PLANCHE):
        print('✎', f.relative_to(RACINE), f'({f.stat().st_size // 1024} Ko)')


def main(argv):
    if '--verifier' in argv:
        ok = SOURCE.exists() and SOURCE.read_text(encoding='utf-8') == fodp() and ODP.exists() and PLANCHE.exists()
        print('✅ diaporama modèle du Book Train à jour' if ok else '✘ python3 _outils/generer_diaporama_modele_book_train.py')
        return 0 if ok else 1
    construire()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
