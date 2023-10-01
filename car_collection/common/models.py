from django.db import models

from car_collection.account.models import Profile
from car_collection.car.models import Car


class CarLookedAt(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        Profile,
        on_delete=models.RESTRICT,
    )
