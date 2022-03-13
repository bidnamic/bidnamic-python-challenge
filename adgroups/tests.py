from django.test import TestCase
from .models import Adgroups
from campaigns.models import Campaigns
# Create your tests here.

class AdgroupTest(TestCase):
    """
    Test case to test insertion of data into adgroups table
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
        Adgroups.objects.create(
            campaign_id= self.camp2,
            ad_group_id= 456,
            alias= 'textfield',
            status= 'Enabled',
        )
        Adgroups.objects.create(
            campaign_id= self.camp2,
            ad_group_id= 76289,
            alias= 'Moments',
            status= 'Disable',
        )
        self.count= Adgroups.objects.all().count()


    def test_data_insert(self):
        data = Adgroups.objects.create(
            campaign_id= self.camp,
            ad_group_id= 7593089,
            alias= 'starts',
            status= 'Disable',
            )
        self.assertEqual(data.id, 3)