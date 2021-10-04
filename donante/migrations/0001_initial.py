# Generated by Django 3.1.1 on 2021-10-04 12:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skincolor', '0002_auto_20211004_1349'),
        ('core', '0002_auto_20211004_1405'),
        ('consultorio', '0002_auto_20211004_1013'),
        ('bloodgroup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{11}$', message='Carné incorrecto'), django.core.validators.MinLengthValidator(11, message='El carné debe contener 11 caracteres')], verbose_name='Carnet de identidad')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('edad', models.IntegerField(validators=[django.core.validators.MaxValueValidator(25, message='La edad no puede ser superior a 25 años'), django.core.validators.MinValueValidator(5, message='La edad no puede ser menor a 5 años')], verbose_name='Edad')),
                ('direccion', models.TextField(max_length=200, verbose_name='Direccion')),
                ('bloodgroup', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='BloodGroup', to='bloodgroup.bloodgroup', verbose_name='Grupo sanguineo')),
                ('consultorio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Consultorio', to='consultorio.consultorio', verbose_name='Consultorio')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Sexo', to='core.sexo', verbose_name='Sexo')),
                ('skincolor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='SkinColor', to='skincolor.skincolor', verbose_name='Color de la piel')),
            ],
            options={
                'verbose_name': 'Donante',
                'verbose_name_plural': 'Donantes',
            },
        ),
    ]
