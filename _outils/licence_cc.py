# -*- coding: utf-8 -*-
"""licence_cc.py — la mention de licence des pages, et le geste qui la pose.

Décision de Pascal du 08/11/2026 : tout le dépôt est sous **CC BY-NC-SA 4.0** (LICENSE.md),
et chaque page HTML lue par un élève ou un collègue porte la mention en pied (règle d'or
n°321). Ce module est la source unique du texte : `make_index.py`, `generer_lexique.py` et
`controle_licence.py --corriger` l'importent — personne ne recopie la phrase.

La mention est reconnue par son attribut `data-licence="cc-by-nc-sa"` : c'est lui que le
contrôle cherche, pas le texte, pour qu'un libellé retouché ne passe pas pour une absence.

Le lien porte sa couleur par une feuille posée avec la mention — `a` ET `a:visited` en `color:inherit`,
souligné, et `#000` sur papier : sur 91 pages sans règle de couleur pour `a`, il restait au bleu par
défaut du navigateur (2,03:1 sur fond sombre, règle d'or n°303, 10/11/2026). Un `style` en ligne sur le
lien (audit externe, étape 2) ne suffisait pas : il ne peut pas dire l'état visité, et sur un pied de page
imprimé en gris clair (QCM de 4e_C2.1) l'héritage tombait à 2,54:1.
"""
import re

URL = "https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr"
AUTEUR = "Pascal Gouacide"
ANNEE = "2026"
MARQUEUR = 'data-licence="cc-by-nc-sa"'

MENTION = (
    '<style>.licence-cc a,.licence-cc a:visited{color:inherit;text-decoration:underline}@media print{.licence-cc a,.licence-cc a:visited{color:#000}}</style>'
    f'<p class="licence-cc" {MARQUEUR} style="font-size:.85em;margin-top:.8em">'
    f'📄 Ressource sous licence <a href="{URL}" rel="license">CC BY-NC-SA 4.0</a> '
    f'— © {AUTEUR}, {ANNEE} · Technologie cycle 4 · réutilisation et adaptation libres '
    f'à condition de citer l’auteur, sans usage commercial et en partageant dans les mêmes conditions.</p>'
)

MENTION_MD = (
    f"📄 Ce dépôt est sous licence [CC BY-NC-SA 4.0]({URL}) — © {AUTEUR}, {ANNEE}. "
    f"Réutilisation et adaptation libres à condition de citer l’auteur, sans usage commercial "
    f"et en partageant dans les mêmes conditions. Voir `LICENSE.md`."
)


# Hors de tout repère, la mention est du « texte hors repère » (axe-core `region`, mesuré le 26/11/2026 : 49 pages
# où elle suivait `</main>`). Quand la page n'a pas de pied, elle en reçoit un : `<footer>` au premier niveau est le
# repère « informations sur le document ». Sans style propre, il ne change rien au rendu.
PIED = "<footer>" + MENTION + "</footer>"

_MASQUE = re.compile(r"<!--.*?-->|<script\b.*?</script>|<style\b.*?</style>", re.S | re.I)
_REPERES = ("main", "footer", "header", "nav", "aside")


def porte_mention(html: str) -> bool:
    return MARQUEUR in html


def injecter(html: str) -> str:
    """Pose la mention une seule fois : avant le dernier `</footer>` s'il y en a un, sinon dans
    un pied neuf (`PIED`) avant `</body>`, sinon à la fin du fichier. Retourne le texte inchangé
    s'il la porte déjà."""
    if porte_mention(html):
        return html
    pos = html.lower().rfind("</footer>")
    if pos >= 0:
        return html[:pos] + MENTION + "\n" + html[pos:]
    pos = html.lower().rfind("</body>")
    if pos >= 0:
        return html[:pos] + PIED + "\n" + html[pos:]
    return html.rstrip("\n") + "\n" + MENTION + "\n"


def hors_repere(html: str, pos: int) -> bool:
    """Vrai si la position tombe hors de tout repère (main, footer, header, nav, aside), en ne
    comptant ni les commentaires, ni les scripts, ni les styles."""
    avant = _MASQUE.sub(lambda m: " " * len(m.group(0)), html[:pos]).lower()
    for r in _REPERES:
        if len(re.findall(r"<%s\b" % r, avant)) > len(re.findall(r"</%s\s*>" % r, avant)):
            return False
    return True


def ranger(html: str) -> str:
    """Range dans un pied (`<footer>`) la mention posée hors de tout repère, avec la feuille qui
    la précède ; ne touche à rien d'autre. Pour une page dont le CSS stylise `footer`, le pied
    changerait son allure : la ranger dans `<main>` à la main, et vérifier le rendu."""
    m = re.search(r'(<style>\.licence-cc a[^<]*</style>\s*)?<p class="licence-cc" data-licence="cc-by-nc-sa"[^>]*>.*?</p>',
                  html, re.S)
    if not m or not hors_repere(html, m.start()):
        return html
    return html[:m.start()] + "<footer>" + m.group(0) + "</footer>" + html[m.end():]


def retirer(html: str) -> str:
    """L'inverse d'`injecter` — pour les bancs et pour un retrait voulu, jamais appelé en production."""
    return re.sub(r'(<style>\.licence-cc a[^<]*</style>)?<p class="licence-cc" data-licence="cc-by-nc-sa"[^>]*>.*?</p>\n?', "", html, flags=re.S)
