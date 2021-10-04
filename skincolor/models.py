from django.db import models

# Create your models here.
from django.forms import model_to_dict


class SkinColor(models.Model):
    nskincolor = models.CharField('Color de la Piel', unique=True, max_length=15)

    def __str__(self):
        return self.nskincolor

    class Meta:
        verbose_name = 'Skincolor'
        verbose_name_plural = 'Skincolors'
        # ordering = ['sexo']

    def toJson(self):
        item = model_to_dict(self)
        return item
