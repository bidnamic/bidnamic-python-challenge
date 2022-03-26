from file_controls.models import Campaign, AdGroup, SearchTerm
from rest_framework import serializers


class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaign
        fields = ['structure_value']


class AdGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdGroup
        fields = ['campaign', 'alias']


class SearchTermSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SearchTerm
        fields = ['ad_group', 'campaign', 'cost', 'conversion_value', 'search_term']

