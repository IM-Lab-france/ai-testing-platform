// frontend/src/pages/CampaignManagementPage.js
import React, { useState } from 'react';
import { createCampaign, startCampaign } from '../services/api'; // Services fictifs pour gérer les campagnes

const CampaignManagementPage = () => {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');

    const handleCreateCampaign = async () => {
        await createCampaign({ name, description });
    };

    const handleStartCampaign = async (campaignId) => {
        await startCampaign(campaignId);
    };

    return (
        <div>
            <h1>Campaign Management</h1>
            <div>
                <input
                    type="text"
                    placeholder="Campaign Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                />
                <button onClick={handleCreateCampaign}>Create Campaign</button>
            </div>
            {/* Ajoutez ici un tableau ou une liste pour afficher les campagnes existantes */}
            <button onClick={() => handleStartCampaign(1)}>Start Campaign</button>
        </div>
    );
};

export default CampaignManagementPage;
