# Generated by Django 2.0 on 2017-12-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0006_auto_20171221_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='codigo_lpu',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
