// frontend/src/components/ProviderForm.js
import React, { useState } from 'react';

const ProviderForm = ({ onSubmit }) => {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [apiUrl, setApiUrl] = useState('');
    const [modulePath, setModulePath] = useState('');
    const [className, setClassName] = useState('');
    const [apiKey, setApiKey] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({ name, description, apiUrl, modulePath, className, apiKey });
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Name:</label>
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
            </div>
            <div>
                <label>Description:</label>
                <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} />
            </div>
            <div>
                <label>API URL:</label>
                <input type="url" value={apiUrl} onChange={(e) => setApiUrl(e.target.value)} required />
            </div>
            <div>
                <label>Module Path:</label>
                <input type="text" value={modulePath} onChange={(e) => setModulePath(e.target.value)} required />
            </div>
            <div>
                <label>Class Name:</label>
                <input type="text" value={className} onChange={(e) => setClassName(e.target.value)} required />
            </div>
            <div>
                <label>API Key:</label>
                <input type="password" value={apiKey} onChange={(e) => setApiKey(e.target.value)} required />
            </div>
            <button type="submit">Submit</button>
        </form>
    );
};

export default ProviderForm;
