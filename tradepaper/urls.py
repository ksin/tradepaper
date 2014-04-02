from django.conf.urls import patterns, include, url

from django.contrib import admin
from users import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^users/', include('users.urls')),
    url(r'^login/$', 'users.views.login'),
    url(r'^register/$', 'users.views.register'),
    url(r'^admin/', include(admin.site.urls)),
)
