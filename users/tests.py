from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()


class UsersManagersTests(TestCase):
    
    def test_create_user(self):
        user = User.objects.create_user(email='test@test.com', password='test')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='test')
    
    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(email='admin@test.com',
                                                   password='admin')
        self.assertEqual(admin_user.email, 'admin@test.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='admin@test.com',
                                          password='admin', is_superuser=False)
