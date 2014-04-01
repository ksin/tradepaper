from django.db import models

class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    city = models.CharField(max_length=60, default="")
    website = models.URLField()
    joindate = models.DateTimeField()

    def __unicode__(self):
        return self.username
