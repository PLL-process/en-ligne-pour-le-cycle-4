import React, { createContext, useContext, useState } from "react";

// Création du contexte global
export const ScoreContext = createContext();

// Fournisseur du contexte
export const ScoreProvider = ({ children }) => {
  const [scores, setScores] = useState({});
  const [completedSections, setCompletedSections] = useState([]);

  // Mise à jour du score d’une section
  const updateScore = (section, score) => {
    setScores(prev => ({ ...prev, [section]: score }));
  };

  // Marquer une section comme terminée
  const completeSection = (section) => {
    if (!completedSections.includes(section)) {
      setCompletedSections(prev => [...prev, section]);
    }
  };

  return (
    <ScoreContext.Provider value={{ scores, updateScore, completeSection }}>
      {children}
    </ScoreContext.Provider>
  );
};

// Hook personnalisé pour accéder facilement au contexte
export const useScore = () => useContext(ScoreContext);
