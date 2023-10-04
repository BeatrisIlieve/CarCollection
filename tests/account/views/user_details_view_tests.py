from django.test import TestCase
from django.urls import reverse


class UserDetailsViewTests(TestCase):
    def test_when_no_account_created_expect_username_to_be_none(self):
        response = self.client.get(reverse('details profile'))

        self.assertEqual(None, response.context['user'])