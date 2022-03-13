from django.test import TestCase
from adgroups.models import Adgroups
from campaigns.models import Campaigns
from django.contrib.auth import get_user_model
from .models import Roas, Search_Terms
from rest_framework.test import APIClient

User= get_user_model()

# Create your tests here.

class AdgroupTest(TestCase):
    """
    Test case to get data from search_terms table and populate Roas table
    """
    def setUp(self):
        self.user1= User.objects.create_superuser(
            username= 'Zues',
            email= 'myemail@gmail.com',
            password= "password",
        )
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
        self.terms = Search_Terms.objects.create(
            date= '2020-02-16',
            campaign_id= self.camp,
            ad_group_id= self.ad,
            clicks= 3,
            cost= 0.7,
            conversion_value= 0,
            conversions= 0,
            search_term= 'venom',
            )
        self.count= Adgroups.objects.all().count()

    def get_client(self):
        client= APIClient()
        return client
    
    def get_client2(self):
        # Function to login super user
        client= APIClient()
        client.login(
            username= self.user1.username,
            password= 'password',
            )
        return client

    def test_data_insert(self):
        # Test function for data retriva and population if Roas table
        
        self.roas= self.terms.conversion_value // self.terms.cost
        create= Roas.objects.create(
            search_id= self.terms,
            search_term= self.terms.search_term,
            total_cost= self.terms.cost,
            total_conversion_value= self.terms.conversion_value,
            roas= self.roas,
        )
        self.assertEqual(create.id, 1)


    def test_unauthorised_request(self):
        # Test function to check if unauthorised user can access api

        user= self.get_client()
        response= user.get("/Roas")
        self.assertEqual(response.status_code, 403)

    def test_authorized_request(self):
        # Test function to if authorised user can access api

        user= self.get_client2()
        response= user.get("/Roas")
        self.assertEqual(response.status_code, 200)

