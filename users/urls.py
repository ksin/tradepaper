from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>\w+)$', views.profile, name='profile')
)
