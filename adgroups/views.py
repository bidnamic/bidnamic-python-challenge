
from rest_framework import status
from rest_framework.response import Response
from campaigns.models import Campaigns
from csvs.models import Csv
from .serializers import AdgroupsSerializer
from csvs.serializers import(
    CSVUploadSerializers
)

from .models import (
    Adgroups
)

from rest_framework import generics
import pandas as pd
from .utils import Load

# Create your views here.

class LoadDataAdgroups(generics.CreateAPIView):
    """
    API gets the csv file,
    read through it,
    remove all commas (,)
    load data into the database
    """

    serializer_class= CSVUploadSerializers
    
    def get_queryset(self):
        return Adgroups.objects.all()
    
    def create(self, *args, **kwargs):
        serializer= CSVUploadSerializers(data= self.request.data)
        if serializer.is_valid(raise_exception= True):
            data= serializer.validated_data
            file= data.get('file')
            file= pd.read_csv(file)
                
            for i,j in file.iterrows():
                camp_id= Campaigns.objects.get(campaign_id= j['campaign_id'])
                data, created= Adgroups.objects.update_or_create(
                    ad_group_id= j['ad_group_id'],
                    campaign_id= camp_id,
                    alias= j['alias'],
                    status= j['status'],
                )
            return Response({"success":"Successfully uploaded"}, status=status.HTTP_201_CREATED)
        return Response({'Error':'Error encountered'}, status= status.HTTP_400_BAD_REQUEST)
