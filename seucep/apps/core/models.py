from django.db import models


class Addresses(models.Model):

    addresses = models.CharField(blank=True, null=True, max_length=36, verbose_name="Logradouro")  #
    state = models.CharField(blank=True, null=True, max_length=2, verbose_name="State")  #
    complement = models.CharField(blank=True, null=True, max_length=100, verbose_name="Complement")  #
    cep = models.CharField(blank=True, null=True, unique=True, max_length=8, verbose_name="CEP")  #
    neighborhood = models.CharField(blank=True, null=True, max_length=72, verbose_name="Bairro")  #
    city = models.CharField(blank=True, null=True, max_length=72, verbose_name="Cidade")  #

    def __str__(self):
        return self.cep
