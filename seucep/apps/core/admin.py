from django.contrib import admin
from seucep.apps.core.models import Addresses


@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    pass
