# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0004_auto_20171201_1755'),
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='solicitud',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofertas', to='solicitudes.Solicitud'),
        ),
    ]
