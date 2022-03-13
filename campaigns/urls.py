
from . import views
from django.urls import path

urlpatterns = [
    path('Campaign/load', views.LoadDataCampaign.as_view()),
]
