# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='credential',
            field=models.TextField(unique=True),
        ),
    ]
