# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 17:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='servicio',
            new_name='servicios',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='suministro',
            new_name='suministros',
        ),
    ]