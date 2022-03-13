from django.test import TestCase
from adgroups.models import Adgroups
from campaigns.models import Campaigns
from .models import Search_Terms

# Create your tests here.

class AdgroupTest(TestCase):
    """
    Test case to test insertion of data into search_terms table
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
        self.ad= Adgroups.objects.create(
            campaign_id= self.camp2,
            ad_group_id= 456,
            alias= 'textfield',
            status= 'Enabled',
        )
        self.ad2= Adgroups.objects.create(
            campaign_id= self.camp2,
            ad_group_id= 76289,
            alias= 'Moments',
            status= 'Disable',
        )
        self.count= Search_Terms.objects.all().count()


    def test_data_insert(self):
        data = Search_Terms.objects.create(
            date= '2020-02-16',
            campaign_id= self.camp,
            ad_group_id= self.ad,
            clicks= 3,
            cost= 0.7,
            conversion_value= 0,
            conversions= 0,
            search_term= 'venom',
            )
        self.assertEqual(data.id, 1)