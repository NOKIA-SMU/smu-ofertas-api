# Generated by Django 2.0 on 2017-12-21 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0020_auto_20171219_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='margen',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True),
        ),
    ]
