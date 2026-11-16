# -*- coding: utf-8 -*-
"""tests_controle_consigne_question.py — le banc de la règle d'or n°335 (une consigne par question, une à la fois).

Chaque cas pose une page d'essai dans une racine vide, joue le contrôle, et vérifie qu'il refuse ce qu'il doit
refuser — l'étiquette « ▢1 : » que Pascal a relevée le 15/11/2026, la phrase à compléter — et SURTOUT qu'il laisse
passer une vraie question et une consigne à l'impératif : un contrôle qui refuse le juste finit désactivé.

Usage : python3 _outils/tests_controle_consigne_question.py
"""
import contextlib, io, os, pathlib, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_consigne_question as C  # noqa: E402
from tests_controle_cadres import par_la_ligne_de_commande  # noqa: E402

SEQ = "theme-3-essai/C9/3e/sequence_3e_essai.html"


def page(corps):
    return "<!doctype html><html lang='fr'><body>%s</body></html>" % corps


def question(enonce, ident="q1", classe="qcm-groupe"):
    return ('<fieldset class="%s" id="%s"><legend>%s</legend>'
            '<div class="qcm-option"><input type="radio" name="%s" id="%s_a" value="A"><label for="%s_a">A</label></div>'
            '<div class="qcm-option"><input type="radio" name="%s" id="%s_b" value="B"><label for="%s_b">B</label></div>'
            '</fieldset>') % (classe, ident, enonce, ident, ident, ident, ident, ident, ident)


def tableau(avant=""):
    return (avant + '<table class="recette"><tr><th>Essai</th><th>Attendu</th></tr>'
            '<tr><td>1</td><td>' + question("résultat attendu essai 1", "t1") + '</td></tr>'
            '<tr><td>2</td><td>' + question("résultat attendu essai 2", "t2") + '</td></tr></table>')


def jouer(racine, *args):
    # le périmètre des pages est celui de la n°331 : les deux modules lisent la racine
    anciens = C.DEPOT, C.n331.DEPOT; C.DEPOT = C.n331.DEPOT = str(racine); s = io.StringIO(); e = io.StringIO()
    try:
        with contextlib.redirect_stdout(s), contextlib.redirect_stderr(e):
            code = C.main(list(args) + [str(racine)])
    finally:
        C.DEPOT, C.n331.DEPOT = anciens
    return code, s.getvalue() + e.getvalue()


def main():
    echecs, n = [], 0

    def cas(titre, corps, attendu_code, attendu="", absent="", args=()):
        nonlocal n; n += 1
        with tempfile.TemporaryDirectory() as tmp:
            fichiers = corps if isinstance(corps, dict) else {SEQ: page(corps)}
            for rel, contenu in fichiers.items():
                p = pathlib.Path(tmp, rel); p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(contenu, encoding="utf-8")
            code, texte = jouer(tmp, *args)
        if code != attendu_code:
            echecs.append("%s : sortie %d au lieu de %d\n     %s" % (titre, code, attendu_code, texte.strip()[:500]))
        elif attendu and attendu not in texte:
            echecs.append("%s : message sans « %s »\n     %s" % (titre, attendu, texte.strip()[:500]))
        elif absent and absent in texte:
            echecs.append("%s : message avec « %s » alors qu'il ne devrait pas\n     %s" % (titre, absent, texte.strip()[:500]))

    # — n°299 : ne rien voir n'est pas être vert
    cas("une racine sans page élève est une panne", {"notes.md": "# rien"}, 2, "EN PANNE")
    cas("une page sans question passe", "<h2>Titre</h2><p>Lis le texte.</p>", 0, "✅ chaque question porte sa consigne")

    # — C1 : ce qui passe
    cas("une vraie question passe", question("Que vaut <code>passages</code> après la ligne 3 ?"), 0,
        "✅ chaque question porte sa consigne")
    cas("une consigne à l'impératif passe", question("Choisis la fonction du capteur."), 0, absent="C1 énoncé sans consigne —")
    cas("une consigne numérotée passe (« 2. Indique… »)", question("2. Indique la valeur affichée."), 0, absent="C1 énoncé sans consigne —")
    cas("la condition d'abord, puis l'impératif, passe (« Pour chaque essai, prédis… »)",
        question("Pour chaque essai, PRÉDIS ce que fait la pompe."), 0, absent="C1 énoncé sans consigne —")
    cas("une phrase longue avant la virgule n'est pas une condition", question(
        "Le capteur que tu as branché sur la broche A0 de la carte hier soir, choisis"), 0, "⚠ C1")
    cas("« ▢1 — Quel signe… ? » passe", question("▢1 — Quel signe compare l'air au seuil de 100 ?"), 0, absent="C1 énoncé sans consigne —")

    # — C1 : ce qui est relevé (le constat de Pascal, puis sa décision « tout réécrire »)
    cas("« ▢1 : » est relevé (⚠, sortie 0)", question("▢1 :"), 0, "⚠ C1 énoncé sans consigne")
    cas("« ▢1 : » refusé avec --strict (✘, sortie 1)", question("▢1 :"), 1, "✘ C1 énoncé sans consigne", args=("--strict",))
    cas("une condition en deux temps, puis l'impératif, passe", question("Pour chaque position, de 1 à 6, choisis l'étape."), 0,
        absent="C1 énoncé sans consigne —")
    cas("un nom qui ressemble à un impératif ne fait pas une consigne (« la mesure »)",
        question("« Comparer la mesure de l'écran à l'état réel du sol » est le test n°…"), 0, "⚠ C1")
    cas("« Mesurer aux points T1 → T4, dans l'ordre, UNE mesure à la fois » est relevé",
        question("Mesurer aux points T1 → T4, dans l'ordre, UNE mesure à la fois"), 0, "⚠ C1")
    cas("« Puis choisis… » passe", question("Puis choisis la bonne valeur."), 0, absent="C1 énoncé sans consigne —")
    cas("une phrase à compléter est relevée", question("Après la ligne 3, passages vaut :"), 0, "⚠ C1")
    cas("une définition à finir est relevée", question("Une variable, en informatique, c'est…"), 0, "⚠ C1")
    cas("une étiquette d'association est relevée", question("Le relais"), 0, "⚠ C1")
    cas("une rangée de réponses courtes est une question comme une autre",
        question("▢2 :", "r2", "qcm-groupe qcm-rangee"), 0, "⚠ C1")
    cas("le compte des C1 est juste (2 relevés, 1 juste)",
        question("▢1 :", "a") + question("Le relais", "b") + question("Quel est le seuil ?", "c"), 0, "2 C1 (énoncé sans consigne)")

    # — C2 : les tableaux et les grilles portent leur consigne juste au-dessus
    cas("un tableau de questions sans consigne au-dessus est relevé, une seule fois", tableau("<h4>Le tableau d'essais</h4>"), 0,
        "1 C2 (tableau ou grille sans consigne)")
    cas("ses cases ne sont pas comptées en C1", tableau("<h4>Le tableau d'essais</h4>"), 0, "0 C1")
    cas("le même tableau avec sa consigne juste au-dessus passe",
        tableau("<h4>Le tableau d'essais</h4><p>① Choisis le résultat attendu de chaque essai.</p>"), 0, "0 C2")
    defilant = lambda avant: avant + '<div class="grille-conforme"><div class="defile">' + tableau() + '</div></div>'
    cas("un tableau qui défile prend la consigne posée avant son enveloppe",
        defilant("<p>Pour chaque ligne : ① PRÉDIS l'attendu.</p>"), 0, "0 C2")
    cas("le même tableau défilant, sans consigne, est relevé", defilant("<h4>La grille</h4>"), 0, "1 C2")
    cas("une question juste au-dessus vaut consigne", tableau("<p>Que doit faire la pompe à chaque essai ?</p>"), 0, "0 C2")
    grille = '<div class="grille">' + question("Bloc 1", "g1", "qcm-groupe qcm-grille") + question("Bloc 2", "g2", "qcm-groupe qcm-grille") + "</div>"
    cas("une grille lettrée sans consigne est relevée", "<h4>Les blocs</h4>" + grille, 0, "1 C2")
    cas("la même grille avec sa consigne passe", "<p>Associe chaque bloc à sa lettre.</p>" + grille, 0, "0 C2")
    rangees = question("Bloc 1", "g1", "qcm-groupe qcm-grille") + question("Bloc 2", "g2", "qcm-groupe qcm-grille") + question("Bloc 3", "g3", "qcm-groupe qcm-grille")
    cles = '<div class="qcm-cles">Les réponses possibles — choisis une lettre pour chaque ligne : A le début, B la fin</div>'
    cas("des rangées à la suite font UNE grille, relevée une fois", "<h4>Les blocs</h4>" + cles + rangees, 0, "1 C2")
    cas("le bloc des réponses lettrées ne vaut pas consigne (en mission, il devient la réserve d'étiquettes)",
        "<h4>Les blocs</h4>" + cles + rangees, 0, "⚠ C2")
    cas("la consigne posée avant le bloc des réponses compte", "<p>Associe chaque bloc à sa place dans l'algorigramme.</p>" + cles + rangees, 0, "0 C2")

    # — le point d'entrée parle et sort proprement (n°299)
    code, texte = par_la_ligne_de_commande("controle_consigne_question.py", ["--muet"])
    if code != 0:
        echecs.append("lancé en ligne de commande, le contrôle sort à %d :\n     %s" % (code, texte.strip()[:400]))
    if not any(c.isdigit() for c in texte):
        echecs.append("lancé en ligne de commande, le contrôle n'écrit AUCUN chiffre (règle n°299)")

    if echecs:
        print("✘ %d/%d cas en échec :" % (len(echecs), n))
        for e in echecs:
            print(" -", e)
        return 1
    print("✅ %d/%d cas passent — controle_consigne_question.py relève les énoncés sans consigne et laisse passer le juste" % (n, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
