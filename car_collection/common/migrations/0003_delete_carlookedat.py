# Generated by Django 4.2.4 on 2023-10-01 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_carlookedat_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarLookedAt',
        ),
    ]
