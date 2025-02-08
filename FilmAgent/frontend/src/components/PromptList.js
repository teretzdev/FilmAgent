import React, { useState, useEffect } from 'react';
import { fetchPrompts } from '../services/api'; // Assuming an API service is available for fetching prompts.

const PromptList = () => {
  const [prompts, setPrompts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const handleEdit = (id) => {
    window.location.href = `/form?id=${id}`;
  };

  const handleDelete = async (id) => {
    if (window.confirm("Are you sure you want to delete this prompt?")) {
      try {
        await deletePrompt(id); // Assuming deletePrompt is defined in the API service
        setPrompts(prompts.filter((prompt) => prompt.id !== id));
      } catch (err) {
        setError("Failed to delete the prompt. Please try again.");
      }
    }
  };

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
      <table style={styles.table}>
        <thead>
          <tr>
            <th style={styles.tableHeader}>Prompt</th>
            <th style={styles.tableHeader}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {prompts.map((prompt, index) => (
            <tr key={index} style={styles.tableRow}>
              <td style={styles.tableCell}>{prompt.text}</td>
              <td style={styles.tableCell}>
                <button
                  style={styles.editButton}
                  onClick={() => handleEdit(prompt.id)}
                >
                  Edit
                </button>
                <button
                  style={styles.deleteButton}
                  onClick={() => handleDelete(prompt.id)}
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
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
  table: {
    width: '100%',
    borderCollapse: 'collapse',
    marginTop: '20px',
  },
  tableHeader: {
    backgroundColor: '#f4f4f4',
    padding: '10px',
    border: '1px solid #ddd',
    textAlign: 'left',
  },
  tableRow: {
    borderBottom: '1px solid #ddd',
  },
  tableCell: {
    padding: '10px',
    border: '1px solid #ddd',
  },
  editButton: {
    backgroundColor: '#4CAF50',
    color: 'white',
    border: 'none',
    padding: '5px 10px',
    marginRight: '5px',
    cursor: 'pointer',
  },
  deleteButton: {
    backgroundColor: '#f44336',
    color: 'white',
    border: 'none',
    padding: '5px 10px',
    cursor: 'pointer',
  },
};

export default PromptList;