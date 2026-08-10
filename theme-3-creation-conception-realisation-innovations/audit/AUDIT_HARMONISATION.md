# Audit d'harmonisation — les règles d'or à l'échelle du dépôt

*Document **engendré** par `audit_spiralaire.py`, jamais rédigé à la main —
aucun chiffre n'y est recopié, il se régénère d'une commande et ne peut donc
pas mentir sur l'état réel du dépôt.*

```bash
# depuis la racine du dépôt
python3 theme-3-creation-conception-realisation-innovations/audit/audit_spiralaire.py \
    > theme-3-creation-conception-realisation-innovations/audit/AUDIT_HARMONISATION.md
```

Constats de FAITS vérifiés sur les fichiers, pas de jugements pédagogiques.
**180 pages examinées.**

## Ce qu'il faut lire en premier

Ces chiffres ne sont pas une note. Ils disent **où appliquer** ce qu'on a écrit,
et dans quel ordre.

**1. La clé de voûte (n°87) — 0 séances.** Le chantier qui change quelque chose
pour l'élève : ces séances de 4e et de 3e s'appuient sur un prérequis sans jamais
rappeler ce qu'il a **déjà produit**. Court par séance — trois paragraphes — mais
il faut savoir ce qui précède, donc remonter la progression. C'est là que se joue
la cohérence du cycle.

**2. Les impasses (n°88) — 0 pages.** Une page où l'on entre sans pouvoir sortir.
Mécanique, corrigeable par lot puisque ces pages partagent leur gabarit.

**3. Les images absentes — 3 pages.** Les TP de CAO, en cours de production.

**4. Le bonus sans corrigé (n°86) — 0 page(s).** À vérifier à la main avant de
conclure : un chiffre bas peut vouloir dire « tout va bien » ou « le script ne
voit pas ».

**5. Le réseau (n°40) — 6 pages.** Ressources réellement chargées depuis
l'extérieur. Une page qui en dépend ne fonctionne pas dans une salle sans connexion.

**6. Les liens sortants — 3 pages.** Ils ne cassent rien hors ligne, mais ils
disent où l'on envoie des élèves : cette liste se relit avec d'autres yeux que
techniques.

## Une mise en garde sur ce que ce rapport ne dit pas

Un script détecte l'**absence** d'un bloc, jamais la **platitude** de son contenu.
Une séance peut porter un rappel spiralaire parfaitement conforme et parfaitement
inutile — « tu as vu les capteurs en 4e » coche la case et n'apprend rien. Le vrai
critère reste celui qu'on s'est donné : le rappel nomme-t-il une **production** de
l'élève, dit-il ce qui **change**, tient-il debout pour celui qui n'était pas là ?

Ces trois questions-là ne se mesurent pas. Elles se lisent.

---

| Règle | Pages concernées |
|---|---|
| n°88 | **0** |
| n°87 | **0** |
| n°86 | **0** |
| images | **3** |
| n°40 | **6** |
| liens | **3** |

## n°88 — une page se juge aussi sur ce qu'on peut en faire quand on y est arrivé

Aucun manquement.

## n°87 (CLÉ DE VOÛTE) — toute séance qui s'appuie sur un prérequis s'ouvre par un rappel

Aucun manquement.

## n°86 — un bonus sans corrigé n'est pas un bonus, c'est un devoir non rendu

Aucun manquement.

## Images annoncées et absentes — les « fenêtres blanches »

3 page(s).

- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.4/activite-bonus-cyber-immersive-2fa.html` — 2 image(s) annoncée(s) et absente(s)
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/qcm_automatisation_premium.html` — 1 image(s) annoncée(s) et absente(s)
- `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1_book-train/sequence_4e_C4.1-C4.2-C4.4_book-train.html` — 1 image(s) annoncée(s) et absente(s)

## n°40 — une page doit fonctionner hors ligne (ressources CHARGÉES)

6 page(s).

- `theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.2/sequence-jardin-connecte-arrosage-automatique.html` — charge depuis le réseau : fr.vittascience.com
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/sequence_3e_C7_capteur-confort-ny.html` — charge depuis le réseau : fr.vittascience.com
- `theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.1/sequence_5e_C7_mini-projet-objet.html` — charge depuis le réseau : fr.vittascience.com
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/sequence_3e_C9.1_variables_types_systemes.html` — charge depuis le réseau : fr.vittascience.com
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/4e/4e_C9.1/sequence_4e_C9_jardin-programme.html` — charge depuis le réseau : fr.vittascience.com
- `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/5e/5e_C9.1/sequence_5e_C9.1-C9.3_boite_etiquetee.html` — charge depuis le réseau : fr.vittascience.com

## Liens sortants — pour information : ils ne cassent pas la page hors ligne, mais ils méritent une relecture (à quoi envoie-t-on des collégiens ?)

3 page(s).

- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/3e/3e_C1.5/sequence-numerique-societe-economie-environnement-sante.html` — renvoie vers : online-python-compiler.com, online-python.com, programiz.com
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.4/activite-bonus-cyber-immersive-2fa.html` — renvoie vers : chat.openai.com, www.online-python.com
- `theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.4/sequence-cybersecurite-protection-donnees.html` — renvoie vers : chat.openai.com

---

## Périmètre de cet audit

**Vérifié mécaniquement** : présence et validité des liens de navigation, présence
d'un rappel spiralaire sur les pages de 4e et de 3e, présence d'un corrigé dans les
blocs bonus, existence réelle des images annoncées, appels réseau.

**NON couvert** : la qualité du rappel — nomme-t-il une PRODUCTION ou seulement une
notion, dit-il ce qui change, est-il auto-suffisant ? La justesse des corrigés. La
pertinence des situations déclenchantes. Un script détecte l'absence d'un bloc, jamais
la platitude de son contenu. Ces jugements-là restent humains.
