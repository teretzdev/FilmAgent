import React, { useState } from "react";
import axios from "axios";

const GeneratorComponent = () => {
  const [prompt, setPrompt] = useState("");
  const [scriptFile, setScriptFile] = useState(null);
  const [message, setMessage] = useState("");

  // Handle prompt input change
  const handlePromptChange = (e) => {
    setPrompt(e.target.value);
  };

  // Handle script file upload
  const handleFileChange = (e) => {
    setScriptFile(e.target.files[0]);
  };

  // Trigger script generation
  const generateScript = async () => {
    if (!prompt) {
      setMessage("Please enter a prompt to generate a script.");
      return;
    }

    try {
      setMessage("Generating script...");
      const response = await axios.post("/api/generate-script", { prompt });
      setMessage(`Script generated successfully: ${response.data.message}`);
    } catch (error) {
      setMessage(`Error generating script: ${error.response?.data?.message || error.message}`);
    }
  };

  // Trigger image generation
  const generateImages = async () => {
    if (!scriptFile) {
      setMessage("Please upload a script file to generate images.");
      return;
    }

    const formData = new FormData();
    formData.append("script", scriptFile);

    try {
      setMessage("Generating images...");
      const response = await axios.post("/api/generate-images", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setMessage(`Images generated successfully: ${response.data.message}`);
    } catch (error) {
      setMessage(`Error generating images: ${error.response?.data?.message || error.message}`);
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.header}>Generator Component</h1>

      <div style={styles.inputGroup}>
        <label htmlFor="prompt" style={styles.label}>
          Enter Prompt:
        </label>
        <input
          type="text"
          id="prompt"
          value={prompt}
          onChange={handlePromptChange}
          style={styles.input}
          placeholder="Enter your prompt here..."
        />
      </div>

      <div style={styles.inputGroup}>
        <label htmlFor="scriptFile" style={styles.label}>
          Upload Script File:
        </label>
        <input
          type="file"
          id="scriptFile"
          onChange={handleFileChange}
          style={styles.input}
        />
      </div>

      <div style={styles.buttonGroup}>
        <button onClick={generateScript} style={styles.button}>
          Generate Script
        </button>
        <button onClick={generateImages} style={styles.button}>
          Generate Images
        </button>
      </div>

      {message && <p style={styles.message}>{message}</p>}
    </div>
  );
};

const styles = {
  container: {
    maxWidth: "600px",
    margin: "0 auto",
    padding: "20px",
    border: "1px solid #ccc",
    borderRadius: "8px",
    backgroundColor: "#f9f9f9",
    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
  },
  header: {
    textAlign: "center",
    marginBottom: "20px",
    color: "#333",
  },
  inputGroup: {
    marginBottom: "15px",
  },
  label: {
    display: "block",
    marginBottom: "5px",
    fontWeight: "bold",
  },
  input: {
    width: "100%",
    padding: "10px",
    border: "1px solid #ccc",
    borderRadius: "4px",
  },
  buttonGroup: {
    display: "flex",
    justifyContent: "space-between",
    marginTop: "20px",
  },
  button: {
    padding: "10px 20px",
    backgroundColor: "#007bff",
    color: "#fff",
    border: "none",
    borderRadius: "4px",
    cursor: "pointer",
  },
  buttonHover: {
    backgroundColor: "#0056b3",
  },
  message: {
    marginTop: "20px",
    textAlign: "center",
    color: "#007bff",
  },
};

export default GeneratorComponent;
