from rest_framework import serializers

from adgroups.models import Adgroups

class AdgroupsSerializer(serializers.ModelSerializer):
    # serializer class displays adgroups data

    class Meta:
        model= Adgroups
        fields= "__all__"
        depth= 1