// frontend/src/pages/HomePage.js
import React, { useEffect, useState } from 'react';
import CampaignTable from '../components/CampaignTable';
import { fetchCampaigns } from '../services/api'; // Service fictif pour récupérer les campagnes

const HomePage = () => {
    const [campaigns, setCampaigns] = useState([]);

    useEffect(() => {
        const getCampaigns = async () => {
            const data = await fetchCampaigns();
            setCampaigns(data);
        };

        getCampaigns();
    }, []);

    return (
        <div>
            <h1>Dashboard</h1>
            <CampaignTable campaigns={campaigns} />
        </div>
    );
};

export default HomePage;
