from django.db import models


class Addresses(models.Model):

    cep = models.CharField(primary_key=True, max_length=8, verbose_name="CEP")
    addresses = models.CharField(max_length=36, verbose_name="Logradouro")
    state = models.CharField(max_length=2, verbose_name="State")
    complement = models.CharField(blank=True, null=True, max_length=100, verbose_name="Complement")
    neighborhood = models.CharField(blank=True, null=True, max_length=72, verbose_name="Bairro")
    city = models.CharField(blank=True, null=True, max_length=72, verbose_name="Cidade")
    loc_nu = models.CharField(blank=True, null=True, max_length=72, verbose_name="loc_nu")
    bairro_nu_ini = models.CharField(blank=True, null=True, max_length=72, verbose_name="bairro_nu_ini")

    def __str__(self):
        return self.cep
