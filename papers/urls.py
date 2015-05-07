from django.conf.urls import patterns, url

from papers import views

urlpatterns = patterns('',
    url(r'^new/$', views.new_listing, name='new_listing'),
    url(r'^request/(?P<id>\w+)/$', views.trade, name='trade'),
    url(r'^new-request/(?P<listing_id>\w+)/$', views.new_trade(), name='new_trade()'),
    url(r'^(?P<id>\w+)/$', views.listing, name='listing'),
)
