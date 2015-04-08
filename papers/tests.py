import os
import codecs

from papers.models import Listing, Request, Message
from tradepaper.settings import MEDIA_ROOT

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.files import File
from django.utils import timezone
from django.contrib.auth import SESSION_KEY, get_user_model

def create_listing(title, edition, condition, user):
    listing = Listing.objects.create(
        title = title,
        edition = edition,
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

def create_request():
    requestee = create_user('che@me.com', 'ok', 'che', 'New Mexico')
    requestee.save()
    requester = create_user('eli@me.com', 'ok', 'eli', 'New York')
    requester.save()
    listing = create_listing('Playdog', '2nd', 8.5, requestee)
    listing.save()
    request = Request.objects.create(
        requester = requester,
        requestee = requestee,
        date_initiated = timezone.now(),
        listing = listing
    )
    request.save()
    return request

def create_message(request, sent_by_requester, date, text):
    message = Message.objects.create(
        request = request,
        date = date,
        text = text,
        sent_by_requester = sent_by_requester
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

class RequestTestCase(TestCase):
    def test_create_new_request_with_no_messages(self):
        request = create_request()
        self.assertEqual('Playdog', request.listing.title)
        self.assertEqual('eli', request.requester.name)
        self.assertEqual('che', request.requestee.name)
        self.assertEqual(request.messages.count(), 0)

    def test_create_new_request_with_some_messages(self):
        request = create_request()
        first_message = create_message(request,
                                       True,
                                       timezone.now()-timezone.timedelta(days=3),
                                       'Hey! Want to trade?')
        second_message = create_message(request,
                                        False,
                                        timezone.now()-timezone.timedelta(days=2),
                                        'Hellllz yeah!')
        third_message = create_message(request,
                                       True,
                                       timezone.now()-timezone.timedelta(days=1),
                                       'iight coo')
        self.assertEqual('Playdog', request.listing.title)
        self.assertEqual('eli', request.requester.name)
        self.assertEqual('che', request.requestee.name)
        self.assertEqual(request.messages.count(), 3)

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
                "edition":"First",
                "condition":7,
                "image": image
                }, follow=True)
        l = user.listing_set.all()[0]
        self.assertEqual(l.title, "Art Forum")
        self.assertEqual(l.edition, "First")
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
                'edition':'First'
                }, follow=True)
        self.assertEqual(user.listing_set.count(), 0)

        # create new listing with no edition
        response = self.client.post(reverse('papers:new_listing'), {
                'title':"Art Forum",
                'condition':7
                }, follow=True)
        self.assertEqual(user.listing_set.count(), 0)
