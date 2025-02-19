// frontend/tests/components/test_ResultsChart.js
import React from 'react';
import { render } from '@testing-library/react';
import ResultsChart from '../../src/components/ResultsChart';

test('ResultsChart renders correctly', () => {
    const data = [
        { campaign_name: 'Campaign1', tokens_count: 100 },
        { campaign_name: 'Campaign2', tokens_count: 150 },
    ];

    const { container } = render(<ResultsChart data={data} />);

    expect(container.querySelector('canvas')).toBeInTheDocument();
});
