// frontend/src/services/AIService.js
import axios from 'axios';

const API_URL = 'http://localhost:8000/api'; // Remplacez par l'URL de votre API backend

export const addProvider = async (providerData) => {
    try {
        const response = await axios.post(`${API_URL}/providers/`, providerData);
        return response.data;
    } catch (error) {
        throw new Error('Failed to add provider');
    }
};

export const getProviders = async () => {
    try {
        const response = await axios.get(`${API_URL}/providers/`);
        return response.data;
    } catch (error) {
        throw new Error('Failed to fetch providers');
    }
};
