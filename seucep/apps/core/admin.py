from django.contrib import admin
from seucep.apps.core.models import Address


@admin.register(Address)
class AddressesAdmin(admin.ModelAdmin):
    search_fields = ["cep", "bairro_nu_ini", "loc_nu"]
