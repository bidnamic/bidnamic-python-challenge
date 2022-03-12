
from . import views
from django.urls import path

urlpatterns = [
    path('Roas/insert', views.PopulateRoasTableView.as_view()),
    path('Roas', views.RetrieveTop10DataView.as_view()),
]
