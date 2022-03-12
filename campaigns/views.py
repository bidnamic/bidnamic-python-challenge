from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from campaigns.models import Campaigns
from campaigns.serializers import CampaignSerializer
from csvs.models import Csv

from csvs.serializers import(
    CSVUploadSerializers
)

from .models import (
    Campaigns
)

from rest_framework import generics
import csv
from adgroups.utils import Load
import pandas as pd
from adgroups.utils import Load

# Create your views here.

class LoadDataCampaign(generics.CreateAPIView):
    """
    API gets the csv file,
    read through it,
    remove all commas (,)
    load data into the database
    """

    serializer_class= CSVUploadSerializers
    
    def get_queryset(self):
        return Campaigns.objects.all()
    
    def create(self, *args, **kwargs):
        serializer= CSVUploadSerializers(data= self.request.data)
        if serializer.is_valid(raise_exception= True):
            data= serializer.validated_data
            file= data.get('file')
            file= pd.read_csv(file)
            data= file.shape[0]

            for i,j in file.iterrows():
                data, created= Campaigns.objects.update_or_create(
                    campaign_id= j['campaign_id'],
                    structure_value= j['structure_value'],
                    status= j['status'],
                )
            return Response({"success":"Successfully uploaded"}, status=status.HTTP_201_CREATED)
        return Response({'Error':'Error encountered'}, status= status.HTTP_400_BAD_REQUEST)


class GetfIRST10(generics.ListAPIView):
    serializer_class= CampaignSerializer

    def get_queryset(self):
        return Campaigns.objects.all().order_by('-id')[:10]
