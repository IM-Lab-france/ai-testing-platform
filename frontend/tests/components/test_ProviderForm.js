// frontend/tests/components/test_ProviderForm.js
import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import ProviderForm from '../../src/components/ProviderForm';

test('ProviderForm submits data correctly', () => {
    const handleSubmit = jest.fn();
    const { getByLabelText, getByText } = render(<ProviderForm onSubmit={handleSubmit} />);

    fireEvent.change(getByLabelText(/Name/i), { target: { value: 'TestProvider' } });
    fireEvent.change(getByLabelText(/API URL/i), { target: { value: 'http://test.com' } });
    fireEvent.change(getByLabelText(/Module Path/i), { target: { value: 'test.module' } });
    fireEvent.change(getByLabelText(/Class Name/i), { target: { value: 'TestClass' } });
    fireEvent.change(getByLabelText(/API Key/i), { target: { value: 'test_key' } });

    fireEvent.click(getByText(/Submit/i));

    expect(handleSubmit).toHaveBeenCalledWith({
        name: 'TestProvider',
        apiUrl: 'http://test.com',
        modulePath: 'test.module',
        className: 'TestClass',
        apiKey: 'test_key',
    });
});
