from django.conf.urls import patterns, url

from users import views
from papers import views as papers_views

urlpatterns = patterns('',
    url(r'^(?P<name>[\w\ ]+)$', views.profile, name='profile'),
)
