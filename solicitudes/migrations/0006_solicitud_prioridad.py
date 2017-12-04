# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0005_auto_20171203_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='prioridad',
            field=models.CharField(blank=True, choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')], max_length=255, null=True),
        ),
    ]