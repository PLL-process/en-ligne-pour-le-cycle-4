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

## 3. Créer le test d'une séquence

1. Dans la section de la séquence : **Ajouter une activité** → **Test**.
2. Réglages conseillés pour une évaluation : une tentative, navigation libre, **relecture après
   fermeture seulement** (sinon les corrigés circulent entre classes), note sur 20.
3. **Questions** → **Ajouter** → **de la banque de questions** → cocher la catégorie du QCM →
   tout sélectionner → **Ajouter**. Les 30 questions arrivent dans l'ordre du site (pas de tirage
   aléatoire, décision du 23/10/2026) et sans mélange des réponses.

## 4. Ce que l'élève voit

- Pendant le test : l'énoncé, l'image s'il y en a une, quatre réponses.
- À la relecture : la bonne réponse, la **rétroaction de sa réponse** (pourquoi ce distracteur est
  faux), et le **corrigé exhaustif** (pourquoi, exemple, erreur fréquente, nuance, à retenir) —
  le même texte que la page du site.

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
