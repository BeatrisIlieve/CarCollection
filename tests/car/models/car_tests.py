from django.test import TestCase

from car_collection.car.models import Car


class CarModelTests(TestCase):
    def test_car_save__when__year_is_valid__expect_correct_resul(self):
        car = Car(
            brand='Audi',
            model='TT',
            year=1850,
            car_image='some_image',
            price=100
        )

        car.full_clean()
        car.save()
        self.assertIsNotNone(car.pk)