from django.conf.urls import url, patterns, include
from rest_framework import routers
from .viewsets import UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'staff', UserViewSet)

urlpatterns = patterns('',

        url('^', include(router.urls)),

    )