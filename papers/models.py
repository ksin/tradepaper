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

class Trade(models.Model):
    date_initiated = models.DateTimeField(default=timezone.now())
    listing = models.ForeignKey(Listing)
    trader = models.ForeignKey(User, related_name='trades_sent')
    tradee = models.ForeignKey(User, related_name='trades_received')

    def __str__(self):
        return "listing: %s, trader: %s" % (self.listing, self.trader)

class Message(models.Model):
    sent_by_trader = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now())
    text = models.TextField(max_length=4096)
    trade = models.ForeignKey(Trade, related_name='messages', null=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        if self.sent_by_trader:
            return "%s: %s" % (self.trade.trader.name, self.text)
        else:
            return "%s: %s" % (self.trade.tradee.name, self.text)
