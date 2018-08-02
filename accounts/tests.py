from django.test import TestCase

from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='cfe', email='hello@cfe.com')
        user.set_password("yeahhhcfe")
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='cfe')
        self.assertEqual(qs.count(), 1)

# from django.test import TestCase
#
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# class StatusTestCase(TestCase):
#     def setUp(self):
#         user = User.objects.create(username='cfe', email='hello@cfe.com')
#         user.set_password("UserTest")
#         user.save()
#
#     def test_created_user(self):
#         qs = User.objects.filter(username='cfe')
#         self.assertEqual(qs.count(), 1)  # <-- this command runs test. Tests to make that one user was created
#

