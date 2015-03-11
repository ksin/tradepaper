from django.conf.urls import patterns, url

from users import views
from papers import views as papers_views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^myaccount/$', views.my_account, name='my_account'),
    url(r'^requests/$', views.requests, name='requests'),
    url(r'^(?P<name>[\w\ ]+)$', views.profile, name='profile'),
)
