from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE = 'Ensure the name contains only letters.'

VALIDATE_CAR_MANUFACTURING_YEAR_MESSAGE = 'Ensure the car manufacturing year is greater than 1849.'

VALIDATE_CAR_MIN_PRICE_MESSAGE = 'Ensure the car price is greater than zero.'

MIN_MANUFACTURING_YEAR = 1850

MIN_CAR_PRICE = 0


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError(VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE)


def validate_car_manufacturing_year(value):
    if not value >= MIN_MANUFACTURING_YEAR:
        raise ValidationError(VALIDATE_CAR_MANUFACTURING_YEAR_MESSAGE)


def validate_car_price(value):
    if value < MIN_CAR_PRICE:
        raise ValidationError(VALIDATE_CAR_MIN_PRICE_MESSAGE)


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f"Max file size is {self.max_size:.2f}MB"
