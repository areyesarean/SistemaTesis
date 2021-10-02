from django.db import models
# Create your models here.
from django.forms import model_to_dict

from municipio.models import Municipios


class AreaSalud(models.Model):
    nombre = models.CharField('Nombre', unique=True, max_length=60)
    municipio = models.ForeignKey(Municipios, on_delete=models.PROTECT, verbose_name='Municipio')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'AreaSalud'
        verbose_name_plural = 'AreaSaluds'
        # ordering = ['municipio']

    def toJson(self):
        item = model_to_dict(self)
        item['municipio'] = self.municipio.municipio
        return item
