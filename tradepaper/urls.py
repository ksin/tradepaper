from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.contrib import admin
from general import views
from users import views
admin.autodiscover()

urlpatterns = patterns('',
    # pass requests on to other url configs
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^papers/', include('papers.urls', namespace='papers')),
    url(r'^admin/', include(admin.site.urls)),

    # general views
    url(r'^/?$', 'general.views.home', name='home'),
    url(r'^about/?$', 'general.views.about', name='about'),
    url(r'^faq/?$', 'general.views.faq', name='faq'),
    url(r'^shipping/?$', 'general.views.shipping', name='shipping'),
    url(r'^resetpassword/?$', 'general.views.reset_password', name='reset_password'),
    url(r'^resetlink/?$', 'general.views.reset_link', name='reset_link'),

    # users views
    url(r'^login/?$', 'users.views.login', name='login'),
    url(r'^logout/?$', 'users.views.logout', name='logout'),
    url(r'^register/?$', 'users.views.register', name='register'),
    url(r'^myaccount/?$', 'users.views.my_account', name='my_account'),
    url(r'^myaccount/preferences/?$', 'users.views.preferences', name='preferences'),
    url(r'^requests/?$', 'users.views.requests', name='requests'),
    url(r'^manage/?$', 'users.views.manage', name='manage'),
    url(r'^editprofile/?$', 'users.views.edit_profile', name='edit_profile'),

    # papers views
    url(r'^browse/?$', 'papers.views.browse', name='browse'),
)

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
