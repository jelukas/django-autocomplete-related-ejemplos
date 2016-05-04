from __future__ import unicode_literals
from cities_light.models import City, Country
from django.db import models


class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.ForeignKey(Country, verbose_name='pais')
    ciudad = models.ForeignKey(City, verbose_name='ciudad')

    def __str__(self):
        return self.nombre
