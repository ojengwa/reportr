from django.conf.urls import patterns, include, url
from django.contrib import admin
import resource


urlpatterns = patterns('',
    # Examples:
    url(r'', include('apps.home.urls')),
    url(r'', include('apps.users.urls', namespace='staff')),

    # Register Home Views
    # url(r'^$', include(core.urls)),

    # Register Admin Views
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'home/login.html'}, name='login'),
    url(r'', include('social_auth.urls')),

    # API routes definition
    url(r'^api/v1/auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include(resource.urls))
)