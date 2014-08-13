from django.conf.urls import patterns, url

from users import views
from papers import views as papers_views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name>[\w\ ]+)$', views.profile, name='profile'),
    url(r'^(?P<name>[\w\ ]+)/(?P<title>[\w\ ]+)/(?P<edition>[\w\ ]+)$', papers_views.listing, name='listing'),
)
