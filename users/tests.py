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

    def test_post_have_category(self):
        first_post = Post.objects.get(id=1)
        second_post = Post.objects.get(id=2)
        self.assertEqual(first_post.email, 'elibierman@gmail.com')
        self.assertEqual(second_post.email, 'amardeep34@gmail.com')
