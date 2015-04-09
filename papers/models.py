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

    def __str__(self):
        return "%s, %s" % (self.title, self.edition)

class Request(models.Model):
    date_initiated = models.DateTimeField(default=timezone.now())
    listing = models.ForeignKey(Listing)
    requester = models.ForeignKey(User, related_name='requests_sent')
    requestee = models.ForeignKey(User, related_name='requests_received')

    def __str__(self):
        return "listing: %s, requester: %s" % (self.listing, self.requester)

class Message(models.Model):
    sent_by_requester = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now())
    text = models.TextField(max_length=4096)
    request = models.ForeignKey(Request, related_name='messages', null=True)

    def __str__(self):
        if self.sent_by_requester:
            return "%s: %s" % (self.request.requester.name, self.text)
        else:
            return "%s: %s" % (self.request.requestee.name, self.text)
