import React, { useState } from "react";

const CCGame = ({ onComplete }) => {
  const [completed, setCompleted] = useState(false);

  const handleClick = () => {
    setCompleted(true);
    onComplete(4); // par exemple, 4 points
  };

  return (
    <button onClick={handleClick} disabled={completed}>
      Terminer le mini-jeu
    </button>
  );
};

export default CCGame;
