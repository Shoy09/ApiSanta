# Generated by Django 5.0.1 on 2024-02-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_sucursal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumidor',
            fields=[
                ('idconsumidor', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre_apellido', models.CharField(max_length=250)),
            ],
        ),
    ]
