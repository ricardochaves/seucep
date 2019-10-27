from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from seucep.apps.core.models import Addresses
from seucep.apps.drf.serializers import AddressesSerializer


class AddressesBaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializer
