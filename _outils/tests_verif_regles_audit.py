# -*- coding: utf-8 -*-
"""tests_verif_regles_audit.py — le banc du vérificateur de règles d'audit.

POURQUOI CE BANC EXISTE SEULEMENT AUJOURD'HUI
---------------------------------------------
`verif_regles_audit.py` est l'outil le plus lu du dépôt : c'est lui qui écrit
« 60 séquence(s) analysée(s) · 136 manquement(s) » à la fin de chaque lot. Il
n'avait aucun banc. Or il rendait **0 dans tous les cas** — y compris sur une
cible mal écrite en argument, qui donnait « 0 séquence(s) analysée(s) » suivi
d'une sortie 0. Quelqu'un qui se trompe d'un caractère en passant un chemin
obtient donc un contrôle vert sur rien.

Le balayage du 19/09/2026 a mesuré la même chose sur les seize autres contrôles
du dépôt : recopiés dans une racine vide, **tous** sortaient à 0.

CE QUE CE BANC VÉRIFIE
----------------------
Deux choses, et la seconde est le second corollaire de la règle d'or n°299 :
que le contrôle voie ce qu'il doit voir, et qu'il le voie **par son point
d'entrée**, lancé en sous-processus comme on le lance vraiment.

Il éprouve les règles d'or n°300, n°301 et n°302 — les seules qu'il juge au fond,
parce qu'elles sont nées de ce chantier — et ne juge PAS la justesse des
autres règles mécaniques : elles ont
leur propre histoire dans le journal, et les éprouver une à une demanderait un
lot d'essai complet. Ce banc tient la porte d'entrée et la panne — c'est son
périmètre, et il le déclare (règle d'or n°47).

Usage : python3 _outils/tests_verif_regles_audit.py
"""
import contextlib
import io
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verif_regles_audit as V  # noqa: E402

ICI = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(ICI, "verif_regles_audit.py")

SEQUENCE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>Essai</title></head>
<body><h1>Une séquence d'essai</h1><p>Rien de particulier.</p></body></html>
"""


def jouer(argv):
    """`main()` appelé en direct — stdout ET stderr, car la panne part sur stderr."""
    sortie, erreur = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(erreur):
        code = V.main(argv)
    return code, sortie.getvalue() + erreur.getvalue()


def par_la_ligne_de_commande(args=()):
    """Le contrôle lancé comme on le lance vraiment (règle d'or n°299).

    Un banc qui se contente d'appeler `main()` ne passe jamais par le point
    d'entrée : c'est ainsi que `controle_impression.mjs` est resté muet
    dix-sept jours sous un banc vert.
    """
    r = subprocess.run([sys.executable, SCRIPT] + list(args),
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=900)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    echecs, n = [], 0

    def cas(titre, fait):
        nonlocal n
        n += 1
        try:
            ennui = fait()
        except Exception as e:                      # noqa: BLE001
            ennui = "le banc lui-même a levé — %s" % e
        if ennui:
            echecs.append("%s : %s" % (titre, ennui))

    # ── 1. La panne : règle d'or n°299 ─────────────────────────────────────
    def cible_introuvable():
        code, texte = jouer(["verif_regles_audit.py", "theme-42-qui-nexiste-pas"])
        if code != 2:
            return ("sortie %d au lieu de 2 — une cible mal écrite donnait « 0 séquence(s) "
                    "analysée(s) » et un contrôle vert" % code)
        return None if "EN PANNE" in texte else "la panne n'est pas annoncée sur stderr"

    cas("une cible qui n'existe pas est une panne, pas « 0 manquement »", cible_introuvable)

    def racine_sans_sequence():
        bac = pathlib.Path(tempfile.mkdtemp())
        ancien = V.RACINE
        try:
            (bac / "lot").mkdir()
            (bac / "lot" / "qcm_x.html").write_text(SEQUENCE, encoding="utf-8")
            V.RACINE = bac
            code, texte = jouer(["verif_regles_audit.py"])
        finally:
            V.RACINE = ancien
            shutil.rmtree(bac, ignore_errors=True)
        if code != 2:
            return "sortie %d au lieu de 2 — aucune séquence, et le contrôle se dit content" % code
        return None if "EN PANNE" in texte else "la panne n'est pas annoncée"

    cas("une racine sans séquence est une panne (un QCM n'est pas une séquence)",
        racine_sans_sequence)

    # ── 2. Ce qu'il doit voir : les trois motifs de nom ─────────────────────
    def les_trois_motifs():
        bac = pathlib.Path(tempfile.mkdtemp())
        ancien = V.RACINE
        try:
            (bac / "lot").mkdir()
            # Les trois formes que l'outil déclare regarder. Le trait d'union a
            # été ajouté après coup : six séquences étaient invisibles.
            for nom in ("sequence_a.html", "sequence-b.html", "sequence.html"):
                (bac / "lot" / nom).write_text(SEQUENCE, encoding="utf-8")
            V.RACINE = bac
            code, texte = jouer(["verif_regles_audit.py"])
        finally:
            V.RACINE = ancien
            shutil.rmtree(bac, ignore_errors=True)
        if code != 0:
            return "sortie %d au lieu de 0" % code
        if "3 séquence(s) analysée(s)" not in texte:
            return ("les trois formes de nom ne sont pas toutes vues :\n     %s"
                    % texte.strip()[-300:])
        return None

    cas("sequence_x.html, sequence-x.html et sequence.html sont vues toutes les trois",
        les_trois_motifs)

    def archive_ecartee():
        bac = pathlib.Path(tempfile.mkdtemp())
        ancien = V.RACINE
        try:
            (bac / "_archive-anciennes-versions").mkdir()
            (bac / "_archive-anciennes-versions" / "sequence_v1.html").write_text(
                SEQUENCE, encoding="utf-8")
            (bac / "lot").mkdir()
            (bac / "lot" / "sequence_a.html").write_text(SEQUENCE, encoding="utf-8")
            V.RACINE = bac
            code, texte = jouer(["verif_regles_audit.py"])
        finally:
            V.RACINE = ancien
            shutil.rmtree(bac, ignore_errors=True)
        if code != 0:
            return "sortie %d au lieu de 0" % code
        if "1 séquence(s) analysée(s)" not in texte:
            return ("l'archive n'est pas écartée, ou la séquence hors archive n'est pas "
                    "lue :\n     %s" % texte.strip()[-300:])
        return None

    # Deux séquences, pas une : sans celle hors archive, la racine ne ferait
    # RIEN analyser et le cas passerait au vert en ne prouvant rien.
    cas("l'archive est une trace, pas une ressource — et le reste est bien analysé",
        archive_ecartee)


    # ── 4. La règle d'or n°300 — la question occupe le flux ────────────────
    LISTE = """<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>Essai</title></head><body><main>
<div class="assoc"><label for="q1">Une question ?</label>
  <select id="q1"><option value="">— choisir —</option>
    <option>oui</option><option>non</option></select></div>
</main></body></html>
"""
    RADIOS = """<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>Essai</title></head><body><main>
<fieldset class="qcm-groupe" id="q1"><legend>Une question ?</legend>
  <div class="qcm-option"><input type="radio" name="q1" id="q1__1" value="oui">
    <label for="q1__1">oui</label></div>
  <div class="qcm-option"><input type="radio" name="q1" id="q1__2" value="non">
    <label for="q1__2">non</label></div>
</fieldset>
</main></body></html>
"""

    def etat_300(source):
        """L'état rendu par la n°300 sur une séquence d'essai."""
        bac = pathlib.Path(tempfile.mkdtemp())
        ancien = V.RACINE
        try:
            (bac / "lot").mkdir()
            (bac / "lot" / "sequence_a.html").write_text(source, encoding="utf-8")
            V.RACINE = bac
            _code, texte = jouer(["verif_regles_audit.py"])
        finally:
            V.RACINE = ancien
            shutil.rmtree(bac, ignore_errors=True)
        for ligne in texte.splitlines():
            if "n°300" in ligne and ("✔" in ligne or "✘" in ligne):
                return ("ECHEC" if "✘" in ligne else "OK"), ligne.strip()
        return "ABSENT", texte.strip()[-300:]

    cas("une liste déroulante de question est refusée (n°300)", lambda: (
        lambda e: None if e[0] == "ECHEC"
        else "état %s au lieu de ECHEC — %s" % e)(etat_300(LISTE)))

    cas("le gabarit du pilote — fieldset, legend, boutons radio — passe (n°300)", lambda: (
        lambda e: None if e[0] == "OK"
        else "état %s au lieu de OK — %s" % e)(etat_300(RADIOS)))

    cas("le refus NOMME les champs en cause, il ne dit pas seulement « non »", lambda: (
        lambda e: None if "q1" in e[1] else "le message ne nomme pas q1 : %s" % e[1])(etat_300(LISTE)))

    cas("une case à cocher n'est PAS refusée — elle reste légitime à plusieurs réponses", lambda: (
        lambda e: None if e[0] == "OK" else "état %s au lieu de OK — %s" % e)(
            etat_300(RADIOS.replace('type="radio"', 'type="checkbox"'))))

    cas("le dépôt réel : 3e_C1.1 est au vert sur la n°300", lambda: (
        lambda t: None if "✔ n°300" in t
        else "3e_C1.1 n'est pas au vert : %s" % ([l for l in t.splitlines() if "n°300" in l] or "(rien)"))(
            par_la_ligne_de_commande([
                "theme-1-objets-systemes-usages-interactions/"
                "C1-decrire-les-liens-entre-usages-et-evolutions/3e/3e_C1.1"])[1]))


    # ── 5. La règle d'or n°301 — le bilan clôt la séquence ─────────────────
    def page(corps):
        return ('<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
                '<title>Essai</title></head><body><main>' + corps + '</main></body></html>')

    BILAN = '<section><h3>📍 Je me positionne</h3><textarea id="pos1"></textarea></section>'
    BONUS = '<section><h2>🎁 Bonus (facultatif)</h2><p>Un défi à lire.</p></section>'

    def etat_301(corps):
        """L'état rendu par la n°301 sur une séquence d'essai."""
        bac = pathlib.Path(tempfile.mkdtemp())
        ancien = V.RACINE
        try:
            (bac / "lot").mkdir()
            (bac / "lot" / "sequence_a.html").write_text(page(corps), encoding="utf-8")
            V.RACINE = bac
            _code, texte = jouer(["verif_regles_audit.py"])
        finally:
            V.RACINE = ancien
            shutil.rmtree(bac, ignore_errors=True)
        for ligne in texte.splitlines():
            if "n°301" in ligne and ("✔" in ligne or "✘" in ligne):
                return ("ECHEC" if "✘" in ligne else "OK"), ligne.strip()
        return "ABSENT", texte.strip()[-300:]

    cas("une séquence sans aucun bilan est refusée (n°301)", lambda: (
        lambda e: None if e[0] == "ECHEC" and "aucun bilan" in e[1]
        else "état %s — %s" % e)(etat_301('<section><h2>Activité</h2></section>')))

    cas("un Bonus placé APRÈS le bilan est refusé", lambda: (
        lambda e: None if e[0] == "ECHEC" and "APRÈS le bilan" in e[1]
        else "état %s — %s" % e)(etat_301(BILAN + BONUS)))

    cas("le même Bonus placé AVANT le bilan passe", lambda: (
        lambda e: None if e[0] == "OK" else "état %s — %s" % e)(etat_301(BONUS + BILAN)))

    cas("une séquence à bilan et sans Bonus passe", lambda: (
        lambda e: None if e[0] == "OK" else "état %s — %s" % e)(etat_301(BILAN)))

    cas("le bilan est reconnu sous ses autres écritures — « Mon auto-positionnement »", lambda: (
        lambda e: None if e[0] == "OK" else "état %s — %s" % e)(
            etat_301('<section><h3>Mon auto-positionnement</h3><textarea id="ap1"></textarea></section>')))

    cas("le bilan est reconnu au seul titre « Bilan personnel »", lambda: (
        # Cas réel : 4e_C8. Le titre est la SEULE marque ici — le champ porte une
        # étiquette neutre — sans quoi ce cas passerait encore en retirant
        # « bilan personnel » du motif, et ne prouverait donc rien.
        lambda e: None if e[0] == "OK" else "état %s — %s" % e)(
            etat_301('<section><h2>🙋 Bilan personnel</h2>'
                     '<input id="b1" aria-label="Ce que tu as appris"></section>')))

    cas("le bilan est reconnu quand la phrase ne vit que dans un aria-label", lambda: (
        lambda e: None if e[0] == "OK" else "état %s — %s" % e)(
            etat_301('<section><h2>🙋 Pour finir</h2>'
                     '<input id="b1" aria-label="Auto-positionnement 1"></section>')))

    cas("la n°301 ne juge PAS les champs du Bonus — c'est déclaré, pas oublié", lambda: (
        # un Bonus sans champ, placé AVANT le bilan, doit passer ici : délimiter
        # son bloc demande d'analyser l'arbre, et c'est audit_cloture_sequence.mjs
        # qui le mesure. Ce cas tient la frontière entre les deux outils.
        lambda e: None if e[0] == "OK" else "état %s — %s" % e)(etat_301(BONUS + BILAN)))

    # ── 6. La règle d'or n°302 — on parle À l'élève ────────────────────────
    def etat_302(corps):
        bac = pathlib.Path(tempfile.mkdtemp())
        ancien = V.RACINE
        try:
            (bac / "lot").mkdir()
            (bac / "lot" / "sequence_a.html").write_text(page(corps), encoding="utf-8")
            V.RACINE = bac
            _code, texte = jouer(["verif_regles_audit.py"])
        finally:
            V.RACINE = ancien
            shutil.rmtree(bac, ignore_errors=True)
        for ligne in texte.splitlines():
            if "n°302" in ligne and ("V" in ligne or "X" in ligne or "✔" in ligne or "✘" in ligne):
                return ("ECHEC" if "✘" in ligne else "OK"), ligne.strip()
        return "ABSENT", texte.strip()[-300:]

    cas("un en-tete de colonne qui parle de l'eleve est refuse (n°302)", lambda: (
        lambda e: None if e[0] == "ECHEC" else "etat %s - %s" % e)(
            etat_302('<table><tr><th>Ce que l\'élève doit savoir faire</th></tr></table>' + BILAN)))

    cas("le meme en-tete a la premiere personne passe", lambda: (
        lambda e: None if e[0] == "OK" else "etat %s - %s" % e)(
            etat_302('<table><tr><th>Je serai capable de…</th></tr></table>' + BILAN)))

    cas("un vouvoiement dans un intitule est refuse", lambda: (
        lambda e: None if e[0] == "ECHEC" else "etat %s - %s" % e)(
            etat_302('<h2>Si vous êtes trois ou quatre</h2>' + BILAN)))

    cas("la prose du corps n'est PAS jugee - c'est declare, pas oublie", lambda: (
        lambda e: None if e[0] == "OK" else "etat %s - %s" % e)(
            etat_302('<p>Ici, l\'élève observe le système.</p>' + BILAN)))

    cas("la legende d\'un groupe de questions est un enonce, pas un intitule", lambda: (
        lambda e: None if e[0] == "OK" else "etat %s - %s" % e)(
            etat_302('<fieldset class="qcm-groupe" id="q1">'
                     '<legend>Un mot de passe partagé entre tous les élèves :</legend>'
                     '<input type="radio" name="q1" id="q1a" value="oui">'
                     '<label for="q1a">oui</label></fieldset>' + BILAN)))

    cas("un commentaire CSS citant une balise ne doit pas etre lu comme un intitule", lambda: (
        # Cas reel : la n°300 a laisse dans la feuille de style un commentaire
        # ou figure le mot <legend>. Sans retrait du style, le moteur ouvrait
        # une balise qu'il refermait sur la premiere vraie legende venue.
        lambda e: None if e[0] == "OK" else "etat %s - %s" % e)(
            etat_302('<style>/* L\'enonce vit dans la <legend> : vous ne pouvez pas '
                     'le recouvrir */</style>'
                     '<fieldset class=\"qcm-groupe\" id=\"q9\"><legend>Une question ordinaire ?</legend>'
                     '<input type=\"radio\" name=\"q9\" id=\"q9a\" value=\"oui\"><label for=\"q9a\">oui</label></fieldset>' + BILAN)))

    # ── 7. La liste d'exceptions de la n°302 — et ses bornes ───────────────
    # Tranché par Pascal : « La mairie vous appelle » est une parole RAPPORTÉE,
    # attribuée à un tiers nommé. Ce qui suit vérifie que la tolérance est bien
    # BORNÉE : par fichier ET par phrase, jamais l'une sans l'autre.
    TOLERE = "sequence_3e_C9.2-C8.3_station_1_besoin-et-algorithme.html"
    PHRASE = "<h2>📞 Séance 1 — « La mairie vous appelle » : du besoin à l'algorithme</h2>"

    def etat_302_nomme(corps, nom):
        bac = pathlib.Path(tempfile.mkdtemp())
        ancien = V.RACINE
        try:
            (bac / "lot").mkdir()
            (bac / "lot" / nom).write_text(page(corps), encoding="utf-8")
            V.RACINE = bac
            _code, texte = jouer(["verif_regles_audit.py"])
        finally:
            V.RACINE = ancien
            shutil.rmtree(bac, ignore_errors=True)
        for ligne in texte.splitlines():
            if "n°302" in ligne and ("\u2714" in ligne or "\u2718" in ligne):
                return ("ECHEC" if "\u2718" in ligne else "OK"), ligne.strip()
        return "ABSENT", texte.strip()[-300:]

    cas("la phrase tolérée passe, dans le fichier où elle est tolérée", lambda: (
        lambda e: None if e[0] == "OK" else "état %s — %s" % e)(
            etat_302_nomme(PHRASE + BILAN, TOLERE)))

    cas("la MÊME phrase est refusée dans un AUTRE fichier", lambda: (
        # la tolérance est attachée au fichier : sans cela, elle deviendrait une
        # exemption générale pour « la narration », que personne ne saurait appliquer
        lambda e: None if e[0] == "ECHEC" else "état %s — %s" % e)(
            etat_302_nomme(PHRASE + BILAN, "sequence_autre_lot.html")))

    cas("un AUTRE vouvoiement reste refusé dans le fichier toléré", lambda: (
        # la tolérance est attachée à la phrase : le fichier n'est pas blanchi
        lambda e: None if e[0] == "ECHEC" else "état %s — %s" % e)(
            etat_302_nomme("<h2>Si vous êtes trois ou quatre</h2>" + BILAN, TOLERE)))

    cas("la liste d'exceptions ne dépasse pas cinq entrées", lambda: (
        lambda n: None if n <= 5 else
        "%d entrées : c'est la règle qu'il faut revoir, pas la liste qu'il faut rallonger" % n)(
            sum(len(v) for v in V.EXCEPTIONS_302.values())))

    # ── 3. Le VRAI point d'entrée, en sous-processus ───────────────────────
    def ligne_de_commande():
        code, texte = par_la_ligne_de_commande()
        if code != 0:
            return "sortie %d :\n     %s" % (code, texte.strip()[:400])
        if "séquence(s) analysée(s)" not in texte:
            return ("le script n'écrit pas son compte — un script muet ne prouve rien :\n"
                    "     %s" % (texte.strip()[:400] or "(rien du tout)"))
        return None

    cas("lancé en ligne de commande, le contrôle analyse le dépôt et le chiffre",
        ligne_de_commande)

    def sortie_json():
        code, texte = par_la_ligne_de_commande(["--json"])
        if code != 0:
            return "sortie %d" % code
        return None if texte.lstrip().startswith("[") else "la sortie --json n'est pas un tableau JSON"

    cas("--json rend un tableau, par la ligne de commande aussi", sortie_json)

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n))
        return 1
    print("✅ %d contrôles — le vérificateur voit les trois formes de nom, écarte l'archive, "
          "et refuse de sortir vert sans avoir analysé une séquence" % n)
    print("\n%d / %d" % (n, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
