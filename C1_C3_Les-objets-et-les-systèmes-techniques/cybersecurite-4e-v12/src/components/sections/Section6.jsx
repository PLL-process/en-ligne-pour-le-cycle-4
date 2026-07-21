// src/components/sections/Section6.jsx
import React, { useState } from 'react';
import { useScore } from '../../contexts/ScoreContext';
import CCGame from '../../components/CCGame';
import QCM from '../../components/QCM';
import { runAxeTest } from '../../utils/accessibility';

const Section6 = () => {
  const { updateScore, completeSection } = useScore();
  const [qcmScore, setQcmScore] = useState(0);
  
  const handleQCMComplete = (score) => {
    setQcmScore(score);
    updateScore(6, score);
  };

  const handleGameComplete = (score) => {
    updateScore(6, qcmScore + score);
    if (qcmScore + score === 15) completeSection(6);
  };

  return (
    <section id="sec6" aria-labelledby="sec6-title">
      <h2 id="sec6-title">
        ⚖️ Propriété intellectuelle <span className="badge">0/15</span>
      </h2>

      {/* 6.a V/F - 2pts */}
      <QCM 
        questions={[
          { q: "Photo sans accord autorisée 'pour rire'?", options: ["Non", "Oui"], correct: 0 }
        ]}
        onComplete={handleQCMComplete}
      />

      {/* 6.b Drag Drop - 2pts */}
      {/* TODO: Ajouter composant DragDrop plus tard */}

      {/* 6.c CC GAME - 4pts */}
      <CCGame onComplete={handleGameComplete} />

      {/* 6.d Quiz - 7pts */}
      <QCM 
        questions={[
          { q: "Droit d'auteur protège :", options: ["Œuvres", "Objets"], correct: 0 },
          // ... autres questions
        ]}
        onComplete={handleQCMComplete}
      />

      <button onClick={() => runAxeTest(document.getElementById('sec6'))}>
        🧑‍🔬 Tester Accessibilité
      </button>
    </section>
  );
};

export default Section6;
