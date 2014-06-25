import datetime

from django.test import TestCase, Client
from django.contrib.auth import SESSION_KEY
from users.models import User
from django.core.urlresolvers import reverse

from users.models import User

class UserTestCase(TestCase):
    def setUp(self):
        u1 = User.objects.create(id=1,
            email='elibierman@gmail.com',
            password='please',
            name='eli',
            website='elibierman.com',
            city='Ridgewood',
            )
        u1.save()
        u2 = User.objects.create(id=2,
            email='amardeep34@gmail.com',
            password='please',
            name='amardeep',
            website='portfolio.amardeeps.com',
            city='Ridgewood',
            )
        u2.save()

    def test_users_have_category(self):
        first_user = User.objects.get(id=1)
        second_user = User.objects.get(id=2)
        self.assertEqual(first_user.email, 'elibierman@gmail.com')
        self.assertEqual(second_user.email, 'amardeep34@gmail.com')

def create_user(email, password, name, city):
    user = User.objects.create(
        email = email,
        password = password,
        name = name,
        city = city
        )
    user.save()

class UserViewTest(TestCase):
    def test_create_and_log_in_user_with_correct_credentials(self):
        user = create_user('eli@me.com', 'ok', 'eli', 'New York')
        response = self.client.post(reverse('users:login'), {'email':'eli', 'password':'ok'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(SESSION_KEY in self.client.session)

    def test_create_and_log_in_user_with_wrong_password(self):
        user = create_user('eli@me.com', 'ok', 'eli', 'New York')
        response = self.client.post(reverse('users:login'), {'email':'eli', 'password':'NOPE'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(SESSION_KEY in self.client.session)

    def test_create_and_log_in_user_with_wrong_username(self):
        user = create_user('eli@me.com', 'ok', 'eli', 'New York')
        response = self.client.post(reverse('users:login'), {'email':'elly', 'password':'ok'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(SESSION_KEY in self.client.session)

    def test_create_and_log_in_user_and_log_out(self):
        user = create_user('eli@me.com', 'ok', 'eli', 'New York')
        self.client.login(name='eli', password='ok')
        self.assertTrue(SESSION_KEY in self.client.session)
        response = self.client.post(reverse('users:logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(SESSION_KEY in self.client.session)

    def test_create_and_log_in_user_and_check_user_index(self):
        user = create_user('eli@me.com', 'ok', 'eli', 'New York')
        self.client.login(name='eli', password='ok')
        self.assertTrue(SESSION_KEY in self.client.session)
        response = self.client.post(reverse('users:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'eli')
