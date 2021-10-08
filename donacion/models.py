from datetime import datetime

from django.db import models
from django.forms import model_to_dict

from bloodbank.models import BloodBank
from consultorio.models import Consultorio
from donante.models import Donante


# Create your models here.
class Donacion(models.Model):
    bloodbank = models.ForeignKey(BloodBank, on_delete=models.PROTECT, verbose_name='BloodBank',
                                  related_name='BloodBank')
    donante = models.ForeignKey(Donante, on_delete=models.PROTECT, verbose_name='Donante', related_name='Donante')

    consultorio = models.ForeignKey(Consultorio, on_delete=models.PROTECT, verbose_name='Consultorio',
                                    related_name='Donacion.consultorio+')

    fecha = models.DateField(default=datetime.now, verbose_name='Fecha de la donación')

    observaciones = models.TextField('Observaciones', default='Sin observaciones', unique=False, max_length=500, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.donante, self.consultorio)

    class Meta:
        verbose_name = 'Donacion'
        verbose_name_plural = 'Donaciones'
        # ordering = ['municipio']

    def toJson(self):
        item = model_to_dict(self)
        item['consultorio'] = self.bloodbank.nombre
        item['donante'] = self.donante.ci
        item['consultorio'] = self.consultorio.numero
        return item
