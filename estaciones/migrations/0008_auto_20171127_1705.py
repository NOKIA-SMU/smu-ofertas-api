# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0007_auto_20171127_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacion',
            name='latitud',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='estacion',
            name='longitud',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
