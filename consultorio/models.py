from django.db import models

# Create your models here.
from django.forms import model_to_dict

from areasalud.models import AreaSalud


class Consultorio(models.Model):
    numero = models.IntegerField('Numero', unique=False)
    direccion = models.TextField('Direccion', unique=False, max_length=200)
    areasalud = models.ForeignKey(AreaSalud, on_delete=models.PROTECT, verbose_name='AreaSalud')

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = 'Consultorio'
        verbose_name_plural = 'Consultorios'
        # ordering = ['municipio']

    def toJson(self):
        item = model_to_dict(self)
        item['areasalud'] = self.areasalud.areasalud
        return item