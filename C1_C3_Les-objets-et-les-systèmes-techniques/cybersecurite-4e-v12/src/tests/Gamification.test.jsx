import React from "react";
import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import { act } from "react";
import Gamification from "../components/Gamification";

test("affiche le niveau et les étoiles", () => {
  act(() => {
    render(<Gamification level={3} stars={2} badges={["a", "b"]} />);
  });

  expect(screen.getByText(/Niveau 3/i)).toBeInTheDocument();
  expect(screen.getByText(/⭐2/i)).toBeInTheDocument();
});
