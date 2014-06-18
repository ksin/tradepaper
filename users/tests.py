import datetime

from django.test import TestCase
from users.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(id=1,
            username='eli',
            email='elibierman@gmail.com',
            password='please',
            website='elibierman.com',
            city='Ridgewood',
            joindate=datetime.datetime.now(),
            )
        User.objects.create(id=2,
            username='amardeep',
            email='amardeep34@gmail.com',
            password='please',
            website='portfolio.amardeeps.com',
            city='Ridgewood',
            joindate=datetime.datetime.now(),
            )

    def test_users_have_category(self):
        first_user = User.objects.get(id=1)
        second_user = User.objects.get(id=2)
        self.assertEqual(first_user.email, 'elibierman@gmail.com')
        self.assertEqual(second_user.email, 'amardeep34@gmail.com')

class UserViewTest(TestCase):
    def test_create_and_log_in_user_with_correct_credentials(self):

    def test_create_and_log_in_user_with_wrong_password(self):

    def test_create_and_log_in_user_with_nonexistent_username(self):

    def test_create_and_log_in_user_and_log_out(self):

    def test_create_and_log_in_user_and_check_user_index(self):
