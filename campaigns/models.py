#model class to load campaigns csv to database

from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Campaigns(models.Model):
    # create objects instance based of campiagns csv row

    campaign_id= models.TextField()

    structure_value= models.TextField()

    status= models.CharField(
        blank= False,
        max_length= 7,
        null= False,
    )