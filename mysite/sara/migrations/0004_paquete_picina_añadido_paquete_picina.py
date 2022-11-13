# Generated by Django 4.1.2 on 2022-11-07 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sara', '0003_alter_galeria_picina_imagen_alter_picina_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paquete_picina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('picina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sara.picina')),
            ],
        ),
        migrations.CreateModel(
            name='Añadido_paquete_picina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('picina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sara.picina')),
            ],
        ),
    ]
