import React, { useState, useEffect } from 'react';
import { fetchScript } from '../services/api'; // Assuming an API service is available for fetching scripts.

const PromptPreview = () => {
  const [script, setScript] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getScript = async () => {
      try {
        const data = await fetchScript(); // Fetch the script data from the backend API.
        setScript(data);
      } catch (err) {
        setError('Failed to fetch the script. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    getScript();
  }, []);

  if (loading) {
    return <div style={styles.loading}>Loading script preview...</div>;
  }

  if (error) {
    return <div style={styles.error}>{error}</div>;
  }

  if (!script || script.length === 0) {
    return <div style={styles.empty}>No script available for preview.</div>;
  }

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Script Preview</h2>
      {script.map((scene, index) => (
        <div key={index} style={styles.scene}>
          <h3 style={styles.sceneTitle}>Scene {index + 1}</h3>
          <p style={styles.sceneInfo}>
            <strong>Who:</strong> {scene.scene_information.who.join(', ')}<br />
            <strong>Where:</strong> {scene.scene_information.where}<br />
            <strong>What:</strong> {scene.scene_information.what}
          </p>
          <div style={styles.dialogues}>
            {scene.dialogues.map((dialogue, idx) => (
              <div key={idx} style={styles.dialogue}>
                <p>
                  <strong>{dialogue.speaker}:</strong> {dialogue.content}
                </p>
                <ul style={styles.actions}>
                  {dialogue.actions.map((action, actionIdx) => (
                    <li key={actionIdx}>
                      <strong>Character:</strong> {action.character}, <strong>State:</strong> {action.state}, <strong>Action:</strong> {action.action}
                    </li>
                  ))}
                </ul>
                <p>
                  <strong>Selected Shot:</strong> {dialogue.selected_shot}
                </p>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};

const styles = {
  container: {
    padding: '20px',
    maxWidth: '800px',
    margin: '0 auto',
    backgroundColor: '#f9f9f9',
    borderRadius: '8px',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
  },
  title: {
    textAlign: 'center',
    fontSize: '24px',
    marginBottom: '20px',
  },
  scene: {
    marginBottom: '20px',
    padding: '10px',
    border: '1px solid #ccc',
    borderRadius: '8px',
    backgroundColor: '#fff',
  },
  sceneTitle: {
    fontSize: '20px',
    marginBottom: '10px',
  },
  sceneInfo: {
    fontSize: '16px',
    marginBottom: '10px',
  },
  dialogues: {
    marginTop: '10px',
  },
  dialogue: {
    marginBottom: '15px',
    padding: '10px',
    border: '1px solid #ddd',
    borderRadius: '8px',
    backgroundColor: '#f7f7f7',
  },
  actions: {
    marginTop: '5px',
    paddingLeft: '20px',
    fontSize: '14px',
  },
  loading: {
    textAlign: 'center',
    fontSize: '18px',
    color: '#555',
  },
  error: {
    textAlign: 'center',
    fontSize: '18px',
    color: 'red',
  },
  empty: {
    textAlign: 'center',
    fontSize: '18px',
    color: '#777',
  },
};

export default PromptPreview;
