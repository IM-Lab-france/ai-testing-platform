// frontend/src/components/CampaignTable.js
import React from 'react';

const CampaignTable = ({ campaigns }) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Status</th>
                    <th>Created At</th>
                </tr>
            </thead>
            <tbody>
                {campaigns.map((campaign) => (
                    <tr key={campaign.id}>
                        <td>{campaign.name}</td>
                        <td>{campaign.description}</td>
                        <td>{campaign.status}</td>
                        <td>{new Date(campaign.created_at).toLocaleString()}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default CampaignTable;
