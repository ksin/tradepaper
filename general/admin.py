from django.contrib import admin
from papers.models import Request, Listing, Message
from users.models import User

admin.site.register([Request, Listing, Message, User])
