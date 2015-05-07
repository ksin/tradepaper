from django.contrib import admin
from papers.models import Trade, Listing, Message
from users.models import User

admin.site.register([Trade, Listing, Message, User])
