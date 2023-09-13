# car/models.py
from django.db import models

from car_collection.core.validators import MaxFileSizeInMbValidator, validate_car_manufacturing_year, validate_car_price


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
    DEFAULT_MANUFACTURING_YEAR = 1850

    CARS = (
        (SPORT_CAR, SPORT_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    brand = models.CharField(
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
        default=DEFAULT_MANUFACTURING_YEAR,
        null=False,
        blank=False,
        validators=(
            validate_car_manufacturing_year,
        ),
    )

    car_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=False,
        blank=False,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )

    price = models.FloatField(
        default=CAR_PRICE_DEFAULT_VALUE,
        null=False,
        blank=False,
        validators=(
            validate_car_price,
        ),
    )
