from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=40, unique=True)
    city = models.CharField(max_length=60, blank=True)
    website = models.URLField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'city']

    def __unicode__(self):
        return self.username
