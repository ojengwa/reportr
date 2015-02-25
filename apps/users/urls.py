from django.conf.urls import patterns, include, url
from apps.users import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^profile/(?P<username>[^/]+)$', views.profile, name='profile'),
    url(r'^home/$', views.success, name='success'),
)
