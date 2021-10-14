from django.db import models
# Create your models here.
from django.forms import model_to_dict

from areasalud.models import AreaSalud


class Consultorio(models.Model):
    numero = models.IntegerField('Número', unique=False)
    direccion = models.TextField('Dirección', unique=False,blank=True, max_length=200)
    areasalud = models.ForeignKey(AreaSalud, on_delete=models.PROTECT, verbose_name='Área de Salud')

    def __str__(self):
        return '#{} - {}'.format(self.numero, self.areasalud)

    class Meta:
        verbose_name = 'Consultorio'
        verbose_name_plural = 'Consultorios'
        # ordering = ['municipio']

    def toJson(self):
        item = model_to_dict(self)
        item['areasalud'] = self.areasalud.nombre
        item['municipio'] = self.areasalud.municipio.municipio
        return item
