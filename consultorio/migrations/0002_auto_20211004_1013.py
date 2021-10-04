# Generated by Django 3.1.1 on 2021-10-04 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('areasalud', '0002_auto_20211002_0909'),
        ('consultorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultorio',
            name='areasalud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='areasalud.areasalud', verbose_name='Área de Salud'),
        ),
        migrations.AlterField(
            model_name='consultorio',
            name='direccion',
            field=models.TextField(blank=True, max_length=200, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='consultorio',
            name='numero',
            field=models.IntegerField(verbose_name='Número'),
        ),
    ]
