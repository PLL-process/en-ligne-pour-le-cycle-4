#!/usr/bin/env python3
"""Pose le tableau de bord des tâches (règle d'or n°30) à partir des libellés écrits à la main.

La barre de progression COMPTE ; ce bandeau SITUE. C'est ce dont a besoin l'élève
attentionnellement fragile : savoir où il en est sans relire la page.

Ce script ne fabrique aucun libellé — il installe ceux de libelles_bandeaux_taches.py, et
refuse tout fichier dont la liste des tâches ne correspond pas exactement aux boutons
`data-check` réellement présents. C'est la garde apprise le 08/08/2026 au matin, quand une
extraction automatique des titres avait produit des tâches trompeuses.
"""
import html, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from libelles_bandeaux_taches import L

CSS = """
  /* Règle d'or n°30 — tableau de bord des tâches : la barre COMPTE, ce bandeau SITUE */
  #tachesBandeau{margin:10px 0 14px;padding:9px 15px;background:#0d2347;
    border:1px solid #274a8a;border-radius:10px;font-size:.92em;line-height:1.55;color:#e4eaf5}
  #tachesBandeau .tb-titre{font-weight:700;color:#61dafb;display:block;margin-bottom:3px}
  #tachesBandeau ul{list-style:none;margin:0;padding:0}
  #tachesBandeau li{margin:2px 0}
  #tachesBandeau li.faite{opacity:.6;text-decoration:line-through}
  @media print{#tachesBandeau{display:none}}
"""

JS = """
/* ══════ Règle d'or n°30 — tableau de bord des tâches (libellés écrits à la main) ══════ */
const TACHES = %s;
function majTaches(){
  const hote = document.getElementById("tachesBandeau"); if(!hote) return;
  const onglet = document.querySelector(".seance-tab.active");
  const bloc = TACHES[onglet ? onglet.dataset.panel : ""];
  if(!bloc){ hote.hidden = true; return; }
  hote.hidden = false;
  const v = window.__valid || {};
  const faites = bloc.taches.filter(t => v[t.n]).length;
  hote.innerHTML = "<span class='tb-titre'>" + bloc.titre + " — étape " +
    Math.min(faites + 1, bloc.taches.length) + " sur " + bloc.taches.length + "</span><ul>" +
    bloc.taches.map(t => "<li class='" + (v[t.n] ? "faite" : "") + "'>" +
      (v[t.n] ? "☑" : "☐") + " " + t.libelle + "</li>").join("") + "</ul>";
}
document.querySelectorAll(".seance-tab").forEach(t =>
  t.addEventListener("click", () => setTimeout(majTaches, 0)));
majProgress = (function(precedent){
  return function(){ const r = precedent.apply(this, arguments); majTaches(); return r; };
})(majProgress);
majTaches();
"""


def js_taches(pans: dict) -> str:
    def ech(s): return s.replace("\\", "\\\\").replace('"', '\\"')
    blocs = []
    for cle, (titre, taches) in pans.items():
        lignes = ", ".join('{n:%d, libelle:"%s"}' % (n, ech(lib)) for n, lib in taches)
        blocs.append('\n  "%s": {titre:"%s", taches:[%s]}' % (cle, ech(titre), lignes))
    return "{" + ",".join(blocs) + "\n}"


def traiter(chemin: pathlib.Path, essai: bool) -> int:
    pans = L.get(chemin.name)
    if not pans:
        return 0
    src = chemin.read_text(encoding="utf-8")
    if "tachesBandeau" in src:
        print(f"·  {chemin.name} — déjà traité")
        return 0

    # Garde : les tâches écrites doivent recouvrir EXACTEMENT les boutons présents.
    presents = {int(n) for n in re.findall(r'data-check="(\d+)"', src)}
    ecrits = {n for _, taches in pans.values() for n, _ in taches}
    if presents != ecrits:
        print(f"✘  {chemin.name} — libellés ({sorted(ecrits)}) ≠ boutons ({sorted(presents)}) : "
              f"fichier NON réécrit")
        return 0
    # Garde : chaque clé de panneau doit exister dans la page.
    panneaux = set(re.findall(r'data-panel="([^"]+)"', src))
    if set(pans) - panneaux:
        print(f"✘  {chemin.name} — panneaux inconnus {sorted(set(pans)-panneaux)} : NON réécrit")
        return 0

    i = src.index('class="seance-tabs"')
    j = src.index("</div>", src.rindex("</button>", i, src.index("</div>", src.index("</button>", i)) + 6)) + 6
    src = src[:j] + '\n<div id="tachesBandeau" aria-live="polite" ' \
                    'aria-label="Tâches de la séance en cours"></div>' + src[j:]
    src = src[:src.rindex("</style>")] + CSS + src[src.rindex("</style>"):]
    k = src.rindex("</script>")
    src = src[:k] + JS % js_taches(pans) + src[k:]

    if not essai:
        chemin.write_text(src, encoding="utf-8")
    print(f"{'≡' if essai else '✔'}  {chemin.name} — {len(ecrits)} tâche(s) "
          f"sur {len(pans)} séance(s)")
    return len(ecrits)


def main(argv):
    essai = "--essai" in argv
    racine = pathlib.Path("theme-2-structure-fonctionnement-comportement")
    total = sum(traiter(f, essai) for f in sorted(racine.glob("**/sequence_*.html")))
    print(f"\n{total} tâche(s) posée(s) au tableau de bord.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
