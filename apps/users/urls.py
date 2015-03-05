from django.conf.urls import patterns, include, url
from apps.users import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^profile/(?P<username>[^/]+)$', views.profile, name='profile'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^home/$', views.success, name='success'),
    url(r'^parapo/$', views.parapo, name='parapo'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^reports/new/$', views.create_report, name='create_report'),
)
