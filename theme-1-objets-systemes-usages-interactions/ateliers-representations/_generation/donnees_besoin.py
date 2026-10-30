# -*- coding: utf-8 -*-
"""Atelier — Le besoin (bête à cornes).

Codes servis (plan du 24/10/2026) : 5e_C3.3 ; 4e_C1.3 et 4e_C3.1 ; 3e_C3.1.
Objets-fils : 5e, le vélo-cargo de Léa et le lampadaire intelligent d'un parking de
Sainte-Luce ; 4e, le système d'arrosage du jardin partagé du collège ; 3e, la station
d'alerte cyclonique.

Le verbe change d'un niveau à l'autre, pas la notion :
  5e  RECONNAÎTRE le besoin (lire, compléter, choisir l'objet qui remplit les trois branches) ;
  4e  FORMULER (le nouveau but quand le besoin évolue ; les caractéristiques qu'il appelle) ;
  3e  ÉLARGIR la liste des OST possibles, puis ARBITRER une formulation du besoin.

La carte des représentations le fixe : dix minutes pour formuler le besoin, pas une séance
sur le formalisme, jamais un objectif évalué. Les exercices sont donc courts, et aucun ne
demande de dessiner le gabarit.
"""
import figures

SLUG = "besoin-bete-a-cornes"
COURT = "bc"
EMOJI = "🐂"
TITRE = "Le besoin"
TITRE_COURT = "le besoin (bête à cornes)"
TITRE_COMPLET = "Le besoin, souvent représenté par la bête à cornes"
ETIQUETTE = "🐂 bête à cornes"
ETIQUETTE_COURTE = "Besoin"
MENTION_FICTION = ("Situations imaginées pour les exercices : Léa et ses enfants, le lampadaire du parking, Mme Joseph et "
                   "le jardin du collège, l'équipe du projet d'alerte et son quartier de Sainte-Luce sont inventés.")


def bac(ident, a_qui, sur_quoi, objet, but, titre, desc, vivants=None):
    return figures.bete_a_cornes(ident, a_qui, sur_quoi, objet, but, titre, desc, vivants=vivants)


# ─────────────────────────────────────────────────────────────────────────────
# Les dessins (un identifiant par apparition : deux SVG d'une même page ne
# partagent jamais un identifiant)
# ─────────────────────────────────────────────────────────────────────────────
BAC_VELO = bac(
    "bc-velo", "Léa", "ses deux enfants et ses courses", "Le vélo-cargo",
    "transporter ses deux enfants et ses courses en ville",
    "La bête à cornes du vélo-cargo de Léa",
    "En haut à gauche, sous la question « À qui le produit rend-il service ? », la case dit : Léa. En haut à droite, "
    "sous la question « Sur quoi le produit agit-il ? », la case dit : ses deux enfants et ses courses. Une grande courbe "
    "part des deux cases et passe sous le vélo-cargo, écrit au centre. Une flèche descend vers la case « Dans quel but ? » : "
    "transporter ses deux enfants et ses courses en ville.")

VIVANTS_LAMPE = {"a_qui": "bc-l-qui", "sur_quoi": "bc-l-quoi", "but": "bc-l-but"}
BAC_LAMPE = bac(
    "bc-lampe", "", "", "Le lampadaire intelligent", "",
    "La bête à cornes du lampadaire intelligent, à compléter",
    "Au centre, le lampadaire intelligent. Les trois cases sont vides et en pointillés : en haut à gauche, « À qui le "
    "produit rend-il service ? » ; en haut à droite, « Sur quoi le produit agit-il ? » ; en bas, « Dans quel but ? ».",
    vivants=VIVANTS_LAMPE)

BAC_LAMPE_C = bac(
    "bc-lampe-c", "les piétons", "la rue du parking", "Le lampadaire intelligent",
    "éclairer la rue du parking la nuit, pour que les piétons y marchent en sécurité",
    "La bête à cornes du lampadaire intelligent, corrigée",
    "À qui le produit rend-il service : les piétons. Sur quoi agit-il : la rue du parking. Au centre, le lampadaire "
    "intelligent. Dans quel but : éclairer la rue du parking la nuit, pour que les piétons y marchent en sécurité.")

BAC_BESOIN = bac(
    "bc-besoin", "Léa", "ses deux enfants et ses courses", "Quel objet ?",
    "transporter ses deux enfants et ses courses en ville, sans voiture",
    "Le besoin de Léa, avant de choisir l'objet",
    "À qui le produit rend-il service : Léa. Sur quoi agit-il : ses deux enfants et ses courses. Au centre, à la place "
    "du produit, une question : quel objet ? Dans quel but : transporter ses deux enfants et ses courses en ville, sans voiture.")

BAC_ARROSOIR = bac(
    "bc-arrosoir", "la gardienne du jardin", "les plantes du jardin", "L'arrosoir",
    "arroser les plantes du jardin",
    "Avant : la bête à cornes de l'arrosoir",
    "À qui le produit rend-il service : la gardienne du jardin. Sur quoi agit-il : les plantes du jardin. Au centre, "
    "l'arrosoir. Dans quel but : arroser les plantes du jardin.")

BAC_ARROSAGE = bac(
    "bc-arrosage", "la gardienne du jardin", "les plantes du jardin", "Le système d'arrosage connecté", "",
    "Après : la bête à cornes du système d'arrosage connecté, sans son but",
    "À qui le produit rend-il service : la gardienne du jardin. Sur quoi agit-il : les plantes du jardin. Au centre, "
    "le système d'arrosage connecté. La case « Dans quel but ? » est vide et en pointillés : c'est à toi de l'écrire.",
    vivants={"but": "bc-a-but"})

BUT_ARROSAGE = "arroser les plantes du jardin, même en l'absence de la gardienne, sans gaspiller l'eau"
DESC_ARROSAGE = ("À qui le produit rend-il service : la gardienne du jardin. Sur quoi agit-il : les plantes du jardin. "
                 "Au centre, le système d'arrosage connecté. Dans quel but : arroser les plantes du jardin, même en "
                 "l'absence de la gardienne, sans gaspiller l'eau.")
BAC_ARROSAGE_C = bac("bc-arrosage-c", "la gardienne du jardin", "les plantes du jardin", "Le système d'arrosage connecté",
                     BUT_ARROSAGE, "Après : la bête à cornes du système d'arrosage connecté, corrigée", DESC_ARROSAGE)
BAC_ARROSAGE_E5 = bac("bc-arrosage-5", "la gardienne du jardin", "les plantes du jardin", "Le système d'arrosage connecté",
                      BUT_ARROSAGE, "La bête à cornes du système d'arrosage connecté", DESC_ARROSAGE)

BUT_ALERTE = "prévenir les habitants du quartier de l'arrivée d'un cyclone"
DESC_ALERTE = ("À qui le produit rend-il service : les habitants du quartier. Sur quoi agit-il : les habitants du "
               "quartier, qu'il faut prévenir. Au centre, à la place du produit, une question : quel objet ? Dans quel "
               "but : prévenir les habitants du quartier de l'arrivée d'un cyclone.")
BAC_ALERTE = bac("bc-alerte", "les habitants du quartier", "les habitants du quartier", "Quel objet ?", BUT_ALERTE,
                 "Le besoin du quartier, avant de chercher les objets possibles", DESC_ALERTE)
BAC_ALERTE_C = bac("bc-alerte-c", "les habitants du quartier", "les habitants du quartier", "Quel objet ?", BUT_ALERTE,
                   "La bête à cornes de l'autre équipe, corrigée", DESC_ALERTE)

BAC_MAL = bac(
    "bc-mal", "les habitants du quartier", "la sécurité du quartier", "Quel objet ?", "envoyer un SMS aux habitants",
    "La bête à cornes d'une autre équipe, à vérifier",
    "À qui le produit rend-il service : les habitants du quartier. Sur quoi agit-il : la sécurité du quartier. Au centre, "
    "une question : quel objet ? Dans quel but : envoyer un SMS aux habitants.")

# ─────────────────────────────────────────────────────────────────────────────
# Les motifs des réponses écrites (texte normalisé : minuscules, sans accents)
# ─────────────────────────────────────────────────────────────────────────────
#: un verbe à l'infinitif en tête de phrase (« Éclairer… », « Pour arroser… », « Permettre… »)
VERBE = (r"^\W*(pour |il doit |il sert a |sert a |le but est de |le but est d'|son but est de |son but est d')?"
         r"(?!lumiere\b|derriere\b|premiere\b|riviere\b|entre\b|notre\b|votre\b|autre\b|leur\b)[a-z]+(er|ir|re)\b")
SOL_LAMPE = (r"\bleds?\b|capteur|detecteur|ampoule|\blampes?\b|lanterne|panneau|solaire|batterie|\bpiles?\b|"
             r"programme|microcontroleur|carte electronique|arduino|cellule|interrupteur|\bcables?\b|fil electrique")
SOL_ARROSAGE = (r"capteur|sonde|electrovanne|vanne|programmateur|programme|smartphone|telephone|portable|application|"
                r"\bappli\b|wi.?fi|internet|bluetooth|pompe|tuyau|goutte|arduino|carte electronique|microcontroleur|"
                r"minuteur|batterie|panneau solaire|connecte|robot")
SOL_ALERTE = (r"\bsms\b|texto|message|telephone|portable|smartphone|application|\bappli\b|sirene|radio|haut.?parleur|"
              r"megaphone|internet|reseau|panneau|ecran|televi|e.?mail|whatsapp|facebook|gyrophare|cloche|notification|klaxon")

MOTS_BESOIN = [
    ("besoin", "ce qui manque à quelqu'un, ou ce qui lui est nécessaire. C'est le point de départ de tout objet technique&nbsp;: "
     "on fabrique ou on choisit un objet parce que quelqu'un en a besoin."),
    ("bête à cornes", "le nom courant du schéma qui exprime le besoin&nbsp;: deux cases en haut (à qui&nbsp;? sur quoi&nbsp;?), "
     "le produit au milieu, le but en bas. Sa grande courbe fait penser aux cornes d'un taureau."),
]

# ─────────────────────────────────────────────────────────────────────────────
# 5e — RECONNAÎTRE le besoin (5e_C3.3)
# ─────────────────────────────────────────────────────────────────────────────
E1 = dict(
    id="e1", titre="Lire la bête à cornes du vélo-cargo", code="5e_C3.3", duree=6,
    objectif="lire, dans une bête à cornes, à qui l'objet rend service, sur quoi il agit et dans quel but il existe.",
    production="trois réponses, une par question de la bête à cornes.",
    mots=MOTS_BESOIN + [
        ("rendre service", "aider quelqu'un, lui être utile. L'objet rend service à la personne qui s'en sert."),
        ("agir sur", "déplacer, toucher, transformer ou changer quelque chose. Le vélo-cargo agit sur ce qu'il transporte&nbsp;: "
         "il le fait changer de place."),
        ("but", "ce pour quoi l'objet existe. Il s'écrit avec un verbe à l'infinitif&nbsp;: transporter, éclairer, arroser…"),
        ("solution", "une pièce ou un moyen qui dit <b>comment</b> l'objet fait son travail (le grand bac, les vitesses). "
         "Le but, lui, dit <b>pourquoi</b> l'objet existe.")],
    documents=[dict(svg=BAC_VELO, legende="La bête à cornes du vélo-cargo de Léa.",
                    description="<ul><li><b>À qui le produit rend-il service&nbsp;?</b> Léa.</li>"
                                "<li><b>Sur quoi le produit agit-il&nbsp;?</b> Ses deux enfants et ses courses.</li>"
                                "<li><b>Au centre&nbsp;:</b> le vélo-cargo.</li>"
                                "<li><b>Dans quel but&nbsp;?</b> Transporter ses deux enfants et ses courses en ville.</li></ul>")],
    intro="<p>Léa vit en ville et n'a pas de voiture. Chaque jour, elle emmène ses deux enfants et rapporte ses courses avec "
          "son <b>vélo-cargo</b> — un vélo avec un grand bac devant. Pour dire le <b>besoin</b> auquel répond cet objet, on "
          "pose trois questions. Le schéma qui rassemble les réponses s'appelle souvent la <b>bête à cornes</b>.</p>",
    consigne="<p>La bête à cornes répond à trois questions&nbsp;: <b>à qui</b> l'objet rend-il service (qui s'en sert)&nbsp;? "
             "<b>sur quoi</b> agit-il (ce qu'il déplace, touche ou transforme)&nbsp;? <b>dans quel but</b> existe-t-il&nbsp;? "
             "<b>Lis le schéma, puis choisis, pour chaque question, la phrase qui l'explique.</b></p>",
    critere="trois réponses justes, et tu sais dire pourquoi les enfants sont dans la case « sur quoi&nbsp;? » et pas dans "
            "la case « à qui&nbsp;? ».",
    widgets=[dict(type="choix", name="qui",
                  legende="① <b>À qui&nbsp;?</b> Le schéma dit&nbsp;: Léa. Pourquoi Léa&nbsp;?",
                  options=[("sert", "Parce que c'est elle qui se sert du vélo-cargo&nbsp;: il l'aide à faire ses trajets."),
                           ("paie", "Parce que c'est elle qui l'a acheté au magasin."),
                           ("forte", "Parce qu'elle est la plus grande et la plus forte de la famille."),
                           ("piece", "Parce qu'elle pédale&nbsp;: elle fait partie du vélo-cargo.")],
                  bonne="sert",
                  retours={"sert": "Oui : la case « à qui ? » nomme la personne que l'objet aide, celle qui s'en sert.",
                           "paie": "Elle l'a peut-être acheté, mais ce n'est pas la raison : un parent qui offre un vélo à son enfant le paie, et c'est pourtant à l'enfant qu'il rend service.",
                           "forte": "La taille et la force ne décident de rien : la case « à qui ? » nomme la personne que l'objet aide.",
                           "piece": "Léa pédale, mais elle n'est pas une pièce du vélo : elle reste en dehors de l'objet, c'est la personne qu'il aide."}),
             dict(type="choix", name="quoi",
                  legende="② <b>Sur quoi&nbsp;?</b> Le schéma dit&nbsp;: ses deux enfants et ses courses. Pourquoi eux, et pas la route&nbsp;?",
                  options=[("deplace", "Parce que ce sont eux que le vélo-cargo fait changer de place."),
                           ("bac", "Parce qu'ils sont assis ou posés dans le grand bac, juste devant Léa."),
                           ("importants", "Parce qu'ils comptent plus pour Léa que la route."),
                           ("touche", "Parce que la route ne touche jamais le vélo-cargo.")],
                  bonne="deplace",
                  retours={"deplace": "Oui : le vélo-cargo agit sur ce qu'il déplace. La route, elle, reste à sa place.",
                           "bac": "C'est vrai, ils sont dans le bac, mais ce n'est pas la raison : avec un bac à l'arrière, le vélo-cargo agirait sur eux de la même façon. Ce qui compte, c'est qu'il les fait changer de place.",
                           "importants": "L'importance ne décide pas de la case : on cherche ce que l'objet déplace ou transforme.",
                           "touche": "La route touche les roues ! Mais le vélo-cargo ne la change pas : elle reste où elle est."}),
             dict(type="choix", name="but",
                  legende="③ <b>Dans quel but&nbsp;?</b> Laquelle de ces phrases pourrait aussi aller dans la case du bas&nbsp;?",
                  options=[("but", "Déplacer ses enfants et ses courses d'un bout à l'autre de la ville."),
                           ("solution", "Avoir un grand bac devant le guidon et huit vitesses."),
                           ("nom", "Le vélo-cargo de Léa, avec ses deux roues et son bac."),
                           ("contrainte", "Résister à la pluie et monter les côtes sans trop d'effort.")],
                  bonne="but",
                  retours={"but": "Oui : un verbe à l'infinitif (déplacer), et aucune solution. C'est le même but, dit autrement.",
                           "solution": "Le grand bac et les vitesses disent COMMENT le vélo-cargo fait son travail : ce sont des solutions. Le but dit POURQUOI il existe.",
                           "nom": "C'est le nom de l'objet, déjà écrit au centre du schéma. Le but commence par un verbe à l'infinitif.",
                           "contrainte": "Ce sont des conditions que le vélo-cargo doit respecter : elles viendront avec le diagramme des interacteurs. Le but dit pourquoi l'objet existe."})],
    aides=["<p>Lis le schéma comme une phrase&nbsp;: « Le vélo-cargo rend service <b>à</b> …, en agissant <b>sur</b> …, "
           "<b>pour</b> … ». Puis, pour chaque case, pose-toi une question simple&nbsp;: qui s'en sert&nbsp;? qu'est-ce qui "
           "change de place&nbsp;? pourquoi l'objet existe-t-il&nbsp;?</p>",
           "<p>À qui&nbsp;? → qui pédale et décide du trajet&nbsp;? → Léa → elle se sert de l'objet.<br>"
           "Sur quoi&nbsp;? → qu'est-ce qui change de place&nbsp;? → les enfants et les courses → la route, elle, ne bouge pas.<br>"
           "Dans quel but&nbsp;? → un verbe à l'infinitif → « déplacer », « transporter » → pas de solution (ni bac, ni vitesses).</p>"],
    jumeau=dict(consigne="Un cartable&nbsp;: à qui rend-il service, sur quoi agit-il, dans quel but existe-t-il&nbsp;?",
                correction="À qui&nbsp;? → <b>l'élève</b>, qui le porte. Sur quoi&nbsp;? → <b>ses livres et ses cahiers</b>, que le "
                           "cartable déplace. But&nbsp;: <b>transporter ses affaires de classe entre la maison et le collège</b> — un "
                           "verbe, et aucune solution (ni bretelles, ni poches)."),
    correction=[
        "<b>La phrase du schéma&nbsp;:</b> le vélo-cargo rend service <b>à Léa</b>, en agissant <b>sur ses deux enfants et ses "
        "courses</b>, <b>pour</b> les transporter en ville.",
        "<b>① À qui&nbsp;?</b> → Léa → c'est elle qui se sert du vélo-cargo",
        "Refusés&nbsp;: « elle l'a acheté » → celui qui paie n'est pas toujours celui à qui l'objet rend service&nbsp;; « la plus "
        "forte » → la force ne décide de rien&nbsp;; « une pièce du vélo » → Léa reste en dehors de l'objet.",
        "<b>② Sur quoi&nbsp;?</b> → les enfants et les courses → le vélo-cargo les fait changer de place",
        "Refusés&nbsp;: « ils sont dans le bac » → vrai, mais un bac à l'arrière ne changerait rien&nbsp;; « plus importants » → "
        "l'importance ne décide pas&nbsp;; « la route ne touche pas » → faux, elle touche les roues, mais elle ne bouge pas.",
        "<b>③ Dans quel but&nbsp;?</b> → « déplacer ses enfants et ses courses d'un bout à l'autre de la ville » → un verbe à "
        "l'infinitif, aucune solution",
        "Refusés&nbsp;: le bac et les vitesses → des solutions (comment)&nbsp;; « le vélo-cargo de Léa » → le nom de l'objet&nbsp;; "
        "« résister à la pluie » → une contrainte, pas le but.",
        ("conclusion", "La bête à cornes se lit comme une phrase&nbsp;: <b>à qui</b> → <b>sur quoi</b> → <b>pour quoi</b>."),
    ],
    retenir="la bête à cornes se lit comme une phrase&nbsp;: l'objet rend service <b>à quelqu'un</b>, en agissant <b>sur "
            "quelque chose</b>, <b>pour</b> un but écrit avec un verbe à l'infinitif.",
    piege="mettre dans la case « à qui&nbsp;? » tout ce que l'objet transporte&nbsp;: les enfants sont dans le bac, mais c'est "
          "Léa que le vélo-cargo aide — les enfants sont ce sur quoi il agit.",
)

BANQUE_LAMPE = ["les piétons", "la rue du parking", "la mairie", "l'ampoule", "la nuit"]

E2 = dict(
    id="e2", titre="Compléter la bête à cornes du lampadaire", code="5e_C3.3", duree=10,
    objectif="compléter la bête à cornes d'un objet, puis écrire son but sans nommer de solution.",
    production="les deux cases du haut complétées, et le but écrit en une phrase.",
    mots=[("piéton", "une personne qui se déplace à pied."),
          ("mairie", "le service de la commune qui décide d'installer les lampadaires et qui les paie."),
          ("solution technique", "une pièce ou un moyen qui dit <b>comment</b> l'objet fait son travail&nbsp;: l'ampoule, le "
           "capteur qui repère un piéton, le panneau solaire. Une solution n'a rien à faire dans le but."),
          ("verbe à l'infinitif", "la forme du verbe qu'on trouve dans le dictionnaire&nbsp;: éclairer, transporter, arroser…"),
          ("intrus", "un mot qui n'a pas sa place dans la liste.")],
    intro="<p>Sur un parking de Sainte-Luce, la mairie a fait installer un <b>lampadaire intelligent</b>&nbsp;: la nuit, il "
          "s'allume quand un piéton passe, et il reste éteint le reste du temps.</p>",
    consigne="<p><b>Complète les deux cases du haut</b> avec les mots de la banque&nbsp;: <i>les piétons · la rue du parking · "
             "la mairie · l'ampoule · la nuit</i>. Tes choix s'écrivent dans le schéma. Trois mots de la banque sont des "
             "<b>intrus</b>. Puis <b>écris le but</b> du lampadaire&nbsp;: une phrase qui commence par un <b>verbe à "
             "l'infinitif</b> (éclairer, permettre…) et qui ne nomme <b>aucune solution technique</b> — ni ampoule, ni "
             "capteur, ni panneau solaire. Une solution dit <i>comment</i>&nbsp;; le but dit <i>pourquoi</i>.</p>",
    critere="les deux cases portent les bons mots, et ton but commence par un verbe, dit où, quand et pour qui, sans nommer "
            "de solution.",
    widgets=[dict(type="slots", intro='<figure class="figure schema-vivant">' + BAC_LAMPE +
                  '<figcaption>La bête à cornes du lampadaire intelligent. Tes choix et ton but s\'écrivent dans les cases en '
                  'pointillés.</figcaption></figure>',
                  slots=[dict(name="qui", cible="bc-l-qui", legende="Case « À qui le produit rend-il service&nbsp;? »",
                              options=BANQUE_LAMPE, bonnes=["les piétons"],
                              indice="Case « à qui ? » : la personne que le lampadaire aide quand il s'allume, pas celle qui l'a commandé."),
                         dict(name="quoi", cible="bc-l-quoi", legende="Case « Sur quoi le produit agit-il&nbsp;? »",
                              options=BANQUE_LAMPE, bonnes=["la rue du parking"],
                              indice="Case « sur quoi ? » : ce que la lumière touche et rend visible.")]),
             dict(type="texte", name="but", lignes=3, miroir="bc-l-but",
                  label="Écris le but du lampadaire intelligent (il s'écrit aussi dans le schéma).",
                  criteres=[dict(label="ton but commence par un verbe à l'infinitif (éclairer, permettre…)",
                                 motifs=[VERBE],
                                 manque="Commence ton but par un verbe à l'infinitif : « Éclairer… », « Permettre… »."),
                            dict(label="il dit où et quand&nbsp;: la rue (ou le parking) et la nuit",
                                 motifs=[r"\b(rue|chemin|parking|trottoir|route|allee|passage|sol|endroit|lieu|quartier|place)\b",
                                         r"\b(nuit|noir|obscurite|sombre|soir|nocturne)"], min=2,
                                 manque="Dis OÙ (la rue, le parking) et QUAND (la nuit) le lampadaire est utile."),
                            dict(label="il dit pour qui&nbsp;: les piétons, leur sécurité",
                                 motifs=[r"pieton|passant|marcheur|promeneur|personne|gens|habitant|usager|securi|danger|accident|chute|tomber|bless"],
                                 manque="Dis POUR QUI : qui marche sur le parking, la nuit ?")],
                  interdits=[dict(motifs=[SOL_LAMPE],
                                  message="Ton but nomme une solution technique (une ampoule, un capteur, un panneau solaire…). "
                                          "Le but dit POURQUOI le lampadaire existe, pas COMMENT il est fait : enlève-la.")],
                  exemple="Éclairer la rue du parking la nuit, pour que les piétons y marchent en sécurité.",
                  etayage=["Éclairer … la nuit, pour que les piétons …", "Permettre aux piétons de … quand il fait nuit."])],
    aides=["<p>Pour la case « à qui&nbsp;? », cherche la personne qui profite du lampadaire au moment où il s'allume. Pour la "
           "case « sur quoi&nbsp;? », cherche ce que la lumière touche. Pour le but, termine la phrase&nbsp;: « Le lampadaire "
           "existe pour… ».</p>",
           "<p>La mairie → elle décide et elle paie, mais elle ne marche pas sur le parking la nuit → pas dans « à qui&nbsp;? ».<br>"
           "Les piétons → c'est eux que la lumière aide → <b>« à qui&nbsp;? »</b>.<br>"
           "La rue du parking → c'est elle que la lumière éclaire → <b>« sur quoi&nbsp;? »</b>.<br>"
           "La nuit → le moment où le lampadaire travaille, pas ce sur quoi il agit.<br>"
           "L'ampoule → une pièce du lampadaire, une solution → aucune case.<br>"
           "Le but → un verbe (éclairer) + où (la rue du parking) + quand (la nuit) + pour qui (les piétons).</p>"],
    jumeau=dict(consigne="Une sonnette de vélo&nbsp;: à qui rend-elle service, sur quoi agit-elle, et quel est son but&nbsp;?",
                correction="À qui&nbsp;? → <b>la personne qui roule</b>. Sur quoi&nbsp;? → <b>les piétons et les autres usagers devant "
                           "elle</b>&nbsp;: le son les prévient. But&nbsp;: <b>prévenir les autres de son arrivée</b> — sans nommer de "
                           "solution (ni clochette, ni ressort)."),
    correction=[
        '<figure class="figure">' + BAC_LAMPE_C + '<figcaption>La bête à cornes du lampadaire, corrigée.</figcaption></figure>',
        "<b>À qui&nbsp;?</b> → <b>les piétons</b> → c'est eux que la lumière aide à voir où ils marchent",
        "<b>Sur quoi&nbsp;?</b> → <b>la rue du parking</b> → c'est elle que la lumière éclaire",
        "<b>La mairie</b> → elle commande et paie le lampadaire, mais elle n'est pas sur le parking la nuit → celui qui paie "
        "n'est pas forcément celui à qui l'objet rend service",
        "<b>La nuit</b> → le moment où le lampadaire travaille&nbsp;; la lumière ne la change pas → ni « à qui&nbsp;? », ni « sur quoi&nbsp;? »",
        "<b>L'ampoule</b> → une pièce du lampadaire&nbsp;: une solution technique → aucune case",
        "<b>Un but attendu&nbsp;:</b> « Éclairer la rue du parking la nuit, pour que les piétons y marchent en sécurité. » → un "
        "verbe à l'infinitif, le lieu, le moment, les personnes",
        "<b>Refusé&nbsp;:</b> « Allumer une ampoule quand le capteur voit quelqu'un » → c'est <i>comment</i> le lampadaire "
        "marche, avec deux solutions (l'ampoule, le capteur)",
        ("conclusion", "Le but dit <b>pourquoi</b> l'objet existe&nbsp;; les solutions disent <b>comment</b>. Et celui qui "
                       "<b>paie</b> n'est pas toujours celui à qui l'objet <b>rend service</b>."),
    ],
    retenir="le but s'écrit avec un <b>verbe à l'infinitif</b> et ne nomme <b>aucune solution</b>&nbsp;; la case « à qui&nbsp;? » "
            "nomme la personne que l'objet aide, pas celle qui l'a commandé.",
    piege="mettre la mairie dans la case « à qui&nbsp;? », ou écrire dans le but comment l'objet fonctionne (« allumer une "
          "ampoule grâce à un capteur »).",
)

OBJETS_E3 = [("cargo", "un vélo-cargo"), ("voiture", "une voiture familiale"), ("sac", "un sac à dos"),
             ("trott", "une trottinette"), ("siege", "un vélo avec un siège enfant"), ("drais", "une draisienne")]

E3 = dict(
    id="e3", titre="Choisir l'objet qui répond au besoin", code="5e_C3.3", duree=9,
    objectif="choisir, parmi plusieurs objets, celui qui remplit les trois branches d'un besoin, et dire pourquoi les autres "
             "ne conviennent pas.",
    production="l'objet choisi, et la branche qui fait échouer chacun des cinq autres.",
    mots=[("branche", "une des trois parties de la bête à cornes&nbsp;: « à qui&nbsp;? », « sur quoi&nbsp;? », « dans quel but&nbsp;? »."),
          ("répondre au besoin", "remplir les trois branches à la fois&nbsp;: servir la bonne personne, agir sur la bonne chose, "
           "atteindre tout le but."),
          ("draisienne", "un petit vélo sans pédales, pour qu'un jeune enfant apprenne à garder l'équilibre."),
          ("siège enfant", "un petit siège fixé à l'arrière d'un vélo, pour un seul enfant."),
          ("écarter", "mettre de côté un objet qui ne convient pas.")],
    documents=[dict(svg=BAC_BESOIN, legende="Le besoin de Léa, avant d'acheter&nbsp;: le produit est encore à trouver.",
                    description="<ul><li><b>À qui&nbsp;?</b> Léa.</li><li><b>Sur quoi&nbsp;?</b> Ses deux enfants et ses courses.</li>"
                                "<li><b>Au centre&nbsp;:</b> une question, quel objet&nbsp;?</li>"
                                "<li><b>Dans quel but&nbsp;?</b> Transporter ses deux enfants et ses courses en ville, sans voiture.</li></ul>")],
    intro="<p>Retour en arrière&nbsp;: avant d'acheter son vélo-cargo, Léa a écrit son <b>besoin</b>. Au centre de la bête à "
          "cornes, le produit est encore un point d'interrogation&nbsp;: on exprime le besoin <b>avant</b> de choisir l'objet. "
          "Six objets sont proposés&nbsp;: <b>un vélo-cargo · une voiture familiale · un sac à dos · une trottinette · un vélo "
          "avec un siège enfant · une draisienne</b>.</p>",
    consigne="<p>Un objet répond au besoin s'il remplit les <b>trois branches</b> de la bête à cornes à la fois. <b>Choisis "
             "l'objet qui répond au besoin de Léa.</b> Puis, pour chacun des cinq autres, <b>dis quelle branche échoue en "
             "premier</b>, en lisant dans l'ordre&nbsp;: à qui&nbsp;? → sur quoi&nbsp;? → dans quel but&nbsp;?</p>",
    critere="le bon objet, et cinq branches justes&nbsp;; tu sais dire pourquoi la voiture, qui transporte pourtant tout le "
            "monde, est écartée.",
    widgets=[dict(type="choix", name="objet", legende="Quel objet remplit les trois branches du besoin de Léa&nbsp;?",
                  options=OBJETS_E3, bonne="cargo",
                  retours={"cargo": "Oui : à qui ? Léa ; sur quoi ? deux enfants et des courses, dans le bac ; but : en ville, sans voiture. Les trois branches sont remplies.",
                           "voiture": "La voiture transporte bien les enfants et les courses, mais le but dit « sans voiture » : une branche échoue.",
                           "sac": "Un sac à dos porte des courses, pas deux enfants.",
                           "trott": "Une trottinette ne porte que la personne debout dessus.",
                           "siege": "Un siège enfant ne porte qu'un enfant, et il ne reste pas de place pour les courses.",
                           "drais": "Une draisienne sert à un jeune enfant qui apprend l'équilibre : elle n'est pas faite pour Léa."}),
             dict(type="classer", name="branche",
                  categories=[("qui", "« à qui&nbsp;? » échoue&nbsp;: il n'est pas fait pour Léa"),
                              ("quoi", "« sur quoi&nbsp;? » échoue&nbsp;: il ne peut pas porter deux enfants et des courses"),
                              ("but", "« dans quel but&nbsp;? » échoue&nbsp;: il ne respecte pas tout le but")],
                  items=[("La voiture familiale", "but", "La voiture porte bien tout le monde : relis le but jusqu'au bout."),
                         ("Le sac à dos", "quoi", "Le sac à dos porte les courses… et les deux enfants ?"),
                         ("La trottinette", "quoi", "Sur une trottinette, qui peut monter ?"),
                         ("Le vélo avec un siège enfant", "quoi", "Un siège enfant : combien d'enfants ? Et les courses ?"),
                         ("La draisienne", "qui", "Une draisienne : qui s'assoit dessus ?")])],
    aides=["<p>Prends les objets un par un et pose les trois questions <b>dans l'ordre</b>. Dès qu'une réponse est « non », "
           "l'objet est écarté&nbsp;: inutile de lire la suite.</p>",
           "<p>La draisienne → à qui&nbsp;? → à un jeune enfant qui apprend l'équilibre, pas à Léa → écartée dès la première branche.<br>"
           "La trottinette → à qui&nbsp;? Léa ✔ → sur quoi&nbsp;? elle ne porte que Léa ✘ → écartée.<br>"
           "La voiture → à qui&nbsp;? ✔ → sur quoi&nbsp;? ✔ → but&nbsp;: « sans voiture » ✘ → écartée.<br>"
           "Le vélo-cargo → ✔ ✔ ✔ → il répond.</p>"],
    jumeau=dict(consigne="Besoin&nbsp;: à qui&nbsp;? un élève&nbsp;; sur quoi&nbsp;? son eau&nbsp;; but&nbsp;: garder son eau fraîche toute la "
                         "journée de classe. Parmi une gourde isotherme, un verre en plastique et un réfrigérateur, lequel répond&nbsp;? "
                         "Pour les deux autres, quelle branche échoue&nbsp;?",
                correction="La <b>gourde isotherme</b> répond aux trois branches. Le verre → il contient l'eau, mais ne la garde pas "
                           "fraîche et se renverse dans le sac → <b>« dans quel but&nbsp;? »</b> échoue. Le réfrigérateur → il sert à toute "
                           "la famille et reste à la maison → <b>« à qui&nbsp;? »</b> échoue déjà (et le but aussi&nbsp;: pas en classe)."),
    correction=[
        "<b>Le vélo-cargo</b> → à qui&nbsp;? Léa ✔ → sur quoi&nbsp;? deux enfants et des courses, dans le bac ✔ → but&nbsp;: en ville, "
        "sans voiture ✔ → <b>il répond au besoin</b>",
        "<b>La draisienne</b> → à qui&nbsp;? elle sert à un jeune enfant qui apprend l'équilibre, pas à Léa ✘ → <b>« à qui&nbsp;? »</b>",
        "<b>La trottinette</b> → à qui&nbsp;? Léa ✔ → sur quoi&nbsp;? elle ne porte que la personne debout dessus ✘ → <b>« sur quoi&nbsp;? »</b>",
        "<b>Le sac à dos</b> → à qui&nbsp;? Léa ✔ → sur quoi&nbsp;? les courses oui, les deux enfants non ✘ → <b>« sur quoi&nbsp;? »</b>",
        "<b>Le vélo avec un siège enfant</b> → à qui&nbsp;? Léa ✔ → sur quoi&nbsp;? un seul enfant, et pas de place pour les courses ✘ "
        "→ <b>« sur quoi&nbsp;? »</b>",
        "<b>La voiture familiale</b> → à qui&nbsp;? Léa ✔ → sur quoi&nbsp;? les enfants et les courses ✔ → but&nbsp;: « sans voiture » ✘ "
        "→ <b>« dans quel but&nbsp;? »</b>",
        "Le piège&nbsp;: la voiture fait le transport, mais elle ne respecte pas <b>tout</b> le but. Faire « presque tout » ne suffit pas.",
        ("conclusion", "Pour choisir un objet, on garde celui qui remplit <b>les trois branches</b>&nbsp;: une seule branche qui "
                       "échoue suffit à l'écarter."),
    ],
    retenir="un objet répond au besoin quand il remplit <b>les trois branches</b> de la bête à cornes à la fois. On exprime le "
            "besoin <b>avant</b> de choisir l'objet.",
    piege="garder un objet parce qu'il fait « presque tout » (la voiture transporte bien les enfants et les courses)&nbsp;: une "
          "seule branche qui échoue suffit à l'écarter.",
)

# ─────────────────────────────────────────────────────────────────────────────
# 4e — FORMULER (4e_C1.3, 4e_C3.1)
# ─────────────────────────────────────────────────────────────────────────────
E4 = dict(
    id="e4", titre="Le besoin évolue&nbsp;: de l'arrosoir au système connecté", code="4e_C1.3", duree=12,
    objectif="repérer, entre deux bêtes à cornes, ce qui a changé, formuler le nouveau but, et justifier l'évolution de "
             "l'objet par celle du besoin.",
    production="les quatre parties comparées, le nouveau but écrit en une phrase, et la raison de l'évolution.",
    mots=MOTS_BESOIN + [
        ("évolution d'un objet", "le passage d'un objet à un autre, plus récent, qui répond à un besoin qui a changé."),
        ("justifier", "donner la raison, preuve à l'appui."),
        ("système d'arrosage connecté", "un système qui arrose seul les plantes, à l'heure choisie, et envoie des nouvelles sur "
         "un téléphone."),
        ("carême", "en Martinique, la saison sèche du début de l'année&nbsp;: il pleut peu, l'eau est précieuse."),
        ("cuve", "un grand réservoir qui recueille l'eau de pluie du toit."),
        ("gaspiller", "utiliser plus qu'il ne faut, et perdre le reste.")],
    documents=[dict(svg=BAC_ARROSOIR, legende="Avant&nbsp;: la bête à cornes de l'arrosoir.",
                    description="<ul><li><b>À qui&nbsp;?</b> La gardienne du jardin.</li><li><b>Sur quoi&nbsp;?</b> Les plantes du jardin.</li>"
                                "<li><b>Au centre&nbsp;:</b> l'arrosoir.</li><li><b>Dans quel but&nbsp;?</b> Arroser les plantes du jardin.</li></ul>")],
    intro="<p>Au jardin partagé du collège, Mme Joseph, la gardienne, arrosait chaque matin avec un <b>arrosoir</b>. Deux "
          "choses ont changé&nbsp;: pendant les <b>vacances</b>, plus personne ne vient au jardin&nbsp;; et en <b>carême</b>, la "
          "saison sèche, l'eau de la cuve devient rare. Le jardin s'équipe donc d'un <b>système d'arrosage connecté</b>. "
          "Ci-dessus, la bête à cornes de l'arrosoir&nbsp;; plus bas, celle du nouveau système, qui n'a pas encore de but.</p>",
    consigne="<p>Pour <b>justifier</b> l'évolution d'un objet, on compare ce qu'on lui demande avant et après. <b>Compare les "
             "deux bêtes à cornes partie par partie</b>, puis <b>écris le nouveau but</b>&nbsp;: un verbe à l'infinitif, "
             "<b>sans nommer de solution</b> (ni capteur, ni pompe, ni smartphone). Enfin, <b>dis pourquoi</b> le jardin a "
             "changé d'objet.</p>",
    critere="quatre comparaisons justes, un but qui dit « même sans la gardienne » et « sans gaspiller l'eau » sans nommer de "
            "solution, et la bonne raison de l'évolution.",
    widgets=[dict(type="classer", name="compare",
                  intro='<figure class="figure schema-vivant">' + BAC_ARROSAGE +
                        '<figcaption>Après&nbsp;: la bête à cornes du système d\'arrosage connecté. Ton but s\'écrit dans la case '
                        'en pointillés.</figcaption></figure>',
                  categories=[("pareil", "elle est la même dans les deux schémas"),
                              ("change", "elle change d'un schéma à l'autre")],
                  items=[("La case « à qui&nbsp;? »", "pareil", "Compare les deux cases du haut, à gauche : qui se sert de l'objet, avant et après ?"),
                         ("La case « sur quoi&nbsp;? »", "pareil", "Compare les deux cases du haut, à droite."),
                         ("Le produit, au centre", "change", "Au centre : un arrosoir, puis… ?"),
                         ("La case « dans quel but&nbsp;? »", "change", "Relis l'histoire : les vacances et le carême demandent-ils le même but qu'avant ?")]),
             dict(type="texte", name="but", lignes=3, miroir="bc-a-but",
                  label="Écris le nouveau but (il s'écrit aussi dans le second schéma).",
                  criteres=[dict(label="ton but commence par un verbe à l'infinitif (arroser…)", motifs=[VERBE],
                                 manque="Commence ton but par un verbe à l'infinitif : « Arroser… »."),
                            dict(label="il dit que l'arrosage se fait même sans la gardienne (absence, vacances)",
                                 motifs=[r"absen|sans (la gardienne|elle|personne|mme|madame|quelqu'un|etre la|qu'elle|que la gardienne)|"
                                         r"vacances|tout seul|toute seule|\bseule?s?\b|automatique|meme quand|meme si|"
                                         r"quand (elle|la gardienne|personne|mme joseph) n'est|n'est pas la|sans intervention|"
                                         r"sans surveillance|personne n'est"],
                                 manque="Dis que les plantes doivent être arrosées MÊME quand la gardienne n'est pas là (pendant les vacances)."),
                            dict(label="il dit que l'eau ne doit pas être gaspillée",
                                 motifs=[r"gaspill|econom|juste (ce qu|la bonne|assez)|ce qu'il faut|la bonne quantite|"
                                         r"sans (trop|perdre)|moins d'eau|peu d'eau|necessaire|besoin|pas trop|ne pas perdre|preserv"],
                                 manque="Dis que l'eau ne doit pas être gaspillée : en carême, elle est rare.")],
                  interdits=[dict(motifs=[SOL_ARROSAGE],
                                  message="Ton but nomme une solution (un capteur, une pompe, le smartphone, un programme, « connecté »…). "
                                          "Le but dit ce qu'il faut obtenir ; le système connecté est la solution choisie pour y arriver.")],
                  exemple="Arroser les plantes du jardin même quand la gardienne est absente, sans gaspiller l'eau de la cuve.",
                  etayage=["Arroser les plantes du jardin même quand …, sans …",
                           "Arroser … pendant les vacances, en n'utilisant que …"]),
             dict(type="choix", name="pourquoi",
                  legende="Pourquoi le jardin est-il passé de l'arrosoir au système d'arrosage connecté&nbsp;?",
                  options=[("besoin", "Parce que le besoin a changé&nbsp;: arroser pendant les vacances, et économiser l'eau en carême."),
                           ("casse", "Parce que l'arrosoir était percé, et qu'il fallait bien le remplacer par autre chose."),
                           ("mode", "Parce que les objets connectés sont plus modernes que l'arrosoir."),
                           ("plantes", "Parce que les plantes du jardin ne sont plus les mêmes qu'avant.")],
                  bonne="besoin",
                  retours={"besoin": "Oui : à qui et sur quoi n'ont pas bougé ; c'est le but qui s'est enrichi. L'objet a évolué pour répondre à ce nouveau but.",
                           "casse": "Un arrosoir percé se remplace par un autre arrosoir : la panne d'un objet ne change pas le besoin.",
                           "mode": "Être moderne ne suffit pas à justifier un changement : sans les vacances et le carême, l'arrosoir répondrait encore au besoin.",
                           "plantes": "La case « sur quoi ? » est la même dans les deux schémas : ce sont toujours les plantes du jardin."})],
    aides=["<p>Compare les deux schémas case par case, comme dans un jeu des sept différences. Puis relis l'histoire&nbsp;: "
           "qu'est-ce que l'arrosoir ne permet plus de faire&nbsp;?</p>",
           "<p>À qui&nbsp;? → la gardienne, dans les deux → pareil.<br>"
           "Sur quoi&nbsp;? → les plantes du jardin, dans les deux → pareil.<br>"
           "Le but de l'arrosoir → « arroser les plantes » → il demande que quelqu'un soit là.<br>"
           "Les vacances → personne au jardin → le but doit dire&nbsp;: <b>même en l'absence de la gardienne</b>.<br>"
           "Le carême → l'eau est rare → le but doit dire&nbsp;: <b>sans gaspiller l'eau</b>.<br>"
           "Nouveau but = verbe + les plantes + l'absence + l'eau, sans aucune solution.</p>"],
    jumeau=dict(consigne="Un élève portait ses affaires dans un cartable. Ses livres sont devenus trop lourds pour son dos&nbsp;: il "
                         "utilise maintenant un sac à roulettes. Quelle branche du besoin a changé, et quel est le nouveau but&nbsp;?",
                correction="À qui&nbsp;? → l'élève, pareil. Sur quoi&nbsp;? → ses affaires de classe, pareil. <b>Le but change</b>&nbsp;: "
                           "« transporter ses affaires de classe » devient « transporter ses affaires de classe <b>sans se faire mal "
                           "au dos</b> ». Les roulettes sont la solution&nbsp;: elles n'entrent pas dans le but."),
    correction=[
        '<figure class="figure">' + BAC_ARROSAGE_C + '<figcaption>Après&nbsp;: la bête à cornes du système d\'arrosage, avec son '
        'nouveau but.</figcaption></figure>',
        "<b>À qui&nbsp;?</b> → la gardienne, dans les deux schémas → <b>pareil</b>",
        "<b>Sur quoi&nbsp;?</b> → les plantes du jardin, dans les deux → <b>pareil</b>",
        "<b>Le produit</b> → l'arrosoir devient le système d'arrosage connecté → <b>change</b>",
        "<b>Le but</b> → « arroser les plantes du jardin » ne suffit plus → <b>change</b>",
        "<b>Un nouveau but attendu&nbsp;:</b> « Arroser les plantes du jardin, même en l'absence de la gardienne, sans gaspiller l'eau. »",
        "« même en l'absence de la gardienne » → vient des vacances&nbsp;; « sans gaspiller l'eau » → vient du carême et de la cuve",
        "<b>Refusé&nbsp;:</b> « Arroser grâce à un capteur et à une pompe » → deux solutions dans le but",
        "<b>Pourquoi l'objet a évolué</b> → parce que le besoin a changé. Un arrosoir percé se remplacerait par un arrosoir&nbsp;; "
        "la mode ne suffit pas&nbsp;; les plantes sont les mêmes.",
        ("conclusion", "Un objet évolue parce que le <b>besoin</b> évolue&nbsp;: ici, c'est le <b>but</b> qui s'est enrichi, pas la "
                       "personne servie ni ce sur quoi on agit."),
    ],
    retenir="pour justifier l'évolution d'un objet, on compare les bêtes à cornes d'avant et d'après&nbsp;: la partie qui change "
            "dit quel besoin nouveau l'objet doit satisfaire.",
    piege="justifier l'évolution par la nouveauté (« c'est plus moderne ») ou par une panne, au lieu du besoin qui a changé.",
)

E5 = dict(
    id="e5", titre="Du besoin aux caractéristiques", code="4e_C3.1", duree=10,
    objectif="tirer d'une bête à cornes les caractéristiques qui comptent pour choisir un système, et écarter celles qui ne "
             "servent pas le besoin.",
    production="les caractéristiques à prendre en compte, et trois d'entre elles reliées à la partie du besoin qu'elles servent.",
    mots=[("caractéristique", "ce qui décrit un modèle et que l'on peut comparer d'un modèle à l'autre&nbsp;: une capacité, une "
           "consommation, une durée, une résistance…"),
          ("autonomie", "le temps pendant lequel un système fonctionne seul, sans que personne n'intervienne."),
          ("capacité", "la quantité qu'un récipient peut contenir, en litres pour une cuve."),
          ("consommation", "ce que le système utilise pour fonctionner&nbsp;: de l'eau, en litres par jour, ou de l'énergie électrique."),
          ("prendre en compte", "regarder, et faire peser dans le choix.")],
    documents=[dict(svg=BAC_ARROSAGE_E5, legende="Le besoin auquel le système d'arrosage doit répondre.",
                    description="<ul><li><b>À qui&nbsp;?</b> La gardienne du jardin.</li><li><b>Sur quoi&nbsp;?</b> Les plantes du jardin.</li>"
                                "<li><b>Au centre&nbsp;:</b> le système d'arrosage connecté.</li><li><b>Dans quel but&nbsp;?</b> Arroser les plantes "
                                "du jardin, même en l'absence de la gardienne, sans gaspiller l'eau.</li></ul>")],
    intro="<p>Le collège doit choisir <b>un</b> système d'arrosage parmi plusieurs modèles vendus dans le commerce. Pour comparer "
          "les modèles, il faut d'abord savoir <b>quoi regarder</b>. La bête à cornes le dit&nbsp;: chaque partie du besoin "
          "demande une caractéristique.</p>",
    consigne="<p>Une <b>caractéristique</b>, c'est ce qui décrit un modèle et qu'on peut comparer d'un modèle à l'autre (une "
             "capacité, une consommation, une durée…). <b>Coche les caractéristiques à prendre en compte pour choisir un système "
             "qui réponde à ce besoin</b>, et laisse celles qui ne le servent pas. Puis <b>relie</b> trois d'entre elles à la "
             "partie du besoin qu'elles servent.</p>",
    critere="les huit cases justes, et chaque caractéristique reliée à la bonne partie du besoin.",
    widgets=[dict(type="cases", name="carac", legende="Les caractéristiques à prendre en compte pour choisir le système",
                  options=[("autonomie", "l'autonomie&nbsp;: combien de jours il arrose seul, sans que personne n'intervienne"),
                           ("eau", "la consommation d'eau par jour, en litres"),
                           ("couleur", "la couleur du boîtier"),
                           ("cuve", "la capacité de la cuve qu'il peut utiliser, en litres"),
                           ("marque", "une marque connue, vue dans une publicité"),
                           ("pluie", "la résistance à la pluie et au soleil, puisqu'il reste dehors"),
                           ("boutons", "le nombre de boutons décoratifs sur le boîtier"),
                           ("reglage", "la facilité de réglage de l'heure et de la quantité d'eau")],
                  bonnes=["autonomie", "eau", "cuve", "pluie", "reglage"],
                  retours={"autonomie": "Oui : « même en l'absence de la gardienne » se mesure en jours d'autonomie.",
                           "eau": "Oui : « sans gaspiller l'eau » se mesure en litres par jour.",
                           "cuve": "Oui : pendant les vacances, la cuve doit contenir assez d'eau pour tous les jours d'absence.",
                           "pluie": "Oui : un système en panne après une averse n'arrose plus rien — et personne n'est là pour le voir.",
                           "reglage": "Oui : c'est la gardienne qui règle le système (la branche « à qui ? »).",
                           "couleur": "La couleur ne change ni l'arrosage, ni l'eau, ni l'absence : elle ne sert pas ce besoin.",
                           "marque": "Une marque connue ne dit rien de ce que fait le système : ce sont ses caractéristiques qui comptent.",
                           "boutons": "Des boutons décoratifs n'aident ni à arroser, ni à économiser l'eau."},
                  indice="Pour chaque ligne, demande-toi : si cette caractéristique changeait, le système répondrait-il mieux ou moins bien au besoin ?"),
             dict(type="classer", name="lien",
                  categories=[("qui", "« à qui&nbsp;? »&nbsp;: la gardienne, qui règle le système"),
                              ("absence", "le but&nbsp;: « même en l'absence de la gardienne »"),
                              ("eau", "le but&nbsp;: « sans gaspiller l'eau »")],
                  items=[("L'autonomie, en jours", "absence", "L'autonomie dit combien de temps le système tient sans personne."),
                         ("La consommation d'eau, en litres par jour", "eau", "Des litres par jour : quelle partie du but parle de l'eau ?"),
                         ("La facilité de réglage", "qui", "Qui règle le système ?")])],
    aides=["<p>Pour chaque caractéristique, demande-toi&nbsp;: si elle changeait, est-ce que le système répondrait mieux ou "
           "moins bien au besoin&nbsp;? Si la réponse est « ça ne change rien », écarte-la.</p>",
           "<p>« Même en l'absence de la gardienne » → combien de jours seul&nbsp;? → <b>l'autonomie</b>&nbsp;; assez d'eau pour ces "
           "jours&nbsp;? → <b>la capacité de la cuve</b>&nbsp;; pas de panne dehors → <b>la résistance à la pluie et au soleil</b>.<br>"
           "« Sans gaspiller l'eau » → <b>la consommation d'eau par jour</b>.<br>"
           "« À qui&nbsp;? » la gardienne → elle règle le système → <b>la facilité de réglage</b>.<br>"
           "La couleur, la marque, les boutons décoratifs → si on les change, l'arrosage reste le même → écartés.</p>"],
    jumeau=dict(consigne="Besoin&nbsp;: à qui&nbsp;? une famille&nbsp;; sur quoi&nbsp;? les boissons et le repas&nbsp;; but&nbsp;: garder le "
                         "pique-nique au frais toute la journée à la plage. Pour choisir une glacière, lesquelles de ces "
                         "caractéristiques comptent&nbsp;: sa capacité en litres&nbsp;; sa couleur&nbsp;; le nombre d'heures pendant lequel "
                         "elle garde le froid&nbsp;; le logo sur le couvercle&nbsp;; son poids&nbsp;?",
                correction="À prendre en compte&nbsp;: <b>la capacité</b> (assez pour toute la famille), <b>le nombre d'heures au frais</b> "
                           "(toute la journée), <b>le poids</b> (on la porte jusqu'au sable). À écarter&nbsp;: la couleur et le logo — ils "
                           "peuvent plaire, mais ils ne servent pas le besoin."),
    correction=[
        "<b>L'autonomie</b> → « même en l'absence de la gardienne »&nbsp;: combien de jours seul&nbsp;? → <b>à prendre en compte</b>",
        "<b>La consommation d'eau par jour</b> → « sans gaspiller l'eau » → <b>à prendre en compte</b>",
        "<b>La capacité de la cuve</b> → assez d'eau pour tous les jours d'absence → <b>à prendre en compte</b>",
        "<b>La résistance à la pluie et au soleil</b> → le système vit dehors&nbsp;; en panne, il n'arrose plus en l'absence de la "
        "gardienne → <b>à prendre en compte</b>",
        "<b>La facilité de réglage</b> → la gardienne règle l'heure et la quantité → <b>à prendre en compte</b>",
        "<b>La couleur, la marque, les boutons décoratifs</b> → si on les change, l'arrosage, l'eau et l'absence restent les mêmes "
        "→ <b>à écarter</b>",
        "<b>Les liens</b> → l'autonomie → « même en l'absence »&nbsp;; la consommation d'eau → « sans gaspiller l'eau »&nbsp;; la "
        "facilité de réglage → « à qui&nbsp;? », la gardienne",
        ("conclusion", "Chaque partie du besoin appelle une <b>caractéristique</b> que l'on peut comparer. Ce qui ne sert pas le "
                       "besoin ne doit pas peser dans le choix."),
    ],
    retenir="pour choisir un objet, on part du <b>besoin</b>&nbsp;: chaque partie de la bête à cornes indique une "
            "<b>caractéristique</b> à comparer (autonomie, consommation, capacité, résistance…).",
    piege="choisir sur ce qui se voit (la couleur, la marque) au lieu de ce qui sert le besoin.",
)

# ─────────────────────────────────────────────────────────────────────────────
# 3e — ÉLARGIR puis ARBITRER (3e_C3.1)
# ─────────────────────────────────────────────────────────────────────────────
E6 = dict(
    id="e6", titre="Établir une liste d'objets ou de systèmes possibles", code="3e_C3.1", duree=12,
    objectif="à partir d'un besoin, établir une liste d'objets ou de systèmes techniques possibles, de familles différentes, "
             "sans y mettre ce qui n'en est pas.",
    production="une liste d'au moins quatre objets ou systèmes techniques qui pourraient répondre au besoin, et la raison "
               "d'une liste longue.",
    mots=MOTS_BESOIN + [
        ("OST", "objet ou système technique&nbsp;: un objet fabriqué (une sirène), ou plusieurs objets qui travaillent ensemble "
         "(une sirène, une antenne et un programme)."),
        ("établir une liste", "chercher le plus de possibilités, de familles différentes, avant de choisir."),
        ("SMS", "un court message écrit envoyé d'un téléphone portable à un autre&nbsp;; on dit aussi « texto ». Le sigle vient de "
         "l'anglais <i>short message service</i>."),
        ("commune", "la ville ou le village, et la mairie qui l'administre."),
        ("cyclone", "une tempête tropicale très violente&nbsp;: vents forts, pluies intenses, mer qui monte. Aux Antilles, la saison "
         "cyclonique va de juin à novembre.")],
    documents=[dict(svg=BAC_ALERTE, legende="Le besoin du quartier, avant de choisir&nbsp;: le produit est encore à trouver.",
                    description="<ul><li><b>À qui&nbsp;?</b> Les habitants du quartier.</li><li><b>Sur quoi&nbsp;?</b> Les habitants du "
                                "quartier, qu'il faut prévenir.</li><li><b>Au centre&nbsp;:</b> une question, quel objet&nbsp;?</li>"
                                "<li><b>Dans quel but&nbsp;?</b> Prévenir les habitants du quartier de l'arrivée d'un cyclone.</li></ul>")],
    intro="<p>À Sainte-Luce, la commune veut mieux protéger un quartier proche de la mer. Avant de construire quoi que ce soit, "
          "l'équipe du projet écrit le <b>besoin</b>&nbsp;: prévenir les habitants du quartier de l'arrivée d'un cyclone. La "
          "commune commande et paie&nbsp;; mais c'est aux <b>habitants</b> que l'objet rendra service. Ici, les mêmes personnes "
          "sont dans les deux cases du haut&nbsp;: l'objet rend service aux habitants en agissant sur eux — il les prévient.</p>",
    consigne="<p>Un <b>OST</b> — un <b>objet ou système technique</b> — est un objet fabriqué, ou plusieurs objets qui "
             "travaillent ensemble. <b>Établis la liste des OST qui pourraient répondre à ce besoin</b>&nbsp;: au moins quatre, un "
             "par ligne, de familles différentes (un son, une lumière ou une image, un téléphone, la voix d'une personne…). Ne "
             "mets dans ta liste <b>ni une personne, ni une action, ni le cyclone lui-même</b>. Puis dis pourquoi une liste "
             "longue vaut mieux qu'une seule idée.</p>",
    critere="au moins quatre OST reconnus, aucun refus, et tu sais dire ce que gagne une liste longue.",
    widgets=[dict(type="liste", name="liste", min=4, lignes=7,
                  label="Mes objets ou systèmes techniques possibles (un par ligne)",
                  attendus=[
                      dict(nom="une sirène", motifs=["sirene", "corne de brume", "klaxon", "alarme sonore", "trompe"]),
                      dict(nom="une application d'alerte sur le smartphone", motifs=["application", r"\bappli", "notification", r"\bapp\b"]),
                      dict(nom="un SMS sur le téléphone", motifs=[r"\bsms\b", "texto", "message", "appel", "telephone", "portable",
                                                                  "smartphone", "mobile"]),
                      dict(nom="un talkie-walkie", motifs=["talkie", "walkie", "emetteur", r"\bcb\b"]),
                      dict(nom="la radio locale", motifs=["radio", r"\bposte\b", r"\bfm\b"]),
                      dict(nom="la télévision", motifs=["televi", r"\btele\b", r"\btv\b", "journal televise"]),
                      dict(nom="un haut-parleur sur une voiture", motifs=[r"haut.?parleur", "megaphone", r"porte.?voix", r"\bsono"]),
                      dict(nom="un gyrophare", motifs=["gyrophare", "clignot", r"\bflash", r"\bfeux?\b", "lumiere qui"]),
                      dict(nom="un panneau lumineux", motifs=["panneau", "ecran", "affich", "lumineux"]),
                      dict(nom="un site internet", motifs=[r"\bsite", "internet", "reseaux? soci", "facebook", "whatsapp", r"e.?mail",
                                                           "courriel", r"\bweb\b"]),
                      dict(nom="les cloches de l'église", motifs=["cloche", "carillon"]),
                  ],
                  refuses=[
                      dict(motifs=[r"^(le |du |faire du |faire le )?porte.?a.?porte\s*$", r"^(fermer|rester|partir|evacuer|courir|"
                                   r"se cacher|se proteger|s'abriter|crier|aller)\b"],
                           message="{ligne} est une action ou une façon de s'organiser, pas un objet ni un système technique. Avec quel objet ? (un mégaphone, un téléphone…)"),
                      dict(motifs=[r"^(la |le |les |l'|des |un |une )?(mairie|maire|commune|pompiers?|gendarmes?|policiers?|voisins?|"
                                   r"benevoles?|habitants?|meteo.?france|prefecture|secouristes?|gens)\b"],
                           message="{ligne} est une personne ou un service : il choisit ou utilise un OST, il n'en est pas un. Quel objet utiliserait-il pour prévenir ?"),
                      dict(motifs=[r"^(le |la |l'|un |une )?(vent|cyclone|ouragan|pluie|nuages?|ciel|mer|houle|danger|peur|securite|tempete)\b"],
                           message="{ligne} n'est pas un objet : c'est le danger lui-même, ou ce qu'on veut obtenir."),
                      dict(motifs=[r"volets?|\babri|bache|sacs? de sable|groupe electrogene|planches?|contreplaque|lampe torche|bougie"],
                           message="{ligne} est bien un objet, mais il protège ; il ne prévient pas. Relis la case « dans quel but ? »."),
                  ],
                  inconnu="{ligne} : je ne le reconnais pas. Vérifie que c'est un objet qu'on peut fabriquer ou acheter, et qu'il "
                          "préviendrait les habitants — ou écris-le avec un autre mot.",
                  exemple="une sirène\nun SMS sur le téléphone\nla radio locale\nun haut-parleur sur une voiture\nun panneau lumineux",
                  etayage=["Un objet qui fait du bruit dans tout le quartier : …",
                           "Un objet que presque chaque habitant a dans sa poche : …",
                           "Un objet qu'on écoute à la maison ou en voiture : …",
                           "Un objet qui montre un message ou une lumière dans la rue : …",
                           "Un objet qui porte la voix d'une personne dans une rue : …"]),
             dict(type="choix", name="longue",
                  legende="Pourquoi établir une longue liste d'OST, au lieu de garder la première idée&nbsp;?",
                  options=[("faiblesses", "Parce que chaque OST a ses faiblesses&nbsp;: si le cyclone coupe le réseau, il faut d'autres moyens."),
                           ("travail", "Parce qu'une liste longue montre qu'on a beaucoup travaillé sur le projet."),
                           ("tous", "Parce qu'il faudra installer tous les OST de la liste, pour être sûr."),
                           ("premiere", "Parce que la première idée est toujours la moins bonne de toutes.")],
                  bonne="faiblesses",
                  retours={"faiblesses": "Oui : le SMS a besoin du réseau téléphonique, que le cyclone peut couper ; la sirène s'entend mal dans une maison fermée. Une liste longue garde d'autres possibilités.",
                           "travail": "Le travail fourni ne dit rien de la qualité du choix : la liste sert à ne pas passer à côté d'un OST qui répondrait mieux au besoin.",
                           "tous": "La liste n'est pas une commande : on choisira ensuite, avec des critères (fonctionner sans électricité, coût…). Établir n'est pas acheter.",
                           "premiere": "La première idée peut être excellente ! Mais sans liste, on ne peut pas le vérifier : c'est la comparaison qui le dit."})],
    aides=["<p>Cherche famille par famille&nbsp;: ce qui fait du bruit&nbsp;; ce qui se voit (une lumière, un écran)&nbsp;; ce que les "
           "habitants ont dans leur poche&nbsp;; ce qu'ils écoutent ou regardent à la maison&nbsp;; ce qui porte la voix d'une "
           "personne. Pour chaque idée, demande-toi&nbsp;: est-ce un objet qu'on pourrait fabriquer ou acheter&nbsp;?</p>",
           "<p>Une sirène → un objet fabriqué ✔ → elle prévient tout le quartier en même temps.<br>"
           "La radio locale → un système (un émetteur, des postes chez les habitants) ✔.<br>"
           "La mairie → un service ✘ → elle choisit l'OST, elle n'en est pas un.<br>"
           "« Fermer les volets » → une action ✘ → elle protège, elle ne prévient pas.<br>"
           "Le vent → le danger lui-même ✘.</p>"],
    jumeau=dict(consigne="Besoin&nbsp;: à qui&nbsp;? les élèves du collège&nbsp;; sur quoi&nbsp;? les élèves&nbsp;; but&nbsp;: leur signaler la "
                         "fin de la récréation. Établis une liste de trois OST possibles.",
                correction="Par exemple&nbsp;: <b>une sonnerie</b> électrique, <b>une cloche</b>, <b>un haut-parleur</b> qui diffuse un "
                           "message, <b>un écran</b> dans la cour, <b>un sifflet</b>. Refusés&nbsp;: « le surveillant » (une personne) et "
                           "« rentrer en classe » (une action)."),
    correction=[
        "<b>Ce qui fait du bruit</b> → une sirène, les cloches de l'église, un haut-parleur ou un mégaphone sur une voiture",
        "<b>Ce qui se voit</b> → un gyrophare, un panneau lumineux à l'entrée du quartier",
        "<b>Ce que les habitants ont dans la poche</b> → un SMS (un texto) sur le téléphone, une application qui envoie une alerte",
        "<b>Ce qu'on écoute ou regarde à la maison</b> → la radio locale, la télévision, un site internet",
        "<b>Ce qui porte la voix</b> → un talkie-walkie pour les secouristes, un mégaphone",
        "<b>Refusés&nbsp;:</b> la mairie, les pompiers, les voisins → des personnes ou des services&nbsp;; « fermer les volets », "
        "« évacuer » → des actions&nbsp;; le porte-à-porte seul → une organisation (avec quel objet&nbsp;?)&nbsp;; le vent, le "
        "cyclone → le danger lui-même&nbsp;; les volets, un abri → des objets, mais ils protègent, ils ne préviennent pas",
        "<b>Pourquoi une liste longue</b> → chaque OST a ses faiblesses&nbsp;: le SMS a besoin du réseau téléphonique, que le "
        "cyclone peut couper&nbsp;; la sirène s'entend mal dans une maison fermée → d'autres OST prennent le relais",
        "Refusés&nbsp;: « on a beaucoup travaillé » → la quantité de travail ne dit rien du choix&nbsp;; « tout installer » → établir "
        "n'est pas acheter&nbsp;; « la première idée est mauvaise » → elle peut être la meilleure, la liste sert à le vérifier.",
        ("conclusion", "Établir une liste, c'est <b>élargir</b> avant de choisir&nbsp;: un but écrit sans solution laisse entrer des "
                       "OST de familles différentes. On ne choisit qu'ensuite, avec des critères."),
    ],
    retenir="pour établir une liste d'OST possibles, on part d'un but <b>sans solution</b> et on cherche dans des <b>familles "
            "différentes</b>&nbsp;; une personne, une action ou le danger lui-même ne sont pas des OST.",
    piege="mettre dans la liste une personne (la mairie, les pompiers) ou une action (évacuer)&nbsp;: ce ne sont ni des objets ni "
          "des systèmes techniques.",
)

E7 = dict(
    id="e7", titre="Un besoin mal formulé ferme la liste", code="3e_C3.1", duree=10,
    objectif="repérer les erreurs d'une bête à cornes, comprendre pourquoi un but qui nomme une solution ferme la liste des OST "
             "possibles, et réécrire ce but.",
    production="les trois cases jugées, la raison du problème, et le but réécrit sans solution.",
    mots=[("formuler", "dire ou écrire avec des mots précis."),
          ("une idée (et non une chose)", "ce qu'on ne peut ni voir ni toucher&nbsp;: la sécurité, le confort, la santé. On peut "
           "vouloir l'obtenir, mais on n'agit pas « sur » elle."),
          ("solution technique", "une pièce ou un moyen qui dit <b>comment</b> on répond au besoin&nbsp;: un SMS, une sirène, "
           "une radio. Sa place est dans la liste des OST, pas dans le but."),
          ("SMS", "un court message écrit envoyé d'un téléphone portable à un autre (un « texto »).")],
    documents=[dict(svg=BAC_MAL, legende="La bête à cornes d'une autre équipe&nbsp;: trouve ce qui ne va pas.",
                    description="<ul><li><b>À qui&nbsp;?</b> Les habitants du quartier.</li><li><b>Sur quoi&nbsp;?</b> La sécurité du "
                                "quartier.</li><li><b>Au centre&nbsp;:</b> une question, quel objet&nbsp;?</li>"
                                "<li><b>Dans quel but&nbsp;?</b> Envoyer un SMS aux habitants.</li></ul>")],
    intro="<p>Une autre équipe a commencé le même projet d'alerte. Voici sa bête à cornes. Résultat&nbsp;: sa liste d'OST ne "
          "contient qu'une ligne — « un SMS ».</p>",
    consigne="<p>Dans une bête à cornes, la case « sur quoi&nbsp;? » nomme <b>une personne ou une chose</b> sur laquelle l'objet "
             "agit, et le but s'écrit avec un verbe à l'infinitif <b>sans nommer de solution</b>. <b>Juge chaque case</b>&nbsp;: "
             "juste, ou à corriger&nbsp;? Puis <b>dis pourquoi</b> ce but a fermé la liste, et <b>réécris-le</b>.</p>",
    critere="trois cases bien jugées, la bonne raison, et un but réécrit qui dit qui prévenir et de quel danger, sans aucune solution.",
    widgets=[dict(type="classer", name="cases",
                  categories=[("juste", "juste"),
                              ("idee", "à corriger&nbsp;: c'est une idée, pas une personne ni une chose"),
                              ("solution", "à corriger&nbsp;: elle nomme déjà une solution")],
                  items=[("Case « à qui&nbsp;? »&nbsp;: « les habitants du quartier »", "juste", "Case « à qui ? » : qui l'objet aidera-t-il ?"),
                         ("Case « sur quoi&nbsp;? »&nbsp;: « la sécurité du quartier »", "idee", "Case « sur quoi ? » : la sécurité, peut-on la toucher, la déplacer, la prévenir ?"),
                         ("Case « dans quel but&nbsp;? »&nbsp;: « envoyer un SMS aux habitants »", "solution", "Case « dans quel but ? » : un SMS, est-ce ce qu'on veut obtenir, ou un moyen d'y arriver ?")]),
             dict(type="choix", name="pourquoi", legende="Pourquoi ce but a-t-il fermé la liste des OST possibles&nbsp;?",
                  options=[("ferme", "Il nomme déjà une solution&nbsp;: seul le SMS entre dans la liste, et ceux qui n'ont pas de réseau sont oubliés."),
                           ("mauvais", "Parce que le SMS est une mauvaise solution, qu'il faut interdire."),
                           ("court", "Parce qu'un but doit toujours tenir sur plusieurs lignes pour être complet."),
                           ("habitants", "Parce qu'un but ne doit jamais nommer les habitants.")],
                  bonne="ferme",
                  retours={"ferme": "Oui : un but qui nomme une solution donne la réponse avant d'avoir cherché.",
                           "mauvais": "Le SMS n'est pas une mauvaise solution : il a sa place DANS la liste, à côté de la sirène ou de la radio. Ce qui ne va pas, c'est de l'écrire dans le but.",
                           "court": "La longueur ne compte pas : « prévenir les habitants de l'arrivée d'un cyclone » est court, et juste.",
                           "habitants": "Au contraire : le but dit qui l'objet doit prévenir. Les habitants y ont leur place ; c'est le SMS qui n'y a pas la sienne."}),
             dict(type="texte", name="but", lignes=3,
                  label="Réécris le but, sans nommer aucune solution.",
                  criteres=[dict(label="ton but commence par un verbe à l'infinitif (prévenir, avertir…)", motifs=[VERBE],
                                 manque="Commence ton but par un verbe à l'infinitif : « Prévenir… », « Avertir… »."),
                            dict(label="il dit qui prévenir&nbsp;: les habitants du quartier",
                                 motifs=[r"habitant|population|\bgens\b|familles?|personnes|\bmonde\b|quartier|riverain|voisin|resident"],
                                 manque="Dis QUI doit être prévenu."),
                            dict(label="il dit de quoi&nbsp;: le cyclone, le danger",
                                 motifs=[r"cyclone|ouragan|tempete|danger|alerte|menace|risque|vent violent|intemperie|catastrophe"],
                                 manque="Dis DE QUOI il faut prévenir : de quel danger ?")],
                  interdits=[dict(motifs=[SOL_ALERTE],
                                  message="Ton but nomme encore une solution (un SMS, un message, une sirène, la radio, une application…). "
                                          "Garde ces idées pour la liste des OST : le but dit seulement ce qu'il faut obtenir.")],
                  exemple="Prévenir les habitants du quartier de l'arrivée d'un cyclone, à temps pour qu'ils se mettent à l'abri.",
                  etayage=["Prévenir … de …, pour qu'ils …", "Avertir les habitants du quartier que …"])],
    aides=["<p>Pour la case « sur quoi&nbsp;? », demande-toi&nbsp;: peut-on toucher, déplacer ou prévenir ce qui est écrit&nbsp;? Pour "
           "le but, demande-toi&nbsp;: est-ce ce qu'on veut obtenir, ou un moyen d'y arriver&nbsp;?</p>",
           "<p>« Les habitants du quartier » → c'est eux que l'objet aidera → juste.<br>"
           "« La sécurité du quartier » → une idée, qu'on ne touche pas → c'est ce qu'on veut obtenir&nbsp;; dans la case, on met "
           "<b>les habitants</b>, que l'objet prévient.<br>"
           "« Envoyer un SMS » → un moyen, une solution → la liste ne contiendra que lui.<br>"
           "Réécrire → un verbe (prévenir) + qui (les habitants) + de quoi (le cyclone), et aucun objet.</p>"],
    jumeau=dict(consigne="Pour la cantine, une bête à cornes dit&nbsp;: à qui&nbsp;? les élèves&nbsp;; sur quoi&nbsp;? les élèves&nbsp;; "
                         "but&nbsp;: « installer un écran qui affiche le menu ». Qu'est-ce qui ne va pas&nbsp;? Réécris le but.",
                correction="Le but nomme une solution (un écran). Réécrit&nbsp;: « <b>Informer les élèves du menu du jour</b> ». La liste "
                           "s'ouvre alors&nbsp;: un écran, une affiche, une annonce au haut-parleur, un message sur l'espace numérique "
                           "du collège…"),
    correction=[
        '<figure class="figure">' + BAC_ALERTE_C + '<figcaption>La bête à cornes corrigée&nbsp;: les habitants dans les deux '
        'cases du haut, et un but sans solution.</figcaption></figure>',
        "<b>« À qui&nbsp;? » — les habitants du quartier</b> → c'est eux que l'objet aidera → <b>juste</b>",
        "<b>« Sur quoi&nbsp;? » — la sécurité du quartier</b> → une idée, qu'on ne peut ni toucher ni prévenir → c'est ce qu'on "
        "veut obtenir → <b>à corriger</b>&nbsp;: l'objet agit sur <b>les habitants</b>, il les prévient",
        "<b>« Dans quel but&nbsp;? » — envoyer un SMS</b> → un moyen, une solution → <b>à corriger</b>",
        "<b>Pourquoi la liste s'est fermée</b> → le but donnait déjà la réponse&nbsp;: seul le SMS pouvait y entrer. Les habitants "
        "sans téléphone, ou privés de réseau quand le cyclone frappe, étaient oubliés.",
        "Refusés&nbsp;: « le SMS est mauvais » → non, il reste une bonne idée, à sa place dans la liste&nbsp;; « un but doit être "
        "long » → la longueur ne compte pas&nbsp;; « ne jamais nommer les habitants » → au contraire, ils doivent y être.",
        "<b>Un but attendu&nbsp;:</b> « Prévenir les habitants du quartier de l'arrivée d'un cyclone. » → un verbe, qui, de quoi, "
        "et aucune solution",
        ("conclusion", "Un but qui nomme une solution <b>ferme</b> la liste avant qu'on la fasse. Écrit sans solution, il "
                       "l'<b>ouvre</b>&nbsp;: c'est ensuite, avec des critères, qu'on choisit."),
    ],
    retenir="un but qui nomme une solution ferme la liste des OST possibles&nbsp;; on l'écrit avec un verbe, en disant <b>qui</b> "
            "et <b>de quoi</b>, et on garde les solutions pour la liste.",
    piege="croire que la solution écrite dans le but est mauvaise&nbsp;: elle est peut-être bonne — mais à sa place, dans la "
          "liste, pas dans le but.",
)

# ─────────────────────────────────────────────────────────────────────────────
# Le cours, niveau par niveau
# ─────────────────────────────────────────────────────────────────────────────
BETE_VERS_PIEUVRE = figures.bete_vers_pieuvre(
    "bc-bp", "Léa", "ses enfants", "le vélo-cargo", "transporter ses enfants en ville",
    "permettre à Léa de transporter ses enfants", "protéger les enfants pendant le trajet",
    "De la bête à cornes au diagramme pieuvre",
    "À gauche, la bête à cornes du vélo-cargo : repère 1, à qui rend-il service ? Léa ; repère 2, sur quoi agit-il ? ses "
    "enfants ; la corne bleue relie les deux en passant sous le vélo-cargo ; repère 3, dans quel but ? transporter ses "
    "enfants en ville. Une flèche marquée « devient » mène à droite, au diagramme pieuvre : la bulle Léa (repère 1) et la "
    "bulle ses enfants (repère 2) sont en haut ; la courbe bleue FP1 part de Léa, descend passer par le vélo-cargo et "
    "remonte aux enfants, comme la corne. Un trait rouge FC1 relie le vélo-cargo aux enfants. En dessous, repère 3 : FP1, "
    "permettre à Léa de transporter ses enfants ; FC1, protéger les enfants pendant le trajet. Légende : le repère 1 est "
    "la bulle d'où part la FP1, le repère 2 la bulle où elle arrive, le repère 3 la phrase de la FP1.")

COURS = {
    "5e": ("<h3>Le besoin</h3><ul>"
           "<li>Un <b>besoin</b>, c'est ce qui manque à quelqu'un, ou ce qui lui est nécessaire. Un objet technique existe parce "
           "que quelqu'un en a besoin.</li>"
           "<li>Avant de choisir ou de fabriquer un objet, on <b>exprime le besoin</b>. Le schéma le plus courant pour le faire "
           "s'appelle la <b>bête à cornes</b>.</li></ul>"
           "<h3>Trois questions, trois cases</h3>"
           '<div class="defile"><table><caption>La bête à cornes du vélo-cargo de Léa</caption>'
           "<tr><th>Question</th><th>Ce qu'on y écrit</th><th>Pour le vélo-cargo</th></tr>"
           "<tr><td>À qui le produit rend-il service&nbsp;?</td><td>la personne que l'objet aide, celle qui s'en sert</td><td>Léa</td></tr>"
           "<tr><td>Sur quoi le produit agit-il&nbsp;?</td><td>la personne ou la chose que l'objet déplace, touche ou transforme</td>"
           "<td>ses deux enfants et ses courses</td></tr>"
           "<tr><td>Dans quel but&nbsp;?</td><td>pourquoi l'objet existe, avec un verbe à l'infinitif</td>"
           "<td>transporter ses enfants et ses courses en ville</td></tr></table></div>"
           "<h3>Lire une bête à cornes</h3><ul>"
           "<li>Elle se lit comme une phrase&nbsp;: « Le vélo-cargo rend service <b>à</b> Léa, en agissant <b>sur</b> ses enfants et "
           "ses courses, <b>pour</b> les transporter en ville. »</li>"
           "<li>Le produit est au milieu. Il peut rester un point d'interrogation&nbsp;: on exprime le besoin <b>avant</b> de "
           "connaître l'objet.</li></ul>"
           "<h3>Écrire le but</h3><ul>"
           "<li>Un <b>verbe à l'infinitif</b>&nbsp;: transporter, éclairer, arroser, prévenir…</li>"
           "<li><b>Aucune solution</b>&nbsp;: le but dit <i>pourquoi</i> l'objet existe, pas <i>comment</i> il est fait. « Éclairer "
           "la rue du parking la nuit », pas « allumer une ampoule ».</li></ul>"
           "<h3>Trois pièges</h3><ul>"
           "<li>Celui qui <b>paie</b> ou commande l'objet (la mairie) n'est pas forcément celui à qui il <b>rend service</b> (les "
           "piétons).</li>"
           "<li>La case « sur quoi&nbsp;? » nomme une personne ou une chose, pas une idée&nbsp;: « la rue », pas « la sécurité ».</li>"
           "<li>La bête à cornes ne liste pas ce que l'objet doit respecter (résister à la pluie…)&nbsp;: c'est le rôle du "
           "diagramme des interacteurs extérieurs, souvent appelé diagramme pieuvre.</li></ul>"
           "<h3>Ensuite&nbsp;: la bête à cornes devient la fonction principale du diagramme pieuvre</h3>"
           "<ul><li>La corne relie «&nbsp;à qui&nbsp;?&nbsp;» et «&nbsp;sur quoi&nbsp;?&nbsp;» en passant par le produit. Dans le "
           "diagramme pieuvre, la même liaison s'appelle la <b>fonction principale</b> FP1&nbsp;: elle part de Léa, passe par le "
           "vélo-cargo et arrive aux enfants.</li>"
           "<li>Sa phrase dit le but&nbsp;: «&nbsp;permettre à Léa de transporter ses enfants&nbsp;». La FP1 décrit donc la "
           "<b>fonction d'usage</b>.</li>"
           "<li>Au bout de la FP1, les enfants imposent aussi une condition&nbsp;: c'est souvent la FC1 (les protéger pendant le "
           "trajet).</li></ul>"
           '<figure class="figure">' + BETE_VERS_PIEUVRE + '<figcaption>La même liaison, deux fois&nbsp;: la corne de la bête à '
           'cornes devient la fonction principale FP1. Les repères ①②③ se répondent d\'un schéma à l\'autre.</figcaption></figure>' 
           "<h3>Choisir un objet</h3><ul>"
           "<li>Un objet répond au besoin s'il remplit <b>les trois branches</b> à la fois&nbsp;; une seule branche qui échoue "
           "suffit à l'écarter.</li>"
           "<li>Le but devient la <b>fonction d'usage</b> de l'objet choisi&nbsp;: ce à quoi il sert.</li></ul>"),
    "4e": ("<h3>Rappel&nbsp;: la bête à cornes</h3><ul>"
           "<li>Trois questions&nbsp;: à qui le produit rend-il service&nbsp;? sur quoi agit-il&nbsp;? dans quel but&nbsp;?</li>"
           "<li>Le but, écrit avec un verbe à l'infinitif et sans solution, est la <b>fonction d'usage</b> de l'objet.</li></ul>"
           "<h3>Quand le besoin évolue, l'objet évolue</h3><ul>"
           "<li>Un besoin évolue avec la façon de vivre (les vacances, le travail loin de chez soi), avec une <b>invention</b> ou "
           "une <b>innovation</b> qui rend possible ce qui ne l'était pas, et avec le <b>développement durable</b> (économiser "
           "l'eau, l'énergie).</li>"
           "<li>Pour <b>justifier</b> l'évolution d'un objet, on compare les bêtes à cornes d'avant et d'après, partie par partie. "
           "Souvent, c'est le <b>but</b> qui s'enrichit&nbsp;: « arroser les plantes » devient « arroser les plantes, même en "
           "l'absence de la gardienne, sans gaspiller l'eau ».</li>"
           "<li>Une panne ou la mode ne justifient pas une évolution&nbsp;: un objet cassé se remplace par le même.</li></ul>"
           "<h3>Du besoin aux caractéristiques</h3><ul>"
           "<li>Une <b>caractéristique</b> décrit un modèle et se compare d'un modèle à l'autre&nbsp;: une capacité, une "
           "consommation, une durée, une résistance.</li>"
           "<li>Chaque partie du besoin appelle une caractéristique à comparer&nbsp;:</li></ul>"
           '<div class="defile"><table><caption>Le système d\'arrosage du jardin</caption>'
           "<tr><th>Partie du besoin</th><th>Caractéristique à comparer</th><th>Unité</th></tr>"
           "<tr><td>« même en l'absence de la gardienne »</td><td>l'autonomie</td><td>jours</td></tr>"
           "<tr><td>« sans gaspiller l'eau »</td><td>la consommation d'eau</td><td>litres par jour</td></tr>"
           "<tr><td>« à qui&nbsp;? » la gardienne, qui règle le système</td><td>la facilité de réglage</td><td>minutes pour régler</td></tr>"
           "</table></div><ul>"
           "<li>Le programme cite aussi des critères de choix valables pour presque tous les objets&nbsp;: la <b>qualité</b>, "
           "l'<b>efficacité énergétique</b>, la <b>durabilité</b>, la <b>recyclabilité</b>.</li>"
           "<li>On écarte ce qui ne sert pas le besoin (la couleur, la marque, un bouton décoratif)&nbsp;: si on le change, l'objet "
           "répond tout aussi bien.</li></ul>"),
    "3e": ("<h3>Rappel&nbsp;: un besoin bien écrit</h3><ul>"
           "<li>À qui&nbsp;? sur quoi&nbsp;? dans quel but&nbsp;? Le but commence par un verbe à l'infinitif et ne nomme <b>aucune "
           "solution</b>.</li>"
           "<li>Les mêmes personnes peuvent être dans les deux cases du haut&nbsp;: un réveil rend service à l'élève et agit sur "
           "l'élève — il le réveille&nbsp;; la station d'alerte rend service aux habitants et agit sur eux — elle les prévient.</li>"
           "<li>Celui qui commande et paie (la commune) n'est pas forcément celui à qui l'objet rend service (les habitants).</li></ul>"
           "<h3>Établir une liste d'OST possibles</h3><ul>"
           "<li>Un <b>OST</b> est un <b>objet ou système technique</b>&nbsp;: un objet fabriqué, ou plusieurs objets qui travaillent "
           "ensemble.</li>"
           "<li><b>Élargir</b>&nbsp;: chercher famille par famille (le son, la lumière ou l'image, le téléphone, la voix d'une "
           "personne…), sans juger trop tôt.</li>"
           "<li>Ne pas mettre dans la liste&nbsp;: une <b>personne</b> ou un service (la mairie), une <b>action</b> (évacuer), le "
           "danger lui-même (le vent), ni un objet qui répond à un autre but (des volets protègent, ils ne préviennent pas).</li></ul>"
           "<h3>Un but qui nomme une solution ferme la liste</h3><ul>"
           "<li>« Envoyer un SMS aux habitants » donne la réponse avant d'avoir cherché&nbsp;: la liste ne contient qu'une ligne, "
           "et ceux qui n'ont pas de réseau sont oubliés.</li>"
           "<li>La solution n'est pas mauvaise pour autant&nbsp;: sa place est <b>dans la liste</b>, pas dans le but.</li></ul>"
           "<h3>Et ensuite&nbsp;?</h3><ul>"
           "<li>Une fois la liste établie, on <b>choisit</b>&nbsp;: on compare les OST selon des critères (fonctionner sans "
           "électricité, coût, entretien…) et on argumente son choix.</li></ul>"),
}

# ─────────────────────────────────────────────────────────────────────────────
# Les trois niveaux
# ─────────────────────────────────────────────────────────────────────────────
NIVEAUX = {
    "5e": dict(
        codes=["5e_C3.3"],
        mission="Dire en trois questions le besoin auquel répond un objet, puis s'en servir pour choisir un objet.",
        avant=[("Je sais dire à quoi sert un objet de ma vie de tous les jours, en une phrase.",
                "cycle 3 — sciences et technologie", "@synthese#les-mots", "les mots de l'atelier, dans la synthèse (2 minutes)"),
               ("Je sais distinguer la personne qui se sert d'un objet et ce que cet objet transporte ou transforme.",
                "cycle 3 — sciences et technologie", "@synthese#les-mots", "les mots de l'atelier, dans la synthèse (2 minutes)")],
        situation_titre="Deux noms pour une même idée",
        situation="<p>Avant de fabriquer ou de choisir un objet, on se demande <b>à quoi il doit servir</b>&nbsp;: le programme "
                  "de technologie parle d'<b>exprimer le besoin</b>. On pose trois questions&nbsp;:</p>"
                  "<ul><li><b>à qui</b> l'objet rend-il service&nbsp;?</li><li><b>sur quoi</b> agit-il&nbsp;?</li>"
                  "<li><b>dans quel but</b> existe-t-il&nbsp;?</li></ul>"
                  "<p>Le schéma qui rassemble les trois réponses s'appelle souvent la <b>bête à cornes</b>&nbsp;: avec ses deux "
                  "cases en haut et sa grande courbe, il fait penser à une tête de taureau.</p>"
                  "<p>Dans cet atelier, tu lis la bête à cornes du <b>vélo-cargo</b> de Léa, tu complètes celle du <b>lampadaire "
                  "intelligent</b> d'un parking de Sainte-Luce, puis tu t'en sers pour <b>choisir</b> un objet.</p>",
        question="Comment dire, en peu de mots, ce qu'un objet doit faire — avant même de savoir quel objet choisir&nbsp;?",
        hypothese_amorces=["Je pense qu'il faut d'abord savoir pour qui…", "Pour dire à quoi sert un objet, j'écrirais…",
                           "Avant de choisir un objet, je regarderais…"],
        exercices=[E1, E2, E3],
        a_retenir="<ul><li>Le <b>besoin</b> s'exprime avec trois questions&nbsp;: <b>à qui</b> le produit rend-il service&nbsp;? "
                  "<b>sur quoi</b> agit-il&nbsp;? <b>dans quel but</b>&nbsp;? Le schéma qui les rassemble s'appelle souvent la "
                  "<b>bête à cornes</b>.</li>"
                  "<li>Le <b>but</b> s'écrit avec un verbe à l'infinitif et ne nomme <b>aucune solution</b>&nbsp;: il dit pourquoi, "
                  "pas comment. Il devient la <b>fonction d'usage</b> de l'objet.</li>"
                  "<li>Celui qui paie n'est pas forcément celui à qui l'objet rend service.</li>"
                  "<li>Un objet répond au besoin s'il remplit <b>les trois branches</b> à la fois&nbsp;: c'est ainsi qu'on choisit "
                  "parmi plusieurs objets.</li></ul>",
        bonus=[dict(titre="La bête à cornes de ta brosse à dents",
                    consigne="<p>Écris les trois cases de la bête à cornes d'une <b>brosse à dents</b>&nbsp;: à qui, sur quoi, et le "
                             "but — sans nommer de solution (ni poils, ni manche).</p>",
                    correction=["<b>À qui&nbsp;?</b> → la personne qui se brosse les dents",
                                "<b>Sur quoi&nbsp;?</b> → ses dents",
                                "<b>But</b> → nettoyer ses dents (ou&nbsp;: garder ses dents propres)",
                                ("conclusion", "Les poils et le manche disent <i>comment</i>&nbsp;: ce sont des solutions, pas le but.")]),
               dict(titre="Le pêcheur et ses poissons",
                    consigne="<p>Besoin&nbsp;: à qui&nbsp;? un pêcheur de Sainte-Luce&nbsp;; sur quoi&nbsp;? ses poissons&nbsp;; but&nbsp;: garder "
                             "ses poissons frais jusqu'au marché. Propose <b>deux objets</b> qui répondent, et <b>un</b> qui n'y "
                             "répond pas, en disant quelle branche échoue.</p>",
                    correction=["<b>Répondent</b> → une glacière, une caisse remplie de glace",
                                "<b>Ne répond pas</b> → un seau d'eau laissé au soleil → le but échoue&nbsp;: les poissons ne restent pas frais",
                                ("conclusion", "Plusieurs objets peuvent répondre au même besoin&nbsp;: on choisira ensuite entre eux.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre « à qui&nbsp;? » et « sur quoi&nbsp;? », ou entre un but et une "
                      "solution. Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
    "4e": dict(
        codes=["4e_C1.3", "4e_C3.1"],
        mission="Comparer deux besoins pour expliquer pourquoi un objet évolue, puis tirer du besoin ce qu'il faut regarder pour "
                "choisir.",
        avant=[("Je sais lire et compléter une bête à cornes&nbsp;: à qui, sur quoi, dans quel but.",
                "5e_C3.3", "@niveau:5e#bc_5e_e1", "l'atelier de 5e, exercices 1 et 2 (16 minutes)"),
               ("Je sais écrire un but avec un verbe à l'infinitif, sans nommer de solution.",
                "5e_C3.3", "@niveau:5e#bc_5e_e2", "l'atelier de 5e, exercice 2 (10 minutes)")],
        situation_titre="Deux noms pour une même idée",
        situation="<p>Dire à qui un objet rend service, sur quoi il agit et dans quel but&nbsp;: le programme de technologie "
                  "appelle cela <b>exprimer le besoin</b>, et le schéma qui le montre s'appelle souvent la <b>bête à "
                  "cornes</b>. En 4e, on s'en sert pour deux choses&nbsp;: <b>expliquer</b> pourquoi un objet a changé — parce "
                  "que le besoin a changé — et <b>savoir quoi comparer</b> avant de choisir un objet.</p>"
                  "<p>Dans cet atelier, l'objet est le <b>système d'arrosage connecté</b> du jardin partagé du collège.</p>",
        question="Pourquoi un objet change-t-il au fil du temps, et comment savoir ce qu'il faut regarder pour en choisir un&nbsp;?",
        hypothese_amorces=["Je pense qu'un objet change quand…", "Pour choisir entre deux modèles, je comparerais…",
                           "Ce qui ne compte pas pour choisir, c'est…"],
        exercices=[E4, E5],
        a_retenir="<ul><li>Un objet <b>évolue</b> parce que le <b>besoin</b> évolue&nbsp;: nouvelles façons de vivre, inventions et "
                  "innovations, développement durable.</li>"
                  "<li>Pour <b>justifier</b> une évolution, on compare les bêtes à cornes d'avant et d'après&nbsp;: la partie qui "
                  "change — souvent le but — dit ce que l'objet doit faire de nouveau.</li>"
                  "<li>Le nouveau but s'écrit avec un verbe à l'infinitif, <b>sans nommer de solution</b>.</li>"
                  "<li>Pour <b>choisir</b> un objet, chaque partie du besoin indique une <b>caractéristique</b> à comparer "
                  "(autonomie, consommation, capacité, résistance…)&nbsp;; ce qui ne sert pas le besoin est écarté.</li></ul>",
        bonus=[dict(titre="De la lampe à pétrole à la lampe solaire",
                    consigne="<p>Autrefois, beaucoup de familles s'éclairaient le soir avec une lampe à pétrole. Aujourd'hui, on "
                             "garde une lampe solaire pour les coupures de courant après un cyclone. Quelle partie du besoin a "
                             "changé&nbsp;? Écris le nouveau but.</p>",
                    correction=["<b>À qui&nbsp;?</b> → la famille → pareil",
                                "<b>Sur quoi&nbsp;?</b> → la pièce de la maison → pareil",
                                "<b>Le but</b> change&nbsp;: « éclairer la pièce le soir » devient « éclairer la pièce le soir, même "
                                "pendant une coupure de courant, sans fumée ni flamme »",
                                ("conclusion", "Le panneau solaire et la batterie sont des solutions&nbsp;: ils n'entrent pas dans le but.")]),
               dict(titre="Lire une fiche de produit",
                    consigne="<p>Sur la fiche d'un système d'arrosage, tu lis&nbsp;: <i>autonomie 10 jours · consommation 8 litres "
                             "par jour · boîtier « bleu lagon » · résiste à la pluie · réglage en 2 minutes</i>. Quelles lignes "
                             "servent le besoin du jardin&nbsp;? Laquelle ne sert à rien pour le choix&nbsp;?</p>",
                    correction=["<b>Servent le besoin</b> → l'autonomie (l'absence de la gardienne), la consommation (ne pas "
                                "gaspiller), la résistance à la pluie (il vit dehors), le réglage (la gardienne)",
                                "<b>Ne sert à rien pour le choix</b> → la couleur « bleu lagon »",
                                ("conclusion", "Une fiche de produit se lit avec le besoin à côté&nbsp;: chaque ligne utile répond à une "
                                               "partie de la bête à cornes.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre ce qui a changé et ce qui est resté pareil, ou entre une "
                      "caractéristique utile et une caractéristique qui ne sert pas le besoin. Qu'est-ce que tu dois encore revoir, "
                      "et comment&nbsp;?",
    ),
    "3e": dict(
        codes=["3e_C3.1"],
        mission="Partir d'un besoin bien écrit pour établir une liste large d'objets ou de systèmes possibles — et voir ce "
                "qu'un besoin mal écrit fait perdre.",
        avant=[("Je sais formuler un but avec un verbe à l'infinitif, sans nommer de solution, et dire pourquoi un objet évolue "
                "quand le besoin évolue.", "4e_C1.3", "@niveau:4e#bc_4e_e4", "l'atelier de 4e, exercice 1 (12 minutes)"),
               ("Je sais dire quelles caractéristiques comptent pour choisir un objet qui répond à un besoin.",
                "4e_C3.1", "@niveau:4e#bc_4e_e5", "l'atelier de 4e, exercice 2 (10 minutes)")],
        situation_titre="Deux noms pour une même idée",
        situation="<p>Avant de chercher des solutions, on écrit le <b>besoin</b>&nbsp;: à qui l'objet rendra service, sur quoi il "
                  "agira, dans quel but. C'est ce que le programme appelle <b>exprimer le besoin</b>&nbsp;; le schéma qui le "
                  "montre s'appelle souvent la <b>bête à cornes</b>. En 3e, on s'en sert pour <b>établir une liste</b> "
                  "d'objets ou de systèmes techniques possibles — avant de choisir.</p>"
                  "<p>Dans cet atelier, le projet est celui d'une <b>alerte cyclonique</b> pour un quartier de Sainte-Luce.</p>",
        question="Comment trouver toutes les solutions possibles à un besoin, sans s'enfermer dans la première idée&nbsp;?",
        hypothese_amorces=["Je pense qu'il faut d'abord écrire…", "Pour ne pas m'enfermer dans une idée, je…",
                           "Une liste de solutions est utile parce que…"],
        exercices=[E6, E7],
        a_retenir="<ul><li>Pour <b>établir une liste d'OST possibles</b> (objets ou systèmes techniques), on part d'un besoin "
                  "dont le but ne nomme <b>aucune solution</b>.</li>"
                  "<li>On cherche dans des <b>familles différentes</b>&nbsp;; une personne, une action ou le danger lui-même ne "
                  "sont pas des OST.</li>"
                  "<li>Un but qui nomme une solution <b>ferme</b> la liste avant qu'on la fasse&nbsp;: la solution n'est pas "
                  "mauvaise, mais sa place est dans la liste.</li>"
                  "<li>La liste établie, on <b>choisit</b> ensuite, avec des critères, et on argumente.</li></ul>",
        bonus=[dict(titre="Le réveil",
                    consigne="<p>Écris la bête à cornes d'un <b>réveil</b>. Pourquoi la même personne est-elle dans les deux cases "
                             "du haut&nbsp;?</p>",
                    correction=["<b>À qui&nbsp;?</b> → l'élève qui doit se lever",
                                "<b>Sur quoi&nbsp;?</b> → l'élève lui-même&nbsp;: c'est lui que le réveil réveille",
                                "<b>But</b> → réveiller l'élève à l'heure choisie",
                                ("conclusion", "L'objet rend service à la personne en agissant sur elle&nbsp;: les deux cases portent "
                                               "alors le même nom, et ce n'est pas une erreur.")]),
               dict(titre="Après le cyclone",
                    consigne="<p>Nouveau besoin&nbsp;: <i>permettre aux habitants de donner des nouvelles à leur famille après le "
                             "cyclone, même si le réseau est coupé</i>. Établis une liste de quatre OST possibles.</p>",
                    correction=["<b>Possibles</b> → un téléphone satellite, une radio amateur, un talkie-walkie, une borne de "
                                "recharge solaire pour les téléphones, un panneau d'affichage à la mairie",
                                "<b>Refusés</b> → « attendre le retour du réseau » (une action), « les voisins » (des personnes)",
                                ("conclusion", "« Même si le réseau est coupé » élargit la liste vers des OST qui n'en ont pas besoin.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre un objet et une action, ou entre un but et une solution. Qu'est-ce "
                      "que tu dois encore revoir, et comment&nbsp;?",
    ),
}

# ─────────────────────────────────────────────────────────────────────────────
# Ce que le reste du site lit de cet atelier
# ─────────────────────────────────────────────────────────────────────────────
MODULE = "besoin"
NOM_PANNEAU = "bete_a_cornes"
PANNEAU_TEXTE = {
    "5e": "Le <b>besoin</b> — souvent représenté par la <b>bête à cornes</b> — sur un vélo-cargo et un lampadaire de "
          "Sainte-Luce&nbsp;: tu lis les trois questions (à qui&nbsp;? sur quoi&nbsp;? dans quel but&nbsp;?), tu en complètes une, "
          "puis tu choisis l'objet qui répond au besoin.",
    "4e": "Le <b>besoin</b> — souvent représenté par la <b>bête à cornes</b> — sur le système d'arrosage du jardin&nbsp;: tu "
          "compares deux besoins pour justifier l'évolution de l'objet, puis tu tires du besoin les caractéristiques qui "
          "comptent pour choisir.",
    "3e": "Le <b>besoin</b> — souvent représenté par la <b>bête à cornes</b> — sur un projet d'alerte cyclonique&nbsp;: tu "
          "établis une liste d'objets ou de systèmes techniques possibles, puis tu vois comment un besoin mal écrit la ferme.",
}
IMAGES = {
    "bete_a_cornes_velo_cargo.svg": BAC_VELO,
    "bete_a_cornes_lampadaire_a_completer.svg": BAC_LAMPE,
    "bete_a_cornes_lampadaire_corrige.svg": BAC_LAMPE_C,
    "bete_a_cornes_besoin_de_lea.svg": BAC_BESOIN,
    "bete_a_cornes_arrosoir.svg": BAC_ARROSOIR,
    "bete_a_cornes_arrosage_connecte.svg": BAC_ARROSAGE_C,
    "bete_a_cornes_alerte_cyclonique.svg": BAC_ALERTE,
    "bete_a_cornes_alerte_mal_formulee.svg": BAC_MAL,
}
VOCAB_EN = [("besoin", "need"), ("bête à cornes", "need diagram"), ("rendre service", "to serve, to help"),
            ("but", "purpose"), ("fonction d'usage", "use function"), ("usager", "user"),
            ("solution technique", "technical solution"), ("caractéristique", "characteristic"),
            ("autonomie", "autonomy, running time"), ("évolution", "evolution, development")]
VERBES = {"5e": "<b>reconnaître</b> le besoin&nbsp;: lire et compléter une bête à cornes, écrire un but sans solution, puis "
                "<b>choisir</b> l'objet qui remplit les trois branches (5e_C3.3)",
          "4e": "<b>formuler</b>&nbsp;: comparer deux besoins pour justifier l'évolution d'un objet et écrire le nouveau but "
                "(4e_C1.3), puis tirer du besoin les caractéristiques à comparer pour choisir (4e_C3.1)",
          "3e": "<b>élargir</b>&nbsp;: établir une liste d'OST possibles à partir d'un but sans solution, puis <b>arbitrer</b>&nbsp;: "
                "juger une formulation du besoin et voir ce qu'elle ferme (3e_C3.1)"}
CHAINE = ("<p><b>Analyse externe</b>&nbsp;: <b>besoin <i>(bête à cornes)</i></b> → fonction d'usage → interacteurs <i>(diagramme "
          "des interacteurs, « pieuvre »)</i> → contraintes et exigences → cahier des charges.</p>"
          "<p>Cet atelier est le <b>premier maillon</b>. Le but écrit dans la bête à cornes devient la fonction d'usage&nbsp;; le "
          "diagramme des interacteurs part de là pour trouver les contraintes. En 4e et en 3e, la même bête à cornes sert à "
          "justifier une évolution (4e_C1.3), à choisir ce qu'on compare (4e_C3.1) et à établir une liste d'OST possibles "
          "(3e_C3.1), avant de les évaluer selon des critères (3e_C3.3).</p>")
NOTES_PROF = (
    "<ul><li>Plan du 24/10/2026&nbsp;: 5e_C3.3 (reconnaître le besoin), 4e_C1.3 et 4e_C3.1 (formuler), 3e_C3.1 (élargir, puis "
    "arbitrer)&nbsp;; sept exercices.</li>"
    "<li>La carte des représentations le fixe&nbsp;: la bête à cornes, c'est <b>dix minutes pour formuler le besoin — pas une "
    "séance sur le formalisme, et jamais un objectif évalué</b>. D'où des exercices courts (6 à 12 minutes), centrés sur le "
    "besoin et jamais sur le dessin&nbsp;: aucun ne demande de tracer le gabarit. Le positionnement de fin porte sur les codes "
    "du référentiel (choisir un OST, justifier une évolution, identifier des caractéristiques, établir une liste), jamais sur "
    "« savoir faire une bête à cornes ».</li>"
    "<li>Conséquence assumée&nbsp;: chaque page de niveau totalise 22 à 25 minutes d'exercices, en dessous des 30 à 40 minutes "
    "habituelles des ateliers. Le reste de la séance va à l'ouverture, au bilan et au QCM, ou à l'atelier du diagramme des "
    "interacteurs, qui suit.</li>"
    "<li>Le programme ne nomme pas la « bête à cornes »&nbsp;: il parle de <i>besoin</i>, et la bête à cornes produit la "
    "fonction d'usage. Le schéma est donc nommé deux fois&nbsp;: le mot du programme d'abord, le nom courant ensuite.</li>"
    "<li>Conventions tenues dans tout l'atelier&nbsp;: la case « sur quoi&nbsp;? » porte une personne ou une chose concrète, "
    "jamais une idée (« la sécurité », « le confort »)&nbsp;; les mêmes personnes peuvent occuper les deux cases du haut (la "
    "station d'alerte rend service aux habitants et agit sur eux)&nbsp;; le but commence par un verbe à l'infinitif et ne nomme "
    "aucune solution&nbsp;; le commanditaire (la mairie, la commune) n'est pas l'usager.</li>"
    "<li>Deux buts portent une condition, voulue par le plan&nbsp;: « sans voiture » (5e, exercice 3) et « sans gaspiller "
    "l'eau » (4e, exercice 1). Ce sont des parties du besoin lui-même — sans elles, l'objet choisi ne serait pas le même — et "
    "non des contraintes de conception. Une contrainte comme « sans éblouir » ou « résister à la pluie » n'entre pas dans le "
    "but&nbsp;: elle va au diagramme des interacteurs (c'est l'un des distracteurs de l'exercice 1 de 5e).</li>"
    "<li>Source d'inspiration&nbsp;: le cahier « 123 Techno » (Bordas, 2021), fiches « bête à cornes » de 4e et de 3e — pour "
    "des mécaniques seulement&nbsp;: compléter un gabarit partiellement rempli, distinguer celui qui commande de celui à qui "
    "l'objet rend service, dire ce que la bête à cornes ne fait pas (elle ne liste pas les contraintes), reconnaître la "
    "représentation parmi d'autres. Aucun énoncé, aucune image, aucun objet de l'éditeur n'est repris. Écarts assumés&nbsp;: "
    "chez nous, la case « sur quoi&nbsp;? » ne reçoit jamais une notion abstraite&nbsp;; la pyramide des besoins (Maslow), "
    "présente chez l'éditeur, n'est pas au programme 2024 et reste hors de l'atelier.</li>"
    "<li>Exercice 6 (3e)&nbsp;: le « porte-à-porte » écrit seul est refusé avec un message qui demande « avec quel objet&nbsp;? » "
    "— c'est une organisation, pas un OST&nbsp;; « porte-à-porte avec un mégaphone » est accepté, par le mégaphone. Les volets "
    "et l'abri sont refusés comme « vrais mais hors sujet »&nbsp;: des objets qui protègent, sans prévenir.</li>"
    "<li>En 4e et en 3e, l'élève n'a pas forcément fait l'atelier du niveau précédent&nbsp;: l'ouverture renvoie aux exercices "
    "de 5e, puis de 4e, pour rattraper en une dizaine de minutes.</li>"
    "<li>Les objets sont les objets-fils des séquences&nbsp;: le lampadaire qui s'allume la nuit au passage d'un piéton (5e), le "
    "système d'arrosage du jardin partagé et sa gardienne (4e, comme dans l'atelier du diagramme des interacteurs), la station "
    "d'alerte cyclonique de Sainte-Luce (3e), ici prise avant sa conception, au moment où l'on écrit le besoin.</li></ul>")
DEUX_NOMS = ("Le programme de technologie parle d'<b>exprimer le besoin</b>&nbsp;: dire à qui l'objet rend service, sur quoi il "
             "agit, et dans quel but. Le schéma qui le montre s'appelle, dans beaucoup de livres et de classes, la <b>bête à "
             "cornes</b>&nbsp;: ses deux cases du haut et la grande courbe qui passe sous l'objet font penser à la tête d'un "
             "taureau. Si tu rencontres l'un des deux noms, tu sauras que c'est la même idée.")
QCM_SOUS_TITRE = ("Lire et compléter la bête à cornes, choisir l'objet qui répond au besoin (5e) ; justifier une évolution, "
                  "tirer du besoin les caractéristiques (4e) ; établir une liste d'objets ou de systèmes techniques possibles "
                  "à partir d'un besoin bien écrit (3e)")
