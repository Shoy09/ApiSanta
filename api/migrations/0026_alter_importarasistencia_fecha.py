# Generated by Django 5.0.1 on 2024-02-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_estado_fecha_hora_cierre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importarasistencia',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
