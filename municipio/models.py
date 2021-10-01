from django.db import models

# Create your models here.
from django.forms import model_to_dict

from provincia.models import Provincias


class Municipios(models.Model):
    municipio = models.CharField('Municipio', unique=True, max_length=20)
    provincia = models.ForeignKey(Provincias, on_delete=models.PROTECT, verbose_name='Provincia')

    def __str__(self):
        return self.municipio

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        # ordering = ['municipio']

    def toJson(self):
        item = model_to_dict(self)
        item['provincia'] = self.provincia.provincia
        return item