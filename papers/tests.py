import os
import codecs

from papers.models import Listing, Trade, Message
from tradepaper.settings import MEDIA_ROOT

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.files import File
from django.utils import timezone
from django.contrib.auth import SESSION_KEY, get_user_model

def create_listing(title, issue, condition, user):
    listing = Listing.objects.create(
        title = title,
        issue = issue,
        condition = condition,
        user = user
    )
    listing.save()
    return listing

def create_user(email, password, name, city):
    user = get_user_model().objects.create_user(
        email = email,
        password = password,
        name = name,
        city = city
        )
    user.save()
    return user

def create_trade():
    tradee = create_user('che@me.com', 'ok', 'che', 'New Mexico')
    tradee.save()
    trader = create_user('eli@me.com', 'ok', 'eli', 'New York')
    trader.save()
    listing = create_listing('Playdog', '2nd', 8.5, tradee)
    listing.save()
    trade = Trade.objects.create(
        trader = trader,
        tradee = tradee,
        date_initiated = timezone.now(),
        listing = listing
    )
    trade.save()
    return trade

def create_message(trade, sent_by_trader, date, text):
    message = Message.objects.create(
        trade = trade,
        date = date,
        text = text,
        sent_by_trader = sent_by_trader
    )
    message.save()
    return message

class ListingTestCase(TestCase):
    def test_create_listings(self):
        user = create_user('eli@me.com', 'ok', 'eli', 'New York')
        listing = create_listing('Playdog', '2nd', 8.5, user)
        self.assertEqual(user.listing_set.all()[0], listing)
        self.assertEqual(listing.user, user)
        self.assertEqual('Playdog', listing.title)
        self.assertEqual('eli', listing.user.name)
        self.assertGreater(timezone.now(), listing.date_posted)

class TradeTestCase(TestCase):
    def test_create_new_trade_with_no_messages(self):
        trade = create_trade()
        self.assertEqual('Playdog', trade.listing.title)
        self.assertEqual('eli', trade.trader.name)
        self.assertEqual('che', trade.tradee.name)
        self.assertEqual(trade.messages.count(), 0)

    def test_create_new_trade_with_some_messages(self):
        trade = create_trade()
        first_message = create_message(trade,
                                       True,
                                       timezone.now()-timezone.timedelta(days=3),
                                       'Hey! Want to trade?')
        second_message = create_message(trade,
                                        False,
                                        timezone.now()-timezone.timedelta(days=2),
                                        'Hellllz yeah!')
        third_message = create_message(trade,
                                       True,
                                       timezone.now()-timezone.timedelta(days=1),
                                       'iight coo')
        self.assertEqual('Playdog', trade.listing.title)
        self.assertEqual('eli', trade.trader.name)
        self.assertEqual('che', trade.tradee.name)
        self.assertEqual(trade.messages.count(), 3)

class ListingViewTestCase(TestCase):
    def test_log_in_and_create_new_listing(self):
        # create user and log in
        user = create_user('eli@me.com', 'ok', 'eli', 'New York')
        self.client.login(email='eli@me.com', password='ok')
        self.assertTrue(SESSION_KEY in self.client.session)

        # create new listing
        image = codecs.open(os.path.join(MEDIA_ROOT, '1x1.GIF'))
        response = self.client.post(reverse('papers:new_listing'), {
                "title":"Art Forum",
                "issue":"First",
                "condition":7,
                "image": image
                }, follow=True)
        l = user.listing_set.all()[0]
        self.assertEqual(l.title, "Art Forum")
        self.assertEqual(l.issue, "First")
        self.assertEqual(l.condition, 7)
        self.assertEqual(l.user, user)
        self.assertEqual(response.status_code, 200)

    def test_log_in_and_create_new_listing_with_missing_fields(self):
        # create user and log in
        user = create_user('eli@me.com', 'ok', 'eli', 'New York')
        self.client.login(email='eli@me.com', password='ok')
        self.assertTrue(SESSION_KEY in self.client.session)

        # create new listing with no condition
        response = self.client.post(reverse('papers:new_listing'), {
                'title':"Art Forum",
                'issue':'First'
                }, follow=True)
        self.assertEqual(user.listing_set.count(), 0)

        # create new listing with no issue
        response = self.client.post(reverse('papers:new_listing'), {
                'title':"Art Forum",
                'condition':7
                }, follow=True)
        self.assertEqual(user.listing_set.count(), 0)
