# Generated by Django 3.1.1 on 2021-10-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodgroup', models.CharField(max_length=5, unique=True, verbose_name='Grupo Sanguineo')),
            ],
            options={
                'verbose_name': 'BloodGroup',
                'verbose_name_plural': 'BloodGroups',
            },
        ),
    ]