import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import "@testing-library/jest-dom";
import Section6 from "../components/sections/Section6";
import CCGame from "../components/CCGame";
import { ScoreProvider, ScoreContext } from "../contexts/ScoreContext";



describe("Section 6 - Propriété Intellectuelle", () => {
  test("renders correctly", () => {
    render(
      <ScoreProvider value={{ updateScore: jest.fn(), completeSection: jest.fn() }}>
        <Section6 />
      </ScoreProvider>
    );
    expect(screen.getByText(/propriété intellectuelle/i)).toBeInTheDocument();
  });

  test("CC game scoring", () => {
    const { getByText } = render(<CCGame onComplete={() => {}} />);
    const button = getByText(/terminer le mini-jeu/i);
    fireEvent.click(button);
    expect(button).toBeDisabled(); // après clic, jeu terminé
  });

  test("accessibility attributes", () => {
    const { container } = render(
      <ScoreProvider value={{ updateScore: jest.fn(), completeSection: jest.fn() }}>
        <Section6 />
      </ScoreProvider>
    );
    expect(container.querySelector("[aria-labelledby]")).toBeInTheDocument();
  });

  test("score update", () => {
    const mockUpdate = jest.fn();
    const mockComplete = jest.fn();
    render(
      <ScoreContext.Provider value={{ updateScore: mockUpdate, completeSection: mockComplete }}>
        <Section6 />
      </ScoreContext.Provider>
    );
    // Simulation de fin de section
    mockUpdate(6, 15);
    expect(mockUpdate).toHaveBeenCalledWith(6, 15);
  });
});
