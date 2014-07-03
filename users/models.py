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
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'city']

    objects = UserManager()

    def has_perm(perm, obj=None):
        return False;
        # Returns True if the user has the named permission. If obj is provided,
        # the permission needs to be checked against a specific object instance
    def has_module_perms(app_label):
        return False;
        # Returns True if the user has permission to access models in the given app.

    def __unicode__(self):
        return self.email
