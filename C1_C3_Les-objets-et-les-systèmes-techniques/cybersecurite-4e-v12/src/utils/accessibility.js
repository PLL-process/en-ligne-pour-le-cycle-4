import axe from "axe-core";
import axeConfig from "../axe.config.js";

/**
 * Lance une analyse d’accessibilité axe-core sur un élément DOM donné.
 * @param {HTMLElement} element Élément racine à analyser (souvent document.body)
 * @returns {Promise<Object>} Résultats de l’analyse
 */
export async function runAxeTest(element = document.body) {
  if (!element) {
    console.warn("⚠️ Aucun élément spécifié pour runAxeTest");
    return null;
  }

  try {
    console.log("🔍 Lancement du test d’accessibilité axe-core...");
    const results = await axe.run(element, axeConfig);
    console.log("📊 Résultats axe-core :", results);

    if (results.violations.length > 0) {
      results.violations.forEach(v => {
        console.warn(`❌ ${v.id}: ${v.description}`);
        console.table(v.nodes.map(n => n.target));
      });
    } else {
      console.log("✅ Aucun problème d’accessibilité détecté !");
    }

    return results;
  } catch (error) {
    console.error("Erreur lors du test d’accessibilité :", error);
    return null;
  }
}
