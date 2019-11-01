from django.test import Client
from django.test import TestCase
from django.test import override_settings
from seucep.apps.core.models import Address


@override_settings(STATICFILES_STORAGE="django.contrib.staticfiles.storage.StaticFilesStorage")
class TestRoutes(TestCase):
    def setUp(self):
        self.client = Client()

        Address.objects.create(cep="27185000", addresses="Arrozal (Piraí)", state="RJ")

    def test_should_return_yaml_result(self):

        headers = {"HTTP_ACCEPT": "application/yaml"}

        response = self.client.get("/api/v1/ceps/27185000/", None, None, **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response._headers["content-type"][0], "Content-Type")
        self.assertEqual(response._headers["content-type"][1], "application/yaml; charset=utf-8")

    def test_should_return_xml_result(self):

        headers = {"HTTP_ACCEPT": "application/xml"}

        response = self.client.get("/api/v1/ceps/27185000/", None, None, **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response._headers["content-type"][0], "Content-Type")
        self.assertEqual(response._headers["content-type"][1], "application/xml; charset=utf-8")

    def test_should_return_piped_result(self):

        headers = {"HTTP_ACCEPT": "text/piped"}

        response = self.client.get("/api/v1/ceps/27185000/", None, None, **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response._headers["content-type"][0], "Content-Type")
        self.assertEqual(response._headers["content-type"][1], "text/piped; charset=utf-8")
