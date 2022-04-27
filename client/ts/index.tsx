import React from "react";
import { createRoot } from "react-dom/client";
import Books from "./Books";
import PiSeries from "./PiSeries";

function App() {
  return (
    <div>
      <Books />
      <PiSeries />
    </div>
  );
}

const root = createRoot(document.body);
root.render(<App />);
