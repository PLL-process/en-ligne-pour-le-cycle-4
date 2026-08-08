#!/usr/bin/env python3
"""Applique aux séquences existantes les parties MÉCANISABLES des règles d'or n°29 et n°34.

Ce que fait ce script, et lui seul :
  n°29  installe le mode essentiel — bouton, CSS, bascule JS, persistance — sur les
        séquences bâties sur le gabarit maison (barre d'outils + `restore()`).
  n°34  donne une étiquette (`aria-label`) à tout `select` ou `textarea` qui n'en a pas,
        en reprenant le texte du `<label>` voisin, de l'en-tête de ligne du tableau, ou
        du paragraphe qui précède.

Ce qu'il NE FAIT PAS, volontairement :
  n°23  les durées par activité relèvent du jugement pédagogique — il faut connaître le
        contenu pour dire combien de temps il prend. À la main, lot par lot.
  n°26  le diagnostic d'entrée demande d'écrire des questions justes sur les prérequis.
  n°30  le tableau de bord des tâches a été TENTÉ automatiquement, puis retiré : les
        séquences du dépôt ne nomment pas leurs activités (leurs `<h2>` portent le titre
        de la SÉANCE, et les titres intermédiaires sont des fragments du type
        « c) Je conclus mon inspection »). L'extraction produisait donc des listes de
        tâches trompeuses — pire que pas de bandeau du tout pour l'élève qu'elle vise.
        Les libellés doivent être écrits à la main, lot par lot.
  n°31  la version étayée demande de rédiger des amorces de phrases qui tiennent debout.
  n°33  scinder un pavé au bon endroit demande de savoir où l'idée change.

Autrement dit : ce script fait le travail bête, et refuse de faire semblant de faire
l'autre. Il annonce toujours ce qu'il a modifié, et ne réécrit jamais un fichier qu'il
n'a pas su traiter proprement.

Usage :
    python _outils/retrofit_regles_audit.py <fichier.html> [...]      # applique
    python _outils/retrofit_regles_audit.py --essai <fichier.html>    # simule
"""
from __future__ import annotations

import html
import pathlib
import re
import sys

CSS_ESSENTIEL = """
  /* Règle d'or n°29 — mode essentiel : alléger la lecture sans retirer du parcours */
  body.essentiel .referentiel-card,
  body.essentiel details.correction,
  body.essentiel .approfondissement { display:none }
"""

BOUTON = ('\n  <button class="btn ghost" id="btnEssentiel" aria-pressed="false">'
          '🎯 Mode essentiel : OFF</button>')

NOTE = ('\n<p class="saved-note" style="text-align:center">Le <b>mode essentiel</b> masque le référentiel, '
        'les corrections et les compléments&nbsp;: il ne reste que les consignes et les exercices. '
        'À activer si la page te paraît trop chargée.</p>')

JS_ESSENTIEL = """
/* ══════ Règle d'or n°29 — mode essentiel ══════ */
function majEssentiel(){
  const b = document.getElementById("btnEssentiel");
  if(!b) return;
  const on = document.body.classList.contains("essentiel");
  b.textContent = on ? "🎯 Mode essentiel : ON" : "🎯 Mode essentiel : OFF";
  b.setAttribute("aria-pressed", on ? "true" : "false");
}
(function(){
  const b = document.getElementById("btnEssentiel");
  if(!b) return;
  b.addEventListener("click", ()=>{
    document.body.classList.toggle("essentiel");
    window.__exp = window.__exp || {};
    window.__exp["mode_essentiel"] = document.body.classList.contains("essentiel") ? 1 : 0;
    majEssentiel();
    if(typeof save === "function") save(false);
  });
})();
"""

INIT_ESSENTIEL = ('\nif((window.__exp||{})["mode_essentiel"]) document.body.classList.add("essentiel");'
                  '\nmajEssentiel();')


def marquer_referentiel(src: str) -> tuple[str, bool]:
    """Donne la classe `referentiel-card` à la carte du référentiel, si elle existe."""
    if "referentiel-card" in src:
        return src, False
    motif = re.compile(r'(<section class="card")(>\s*<h2>📚 Le référentiel)')
    nouveau, n = motif.subn(r'\1 referentiel-card\2', src, count=1)
    return nouveau, bool(n)


def poser_css(src: str) -> tuple[str, bool]:
    if "body.essentiel" in src:
        return src, False
    i = src.find("</style>")
    if i < 0:
        return src, False
    return src[:i] + CSS_ESSENTIEL + src[i:], True


def poser_bouton(src: str) -> tuple[str, bool]:
    if 'id="btnEssentiel"' in src:
        return src, False
    m = re.search(r'<button[^>]*id="btnReset"[^>]*>.*?</button>', src, re.S)
    if not m:
        return src, False
    fin = m.end()
    ferme = src.find("</div>", fin)
    if ferme < 0:
        return src, False
    return src[:fin] + BOUTON + src[fin:ferme + len("</div>")] + NOTE + src[ferme + len("</div>"):], True


def poser_js(src: str) -> tuple[str, bool]:
    if "majEssentiel" in src:
        return src, False
    m = re.search(r'^\s*restore\(\);', src, re.M)
    if not m:
        return src, False
    src = src[:m.start()] + JS_ESSENTIEL + src[m.start():]
    m = re.search(r'^\s*restore\(\);', src, re.M)
    return src[:m.end()] + INIT_ESSENTIEL + src[m.end():], True


def etiqueter(src: str) -> tuple[str, int]:
    """Règle n°34 : tout champ de saisie porte une étiquette lisible par un lecteur d'écran."""
    labels = set(re.findall(r'<label[^>]*\bfor="([^"]+)"', src))
    poses = 0

    def texte_de(fragment: str) -> str:
        t = html.unescape(re.sub(r"<[^>]+>", " ", fragment))
        t = re.sub(r"\s+", " ", t.replace("\u00a0", " ")).strip(" :;·—-")
        return t[:110].replace('"', "'")

    def remplacer(mo: re.Match) -> str:
        nonlocal poses
        balise = mo.group(0)
        ident = re.search(r'\bid="([^"]+)"', balise)
        if not ident or ident.group(1) in labels or "aria-label" in balise:
            return balise
        # Priorité au texte qui SUIT immédiatement le champ : dans les listes de rangs
        # (« ▭ traitement [ 3 ] Mesurer l'humidité »), c'est lui qui dit de quoi il s'agit.
        apres = src[mo.end():mo.end() + 1500]
        suivant = re.match(
            r"\s*(?:<option[^>]*>.*?</option>\s*)*(?:</select>)?\s*<span[^>]*>(.*?)</span>",
            apres, re.S)
        libelle = texte_de(suivant.group(1)) if suivant else ""
        if not libelle:
            avant = src[max(0, mo.start() - 1200):mo.start()]
            source = ""
            for motif in (r'<th[^>]*scope="row"[^>]*>(.*?)</th>',
                          r'<label[^>]*>(.*?)</label>',
                          r'<p[^>]*>(.*?)</p>'):
                trouves = re.findall(motif, avant, re.S)
                if trouves:
                    source = trouves[-1]
                    break
            libelle = texte_de(source)
        if not libelle:
            # On ne fabrique pas une étiquette vide de sens : mieux vaut le signaler.
            print(f"   ⚑ {ident.group(1)} : aucune source d'étiquette trouvée, à écrire à la main")
            libelle = "champ à renseigner"
        poses += 1
        return balise[:-1] + f' aria-label="{libelle}">'

    return re.sub(r"<(?:select|textarea)\b[^>]*>", remplacer, src), poses


def traiter(chemin: pathlib.Path, essai: bool) -> None:
    src = origine = chemin.read_text(encoding="utf-8")
    faits: list[str] = []

    src, ok = marquer_referentiel(src)
    if ok:
        faits.append("carte référentiel marquée")
    src, ok = poser_css(src)
    if ok:
        faits.append("CSS n°29")
    src, ok = poser_bouton(src)
    if ok:
        faits.append("bouton n°29")
    src, ok = poser_js(src)
    if ok:
        faits.append("bascule JS n°29")
    src, n = etiqueter(src)
    if n:
        faits.append(f"{n} étiquette(s) n°34")

    if not faits:
        print(f"·  {chemin.name} — rien à faire")
        return
    # Garde-fou : on ne livre jamais un mode essentiel à moitié posé. Du CSS sans bouton,
    # ou un bouton sans bascule, ce n'est pas une conformité partielle — c'est du code mort
    # qui ferait passer la séquence pour traitée alors qu'elle ne l'est pas.
    pose = {"css": "body.essentiel" in src, "bouton": 'id="btnEssentiel"' in src,
            "js": "majEssentiel" in src}
    if any(pose.values()) and not all(pose.values()):
        manquant = ", ".join(k for k, v in pose.items() if not v)
        print(f"✘  {chemin.name} — mode essentiel incomplet ({manquant} manquant) : "
              f"fichier NON réécrit, gabarit à traiter à la main")
        return
    if not essai:
        chemin.write_text(src, encoding="utf-8")
    print(f"{'≡' if essai else '✔'}  {chemin.name} — " + " · ".join(faits)
          + f"  ({len(origine)} → {len(src)} octets)")


def main(argv: list[str]) -> int:
    essai = "--essai" in argv
    cibles = [pathlib.Path(a) for a in argv[1:] if not a.startswith("--")]
    if not cibles:
        print(__doc__)
        return 1
    for c in cibles:
        traiter(c, essai)
    print("\nRappel : les règles n°23, n°26, n°30, n°31 et n°33 ne sont PAS traitées ici.")
    print("Elles demandent de connaître le contenu — elles se font à la main, lot par lot.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
