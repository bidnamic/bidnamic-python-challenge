# creating a form field that accepts the csv file 

from rest_framework import serializers
from .models import Csv
from adgroups.models import Adgroups


class CSVUploadSerializers(serializers.ModelSerializer):
    # get the file and edits and save the file
    
    class Meta:
        model= Csv
        fields= ['file', ]

