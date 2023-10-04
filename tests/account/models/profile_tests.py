from django.test import TestCase

from car_collection.account.models import Profile, CarCollectionUser


class ProfileModelTests(TestCase):
    def test_profile_save__when_first_name_is_valid__expect_corrct_result(self):
        user = CarCollectionUser(
            email='beatrisilieve@icloud.com',
            password='S@3ana3a'
        )

        user.full_clean()
        user.save()

        profile = Profile(
            first_name='Beatris',
            last_name='Ilieve',
            user=user,

        )

        profile.full_clean()
        profile.save()

        self.assertIsNotNone(profile.user_id)