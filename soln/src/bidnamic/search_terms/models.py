#model class to load search_terms csv into database

from django.db import models
from adgroups.models import Adgroups
from campaigns.models import Campaigns
from django.utils.translation import gettext as _

# Create your models here.

class Search_Terms(models.Model):
    # class instances based off search_terms csv colums headers

    date= models.DateField(
        auto_now= True,
    )
    ad_group_id= models.ForeignKey(
        Adgroups,
        on_delete= models.CASCADE,
    )
    campaign_id= models.ForeignKey(
        Campaigns,
        on_delete= models.CASCADE,
    )
    clicks= models.IntegerField()
    cost= models.FloatField()
    conversion_value= models.IntegerField()
    conversions= models.IntegerField()
    search_term= models.TextField(
        blank= True,
        null= True,
    )

