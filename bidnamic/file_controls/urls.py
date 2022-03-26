from django.urls import path
from file_controls.views import ReadCSVFileView

urlpatterns = [
    path('read-csv-files', ReadCSVFileView.as_view(), name='read-csv-files'),
]
