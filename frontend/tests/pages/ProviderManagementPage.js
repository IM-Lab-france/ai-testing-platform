// frontend/tests/pages/test_ProviderManagementPage.js
import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import ProviderManagementPage from '../../src/pages/ProviderManagementPage';
import { addProvider } from '../../src/services/api';

jest.mock('../../src/services/api', () => ({
    addProvider: jest.fn(),
}));

test('ProviderManagementPage adds a provider', () => {
    const { getByLabelText, getByText } = render(<ProviderManagementPage />);

    fireEvent.change(getByLabelText(/Name/i), { target: { value: 'NewProvider' } });
    fireEvent.change(getByLabelText(/API URL/i), { target: { value: 'http://newprovider.com' } });
    fireEvent.change(getByLabelText(/Module Path/i), { target: { value: 'new.module' } });
    fireEvent.change(getByLabelText(/Class Name/i), { target: { value: 'NewClass' } });
    fireEvent.change(getByLabelText(/API Key/i), { target: { value: 'new_key' } });

    fireEvent.click(getByText(/Submit/i));

    expect(addProvider).toHaveBeenCalledWith({
        name: 'NewProvider',
        apiUrl: 'http://newprovider.com',
        modulePath: 'new.module',
        className: 'NewClass',
        apiKey: 'new_key',
    });
});
