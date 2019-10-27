from django.test import Client
from django.test import TestCase
from django.test import override_settings


@override_settings(STATICFILES_STORAGE="django.contrib.staticfiles.storage.StaticFilesStorage")
class TestRoutes(TestCase):
    def setUp(self):
        self.client = Client()

    def test_should_return_200_on_home(self):

        response = self.client.get("/api/v1/ceps/")

        self.assertEqual(response.status_code, 200)

    # def test_should_return_302_on_ricardo(self):
    #
    #     response = self.client.get("/ricardo/")
    #
    #     self.assertEqual(response.status_code, 302)
