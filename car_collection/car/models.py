from django.db import models

from car_collection.account.validators import MaxFileSizeInMbValidator


class Car(models.Model):
    MAX_MODEL_LENGTH = 30

    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'cars/'

    SPORT_CAR = "Sport Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CAR_PRICE_DEFAULT_VALUE = 0
    CAR_YEAR = 1850

    CARS = (
        (SPORT_CAR, SPORT_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        choices=CARS,
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        default=CAR_YEAR,
        null=False,
        blank=False,
    )

    car_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )

    price = models.FloatField(
        default=CAR_PRICE_DEFAULT_VALUE,
        null=False,
        blank=False,
    )
