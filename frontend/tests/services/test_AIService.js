// frontend/tests/services/test_AIService.js
import axios from 'axios';
import { addProvider, getProviders } from '../../src/services/AIService';

jest.mock('axios');

describe('AIService', () => {
    test('addProvider successfully adds a provider', async () => {
        const providerData = { name: 'TestProvider', apiUrl: 'http://test.com' };
        axios.post.mockResolvedValue({ data: providerData });

        const result = await addProvider(providerData);

        expect(axios.post).toHaveBeenCalledWith('http://localhost:8000/api/providers/', providerData);
        expect(result).toEqual(providerData);
    });

    test('getProviders successfully fetches providers', async () => {
        const providers = [{ name: 'Provider1' }, { name: 'Provider2' }];
        axios.get.mockResolvedValue({ data: providers });

        const result = await getProviders();

        expect(axios.get).toHaveBeenCalledWith('http://localhost:8000/api/providers/');
        expect(result).toEqual(providers);
    });
});
