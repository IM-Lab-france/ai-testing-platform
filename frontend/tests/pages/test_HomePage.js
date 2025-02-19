// frontend/tests/pages/test_HomePage.js
import React from 'react';
import { render } from '@testing-library/react';
import HomePage from '../../src/pages/HomePage';
import { fetchCampaigns } from '../../src/services/api';

jest.mock('../../src/services/api', () => ({
    fetchCampaigns: jest.fn(),
}));

test('HomePage fetches and displays campaigns', async () => {
    fetchCampaigns.mockResolvedValue([
        { id: 1, name: 'Campaign1', description: 'Test', status: 'completed', created_at: '2023-10-01T12:00:00' },
    ]);

    const { findByText } = render(<HomePage />);

    expect(await findByText('Campaign1')).toBeInTheDocument();
});
