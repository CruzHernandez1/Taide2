# Generated by Django 4.1.2 on 2022-11-09 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sara', '0005_suministro_picina_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete_picina',
            name='descripcion',
            field=models.TextField(max_length=100),
        ),
    ]
