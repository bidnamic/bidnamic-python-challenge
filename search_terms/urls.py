from . import views
from django.urls import path

urlpatterns = [
    path('Search', views.LoadSearchTableView.as_view()),
]
