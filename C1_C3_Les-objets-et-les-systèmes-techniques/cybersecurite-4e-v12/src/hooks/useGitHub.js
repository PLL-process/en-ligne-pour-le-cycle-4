// src/hooks/useGitHub.js
import { useState, useEffect } from "react";
import { runAxeTest } from "../utils/accessibility"; // ✅ import correct

// (optionnel) simulation locale des tests unitaires
const runAllTests = async () => {
  console.log("🧪 Simulation des tests unitaires...");
  return {
    jest: "✅ Tous les tests passés",
    coverage: "95%",
  };
};

export const useGitHub = () => {
  const [feedback, setFeedback] = useState("🟢 En attente d’envoi...");

  const syncToGitHub = async (data) => {
    try {
      const student = localStorage.getItem("studentName") || "Anonyme";
      const section = data.section || "générale";
      const score = data.score || 0;

      // 🧩 Simulation des tests + accessibilité
      const tests = await runAllTests();
      const accessibility = await runAxeTest(document.body);

      const payload = {
        student,
        section,
        score,
        tests,
        accessibility,
        time: new Date().toISOString(),
      };

      console.log("📤 Données à envoyer à GitHub :", payload);

      // 🚧 Simulation (à remplacer par ton API GitHub Classroom plus tard)
      const response = await fetch("/api/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (!response.ok) throw new Error("Erreur lors de l’envoi");

      const result = await response.json();
      setFeedback(result.feedback || "✅ Données envoyées avec succès !");

      if (result.humanComment) {
        alert(`💬 Commentaire du professeur : ${result.humanComment}`);
      }
    } catch (err) {
      console.error("❌ Erreur de synchronisation :", err);
      setFeedback("❌ Erreur : impossible de synchroniser les données.");
    }
  };

  // 🕓 Optionnel : message de démarrage
  useEffect(() => {
    console.log("🔗 Hook useGitHub initialisé");
  }, []);

  return { syncToGitHub, feedback };
};
