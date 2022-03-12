
from turtle import done
from rest_framework import status
from rest_framework.response import Response
from csvs.models import Csv
from csvs.serializers import CSVUploadSerializers
from adgroups.models import Adgroups
from campaigns.models import Campaigns
from rest_framework import generics
import pandas as pd
from adgroups.utils import Load

# Create your views here.

class LoadSearchTableView(generics.CreateAPIView):
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
            data= file.shape[0]
                
            for i,j in file.iterrows():
                camp_id= Campaigns.objects.get(campaign_id= j['campaign_id'])
                adgroups_id= Adgroups.objects.get(ad_groupd_id= j['ad_group_id'])
                data, created= Adgroups.objects.update_or_create(
                    date= j['date'],
                    ad_group_id= adgroups_id,
                    campaign_id= camp_id,
                    clicks= j['clicks'],
                    cost= j['cost'],
                    conversion_value= j['conversion_value'],
                    conversions= j['conversions'],
                    search_term= j['search_term'],
                )
                print(created)
                print(data)
                print('done')
            return Response({"success":"Successfully uploaded"}, status=status.HTTP_201_CREATED)
        return Response({'Error':'Error encountered'}, status= status.HTTP_400_BAD_REQUEST)


