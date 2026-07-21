import "@testing-library/jest-dom";

// 🧹 Nettoyage automatique du DOM entre les tests
import { cleanup } from "@testing-library/react";
afterEach(cleanup);
