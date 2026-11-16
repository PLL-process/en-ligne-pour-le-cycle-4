# -*- coding: utf-8 -*-
"""Le mouvement des pages : chaque animation a son repli « moins de mouvement », et une boucle sans fin se met en pause.

    python3 _outils/controle_mouvement.py [chemins…]          # le bilan (le site entier sans chemin)
    python3 _outils/controle_mouvement.py --liste [chemins…]  # chaque page et chaque animation relevée

Veille du 16/11/2026 (`lottiefiles/motion-design-skill`, licence MIT, réécrit ici) : un élève peut demander à son
appareil « moins de mouvement » (`prefers-reduced-motion`) ; une boucle qui tourne plus de cinq secondes, à côté d'un
texte à lire, distrait — il faut pouvoir l'arrêter (WCAG 2.2.2, « Mettre en pause, arrêter, masquer »).

Ce qui est relevé, page par page (HTML et SVG ; ni `_outils/`, ni `docs/`, ni les archives) :
  M1  une animation CSS (`@keyframes` utilisée par une règle) qu'aucune règle `@media (prefers-reduced-motion: reduce)`
      de la page n'arrête : ni `*`, ni le sélecteur qui l'anime (une de ses classes ou son id) n'y reçoit
      `animation: none`, `display: none` ou `visibility: hidden` ;
      (« .zone * » compte pour tout ce qui est dessous : la mesure lit le CSS, pas l'arbre de la page) ; une animation
      posée seulement sous `@media (prefers-reduced-motion: no-preference)` ne joue pas sous « moins de mouvement » :
      elle est son propre repli ;
  M2  une page HTML qui porte une boucle sans fin (`infinite`) et aucun moyen de l'arrêter : ni bouton dont le texte ou
      l'étiquette dit « pause », « ⏸ », « arrêter l'animation » ou « figer », ni bloc qui en pose un (attribut
      `data-pause-animations` dans la page). Une image SVG ne porte pas de bouton : ses boucles sont comptées à part
      (« images en boucle »), c'est la page qui l'affiche qui doit savoir les arrêter.
Ce n'est qu'une mesure : **⚠ seulement, la sortie vaut toujours 0** (décision de la veille du 15/11 : rien ne passe au
rouge sans l'avis de Pascal). Les animations conduites en JavaScript (`requestAnimationFrame`) ne sont pas lues.
"""
import pathlib
import re
import signal
import sys

DEPOT = pathlib.Path(__file__).resolve().parent.parent
EXCLUS = ("_outils", "docs", "node_modules", ".git", ".claude")

STYLE = re.compile(r"<style\b[^>]*>(.*?)</style>", re.S | re.I)
MEDIA_RM = re.compile(r"@media[^{]*prefers-reduced-motion\s*:\s*reduce[^{]*\{", re.I)
MEDIA_NP = re.compile(r"@media[^{]*prefers-reduced-motion\s*:\s*no-preference[^{]*\{", re.I)
REGLE = re.compile(r"([^{}@]+)\{([^{}]*)\}")
ANIM = re.compile(r"animation(?:-name)?\s*:\s*([^;}]+)", re.I)
INLINE = re.compile(r"""style\s*=\s*["'][^"']*animation\s*:\s*([^"';]+)""", re.I)
ARRET = re.compile(r"animation\s*:\s*none|animation-name\s*:\s*none|display\s*:\s*none|visibility\s*:\s*hidden|"
                   r"animation-play-state\s*:\s*paused", re.I)
BOUTON = re.compile(r"<button\b[^>]*>.*?</button>", re.S | re.I)
PAUSE = re.compile(r"pause|⏸|arr[êe]ter? l.animation|arr[êe]ter? le mouvement|figer", re.I)


def blocs_reduits(css, motif=MEDIA_RM):
    """Le contenu des blocs @media (prefers-reduced-motion: reduce) — ou d'un autre motif —, et le reste du CSS."""
    dedans, reste, i = [], [], 0
    for m in motif.finditer(css):
        if m.start() < i:
            continue
        reste.append(css[i:m.start()])
        prof, j = 1, m.end()
        while j < len(css) and prof:
            prof += {"{": 1, "}": -1}.get(css[j], 0)
            j += 1
        dedans.append(css[m.end():j - 1])
        i = j
    reste.append(css[i:])
    return "\n".join(dedans), "\n".join(reste)


def jetons(sel):
    return set(re.findall(r"[.#][\w-]+", sel))


def lire(texte):
    """[(nom de l'animation, sélecteur, infinie ?)], couvertes (noms), page avec bouton pause ?"""
    css = "\n".join(STYLE.findall(texte))
    reduit, normal = blocs_reduits(css)
    sans_pref, _ = blocs_reduits(normal, MEDIA_NP)   # ce qui ne joue que sans préférence est déjà son propre repli
    regles_np = set(" ".join(s.split()) for s, _ in REGLE.findall(sans_pref))
    noms = set(re.findall(r"@keyframes\s+([\w-]+)", css))
    anims = []
    for sel, decl in REGLE.findall(normal):
        for valeur in ANIM.findall(decl):
            for part in valeur.split(","):
                mots = part.split()
                nom = next((m for m in mots if m in noms), None)
                if nom:
                    anims.append((nom, " ".join(sel.split()), "infinite" in mots))
    for valeur in INLINE.findall(texte):
        for part in valeur.split(","):
            mots = part.split()
            nom = next((m for m in mots if m in noms), None)
            if nom:
                anims.append((nom, "(attribut style)", "infinite" in mots))
    arrets = [sel for sel, decl in REGLE.findall(reduit) if ARRET.search(decl)]
    tout = any(re.search(r"(^|[\s,>])\*($|[\s,:])", " " + s + " ") for s in arrets)
    jetons_arret = set().union(*[jetons(s) for s in arrets]) if arrets else set()
    couvertes = set()
    for nom, sel, _ in anims:
        if tout or (jetons(sel) & jetons_arret) or sel in regles_np:
            couvertes.add((nom, sel))
    pause = "data-pause-animations" in texte or any(PAUSE.search(b) for b in BOUTON.findall(texte))
    return anims, couvertes, pause


def fichiers(chemins):
    racines = [pathlib.Path(c).resolve() for c in chemins] or [DEPOT]
    for r in racines:
        liste = [r] if r.is_file() else sorted(list(r.rglob("*.html")) + list(r.rglob("*.svg")))
        for f in liste:
            rel = f.relative_to(DEPOT) if DEPOT in f.parents else f
            if any(p in EXCLUS or p.startswith("_archive") for p in rel.parts[:-1]):
                continue
            yield f, rel


def main(argv):
    liste = "--liste" in argv
    chemins = [a for a in argv if not a.startswith("--")]
    n_pages = n_m1 = n_m2 = n_anim = n_img = 0
    for f, rel in fichiers(chemins):
        texte = f.read_text(encoding="utf-8", errors="ignore")
        if "@keyframes" not in texte:
            continue
        anims, couvertes, pause = lire(texte)
        if not anims:
            continue
        n_pages += 1
        uniques = sorted(set((a, s) for a, s, _ in anims))
        n_anim += len(uniques)
        m1 = [x for x in uniques if x not in couvertes]
        boucle = any(inf for _, _, inf in anims)
        image = f.suffix.lower() == ".svg"
        m2 = boucle and not pause and not image
        n_m1 += len(m1)
        n_m2 += 1 if m2 else 0
        n_img += 1 if (boucle and image) else 0
        if liste and (m1 or m2):
            print(str(rel))
            for nom, sel in m1:
                print("  ⚠ M1 sans repli « moins de mouvement » — %s (%s)" % (nom, sel[:70]))
            if m2:
                boucles = sorted(set(a for a, _, inf in anims if inf))
                print("  ⚠ M2 boucle sans fin, aucun bouton pour l'arrêter — %s" % ", ".join(boucles))
    print("%d page(s) animée(s), %d animation(s) · ⚠ M1 %d sans repli « moins de mouvement » · ⚠ M2 %d page(s) "
          "dont une boucle sans fin ne s'arrête pas · %d image(s) SVG en boucle" % (n_pages, n_anim, n_m1, n_m2, n_img))
    return 0


if __name__ == "__main__":
    if hasattr(signal, "SIGPIPE"):
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    sys.exit(main(sys.argv[1:]))
