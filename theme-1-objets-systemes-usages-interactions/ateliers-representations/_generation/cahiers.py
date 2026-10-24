# -*- coding: utf-8 -*-
"""Les cahiers de niveau : tous les exercices d'un niveau, toutes représentations confondues.

Chaque exercice garde la MÊME clé de sauvegarde que dans son atelier : ce que
l'élève a fait dans l'atelier se retrouve dans son cahier, et inversement.
"""
import moteur

e = moteur.e


def page(niv, ats, cahier, page_niveau, chemins_fn):
    chemin = cahier(niv)
    d = chemin.parent
    defs, onglets, panneaux, codes = {}, [], [], []
    for at in ats:
        N = at.NIVEAUX[niv]
        corps = ['<section class="card"><h2>%s %s</h2><p>%s</p><p class="note">Ces exercices sont les mêmes que ceux de '
                 '<a href="%s">l\'atelier de %s</a>&nbsp;: ce que tu fais ici s\'y retrouve, et inversement.</p></section>'
                 % (at.EMOJI, at.TITRE, at.PANNEAU_TEXTE[niv], moteur.rel(d, page_niveau(at, niv)), niv)]
        for i, ex in enumerate(N["exercices"]):
            uid = "%s_%s_%s" % (at.COURT, niv, ex["id"])
            cle = "rep_%s_%s_%s" % (at.SLUG, niv, ex["id"])
            h, df = moteur.exercice(ex, i + 1, uid, cle)
            corps.append(h)
            defs[uid] = df
        k = len(onglets)
        corps.append('<p><button type="button" class="btn suivant" data-vers="%d">%s ›</button></p>'
                     % (k + 1, "Représentation suivante" if k + 1 < len(ats) else "Mon bilan"))
        onglets.append(('%s %s<span class="etat">%d exercices</span>' % (at.EMOJI, at.ETIQUETTE_COURTE, len(N["exercices"])), "c-" + at.COURT))
        panneaux.append(("".join(corps), "c-" + at.COURT))
        for c in N["codes"]:
            if c not in codes:
                codes.append(c)
    pid = "cahier_%s" % niv
    fin = ['<section class="card bilan" data-cle="%s__bilan"><h2>🏁 Mon bilan du cahier</h2>' % pid,
           '<label class="champ" for="%s__bilan_m">Quelle représentation te semble la plus utile, et pour quoi faire&nbsp;? '
           'Laquelle dois-tu encore revoir&nbsp;?</label><textarea id="%s__bilan_m" name="bilan_m" rows="4"></textarea>' % (pid, pid),
           moteur.Rendu("x").etayage(["La représentation la plus utile pour moi est… parce qu'elle montre…",
                                       "Je dois encore revoir… : je vais refaire l'exercice… de l'atelier…"]),
           '<h3>Je me positionne</h3><p class="lsu-legende">Pour chaque compétence travaillée dans ce cahier, choisis la phrase qui '
           'te ressemble aujourd\'hui. Ce n\'est pas une note.</p>']
    for c in codes:
        name = "pos_%s" % c.replace(".", "_")
        fin.append('<fieldset class="qcm-groupe"><legend>%s <span class="note">(%s)</span></legend><div class="options">'
                   % (moteur.avec_sigles(moteur.formulation(c)), e(c)))
        for j, nv in enumerate(moteur.LSU):
            ident = "%s__%s-%d" % (pid, name, j)
            fin.append('<label class="option" for="%s"><input type="radio" id="%s" name="%s" value="%d"><span>%s</span></label>'
                       % (ident, ident, name, j, nv))
        fin.append("</div></fieldset>")
    fin.append("</section>")
    qcms = []
    for at in ats:
        c = chemins_fn(at, niv, d)
        if c.get("qcm"):
            qcms.append('<li><a href="%s">%s %s</a> — %d questions</li>' % (c["qcm"] + c.get("qcm_ancre", ""), at.EMOJI, at.TITRE, c["qcm_nb"]))
    if qcms:
        fin.append('<section class="card"><h2>🧠 Prêt·e à t\'entraîner&nbsp;?</h2><p>Chaque représentation a son QCM, avec une '
                   'correction complète pour chaque question. Le lien ouvre directement les questions de ton niveau.</p><ul>%s</ul></section>'
                   % "".join(qcms))
    onglets.append(('🏁 Mon bilan<span class="etat">et les QCM</span>', "c-fin"))
    panneaux.append(("".join(fin), "c-fin"))

    total = sum(x["duree"] for at in ats for x in at.NIVEAUX[niv]["exercices"])
    nb = sum(len(at.NIVEAUX[niv]["exercices"]) for at in ats)
    h = [moteur.entete("Thème 1 · %s — Mon cahier des représentations" % niv,
                       "Cahier de %s : %d exercices corrigés sur %d façons de représenter une idée technique." % (niv, nb, len(ats))),
         '<body>\n<a class="evitement" href="#contenu">Aller au contenu</a>\n',
         '<nav id="navharm" aria-label="Navigation du site"><a href="%s">&#8962; Accueil</a><a href="%s">🧭 Toutes les représentations</a>%s</nav>\n'
         % (moteur.rel(d, moteur.DEPOT / "index.html"), moteur.rel(d, moteur.THEME1 / "_reperes" / "carte_des_representations.html"),
            "".join('<a href="%s">%s %s</a>' % (moteur.rel(d, cahier(n2)), "📒", "Cahier de " + n2) for n2 in ("5e", "4e", "3e") if n2 != niv)),
         '<main id="contenu" class="page">',
         '<h1>📒 Mon cahier des représentations — %s</h1>' % niv,
         '<p class="mission">Toutes les façons de montrer une idée technique travaillées en %s, réunies au même endroit.</p>' % niv,
         '<div class="toolbar"><button type="button" class="btn" id="btnImprimer">🖨 Imprimer</button>'
         '<button type="button" class="btn ghost" id="btnEffacer">🗑 Effacer ma sauvegarde</button>'
         '<button type="button" class="btn ghost" id="btnEssentiel" aria-pressed="false">🎯 Mode essentiel : désactivé</button></div>',
         '<p class="note" id="noteSauvegarde" style="text-align:center" aria-live="polite">Ton travail s\'enregistre tout seul dans ce navigateur.</p>',
         '<div class="etiquettes"><span class="etiquette niveau" title="Niveau de classe" aria-label="Niveau : %s">%s</span>' % (niv, niv)]
    for c in codes:
        h.append('<span class="etiquette code" title="%s" aria-label="Compétence %s : %s">%s</span>'
                 % (e(moteur.formulation(c)), e(c), e(moteur.formulation(c)), e(c)))
    h.append('<span class="etiquette duree" title="Durée indicative de tous les exercices" aria-label="Durée indicative : environ %d minutes">⏱ ≈ %d min en tout</span></div>' % (total, total))
    h.append('<details class="rappel-ouverture" open><summary>📖 Rappel : à quoi sert ce cahier</summary><section class="card">'
             '<h2>🧭 Une idée technique se montre de plusieurs façons</h2><p>Chaque onglet est une représentation, avec son nom dans le '
             'programme et son nom courant. Tu peux les faire dans l\'ordre, ou commencer par celle que ton professeur te donne. '
             'Chaque exercice se vérifie dans la page et a sa correction complète.</p></section></details>')
    h.append('<div class="progression"><div class="barre" aria-hidden="true"><div id="barreProgression"></div></div>'
             '<p id="texteProgression" aria-live="polite"></p></div>')
    h.append('<div class="onglets" role="tablist" aria-label="Les représentations du cahier">')
    for i, (lib, pid2) in enumerate(onglets):
        h.append('<button type="button" class="onglet" role="tab" id="tab-%s" aria-controls="%s" aria-selected="%s" tabindex="%d">%s</button>'
                 % (pid2, pid2, "true" if i == 0 else "false", 0 if i == 0 else -1, lib))
    h.append("</div>")
    for i, (contenu, pid2) in enumerate(panneaux):
        h.append('<section class="panneau" role="tabpanel" id="%s" aria-labelledby="tab-%s"%s>%s</section>'
                 % (pid2, pid2, "" if i == 0 else " hidden", contenu))
    h.append("</main>")
    mentions = " ".join(at.MENTION_FICTION for at in ats)
    h.append('<footer class="pied"><p>%s</p><p>Technologie cycle 4 · programme 2024 · page utilisable sans Internet · ton travail '
             'reste dans ce navigateur, rien n\'est envoyé.</p></footer>' % mentions)
    h.append(moteur.fin_page({"page": pid, "exercices": defs}))
    return chemin, "".join(h)


def ecrire(tous, cahier, page_niveau, chemins_fn, ecrire_fn):
    n = 0
    for niv in ("5e", "4e", "3e"):
        ats = [a for a in tous if niv in a.NIVEAUX]
        if not ats:
            continue
        chemin, html = page(niv, ats, cahier, page_niveau, chemins_fn)
        ecrire_fn(chemin, html)
        n += 1
    return n
