from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from file_controls.views import ReadCSVFileView


class URLTests(SimpleTestCase):
    def test_read_csv_files(self):
        url = reverse('read-csv-files')
        self.assertEqual(resolve(url).func.view_class, ReadCSVFileView)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.read_csv_files_url = reverse('read-csv-files')

    def test_read_csv_files_GET(self):
        response = self.client.get(self.read_csv_files_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'read-csv-file.html')
