# Generated by Django 3.1.1 on 2021-10-02 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('municipio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, unique=True, verbose_name='Nombre')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='municipio.municipios', verbose_name='Municipio')),
            ],
            options={
                'verbose_name': 'BloodBank',
                'verbose_name_plural': 'BloodBanks',
            },
        ),
    ]
