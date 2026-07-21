# -*- coding: utf-8 -*-
"""Génère des QCM au modèle exact de QCM_XXL_40_Reseaux (fixed3).
Types de questions :
  ("m", comp, question, [options], good_idx, aide)            -> radio, checkMCQ
  ("M", comp, question, [options], [good_idx...], aide)       -> checkboxes, checkMulti
  ("t", comp, question, [mots_cles], placeholder, aide)       -> texte, checkTextIncludes
  ("n", comp, question, nombre, aide)                          -> nombre, checkNumber
"""
import re, html, json

MODEL = "theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.7/qcm_xxl_40_reseaux_ip_nfc_rfid_zigbee.html"


def load_model_parts(model_path=MODEL):
    t = open(model_path, encoding="utf-8").read()
    style = re.search(r"<style>(.*?)</style>", t, re.S).group(1)
    script = re.search(r"<script>(.*?)</script>", t, re.S).group(1)
    top_start = t.find('<div class="wrap">')
    first_sec = t.find('<section class="card"')
    top_block = t[top_start:first_sec]
    bot_start = t.find('<div class="footer">')
    bot_end = t.find('<!-- Fin du wrap -->')
    bottom_block = t[bot_start:bot_end] + '<!-- Fin du wrap -->'
    return style, script, top_block, bottom_block


def esc(s):
    return html.escape(s, quote=False)


def card(idx, item):
    typ = item[0]
    comp = item[1]
    q = esc(item[2])
    n = idx
    head = (f'<section class="card" data-competence="{comp}" data-points="1">\n'
            f'  <p class="q-title">{q}</p>\n'
            f'  <span class="badge">Compétence visée : {comp}</span>\n'
            f'  <span class="pts">(1 pt)</span>\n')
    tail_btn = lambda call: (f'  <div class="row">\n'
            f'    <button class="btn small" onclick="aide(\'a{n}\')">Aide</button>\n'
            f'    <button class="btn small" onclick="{call}">Corriger</button>\n'
            f'  </div>\n')
    if typ == "m":
        opts, good, help_ = item[3], item[4], item[5]
        body = "".join(f'  <label><input type="radio" name="q{n}" value="v{i}"> {esc(o)}</label>\n' for i, o in enumerate(opts))
        call = f"checkMCQ('q{n}','v{good}','fb{n}',1)"
    elif typ == "M":
        opts, goods, help_ = item[3], item[4], item[5]
        body = "".join(f'  <label><input type="checkbox" name="q{n}" value="v{i}"> {esc(o)}</label>\n' for i, o in enumerate(opts))
        arr = json.dumps([f"v{g}" for g in goods]).replace('"', "'")
        call = f"checkMulti('q{n}',{arr},'fb{n}',1)"
    elif typ == "t":
        kws, ph, help_ = item[3], item[4], item[5]
        body = f'  <input type="text" id="q{n}" placeholder="{esc(ph)}">\n'
        arr = json.dumps(kws, ensure_ascii=False).replace('"', "'")
        call = f"checkTextIncludes('q{n}',{arr},'fb{n}',1)"
    elif typ == "n":
        num, help_ = item[3], item[4]
        body = f'  <input type="number" id="q{n}" placeholder="Nombre">\n'
        call = f"checkNumber('q{n}',{num},'fb{n}',1)"
    else:
        raise ValueError(typ)
    return (head + body + tail_btn(call)
            + f'  <div id="a{n}" class="help">{esc(help_)}</div>\n'
            + f'  <div id="fb{n}" class="answer"></div>\n</section>\n')


def build_qcm(title, note, bank, out_path, model_path=MODEL):
    style, script, top_block, bottom_block = load_model_parts(model_path)
    top_block = re.sub(r'<div class="note">Les questions ciblent.*?</div>',
                       '<div class="note">' + note + '</div>', top_block, flags=re.S)
    cards = "".join(card(i + 1, it) for i, it in enumerate(bank))
    doc = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <style>{style}</style>
</head>
<body>
  <header><h1>{esc(title)}</h1></header>
  {top_block}
{cards}
    {bottom_block}
  <script>{script}</script>
</body>
</html>
"""
    open(out_path, "w", encoding="utf-8").write(doc)
    return len(bank)


def sanity_check(path):
    """Vérifie l'équilibre des balises et la cohérence ids/onclick."""
    t = open(path, encoding="utf-8").read()
    n_sec = len(re.findall(r'<section class="card" data-competence', t))
    fbs = set(re.findall(r'id="(fb\d+)"', t))
    calls = set(re.findall(r"'(fb\d+)'", t))
    missing = calls - fbs
    return n_sec, sorted(missing)
