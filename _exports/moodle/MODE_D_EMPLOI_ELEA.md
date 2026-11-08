# Importer les QCM dans Éléa (Martinique) — mode d'emploi

Éléa est un Moodle : les fichiers `5e.xml`, `4e.xml`, `3e.xml` et `ateliers.xml` de ce dossier
sont des **banques de questions au format XML Moodle**. Une importation par fichier suffit ;
les catégories (un dossier par QCM, rangé par niveau et par code de séquence) se créent toutes seules.

## 1. Préparer un parcours par niveau

1. `martinique.elea.apps.education.fr` → **Mes parcours** → **Créer un parcours**.
2. Un parcours par niveau (ex. « Technologie 5e — 2026-2027 »). Le parcours est un cours Moodle :
   c'est lui qui porte la banque de questions et les tests.

## 2. Importer une banque

1. Dans le parcours, ouvrir la **Banque de questions** (menu du parcours, souvent sous « Plus »).
2. Onglet ou menu **Importer** → format **« Format XML Moodle »**.
3. Déposer `5e.xml` (ou le niveau voulu) → **Importation**. Compter une à deux minutes : les images
   sont dans le fichier.
4. Vérifier : la banque affiche les catégories `Technologie Cycle 4 / 5e / Thème 1 — 5e_C1.1 · …`,
   chacune avec ses 30 questions numérotées `01 · 5e_C1.1 · …`.

Attention : Moodle ne fusionne pas à l'importation. Réimporter un fichier **ajoute** les questions
une seconde fois. Pour mettre à jour un QCM : supprimer sa catégorie dans la banque, puis importer
le fichier `par-qcm/<slug>.xml` régénéré. L'idnumber de chaque question (`<slug>-q<numéro>`) sert à
retrouver une question du site dans la banque, pas à dédoublonner.

## 3. Créer le test d'une séquence — les réglages « premium »

1. Dans la section de la séquence : **Ajouter une activité** → **Test**.
2. **Comportement des questions** → **Interactif avec essais multiples** : à chaque erreur, l'élève lit la
   rétroaction de *sa* réponse et un indice, le choix faux s'efface, il réessaie. Trois essais par question
   (deux indices sont dans la banque) ; la note baisse d'un tiers par essai raté, jamais à zéro tant qu'il
   finit par trouver. C'est ce réglage qui fait travailler, pas seulement mesurer.
3. **Note** → **Tentatives autorisées : illimité** ; **Méthode de notation : note la plus haute** ;
   **Chaque tentative s'appuie sur la précédente : non** (il recommence vraiment).
4. **Mise en page** → une question par page ou cinq par page selon la classe ; **Navigation : libre**.
5. **Options de relecture** : pendant la tentative, cocher *La tentative*, *Si correcte*, *Points*,
   *Feedback spécifique*, *Feedback général*, *Réponse juste* — c'est tout le corrigé exhaustif qui s'affiche
   à chaque essai. Pour une évaluation sommative, décocher *Feedback général* et *Réponse juste* pendant la
   tentative et les laisser **après la fermeture du test** seulement.
6. **Questions** → **Ajouter** → **de la banque de questions** → cocher la catégorie du QCM → tout
   sélectionner → **Ajouter**. Les 30 questions arrivent dans l'ordre du site (pas de tirage aléatoire,
   décision du 23/10/2026) et sans mélange des réponses.

## 4. Ce que l'élève voit

- Pendant le test : l'énoncé, l'image s'il y en a une, quatre réponses.
- Après une erreur (mode interactif) : « ❌ Pas celle-là. … » avec la raison propre à ce distracteur, puis
  l'indice 1 (le piège classique), le bouton **Réessayer** ; à la deuxième erreur, l'indice 2 (à retenir).
- À la correction : **✅ La bonne réponse**, puis le corrigé en cinq temps numérotés — *Pourquoi*,
  *Un exemple*, *Le piège classique*, *Pour aller plus loin* (quand il y a une nuance), **📌 À retenir** —
  le même texte que la page du site, dans l'ordre où on l'apprend.

## 5. Ce qui reste sur le site

La page `qcm_*.html` publiée sur pll-process.github.io reste l'**entraînement** auto-corrigé, libre
d'accès. Éléa porte la **note** et la trace par élève. Les corrigés d'évaluation ne vivent donc plus
que côté serveur : c'est la vraie protection du travail.

## Régénérer après une modification d'un QCM

```bash
node _outils/export_moodle_xml.mjs
node _outils/tests_export_moodle_xml.mjs   # le banc
```

Puis, dans Éléa, supprimer la catégorie du QCM modifié et importer son fichier `par-qcm/<slug>.xml`.
Les tests déjà construits sur l'ancienne catégorie gardent leurs questions : les reconstruire si le fond a changé.
