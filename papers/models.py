from users.models import User

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

class Listing(models.Model):
    title = models.CharField(max_length=140)
    edition = models.CharField(max_length=60)
    condition = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(10)])
    user = models.ForeignKey(User)
    date_posted = models.DateTimeField(default=timezone.now())
    image = models.ImageField(upload_to='images')

    def __unicode__(self):
        return "%s, %s" % (self.title, self.edition)
