import datetime

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth import SESSION_KEY, get_user_model
from django.core.urlresolvers import reverse

from users.models import User
import users.views as views

class UserTestCase(TestCase):
    def setUp(self):
        u1 = get_user_model().objects.create(id=1,
            email='elibierman@gmail.com',
            password='please',
            name='eli',
            website='elibierman.com',
            city='Ridgewood',
            )
        u1.save()
        u2 = get_user_model().objects.create(id=2,
            email='amardeep34@gmail.com',
            password='please',
            name='amardeep',
            website='portfolio.amardeeps.com',
            city='Ridgewood',
            )
        u2.save()

    def test_users_have_category(self):
        first_user = get_user_model().objects.get(id=1)
        second_user = get_user_model().objects.get(id=2)
        self.assertEqual(first_user.email, 'elibierman@gmail.com')
        self.assertEqual(second_user.email, 'amardeep34@gmail.com')

def create_user(email, password, name, city):
    user = get_user_model().objects.create_user(
        email = email,
        password = password,
        name = name,
        city = city
        )
    user.save()
    return user

class UserViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_create_and_log_in_user_with_correct_credentials(self):
        user = create_user('eli@me.com', 'ok', 'eli', 'New York')
        response = self.client.post(reverse('login'), {'email':'eli@me.com', 'password':'ok'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(SESSION_KEY in self.client.session)

    def test_create_and_log_in_user_with_wrong_password(self):
        user = create_user('eli@me.com', 'ok', 'eli', 'New York')
        response = self.client.post(reverse('login'), {'email':'eli@me.com', 'password':'NOPE'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(SESSION_KEY in self.client.session)

    def test_create_and_log_in_user_with_wrong_email(self):
        user = create_user('eli@me.com', 'ok', 'eli', 'New York')
        response = self.client.post(reverse('login'), {'email':'elly@me.com', 'password':'ok'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(SESSION_KEY in self.client.session)

    def test_create_and_log_in_user_and_log_out(self):
        user = create_user('eli@me.com', 'ok', 'eli', 'New York')
        self.client.login(email='eli@me.com', password='ok')
        self.assertTrue(SESSION_KEY in self.client.session)
        response = self.client.get(reverse('logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(SESSION_KEY in self.client.session)

    def test_register_new_user_with_all_fields_and_check_if_logged_in(self):
        response = self.client.post(reverse('register'),
                {'email':'eli@me.com',
                'password':'ok',
                'name':'eli',
                'city':'NYC'},
                follow=True)
        self.assertTrue(SESSION_KEY in self.client.session)
        self.assertEqual(response.status_code, 200)

    def test_register_new_user_with_missing_fields_and_check_if_logged_in(self):
        # improper email
        response = self.client.post(reverse('register'),
                {'email':'eli',
                'password':'ok',
                'name':'eli',
                'city':'NYC'},
                follow=True)
        self.assertFalse(SESSION_KEY in self.client.session)
        self.assertEqual(response.status_code, 200)
        # missing city field
        response = self.client.post(reverse('register'),
                {'email':'eli',
                'password':'ok',
                'name':'eli'},
                follow=True)
        self.assertFalse(SESSION_KEY in self.client.session)
        self.assertEqual(response.status_code, 200)

#    def test_vet_user_without_logging_in(self):
#        request = self.factory.get('/my-account')
#        try:
#            user = views.vet_user(request, "You need to be logged in to do that.")
#        except LoginException, redirect:
#            self.assertEqual(redirect.resolver_match.func, views.login)
#            self.assert(redirect in self.client.session)
#            return
#        # if it gets here, it didn't catch the exception
#        self.assertTrue(False)
