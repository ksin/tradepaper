import datetime

from django.test import TestCase
from users.models import User

class UserTestCase(TestCase):
    def test_setUp(self):
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
        print 'setup:', User.objects.all()

    def test_post_have_category(self):
        print 'setup:', User.objects.all()
        first_user = User.objects.get(id=1)
        second_user = User.objects.get(id=2)
        self.assertEqual(first_user.email, 'elibierman@gmail.com')
        self.assertEqual(second_user.email, 'amardeep34@gmail.com')
