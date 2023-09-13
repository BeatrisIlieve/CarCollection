# Generated by Django 4.2.4 on 2023-09-13 13:46

import car_collection.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_rename_type_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(default=1850, validators=[car_collection.core.validators.validate_car_manufacturing_year]),
        ),
    ]