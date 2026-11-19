#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""changer_proposition.py — changer le texte d'une proposition de bouton radio partout où il vit (skill
propositions-sans-indice, § 3 ; règle d'or n°341), en une fois : value, aria-label, title et texte du <label>,
data-pourquoi, réponse attendue dans le script (groupe:"…"), clé du mission_<lot>.json.

Module, pas une commande : on l'importe dans un petit script de passe.
    from changer_proposition import changer
    s = changer(s, mission, "d3_1", "ancien texte", "nouveau texte", pourquoi=None)
`pourquoi` remplace le data-pourquoi (et le pourquoi du mission_<lot>.json) ; None garde l'ancien.
Dans le mission_<lot>.json, une clé peut n'être que le début du texte (« casse » pour « casse le détecteur ») : elle
est retrouvée comme le fait mode_mission/enrichir.py, puis réécrite avec le texte entier (correction du 19/11/2026 :
une clé « début de texte » restait sur l'ancienne proposition, et enrichir.py --verifier refusait la page).
Après la passe : `python3 _outils/mode_mission/enrichir.py <page> <mission> --verifier` doit dire « à jour ».
Une proposition introuvable lève une erreur : rien n'est changé à moitié.
Après : banc du lot, tests_regle_311, mode_mission/banc_generique.mjs, controle_propositions_indices.py."""
import html, json, re

def esc_attr(t):
    return t.replace("&", "&amp;").replace('"', "&quot;").replace("'", "&#x27;")

def esc_pourquoi(t):
    # même écriture que mode_mission/enrichir.py (attr) : l'apostrophe reste telle quelle entre guillemets doubles
    return html.escape(t, quote=True).replace("&#x27;", "'")

def esc_txt(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def changer(page_txt, mission, groupe, ancien, nouveau, pourquoi=None):
    """Retourne le texte de page modifié ; modifie `mission` (dict) sur place."""
    s = page_txt
    va, vn = esc_attr(ancien), esc_attr(nouveau)
    motif = re.compile(r'(<input type="radio" name="%s" id="%s__\d+" value=")%s("(?: aria-label="[^"]*")?(?: data-pourquoi="[^"]*")?>)(<label for="%s__\d+"(?: title="[^"]*")?>)(.*?)(</label>)'
                       % (re.escape(groupe), re.escape(groupe), re.escape(va), re.escape(groupe)))
    m = motif.search(s)
    assert m, (groupe, ancien)
    debut, fin_input, lab_ouv, lab_txt, lab_fer = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
    fin_input = fin_input.replace('aria-label="' , 'aria-label="', 1)
    if pourquoi is not None:
        if 'data-pourquoi="' in fin_input:
            fin_input = re.sub(r'data-pourquoi="[^"]*"', 'data-pourquoi="%s"' % esc_pourquoi(pourquoi).replace('\\', '\\\\'), fin_input)
        else:
            fin_input = fin_input[:-2] + ' data-pourquoi="%s">' % esc_pourquoi(pourquoi) if fin_input.endswith('">') else fin_input
    fin_input = re.sub(r'(aria-label="[A-D] — )[^"]*"', lambda k: k.group(1) + vn + '"', fin_input)
    lab_ouv = re.sub(r'title="[^"]*"', 'title="%s"' % vn, lab_ouv)
    if lab_txt.strip() not in "ABCD" or len(lab_txt.strip()) != 1:
        lab_txt = esc_txt(nouveau)
    s = s[:m.start()] + debut + vn + fin_input + lab_ouv + lab_txt + lab_fer + s[m.end():]
    # la réponse attendue dans le script : groupe:"ancien"
    js_old = '%s:"%s"' % (groupe, ancien.replace('"', '\\"'))
    if js_old in s:
        assert s.count(js_old) == 1, js_old
        s = s.replace(js_old, '%s:"%s"' % (groupe, nouveau.replace('"', '\\"')))
    # le mission_<lot>.json : les « pourquoi » sont rangés par texte de proposition
    if mission is not None:
        du_groupe = None
        if isinstance(mission, dict):
            if isinstance(mission.get('pourquoi'), dict) and isinstance(mission['pourquoi'].get(groupe), dict):
                du_groupe = mission['pourquoi'][groupe]
            elif isinstance(mission.get(groupe), dict):
                du_groupe = mission[groupe]
        if du_groupe is not None:
            # la clé exacte, sinon la seule clé qui est un début de l'ancien texte (comme enrichir.py)
            cle = ancien if ancien in du_groupe else None
            if cle is None:
                debuts = [k for k in du_groupe if ancien.startswith(k)]
                assert len(debuts) <= 1, (groupe, ancien, debuts)
                cle = debuts[0] if debuts else None
            cibles = [(du_groupe, cle)] if cle is not None else []
        else:
            cibles = [(b, ancien) for b in _blocs(mission) if ancien in b]
        for bloc, cle in cibles:
            items = list(bloc.items()); bloc.clear()
            for k, v in items:
                if k == cle:
                    bloc[nouveau] = pourquoi if pourquoi is not None else v
                else:
                    bloc[k] = v
    return s

def _blocs(o):
    if isinstance(o, dict):
        yield o
        for v in o.values():
            yield from _blocs(v)
    elif isinstance(o, list):
        for v in o:
            yield from _blocs(v)
