# -*- coding: utf-8 -*-
"""controle_navigation_seances.py — chaque séance mène explicitement à la suivante (règle n°101).

LE CONSTAT QUI A DONNÉ CE CONTRÔLE
----------------------------------
Règle d'or n°101, posée le 26/08/2026 : « chaque séance se termine par un
bouton qui mène à la suivante » — pour qu'un élève arrivé au bas de la
Séance 2 n'ait pas à remonter jusqu'à la barre d'onglets pour ouvrir la
Séance 3. Elle a d'abord été appliquée à la famille C9 (règle n°95), puis
plus nulle part ailleurs : la règle existait, mais rien ne la mesurait.

Le 28/09/2026, en testant lui-même `4e_C1.1` (Tsinghua feux), Pascal
signale que la fin de la Séance 2 ne mène nulle part. Une marche sur les
**40** pages du dépôt qui portent un système d'onglets `.seance-tab` /
`.seance-panel` montre que **31** d'entre elles n'ont ce bouton nulle
part — la règle n'avait jamais quitté la famille C9 où elle était née.
Un lot du même jour ajoute le bouton sur les 31 pages restantes (plus une
déjà posée, mais avec un nom de classe différent de celui de C9, corrigé
au passage pour une seule convention dans tout le dépôt).

Le même lot a introduit, puis corrigé au fil de l'eau, DEUX bugs que seul
le banc au navigateur (jamais ce contrôle-ci) a vus :
1. le bouton posé APRÈS la fermeture de son panneau (orphelin — voir
   `fin_reelle_du_panneau`) ;
2. sur `4e_C1.4` : le panneau « hors » (le bloc Python, hors compétence)
   est intercalé PHYSIQUEMENT entre s1 et s2 dans le fichier, bien
   qu'exclu de la chaîne logique. Chercher le bouton de s1 jusqu'à la
   position du panneau s2 (le prochain de la chaîne LOGIQUE) balayait
   donc aussi tout le panneau « hors » — et un bouton posé par erreur
   dans « hors » se faisait compter comme appartenant à s1. Voir
   `fin_du_panneau_suivant_physique` : la recherche du contenu propre
   d'un panneau s'arrête désormais au tout premier panneau suivant DANS
   LE FICHIER, « hors » ou pas, jamais au prochain de la chaîne logique.

CE QU'IL MESURE
----------------
Dans chaque page qui a au moins deux onglets `.seance-tab[data-panel]` :
l'ordre des onglets (hors onglet marqué `hors`, un module volontairement
en dehors du parcours — ex. le bloc Python de `3e_C1.5`/`4e_C1.4`, hors
compétence). Pour chaque onglet sauf le DERNIER de cet ordre, son panneau
doit contenir un bouton `.vers-seance[data-vers="<id du panneau suivant>"]`
— la convention posée par la famille C9 le 26/08/2026 et étendue à tout le
dépôt le 28/09/2026. Le dernier onglet n'a rien à promettre : il n'y a pas
de séance suivante.

CE QU'IL NE FAIT PAS
---------------------
Il ne vérifie pas que le bouton MÈNE réellement au bon endroit une fois
cliqué (le clic simule un clic sur l'onglet cible — voir le banc du lot,
au navigateur) : seulement qu'il existe et pointe sur le bon identifiant.
Il ne juge pas la formulation du texte du bouton. Et il ne s'applique
qu'aux pages à onglets `.seance-tab` — une séquence à défilement continu,
sans onglets, n'entre pas dans son périmètre.

Usage :
    python3 _outils/controle_navigation_seances.py           # rapport complet
    python3 _outils/controle_navigation_seances.py --muet    # seulement les refus
Sortie : 0 si chaque séance (hors la dernière de chaque page) a son bouton, 1 sinon.
"""

import glob
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)

TAB_RE = re.compile(
    r'<button\s+class="seance-tab([^"]*)"[^>]*?data-panel="([a-z0-9]+)"'
    r'|<button\s+class="seance-tab([^"]*)"[^>]*?aria-controls="[^"]*"[^>]*?data-panel="([a-z0-9]+)"',
    re.S
)
PANNEAU_RE = re.compile(r'<(?:div|section)\s+class="seance-panel[^"]*"[^>]*?\bid="([a-z0-9]+)"')
VERS_RE = re.compile(r'class="[^"]*\bvers-seance\b[^"]*"[^>]*?data-vers="([a-z0-9]+)"')

#: Pages tolérées avec leur raison — ne s'agrandit pas sans décision écrite
#: (même principe que `controle_atteignabilite.py`, règle n°273).
TOLEREES = {
    # Vide au 28/09/2026 : les 40 pages à onglets du dépôt sont conformes.
}


def onglets_ordre(texte):
    """[(panel_id, est_hors)] dans l'ordre du document, hors doublons."""
    vus, out = set(), []
    for m in TAB_RE.finditer(texte):
        classes = m.group(1) if m.group(1) is not None else m.group(3)
        panel_id = m.group(2) if m.group(2) is not None else m.group(4)
        if panel_id in vus:
            continue
        vus.add(panel_id)
        hors = 'hors' in classes.split()
        out.append((panel_id, hors))
    return out


def pages(racine):
    return sorted(f for f in glob.glob(os.path.join(racine, "**", "*.html"), recursive=True)
                  if not any(e in f for e in ECARTES))


FERMETURE_RE = re.compile(r'^[ \t]*</(?:div|section)>[ \t]*(?:<!--.*?-->[ \t]*)?$', re.M)


def fin_reelle_du_panneau(texte, debut, fin):
    """Position de la fermeture PROPRE du panneau (avant le suivant), en sautant
    les lignes vides et les commentaires. Un bouton posé APRÈS cette fermeture
    n'est plus dans le panneau : il resterait affiché quel que soit l'onglet actif
    (bug réel trouvé le 28/09/2026 sur `3e_C1.5`/`4e_C1.4`, corrigé avant livraison,
    et que seul le banc au navigateur avait révélé — d'où cette bordure resserrée
    ici, pour qu'une régression pareille se voie sans rouvrir un navigateur)."""
    # (la fermeture peut porter un commentaire de fin de bloc sur la même ligne,
    # ex. `</section><!-- fin de #s1 -->` — FERMETURE_RE le tolère : sinon la
    # borne retombe sur une fermeture plus interne, plus tôt, et un bouton posé
    # correctement juste avant la vraie fermeture se ferait exclure à tort —
    # bug réel trouvé le 28/09/2026 en corrigeant `4e_C1.4`)
    dernieres = list(FERMETURE_RE.finditer(texte, debut, fin))
    return dernieres[-1].start() if dernieres else fin


def fin_du_panneau_suivant_physique(positions, debut, fin_texte):
    """Position du tout premier panneau qui suit `debut` DANS LE FICHIER — « hors »
    ou pas. Borne la recherche du bouton d'un panneau à son contenu propre : si un
    panneau « hors » est intercalé physiquement avant le prochain panneau de la
    chaîne LOGIQUE (bug réel du 28/09/2026 sur `4e_C1.4` : le bloc Python, hors
    compétence, posé entre s1 et s2 dans le fichier), la recherche s'arrête à lui,
    pas au panneau logique suivant — sinon un bouton égaré dans le panneau « hors »
    se ferait compter comme appartenant au panneau précédent."""
    suivants = [p for p in positions.values() if p > debut]
    return min(suivants) if suivants else fin_texte


def juger(chemin):
    """[(panneau_incomplet, panneau_suivant_attendu)] — vide si conforme."""
    texte = open(chemin, encoding="utf-8", errors="replace").read()
    onglets = [o for o in onglets_ordre(texte) if not o[1]]
    if len(onglets) < 2:
        return []
    positions = {m.group(1): m.start() for m in PANNEAU_RE.finditer(texte)}
    manques = []
    for i in range(len(onglets) - 1):
        cur_id, _ = onglets[i]
        nxt_id, _ = onglets[i + 1]
        if cur_id not in positions or nxt_id not in positions:
            continue  # onglet sans panneau : signalé ailleurs (pas le rôle de ce contrôle)
        debut = positions[cur_id]
        fin = fin_du_panneau_suivant_physique(positions, debut, len(texte))
        fin_propre = fin_reelle_du_panneau(texte, debut, fin)
        segment = texte[debut:fin_propre]
        cibles = VERS_RE.findall(segment)
        if nxt_id not in cibles:
            manques.append((cur_id, nxt_id))
    return manques


def main(muet=False):
    toutes = pages(DEPOT)
    if not toutes:
        # Règle d'or n°299 : une racine sans page n'est pas « aucun écart », c'est
        # une panne — sinon un DEPOT mal réglé se déclarerait tranquillement content.
        print("⛔ EN PANNE : aucune page .html trouvée sous %s — ce contrôle n'a "
              "rien pu lire, ce n'est pas la preuve d'une conformité" % DEPOT)
        return 2

    total_pages, total_onglets, ecarts = 0, 0, []
    for f in toutes:
        texte_brut = open(f, encoding="utf-8", errors="replace").read()
        if texte_brut.count('class="seance-tab') < 2:
            continue
        total_pages += 1
        manques = juger(f)
        total_onglets += len(onglets_ordre(texte_brut))
        rel = os.path.relpath(f, DEPOT).replace(os.sep, "/")
        if manques and rel not in TOLEREES:
            ecarts.append((rel, manques))

    fantomes = [p for p in TOLEREES if not any(
        os.path.relpath(f, DEPOT).replace(os.sep, "/") == p for f in toutes)]

    if not muet:
        print("%d page(s) à onglets de séances · %d onglet(s) au total · %d page(s) en écart"
              % (total_pages, total_onglets, len(ecarts)))
        print("     NON LU : que le clic mène au bon endroit une fois exécuté (le banc du lot, "
              "au navigateur) ;\n     la formulation du texte du bouton ; les pages sans onglets "
              "(défilement continu).")

    if fantomes:
        print("\n⚠ %d entrée(s) tolérée(s) n'existent plus — à retirer de TOLEREES :" % len(fantomes))
        for p in fantomes:
            print("  " + p)

    if ecarts:
        print("\n⛔ %d page(s) où une séance ne mène pas explicitement à la suivante "
              "(règle n°101) :" % len(ecarts))
        for rel, manques in ecarts:
            for cur_id, nxt_id in manques:
                print("  %s\n     panneau « %s » : aucun bouton .vers-seance vers « %s »"
                      % (rel, cur_id, nxt_id))
        return 1
    print("\n✅ chaque séance (hors la dernière de sa page) mène explicitement à la suivante")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
