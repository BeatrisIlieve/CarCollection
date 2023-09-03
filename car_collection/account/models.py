# account/models.py

from django.db import models


class Profile(models.Model):
    MAX_NAME = 10

    username = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False
    )
