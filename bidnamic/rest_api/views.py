from rest_api.serializers import CampaignSerializer, AdGroupSerializer, SearchTermSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class CampaignView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, structure_value, format=None):
        content = {}
        return Response(content)


class AdGroupView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, alias, format=None):
        content = {}
        return Response(content)
