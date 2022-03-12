from rest_framework import serializers
from .models import Campaigns


class CampaignSerializer(serializers.ModelSerializer):
    # Serializer class displays all Campaigns data

    class Meta:
        model= Campaigns
        fields= "__all__"

        