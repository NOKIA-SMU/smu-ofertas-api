# Generated by Django 2.0 on 2017-12-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suministros', '0005_auto_20171221_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suministro',
            name='codigo_lpu',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='suministro',
            name='codigo_mm',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='suministro',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
