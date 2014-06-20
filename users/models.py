from django.db import models

class User(models.Model):
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(unique=True, )
    city = models.CharField(max_length=60, blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.username
