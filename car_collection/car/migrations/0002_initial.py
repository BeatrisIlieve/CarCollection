# Generated by Django 4.2.4 on 2023-09-29 16:19

import car_collection.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField()),
                ('model', models.CharField(choices=[('Sport Car', 'Sport Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Minibus', 'Minibus'), ('Other', 'Other')], max_length=30)),
                ('year', models.IntegerField(default=1850, validators=[car_collection.core.validators.validate_car_manufacturing_year])),
                ('car_image', models.ImageField(upload_to='cars/', validators=[car_collection.core.validators.MaxFileSizeInMbValidator(5)])),
                ('price', models.FloatField(default=0, validators=[car_collection.core.validators.validate_car_price])),
            ],
        ),
    ]
