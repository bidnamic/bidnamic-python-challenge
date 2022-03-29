from django.urls import path
from rest_api.views import CampaignView, AdGroupView, CustomAuthToken

urlpatterns = [
    path('campaign/', CampaignView.as_view(), name='campaign'),
    path('ad_group/', AdGroupView.as_view(), name='ad_group'),
    path('api-token-auth/', CustomAuthToken.as_view()),
]
