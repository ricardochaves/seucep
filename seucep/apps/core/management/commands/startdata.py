import json

import requests
from django.core.management import BaseCommand
from seucep.apps.core.models import Addresses


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Goole Maps API.
        link = "https://storage.googleapis.com/seu-cep-prd/data.json"

        # Request data from link as 'str'
        data = requests.get(link).text

        # convert 'str' to Json
        data = json.loads(data)

        # Now you can access Json
        for a in data["a"]:
            Addresses.objects.create(
                cep=a["cep"],
                addresses=a["log_no_abrev"],
                state=a["state"],
                complement=a["complement"],
                bairro_nu_ini=a["bairro_nu_ini"],
                loc_nu=["loc_nu"],
            )

        for b in data["b"]:
            Addresses.objects.filter(bairro_nu_ini=b["bairro_nu_ini"]).update(neighborhood=b["name"])

        for c in data["b"]:
            Addresses.objects.filter(loc_nu=c["loc_nu"]).update(city=c["name"])
