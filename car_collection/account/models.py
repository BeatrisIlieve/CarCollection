# account/models.py
from django.core.validators import MinLengthValidator
from django.db import models

from car_collection.core.validators import MaxFileSizeInMbValidator, validate_only_letters


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 25

    USERNAME_MIN_LENGTH = 2
    USERNAME_MAX_LENGTH = 15

    TOTAL_PRICE_DEFAULT_VALUE = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'cars/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
        ),
        null=False,
        blank=False
    )

    email = models.EmailField()

    age = models.IntegerField()

    total_price = models.FloatField(
        default=TOTAL_PRICE_DEFAULT_VALUE,
    )

    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )
