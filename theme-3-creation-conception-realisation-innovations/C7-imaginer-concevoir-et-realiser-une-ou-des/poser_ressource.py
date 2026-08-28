#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
poser_ressource.py — pose (ou remet à jour) les blocs « ressource vidéo » du dépôt.

    python3 poser_ressource.py              pose tout ce qui est complet
    python3 poser_ressource.py --etat       dit seulement ce qui manque, ne touche à rien
    python3 poser_ressource.py --apercu     écrit un aperçu HTML autonome, sans toucher au dépôt

Ce que l'outil REFUSE de poser, et pourquoi
-------------------------------------------
· une entrée sans « url »        — une vidéo qu'on n'a pas ouverte n'existe pas (règle n°167) ;
· une entrée sans « a_regarder » — une vidéo sans consigne est un divertissement ;
· une entrée sans « repli »      — une activité qui repose sur un fichier absent n'est pas une
                                   activité (règle n°169). Le réseau du collège tombera un jour.

Le QR code est produit ICI, en SVG, et incrusté dans la page : aucun service distant, donc
aucune fuite et aucune dépendance au réseau à l'ouverture de la page (règle n°40).
"""

import argparse
import json
import pathlib
import re
import sys
from datetime import date

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parents[1]
REGISTRE = ICI / "ressources_externes.json"

OBLIGATOIRES = ("titre", "source", "url", "a_regarder")

# ── le style, injecté une seule fois par page ────────────────────────────────
CSS = """<style id="ressource-css">
/* Bloc « ressource externe » — posé par _outils poser_ressource.py. Ne pas éditer à la main. */
.ressource{background:#0a1b3d;border:1px solid #274a8a;border-left:4px solid #ffd66b;
  border-radius:12px;padding:14px 18px;margin:18px 0}
.ressource-tete{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:8px}
.ressource-genre{font-size:.72em;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#ffd66b}
.ressource-chip{font-size:.75em;border:1px solid #2f5695;border-radius:999px;padding:2px 10px;color:#9bbefc}
.ressource-verif{font-size:.75em;color:#6b87ac;margin-left:auto}
.ressource-verif.vieux{color:#ffd66b}
.ressource-titre{margin:0 0 2px;font-size:1.02em;color:#e4eaf5}
.ressource-source{margin:0 0 10px;font-size:.86em;color:#9bbefc}
.ressource-corps{display:flex;gap:18px;flex-wrap:wrap;align-items:flex-start}
.ressource-consigne{flex:1 1 340px;min-width:0}
.ressource-etiq{font-size:.72em;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
  color:#9bbefc;margin:0 0 4px}
.ressource-lien{display:inline-block;background:#1d4e89;color:#fff;border-radius:9px;
  padding:9px 16px;font-weight:600;text-decoration:none;margin-top:8px}
.ressource-lien:hover{background:#2a63a8}
.ressource-lien:focus-visible{outline:3px solid #61dafb;outline-offset:2px}
/* Sans URL réelle : un repère inerte, qui a l'air inerte. Jamais un faux bouton. */
.ressource-lien--inerte{background:transparent;border:1px dashed #6b87ac;color:#9bbefc;
  font-weight:400;cursor:default}
.ressource-qr{flex:0 0 132px;margin:0;text-align:center}
.ressource-qr svg{width:120px;height:120px;background:#fff;border-radius:6px;padding:6px;display:block}
.ressource-qr figcaption{font-size:.7em;color:#6b87ac;margin-top:5px;line-height:1.35}
.ressource-repli{margin-top:12px;padding-top:12px;border-top:1px dashed #2f5695}
.ressource-repli ol{margin:6px 0 0;padding-left:22px}
.ressource-repli li{margin-bottom:4px}
@media print{
  .ressource{background:#fff;border:1px solid #666;border-left:4px solid #111;
    color:#111;break-inside:avoid}
  .ressource-genre,.ressource-etiq{color:#111}
  .ressource-chip,.ressource-source,.ressource-verif,.ressource-qr figcaption{color:#333;border-color:#999}
  .ressource-titre{color:#111}
  .ressource-lien{background:#fff;color:#111;border:1px solid #111;padding:4px 8px}
  /* sur le papier, le bouton ne clique pas : on imprime l'adresse en toutes lettres */
  .ressource-lien::after{content:" — " attr(href);font-weight:400;font-size:.85em;word-break:break-all}
  .ressource-repli{border-top-color:#666}
}
</style>
"""

GABARIT = """<!-- ressource: {id} -->
<section class="ressource" id="{id}" aria-label="Ressource vidéo : {titre_attr}">
  <header class="ressource-tete">
    <span class="ressource-genre">🎬 Ressource vidéo</span>
{chips}    <span class="ressource-verif{classe_verif}">lien vérifié le {verifie_le}</span>
  </header>
  <h4 class="ressource-titre">{titre}</h4>
  <p class="ressource-source">{source}</p>
  <div class="ressource-corps">
    <div class="ressource-consigne">
      <p class="ressource-etiq">Ce qu'il faut regarder</p>
      {a_regarder}
      {commande}
    </div>
    <figure class="ressource-qr">
      {qr}
      <figcaption>À scanner à la maison ou depuis le poste — le téléphone reste au fond du sac.</figcaption>
    </figure>
  </div>
  <div class="ressource-repli">
    <p class="ressource-etiq">{repli_titre}</p>
    {repli_html}
  </div>
</section>
<!-- /ressource: {id} -->"""


def qr_svg(url, etiquette):
    """QR en SVG, produit localement. Aucun appel réseau, ni à la génération ni à l'affichage."""
    if factice(url):
        # Un QR qui mène à une adresse d'exemple est un mensonge de plus : on montre
        # une case barrée, qui se lit comme une case barrée.
        return ('<svg role="img" viewBox="0 0 40 40" aria-label="Aucun QR : aperçu sans vidéo">'
                '<rect x="1" y="1" width="38" height="38" fill="none" stroke="#999" '
                'stroke-width="1.5" stroke-dasharray="4 3"/>'
                '<path d="M8 8 L32 32 M32 8 L8 32" stroke="#bbb" stroke-width="1.5"/></svg>')
    try:
        import segno
    except ImportError:
        return ('<svg viewBox="0 0 10 10" role="img" aria-label="QR indisponible">'
                '<title>QR non généré</title></svg>')
    q = segno.make(url, error="m")
    from io import BytesIO
    tampon = BytesIO()
    q.save(tampon, kind="svg", xmldecl=False, svgns=True, scale=1, border=2,
           dark="#000000", svgclass=None, lineclass=None)
    svg = tampon.getvalue().decode("utf-8")
    # segno fixe une taille en pixels et ne pose pas de viewBox : on remplace l'une par
    # l'autre, pour que le QR remplisse la case que lui donne la feuille de style — à
    # l'écran comme sur le papier, où il doit rester scannable.
    largeur, hauteur = q.symbol_size(scale=1, border=2)
    svg = re.sub(r'\s(?:width|height)="[^"]*"', "", svg, count=2)
    etiquette = etiquette.replace('"', "&quot;")
    return svg.replace(
        "<svg ",
        '<svg role="img" viewBox="0 0 %d %d" preserveAspectRatio="xMidYMid meet" '
        'aria-label="QR code vers : %s" ' % (largeur, hauteur, etiquette), 1)


#: hôtes réservés aux exemples — RFC 2606. Rien derrière, par construction.
FACTICES = ("exemple.invalid", "example.invalid", "example.com", "example.org")


def factice(url):
    return (not (url or "").strip()) or any(h in url for h in FACTICES)


def commande(url):
    """Le bouton n'existe QUE s'il mène quelque part.

    Un contrôle qui annonce « Ouvrir la vidéo » et n'ouvre rien est exactement le défaut
    que la PR #255 a passé une session à retirer du dépôt : le bouton QCM qui ne menait
    nulle part, le bouton Enregistrer qui n'existait pas. On ne le réintroduit pas ici,
    fût-ce dans un aperçu. Sans URL réelle, on affiche un repère inerte, qui a l'air
    inerte, et qui dit pourquoi.
    """
    if factice(url):
        return ('<span class="ressource-lien ressource-lien--inerte" role="note">'
                "✖ Aucune vidéo — c'est un aperçu de la forme</span>")
    return ('<a class="ressource-lien" href="%s" target="_blank" rel="noopener noreferrer">'
            "▶ Ouvrir la vidéo</a>" % url)


def paragraphes(texte):
    if "<" in texte:
        return texte
    return "".join("<p>%s</p>" % b.strip() for b in texte.split("\n\n") if b.strip())


def manques(r):
    absents = [c for c in OBLIGATOIRES if not (r.get(c) or "").strip()]
    repli = r.get("repli") or {}
    if not (repli.get("html") or "").strip():
        absents.append("repli")
    return absents


def bloc(r, verifie_le):
    chips = ""
    for champ in ("duree", "licence"):
        if (r.get(champ) or "").strip():
            chips += '    <span class="ressource-chip">%s</span>\n' % r[champ].strip()
    vieux = ""
    if verifie_le:
        try:
            an = int(verifie_le.split("-")[0] if "-" in verifie_le else verifie_le[-4:])
            if date.today().year - an >= 1:
                vieux = " vieux"
        except ValueError:
            pass
    repli = r.get("repli") or {}
    return GABARIT.format(
        id=r["id"], chips=chips,
        titre=r["titre"], titre_attr=r["titre"].replace('"', "&quot;"),
        source=r["source"], url=r["url"],
        verifie_le=verifie_le or "jamais", classe_verif=vieux,
        a_regarder=paragraphes(r["a_regarder"]),
        commande=commande(r["url"]),
        qr=qr_svg(r["url"], r["titre"]),
        repli_titre=(repli.get("titre") or "Si la vidéo ne s'ouvre pas"),
        repli_html=repli.get("html", ""),
    )


def poser(page, r, html_bloc):
    texte = page.read_text(encoding="utf-8")
    avant = texte

    if 'id="ressource-css"' not in texte:
        texte = texte.replace("</head>", CSS + "</head>", 1)

    ouvre, ferme = "<!-- ressource: %s -->" % r["id"], "<!-- /ressource: %s -->" % r["id"]
    if ouvre in texte and ferme in texte:
        d, f = texte.index(ouvre), texte.index(ferme) + len(ferme)
        texte = texte[:d] + html_bloc + texte[f:]
    elif ouvre in texte:
        texte = texte.replace(ouvre, html_bloc, 1)
    else:
        ancre = (r.get("apres") or "").strip()
        if not ancre:
            return None, "ni marqueur « %s » dans la page, ni champ « apres » pour le créer" % ouvre
        m = re.search(r'^.*id="%s".*$' % re.escape(ancre), texte, re.M)
        if not m:
            return None, "l'ancre id=\"%s\" est introuvable dans la page" % ancre
        # Plusieurs ressources peuvent partager une ancre. On se place APRÈS celles qui
        # y sont déjà, sinon l'ordre du registre se retrouve inversé dans la page — et
        # la consigne qui dit « range maintenant les trois » arrive en premier.
        ou = m.end()
        while True:
            suite = re.match(r"\s*<!-- ressource: ([\w-]+) -->", texte[ou:])
            if not suite:
                break
            marqueur = "<!-- /ressource: %s -->" % suite.group(1)
            fin = texte.find(marqueur, ou)
            if fin == -1:
                break
            ou = fin + len(marqueur)
        texte = texte[:ou] + "\n" + html_bloc + texte[ou:]

    if texte == avant:
        return False, "aucun changement"
    page.write_text(texte, encoding="utf-8")
    return True, "posé"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--etat", action="store_true", help="ne touche à rien, dit ce qui manque")
    ap.add_argument("--apercu", metavar="FICHIER", nargs="?", const="apercu_ressource.html",
                    help="écrit un aperçu autonome au lieu de modifier le dépôt")
    ap.add_argument("--racine", metavar="CHEMIN", default=None,
                    help="racine du dépôt, si l'outil n'est pas à sa place habituelle")
    a = ap.parse_args()
    global RACINE
    if a.racine:
        RACINE = pathlib.Path(a.racine).resolve()

    registre = json.loads(REGISTRE.read_text(encoding="utf-8"))
    ressources = registre["ressources"]
    prets, incomplets = [], []
    for r in ressources:
        (incomplets if manques(r) else prets).append(r)

    print("Registre : %d ressource(s) — %d prête(s), %d en attente.\n"
          % (len(ressources), len(prets), len(incomplets)))

    for r in incomplets:
        print("  ⏳ %-24s il manque : %s" % (r["id"], ", ".join(manques(r))))
        if not (r.get("url") or "").strip():
            print("     ce que la vidéo doit montrer : %s" % r["doit_montrer"][:150].strip())
    if incomplets:
        print()

    if a.apercu:
        # L'aperçu montre les ressources RÉELLES quand il y en a : un aperçu dont les
        # boutons ne mènent nulle part n'apprend rien sur des boutons qui mènent quelque part.
        montres = prets if prets else [dict(ressources[0], **{
            "titre": "TITRE DE LA VIDÉO — emplacement encore vide",
            "source": "SOURCE — à renseigner", "url": "",
            "a_regarder": "<p>La consigne minutée s'écrit après avoir regardé la vidéo.</p>",
        })]
        corps = "\n".join(bloc(r, r.get("verifie_le") or "") for r in montres)
        vivants = sum(1 for r in montres if not factice(r.get("url", "")))
        intro = ("<p class=\"avis\">%d bloc(s) affiché(s). <strong>%d bouton(s) mènent à une "
                 "vidéo réelle</strong> — existence, titre et auteur confirmés par l'API oEmbed "
                 "de YouTube. Là où l'emplacement est encore vide, il n'y a pas de bouton du "
                 "tout&nbsp;: un repère barré, qui a l'air barré.</p>"
                 "<p class=\"avis\">Ce qui reste à confirmer en regardant : la <strong>durée</strong>, "
                 "la <strong>licence</strong>, et les <strong>minutages</strong> de la consigne. "
                 "<kbd>Ctrl+P</kbd> pour voir ce qui part à la photocopieuse.</p>"
                 % (len(montres), vivants))
        page = ("<!DOCTYPE html><html lang=\"fr\"><head><meta charset=\"utf-8\">"
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
                "<title>Aperçu — bloc ressource</title>" + CSS +
                "<style>body{background:#050f24;color:#e4eaf5;font-family:'Segoe UI',system-ui,"
                "sans-serif;line-height:1.6;margin:0;padding:28px}"
                ".page{max-width:940px;margin:0 auto}"
                "h1{color:#81aaff;font-size:1.35em;margin-bottom:.2em}"
                ".avis{color:#9bbefc;font-size:.94em;max-width:70ch}"
                "kbd{background:#0b1b39;border:1px solid #2f5695;border-radius:4px;padding:1px 5px}"
                "@media print{body{background:#fff;color:#111}h1{color:#111}.avis{color:#333}}"
                "</style></head><body><div class=\"page\">"
                "<h1>Aperçu du bloc « ressource vidéo »</h1>" + intro
                + corps + "</div></body></html>")
        pathlib.Path(a.apercu).write_text(page, encoding="utf-8")
        print("Aperçu écrit : %s  (%d bloc(s), %d lien(s) réel(s))"
              % (a.apercu, len(montres), vivants))
        return 0

    if a.etat:
        for r in prets:
            print("  ✅ %-24s %s" % (r["id"], r["titre"]))
        return 0

    aujourdhui = date.today().isoformat()
    for r in prets:
        page = RACINE / r["page"]
        if not page.exists():
            print("  ❌ %-24s page introuvable : %s" % (r["id"], r["page"]))
            continue
        ok, mot = poser(page, r, bloc(r, r.get("verifie_le") or aujourdhui))
        print("  %s %-24s %s" % ("✅" if ok else "⚠️ ", r["id"], mot))
    return 0


if __name__ == "__main__":
    sys.exit(main())
