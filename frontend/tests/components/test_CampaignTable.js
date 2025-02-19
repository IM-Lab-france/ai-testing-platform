// frontend/tests/components/test_CampaignTable.js
import React from 'react';
import { render } from '@testing-library/react';
import CampaignTable from '../../src/components/CampaignTable';

test('CampaignTable renders correctly', () => {
    const campaigns = [
        { id: 1, name: 'Campaign1', description: 'First campaign', status: 'completed', created_at: '2023-10-01T12:00:00' },
    ];

    const { getByText } = render(<CampaignTable campaigns={campaigns} />);

    expect(getByText('Campaign1')).toBeInTheDocument();
    expect(getByText('First campaign')).toBeInTheDocument();
    expect(getByText('completed')).toBeInTheDocument();
});
