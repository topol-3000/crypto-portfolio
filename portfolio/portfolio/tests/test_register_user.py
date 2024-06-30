from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from portfolio.models import User


class UserRegistrationViewTestCase(TestCase):
    """
    Test case for UserRegistrationView
    """

    def setUp(self):
        """
        Setup test client and url
        """
        self.client = Client()
        self.url = reverse("registration")

    def test_post_request_creates_user(self):
        """
        Test post request that should create a user and return a 201 status code.
        """
        initial_user_count = User.objects.count()
        data = {
            "full_name": "Full Name",
            "email": "test@example.com",
            "password": "testpassword",
        }
        response = self.client.post(self.url, data)
        response_expected = {
            "full_name": "Full Name",
            "email": "test@example.com",
        }

        final_user_count = User.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.get("content-type"), "application/json")
        self.assertDictEqual(response.json(), response_expected)
        self.assertEqual(final_user_count, initial_user_count + 1)

    def test_get_request_does_not_create_user(self):
        """
        Test get request that should not create a user and return a 405 status code.
        """
        initial_user_count = User.objects.count()
        response = self.client.get(self.url)
        self.assertEqual(response.get("content-type"), "application/json")
        self.assertEqual(response.json(), {"detail": 'Method "GET" not allowed.'})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        final_user_count = User.objects.count()
        self.assertEqual(initial_user_count, final_user_count)
