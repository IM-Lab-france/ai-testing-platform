// frontend/src/services/CampaignService.js
import axios from 'axios';

const API_URL = 'http://localhost:8000/api'; // Remplacez par l'URL de votre API backend

export const createCampaign = async (campaignData) => {
    try {
        const response = await axios.post(`${API_URL}/campaigns/`, campaignData);
        return response.data;
    } catch (error) {
        throw new Error('Failed to create campaign');
    }
};

export const startCampaign = async (campaignId) => {
    try {
        const response = await axios.post(`${API_URL}/campaigns/${campaignId}/run`);
        return response.data;
    } catch (error) {
        throw new Error('Failed to start campaign');
    }
};

export const getCampaigns = async () => {
    try {
        const response = await axios.get(`${API_URL}/campaigns/`);
        return response.data;
    } catch (error) {
        throw new Error('Failed to fetch campaigns');
    }
};
