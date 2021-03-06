from django.db import models
# Create your models here.
from django.forms import model_to_dict

from bloodgroup.bloodgroup_choices import bloodgroup


class BloodGroup(models.Model):
    bloodgroup = models.CharField('Grupo Sanguineo', choices=bloodgroup, unique=True, max_length=5)

    def __str__(self):
        return '{}'.format(self.bloodgroup)

    class Meta:
        verbose_name = 'BloodGroup'
        verbose_name_plural = 'BloodGroups'
        # ordering = ['municipio']

    def toJson(self):
        item = model_to_dict(self)
        return item
