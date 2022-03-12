"""
Model class to load adgroups csv into database, based off csv colums heads
"""
from django.db import models
from campaigns.models import Campaigns
from django.utils.translation import gettext as _


# Create your models here.

class Adgroups(models.Model):
    
    #create tables data based of adgroups csv columns headings
    #add foriegnkey id  attribute to campigns_id
    
    ad_group_id= models.TextField()
    campaign_id= models.ForeignKey(
        Campaigns,
        on_delete= models.CASCADE,
        )
    alias= models.TextField()
    status= models.CharField(
        max_length= 7,
        blank= False,
        null= False,
        )
