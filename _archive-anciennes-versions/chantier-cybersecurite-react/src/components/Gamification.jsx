// src/components/Gamification.jsx
import React from "react";

const Gamification = ({ badges = [], level = 1, stars = 0, feedback = [] }) => {
  // ✅ Normalisation : transformer feedback string en tableau
  const feedbackArray = Array.isArray(feedback)
    ? feedback
    : feedback
    ? [{ type: "info", message: feedback }]
    : [];

  return (
    <aside
      className="gamification"
      aria-label="Zone de progression et de récompenses"
      style={{
        background: "#0e1630",
        color: "#a9b6df",
        padding: "1rem",
        marginTop: "1.5rem",
        borderRadius: "12px",
        boxShadow: "0 0 10px rgba(122,162,247,0.3)",
      }}
    >
      {/* 🧭 Barre de niveau */}
      <div className="level-bar" style={{ marginBottom: "1rem" }}>
        <h3 style={{ color: "#7aa2f7" }}>
          Niveau {level} &nbsp;⭐{stars}
        </h3>
        <div
          className="progress"
          role="progressbar"
          aria-valuenow={badges.length}
          aria-valuemin="0"
          aria-valuemax="30"
          style={{
            background: "#2c3e50",
            height: "10px",
            borderRadius: "10px",
            overflow: "hidden",
          }}
        >
          <div
            style={{
              width: `${(badges.length / 30) * 100}%`,
              background: "#7aa2f7",
              height: "100%",
              transition: "width 0.5s ease-in-out",
            }}
          ></div>
        </div>
      </div>

      {/* 🏅 Liste des badges */}
      <div
        className="badges-grid"
        role="list"
        style={{
          display: "flex",
          flexWrap: "wrap",
          gap: "0.5rem",
          justifyContent: "center",
          marginTop: "1rem",
        }}
      >
        {badges.length > 0 ? (
          badges.map((badge, i) => (
            <span
              key={i}
              role="listitem"
              className={`badge ${badge}`}
              title={badge}
              style={{
                background: "#1b2838",
                border: "1px solid #7aa2f7",
                borderRadius: "50%",
                width: "40px",
                height: "40px",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: "1.2rem",
              }}
            >
              🏅
            </span>
          ))
        ) : (
          <p style={{ fontStyle: "italic", color: "#6f84b5" }}>
            Aucun badge débloqué pour le moment.
          </p>
        )}
      </div>

      {/* 💬 Feedback des tests ou du professeur */}
      {feedbackArray.length > 0 && (
        <div
          className="feedback"
          style={{
            marginTop: "1rem",
            background: "#111a2e",
            padding: "0.8rem",
            borderRadius: "8px",
            borderLeft: "4px solid #7aa2f7",
          }}
        >
          {feedbackArray.map((f, i) => (
            <div key={i} className={f.type}>
              {f.message}
            </div>
          ))}
        </div>
      )}
    </aside>
  );
};

export default Gamification;
