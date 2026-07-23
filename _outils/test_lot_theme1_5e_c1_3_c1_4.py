# -*- coding: utf-8 -*-
# Ce script contrôle statiquement le lot pédagogique 5e_C1.3–C1.4.
# Il ne remplace pas les tests fonctionnels dans un navigateur réel.
# Il doit être exécuté depuis la racine du dépôt avec Python 3.

# Importe Path pour manipuler les chemins de manière portable.
from pathlib import Path
# Importe re pour rechercher des motifs dans le HTML et le JavaScript.
import re
# Importe sys pour retourner un code d’erreur exploitable par GitHub Actions.
import sys

# Définit la racine du dépôt à partir de l’emplacement du script.
RACINE = Path(__file__).resolve().parent.parent
# Définit le dossier du lot contrôlé.
DOSSIER = RACINE / "theme-1-objets-systemes-usages-interactions" / "C1-decrire-les-liens-entre-usages-et-evolutions" / "5e" / "5e_C1.3"
# Définit le chemin de la séquence.
SEQUENCE = DOSSIER / "sequence_C1.3-C1.4_SI_gestion_donnees.html"
# Définit le chemin du QCM.
QCM = DOSSIER / "qcm_systemes_information_donnees.html"
# Définit le chemin de la synthèse élève.
SYNTHESE_ELEVE = DOSSIER / "synthese_eleve_5e_C1.3-C1.4.html"
# Définit le chemin de la synthèse professeur.
SYNTHESE_PROF = DOSSIER / "synthese_professeur_5e_C1.3-C1.4.html"
# Définit le chemin de la matrice de couverture.
COUVERTURE = DOSSIER / "couverture_sequence_qcm.json"
# Définit le chemin du rapport de lot.
RAPPORT = DOSSIER / "RAPPORT_LOT_PILOTE.md"
# Regroupe les fichiers obligatoires du lot.
FICHIERS_OBLIGATOIRES = [SEQUENCE, QCM, SYNTHESE_ELEVE, SYNTHESE_PROF, COUVERTURE, RAPPORT]

# Prépare la liste des erreurs bloquantes.
erreurs = []
# Prépare la liste des avertissements non bloquants.
avertissements = []

# Vérifie la présence de chaque fichier obligatoire.
for fichier in FICHIERS_OBLIGATOIRES:
    # Ajoute une erreur lorsque le fichier attendu est absent.
    if not fichier.is_file():
        erreurs.append(f"Fichier obligatoire absent : {fichier.relative_to(RACINE)}")

# Interrompt les contrôles de contenu lorsque les deux pages principales manquent.
if not SEQUENCE.is_file() or not QCM.is_file():
    # Affiche toutes les erreurs déjà détectées.
    for erreur in erreurs:
        print(f"ERREUR : {erreur}")
    # Retourne un code d’échec.
    sys.exit(1)

# Lit la séquence en UTF-8.
sequence_html = SEQUENCE.read_text(encoding="utf-8")
# Lit le QCM en UTF-8.
qcm_html = QCM.read_text(encoding="utf-8")

# Définit les éléments imposés par l’en-tête standard du QCM.
marqueurs_qcm = {
    # Vérifie la présence d’un titre principal.
    "titre H1": r"<h1\b",
    # Vérifie le retour obligatoire vers la séquence.
    "retour vers la séquence": r"(?:Retour|Revenir).{0,80}(?:séquence|Séquence)",
    # Vérifie les champs d’identité obligatoires.
    "champ Nom": r"(?:id|name)=[\"']nom[\"']",
    # Vérifie le champ Prénom obligatoire.
    "champ Prénom": r"(?:id|name)=[\"']prenom[\"']",
    # Vérifie le champ Classe obligatoire.
    "champ Classe": r"(?:id|name)=[\"']classe[\"']",
    # Vérifie le champ Date obligatoire.
    "champ Date": r"(?:id|name)=[\"']date[\"']",
    # Vérifie la carte de progression.
    "carte Ma progression": r"Ma progression",
    # Vérifie le compteur Répondu.
    "compteur Répondu": r"Répondu",
    # Vérifie le compteur Correctes.
    "compteur Correctes": r"Correctes",
    # Vérifie le compteur Incorrectes.
    "compteur Incorrectes": r"Incorrectes",
    # Vérifie le compteur Restantes.
    "compteur Restantes": r"Restantes",
    # Vérifie le compteur À revoir.
    "compteur À revoir": r"À revoir|A revoir",
    # Vérifie le compteur Score.
    "compteur Score": r"Score\s*%|Score",
    # Vérifie le compteur Note sur 20.
    "compteur Note /20": r"Note\s*/\s*20|/\s*20",
    # Vérifie la présence du minuteur.
    "minuteur": r"minuteur|Minuteur",
    # Vérifie la carte des modes de travail.
    "carte Mode de travail": r"Mode de travail",
    # Vérifie le mode parcours complet.
    "mode Parcours complet": r"Parcours complet",
    # Vérifie le mode dix questions.
    "mode 10 questions": r"10 questions",
    # Vérifie le mode révision ciblée.
    "mode Révision ciblée": r"Révision ciblée|Revision ciblee",
    # Vérifie le mode erreurs.
    "mode erreurs": r"Uniquement mes erreurs|mes erreurs",
}

# Contrôle chaque marqueur obligatoire dans le QCM.
for nom, motif in marqueurs_qcm.items():
    # Ajoute une erreur si le marqueur n’est pas trouvé sans tenir compte de la casse.
    if not re.search(motif, qcm_html, flags=re.IGNORECASE | re.DOTALL):
        erreurs.append(f"En-tête standard incomplet : {nom}")

# Vérifie la présence des deux codes couverts dans le QCM.
for code in ("5e_C1.3", "5e_C1.4"):
    # Ajoute une erreur lorsque le code n’est pas mentionné.
    if code not in qcm_html:
        erreurs.append(f"Code absent du QCM : {code}")

# Vérifie que l’appellation interdite n’apparaît pas dans l’interface élève.
if re.search(r"\bXXL\b", qcm_html, flags=re.IGNORECASE):
    # Ajoute une erreur lorsque l’appellation interdite est détectée.
    erreurs.append("Appellation XXL détectée dans le QCM")

# Compte les balises image présentes dans le QCM.
images_qcm = re.findall(r"<img\b[^>]*>", qcm_html, flags=re.IGNORECASE)
# Vérifie que chaque image possède un texte alternatif non vide.
for index, balise in enumerate(images_qcm, start=1):
    # Recherche l’attribut alt dans la balise image.
    correspondance_alt = re.search(r"\balt=[\"']([^\"']*)[\"']", balise, flags=re.IGNORECASE)
    # Ajoute une erreur si le texte alternatif est absent ou vide.
    if correspondance_alt is None or not correspondance_alt.group(1).strip():
        erreurs.append(f"Image QCM n°{index} sans texte alternatif pertinent")

# Signale un avertissement lorsque moins de six images-objet sont présentes.
if len(images_qcm) < 6:
    # L’avertissement n’est pas bloquant lorsque le contenu ne justifie pas artificiellement six images.
    avertissements.append(f"Le QCM contient {len(images_qcm)} image(s) ; justifier ce nombre au regard de la règle images v2")

# Recherche les liens réciproques entre la séquence et le QCM.
if "qcm_systemes_information_donnees.html" not in sequence_html:
    # Ajoute une erreur si la séquence ne pointe pas vers le QCM.
    erreurs.append("Lien séquence vers QCM absent")
# Vérifie que le QCM contient un lien vers la séquence.
if "sequence_C1.3-C1.4_SI_gestion_donnees.html" not in qcm_html:
    # Ajoute une erreur si le QCM ne pointe pas vers la séquence.
    erreurs.append("Lien QCM vers séquence absent")

# Compte les activités identifiables dans la séquence.
activites = re.findall(r"Activité\s*[0-9]+|data-activite=", sequence_html, flags=re.IGNORECASE)
# Ajoute une erreur lorsque moins de trois activités sont détectées.
if len(activites) < 3:
    erreurs.append("La séquence ne présente pas au moins trois activités identifiables")

# Vérifie la présence des éléments pédagogiques attendus dans la séquence.
for element in ("Problématique", "À retenir", "Correction", "Aide"):
    # Ajoute une erreur lorsque l’élément n’apparaît pas dans le contenu.
    if element.lower() not in sequence_html.lower():
        erreurs.append(f"Élément pédagogique absent de la séquence : {element}")

# Affiche les avertissements détectés.
for avertissement in avertissements:
    # Préfixe chaque avertissement pour faciliter la lecture dans les journaux.
    print(f"AVERTISSEMENT : {avertissement}")

# Affiche les erreurs détectées.
for erreur in erreurs:
    # Préfixe chaque erreur pour faciliter la lecture dans les journaux.
    print(f"ERREUR : {erreur}")

# Retourne un échec si au moins une erreur bloquante existe.
if erreurs:
    # Affiche un résumé du résultat.
    print(f"ÉCHEC : {len(erreurs)} erreur(s) bloquante(s) détectée(s).")
    # Retourne le code d’échec standard.
    sys.exit(1)

# Affiche le succès lorsque tous les contrôles statiques passent.
print("SUCCÈS : contrôles statiques du lot 5e_C1.3–C1.4 validés.")
# Retourne explicitement le code de succès.
sys.exit(0)
