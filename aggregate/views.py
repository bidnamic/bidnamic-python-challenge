from tokenize import ContStr
from rest_framework import status
from rest_framework.response import Response

from search_terms.models import Search_Terms
from.serializers import RoasSerializer
from .models import (
    Roas
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework.views import APIView
from adgroups.utils import Load


class PopulateRoasTableView(APIView):
    """
    API to update or populate Roas Table,
    based off new entries to Search_term table
    """

    def post(self, *args, **kwargs):
        # function gets all data fro search_term table
        # and fill roas table using information gotten

        data= Search_Terms.objects.all()
        for i in data:
            roas= i.conversion_values // i.cost
            data, created= Roas.objects.update_or_create(
                search_id= i,
                search_term= i.search_term,
                total_conversion= i.conversion_value,
                total_cost= i.cost,
                roas= roas,
            )
            Load.load_data(created)
            data.save()
        return Response({'Success':'Successfully Uploaded'}, status= status.HTTP_201_CREATED)

class RetrieveTop10DataView(generics.ListAPIView):
    """
    API to retrieve top 10 search term
    Based off Roas
    Roas = conversion_value // cost
    """

    serializer_class= RoasSerializer
    permission_classes= [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        # function get all data from Roas table,
        # then order data by descending order
        # return only the top 10 results
        qs= Roas.objects.all().order_by('-roas')[:10]
        return qs



