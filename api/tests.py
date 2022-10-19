from urllib import response
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class ApiTest(TestCase):
    def test_view_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 405)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('upload-list'))
        self.assertEqual(response.status_code, 405)
