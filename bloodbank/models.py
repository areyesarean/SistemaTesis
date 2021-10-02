from django.db import models
# Create your models here.
from django.forms import model_to_dict

from municipio.models import Municipios


class BloodBank(models.Model):
    nombre = models.CharField('Nombre', unique=False, max_length=60)
    municipio = models.ForeignKey(Municipios, on_delete=models.PROTECT, verbose_name='Municipio')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'BloodBank'
        verbose_name_plural = 'BloodBanks'
        # ordering = ['municipio']

    def toJson(self):
        item = model_to_dict(self)
        item['municipio'] = self.municipio.municipio
        return item
