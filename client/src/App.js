import React from "react";
import GeneratorComponent from "./components/GeneratorComponent";

function App() {
  return (
    <div>
      <header style={styles.header}>
        <h1 style={styles.title}>FilmAgent: Script and Image Generator</h1>
      </header>
      <main style={styles.main}>
        <GeneratorComponent />
      </main>
    </div>
  );
}

const styles = {
  header: {
    backgroundColor: "#282c34",
    padding: "20px",
    textAlign: "center",
    color: "white",
  },
  title: {
    fontSize: "1.8rem",
    margin: 0,
  },
  main: {
    padding: "20px",
    display: "flex",
    justifyContent: "center",
  },
};

export default App;
