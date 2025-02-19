// frontend/src/components/ResultsChart.js
import React from 'react';
import { Bar } from 'react-chartjs-2';

const ResultsChart = ({ data }) => {
    const chartData = {
        labels: data.map(result => result.campaign_name),
        datasets: [
            {
                label: 'Tokens Used',
                data: data.map(result => result.tokens_count),
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
            },
        ],
    };

    return <Bar data={chartData} />;
};

export default ResultsChart;
