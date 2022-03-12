#upload csv into model class csv

from django.db import models

# Create your models here.

class Csv(models.Model):
    #get the csv file 

    file= models.FileField(
        upload_to= './csvfiles',
        blank= False,
        null= False,
    )
    date= models.DateTimeField(
        auto_now_add= True,
    )
    loaded= models.BooleanField(default= False)

