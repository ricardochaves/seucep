from rest_framework import serializers
from seucep.apps.core.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("addresses", "state", "complement", "cep", "neighborhood", "city", "abbreviation", "address_type")
