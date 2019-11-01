from django.db import models


class Address(models.Model):
    cep = models.CharField(primary_key=True, max_length=8, verbose_name="CEP")

    log_nu = models.CharField(max_length=8, verbose_name="Chave do logradouro")
    loc_nu = models.CharField(max_length=8, verbose_name="Chave da localidade")
    bairro_nu_ini = models.CharField(max_length=8, verbose_name="Chave do bairro inicial do logradouro")
    bairro_nu_fim = models.CharField(
        blank=True, null=True, max_length=8, verbose_name="Chave do bairro final do logradouro"
    )
    address_type = models.CharField(max_length=36, verbose_name="Tipo de logradouro")
    log_sta_tlo = models.BooleanField(default=False, verbose_name="Se tem tipo de logradouro ou não")
    abbreviation = models.CharField(max_length=36, verbose_name="Abreviatura do nome do logradouro")
    state = models.CharField(max_length=2, verbose_name="State")
    addresses = models.CharField(max_length=100, verbose_name="Addresses")
    complement = models.CharField(blank=True, null=True, max_length=100, verbose_name="Complement")
    neighborhood = models.CharField(max_length=72, verbose_name="Bairro")
    city = models.CharField(max_length=72, verbose_name="Cidade")

    def __str__(self):
        return self.cep
