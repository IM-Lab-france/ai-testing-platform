// frontend/src/pages/ProviderManagementPage.js
import React from 'react';
import ProviderForm from '../components/ProviderForm';
import { addProvider } from '../services/api'; // Service fictif pour ajouter un fournisseur

const ProviderManagementPage = () => {
    const handleSubmit = async (providerData) => {
        await addProvider(providerData);
    };

    return (
        <div>
            <h1>Provider Management</h1>
            <ProviderForm onSubmit={handleSubmit} />
        </div>
    );
};

export default ProviderManagementPage;
