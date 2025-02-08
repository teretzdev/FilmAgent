import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { createPrompt, updatePrompt } from '../services/api';

const PromptForm = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const editingPrompt = location.state?.prompt || null;

  const [promptText, setPromptText] = useState(editingPrompt ? editingPrompt.text : '');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (editingPrompt) {
      setPromptText(editingPrompt.text);
    }
  }, [editingPrompt]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!promptText.trim()) {
      setError('Prompt text cannot be empty.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      if (editingPrompt) {
        await updatePrompt(editingPrompt.id, { text: promptText });
      } else {
        await createPrompt({ text: promptText });
      }
      navigate('/');
    } catch (err) {
      setError('Failed to save the prompt. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>{editingPrompt ? 'Edit Prompt' : 'Create New Prompt'}</h2>
      <form onSubmit={handleSubmit} style={styles.form}>
        <textarea
          style={styles.textarea}
          value={promptText}
          onChange={(e) => setPromptText(e.target.value)}
          placeholder="Enter your prompt here..."
        />
        {error && <div style={styles.error}>{error}</div>}
        <div style={styles.buttonContainer}>
          <button type="submit" style={styles.button} disabled={loading}>
            {loading ? 'Saving...' : editingPrompt ? 'Update Prompt' : 'Create Prompt'}
          </button>
          <button
            type="button"
            style={styles.cancelButton}
            onClick={() => navigate('/')}
            disabled={loading}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

const styles = {
  container: {
    maxWidth: '600px',
    margin: '0 auto',
    padding: '20px',
    border: '1px solid #ccc',
    borderRadius: '8px',
    backgroundColor: '#f9f9f9',
  },
  title: {
    textAlign: 'center',
    marginBottom: '20px',
    fontSize: '24px',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
  },
  textarea: {
    width: '100%',
    height: '100px',
    padding: '10px',
    fontSize: '16px',
    borderRadius: '4px',
    border: '1px solid #ccc',
    marginBottom: '10px',
  },
  error: {
    color: 'red',
    marginBottom: '10px',
    textAlign: 'center',
  },
  buttonContainer: {
    display: 'flex',
    justifyContent: 'space-between',
  },
  button: {
    padding: '10px 20px',
    fontSize: '16px',
    color: '#fff',
    backgroundColor: '#007bff',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  },
  cancelButton: {
    padding: '10px 20px',
    fontSize: '16px',
    color: '#fff',
    backgroundColor: '#6c757d',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  },
};

export default PromptForm;
