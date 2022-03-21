from django.urls import path
from filecontrols.views import ReadCSVFileView

app_name = 'filecontrols'

urlpatterns = [
    path('read-csv-files', ReadCSVFileView.as_view(), name='read-csv-files'),
]
