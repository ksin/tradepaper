from django.conf.urls import patterns, url

from papers import views

urlpatterns = patterns('',
    url(r'^browse/$', views.browse, name='browse'),
)
