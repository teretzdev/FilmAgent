import axios from 'axios';

const BASE_URL = 'http://localhost:5000/api/prompts'; // Replace with your backend API base URL

// Fetch all prompts
export const fetchPrompts = async () => {
  try {
    const response = await axios.get(BASE_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching prompts:', error);
    throw error;
  }
};

// Create a new prompt
export const createPrompt = async (promptData) => {
  try {
    const response = await axios.post(BASE_URL, promptData);
    return response.data;
  } catch (error) {
    console.error('Error creating prompt:', error);
    throw error;
  }
};

// Update an existing prompt
export const updatePrompt = async (id, promptData) => {
  try {
    const response = await axios.put(`${BASE_URL}/${id}`, promptData);
    return response.data;
  } catch (error) {
    console.error('Error updating prompt:', error);
    throw error;
  }
};

// Delete a prompt
export const deletePrompt = async (id) => {
  try {
    const response = await axios.delete(`${BASE_URL}/${id}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting prompt:', error);
    throw error;
  }
};

 // Fetch a script preview
export const fetchScriptPreview = async () => {
  try {
    const response = await axios.get('http://localhost:5000/api/scripts/preview');
    return response.data;
  } catch (error) {
    console.error('Error fetching script preview:', error);
    throw error;
  }
};

export default {
  fetchPrompts,
  createPrompt,
  updatePrompt,
  deletePrompt,
  fetchScriptPreview,
};