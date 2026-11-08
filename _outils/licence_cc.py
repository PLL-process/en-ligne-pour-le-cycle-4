# -*- coding: utf-8 -*-
"""licence_cc.py — la mention de licence des pages, et le geste qui la pose.

Décision de Pascal du 08/11/2026 : tout le dépôt est sous **CC BY-NC-SA 4.0** (LICENSE.md),
et chaque page HTML lue par un élève ou un collègue porte la mention en pied (règle d'or
n°321). Ce module est la source unique du texte : `make_index.py`, `generer_lexique.py` et
`controle_licence.py --corriger` l'importent — personne ne recopie la phrase.

La mention est reconnue par son attribut `data-licence="cc-by-nc-sa"` : c'est lui que le
contrôle cherche, pas le texte, pour qu'un libellé retouché ne passe pas pour une absence.
"""
import re

URL = "https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr"
AUTEUR = "Pascal Gouacide"
ANNEE = "2026"
MARQUEUR = 'data-licence="cc-by-nc-sa"'

MENTION = (
    f'<p class="licence-cc" {MARQUEUR} style="font-size:.8em;opacity:.85;margin-top:.8em">'
    f'📄 Ressource sous licence <a href="{URL}" rel="license">CC BY-NC-SA 4.0</a> '
    f'— © {AUTEUR}, {ANNEE} · Technologie cycle 4 · réutilisation et adaptation libres '
    f'à condition de citer l’auteur, sans usage commercial et en partageant dans les mêmes conditions.</p>'
)

MENTION_MD = (
    f"📄 Ce dépôt est sous licence [CC BY-NC-SA 4.0]({URL}) — © {AUTEUR}, {ANNEE}. "
    f"Réutilisation et adaptation libres à condition de citer l’auteur, sans usage commercial "
    f"et en partageant dans les mêmes conditions. Voir `LICENSE.md`."
)


def porte_mention(html: str) -> bool:
    return MARQUEUR in html


def injecter(html: str) -> str:
    """Pose la mention une seule fois : avant le dernier `</footer>` s'il y en a un, sinon
    avant `</body>`, sinon à la fin du fichier. Retourne le texte inchangé s'il la porte déjà."""
    if porte_mention(html):
        return html
    for balise in ("</footer>", "</body>"):
        pos = html.lower().rfind(balise)
        if pos >= 0:
            return html[:pos] + MENTION + "\n" + html[pos:]
    return html.rstrip("\n") + "\n" + MENTION + "\n"


def retirer(html: str) -> str:
    """L'inverse d'`injecter` — pour les bancs et pour un retrait voulu, jamais appelé en production."""
    return re.sub(r'<p class="licence-cc" data-licence="cc-by-nc-sa"[^>]*>.*?</p>\n?', "", html, flags=re.S)
