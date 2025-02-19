// frontend/tests/pages/test_CampaignManagementPage.js
import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import CampaignManagementPage from '../../src/pages/CampaignManagementPage';
import { createCampaign } from '../../src/services/api';

jest.mock('../../src/services/api', () => ({
    createCampaign: jest.fn(),
}));

test('CampaignManagementPage creates a campaign', async () => {
    const { getByPlaceholderText, getByText } = render(<CampaignManagementPage />);

    fireEvent.change(getByPlaceholderText(/Campaign Name/i), { target: { value: 'New Campaign' } });
    fireEvent.change(getByPlaceholderText(/Description/i), { target: { value: 'New Description' } });

    fireEvent.click(getByText(/Create Campaign/i));

    expect(createCampaign).toHaveBeenCalledWith({ name: 'New Campaign', description: 'New Description' });
});
