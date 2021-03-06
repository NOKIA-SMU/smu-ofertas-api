# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 01:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estaciones', '0012_auto_20171127_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subsistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('estado', models.BooleanField(default=True, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subsistemas', to='estaciones.Estacion')),
            ],
            options={
                'verbose_name': 'subsistema',
                'verbose_name_plural': 'subsistemas',
                'ordering': ('creado',),
            },
        ),
    ]
