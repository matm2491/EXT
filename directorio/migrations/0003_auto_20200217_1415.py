# Generated by Django 3.0.2 on 2020-02-17 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0002_tinciudades_tinestados_tinmunicipios2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TinCiudades',
        ),
        migrations.DeleteModel(
            name='TinEstados',
        ),
        migrations.DeleteModel(
            name='TinMunicipios2',
        ),
    ]