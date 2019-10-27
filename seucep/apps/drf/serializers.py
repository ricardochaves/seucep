from rest_framework import serializers
from seucep.apps.core.models import Addresses


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = ("addresses", "state", "complement", "cep", "neighborhood", "city")
