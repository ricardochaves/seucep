from rest_framework import viewsets
from seucep.apps.core.models import Address
from seucep.apps.drf.serializers import AddressSerializer


class AddressBaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
