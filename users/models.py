from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):

    def create_user(self, email, password, name, city, is_staff=False, is_superuser=False):
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          city=city, is_active=True,
                          is_staff=is_staff, is_superuser=is_superuser,
                          last_login=now, date_joined=now)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, name, city):
        return self.create_user(email, password, name, city, True, True)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=40, unique=True)
    city = models.CharField(max_length=60, blank=True)
    website = models.URLField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'city']

    objects = UserManager()

    def __unicode__(self):
        return self.username
