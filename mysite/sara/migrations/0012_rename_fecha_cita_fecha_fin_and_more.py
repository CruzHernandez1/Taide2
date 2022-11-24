# Generated by Django 4.1.3 on 2022-11-24 04:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sara', '0011_remove_cita_fecha_hora_final_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cita',
            old_name='fecha',
            new_name='fecha_fin',
        ),
        migrations.RenameField(
            model_name='cita',
            old_name='hora',
            new_name='hora_fin',
        ),
        migrations.AddField(
            model_name='cita',
            name='fecha_inicio',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cita',
            name='hora_inicio',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]