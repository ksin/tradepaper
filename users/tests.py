import datetime

from django.test import TestCase, Client
from users.models import User
from django.core.urlresolvers import reverse

from users.models import User

class UserTestCase(TestCase):
    def setUp(self):
        u1 = User.objects.create(id=1,
            username='eli',
            email='elibierman@gmail.com',
            password='please',
            website='elibierman.com',
            city='Ridgewood',
            )
        u1.save()
        u2 = User.objects.create(id=2,
            username='amardeep',
            email='amardeep34@gmail.com',
            password='please',
            website='portfolio.amardeeps.com',
            city='Ridgewood',
            )
        u2.save()

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
        response = self.client.post(reverse('users:login'), {'username':'eli', 'password':'ok'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('_auth_user_id', self.client.session)
        self.assertEqual(self.client.session['_auth_user_id'], user.pk)

    # def test_create_and_log_in_user_with_wrong_password(self):
    #     user = create_user('eli', 'eli@me.com', 'ok')
    #     login_response = self.client.get(reverse('users:login'))
    #     self.assertEqual(login_response.status_code, 200)
    #     logged_in_response = self.client.get(reverse('users:login'))
    #     self.assertEqual(response.request.user.is_authenticated(), True)
    #
    # def test_create_and_log_in_user_with_wrong_username(self):
    #     user = create_user('eli', 'eli@me.com', 'ok')
    #     c = Client()
    #     logged_in = c.login(username='eli', password='ok')
    #     self.assertEqual(logged_in, True)
    #     logged_out = c.logout()
    #     self.assertEqual(logged_in, True)
    #
    # def test_create_and_log_in_user_and_log_out(self):
    #     user = create_user('eli', 'eli@me.com', 'ok')
    #     c = Client()
    #     logged_in = c.login(username='fred', password='ok')
    #     self.assertEqual(logged_in, False)
    #
    # def test_create_and_log_in_user_and_check_user_index(self):
