from papers import models

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model

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

class ListingTestCase(TestCase):
    def test_create_listings(self):
        user = create_user('eli@me.com', 'ok', 'eli', 'New York')
        listing = create_listing('Playdog', '2nd', 8.5, user)
        self.assertContains(user.listing_set.all(), user)
        self.assertEqual(listing.user, user)
        self.assertEqual('Playdog', listing.title)
        self.assertEqual('eli', listing.user.name)
        self.assertGreater(timezone.now(), listing.date_created)
