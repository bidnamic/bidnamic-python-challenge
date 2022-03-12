from rest_framework import serializers
from .models import Search_Terms

class SearchTermSerializer(serializers.ModelSerializer):
    # serializer class displays Search_term in json format

    class Meta:
        model= Search_Terms
        fields= "__all__"
        depth= 2