from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from file_controls.models import Campaign, AdGroup, SearchTerm
from rest_api.search_calculation import campaign_calculation, ad_group_calculation


class CampaignView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Have permission users and token return first 10 search term depend on Campaign structure value sort by ROAS
        Args:
            request: None
            format: json, api, None

        Returns:
            success: First 10 search term depend on Campaign structure value sort by ROAS
            error: Cannot find related calculations
        """
        campaign = Campaign.objects.all().distinct('structure_value')
        campaign_related_search_term = SearchTerm.objects.all()
        calculation_result = campaign_calculation(campaign, campaign_related_search_term)
        if calculation_result:
            return Response(calculation_result, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Cannot find related calculations'}, status=status.HTTP_400_BAD_REQUEST)


class AdGroupView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Have permission users and token return first 10 search term depend on AdGroup alias sort by ROAS
        Args:
            request: None
            format: json, api, None
        Returns:
            success: First 10 search term depend on AdGroup alias sort by ROAS
            error: Cannot find related calculations
        """
        ad_group = AdGroup.objects.all().distinct('alias')
        ad_group_related_search_term = SearchTerm.objects.all()
        calculation_result = ad_group_calculation(ad_group, ad_group_related_search_term)
        if calculation_result:
            return Response(calculation_result, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Cannot find related calculations'}, status=status.HTTP_400_BAD_REQUEST)


class CustomAuthToken(ObtainAuthToken):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Return token for registered user
        Args:
            request:
            *args:
            **kwargs:

        Returns:
            token: Created or requested user token
            user: Registered user's username
        """
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': user.username})
