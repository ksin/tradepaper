from django.conf.urls import patterns, url

from papers import views

urlpatterns = patterns('',
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^new/$', views.new_listing, name='new_listing'),
    url(r'^(?P<id>\w+)/$', views.listing, name='listing'),
)
