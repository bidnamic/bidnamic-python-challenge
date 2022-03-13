from django.test import TestCase
from .models import Campaigns

# Create your tests here.

class CampaignTest(TestCase):
    """
    Test case to test insertion of data into campaigns table
    """
    def setUp(self):
        self.camp2= Campaigns.objects.create(
            campaign_id= '34566',
            structure_value= 'moniced',
            status= 'Enabled',
        )
        self.camp= Campaigns.objects.create(
            campaign_id= '5680',
            structure_value= 'moniced',
            status= 'Enabled',
        )

        self.count= Campaigns.objects.all().count()


    def test_data_insert(self):
        data = Campaigns.objects.create(
            campaign_id= 4697085,
            structure_value= 'Adaptors',
            status= 'Enabled',
            )
        self.assertEqual(data.id, 3)