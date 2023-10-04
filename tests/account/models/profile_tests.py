from django.core.exceptions import ValidationError
from django.test import TestCase

from car_collection.account.models import Profile, CarCollectionUser


class ProfileModelTests(TestCase):
    def setUp(self) -> None:
        self.user = CarCollectionUser(
            email='beatrisilieve@icloud.com',
            password='S@3ana3a'
        )

        self.user.full_clean()
        self.user.save()

    def test_profile_save__when_first_name_min_length_is_valid__expect_correct_result(self):
        profile = Profile(
            first_name='Beatris',
            last_name='Ilieve',
            user=self.user,

        )

        profile.full_clean()
        profile.save()

        self.assertIsNotNone(profile.user_id)

    def test_profile_save__when_first_name_min_length_is_invalid__expect_exception(self):
        profile = Profile(
            first_name='B',
            last_name='Ilieve',
            user=self.user,

        )

        with self.assertRaises(ValidationError) as ve:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(ve)

    def test_profile_save__when_first_name_does_not_contain_only_letters_invalid__expect_exception(self):
        profile = Profile(
            first_name='B3@',
            last_name='Ilieve',
            user=self.user,

        )

        with self.assertRaises(ValidationError) as ve:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(ve)

    def test_profile_save__when_last_name_min_length_is_valid__expect_correct_result(self):
        profile = Profile(
            first_name='Beatris',
            last_name='Ilieve',
            user=self.user,

        )

        profile.full_clean()
        profile.save()

        self.assertIsNotNone(profile.user_id)

    def test_profile_save__when_last_name_min_length_is_invalid__expect_exception(self):
        profile = Profile(
            first_name='Beatris',
            last_name='I',
            user=self.user,

        )

        with self.assertRaises(ValidationError) as ve:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(ve)

    def test_profile_save__when_last_name_does_not_contain_only_letters_invalid__expect_exception(self):
        profile = Profile(
            first_name='Beatris',
            last_name='Iliev3',
            user=self.user,

        )

        with self.assertRaises(ValidationError) as ve:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(ve)

