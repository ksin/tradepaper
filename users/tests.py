import datetime

from django.test import TestCase, Client
from users.models import User
from django.core.urlresolvers import reverse

from users.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(id=1,
            username='eli',
            email='elibierman@gmail.com',
            password='please',
            website='elibierman.com',
            city='Ridgewood',
            )
        User.objects.create(id=2,
            username='amardeep',
            email='amardeep34@gmail.com',
            password='please',
            website='portfolio.amardeeps.com',
            city='Ridgewood',
            )

    def test_users_have_category(self):
        first_user = User.objects.get(id=1)
        second_user = User.objects.get(id=2)
        self.assertEqual(first_user.email, 'elibierman@gmail.com')
        self.assertEqual(second_user.email, 'amardeep34@gmail.com')

def create_user(username, email, password):
    User.objects.create(
        username=username,
        email=email,
        password=password,
        )

class UserViewTest(TestCase):
    def test_create_and_log_in_user_with_correct_credentials(self):
        user = create_user('eli', 'eli@me.com', 'ok')
        c = Client()
        logged_in = c.login(username='eli', password='ok')
        self.assertEqual(logged_in, True)

    def test_create_and_log_in_user_with_wrong_password(self):
        user = create_user('eli', 'eli@me.com', 'ok')
        c = Client()
        logged_in = c.login(username='eli', password='NOk')
        self.assertEqual(logged_in, False)

    def test_create_and_log_in_user_with_wrong_username(self):
        user = create_user('eli', 'eli@me.com', 'ok')
        c = Client()
        logged_in = c.login(username='fred', password='ok')
        self.assertEqual(logged_in, False)

    # def test_create_and_log_in_user_and_log_out(self):
    #
    # def test_create_and_log_in_user_and_check_user_index(self):
