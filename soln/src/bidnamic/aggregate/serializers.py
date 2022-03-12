from rest_framework import serializers
from .models import Roas


class RoasSerializer(serializers.ModelSerializer):
    # serializer to display top 10 search terms
    # goes through various depth

    class Meta:
        model= Roas
        fields= '__all__'
        depth= 3

