#!/usr/bin/env python3
"""Construit l'entraînement DNB « algorigrammes » au gabarit maison, à partir de ex.py."""
import html, pathlib, random, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from dnb_exercices import E

MANCHES = {1: ("Manche 1 — Le vocabulaire et les symboles",
               "Ce qu'on doit savoir nommer avant de savoir lire."),
           2: ("Manche 2 — Lire et dérouler", "On suit les flèches, on note ce que devient chaque variable."),
           3: ("Manche 3 — Compteurs, tests et cas limites", "Là où se perdent les points au brevet."),
           4: ("Manche 4 — Sujets type DNB", "Des situations complètes, comme à l'épreuve.")}

alea = random.Random(2608)   # graine fixe : la page est reproductible à l'identique
def e(x): return html.escape(x, quote=True)


# Répartition déterministe de la bonne réponse sur A/B/C/D : sept exercices sur huit
# au maximum par position, plutôt qu'un tirage libre qui déséquilibre (15 sur C au
# premier essai). Même principe que _outils/fix_r.js pour les QCM.
POSITIONS = [(i * 3 + 1) % 4 for i in range(len(E))]


def bloc_exercice(i, x):
    opts = [x["bonne"]] + [d[0] for d in x["dis"]]
    cible = POSITIONS[i - 1]
    autres = [1, 2, 3]; alea.shuffle(autres)
    ordre = autres[:cible] + [0] + autres[cible:]
    lettres = "ABCD"
    options = "".join(f'<option>{e(opts[k])}</option>' for k in ordre)
    refut = "".join(
        f"<li><b>{lettres[p]}.</b> {e(opts[k])} — {e(dict((d[0], d[1]) for d in x['dis'])[opts[k]])}</li>"
        for p, k in enumerate(ordre) if k != 0)
    fig = ""
    if x["img"]:
        fig = (f'<figure class="ex-figure"><img src="{x["img"][0]}" alt="{e(x["img"][1])}">'
               f'<figcaption>📷 Document à lire pour répondre</figcaption></figure>')
    pre = f'<pre class="algo">{e(x["pre"])}</pre>' if x["pre"] else ""
    tag = f'<span class="tag-dnb">{e(x["tag"])}</span>' if x["tag"] else ""
    return f"""
    <article class="exo" id="exo{i}">
      <h3>Exercice {i} — {e(x["t"])} {tag}</h3>
      {fig}{pre}
      <div class="assoc">
        <label for="q{i}">{x["q"]}</label>
        <select id="q{i}"><option value="">— choisir —</option>{options}</select>
      </div>
      <details class="aide aide1"><summary>💡 Aide de niveau 1</summary><p>{x["a1"]}</p></details>
      <details class="aide aide2"><summary>💡💡 Aide de niveau 2</summary><p>{x["a2"]}</p></details>
      <details class="correction"><summary>📖 Correction (à ouvrir APRÈS avoir vérifié)</summary>
        <p><b>Réponse attendue :</b> {e(x["bonne"])}</p>
        <p><b>Pourquoi les autres sont fausses :</b></p>
        <ul>{refut}</ul>
        <p class="retenir">🧠 À retenir : {e(x["ret"])}</p>
      </details>
    </article>"""


def main():
    par_manche = {m: [(i + 1, x) for i, x in enumerate(E) if x["m"] == m] for m in MANCHES}
    onglets, panneaux, checks, taches = [], [], [], []
    for m, (titre, sous) in MANCHES.items():
        actif = " active" if m == 1 else ""
        onglets.append(f'<button class="seance-tab{actif}" role="tab" '
                       f'aria-selected="{"true" if m==1 else "false"}" data-panel="m{m}" '
                       f'id="tab-m{m}">Manche {m}<br>{sous.split(" ")[0]}…'
                       f'<span class="done" id="done-m{m}"></span></button>')
        exos = "".join(bloc_exercice(i, x) for i, x in par_manche[m])
        panneaux.append(f"""
<div class="seance-panel{actif}" id="m{m}" role="tabpanel" aria-labelledby="tab-m{m}">
<section class="card">
  <h2>{e(titre)}</h2>
  <p>{e(sous)} <b>{len(par_manche[m])} exercices.</b></p>
  <p>Chaque réponse fausse est expliquée dans la correction&nbsp;: c'est là que se trouve
  l'essentiel du travail, bien plus que dans le score.</p>
  {exos}
  <button class="btn check" data-check="{m}" type="button">✅ Vérifier la manche {m}</button>
  <p class="feedback" id="fb{m}" role="status"></p>
</section>
</div>""")
        att = ",\n               ".join(f'q{i}:"{x["bonne"].replace(chr(92), chr(92)*2).replace(chr(34), chr(92)+chr(34))}"'
                                        for i, x in par_manche[m])
        checks.append(f"""  {m}: function(){{
    let ok=0, vides=0;
    const att={{{att}}};
    Object.entries(att).forEach(([id,v])=>{{ const r=val(id); if(!r) vides++; else if(r===v) ok++; }});
    return {{score:ok, total:{len(par_manche[m])}, vides:vides, valide: ok >= {max(1, round(len(par_manche[m])*0.75))}}};
  }}""")
        taches.append(f'  m{m}: {{titre:"{e(titre)}", taches:[{{n:{m}, '
                      f'libelle:"Traiter les {len(par_manche[m])} exercices de la manche {m}"}}]}}')

    total = len(E)
    gabarit = pathlib.Path(__file__).parent / "dnb_gabarit.html"
    src = gabarit.read_text(encoding="utf-8")
    src = (src.replace("@@ONGLETS@@", "\n  ".join(onglets))
              .replace("@@PANNEAUX@@", "\n".join(panneaux))
              .replace("@@CHECKS@@", ",\n".join(checks))
              .replace("@@TACHES@@", ",\n".join(taches))
              .replace("@@TOTAL@@", str(total))
              .replace("@@NBMANCHES@@", str(len(MANCHES))))
    cible = pathlib.Path(sys.argv[1])
    cible.write_text(src, encoding="utf-8")
    print(f"{cible.name} — {total} exercices, {len(MANCHES)} manches, {len(src)} octets")


if __name__ == "__main__":
    main()
