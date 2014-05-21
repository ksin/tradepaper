from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from general import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^papers/', include('papers.urls', namespace='papers')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', 'general.views.home', name='home'),
    url(r'^about/?$', 'general.views.about', name='about'),
)

urlpatterns += staticfiles_urlpatterns()
