from django import views
from . import views
from django.urls import path

urlpatterns = [
    path('Adgroups/load', views.LoadDataAdgroups.as_view()),
]
