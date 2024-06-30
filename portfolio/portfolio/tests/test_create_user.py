from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    """
    Tests for the custom user model manager.
    """

    def test_create_user(self):
        """
        Creates a normal user with the given info.
        """
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo", full_name="Normal User")
        self.assertEqual(user.email, "normal@user.com")
        self.assertEqual(user.full_name, "Normal User")

        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(hasattr(user, "username"))

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")

    def test_create_superuser(self):
        """
        Creates a superuser with the given info.
        """
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo", full_name="Super User")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertEqual(admin_user.full_name, "Super User")

        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertFalse(hasattr(admin_user, "username"))

        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="super@user.com", password="foo", is_superuser=False)
