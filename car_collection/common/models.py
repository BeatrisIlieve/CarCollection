from django.contrib.auth import get_user_model
from django.db import models

from car_collection.car.models import Car

CarCollectionUserModel = get_user_model()


class CarLookedAt(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        CarCollectionUserModel,
        on_delete=models.RESTRICT,
    )
