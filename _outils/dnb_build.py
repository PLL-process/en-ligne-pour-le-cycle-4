#!/usr/bin/env python3
"""dnb_build.py — construit l'entraînement DNB « algorigrammes » (3e_C6.2) au gabarit maison.

    python3 _outils/dnb_build.py <page.html>

Sources : dnb_exercices.py (les 30 exercices), dnb_schemas.py (les algorigrammes, en SVG dans la page),
dnb_gabarit.html (l'en-tête, le rappel, le vérificateur), _ressources-communes/code-colore/ (copié dans la page).

Après la construction, rejouer sur la page les quatre blocs injectés par les outils du site (ils ne vivent pas dans
le gabarit, chacun a sa source unique) :
    python3 _outils/onglets_clavier.py --ecrire <page>     (n°326)
    python3 _outils/retrait_validation.py --ecrire <page>  (n°340)
    python3 _outils/onglets_seance.py --ecrire <page>
    python3 _outils/entete_telephone.py --ecrire <page>

Révision du 21/11/2026 (audit pédagogique et fonctionnel) :
  · questions en boutons radio dans un <fieldset> (n°300), plus de listes déroulantes ;
  · place de la bonne réponse : la suite fixe PLACES, équilibrée (8/8/7/7) et sans motif — l'ancienne répétait
    2-1-4-3 de la question 1 à la question 30 ;
  · retour par exercice après « Vérifier » (✔ juste, ✘ à revoir, ○ à faire), « Revoir mon erreur », avancement et
    réussite séparés dans le bandeau ;
  · une cinquième page, l'épreuve écrite de l'abri à vélos, sans propositions.
"""
import html
import json
import pathlib
import random
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from dnb_exercices import E, FORMES  # noqa: E402
import dnb_schemas as S  # noqa: E402

MANCHES = {
    1: dict(titre="Symboles", seuil=6,
            intro="Ce qu'on doit savoir reconnaître avant de savoir lire."),
    2: dict(titre="Déroulement", seuil=6,
            intro="On prédit, puis on vérifie : on suit les flèches et on note ce que devient chaque variable."),
    3: dict(titre="Auto-test", seuil=4,
            intro="Chaque matin à 7 h, la station d'alerte de Sainte-Luce teste ses quatre organes — anémomètre, "
                  "gyrophare, sirène, liaison radio —, compte les défauts et envoie un seul bilan au gardien."),
    4: dict(titre="Transfert", seuil=6,
            intro="Des situations nouvelles, comme au brevet : un algorigramme à parcourir, une condition à essayer, "
                  "une justification à choisir."),
}
NB = len(E)


def e(x):
    return html.escape(x, quote=True)


def fr(t):
    """Espaces insécables de la typographie française (« », ? ! : ;) ; une instruction citée entre guillemets
    (« defauts ← defauts + 1 ») ne se coupe pas en fin de ligne."""
    t = re.sub(r" ([?!:;»])", "\u00a0\\1", t)
    t = t.replace("« ", "«\u00a0")
    return re.sub(r"«\u00a0[^«»]*[←=<>≤≥+][^«»]*\u00a0»", lambda m: m.group(0).replace(" ", "\u00a0"), t)


def places(graine=2111):
    """La place de la bonne réponse (0 à 3), exercice par exercice, tirée une fois pour toutes (graine fixe : la page
    est reproductible, et la place d'une réponse ne change pas d'une génération à l'autre). Contraintes vérifiées :
      · dans chaque manche, chaque place sert deux fois (manches de 8) ou une à deux fois (manche de 6) — répondre
        toujours la même place ne valide aucune manche ;
      · jamais trois fois de suite la même place ;
      · aucun motif périodique : pas de période 2 sur 5 exercices, 3 sur 7, 4 sur 9 (l'ancienne suite répétait
        2-1-4-3 sur les trente exercices)."""
    alea = random.Random(graine)
    tailles = [sum(1 for x in E if x["m"] == m) for m in MANCHES]
    while True:
        p = []
        for t in tailles:
            bloc = [k % 4 for k in range(t)]
            alea.shuffle(bloc)
            p += bloc
        n = len(p)
        if any(p[i] == p[i + 1] == p[i + 2] for i in range(n - 2)):
            continue
        if any(all(p[i + k] == p[i + k + per] for k in range(lg - per))
               for per, lg in ((2, 5), (3, 7), (4, 9)) for i in range(n - lg + 1)):
            continue
        if sorted(p.count(k) for k in range(4)) != [7, 7, 8, 8]:
            continue
        return p


PLACES = places()


def doc_html(x, i):
    d = x["doc"]
    if not d:
        return ""
    if "pre" in d:
        return f'<pre class="algo" data-code-colore="algo">{e(d["pre"])}</pre>'
    if "svg" in d:
        svg = S.SCHEMAS[d["svg"]]()
        desc = re.search(r"<desc[^>]*>(.*?)</desc>", svg).group(1)
        # le même texte que la description lue par un lecteur d'écran, une étape par ligne (ni plus, ni moins d'indices)
        etapes = "".join(f"<li>{x}</li>" for x in re.split(r"(?<=[.?])\s+(?=[A-ZÉÀÈ«])", desc) if x.strip())
        return (f'<div class="doc"><p class="doc-titre">📄 {e(fr(d["legende"]))}</p>{svg}'
                f'<p class="loupe-indice">🔍 Touche ou clique le schéma pour l\'agrandir.</p>'
                f'<details class="desc-schema"><summary>📝 Le schéma, en texte</summary><ol>{etapes}</ol></details></div>')
    if d.get("trace"):
        lignes = [("—", "avant la boucle", "—", "0")]
        orgs = [("anémomètre", "en panne"), ("gyrophare", "fonctionne"), ("sirène", "en panne"),
                ("liaison radio", "fonctionne")]
        corps = "<tr><td>—</td><td>avant la boucle</td><td>—</td><td>0</td></tr>"
        for k, (o, r) in enumerate(orgs, 1):
            corps += (f'<tr><td>{k}</td><td>{o}</td><td>{r}</td><td><input type="number" inputmode="numeric" '
                      f'id="tr_{k}" aria-label="defauts après le tour {k}"><span class="marque" id="m_tr_{k}"></span>'
                      f'</td></tr>')
        return (f'<div class="doc trace-a-completer"><p class="doc-titre">📄 {e(fr(d["legende"]))}</p>'
                f'<div class="tableau-defile"><table class="trace"><thead><tr><th scope="col">Tour</th>'
                f'<th scope="col">Organe testé</th><th scope="col">Résultat du test</th>'
                f'<th scope="col">defauts après ce tour</th></tr></thead><tbody>{corps}</tbody></table></div></div>')
    if "html" in d:
        return d["html"]
    return ""


def corr_doc(x):
    c = x["corr"]
    if not c:
        return ""
    if "svg" in c:
        svg = S.SCHEMAS[c["svg"]]()
        return f'<div class="doc"><p class="doc-titre">📄 {e(fr(c["legende"]))}</p>{svg}</div>'
    return c["html"]


def bloc_exercice(i, x):
    qid = f"q{i}"
    bonne = fr(x["bonne"])
    intrus = [(fr(t), fr(p)) for t, p in x["intrus"]]
    place = PLACES[i - 1]
    opts = [None] * 4
    opts[place] = (bonne, None)
    reste = iter(intrus)
    for k in range(4):
        if opts[k] is None:
            opts[k] = next(reste)
    lignes = []
    for k, (t, pq) in enumerate(opts, 1):
        ic = S.icone(FORMES[x["bonne"] if pq is None else [a for a, b in x["intrus"] if fr(a) == t][0]]) \
            if x["icones"] else ""
        pourquoi = f' data-pourquoi="{e(pq)}"' if pq else ""
        lignes.append(f'<div class="qcm-option"><input type="radio" name="{qid}" id="{qid}__{k}" value="{e(t)}"'
                      f'{pourquoi}>{ic}<label for="{qid}__{k}">{e(t)}</label></div>')
    voile = ""
    pred = ""
    if x["pred"]:
        voile = " voile"
        pred = (f'<div class="prediction"><label for="pred-{qid}">🔮 Prédis d\'abord, sans regarder les '
                f'propositions&nbsp;: qu\'attends-tu&nbsp;?</label><div class="ligne"><input type="text" '
                f'id="pred-{qid}" autocomplete="off" placeholder="ma prédiction"><button type="button" '
                f'class="btn ghost" data-montrer="{qid}">👀 Voir les propositions</button></div></div>')
    tag = ""
    if x["cle"] is True:
        tag = '<span class="tag cle">🔑 indispensable</span>'
    elif x["cle"] is False:
        tag = '<span class="tag rev">🔁 révision</span>'
    refut = "".join(f"<li>«&nbsp;{e(t)}&nbsp;» — {e(p)}</li>" for t, p in intrus)
    apres = f'<p class="apres">{fr(x["apres"])}</p>' if x["apres"] else ""
    return f"""
    <article class="exo" id="exo{i}">
      <div class="exo-tete"><h3>Exercice {i} — {e(fr(x["t"]))}</h3>{tag}<span class="etat" id="etat-{qid}"></span></div>
      {doc_html(x, i)}{pred}
      <fieldset class="qcm-groupe{voile}" id="{qid}">
        <legend>{e(fr(x["q"]))}</legend>
        {"".join(lignes)}
      </fieldset>
      <div class="revoir" id="revoir-{qid}" role="status" hidden></div>
      <details class="aide aide1"><summary>💡 Aide 1 — un indice</summary><p>{e(fr(x["a1"]))}</p></details>
      <details class="aide aide2"><summary>💡💡 Aide 2 — la démarche</summary><p>{e(fr(x["a2"]))}</p></details>
      <details class="correction"><summary>📖 Correction complète</summary>
        <p><b>✅ Réponse&nbsp;:</b> «&nbsp;{e(bonne)}&nbsp;»</p>
        <p class="copie"><b>✍️ Sur ta copie, on peut écrire&nbsp;:</b> «&nbsp;{e(fr(x["copie"]))}&nbsp;»</p>
        {corr_doc(x)}
        <p><b>Pourquoi pas les autres propositions&nbsp;?</b></p>
        <ul>{refut}</ul>
        {apres}
        <p class="retenir">🧠 À retenir&nbsp;: {e(fr(x["ret"]))}</p>
      </details>
    </article>"""


SUIVANTE = {1: ("m2", "Manche 2 — Déroulement ›"), 2: ("m3", "Manche 3 — Auto-test ›"),
            3: ("m4", "Manche 4 — Transfert ›"), 4: ("ep", "Épreuve écrite — l'abri à vélos ›")}

BANC = """
<section class="card banc" id="versBanc">
  <h3>🩺 Et maintenant&nbsp;: éprouve l'algorithme au banc d'essai</h3>
  <p>Le banc d'essai de l'atelier 3e_C6.2 fait tourner l'auto-test pour de vrai&nbsp;: tu choisis les organes en panne, tu lances, tu lis le journal.</p>
  <p>Rejoue le matin des exercices 18 et 19 (anémomètre et sirène en panne)&nbsp;: le journal donne-t-il le même compteur que ta trace&nbsp;?
  <br>Puis fais les deux essais que demande l'atelier&nbsp;: un matin sans aucune panne, et un matin avec au moins deux pannes.</p>
  <p>➡ <a href="sequence_3e_C6.2_auto_test_station.html#banc-essai">Atelier C6.2 – Auto-test&nbsp;: le banc d'essai (activité 4)</a></p>
</section>"""

EPREUVE_QUESTIONS = [
    ("À 79 lux, avec une présence&nbsp;: indique le trajet suivi dans l'algorigramme, et justifie la commande de la lampe.",
     "À 79 lux, «&nbsp;79 &lt; 80&nbsp;» est …… ; une présence est …… ; donc «&nbsp;L &lt; 80 ET présence&nbsp;» est …… . "
     "Je suis la branche «&nbsp;……&nbsp;», qui …… la lampe."),
    ("À 80 lux, avec une présence&nbsp;: prévois l'état de la lampe, et justifie-le par le signe du comparateur.",
     "«&nbsp;80 &lt; 80&nbsp;» est …… , car le signe &lt; …… l'égalité. La condition est donc …… : je suis la branche "
     "«&nbsp;……&nbsp;», et la lampe …… ."),
    ("Le nouveau besoin demande l'allumage aussi à 80 lux, avec une présence. Modifie la condition (document 2), puis "
     "propose un essai qui distingue l'ancienne version de la nouvelle.",
     "Nouvelle condition&nbsp;: L …… 80 ET présence. Essai&nbsp;: …… lux, avec une présence → l'ancienne version …… , la "
     "nouvelle …… ."),
    ("Propose un autre essai qui vérifie que la présence reste obligatoire dans la nouvelle version.",
     "Essai&nbsp;: …… lux, …… présence → la lampe doit rester …… , dans les deux versions."),
]

EPREUVE_CORRECTION = [
    ("«&nbsp;79 &lt; 80&nbsp;» est vrai, et une présence est détectée&nbsp;: les deux conditions sont vraies, donc «&nbsp;L &lt; 80 ET "
     "présence&nbsp;» est vraie. Je suis la branche «&nbsp;oui&nbsp;», qui commande l'allumage de la lampe.",
     "la branche nommée («&nbsp;oui&nbsp;») <b>et</b> les deux conditions évaluées avec la valeur 79.",
     ["«&nbsp;La lampe s'allume car il fait sombre.&nbsp;» — une seule condition, et sans la valeur."]),
    ("«&nbsp;80 &lt; 80&nbsp;» est faux&nbsp;: le signe &lt; est strict, il exclut l'égalité. La condition ET est donc fausse, même "
     "avec une présence&nbsp;: je suis la branche «&nbsp;non&nbsp;», la lampe s'éteint.",
     "le signe &lt; cité, l'égalité exclue, et l'état «&nbsp;éteinte&nbsp;».",
     ["«&nbsp;Elle s'allume, 80 lux c'est sombre.&nbsp;» — le comparateur n'est pas utilisé."]),
    ("Nouvelle condition&nbsp;: <b>L ≤ 80 ET présence</b> («&nbsp;ET présence&nbsp;» est gardé). Essai qui distingue les deux "
     "versions&nbsp;: <b>80 lux avec une présence</b> — l'ancienne version éteint, la nouvelle allume.",
     "≤ à la place de &lt;, «&nbsp;ET présence&nbsp;» conservé&nbsp;; un essai pile sur 80 lux, avec une présence, et le résultat "
     "des deux versions.",
     ["«&nbsp;L ≤ 80 OU présence&nbsp;» — la présence ne serait plus obligatoire.",
      "«&nbsp;Essai à 50 lux avec une présence&nbsp;» — les deux versions allument&nbsp;: l'essai ne distingue rien."]),
    ("Par exemple <b>79 lux sans présence</b>&nbsp;: la lampe doit rester éteinte, dans les deux versions (80 lux sans "
     "présence convient aussi).",
     "un essai <b>sans</b> présence, à une luminosité où la lampe s'allumerait avec une présence&nbsp;; le résultat "
     "attendu&nbsp;: éteinte.",
     ["«&nbsp;79 lux avec une présence&nbsp;» — la présence est là&nbsp;: l'essai ne prouve pas qu'elle est obligatoire.",
      "«&nbsp;120 lux sans présence&nbsp;» — la lampe serait éteinte de toute façon, à cause de la luminosité&nbsp;: l'essai "
      "ne teste pas la présence."]),
]


def epreuve():
    qs = ""
    for k, (q, et) in enumerate(EPREUVE_QUESTIONS, 1):
        qs += (f'<div class="question-ecrite"><label class="q" for="ep{k}">{k}. {q}</label>'
               f'<textarea id="ep{k}" rows="4" placeholder="Ta réponse, en phrases complètes"></textarea>'
               f'<details class="aide etayee"><summary>🪜 Coup de pouce — la phrase à compléter</summary>'
               f'<p>{et}</p></details></div>')
    corr = ""
    for k, (att, crit, contres) in enumerate(EPREUVE_CORRECTION, 1):
        cs = "".join(f'<li class="contre">✘ {c}</li>' for c in contres)
        corr += (f'<h4>Question {k}</h4><p class="copie"><b>✍️ Une réponse possible&nbsp;:</b> {att}</p>'
                 f'<p><b>🎯 Ce qui est attendu&nbsp;:</b> {crit}</p><ul>{cs}</ul>')
    return f"""
<div class="seance-panel" id="ep" role="tabpanel" aria-labelledby="tab-ep">
<section class="card">
  <h2>✍️ Épreuve écrite — l'éclairage de l'abri à vélos</h2>
  <p>Ici, <b>aucune proposition</b>&nbsp;: tu rédiges, comme au brevet. Compte une dizaine de minutes.</p>
  <p class="complement">Au brevet, à partir de la session 2027, la technologie compte pour <b>10 points</b>, en 30 minutes environ, dont <b>1 point</b> pour la maîtrise de la langue&nbsp;: écris des phrases complètes, avec les valeurs.
  <br>Ce mini-sujet n'est pas une épreuve entière&nbsp;: il entraîne trois gestes — suivre une branche, justifier avec les données, modifier et vérifier.</p>
  <h3>La situation</h3>
  <p><i>Situation fictive.</i> Au Lamentin, un contrôleur commande la lampe d'un abri à vélos. Toutes les secondes, il lit la luminosité L, en lux, et la présence d'un usager.
  <br>La lampe <b>s'allume</b> lorsque la luminosité est <b>strictement inférieure à 80 lux</b> <b>et</b> qu'une présence est détectée. Dans les autres cas, elle <b>s'éteint</b>.
  <br>Le contrôleur recommence ensuite une mesure.</p>
  <div class="doc"><p class="doc-titre">📄 Document 1 — l'algorigramme du contrôleur</p>{S.abri()}
  <p class="loupe-indice">🔍 Touche ou clique le schéma pour l'agrandir.</p></div>
  <div class="doc"><p class="doc-titre">📄 Document 2 — la condition d'origine, pour la question 3</p>
  <pre class="algo" data-code-colore="algo">L &lt; 80 ET présence</pre></div>
  {qs}
  <p class="note-relue">✍ Tes réponses seront relues par ton professeur&nbsp;: aucun bouton ne les note. Compare-les à la correction, puis coche la grille.</p>
  <details class="correction" id="epCorrection"><summary>📖 Correction complète — à ouvrir quand tes quatre réponses sont écrites</summary>
    {corr}
    <p class="retenir">🧠 À retenir&nbsp;: une justification cite la branche suivie, les valeurs et le signe du comparateur. Un bon essai est celui dont le résultat change selon ce qu'on veut vérifier.</p>
  </details>
  <div class="grille">
    <h3>☑ Ma grille — ce que ma copie montre</h3>
    <label><input type="checkbox" id="crit1"><span><b>Suivre la branche</b>&nbsp;: je nomme la branche suivie (questions 1 et 2).</span></label>
    <label><input type="checkbox" id="crit2"><span><b>Justifier avec les données</b>&nbsp;: j'écris les valeurs et le signe du comparateur (questions 1 et 2).</span></label>
    <label><input type="checkbox" id="crit3"><span><b>Modifier et vérifier</b>&nbsp;: je modifie la condition et je propose des essais qui vérifient (questions 3 et 4).</span></label>
  </div>
</section>
</div>"""


def main():
    par_manche = {m: [(i + 1, x) for i, x in enumerate(E) if x["m"] == m] for m in MANCHES}
    onglets, panneaux, checks, mjs = [], [], [], {}
    for m, M in MANCHES.items():
        exs = par_manche[m]
        total = len(exs)
        actif = " active" if m == 1 else ""
        onglets.append(f'<button class="seance-tab{actif}" role="tab" aria-selected="{"true" if m == 1 else "false"}" '
                       f'data-panel="m{m}" id="tab-m{m}" type="button">Manche {m}<small>{M["titre"]}</small>'
                       f'<span class="done" id="done-m{m}"></span></button>')
        nb_cles = sum(1 for _, x in exs if x["cle"])
        compte = f"{total} exercices" + (f", dont {nb_cles} indispensables 🔑" if nb_cles else "")
        corps = "".join(bloc_exercice(i, x) for i, x in exs)
        nxt, lib = SUIVANTE[m]
        panneaux.append(f"""
<div class="seance-panel{actif}" id="m{m}" role="tabpanel" aria-labelledby="tab-m{m}">
<section class="card">
  <h2>Manche {m} — {M["titre"]}</h2>
  <p>{e(fr(M["intro"]))} <b>{compte}.</b></p>
  <p class="complement">✍️ Après avoir choisi, entraîne-toi à expliquer ton cheminement en une ou deux phrases, sur une feuille de brouillon.</p>
  {corps}
  <p class="critere">🎯 <b>Critère de réussite&nbsp;:</b> au moins {M["seuil"]} réponses justes sur {total}.</p>
  <button class="btn check" data-check="{m}" type="button">✅ Vérifier la manche {m}</button>
  <div class="feedback" id="fb{m}" role="status"></div>
</section>{BANC if m == 3 else ""}
<p class="page-suivante"><button class="btn vers-seance" data-vers="{nxt}" type="button">{lib}</button></p>
</div>""")
        att = ",".join(f"{json.dumps(f'q{i}')}:{json.dumps(fr(x['bonne']), ensure_ascii=False)}" for i, x in exs)
        checks.append(f"""  {m}: function(){{
    const att={{{att}}};
    const r=corriger(att);
    return {{score:r.ok, total:{total}, vides:r.vides, detail:r.detail, valide: r.ok >= {M["seuil"]}}};
  }}""")
        mjs[m] = dict(titre=M["titre"], seuil=M["seuil"], total=total, ids=[f"q{i}" for i, _ in exs],
                      titres={f"q{i}": fr(x["t"]) for i, x in exs})
    onglets.append('<button class="seance-tab" role="tab" aria-selected="false" data-panel="ep" id="tab-ep" '
                   'type="button">Épreuve<small>écrite</small><span class="done" id="done-ep"></span></button>')
    panneaux.append(epreuve())

    src = (ICI / "dnb_gabarit.html").read_text(encoding="utf-8")
    cc = ICI.parent / "_ressources-communes" / "code-colore"
    remplace = {
        "@@ONGLETS@@": "\n  ".join(onglets),
        "@@PANNEAUX@@": "\n".join(panneaux),
        "@@CHECKS@@": ",\n".join(checks),
        "@@MANCHES_JS@@": json.dumps({str(k): v for k, v in mjs.items()}, ensure_ascii=False),
        "@@TOTAL@@": str(NB),
        "@@NBMANCHES@@": str(len(MANCHES)),
        "@@CODE_COLORE_CSS@@": (cc / "code-colore.css").read_text(encoding="utf-8").strip(),
        # « </script> » écrit dans un commentaire du fichier fermerait la balise : on l'écrit « <\/script> »
        "@@CODE_COLORE_JS@@": (cc / "code-colore.js").read_text(encoding="utf-8").strip().replace("</script", "<\\/script"),
        "@@SVG:voyants@@": S.SCHEMAS["voyants"](),
    }
    for forme in ("terminal", "rectangle", "losange", "parallelogramme"):
        remplace[f"@@ICONE:{forme}@@"] = S.icone(forme).replace('width="52" height="32"', 'width="64" height="40"')
    for k, v in remplace.items():
        assert k in src, k
        src = src.replace(k, v)
    reste = re.findall(r"@@[A-Z_:a-z]+@@", src)
    assert not reste, reste
    cible = pathlib.Path(sys.argv[1])
    cible.write_text(src, encoding="utf-8")
    comptes = [PLACES.count(k) for k in range(4)]
    print(f"{cible.name} — {NB} exercices, {len(MANCHES)} manches + l'épreuve écrite, {len(src)} octets")
    print(f"places de la bonne réponse (1 à 4) : {' '.join(str(p + 1) for p in PLACES)} · répartition {comptes}")
    print("À rejouer maintenant : onglets_clavier, retrait_validation, onglets_seance, entete_telephone (--ecrire).")


if __name__ == "__main__":
    main()
