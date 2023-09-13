# account/models.py
from django.core.validators import MinLengthValidator
from django.db import models

from car_collection.car.models import Car
from car_collection.core.validators import MaxFileSizeInMbValidator, validate_only_letters


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 25

    TOTAL_PRICE_DEFAULT_VALUE = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

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

    email = models.EmailField()

    age = models.IntegerField()

    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


