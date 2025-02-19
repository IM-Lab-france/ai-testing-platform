// frontend/tests/services/test_CampaignService.js
import axios from 'axios';
import { createCampaign, startCampaign, getCampaigns } from '../../src/services/CampaignService';

jest.mock('axios');

describe('CampaignService', () => {
    test('createCampaign successfully creates a campaign', async () => {
        const campaignData = { name: 'TestCampaign', description: 'Test description' };
        axios.post.mockResolvedValue({ data: campaignData });

        const result = await createCampaign(campaignData);

        expect(axios.post).toHaveBeenCalledWith('http://localhost:8000/api/campaigns/', campaignData);
        expect(result).toEqual(campaignData);
    });

    test('startCampaign successfully starts a campaign', async () => {
        const campaignId = 1;
        axios.post.mockResolvedValue({ data: { message: 'Campaign started' } });

        const result = await startCampaign(campaignId);

        expect(axios.post).toHaveBeenCalledWith(`http://localhost:8000/api/campaigns/${campaignId}/run`);
        expect(result).toEqual({ message: 'Campaign started' });
    });

    test('getCampaigns successfully fetches campaigns', async () => {
        const campaigns = [{ name: 'Campaign1' }, { name: 'Campaign2' }];
        axios.get.mockResolvedValue({ data: campaigns });

        const result = await getCampaigns();

        expect(axios.get).toHaveBeenCalledWith('http://localhost:8000/api/campaigns/');
        expect(result).toEqual(campaigns);
    });
});
