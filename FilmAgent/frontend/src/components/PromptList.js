import React, { useState, useEffect } from 'react';
import { fetchPrompts } from '../services/api'; // Assuming an API service is available for fetching prompts.

const PromptList = () => {
  const [prompts, setPrompts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getPrompts = async () => {
      try {
        const data = await fetchPrompts(); // Fetch prompts from the backend API.
        setPrompts(data);
      } catch (err) {
        setError('Failed to fetch prompts. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    getPrompts();
  }, []);

  if (loading) {
    return <div style={styles.loading}>Loading prompts...</div>;
  }

  if (error) {
    return <div style={styles.error}>{error}</div>;
  }

  if (prompts.length === 0) {
    return <div style={styles.empty}>No prompts available.</div>;
  }

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Prompt List</h2>
      <ul style={styles.list}>
        {prompts.map((prompt, index) => (
          <li key={index} style={styles.listItem}>
            {prompt}
          </li>
        ))}
      </ul>
    </div>
  );
};

const styles = {
  container: {
    padding: '20px',
    maxWidth: '600px',
    margin: '0 auto',
    textAlign: 'center',
  },
  title: {
    fontSize: '24px',
    marginBottom: '20px',
  },
  list: {
    listStyleType: 'none',
    padding: 0,
  },
  listItem: {
    padding: '10px',
    borderBottom: '1px solid #ccc',
    textAlign: 'left',
  },
  loading: {
    fontSize: '18px',
    color: '#555',
  },
  error: {
    fontSize: '18px',
    color: 'red',
  },
  empty: {
    fontSize: '18px',
    color: '#777',
  },
};

export default PromptList;
