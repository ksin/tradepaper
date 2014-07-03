from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from general import views
from users import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^papers/', include('papers.urls', namespace='papers')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', 'general.views.home', name='home'),
    url(r'^about/?$', 'general.views.about', name='about'),
    url(r'^login/?$', 'users.views.login', name='login'),
    url(r'^logout/?$', 'users.views.logout', name='logout'),
    url(r'^register/?$', 'users.views.register', name='register'),

)

urlpatterns += staticfiles_urlpatterns()
