from django.conf.urls import patterns, include, url
from apps.home import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'/about/$', views.about, name='about'),
    url(r'/welcome/$', views.login, name='success'),
    # url('', include('social.apps.django_app.urls', namespace='social'))
)
