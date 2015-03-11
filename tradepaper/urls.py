from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

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
    url(r'^faq/?$', 'general.views.faq', name='faq'),
    url(r'^shipping/?$', 'general.views.shipping', name='shipping'),
    url(r'^login/?$', 'users.views.login', name='login'),
    url(r'^logout/?$', 'users.views.logout', name='logout'),
    url(r'^register/?$', 'users.views.register', name='register'),

)

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
