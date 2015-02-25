from django.conf.urls import patterns, include, url
from apps.home import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^error/$', views.errors, name='errors'),
    url(r'^login/$', views.login, name='login'),
)
