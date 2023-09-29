# account/models.py
from enum import Enum

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from car_collection.account.manager import CarCollectionUserManager
from car_collection.car.models import Car
from car_collection.core.modelmixins import ChoicesEnumMixin
from car_collection.core.validators import MaxFileSizeInMbValidator, validate_only_letters


class CarCollectionUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False
    )

    USERNAME_FIELD = 'email'

    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )

    objects = CarCollectionUserManager()


class Gender(ChoicesEnumMixin, Enum):
    Female = 'Female'
    Male = 'Male'
    DoNotShow = 'Do not Show'


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

    age = models.IntegerField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        null=True,
        blank=True,
        choices=Gender.choices(),
        max_length=Gender.max_length(),
    )

    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )

    user = models.OneToOneField(
        CarCollectionUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
